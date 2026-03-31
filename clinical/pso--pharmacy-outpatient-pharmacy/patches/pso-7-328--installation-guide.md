---
title: PSO*7*328 AudioCARE Renewal Release Notes and Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: AudioCARE Renewal Release Notes and Install Guide
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*328
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 1
description: This document provides set-up steps and installation instructions to activate the AudioRENEWAL™ Module within the AudioCARE® telephone refill system. The AudioRENEWAL Module was de-activated by all VA locations currently using renewal functionality on January16, 2009 to prevent a problem reported in
audience: 
keywords: 
  - renewal
  - order
  - strong
  - provider
  - message
  - audiorenewal
  - install
  - audiocare
  - request
  - patch
page_count: 0
word_count: 10789
section_count: 1
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p328_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p328_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

AudioCARE Renewal

PSO\*7\*328 and OR\*3\*336 & OR\*3\*349

Release Notes and Installation Guide

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/001.png)

February 2014

Veterans Health Information Technology

######### Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1/10/2011</td>
<td>All</td>
<td>OR*3*336</td>
<td>Initial document</td>
</tr>
<tr class="even">
<td>2/7/2014</td>
<td>4, 7, 15, 22, 32-49</td>
<td>OR*3*349</td>
<td>Added information about maintenance patch OR*3*349 and added “AudioRENEWAL in CPRS” section.</td>
</tr>
</tbody>
</table>

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
- [Introduction](#introduction)
- [Release Notes](#release-notes)
- [New Notification OP RX RENEWAL REQUEST](#new-notification-op-rx-renewal-request)
- [New General Parameter OR AUTORENEWAL USER](#new-general-parameter-or-autorenewal-user)
- [# New Mail Group AUTORENEWAL](#new-mail-group-autorenewal)
- [AudioRENEWAL Clinic Entry, Parameters, and Activation](#audiorenewal-clinic-entry-parameters-and-activation)
- [Installation Guide](#installation-guide)
- [Pre Installation – Retrieve VEXRX](#pre-installation-retrieve-vexrx)
- [Installation Procedure – OR\3\336](#installation-procedure-or3336)
- [Post Installation – Activate AudioRENEWAL](#post-installation-activate-audiorenewal)
Introduction [4](#introduction)
Release Notes [6](#release-notes)
New Notification OP RX RENEWAL REQUEST [7](#new-notification-op-rx-renewal-request)
New General Parameter OR AUTORENEWAL USER [11](#new-general-parameter-or-autorenewal-user)
New Mail Group AUTORENEWAL [13](#new-mail-group-autorenewal)
AudioRENEWAL Clinic Entry, Parameters, and Activation [17](#audiorenewal-clinic-entry-parameters-and-activation)
Installation Guide [25](#installation-guide)
Pre Installation – Retrieve VEXRX [25](#pre-installation-retrieve-vexrx)
Installation Procedure – OR\*3\*336 [27](#_Toc379892231)
Post Installation – Activate AudioRENEWAL [31](#post-installation-activate-audiorenewal)
AudioRENEWAL in CPRS [32](#_Toc379892233)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides set-up steps and installation instructions to activate the AudioRENEWAL™ Module within the AudioCARE® telephone refill system. The AudioRENEWAL Module was de-activated by all VA locations currently using renewal functionality on January16, 2009 to prevent a problem reported in PSPO \#1218.

Patch PSO\*7\*328 was released Jul. 21, 2010, with a compliance date of Aug. 21, 2010.

Patch OR\*3\*336 was released Jan. 10, 2011, with a compliance date of Feb. 7, 2011.

All sites are expected to install patch OR\*3\*336 to their production VistA system, even if they are not currently using the AudioCARE telephone refill system. For sites not using the AudioCARE telephone refill system the installation of patch OR\*3\*336 is all that needs to be done. For sites currently using the AudioCARE telephone refill system, everything in this Release Notes and Installation Guide is for you.

> **NOTE:** Patch OR\*3\*336 is a replacement patch for OR\*3\*290, which has been entered in error. If you installed OR\*3\*290 successfully, do not uninstall it. Whether you have installed OR\*3\*290 successfully or not, you will need to install OR\*3\*336. There is no replacement patch for PSO\*7\*328 or the

VEXRX routines.

This document has been updated to include information on patch OR\*3\*349, a maintenance patch that addressed the four renewal issues below, released in February, 2014:

> 1\. Add a description to the Parameter OR AUTORENEWAL USER.

> 2\. Use the OR AUTORENEWAL USER parameter value to populate the ENTERED

> BY (#16) field in the PRESCRIPTION (#52) file for AudioRENEWAL

> prescriptions.

> 3\. MailMan messages from AudioRENEWAL module are not displaying enough

> information to quickly take appropriate follow-up action. Additional information

> added:

1.  Message subject: RENEWAL REQUESTS WITH ORDER CHECKS
- Added patient identifier (first initial of last name and last 4 of SSN)
- Added the name of the Drug/Product ordered
2.  Message subject: RENEWAL REQUESTS NOT SENT TO PROVIDERS
- Added patient identifier (first initial of last name and last 4 of SSN)
- Added the name of the Drug/Product ordered
- Added the Provider Name (when applicable)

> 4\. The software that runs when pharmacy executes the option Process Telephone Refills

> has been modified.

> During this process, the current status of the ordering provider is checked. Before

> patch OR\*3\*349, when the provider status was either terminated or disusered, the

> renewal request would stop at this point and enter this record in the Mailman

> message RENEWAL REQUESTS NOT SENT TO PROVIDERS with the problem

> reported as “Provider flagged as Terminated”.

> Now, with patch OR\*3\*349, after the software determines the ordering provider’s

> status is either terminated or disusered, an additional check is made to see if the

> terminated provider has a designated surrogate. When an active surrogate is

> designated the renewal process will continue, creating the new unsigned renewal

> order which in turn generates the ORDER REQUIRES ELEC SIGNATURE

> notification which is distributed based on surrogacy and provider recipient codes set

> for this notification in the Notification Mgmt. Menus.

If no surrogate is assigned to terminate/disusered providers when renewals are

> processed, the result will be the same as before patch OR\*3\*349.

AudioCARE® applications and AudioRENEWAL™, AudioREFILL™, AudioRxINFO™ Modules are trademarks of AudioCARE Systems (ACS).

# Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AudioRENEWAL module will now use a standard CPRS Application Programming Interface (API) to perform the renewal. This new Class I interface has been written in such a way that other renewal systems will be able to utilize the same API in order to renew Outpatient prescriptions. Note, however, that other renewal systems have not been tested using this API.

In order to implement the Class I interface for the renewal process, modifications to the renewal code in the Class III AudioCARE routine VEXRX were necessary. The refill code of the VEXRX routine was not affected. Patch PSO\*7\*328 is an “information only” patch that provides instructions for obtaining the updated version of routine VEXRX.

The instructions in patch PSO\*7\*328 should be followed at sites using AudioCARE applications, even if they are not using the renewal functionality. The associated patch, OR\*3\*336, performs an environment check to confirm that the updated 'renewal' version of VEXRX has been retrieved and installed as instructed. If the previous 'renewal' version is detected the patch installation will abort.

Patch OR\*3\*336 installs the new API (RENEW), a new notification (OP RX RENEWAL REQUEST), a new mail group (AUTORENEWAL), and a new General Parameter (OR AUTORENEWAL USER). The refill portion of AudioCARE will not be affected. Complete the set-up for these new components after installing patch OR\*3\*336.

It is recommended that sites should install patch OR\*3\*336 in test accounts prior to installing the patch in a production account. It is not possible to test AudioRENEWAL in test accounts because the AudioCARE server is only available to production systems.

Do not install the routine VEXRX when the option to process telephone refills \[A3A PHONE REFILLS\] is in use. This option name may vary slightly between sites. Patch OR\*3\*336 may be installed with users on the system.

Each of the two patch installations take less than five minutes.

These installations do not change the functionality of CPRS or Outpatient Pharmacy applications.

An updated CPRS Technical Manual and CPRS GUI Technical Manual will be distributed with the release of these patches.

# New Notification OP RX RENEWAL REQUEST 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OR RX RENEWAL REQUEST notification, when enabled, triggers an information alert to the defined recipients when the renewal request is for a non-renewable drug. Sites using the AudioRENEWAL Module have several aspects to consider when determining how to use this notification in conjunction with the AudioRENEWAL user parameters. AudioRENEWAL user parameters reside on the AudioCARE server.

\*\*\*Note: Due to the INFORMATION ONLY type of this notification, the notification is removed after it is selected for processing and does not display any additional information or open the patients chart. Many VA locations may have set the AudioCARE AudioRENEWAL parameter Process Non-renewable to ‘N’ until this notification is converted to an action alert. The Notification can also be disabled in the OERR Notification system. Use of this functionality is not advised until this problem is resolved. Refer to PSPO \#2052. This problem is scheduled for resolution in a future version of CPRS GUI.

If the AudioRENEWAL parameter Process Non-renewable is set to 'Y' the patient receives the recorded message that the renewal request has been submitted. The request will list in the MailMan message with the subject line 'Renewal Requests not sent to Providers' with the detail of the message listing the patient's name, prescription number and the problem detail 'Drug not Renewable'. If the OP RX RENEWAL REQUEST Notification is <u>enabled</u> the site can use the 'Set Provider Recipients' values and designate who receives the notification. In this situation no renewal order is automatically created. Actually, the renewal processing is <u>never</u> allowed to automatically create a renewal order for a non-renewable drug.

If the AudioRENEWAL parameter Process Non-renewable is set to 'Y' the patient receives the recorded message that the renewal request has been submitted. The request will list in the MailMan message with the subject line 'Renewal Requests not sent to Providers' with the detail of the message listing the patient's name, prescription number and the problem detail 'Drug not Renewable'. If the OP RX RENEWAL REQUEST Notification is <u>disabled</u> the providers will <u>not</u> receive a notification. The idea would be to have a Pharmacist or a Pharmacy Technician monitoring the MailMan message for the non-renewable drug requests make the determination, per the facility business rules, to manually renew the prescription. This action would send the 'Order requires electronic signature' notification to the appropriate provider. The Provider would then determine if the renewed order should be signed or if other action is preferred (schedule/contact the patient).

If the AudioRENEWAL parameter Process Non-renewable is set to 'N' the patient receives the recorded message that the drug/prescription is not renewable and is instructed to contact the Provider or Pharmacy.

\*This can also be set up to be a phone transfer point (see Parameter section)

This notification is being released with the following default values:

- ORB ARCHIVE PERIOD - 30
- ORB DELETE MECHANISM - All Recipients
- ORB FORWARD BACKUP REVIEWER - No
- ORB FORWARD SUPERVISOR - No
- ORB FORWARD SURROGATES - No
- ORB PROCESSING FLAG - Disabled
- ORB PROVIDER RECIPIENTS - Ordering Provider, Attending, Primary and Teams
- ORB URGENCY – High

The three examples below demonstrate options when setting up the OP RX RENEWAL REQUEST notification. Each site needs to determine what settings are appropriate for their renewal notification. If your site elects to use this new notification, changes can be made for system, division, and other entities depending on how each parameter is defined. Notification parameter values for Package entities (Order Entry/Results Reporting) should never be modified.

1) Turn notification ON (Exported (Default) Value: ORB PROCESSING FLAG – Disabled.) This example shows enabling at the SYSTEM level.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: ORB NOT MGR MENU Notification Mgmt Menu</p>
<p>Select Notification Mgmt Menu Option: 1 Enable/Disable Notifications</p>
<blockquote>
<p>Set PROCESSING FLAG Parameters for Notifications</p>
</blockquote>
<p>Processing Flag may be set for the following:</p>
<p>1 User USR [choose from NEW PERSON]</p>
<p>2 Team (OE/RR) OTL [choose from OE/RR LIST]</p>
<p>3 Service SRV [choose from SERVICE/SECTION]</p>
<p>4 Location LOC [choose from HOSPITAL LOCATION]</p>
<p>5 Division DIV [choose from INSTITUTION]</p>
<p>6 System SYS [TEST.CHEYENNE.MED.VA.GOV]</p>
<p>7 Package PKG [ORDER ENTRY/RESULTS REPORTING]</p>
<p>Enter selection: 6 System TEST.CHEYENNE.MED.VA.GOV</p>
<p>---- Setting Processing Flag for System: TEST.CHEYENNE.MED.VA.GOV -------</p>
<p>Select Notification: OP RX RENEWAL REQUEST</p>
<p>Notification: OP RX RENEWAL REQUEST// OP RX RENEWAL REQUEST OP RX RENEWAL RE</p>
<p>QUEST</p>
<p>Value: Disabled// <strong>EN Enabled</strong></p>
<p>Select Notification:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2) Set Provider Recipients (Exported \[Default\] Value: ORB PROVIDER RECIPIENTS - Ordering Provider, Attending, Primary and Teams.) This example shows setting at the SYSTEM level.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Notification Mgmt Menu Option: 7 Set Provider Recipients for Notifications</p>
<p>Set PROVIDER RECIPIENTS Parameters for Notifications</p>
<p>Provider Recipients may be set for the following:</p>
<p>1 Division DIV [choose from INSTITUTION]</p>
<p>2 System SYS [TEST.CHEYENNE.MED.VA.GOV]</p>
<p>3 Package PKG [ORDER ENTRY/RESULTS REPORTING]</p>
<p>Enter selection: 2 System TEST.CHEYENNE.MED.VA.GOV</p>
<p>----- Setting Provider Recipients for System: TEST.CHEYENNE.MED.VA.GOV -----</p>
<p>Select Notification: OP RX RENEWAL REQUEST</p>
<p>Notification: OP RX RENEWAL REQUEST// OP RX RENEWAL REQUEST OP RX RENEWAL RE</p>
<p>QUEST</p>
<p>Value: OAPT// ?? <strong>OAPT is set when patch is installed</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Set of codes indicating default provider recipients of a notification by their title or relationship to the patient. Notifications can be set up with any or all of the following codes:

> P (Primary Provider): deliver notification to the patient's Primary Provider.

> A (Attending Physician): deliver notification to the patient's Attending Physician.

> T (Patient Care Teams): deliver notification to the patient's OE/RR Teams (personal

> patient and team lists are evaluated for potential recipients) and to devices on an

> OE/RR team.

> O (Ordering Provider): deliver notification to the provider who placed the order which

> trigger the notification.

> M (PCMM Team): deliver notification to users/providers linked to the patient via PCMM

> Team Position assignments.

> E (Entering User): deliver notification to the user/provider who entered the order's most

> recent activity.

> R (PCMM Primary Care Practitioner): deliver notification to the patient's PCMM

> Primary Care Practitioner.

> S (PCMM Associate Provider): deliver notification to the patient's PCMM Associate

> Provider.

> C (PCMM Mental Health Treatment Coordinator): deliver notification to the patient's

> PCMM Mental Health Treatment Coordinator.

> The providers, physicians and teams, must be set up properly and accurately for the correct individuals to receive the notification.

3) Set Default Recipient(s). This is an optional setting. A default user or team recipient will always receive OP RX RENEWAL REQUEST notifications for all patients, despite settings in the parameter ORB PROCESSING FLAG. This example shows enabling at the USER level.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Notification Mgmt Menu Option: 5 Set Default Recipient(s) for Notifications</p>
<p>Set REGULAR (DEFAULT) RECIPIENTS Parameters for Notifications</p>
<p>Notification Regular Recipients may be set for the following:</p>
<p>1 User USR [choose from NEW PERSON]</p>
<p>2 Team (OE/RR) OTL [choose from OE/RR LIST]</p>
<p>Enter selection: 1 User NEW PERSON</p>
<p>Select NEW PERSON NAME: CPRSPROVIDER,ONE PT 192 OI&amp;T STAFF</p>
<p>------ Setting Notification Regular Recipients for User: CPRSPROVIDER,ONE -----</p>
<p>Select Notification: op rx RENEWAL REQUEST</p>
<p>Notification: OP RX RENEWAL REQUEST// OP RX RENEWAL REQUEST OP RX RENEWAL REQUEST</p>
<p>Value: <strong>YES</strong>// ??</p>
<p>Default user or team recipients of a notification despite settings in the parameter ORB PROCESSING FLAG. These users/teams will always receive the notification, regardless of patient.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example Notifications:

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/002.png)

The patient in this example, CPRSPATIENT,ONE had three non-renewable prescriptions requested. Note that each prescription triggers an individual Informational alert.

The corresponding MailMan Message:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Subj: RENEWAL REQUESTS NOT SENT TO PROVIDERS [#166046] 06/15/13@19:06 8 lines</p>
<p>From: AUTO,RENEWAL In 'IN' basket. Page 1 *New*</p>
<p>-------------------------------------------------------------------------------</p>
<p>Renewal Requests Not Sent to Provider</p>
<p>PATIENT RX# DRUG</p>
<p>PROBLEM</p>
<p>==============================================================================</p>
<p>CPRSPATIENT,ONE (C9867) 12980442 MEPERIDINE INJ,SOLN</p>
<p>Drug not renewable</p>
<p>CPRSPATIENT,ONE (C9867) 12980443 DEXTROAMPHETAMINE TAB</p>
<p>Drug not renewable</p>
<p>CPRSPATIENT,ONE (C9867) 12980444 CODEINE SO4 TAB</p>
<p>Drug not renewable</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# New General Parameter OR AUTORENEWAL USER 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new parameter will allow sites to enter a proxy user value used by the auto renewal process which will populate the ‘entered by’ value in the ORDERS (#100) file, as well as the ‘entered by’ value in the PRESCRIPTION (#52) file. This is a one-time set up. Sites will need to create a proxy user to place in this new parameter. The use of a proxy user will allow providers to easily identify a renewal order generated by the AudioRENEWAL module as each of these orders will contain the same ‘entered by’ value for reference.

Sites may already have USER,AUDIOCARE PHONE set up for renewals. If not, set up the proxy user in the NEW PERSON (#200) file for filing renewal requests. For example: RENEWAL,AUTO. This entry does not need menu access or keys.

Example of the proxy user's name in the CPRS renewal order detail:

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/003.png)

Example of the proxy user's name in the pharmacy prescription detail:

> ![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/004.png)

Example of entering the proxy user in the OR AUTORENEWAL USER parameter:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: <strong>OR PARAM IRM MENU</strong> CPRS Configuration (IRM)</p>
<p>&lt;TEST ACCOUNT&gt; Order Check Expert System Main Menu ...</p>
<p>&lt;TEST ACCOUNT&gt; ORMTIME Main Menu ...</p>
<p>&lt;TEST ACCOUNT&gt; CPRS Clean-up Utilities ...</p>
<p>&lt;TEST ACCOUNT&gt; General Parameter Tools ...</p>
<p>&lt;TEST ACCOUNT&gt; HealtheVet Desktop Configuration ...</p>
<p>&lt;TEST ACCOUNT&gt; Remote Data Order Checking Parameters</p>
<p>Select CPRS Configuration (IRM) &lt;TEST ACCOUNT&gt; Option: <strong>GENeral Parameter Tools</strong></p>
<p>&lt;TEST ACCOUNT&gt; List Values for a Selected Parameter</p>
<p>&lt;TEST ACCOUNT&gt; List Values for a Selected Entity</p>
<p>&lt;TEST ACCOUNT&gt; List Values for a Selected Package</p>
<p>&lt;TEST ACCOUNT&gt; List Values for a Selected Template</p>
<p>&lt;TEST ACCOUNT&gt; Edit Parameter Values</p>
<p>&lt;TEST ACCOUNT&gt; Edit Parameter Values with Template</p>
<p>&lt;TEST ACCOUNT&gt; Edit Parameter Definition Keyword</p>
<p>Select General Parameter Tools &lt;TEST ACCOUNT&gt; Option: <strong>EP Edit Parameter Values</strong></p>
<p>--- Edit Parameter Values ---</p>
<p>Select PARAMETER DEFINITION NAME: <strong>OR AUTORENEWAL USER</strong> CPRS AUTO-RENEWAL USER DUZ</p>
<p>--- Setting OR AUTORENEWAL USER for System: TEST.CENTRAL-TEXAS.MED.VA.GOV ---</p>
<p>CPRS AUTO-RENEWAL USER ID: // <strong>RENEWAL, AUTO</strong> JW 119T PHARMACY</p>
<p>SERVICE</p>
<p>-------------------------------------------------------------------------------</p>
<p>Select PARAMETER DEFINITION NAME:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# # New Mail Group AUTORENEWAL 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3\*336 installs the new mail group AUTORENEWAL that reports information about prescription refills/renewal processing. Before the install of patch OR\*3\*336, pharmacy staff should identify the appropriate person to coordinate the membership for the mail group to the person that will be installing the patch. The patch cannot be installed without this information. After the installation of the patch, assign at least one user to the AUTORENEWAL mail group using the option Mail Group Edit (XMEDITMG). Any pharmacy user that executes the Process Telephone Refills (A3A PHONE REFILLS) option will receive the MailMan messages for that session. Members of the mail group will also receive the MailMan messages each time the option is executed. This mail group installs with 'self-enrollment' allowed.

Below is an example of the phone refill option by division:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: PROCESS TELEPHONE REFILLS A3A PHONE REFILLS</p>
<p>Looking for refill requests for inactive Outpatient divisions....none found.</p>
<p>Outpatient Pharmacy software - Version 7.0</p>
<p>Division: EVANSTON CBOC <strong>556GA</strong> <strong>specific division entered</strong></p>
<p>You are logged on under the EVANSTON CBOC division.</p>
<p>Select LABEL PRINTER: OPLBL// HFS IRM</p>
<p>HOST FILE NAME: NCH_HFS$:[TMP]TMP.DAT// ADDRESS/PARAMETERS: "NWS"//</p>
<p>OK to assume label alignment is correct? YES//</p>
<p>Bingo Board Display: OUTPATIENT//</p>
<p>Division: EVANSTON CBOC</p>
<p>Please answer the following for this session of prescriptions</p>
<p>FILL DATE: (11/12/2009 - 12/31/2699): TODAY// (MAY 11, 2010)</p>
<p>MAIL/WINDOW: MAIL// MAIL</p>
<p>Will these refills be Queued or Suspended ? S// USPENDED</p>
<p>Allow refills for inpatient ? N// O</p>
<p>Allow refills for CNH ? N// O</p>
<p>Process telephone refill requests at this time? YES//</p>
<p>Process telephone refills for all divisions? YES// <strong>NO only division 556GA</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The resulting MailMan Messages contain the division number 556GA. Note that the first two Messages listed (#167 and \#166) do not contain a division number. This is a result of answering the 'for all divisions' question YES.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>IN Basket, 22 messages (4-47), 1 new</p>
<p>*=New/!=Priority.......Subject.........................From..............</p>
<p>167. [165957] 05/13/10 RENEWAL REQUESTS NOT SENT TO 6 AUTO,RENEWAL</p>
<p>166. [165956] 05/13/10 REFILL TOTALS 5 AUTO,RENEWAL</p>
<p>165. [165955] 05/13/10 556 RENEWAL REQUESTS NOT SEN 7 AUTO,RENEWAL</p>
<p>164. [165954] 05/13/10 556 REFILL TOTALS 5 AUTO,RENEWAL</p>
<p>163. [165953] 05/13/10 556GA RENEWAL REQUESTS WITH 7 AUTO,RENEWAL</p>
<p>*162. [165952] 05/13/10 556GA REFILL TOTALS 5 AUTO,RENEWAL</p>
<p>161. [165951] 05/13/10 556 RENEWAL REQUESTS NOT SEN 7 AUTO,RENEWAL</p>
<p>160. [165950] 05/13/10 556 REFILL TOTALS 5 AUTO,RENEWAL</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

There are three potential mailman messages generated when the Process Telephone Refills option is initiated. These messages will be sent to the AUTORENEWAL mail group. No more than one of each subject type will generate for each division processed one or all three of these messages will be generated each time the Process Telephone Refills option is processed.

1) Subject: Renewal Requests Not Sent to Provider

There are multiple situations when a renewal request may not process. A VISTA mailman message will be generated titled Renewal Requests Not Sent to Provider. The message detail will contain the patient’s name and patient identifier (first initial of the last name and last 4 of the SSN), prescription number, name of the drug prescribed, and one of the problem reasons from the list below. When the problem involves provider information the name of the provider will be included.

- Failed DEA Check
- Chart Lock Failed
- Order lock Failed
- RX Status not Active or Expired
- Ordering Provider not Primary Care
- Provider NOT FOUND
- Provider flagged as TERMINATED
- Provider flagged as DISUSER
- Invalid Action – Details Below (i.e. This order may not be renewed.)
- No Auto-renewal User Defined
- No CPRS Order Number
- Order missing from ORDERS file
- Drug not renewable
- Clozapine Failed – details below
- Invalid Order number
- Problem with package in ORDERS file

Site personnel should review each message with this subject line and take the appropriate action based on the problem listed to ensure that patients either receive the requested medication or some other communication. (An unsigned renewal order <u>is not</u> created for prescriptions listed in this message.) At this point the last information to the patient was the recorded instruction that the renewal request had been submitted and the number of days they should allow before calling back to check the status.

Example of message:

| ![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/005.png) |
|-----------------------------------------------------------------------------------------------------|

2) Subject: Renewal Requests with Order Checks

The message detail will contain the patient’s name and patient identifier (first initial of the last name and last 4 of the SSN), prescription number, name of the drug prescribed, and the order check information. The orders checks that will be contained in the mail man message are limited to order checks triggered by the main ordering event 'Order dialog/display' by the special event 'Orders Renewed or Edited'.

- Estimated creatinine clearance if \< 50
- Order checking not available/supported
- Renal functions for patients over 65
- Polypharmacy

| ![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/006.png) |
|-----------------------------------------------------------------------------------------------------|

Site personnel should review this list considering the drug being renewed with the order check message listed. Combinations that could be clinically significant in the care of the patient should be reviewed in greater detail and/or communicated to the health care provider

3) Subject: Refill Totals

This message is generated each time the phone refill process is executed. The message detail contains the total counts processed.

- Refills Processed
- Refills not Processed
- Renewals Processed
- Renewals not Processed

| ![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/007.png) |
|-----------------------------------------------------------------------------------------------------|

# AudioRENEWAL Clinic Entry, Parameters, and Activation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RENEWAL function was deactivated due to a software problem in January 2009. Sites activating RENEWAL should consider what clinic updates may be needed as they prepare to re-activate RENEWAL (i.e. new clinics, inactivated clinics) after installing patch OR\*3\*336. This section explains how AudioRENEWAL clinic options function and how to make clinic updates on your AudioCARE server.

Actual screen displays, step order, and verbiage may vary depending on which version of AudioRENEWAL your site is using.

AudioRENEWAL should not be activated until after Clinic Entry type has been set up, parameters defined, and messages/transfer tables setup/reviewed.

Clinic Options

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/008.png)

The Clinic Entry option is used to control which clinics (IEN of record in file \#44 HOSPITAL LOCATION) will allow or not allow patients to request renewals with the AudioRENEWAL module. The control is achieved by entering the clinic IEN numbers on a list in the AudioRENEWAL module. There are two list types that can be used to restrict clinics, and one list type to allow all clinics to process renewals. The available list types are:

> "I" to define specific clinics to allow process renewal prescriptions (Include)

> "E" to define specific clinics not allowed to process renewal prescriptions (Exclude)

> "A" to allow all clinics to process renewal prescriptions (All)

Only the displayedList Type is 'in use' at any given time.

Select Clinic Entry. The following screen will display:

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/009.png)

It is very important at this point to note the 'List Type' value that displays (indicated by arrow above). The value displayed indicates which list type is currently 'in use' by your system. <u>Be careful to NOT change the value accidentally</u>.

How these lists work: As the AudioRENEWAL software processes the prescription number entered by the patient the clinic of the original prescription is checked against the 'in use' list.

<u>Example One</u>: Site Blue has selected list type ' I '. A renewable prescription originated in Site Blue's Clinic A. The patient calls in for a refill, there are no refills left so the renewal request is initiated. Clinic A is in the 'I' (Include) list so the renewal request processes.

<u>Example Two</u>: Site Blue has selected list type ' I '. A renewable prescription originated in Site Blue's Clinic B. The patient calls in for a refill, but as there are no refills left the renewal request is initiated. Clinic B is NOT in the 'I' (Include) list. The renewal is NOT allowed and the patient is given the recorded message that the clinic does not allow renewals; the patient should contact the physician.

\*A phone transfer point may also be set up (see Parameter section).

<u>Example Three</u>: Site Green has selected list type ' E '. A renewable prescription originated in Site Green's Clinic C. The patient calls in for a refill, there are no refills left so the renewal request is initiated. Clinic C is in the 'E' (Exclude) list. The renewal is NOT allowed and the patient is given the recorded message that the clinic does not allow renewals; the patient should contact the physician.

\*A phone transfer point may also be set up (see Parameter section).

<u>Example Four</u>: Site Green has selected list type ' E '. A renewable prescription originated in Site Green's Clinic D. The patient calls in for a refill, there are no refills left so the renewal request is initiated. Clinic D is NOT in the 'E' (Exclude) list so the renewal request processes.

<u>Example Five</u>: Site Yellow has selected list type ' A '. All renewable prescriptions for all Site Yellow Clinic's process with no clinic restrictions.

> **NOTE:** The clinic locations in the Hospital Location File (#44) should be reviewed and the , clinics that are approved and/or not approved for the renewal process should be identified by the facility. This information will determine how to set the List Type. In general, the 'in use' type of setting of Include or Exclude will be the 'shortest path' for manual clinic entry. The following examples demonstrate what is meant by the term 'shortest path'.

<u>Example One</u>: A site has 500 clinics, and 400 clinics are approved for the renewal process. The 'in use' list would be the ' E ' (Exclude) list and you would confirm that the 100 clinics NOT approved are on the ' E ' list.

<u>Example Two</u>: A site has 200 clinics, and 50 clinics are approved for the renewal process. The 'in use' list would be the ' I ' (Include) list and the site would confirm that the 50 approved clinics are on the ' I ' list.

<u>Example Three</u>: In this final example, a site would like to test the re-activation of the new RENEWAL software using a limited number of clinics. They have determined that the last 'in use' List Type is ' E ' (Exclude). In the future, when testing is complete, the 'shortest path' for manual clinic entry will be the ' E ' list. For the testing period they select the ' I ' list and add the specific clinics to be included in the test. They delete all other clinics from the ‘ I ‘ list (if any). They confirm that when Clinic Entry is selected the following screen displays with ' I ' in the List Type.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/010.png)

When they select F5=List (CTRL L if using telnet) only the clinics to be included in the test phase display in the ' I ' list. When the test phase ends, they will select Clinic Entry and enter ' E ' so the 'in use' list changes from the ' I ' Include list to the ' E ' Exclude list.

List MaintenanceNote: Maintenance of clinic entries should be done only on the list type currently displayed as 'in use'. Only one List Type can be 'in use' at any given time.

Select Clinic Entry to perform maintenance to the 'in use' list type. Clinic maintenance should be performed when caller activity is low. After selecting Clinic Entry the List Type displayed is the 'in use' list. Follow the guidelines below when making changes to your specific List Type:

<u>List Type " A "</u>

No maintenance necessary. All clinics will be allowed to process renewals.

<u>List Type " I "</u>  - Clinics entered and saved to this list will process renewals.

Include additional clinics:

- Enter the clinic IEN at the 'Clinic:' prompt and press \<enter\>
- If the system  prompts to delete the clinic select “No” (It's already on the list)
- Repeat the steps to add more clinics
- When finished entering new clinic IENs, press Ctrl-L or F5 to display the list to verify that the list is correct.
- Press F3 to file and save the updated list
- This clinic(s) will now be able to process renewals

Remove a listed clinic:

- Enter the clinic IEN at the 'Clinic:' prompt and press \<enter\>
- The clinic will display
- At the 'Delete' prompt arrow to 'Y' and press \<enter\>
- The message "Clinic removed" will display
- Repeat the steps to remove more clinics
- Press F3 to file and save the updated list
- This clinic(s) will no longer be able to process renewals

<u>List Type " E "</u> - Clinics entered and saved to this list will not process renewals.

Exclude additional clinics:

- Enter the clinic IEN at the 'Clinic:' prompt and press \<enter\>
- If the system  prompts to delete the clinic select “No” (\*This means it is already on the list)
- Repeat the steps to exclude more clinics
- When finished entering new clinic IENs, press Ctrl-L or F5 to display the list to verify that the list is correct.
- Press F3 to file and save the updated list
- This clinic(s) will no longer be able to process renewals

Remove a listed clinic:

- Enter the clinic IEN at the 'Clinic:' prompt and press \<enter\>
- At the 'Delete' prompt arrow to 'Y' and press \<enter\>
- The message "Clinic removed" will display
- Repeat the steps to remove more clinics
- Press F3 to file and save the updated list
- This clinic(s) will now be able to process renewals

> **NOTE:** A mailman message can be generated from the AudioCARE server and sent to the person responsible for clinic entry review.

AudioRENEWAL Parameters

Access the AudioRENEWAL module from the AudioCARE Systems Main Menu by selecting Application Modules and then selecting AudioRENEWAL. The following screen will display:

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/011.png)

Select User Parameters. The following screen will display:

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/012.png)

The AudioRENEWAL parameters define how renewal works, what recorded messages are spoken to patients requesting renewals, and also prevents certain renewal requests from being entered in the queue and failing when pharmacy processes the phone requests.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Days to Allow:</strong></th>
<th><p>Enter the number of days permitted prior to the renew</p>
<p>date for the provider to respond to a renewal request.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>No Action – Transfer or Message:</strong></td>
<td>Enter “<strong>T</strong>” to transfer the call when no action was taken on their renewal request. Enter “<strong>M</strong>” to play a user defined message advising the patient who to contact.</td>
</tr>
<tr class="even">
<td><strong>No Action Transfer:</strong></td>
<td>Enter the entry number for a <strong>No Action Transfer</strong> defined in the transfer setup table.</td>
</tr>
<tr class="odd">
<td><strong>Not Approved – Transfer or Message:</strong></td>
<td>When the provider does not approve a renewal request, the user chooses whether to enter “<strong>T” to transfer</strong> the patient or enter an “<strong>M</strong>” to play a user defined advising the patient who to contact.</td>
</tr>
<tr class="even">
<td><strong>Not Approved Transfer:</strong></td>
<td>Enter the entry number for a <strong>Not Approved Transfer</strong> defined in the transfer setup table.</td>
</tr>
<tr class="odd">
<td><strong>Renewable Transfer or Message:</strong></td>
<td><p>When the prescription is not renewable, the user chooses whether to enter “<strong>T” to transfer</strong> the patient</p>
<p>or enter an “<strong>M</strong>” to play a user defined message advising the patient who to contact.</p></td>
</tr>
<tr class="even">
<td><strong>Not Renewable Transfer:</strong></td>
<td>Enter the entry number for a <strong>Not Renewable Transfer</strong> defined in the transfer setup table.</td>
</tr>
<tr class="odd">
<td><strong>Days to Keep Records:</strong></td>
<td>Enter the number of days to save renewal transactions on the <strong>AudioCARE</strong> server.</td>
</tr>
<tr class="even">
<td><strong>Days for delivery:</strong></td>
<td>Enter the number of days expected delivery from CMOP will take after renewal approval.</td>
</tr>
<tr class="odd">
<td><strong>Post Unsigned Notifications:</strong></td>
<td>N/A. Notifications are determined by the OERR Notification system in VistA.</td>
</tr>
<tr class="even">
<td><strong>Host User ID#:</strong></td>
<td>Enter the <strong>User</strong> <strong>ID</strong> number from the <strong>New</strong> <strong>Person</strong> <strong>File</strong> for the proxy user that is used to populate the OR AUTORENEWAL USER parameter.</td>
</tr>
<tr class="odd">
<td><strong>Providers to Include:</strong></td>
<td>To allow renewals for orders written by only PCMM primary care providers and associates enter a “<strong>P</strong>”. Enter an “<strong>A</strong>” to allow renewals from all providers.</td>
</tr>
<tr class="even">
<td><strong>Ask Renewal Question:</strong></td>
<td>Enter “<strong>N</strong>” to automatically process a renewal request or “<strong>Y</strong>” to ask the caller if they would like a renewal.</td>
</tr>
<tr class="odd">
<td><strong>Play Decision by Provider:</strong></td>
<td>Enter “<strong>Y</strong>” to include a message to inform the caller that the decision to approve or cancel the renewal request is made by the provider. Enter an <strong>“N”</strong> to omit this message.</td>
</tr>
<tr class="even">
<td><strong>Process Non-Renewable:</strong></td>
<td>Enter “<strong>Y</strong>” to allow non-renewable drug renewal requests to process and create the appropriate VistA MailMan message and provider notification (if enabled). A renewal order is NOT automatically created. Enter ”<strong>N</strong>” to play a message that will inform the caller that the prescription is not renewable. Non- renewable in this case is based on the drugs DEA special handling code(s) and the RX patient status code.</td>
</tr>
<tr class="odd">
<td><strong>Expire date age limit:</strong></td>
<td><p>Enter the number of days to allow renewal requests for expired prescriptions, after which the prescription is too old to be renewed.</p>
<p><strong>VA pharmacy software caps this at 120 days</strong></p></td>
</tr>
</tbody>
</table>

Activate AudioRENEWAL:

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/013.png)

Please Note: Do NOT activate until all the parameters above have been defined.

To activate AudioRENEWAL enter an “A” in the Activate/Deactivate Renewal: field. The letter "D" is entered to deactivate AudioRENEWAL. Then press F3 to save.

To Change the Refill/Pharmacy Menu Message

To change the AudioREFILL menu option prompt to include “Press 4 to request a Renewal”, follow the instructions below. 

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 95%" />
</colgroup>
<tbody>
<tr class="odd">
<td>#</td>
<td><strong>Instructions</strong></td>
</tr>
<tr class="even">
<td>1.</td>
<td>From the AudioCARE Main Menu, Select Application Modules.</td>
</tr>
<tr class="odd">
<td>2.</td>
<td>From Application Modules, Select AudioREFILL.</td>
</tr>
<tr class="even">
<td>3.</td>
<td>From AudioREFILL Set-up Menu, Select Voice Recordings.</td>
</tr>
<tr class="odd">
<td>4.</td>
<td><p>On the Voice Recording Screen, use the cursor to advance to the Main Option field. </p>
<p>The text of the pharmacy menu will display across the bottom of the screen.  Look to see if there is an Option 4 for Renewal.  If there is an Option 4, no action needs to be taken.</p></td>
</tr>
<tr class="even">
<td>5.</td>
<td>If there is no Option 4 – for Renewal, press the F5 key (CNTRL L if in telnet) for a list of available alternatives.  AudioCARE archives the voice recordings.  Look for a recording that contains all the same menu options in addition to Option 4 for Renewal. (Press the up and down arrow keys to display more recording options.) If no message contains option 4 for RENEWAL, use current message. When the caller enters the prescription number in the REFILL system, the system will verify it as eligible for RENEWAL.  It will initiate the RENEWAL process and speak the appropriate message to the patient.</td>
</tr>
<tr class="odd">
<td>6.</td>
<td>Use the down arrow to select the voice file number and description of the menu option you wish to select.  Press [Enter] to accept as the Main Option field.  Please keep in mind other inbound pharmacy applications such as AudioRxINFO or the capability to transfer to the pharmacy.</td>
</tr>
<tr class="even">
<td>7.</td>
<td>Press [Enter] and the [F3] function key to FILE.  Press [Enter] again at the update complete prompt.  The Renewal menu option should be activated.</td>
</tr>
</tbody>
</table>

To contact AudioCARE Customer Service for additional assistance call 1-610-296-9840 and select option \#2.

# Installation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Every site is expected to install patch OR\*3\*336 (shown in the steps below), even if they are not currently using AudioCARE applications. Sites using AudioCARE applications are expected to follow the instructions in patch PSO\*7\*328 to obtain and install the updated Class III routine VEXRX.

The patch descriptions of both patches PSO\*7\*328 and OR\*3\*336 refer to this documentation.

# Pre Installation – Retrieve VEXRX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  Retrieve VEXRX routine from SHOP ALL (Sites using AudioCARE applications only)

Since routine VEXRX is not a PSO namespaced routine, it must be retrieved using SHOP,ALL on FORUM.

The following capture shows how to retrieve the updated routine using SHOP,ALL on FORUM. Note that the name of the message is "ROUTINE VEXRX FOR PATCH PSO\*7\*328", and it is located in the TELEPHONE REFILL REQUESTS basket.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Software Services Primary Menu Option: SHOP SHOP,ALL FOURWARD</p>
<p>====</p>
<p>ISC-CHICAGO</p>
<p>$ set NOver !!!!!!! Now connected to FOURWORD !!!!!!!</p>
<p>Select FORUM,FORUM at the SURROGATE NAME: // prompt to logout.</p>
<p>Choose from:</p>
<p>PATCH,ALL Read Privilege</p>
<p>SHOP,ALL Read Privilege</p>
<p>SHARED,MAIL Read Privilege</p>
<p>Select NEW PERSON NAME: SHARED,MAIL// SHOP,ALL Read Privilege</p>
<p>========</p>
<p>VA MailMan 7.1 service for SHOP.ALL@ISC-CHICAGO.VA.GOV</p>
<p>(Surrogate: FORUM,FORUM)</p>
<p>SHOP,ALL last used MailMan: 08 Sep 09 11:49 (Surrogate: FORUM,FORUM)</p>
<p>SHOP,ALL's current banner: SHOPALL BULLETIN BOARD</p>
<p>Select message reader: Classic// &lt;RTN&gt;</p>
<p>Read mail in basket: TELEPHONE REFILL REQUESTS (7 messages)</p>
<p>Last message number: 7 Messages in basket: 7</p>
<p>Enter ??? for help.</p>
<p>TELEPHONE REFILL REQUESTS Basket Message: 1// ?</p>
<p>TELEPHONE REFILL REQUESTS Basket, 7 messages (1-7)</p>
<p>*=New/!=Priority.......Subject........................From.....................</p>
<p>1. AUDIOFAX VEXRX RTN AFTER PSO*6*141 &lt;Name Removed@ISC-BIRM.</p>
<p>2. AUDIOFAX VEXRX RTN 3/15/96 &lt;Name Removed@FORUM.VA.</p>
<p>3. VEXRX for Outpatient V.7 &lt;Name Removed@ISC-BIRM.</p>
<p>4. VEXRX FOR OUTPATIENT 7.0 (11/26/01) &lt;Name Removed@CPR.ISC-C</p>
<p>5. VEXRX FOR OUTPATIENT 7.0 &lt;Name Removed@CPR.ISC-C</p>
<p>6. VEXRX FOR OUTPATIENT 7.0 &lt;Name Removed@CPR.ISC-C</p>
<p>7. ROUTINE VEXRX FOR PATCH PSO*7*197 &lt;Name Removed@LAWVAA.FO</p>
<p>8. <strong>ROUTINE VEXRX FOR PATCH PSO*7*328</strong> &lt;Name Removed@CHEY19.FO</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

At this point, select the message "ROUTINE VEXRX FOR PATCH PSO\*7\*328". In this example it is message number 8, but be sure to verify the correct message title. Then at the "message action" prompt, forward the message to your local system.

2)  Load the Distribution for patch OR\*3\*336 from the MailMan message (All Sites)
- Choose the Packman message containing patch OR\*3\*336.
- At the 'message action' prompt type 'X' to invoke the INSTALL/CHECK MESSAGE PackMan option.
- At the 'Select PackMan function:' prompt type 'INSTALL/CHECK MESSAGE' to load the distribution.

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select *=New/!=Priority..........Subject..................Lines.From.........Read/Rcvd</p>
<p>127. [4059580] 03/10/10 OR*3*336 1246 &lt;"NPM [#51710262]"@F</p>
<p>Search finished.</p>
<p>Enter message number or command: <strong>127</strong></p>
<p>Subj: OR*3*336 [#4059580] 10 Mar 2010 11:52:27 -0500 (EST) 1246 lines</p>
<p>From: &lt;"NPM [#51710262]"@FORUM.VA.GOV&gt; In 'IN' basket. Page 1</p>
<p>-------------------------------------------------------------------------------</p>
<p>$TXT Created by Developer,One at CHEY19.FO-BAYPINES.MED.VA.GOV (KIDS) on Wedne</p>
<p>sday, 03/10/10 at 11:22</p>
<p>=============================================================================</p>
<p>Run Date: MAR 10, 2010 Designation: OR*3*336</p>
<p>Package : OR - ORDER ENTRY/RESULTS REPORTING Priority: Mandatory</p>
<p>Version : 3 Status: Released</p>
<p>Compliance Date: &lt;Compliance Date&gt;</p>
<p>=============================================================================</p>
<p>Associated patches: (v)OR*3*243 &lt;&lt;= must be installed BEFORE `OR*3*336'</p>
<p>Subject: AUDIOCARE RENEWAL</p>
<p>Category: ROUTINE</p>
<p>Description:</p>
<p>============</p>
<p>This patch is a replacement patch for OR*3*290, which has been entered in</p>
<p>Enter RETURN to continue or '^' to exit: ^</p>
<p>Enter message action (in IN basket): Ignore// Xtract KIDS</p>
<p>Select PackMan function: 6 INSTALL/CHECK MESSAGE</p>
<p>Line 233 Message #4059580 Unloading KIDS Distribution OR*3.0*336</p>
<p>Want to Continue with Load? YES//</p>
<p>Loading Distribution...</p>
<p>OR*3.0*336</p>
<p>Select PackMan function:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Installation Procedure – OR\*3\*336

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  Install the VEXRX routine (Sites using AudioCARE applications only)

From MailMan, load and install the Class III VEXRX routine that has been retrieved and forwarded to your local mail from SHOP ALL (see pre-installation section). Install this routine when the option Process Telephone Refills \[A3A PHONE REFILLS\] is not in use. Install this routine before patch OR\*3\*336.

> **NOTE:** If you have already installed the updated VEXRX routine from PSO\*7\*328 before installing OR\*3\*290, then you do not need to install it again. The VEXRX routine has not changed since the release of PSO\*7\*328.

Below is the step-by-step procedure for installing routine VEXRX.

- Open the MailMan message containing the VEXRX routine.
- At the 'Message Action' prompt type 'X' to invoke the INSTALL/CHECK MESSAGE PackMan option.
- At Select PackMan function prompt enter 6 INSTALL/CHECK MESSAGE.
- At the warning message prompt enter YES.
- At the Preserve routines on disk prompt enter YES.
- At the 'Subject' prompt type 'PSO\*7\*328 Backup'
- Send to your local mailbox.
- At 'And send to' prompt, press enter.
- The routine is now installed.

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select PackMan function: 6 INSTALL/CHECK MESSAGE</p>
<p>Warning: Installing this message will cause a permanent update of globals</p>
<p>and routines.</p>
<p>Do you really want to do this? NO// YES</p>
<p>Routines are the only parts that are backed up. NO other parts</p>
<p>are backed up, not even globals. You may use the 'Summarize Message'</p>
<p>option of PackMan to see what parts the message contains.</p>
<p>Those parts that are not routines should be backed up separately</p>
<p>if they need to be preserved.</p>
<p>Shall I preserve the routines on disk in a separate back-up message? YES//</p>
<p>Subject: PSO*7*328 BACKUP</p>
<p>Send mail to: // (ADD YOUR NAME HERE)</p>
<p>Select basket to send to: IN//</p>
<p>And Send to:</p>
<p>Building PackMan backup message with subject PSO*7*328 BACKUP</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2)  Install patch OR\*3\*336 (All Sites)

Before installing patch OR\*3\*336, consult with the Pharmacy staff to determine the appropriate person to coordinate the membership for the “AUTORENEWAL’ mail group used in the auto renewal process. Communicate this information to the person installing the patches.

Below is the step-by-step procedure for installing patch OR\*3\*336.

This patch can be installed with users on the system. Installation will take less than 5 minutes.

Ensure that the “PROCESS TELEPHONE REFILLS” option is not in use.

 

Suggested time to install: non-peak requirement hours.

This installation does not change the functionality of CPRS or Outpatient Pharmacy applications.

ENVIRONMENT CHECK: OR\*3\*336 contains an environment check that looks for the renewal version of VEXRX that was being used when the problem was reported in January 2009. If the January 2009 renewal version of VEXRX is found, the installation of OR\*3\*336 aborts. If this occurs retrieve and install the correct VEXRX routine, then use the 'Restart Install of Package(s)' option to complete the OR\*3\*336 patch installation. For sites not using AudioCARE refill or renewal, the pre-environment checks will be skipped if the Class III VEXRX routine is not in the system.

1)  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.

> **NOTE:** If patch OR\*3\*290 was not installed routines ORAREN and ORY290 will not exist before installing OR\*3\*336. If you have installed patch OR\*3\*290, which has now been marked entered

in error, the "before" checksums for ORAREN and ORY290 will match the "before" checksum in the Routine Information section of this patch, OR\*3\*336. Both routines have been modified by this patch and the "after" checksum should match what is provided in this patch description. Do not uninstall patch

OR\*3\*290.

2)  From the Kernel Installation & Distribution System menu, select the Installation menu.
3)  From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter OR\*3.0\*336):
- Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
- Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
- Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4)  Use the Install Package(s) option and select the package OR\*3.0\*336.
5)  When prompted "Enter the Coordinator for Mail Group 'AUTORENEWAL', answer with the name of the person who will be responsible for assigning the users who will be monitoring/receiving messages about automatic renewal requests.
6)  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", respond NO.
7)  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//", respond NO.

IMPORTANT NOTE: If you are NOT using the AudioRENEWAL Module, your installation is complete.

Install Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Installation Option: 6 Install Package(s)</p>
<p>Select INSTALL NAME: OR*3.0*336 Loaded from Distribution 3/29/10@15:11:52</p>
<p>=&gt; OR*3*336</p>
<p>This Distribution was loaded on Mar 29, 2010@15:11:52 with header of</p>
<p>OR*3*336 It consisted of the following Install(s):</p>
<p>OR*3.0*336</p>
<p>Checking Install for Package OR*3.0*336</p>
<p>Install Questions for OR*3.0*336</p>
<p>Incoming Files:</p>
<p>100.9 OE/RR NOTIFICATIONS (including data)</p>
<p>Note: You already have the 'OE/RR NOTIFICATIONS' File.</p>
<p>I will OVERWRITE your data with mine.</p>
<p>Incoming Mail Groups:</p>
<p>Enter the Coordinator for Mail Group 'AUTORENEWAL': PHARMACYPERSON,ONE LAH</p>
<p>192 OI&amp;T STAFF</p>
<p>Want KIDS to INHIBIT LOGONs during the install? NO//</p>
<p>Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//</p>
<p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt.</p>
<p>Enter a '^' to abort the install.</p>
<p>DEVICE: HOME// &lt;RETURN&gt;</p>
<p>Install Started for OR*3.0*336 :</p>
<p>Mar 29, 2010@15:16:18</p>
<p>Build Distribution Date: Mar 29, 2010</p>
<p>Installing Routines:</p>
<p>Mar 29, 2010@15:16:18</p>
<p>Running Pre-Install Routine: PRE^ORY290</p>
<p>Installing Data Dictionaries:</p>
<p>Mar 29, 2010@15:16:18</p>
<p>Installing Data:</p>
<p>Mar 29, 2010@15:16:18</p>
<p>Installing PACKAGE COMPONENTS:</p>
<p>OR*3.0*336</p>
<p>──────────────────────────────────────────────</p>
<p>Installing MAIL GROUP</p>
<p>Installing PARAMETER DEFINITION</p>
<p>Mar 29, 2010@15:16:18</p>
<p>Running Post-Install Routine: POST^ORY290</p>
<p>Updating Routine file...</p>
<p>Updating KIDS files...</p>
<p>OR*3.0*336 Installed.</p>
<p>Mar 29, 2010@15:16:18</p>
<p>───────────────────────────────────────────────</p>
<p>┌─────────────────────────────────────────────────────┐</p>
<p>100% │ 25 50 75 │</p>
<p>Complete └─────────────────────────────────────────────────────┘</p>
<p>Install Completed</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Post Installation – Activate AudioRENEWAL 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is only for sites using the AudioRENEWAL Module. The purpose of this section is to provide information for consideration after routine VEXRX and patch OR\*3\*336 are installed. IRM, Pharmacy, and Providers should work together to monitor renewal activity.

Refer to the Release Notes section of this document for additional detail about these items.

1)  Assign members to the AUTORENEWAL mail group using option MAIL GROUP COORDINATOR'S EDIT.
2)  If necessary, set up the proxy user in the NEW PERSON (#200) file for filing renewal requests. Sites may already have USER,AUDIOCARE PHONE set up for renewals. No menu options, person classes, or keys need to be added to this user.
3)  Edit parameter OR AUTORENEWAL USER and enter the proxy user defined in step \#2.
4)  Review the settings for the notification OP RX RENEWAL REQUEST very closely and determine the settings which are most appropriate for your usage of AudioRENEWAL. Do not edit the exported Package level parameter settings.
5)  Enable the notification OP RX RENEWAL REQUEST using option Enable/Disable Notifications.
6)  Update AudioRENEWAL Clinic list on the AudioCARE server.
7)  Review parameter settings on the AudioCARE server.
8)  Re-Activate the AudioRENEWAL functionality on the AudioCARE server.
9)  Notify providers, pharmacy, and nurses that AudioRENEWAL has been reactivated and who to contact for problems.

> After running the option to process refills/renewals:

10) Confirm that the AUTORENEWAL Mail Group is receiving MailMan messages.
11) Verify that unsigned renewal orders are being generated.
12) Confirm that the Notifications are occurring as expected for signature requests.
13) Verify the Refill Count report (MailMan message).

<span id="_Toc379892233" class="anchor"></span>AudioRENEWAL in CPRS

The basic steps of the AudioRENEWAL process that allows patients to request a renewal of their prescriptions by phone are as follows:

1)  Patient calls into the automated system, validates they are a VA patient, and keys in the prescription number. When there are no refills left, the request for renewal begins. If the medication is renewable after passing initial software checks a renewal request record is placed in the telephone queue.
2)  When the option Process Telephone Refills is executed by pharmacy, the renewal request passes addition software checks and the system creates an unsigned order.
3)  The unsigned order triggers the notification “Order Requires Elec Signature” to the defined recipients.
4)  A defined recipients, in general the ordering provider, processes the notification and considers if the medication therapy should continue. If the decision is to continue, the order is signed. If the decision is not to continue, the provider cancels the unsigned renewal order and determines what action to take.
5)  When the order is signed, pharmacy finishes the order and the patient receives the requested medication in the preferred method.

This section of the document explains how these requests appear in CPRS and what to look for when the process doesn’t follow the happy path described above. A few frequently asked questions and answers have been included.

Points to remember:

- The provider always determines if the request should be approved or cancelled.
- Always adhere to facility business rules before making changes to procedures or systems.

<u>User CREATED renewal vs. AudioRENEWAL CREATED renewal</u>

Understanding the difference between a CPRS user taking the RENEW action and the RENEW action being taken when AudioRENEWAL requests are processed can be very informative. The following examples show and explain the differences.

<u>USER CREATED</u>: In the example below, the CPRS user VMPROVIDER, TEST ONE is the new primary care provider for the patient selected. The active outpatient medication order for ACYCLOVIR has been selected and the detail opened. The new provider would like to renew this order now. Notice that the current Currently CPRSPHYSICIAN, LHCLONE is displayed as the ordering provider.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/014.png)

To validate what the order entry system will consider as the ordering provider for the action RENEW, an inquiry on the order in File \#100 ORDER is done. The field showing the value is CURRENT AGENT/PROVIDER:

> Select OPTION: INQUIRE TO FILE ENTRIES

> OUTPUT FROM WHAT FILE: NEW PERSON// 100 ORDER (9362638 entries)

> Select ORDER: \`12980449 12980449

> ANOTHER ONE:

> STANDARD CAPTIONED OUTPUT? Yes// (Yes)

> Include COMPUTED fields: (N/Y/R/B): NO// BOTH Computed Fields and Record Number

> (IEN)

> NUMBER: 12980449 ORDER \#: 12980449

> OBJECT OF ORDER: VMPATIENT,RENEW A

> <span class="mark">CURRENT AGENT/PROVIDER: CPRSPHYSICIAN,LHCLONE</span> ordering provider

> DIALOG: PSO OERR WHO ENTERED: CPRSPHYSICIAN,LHCLONE

> WHEN ENTERED: FEB 05, 2014@13:14 START DATE: FEB 05, 2014

> STOP DATE: MAR 07, 2014

> PATIENT LOCATION: DENTAL DWIGHT PEMBERTON

> (additional data omitted)

In CPRS, the new provider selects the ACYCLOVIR order, then selects Renew.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/015.png)

When the location dialog displays the appropriate location is selected, the renewal dialog is accepted with no changes. The provider signs the new order. Pharmacy finishes and releases the order.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/016.png)

In the screen above a customized view has been selected to show ALL Orders – PHARMACY. The new provider is displayed in the provider column as the provider for the active ACYCLOVIR renewal, and the previous order for ACYCLOVIR has a status of discontinued. To validate that the order entry system now considers VMPROVIDER, TEST ONE, as the ordering provider, check File \#100 ORDER field CURRENT AGENT/PROVIDER:

> NUMBER: 12980451 ORDER \#: 12980451

> OBJECT OF ORDER: VMPATIENT,RENEW A

> <span class="mark">CURRENT AGENT/PROVIDER: VMPROVIDER,TEST ONE</span>

> DIALOG: PSO OERR WHO ENTERED: VMPROVIDER,TEST ONE

> WHEN ENTERED: FEB 05, 2014@14:58 START DATE: FEB 05, 2014

> STOP DATE: MAR 07, 2014 PATIENT LOCATION: GEM CLINIC

To summarize – when an authorized user selects an order that was created by another user and RENEWs it, that user CREATES the new unsigned renewal order and becomes the CURRENT AGENT/PROVIDER of that new order. The CURRENT AGENT/PROVIDER has “ownership”, which means that future renewals and notifications recognize him as the ordering provider.

Now, with some understanding of CURRENT AGENT/PROVIDER, this example applies that information to the AudioRENEWAL process, where the option Process Telephone Refills initiates the RENEW action to create the new order.

<u>AUDIORENEWAL CREATED</u>: Picking up with the same CPRS user VMPROVIDER, TEST ONE and patient, an outpatient medication order for IBUPROFEN has been requested for renewal using the AudioRENEWAL module. The provider has opened the patient chart and selected the Order tab. The option to Process Telephone Refills has already been executed and the unsigned renewal order for IBUPROFEN has been created and selected in the screen capture below. The details of the unsigned renewal order are displayed.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/017.png)

By opening the detail of the renewal order the provider can identify the order as one created by the AudioRENEWAL process with the “entered by” value RENEWAL,PROXY. All AudioRENEWAL orders are <u>created</u> with the CURRENT AGENT/PROVIDER of the order they were requested from. This CURRENT AGENT/PROVIDER is displayed in CPRS when the new order is in the unreleased status, in this example the provider is CPRSPHYSICIAN, LHCLONE. Verify this by looking at the orders in File \#100 ORDER:

File \#100 ORDER record for the <u>new</u> unsigned renewal order:

> NUMBER: 12980453 ORDER \#: 12980453

> OBJECT OF ORDER: VMPATIENT,RENEW A

> <span class="mark">CURRENT AGENT/PROVIDER: CPRSPHYSICIAN,LHCLONE</span>

> DIALOG: PSO OERR WHO ENTERED: RENEWAL,PROXY

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/018.png)

File \#100 ORDER record for existing order to renew from:

> NUMBER: 12980450 ORDER \#: 12980450

> OBJECT OF ORDER: VMPATIENT,RENEW A

> <span class="mark">CURRENT AGENT/PROVIDER: CPRSPHYSICIAN,LHCLONE</span>

> DIALOG: PSO OERR WHO ENTERED: CPRSPHYSICIAN,LHCLONE

If provider VMPROVIDER, TEST ONE <u>signs</u> the order created by the AudioRENEWAL process the current value in field CURRENT AGENT/PROVIDER does not change. The next time this patient requests a renewal using the AudioRENEWAL module the provider that will display on the unreleased renewal order will again be CPRSPHYSICIAN, LHCLONE.

For this exercise, the new provider decides to sign the renewal created using the AudioRENEWAL process.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/019.png)

After pharmacy finishes the order:

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/020.png)

After the order has been signed and released by pharmacy the provider refreshes CPRS and reviews the order (above). The new provider notices that his name displays in the provider column in the Active Order view. This is as it should be since SIGN was the last action taken on this order in CPRS. By rechecking the order in File \#100 ORDER after it has been signed and released it can be confirmed that the SIGN action DOES NOT change the value of the field CURRENT AGENT/PROVIDER. The next time this order is requested for renewal using the AudioRENEWAL module the provider that will display on the unreleased renewal order will again be CPRSPHYSICIAN, LHCLONE.

> NUMBER: 12980453 ORDER \#: 12980453

> OBJECT OF ORDER: VMPATIENT,RENEW A

> <span class="mark">CURRENT AGENT/PROVIDER: CPRSPHYSICIAN,LHCLONE</span>

> DIALOG: PSO OERR WHO ENTERED: RENEWAL,PROXY

> WHEN ENTERED: FEB 05, 2014@15:48 START DATE: FEB 05, 2014

> STOP DATE: MAR 07, 2014

> PATIENT LOCATION: DENTAL DWIGHT PEMBERTON

> TO: OUTPATIENT MEDICATIONS PATIENT CLASS: OUTPATIENT

> PACKAGE: OUTPATIENT PHARMACY SIGNATURE REQUIRED: ORES

> ORDERABLE ITEM: IBUPROFEN TAB

> DATE OF LAST ACTIVITY: FEB 05, 2014@17:35:17

> GRACE DAYS BEFORE PURGE: 90 <span class="mark">STATUS: ACTIVE</span>To summarize – To establish a new ordering provider for a unsigned renewal order created using the AudioRENEWAL process, the new ordering provider could DISCONTINUE the system created order, then refresh CPRS and select the order that the renewal was requested from and RENEW that order manually.Notification Recipient One

In this example, the CPRS session belongs to user VMPROVIDER,RESIDENT ONE who received the signature alert for the unsigned Renewal for LISINOPRIL TAB 5MG (Order \#12980378) that is shown in order detail below. Note that the previous Renew LISINOPRIL TAB 5MG order, with an active status, was signed by this CPRS user. In the order detail, RENEWAL,PROXY is the “entered by” value which indicates that this order was created through the AudioRENEWAL module. CPRSPHYSICIAN,LHCLONE is displayed in the provider column in the Active Order list view for new renewal order and also the “Ordered by:” in the order detail.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/021.png)

<u>Question \#1:</u>

Based on the information provided above, what are the possible situation(s) that allowed VMPROVIDER,RESIDENT ONE to receive the unsigned order signature alert for Renew LISINOPRIL TAB 5MG (12980378)?

<u>Correct Answers:</u>

1.  VMPROVIDER, RESIDENT ONE is currently the assigned surrogate for CPRSPHYSICIAN, LHCLONE.
2.  CPRSPHYSICIAN, LHCLONE forwarded the signature alert to VMPROVIDER, RESIDENT ONE.
3.  In the OERR NOTIFICATION system, the provider recipient codes for the ORDER REQUIRES ELEC SIGNATURE notification are set up in a manner that includes the title or relationship to patient CPRSPATIENT, VMONE of VMPROVIDER, RESIDENT ONE.

Notification Recipient Two

This example continues using the Renew LISINOPRIL TAB 5MG (Order \#12980378) that is shown in the Order Detail of example one. The order has now been signed by VMPROVIDER, RESIDENT ONE and completed by outpatient pharmacy. The screens below display the current information in both outpatient pharmacy and CPRS.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/022.png)

(above) Provider that signed the order displays in pharmacy

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/023.png)

(above) Provider that signed the order displays in CPRS Active Order view

In the CPRS View Orders display below, the view has been changed to a custom view that is displaying all pharmacy orders, showing only the LISINOPRIL TAB 5MG orders:

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/024.png)

CPRSPHYSICIAN, LHCLONE wrote LISINOPRIL TAB 5MG for patient CPRSPATIENT,VMONE. Then the patient was assigned to VMPROVIDER, RESIDENT ONE. Now, each time the patient uses AudioRENEWAL to renew this medication, the unsigned order signature alert goes CPRSPHYSICIAN, LHCLONE even though VMPROVIDER,RESIDENT ONE signed the last two renewals.

<u>Question \#2:</u>

Why doesn’t the alert go to the provider that displayed in outpatient pharmacy and CPRS, and that last signed the order?

<u>Explanation:</u>

When the pharmacy executes the option to process the telephone refills the renewals are processed. There are various checks performed during this process, including the provider checks, which in turn trigger the signature notifications. This process (routine VEXRX) uses the value in field \#1 CURRENT AGENT/PROVIDER of File \#100 ORDER of the order that corresponds with the prescription number enter for the renewal request. For users, the difficulty is that neither outpatient pharmacy nor CPRS GUI displays the CURRENT AGENT/PROVIDER field.

> 100,1         CURRENT AGENT/PROVIDER 0;4 POINTER TO NEW PERSON FILE (#200)

>               LAST EDITED:      MAR 06, 1997

>               HELP-PROMPT:      Enter the name of the requesting clinician for

>                                 this order.

>               DESCRIPTION:      This is the person who is responsible for the

>                                 order. 

Below is order \#12980378 LISINOPRIL TAB 5MG from the ORDER File \#100. Notice the value in CURRENT AGENT/PROVIDER. When the next renewal request from the patient is processed, the value CPRSPHYSICIAN, LHCLONE will again be used to populate the CURRENT AGENT/PROVIDER field when the new unsigned renewal order is created.

> NUMBER: 12980378 ORDER \#: 12980378

> OBJECT OF ORDER: CPRSPATIENT,VMONE

> <span class="mark">CURRENT AGENT/PROVIDER: CPRSPHYSICIAN,LHCLONE</span>

> DIALOG: PSO OERR WHO ENTERED: RENEWAL,PROXY

> WHEN ENTERED: JAN 17, 2014@19:11 START DATE: JAN 17, 2014

> STOP DATE: FEB 16, 2014 PATIENT LOCATION: 23 HOUR OBSERVATION

> TO: OUTPATIENT MEDICATIONS PATIENT CLASS: OUTPATIENT

> PACKAGE: OUTPATIENT PHARMACY SIGNATURE REQUIRED: ORES

> ORDERABLE ITEM: LISINOPRIL TAB

> DATE OF LAST ACTIVITY: JAN 17, 2014@20:06:39

> GRACE DAYS BEFORE PURGE: 90 STATUS: ACTIVE

> REPLACED ORDER: 12980377 CURRENT ACTION: 1

> TYPE: RENEW PACKAGE REFERENCE: 4314948

> (removed the middle ITEM ENTRY data)

> DATE/TIME ORDERED: JAN 17, 2014@19:11 ACTION: NEW

> PROVIDER: VMPROVIDER,RESIDENT ONE SIGNATURE STATUS: ELECTRONIC

> SIGNED BY: VMPROVIDER,RESIDENT ONE DATE/TIME SIGNED: JAN 17, 2014@20:04

> NATURE OF ORDER: ELECTRONICALLY ENTERED

> ENTERED BY: RENEWAL,PROXY TEXT REFERENCE: 1

> RELEASE DATE/TIME: JAN 17, 2014@20:04

> RELEASING PERSON: VMPROVIDER,RESIDENT ONE

> ORDER TEXT:

> LISINOPRIL TAB 5MG

> TAKE ONE TABLET BY MOUTH Before Breakfast

> Quantity: 30 Refills: 0

<u>Question \#3:</u>

Are there any suggestions regarding how to update the CURRENT AGENT/PROVIDER to the patients new provider for future renewals?

<u>Explanation:</u>

When a new provider becomes responsible for the order, that provider needs to be established as the CURRENT AGENT/PROVIDER. This can only be done when an order is CREATED. Since AudioRENEWAL creates the unsigned orders, these orders cannot be used to change the CURRENT AGENT/PROVIDER field. If the new provider decides to continue the medication for the patient, to take ownership of that order the provider would need to CREATE the renewal. The AudioRENEWAL generated unreleased (unsigned) order can be discontinued by the provider and then RENEW action can be taken on the existing order (manually).

Using the active order above, the new provider VMPROVIDER, RESIDENT ONE, renews the order.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/025.png)

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/026.png)

To verify this action established the new provider as the CURRENT AGENT/PROVIDER for this medication order the ORDER file is checked:

> NUMBER: 12980420 ORDER \#: 12980420

> OBJECT OF ORDER: CPRSPATIENT,VMONE

> <span class="mark">CURRENT AGENT/PROVIDER: VMPROVIDER,RESIDENT ONE</span>

> DIALOG: PSO OERR WHO ENTERED: VMPROVIDER,RESIDENT ONE

> WHEN ENTERED: JAN 27, 2014@13:37 PATIENT LOCATION: 23 HOUR OBSERVATION

> TO: OUTPATIENT MEDICATIONS PATIENT CLASS: OUTPATIENT

> PACKAGE: OUTPATIENT PHARMACY SIGNATURE REQUIRED: ORES

> ORDERABLE ITEM: LISINOPRIL TAB

> DATE OF LAST ACTIVITY: JAN 27, 2014@13:37:45

> GRACE DAYS BEFORE PURGE: 90 STATUS: UNRELEASED

> REPLACED ORDER: 12980378 CURRENT ACTION: 1

> TYPE: RENEW

> (partial record displayed)

The next time the patient requests a renewal by phone this provider will be used to populate the CURRENT AGENT/PROVIDER field when the new unsigned renewal order is created, and will also be the ordering provider recipient of unsigned order signature notifications.

<u>Question \#4:</u>

The surrogates assigned to terminated providers are not receiving the ORDER REQUIRES ELEC SIGNATURE notification.

<u>Explanation:</u>

This is because the unsigned renewal order is not being created. When an AudioRENEWAL request is processed and the outpatient medication order is renewable but the ordering provider status is terminated or disusered, the unsigned renewal order is not created. An entry is made in the MailMan message with the subject line 'Renewal Requests not Sent to Providers' with the problem listed as 'Provider flagged as \<STATUS\>', where status will state the problem with the provider. The person that calls in the renewal request is hearing the message "Your renewal request has been submitted. Please call back in \<number of\> days for a status." If site personnel fail to take action on the problem listed in the MailMan message, the patient may call back days later to find out that no action has occurred on the renewal, or may not call until they have run out of the medication. This could create a situation where the patient misses multiple doses of a needed medication.

<u>Patch OR\*3\*349</u> modified routine ORAREN so that when the ordering provider of a renewable outpatient medication order having a status of terminated or disusered has an active surrogate designated, the routine 'accepts' the surrogate's active status and creates the new unsigned renewal order. This new unsigned order generates the ORDER REQUIRES ELEC SIGNATURE notification which is distributed based on surrogacy and provider recipient codes set for this notification in the Notification Mgmt. Menus.

If no surrogate is assigned to inactive providers when renewals are processed, the result will be the same as before this patch. When the ordering provider is terminated or disusered, and there is NO designated surrogate, NO renewal order is created. Since there is no unsigned order, no notification is generated. An entry is made in the MailMan message with the subject line 'Renewal Requests not Sent to Providers' with the problem listed as 'Provider \<name\> flagged as \<STATUS\>' where status will state the problem with the provider and \<name\> will contain the name of the inactive provider.

Demonstration of Surrogate designation:

In this scenario, the patient has requested a renewal for HYDROCHLOROTHIAZIDE. The ordering provider VMPROVIDER, TEST TWO has a status of terminated and provider CPRSPHYSICIAN, LHCLONE is the designated surrogate and new provider for this patient. The provider CPRSPHYSICIAN, LHCLONE received the signature notification as expected. As the new provider for this patient, CPRSPHYSICIAN, LHCLONE has decided to continue the medication. CPRSPHYSICIAN, LHCLONE understands that he needs to CREATE the renewal order or the next renewal request will continue to list the terminated provider, and if the surrogacy is inadvertently removed future renewals will fail to process. The new provider selected the original order, then selected ACTION, RENEW which resulted in the “Unable to Renew Order” message below.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/027.png)

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/028.png)

CPRSPHYSICIAN,LHCLONE then selected the renewal order created by AudioRENEWAL process and discontinued it. To check the status, the view order display was customized to view ALL Orders - PHARAMCY and the renewal order has a status of cancelled.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/029.png)

The new provider again selected the original order, then selected ACTION, RENEW, and this time because there was no other renewal order tied to the original order the renewal was allowed.

CPRSPHYSICIAN, LHCLONE selected OK and signed the renewal order. After pharmacy completes the prescription and the status displays as active in CPRS, new provider displays as the ordering provider. (Next page)

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/030.png)

In the screen capture above there have been three orders for the medication HYDROCHLOROTHIAZIDE. Since AudioRENEWAL will use the CURRENT AGENT/PROVIDER when the next renewal request is processed, that field has been captured for each order:

> <u>Order \# 12980444 Initial order:</u>

> NUMBER: 12980444 ORDER \#: 12980444

> OBJECT OF ORDER: CPRSPATIENT,VMONE

> <span class="mark">CURRENT AGENT/PROVIDER: VMPROVIDER,TEST TWO</span>

> DIALOG: PSO OERR WHO ENTERED: VMPROVIDER,TEST TWO

> <u>Order \# 12980445 generated by the AudioRENEWAL process:</u>

> NUMBER: 12980445 ORDER \#: 12980445

> OBJECT OF ORDER: CPRSPATIENT,VMONE

> <span class="mark">CURRENT AGENT/PROVIDER: VMPROVIDER,TEST TWO</span>

> DIALOG: PSO OERR WHO ENTERED: RENEWAL,PROXY

> <u>Order \#12980446 renewal order entered by CPRSPHYSICIAN,LHCLONE</u>

> NUMBER: 12980446 ORDER \#: 12980446

> OBJECT OF ORDER: CPRSPATIENT,VMONE

> <span class="mark">CURRENT AGENT/PROVIDER: CPRSPHYSICIAN,LHCLONE</span> will be used next renewal

> DIALOG: PSO OERR WHO ENTERED: CPRSPHYSICIAN,LHCLONE

The next AudioRENEWAL is processed and <u>does</u> use the new provider, CPRSPHYSICIAN,LHCLONE.

![](pso-7-328-audiocare-renewal-release-notes-and-install-guide/031.png)

> NUMBER: 12980447 ORDER \#: 12980447

> OBJECT OF ORDER: CPRSPATIENT,VMONE

> <span class="mark">CURRENT AGENT/PROVIDER: CPRSPHYSICIAN,LHCLONE</span> will be used next renewal

> DIALOG: PSO OERR WHO ENTERED: RENEWAL,PROXY

<u>Question \#5:</u>

Why is there an entry in the MailMan message with the subject line 'Renewal Requests not Sent to Providers' with the problem listed as “Invalid Action – details below. OREMAS key holders may not enter medication orders”?

<u>Explanation:</u>

This is because the person executing the option to process the telephone refills holds the OREMAS key and the general parameter ALLOW CLERKS TO ACT ON MED ORDERS is set to NO. Running this process enters renewal orders into the system, and so this process checks the user ID to see if the person running the option is authorized. More information about this parameter can be found in the CPRS Technical Manual: GUI Version.

<u>Question \#6:</u>

Why are there entries in the MailMan message with the subject line 'Renewal Requests not Sent to Providers' with the problem listed as “Invalid Action – details below. Prescription Expired more than 120 Days”?

<u>Explanation:</u>

The AudioRENEWAL parameter Expire date age limit: is set to a value greater than 120 days. A higher number in the parameter allows the renewal request to enter the telephone queue, but when the records are processed by the pharmacy PROCESS TELEPHONE REFILLS option the outpatient pharmacy software enforces the 120 day limit and the request fails. Change the AudioRENEWAL module parameter setting to 120 days to prevent these requests from being entered.