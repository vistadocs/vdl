---
title: "Kernel 8.0 Developerâ€™s Guide: Alerts User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Alerts"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - alert
  - alerts
  - span
  - table
  - contents
  - identifier
  - class
  - input
  - example
  - xqaid
page_count: 0
word_count: 11157
section_count: 30
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_alerts_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_alerts_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  Alerts Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-alerts-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-alerts-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Toc199951034" class="anchor"></span>Table 1: Alerts—Related Terms and Definitions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
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
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Alerts Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Toc199951034" class="anchor"></span>Table 1: Alerts—Related Terms and Definitions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc207253080" class="anchor"></span>List of Figures

<span id="_Toc207253081" class="anchor"></span>List of Tables

[Table 1: Alerts—Related Terms and Definitions [4](#_Toc199951034)](#_Toc199951034)

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-alerts-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Package Identifier or Alert Identifier](#package-identifier-or-alert-identifier)
    - [Package Identifier](#package-identifier)
    - [Alert Identifier](#alert-identifier)
  - [Package Identifier Conventions](#package-identifier-conventions)
  - [Alerts Glossary of Terms](#alerts-glossary-of-terms)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [AHISTORY^XQALBUTL(): Get Alert Tracking File Information](#ahistoryxqalbutl-get-alert-tracking-file-information)
    - [Example](#example)
  - [ALERTDAT^XQALBUTL(): Get Alert Tracking File Information](#alertdatxqalbutl-get-alert-tracking-file-information)
    - [Example](#example-1)
  - [DELSTAT^XQALBUTL(): Get Recipient Information and Alert Status](#delstatxqalbutl-get-recipient-information-and-alert-status)
    - [Example](#example-2)
  - [NOTIPURG^XQALBUTL(): Purge Alerts Based on Code](#notipurgxqalbutl-purge-alerts-based-on-code)
  - [\$\$PENDING^XQALBUTL(): Pending Alerts for a User](#pendingxqalbutl-pending-alerts-for-a-user)
    - [Examples](#examples)
  - [\$\$PKGPEND^XQALBUTL(): Pending Alerts for a User in Specified Software](#pkgpendxqalbutl-pending-alerts-for-a-user-in-specified-software)
    - [Examples](#examples-1)
  - [PTPURG^XQALBUTL(): Purge Alerts Based on Patient](#ptpurgxqalbutl-purge-alerts-based-on-patient)
  - [RECIPURG^XQALBUTL(): Purge User Alerts](#recipurgxqalbutl-purge-user-alerts)
  - [USERDATA^XQALBUTL(): Get User Information for an Alert](#userdataxqalbutl-get-user-information-for-an-alert)
    - [Example](#example-3)
  - [USERLIST^XQALBUTL(): Get Recipient Information for an Alert](#userlistxqalbutl-get-recipient-information-for-an-alert)
    - [Example](#example-4)
  - [ACTION^XQALERT(): Process an Alert](#actionxqalert-process-an-alert)
  - [DELETE^XQALERT: Clear Obsolete Alerts](#deletexqalert-clear-obsolete-alerts)
  - [DELETEA^XQALERT: Clear Obsolete Alerts](#deleteaxqalert-clear-obsolete-alerts)
  - [GETACT^XQALERT(): Return Alert Variables](#getactxqalert-return-alert-variables)
  - [PATIENT^XQALERT(): Get Alerts for a Patient](#patientxqalert-get-alerts-for-a-patient)
  - [SETUP^XQALERT: Send Alerts](#setupxqalert-send-alerts)
    - [Details—When the Alert is Processed](#detailswhen-the-alert-is-processed)
    - [Example](#example-5)
  - [\$\$SETUP1^XQALERT: Send Alerts](#setup1xqalert-send-alerts)
    - [Details—When the Alert is Processed](#detailswhen-the-alert-is-processed-1)
    - [Example](#example-6)
  - [USER^XQALERT(): Get Alerts for a User](#userxqalert-get-alerts-for-a-user)
    - [Example](#example-7)
  - [FORWARD^XQALFWD(): Forward Alerts](#forwardxqalfwd-forward-alerts)
    - [Example](#example-8)
  - [\$\$CURRSURO^XQALSURO(): Get Current Surrogate for Alerts](#currsuroxqalsuro-get-current-surrogate-for-alerts)
  - [\$\$GETSURO^XQALSURO(): Get Current Surrogate Information](#getsuroxqalsuro-get-current-surrogate-information)
    - [Example](#example-9)
  - [REMVSURO^XQALSURO(): Remove Surrogates for Alerts](#remvsuroxqalsuro-remove-surrogates-for-alerts)
  - [SETSURO1^XQALSURO(): Establish a Surrogate for Alerts](#setsuro1xqalsuro-establish-a-surrogate-for-alerts)
    - [Example](#example-10)
  - [SUROFOR^XQALSURO(): Return a Surrogate’s List of Users](#suroforxqalsuro-return-a-surrogates-list-of-users)
    - [Example](#example-11)
  - [SUROLIST^XQALSURO(): List Surrogates for a User](#surolistxqalsuro-list-surrogates-for-a-user)
    - [Example](#example-12)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Alerts Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application might want to issue an alert to one or more users when certain conditions are met, such as depleted stock levels or abnormal lab test results.

Alerts are usually generated through APIs. The [SETUP^XQALERT](#setupxqalert-send-alerts) API creates an alert.

You may want to send alerts from within an application program or as part of a trigger in a VA FileMan file. Developers and system administrators are invited to discover imaginative ways to integrate alerts within local and national programming. Remember, however, *not* to overwhelm the user with alerts.

Once you have sent an alert, one way you can confirm that the alert was sent is to use the VA FileMan Inquire to File Entries \[DIINQUIRE\] option and examine the entry in the ALERT (#8992) file for the users to whom you sent the alert.

<span id="_Toc199950510" class="anchor"></span>Figure 1: Alerts—Creating an Alert for a User (such as #14)

; send alert

S XQA(14)="",XQAMSG="Enter progress note",XQAOPT="ZZNOTES"

D SETUP^XQALERT

<span id="_Toc200269954" class="anchor"></span>Figure 2: Alerts—Checking that the Alert was Sent

\><span class="mark">D Q^DI</span>

Select OPTION: <span class="mark">INQ \<Enter\></span> UIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: <span class="mark">ALERT</span>

Select ALERT RECIPIENT: <span class="mark">\`14 \<Enter\></span> XUUSER,14

ANOTHER ONE: <span class="mark">\<Enter\></span>

STANDARD CAPTIONED OUTPUT? YES// <span class="mark">\<Enter\></span>

Include COMPUTED fields: (N/Y/R/B): NO// <span class="mark">\<Enter\></span> - No record number (IEN), no Computed Fields

RECIPIENT: XUUSER,15

ALERT DATE/TIME: DEC 01, 1994@08:02:21

ALERT ID: NO-ID;161;2941201.080221

MESSAGE TEXT: Enter Progress Note NEW ALERT FLAG: NEW

ACTION FLAG: RUN ROUTINE ENTRY POINT: ZZOPT

## Package Identifier or Alert Identifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Package Identifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software application identifier for an alert is defined as the original value of the XQAID input variable when the alert is created through the <u>SETUP^XQALERT: Send Alerts</u> API. Typically, the software application identifier should begin with the software application namespace.

### Alert Identifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The alert identifier consists of three semicolon pieces:

pkgid\_";"\_duz\_";"\_time

Where:

- pkgid is the original software application identifier.
- duz is the DUZ of the user who created the alert.
- time is the time the alert was created (in VA FileMan format).

The alert identifier uniquely identifies a particular alert (it is used as the value of the .01 field in the ALERT TRACKING \[#8992.1\] file).

The distinction between software application identifier and alert identifier is important. More than one alert can share the same software application identifier, but the alert identifier is unique. Some Alert Handler APIs ask for a software application identifier (and act on multiple alerts), while other APIs ask for an alert identifier (and act on a single alert).

## Package Identifier Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) software uses a convention for the format of the software application identifier consisting of three comma-delimited pieces:

namespace\_“,”\_dfn\_“,”\_notificationcode

Where:

- namespace is the software application namespace.
- dfn is the internal entry number of the patient whom the alert concerns in the PATIENT (#2) file.
- notificationcode is a code maintained by the CPRS software describing the type of alert.

![](kernel-8-0-developer-s-guide-alerts-user-guide/004.png) NOTE: This three-comma-piece software application identifier is still only the first semicolon piece of an alert identifier.

Several Alert Handler APIs make use of these software application identifier conventions:

- [PATIENT^XQALERT](#patientxqalert-get-alerts-for-a-patient) returns an array of alerts for a particular patient, based on the second comma-piece of alerts’ software application identifiers.
- [PTPURG^XQALBUTL](#ptpurgxqalbutl-purge-alerts-based-on-patient) purges alerts for a particular patient, based on the second comma-piece of alerts’ software application identifiers.
- [NOTIPURG^XQALBUTL](#notipurgxqalbutl-purge-alerts-based-on-code) purges alerts with a particular notification code, based on the third comma-piece of alerts’ software application identifiers.

## Alerts Glossary of Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Alerts</strong></td>
<td><p>An alert notifies one or more users of a matter requiring immediate attention. Alerts function as brief notices that are distinct from mail messages or triggered bulletins.</p>
<p>Alerts are designed to provide interactive notification of pending computing activities (such as the need to reorder supplies or review a patient’s clinical test results). Along with the alert message is an indication that the <strong>View Alerts</strong> [XQALERT] common option should be chosen to take further action.</p>
<p>An alert includes any specifications made by the developer when designing the alert. This minimally includes the alert message and the list of recipients (an information-only alert). It can also include an alert action, software application identifier, alert flag, and alert data. Alerts are stored in the ALERT (#8992) file.</p></td>
</tr>
<tr class="even">
<td><strong>Alert Action</strong></td>
<td>The computing activity that can be associated with an alert (that is an option [<strong>XQAOPT</strong> input variable] or routine [<strong>XQAROU</strong> input variable]).</td>
</tr>
<tr class="odd">
<td><strong>Alert Data</strong></td>
<td>An optional string that the developer can define when creating the alert. This string is restored in the <strong>XQADATA</strong> input variable when the alert action is taken.</td>
</tr>
<tr class="even">
<td><strong>Alert Flag</strong></td>
<td>An optional tool currently controlled by the Alert Handler to indicate how the alert should be processed (<strong>XQAFLG</strong> input variable).</td>
</tr>
<tr class="odd">
<td><strong>Alert Handler</strong></td>
<td>The name of the mechanism by which alerts are stored, presented to the user, processed, and deleted. The Alert Handler is a part of Kernel, in the <strong>XQAL</strong> namespace.</td>
</tr>
<tr class="even">
<td><strong>Alert Identifier</strong></td>
<td>A three-semicolon piece identifier; composed of the original Package Identifier (described below) as the first piece; the <strong>DUZ</strong> of the alert creator as the second piece; and the date and time (in VA FileMan format) when the alert was created as the third piece. The Alert Identifier is created by the Alert Handler and uniquely identifies an alert.</td>
</tr>
<tr class="odd">
<td><strong>Alert Message</strong></td>
<td>One line of text that is displayed to the user (the <strong>XQAMSG</strong> input variable).</td>
</tr>
<tr class="even">
<td><strong>Package Identifier</strong></td>
<td>An optional identifier that the developer can use to identify the alert for such purposes as subsequent lookup and deletion (<strong>XQAID</strong> input variable).</td>
</tr>
<tr class="odd">
<td><strong>Purge Indicator</strong></td>
<td>Checked by the Alert Handler (in the <strong>XQAKILL</strong> input variable) to determine whether an alert should be deleted, and whether deletion should be for the current user or for all users who might receive the alert.</td>
</tr>
</tbody>
</table>

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Alerts APIs and Extrinsic Functions are available for developers to work with alerts. These APIs and Extrinsic Functions are described below.

## AHISTORY^XQALBUTL(): Get Alert Tracking File Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 2788

Description: The AHISTORY^XQALBUTL API returns information from the ALERT TRACKING (#8992.1) file for alerts with the xqaid input parameter as its alert ID. The data is returned descendent from the closed root passed in the root input parameter. Usually, xqaid is known based on alert processing.

Format: AHISTORY^XQALBUTL(xqaid,root)

Input Parameters:xqaid: (required) This is the value of the alert identifier. It is passed to the routine or option that is run when the alert is selected. It can also be obtained from a listing of all xqaid values for a specified user and/or patient.

root: (required) This parameter is a closed reference to a local or global root. The information associated with the desired entry in the ALERT TRACKING (#8992.1) file is returned descendent from the specified root.

![](kernel-8-0-developer-s-guide-alerts-user-guide/005.png) NOTE: A more user (developer) friendly call would be the <u>ALERTDAT^XQALBUTL(): Get Alert Tracking File Information</u> API, which returns the data in an array with the field numbers and names as the subscripts and the internal and external (if different) values as the value.

Output: returns: The data returned reflects the global structure of the ALERT TRACKING (#8992.1) file.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 3</u> illustrates the use of the AHISTORY^XQALBUTL API and the format of the data returned.

<span id="_Ref500327649" class="anchor"></span>Figure 3: AHISTORY^XQALBUTL API—Example: Sample Use and Format of Data Returned

\><span class="mark">S XQAID="NO-ID;20;2990212.11294719"</span>

\><span class="mark">D AHISTORY^XQALBUTL(XQAID,"XXXROOT")</span>

\><span class="mark">ZW XXXROOT</span>

XXXROOT(0)=NO-ID;20;2990212.11294719^2990212.112947^NO-ID^^20

XXXROOT(1)=TEST MESSAGE (ROUTINE) 20^^^XM

XXXROOT(20,0)=^8992.11^20^1

XXXROOT(20,1,0)=20^2990212.112954^2990212.145609^2990212.145621^2990212.145621

XXXROOT(20,"B",20,1)=

<u>Figure 4</u> is in the basic structure of the nodes taken from the global for this entry, which can be seen from a global map view of the ALERT TRACKING (#8992.1) file:

<span id="_Ref500327650" class="anchor"></span>Figure 4: AHISTORY^XQALBUTL API—Example: Basic Structure of Nodes Taken from the Global for this Entry as seen through a Global Map View of the ALERT TRACKING (#8992.1) File

^XTV(8992.1,D0,0)= (#.01) NAME \[1F\] ^ (#.02) DATE CREATED \[2D\]^ (#.03) PKG

==\>ID \[3F\] ^ (#.04) PATIENT \[4P\] ^ (#.05)

GENERATED BY \[5P\] ^

==\>(#.06) GENERATED WHILE QUEUED \[6S\] ^ (#.07)

STATUS \[7S\] ^

==\>(#.08) RETENTION DATE \[8D\] ^

^XTV(8992.1,D0,1)= (#1.01) DISPLAY TEXT \[1F\] ^ (#1.02) OPTION FOR PROCESSING

==\>\[2F\] ^ (#1.03) ROUTINE TAG \[3F\] ^ (#1.04)

ROUTINE FOR

==\>PROCESSING \[4F\] ^

^XTV(8992.1,D0,2)= (#2) DATA FOR PROCESSING \[E1,245F\] ^

^XTV(8992.1,D0,20,0)=^8992.11PA^^ (#20) RECIPIENT

^XTV(8992.1,D0,20,D1,0)= (#.01) RECIPIENT \[1P\] ^ (#.02) ALERT FIRST DISPLAYED

==\>\[2D\] ^ (#.03) FIRST SELECTED ALERT \[3D\] ^ (#.04)

==\>PROCESSED ALERT \[4D\] ^ (#.05) DELETED ON \[5D\] ^

==\>(#.06) AUTO DELETED \[6D\] ^ (#.07) FORWARDED BY \[7P\]

==\>^ (#.08) DATE/TIME FORWARDED \[8D\] ^ (#.09) DELETED

==\>BY USER \[9P\] ^

![](kernel-8-0-developer-s-guide-alerts-user-guide/006.png) NOTE: A more user (developer) friendly API would be the <u>ALERTDAT^XQALBUTL(): Get Alert Tracking File Information</u> API, which returns the data in an array with the field numbers and names as the subscripts and the internal and external (if different) values as the value.

## ALERTDAT^XQALBUTL(): Get Alert Tracking File Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 2788

Description: The ALERTDAT^XQALBUTL API returns information from the ALERT TRACKING (#8992.1) file for alerts with the xqaid input parameter as its alert ID in the array specified by the root input parameter. If root is *not* specified, then the data is returned in an XQALERTD array. If the specified alert is *not* present, the root array is returned with a NULL value.

Format: ALERTDAT^XQALBUTL(xqaid\[,root\])

Input Parameters:xqaid: (required) This is the value of the alert identifier. It is passed to the routine or option that is run when the alert is selected. It can also be obtained from a listing of all xqaid values for a specified user and/or patient.

root: (optional) This parameter is a closed reference to a local or global root. If root is *not* specified, then the data is returned in an XQALERTD array.

Output: returns: Returns:

- ALERT TRACKING File Entry—The information associated with the desired entry in the ALERT TRACKING (#8992.1) file descendent from the specified root.
- NULL—If the specified alert is *not* present, the array root is returned with a NULL value.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950514" class="anchor"></span>Figure 5: ALERTDAT^XQALBUTL API—Example

\><span class="mark">S XQAID="NO-ID;20;2990212.11294719"</span>

\><span class="mark">D ALERTDAT^XQALBUTL(XQAID,\$NA(^TMP(\$J,"A")))</span>

\><span class="mark">D ^%G Global ^TMP(\$J,"A"</span>

TMP(\$J,"A"

^TMP(000056198,"A",.01) = NO-ID;20;2990212.11294719

^TMP(000056198,"A",.01,"NAME") =

^TMP(000056198,"A",.02) = 2990212.112947^FEB 12, 1999@11:29:47

^TMP(000056198,"A",.02,"DATE CREATED") =

^TMP(000056198,"A",.03) = NO-ID ^TMP(000056198,"A",.03,"PKG ID") = ^TMP(000056198,"A",.04) =

^TMP(000056198,"A",.04,"PATIENT") = ^TMP(000056198,"A",.05) = 20^USER,XXX ^TMP(000056198,"A",.05,"GENERATED BY") =

^TMP(000056198,"A",.06) = ^TMP(000056198,"A",.06,"GENERATED WHILE QUEUED") = ^TMP(000056198,"A",.07) =

^TMP(000056198,"A",.07,"STATUS") =

^TMP(000056198,"A",.08) =

^TMP(000056198,"A",.08,"RETENTION DATE") =

^TMP(000056198,"A",1.01) = TEST MESSAGE (ROUTINE) 20

^TMP(000056198,"A",1.01,"DISPLAY TEXT") =

^TMP(000056198,"A",1.02) = ^TMP(000056198,"A",1.02,"OPTION FOR PROCESSING") = ^TMP(000056198,"A",1.03) =

^TMP(000056198,"A",1.03,"ROUTINE TAG") =

^TMP(000056198,"A",1.04) = XM ^TMP(000056198,"A",1.04,"ROUTINE FOR PROCESSING") = ^TMP(000056198,"A",2) =

^TMP(000056198,"A",2,"DATA FOR PROCESSING") =

The data elements at the top level of the ACTIVITY TRACKING file are returned subscripted by the field numbers. This subscript is sufficient to obtain the data. The values are shown as internal^external if the internal and external forms are different. The next subscript after the field number provides the field names if they are desired.

## DELSTAT^XQALBUTL(): Get Recipient Information and Alert Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3197

Description: The DELSTAT^XQALBUTL API obtains information on the recipients of the most recent alert with a specified alert ID and the status of whether the alert has been deleted or not for those recipients.

Format: DELSTAT^XQALBUTL(xqaidval,.values)

Input Parameters:xqaidval: (required) This input parameter is a value that has been used as the xqaid value for generating an alert by a software application. This value identifies the most recent alert generated with this xqaid value and that alert generates the responses in terms of recipients and deletion status of the alert for each of the recipients.

Output Parameters:.values: This parameter is passed by reference and is returned as an array. The value of the values array indicates the number of entries in the array. The entries are then ordered in numerical order in the values array. The array contains the DUZ for users along with an indicator of whether the alert has been deleted.

![](kernel-8-0-developer-s-guide-alerts-user-guide/007.png) NOTE: The contents of the array are KILLed prior to building the list.

For example:

- DUZ^1—If alert deleted.
- DUZ^0—If alert *not* deleted.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950515" class="anchor"></span>Figure 6: DELSTAT^XQALBUTL API—Example

\><span class="mark">D DELSTAT^XQALBUTL("OR;14765;23",.VALUE)</span>

The value of VALUE indicates the number of entries in the array. The entries are then ordered in numerical order in the VALUE array:

<span id="_Toc199950516" class="anchor"></span>Figure 7: DELSTAT^XQALBUTL API—Example: Sample VALUE Array

VALUE = 3

VALUE(1) = "146^0" User 146 - not deleted

VALUE(2) = "297^1" User 297 - deleted

VALUE(3) = "673^0" User 673 - not deleted

## NOTIPURG^XQALBUTL(): Purge Alerts Based on Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3010

Description: The NOTIPURG^XQALBUTL API deletes all alerts that have the specified notifnum notification number as the third comma-piece of the alert’s Package Identifier (the original value of XQAID when the alert was created).

Format: NOTIPURG^XQALBUTL(notifnum)

Input Parameters:notifnum: (required) The notification number for which all alerts should be deleted. Alerts are deleted if the value of this parameter matches the third comma-piece in the alert’s Package Identifier.

Output: none.

## \$\$PENDING^XQALBUTL(): Pending Alerts for a User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 2788

Description: The \$\$PENDING^XQALBUT extrinsic function returns whether the user specified has the alert indicated by the xqaid input parameter as pending. It returns either of the following:

- 1—YES, alert is pending.
- 0—NO, alert is *not* pending.

Format: \$\$PENDING^XQALBUTL(xqauser,xqaid)

Input Parameters:xqauser: (required) This is the Internal Entry Number (IEN, DUZ value) in the NEW PERSON (#200) file for the desired user.

xqaid: (required) This is the value of the alert identifier. It is passed to the routine or option that is run when the alert is selected. It can also be obtained from a listing of all xqaid values for a specified user and/or patient.

Output: returns: Returns:

- 1—YES, alert is pending.
- 0—NO, alert is *not* pending.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<u>Figure 8</u> is an example of an alert *not* pending:

<span id="_Ref499809195" class="anchor"></span>Figure 8: \$\$PENDING^XQALBUTL API—Example 1

\><span class="mark">S XQAID="NO-ID;20;2990212.11294719"</span>

\><span class="mark">W \$\$PENDING^XQALBUTL(20,XQAID)</span>

0

#### Example 2

<u>Figure 9</u> is an example of an alert pending:

<span id="_Ref499809202" class="anchor"></span>Figure 9: \$\$PENDING^XQALBUTL API—Example 2

\><span class="mark">S XQAID="NO-ID;20;2990212.15540723"</span>

\><span class="mark">W \$\$PENDING^XQALBUTL(20,XQAID)</span>

1

## \$\$PKGPEND^XQALBUTL(): Pending Alerts for a User in Specified Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 2788

Description: The \$\$PKGPEND^XQALBUTL extrinsic function returns whether the user specified has an alert with XQAID containing the first “;”-piece (software/package identifier) indicated by the xqapkg input parameter pending. It returns either of the following:

- 1—YES, indicates one *or more* alerts pending for the specified user containing the software/package identifier.
- 0—NO, alerts *not* pending.

Format: \$\$PENDING^XQALBUTL(xqauser,xqapkg)

Input Parameters: xqauser: (required) This is the Internal Entry Number (IEN, DUZ value) in the NEW PERSON (#200) file for the desired user.

xqapkg: (required) This is the software/package identifier portion of the alert identifier (XQAID). It is a textual identifier for the software that created the alert and is the first “;”-piece of XQAID. It can be used in this context to determine whether the user specified by the xqauser input parameter has any alerts pending containing the specified software identifier. The software identifier used can be a complete software identifier (such as XU-TSK) or more general (such as XU) to find users with any XU software alerts.

Output: returns: Returns:

- 1—YES, indicates one *or more* alerts pending for the specified user containing the software/package identifier string in the package part of XQAID.
- 0—NO, alerts *not* pending.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<u>Figure 10</u> is an example of an alert *not* pending:

<span id="_Ref499810018" class="anchor"></span>Figure 10: \$\$PKGPEND^XQALBUTL API—Example 1

\><span class="mark">S XQKG="XU"</span>

\><span class="mark">W \$\$PKGPEND^XQALBUTL(20,XQKG)</span>

0

#### Example 2

<u>Figure 11</u> is an example of an alert pending (one or more):

<span id="_Ref499810027" class="anchor"></span>Figure 11: \$\$PKGPEND^XQALBUTL API—Example 2

\><span class="mark">S XQKG="XU"</span>

\><span class="mark">W \$\$PKGPEND^XQALBUTL(20,XQKG)</span>

1

## PTPURG^XQALBUTL(): Purge Alerts Based on Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3010

Description: The PTPURG^XQALBUTL API deletes all alerts that have the specified patient internal entry number (DFN) as the second comma-piece of the alert’s Package Identifier (the original value of XQAID when the alert was created).

Format: PTPURG^XQALBUTL(dfn)

Input Parameters: dfn: (required) Internal entry number (DFN in the PATIENT \[#2\] file) for which alerts are deleted.

Output: none.

## RECIPURG^XQALBUTL(): Purge User Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3010

Description: The RECIPURG^XQALBUTL API deletes all alerts that have been sent to the user in the NEW PERSON (#200) file, as indicated by the duz parameter.

Format: RECIPURG^XQALBUTL(duz)

Input Parameters:duz: (required) Internal Entry Number (IEN in the NEW PERSON \[#200\] file) of the user who received alerts is deleted.

Output: none.

## USERDATA^XQALBUTL(): Get User Information for an Alert

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 2788

Description: The USERDATA^XQALBUTL API returns recipients of the alert with the xqaid input parameter as its alert ID from the ALERT TRACKING (#8992.1) file in the array specified by the root input parameter. If root is *not* specified, then the data is returned in the XQALUSER array. If the specified alert is *not* present, the root array is returned with a NULL value.

Format: USERDATA^XQALBUTL(xqaid,xqauser,root)

Input Parameters: xqaid: (required) This is the value of the alert identifier. It is passed to the routine or option that is run when the alert is selected. It can also be obtained from a listing of all xqaid values for a specified user and/or patient.

xqauser: (required) This is the Internal Entry Number (IEN, DUZ value) in the NEW PERSON (#200) file for the desired user.

root: (optional) This parameter is a closed reference to a local or global root. If root is *not* specified, then the data is returned in the XQALUSER array.

Output: returns: Returns:

- ALERT TRACKING File Entry—The information associated with the desired entry in the ALERT TRACKING (#8992.1) file descendent from the specified root.
- NULL—If the specified alert is *not* present, the array root is returned with a NULL value.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950521" class="anchor"></span>Figure 12: USERDATA^XQALBUTL API—Example

\><span class="mark">D USERDATA^XQALBUTL(XQAID,20,"XXX")</span>

\><span class="mark">ZW XXX</span>

XXX(.01)=20^USER,XXX XXX(.01,"RECIPIENT")=

XXX(.02)=2990212.112954^FEB 12, 1999@11:29:54 XXX(.02,"ALERT FIRST DISPLAYED")=

XXX(.03)=2990212.145609^FEB 12, 1999@14:56:09 XXX(.03,"FIRST SELECTED ALERT")=

XXX(.04)=2990212.145621^FEB 12, 1999@14:56:21 XXX(.04,"PROCESSED ALERT")=

XXX(.05)=2990212.145621^FEB 12, 1999@14:56:21 XXX(.05,"DELETED ON")=

XXX(.06)= XXX(.06,"AUTODELETED")=

XXX(.07)= XXX(.07,"FORWARDED BY")=

XXX(.08)= XXX(.08,"DATE/TIME FORWARDED")=

XXX(.09)= XXX(.09,"DELETED BY USER")=

## USERLIST^XQALBUTL(): Get Recipient Information for an Alert

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 2788

Description: The USERLIST^XQALBUTL API returns recipients of the alert with the xqaid input parameter as its alert ID from the ALERT TRACKING (#8992.1) file in the array specified by the root input parameter. If root is *not* specified, then the data is returned in the XQALUSRS array. If the specified alert is *not* present, the root array is returned with a NULL value.

Format: USERLIST^XQALBUTL(xqaid,root)

Input Parameters:xqaid: (required) This is the value of the alert identifier. It is passed to the routine or option that is run when the alert is selected. It can also be obtained from a listing of all xqaid values for a specified user and/or patient.

root: (optional) This parameter is a closed reference to a local or global root. If root is *not* specified, then the data is returned in the XQALUSRS array.

Output: returns: Returns:

- ALERT TRACKING File Entry—The information associated with the desired entry in the ALERT TRACKING (#8992.1) file descendent from the specified root.
- NULL—If the specified alert is *not* present, the array root is returned with a NULL value.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950522" class="anchor"></span>Figure 13: USERLIST^XQALBUTL API—Example

\><span class="mark">D USERLIST^XQALBUTL(XQAID)</span>

\><span class="mark">ZW XQALUSRS XQALUSRS(1)=20^USER,XXX</span>

## ACTION^XQALERT(): Process an Alert

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 10081

Description: The ACTION^XQALERT API processes an alert for a user, if that user is the current user. Processing of the alert happens exactly as if the user had chosen to process the alert from the View Alerts menu.

Format: ACTION^XQALERT(alertid)

Input Parameters:alertid: (required) Alert Identifier of the alert to process (same as ALERT ID field in ALERT \[#8992\] file). This contains three semicolon-delimited pieces:

1.  Original software application identifier.
2.  DUZ of the alert creator.
3.  VA FileMan date and time the alert was created.

Output: none.

## DELETE^XQALERT: Clear Obsolete Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 10081

Description: The DELETE^XQALERT API deletes (clears) a single alert, for the current user (XQAKILL=1) or all recipients (XQAKILL=0 or XQAKILL undefined). The current user (as identified by the value of DUZ) does *not* need to be a recipient of an alert; however, in that case, only a value of Zero (0 or undefined) for XQAKILL makes sense.

DELETE^XQALERT, unlike [DELETEA^XQALERT](#deleteaxqalert-clear-obsolete-alerts), deletes only a single alert whose alert identifier matches the complete Alert Identifier.

![](kernel-8-0-developer-s-guide-alerts-user-guide/008.png) REF: For more information on alert identifiers, see the “<u>Package Identifier or Alert Identifier</u>” section.

Format: DELETE^XQALERT

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
2.  Set all input variables.
3.  Call the API.

Input Variables: XQAID: (required) Alert Identifier of the alert to delete. It *must* be a complete Alert Identifier, containing all three semicolon pieces:

1.  The first semicolon piece (Package Identifier) *must* be in the same form as the alert creator defined it.
4.  The second piece being the DUZ of the user who created the alert.
5.  The third piece being the time the alert was created.

![](kernel-8-0-developer-s-guide-alerts-user-guide/009.png) NOTE: The second and third pieces are defined by the Alert Handler.

XQAKILL: (optional) XQAKILL determines how the alert is deleted.

- If XQAKILL is undefined or Zero (0), the Alert Handler deletes the alert for all recipients.
- If XQAKILL is set to 1, Alert Handler only purges the alert for the current user, as identified by DUZ (using a value of 1 only makes sense if the current user is a recipient of the alert, however).

If the software application identifier portion of the alert identifier is “NO-ID”, however, the alert is treated as if XQAKILL were set to 1 (that is the alert is deleted only from one user), regardless of how it is set.

Output: none.

## DELETEA^XQALERT: Clear Obsolete Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 10081

Description: The DELETEA^XQALERT API deletes (clears) all alerts with the same software application identifier, for the current user (XQAKILL=1) or all recipients (XQAKILL=0 or XQAKILL undefined). The current user (as identified by the value of DUZ) does *not* need to be a recipient of an alert; however, in that case, only a value of Zero (0 or undefined) for XQAKILL makes sense.

One example of the use of DELETEA^XQALERT is when a troublesome condition has been resolved. You can use this API to delete any unprocessed alerts associated with the condition. It deletes *all* alerts whose software application identifiers match the software application identifier you pass in the XQAID input variable (multiple alerts can potentially share the same software application identifier).

![](kernel-8-0-developer-s-guide-alerts-user-guide/010.png) REF: For more information on software application identifiers, see the “<u>Package Identifier or Alert Identifier</u>” section in this section.

Format: DELETEA^XQALERT

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
4.  Set all input variables.
5.  Call the API.

> Input Variables: XQAID: (required) All alerts whose software application identifier matches the value of this input parameter is deleted, for the alert recipients designated by the XQAKILL input variable.

> The form of XQAID can be exactly as initially set when creating the alert. Alternatively, it can contain the two additional semicolon pieces added by the Alert Handler (the full alert identifier). The two additional semicolon pieces are ignored, however; this API only requires the original software application identifier.

> If the alert identifier you specify is “NO-ID”, however, (the generic software application ID assigned to alerts with no original software application identifier), this API does *not* delete matching alerts.

XQAKILL: (optional) XQAKILL determines how the alert is deleted. If XQAKILL is:

- Undefined or Zero (0)—The Alert Handler deletes matching alerts for all recipients.
- Set to 1—Alert Handler deletes matching alerts for the current user, as identified by DUZ.

![](kernel-8-0-developer-s-guide-alerts-user-guide/011.png) NOTE: Using a value of 1 only makes sense if the current user is also a recipient of the alert, however.

Output: none.

## GETACT^XQALERT(): Return Alert Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 10081

Description: The GETACT^XQALERT API returns to the calling routine the required variables to act on a specific alert.

Format: GETACT^XQALERT(alertid)

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
6.  Set all input variables.
7.  Call the API.

Input Parameters:alertid: (required) This is the alert identifier in the ALERT TRACKING (#8992.1) file.

Output Variables: XQAID: This is the full alert identifier.

XQADATA: The XQADATA variable stores any software application-specific data string that was passed at the time the alert was generated.

XQAOPT: Indicates a *non*-menu type option on the user’s primary, secondary or common menu to be run if *not*NULL.

XQAROU: Indicates the routine or tag^routine to run when the alert is processed. It can have three values:

- NULL—A NULL value indicates no routine to be used (XQAOPT contains option name to be run).
- ^*\<space\>*—A value of ^\<space\> indicates that the alert is information only (no routine or option action involved).
- ^ROUTINE or TAG^ROUTINE—The name of the routine as ^ROUTINE or TAG^ROUTINE.

## PATIENT^XQALERT(): Get Alerts for a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 10081

Description: The PATIENT^XQALERT API allows you to return an array of all alerts for a particular patient that are either:

- Open.
- Within a given time range (both open and closed).

The association of an alert with a patient is based on the conventions used by the CPRS software application for the Package Identifier (original value of XQAID input variable when creating the alert), where the second comma-piece is a POINTER to the PATIENT (#2) file.

![](kernel-8-0-developer-s-guide-alerts-user-guide/012.png) REF: For information on CPRS conventions for the format of the Package Identifier, see the “<u>Package Identifier or Alert Identifier</u>” section.

Format: PATIENT^XQALERT(root,dfn\[,startdate\]\[,enddate\])

Input Parameters:root: (required) Fully resolved global or local reference in which to return a list of matching alerts.

dfn: (required) Internal entry number (DFN in the PATIENT \[#2\] file) of the patient for whom alerts are returned.

startdate: (optional) Starting date to check for alerts. If you pass this parameter, all alerts are returned, open or closed, from the startdate until the enddate (if no enddate is specified, all alerts beyond the startdate are returned). If you omit this parameter (and enddate), only currently open alerts are returned.

enddate: (optional) Ending date to check for alerts. If you omit this parameter, but pass a startdate, all alerts are returned beyond the startdate.

Output Parameters: root: All alerts matching the request are returned in the input parameter you specified in root, in the following format:

root=number of matching alerts

root(1)= "I "\_messagetext\_"^"\_alertid

root(2)=...

Where the first three characters are either:

- “I ”—If the alert is informational.
- “ ”—If the alert runs a routine.

In addition, where alertid (Alert Identifier) contains three semicolon-delimited pieces:

1.  The original software application identifier (value of XQAID).
6.  The DUZ of the alert creator.
7.  The VA FileMan date and time the alert was created.

## SETUP^XQALERT: Send Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 10081

Description: The SETUP^XQALERT API sends alerts to users; however, the *preferred* API to use is <u>\$\$SETUP1^XQALERT: Send Alerts</u>.

To send an information-only alert, make sure that XQAOPT and XQAROU input variables are *not* defined. To send an alert that takes an action, specify either the XQAOPT (to run an option) or XQAROU (to run a routine) input variables.

Format: SETUP^XQALERT

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
8.  Set all input variables.
9.  Call the API.

Input Variables: XQA: (required) Array defining at least one user to receive the alert. Subscript the array with users’ DUZ numbers to send to individual users; subscript the array with mail group names to send to users in mail groups:

\>S XQA(USERDUZ)=""

\>S XQA("G.MAILGROUP")=""XQAARCH: (optional) Number of days that alert tracking information for this alert should be retained in the ALERT TRACKING (#8992.1) file. Default period is 30 days. Users can specify a different number of days using this input variable. To retain information forever, a value of 100000 is *recommended* (good for proximately 220 years).

XQACNDEL: (optional) Setting a value in the XQACNDEL variable prior to calling this API causes the CAN DELETE WITHOUT PROCESSING (#.1) field in the ALERT (#8992) file to be set. A value in this field indicates that the alert can be deleted by the user without having processed it.

XQADATA: (optional) Use this to store a software application-specific data string, in any format. It is restored in the XQADATA input variable when the user processes the alert, and is therefore, available to the routine or option that processes the alert.

You can use any delimiter in the input variable, including the caret. You can use it to make data, such as patient number, lab accession, or cost center, available to your software application-specific routine or option without needing to query the user when they process the alert. It is up to your routine or option to know what format is used for data in this string.

XQAFLG: (optional) Alert flag to regulate processing (currently *not* supported). The values are:

- D—To delete an information-only alert after it has been processed (the default for information-only alerts).
- R—To run the alert action immediately upon invocation (the default for alerts that have associated alert actions).

This input variable currently has no effect, however.

XQAGUID: (optional) As of Kernel Patch XU\*8.0\*207, the GUID FOR GUI adds an interface GUID (a 32-character string containing hexadecimal digits in a specific format within curly braces) to permit a program on the client to process the alert. The presence of a GUID in the variable indicates that the alert can be processed within a GUI environment and opens the correct application to process the alert within the GUI environment.

![](kernel-8-0-developer-s-guide-alerts-user-guide/013.png) NOTE: This functionality has never been implemented by CPRS or other GUI applications.

XQAID: (optional) Package identifier for the alert, typically a software application namespace followed by a short character string. *Mustnot* contain carets (^) or semicolons (;). If you do *not* set XQAID, you are *not* able to identify the alert in the future, either during alert processing, to delete the alert, or to perform other actions with the alert.

![](kernel-8-0-developer-s-guide-alerts-user-guide/014.png) REF: For information on CPRS conventions for the format of the Package Identifier, see the “<u>Package Identifier or Alert Identifier</u>” section.

XQAMSG: (required) Contains the text of the alert:

- 80 characters can be displayed in the original alert.
- 70 characters can be displayed in the View Alert listing.
- The string *cannot* contain a caret (^).

XQAOPT: (optional) Name of a *non*-menu type option on the user’s primary, secondary or common menu. The phantom jump navigates to the destination option, checking pathway restrictions in so doing. An error results if the specified option is *not* in the user’s menu pathway.

XQAROU: (optional) Indicates a routine or tag^routine to run when the alert is processed. If both XQAOPT and XQAROU are defined, XQAOPT is used and XQAROU is ignored.

XQASUPV: (optional) Number of days to wait before Delete Old (\>14d) Alerts \[XQALERT DELETE OLD\] option forwards alert to recipient’s supervisor based on Service/Section, if alert is unprocessed by recipient. Can be a number from 1 to 30.

XQASURO: (optional) Number of days to wait before Delete Old (\>14d) Alerts \[XQALERT DELETE OLD\] option forwards alert to recipient’s MailMan surrogates (if any), if alert is unprocessed by recipient. Can be a number from 1 to 30.

XQATEXT: (optional) Released with Kernel Patch XU\*8.0\*207, this variable permits informational text of any length to be passed with an alert. When the alert is selected, the contents of this variable is displayed in a ScreenMan form within the roll and scroll environment.

![](kernel-8-0-developer-s-guide-alerts-user-guide/015.png) NOTE: It was also intended to be displayed within a text display box within the GUI environment. However, CPRS has never implemented this functionality, so it can only be viewed in the roll and scroll environment.

Output: none.

### Details—When the Alert is Processed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the alert is created, the user is then able to receive and process the alert from their View Alerts listing. When this occurs, Alert Handler executes the following four steps for the alert:

1.  Alert Handler sets up the following input variables:
- XQADATA—If originally set when alert was created.
- XQAID—If originally set when alert was created.
- XQAKILL—The purge indicator. It is always set to 1 by the Alert Handler.

If you associated a software application identifier, XQAID, with the alert, it is restored along with two additional semicolon pieces:

- Current user number.
- Current DATE/TIME.

With the two additional semicolon pieces, the software application identifier becomes the alert identifier. If you did *not* define XQAID when creating the alert, Alert Handler sets XQAID input variable to “NO-ID” followed by the two additional semicolon pieces.

2.  Alert Handler runs the routine, or any option specified in the XQAOPT or XQAROU input variables.
3.  You can refer to the three input variables listed above (that is XQADATA, XQAID, and XQAKILL) in the option or routine that processes the alert.
4.  Once the routine or option finishes, Alert Handler deletes the alert, under the following conditions:
- If XQAKILL remains at the value of 1 as it was set in Step 1, the alert is deleted for the current user only.
- To prevent the alert from being deleted, KILL XQAKILL during Step 2 above. You may *not* want the alert to be deleted if processing, such as entering an electronic signature, was *not* completed.
- To delete the alert for all recipients of the alert, *not* just the current user, SET XQAKILL to Zero (0) during Step 2. When XQAKILL is set to 0, Alert Handler searches for any alerts with a matching Alert Identifier, all three semicolon pieces:
  - Original Package Identifier.
  - Alert sender.
  - DATE/TIME the alert was sent.

It purges them so that other users need *not* be notified of an obsolete alert.

![](kernel-8-0-developer-s-guide-alerts-user-guide/016.png) NOTE: To delete an alert for all recipients, you *must* define XQAID with appropriate specificity when creating the alert.

5.  Finally, the Alert Handler cleans up by KILLing XQADATA, XQAID, and XQAKILL. Alert Handler returns the user to the View Alerts listing if pending alerts remain. Otherwise, Alert Handler returns the user to their last menu prompt.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200269956" class="anchor"></span>Figure 14: SETUP^XQALERT API—Example: Call to Send an Alert Sample

;send an alert

;assume DFN is for patient XUPATIENT,ONE

N XQA,XQAARCH,XQADATA,XQAFLG,XQAGUID,XQAID,XQAMSG,XQAOPT,XQAROU,XQASUPV,XQASURO,  
XQATEXT,XQALERR

S XQA(161)="" ; recipient is user \`161

S XQAMSG="Elevated CEA for "\_\$\$GET1^DIQ(2,DFN\_",",.01)\_" ("\_\$E(\$\$GET1^DIQ(2,DFN\_",",9),6,9)\_") Schedule follow-up exam in Surgical Clinic."

D SETUP^XQALERT

Q

<span id="_Toc200269957" class="anchor"></span>Figure 15: SETUP^XQALERT API—Example: Resulting Alert, from View Alerts Option

Select Systems Manager Menu Option: <span class="mark">"VA</span>

1.I Elevated CEA for XUPATIENT,ONE (5345). Schedule follow-up exam in Surgical Clinic.

Select from 1 to 1

or enter ?, A, I, P, M, R, or ^ to exit:

## \$\$SETUP1^XQALERT: Send Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 10081

Description: The \$\$SETUP1^XQALERT extrinsic function sends alerts to users. This is the *preferred* API rather than <u>SETUP^XQALERT: Send Alerts</u> API.

- To send an information-only alert, make sure that XQAOPT and XQAROU input variables are *not* defined.
- To send an alert that takes an action, specify either the XQAOPT (to run an option) or XQAROU (to run a routine) input variables.

Format: \$\$SETUP1^XQALERT

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
10. Set all input variables.
11. Call the API.

Input Variables: XQA: (required) Array defining at least one user to receive the alert. Subscript the array with users’ DUZ numbers to send to individual users; subscript the array with mail group names to send to users in mail groups:

\>S XQA(USERDUZ)=""

\>S XQA("G.MAILGROUP")=""XQAARCH: (optional) Number of days that alert tracking information for this alert should be retained in the ALERT TRACKING (#8992.1) file. Default period is 30 days. Users can specify a different number of days using this input variable.

![](kernel-8-0-developer-s-guide-alerts-user-guide/017.png) NOTE: Critical patient data, as part of medical records, should be retained for at least 65 years, which is 23,725 days. To retain information forever, a value of 100000 is *recommended* (good for about 273+ years). Sites may *not* have sufficient disk storage space to accommodate this need, however.

XQACNDEL: (optional) Setting a value in the XQACNDEL variable prior to calling this API causes the CAN DELETE WITHOUT PROCESSING (#.1) field in the ALERT (#8992) file to be set. A value in this field indicates that the alert can be deleted by the user *without* having processed it.

XQADATA: (optional) Use this variable to store a software application-specific data string, in any format. It is restored in the XQADATA input variable when the user processes the alert and is therefore available to the routine or option that processes the alert.

You can use any delimiter in the input variable, including the caret. You can use it to make data such as patient number, lab accession, or cost center available to your software application-specific routine or option without needing to query the user when they process the alert. It is up to your routine or option to know what format is used for data in this string.

XQAFLG: (optional) Alert flag to regulate processing (currently *not* supported). The values are:

- D—To delete an information-only alert after it has been processed (the default for information-only alerts).
- R—To run the alert action immediately upon invocation (the default for alerts that have associated alert actions).

This input variable currently has no effect, however.

XQAGUID: (optional) As of Kernel Patch XU\*8.0\*207, the GUID FOR GUI adds an interface GUID (a 32 character string containing hexadecimal digits in a specific format within curly braces) to permit a program on the client to process the alert. The presence of a GUID in the variable indicates that the alert can be processed within a GUI environment and opens the correct application to process the alert within the GUI environment.

![](kernel-8-0-developer-s-guide-alerts-user-guide/018.png) NOTE: Currently, this functionality has *not* been implemented by CPRS or other GUI applications.

XQAID: (optional) Package identifier for the alert; typically, a software application namespace followed by a short character string. *Must not* contain carets (^) or semicolons (;). If you do *not* set XQAID, you are *not* able to identify the alert in the future, either during alert processing, to delete the alert, or to perform other actions with the alert.

![](kernel-8-0-developer-s-guide-alerts-user-guide/019.png) REF: For information on CPRS conventions for the format of the Package Identifier, see the “<u>Package Identifier or Alert Identifier</u>” section.

XQAMSG: (required) Contains the text of the alert:

- 80 characters can be displayed in the original alert.
- 70 characters can be displayed in the View Alert listing.
- The string *cannot* contain a caret (^).

XQAOPT: (optional) Name of a *non*-menu type option on the user’s primary, secondary or common menu. The phantom jump navigates to the destination option, checking pathway restrictions in so doing. An error results if the specified option is *not* in the user’s menu pathway.

XQAREVUE: (optional) This variable sets the DAYS FOR BACKUP REVIEWER (#.15) field in the ALERTS (#8992) file. It *must* be an integer from 1 to 15.

XQAROU: (optional) Indicates a routine or tag^routine to run when the alert is processed. If both XQAOPT and XQAROU are defined, XQAOPT is used and XQAROU is ignored.

XQASUPV: (optional) Supervisor forwarding. Number of days to wait before Delete Old (\>14d) Alerts \[XQALERT DELETE OLD\] option forwards alert to recipient’s supervisor, if unprocessed by recipient. Can be a number from 1 to 30. Supervisor is determined from the recipient’s NEW PERSON (#200) file entry POINTER to the SERVICE/SECTION (#49) file, and then the entry (if any) in the pointed-to Service/Section’s CHIEF field.

XQASURO: (optional) Number of days to wait before Delete Old (\>14d) Alerts \[XQALERT DELETE OLD\] option forwards alert to recipient’s MailMan surrogates (if any), if alert is unprocessed by recipient. Can be a number from 1 to 30.

XQATEXT: (optional) Released with Kernel Patch XU\*8.0\*207, this variable permits informational text of any length to be passed with an alert. When the alert is selected, the contents of this variable are displayed in a ScreenMan form within the roll-and-scroll environment.

![](kernel-8-0-developer-s-guide-alerts-user-guide/020.png) NOTE: It was also intended to be displayed within a text display box within the GUI environment. Currently, CPRS has *not* implemented this functionality, so it can only be viewed in the roll-and-scroll environment.

Output: returns: Returns:

- 1—The alert was sent successfully.
- 0—The alert was *not* sent successfully, in which case the XQALERR variable contains a text string indicating the reason that the alert was *not* sent.

Output Variables:XQALERR: Returns:

- NULL—If the alert was sent successfully, this variable is NULL.
- Text String—If the alert was *not* sent successfully, this variable contains a text string that indicates the reason that the alert was *not* sent.

### Details—When the Alert is Processed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the alert is created, the user is then able to receive and process the alert from their View Alerts listing. When this occurs, Alert Handler executes the following four steps for the alert:

1.  <span id="Alert_Processing_Step_01" class="anchor"></span>Alert Handler sets up the following input variables:
- XQADATA—If originally set when alert was created.
- XQAID—If originally set when alert was created.
- XQAKILL—The purge indicator. It is always set to 1 by the Alert Handler.

If you associated a software application identifier, XQAID, with the alert, it is restored along with two additional semicolon pieces:

- Current user number.
- Current DATE/TIME.

With the two additional semicolon pieces, the software application identifier becomes the alert identifier. If you did *not* define XQAID when creating the alert, Alert Handler sets XQAID input variable to “NO-ID” followed by the two additional semicolon pieces.

12. <span id="Alert_Processing_Step_02" class="anchor"></span>Alert Handler runs the routine, or any option specified in the XQAOPT or XQAROU input variables.

You can refer to the three input variables listed above (that is XQADATA, XQAID, and XQAKILL) in the option or routine that processes the alert.

13. Once the routine or option finishes, Alert Handler deletes the alert, under the following conditions:
- If XQAKILL remains at the value of 1 as it was set in [Step 1](#Alert_Processing_Step_01), the alert is deleted for the current user only.
- To prevent the alert from being deleted, KILL XQAKILL during [Step 2](#Alert_Processing_Step_02). You may *not* want the alert to be deleted if processing, such as entering an electronic signature, was *not* completed.
- To delete the alert for all recipients of the alert, *not* just the current user, set XQAKILL to Zero (0) during [Step 2](#Alert_Processing_Step_02). When XQAKILL is set to 0, Alert Handler searches for any alerts with a matching Alert Identifier, all three semicolon pieces:
- Original Package Identifier.
- Alert sender.
- DATE/TIME the alert was sent.

It purges them so that other users need *not* be notified of an obsolete alert.

![](kernel-8-0-developer-s-guide-alerts-user-guide/021.png) NOTE: To delete an alert for all recipients, you *must* define XQAID with appropriate specificity when creating the alert.

14. Finally, the Alert Handler cleans up by KILLing XQADATA, XQAID, and XQAKILL. Alert Handler returns the user to the View Alerts listing if pending alerts remain. Otherwise, Alert Handler returns the user to their last menu prompt.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200269958" class="anchor"></span>Figure 16: \$\$SETUP1^XQALERT API—Example: Call to Send an Alert Sample

;send an alert

;assume DFN is for patient XUPATIENT,ONE

N XQA,XQAARCH,XQADATA,XQAFLG,XQAGUID,XQAID,XQAMSG,XQAOPT,XQAROU,XQASUPV,XQASURO,XQATEXT,XQALERR

S XQA(161)="" ; recipient is user \`161

S XQAMSG="Elevated CEA for "\_\$\$GET1^DIQ(2,DFN\_",",.01)\_" ("\_\$E(\$\$GET1^DIQ(2,DFN\_",",9),6,9)\_") Schedule follow-up exam in Surgical Clinic."

S VAR=\$\$SETUP1^XQALERT I 'XQALERR W !,"ERROR IN ALERT: ",XQALERR

Q

<span id="_Toc200269959" class="anchor"></span>Figure 17: \$\$SETUP1^XQALERT API—Example: Resulting Alert, from View Alerts Option

Select Systems Manager Menu Option: <span class="mark">"VA</span>

1.I Elevated CEA for XUPATIENT,ONE (5345). Schedule follow-up exam in Surgical Clinic.

Select from 1 to 1

or enter ?, A, I, P, M, R, or ^ to exit:

## USER^XQALERT(): Get Alerts for a User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 10081

Description: The USER^XQALERT API returns a list of alerts for a given user. You can return a list of all alerts for a particular user that are either:

- Open.
- Within a given time range (open and closed).

Format: USER^XQALERT(root\[,duz\]\[,startdate\]\[,enddate\])

Input Parameters: root: (required) Fully resolved global or local reference in which to return a list of matching alerts.

duz: (optional) DUZ number of the user for whom the alert list is returned. If you do *not* pass a number, it uses the current user’s DUZ.

startdate: (optional) Starting date to check for alerts. If you pass this parameter, all alerts are returned, open or closed, from the startdate until the enddate (if no enddate is specified, all alerts beyond the startdate are returned). If you omit the startdate parameter (and enddate), only currently open alerts are returned.

enddate: (optional) Ending date to check for alerts. If you omit this parameter, but pass a startdate, all alerts are returned beyond the startdate.

Output Parameters: root: All alerts matching the request are returned in the input parameter you specified in root, in the following format:

root=number of matching alerts

root(1)= "I "\_messagetext\_"^"\_alertid

root(2)=...

Where the first three characters are either:

- “I ”: If the alert is informational
- “ ”: If the alert runs a routine

In addition, where alertid (Alert Identifier) contains three semicolon-delimited pieces:

1.  The original software application identifier (value of XQAID).
8.  The DUZ of the alert creator.
9.  The VA FileMan date and time the alert was created.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950527" class="anchor"></span>Figure 18: USER^XQALERT API—Example

\><span class="mark">D USER^XQALERT("ZZALRT",ZZDUZ,2900101)</span>

\><span class="mark">ZW ZZALRT</span>

ZZALRT=1

ZZLART(1)="I Test Message^NO-ID;92;2940729.10312"

## FORWARD^XQALFWD(): Forward Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3009

Description: The FORWARD^XQALFWD API can be used to forward alerts (in most cases, for the current user only). It is a silent (no screen input or output) API, so it can be used for windowed applications.

Format: FORWARD^XQALFWD(\[.\]alerts,\[.\]users,type\[,comment\])

Input Parameters: \[.\]alerts: (required) Array of alerts to be forwarded, each identified by its full alert identifier (the value of the ALERT ID \[#8992.01,.02\] field in the ALERT DATE/TIME \[#8992.01,.01\] Multiple field of the current user’s entry in the ALERT \[#8992\] file). Use the <u>\$\$SETUP1^XQALERT: Send Alerts</u> API to obtain alert identifiers for a user’s current open alerts.

If only a single alert is to be forwarded, only the top node *must* be set (set it to the alert identifier of the alert to forward and pass by value). If there are multiple alerts to forward, the value of each entry in the array should be one of the desired alert identifier. For example:

A6AALRT(1)="NO-ID;92;2941215.100432"

A6AALRT(2)="NO-ID;161;2941220.111907"

A6AALRT(3)="NO-ID;161;2941220.132401"

If using an array, the array *must* be passed by reference in the parameter list.

\[.\]users: (required) Users to forward alert to. For forwarding as an alert or as a mail message (when the type parameter is A or M), the input parameter can specify one or more users, and/or mail groups. For users, specify by IEN (in the NEW PERSON \[#200\] file). You do *not* need to precede the user’s IEN with a grave accent (\`). For mail groups, specify in format G.MAILGROUP.

If there is only a single user or mail group, just set the top node of the array to that value and pass it by value. If there are multiple values to be passed, pass them as the values of numerically subscripted array nodes (and pass the array by reference). For example:

A6AUSER(1)="G.MAS CLERKS"

A6AUSER(2)="G.MAS OVERNIGHT"

For forwarding to a printer (when the type parameter is P), there should be only a single value specifying the desired entry in the DEVICE (#3.5) file. You can specify the device either by name or by Internal Entry Number (IEN). If specifying by IEN, precede the IEN with an accent grave (such as \`202).

type: (required) Indicates the method of forwarding desired. The options are the single characters:

- A—Forward as an Alert.
- M—Forward as a Mail Message.
- P—Print a copy of the alert.

If the value passed is *not*A, M, or P, then no action is taken.

comment: (optional) A character string to use as a comment to accompany the alert when it is forwarded.

Output: none.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200269960" class="anchor"></span>Figure 19: FORWARD^XQALFWD API—Example

; get open alerts for current user

K A6AALRT D USER^XQALERT("A6AALRT")

;

I +A6AALRT D ; if any current alerts...

.; loop through A6AALRT array, parse alert id for each open alert

.K A6AALRT1 S A6ASUB="",A6AI=0

.F S A6ASUB=\$O(A6AALRT(A6ASUB)) Q:'\$L(A6ASUB) D

..S A6AI=A6AI+1,A6AALRT1(A6AI)=\$P(A6AALRT(A6ASUB),"^",2)

.;

.;forward open alerts of current user to MAS CLERKS mail group

.K A6AUSER S A6AUSER="G.MAS CLERKS"

.D FORWARD^XQALFWD(.A6AALRT1,A6AUSER,"A","Forwarded Alert")

Q

## \$\$CURRSURO^XQALSURO(): Get Current Surrogate for Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 2790

Description: The \$\$CURRSURO^XQALSURO extrinsic function obtains the current surrogate for alerts (if any) for the user with DUZ specified by the xqauser input parameter.

Format: \$\$CURRSURO^XQALSURO(xqauser)

Input Parameters: xqauser: (required) This is the Internal Entry Number (IEN, DUZ value) in the NEW PERSON (#200) file for the specified user with the surrogate.

Output: returns: Returns:

- DUZ—Internal Entry Number (IEN) of the surrogate.
- -1—If there is no surrogate specified.

## \$\$GETSURO^XQALSURO(): Get Current Surrogate Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3213

Description: The \$\$GETSURO^XQALSURO extrinsic function returns the following string of information on the current surrogate for the user with XQAUSER as his or her Internal Entry Number (IEN) in the NEW PERSON (#200) file:

ien^NAME^FM_STARTDATE^FM_ENDDATE

If there is no surrogate, the result is:

^^^

If either of the start or end dates and times is *not* specified, a NULL value is returned for that piece of the return string.

![](kernel-8-0-developer-s-guide-alerts-user-guide/022.png) REF: For a description of each piece of information separated by the caret (^), see the “Output” section below.

Format: \$\$GETSURO^XQALSURO(xqauser)

Input Parameters: xqauser: (required) This is the Internal Entry Number (IEN) in the NEW PERSON (#200) file of the user for whom the alert surrogate information is to be returned.

Output: returns: Returns the following string of information, each piece separated by a caret (^):

IEN^NAME^FM_STARTDATE^FM_ENDDATE

- IEN—Internal Entry Number (IEN) of the SURROGATE in the NEW PERSON (#200) file.
- NAME—Contents of the .01 field for the SURROGATE.
- FM_STARTDATE—Starting DATE/TIME for the SURROGATE in internal VA FileMan format.
- FM_ENDDATE—Ending DATE/TIME for the SURROGATE in internal VA FileMan format.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950529" class="anchor"></span>Figure 20: \$\$GETSURO^XQALSURO API—Example

\><span class="mark">S X=\$\$GETSURO^XQALSURO(124)</span>

\><span class="mark">W X</span>

2327^XUUSER,FOUR^3000929.1630^3001006.0800

This indicates that user \#2327 (FOUR XUUSER) becomes active as surrogate at 4:30 PM 9/29/00 and remains surrogate until 8:00 am on 10/06/00.

## REMVSURO^XQALSURO(): Remove Surrogates for Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 2790

Description: The REMVSURO^XQALSURO API removes any surrogates for alerts for the specified user.

Format: REMVSURO^XQALSURO(xqauser\[,.xqalsuro\]\[,.xqalstrt\])

Input Parameters: xqauser: (required) This is the Internal Entry Number (IEN, DUZ value) in the NEW PERSON (#200) file for the specified user.

xqalsuro: (optional) IEN of user in the NEW PERSON (#200) file. If passed, only the user who is passed is removed from the list of surrogates. If *not* passed, only the current surrogate is removed (if any).

xqalstrt: (optional) If passed, the surrogate is removed only from the start date indicated. If it is *not* passed, the surrogate is removed starting from the date of the current surrogate (if any). If there is no current surrogate, no entries are removed.

Output: none.

## SETSURO1^XQALSURO(): Establish a Surrogate for Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3213

Description: The SETSURO1^XQALSURO API establishes a surrogate for alerts. It should be used instead of the (obsolete) SETSURO^XQALSURO API. The SETSURO1^XQALSURO API also tests for cyclic relationships (such that the user eventually would become the surrogate). SETSURO1 does these tests, and therefore, has the possibility of failure. It returns either of the following values:

- IEN (value \> 0; True)—Surrogate was created successfully.
- Text String (False)—Text explaining why the surrogate was *not* created.

Previously, the (obsolete) SETSURO^XQALSURO API returned no value and, as long as both a user and surrogate were specified, would simply store the values. This left open the possibility that the user was specified as the surrogate or that a chain of surrogates ended up pointing again at the user; cases that could result in a very tight, *non*-ending, loop being generated if an alert was sent. These possibilities have been tested for in the interactive specification of surrogates and is tested for *non*-interactive usage in the SETSURO1^XQALSURO API.

![](kernel-8-0-developer-s-guide-alerts-user-guide/023.png) NOTE: The SETSURO1^XQALSURO API should be used instead of the (obsoelte) SETSURO^XQALSURO API (that is ICR \#2790).

Format: SETSURO1^XQALSURO(xqauser,xqalsuro\[,xqalstrt\]\[,xqalend\])

Input Parameters: xqauser: (required) User’s DUZ number (that is Internal Entry Number in the NEW PERSON \[#200\] file) for which the surrogate should act in receiving alerts.

xqalsuro: (required) Surrogate’s DUZ number (that is Internal Entry Number in the NEW PERSON \[#200\] file) for the user who receives and processes alerts for xqauser.

xqalstrt: (optional) The start DATE/TIME or the surrogate activity, in VA FileMan internal format. If the start DATE/TIME is *not* specified, the surrogate relationship begins immediately.

xqalend: (optional) The end DATE/TIME for the end of the surrogate relationship, in VA FileMan internal format. If the end DATE/TIME is *not* specified, the surrogate remains active until another surrogate is specified or the surrogate is deleted.

Output: returns: Returns:

- IEN (value \> 0; True)—Surrogate was created successfully.
- Text String (False)—Text explaining why the surrogate was *not* created.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950530" class="anchor"></span>Figure 21: SETSURO1^XQALSURO—Example

\>S XQAUSER=DUZ

\>S XQASURRO=45

\>S XQASTART=3001004.1630

\>S XQAEND=3001008.1630

\>S X=\$\$SETSURO1^XQALSURO(XQAUSER,XQASURRO,XQASTART,XQAEND)

\>I 'X W !,"Could not activate surrogate",!,?5,X Q

## SUROFOR^XQALSURO(): Return a Surrogate’s List of Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3213

Description: The SUROFOR^XQALSURO API returns a list of users for which the user, as defined by the xqauser input parameter, is acting as a surrogate.

Format: SUROFOR^XQALSURO(.xqalist.xqauser)

Input Parameters: .xqalist: (required) Passed by reference; it contains the name of the output array.

xqauser: (required) This is the Internal Entry Number (IEN, DUZ value) in the NEW PERSON (#200) file for the specified user.

Output: .xqalist: The output contains the list of users for whom the specified user is currently acting as a surrogate. The data in the list includes the:

- User’s internal entry number (DUZ).
- User’s name.
- Start and end dates for the surrogate period.

> Set to a number equal to the count of the total number of surrogates returned in the list:

XQALIST(*n*)

> Where *n* is a sequential integer starting with 1. Each entry in the array contains:

IEN^Name^Start Date/Time^End Date/Time

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950531" class="anchor"></span>Figure 22: SUROFOR^XQALSURO API—Example

\><span class="mark">S XQAUSER=DUZ</span>

\><span class="mark">D SUROFOR^XQALSURO(XQAUSER,.USERLIST)</span>

Returns:

<span id="_Toc199950532" class="anchor"></span>Figure 23: SUROFOR^XQALSURO API—Example: Returns

USERLIST=count

USERLIST(1)=IEN2^NEWPERSON,USER2^STARTDATETIME^ENDDATETIME

USERLIST(2)=3^NAME,USER3^3050407.1227^3050406

\><span class="mark">ZW USERLIST</span>

OUTPUT=2

OUTPUT(1)="5206652^PERSON,FIRST^3071113.141547^3071113.142"

OUTPUT(2)="5206656^PERSON,SECOND^3071114^3071114.08"

## SUROLIST^XQALSURO(): List Surrogates for a User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Alerts

ICR \#: 3213

Description: The SUROLIST^XQALSURO API returns a list of current or future surrogates for the user that is defined by the xqauser input parameter. It also sets the following surrogate fields in the ALERT (#8992) file if there is a current surrogate for this user:

- SURROGATE FOR ALERTS (#.02)
- SURROGATE START DATE/TIME (#.03)
- SURROGATE END DATE/TIME (#.04)

Format: SUROLIST^XQALSURO(xqauser,.xqalist)

Input Parameters: xqauser: (required) This is the Internal Entry Number (IEN, DUZ value) in the NEW PERSON (#200) file for the specified user.

xqalist: (required) Passed by reference; it contains the name of the output array.

Output: xqalist: The output contains the list of current and future surrogates for the specified user. The data in the list includes the following:

- User’s internal entry number (DUZ).
- User’s name.
- Start and end dates for the surrogate period.

> Set to a number equal to the count of the total number of surrogates returned in the list:

XQALIST(*n*)

> Where *n* is a sequential integer starting with 1. Each entry in the array contains:

IEN^Name^Start Date/Time^End Date/Time

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950533" class="anchor"></span>Figure 24: SUROLIST^XQALSURO API—Example

\><span class="mark">D SUROLIST^XQALSURO(duz,.output)</span>

\><span class="mark">ZW OUTPUT</span>

OUTPUT=2

OUTPUT(1)="5206652^PERSON,FIRST^3071113.141547^3071113.142"

OUTPUT(2)="5206656^PERSON,SECOND^3071114^3071114.08"

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-alerts-user-guide/024.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-alerts-user-guide/025.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-alerts-user-guide/026.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.