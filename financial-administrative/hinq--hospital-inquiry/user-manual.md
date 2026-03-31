---
title: DVB Version 4 User Manual (Revised 3/27/12)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: (Revised 3/27/12)
app_code: HINQ
app_name: Hospital Inquiry
section: FIN
app_status: active
pkg_ns: HINQ
patch_ver: 4
patch_id: HINQ*4
group_key: "HINQ:HINQ:4"
file_numbers: []
security_keys: []
menu_options: 0
description: Hospital Inquiry (HINQ) is a request that is sent to the VBA (Veterans Benefits Administration) from the VA Medical Center for information pertaining to a veteran. HINQ requests are sent from a VISTA computer over TCP/IP to a remote VBA computer via the Austin Automation Center (AAC) where veteran i
audience: 
keywords: 
  - hinq
  - table
  - contents
  - patient
  - suspense
  - number
  - example
  - date
  - response
  - request
page_count: 0
word_count: 13818
section_count: 76
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1992
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_62_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_62_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=41"
---

![](dvb-version-4-user-manual-revised-3-27-12/001.png)

HOSPITAL INQUIRY (HINQ)

USER MANUAL

March 1992

Office of Enterprise Development

Management, Enrollment and Financial Systems (MEFS)

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [# Introduction](#introduction)
- [Overview](#overview)
- [Scope](#scope)
- [# Using the Software](#using-the-software)
  - [Accessing the Software](#accessing-the-software)
    - [HINQ Replacement Diagram](#hinq-replacement-diagram)
- [# Functional Description](#functional-description)
  - [Suspense File](#suspense-file)
  - [Pending](#pending)
  - [New Mail](#new-mail)
  - [Error](#error)
  - [# Using the Menu Options](#using-the-menu-options)
- [HINQUP Features](#hinqup-features)
  - [Enter a Request in the HINQ Suspense File](#enter-a-request-in-the-hinq-suspense-file)
  - [Generate HINQ Requests](#generate-hinq-requests)
  - [Individual HINQ Request](#individual-hinq-request)
  - [Print Suspense File Messages](#print-suspense-file-messages)
  - [Process the HINQ Suspense File](#process-the-hinq-suspense-file)
  - [Status of HINQ By Patient](#status-of-hinq-by-patient)
  - [Utilities for Suspense File](#utilities-for-suspense-file)
  - [View the HINQ Suspense File](#view-the-hinq-suspense-file)
  - [Entering a HINQ Request](#entering-a-hinq-request)
  - [Update HINQ to the Patient File](#update-hinq-to-the-patient-file)
    - [<span class="mark">Example</span>](#span-classmarkexamplespan)
    - [Patient Safety Issue](#patient-safety-issue)
    - [Example](#example)
  - [Screen 0](#screen-0)
  - [Screen 1](#screen-1)
  - [Screen 2](#screen-2)
  - [Screen 3](#screen-3)
  - [Screen 4](#screen-4)
  - [Screen 5](#screen-5)
    - [Example](#example-1)
  - [Review Patient vs. HINQ Data](#review-patient-vs-hinq-data)
    - [Example](#example-2)
  - [HINQ Audit Trail](#hinq-audit-trail)
    - [Example](#example-3)
  - [Enter a Request in the HINQ Suspense File](#enter-a-request-in-the-hinq-suspense-file-1)
  - [As a Stand-Alone Option](#as-a-stand-alone-option)
  - [As Part of the PIMS Options](#as-part-of-the-pims-options)
    - [Example](#example-4)
  - [## Generate HINQ Requests](#generate-hinq-requests-1)
    - [Example](#example-5)
  - [## Individual HINQ Request](#individual-hinq-request-1)
    - [Examples](#examples)
    - [Example 1](#example-1)
    - [Example 2](#example-2)
  - [Print Suspense File Messages](#print-suspense-file-messages-1)
    - [Example](#example-6)
  - [Status of HINQ By Patient](#status-of-hinq-by-patient-1)
    - [Example 1](#example-1-1)
    - [Example 2](#example-2-1)
  - [Utilities for Suspense File](#utilities-for-suspense-file-1)
  - [Create a Mail Message](#create-a-mail-message)
    - [### Example](#example-7)
  - [Create a Mail Message](#create-a-mail-message-1)
  - [Delete Entry from HINQ Suspense File](#delete-entry-from-hinq-suspense-file)
    - [Example](#example-8)
  - [Edit HINQ Suspense File Parameters](#edit-hinq-suspense-file-parameters)
  - [Network Day](#network-day)
  - [Last Net-Workday](#last-net-workday)
  - [Edit HINQ Suspense File Parameters](#edit-hinq-suspense-file-parameters-1)
  - [Network Enabled](#network-enabled)
  - [Batch Processing Enabled](#batch-processing-enabled)
  - [Use High Intensity](#use-high-intensity)
  - [Use HINQ Screens](#use-hinq-screens)
    - [Example](#example-9)
  - [Select HINQ Mail Group:](#select-hinq-mail-group)
    - [Example](#example-10)
  - [Auto-Requeue of IDCU Errors](#auto-requeue-of-idcu-errors)
  - [Auto-Requeue Limit](#auto-requeue-limit)
  - [Requeue Counter](#requeue-counter)
  - [Edit HINQ Suspense File Parameters](#edit-hinq-suspense-file-parameters-2)
  - [HINQ Mail Messages](#hinq-mail-messages)
  - [New IDCU Interface:](#new-idcu-interface)
    - [Example](#example-11)
  - [RDPC Time Difference](#rdpc-time-difference)
  - [RDPC IP Address](#rdpc-ip-address)
    - [Example](#example-12)
  - [## Ask Medical Center Division](#ask-medical-center-division)
  - [IDCU Address](#idcu-address)
  - [IDCU Username-Password](#idcu-username-password)
  - [HINQ Device Name](#hinq-device-name)
  - [Batch Device Name](#batch-device-name)
  - [Institution/Station Number](#institutionstation-number)
  - [Edit HINQ Suspense File Parameters](#edit-hinq-suspense-file-parameters-3)
    - [Example](#example-13)
  - [Network Enable/Disable](#network-enabledisable)
  - [Disable HINQ Network](#disable-hinq-network)
  - [Enable HINQ Network](#enable-hinq-network)
    - [Example](#example-14)
  - [Purge Suspense File (Retain 30 Days)](#purge-suspense-file-retain-30-days)
    - [Example](#example-15)
  - [Recompile HINQ Templates](#recompile-hinq-templates)
    - [Example](#example-16)
  - [## Recompile HINQ Templates](#recompile-hinq-templates-1)
  - [Select View Suspense File](#select-view-suspense-file)
    - [Example](#example-17)
  - [View the HINQ Suspense File](#view-the-hinq-suspense-file-1)
- [# HINQ Response](#hinq-response)
  - [Summary](#summary)
  - [HINQ Response Data Items](#hinq-response-data-items)
  - [HINQ Error Messages](#hinq-error-messages)
- [# Performance Requirements](#performance-requirements)
  - [VBA Common Security Services (CSS)](#vba-common-security-services-css)
    - [All users are required to have a VBA BDN Password, a HINQ employee number and a VistA HINQ security key](#all-users-are-required-to-have-a-vba-bdn-password-a-hinq-employee-number-and-a-vista-hinq-security-key)
    - [A user is required to access HINQ at least once very 90 days to avoid the system locking them out](#a-user-is-required-to-access-hinq-at-least-once-very-90-days-to-avoid-the-system-locking-them-out)
    - [If a user has not accessed their HINQ account after 90 days an error code message will appear denying the user access to the system](#if-a-user-has-not-accessed-their-hinq-account-after-90-days-an-error-code-message-will-appear-denying-the-user-access-to-the-system)
    - [If a user is denied access the user is required to contact the VBA ISO coordinator](#if-a-user-is-denied-access-the-user-is-required-to-contact-the-vba-iso-coordinator)
    - [All users are responsible for following-up with their VBA ISO coordinator in expediting all access requests](#all-users-are-responsible-for-following-up-with-their-vba-iso-coordinator-in-expediting-all-access-requests)
    - [All new employees are required to complete a VAF 20-8824e form to gain access to the HINQ system](#all-new-employees-are-required-to-complete-a-vaf-20-8824e-form-to-gain-access-to-the-hinq-system)
  - [User Response Time](#user-response-time)
  - [## VBA Unsolicited Eligibility Update to HEC (VBA Push)](#vba-unsolicited-eligibility-update-to-hec-vba-push)
  - [Latency](#latency)
  - [Packet Sizing](#packet-sizing)
- [# Glossary](#glossary)
- [# Index](#index)
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 28%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision Description</th>
<th>Project Manager (added 8/30/06)</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>03/1992</td>
<td>Initial Release</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/31/05</td>
<td>Revised the HINQ manual according to team feedback</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/31/05</td>
<td>Updated Introduction section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/31/05</td>
<td>Added Using the Software section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/31/05</td>
<td>Updated references to Screen 0 to HINQ Patient File section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/31/05</td>
<td>Updated references to Screen 1 to HINQ Patient File section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/31/05</td>
<td>Updated references to Screen 2 to HINQ Patient File section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/31/05</td>
<td>Updated references to Screen 3 to HINQ Patient File section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/01/05</td>
<td>Updated references to Screen 5 to HINQ Patient File section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/01/05</td>
<td>Delete Screen 6 to HINQ Patient File section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/01/05</td>
<td>Updated references to Generate a HINQ request section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/01/05</td>
<td>Updated references to Individual HINQ request</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/01/05</td>
<td>Updated Screen 1 to Individual HINQ request</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/03/05</td>
<td>Updated example screen to Print Suspense File Message</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/03/05</td>
<td>Updated Process the HINQ Suspense File</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/07/05</td>
<td>Updates based on review/feedback</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/07/05</td>
<td>Updated the HINQ Suspense File screen</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/07/05</td>
<td>Added new data field value to Status of HINQ by Patient</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/08/05</td>
<td>Updates based on review/feedback</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/08/05</td>
<td>Added new menu option, Use HINQ Screens Field</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/08/05</td>
<td>Added new menu option, Select HINQ Mail Group</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/09/05</td>
<td>Updates based on review/feedback</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/09/05</td>
<td>Updated Edit HINQ Suspense File Parameter</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/09/05</td>
<td>Updated references to Network Enable/Disable fields</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/09/05</td>
<td>Revised data fields in Recompile HINQ template</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/09/05</td>
<td>Updated references to HINQ Response summary</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/10/05</td>
<td>Updated data fields to HINQ Response data items</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/10/05</td>
<td>Updated Screen to Successful HINQ response</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/10/05</td>
<td>Updated Screen to Create a Mail Message</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/10/05</td>
<td>Updated Screen example 2 to Successful HINQ response</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/10/05</td>
<td>Updated reference fields to HINQ Error Messages</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/10/05</td>
<td>Added Performance Requirements section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/10/05</td>
<td>Added VBA Common Security Services (CSS) section</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/15/05</td>
<td>Added Related Manual information</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/15/05</td>
<td>Added Glossary</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/15/05</td>
<td>Added Revision History</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/15/05</td>
<td>Added Index</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/23/05</td>
<td>Entering a HINQ Request</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/27/05</td>
<td>Added HINQ User response time</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>07/27/05</td>
<td>Added HEC Changes to new VBA data</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/04/05</td>
<td>Added HINQ Replacement Diagram</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/04/05</td>
<td>Added HEC through MVR Query Diagram</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/04/05</td>
<td>Added User Interface</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/04/05</td>
<td>Added Latency</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/04/05</td>
<td>Added Packet Sizing</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/04/05</td>
<td>Added VBA Push</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/21/06</td>
<td>Added Patitent Safety Issue ~Patch DVB*4*56</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/30/06</td>
<td>DVB*4*56 - Revised Update HINQ to the Patient File section</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>03/24/11</td>
<td>DVB*4*65 – display VBA Pension and Dental treatment data</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/25/11</td>
<td>DVB*4*65 – TW Review</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>5/10/11</td>
<td><p>DVB*4*65 – Updated Mail Message screen per PS review.</p>
<p>TW Review</p></td>
<td>REDACTED</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>9/9/11</td>
<td>DVB*4*62 – Updated section Update HINQ to the Patient File – MSEs will not upload if authoritative MSEs have been received from ESR.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/5/11</td>
<td>DVB*4*62 – TW Review</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/14/12</td>
<td><p>DVB*4*62 – Added sample screen when MSEs will not upload if authoritative MSEs have been received from ESR.</p>
<p>Updated footer date to April 2012.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/27/12</td>
<td>DVB*4*62 – Changed footers from April to March</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hospital Inquiry (HINQ) is a request that is sent to the VBA (Veterans Benefits Administration) from the VA Medical Center for information pertaining to a veteran. HINQ requests are sent from a V*IST*A computer over TCP/IP to a remote VBA computer via the Austin Automation Center (AAC) where veteran information is stored. Requests are processed by the VBA computer and returned via to the AAC and then to the V*IST*A computer.

HINQ requests can only be directly sent to the VBA computer by users who are holders of the HINQ security key, DVBHINQ, and who have received a HINQ password. Other users may make HINQ requests but these are placed into a file (called the HINQ Suspense file) to be sent by a user with the required security to the VBA computer at a later time

The main features of the HINQ package include the following functionality.

- Requests may be sent individually, when necessary, or numerous requests may be forwarded in batch mode
- Status of Suspense file entries is automatically updated by the system to indicate the current status of the request
- Expanded informational response is obtained
- Provides the capability to update returned HINQ data directly into the PATIENT file

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide instructions for using the menus and options that are available to the HINQ users.

# # Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accessing the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HINQ requests can only be directly sent to the VBA computer by users who have a HINQ password. A HINQ employee number must be entered into the NEW PERSON file for each user who has a HINQ password. This number was distributed by your facility supporting VBA Regional Office ISO staff and entered into the file by a site manager. When a HINQ request is made, this number is sent as part of the HINQ request which will automatically identify the user to VBA. Whenever a user selects options that require a HINQ password, the application will automatically check the password for verification. If there is no password or if the password is not validated or confirmed an error message is generated in place of the VBA response.

### HINQ Replacement Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](dvb-version-4-user-manual-revised-3-27-12/002.png)

# # Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HINQ Suspense file serves two major functions. As its name suggests, HINQ requests can be placed in this file to be processed at a later date. These requests are entered into the file with a status of PENDING. Selected options allow holders of the HINQ security key to release these requests for transmission to the VBA computer. The file, which also serves as a log, updates the status of each Suspense file entry with NEW, ABBREVIATED, or ERROR, depending upon the nature of the response from VBA. This provides the medical center with a log of HINQ activity for HINQs not entered directly...

Status of Suspense file entries is updated automatically by the system to indicate the current status of the request.

## Pending

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a request is placed into the Suspense file for later transmission, the entry is given the status of PENDING. The Suspense file should be used to store requests for batch transmission or when it is not possible to send the request directly to the VBA computer as in the following cases.

- The user does not have the required security - HINQ key and password.
- The network communication system is not functioning.

When these conditions are detected by the HINQ software, the requests are automatically directed to the Suspense file.

## New Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in the Suspense file with the status of PENDING are updated to the NEW MAIL status whenever a request has been processed without any errors by the VBA computer, and when a response has been returned to the HINQ mail group.

## Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in the Suspense file with the status of PENDING are updated to the ERROR status when an error has occurred in the processing of this HINQ request at the VBA computer. For example, the HINQ password was missing or invalid.

## # Using the Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# HINQUP Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options contained in this menu are for updating features. These options are only available to holders of the DVBHINQ and DG ELIGIBILITY security keys.

## Enter a Request in the HINQ Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to enter requests for inquiries into the HINQ Suspense file.

## Generate HINQ Requests 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is only available to holders of the HINQ security key, DVBHINQ. When requests for HINQ inquiries are entered through this option, PENDING entries in the Suspense file are transmitted to the VBA computer.

## Individual HINQ Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is only available to holders of the HINQ security key, DVBHINQ, and is used to immediately transmit requests for HINQ requests to the VBA computer. This option does not create Pending Suspense file entries.

## Print Suspense File Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used to print a listing of those patients currently in the Suspense file with a HINQ response message. You may choose to print by patient, requestor or date/time. This option is only available to holders of the HINQ security key, DVBHINQ

## Process the HINQ Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is only available to holders of the HINQ security key, DVBHINQ. It is used to release PENDING requests in the Suspense file to the VBA computer.

## Status of HINQ By Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option gives information about entries in the Suspense file including the HINQ response message if one has been received. This option is only available to holders of the HINQ security key, DVBHINQ

## Utilities for Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The options contained in this menu are used to perform the following HINQ utility functions such as: purge entries in the HINQ Suspense file, delete an entry from the HINQ Suspense file, edit HINQ parameters, and recompile HINQ templates.

## View the HINQ Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option displays the entries in the Suspense file on the screen.

## Entering a HINQ Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To search for a HINQ the user should enter the identifying number. The Identifying Number is one of the following three numbers, which are listed in the order of preference.

- Claim Number
- SSN
- Service Number

## Update HINQ to the Patient File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Update HINQ to the Patient File option is used to enter returned HINQ data directly into the PATIENT file. You may choose to update the data for a single patient or all patients in the Suspense file who have successfully processed HINQs. If all is selected, only those files which have not already been updated or reviewed will be displayed. While updating HINQs to the PATIENT file, the user can enter a caret (^) to exit the HINQ Update option without waiting for all of the updates to process. If the patient option is selected the user must select a patient, whose record may or may not have already been updated.

The data is arranged so that it can be viewed and updated through various screens. If the USE HIGH INTENSITY parameter at your facility is set to YES, boldface and flashing type will appear on portions of the HINQ screens. Each piece of information is labeled with a number to the left of the data item. Numbers enclosed by brackets \[ \] may be updated while those enclosed by arrows \< \> may not. A question mark \<?\> entered at the prompt which appears at the bottom of each screen (other than Screen 0) will provide you with a HELP SCREEN. This screen describes the use of the \<RET\> and up-arrow \<^\> keys, the way to select one, many or all items to update and the "screen jumping" capability.

The screens display both the data in the HINQ message and what is currently in the PATIENT file for comparison. You may choose to update one, several, or all data items. The second and third screens will automatically update the selected items selected. The first, fourth, and fifth screens list the selected individual data items for manual editing. <span class="mark">If authoritative military service data has been received from ESR, the filing of military service episodes from the HINQ Suspense file will be blocked and a message will be displayed to the user.</span> After the updates have been entered on a screen, it is then redisplayed containing the updated data.

### <span class="mark">Example</span> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REGPATIENT,ONE         Patient File ((4))         HINQ Response      SSN: 6789</span>

<span class="mark">------------------------------------------------------------------------------</span>

<span class="mark">                                                                                                                                                            </span>

<span class="mark">                                                                         </span>

<span class="mark">                                                                             </span>

<span class="mark">     HINQ Data</span>

<span class="mark">     EOD         RAD       Bran. Ser.       Char. Ser.               Ser. Num.</span>

<span class="mark">------------------------------------------------------------------------------</span>

<span class="mark">JAN 15,1963                                                                  </span>

<span class="mark"> JAN 15,1973  JAN 12,1975  Navy             Honorable                        </span>

<span class="mark">                                                                              </span>

<span class="mark">                                  Patient File</span>

<span class="mark">------------------------------------------------------------------------------</span>

<span class="mark">\<1\> Last episode</span>

<span class="mark">Jan 15, 1973  Jan 12, 1975       NAVY          HONORABLE     123456789</span>

<span class="mark">(4) Per. of Ser.: VIETNAM ERA</span>

<span class="mark">\<RET\> to CONTINUE, '^' to QUIT, N  N-N  N,N,N,N  or (A)-ALL to update: 1</span>

<span class="mark">                 Authoritative data, can't edit   \<RET\></span>

### Patient Safety Issue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient lookup algorithms at the VBA have been changed in response to Patient Safety Issue PSI-05-120, which states that a HINQ request could return data belonging to a patient other than the user-selected patient (e.g., when a claim number for one veteran matches another veteran's SSN or Service Number). When the patient data in the HINQ response differs from the patient data in the local VistA database for any of the following identifier fields, the user receives a warning and the discrepant data displays:

- Name
- Date of Birth
- Sex
- SSN

Following the data display, the user is cautioned to review the data before proceeding with any of the following actions:

1\. Update this record.

2\. Take no action at this time.

3\. Delete this record from the SUSPENSE file.

The user can select which of the available actions to take by responding to the “Do you want to process the HINQ on TESTPATIENT,PATIENT NAME? : (1-3): 2//” prompt. The default response is “Take no action at this time.” The user can enter a caret (^) at this prompt to exit the HINQ Update option.

### Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* NOTE: IDENTIFYING DATA FROM HINQ AND VISTA DOES NOT MATCH \*

\* PATIENT FROM HINQ RESPONSE MAY NOT BE THE PATIENT REQUESTED \* \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<u>Patient File data HINQ Data</u>

Name: TESTPATIENT,PATIENT NAME PATIENT T TESTPATIENT

Sex: FEMALE

Date of Birth: 06/17/1901 <u>06/17/1901</u>

<u>SSN: 000000000 000000000</u>

Check displayed data before proceeding.

Choose one of the following:

1\. Update this record.

2\. Take no action at this time.

3\. Delete this record from the SUSPENSE file.

Do you want to process the HINQ on TESTPATIENT,PATIENT NAME? : (1-3): 2//

## Screen 0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a verification screen only. It should be used to assure that the HINQ response and PATIENT file data you are comparing are for the same veteran. The patient's name, address, social security number, claim number, patient type, eligibility code, type of response and whether or not updating has previously occurred are some of the items displayed on this screen. If the veteran's monetary benefits have been terminated, the user is automatically notified by this screen. If the selected patient has died, the following message will appear.

"\*\*VBA indicates Patient is deceased. {Date}\*\*"

## Screen 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen contains the veteran's address information. Display lines are listed for the user to add the following information: street address, city, state, zip code, and county.

## Screen 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen contains the following data items: claim number, date of birth, sex, date of death, incompetency rating, POW status, claims folder location, and unemployable status. If the date of birth returned in the HINQ message does not contain a day, updating of the date of birth will not be allowed. If your system is not running MAS v. 5.2 or greater, uploading of the UNEMPLOYABLE field will not be allowed at this field located in your PATIENT file. The DATE OF BIRTH and SEX fields cannot be edited from this screen.

## Screen 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Screen 3 contains informational service data and disability items such as active duty training indicator, total active service, and permanent and total status. Editable items include Vietnam service, date service data was verified and rated disabilities. Beginning with this version of HINQ, only service connected disabilities will be included in the VBA response. Also, if the veteran has had a rating evaluation by VBA since 2002, then the disability data will come from VBAs Corporate database, which is not limited to six disabilities the way the C&P system is.

If a VBA HINQ response has been received containing service-connected disabilities and you select the rated disabilities for updating, the system will check the following four data items on Screen 0: patient type, veteran status, service-connected status and eligibility code. If any of these items are not consistent with a service-connected rating, the following message will appear.

"HINQ contains SC disabilities, Patient is NSC no updating allowed. Check patient's SERVICE CONNECTION, ELIGIBILITY CODE, VET STATUS, or PATIENT TYPE. Screen 5 contains this."

## Screen 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen contains the data elements connected with a period of service. This would include the following information: entry date, discharge date, branch of service, character of discharge and service number. Up to three periods of service can be displayed - last episode, next-to-last (NTL) episode, and next-next-to-last (NNTL) episode. Up-arrowing \<^\> is not allowed when editing the data elements contained on this screen. You will be unable to select NNTL episode for updating if no NTL episode of service exists

## Screen 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen displays informational eligibility information such as: type of benefit, net award amount, check amount, Income for VA Purposes and aid and attendance status. Data items that may be entered/edited include eligibility status, patient type, verification method, eligibility code and the type and amount received for such benefits as Aid and Attendance, Housebound and VA pension. Up-arrowing (^) is not allowed when editing the data elements contained on this screen. Income for VA Purposes is a new data field and represents the total income that a veteran receives when determining eligibility for pension benefits

With the storage of the returning HINQ information, a check sum has been developed to insure the integrity of the stored data. If the HINQ information in the Suspense file has been adjusted since the last HINQ for the selected patient(s), the following warning message will appear and you will be unable to continue.

"HINQ data does NOT seem right

Re-HINQ and/or Notify system manager.

HINQ check sum failure for {patient name}"

Both the DVBHINQ and DG ELIGIBILITY security keys are required to access the Update HINQs to the Patient file option.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do you want to examine the Suspense file by 'P'atient or 'A'll P// <u>P</u>

Select Patient from "HINQ Suspense file": <u>HINQPATIENT,ONE</u> 08-01-06 123456789

SC VETERAN NOT UPDATED

\*\*\*\*\*\* HINQ Upload/edit \*\*\*\*\*\*\<\<0\>\>

Verification screen only

Patient file VBANOT UPDATED HINQ Response

-----------------------------------------------------------------------------

Name: <u>HINQPATIENT,ONE</u> <u>HINQPATIENT,ONE</u>

Sex: MALE MALE

SSN: 00000000 00000000 Verified VBA

Claim \#: 0000000

Address: 123 Anywhere Street

Pat. Type: SC VETERAN Elig. Stat.:Vet. Y/N: YES Stat. Date:Ser. Con.: YES Verif. Meth.:Ser. Con. %: 50 Disab. Ind.:Elig. code: SERVICE CONNECTED 50% to 100%

Is this the patient to be updated (YES, NO, IGNORE)? YES// <u>\<RET\></u> (YES)

  
TESTA,PATIENT Patient File ((1)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

\[1\] Address: 123 Anywhere Street HINQPATIENT,ONE

123 Anywhere ST

Mytown MS

City: Mytown

State: Mystate

Zip: 99999

County: Mycounty

\<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: \<RET\>

<u>HINQPATIENT,ONE</u> Patient File ((2)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

\[1\] Claim Num. : 0000000

\<2\> Date of Birth: 08/01/1906 AUG 31,1906

\<3\> Sex: MALE MALE

\[4\] Date of Death:

\[5\] Rated Incomp.: Competent, or not an issue

\[6\] POW: Not applicable

\[7\] Folder Loc. : 306

\[8\] Unemployable: Employable

\<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: <u>A</u>

<u>HINQPATIENT,ONE</u> Patient File ((2)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

\[1\] Claim Num. : 0000000 0000000

\[2\] Date of Birth: 08/31/1906 AUG 31,1906

\[3\] Sex: MALE MALE

\[4\] Date of Death:

\[5\] Rated Incomp.: NO Competent, or not an issue

\[6\] POW: NO Not applicable

\[7\] Folder Loc. : 306 306

\[8\] Unemployable: NO Employable

\<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: <u>\<RET\></u>

<u>HINQPATIENT,ONE</u> Patient File ((3)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

Comb. % Disab.: Act. Duty Training:

Total Act. Ser.: Perm. & Tot.:

\[1\] Ver. SVC data: YES

\[2\] Vietnam Ser.:

\<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: <u>A</u>

Verify SC at folder location: 306

No updating allowed.  
<u>HINQPATIENT,ONE</u> Patient File ((3)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

Comb. % Disab.: Act. Duty Training:

Total Act. Ser.: Perm. & Tot.:

\[1\] Ver. SVC data: OCT 27,1902 YES

\[2\] Vietnam Ser.:

\<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: <u>\<RET\></u>

<u>HINQPATIENT,ONE</u> Patient File ((4)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

HINQ Data

EOD RAD Bran. Ser. Char. Ser. Ser. Num.

------------------------------------------------------------------------------

SEP 18,1897 NOV 21,1899 NAVY Honorable 8007926

Patient File

------------------------------------------------------------------------------

(1) Last episode

(2) NTL episode

(3) NNTL episode

(4) Per. of Ser.: WORLD WAR II

\<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: <u>1</u>

<u>HINQPATIENT,ONE</u> Patient File ((4)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

HINQ Data

EOD RAD Bran. Ser. Char. Ser. Ser. Num.

------------------------------------------------------------------------------

SEP 18,1897 NOV 21,1899 NAVY HON 8007926

------------------------------------------------------------------------------

\[LAST\]

L-EOD: <u>9 18 43</u> (SEP 18, 1897)

L-RAD: <u>11 21 45</u> (NOV 21, 1899)

L-Bran.. Ser.: <u>NAVY</u>

L-Char. Ser.: <u>HONORABLE</u>

L-Ser. Num.: <u>8007926</u>

<u>  
HINQPATIENT,ONE</u> Patient File ((4)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

HINQ Data

EOD RAD Bran. Ser. Char. Ser. Ser. Num.

------------------------------------------------------------------------------

SEP 18,1897 NOV 21,1899 NAVY HONORABLE 8007926

Patient File

------------------------------------------------------------------------------

(1) Last episode

SEP 18,1897 NOV 21,1899 NAVY HONORABLE 8007926

(2) NTL episode

(3) NNTL episode

(4) Per. of Ser.: WORLD WAR II

\<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: <u>\<RET\></u>

<u>HINQPATIENT,ONE</u> Patient File ((5)) HINQ Response SSN: 6789

------------------------------------------------------------------------------

Check Amt.: \$600.00 Combined %: Net Award Amt.:

Benefit Type: Income for VA Purposes:

Aid & Attendance:

--- Patient Data ---(1) Elig. Stat.: VERIFIED Elig. Stat. ent. by: USER, TEST

Stat. date: OCT 27,1902 Monetary Ben. Verif:

Verif. Meth.: BIRLS Patient Elig.:

(2) Pat. Type: SC VETERAN Vet. (Y/N)?: YES

Ser. Con.: YES

(3) A&A: Amt.: \$ VA Pension: Amt.: \$

House Bound: Amt.: \$ VA Disability: Amt.: \$

\<RET\> to CONTINUE, '^' to QUIT, N N-N N,N,N,N or (A)-ALL to update: <u>\<RET\></u>

Would you like a HINQ message printed out? NO// <u>\<RET\></u> (NO)

Checking data for consistency...

===\> No inconsistencies found in 0 seconds...

Select Patient from "HINQ Suspense file": <u>\<RET\></u>

## Review Patient vs. HINQ Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Review Patient vs. HINQ data option is used to compare the data in the PATIENT file to the data in the returned HINQ response. This can be done before or after the record has been updated by the HINQ update option. You may select a single patient for comparison or all the applicable patients currently in the Suspense file. If all is selected, you may further specify to print only updated entries, or non-updated entries or both. The system will then notify you of the number of patients that are contained in the selected report. For reports that contain more than one patient, data will automatically be printed on a separate page.

The output produced is a comparison of the data in the PATIENT file to that in the HINQ response. All of the entries that are contained on the screens of the Update HINQs to the Patient file option will appear in the output except all of screen 5. This option is for comparison only, and editing or updating is not allowed. In order to access this option the user must have a DVBHINQ security key.

With the storage of the returning HINQ information, a check sum has been developed to insure the integrity of the stored data. If the HINQ information in the Suspense file has been adjusted to the last HINQ for the selected patient(s), the following warning message will appear and prohibit the user to continue.

"HINQ data does NOT seem right

RE-HINQ and/or Notify system manager

HINQ check sum failure for {patient name}"

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do you want a print out of a (S)ingle patient or (A)ll of the patients? S// <u>\<RET\></u>

Select Patient from "HINQ Suspense file": <u>HINQPATIENT,TWO</u> 08-20-06

000000000 SC VETERAN NOT UPDATED

DEVICE: HOME// <u>HALLWAY PRINTER</u> RIGHT MARGIN: 80// <u>\<RET\></u>

DO YOU WANT YOUR OUTPUT QUEUED? NO// <u>\<RET\></u> (NO)

Patient File vs. HINQ

Patient HINQ

-----------------------------------------------------------------------------

Name: <u>HINQPATIENT,TWO</u> HINQPATIENT,TWO

Address: 123 ANYWHERE STREET

SSN: 000000000 000000000

Claim number: 0000000 0000000

Date of Birth: AUG 20,1906 AUG 20,1906

Date of Death:

Rated Incompetent: NO

POW NO Not applicable

Amount SS:

Folder Location: 306

Verified SVC: YES

Vietnam Service:

Rated Disab. (Patient file) POSTOPERATIVE STOMACH INJURY 60 NO

Rated Disab. (HINQ): POSTOPERATIVE STOMACH INJURY 60 NO

HINQ Data

EOD RAD Bran. Ser. Char. Ser. Ser Num.

-----------------------------------------------------------------------------

SEP 18,1897 NOV 21,1899 NAVY HON 8007985

Patient File

-----------------------------------------------------------------------------

Last episode

SEP 18,1897 NOV 21,1899 NAVY HONORABLE 8007985

NTL episode

NNTL episode

## HINQ Audit Trail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HINQ Audit trail option is used to produce a listing of the patient records that have been changed by the Update HINQs to the Patient file option. The output can be sorted by using two methods.

- By a patient, user who updated the record,
- The date/time the record was last updated.

The date and time the report was generated will appear at the top of each page along with the page number.

After selecting from the following options (patient, user, date/time), the user is then asked to select advice.

> **NOTE:** Only holders with a security key DVBHINQ can access this option.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select one of the following:

1 Patient

2 User

3 Date/Time

By which would you like the sort to begin?: Patient// <u>\<RET\></u>

DEVICE: <u>\<RET\></u> RIGHT MARGIN: 80// <u>\<RET\></u>

HINQ Audit List by Patient OCT 31,1902 10:02 PAGE 1

PATIENT DATE/TIME USER NAME

DATE/TIME ALERT ALERT USER ALERT

------------------------------------------------------------------

<u>HINQPATIENT,THREE</u> OCT 26,1902 11:44 USERA,TEST

AUG 31,1904 15:58 HINQ,USER ACKNOWLEDGE

------------------------------------------------------------------------------

<u>HINQPATIENT,FOUR</u> OCT 26,1902 11:49 USERA,TEST

------------------------------------------------------------------------------

<u>HINQPATIENT,FIVE</u> OCT 27,1902 09:23 USERB,TEST

JUL 14,1904 10:16 HINQ,USER ACKNOWLEDGE

------------------------------------------------------------------------------

The following are examples of the other two sorts.

HINQ Audit List by USER NAME OCT 31,1902 10:02 PAGE 1

USER NAME DATE/TIME PATIENT

------------------------------------------------------------------

USERA,TEST OCT 26,1902 11:44 HINQPATIENT,THREE

USERA,TEST OCT 26,1902 11:49 HINQPATIENT,FOUR

USERB,TEST OCT 27,1902 09:23 HINQPATIENT,FIVE

HINQ Audit List by Date/Time OCT 31,1902 10:03 PAGE 1

DATE/TIME USER NAME PATIENT

------------------------------------------------------------------

OCT 27,1902 09:23 USERB,TEST HINQPATIENT,FIVE

OCT 26,1902 11:49 USERA,TEST HINQPATIENT,FOUR

OCT 26,1902 11:44 USERA,TEST HINQPATIENT,THREE

## Enter a Request in the HINQ Suspense File 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Requests for HINQ inquiries can be entered into the HINQ Suspense file through this option. These requests are given the status of PENDING. They are released for transmission to the VBA computer through another option

This option can also be activated in select Registration and MCCR options of the PIMS package. The flow of this routine differs slightly depending on if the user is going through this routine as a stand-alone option or as part of the PIMS options.

## As a Stand-Alone Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a patient is selected, the routine checks the patient's eligibility status in the station's main PATIENT file. If the patient's eligibility has not been verified, an entry is made in the Suspense file and given the status PENDING. If the patient's eligibility has been verified, it is then indicated on the screen, and the request is entered in the Suspense file with a status of PENDING.

At multi-divisional sites, the ASK MEDICAL CENTER DIVISION parameter can be set to YES. If this occurs, the division (with a default of the main division) is requested after the patient is selected. The division name is stored in the Suspense file entry for the veteran and displayed on the first line of the response.

## As Part of the PIMS Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine can be performed during select Registration and MCCR options when the MAS HINQ parameter is set to YES.

If a HINQ is requested by a user, an entry is created in the Suspense file for the patient and given a PENDING status.

Entries in the Suspense file include the name of the requestor, and the time of the request. The Suspense file also stores the Suspense file status of each entry, and date/time that the status was last updated. When the Suspense file is processed, only the patient's name and social security number are sent to the VBA computer.

When this option is used as a stand-alone option, only patients who are already in the main PATIENT file are selected. A new patient may not be entered into the PATIENT file.

When a request is made for a patient who is already in the Suspense file, the system will add the name of the new requestor(s) and the date/time of request(s) to the existing entry. However, if the same user places more than one request in the Suspense file for the same patient, only the most recent date/time of request will be stored with the user’s name.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following examples demonstrate what might appear on the screen while entering a HINQ Request into the HINQ Suspense file. The ‘Select Medical Center Division’ prompt will only appear if you are at a multi-divisional facility, and the site selectable parameter has been set to YES.

<span id="_Toc319501203" class="anchor"></span>Example 1

This example shows a HINQ request being entered into the HINQ Suspense file through this option as a stand-alone option.

Select Medical Center Division: VAMCNAME MC// <u>VAMCNAME DOM</u>

Select PATIENT NAME: <u>HINQPATIENT,SIX</u> 01-01-02 000000000 SC Veteran

in HINQ suspense file

Select PATIENT NAME: <u>\<RET\></u>

<span id="_Toc319501204" class="anchor"></span>Example 2

This example shows a HINQ request being entered into the Suspense file in the same manner as in Example 1 above. This patient's eligibility has previously been verified.

Select Medical Center Division: VAMCNAME MC// <u>\<RET\></u>

Select PATIENT NAME: <u>HINQPATIENT,SEVEN</u> 10-20-03 000000000 SC VETERAN

Verified in HINQ suspense file

Select PATIENT NAME: <u>\<RET\></u>

<span id="_Toc319501205" class="anchor"></span>Example 3

This example shows a request for an entry in the Suspense file during patient registration.

Select PATIENT NAME: <u>HINQPATIENT,EIGHT</u> 07-10-03 000000000 SC VETERAN

.

.

.

Do you wish to request a HINQ inquiry? NO// <u>Y</u> in HINQ suspense file

.

.

.

## ## Generate HINQ Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generate HINQ Requests allows users that have a required security key (DVBHINQ), and a password to enter HINQ requests. These requests are sent immediately to the VBA computer.

When requests are entered through this option, the system checks the Suspense file for entries with the PENDING status. All entries with the PENDING status are sent to the VBA computer. Only the patient's name and social security number are sent, even if the claim number, and service number are known. If a match is not found, and you know the claim number, use the direct input method of the Individual HINQ Request option.

This option will abort on the first request if the password is invalid. The Suspense file will show the first entry with an ERROR status, while the status of the other transaction remains as PENDING.

Utilizing this option generates a mail bulletin that is sent to all members of the DVBHINQ mail group. The message informs the recipients that the Suspense file was completed, and provides the user with the total number of HINQ requests.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For security purpose only, the entry of the HINQ password is not displayed on this screen. The "Select Medical Center Division" prompt will only appear if you are at a multi-divisional facility and the site selectable parameter has been set to YES.

Select patients, enter your Password and HINQ requests will be sent

Select Medical Center Division: BRONX OPC// <u>\<RET\></u>

Select PATIENT NAME: <u>HINQPATIENT,NINE</u> 02-16-03 000000000 SC VETERAN

Select PATIENT NAME: <u>HINQPATIENT,TEN</u> 07-01-04 000000000 SC VETERAN

Select PATIENT NAME: <u>HINQPATIENT,ELEVEN</u> 09-30-06 000000000 NSC VETERAN

Select PATIENT NAME: <u>\<RET\></u>

Enter HINQ PASSWORD: \_\_\_\_\_\_\_ Direct Requests Queued \#111111111

> **NOTE:** 1\) A mail message is generated when a VBA response is received. This is identical to the mail message received after making an Individual HINQ request.

2\) When the user selects this option, the User Number field in the NEW PERSON file is checked to verify if a HINQ employee number exists. In the event it does not exist, this option is disabled. The following message will appear.

> "HINQ Employee Number not in New Person file

> Notify System Manager"

3\) If the HINQ parameter is set to allow disabling the transmission of HINQ requests, the following message is displayed and the user is returned back to the menu.

> "Network is disabled

> Requests may be entered in the Suspense File"

## ## Individual HINQ Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Individual HINQ Request option allows requests to be immediately transmitted to the VBA computer. This option is activated for users who hold the HINQ security key, DVBHINQ, and a HINQ password.

This option will create a Suspense file entry if an individual request by PATIENT is selected and the request is not already in the Suspense file. The status and time of status update for existing entries in the Suspense file will be changed by this option.

The Individual HINQ Request option is the only HINQ option that supports inquiries for applicants not currently in the PATIENT file. A Direct inquiry prompts for social security number, claim number or service number. This request will not enter the patient into the PATIENT file. At the same time, this option also allows requests on patients in the PATIENT file. A Patient inquiry prompts for a patient name and all the necessary data to make the inquiry it is then taken from the PATIENT file.

For Patient inquiry, the response to a HINQ request transmitted thru this option appears as new mail in the IN basket of all members of the DVBHINQ mail group at the requesting station as well as the original requestor and requestors in the HINQ Suspense file with the DVBHINQ security key. For Direct inquiry, the MailMan message goes only to the requestor.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note that for security reasons, whenever a password is entered, it is not displayed.

### Example 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This example shows a HINQ request being made for a patient who is in the station's PATIENT file.

This option will take 30 seconds to activate – using IP Addressing

Do you wish to continue? YES// <u>\<RET\></u> (YES)

Connecting to VBA database. . .

Select Input: Patient File, or Direct P// <u>\<RET\></u>

Select PATIENT NAME: <u>H6789</u> HINQPATIENT,TWELVE 10-10-04 000000000 SC VETERAN

Enter HINQ PASSWORD:

Request being processed ..

Response received and mailed

### Example 2 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This example shows a HINQ request being made for a patient who may not be in the station's PATIENT file.

This option will take 30 seconds to activate

Do you wish to continue? YES// <u>\<RET\></u> (YES)

Connecting to VBA database . . .

Select Input: Patient File, or Direct P// <u>D</u>

Enter one of the following numbers: Claim Number

Social Security Number, or Service Number.

1\. Claim Number

2\. Social Security Number

3\. Service Number

CHOICE: 1// 2

Social Security: 123456789

OK ? Yes// (Yes)

Enter HINQ PASSWORD:

Response received and mailed

VBA name = HINQPATIENT,ONE

Prior names =

HINQPATIENT,ONE HSee

Name = HINQPATIENT,ONE

Address = 101 TEST

Address = CITYNAME WI

ZIP = 99999

Sex = MALE

Date of Birth = JAN 01, 1960

Date of Death = FEB 08, 2005

VBA SSN = 0000000000

Claim Number = 00000000

Service Number = 000000000

Folder Location = 381 - AIR FORCE

Power of Attorney = The American Legion - 74

POW = Not applicable

INDICATORS( Active Duty Training NO Homeless Veteran NO )

Service data - VBA

--------------------------------------------------------------

Branch of Service = Army

EOD = JAN 1,1901

RAD = JAN 1,1905

Char of Service = Honorable

Type of Benefit = Pension

Pension Award Eff Date = APR 01, 1920 Reason code = 00

DISABILITIES

Combined %=0 Disab. in Record=0 Eff. Date of Comb. Eval.=

AID & ATTEND = A&A Paid

Competency indicator = Competent, or not an issue

Vet married Vet = No spouse or not eligible

Check Amount= '\$770.00' Net Award= '\$807.00'

*  
> **NOTE:** *

1\) Whenever the HINQ parameter is set to the disable option, the following message will appear and the user is automatically returned back to the menu.

> "Network is disabled

> Requests may be entered in the Suspense File"

2\) In the event a VBA connection cannot be established, the following message will automatically appear:

> Device is busy

> Enter requests in the Suspense file

3\) When the User Number field option is selected, it will automatically verify if an HINQ employee number exists. If the employee number is not recognized or it does not exist then this option will automatically disable the USER NUMBER field, and the following message will appear.

> "HINQ Employee Number not in New Person file

> Notify System Manager"

## Print Suspense File Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Suspense File Messages option is used to print a listing of those patients currently in the Suspense file with a HINQ response message. You may choose to print by patient (single or multiple), requestor or date/time.

The most recent HINQ response message that is associated with each entry will be provided. Entries with a pending status will not be displayed unless a HINQ response message has been previously received for that patient. If the Updated Field is “NO,” and a date appears in the Last Updated field, this date refers to a previous HINQ message received for that patient only and is not the most current.

With the storage of the returning HINQ information, a check sum has been developed to insure the integrity of the stored data. If the HINQ information in the Suspense file has been adjusted since the last HINQ for the selected patient(s), the following warning message will appear and you will be unable to continue.

"HINQ data does NOT seem right

Re-HINQ and/or Notify system manager.

HINQ check sum failure for {patient name}"

Only holders of security key DVBHINQ may access this option.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* This option will print out a report, identical to the mail \*

\* messages, of the patients in the suspense file with a \*

\* successful HINQ request. \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Printout by (M)ultiple patients, (R)equestor, (D)ate/time?

Multiple// <u>\<RET\></u>

Select patient from "HINQ Suspense file": <u>TESTM,PATIENT</u> 08-01-02

000000000 SC VETERAN UPDATED (01-11-1990)

Select patient from "HINQ Suspense file": <u>HINQ</u>PATIENT,ONE

06-04-29 000000000 NOT UPDATED

Select patient from "HINQ Suspense file": <u>\<RET\></u>

DEVICE: HOME// <u>\<RET\></u> RIGHT MARGIN: 80// <u>\<RET\></u>

TIME OF STATUS CHANGE: 01/11/92@15:50 STATUS : NEWMAIL

UPDATED? : YES Last Updated : 01/11/92@15:51

REQUESTED BY : USERC,TEST TIME OF REQUEST: 12/24/91@08:33

HINQPATIENT TWO, AUG 1,1899 SSN:000000000 C-#:00000000 S-#:000000000 SC Veteran

VBA name = H TWO

Prior names = Combat Disability = NONE

SSI Income = NEVER

Name = HINQPATIENT TWO

Address = 123 ANYWHERE STREET

Address = MT MS

Zip = 99999

Sex = MALE

Date of Birth = AUG 1,1899

VBA SSN = 000000000 (Verified)

Claim number = 00000000

Service Number = 00000000

Folder Location = NYC-RO

INDICATORS(Active Duty Training NO Homeless Veteran NO)

Service data VBA

-----------------------------------------------

Branch of Service = ARMY

EOD = DEC 3,1902

RAD = JAN 5,1906

Char of Service = Honorable

Type of Benefit =

DISABILITIES

Combined %=40 Disab. in Record=1 Eff Date of Combined %=OCT 01,1920

Original Current

Disability % Extrem Eff Date Eff Date

5202 - UPPER ARM CONDITION - 40 % - LU - -

Perm.,Total Disability = Yes

Perm.,Total Disability Eff Date = OCT 04, 2006

Dental Treatment provided at discharge

Employable indicator = Employable or not an issue

Competency Pay Status = Competent,or not an issue,Pay direct

Check Amount = 50.00

Another request using a patient not in the VBA database.

TIME OF STATUS CHANGE: 01/23/92@11:22 STATUS : Error

UPDATED? : NO Last Updated :

REQUESTED BY : HINQPATIENT THREE TIME OF REQUEST: 1/22/92@10:29

HINQPATIENT THREE JUN 4,1929 SSN:000000000 C-#:00000000 S-#:000000000

HINQ Error = HINQ Error = No Record matches data requested, Retry using

CN. via 'Individual HINQ'.

Inquiry Data Submitted = HINQ7 7169038 000000000 HINQPATIENT THREE

Through this option, all entries in the HINQ Suspense file with the status of PENDING may be transmitted to the VBA computer as a group. Only the patient's name and social security number are sent on the first try, even if the claim number and service number are known. If a match is not found then the HINQ software will retry using the claim number, if available.

The Process the HINQ Suspense File option can only be utilized if the HINQ site parameter, BATCH PROCESSING ENABLED, is set to YES.

This option will abort on the first request if the password is invalid. The Suspense file will show the first entry with ERROR status and the rest would remain PENDING.

Utilizing this option generates a mail bulletin which is sent to all members of the DVBHINQ mail group. The message will inform the recipients that are processing the Suspense file when it is completed, and include the total number of HINQ requests that were completed. This message also includes the number of returned successful response, abbreviated response and an error response.

#### ### Example

Note that for security reasons whenever the password is entered, it will not be displayed. An example of the MailMan bulletin generated by this option is also provided. This bulletin is sent to the DVBHINQ mail group only.

When you enter your HINQ password all 'P'ending

requests in the Suspense file will be generated.

Enter HINQ PASSWORD: Direct Requests Queued \*2222222

*Note:*

When the user selects this option, the User NUMBER field in the NEW PERSON file will verify if the HINQ employee number does exists, and if it does not then the option is automatically disabled, and the following message will appear.

> "HINQ Employee Number not in New Person file

> Notify System Manager"

## Status of HINQ By Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Status of HINQ By Patient option provides information about entries that are currently in the Suspense file. If a HINQ response has been returned for the patient, the response message will also be shown. This option is only available to holders of the HINQ security key, DVBHINQ.

This option provides users who are not members of the HINQ mail group the ability to view the HINQ responses.

The following information is displayed to the user for each selected patient currently in the Suspense file:

- PATIENT NAME, DATE OF BIRTH, and SSN
- TIME OF STATUS CHANGE - date and time that the HINQ status of this entry was last updated
- STATUS - the Suspense file status of this entry (PENDING, NEW MAIL, ERROR, or ABBREVIATED)
- UPDATED- all return HINQ data is updated and filed in the PATIENT file option
- LAST UPDATED – is the date and time the PATIENT file was last updated through the Update HINQs to the Patient file option. If the UPDATED field is set to NO the most recent date that a HINQ message was requested will appear
- REQUESTED BY - name(s) of user(s) who requested a HINQ
- TIME OF REQUEST In the event a user has entered more than one request for a patient, only the most recent date and time is stored
- HINQ RESPONSE the most recent HINQ response message for this patient is displayed to the user
- ELIGIBILITY STATUS -this status message is found in the PATIENT file option: (Verified, Pending Verification, Pending Re-Verification)

If the selected patient is not located in the Suspense file, the following message is displayed.

- Patient not in Suspense file

It is possible for a request to have the NEW MAIL status, but not have any HINQ response message associated with it. If a user decides to delete their messages this can be done through the Waste mail basket option. As with other mail messages, they are stored until all recipients delete them.

If the message has been deleted and you wish to have a copy of the message, use the Create a mail message option located under the Utilities for Suspense File Menu.

### Example 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This example illustrates an entry with the ERROR status.

Select PATIENT NAME: HINQPATIENT,FOUR 07-31-19 000000000

TIME OF STATUS CHANGE: 11/22/91@09:00 STATUS : Error

UPDATED? : NO Last Updated :

REQUESTED BY : USER,THREE TIME OF REQUEST: 11/20/91@10:00

HINQ response for HINQPATIENT,FOUR /requested by USER,TWO

11/22@09:00 HINQPATIENT,FOUR JUL 31,1919 SSN:000000000

Patient not in Suspense file

\*\*\*ELIGIBILITY NOT VERIFIED\*\*\*

### Example 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This example displays a request for an HINQ inquiry and the response from a VBA computer

This example illustrates two requests for HINQ inquiries entered in the Suspense file for the same patient. In the first, a HINQ response has not been returned from the VBA computer.

Select PATIENT NAME: HINQPATIENT,FOUR 07-10-03 000000000 SC Veteran

TIME OF STATUS CHANGE: 11/14/91@08:23 STATUS : Pending

UPDATED? : NO Last Updated : 06/15/91@09:53

REQUESTED BY : USER,ONE TIME OF REQUEST: 11/14/91@08:23

REQUESTED BY : USER,TWO TIME OF REQUEST: 11/06/91@12:55

\*\*\*ELIGIBILITY NOT VERIFIED\*\*\*

Select PATIENT NAME: <u>HINQPATIENT,FIVE</u> 08-01-02 000000000 NSC VETERAN

TIME OF STATUS CHANGE: 01/11/92@15:50 STATUS : NEWMAIL

UPDATED? : YES Last Updated : 01/11/92@15:51

REQUESTED BY : USER,FOUR TIME OF REQUEST: 12/24/91@08:33

HINQPATIENT,FIVE AUG 1,1899 SSN:000000000 C-#:000000000 S-#:000000000 NSC Veteran

VBA name = F HINQPATIENT

Prior names = Combat Disability = NONE

SSI Income = NEVER

Name = FIVE HINQPATIENT

Address = 123 Anywhere Street

Address = ANYCITY MS

Zip = 99999

Sex = MALE

Date of Birth = AUG 1,1899

VBA SSN = 0000000000 (Verified) Claim number = 000000000

Service Number = 000000000

Folder Location = NYC-RO

INDICATORS(Active Duty Training NO Disability NO Homeless Veteran NO)

Service data VBA

-----------------------------------------------

Branch of Service = ARMY

EOD = DEC 3,1902

RAD = JAN 5,1906

Char of Service = Dis for VA Pur

Type of Benefit =

DISABILITIES( Combined % = 10 Number of Disabilities in Record = 1 )

7805 - SCARS - 10% - SERVICE CONNECTED

Perm.,Total Disability =

Press return to continue

AID & ATTEND =

Chief Attorney, fiduciary =

Employable indicator = Employable or not an issue

Competency Pay Status = Competent,or not an issue,Pay direct

Check Amount = 50.00

## Utilities for Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Create a Mail Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a mail message option allows the user to create a mail message for entries in the Suspense file that have a successful HINQ response. The mail message(s) are sent to the members of the DVBHINQ mail group and will contain a copy of the patient's HINQ information.

With the storage of the returning HINQ information, a check sum has been developed to insure the integrity of the stored data. If the HINQ information in the Suspense file has been adjusted to the last HINQ response received from the patient file, the following warning message will appear preventing the user to continue.

"HINQ data does NOT seem right

Re-HINQ and/or Notify system manager.

HINQ check sum failure for {patient name}"

### ### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do you wish to create a mail message, to be sent to

the requestors? NO// <u>Y</u>ES

Select patient from "HINQ Suspense file": <u>TESTQ,PATIENT</u> 08-02-06

000000000 SC VETERAN NOT UPDATED

Select patient from "HINQ Suspense file": <u>\<RET\></u>

.

Mail Sent.

## Create a Mail Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: Hinq response for <u>HINQPATIENT,THREE</u> /requested by USER,FIVE \[4065178\]

26 OCT 91 10:56 18 Lines

From: POSTMASTER (Sender: USER,TEST (TOGUS VAMC)) in 'IN' basket. Page 1

\*\*NEW\*\*

------------------------------------------------------------------------------

HINQPATIENT,THREE AUG 2,1906 SSN:000000000 SC Veteran

VBA name = THREE, HINQPATIENT

Prior names =

Sex = MALE

Date of Birth = AUG 20,1870 Verified SVC-Data

Date of Death = SEP 01,1960

VBA SSN = 000101681 (Verified)

Claim Number = 0000000

Service Number = 0000000

Folder Location = 209

INDICATORS( Active Duty Training NO Homeless Veteran NO )

Service data VBA

----------------------------------------------

Branch of Service = AIR FORCE

EOD = SEP 18,1897

RAD = NOV 20,1899

Char of Svc: Honorable

Type Benefit: Pension

Pension Terminated = JAN 01, 1992 Reason code = 18

Reason code = 15

DISABILITIES

Combined %=0 Disab. in Record=0 Eff. Date of Comb. Eval.=

Vet married Vet = No spouse or not eligible

Check Amount= '\$0.0' Net Award= '\$0.0'

Select MESSAGE ACTION: IGNORE (in basket)//

## Delete Entry from HINQ Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete entry from HINQ Suspense file option allows the user to delete entry/entries from the HINQ Suspense file. This is the only method to delete a name from the Suspense file that was entered in error.

The user is prompted for the name to delete from the Suspense file. Once a name is selected, the system will automatically prompt the user to verify the name entered before deleting it.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will delete an entry from the HINQ suspense file.

Select HINQ SUSPENSE NAME: HINQPATIENT,TEN 08-21-06 000000000 SC Veteran

VETERAN NOT UPDATED

Is this the entry you want deleted? HINQPATIENT,TEN? NO// <u>Y</u> (YES)

Deletion completed on HINQPATIENT,TEN

Select HINQ SUSPENSE NAME:

## Edit HINQ Suspense File Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Suspense file utility option provides users with the ability to view and edit the following HINQ parameters.

## Network Day

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Generally this field contains the current day and date. The first time an option which requires a HINQ password is selected in a network workday, the value to this field is updated with the current day and date.

## Last Net-Workday

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the NETWORK DAY parameter is updated the first time an option which requires the HINQ password is selected (as previously described), this parameter is also automatically updated.

This parameter affects the HINQ option, View the HINQ Suspense File. This option displays entries in the Suspense file beginning with the current day and going back to the LAST NET-WORKDAY date.

To extend the date range for View the HINQ Suspense File option, this parameter can be edited to contain an earlier date. When the first request is transmitted on the following workday, this field will automatically be updated to the previous NETWORK DAY value.

## Edit HINQ Suspense File Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NETWORK DAY: FEB 10,2005//

This should default to the current day. This field is no longer used, as the VBA database is available 24/7.

LAST NET-WORKDAY: FEB 9,2005//

This should default to the last work day. This field is no longer used, as the VBA database is available 24/7.

## Network Enabled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter can be set to a YES or NO value to enable or disable the following options that allow the user to send requests to the VBA computer:

1.  Individual HINQ Request
2.  Process the HINQ Suspense File
3.  Generate HINQ Requests.

If network communication tests indicate a network communication problem exists, it is recommended that the network should be disabled through this parameter temporarily until the problem is resolved.

## Batch Processing Enabled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whenever this parameter is set to a YES or NO value. The value enables/disables the following option:

- Process the HINQ Suspense File.

## Use High Intensity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When this parameter is set to a YES value, the prompt will appear on portions of the HINQ screens as boldface and flashing type.

## Use HINQ Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When this field is set to NO alert processing will not call HINQ screens.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

USE HINQ SCREENS?: YES// ??

Choose from:

y YES

n NO

USE HINQ SCREENS?: YES//

Select HINQ MAIL GROUP: DVBHINQ// ?? take the default

DVBHINQ

## Select HINQ Mail Group: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user must have a DVBHINQ security key in order to access this option.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select HINQ MAIL GROUP: DVBHINQ// ?? take the default

DVBHINQ

## Auto-Requeue of IDCU Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter can be set to YES REQUEUE or NO REQUEUEING. The HINQ software uses the value in this parameter to determine whether or not to automatically resend a HINQ requests when the login to the remote RDPC fails for batch processing.

## Auto-Requeue Limit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter only applies to selected sites that automatically resend requests (as described above) for numbers set between 0 and 100. This number reprints the total number of times the system tries to resend a request when the login to the remote RDPC fails. In most recent circumstances, the numbers between 10 and 20 have been sufficient.

## Requeue Counter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field counts the number of batch processes that have been requeued by the system on a particular day. It is incremented by the system each time the system attempts to resend requests to the remote RDPC before retransmission of requests. The number in this field is compared with the number in the AUTO-REQUEUE LIMIT field. Once the requested numbers have exceeded the AUTO-REQUEUE LIMIT for the day, then any additional request from that point on will not be processed for that day.

## Edit HINQ Suspense File Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field can be edited, if necessary, to allow retransmission of requests after the AUTO-REQUEUE LIMIT has been exceeded. The system resets the counter to zero each workday.

## HINQ Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter should be set to YES if you are requesting your response messages to be generated as a batch HINQ requests. This is available to the user when the user selects the Generate HINQ Requests and Process the HINQ Suspense file options.

## New IDCU Interface: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter should be set to YES, if you are requesting a response message to the IDCU field. This field will no longer be accessed to the user but a new RDPC interface will take its place.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New IDCU Interface: YES// this field is no longer used. Accept the default.

## RDPC Time Difference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is set to the time difference (in hours) between the site time zone and the time zone of the RDPC where the HINQ requests are sent.

## RDPC IP Address 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is set during the installation stage. All users are requested NOT to edit this field. This field contains the IP Address that is required to access a direct connection to the VBA.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RDPC IP ADDRESS: nn.nnn.nnn.nnn// this field is set during installation – users should not edit.

This parameter contains the IP Address of the VBA Remote Data Processing Center

## ## Ask Medical Center Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At multi-divisional facilities, this parameter is set to YES when making a request. The division name is then displayed on the first line of the response.

## IDCU Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field is no longer used.

## IDCU Username-Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This field holds the IDCU username and password for your medical center. Do NOT enter your HINQ password here.

## HINQ Device Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the name/number of the device (as entered in your DEVICE file) which connects the DHCP computer to the site's IDCU for transmitting and receiving HINQ requests.

## Batch Device Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the name/number of the device (entered in your DEVICE file). This is used primarily when the batch process (Process the HINQ Suspense file or Generate HINQ Requests options) are processed. This option is different from the HINQ device.

## Institution/Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the number or name of the (INSTITUTION file) from the station.

## Edit HINQ Suspense File Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NETWORK DAY: DEC 10,1902// <u>\<RET\></u>

LAST NET-WORKDAY: DEC 9,1902// <u>T-5</u> (DEC 4, 1902)

NETWORK ENABLED: YES// <u>\<RET\></u>

BATCH PROCESSING ENABLED: YES// <u>\<RET\></u>

USE HIGH INTENSITY?: <u>YES</u>

AUTO-REQUEUE OF IDCU ERRORS: YES REQUEUE// <u>\<RET\></u>

AUTO-REQUEUE LIMIT: 10// <u>15</u>

REQUEUE COUNTER: 0// <u>\<RET\></u>

HINQ MAIL MESSAGES: <u>NO</u>

RDPC Time Difference: 0// <u>\<RET\></u>

ASK MEDICAL CENTER DIVISION: YES// <u>NO</u>

IDCU ADDRESS: <u>DMS.BDNE</u> Philadelphia

IDCU USERNAME-PASSWORD: <u>OGISC455C-PROVIEKE</u>

HINQ device name: <u>HINQ 10</u>

BATCH DEVICE NAME: <u>MINIOUT9.9</u>

INSTITUTION/STATION NUMBER: 500// <u>\<RET\></u>

## Network Enable/Disable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Disable HINQ Network

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Enable HINQ Network

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Disable HINQ Network and Enable HINQ Network options enable/disable those options which allow the user to transmit HINQ requests. Process the HINQ Suspense File; Generate HINQ Requests, and Individual HINQ Request.

If there are known problems with the communication link as indicated by failure of the HINQ transaction test, or if there are network messages indicating a transmission problem, the network should be disabled through the Disable HINQ Network option. Utilizing that option disables the transmitting functions. Information concerning the HINQ transaction test may be found in the Exported Options section of the HINQ v4.0 Technical Manual.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Utilities for Suspense File Option: <u>N</u>etwork Enable/Disable

Disable HINQ Network

Enable HINQ Network

Select Network Enable/Disable Option: <u>E</u>nable HINQ Network

Network Enabled

## Purge Suspense File (Retain 30 Days)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Suspense File (retains 30 days) option is used to delete entries from the HINQ Suspense file. All entries with the last status update or with a date that is before the last 30 days will automatically be deleted. When this option is utilized, the entries purged from the file are individually listed, and the total number of entries that were purged is also provided.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in the HINQ Suspense file before the last 30 days will

be deleted

Do You wish to continue ? NO// <u>YES</u>

TESTS,PATIENT NOV 01, 1985@10:04.

TESTT,PATIENT NOV 02, 1985@10:04.

TESTU,PATIENT NOV 02, 1985@10:05.

TESTV,PATIENT NOV 01, 1985@10:05.

4 Entries deleted from suspense file

## Recompile HINQ Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All edit templates and most of the print templates located in the HINQ package are compiled for quicker processing time. This option is used by the site manager to recompile the HINQ print and edit templates when a user is installing the system on multiple CPUs.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do you want to Recompile the HINQ edit and print templates? YES// <u>\<RET\></u> (YES)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Recompilation of 'Edit' templates

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

----Recompiling 'DVBHINQ UPDATE' Input Template----

Compiling DVBHINQ UPDATE input template of File 2.

'DVBHCE' ROUTINE FILED....

'DVBHCE1' ROUTINE FILED......

'DVBHCE2' ROUTINE FILED......

'DVBHCE3' ROUTINE FILED..

'DVBHCE4' ROUTINE FILED......

'DVBHCE5' ROUTINE FILED...

'DVBHCE7' ROUTINE FILED...

'DVBHCE8' ROUTINE FILED....

'DVBHCE9' ROUTINE FILED..

'DVBHCE10' ROUTINE FILED

'DVBHCE11' ROUTINE FILED..

'DVBHCE12'.ROUTINE FILED..

'DVBHCE13' ROUTINE FILED..

'DVBHCE14' ROUTINE FILED..

'DVBHCE15' ROUTINE FILED.

'DVBHCE16' ROUTINE FILED..

'DVBHCE17' ROUTINE FILED..

'DVBHCE19' ROUTINE FILED..

'DVBHCE20' ROUTINE FILED.

'DVBHCE6' ROUTINE FILED..

'DVBHCE18' ROUTINE FILED

'DVBHINQ UPDATE' has been recompiled in the ^DVBHCE\* routines.

## ## Recompile HINQ Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Recompilation of 'Print' templates

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

----Recompiling 'DVBHINQ PAT-HINQ COMP' Output Template----

Compiling DVBHINQ PAT-HINQ COMP print template of File 2........

'DVBHCG' ROUTINE FILED

'DVBHCG1' ROUTINE FILED........................................

'DVBHINQ PAT-HINQ COMP' has been recompiled in the ^DVBHCG\* routines.

## Select View Suspense File 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Select View Suspense File option is used to view a listing of entries located in the Suspense file.

The user may decide to list all the entries or specify a Suspense file status (NEW MAIL, PENDING, ERROR) to print only entries with this status. The user is then prompted to select a device.

The entries are listed in order according to the last status update, date/time, beginning with the most recent. The following data, if available to the user is displayed for each entry:

- Patient's Name
- Social Security Number
- Suspense File Status
- Date/Time Status Was Last Updated
- Name(S) Of Requestor(S)
- Date/Time Of Request(S).

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do you wish to view all entries ? ALL// <u>P</u>ENDING

DEVICE: HOME// <u>\<RET\></u> RIGHT MARGIN: 80// <u>\<RET\></u>

Patient SSN ..status..time Requested by

<u>HINQPATIENT,ONE</u> 000000000 ..P..11/25@14:23 USER,TWO 11/25@14:23

<u>HINQPATIENT,TWO</u> 000000000 ..P..11/25@09:41 USER,SEVEN 11/25@09:41

<u>HINQPATIENT,THREE</u> 000000000 ..P..11/24@17:00 USER,EIGHT 11/24@17:00

## View the HINQ Suspense File 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To View the HINQ Suspense File option lists entries from the HINQ Suspense file on the screen.

The HINQ parameter described below controls which Suspense file entries are displayed when this option is selected. Entries with HINQ status have been updated within the time period from the current day back to the LAST NET-WORKDAY.

LAST NET-WORKDAY: This field contains the date of the previous network day.

The following information, if available, is displayed for each entry in the Suspense file within the date range.

Patient's name and SSN

Suspense file status of the request

(PENDING, NEW MAIL, ERROR or ABBREVIATED)

Date/time Suspense file status was last updated

Names of user(s) who have requested a HINQ inquiry for the patient

Date/time of HINQ inquiry request(s)

Once this option is selected, the routine runs automatically with no user prompts.

*Example*

Patient SSN ..status..time Requested by

<u>HINQPATIENT,ONE</u> 000000000 ..N..11/25@14:23 USER,TWO 11/23@14:23

<u>HINQPATIENT,TWO</u> 000000000 ..N..11/25@09:41 USER,ONE 11/23@09:35

USER,NINE 11/23@14:30

<u>HINQPATIENT,THREE</u> 00000000 ..P..11/24@15:21 USER,TEN 11/24@15:21

<u>HINQPATIENT,FOUR</u> 000000000 ..P. 11/24@16:12 USER,ELEVEN 11/24@16:12

<u>HINQPATIENT,FIVE</u> 000000000 ..E..11/24@08:20 USER,TWELVE 11/22@12:09

<u>HINQPATIENT,SIX</u> 0000000000 .. A..11/24@11:43 USER,THIRTEEN 11/22@06:49

# # HINQ Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data contained in the response messages may be viewed through the HINQ Suspense File option.

HINQ responses are transmitted through the Individual HINQ Request option this will appear in the IN basket for all members of the DVBHINQ mail group anytime The Generate HINQ Requests, and Process the HINQ Suspense file options, parameter is set to YES. The messages are processed (saved, printed, etc.) similar to the other mail messages.

The header of the message gives the name of the patient requested in the HINQ inquiry with the name of the requestor, and the date/time of the request. The first line of the message gives the patient's name, date of birth, SSN, claim number and service number from the PATIENT file. If the ASK MEDICAL CENTER DIVISION parameter is set to YES, the division name will also appear in the first line of the response.

All successful responses will have the NEW MAIL status message text. This message text may contain Corporate, BIRLS data only or a combination of both BIRLS and C&P (compensation and pension) data. The Corporate database is searched first, and then the BIRLS and C&P records are searched.

All messages will not contain the same data items information for every veteran. For example, some responses may provide data about the spouse while others do not. The data items that may be included in response messages are listed under HINQ RESPONSE DATA ITEMS on the following pages.

## HINQ Response Data Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Veteran Name
- Prior Names
- Address
- Social Security Number
- Verified SSN Indicator - (Appears as the word "verified" after the SSN)
- Service Number
- Claim Number
- Date of Birth
- Date of Death
- Sex Indicator
- VA Employee
- EOD Date (Entered on duty date)
- RAD Date (Released from active duty date)
- Branch of Service
- Character of Service - (Unverified, Honorable, Other than Honorable, Dishonorable, Honorable for VA purposes, Dishonorable for VA purposes)
- Total Active Service in years, months, days
- Active Duty Training Indicator
- Vietnam Service
- Verified Svc Data - (Service data has been verified)
- Folder Location (VBA station that has jurisdiction for the veteran’s claim folder)
- POW days - (Number of days as prisoner of war)
- Medal of Honor
- Benefit Type
- Pension Award Effective Date
- Pension Award Reason
- Pension Award Termination Date
- Pension Termination Reason Codes (1 to 4 codes)
- Power of Attorney
- Guardianship - (Veteran has appointed guardian)
- Incompetent - (Will appear if veteran so rated)
- Homeless Veteran Indicator
- Chief Attorney, Fiduciary - (No fiduciary or the station number having jurisdiction over the fiduciary file)
- Aid and Attendance payee - (HB and/or A&A TERM; HOSPITALIZED, HB,A&A PAY; PAY A&A; HB ONLY; HB and/or A&A NOT GRANTED. All may contain increment for spouse.)
- Permanent & Total Disability indicator (Yes or No)
- Permanent & Total Disability Effective Date (if P&T Indicator = Yes)
- Dental Treatment provided/not provided at discharge
- Combined % of disability - (Veteran's service connected combined degree. Between 0 and 100)
- Effective Date of Combined SC % Evaluation
- Rated Disabilities – (Up to 150 Service-connected disabilities can be provided)
- Code
- Name
- Percent
- Extremity
- Original Effective Date
- Current Effective Date
- Number of school children
- Number of helpless children
- Number of Birth Segments - (Up to 20 entry birth segments are shown)
- Child Birth Date
- Child Status - (Helpless Child, Minor Child ,Not an Award Dependent, School Child, Unclaimed DIC Child)
- Child Name
- Automobile Adapt Equipment Paid - (Last year that a payment was issued for auto adaptive equipment)
- Auto Allowance Paid
- Special Adapted Housing Paid
- Anatomical Loss Code - (Loss of a limb, organ, etc.)
- Loss of Use Code - (Loss of use of a limb, organ, etc.)
- Other Loss Code - (Special losses which authorize additional payment)
- Veteran Married to Veteran.
- Blind Indicator
- Income for VA purposes
- Net award amount
- Total Check Amount
- Military Payment Code
- No Payment Status Code

## HINQ Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No VBA response available - please try again later.

Timed Out - No VBA Response Available

Invalid Employee number Not AUTHORIZED

PASSWORD missing or invalid

Station \# does not match Station \# of password

Employee Number in New Person file doesn't match the \# in VBA security record

File in alert - NOT available

NO C&P record found

SS \# missing or invalid

NAME missing or invalid.

File NOT available

SENSITIVE File no access authorized

Unsuccessful read of password or sensitive file

Invalid CLAIM NUMBER

Invalid SERVICE NUMBER

No record matches input. Check data and try again via 'Individual HINQ'

Following is an example of a HINQ error message:

Subj: Hinq Response for HINQPATIENT,TWO /requested by USER,TWENTY-TWO \#4049847\] 12 Oct 91 12:00 3 Line

FROM: POSTMASTER (Sender: USER,TWENTY-THR VAMC ANYVA)) in 'IN' basket. Page 1

-----------------------------------------------------------------------------

HINQPATIENT,TWO NOV 6,1950 SSN:000000000 NC Veteran

HINQ Error = PASSWORD missing or invalid

Inquiry Data Submitted = SS000000000

Select MESSAGE Action: IGNORE (IN basket)//

# # Performance Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VBA Common Security Services (CSS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All existing HINQ security requirements are maintained in V*ist*A. This process will not change. To ensure that all HINQ users will receive access to the system the following requirements are listed below:

### All users are required to have a VBA BDN Password, a HINQ employee number and a V*ist*A HINQ security key 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A user is required to access HINQ at least once very 90 days to avoid the system locking them out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### If a user has not accessed their HINQ account after 90 days an error code message will appear denying the user access to the system

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### If a user is denied access the user is required to contact the VBA ISO coordinator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### All users are responsible for following-up with their VBA ISO coordinator in expediting all access requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### All new employees are required to complete a VAF 20-8824e form to gain access to the HINQ system 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### *Note:*

In order to maintain a high security environment for HINQ system data we strongly suggest that access is provided only to those who will use HINQ on a regular basis.

## User Response Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Approximately up to 10,000 queries originate every week between HINQ and HEC and are captured through the e\*Gate server.

Overall VBA response time allows up to 150 diagnostic codes to be returned. In order to avoid transmitting unnecessary blanks, currently the HINQ response variable has been expanded to transmit the same amount of disability codes as the VBA returns them.

## ## VBA Unsolicited Eligibility Update to HEC (VBA Push)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once VBA converts its C&P claims data transactions to the Corporate environment all users will automatically see a decline in the number of records that are located in the C&P master file along with the awards that are authorized in the BDN environment. The C&P mini master file and the BDN will relinquish it effectiveness. The authorization for all new benefit awards and updates to existing awards in VBA’s Corporate database will automatically trigger unsolicited updates from VBA to the HEC, which, in turn, will release updates to all V*ist*A sites of record.

## Latency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Latency is a process that allows transactions to travel throughout the network in regulated intervals. Latency defines the actual amount of time a transaction can travel through the communication network.

Response times are generally affected by this process. In order to avoid long delays that are caused by the demands that are placed on the processor’s resources HINQ has developed a delay mechanism that will automatically trigger a response if it is not received in a adequate amount of time.

## Packet Sizing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a HINQ query is generated the V*ist*A processor first sends a packet of data to the target processor that opens the communication channel. At this point the target processor returns an acknowledgement that the data has been received. All data is captured and transmitted throughout the network in fixed packets of 256 bytes.

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary contains terms and definitions to the HINQ Replacement Interim Solution Phase 1.

BIRLS Beneficiary Information and Records Locator Subsystem

DVBHINQ A security Key in the HINQ package

HINQ Employee Number A number entered into the NEW PERSON file for each user who has a HINQ password

HINQ Response Response from VBA computer to a HINQ request

HINQ Suspense File A file that serves as two major functions:

1.  Stores HINQ requests that are processed at a different time
2.  Serves as a log to HINQ responses that are entered

HINQ Suspense File Status Pending request waiting for transmission

New Mail successful response received

Error error that occurs during an inquiry that is processed at the VBA computer

Abbreviated response received

IDCU error error occurred in the return transmission of the HINQ string

IDCU Integrated Data Communications Utility

VBA Veterans Benefits Administration

# # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

*Accessing the Software* 2

*As a Stand-Alone Option* 17

*As Part of the PIMS Options* 18

*Ask Medical Center Division* 36

*Auto-Requeue Limit* 34

*Auto-Requeue of IDCU Errors* 34

B

*Batch Device Name* 36

*Batch Processing Enabled* 33

BIRLS 48

C

*Create a Mail Message* 30

D

*Delete Entry from HINQ Suspense Fil* 32

DG ELIGIBILITY 4, 9

*Disable HINQ Network* 38

DVBHINQ 1, 4, 5, 9, 14, 16, 19, 20, 21, 23, 25, 26, 30, 34, 39, 40, 42, 48

E

*Edit HINQ Suspense File Parameters* 32, 33, 35, 37

*Enable HINQ Network* 38

*Enter a Request in the HINQ Suspense File* 4, 17

*Entering a HINQ Request* 5

*Error* 3

F

Functional Description 3

G

*Generate HINQ Requests* 4, 19

Glossary 48

H

*HINQ Device Name* 36

*HINQ Error Messages* 44

HINQ Replacement Diagram 2

HINQ Response 42

*HINQ Response Data Items* 42

HINQUP Features 4

I

IDCU 48

*IDCU Address* 36

*IDCU Username-Password* 36

*Individual HINQ Request* 4, 20

*Institution/Station Number* 37

Introduction 1

L

*Last Net-Workday* 32

*Latency* 47

N

*Network Day* 32

*Network Enable/Disable* 38

*Network Enabled* 33

*New IDCU Interface* 35

*New Mail* 3

O

Overview 1

P

*Packet Sizing* 47

Patient Safety Issue 7

*Pending* 3

Performance Requirements 46

*Print Suspense File Messages* 4, 23

*Process the HINQ Suspense File* 5

*Purge Suspense File* 38

R

*RDPC Time Difference* 35

*Recompile HINQ Templates* 39, 40

*Requeue Counter* 35

*Review Patient vs. HINQ Data* 14

Revision History i

S

Scope 1

*Screen 0* 8

*Screen 1* 8

*Screen 2* 8

*Screen 3* 8

*Screen 4* 9

*Screen 5* 9

*Select HINQ Mail Group* 34

*Select View Suspense File* 40

*Status of HINQ By Patient* 5, 26

*Summary* 42

*Suspense File* 3

U

*Update HINQ to the Patient File* 6

*Use High Intensity* 33

*Use HINQ Screens* 34

*User Response Time* 47

Using the Menu Options 4

Using the Software 2

*Utilities for Suspense File* 5, 30

V

VBA 48

*VBA Common Security Services (CSS)* 46

*VBA Unsolicited Eligibility Update to HEC (VBA Push)* 47

*View the HINQ Suspense File* 5, 41