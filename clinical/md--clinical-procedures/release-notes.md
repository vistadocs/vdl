---
consolidated_title: "release notes"
app_code: MD
doc_type: RN
master_source: "MD*1*23 Release Notes (CP Flowsheets)"
master_pub_date: February 2012
consolidated_from: 3 versions
prior_versions:
  - "MD*1*12 Release Notes  (CP Flowsheets)"
  - "MD*1*16 Release Notes (CP Flowsheets)"
---

> ![](md-1-23-release-notes-cp-flowsheets/001.png)

> CLINICAL PROCEDURES (CP) V2.0 FLOWSHEETS MODULE

> RELEASE NOTES

> MD\*1.0\*23

> February 2012

> Department of Veterans Affairs Office of Information & Technology (OI&T)

> Product Development (PD)

> Revision History

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 24%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><strong>Date</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Initial version of MD*1.0*23 release notes</p>
</blockquote></td>
<td>November 2011</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Added IV dose rate content to Implementation Considerations-</p>
<p>Installation section</p>
</blockquote></td>
<td>February 2012</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> *This page intentionally left blank for double-sided printing.*

> ii Clinical Procedures (CP) V2.0 Flowsheets Module February 2012 (MD\*1.0\*23) Release Notes

> *This page intentionally left blank for double-sided printing.*

# Release Notes for Patch MD\*1.0\*23


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes for Patch MD\1.0\23](#release-notes-for-patch-md1023)
  - [Overview](#overview)
- [Patch MD\1.0\23 Features](#patch-md1023-features)
- [Implementation Considerations](#implementation-considerations)
  - [Installation](#installation)
  - [Validated Patient Monitoring Devices](#validated-patient-monitoring-devices)
  - [Additional Medical Monitoring Devices](#additional-medical-monitoring-devices)
> Patch MD\*1.0\*23 releases fixes and updates to the CP Flowsheet and CP Console applications that were initially released as part of MD\*1.0\*16.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MD\*1.0\*23 releases fixes and updates to CP Flowsheets and CP Console. See below for an individual list of fixes released.

# Patch MD\*1.0\*23 Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 41%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Identifier</strong></th>
<th><strong>Description</strong></th>
<th><blockquote>
<p><strong>Fix</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CQ680</td>
<td>General changes to permissions/access privileges</td>
<td><ol type="1">
<li><p>Instead of hiding the HL7 Tab in Flowsheets if the user does not have the CP HL7 MANAGER Key, the HL7 tab will be visible on an ongoing basis. However, the buttons to match a message to either a device or a patient will be disabled unless the user has HL7 MANAGER Key.</p></li>
<li><p>In CP Console, user will need permission (via Vista’s XPAR EDIT PARAMETER - utility) for folder’s visibility. So, user can have access to various folders (VIEW, FS, SHIFT, TOTALS folders).</p></li>
<li><p>Locking the Import/Export functionality. We will be locking Import/Export of Views, Procedures, and Instruments to be based on folder’s permission that is controlled by XPar. So, you will have ONLY access to Import/Export folders you have permission to. Example, if you have only access to Views and Procedures, you won’t be able to import/export Instruments.</p></li>
<li><p>MD ADMIN access will remain as in V1, where s/he will have access to all functionality (ex import/exports), and ability to see edit folders, views….</p></li>
</ol></td>
</tr>
<tr class="even">
<td>CQ720</td>
<td>Easier way to spot inactive terms</td>
<td><blockquote>
<p>All inactive terms now have a *</p>
<p>postpended to the term name in CP</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 41%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Identifier</strong></th>
<th><strong>Description</strong></th>
<th><blockquote>
<p><strong>Fix</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Console</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DM19.12</td>
<td><p>When starting a supplemental view, have it default to that view upon final</p>
<p>steps of opening process</p></td>
<td><blockquote>
<p>Fixed as described.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>ADT</p>
<p>Retransmit</p></td>
<td>Ability for clinicians to re-transmit ADT feed (A08) to medical devices (inpatient or outpatient settings) without having to manually enter patient info on the device.</td>
<td><blockquote>
<p>Modified CP Flowsheets. If the patient is an inpatient, a new menu option will appear in the CP Flowsheets “File”</p>
<p>menu: “Resend Last Message to</p>
<p>Monitor”. If the Patient is an outpatient, a new menu option will appear in the CP Flowsheets “File” menu: “Send PII to Monitor”, along with a list of monitors</p>
<p>that support A08 messages.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CQ580</td>
<td>General Comment not shown on screens or reports</td>
<td><blockquote>
<p>Per SME agreement, we are removing this field in P23 and have tabled it for more analysis.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CQ681</td>
<td>Auto-Refresh was non-functional</td>
<td><blockquote>
<p>Fixed and enabled auto-refresh.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CQ705</td>
<td><p>The column headings in the data entry screen were not lining up with the</p>
<p>columns beneath</p></td>
<td><blockquote>
<p>Realigned column headings.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Terminology Update – Remedy ticket 496628</td>
<td>Improve the interoperability of the terminology conversion for units of measure</td>
<td><blockquote>
<p>The unit conversion for some observations do not convert equally due to a none existent measurement that is needed for the conversion. This causes an error in the Flowsheets reporting mechanism. This patch shall remove the unit from the observation. As a result, this will improve the interoperability of</p>
<p>the terminology conversion.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>NK</td>
<td><p>Enable official support for Nihon-</p>
<p>Koden devices</p></td>
<td><blockquote>
<p>Nihon-Koden devices are now officially</p>
<p>supported.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CQ711</td>
<td><p>Ability to Save changes to TIU Note</p>
<p>in CPConsole</p></td>
<td><blockquote>
<p>Fixed TIU note selection to ensure note</p>
<p>changes are saved.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CQ695</td>
<td><p>Space needed between title and date in</p>
<p>Report/TIU note</p></td>
<td><blockquote>
<p>Added space.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>CQ708 –</p>
<p>Remedy ticket 525716</p></td>
<td><p>Ability to see data entered in a Supplemental Page if the page</p>
<p>definition is changed to Optional in Flowsheet definition</p></td>
<td><blockquote>
<p>Modified Flowsheets to display the data. Note that changing view definitions</p>
<p>from Supplemental to Optional is still strongly discouraged.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CQ579</td>
<td>Remove location selection from TIU note, as location selected was not shown in TIU.</td>
<td><blockquote>
<p>Due to TIU business rules, sending a location has no effect unless/until a visit is created for the location prior to the note being generated. Adding visits to</p>
<p>TIU was beyond the scope of the patch,</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 41%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Identifier</strong></th>
<th><strong>Description</strong></th>
<th><blockquote>
<p><strong>Fix</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>so ability to select a location was</p>
<p>removed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>CQ715 –</p>
<p>Remedy Ticket 525716</p></td>
<td>The report tab in CP Flowsheets is not correctly filtering observations that were entered in a supplemental view.</td>
<td><blockquote>
<p>Filtering was enhanced to ensure that totals for each supplemental view were accurate.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CQ638</td>
<td>Add ability to show comments for an observation as a hint</td>
<td><blockquote>
<p>Due to Windows restrictions, adding a hint was not feasible. Instead, a status bar was added in each view between the title bar and the view grid which will show observation information and comments when an observation is</p>
<p>hovered over.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CQ712</td>
<td><p>Spell out qualifiers for Juice and Water. Currently, only the first letter (“J” or “W” show up in flowsheets or</p>
<p>TIU note)</p></td>
<td><blockquote>
<p>Corrected as part of the terminology update.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CQ713</td>
<td><p>Take out date/time as part of TIU Note</p>
<p>entry</p></td>
<td><blockquote>
<p>See fix for CQ579</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CQ714</td>
<td><p>Allow copy of procedures and</p>
<p>instruments in CP Console</p></td>
<td><blockquote>
<p>Fixed as described.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Remedy Ticket 554645</td>
<td>PSI – Location, Position, Method, and Product not being shown in Flowsheet view title bar</td>
<td><blockquote>
<p>Added Location, Position, Method, and Product to bottom left of title bar for supplemental views, as well as to the end of the title description (to ensure visibility to JAWS). REMOVED Location, Position, Method, and Product from Optional views, as their presence</p>
<p>can be misleading and confusing.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Implementation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To install patch MD\*1.0\*23, follow the *Clinical Procedures (CP) V1.0 Flowsheets Module Installation Guide* (distributed with patch MD\*1.0\*26) carefully. Although part of CP, CP Flowsheets is independent of CP User, CP Manager, CP Gateway, and CP Hemodialysis.

> ![](md-1-23-release-notes-cp-flowsheets/002.png) Vitals patches GMRV\*5.0\*22, GMRV\*5.0\*23, MD\*1.0\*21, MD\*1.0\*16, MD\*1.0\*26, and MD\*1.0\*12 must be installed prior to the installation of the MD\*1.0\*23 software. A test version of MD\*1.0\*12 is available from the same download site from which you received MD\*1.0\*23.

> ![](md-1-23-release-notes-cp-flowsheets/003.png) It is suggested that the output of the KIDS installation process be saved to a text file for distribution to CACs/Flowsheet administrators at the local site for review. The post

> install process will display a report of terms that were deactivated that are still being used in a flowsheet, allowing local staff to modify those views and flowsheets.

> ![](md-1-23-release-notes-cp-flowsheets/004.png) MD\*1.0\*23 includes *pre-install* routine MDPRE23 and *post-install* routine MDPOST23.

> Verify that these routines are complete before attempting to use CP Flowsheets.

> ![](md-1-23-release-notes-cp-flowsheets/005.png) The IV DOSE Rate observation is deactivated in MD\*1.0\*23 and replaced with a series of dosage/rate specific observations. Before you install MD\*1.0\*23, print reports covering the appropriate time span prior to installation if your site uses IV Dose Rate observations. After the patch is installed, please update observations and views based on need.

## Validated Patient Monitoring Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A supported device is one that has its data elements mapped to the standard terminology of the CliO database. The following devices are currently supported:

> ![](md-1-23-release-notes-cp-flowsheets/006.png)Intesys Clinical Suite (Spacelabs) PC1 (Spacelabs)

> PC2 (Spacelabs)

> Ultraview 1050 (Spacelabs)

> Ultraview 1600 (Spacelabs)

> Ultraview 1700 (Spacelabs) Ultraview SL2200 (Spacelabs) Ultraview SL2400 (Spacelabs) Ultraview SL2600 (Spacelabs) Ultraview SL2700 (Spacelabs) Ultraview SL2800 (Spacelabs) Ultraview SL3800 (Spacelabs) Nihon Koden

## Additional Medical Monitoring Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ICU devices will be added to the list of validated instruments as the devices are certified through the Hines Field Office.

> For sites that want to implement ICU devices, but do not have Clinical Procedures implemented, refer to the *Clinical Procedures (CP) V1.0 Flowsheets Module Implementation Guide*. You do not need to implement the legacy Clinical Procedures.

> For sites that use legacy Clinical Procedures and want to implement the CP Flowsheets patch, continue using the legacy CP modules and use CP Console to configure the ICU devices.

> Note: The CP Manager application is no longer supported after the installation of MD\*1.0\*16, which must be installed prior to the installation of MD\*1.0\*23. Use CP Console to perform the functions previously provided by CP Manager

> *This page intentionally left blank for double-sided printing.*

> .

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MD*1*16 Release Notes (CP Flowsheets)

## Interface with Third Party Monitoring Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MD\*1.0\*16 provides an interface for the collection of patient observational data from monitoring devices. The collected data is stored automatically in the appropriate VistA database(s).

## Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MD\*1.0\*16 provides standardized terminology with VA Unique Identifiers (VUIDs). This facilitates exporting CliO data to other VA systems that use standardized terminology.

## GUI Flowsheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets utilizes locally-customizable flowsheets to view, enter, and edit patient data entered manually or received via the CliO infrastructure. Ultimately, this application will provide the front-end for other clinical systems, such as the Renal Dialysis, and Intake and Output (I&O) packages.

## ADT HL7 Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets introduces an Admission Discharge and Transfer (ADT) Health Level 7 (HL7) message feed. The ADT feed monitors the admitted, discharged, and transferred events from the Patient Information Management System (PIMS) and notifies interested patient medical monitoring devices.

## Manual Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets allows you to manually enter data personally observed by clinical staff or collected by monitors that are not able to electronically send that information.

## Data to CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MD\*1.0\*16 is capable of publishing data to CPRS in two ways. Vitals observations entered into the CliO service architecture is directly viewable in Vitals/Vitals Lite in the Computerized Patient Record System (CPRS). All other observational data entered may be published in a Text Integration Utilities (TIU) note, which is then viewable in CPRS.

## GUI Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Console is a user-friendly GUI with which you can configure system parameters and patient medical monitoring devices, schedule background tasks and shifts, and design flowsheet templates to meet site-specific requirements.

## Background Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Console provides specific background tasks to purge and clean up the system with regard to processed flowsheet data and legacy CP studies.

## Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new CP Gateway Service is a service that allows patient monitoring devices to send observational data to VistA.

## List of Outstanding Anomalies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A Request for Concurrence to Release Software with Known Anomalies was submitted containing the following anomalies:

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 22%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Headline/Description</strong></th>
<th><strong>Severity</strong></th>
<th><strong>Priority</strong></th>
<th><strong>Application</strong></th>
<th><p><strong>Workaround/</strong></p>
<p><strong>Comments</strong></p></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CQ580</td>
<td>The general comment given when entering Flowsheet data (shown on same line as location) does not appear on any reports.</td>
<td>Low</td>
<td>Low</td>
<td>CP Flowsheet GUI</td>
<td>User will be advised via training not to use the comment field. Severity Level low determined via discussion of defect with stakeholders and test sites. The design was to document process flow and not actual measurements.</td>
<td><blockquote>
<p>Designated to patch 23</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CQ681</td>
<td>Auto Refresh not working.</td>
<td>Low</td>
<td>Low</td>
<td>CP Flowsheets GUI</td>
<td><p>Impact is minimal because there is no user setting to apply an auto refresh, so users are unaware of the option. Functionality taken away due to system constraints on other functionality and development time needed to analyze functionality further. Training and User</p>
<p>Manual reflect the use of the Manual.</p></td>
<td><blockquote>
<p>Designated to patch 23</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CQ705</td>
<td>Not all of the Column Headings match up with the selections in the Add Data screen of Flowsheets view</td>
<td>Low</td>
<td>Low</td>
<td>CP Flowsheets GUI</td>
<td><p>Impact is minimal as it is not always noticeable by everyone. Training will point out the anomaly. This is only one screen and the information for the column selections is very</p>
<p>distinguishable from one column to the next.</p></td>
<td><blockquote>
<p>Designated to patch 23</p>
</blockquote></td>
</tr>
</tbody>
</table>

### From: MD*1*12 Release Notes  (CP Flowsheets)

## Support HL7 ADT Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets introduced an Admission Discharge and Transfer (ADT) Health Level 7 (HL7) message feed. This ADT feed monitors the admitted, discharged, and transferred events from the Patient Information Management System (PIMS) and notifies interested patient medical monitoring devices via HL7 version 2.4 messages. Patch MD\*1.0\*12 provides HL7 messaging apparatus that eliminates CP Flowsheets’ dependency on VDEF. There are occasions during a PIMS ADT discharge/cancel discharge events when room/bed information is not provided. With the support of patch MD\*1.0\*12, CP Flowsheets will transmit ADT discharge (A03)/cancel discharge (A13) messages when those events are triggered by PIMS inpatient activity when there is no room/bed information supplied.

## Support Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Following the release of MD\*1.0\*12, users will enter a Remedy Ticket or contact the VA Service Desk (VASD) directly when a problem arises. Once a Remedy Ticket is logged to the appropriate Category Type and Item either by the site themselves or Tier 1 support(VASD), the appropriate team will receive a Remedy alert. The Tier 2 (Product Support) support specialist assigned to the ticket will contact the site to troubleshoot and resolve the problem. If unable to do so, the ticket is referred to the Tier 3 group MNT-CP or DEV-CP for technical assistance.

> Maintenance priority is a required field to be selected by Tier 2 upon referral. They include:

- Priority 1 – Patient Safety Adversely Affected
- Priority 2 – Logging Software Error, Functionality Essential
- Priority 3 – Systems/Resource Issue
- Priority 4 – Patient Personally Affected
- Priority 5 – Logging Software Error, Functionality Needed
- Priority 6 – Functionality called into question
- Priority 7 – External Database Interface Issue
- Priority 8 – Nuisance Problem, Work Around in Place
- Priority 9 – Miscellaneous/Housekeeping

> Any referred Remedy tickets will be returned to the Tier 2 support for closure by the release coordinator of the resolving patch or original support specialist if a patch is not involved.

> Clinical Procedures MD\*1.0\*12, Clinical Flowsheet, tickets will be received by the Clinical 3 Product Support Team (Clin3). The tickets will be logged under:

- Category: Application-Vista
- Type: Clinical Procedures 1.0
- Item: Clinical Flowsheets

> Product Support maintains four fully patched support accounts which includes the Clinical Procedures application and will be used by Clin3 to troubleshoot flowsheet issues in a non- production environment.

> *This page intentionally left blank for double-sided printing.*
