---
title: "Kernel 8.0 Systems Management: Utilities User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Systems Management: Utilities"
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
menu_options: 8
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - span
  - class
  - mark
  - date
  - edit
  - lock
  - service
  - print
  - table
  - management
page_count: 0
word_count: 38325
section_count: 30
table_count: 4
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Systems Management:

  Utilities User Guide
---

![](kernel-8-0-systems-management-utilities-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-systems-management-utilities-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref505577026" class="anchor"></span>Table 1: Alert Processing Codes</p></caption>
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
<td>08/31/2025</td>
<td>1.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Added bookmarks to all sections.</p></li>
<li><p>Updated references and links to the Kernel Developer’s Guide.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>07/23/2025</td>
<td></td>
<td><p>Updates:</p>
<p>Updated external document links to open documents in a new window.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
<tr class="odd">
<td>06/13/2025</td>
<td>1.1</td>
<td><p>Kernel Patch <strong>XU*8.0*807</strong> Updates:</p>
<p>Added Section <u>7</u>, “<u>Service/Section Edit</u>.”</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
<tr class="even">
<td>05/02/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Systems Management: Utilities User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref505577026" class="anchor"></span>Table 1: Alert Processing Codes

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc204765338" class="anchor"></span>List of Figures

<span id="_Toc204765339" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-systems-management-utilities-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Alerts](#alerts)
  - [Alerts User Interface](#alerts-user-interface)
    - [Processing Alerts](#processing-alerts)
    - [Deleting Alerts](#deleting-alerts)
    - [Forwarding Alerts](#forwarding-alerts)
    - [Surrogates and Alerts](#surrogates-and-alerts)
  - [Alerts System Management](#alerts-system-management)
    - [Alert Management Menu](#alert-management-menu)
    - [Troubleshooting Using ALERT TRACKING (#8992.1) File](#troubleshooting-using-alert-tracking-89921-file)
- [Error Processing](#error-processing)
  - [Error Processing User Interface](#error-processing-user-interface)
  - [Error Processing System Management](#error-processing-system-management)
    - [Error Screens](#error-screens)
    - [Enhanced Error Processing](#enhanced-error-processing)
    - [Print 1 Occurrence of Each Error for T-1 (QUEUE) Option](#print-1-occurrence-of-each-error-for-t-1-queue-option)
    - [Print 2 Occurrences of Errors on T-1 (QUEUED) Option](#print-2-occurrences-of-errors-on-t-1-queued-option)
    - [Clean Error Trap Option](#clean-error-trap-option)
    - [Error Trap Display Option](#error-trap-display-option)
    - [Interactive Print of Error Messages Option](#interactive-print-of-error-messages-option)
- [Lock Manager Utility](#lock-manager-utility)
  - [Kernel Lock Manager Overview](#kernel-lock-manager-overview)
  - [Configuration](#configuration)
    - [Entering Site Parameters—Edit Lock Manager Parameters Option](#entering-site-parametersedit-lock-manager-parameters-option)
    - [Add Lock Manager Users](#add-lock-manager-users)
  - [Lock Manager Options](#lock-manager-options)
  - [Using the Lock Manager](#using-the-lock-manager)
    - [List Locks Screen](#list-locks-screen)
    - [Single Lock Details Screen](#single-lock-details-screen)
  - [Managing the Lock Manager](#managing-the-lock-manager)
  - [Maintaining the Lock Dictionary](#maintaining-the-lock-dictionary)
    - [Adding Lock Templates—Edit Lock Dictionary Option](#adding-lock-templatesedit-lock-dictionary-option)
    - [Exporting Lock Templates](#exporting-lock-templates)
  - [Viewing and Purging Lock Manager Logs](#viewing-and-purging-lock-manager-logs)
    - [View Lock Manager Log Option](#view-lock-manager-log-option)
    - [Purge Lock Manager Log Option](#purge-lock-manager-log-option)
  - [Lock Manager Troubleshooting](#lock-manager-troubleshooting)
    - [Node Connection Error](#node-connection-error)
- [DEA ePCS Utility](#dea-epcs-utility)
  - [DEA ePCS Utility Overview](#dea-epcs-utility-overview)
    - [History](#history)
    - [Requirements](#requirements)
    - [Benefits](#benefits)
    - [Intended Audience](#intended-audience)
  - [Processes](#processes)
    - [Manual Paper-based Process](#manual-paper-based-process)
    - [e-Prescribing Process](#e-prescribing-process)
  - [Configuring the DEA ePCS Utility](#configuring-the-dea-epcs-utility)
    - [Set the XUEPCS REPORT DEVICE Parameter](#set-the-xuepcs-report-device-parameter)
    - [Add DEA ePCS Utility Users](#add-dea-epcs-utility-users)
  - [Using the DEA ePCS Utility](#using-the-dea-epcs-utility)
    - [DEA ePCS Utility Functions Main Menu](#dea-epcs-utility-functions-main-menu)
    - [Print DEA Expiration Date Null Option](#print-dea-expiration-date-null-option)
    - [Print DISUSER DEA Expiration Date Null Option](#print-disuser-dea-expiration-date-null-option)
    - [Print DEA Expiration Date Expires 30 days Option](#print-dea-expiration-date-expires-30-days-option)
    - [Print DISUSER DEA Expiration Date Expires 30 days Option](#print-disuser-dea-expiration-date-expires-30-days-option)
    - [Print Prescribers with Privileges Option](#print-prescribers-with-privileges-option)
    - [Print DISUSER Prescribers with Privileges Option](#print-disuser-prescribers-with-privileges-option)
    - [Print PSDRPH Key Holders Option](#print-psdrph-key-holders-option)
    - [Print Setting Parameters Privileges Option](#print-setting-parameters-privileges-option)
    - [Print Audits for Prescriber Editing Option](#print-audits-for-prescriber-editing-option)
    - [Task Changes to DEA Prescribing Privileges Report Option](#task-changes-to-dea-prescribing-privileges-report-option)
    - [Task Allocation Audit of PSDRPH Key Report Option](#task-allocation-audit-of-psdrph-key-report-option)
    - [Allocate/De-Allocate of PSDRPH Key Option](#allocatede-allocate-of-psdrph-key-option)
    - [Edit Facility DEA# and Expiration Date Option](#edit-facility-dea-and-expiration-date-option)
    - [ePCS Edit Prescriber Data Option](#epcs-edit-prescriber-data-option)
    - [ePCS Set SAN from PIV Card Option](#epcs-set-san-from-piv-card-option)
  - [Prescription Validation and Verification Process—PKIServer.exe Application](#prescription-validation-and-verification-processpkiserverexe-application)
  - [PIV Card Validation—Revocation Server](#piv-card-validationrevocation-server)
  - [Windows Authentication and Cryptographic Operations](#windows-authentication-and-cryptographic-operations)
    - [History](#history-1)
    - [Current Capabilities](#current-capabilities)
    - [Future Capabilities](#future-capabilities)
- [National Provider Identifier (NPI)](#national-provider-identifier-npi)
  - [VHA and NPI](#vha-and-npi)
  - [NPI Registry and Data Files](#npi-registry-and-data-files)
  - [NPI VistA Options](#npi-vista-options)
    - [Adding NPI Options to Secondary Menu Options](#adding-npi-options-to-secondary-menu-options)
    - [List of NPI data for CBO Option](#list-of-npi-data-for-cbo-option)
    - [XUS NPI EXTRACT REPORT Option](#xus-npi-extract-report-option)
    - [NPI (National Provider ID) Menu](#npi-national-provider-id-menu)
    - [PROVIDER NPI SELF ENTRY Option](#provider-npi-self-entry-option)
  - [NPI APIs](#npi-apis)
  - [NPI RPCs](#npi-rpcs)
    - [XUS MVI ENRICH NEW PERSON](#xus-mvi-enrich-new-person)
  - [NPI Security Key](#npi-security-key)
  - [NPI Parameters](#npi-parameters)
    - [XUSNPI QUALIFIED IDENTIFIER Parameter](#xusnpi-qualified-identifier-parameter)
- [Service/Section Edit](#servicesection-edit)
  - [Overview](#overview)
  - [Menus and Options](#menus-and-options)
    - [User Information Menu](#user-information-menu)
    - [Service/Section Edit Option](#servicesection-edit-option)
  - [SERVICE/SECTION (#49) File Editable Fields](#servicesection-49-file-editable-fields)
    - [Service/Section Edit—Edit NAME Field](#servicesection-editedit-name-field)
    - [Service/Section Edit—Edit CLOSE SERVICE SECTION Field](#servicesection-editedit-close-service-section-field)
    - [Service/Section—Edit RE-OPEN SERVICE SECTION Field](#servicesectionedit-re-open-service-section-field)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Systems Management: Utilities User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*. These kernel utilities are programs to help users manage, maintain, and optimize their computer systems or Kernel application software.
This guide describes the following Kernel utilities:
- <u>Alerts</u>
- <u>Error Processing</u>
- <u>Lock Manager Utility</u>
- <u>DEA ePCS Utility</u>
- <u>National Provider Identifier (NPI)</u>

# Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Alerts User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you receive an alert, something on the computer system is requesting your immediate attention. A software application might issue an alert to one or more users when certain conditions are met (such as depleted stock levels or abnormal lab test results).

The first time you reach a menu prompt after receiving a particular alert, the alert’s message is displayed to you by the menu system. The alert message is displayed along with a standard notice to select the View Alerts \[XQALERT\] option on the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu) to process the alert (see <u>Figure 1</u>).

When you receive an alert, you should find out what the alert is asking of you and attend to it. This is called processing the alert.

Until you process all unprocessed alerts you receive, you’ll be reminded that you have pending alerts each time you are at a menu prompt. You do *not*, however, see the alert message; you only see that the first time you receive an alert and reach the menu prompt.

<span id="_Ref84815074" class="anchor"></span>Figure 1: Alert—Sample User Message

Dr. You need to enter a progress note on 'KRNPATIENT,ONE'.

Enter "VA VIEW ALERTS to review alerts

Select Systems Manager Menu Option:

### Processing Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To process alerts, choose the View Alerts \[XQALERT\] from the SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu). The View Alerts \[XQALERT\] option presents a list of all pending alerts, numbered consecutively with the most recent alerts listed first, except for Critical alerts (as of Kernel patch XU\*8.0\*602):

- Critical alerts move to the top of the list and are shown in reverse video.
- Critical alerts are identified by strings of text contained in the ALERT CRITICAL TEXT (#8992.3) file.

![](kernel-8-0-systems-management-utilities-user-guide/004.png) REF: For more information on Critical alerts, see Section <u>2.1.1.1</u>, “[Critical Alerts](#critical-alerts).”

Information-only alerts are displayed with the letter “I” in front of the alert message. When you process Information-only alerts, all that happens is that they are removed from the pending alerts list. Their only purpose was to send you a one-line alert message.

When you process alerts that are *not*Information-only, processing the alert may send you to a particular option or program. Afterwards, you are returned to the View Alerts screen if more alerts need processing, or back to the menu prompt if no pending alerts remain.

<u>Table 1</u> lists the various methods for processing alerts from the View Alerts screen. You can enter any of the alert process codes in <u>Table 1</u> (listed alphabetically):

| Process Code | Description                                                                                                                                                                                                                              |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A        | Process all alerts in the order shown.                                                                                                                                                                                                   |
| D        | Delete specific alerts (some alerts *cannot* be deleted). Only listed if one or more INFORMATION-ONLY alerts have been listed. If unable to delete an alert, users see: “Unable to delete alerts which require action: n,n,n, …” |
| F        | Forward one or more specific alerts. Forwarding may be sent as an alert to specific users or mail groups, a mail message, or sent to a specific printer.                                                                                 |
| I        | Process all INFORMATION-ONLY alerts. Only listed if one or more INFORMATION-ONLY alerts have been listed.                                                                                                                        |
| M        | List pending alerts in a mail message and deliver the message to your VistA MailMan IN basket.                                                                                                                                       |
| n        | Single number to process a single alert.                                                                                                                                                                                                 |
| n,n,n-n  | Range of numbers to process a range of alerts (such as 1,3,5-8).                                                                                                                                                                     |
| P        | Print a copy of the pending alerts to a printer.                                                                                                                                                                                         |
| R        | Redisplay available alerts.                                                                                                                                                                                                              |
| S        | Add or remove a surrogate to receive alerts for you. An optional start and end date can also be entered.                                                                                                                                 |
| ^        | Exit the alert processing screen by entering a caret (^).                                                                                                                                                                            |

<span id="_Ref508094065" class="anchor"></span>Table 2: Lock Manager—Options

The Alert Handler ordinarily deletes alerts once you have processed the alert. If you have processed all pending alerts and try to select the View Alerts \[XQALERT\] option, nothing is displayed. The View Alerts option only offers a listing when there are pending alerts; if no alerts are pending, the View Alerts option simply returns you to the menu prompt.

<span id="_Toc204765474" class="anchor"></span>Figure 2: View Alerts Option—Sample User Dialog

ACCESS CODES: <span class="mark">\*\*\*\*\*\*\*\*</span>

VERIFY CODES: <span class="mark">\*\*\*\*\*\*\*\*</span>

Good evening One You last signed on Jan 9,2004 at 14:39

Dr. You need to enter a progress note on 'KRNPATIENT,ONE'.

Enter "VA VIEW ALERTS to review alerts

Select Clinic Manager Menu Option: <span class="mark">"VA</span>

1\. Dr. You need to enter a progress note on 'KRNPATIENT,ONE'.

2\. Alk Phos elevated, schedule fu bone scan

3.I For your information, meeting at 12 noon, room 223

Select from 1 to 3

or enter ?, A, I, F, S, P, M, R, or ^ to exit: <span class="mark">?</span>

YOU MAY ENTER:

One or more numbers in the range 1 to 3 to select specific alert(s)

for processing. This may be a series of numbers, e.g., 2,3,6-9

A to process all of the pending alerts in the order shown.

I to process all of the INFORMATION ONLY alerts, if any, without further ado.

S to add or remove a surrogate to receive alerts for you

F to forward one or more specific alerts. Forwarding may be as an ALERT

to specific user(s) and/or mail group(s), or as a MAIL MESSAGE, or to a

specific PRINTER.

D to delete specific alerts (some alerts may not be deleted)

P to print a copy of the pending alerts on a printer

M to receive a MailMan message containing a copy of these pending alerts

R to Redisplay the available alerts

^ to exit

or RETURN to see additional pending ALERTS

Select from 1 to 3

or enter ?, A, I, F, S, P, M, R, or ^ to exit

or RETURN to continue:

#### Critical Alerts

The ALERT CRITICAL TEXT file (#8992.3) is a VistA file designed to accommodate the addition of Critical alerts in VistA. This file stores text entries that, when included in an alert, identify it as a Critical-type alert.

These file entries are used instead of hard-coded text within the following routines:

- XQALERT
- XQALERT1

Kernel Patch XU\*8.0\*690 modified the following reports output:

- [Critical Alerts Count Report](\l) \[XQAL CRITICAL ALERT COUNT\] option.
- [User Alerts Count Report](\l) \[XQAL USER ALERTS COUNT\] option.

Any Critical-type alerts preceded with the words "NOT" or “NON”, the only two supported Critical-type alert negation indicators, are automatically screened from these reports.

![](kernel-8-0-systems-management-utilities-user-guide/005.png) CAUTION: Alerts containing critical text that are *not* to be reported as Critical *must* obey the following rules to pass the Critical-type alert negation test:

- Only use the negation words “NOT” or “NON”.
- Negation words can be upper-, lower-, or mixed-case (that is *not* case-sensitive).
- Negation words *must* be followed by a single space and no other punctuation marks.

![](kernel-8-0-systems-management-utilities-user-guide/006.png) NOTE: The ALERT CRITICAL TEXT file (#8992.3) file was released with Kernel Patch XU\*8.0\*513.

As of 04/16/2018, the ALERT CRITICAL TEXT (#8992.3) file contains the following text entries that, when included in an alert, identify it as a Critical-type alert:

- ABNL IMA

![](kernel-8-0-systems-management-utilities-user-guide/007.png) NOTE: This entry was added with Kernel Patch XU\*8.0\*690.

- ABNORMAL IMA
- CRITICAL
- POSSIBLE MALIG
- TESTING-ALERTID-ONLY

Integration Control Registration (ICR) \#6869, ALERT CRITICAL TEXT LOOKUP AND EDIT, is a “Controlled Subscription” type ICR that allows application development teams to release patches that update the ALERT CRITICAL TEXT (#8992.3) file.

Specifically, ICR \#6869 grants permission to do the following:

- Look up alert Critical-type text using VA FileMan APIs, such as ^DIC or \$\$FIND1^DIC.
- Add or edit data in the ALERT CRITICAL TEXT (#8992.3) file using VA FileMan APIs, such as ^DIE, UPDATE^DIE, or FILE^DIE.

![](kernel-8-0-systems-management-utilities-user-guide/008.png) CAUTION: Application development teams making changes to the ALERT CRITICAL TEXT (#8992.3) file are responsible for confirming the change does *not* affect Kernel’s reporting of Critical-type alerts.  
  
When adding an entry with Critical-type text to the ALERT CRITICAL TEXT (#8992.3) file, be aware of the following:

- Reports any alert containing that text as Critical.
- Requires careful analysis to confirm changes do *not* cause malfunction of any VistA alerts.
- (*recommendation*) Indicate the associated application in the CREATING PACKAGE (#.03) field. Thus, any inquiries regarding the Critical alert text can be directed to the appropriate development team.
- Review and determine if the description in the PACKAGE-ID (#.02) field in the ALERT CRITICAL TEXT (#8992.3) file needs to be defined. That field's description indicates that data in this field can further screen alerts from being reported as critical. Its use should be understood when adding entries to the ALERT CRITICAL TEXT (#8992.3) file.  
    
  If the PACKAGE-ID (#.02) field in the ALERT CRITICAL TEXT (#8992.3) file is defined, then any alert entry in the ALERT (#8992) file containing the Critical text will only be reported as Critical when it’s data in the ALERT DATE/TIME sub-file (#8992.01) ALERT ID (#.02) field contains the data string in the PACKAGE-ID (#.02) field in the ALERT CRITICAL TEXT (#8992.3) file.  
    
  In other words, to report an alert as Critical based upon an entry in the ALERT CRITICAL TEXT file when the entry has defined the PACKAGE-ID, the ALERT CRITICAL TEXT file, PACKAGE-ID field data *must* be contained in the ALERT FILE, ALERT DATE/TIME file ALERT ID field.

### Deleting Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of Kernel patch XU\*8.0\*114, you can delete alerts by using the D alert processing code when using the View Alerts \[XQALERT\] option. The user can, if desired, delete specific alerts without viewing or processing them. This option provides the ability to delete “INFORMATION ONLY” alerts. Alerts that require processing *cannot* currently be deleted. However, if alerts requiring processing are created with the XQACNDEL variable set to 1 they too would be able to be deleted (that is the developer of the code that creates the alert can specify if it *must* be processed or can be deleted). Any alerts that were selected for deletion, but could *not* be deleted, are noted for the user.

The ability for the user to delete alerts other than INFORMATION ONLY requires that the developers within a software application decide that specific alerts, which would normally invoke processing through an option or routine, can be deleted specifically by the user *without* processing. They would then set the XQACNDEL variable to a value of 1 (one) prior to calling the SET^XQALERT API to set up the alert. Deletion of an alert by the user (or by system administrators or ADPACs using the existing option) is noted within the ALERT TRACKING (#8992.1) file as deletion by a user (with the user ID) *without* processing of the alert.

### Forwarding Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Beginning with Kernel 8.0, you can forward alerts by using the “F” alert processing code when viewing alerts. You can choose one or more alerts and forward them in the following ways:

- Forward as alerts to a specific user on the computer system.
- Forward as alerts to a mail group on the system.
- Copy alerts into mail messages and send to users and mail groups on the system.
- Print to an output device on the system (such as a printer).

### Surrogates and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Beginning with Kernel patch XU\*8.0\*114, you can designate or remove a surrogate for alerts by using the “S” alert processing code when viewing alerts. The user can, if desired, specify a start DATE/TIME or an end DATE/TIME for the surrogate to be effective. If a start DATE/TIME is *not* specified, the surrogate becomes active immediately. If an end DATE/TIME is specified, the surrogate is removed automatically effective with the first alert sent to the user after the end DATE/TIME has passed. If an end DATE/TIME is *not* specified, the surrogate is active until another surrogate is specified or the user removes the surrogate.

As of Kernel patch XU\*8.0\*602, entering a start or end DATE/TIME in the past is *not* permitted:

- If a date is entered, then a time is also required.
- If a start date or end date is entered *without* the year and appending the *current* year creates a date in the past, then the next *future* year is appended to the date.

A message is sent to the surrogate to indicate that he has been designated as a surrogate, and a message is sent when the surrogate is removed.

If the user has no alerts and selects the View Alerts \[XQALERT\] option, he is asked if he wants to add or remove a surrogate. The Alerts - Set/Remove Surrogate for User \[XQALERT SURROGATE SET/REMOVE\] option is also provided. It can be used by system administrators or ADPACs to add or remove a surrogate for a selected user. This option is located on the Alert Management \[XQALERT MGR\] menu.

As of Kernel Patch XU\*8.0\*730, after running the Alerts - Set/Remove Surrogate for User \[XQALERT SURROGATE SET/REMOVE\] option, you can see some examples of surrogate periods for a user, as shown in <u>Figure 3</u> and <u>Figure 4</u>:

<span id="_Ref45778965" class="anchor"></span>Figure 3: Display of Surrogate Periods—Surrogate with a START DATE and an END DATE

Current Surrogate(s): START DATE END DATE

<span class="mark">1 SURROGATE,ONE May 11, 2020@19:31:29 May 18, 2020@00:01</span>

<span id="_Ref45802625" class="anchor"></span>Figure 4: Display of Surrogate Periods——Surrogate with a START DATE and No END DATE

Current Surrogate(s): START DATE END DATE

<span class="mark">1 SURROGATE,ONE May 11, 2020@19:31:29</span>

#### Multiple Sequential Surrogate Periods

Scheduling multiple, sequential, surrogate periods have been available beginning with Kernel Patch XU\*8.0\*366, but their usage was *not* documented at the time. As of Kernel Patch XU\*8.0\*730, these surrogate periods are now being documented.

The surrogate periods are sequential; that is, one period ends when the next period starts. Only the last surrogate period has no end DATE/TIME specified.

<u>Figure 5</u> shows an example of creating multiple sequential surrogate periods:

<span id="_Ref45779508" class="anchor"></span>Figure 5: Multiple Sequential Surrogate Periods

Select OPTION NAME: <span class="mark">XQALERT SURROGATE SET/REMOVE</span><span class="mark">\<Enter\></span> Alerts - Set/Remove Surrogate for User

Alerts - Set/Remove Surrogate for User

SURROGATE related to which

NEW PERSON entry: <span class="mark">USER,ONE \<Enter\></span>

No current surrogates

Do you want to SET a new surrogate recipient? NO// <span class="mark">YES</span>

Select USER to be SURROGATE: <span class="mark">SURROGATE,ONE \<Enter\></span>

Enter Date/Time SURROGATE is to start: (MAY 11, 2020@19:31:24-DEC 31, 2699): <span class="mark">\<Enter\></span>

Enter Date/Time SURROGATE is to end: (MAY 11, 2020@19:31:27-DEC 31, 2699): <span class="mark">\<Enter\></span>

Current Surrogate(s): START DATE END DATE

<span class="mark">1 SURROGATE,ONE May 11, 2020@19:31:29</span>

Do you want to SET a new surrogate recipient? NO// <span class="mark">YES \<Enter\></span>

Select USER to be SURROGATE: <span class="mark">SURROGATE,TWO \<Enter\></span>

Enter Date/Time SURROGATE is to start: (MAY 11, 2020@19:36:22-DEC 31, 2699): <span class="mark">May 18@00:01 \<Enter\></span> (MAY 18, 2020@00:01)

Enter Date/Time SURROGATE is to end: (MAY 11, 2020@19:36:55-DEC 31, 2699): <span class="mark">\<Enter\></span>

Current Surrogate(s): START DATE END DATE

<span class="mark">1 SURROGATE,ONE May 11, 2020@19:31:29 May 18, 2020@00:01</span><span class="mark">2 SURROGATE,TWO May 18, 2020@00:01</span>

Do you want to SET a new surrogate recipient? NO// YES

Select USER to be SURROGATE: <span class="mark">SURROGATE,THREE \<Enter\></span>

Enter Date/Time SURROGATE is to start: (MAY 11, 2020@19:44:04-DEC 31, 2699): <span class="mark">May 25@00:01 \<Enter\></span> (MAY 25, 2020@00:01)

Enter Date/Time SURROGATE is to end: (MAY 11, 2020@19:44:24-DEC 31, 2699): <span class="mark">June 01@00:01 \<Enter\></span> (JUN 01, 2020@00:01)

Current Surrogate(s): START DATE END DATE

<span class="mark">1 SURROGATE,ONE May 11, 2020@19:31:29 May 18, 2020@00:01</span><span class="mark">2 SURROGATE,TWO May 18, 2020@00:01 May 25, 2020@00:01</span><span class="mark">3 SURROGATE,THREE May 25, 2020@00:01 Jun 01, 2020@00:01</span>

Do you want to SET a new surrogate recipient? NO// \<Enter\>

#### Transitive Surrogates

Transitive surrogates occur when a user has a surrogate for a time-period (Surrogate Period 1), and the surrogate also has a surrogate for a time-period (Surrogate Period 2) that coincides with part of the Surrogate Period 1; however, this functionality was broken since Kernel patch XU\*8.0\*513, where the Surrogate Period 1 was inadvertently removed. This problem has been fixed as of Kernel Patch XU\*8.0\*730. For examples, see <u>Figure 6</u> and <u>Figure 7</u>.

#### Example 1

Step 1: Parent Surrogate Period: USER,ONE has one surrogate period with SURROGATE,ONE, as shown in <u>Figure 6</u>:

<span id="_Ref45780963" class="anchor"></span>Figure 6: Transitive Surrogates—Step 1: Parent Surrogate Period

Select OPTION NAME: <span class="mark">XQALERT SURROGATE SET/REMOVE \<Enter\></span> Alerts - Set/Remove Surrogate for User

Alerts - Set/Remove Surrogate for User

SURROGATE related to which

NEW PERSON entry: <span class="mark">USER,ONE \<Enter\></span>

Current Surrogate(s): START DATE END DATE

<span class="mark">1 SURROGATE,ONE May 11, 2020@19:31:29</span>

Do you want to REMOVE THIS surrogate recipient? NO// <span class="mark">\<Enter\></span>

Do you want to SET a new surrogate recipient? NO// <span class="mark">\<Enter\></span>

#### Example 2

Step 2: Child (Transitive) Surrogate Period: SURROGATE,ONE has one surrogate period with SURROGATE,TWO, as shown in <u>Figure 7</u>:

<span id="_Ref45803109" class="anchor"></span>Figure 7: Transitive Surrogates—Step 2: Child (Transitive) Surrogate Period

Select OPTION NAME: <span class="mark">XQALERT SURROGATE SET/REMOVE \<Enter\></span> Alerts - Set/Remove Surrogate for User

Alerts - Set/Remove Surrogate for User

SURROGATE related to which

NEW PERSON entry: <span class="mark">SURROGATE,ONE \<Enter\></span>

Select USER to be SURROGATE: <span class="mark">SURROGATE,TWO \<Enter\></span>

Enter Date/Time SURROGATE is to start: (MAY 11, 2020@20:04:42-DEC 31, 2699): <span class="mark">T+1@00:01 \<Enter\></span>

Enter Date/Time SURROGATE is to end: (MAY 11, 2020@20:04:57-DEC 31, 2699): <span class="mark">T+2@00:01 \<Enter\></span> (MAY 12, 2020@00:01)

Current Surrogate(s): START DATE END DATE

<span class="mark">1 SURROGATE,TWO May 12, 2020@00:01 May 13, 2020@00:01</span>

Do you want to SET a new surrogate recipient? NO// <span class="mark">\<Enter\></span>

## Alerts System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An alert notifies one or more users of a matter requiring immediate attention. Thus, alerts function as brief notices that are distinct from mail messages or triggered bulletins.

Starting with Kernel 8.0, alerts are stored in the ALERT (#8992) file, which are stored in the ^XTV(8992, global. Also, the ALERT TRACKING (#8992.1) file, stored in ^XTV(8992.1,) provides a means to track alerts and users’ responses to alerts.

For each user to whom an alert is sent, the ALERT TRACKING (#8992.1) file stores the following data:

- Alert name.
- Date created.
- Software identifier of alert.
- User who generated the alert.
- Message text of the alert.
- Action associated with the alert.
- Data associated with the alert.

For each recipient of the alert, the ALERT TRACKING (#8992.1) file stores the following data:

- First date and time observed (shown in menu cycle).
- First date and time selected for processing.
- Date and time processing completed (if any).
- Date and time alert was deleted.
- Forwarding information—If alert was forwarded:
- User who forwarded it.
- Date and time of forwarding.
- Surrogate information—If a surrogate was added for alerts:
- User who was the surrogate.
- Date and time of the surrogate.

The PATIENT^XQALERT and USER^XQALERT functions provide access to information in the ALERT TRACKING (#8992.1) file.

![](kernel-8-0-systems-management-utilities-user-guide/009.png) REF: For a description of the XQALERT and other alert-related APIs, see the [*Kernel 8.0 Developer’s Guide: Alerts: Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_alerts_ug.pdf). Kernel and Kernel Toolkit APIs are also available in HTML format at a VA Intranet Website.

### Alert Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Alert Management \[XQALERT MGR\] menu contains the options shown in <u>Figure 8</u>:

<span id="_Ref178564462" class="anchor"></span>Figure 8: Alert Management Menu Options

SYSTEMS MANAGER MENU ... \[EVE\]

Operations Management ... \[XUSITEMGR\]

Alert Management... \[XQALERT MGR\]

SURO Alerts - Set/Remove Surrogate for User \[XQALERT SURROGATE SET/REMOVE\]

Delete Old (\>14 d) Alerts \[XQALERT DELETE OLD\]

Make an Alert on the fly \[XQALERT MAKE\]

Purge Alerts for a User \[XQALERT BY USER DELETE\]

\*\*\> Locked with XQAL-DELETE

Report Menu for Alerts ... \[XQAL REPORTS MENU\]

Set Backup Reviewer for Alerts \[XQAL SET BACKUP REVIEWER\]

Surrogate for which Users? \[XQAL SURROGATE FOR WHICH USERS\]

#### Alerts - Set/Remove Surrogate for Users Option

The Alerts - Set/Remove Surrogate for User \[XQALERT SURROGATE SET/REMOVE\] option is provided so that system administrators or ADPAC personnel can do the following:

- Set a surrogate to receive alerts for a user.
- Remove a surrogate from receiving alerts for a user.

The option asks for a user to be selected, then is ready to specify a new surrogate for the selected user, or to remove the current surrogate for that user.

This option is *not* needed by the individual users who may select to name or remove a surrogate as one of the options while processing alerts (or if no alerts are present for the user, as their only option on selecting alert processing).

#### Delete Old (\>14 d) Alerts Option

![](kernel-8-0-systems-management-utilities-user-guide/010.png) NOTE: Kernel Patch XU\*8\*798 addressed accidental purging of alerts by eliminating interactive use of the Delete Old (\>14 d) Alerts \[XQALERT DELETE OLD\] option. This option remains on the Alert Management \[XQALERT MGR\] and Operations Management \[XUSITEMGR\] menus, but you are only able to invoke it from TaskMan.

The Delete Old (\>14 d) Alerts \[XQALERT DELETE OLD\] option performs the following functions:

- Purges unprocessed alerts from the ALERT (#8992) file.
- Forwards unprocessed alerts to the Backup Reviewer or Supervisor.

![](kernel-8-0-systems-management-utilities-user-guide/011.png) NOTE: As of Kernel Patch XU\*8.0\*772, entries in the ALERT TRACKING (#8992.1) file are *not* deleted but retained as per a litigation hold, which specifically addressed ServiceNow (SNOW) Ticket INC \#24097729.

The Delete Old (\>14 d) Alerts \[XQALERT DELETE OLD\] option purges all alerts that have been unprocessed for longer than a specified retention period (the default is 14 days). It is assumed that an alert becomes obsolete within this period and can be purged by system administrators when invoked from TaskMan. Due to the number of tasks performed by this option, it should be queued through TaskMan on a regular basis. The suggested scheduling frequency is once every day. This option also performs additional functions, which are described below.

Although it is *not recommended* to increase the retention period, since alerts require the initial recipient’s immediate attention, you can specify a retention period other than the 14-day default when you queue the option by using the TASK PARAMETERS field of the OPTION SCHEDULING (#19.2) file. If you put a numeric value in the TASK PARAMETERS field of the OPTION SCHEDULING (#19.2) file, this value replaces the default alert retention value of 14 days. If you set a numeric value in this field that is longer than the default value, try to make it temporary and remove the value when it is no longer needed, so that the default value of 14 days for the retention period is used.

In addition to purging old alerts, the routine for this option is also responsible for forwarding unprocessed alerts to the next designated recipient, such as supervisors and surrogates (if this was requested when the alert was created). However, if the period to wait before forwarding exceeds the purging retention period used by this option, the alerts are purged rather than forwarded. Alerts that go unprocessed by the initial recipient that are also not forwarded on to SURROGATES, SERVICE CHIEFS, and/or BACKUP REVIEWERS can pose a risk to patient safety.

#### Make an Alert on the Fly Option

The Make an Alert on the Fly \[XQALERT MAKE\] option allows you to generate an alert on the fly. It interactively asks you for the alert message, recipients, and alert action, if any (you can specify an alert action type of routine or option). It then generates the alert on the fly.

This option is *recommended* primarily for system administrators and ADPACs; it may or may not be appropriate for other selected users.

![](kernel-8-0-systems-management-utilities-user-guide/012.png) NOTE: This option does *not* allow the user to set the CAN DELETE WITHOUT PROCESSING (#.1) field in the ALERT (#8992) file.

#### Purge Alerts for a User Option

The Purge Alerts for a User \[XQALERT BY USER DELETE\] option allows you to delete alerts for a user. The main purpose of this option is to provide a way to delete alerts for a user who has been inactive for a time-period (such as on leave), and who has accumulated several alerts that should *not* need processing.

This option is locked with the XQAL-DELETE security key, and it should only be used by system administrators or ADPACs.

#### Report Menu for Alerts Menu

The Report Menu for Alerts \[XQAL REPORTS MENU\] menu provides several options for generating reports on alerts for users or patients. It consists of the submenu items shown in <u>Figure 9</u>:

<span id="_Ref511294832" class="anchor"></span>Figure 9: Report Menu for Alerts Menu Options

Select Report Menu for Alerts Option: <span class="mark">?? \<Enter\></span>

Critical Alerts Count Report \[XQAL CRITICAL ALERT COUNT\]

List Alerts for a user from a specified date \[XQAL ALERT LIST FROM DATE\]

Patient Alert List for specified date \[XQAL PATIENT ALERT LIST\]

User Alerts Count Report \[XQAL USER ALERTS COUNT\]

View data for Alert Tracking file entry \[XQAL VIEW ALERT TRACKING ENTRY\]

#### Critical Alerts Count Report Option

The Critical Alerts Count Report \[XQAL CRITICAL ALERT COUNT\] option is used to generate a report of users who have alerts defined as Critical based upon inclusion of text entries from the ALERT CRITICAL TEXT (#8992.3) file between the specified start and end dates. For example, Critical-type alerts contain the following words:

- ABNL IMA

![](kernel-8-0-systems-management-utilities-user-guide/013.png) NOTE: This entry was added with Kernel Patch XU\*8.0\*690.

- ABNORMAL IMA
- CRITICAL
- POSSIBLE MALIG

How the report is presented depends on the order by which method the user selects:

- Name—Report lists items alphabetized by name.
- Number—Report list items in descending order for the number of Critical-type alerts present.

Kernel Patch XU\*8.0\*690 modified the Critical Alerts Count Report output, so any Critical-type alerts preceded with the words "NOT" or “NON”, the only two supported Critical-type alert negation indicators, are automatically screened from this report.

![](kernel-8-0-systems-management-utilities-user-guide/014.png) CAUTION: Alerts containing critical text that are *not* to be reported as Critical *must* obey the following rules to pass the Critical-type alert negation test:

- Only use the negation words “NOT” or “NON”.
- Negation words can be upper-, lower-, or mixed-case (that is *not* case-sensitive).
- Negation words *must* be followed by a single space and no other punctuation marks.

![](kernel-8-0-systems-management-utilities-user-guide/015.png) REF: For more information on Critical-type alerts, see Section [10.1.1.1](#critical-alerts), “[Critical Alerts](#critical-alerts).”

For each user who has the specified number of Critical-type alerts or more, the report includes the following:

- Name—User name.
- Service/Section—Section/Service for the user.
- Alerts—Number of alerts in the ALERT (#8992) file.
- Last Sign-on—Last sign-on date.
- CRIT—Number of alerts with Critical-type text.
- Alert—Date of the oldest alert.

#### Error Handling—Missing SERVICE/SECTION Data

As of Kernel Patch XU\*8.0\*690, the Critical Alerts Count Report \[XQAL CRITICAL ALERT COUNT\], and User Alerts Count Report \[XQAL USER ALERTS COUNT\] Kernel alert report options no longer abort but gracefully handle reporting users that are missing the SERVICE/SECTION (#29) field data in their NEW PERSON (#200) file definitions.

![](kernel-8-0-systems-management-utilities-user-guide/016.png) NOTE: The examples in this section apply to both the Critical Alerts Count Report \[XQAL CRITICAL ALERT COUNT\] and User Alerts Count Report \[XQAL USER ALERTS COUNT\] options, since both options use the same Application Programming Interfaces (APIs).

Using either the Critical Alerts Count Report \[XQAL CRITICAL ALERT COUNT\], or User Alerts Count Report \[XQAL USER ALERTS COUNT\] options, the system no longer aborts but lists those entries missing the SERVICE/SECTION (#29) field data. For example:

1.  Execute the Critical Alerts Count Report \[XQAL CRITICAL ALERT COUNT\] option, located on the Report Menu for Alerts \[XQAL REPORTS MENU\] menu (<u>Figure 10</u>).
1.  Change users with Critical Alerts of at least 10 to 1.
2.  At the “Display users whose CRITICAL ALERT count is at least: 10//” prompt, enter 1.
3.  Enter a start date prior to the DATE/TIME of the pending alert for the active user missing SERVICE/SECTION data.
4.  Enter an end date following the DATE/TIME of the pending alert for the active user missing SERVICE/SECTION data.
5.  Do *not* break out by one or more divisions.
6.  Order results “By Service/Section”.
7.  Sub-sort the results “By Name”.
8.  Notice that the report will list \<No Service\> for users missing SERVICE/SECTION data. If the Kernel System Parameter limiting the number of errors trapped each day is exceeded, a message is included on the report to note the users who will *not* have error trap entries, as shown in <u>Figure 10</u>.

> <span id="_Ref522628585" class="anchor"></span>Figure 10: Testing Reports with Missing Service/Section Data—Critical Alerts Count Report \[XQAL CRITICAL ALERT COUNT\] Option

Select Report Menu for Alerts \<TEST ACCOUNT\> Option: <span class="mark">Critical Alerts Count Report \<Enter\></span>

Display users whose CRITICAL ALERT count is at least:  10// <span class="mark">1</span>

START DATE: <span class="mark">12/1/17 \<Enter\></span>

END DATE: <span class="mark">T \<Enter\></span>

Breakout by One or More Divisions? <span class="mark">NO \<Enter\></span>

     Select one of the following:

                   

          1         By Name

          2         By Number

          <span class="mark">3         By Service/Section</span>

Select the ordering of results desired: <span class="mark">3 \<Enter\></span>

Show ALL Service/Sections? <span class="mark">YES \<Enter\></span>

     Select one of the following:

                    

          1         By Name

          2         By Number

Within Service/Section order results by: <span class="mark">1 \<Enter\></span>

DEVICE: HOME// <span class="mark">\<Enter\></span> Right Margin: 80// <span class="mark">*\<Select Device and Margin\>* \<Enter\></span>

COUNT of ALERTS - users with more than 1 on Jul 31, 2018@10:45:54

   for date range 12/01/2017 to 07/31/2018

CRIT column indicates number of alerts containing critical text

                                 Total             Oldest

Name           Service/section   Alerts Last Sign-on  CRIT   Alert

------------   ----------------- ------ ------------  ---- ---------

XUSTUDENT,EIGHTEEN <span class="mark">\<No Service\></span> 1           1 07/30/2018

XUSTUDENT,ELEVEN <span class="mark">\<No Service\></span> 1     AUG 01, 1996 1    07/30/2018

XUSTUDENT,FIFTEEN <span class="mark">\<No Service\></span> 1                   1    07/30/2018

XUSTUDENT,FOURTEEN <span class="mark">\<No Service\></span> 1             1    07/30/2018

XUSTUDENT,NINETEEN <span class="mark">\<No Service\></span> 1                  1    07/30/2018

XUSTUDENT,SEVENTEEN <span class="mark">\<No Service\></span> 1                 1    07/30/2018

XUSTUDENT,SIXTEEN <span class="mark">\<No Service\></span> 1                1    07/30/2018

XUSTUDENT,THIRTEEN <span class="mark">\<No Service\></span> 1                 1    07/30/2018

XUSTUDENT,THIRTY <span class="mark">\<No Service\></span> 1                 1    07/30/2018

XUSTUDENT,THIRTYONE <span class="mark">\<No Service\></span> 1               1    07/30/2018

<span class="mark">Daily Error Trap limit is 100 errors for users missing SERVICE/SECTION.</span>

<span class="mark">Limit Reached.  No more entries will be added for '\<No Service\>' users today!</span>

XUSTUDENT,TWELVE <span class="mark">\<No Service\></span> 1    AUG 02, 1996  1    07/30/2018

XUSTUDENT,TWENTY <span class="mark">\<No Service\></span> 1                1    07/30/2018

XUSTUDENT,28 <span class="mark">\<No Service\></span> 1               1    07/30/2018

Type \<Enter\> to continue or '^' to exit:

As you can see in <u>Figure 10</u>, the report runs to completion without aborting; even though there are entries with missing SERVICE/SECTION data for multiple users (that is indicated on the report as \<No Service\>). The report option indicates *all* entries that are missing SERVICE/SECTION data. It also writes an entry in the error log for a fixed number of entries up to the Daily Error Trap limit.

Once that limit has been reached for this error, the option displays a message that no more entries will be added to the error log, as shown in <u>Figure 11</u>:

> <span id="_Ref522629954" class="anchor"></span>Figure 11: Sample Error Limit Reached Message for Users Missing SERVICE/SECTION Data

Daily Error Trap limit is 100 errors for users missing SERVICE/SECTION.

Limit Reached.  No more entries will be added for '\<No Service\>' users today!

The example in <u>Figure 12</u> uses the User Alerts Count Report \[XQAL USER ALERTS COUNT\] option:

<span id="_Ref522696707" class="anchor"></span>Figure 12: Testing Reports with Missing Service/Section Data—User Alerts Count Report \[XQAL USER ALERTS COUNT\] Option

Select Report Menu for Alerts \<TEST ACCOUNT\> Option: <span class="mark">USER Alerts Count Report \<Enter\></span>

Do you want to count only alerts containing specific words or phrase(s)? <span class="mark">NO \<Enter\></span>

Display users whose ALERT count is at least:  100// <span class="mark">1 \<Enter\></span>

START DATE: <span class="mark">12/1/17 \<Enter\></span> (DEC 01, 2017)

END DATE: <span class="mark">T \<Enter\></span> (AUG 22, 2018)

Breakout by One or More Divisions? <span class="mark">NO \<Enter\></span>

     Select one of the following:

                   

          1         By Name

          2         By Number

          <span class="mark">3         By Service/Section</span>

Select the ordering of results desired: <span class="mark">3 \<Enter\></span> By Service/Section

Show ALL Service/Sections? <span class="mark">YES \<Enter\></span>

     Select one of the following:

                   

          <span class="mark">1         By Name</span>

          2         By Number

Within Service/Section order results by: <span class="mark">1 \<Enter\></span> By Name

DEVICE: HOME// <span class="mark">UCX/TELNET \<Enter\></span> Right Margin: 80// <span class="mark">\<Enter\></span>

COUNT of ALERTS - users with more than 1 on Aug 22, 2018@07:09:24

   for date range 12/01/2017 to 08/22/2018

CRIT column indicates number of alerts containing critical text

                                            Total                     Oldest

Name                     Service/section   Alerts Last Sign-on  CRIT   Alert

-----------------        ----------------- ------ ------------  ---- ----------

    <span class="mark">Daily Error Trap limit is 10 errors for users missing SERVICE/SECTION.</span>

<span class="mark">  Limit Reached.  No more entries will be added for '\<No Service\>' users today!</span>

XUSTUDENT,EIGHTEEN       <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,ELEVEN         <span class="mark">\<No Service\></span>      1      AUG 01, 1996  1    07/30/2018

XUSTUDENT,FIFTEEN        <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,FOURTEEN       <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,NINETEEN       <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,SEVENTEEN     <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,SIXTEEN        <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,THIRTEEN     <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,THIRTY         <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,THIRTYONE      <span class="mark">\<No Service\></span>      1                    1    07/30/2018

XUSTUDENT,TWELVE         <span class="mark">\<No Service\></span>      1      AUG 02, 1996  1    07/30/2018

XUSTUDENT,TWENTY         <span class="mark">\<No Service\></span>      1                    1    07/30/2018

Type \<Enter\> to continue or '^' to exit:

As you can see in <u>Figure 12</u>, the report runs to completion without aborting; even though there are entries with missing SERVICE/SECTION data for multiple users (that is indicated on the report as \<No Service\>). The report option indicates *all* entries that are missing SERVICE/SECTION data. It also writes an entry in the error log for a *fixed number* of entries up to the Daily Error Trap limit.

Once that limit has been reached for this error, the option displays a message that no more entries will be added to the error log. In this example ( <u>Figure 12</u>), the limit was reached before the system started listing entries to the report, so the error limit message (<u>Figure 11</u>) appears at the top of the report.

#### List Alerts for a user from a specified date Option

The List Alerts for a user from a specified date \[XQAL ALERT LIST FROM DATE\] option reports all alerts from the ALERT TRACKING (#8992.1) file for a selected user within a specified date range. If an end date is *not* specified, the report does *not* run.

The listing includes the following:

- Internal Entry Number (IEN) for the alert in the ALERT TRACKING (#8992.1) file.
- Date and time the alert was generated.
- Message text of the alert.
- Information about any option or routine to be executed for processing the alert.

#### Patient Alert List for specified date Option

The Patient Alert List for specified date \[XQAL PATIENT ALERT LIST\] option is used to obtain a list of alerts for a specified patient from the ALERT TRACKING (#8992.1) file for a selected date.

A prompt is provided to obtain a quick scan listing of dates with at least some alerts for the patient on it based on OR and DVB alerts (other patient related alerts need to be identified by looking at each alert’s message text and are included in the full list, but *not* the quick scan).

The listing includes the following:

- Internal Entry Number (IEN) for the alert in the ALERT TRACKING (#8992.1) file.
- Date and time the alert was generated.
- Message text of the alert.
- Information about any option or routine to be executed for processing the alert.

#### User Alerts Count Report Option

The User Alerts Count Report \[XQAL USER ALERTS COUNT\] option is used to generate a report on users who have more than a specified number of alerts in the ALERT (#8992) file. This report also includes users who have alerts defined as Critical based upon inclusion of text entries from the ALERT CRITICAL TEXT (#8992.3) file. For example, Critical-type alerts containing the following words:

- ABNL IMA

![](kernel-8-0-systems-management-utilities-user-guide/017.png) NOTE: This entry was added with Kernel Patch XU\*8.0\*690.

- ABNORMAL IMA
- CRITICAL
- POSSIBLE MALIG

Kernel Patch XU\*8.0\*690 modified the User Alerts Count Report output, so any Critical-type alerts preceded with the words "NOT" or “NON”, the only two supported Critical-type alert negation indicators, are automatically screened from this report.

![](kernel-8-0-systems-management-utilities-user-guide/018.png) CAUTION: Alerts containing critical text that are *not* to be reported as Critical *must* obey the following rules to pass the Critical-type alert negation test:

- Only use the negation words “NOT” or “NON”.
- Negation words can be upper-, lower-, or mixed-case (that is *not* case-sensitive).
- Negation words *must* be followed by a single space and no other punctuation marks.

![](kernel-8-0-systems-management-utilities-user-guide/019.png) REF: For more information on Critical-type alerts, see Section [10.1.1.1](#critical-alerts), “[Critical Alerts](#critical-alerts).”

The report covers a specified range of dates. It can be sorted by any of the following data:

- User name.
- Number of alerts.
- Service/Section.

In addition, the report in each of these formats may be generated by Divisions if desired.

For each user who has the specified number of alerts or more, the report includes the following:

- Name—User name.
- Service/Section—Section/Service for the user.
- Alerts—Number of alerts in the ALERTS (#8992) file.
- Last Sign-on—Last sign-on date.
- CRIT—Number of alerts with Critical-type text.
- Alert—Date of the oldest alert.

![](kernel-8-0-systems-management-utilities-user-guide/020.png) NOTE: For error handling of missing SERVICE/SECTION (#29) field data with the User Alerts Count Report \[XQAL USER ALERTS COUNT\] and Critical Alerts Count Report \[XQAL CRITICAL ALERT COUNT\] options, see Section <u>2.2.1.5.1.1</u>, “[Error Handling—Missing SERVICE/SECTION Data](#error-handlingmissing-servicesection-data).”

#### View data for Alert Tracking file entry Option

The View data for Alert Tracking file entry \[XQAL VIEW ALERT TRACKING ENTRY\] option can be used to view data for one or more entries in the ALERT TRACKING (#8992.1) file in captioned format. The internal entry numbers for the entries to be displayed *must* be entered individually.

#### Set Backup Reviewer for Alerts Option

The Set Backup Reviewer for Alerts \[XQAL SET BACKUP REVIEWER\] option provides a mechanism for a user to set entries into the PARAMETERS (#8989.5) file. It assigns an individual as the “Backup Reviewer for Unprocessed Alerts,” which is the DISPLAY TEXT (#.02) field for the “XQAL BACKUP REVIEWER” entry in the NAME (#.01) field in the PARAMETER DEFINITION (#8989.51) file, if there is a date specified in the DAYS FOR BACKUP REVIEWER (#.15) field in the ALERT DATE/TIME (#.01) Multiple field in the ALERT (#8992) file for that alert.

If this is the case, an alert that remains unread for the specified number of days is forwarded to the “Backup Reviewer for Unprocessed Alerts” indicated at the lowest level found for processing for the user in the PARAMETERS (#8989.5) file. The following is the processing order (listed lowest to highest level):

1.  User
2.  OERR Team
3.  Team
4.  Service
5.  Division
6.  System

![](kernel-8-0-systems-management-utilities-user-guide/021.png) NOTE: This option was released with Kernel patch XU\*8.0\*174.

#### XQAL UNPROCESSED ALERTS Mail Group

There are two mechanisms to send unprocessed alerts:

- The [Set Backup Reviewer for Alerts \[XQAL SET BACKUP REVIEWER\]](#set-backup-reviewer-for-alerts-option) option sets the “BACKUP REVIEWER” entries in the PARAMETERS (#8989.5) file to whom you can send the alert.
- The XQAL UNPROCESSED ALERTS mail group is set up to provide a place to send unprocessed alerts if the “BACKUP REVIEWER” entries in the PARAMETERS (#8989.5) file are *not* available.  
    
  If the “BACKUP REVIEWER” entries in the PARAMETERS (#8989.5) file are available, then alerts will *not* be sent to this mail group. This mail group is only used if the other mechanism results in no active users.

#### Surrogate for which Users? Option

The Surrogate for which Users? \[XQAL SURROGATE FOR WHICH USERS\] option provides a view of which users have specified a selected user as surrogates for themselves.

### Troubleshooting Using ALERT TRACKING (#8992.1) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Simple Alert to INITIAL RECIPIENT

<u>Figure 13</u> is an example of a simple alert that was generated by user SENDER and delivered to user RECIPIENT,ORIGINAL:

- Actual recipient is the one with the RECIPIENT TYPE as INITIAL RECIPIENT.
- Alert has *not* been viewed nor processed by the recipient.

<span id="_Ref145512499" class="anchor"></span>Figure 13: Sample Output—Simple Alert to INITIAL RECIPIENT

NAME: NO-ID;76;3230815.140237 DATE CREATED: AUG 15, 2023@14:02:37

PKG ID: NO-ID GENERATED BY: <span class="mark">SENDER</span>

DISPLAY TEXT: A Simple Alert ROUTINE TAG: EN

ROUTINE FOR PROCESSING: AROUTINE

RECIPIENT: <span class="mark">RECIPIENT,ORIGINAL</span>

RECIPIENT TYPE: <span class="mark">INITIAL RECIPIENT</span> ALERT DATE/TIME: AUG 15, 2023@14:02:37

When the user views and processes the alert, the entry is updated as shown in <u>Figure 14</u>.

![](kernel-8-0-systems-management-utilities-user-guide/022.png) NOTE: Typically, it is expected that the time stamp is the same for the following pairs of fields:

- ALERT FIRST DISPLAYED and FIRST SELECTED ALERT.
- PROCESSED ALERT and DELETED ON.

<span id="_Ref145512635" class="anchor"></span>Figure 14: Sample Output—When the User Views and Processes the Alert

NAME: NO-ID;76;3230815.140237 DATE CREATED: AUG 15, 2023@14:02:37

PKG ID: NO-ID GENERATED BY: SENDER

DISPLAY TEXT: A Simple Alert ROUTINE TAG: EN

ROUTINE FOR PROCESSING: AROUTINE

RECIPIENT: RECIPIENT,ORIGINAL

<span class="mark">ALERT FIRST DISPLAYED: AUG 16, 2023@10:15:02</span>

<span class="mark">FIRST SELECTED ALERT: AUG 16, 2023@10:15:02</span>

<span class="mark">PROCESSED ALERT: AUG 16, 2023@10:17:13</span>

<span class="mark">DELETED ON: AUG 16, 2023@10:17:13</span>

RECIPIENT TYPE: INITIAL RECIPIENT ALERT DATE/TIME: AUG 15, 2023@14:02:37

#### Alert to Surrogate—Who Processes the Alert

When a user has a surrogate and an alert is addressed to the user during the surrogate period, the alert is instead delivered to the surrogate (<u>Figure 15</u>):

- Actual recipient is the one with the RECIPIENT TYPE as INITIAL RECIPIENT-SURROGATE.
- Alert has *not* been viewed nor processed by any of the recipients.

<span id="_Ref145512867" class="anchor"></span>Figure 15: Sample Output—Alert to Surrogate who Processes the Alert

NAME: NO-ID;76;3230728.150546 DATE CREATED: JUL 28, 2023@15:05:46

PKG ID: NO-ID GENERATED BY: SENDER

DISPLAY TEXT: Alert during surrogacy ROUTINE TAG: EN

ROUTINE FOR PROCESSING: AROUTINE

RECIPIENT: RECIPIENT,ORIGINAL

RECIPIENT TYPE: INITIAL RECIPIENT <span class="mark">SENT TO SURROGATE: SURROGATE,ONE</span>

ALERT DATE/TIME: JUL 28, 2023@15:05:46

<span class="mark">RECIPIENT: SURROGATE,ONE</span>

<span class="mark">RECIPIENT TYPE: INITIAL RECIPIENT-SURROGATE</span>

<span class="mark">ACTING AS SURROGATE: YES</span> <span class="mark">ALERT DATE/TIME: JUL 28, 2023@15:05:46</span>

<span class="mark">SURROGATE FOR: RECIPIENT,ORIGINAL</span>

<span class="mark">DATE/TIME - SURROGATE FOR: JUL 28, 2023@15:05:46</span>

It is expected that the surrogate will view and process the alert as shown in <u>Figure 16</u>.

![](kernel-8-0-systems-management-utilities-user-guide/023.png) NOTE: The <span class="mark">DATE-TIME RETURNED</span> field is populated at a later DATE/TIME when the surrogate period has ended and either of the two users signs on to CPRS/VistA.

<span id="_Ref145512962" class="anchor"></span>Figure 16: Sample Output—Surrogate Views and Processes the Alert

NAME: NO-ID;76;3230728.150546 DATE CREATED: JUL 28, 2023@15:05:46

PKG ID: NO-ID GENERATED BY: SENDER

DISPLAY TEXT: Alert during surrogacy ROUTINE TAG: EN

ROUTINE FOR PROCESSING: AROUTINE

RECIPIENT: RECIPIENT,ORIGINAL

RECIPIENT TYPE: INITIAL RECIPIENT SENT TO SURROGATE: SURROGATE,ONE

ALERT DATE/TIME: JUL 28, 2023@15:05:46

RECIPIENT: SURROGATE,ONE

<span class="mark">ALERT FIRST DISPLAYED: JUL 28, 2023@15:09:26</span>

<span class="mark">FIRST SELECTED ALERT: JUL 28, 2023@15:09:26</span>

<span class="mark">PROCESSED ALERT: JUL 28, 2023@15:10:09</span>

<span class="mark">DELETED ON: JUL 28, 2023@15:10:09</span>

RECIPIENT TYPE: INITIAL RECIPIENT-SURROGATE

ACTING AS SURROGATE: YES ALERT DATE/TIME: JUL 28, 2023@15:05:46

SURROGATE FOR: RECIPIENT,ORIGINAL

DATE/TIME - SURROGATE FOR: JUL 28, 2023@15:05:46

<span class="mark">DATE-TIME RETURNED: JUL 28, 2023@15:27:32</span>

In this scenario (<u>Figure 16</u>), the Kernel Alerts software is attempting to review all the alerts that occurred during the surrogate period and may attempt to return the alert to the initial recipient if necessary. In this case, the alert is *not* returned, because the surrogate processed the alert.

#### Alert to Surrogate—Who Ignores Alert

If the surrogate does *not* process the alert during the surrogate period, the alert is returned (forwarded) to the initial recipient at the end of the surrogate period and when either of the users signs on to CPRS/VistA, as shown in <u>Figure 17</u>.

Sequence of events:

1.  <span class="mark">Alert is delivered to surrogate</span> (<span class="mark">JUL 28, 2023@09:14:55</span>).
9.  Surrogate period ends.
10. One of the recipients signs on to CPRS/VistA.
11. <span class="mark">Alert is restored from surrogate</span> (JUL 30, 2023@<span class="mark">09:45:21</span>) and forwarded.
12. <span class="mark">Original recipient processes the alert</span> (JUL 30, 2023@<span class="mark">09:52:12</span>).

<span id="_Ref145514649" class="anchor"></span>Figure 17: Sample Output—Alert to Surrogate Who Ignores Alert

NAME: NO-ID;76;3230728.091455 DATE CREATED: JUL 28, 2023@09:14:55

PKG ID: NO-ID GENERATED BY: SENDER

DISPLAY TEXT: Alert during surrogacy ROUTINE TAG: EN

ROUTINE FOR PROCESSING: AROUTINE

RECIPIENT: RECIPIENT,ORIGINAL

ALERT FIRST DISPLAYED: JUL 30, 2023@09:50:15

FIRST SELECTED ALERT: JUL 30, 2023@09:50:15

<span class="mark">PROCESSED ALERT: JUL 30, 2023@09:52:12</span>

<span class="mark">DELETED ON: JUL 30, 2023@09:52:12</span>

RECIPIENT TYPE: INITIAL RECIPIENT <span class="mark">SENT TO SURROGATE: SURROGATE,ONE</span>

<span class="mark">ALERT DATE/TIME: JUL 28, 2023@09:14:55</span>

<span class="mark">RECIPIENT TYPE: RESTORE FROM SURROGATE ALERT DATE/TIME: JUL 30, 2023@09:45:21</span>

<span class="mark">FORWARDED DATE/TIME: JUL 30, 2023@09:45:21</span>

<span class="mark">FORWARDING CATEGORY: RESTORE FROM SURROGATE</span>

<span class="mark">FORWARDED BY OR FOR: SURROGATE,ONE</span>

<span class="mark">FORWARDING COMMENT: RESTORED FROM SURROGATE</span>

RECIPIENT: SURROGATE,ONE

ALERT FIRST DISPLAYED: JUL 28, 2023@10:11:03

FIRST SELECTED ALERT: JUL 28, 2023@10:11:03

<span class="mark">DELETED ON: JUL 30, 2023@09:45:21</span>

RECIPIENT TYPE: INITIAL RECIPIENT-SURROGATE

<span class="mark">ACTING AS SURROGATE: YES ALERT DATE/TIME: JUL 28, 2023@09:14:55</span>

<span class="mark">SURROGATE FOR: RECIPIENT,ORIGINAL</span>

<span class="mark">DATE/TIME - SURROGATE FOR: JUL 28, 2023@09:14:55</span>

<span class="mark">DATE-TIME RETURNED: JUL 30, 2023@09:45:21</span>

In this case (<u>Figure 17</u>), note that the RECIPIENT,ORIGINAL has two instances of the RECIPIENT TYPE field:

1.  During the surrogate period: INITIAL RECIPIENT.
13. After the surrogate period: RESTORE FROM SURROGATE.

# Error Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Error Processing User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an option you are using encounters an error condition, you are usually returned to the menu system. A message is displayed indicating that an error has occurred. You are then presented with the last menu prompt and can continue.

There are certain error conditions, however, that may prohibit or prevent return to the menu system. In these situations, you are halted off the system.

## Error Processing System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Error Processing \[XUERRS\] menu handles errors for Caché systems. It provides access to options pertaining to the error trap, displaying, printing, and purging errors. Like the error traps provided by the operating systems, the utility allows the investigation of program execution errors or the examination of system errors by capturing a picture of the environment for later reconstruction.

The %ZTER\* routines are called from ERR^ZU to trap errors and store them in the ^%ZTER global, a Manager account global that should be translated so that all errors are included on one report. The XTER\* routines are used to format the error report.

### Error Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At times you may not want to trap a certain type of error, but merely to count them because you are already aware of the error and can do nothing to prevent it. At other times you may not even want to count the error because it is inevitable or harmless. An error screen is a string of characters that is compared with the error message of every error trapped. Any trapped error whose message contains the screen is screened out. You decide for each screen whether the error is counted or completely ignored. In either case the error is *not* recorded in either the Kernel ERROR LOG (#3.075) file or the TaskMan Error Log. In TaskMan, if a running task encounters a screened error, the submanager still notes the error in the record for that task.

Kernel gives you four options with which to manage your error screens:

- [List Error Screens Option](#list-error-screens-option) \[XUTM ERROR SCREEN LIST\]
- [Add Error Screens Option](#add-error-screens-option) \[XUTM ERROR SCREEN ADD\]
- [Edit Error Screens Option](#edit-error-screens-option) \[XUTM ERROR SCREEN EDIT\]
- [Remove Error Screens Option](#remove-error-screens-option) \[XUTM ERROR SCREEN REMOVE\]

![](kernel-8-0-systems-management-utilities-user-guide/024.png) NOTE: Even though these four option names are prefixed with “XUTM” and located on TaskMan menus, these error screen options apply to all errors and *not* just TaskMan-specific errors. These four options are located on the Taskman Error Log \[XUTM ERROR\] menu, located under the Taskman Management Utilities \[XUTM UTIL\] menu, located under the Taskman Management \[XUTM MGR\] menu, which are all located under the Systems Manager Menu \[EVE\].

#### List Error Screens Option

<span id="_Toc193181725" class="anchor"></span>Figure 18: List Error Screens Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Taskman Error Log ... \[XUTM ERROR\]

<span class="mark">List Error Screens</span> \[XUTM ERROR SCREEN LIST\]

The List Error Screens \[XUTM ERROR SCREEN LIST\] option lists in a simple table the screens you have established and the number of errors that have been screened out by each.

#### Add Error Screens Option

<span id="_Toc193181726" class="anchor"></span>Figure 19: Add Error Screens Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Taskman Error Log ... \[XUTM ERROR\]

<span class="mark">Add Error Screens</span> \[XUTM ERROR SCREEN ADD\]

With the Add Error Screens \[XUTM ERROR SCREEN ADD\] option you can enter a screen and specify whether the errors should be counted. If there are already similar screens in place (such as entering SYN when SYNTAX is already established) you are so informed, shown the similar screens, and prompted for confirmation before being asked about the count. Entering two question marks (??) at the “Enter Screen To Apply:” prompt displays the list of error screens.

#### Edit Error Screens Option

<span id="_Toc193181727" class="anchor"></span>Figure 20: Edit Error Screens Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Taskman Error Log ... \[XUTM ERROR\]

<span class="mark">Edit Error Screens</span> \[XUTM ERROR SCREEN EDIT\]

Use the Edit Error Screens \[XUTM ERROR SCREEN EDIT option if you want to reset the counter on a screen or change your mind about whether the screen counts its errors. You *must* type in the exact screen you wish to edit. Again, entering two questions marks displays the list of error screens currently in place.

#### Remove Error Screens Option

<span id="_Toc193181728" class="anchor"></span>Figure 21: Remove Error Screens Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Taskman Error Log ... \[XUTM ERROR\]

<span class="mark">Remove Error Screens</span> \[XUTM ERROR SCREEN REMOVE\]

When you type in a screen at the prompt for Remove Error Screens \[XUTM ERROR SCREEN REMOVE\] option, the screen is removed for you. If there are any similar screens, this option asks whether you wish to remove them also. Again, entering two question marks (??) displays the list of error screens.

### Enhanced Error Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enhanced error processing for Caché sites is supported. Kernel’s error trap captures variables in their state at the time errors occur, regardless of how variables may have been NEWed beforehand. Stack levels for the routine call stack are recorded in the error trap in the \$STACK variable.

The Error Processing \[XUERRS\] menu is comprised of the options that are shown in <u>Figure 22</u>. The description for each option is described in the sections that follow and are arranged in the same order as the options appear on the Error Processing menu.

<span id="_Ref511300788" class="anchor"></span>Figure 22: Error Processing Options

SYSTEMS MANAGER MENU ... \[EVE\]

Programmer Options ... \[XUPROG\]

<span class="mark">Error Processing ...</span> \[XUERRS\]

P1 Print 1 occurrence of each error for T-1 (QUEUE) \[XUERTRP PRINT T-1 1 ERR\]

P2 Print 2 occurrences of errors on T-1 (QUEUED) \[XUERTRP PRINT T-1 2 ERR\]

Clean Error Trap \[XUERTRP CLEAN\]

Error Trap Display \[XUERTRAP\]

Interactive Print of Error Messages \[XUERTRP PRINT ERRS\]

### Print 1 Occurrence of Each Error for T-1 (QUEUE) Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print 1 occurrence of each error for T-1 (QUEUE) \[XUERTRP PRINT T-1 1 ERR\] option lists the first occurrence of each error recorded on the previous day.

T-1 represents “Today-1 = Yesterday”

You can queue it to run shortly after midnight:

- If a device is specified, the output is sent to the specified device.
- If a device is *not* specified, the output is placed in a mail message and sent to the individual who queued the option to run. It should be set to automatically requeue at a 1-day (D) interval.

### Print 2 Occurrences of Errors on T-1 (QUEUED) Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print 2 occurrences of errors on T-1 (QUEUED) \[XUERTRP PRINT T-1 2 ERR\] option lists the first two occurrences of each error recorded on the previous day:

T-1 represents “Today-1 = Yesterday”

It can be queued to run shortly after midnight:

- If a device is specified, the output is sent to the specified device.
- If a device is *not* specified, the output is placed in a mail message and sent to the individual who queued the option to run. It should be set to automatically requeue at a 1-day (D) interval.

### Clean Error Trap Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Clean Error Trap \[XUERTRP CLEAN\] option to purge the error log. It is locked with the XUPROGMODE security key. You can use the corresponding direct mode utility, ^XTERPUR, in Programmer mode. There is also a queueable version, Error Trap Auto Clean \[XUERTRP AUTO CLEAN\] option.

Purging is a partial clearing of the ERROR LOG (#3.075) file stored in the ^%ZTER(1, global. This global node should *not* be deleted directly since potentially important recent errors would be purged. Deletion of the entire ^%ZTER global would be a greater mistake since the standard reference data contained in the ERROR MESSAGES (#3.076) file stored in ^%ZTER(2, would be lost.

You are first prompted for the number of days to leave in the error trap (<u>Figure 23</u>). If you enter several days to retain errors, all errors older than the specified number of days are immediately purged:

<span id="_Ref67406313" class="anchor"></span>Figure 23: Choosing the Number of Days to Leave Errors in the Error Trap

To Remove ALL entries except the last N days, simply enter the number N at the prompt. OTHERWISE, enter return at the first prompt, and a DATE at the second prompt. If no ending date is entered at the third prompt, then only the date specified will be deleted. If an ending date is entered that range of dates INCLUSIVE will be deleted from the error log.

Number of days to leave in error trap: <span class="mark">50 \<Enter\></span>

DONE

If you just press \<Enter\> instead of entering several days to retain, you are then prompted for a start date and end date between which to remove errors (<u>Figure 24</u>). Errors in the period you specify are then purged immediately:

<span id="_Ref67406359" class="anchor"></span>Figure 24: Choosing a Start and End Date Range to Delete Errors from the Error Trap

Starting Date to DELETE ERRORS from: <span class="mark">1/1 \<Enter\></span> (JAN 01, 2004)

Ending Date to DELETE ERRORS from: <span class="mark">1/31 \<Enter\></span> (JAN 31, 2004)

The queueable version of this option, Error Trap Auto Clean \[XUERTRP AUTO CLEAN\], can be scheduled to run in the background. By default, it cleans up errors recorded more than 7 days in the past. You can specify a different interval by placing a numeric value (representing the number of days beyond which to purge) in this option’s TASK PARAMETERS field of the OPTION SCHEDULING (#19.2) file.

### Error Trap Display Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Error Trap Display \[XUERTRAP\] option displays errors that have been trapped on the system. The messages for these errors are operating-system dependent. You can use the corresponding direct mode utility, ^XTER, from Programmer mode.

The error trap tries to capture the following (<u>Figure 25</u>):

- Description of the error.
- Local symbol table.
- Last global reference.
- Other signon statistics.

For Caché, \$ZC calls are used to record IO counts, CPU time, and page faults.

<span id="_Ref67406428" class="anchor"></span>Figure 25: Error Trap Display Option—Sample User Dialog

In response to the DATE prompt you can enter:

'S' to specify text to be matched in error or routine name.

Which date? \> <span class="mark">T-1 \<Enter\></span>

1 error logged on 2/9/95

1\) \<ECODETRAP\>PRGMODE+5^%ZOSV:2 07:41:52 KDE,KDE 20801D46

\_TNA4523:

No disconnect error

Which error? \> <span class="mark">1 \<Enter\></span>

Process ID: 2020107A (538972282) JAN 18, 1992 17:19:21

Username: EXAMPLE Process Name: VISTA User

UCI/VOL: \[NXT~NXT~ABC999~NXT:KDAABC999\]

\$ZA: 0 \$ZB: \013

Current \$IO: \_TNA4523: Current \$ZIO: LTA_00129420196A

CPU time: 3.17 Page Faults: 1204

Direct I/O: 81 Buffered I/O: 96

\$ZE= \<ECODETRAP\>PRGMODE+5^%ZOSV:2

D @XQZ G OUT"

Last Global Ref: ^XUSEC(0,"CUR",24,2950209.074142)

Which symbol? \>

Errors can be reported by searching for a date range or character string. Question marks show a count of errors for the selected range:

- Two question marks (??) exclude disconnects.
- Three question marks (???) include disconnects.

A string search could be used to find XQ in all routines or an UNDEF in the definition of all errors. Once an error is identified, the report generator shows the following:

- Job Number
- Username
- IO value
- DATE/TIME
- UCI/Volume Set
- Error Type
- Last Global Reference
- Line of code that caused the error

It then prompts for a listing of variables, enter ^L to list all or a letter, such as X, to list those starting with X. The listing can be printed to the screen or to an output device. You can page through the screen listing, one screen at a time, and enter ^Q to quit or enter ^ to exit at the end of each screen.

A restore feature can be invoked by entering ^R provided that the user is working in Programmer mode. Programmer mode is required as a protection against restoration of variables from within the menu system. To the extent possible, the environment at the time of the error is restored with the routine and local symbol table intact.

<span id="_Toc193181733" class="anchor"></span>Figure 26: Local Symbol Table Help

Which symbol? \> <span class="mark">? \<Enter\></span>

Enter:

^Q to EXIT

'^' to return to the last question

Leading character(s) of symbol(s) you wish to examine

\$ to get a display of the \$ system variables

^L to obtain a list of all symbols

^R to restore the symbol table and ... and enter direct mode

After reviewing the error log, you are given the opportunity to examine the operating system’s error log (<u>Figure 27</u>). Since most VistA applications record their errors in Kernel’s error log, there is less need to track VistA errors in the operating system error log.

<span id="_Ref67406511" class="anchor"></span>Figure 27: Choosing to Examine the Operating System’s Error Log—Sample User Dialog

Do you want to check the OPERATING SYSTEM ERROR TRAP too? NO//

### Interactive Print of Error Messages Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Interactive Print of Error Messages \[XUERTRP PRINT ERRS\] option provides for an interactive print of the first “n” of occurrences of an error (where “n” is user selectable) over a specified date range.

# Lock Manager Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Kernel Lock Manager Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Lock Manager utility is based on the original Class 3 VistA Lock Manager software developed by TM. This software has been updated to Class 1 software by the following Kernel patches:

- XU\*8.0\*608—Contains all the software components that make up the Kernel Lock Manager, which includes the XULM LOCK DICTIONARY (#8993) file.
- XU\*8.0\*607—Populates the XULM LOCK DICTIONARY (#8993) file, which is included in Patch XU\*8.0\*608. It requires the KIDS enhancement Patch XU\*8.0\*672.
- XU\*8.0\*672—Enhances the Kernel Installation and Distribution System (KIDS) to allow applications to distribute entries in the XULM LOCK DICTIONARY (#8993) file as KIDS components.

The principle use of the Kernel Lock Manager utility is to assist users in locating locks held by a process that has become dissociated from an active user. Once located, this utility kills the process that owns the lock, thereby releasing the locks held by that process.

The principal advantages of the Kernel Lock Manager utility over the existing Caché utilities include the following functionality:

- Ability to use the Lock Manager from within Veterans Health Information Systems and Technology Architecture (VistA).
- Cross-Node capabilities—No longer need to log into multiple nodes, even if the process that holds the lock is on a different node than the one you currently logged onto. This is accomplished by using the RPC Data Broker to execute Remote Procedure Calls (RPCs) on the other nodes to obtain the lock table and to terminate processes.
- Built-in VistA expertise through the new XULM LOCK DICTIONARY (#8993) file—This file provides in-depth details about the following:
- Locks
- Files that the locks reference
- Processes that hold the locks
- Extendible Lock dictionary—Ability to add information about locks is included in the initial release of the Lock Dictionary. The LOCK TEMPLATE component was added to KIDS with Kernel Patch XU\*8.0\*672. It allows application developers to add to the Lock Dictionary and distribute their additions through KIDS.

## Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two steps to configuring the Lock Manager:

1.  [Entering Site Parameters](#entering-site-parametersedit-lock-manager-parameters-option)
2.  [Add Lock Manager Users](#add-lock-manager-users)

### Entering Site Parameters—Edit Lock Manager Parameters Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Edit Lock Manager Parameters \[XULM EDIT PARAMETERS\] option to update the Lock Manager parameters in the XULM LOCK MANAGER PARAMETER S (#8993.1) file.

To edit the Lock Manager parameter, do the following:

1.  From the Lock Manager Menu \[XULM LOCK MANAGER MENU\], select the Edit Lock Manager Parameters \[XULM EDIT PARAMETERS\] option.
14. At the “APPLICATION STATUS:” prompt, set the application status to ENABLED.
15. For each node in the system configuration, do the following:
1.  At the “Select NODES:” prompt, enter Caché instance. The name can be obtained by logging onto each node and entering at the M prompt:

w \##class(%SYS.System).GetInstanceName()

The returned value is the Caché instance name.

In the example in <u>Figure 28</u>, the instance is named *ABC999*.

> <span id="_Ref393952302" class="anchor"></span>Figure 28: Sample Code Using GetInstanceName Library Call to Get Instance Name

w \##class(%SYS.System).GetInstanceName()

2.  At the “TCP/IP ADDRESS:” prompt, enter the IP address.
3.  At the “BROKER PORT:” prompt, enter the port number of the Broker running on that node. Either the RPC Broker port or the M-to-M port can be used, but the RPC Broker port is recommended and is more widely available.
4.  The “SHORT DISPLAY NAME” prompt is optional. If the node’s name is over 8 characters long, it is necessary at times to display a shortened version. The default is to display only the last 8 characters. If the result is *not* satisfactory, you can enter a shortened name for the node to use as an alternative. <span class="mark">This pertains especially to Linux systems.</span>

> <span id="_Toc23169091" class="anchor"></span>Figure 29: Edit Lock Manager Parameters Option \[XULM EDIT PARAMETERS\]—Editing Site Parameters

Select Operations Management Option: <span class="mark">LOCK \<Enter\></span> Lock Manager Menu

LM Kernel Lock Manager

EDIT Edit Lock Dictionary

LOG View Lock Manager Log

<span class="mark">SITE Edit Lock Manager Parameters</span>

PURG PURGE LOCK MANAGER LOG

Select Lock Manager Menu Option: <span class="mark">SITE \<Enter\></span> Edit Lock Manager Parameters

APPLICATION STATUS: <span class="mark">ENABLED</span>// <span class="mark">\<Enter\></span>

Select NODES: *YYYYYYYY*// <span class="mark">\<Enter\></span>

TCP/IP ADDRESS: *99.9.99.99*// <span class="mark">\<Enter\></span>

BROKER PORT: *9999*// <span class="mark">\<Enter\></span>

SHORT DISPLAY NAME: NODEX// <span class="mark">\<Enter\></span>

### Add Lock Manager Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps give a user access to the Lock Manager:

1.  [Assign XULM LOCKS Security Key](#assign-xulm-locks-security-key)
16. [Edit User Settings for Lock Manager](#edit-user-settings-for-lock-manager)
17. [Assign XULM SYSTEM LOCKS Security Key](#assign-xulm-system-locks-security-key)

#### Assign XULM LOCKS Security Key

> To assign the XULM LOCKS security key, do the following:

1.  From the Systems Manager Menu \[EVE\], select the Menu Management \[XUMAINT\] menu.
18. At the “Select Menu Management Option:” prompt, select the Key Management \[XUKEYMGMT\] menu.
19. At the “Select Key Management Option:” prompt, select the Allocation of Security Keys \[XUKEYALL\] option.
20. At the “Allocate key:” prompt, enter XULM LOCKS security key.
21. At the “Another key:” prompt, press Enter to complete your entries.
22. At the “Holder of key:” prompt, enter the user’s name.
23. At the “Another holder:” prompt, enter any additional user names that need access to the Lock Manager. When complete, press Enter.
24. At the “You are allocating keys. Do you wish to proceed? YES//” prompt, press Enter to accept the YES default response.

> <span id="_Toc23169092" class="anchor"></span>Figure 30: Adding Lock Manager Users by Assigning XULM LOCKS Security Key

Select Systems Manager Menu Option: <span class="mark">MENU \<Enter\></span> Management

Edit options

<span class="mark">Key Management ...</span>

Secure Menu Delegation ...

Restrict Availability of Options

Option Access By User

List Options by Parents and Use

Fix Option File Pointers

Help Processor ...

OPED Screen-based Option Editor

Display Menus and Options ...

Edit a Protocol

Menu Rebuild Menu ...

Out-Of-Order Set Management ...

See if a User Has Access to a Particular Option

Show Users with a Selected primary Menu

Select Menu Management Option: <span class="mark">KEY \<Enter\></span> Management

<span class="mark">Allocation of Security Keys</span>

De-allocation of Security Keys

Enter/Edit of Security Keys

All the Keys a User Needs

Change user's allocated keys to delegated keys

Delegate keys

Keys For a Given Menu Tree

List users holding a certain key

Remove delegated keys

Show the keys of a particular user

Select Key Management Option: <span class="mark">ALLOC \<Enter\></span> ation of Security Keys

Allocate key: <span class="mark">XULM LOCKS \<Enter\></span>

Another key: <span class="mark">\<Enter\></span>

Holder of key: <span class="mark">XUUSER,ONE \<Enter\></span> OX TECHNICAL WRITER

Another holder: <span class="mark">\<Enter\></span>

You've selected the following keys:

XULM LOCKS

You've selected the following holders:

XUUSER,ONE

You are allocating keys. Do you wish to proceed? YES// <span class="mark">\<Enter\></span>

XULM LOCKS being assigned to:

XUUSER,ONE

#### Edit User Settings for Lock Manager

To use the Lock Manager each user *must* have the following user settings in the NEW PERSON (#200) file:

- Assign XULM RPC BROKER CONTEXT Option—The KERNEL LOCK MANAGER \[XULM RPC BROKER CONTEXT\] option is the context option the RPC Broker uses for the Lock Manager when making remote procedure calls.
- Set MULTIPLE SIGN-ON Field to ALLOWED.

To edit these user settings, do the following:

1.  From the Systems Manager Menu \[EVE\], select the User Management \[XUSER\] menu.
25. At the “Select User Management Option:” prompt, select the Edit an Existing User \[XUSEREDIT\] option.
26. At the “Select NEW PERSON NAME:” prompt, enter the user’s name.
27. Assign the XULM RPC BROKER CONTEXT option to the user:
1.  In the “Edit an Existing User” main screen (Page 1), tab down to the “Select SECONDARY MENU OPTIONS:” prompt, enter the XULM RPC BROKER CONTEXT option (<u>Figure 31</u>).
1.  (Optional) In the “SECONDARY MENU OPTIONS” popup screen, tab to “SYNONYM:” prompt and enter a synonym for this context option (<u>Figure 32</u>).
2.  Tab to the “COMMAND:” prompt, enter CLOSE. The “SECONDARY MENU OPTIONS” popup screen closes, and you are returned to the “Edit an Existing User” main screen (Page 1).

> <span id="_Ref32483588" class="anchor"></span>Figure 31: Assigning XULM RPC BROKER CONTEXT Option—Sample User Entries and System Responses (1 of 2)

Select Systems Manager Menu Option: <span class="mark">USER \<Enter\></span> Management

Add a New User to the System

Grant Access by Profile

Edit an Existing User

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

OAA OAA Trainee Registration Menu ...

Electronic Signature Block Edit

List Inactive Person Class Users

Manage User File ...

Person Class Edit

Print Patch Report

Reprint Access agreement letter

Select User Management Option: <span class="mark">EDIT \<Enter\></span> an Existing User

Select NEW PERSON NAME: <span class="mark">XUUSER \<Enter\></span> XUUSER,ONE OX TECHNICAL WRITER

<span class="mark">Edit an Existing User</span>

NAME: XUUSER,ONE <span class="mark">Page 1 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME... XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

<span class="mark">Select SECONDARY MENU OPTIONS:</span> <span class="mark">XULM RPC BROKER CONTEXT \<Enter\></span>

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION: SAN FRANCISCO

SERVICE/SECTION: OIFO Field Office

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

> <span id="_Ref32483601" class="anchor"></span>Figure 32: Assigning XULM RPC BROKER CONTEXT Option—Sample User Entries and System Responses (2 of 2)

Edit an Existing User

<u>NAME</u>: XUUSER,ONE <span class="mark">Page 1 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<u>NAME...</u> XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:



Select  SECONDARY MENU OPTIONS 

Want to  

Want to  SECONDARY MENU OPTIONS: <span class="mark">XULM RPC BROKER CONTEXT</span> 

 \| SYNONYM: <span class="mark">XULM</span> 

  



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Close Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">Close</span> Press \<PF1\>H for help Insert

Edit an Existing User

<u>NAME</u>: XUUSER,ONE <span class="mark">Page 1 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<u>NAME...</u> XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

Select SECONDARY MENU OPTIONS:

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION: SAN FRANCISCO

<u>SERVICE/SECTION</u>: OIFO Field Office

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

28. Tab to the “COMMAND:” prompt, enter NEXT PAGE (N). The “Edit an Existing User” screen moves to Page 2.
29. Set the MULTIPLE SIGN-ON Field to ALLOWED:
1.  In the “Edit an Existing User” main screen (Page 2), tab down to the “MULTIPLE SIGN-ON” field (<u>Figure 33</u>).
2.  If *not* already set to ALLOWED, enter ALLOWED at the “MULTIPLE SIGN-ON:” prompt.

> <span id="_Ref32489024" class="anchor"></span>Figure 33: Setting MULTIPLE SIGN-ON Field to ALLOWED—Sample User Entries and System Responses

Edit an Existing User

NAME: XUUSER,ONE <span class="mark">Page 2 of 5</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NETWORK USERNAME: VHAISFXXXXX

TIMED READ (# OF SECONDS): 900

<span class="mark">MULTIPLE SIGN-ON:</span> <span class="mark">ALLOWED</span> MULTIPLE SIGN-ON LIMIT: 4

ASK DEVICE TYPE AT SIGN-ON: DON'T ASK AUTO MENU: YES, MENUS GENERATED

PROHIBITED TIMES FOR SIGN-ON: TYPE-AHEAD: ALLOWED

AUTO SIGN-ON:

Preferred Editor: SCREEN EDITOR - VA FILEMAN

ALLOWED TO USE SPOOLER: PAC:

CAN MAKE INTO A MAIL MESSAGE:

FILE RANGE:

ALWAYS SHOW SECONDARIES:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for helpInsert

#### Assign XULM SYSTEM LOCKS Security Key

![](kernel-8-0-systems-management-utilities-user-guide/025.png) CAUTION: Use discretion when assigning this security key; deleting a system lock can result in database corruption!

> To assign the XULM SYSTEM LOCKS security key, do the following:

1.  From the Systems Manager Menu \[EVE\], select the Menu Management \[XUMAINT\] menu.
30. At the “Select Menu Management Option:” prompt, select the Key Management \[XUKEYMGMT\] menu.
31. At the “Select Key Management Option:” prompt, select the Allocation of Security Keys \[XUKEYALL\] option.
32. At the “Allocate key:” prompt, enter XULM SYSTEM LOCKS security key.
33. At the “Another key:” prompt, press Enter to complete your entries.
34. At the “Holder of key:” prompt, enter the user’s name.
35. At the “Another holder:” prompt, enter any additional user names that need access to the Lock Manager. When complete, press Enter.
36. At the “You are allocating keys. Do you wish to proceed? YES//” prompt, press Enter to accept the YES default response.

> <span id="_Toc23169095" class="anchor"></span>Figure 34: Adding Lock Manager Users by Assigning XULM SYSTEM LOCKS Security Key

Select Systems Manager Menu Option: <span class="mark">MENU \<Enter\></span> Management

Edit options

<span class="mark">Key Management ...</span>

Secure Menu Delegation ...

Restrict Availability of Options

Option Access By User

List Options by Parents and Use

Fix Option File Pointers

Help Processor ...

OPED Screen-based Option Editor

Display Menus and Options ...

Edit a Protocol

Menu Rebuild Menu ...

Out-Of-Order Set Management ...

See if a User Has Access to a Particular Option

Show Users with a Selected primary Menu

Select Menu Management Option: <span class="mark">KEY \<Enter\></span> Management

<span class="mark">Allocation of Security Keys</span>

De-allocation of Security Keys

Enter/Edit of Security Keys

All the Keys a User Needs

Change user's allocated keys to delegated keys

Delegate keys

Keys For a Given Menu Tree

List users holding a certain key

Remove delegated keys

Show the keys of a particular user

Select Key Management Option: <span class="mark">ALLOC \<Enter\></span> ation of Security Keys

Allocate key: <span class="mark">XULM SYSTEM LOCKS \<Enter\></span>

Another key: <span class="mark">\<Enter\></span>

Holder of key: <span class="mark">XUUSER,ONE \<Enter\></span> OX TECHNICAL WRITER

Another holder: <span class="mark">\<Enter\></span>

You've selected the following keys:

XULM SYSTEM LOCKS

You've selected the following holders:

XUUSER,ONE

You are allocating keys. Do you wish to proceed? YES// <span class="mark">\<Enter\></span>

XULM SYSTEM LOCKS LOCKS being assigned to:

XUUSER,ONE

## Lock Manager Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lock Manager Menu \[XULM LOCK MANAGER MENU\] is located on the Operations Management \[XUSITEMGR\] menu:

<span id="_Toc23169096" class="anchor"></span>Figure 35: Lock Manager Menu \[XULM LOCK MANAGER MENU\]

Select Systems Manager Menu Option: <span class="mark">OPER \<Enter\></span> ations Management

System Status

Introductory text edit

CPU/Service/User/Device Stats

<span class="mark">LOCK Lock Manager Menu ...</span>

RJD Kill off a users' job

Alert Management ...

Alpha/Beta Test Option Usage Menu ...

Clean old Job Nodes in XUTL

Delete Old (\>14 d) Alerts

Foundations Management

Kernel Management Menu ...

Post sign-in Text Edit

User Management Menu ...

Select Operations Management Option: <span class="mark">LOCK \<Enter\></span> Lock Manager Menu

LM Kernel Lock Manager

EDIT Edit Lock Dictionary

LOG View Lock Manager Log

SITE Edit Lock Manager Parameters

PURG Purge Lock Manager Log

Select Lock Manager Menu Option:

The Lock Manager Menu \[XULM LOCK MANAGER MENU\] includes the options listed in <u>Table 2</u>:

<table>
<caption><p><span id="_Ref332363902" class="anchor"></span>Table 3: Lock Manager—Actions</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 28%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Menu Text</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XULM LOCK MANAGER</td>
<td><strong>Kernel Lock Manager</strong></td>
<td><p>Use this option to display the Lock Table and terminate processes that hold problem locks.</p>
<p>This option is locked with the <strong>XULM LOCKS</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XULM EDIT LOCK DICTIONARY</td>
<td><strong>Edit Lock Dictionary</strong></td>
<td>User this option to add entries to the Lock Dictionary or edit existing entries.</td>
</tr>
<tr class="odd">
<td>XULM VIEW LOCK MANAGER LOG</td>
<td><strong>View Lock Manager Log</strong></td>
<td>Use this option to view the Kernel Lock Manager Log.</td>
</tr>
<tr class="even">
<td>XULM EDIT PARAMETERS</td>
<td><strong>Edit Lock Manager Parameters</strong></td>
<td>Use this option to edit the site parameters for the Kernel Lock Manager.</td>
</tr>
<tr class="odd">
<td>XULM PURGE LOCK MANAGER LOG</td>
<td><strong>Purge Lock Manager Log</strong></td>
<td>Use this option to purge the Lock Manager Log of old entries.</td>
</tr>
</tbody>
</table>

<span id="_Ref332363902" class="anchor"></span>Table 3: Lock Manager—Actions

## Using the Lock Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### List Locks Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Kernel Lock Manager \[XULM LOCK MANAGER\] option to view the lock table and the processes that own the locks. This option is locked with the XULM LOCKS security key.

Upon entering the option, you may be asked to enter your Access and Verify Code. The Lock Manager uses these codes to query each node for information regarding locks and processes, using the RPC Data Broker. However, if the system consists of the single node on which you are already logged onto, you are *not* asked to enter your Access and Verify Code.

<span id="_Toc23169097" class="anchor"></span>Figure 36: Using Kernel Lock Manager Option \[XULM LOCK MANAGER\]—Sample User Entries and Report

Select Operations Management Option: <span class="mark">LOCK \<Enter\></span> Lock Manager Menu

<span class="mark">LM Kernel Lock Manager</span>

EDIT Edit Lock Dictionary

LOG View Lock Manager Log

SITE Edit Lock Manager Parameters

PURG Purge Lock Manager Log

Select Lock Manager Menu Option: <span class="mark">LM \<Enter\></span> Kernel Lock Manager

Please enter your VistA access and verify codes.

ACCESS CODE:<span class="mark">\*\*\*\*\*\*\*\* \<Enter\></span>

VERIFY CODE:<span class="mark">\*\*\*\*\*\*\*\*\* \<Enter\></span>

Compiling the locks...

Building the display screen....

<u>KERNEL LOCK MANAGER Jul 26, 2012@12:31:51 Page: 1 of 4\_</u>

<u>\# Patient Lock User</u>

1 XUPATIENT,ONE ^DGPT(5,0) XUUSER,ONE

2 XUPATIENT,TWO ^DPT(5,0) XUUSER,TWO

\+ User Locks Sorted by Patient \>\>\>

<span class="mark">SL Select a Lock</span> <span class="mark">RL Refresh Locks</span> <span class="mark">SS Sort/Screen User Locks</span>

<span class="mark">GO Go To a List Entry</span> <span class="mark">SYS System Locks</span> <span class="mark">SN Select Node</span>

Select Action: Next Screen//

The main “User Locks” screen contains only user locks, as opposed to system locks. System locks are those locks used by VASS applications, such as the Kernel and HL7 packages, and are generally not of interest to users of the Lock Manager. To see the system locks, you can use the SYS—System Locks action.

<u>Table 3</u> lists the actions available on the “List Locks” screen.

<table>
<caption><p><span id="_Ref332297969" class="anchor"></span>Table 4: Lock Manager—Management Functions</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Lock Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SL—Select a Lock</strong></td>
<td>This action allows a user to select a lock from the list. It then displays a new screen with detailed information about the lock.</td>
</tr>
<tr class="even">
<td><strong>GO—Go To a List Entry</strong></td>
<td>This List Manager action asks the user where they want to go to on the list and then shifts the display to that location.</td>
</tr>
<tr class="odd">
<td><strong>RL—Refresh Locks</strong></td>
<td>This action rebuilds the list of locks by reading the lock table.</td>
</tr>
<tr class="even">
<td><strong>SYS—System Locks</strong></td>
<td><p>This action displays the list of the system locks. System locks are generally ignored within the Lock Manager. They are locks held by VASS applications, such as the Kernel or the HL7 package.</p>
<p>![](kernel-8-0-systems-management-utilities-user-guide/026.png) <strong>NOTE:</strong> Only holders of the <strong>XULM SYSTEM LOCKS</strong> security key can use this option.</p></td>
</tr>
<tr class="odd">
<td><strong>SS—Sort/Screen User Locks</strong></td>
<td><p>This action provides the user with several options for how the list locks should be displayed. The options include sorting the list by the following:</p>
<ul>
<li><blockquote>
<p>Patient Name</p>
</blockquote></li>
<li><blockquote>
<p>User Name</p>
</blockquote></li>
<li><blockquote>
<p>Lock string, or screening the entries by lock reference, which means that only locks that relate to a specific file are included in the display.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>SN—Select Node</strong></td>
<td>This action allows the user to select either a single computer node or all computer nodes. If the user selects a single node, then the display of locks includes only locks placed by processes running on that node.</td>
</tr>
</tbody>
</table>

<span id="_Ref332297969" class="anchor"></span>Table 4: Lock Manager—Management Functions

### Single Lock Details Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the SL—Select a Lock action to view the lock details (<u>Figure 37</u>). The detailed information includes the following information:

- Node Information
- Lock ID
- Process ID (decimal and Hex)—Process that owns the lock.
- User Name
- Task Information
- Lock Usage
- File References—Files that the lock references
- Other locks held by process

<span id="_Ref343777312" class="anchor"></span>Figure 37: Select a Lock Action—Sample Detailed Lock Information

DETAILED LOCK INFORMATION Jul 27, 2012@10:30:47 Page: 1 of 2

Node: *AABC999*Lock: ^DGBT(392,3120311.080346,0)

Full Reference: ^\[^"^\_\$1\$DGA4:\[ *XXX.YYY*\]"\]DGBT(392,3120311.080346,0)

Process ID (decimal): 542188409

Process ID (hex): 20512379

User Name: XUUSER,ONE DUZ: 53

Task Information:Task#: 3808610

Started: Jul 27, 2012@10:26:29

Option:Description: No Description (%ZTLOAD)

Lock Usage:

This lock is on a record in the BENEFICIARY TRAVEL CLAIM file (#392).

File References:PATIENT FILE RECORD:Patient Name: XUPATIENT,ONE

Sex: FEMALE

DOB: Mar 03, 1955

SSN: 000567987

BENEFICIARY TRAVEL CLAIM FILE RECORD:Claim Dt/Tm: Mar 11, 2012@08:03:46

Account#: 111 CAR,TRAINS, AND PLACES

Patient Name: XUPATIENT,ONE

Sex: FEMALE

DOB: Mar 03, 1955

SSN: 000567987

Other locks held by process:

^%ZTSCH("TASK",3808610)

^DPT(27,0)

\+ Enter ?? for more actions \>\>\>

KILL Terminate this Process

Select Action: Next Screen//

#### Terminate this Process Action

Use the KILL—Terminate this Process action to terminate the process, thereby releasing all the locks held by it.

![](kernel-8-0-systems-management-utilities-user-guide/027.png) CAUTION: This action is irreversible! Before terminating a process, examine all the information provided on the screen. Do *not* terminate the process unless you are sure the user is no longer active.  
  
Do *not* terminate a system process unless you have the expertise to ascertain the effect. Incorrectly terminating a system process could have adverse effects on multiple users or applications.

When a process is terminated, an entry is made in the XULM LOCK MANAGER LOG (#8993.2) file. It consists of the following data:

- User’s Name
- DATE/TIME of Action
- Detailed Lock Information

## Managing the Lock Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 4</u> reviews the various management functions available within the Lock Manager and the corresponding option where the function can be performed.

<table>
<caption><p><span id="_Ref129238325" class="anchor"></span>Table 5: DEA ePCS Utility—Main Menu Options</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Option</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enable/Disable the Lock Manager</td>
<td><p><strong>Edit Lock Manager Parameters</strong></p>
<p>[XULM EDIT PARAMETERS]</p></td>
</tr>
<tr class="even">
<td>Edit IP address and port numbers of RPC Data Broker on the system nodes.</td>
<td><p><strong>Edit Lock Manager Parameters</strong></p>
<p>[XULM EDIT PARAMETERS]</p></td>
</tr>
<tr class="odd">
<td><p>Edit the list of system locks.</p>
<p>System locks are generally excluded from view within the Lock Manager, which makes it easier for users to review the lock table.</p></td>
<td><p><strong>Edit Lock Manager Parameters</strong></p>
<p>[XULM EDIT PARAMETERS]</p></td>
</tr>
<tr class="even">
<td>View the Lock Manager: use log that records each instance of a process being terminated.</td>
<td><p><strong>View Lock Manager Log</strong></p>
<p>[XULM VIEW LOCK MANAGER LOG]</p></td>
</tr>
<tr class="odd">
<td>Purge the Lock Manager use log.</td>
<td><p><strong>Purge Lock Manager Log</strong></p>
<p>[XULM PURGE LOCK MANAGER LOG]</p></td>
</tr>
<tr class="even">
<td>Add or Edit entries in the Lock Dictionary.</td>
<td><p><strong>Edit Lock Dictionary</strong></p>
<p>[XULM EDIT LOCK DICTIONARY]</p></td>
</tr>
</tbody>
</table>

<span id="_Ref129238325" class="anchor"></span>Table 5: DEA ePCS Utility—Main Menu Options

## Maintaining the Lock Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Adding Lock Templates—Edit Lock Dictionary Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Edit Lock Dictionary \[XULM EDIT LOCK DICTIONARY\] option to add to or edit entries in the XULM LOCK DICTIONARY (#8993) file.

A “Lock Template” is a description of the lock. It looks like the entry in the lock table, except that it can contain a variable in place of a subscript. A variable is used when the actual subscript value is *not* known in advance. Usually, it represents the internal entry number (IEN) of the record that is being locked. Variables are important, because they can be used in M code (see <u>Figure 38</u>).

To add an entry to the XULM LOCK DICTIONARY (#8993) file, do the following:

1.  From the Lock Manager Menu \[XULM LOCK MANAGER MENU\] at the “Select Lock Manager Menu Option:” prompt, select the Edit Lock Dictionary \[XULM EDIT LOCK DICTIONARY\] option.
37. At the “Enter response: E//” prompt, enter one of the following values related to entries in the lock dictionary:
- E—Edit an existing entry.
- D—Delete an existing entry.
- A—Add a new entry.

In this example, the user is adding a new entry; so, she selected A—Add a new entry.

38. At the “LOCK TEMPLATE:” prompt, enter a Lock template based on the following rules:
- Locks are almost always on a global; though, it is allowable to lock a local variable. For the case of a global lock, enter a space as the first character, since VA FileMan does *not* allow a caret (^) as the first character (such as ^DGCR(399,IEN; this sample includes a leading space before the ^).
- Subscripts that are *not* variables should include quotes unless they are numbers.
- Variables should start with a letter and should not be quoted.
39. At the “GLOBAL LOCK?: YES//” prompt, press Enter to accept the YES default. Locks are usually on globals, but it is possible to lock a local variable too.
40. At the “XULM LOCK DICTIONARY GLOBAL LOCK?: YES//” prompt, press Enter to accept the YES default.
41. At the “XULM LOCK DICTIONARY PACKAGE:” prompt, enter the package that is responsible for the lock (such as Integrated Billing \[sample\]).
42. At the “PARTIAL MATCH ALLOWED?:” prompt, enter YES. This means that a lock table entry with additional subscripts is still considered as matching the Lock template. For example, by answering YES to this prompt the lock on ^DGCR(399,1,0) would be considered a match; otherwise, the additional subscript 0 would rule it out as a match.
43. At the “Edit? NO//” prompt, enter a description for the purpose of the Lock template.
44. (Optional) At the “Executable check logic for variable IEN (optional):” prompt, enter M code to verify that the variable IEN has a permissible value. It should set Y=0 if *not* OK and Y=1 if OK. For example:

S Y=\$S(\$D(^DGCR(399,IEN,0)):1,1:0)

In this example, you can check that the record exists. If the check fails, then the Lock template is ruled *not* to match the lock. The M code should set Y=1 if the value is acceptable, or 0 if the value is *not* acceptable. Setting Y=0 means that the lock table entry is considered *not* to match the Lock template.

45. (Optional) At the “Select FILE:” prompt, you can enter a file that is related to the lock (such as PATIENT \[#2\] file) in some way. Either the lock is on a record in the file, or a record in the file can be navigated to based on the information contained within the lock.

If you enter a file, then you can enter M code that returns identifiers from a record in that file that can help users identify the problem lock. If there are identifiers that you would like to display to the user, first select the file, and then enter the M code that retrieves the identifiers from the file.

Users of the Lock Manager search for the problem lock by the file or files that it is related to. Entering “COMPUTABLE FILE REFERENCES” is what makes this possible. Most locks of interest are related in some way to a particular patient, so entries in the Lock Dictionary should almost always contain a computable file reference to the PATIENT (#2) file, but other computable file references should also be included when appropriate.

46. At the “Are you adding ‘*XXXXXXXX*’ as a new COMPUTABLE FILE REFERENCES (the *nXX* for this XULM LOCK DICTIONARY)? No//” prompt, enter YES.
47. At the “COMPUTABLE FILE REFERENCES FILE: *XXXXXXXX*//” prompt, press Enter to accept the default response.
48. At the “Enter MUMPS code that returns identifiers for the file:” prompt, enter M code that returns identifiers for the file references. To return identifiers for the PATIENT (#2) file, the application should call the PAT^XULMU API \[see the [*Kernel 8.0 Developer’s Guide: Lock Manager Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_lock_manager_ug.pdf) on the VA Software Document Library (VDL)\]. It takes the patient DFN as the input. For example:

D PAT^XULMU(\$P(\$G(^DGCR(399,IEN,0)),"^",2))

49. At the “Edit? NO//” prompt, enter YES and then enter a description to list the identifiers that are returned for this file reference (such as Name, Sex, Date of Birth \[DOB\], and Social Security Number \[SSN\]).
50. At the “Select FILE:” prompt, enter another computable file identifier (such as BILL/CLAIMS \[#399\] file).
51. At the “Are you adding ‘*XXXXXXXX*’ as a new COMPUTABLE FILE REFERENCES (the *nXX* for this XULM LOCK DICTIONARY)? No//” prompt, enter YES.
52. At the “COMPUTABLE FILE REFERENCES FILE: //” prompt, press Enter.
53. At the “Enter MUMPS code that returns identifiers for the file. MUMPS CODE:” prompt, enter M code that returns identifiers for the file references. This file returns identifiers from the PATIENT (#2) file as well as the bill number. To obtain the patient identifiers when the referenced file is *not* the PATIENT (#2) file use the ADDPAT^XULMU API \[see the [*Kernel 8.0 Developer’s Guide: Lock Manager Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_lock_manager_ug.pdf) on the VDL\]. The input parameter is the patient DFN. For example:

N ND S ND=\$G(^DGCR(399,IEN,0)),ID("IEN")=IEN D ADDPAT^XULMU(+\$P(ND,"^",2)) S ID(0)=ID(0)+1,ID(ID(0))="BILL NUMBER:"\_\$P(ND,"^")

54. At the “Edit? NO//” prompt, enter YES and then enter a description to list the identifiers that are returned for this file reference (such as Name, Sex, Date of Birth \[DOB\], Social Security Number \[SSN\], and Bill Number).

<span id="_Ref343771372" class="anchor"></span>Figure 38: Adding New Entry to XULM LOCK DICTIONARY (#8993) File—Sample ^DGCR(399,IEN) Template

Select Operations Management Option: <span class="mark">LOCK MANAGER MENU \<Enter\></span>

LM Kernel Lock Manager

<span class="mark">EDIT Edit Lock Dictionary</span>

LOG View Lock Manager Log

SITE Edit Lock Manager Parameters

PURG Purge Lock Manager Log

Select Lock Manager Menu Option: <span class="mark">EDIT LOCK DICTIONARY \<Enter\></span>

Do you want to edit an existing entry in the lock dictionary or add a new one?

Select one of the following:

E Edit an entry

D Delete an entry

A Add a new entry

Enter response: E// <span class="mark">ADD A NEW ENTRY \<Enter\></span>

\* You cannot enter the '^' prefix when selecting a lock template. \*\*

LOCK TEMPLATE: <span class="mark">^DGCR(399,IEN) \<Enter\></span>

LOCK TEMPLATE: <span class="mark">\_^DGCR(399,IEN) \<Enter\></span>

LOCK TEMPLATE: ^DGCR(399,IEN)// <span class="mark">\<Enter\></span>

GLOBAL LOCK?: YES// <span class="mark">\<Enter\></span>

XULM LOCK DICTIONARY GLOBAL LOCK?: YES// <span class="mark">\<Enter\></span> YES

XULM LOCK DICTIONARY PACKAGE: <span class="mark">INTEGRATED BILLING \<Enter\></span>

PARTIAL MATCH ALLOWED?: <span class="mark">YES \<Enter\></span>

What is the purpose of this lock?:

No existing text

Edit? NO// <span class="mark">YES \<Enter\></span><span class="mark">This lock is on a record in the BILL/CLAIMS file (#399).</span>

You can optionally enter MUMPS code to verify that the variable IEN

has a permissible value. It should set Y=0 if not ok, Y=1 if ok.

Executable check logic for variable IEN (optional): <span class="mark">S Y=\$S(\$D(^DGCR(399,IEN,0)):1,1:0)</span>

You can display file identifiers for the locked record, or for a record in

another file related to the locked record. Most locks are related to a

specific patient, so most entries in the lock dictionary should include a

file reference to the PATIENT file (#2) and to the file of the locked record,

and perhaps other files as well.

If you would like to include file references, first select the file, and then

enter the MUMPS code that will retrieve the file identifiers from that file.

Select FILE: <span class="mark">*2* \<Enter\></span> *PATIENT*

Are you adding '*PATIENT*' as

a new COMPUTABLE FILE REFERENCES (the 1ST for this XULM LOCK DICTIONARY)? No

// <span class="mark">YES \<Enter\></span>

COMPUTABLE FILE REFERENCES FILE: PATIENT// <span class="mark">\<Enter\></span>

Enter MUMPS code that returns identifiers for the file:

<span class="mark">D PAT^XULMU(\$P(\$G(^DGCR(399,IEN,0)),"^",2)) \<Enter\></span>

List the identifiers that are returned for this file reference.

Identifiers:

No existing text

Edit? NO// <span class="mark">YES \<Enter\></span><span class="mark">Returns the patient's name, sex, date of birth, and Social Security Number.</span>

Select FILE: <span class="mark">*399* \<Enter\></span> *BILL/CLAIMS*

Are you adding '*BILL/CLAIMS* ' as a new COMPUTABLE FILE REFERENCES (the 2ND for this XULM LOCK DICTIONARY)? No// <span class="mark">YES \<Enter\></span>

COMPUTABLE FILE REFERENCES FILE: // <span class="mark">\<Enter\></span>

Enter MUMPS code that returns identifiers for the file.

MUMPS CODE: <span class="mark">N ND S ND=\$G(^DGCR(399,IEN,0)),ID("IEN")=IEN D ADDPAT^XULMU(+\$P(ND,"^",2)) S ID(0)=ID(0)+1,ID(ID(0))="BILL NUMBER:"\_\$P(ND,"^")</span>

List the identifiers that are returned for this file reference.

Identifiers:

No existing text

Edit? NO// <span class="mark">YES \<Enter\></span><span class="mark">This file reference returns the patient name, date of birth, sex,</span><span class="mark">Social Security Number, and BILL NUMBER.</span>

### Exporting Lock Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in the Lock Dictionary can be included in a KIDS distribution. The KIDS enhancement that adds LOCK TEMPLATE as a new component are released in Kernel Patch XU\*8.0\*672.

## Viewing and Purging Lock Manager Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### View Lock Manager Log Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the View Lock Manager Log \[XULM VIEW LOCK MANAGER LOG\] option to display the entries for the terminated lock processes in the XULM LOCK MANAGER LOG (#8993.2) file.

To view the Lock Manager log, do the following:

1.  From the Lock Manager Menu \[XULM LOCK MANAGER MENU\], select the View Lock Manager Log \[XULM VIEW LOCK MANAGER LOG\] option.
55. At the “Select XULM LOCK MANAGER LOG DATE/TIME PROCESS TERMINATED:” prompt, enter a specific DATE/TIME or two question marks (??) to get a list.
56. .At the “DEVICE:” prompt, enter a device to display the log for the specific entry selected.

<span id="_Toc23169100" class="anchor"></span>Figure 39: View Lock Manager Log Option \[XULM VIEW LOCK MANAGER LOG\]—Sample User Entries and Report

Select Lock Manager Menu Option: <span class="mark">VIEW \<Enter\></span> Lock Manager Log

Kernel Lock Manager Log

Select XULM LOCK MANAGER LOG DATE/TIME PROCESS TERMINATED: <span class="mark">?? \<Enter\></span>

Choose from:

JUN 18, 2012@17:14:23

JUN 18, 2012@17:22:32

JUN 18, 2012@17:33:27

JUN 19, 2012@09:03:58

JUN 19, 2012@09:04:43

JUN 19, 2012@09:45:49

JUN 19, 2012@11:04:16

JUN 19, 2012@11:06:47

JUN 19, 2012@12:33:43

JUN 19, 2012@12:35:36

JUN 19, 2012@12:47:21

JUN 19, 2012@12:48:48

JUN 19, 2012@12:50:42

JUN 19, 2012@12:53:16

JUN 19, 2012@12:55:59

JUN 20, 2012@06:40:46

JUN 24, 2012@09:14:55

JUN 24, 2012@09:21:43

JUN 24, 2012@09:22:50

<span class="mark">^ \<Enter\></span>

Select XULM LOCK MANAGER LOG DATE/TIME PROCESS TERMINATED: <span class="mark">JUNE 18 \<Enter\></span> JUN 18, 2012

1 6-18-2012@17:14:23

2 6-18-2012@17:22:32

3 6-18-2012@17:33:27

CHOOSE 1-3: <span class="mark">1 \<Enter\></span> 6-18-2012@17:14:23

DEVICE: <span class="mark">\<Enter\></span> Telnet Terminal Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">XULM LOCK MANAGER LOG LIST</span> AUG 14,2012 16:12 PAGE 1

--------------------------------------------------------------------------------

<span class="mark">DATE/TIME PROCESS TERMINATED: JUN 18, 2012@17:14:23</span>

THE TERMINATOR: XUUSER,ONE

PROCESS DESCRIPTION:

Lock: ^DGBT(1,0)

Node: *AABC999*

Full Reference: ^\["^^\_\$1\$DGA4:\[NXT.NXT\]"\]DGBT(1,0)

Process ID (decimal): 540943078

Process ID (hex): 203E22E6

User Name: UNKNOWN DUZ:

Task Information: not available

Lock Usage: not available

File References: not available

Other locks held by process:

^DGPT(1,0)

^DPT(4,0)

<span class="mark">\<Enter\></span>

XULM LOCK MANAGER LOG LIST AUG 14,2012 16:12 PAGE 2

--------------------------------------------------------------------------------

^DPT(5,0)

Select XULM LOCK MANAGER LOG DATE/TIME PROCESS TERMINATED:

### Purge Lock Manager Log Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Purge Lock Manager Log \[XULM PURGE LOCK MANAGER LOG\] option to purge the Lock Manager log.

To purge the Lock Manager log, do the following:

1.  From the Lock Manager Menu \[XULM LOCK MANAGER MENU\], select the Purge Lock Manager Log \[XULM PURGE LOCK MANAGER LOG\] option.
57. At the “How many days of data should be retained: (0-365): 30//” prompt, enter the number of days to *retain* the log data (such as 30 days). Any log data older than the value entered is purged (such as 31 or more days). The default is 30 days with a maximum of 1 year (365 days).
58. When the data purge is complete, the system displays: DONE!

<span id="_Toc23169101" class="anchor"></span>Figure 40: Purge Lock Manager Log Option \[XULM PURGE LOCK MANAGER LOG\]—Sample User Entries and System Responses

Select Lock Manager Menu Option: <span class="mark">PURG \<Enter\></span> Purge Lock Manager Log

How many days of data should be retained: (0-365): 30// <span class="mark">364 \<Enter\></span>

<span class="mark">DONE!</span>

Enter RETURN to continue or '^' to exit:

## Lock Manager Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Node Connection Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you get a node connection error (such as <u>Figure 41</u>) when using the Kernel Lock Manager \[XULM LOCK MANAGER\] option, contact your system administrator.

<span id="_Ref32496024" class="anchor"></span>Figure 41: Sample Node Connection Error (Excerpt)

...

Compiling the locks...

Failed to connect to node 'ALTR4PA01': Connection error: Port, IP or server logon error.

Continue with lock display? YES//

Failed to connect to node 'ALTR4PA02': Connection error: Port, IP or server logon error.

Continue with lock display? YES//

Failed to connect to node 'ALTR4PA03': Connection error: Port, IP or server logon error.

Continue with lock display? YES//

...

For example, instance names may *not* be defined in the Domain Name Service (DNS). System administrators can try pinging the name as it appears in the configuration, from one of the nodes in the configuration. Pinging should result in resolution to the IP address. If it does *not*, the instance name should be added to the DNS server that is used by these nodes.

# DEA ePCS Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DEA ePCS Utility Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patch XU\*8.0\*580 was created in support of the Drug Enforcement Agency (DEA) e-Prescribing of Controlled Substances (ePCS) Utility using Public Key Infrastructure (PKI). This section describes the modifications and enhancements to Kernel (and other VistA software) to meet the requirements proposed by the DEA Interim Final Rule (IFR) for Electronic Prescriptions for Controlled Substances effective as of June 1, 2010.

![](kernel-8-0-systems-management-utilities-user-guide/028.png) NOTE: This document only describes the changes made to Kernel in support of the DEA ePCS Utility.

![](kernel-8-0-systems-management-utilities-user-guide/029.png) REF: For more information on the DEA ePCS Utility software and other VistA applications, see the following:

- Computerized Patient Record System (CPRS) documentation on the VDL: [VDL CPRS Application Documents](http://www.va.gov/vdl/application.asp?appid=61)
- Pharmacy: Controlled Substances documentation: on the VDL: [VDL Controlled Substances Application Documents](http://www.va.gov/vdl/application.asp?appid=86)

### History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) Patient Care Services Office Pharmacy Benefits Management Services (PBM) requested enhancements to Veterans Health Information Systems and Technology Architecture (VistA), specifically the following software applications:

- Computerized Patient Record System (CPRS)
- Outpatient Pharmacy
- Controlled Substances
- Kernel

The enhancements made to these applications is to ensure that prescriptions for Controlled Substances (that is drugs listed in federal Controlled Substance Schedules II through V) can be digitally signed by the Prescribers and electronically transmitted from Prescribers to a Department of Veterans Affairs (VA) Pharmacy. The request was aimed at filling in the difference between the Hines Drug Enforcement Agency (DEA) ePrescribing pilot project as it stood as of April 2014 and the proposed DEA ePrescribing of Controlled Substances as shown in the June 27, 2008 Federal Register. These regulations allowed the process and proof of concept that was demonstrated with the DEA pilot to be expanded beyond the Hines VA Hospital facility.

The Hines VA/DEA Public Key Infrastructure (PKI) project stems from a pilot initiated in 2002 to demonstrate the ability for CPRS to incorporate digital signatures for Schedule II Controlled Substance narcotic prescriptions. Hines VA Hospital was the pilot site and had previously been granted a waiver of regulations by the DEA to test the system.

The Pilot procedure was as follows:

1.  Prescribers insert a “smart card” into a reader.
59. Prescribers enter an electronic prescription into CPRS.
60. System authenticates the Prescriber’s PKI prescribing credentials on the smart card.
61. System digitally signs the prescription.
62. System delivers the order to the VA pharmacy electronically.

The initial pilot evaluation, which allowed approximately 50 users to prescribe electronically using “smart cards”, was formally concluded in 2003. DEA authorized Hines VA Hospital to continue using the system in its current form until new regulations were published regarding electronic transmission of prescriptions using Personal Identity Verification (PIV) cards (aka smart cards). Subsequently, the VistA software was modified to meet the new standards.

Under the proposed DEA ePrescribing regulations, the CPRS system *must* authenticate the Prescriber’s credentials on a hard token (such as PIV card) and then display a mandatory message with DEA-required intent language that the Prescriber *must* consent to. Only after the Prescriber consents to the DEA-required wording can the prescription be transmitted to the VA Pharmacy.

The PIV card to be used for the DEA ePrescribing is the VA-wide PIV Card program mandated by Homeland Security Presidential Directive \#12 (HSPD-12).

![](kernel-8-0-systems-management-utilities-user-guide/030.png) REF: For information on validating PIV cards, see the “[PIV Card Validation—Revocation Server](#piv-card-validationrevocation-server)” section.

![](kernel-8-0-systems-management-utilities-user-guide/031.png) NOTE: CPRS requested the original funding of this software upgrade as part of the CPRS v29 funding submission.

### Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the DEA ePrescribing regulations were enacted, system changes were required to bring the VA in compliance with DEA regulations. Most of the changes needed for the DEA ePCS Utility are in the VistA CPRS and Outpatient Pharmacy applications; however, there were also some changes needed in Kernel:

- CPRS—Allows VA Prescribers to enter and digitally sign prescriptions.
- Outpatient Pharmacy—Notifies a VA pharmacy that a prescription order was made in CPRS.
- Kernel—Provides the Application Programming Interfaces (APIs) between the VistA Pharmacy and CPRS applications that allow the PKI credentials on the smart card to be verified. The PIV technology ensures that the Prescriber’s credentials are vetted and emplaced on the PIV card according to the DEA regulations once they are enacted into law.

The DEA regulations governing the electronic prescribing and transmission of Controlled Substances pertain to the following conditions:

- VA Prescribers of DEA-regulated Controlled Substances (Schedules II through V).
- Patients using a VA pharmacy.
- VA Pharmacists who fill the Controlled Substance prescriptions.
- Pharmacy Benefits Management (PBM), who has the accountability to minimize the abuse of Control Substances.

### Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The benefits of the DEA EPCS Utility include the following:

- Concise ordering of the correct prescriptions.
- Increased security against abuse of Controlled Substances—Test results showed a 90% reduction in the number of forged, tampered or altered Controlled Substances presented to the pharmacy.
- An electronic record of prescription history that can be monitored and reported.
- Increased patient safety—Test results showed a 75% reduction in the number of Controlled Substance prescription fill errors caused by illegible handwriting.
- Decreased wait time for patients to receive their prescriptions—Test results showed a 50% reduction in the average time from when a prescription is written to when it is process (finished) by pharmacy, primarily affected by the elimination of prescription transit time from remote clinics.

### Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience of this manual is all key stakeholders. The stakeholders for the DEA ePCS Utility include the following:

- (Primary) DEA-registered Prescribers of Controlled Substances—Users who do the following:
- Create the prescription order in the system.
- Digitally sign the prescription.
- Submit the prescription electronically to the Pharmacy.

Under the proposed DEA regulations, these users also electronically reject or agree to DEA-mandated wording prior to electronically signing the prescription.

- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers. These users are also responsible for the following:
- Installing the necessary hardware and software for use of the smart card-based digital certificates.
- Maintaining the server that runs the Certificate Revocation List (CRL) and other signature-checking processes.
- Assisting in the maintenance of the database containing all valid DEA registrants within the VA. This database is an entity outside of VistA. The management of this database is shared by the VA and DEA.
- Information Security Officer (ISO)—The ISO is responsible for information security at each VA site.
- Emerging Health Technologies (EHT)—Users who identify, explore, pilot, and move into Production those technologies that can contribute to VA business needs. In this instance, the Public Key Infrastructure (PKI) technologies.
- Personal Identification Verification (PIV) Project—This VA project provides formatted smart cards for use with the system. The PIV project personnel ensure that the DEA PKI expansion for digitally signing and transmitting electronic prescriptions fits in with the scope and objectives of the Veterans Health Administration (VHA)-wide Homeland Security Presidential Directive (HSPD)-12 mandated directives.
- Drug Enforcement Agency (DEA)—The Federal agency that:
- Enforces the Controlled Substances laws and regulations of the United States.
- Enforces provisions of the Controlled Substances Act as they pertain to the manufacture, distribution, and dispensing of legally produced Controlled Substances.
- Assists in the maintenance of the database containing all valid DEA registrants within the VA. This database is an entity outside of VistA. The management of this database is shared by the VA and DEA.
- Office of Information and Technology (OIT)—VistA legacy development teams.
- Product Support (PS).

## Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Manual Paper-based Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Schedule II Controlled Substance prescriptions within the VA using the manual paper-based process, the procedure is as follows:

1.  VA Prescriber either hand-writes a prescription before signing it or prints off a prescription form and hand-signs it before giving it to the patient.
2.  Patient or courier then hand-delivers the paper prescription form to the VA pharmacist.
3.  VA Pharmacist manually enters the script into the VistA Pharmacy package.
4.  After filling the prescription, the VistA Outpatient Pharmacy package updates CPRS with the record of the new fill.

With this method, CPRS has no way to verify the credentials of the Prescriber when a prescription order is handwritten. Additionally, when the hand-written script is illegible, the VA Pharmacist either guesses at what the Prescriber intends or *must* call the Prescriber to ascertain what the Prescriber intended on the handwritten script. In either of these cases, the prescription fill is delayed, and the VA patient *must* wait for their medically necessary medication.

<span id="_Toc204765514" class="anchor"></span>Figure 42: DEA ePCS—Manual Paper-based Process to Prescribe Schedule II Controlled Substances

![](kernel-8-0-systems-management-utilities-user-guide/032.png)

### e-Prescribing Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Schedule II – V Controlled Substance prescriptions within the VA using the ePrescribing process (that is e-Prescribing of Controlled Substances \[ePCS\] Utility), the procedure is as follows:

1.  VA Prescriber inserts a common access Personal Identity Verification (PIV) card (that is a smart card, which uniquely identifies the Prescriber) into a card reader attached to a computer keyboard.
2.  VA Prescriber enters the prescription order into the Computerized Patient Record System (CPRS).
3.  VA Prescriber signs the script electronically.
4.  CPRS prompts the Prescriber to provide the credentials for the smart card (analogous to an Automated Teller Machine \[ATM\] card’s Personal Identification Number \[PIN\] code).
5.  System verifies the PKI credentials.
6.  System affixes a digital signature to the prescription (digitally signed).
7.  CPRS sends the script order electronically to the VistA Pharmacy system.
8.  VA Pharmacist fills the script in VistA Pharmacy.
9.  VistA Pharmacy automatically sends a record of the prescription fill to CPRS.

<span id="_Toc204765515" class="anchor"></span>Figure 43: DEA ePCS—ePrescribing Process to Prescribe Schedule II - V Controlled Substances

![](kernel-8-0-systems-management-utilities-user-guide/033.png)

![](kernel-8-0-systems-management-utilities-user-guide/034.png) REF: For information on PIV and prescription validation processes, see the following sections:

- [PIV Card Validation—Revocation Server](#piv-card-validationrevocation-server)
- [Prescription Validation and Verification Process—PKIServer.exe Application](#prescription-validation-and-verification-processpkiserver.exe-application)

## Configuring the DEA ePCS Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two steps to configure the DEA ePCS Utility:

1.  [Set the XUEPCS REPORT DEVICE Parameter](#set-the-xuepcs-report-device-parameter).
2.  [Add DEA ePCS Utility Users](#add-dea-epcs-utility-users).

### Set the XUEPCS REPORT DEVICE Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set the XUEPCS REPORT DEVICE Parameter to the printer device. You can set this parameter by using either of the following methods:

- [General Parameter Tools Menu](#general-parameter-tools-menu).
- [XPAREDIT Routine](#xparedit-routine).

#### General Parameter Tools Menu

Use the General Parameter Tools \[XPAR MENU TOOLS\] menu, located under the CPRS Configuration (IRM) \[OR PARAM IRM MENU\] menu, to update the XUEPCS REPORT DEVICE parameter.

To edit the DEA ePCS Utility parameter, do the following:

1.  From the CPRS Manager Menu \[ORMGR\], select the IR—CPRS Configuration (IRM) \[OR PARAM IRM MENU\] option.
2.  At the “Select CPRS Configuration (IRM) Option:” prompt, select the XX—General Parameter Tools \[XPAR MENU TOOLS\]option.
3.  At the “Select General Parameter Tools Option:” prompt, select the EP—Edit Parameter Values \[XPAR EDIT PARAMETER\] option.
4.  At the “Select PARAMETER DEFINITION NAME:” prompt, enter XUEPCS REPORT DEVICE.
5.  At the “Select device for ePCS reports: *XXXXXXXX*//” prompt, enter the printer device appropriate for your system.

<span id="_Toc351026638" class="anchor"></span>

> Figure 44: DEA ePCS: General Parameter Tools Menu \[XPAR MENU TOOLS\]—Editing DEA ePCS Site Parameter

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

<span class="mark">IR CPRS Configuration (IRM) ...</span>

Select CPRS Manager Menu Option: <span class="mark">IR \<Enter\></span> CPRS Configuration (IRM)

OC Order Check Expert System Main Menu ...

TI ORMTIME Main Menu ...

UT CPRS Clean-up Utilities ...

<span class="mark">XX General Parameter Tools ...</span>

HD HealtheVet Desktop Configuration ...

RD Remote Data Order Checking Parameters

Select CPRS Configuration (IRM) Option: <span class="mark">GENERAL \<Enter\></span> Parameter Tools

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

<span class="mark">EP Edit Parameter Values</span>

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: <span class="mark">EP \<Enter\></span> Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: <span class="mark">XUEPCS REPORT DEVICE \<Enter\></span> ePCS Device

Definition for Reports

---- Setting XUEPCS REPORT DEVICE for System: *\<REDACTED\>*.VA.GOV ----

Select device for ePCS reports: *XXXXXXXX*// *<span class="mark">\<Printer Device\></span>*<span class="mark">\<Enter\></span>

Select PARAMETER DEFINITION NAME:

#### XPAREDIT Routine

Use the XPAREDIT routine to update the XUEPCS REPORT DEVICE parameter.

To edit the DEA ePCS Utility parameter, do the following:

1.  From the Programmer prompt, enter the following code:

D ^XPAREDIT

6.  At the “Select PARAMETER DEFINITION NAME:” prompt, enter XUEPCS REPORT DEVICE.
7.  At the “Select device for ePCS reports: *XXXXXXXX*//” prompt, enter the printer or other device appropriate for your system.

> <span id="_Toc351026639" class="anchor"></span>Figure 45: DEA ePCS: XPAREDIT Routine—Editing DEA ePCS Site Parameter: Test Account

\><span class="mark">D ^XPAREDIT \<Enter\></span>

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: <span class="mark">XUEPCS REPORT DEVICE \<Enter\></span> ePCS Device

Definition for Reports

---- Setting XUEPCS REPORT DEVICE for System: *\<REDACTED\>*.VA.GOV ----

Select device for ePCS reports: <span class="mark">SDD DUPLEX P10 \<Enter\></span>

SDD DUPLEX PRINTER next to One, Xuuser

USER\$:\[TEMP\]SDD_DN2\$PRT.TXT

------------------------------------------------------------------------------

Select PARAMETER DEFINITION NAME:

### Add DEA ePCS Utility Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three steps to give a user access to the DEA ePCS Utility:

1.  [Assign the XUEPCSEDIT Security Key](#assign-the-xuepcsedit-security-key).
8.  [Assign the XU EPCS EDIT DATA Option](#assign-the-xu-epcs-edit-data-option).
9.  [Assign the XUSSPKI UPN SET Option](#assign-the-xusspki-upn-set-option).

#### Assign the XUEPCSEDIT Security Key

> To assign the XUEPCSEDIT security key, do the following:

1.  From the Systems Manager Menu \[EVE\], select the Menu Management \[XUMAINT\] menu.
10. At the “Select Menu Management Option:” prompt, select the Key Management \[XUKEYMGMT\] menu.
11. At the “Select Key Management Option:” prompt, select the Allocation of Security Keys \[XUKEYALL\] option.
12. At the “Allocate key:” prompt, enter XUEPCSEDIT security key.
13. At the “Another key:” prompt, press Enter to complete your entries.
14. At the “Holder of key:” prompt, enter the user’s name.
15. At the “Another holder:” prompt, enter any additional user names that need access to the DEA ePCS Utility. When complete, press Enter.
16. At the “You are allocating keys. Do you wish to proceed? YES//” prompt, press Enter to accept the YES default response.

> <span id="_Ref433184020" class="anchor"></span>Figure 46: DEA ePCS: Adding DEA ePCS Utility Users by Assigning the XUEPCSEDIT Security Key

Select Systems Manager Menu Option: <span class="mark">MENU \<Enter\></span> Management

Edit options

<span class="mark">Key Management ...</span>

Secure Menu Delegation ...

Restrict Availability of Options

Option Access By User

List Options by Parents and Use

Fix Option File Pointers

Help Processor ...

OPED Screen-based Option Editor

Display Menus and Options ...

Edit a Protocol

Menu Rebuild Menu ...

Out-Of-Order Set Management ...

See if a User Has Access to a Particular Option

Show Users with a Selected primary Menu

Select Menu Management Option: <span class="mark">KEY \<Enter\></span> Management

<span class="mark">Allocation of Security Keys</span>

De-allocation of Security Keys

Enter/Edit of Security Keys

All the Keys a User Needs

Change user's allocated keys to delegated keys

Delegate keys

Keys For a Given Menu Tree

List users holding a certain key

Remove delegated keys

Show the keys of a particular user

Select Key Management Option: <span class="mark">ALLOC \<Enter\></span> ation of Security Keys

Allocate key: <span class="mark">XUEPCSEDIT \<Enter\></span>

Another key: <span class="mark">\<Enter\></span>

Holder of key: <span class="mark">XUUSER,ONE \<Enter\></span> OX TECHNICAL WRITER

Another holder: <span class="mark">\<Enter\></span>

You've selected the following keys:

XUEPCSEDIT

You've selected the following holders:

XUUSER,ONE

You are allocating keys. Do you wish to proceed? YES// <span class="mark">\<Enter\></span>

XUEPCSEDIT being assigned to:

XUUSER,ONE

#### Assign the XU EPCS EDIT DATA Option

The ePCS Edit Prescriber Data \[XU EPCS EDIT DATA\] option is the context option the RPC Broker uses for the DEA ePCS Utility when making remote procedure calls.

To assign the ePCS Edit Prescriber Data \[XU EPCS EDIT DATA\] option for each user, do the following:

1.  From the Systems Manager Menu \[EVE\], select the User Management \[XUSER\] menu.
17. At the “Select User Management Option:” prompt, select the Edit an Existing User \[XUSEREDIT\] option.
18. At the “Select NEW PERSON NAME:” prompt, enter the user’s name.
19. In the “Edit an Existing User” main screen, tab down to the “Select SECONDARY MENU OPTIONS:” prompt, enter the ePCS Edit Prescriber Data \[XU EPCS EDIT DATA\] option.
20. (Optional) In the “SECONDARY MENU OPTIONS” popup screen, tab to “SYNONYM:” prompt and enter a synonym for this context option.
21. Tab to the “COMMAND:” prompt, enter Close. The “SECONDARY MENU OPTIONS” popup screen closes.
22. Tab to the “COMMAND:” prompt, enter Exit. The “Edit an Existing User” main screen closes.

> <span id="_Ref433184055" class="anchor"></span>Figure 47: DEA ePCS: Assigning the XU EPCS EDIT DATA Option—Sample User Entries (1 of 2)

Select Systems Manager Menu Option: <span class="mark">USER \<Enter\></span> Management

Add a New User to the System

Grant Access by Profile

Edit an Existing User

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

OAA Trainee Registration Menu ...

Electronic Signature Block Edit

Manage User File ...

Person Class Edit

Reprint Access agreement letter

Select User Management Option: <span class="mark">EDIT \<Enter\></span> an Existing User

Select NEW PERSON NAME: <span class="mark">XUUSER \<Enter\></span> XUUSER,ONE OX TECHNICAL WRITER

<span class="mark">Edit an Existing User</span>

NAME: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME... XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

<span class="mark">Select SECONDARY MENU OPTIONS:</span> <span class="mark">XU EPCS EDIT DATA \<Enter\></span>

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION: SAN FRANCISCO

SERVICE/SECTION: OIFO Field Office

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

> <span id="_Toc351026642" class="anchor"></span>Figure 48: DEA ePCS: Assigning the XU EPCS EDIT DATA Option—Sample User Entries (2 of 2)

Edit an Existing User

<u>NAME</u>: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<u>NAME...</u> XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:



Select  SECONDARY MENU OPTIONS 

Want to  

Want to  SECONDARY MENU OPTIONS: <span class="mark">XU EPCS EDIT DATA</span> 

 SYNONYM: <span class="mark">EPCD</span> 

 



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Close Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">Close</span> Press \<PF1\>H for help Insert

Edit an Existing User

<u>NAME</u>: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<u>NAME...</u> XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

Select SECONDARY MENU OPTIONS:

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION: SAN FRANCISCO

<u>SERVICE/SECTION</u>: OIFO Field Office

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">Exit</span> Press \<PF1\>H for help Insert

#### Assign the XUSSPKI UPN SET Option

The ePCS Set SAN from PIV Card \[XUSSPKI UPN SET\] option is the context option the RPC Broker uses for the DEA ePCS Utility when making remote procedure calls.

To assign the ePCS Set SAN from PIV Card \[XUSSPKI UPN SET\] option for each user, do the following:

1.  From the Systems Manager Menu \[EVE\], select the User Management \[XUSER\] menu.
23. At the “Select User Management Option:” prompt, select the Edit an Existing User \[XUSEREDIT\] option.
24. At the “Select NEW PERSON NAME:” prompt, enter the user’s name.
25. In the “Edit an Existing User” main screen, tab down to the “Select SECONDARY MENU OPTIONS:” prompt, enter the ePCS Set SAN from PIV Card \[XUSSPKI UPN SET\] option.
26. (Optional) In the “SECONDARY MENU OPTIONS” popup screen, tab to “SYNONYM:” prompt and enter a synonym for this context option.
27. Tab to the “COMMAND:” prompt, enter Close. The “SECONDARY MENU OPTIONS” popup screen closes.
28. Tab to the “COMMAND:” prompt, enter Exit. The “Edit an Existing User” main screen closes.

> <span id="_Ref433184176" class="anchor"></span>Figure 49: DEA ePCS: Assigning the XUSSPKI UPN SET Option—Sample User Entries (1 of 2)

Select Systems Manager Menu Option: <span class="mark">USER \<Enter\></span> Management

Add a New User to the System

Grant Access by Profile

Edit an Existing User

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

OAA Trainee Registration Menu ...

Electronic Signature Block Edit

Manage User File ...

Person Class Edit

Reprint Access agreement letter

Select User Management Option: <span class="mark">EDIT \<Enter\></span> an Existing User

Select NEW PERSON NAME: <span class="mark">XUUSER \<Enter\></span> XUUSER,ONE OX TECHNICAL WRITER

<span class="mark">Edit an Existing User</span>

NAME: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME... XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

<span class="mark">Select SECONDARY MENU OPTIONS:</span> <span class="mark">XUSSPKI UPN SET \<Enter\></span>

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION: SAN FRANCISCO

SERVICE/SECTION: OIFO Field Office

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

> <span id="_Toc351026644" class="anchor"></span>Figure 50: DEA ePCS: Assigning the XUSSPKI UPN SET Option—Sample User Entries (2 of 2)

Edit an Existing User

<u>NAME</u>: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<u>NAME...</u> XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:



Select  SECONDARY MENU OPTIONS 

Want to  

Want to  SECONDARY MENU OPTIONS: <span class="mark">XUSSPKI UPN SET</span> 

 SYNONYM: <span class="mark">EPCP</span> 

 



\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Close Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">Close</span> Press \<PF1\>H for help Insert

Edit an Existing User

<u>NAME</u>: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<u>NAME...</u> XUUSER,ONE INITIAL: OX

TITLE: TECHNICAL WRITER NICK NAME: ONE

SSN: 000123456 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

Select SECONDARY MENU OPTIONS:

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION: SAN FRANCISCO

<u>SERVICE/SECTION</u>: OIFO Field Office

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">Exit</span> Press \<PF1\>H for help Insert

## Using the DEA ePCS Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DEA ePCS Utility consists of the following standalone menu and options, which are described in detail in the sections that follow:

- [DEA ePCS Utility Functions Main Menu](#dea-epcs-utility-functions-main-menu) \[XU EPCS UTILITY FUNCTIONS\]
- [Edit Facility DEA# and Expiration Date Option](#edit-facility-dea-and-expiration-date-option) \[XU EPCS EDIT DEA# AND XDATE\]
- [ePCS Edit Prescriber Data Option](#epcs-edit-prescriber-data-option) \[XU EPCS EDIT DATA\]
- [ePCS Set SAN from PIV Card Option](#epcs-set-san-from-piv-card-option) \[XUSSPKI UPN SET\]

### DEA ePCS Utility Functions Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Released with Kernel patch XU\*8.0\*580, the ePCS DEA Utility Functions \[XU EPCS UTILITY FUNCTIONS\] main menu is a standalone menu that is *not* linked to any other Kernel menus. It includes the options shown in <u>Figure 51</u>, which are described in <u>Table 5</u>:

<span id="_Ref511208047" class="anchor"></span>Figure 51: DEA ePCS: DEA ePCS Utility Functions Main Menu \[XU EPCS UTILITY FUNCTIONS\]

Select ePCS DEA Utility Functions Option:

1 Print DEA Expiration Date Null

<span class="mark">\*\*\> Out of order: PLACED OUT OF ORDER BY XU\*8\*765</span>

2 Print DISUSER DEA Expiration Date Null

<span class="mark">\*\*\> Out of order: PLACED OUT OF ORDER BY XU\*8\*765</span>

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

<span class="mark">\*\*\> Out of order: PLACED OUT OF ORDER BY XU\*8\*765</span>

11 Task Allocation Audit of PSDRPH Key Report

<span class="mark">\*\*\> Out of order: PLACED OUT OF ORDER BY XU\*8\*765</span>

12 Allocate/De-Allocate of PSDRPH Key

<span class="mark">\*\*\> Out of order: PLACED OUT OF ORDER BY XU\*8\*765</span>

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option:

![](kernel-8-0-systems-management-utilities-user-guide/035.png) NOTE: The following options were placed out of order with Kernel Patch XU\*8.0\*765 and replaced by functionality added to the ePCS DEA Utility Functions \[PSO EPCS UTILITY FUNCTIONS\] menu:

- 1 Print DEA Expiration Date Null
- 2 Print DISUSER DEA Expiration Date Null
- 10 Task Changes to DEA Prescribing Privileges Report
- 11 Task Allocation Audit of PSDRPH Key Report
- 12 Allocate/De-Allocate of PSDRPH Key

<table>
<caption><p><span id="_Ref188602083" class="anchor"></span>Table 6: SERVICE/SECTION (#49) File—Editable Fields</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 28%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Menu Text</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XU EPCS UTILITY FUNCTIONS</td>
<td>ePCS DEA Utility Functions</td>
<td><p>This is the main menu for the DEA ePCS Utility. It includes the following options:</p>
<ul>
<li><p><strong>XU EPCS EXP DATE</strong></p></li>
<li><p><strong>XU EPCS DISUSER EXP DATE</strong></p></li>
<li><p><strong>XU EPCS XDATE EXPIRES</strong></p></li>
<li><p><strong>XU EPCS DISUSER XDATE EXPIRES</strong></p></li>
<li><p><strong>XU EPCS PRIVS</strong></p></li>
<li><p><strong>XU EPCS DISUSER PRIVS</strong></p></li>
<li><p><strong>XU EPCS PSDRPH</strong></p></li>
<li><p><strong>XU EPCS SET PARMS</strong></p></li>
<li><p><strong>XU EPCS PRINT EDIT AUDIT</strong></p></li>
<li><p><strong>XU EPCS LOGICAL ACCESS</strong></p></li>
<li><p><strong>XU EPCS PSDRPH AUDIT</strong></p></li>
<li><p><strong>XU EPCS PSDRPH KEY</strong></p></li>
<li><p><strong>XU EPCS EDIT DEA# AND XDATE</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>XU EPCS EXP DATE</p>
<p>(See Section <u>5.4.2</u>.)</p></td>
<td>Print DEA Expiration Date Null</td>
<td><p>This option prints all active users with an unpopulated DEA# and DEA EXPIRATION DATE. This option prints the following data:</p>
<ul>
<li><p><strong>NAME</strong></p></li>
<li><p><strong>DEA#</strong></p></li>
<li><p><strong>DEA EXPIRATION DATE</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>XU EPCS DISUSER EXP DATE</p>
<p>(See Section <u>5.4.3</u>.)</p></td>
<td>Print DISUSER DEA Expiration Date Null</td>
<td><p>This option prints all DISUSERed users with an unpopulated DEA# and DEA EXPIRATION DATE. This option prints the following data:</p>
<ul>
<li><p><strong>NAME</strong></p></li>
<li><p><strong>DEA#</strong></p></li>
<li><p><strong>TERMINATION DATE</strong></p></li>
<li><p><strong>DEA EXPIRATION DATE</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>XU EPCS XDATE EXPIRES</p>
<p>(See Section <u>5.4.4</u>.)</p></td>
<td>Print DEA Expiration Date Expires 30 days</td>
<td><p>This option prints all active users with DEA # and where the DEA EXPIRATION DATE expires within 30 days. This option prints the following data:</p>
<ul>
<li><p><strong>NAME</strong></p></li>
<li><p><strong>DEA#</strong></p></li>
<li><p><strong>DEA EXPIRATION DATE</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>XU EPCS DISUSER XDATE EXPIRES</p>
<p>(See Section <u>5.4.5</u>.)</p></td>
<td>Print DISUSER DEA Expiration Date Expires 30 days</td>
<td><p>This option prints all DISUSERed users with DEA # and where the DEA EXPIRATION DATE expires within 30 days. This option prints the following data:</p>
<ul>
<li><p><strong>NAME</strong></p></li>
<li><p><strong>DEA#</strong></p></li>
<li><p><strong>DEA EXPIRATION DATE</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>XU EPCS PRIVS</p>
<p>(See Section <u>5.4.6</u>.)</p></td>
<td>Print Prescribers with Privileges</td>
<td><p>This option prints all active users who have privileges to any of the SCHEDULEs II through V and who have a DEA# or VA#. This option prints the following data:</p>
<ul>
<li><p><strong>NAME</strong></p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p><strong>DEA#</strong></p></li>
<li><p><strong>VA#</strong></p></li>
<li><p><strong>SCHEDULESs</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>XU EPCS DISUSER PRIVS</p>
<p>(See Section <u>5.4.7</u>.)</p></td>
<td>Print DISUSER Prescribers with Privileges</td>
<td><p>This option prints all DISUSERed users who have privileges to any of the SCHEDULEs II through V and who have a DEA# or VA#. This option prints the following data:</p>
<ul>
<li><p><strong>NAME</strong></p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p><strong>DEA#</strong></p></li>
<li><p><strong>TERMINATION DATE</strong></p></li>
<li><p><strong>VA#</strong></p></li>
<li><p><strong>SCHEDULESs</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>XU EPCS PSDRPH</p>
<p>(See Section <u>5.4.8</u>.)</p></td>
<td>Print PSDRPH Key Holders</td>
<td><p>This option prints all active users holding the <strong>PSDRPH</strong> security key. This report sorts by Division, and within DIVISION, it sorts by NAME. This option prints the following data:</p>
<ul>
<li><p><strong>NAME</strong></p></li>
<li><p><strong>DUZ</strong></p></li>
<li><p><strong>GIVEN BY</strong> (Person Who Assigned Key)</p></li>
<li><p><strong>DATE GIVEN</strong> (Date Assigned)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>XU EPCS SET PARMS</p>
<p>(See Section <u>5.4.9</u>.)</p></td>
<td>Print Setting Parameters Privileges</td>
<td>This option prints all active users holding the <strong>XUEPCSEDIT</strong> security key. This option identifies individuals responsible for setting the parameters.</td>
</tr>
<tr class="even">
<td><p>XU EPCS PRINT EDIT AUDIT</p>
<p>(See Section <u>5.4.10</u>.)</p></td>
<td>Print Audits for Prescriber Editing</td>
<td>This option prints information related to the editing of prescriber information.</td>
</tr>
<tr class="odd">
<td><p>XU EPCS LOGICAL ACCESS</p>
<p>(See Section <u>5.4.11</u>.)</p></td>
<td>Task Changes to DEA Prescribing Privileges Report</td>
<td><p>This tasked option prints the setting or change to DEA prescribing privileges related to issuance of a controlled substance prescription.</p>
<p>This option only prints data from the previous day and with data that has been modified. The data is retrieved from the XUEPCS DATA (#8991.6) file.</p>
<p>This option should be scheduled to run daily.</p></td>
</tr>
<tr class="even">
<td><p>XU EPCS PSDRPH AUDIT</p>
<p>(See Section <u>5.4.12</u>.)</p></td>
<td>Task Allocation Audit of PSDRPH Key Report</td>
<td><p>This tasked option prints the allocation of the <strong>PSDRPH</strong> security key.</p>
<p>This option only prints data from the previous day and with data that has been modified. The report prints data for the archive XUEPCS PSDRPH AUDIT (#8991.7) file.</p>
<p>This option should be scheduled to run daily.</p></td>
</tr>
<tr class="odd">
<td><p>XU EPCS PSDRPH KEY</p>
<p>(See Section <u>5.4.13</u>.)</p></td>
<td>Allocate/De-Allocate of PSDRPH Key</td>
<td>This option allocates or de-allocates the <strong>PSDRPH</strong> security key.</td>
</tr>
<tr class="even">
<td><p>XU EPCS EDIT DEA# AND XDATE</p>
<p>(See Section <u>5.4.14</u>.)</p></td>
<td>Edit Facility DEA# and Expiration Date</td>
<td>This option edits the FACILITY DEA NUMBER (#52) and FACILITY DEA EXPIRATION DATE (#52.1) fields in the INSTITUTION (#4) file.</td>
</tr>
</tbody>
</table>

<span id="_Ref188602083" class="anchor"></span>Table 6: SERVICE/SECTION (#49) File—Editable Fields

### Print DEA Expiration Date Null Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print DEA Expiration Date Null \[XU EPCS EXP DATE\] option prints all active users from the NEW PERSON (#200) file with the following field values:

- DEA# (#53.2)—NULL (unpopulated).
- DEA EXPIRATION DATE (#747.44)—Not NULL (populated).

This option prints the following data from the NEW PERSON (#200) file:

- NAME (#.01)
- DEA# (#53.2)
- DEA EXPIRATION DATE (#747.44)

![](kernel-8-0-systems-management-utilities-user-guide/036.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765524" class="anchor"></span>Figure 52: DEA ePCS: Print DEA Expiration Date Null Option—Sample User Entries and Report

Select Systems Manager Menu Option: <span class="mark">EPCS \<Enter\></span> ePCS DEA Utility Functions

<span class="mark">1 Print DEA Expiration Date Null</span>

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">1 \<Enter\></span> Print DEA Expiration Date Null

START WITH NAME: FIRST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

NULL 'DEA EXPIRATION DATE' APR 15,2013 16:53 PAGE 1

DEA

EXPIRATION

NAME DEA# DATE

--------------------------------------------------------------------------------

XUUSER,EIGHT AK1662673

XUUSER,ELEVEN MT0300777

XUUSER,FIVE BH2942628

XUUSER,FOUR AK2984082

XUUSER,FOURTEEN AG5333745

XUUSER,NINE BB1770773

XUUSER,ONE SF0963226

XUUSER,SEVEN AP8348458

XUUSER,SIX AM7446001

XUUSER,TEN BD9270911

XUUSER,THIRTEEN FC2158548

XUUSER,THREE FS2138572

XUUSER,TWELVE AR3287946

XUUSER,TWO BG4740850

.

.

.

### Print DISUSER DEA Expiration Date Null Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print DISUSER DEA Expiration Date Null \[XU EPCS DISUSER EXP DATE\] option prints all DISUSERed users from the NEW PERSON (#200) file with the following field values:

- DEA# (#53.2)—NULL (unpopulated).
- DEA EXPIRATION DATE (#747.44)—Not NULL (populated).

This option prints the following data from the NEW PERSON (#200) file:

- NAME (#.01)
- DEA# (#53.2)
- TERMINATION DATE (#9.2)
- DEA EXPIRATION DATE (#747.44)

![](kernel-8-0-systems-management-utilities-user-guide/037.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765525" class="anchor"></span>Figure 53: DEA ePCS: Print DISUSER DEA Expiration Date Null Option—Sample User Entries and Report

1 Print DEA Expiration Date Null

<span class="mark">2 Print DISUSER DEA Expiration Date Null</span>

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">2 \<Enter\></span> Print DISUSER DEA Expiration Date Null

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

DISUSER NULL 'DEA EXPIRATION DATE' APR 15,2013 16:55 PAGE 1

TERMINATION

DATE NAME DEA#

--------------------------------------------------------------------------------

AUG 16,2010 XUUSER,SEVENTY BC6840614

MAR 31,2010 XUUSER,EIGHTY AC7045796

MAR 18,2010 XUUSER,NINETY AL6010968

FEB 1,2010 XUUSER,ONE HUNDRED AM8823191

JAN 29,2010 XUUSER,FORTY AJ1103910

JUN 11,2009 XUUSER,THIRTY BM2745315

MAY 4,2009 XUUSER,FIFTEEN AP9587570

MAY 4,2009 XUUSER,SIXTEEN BB2243854

MAY 4,2009 XUUSER,SIXTY AK4751815

MAY 4,2009 XUUSER,FIFTY BN7729847

APR 20,2009 XUUSER,TWENTY AD6477865

APR 20,2009 XUUSER,TWO HUNDRED BM4942517

APR 20,2009 XUUSER,THREE HUNDRED AA1662673

JAN 1,2009 XUUSER,FOUR HUNDRED FK0178132

AUG 30,2008 XUUSER,FIVE HUNDRED BJ9947081

### Print DEA Expiration Date Expires 30 days Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print DEA Expiration Date Expires 30 days \[XU EPCS XDATE EXPIRES\] option prints all active users from the NEW PERSON (#200) file with the following field values:

- DEA# (#53.2)—Not NULL (populated).
- DEA EXPIRATION DATE (#747.44)—Date expires within 30 days.

This option prints the following data from the NEW PERSON (#200) file:

- NAME (#.01)
- DEA# (#53.2)
- DEA EXPIRATION DATE (#747.44)

![](kernel-8-0-systems-management-utilities-user-guide/038.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765526" class="anchor"></span>Figure 54: DEA ePCS: Print DEA Expiration Date Expires 30 days Option—Sample User Entries and Report

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

<span class="mark">3 Print DEA Expiration Date Expires 30 days</span>

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">3 \<Enter\></span> Print DEA Expiration Date Expires 30 days

START WITH NAME: FIRST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

EXPIRATION DATE EXPIRES IN 30 DAYS APR 15,2013 16:59 PAGE 1

DEA

EXPIRATION

NAME DEA# DATE

--------------------------------------------------------------------------------

<span class="mark">\*\*\* NO RECORDS TO PRINT \*\*\*</span>

### Print DISUSER DEA Expiration Date Expires 30 days Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print DISUSER DEA Expiration Date Expires 30 days \[XU EPCS DISUSER XDATE EXPIRES\] option prints all DISUSERed users from the NEW PERSON (#200) file with the following field values:

- DEA# (#53.2)—Not NULL (populated).
- DEA EXPIRATION DATE (#747.44)—Date expires within 30 days.

This option prints the following data from the NEW PERSON (#200) file:

- NAME (#.01)
- DEA# (#53.2)
- DEA EXPIRATION DATE (#747.44)

![](kernel-8-0-systems-management-utilities-user-guide/039.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765527" class="anchor"></span>Figure 55: DEA ePCS: Print DISUSER DEA Expiration Date Expires 30 days Option—Sample User Entries and Report

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

<span class="mark">4 Print DISUSER DEA Expiration Date Expires 30 days</span>

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">4 \<Enter\></span> Print DISUSER DEA Expiration Date Expires 30 days

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

DISUSER EXPIRATION DATE EXPIRES IN 30 DAYS APR 15,2013 17:08 PAGE 1

DEA

TERMINATION EXPIRATION

DATE NAME DEA# DATE

--------------------------------------------------------------------------------

<span class="mark">\*\*\* NO RECORDS TO PRINT \*\*\*</span>

### Print Prescribers with Privileges Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Prescribers with Privileges \[XU EPCS PRIVS\] option prints all active users from the NEW PERSON (#200) file who have privileges to any of the SCHEDULEs II through V and who have a DEA# or VA#.

This option prints the following data from the NEW PERSON (#200) file:

- NAME (#.01)
- DUZ—Internal Entry Number (IEN) for the user in the NEW PERSON (#200) file
- DEA# (#53.2)
- VA# (#53.3)
- SCHEDULEs:
- SCHEDULE II NARCOTIC (#55.1)
- SCHEDULE II NON-NARCOTIC (#55.2)
- SCHEDULE III NARCOTIC (#55.3)
- SCHEDULE III NON-NARCOTIC (#55.4)
- SCHEDULE IV (#55.5)
- SCHEDULE V (#55.6)

![](kernel-8-0-systems-management-utilities-user-guide/040.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765528" class="anchor"></span>Figure 56: DEA ePCS: Print Prescribers with Privileges Option—Sample User Entries and Report

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

<span class="mark">5 Print Prescribers with Privileges</span>

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">5 \<Enter\></span> Print Prescribers with Privileges

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

PRESCRIBERS WITH PRIVILEGES APR 15,2013 17:13 PAGE 1

NAME DUZ DEA# VA#

--------------------------------------------------------------------------------

DIVISION: ALBANY, NY VAMC

XUUSER,ONE 520736424 AA1234563

SCHEDULE II:

SCHEDULE II NON:

SCHEDULE III:

SCHEDULE III NON: Yes

SCHEDULE IV: Yes

SCHEDULE V:

DIVISION: CHEYENNE VAMC

XUUSER,TWO 520629114 AV4538419

SCHEDULE II:

SCHEDULE II NON:

SCHEDULE III:

SCHEDULE III NON:

SCHEDULE IV:

SCHEDULE V:

.

.

.

### Print DISUSER Prescribers with Privileges Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print DISUSER Prescribers with Privileges \[XU EPCS DISUSER PRIVS\] option prints all DISUSERed users who have privileges to any of the SCHEDULEs II through V and who have a DEA# or VA#.

This option prints the following data from the NEW PERSON (#200) file:

- NAME (#.01)
- DUZ—Internal Entry Number (IEN) for the user in the NEW PERSON (#200) file
- DEA# (#53.2)
- TERMINATION DATE (#9.2)
- VA# (#53.3) (DIVISION)
- SCHEDULEs:
- SCHEDULE II NARCOTIC (#55.1)
- SCHEDULE II NON-NARCOTIC (#55.2)
- SCHEDULE III NARCOTIC (#55.3)
- SCHEDULE III NON-NARCOTIC (#55.4)
- SCHEDULE IV (#55.5)
- SCHEDULE V (#55.6)

![](kernel-8-0-systems-management-utilities-user-guide/041.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765529" class="anchor"></span>Figure 57: DEA ePCS: Print DISUSER Prescribers with Privileges Option—Sample User Entries and Report

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

<span class="mark">6 Print DISUSER Prescribers with Privileges</span>

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">6 \<Enter\></span> Print DISUSER Prescribers with Privileges

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

DISUSER PRESCRIBERS WITH PRIVILEGES APR 15,2013 17:16 PAGE 1

TERMINATION

NAME DUZ DEA# DATE

--------------------------------------------------------------------------------

DIVISION: EMPTY

XUUSER,FIFTEEN 2890 AP9587570 MAY 4,2009

SCHEDULE II:

SCHEDULE II NON:

SCHEDULE III:

SCHEDULE III NON:

SCHEDULE IV:

SCHEDULE V:

XUUSER,SIXTEEN 520629429 BB2243854 MAY 4,2009

SCHEDULE II:

SCHEDULE II NON:

SCHEDULE III:

SCHEDULE III NON:

SCHEDULE IV:

SCHEDULE V:

.

.

.

DIVISION: CHEYENNE VAMC

XUUSER,FIFTY 1000203

SCHEDULE II: Yes

SCHEDULE II NON:

SCHEDULE III: Yes

SCHEDULE III NON:

SCHEDULE IV:

SCHEDULE V:

.

.

.

DIVISION: DENVER-RO

XUUSER,SIXTY 520628843 BT1199125 FEB 2,2007

SCHEDULE II:

SCHEDULE II NON:

SCHEDULE III:

SCHEDULE III NON:

SCHEDULE IV:

SCHEDULE V:

XUUSER,SEVENTY 520628775 AH9494852 FEB 12,1999

SCHEDULE II:

SCHEDULE II NON:

SCHEDULE III:

SCHEDULE III NON:

SCHEDULE IV:

SCHEDULE V:

XUUSER,EIGHTY 520628129 BA4578893 OCT 12,1990

SCHEDULE II: Yes

SCHEDULE II NON: Yes

SCHEDULE III: Yes

SCHEDULE III NON: Yes

SCHEDULE IV: Yes

SCHEDULE V: Yes

.

.

.

### Print PSDRPH Key Holders Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print PSDRPH Key Holders \[XU EPCS PSDRPH\] option prints all active users holding the PSDRPH security key. This report sorts by Division, and within Division, it sorts by Name.

This option prints the following data from the NEW PERSON (#200) file:

- NAME (#.01)
- DUZ—Internal Entry Number (IEN) for the user in the NEW PERSON (#200) file
- GIVEN BY (#1) subfield of the KEYS (#51) Multiple: Person who assigned the PSDRPH security key
- DATE GIVEN (#2) subfield of the KEYS (#51) Multiple: Date assigned

![](kernel-8-0-systems-management-utilities-user-guide/042.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765530" class="anchor"></span>Figure 58: DEA ePCS: Print PSDRPH Key Holders Option—Sample User Entries and Report

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

<span class="mark">7 Print PSDRPH Key Holders</span>

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">7 \<Enter\></span> Print PSDRPH Key Holders

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

PSDRPH KEY HOLDERS APR 15,2013 17:26 PAGE 1

NAME DUZ GIVEN BY DATE GIVEN

--------------------------------------------------------------------------------

DIVISION: EMPTY

XUUSER,SIX 520736417 XUUSER,SIX SEP 20,2012

XUUSER,ONE 520736423 XUUSER,ONE MAR 27,2012

XUUSER,THREE 520736427 XUUSER,THREE MAR 4,2013

XUUSER,FIVE 520736422 XUUSER,FIVE JAN 23,2013

XUUSER,SEVEN 520736428 XUUSER,SEVEN MAR 2,2012

XUUSER,EIGHT 520736430 XUUSER,EIGHT MAR 30,2012

DIVISION: ALBANY, NY VAMC

XUUSER,NINE 520736424 XUUSER,NINE JAN 29,2013

### Print Setting Parameters Privileges Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Setting Parameters Privileges \[XU EPCS SET PARMS\] option prints all active users holding the XUEPCSEDIT security key.

This option identifies individuals responsible for setting the parameters. It prints the following data from the NEW PERSON (#200) file:

- NAME (#.01)
- DUZ—Internal Entry Number (IEN) for the user in the NEW PERSON (#200) file
- GIVEN BY (#1) subfield of the KEYS (#51) Multiple: Person who assigned the PSDRPH security key
- DATE GIVEN (#2) subfield of the KEYS (#51) Multiple: Date assigned

![](kernel-8-0-systems-management-utilities-user-guide/043.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765531" class="anchor"></span>Figure 59: DEA ePCS: Print Setting Parameters Privileges Option—Sample User Entries and Report

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

<span class="mark">8 Print Setting Parameters Privileges</span>

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">8 \<Enter\></span> Print Setting Parameters Privileges

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

USERS RESPONSIBLE FOR SETTING PARAMETERS APR 15,2013 17:28 PAGE 1

NAME DUZ GIVEN BY DATE GIVEN

--------------------------------------------------------------------------------

XUUSER,ONE 520736423 XUUSER,ONE AUG 22,2012

XUUSER,TWO 520736419 XUUSER,TWO APR 3,2012

XUUSER,THREE 520736427 XUUSER,THREE JUL 16,2012

XUUSER,FOUR 520736431 XUUSER,FOUR MAR 19,2012

XUUSER,FIVE 520736422 XUUSER,FIVE JUL 17,2012

### Print Audits for Prescriber Editing Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Audits for Prescriber Editing \[XU EPCS PRINT EDIT AUDIT\] option prints information related to the editing of prescriber information.

The data for this report is retrieved from the XUEPCS DATA (#8991.6) file. It prints the following data:

- DATE/TIME EDITED (#.06)
- NAME (#.01)—This is the name of user edited.
- EDITED BY (#.02)—This is the name of user who edited the data.
- FIELD EDITED (#.03)
- ORIGINAL DATA (#.04)
- EDITED DATA (#.05)

You can sort the data by any of the following data:

- Edited By then Date/Time
- Edited By then User Edited
- Date/Time then Edited By
- Date/Time then User Edited
- User Edited then Edited By
- User Edited then Date

![](kernel-8-0-systems-management-utilities-user-guide/044.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765532" class="anchor"></span>Figure 60: DEA ePCS: Print Audits for Prescriber Editing Option: Sort by Edited By then Date/Time—Sample User Entries and Report

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

<span class="mark">9 Print Audits for Prescriber Editing</span>

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">9 \<Enter\></span> Print Audits for Prescriber Editing

Select one of the following:

<span class="mark">1 Sort by Edited By then Date/time</span>

2 Sort by Edited By then User Edited

3 Sort by Date/time then Edited By

4 Sort by Date/time then User Edited

5 Sort by User Edited then Edited By

6 Sort by User Edited then Date

SORT BY: <span class="mark">1 \<Enter\></span> Sort by Edited By then Date/time

START WITH EDITED BY: FIRST// <span class="mark">\<Enter\></span>

START WITH DATE/TIME EDITED: FIRST// <span class="mark">\<Enter\></span>

START WITH NAME: FIRST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

...HMMM, I'M WORKING AS FAST AS I CAN...

XUEPCS DATA LIST APR 15,2013 17:33 PAGE 1

DATE/TIME EDITED NAME

EDITED BY FIELD EDITED

ORIGINAL DATA

EDITED DATA

--------------------------------------------------------------------------------

MAR 28,2012 11:35 XUUSER,TWO

XUUSER,ONE SCHEDULE II NARCOTIC

1

0

MAR 28,2012 11:41 XUUSER,THREE

XUUSER,ONE SCHEDULE II NARCOTIC

0

1

MAR 28,2012 14:15 XUUSER,FOUR

XUUSER,ONE DEA#

OX4215895

<span id="_Toc204765533" class="anchor"></span>Figure 61: DEA ePCS: Print Audits for Prescriber Editing Option: Sort by User Edited then Edited By—Sample User Entries and Report

SORT BY: <span class="mark">5 \<Enter\></span> Sort by User Edited then Edited By

START WITH NAME: FIRST// <span class="mark">\<Enter\></span>

START WITH EDITED BY: FIRST// <span class="mark">\<Enter\></span>

START WITH DATE/TIME EDITED: FIRST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> HOME (CRT) Right Margin: 80// <span class="mark">\<Enter\></span>

...HMMM, HOLD ON...

XUEPCS DATA LIST APR 15,2013 17:36 PAGE 1

DATE/TIME EDITED NAME

EDITED BY FIELD EDITED

ORIGINAL DATA

EDITED DATA

--------------------------------------------------------------------------------

MAR 28,2012 11:35 XUUSER,TWO

XUUSER,ONE SCHEDULE II NARCOTIC

1

0

MAR 28,2012 11:41 XUUSER,THREE

XUUSER,ONE SCHEDULE II NARCOTIC

0

1

MAR 28,2012 14:15 XUUSER,FOUR

XUUSER,ONE DEA#

OX4215895

### Task Changes to DEA Prescribing Privileges Report Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-systems-management-utilities-user-guide/045.png) CAUTION: Verify that the XUEPCS REPORT DEVICE parameter has been set before using this option.  
  
To set the parameter, see the “[Set the XUEPCS REPORT DEVICE Parameter](#set-the-xuepcs-report-device-parameter)” section.

The Task Changes to DEA Prescribing Privileges Report \[XU EPCS LOGICAL ACCESS\] option prints the setting or change to DEA prescribing privileges related to issuance of a controlled substance prescription.

The option only prints data from the previous day and with data that has been modified. The data is retrieved from the XUEPCS DATA (#8991.6) file.

This option should be scheduled to run daily using TaskMan. The option only prints data from the *previous* day and with *data that has been modified*. The data is retrieved from the XUEPCS DATA (#8991.6) file.

![](kernel-8-0-systems-management-utilities-user-guide/046.png) NOTE: No data is displayed to the screen; the data is printed to the device indicated by the XUEPCS REPORT DEVICE parameter.

![](kernel-8-0-systems-management-utilities-user-guide/047.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

To schedule the option to run daily using TaskMan, do the following:

1.  From the Systems Manager Menu \[EVE\], select the Taskman Management \[XUTM MGR\] option.
2.  At the “Select Taskman Management Option:” prompt, select the Schedule/Unschedule Options \[XUTM SCHEDULE\] option.
3.  At the “Select OPTION to schedule or reschedule:” prompt, enter XU EPCS LOGICAL ACCESS.
4.  At the “...OK? Yes//” prompt, enter YES. A ScreenMan dialog is displayed.
5.  Tab down to the following fields and enter the values shown:
- QUEUED TO RUN AT WHAT TIME: T+1@001 (which means start running it tomorrow at 12:01)
- RESCHEDULING FREQUENCY: 1D (which means run it daily)
6.  At the “COMMAND:” prompt, enter Save.
7.  At the “COMMAND:” prompt, enter Exit.

<span id="_Toc204765534" class="anchor"></span>Figure 62: DEA ePCS: Task Changes to DEA Prescribing Privileges Report Option: TaskMan schedule setup—Sample User Entries

Device Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

FM1 VA FileMan ...

JL Consolidated Practitioner's Menu ...

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Menu Management ...

Verifier Tools Menu ...

Select Systems Manager Menu Option: <span class="mark">TASK \<Enter\></span> man Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

TU TASK UTILITY

VPD Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: <span class="mark">SCHED \<Enter\></span> ule/Unschedule Options

Select OPTION to schedule or reschedule: <span class="mark">XU EPCS LOGICAL ACCESS \<Enter\></span> Task Changes to DEA Prescribing Privileges Report

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

\(R\)

Edit Option Schedule

<u>Option Name</u>: <span class="mark">XU EPCS LOGICAL ACCESS</span>

Menu Text: <span class="mark">Task Changes to DEA Prescribing</span> TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span class="mark">QUEUED TO RUN AT WHAT TIME:</span> <span class="mark">T+1@001 \<Enter\></span>

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

<span class="mark">RESCHEDULING FREQUENCY:</span> <span class="mark">1D \<Enter\></span>

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">SAVE</span> Press \<PF1\>H for help Insert

.

.

.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">EXIT</span> Press \<PF1\>H for help Insert

Select OPTION to schedule or reschedule:

<span id="_Toc204765535" class="anchor"></span>Figure 63: DEA ePCS: Task Changes to DEA Prescribing Privileges Report Option—Sample User Entries (No Report Displays)

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

<span class="mark">10 Task Changes to DEA Prescribing Privileges Report</span>

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">10 \<Enter\></span> Task Changes to DEA Prescribing Privileges Report

### Task Allocation Audit of PSDRPH Key Report Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-systems-management-utilities-user-guide/048.png) CAUTION: Verify that the XUEPCS REPORT DEVICE parameter has been set before using this option.  
  
To set the parameter, see the “[Set the XUEPCS REPORT DEVICE Parameter](#set-the-xuepcs-report-device-parameter)” section.

The Task Allocation Audit of PSDRPH Key Report \[XU EPCS PSDRPH AUDIT\] option prints the allocation of the PSDRPH security key audit report to a device previously selected during setup (that is XUEPCS REPORT DEVICE parameter).

This option should be scheduled to run daily using TaskMan. The option only prints data from the previous day and with data that has been modified. The data is retrieved from the XUEPCS PSDRPH AUDIT (#8991.7) file.

![](kernel-8-0-systems-management-utilities-user-guide/049.png) NOTE: No data is displayed to the screen; the data is printed to the device indicated by the XUEPCS REPORT DEVICE parameter.

![](kernel-8-0-systems-management-utilities-user-guide/050.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

To schedule the option to run daily using TaskMan, do the following:

1.  From the Systems Manager Menu \[EVE\], select the Taskman Management \[XUTM MGR\] option.
8.  At the “Select Taskman Management Option:” prompt, select the Schedule/Unschedule Options \[XUTM SCHEDULE\] option.
9.  At the “Select OPTION to schedule or reschedule:” prompt, enter XU EPCS PSDRPH AUDIT.
10. At the “...OK? Yes//” prompt, enter YES. A ScreenMan dialog is displayed.
11. Tab down to the following fields and enter the values shown:
- QUEUED TO RUN AT WHAT TIME: T+1@001 (which means start running it tomorrow at 12:01)
- RESCHEDULING FREQUENCY: 1D (which means run it daily)
12. At the “COMMAND:” prompt, enter Save.
13. At the “COMMAND:” prompt, enter Exit.

<span id="_Toc204765536" class="anchor"></span>Figure 64: DEA ePCS: Task Allocation Audit of PSDRPH Key Report Option: TaskMan Schedule Setup—Sample User Entries

Device Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

FM1 VA FileMan ...

JL Consolidated Practitioner's Menu ...

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Menu Management ...

Verifier Tools Menu ...

Select Systems Manager Menu Option: <span class="mark">TASK \<Enter\></span> man Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

TU TASK UTILITY

VPD Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: <span class="mark">SCHED \<Enter\></span> ule/Unschedule Options

Select OPTION to schedule or reschedule: <span class="mark">XU EPCS PSDRPH AUDIT \<Enter\></span> Task Allocation Audit of PSDRPH Key Report

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

\(R\)

Edit Option Schedule

<u>Option Name</u>: <span class="mark">XU EPCS PSDRPH AUDIT</span>

Menu Text: <span class="mark">Task Allocation Audit of PSDRPH</span> TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span class="mark">QUEUED TO RUN AT WHAT TIME:</span> <span class="mark">T+1@001 \<Enter\></span>

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

<span class="mark">RESCHEDULING FREQUENCY:</span> <span class="mark">1D \<Enter\></span>

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">SAVE</span> Press \<PF1\>H for help Insert

.

.

.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: <span class="mark">EXIT</span> Press \<PF1\>H for help Insert

Select OPTION to schedule or reschedule:

<span id="_Toc204765537" class="anchor"></span>Figure 65: DEA ePCS: Task Allocation Audit of PSDRPH Key Report Option—Sample User Entries (No Report Displays)

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

<span class="mark">11 Task Allocation Audit of PSDRPH Key Report</span>

12 Allocate/De-Allocate of PSDRPH Key

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">11 \<Enter\></span> Task Allocation Audit of PSDRPH Key Report

<span id="_Ref353961797" class="anchor"></span>Figure 66: DEA ePCS: Task Allocation Audit of PSDRPH Key Report Option—Sample Report Printed to Device Entered into the XUEPCS REPORT DEVICE Parameter

<span class="mark">PSDRPHKEY AUDIT LIST</span> APR 16,2013 16:32 PAGE 1

NAME

ALLOCATION

EDITED BY STATUS DATE/TIME EDITED

----------------------------------------------------------------------------------

XUUSER,ONE XUUSER,TWO ALLOCATED APR 15,2013 15:33

XUUSER,ONE XUUSER,TWO DE-ALLOCATED APR 15,2013 16:33

### Allocate/De-Allocate of PSDRPH Key Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Allocate/De-Allocate of PSDRPH Key \[XU EPCS PSDRPH KEY\] option allocates or de-allocates the PSDRPH security key.

![](kernel-8-0-systems-management-utilities-user-guide/051.png) NOTE: All user security keys are stored in the KEYS (#51) Multiple field in the NEW PERSON (#200) file.

![](kernel-8-0-systems-management-utilities-user-guide/052.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765539" class="anchor"></span>Figure 67: DEA ePCS: Allocate/De-Allocate of PSDRPH Key Option: Allocating PSDRPH—Sample User Entries

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

<span class="mark">12 Allocate/De-Allocate of PSDRPH Key</span>

13 Edit Facility DEA# and Expiration Date

Select ePCS DEA Utility Functions Option: <span class="mark">12 \<Enter\></span> Allocate/De-Allocate of PSDRPH Key

Enter User Name: <span class="mark">XUSER \<Enter\></span>

1 XUUSER,ONE OX

2 XUUSER,TWO TX 192 SYSTEMS ANALYST

3 XUUSER,THREE B TBX

4 XUUSER,FOUR FX

5 XUUSER,FIVE A FAX

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">2 \<Enter\></span> XUUSER,TWO TX 192 SYSTEMS ANALYST

<span class="mark">Allocate PSDRPH</span> for XUUSER,TWO? YES// <span class="mark">\<Enter\></span>

<span id="_Toc204765540" class="anchor"></span>Figure 68: DEA ePCS: Allocate/De-Allocate of PSDRPH Key Option: De-allocating PSDRPH—Sample User Entries

Select ePCS DEA Utility Functions Option: <span class="mark">12 \<Enter\></span> Allocate/De-Allocate of PSDRPH Key

Enter User Name: <span class="mark">XUUSER,TWO \<Enter\></span> XUUSER,TWO TX 192 SYSTEMS ANALYST

<span class="mark">De-allocate PSDRPH</span> for XUUSER,TWO? YES// <span class="mark">\<Enter\></span>

![](kernel-8-0-systems-management-utilities-user-guide/053.png) REF: To review the audit history of the allocation and de-allocation of the PSDRPH security key, see the sample report generated from the Task Allocation Audit of PSDRPH Key Report \[XU EPCS PSDRPH AUDIT\] option in <u>Figure 66</u>.

### Edit Facility DEA# and Expiration Date Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Facility DEA# and Expiration Date \[XU EPCS EDIT DEA# AND XDATE\] option edits the FACILITY DEA NUMBER (#52) and FACILITY DEA EXPIRATION DATE (#52.1) fields in the INSTITUTION (#4) file.

![](kernel-8-0-systems-management-utilities-user-guide/054.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

<span id="_Toc204765541" class="anchor"></span>Figure 69: DEA ePCS: Edit Facility DEA# and Expiration Date Option—Sample User Entries

1 Print DEA Expiration Date Null

2 Print DISUSER DEA Expiration Date Null

3 Print DEA Expiration Date Expires 30 days

4 Print DISUSER DEA Expiration Date Expires 30 days

5 Print Prescribers with Privileges

6 Print DISUSER Prescribers with Privileges

7 Print PSDRPH Key Holders

8 Print Setting Parameters Privileges

9 Print Audits for Prescriber Editing

10 Task Changes to DEA Prescribing Privileges Report

11 Task Allocation Audit of PSDRPH Key Report

12 Allocate/De-Allocate of PSDRPH Key

<span class="mark">13 Edit Facility DEA# and Expiration Date</span>

Select ePCS DEA Utility Functions Option: <span class="mark">13 \<Enter\></span> Edit Facility DEA# and Expiration Date

Select INSTITUTION NAME: <span class="mark">SAN FRANCISCO \<Enter\></span>

1 SAN FRANCISCO CA VAMC 662

2 SAN FRANCISCO CA VCSFO 782

3 SAN FRANCISCO CA NC 903

4 SAN FRANCISCO-OPT CA

5 SAN FRANCISCO-RO CA RO 343

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">1 \<Enter\></span> SAN FRANCISCO CA VAMC 662

FACILITY DEA NUMBER: BB1234563// <span class="mark">? \<Enter\></span>

Answer with a DEA ID, must be 9 characters in length

FACILITY DEA NUMBER: BB1234563// <span class="mark">\<Enter\></span>

FACILITY DEA EXPIRATION DATE: SEP 9,2011// <span class="mark">\<Enter\></span>

Select INSTITUTION NAME:

### ePCS Edit Prescriber Data Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS Edit Prescriber Data \[XU EPCS EDIT DATA\] option is a Broker-type context option that is given to those individuals who are permitted to edit the data related to e-prescribing of controlled substances.

This option is locked with the XUEPCSEDIT security key.

![](kernel-8-0-systems-management-utilities-user-guide/055.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

### ePCS Set SAN from PIV Card Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ePCS Set SAN from PIV Card \[XUSSPKI UPN SET\] option is a Broker-type context option that sets the SUBJECT ALTERNATIVE NAME (#501.2) field (aka SAN field or USER PRINCIPLE NAME) in the NEW PERSON (#200) file from the Personal Identification Verification (PIV) Smart Card. This is used with the DEA ePCS electronic signature (e-sig) to be sure the correct certificate is selected from the PIV card.

![](kernel-8-0-systems-management-utilities-user-guide/056.png) NOTE: This option only needs to be run once for a user at a site.

![](kernel-8-0-systems-management-utilities-user-guide/057.png) NOTE: This option was released with Kernel patch XU\*8.0\*580.

#### XUSSPKI SAN Bulletin

Released with Kernel patch XU\*8.0\*580, the XUSSPKI SAN bulletin is sent when the SUBJECT ALTERNATIVE NAME (#501.2) field in the NEW PERSON (#200) file has been changed or deleted. The bulletin is sent to users holding the PSDMGR security key.

- Subject: “Subject Alternative Name” field
- Message: The “Subject Alternative Name” field in New Person File (#200) has been changed or deleted for: \|3\|  
  Before: \|1\|After:\|2\|

![](kernel-8-0-systems-management-utilities-user-guide/058.png) NOTE: If this value is NULL, the field was deleted!

- Parameters:
- \|1\|—Old value before changed or deleted.
- \|2\|—New value. If NULL, value was deleted.
- \|3\|—Name of the user.

## Prescription Validation and Verification Process—PKIServer.exe Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PKIServer.exe is an application that runs as a service application to handle verification of prescriptions that have been entered using the electronic prescribing of controlled substances (ePCS) in the Computerized Patient Record System (CPRS) application. The PKIServer.exe application itself is written in the Delphi language and uses the cryptographic APIs within the Windows operating system.

![](kernel-8-0-systems-management-utilities-user-guide/059.png) REF: For more information on cryptographic functions, see the “[Windows Authentication and Cryptographic Operations](#windows-authentication-and-cryptographic-operations)” section.

![](kernel-8-0-systems-management-utilities-user-guide/060.png) NOTE: The VA was the original test site (at the Hines VAMC) for ePCS for the DEA starting in 2002 with code in CPRS for this purpose. That test site has continued to use this functionality (and the functionality has been in CPRS) until the current time. The DEA has now come up with the final rules for the use of ePCS and the version of CPRS that is currently in testing moves the functionality to meet the final regulations and expands its use to all sites instead of the single Hines site.

There is code within CPRS that handles the following:

- Cryptographic functionalities involved in verifying the provider’s pin value for the PIV card (the original testing used cards provided by DEA).

![](kernel-8-0-systems-management-utilities-user-guide/061.png) REF: For more information on cryptographic functions, see the “[Windows Authentication and Cryptographic Operations](#windows-authentication-and-cryptographic-operations)” section.

- Validation of the PIV card with respect to expiration or revocation.

![](kernel-8-0-systems-management-utilities-user-guide/062.png) REF: For more information on revoked VA PIV cards, see the “[PIV Card Validation—Revocation Server](#piv-card-validationrevocation-server)” section.

- Creation of the hash for the aggregate prescription data and signing of that hash. The signed hash is created so that it contains a copy of the signing certificate as well.

At the time that the pharmacist goes to fill the prescription there are requirements that the prescription be validated to ensure that there have been no changes to the data associated with the prescription before it is filled. The pharmacist works within the VistA roll-and-scroll environment, which does *not* offer the capabilities required to provide the cryptographic checks necessary.

To validate the prescription using cryptographic checks, the system performs the following procedure:

1.  VistA Pharmacy code passes the current data associated with the prescription and the signed hash value through Kernel utilities to a server location identified by the PKI SERVER (#53.1) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file. There can be up to three IP addresses separated by caret characters (^) in this field. This connects the VistA server to the PKIServer service (identified in the services functionality as PKI_Verify_Service).
2.  PKIServer takes the input data and extracts the signing certificate and original hash from the signed hash.
3.  PKIServer creates a hash of the current data passed in for the prescription.
4.  PKIServer compares the two hashes:
- Hashes match—If the two hashes match, indicating no change in the data, the PKIServer then checks whether the certificate has been revoked (see [Step 5](#validate_prescription_step_05)).
- Hashes do *not* match—If any changes have occurred in the data currently associated with the prescription, the two hashes differ:
1.  PKIServer returns a value indicating prescription is returned.
3.  Prescription is voided.
5.  <span id="validate_prescription_step_05" class="anchor"></span>PKIServer checks whether the certificate has been revoked:
- Active Certificate—If the hashes match and there is confirmation that the certificate has *not* been revoked, the prescription is approved.
- Revoked Certificate—If the provider’s certificate has been revoked, the prescription is voided as well.
- Pending Certificate Check—There may be cases where there are problems in checking the certificate and a return value in this case may indicate that they should wait and check the prescription later.

To meet the DEA requirements, newer, higher level cryptographic methods are required than were previously used in the original Hines testing, and these may require that older server systems be patched to ensure that capabilities (such as SHA-2) are available. Also, the VA has been moving to use functionality (such as Tumbleweed Desktop Validator) to assist in checking certificate statuses, and so on. The PKIServer.exe application does *not* call these directly; however, if they are available, they are called by the Windows operating system using the cryptographic APIs.

![](kernel-8-0-systems-management-utilities-user-guide/063.png) REF: For more information on the PKIServer.exe application, see the *DEA e-Prescribing Installation and Setup Guide* located under CPRS on the VDL: [VDL CPRS Application Documents](http://www.va.gov/vdl/application.asp?appid=61)

## PIV Card Validation—Revocation Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Revocation Server contains a Certificate Revocation List (CRL), which is a list of all revoked VA PIV cards. The distinction is that if a physician prescribes a drug, and then the physician’s certificate expires *before* the prescription is filled, it can still be filled, since it was written *before* it expired. If, however, the physician’s certificate is revoked, then any orders that have *not* been filled are cancelled and *cannot* be filled. In many cases, certificates are revoked due to a change in affiliation.

To check the CRL to see if a PIV card has been revoked, do the following:

1.  Insert the PIV card.
2.  Double click on (or keyboard equivalent) the ActivClient Agent to open it.
3.  Select the My Certificates icon.
4.  Select and double click on (or keyboard equivalent) one of the certificates.
5.  Select the Advanced tab.
6.  Scroll down to find and select the CRL Distribution Points entry. The CRL is the Certificate Revocation List.
7.  Scroll down and see the contents for this entry. You should probably find an entry for the following:
- one http: entry
- one ldap: entry. For example:

URL=http://cdp1.ssp-strong-id.net/CDP/vauser.crl

8.  Copy the http:// URL address and paste it into a Web browser. It brings up a long list of all certificates that have been revoked (as opposed to expired, cancelled, and so on). You should get approximately 30 Megabytes for the Web page.  
      
    The Tumbleweed Desktop Validator is supposed to assist with this if it is on the desktop, and it updates itself at intervals, so that the call does *not* have to be made to the site for each individual request.

## Windows Authentication and Cryptographic Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA’s attempt to use Microsoft<sup>®</sup> Windows-level authentication to access VistA accounts using a secure intermediary authentication server was set to be released in the late 1990s by the Enterprise Single Sign-On (ESSO) patch. During that time the Office of Cyber Security informed the VA that they had a better way and would implement it within six months. Subsequently, the VA stopped the release of the ESSO patch, but nothing more happened regarding Microsoft<sup>®</sup> Windows level authentication.

In 2015, the VA began development of Single Sign-On Internal (SSOi) using Identity and Access Management (IAM) Secure Token Service (STS) to enable 2-Factor Authentication (2FA) of VA employees into VistA. Kernel patches XU\*8.0\*655 and XU\*8.0\*659 enable authentication into VistA using an STS token obtained from IAM. Single Sign-On External (SSOe) authentication of veterans and *non*-VA VistA users is currently in development.

### Current Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Kernel provides the mechanism to authenticate a user with an STS token obtained from IAM. VistA does *not* do direct authentication of a user using a PIV card or similar means. Authentication using a PIV card is delegated to IAM. VistA validates a PKI certificate and digital signature from IAM to secure the delegated authentication process. This process is currently enabled for Remote Procedure Call (RPC) Broker and VistALink applications.

CPRS v30 can handle the electronic prescribing of controlled substances, but all cryptographic operations are handled through the client workstation (for the signing of the prescription). This is before the data is passed to the VistA server, along with a copy of the signed hash generated based on the data for the prescription. At the time of filling of the prescription by the VA pharmacist, the data for the prescription along with a copy of the signed hash is transferred by VistA to a PKIService application. This PKIService application runs on a separate server or workstation for verification that the data associated with the prescription has *not* changed. It compares the original hash value with one created based on the current data.

![](kernel-8-0-systems-management-utilities-user-guide/064.png) REF: For more information on the PKIService verification process, see the “[Prescription Validation and Verification Process—PKIServer.exe Application](#prescription-validation-and-verification-processpkiserver.exe-application)” section.

### Future Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Terminal access (roll-and-scroll) VistA 2-Factor Authentication (2FA) is currently in development. This process will require a script within the terminal emulator software to call IAM to authenticate the user through PIV or similar means and then send the returned STS token to VistA for authentication and identification of the user. Single Sign-On External (SSOe) is currently in development to use 2-Factor Authentication (2FA) to authenticate and identify external (*non*-VistA) users to obtain or edit data within VistA. External users include:

- Veterans
- Department of Defense (DoD) users
- *Non*-VA providers who require access to veteran data.

External users will be required to authenticate with IAM and use the returned STS token to authenticate and identify the user within VistA. Since these users might *not* be currently “known” to VistA, a means of role-based authorization is required to provision the users on-the-fly and restrict their access to specific data based upon their role. Role-based authorization for external VistA users has yet to be developed.

# National Provider Identifier (NPI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Provider Identifier (NPI) is a unique 10-digit identification number issued by the Centers for Medicare and Medicaid Services (CMS) to all healthcare providers in the United States.

To apply for an NPI, visit the [National Plan and Provider Enumeration System (NPPES)](https://nppes.cms.hhs.gov/NPPES) site.

![](kernel-8-0-systems-management-utilities-user-guide/065.png) REF: For instructions on how to apply for an NPI, see the [*How to Apply for an NPI Online*](https://nppes.cms.hhs.gov/assets/How_to_apply_for_an_NPI_online.pdf) document.

To search for your NPI and corresponding information, visit the [National Provider Identifier (NPI) Registry](https://nppes.cms.hhs.gov/NPPES). All information produced by the NPI Registry is provided in accordance with the National Plan and Provider Enumeration System (NPPES) Data Dissemination Notice.

## VHA and NPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) maintains the requirement that all individual Department of Veterans Affairs (VA) health care providers providing billable VA health care services have a valid NPI and associated Taxonomy Code. Each VHA Billable Practitioner should have applied for the NPI through CMS' NPPES. NPI Confirmation Letters are sent by CMS and indicate the NPI assigned. VHA Practitioners can present their NPI Confirmation Letter as a source document to verify the accuracy of the NPI, or they can contact their Local NPI Maintenance Team Leader for assistance. You can use NPI to link providers in VA and Medicare.

![](kernel-8-0-systems-management-utilities-user-guide/066.png) REF: For more information regarding NPI and its requirements within the VA, see [<u>VHA Directive 1066</u>](https://www.va.gov/vhapublications/ViewPublication.asp?pub_ID=9180).

NPI Coordinators and NPI Liaison personnel at a site use the [NPI options](#npi-vista-options) described in this section to maintain proper credentialing and Taxonomy Code updates as needed.

![](kernel-8-0-systems-management-utilities-user-guide/067.png) NOTE: In VistA, the NPI number is stored in the NPI (#41.99) field in the NEW PERSON (#200) file. This section concentrates only on the NEW PERSON (#200) file.

## NPI Registry and Data Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CMS provides a National Plan and Provider Enumeration System (NPPES) Downloadable File, which is also referred to as the NPI Downloadable File or the Full Replacement Monthly NPI File.

In addition to the current Full Replacement Monthly NPI File, CMS also makes available a Weekly Incremental NPI File for downloading. These Weekly Incremental NPI Files are in the same format as the current Full Replacement Monthly NPI File; however, the Weekly Incremental NPI File only include data for a given week.

The Weekly Incremental NPI Files assist users by providing them with more up-to-date information and includes:

- Newly assigned NPIs.
- Updates to NPI data.
- Newly deactivated NPIs covering that week.

![](kernel-8-0-systems-management-utilities-user-guide/068.png) NOTE: The Weekly Incremental NPI File is a supplemental file to be used in conjunction with the Full Replacement Monthly NPI File until the next Full Replacement Monthly NPI File is made available.

In September 2007, CMS began disclosing National Plan and Provider Enumeration System (NPPES) health care provider data that are disclosable under the Freedom of Information Act (FOIA) to the public. In accordance with the e-FOIA Amendments, CMS has disclosed these data through the Internet in two forms:

- [NPI Registry](https://npiregistry.cms.hhs.gov/search): The NPI Registry is a query-only database that is updated daily to enable users to query the NPPES (such as search by NPI, provider name, and so on) and retrieve the FOIA-disclosable data from the search results. There is no charge to view the data.
- [NPI Downloadable File](http://download.cms.gov/nppes/NPI_Files.html):
- Full Replacement Monthly NPI File.
- Weekly Incremental NPI File.
- Full Replacement NPI Deactivation File.

There is no charge to download the data.

![](kernel-8-0-systems-management-utilities-user-guide/069.png) REF: For more information on the NPPES, see the [CMS Data Dissemination website](https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination).

## NPI VistA Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Provider Identifier (NPI) Utility consists of the following standalone menu and options, which are described in detail in the sections that follow:

- <u>List of NPI data for CBO</u> Option
- <u>XUS NPI EXTRACT REPORT Option</u>
- <u>NPI (National Provider ID) Menu</u>:
- <u>Add/Edit NPI values for Providers</u> Option
- <u>Mark/Unmark Provider Exempt from requiring</u> an NPI Option
- <u>Print Local NPI Reports Option</u>

![](kernel-8-0-systems-management-utilities-user-guide/070.png) NOTE: The NPI (National Provider ID) Menu \[XUS NPI MENU\] is locked with the XUSNPIMTL security key.

- <u>PROVIDER NPI SELF ENTRY Option</u>

![](kernel-8-0-systems-management-utilities-user-guide/071.png) NOTE: The Load Institution NPI values option is currently marked Out of Order. You should use the Update/refresh Institution file with IMF data \[XUMF LOAD INSTITUTION\] option.

### Adding NPI Options to Secondary Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NPI options fall under the Kernel XUS namespace. None of these NPI options are attached to a parent menu, other than the three options that are attached to the <u>NPI (National Provider ID) Menu</u>. To access and run these options they *must* be added as Secondary Options.

To add an NPI option as a Secondary Menu Option, from the Kernel Systems Manager Menu \[EVE\], do the following (<u>Figure 70</u> and <u>Figure 71</u>):

<span id="_Ref163223608" class="anchor"></span>Figure 70: Adding an NPI Option to a User as a Secondary Menu Option (1 of 2)

Core Applications ...

Device Management ...

FM VA FileMan ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

<span class="mark">User Management ...</span>

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">USER \<Enter\></span> Management

Add a New User to the System

Grant Access by Profile

<span class="mark">Edit an Existing User</span>

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

Electronic Signature Block Edit

List Inactive Person Class Users

Manage User File ...

OAA Trainee Registration Menu ...

Person Class Edit

Reprint Access agreement letter

Select User Management \<TEST ACCOUNT\> Option: <span class="mark">EDIT</span><span class="mark">\<Enter\></span> an Existing User

Select NEW PERSON NAME: XUUSER,ONE OX

Edit an Existing User

NAME: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME... XUUSER,ONE INITIAL: OX

TITLE: NICK NAME: One

SSN: 000364567 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

PRIMARY MENU OPTION: EVE

Select SECONDARY MENU OPTIONS: <span class="mark">XUS NPI MENU \<Enter\></span>

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE: @

Want to edit VERIFY CODE (Y/N):

Select DIVISION:

SERVICE/SECTION: INFORMATION SYSTEMS CENTER

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NPI (National Provider ID) Menu

Are you adding 'XUS NPI MENU' as

a new SECONDARY MENU OPTIONS (the 1ST for this NEW PERSON)? No// <span class="mark">YES \<Enter\></span>

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref163218739" class="anchor"></span>Figure 71: Adding an NPI Option to a User as a Secondary Menu Option (2 of 2)

Edit an Existing User

NAME: XUUSER,ONE Page 1 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME... XUUSER,ONE INITIAL: OX

TITLE: NICK NAME: One

SSN: 000364567 DOB:

DEGREE: MAIL CODE:

DISUSER: TERMINATION DATE:

Termination Reason:

┌──────────────────────────────────┐

Select │ SECONDARY MENU OPTIONS │

Want to │ │

Want to │ SECONDARY MENU OPTIONS: <span class="mark">XUS NPI MENU</span> │

│ SYNONYM: │

│ │

└──────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Close Refresh

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: <span class="mark">Close</span> Press \<PF1\>H for help Insert

You will repeat this process until you add all parentless NPI options to your Secondary Menu Options. Once completed, the user can then access the NPI options from their list of Secondary Menu Options.

To verify you have added all NPI options as Secondary Menu Options for the user, from the Kernel Systems Manager Menu \[EVE\], do the following (<u>Figure 72</u>):

<span id="_Ref163223567" class="anchor"></span>Figure 72: Verifying NPI Option Added to a User as a Secondary Menu Options

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">?? \<Enter\></span>

Core Applications ... \[XUCORE\]

Device Management ... \[XUTIO\]

FM VA FileMan ... \[DIUSER\]

Menu Management ... \[XUMAINT\]

Programmer Options ... \[XUPROG\]

\*\*\> Locked with XUPROG

Operations Management ... \[XUSITEMGR\]

Spool Management ... \[XU-SPL-MGR\]

Information Security Officer Menu ... \[XUSPY\]

Taskman Management ... \[XUTM MGR\]

User Management ... \[XUSER\]

Application Utilities ... \[XTMENU\]

Capacity Planning ... \[XTCM MAIN\]

Manage Mailman ... \[XMMGR\]

You can also select a <span class="mark">secondary option</span>:

<span class="mark">List of NPI data for CBO \[XUS NPI CBO LIST\]</span>

<span class="mark">NPI (National Provider ID) Menu ... \[XUS NPI MENU\]</span>

\*\*\> Locked with XUSNPIMTL

<span class="mark">NPI Signon Check \[XUS NPI SIGNON CHECK\]</span>

<span class="mark">PROVIDER NPI SELF ENTRY \[XUS NPI PROVIDER SELF ENTRY\]</span>

<span class="mark">XUS NPI EXTRACT REPORT \[XUS NPI EXTRACT\]</span>

. . .

### List of NPI data for CBO Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List of NPI data for CBO \[XUS NPI CBO LIST\] option lists providers related to the NPI rollout. This list is sent to the Chief Business Office (CBO) monthly for tracking status of the rollout. The CBO group should use TaskMan to schedule this option to run monthly. Since the list is sent to the CBO by an email message (<u>Figure 73</u>), there is no further output sent to the screen, so the user is returned to the menu list.

![](kernel-8-0-systems-management-utilities-user-guide/072.png) NOTE: The CBOLIST^XUSNPIED routine runs this option.

<span id="_Ref167354303" class="anchor"></span>Figure 73: List of NPI Data for CBO Report—Sample CBO Message

From: XUUSER.ONE@\<REDACTED\>.VA.GOV \<XUUSER.ONE@\<REDACTED\>.VA.GOV\>

Sent: Wednesday, May 15, 2024 4:58 PM

To: "G.NPI EXTRACT VERIFICATION"@\<REDACTED\>.VA.GOV

Subject: Station 662(TEST) NPI CROSSWALK EXTRACT SUMMARY

SUMMARY

-------

Station: 662^SAN FRANCISCO^CA^94121-1563 5/15/24@13:58:15

Type 1 NEW PERSON FILE (#200) 1 Message(s) Totaling 13 NPI records.

Type 2 INSITUTION FILE (#4) 1 Message(s) Totaling 15 NPI records.

Type 1 NON VA Individual (#355.93) 1 Message(s) Totaling 1 NPI records.

Type 2 NON VA Facility/Group (#355.93) 1 Message(s) Totaling 0 NPI records.

Programmer Notes: 548.14 - TEST

----------------------------------------------------------------------------------

MESSAGE DETAILS

---------------

TYPE MESSAGE NUMBER RECORD COUNT

---------- -------------- ------------

1 1 13

2 1 15

1 (Non-VA) 1 1

2 (Non-VA) 1 0

----------------------------------------------------------------------------------

### XUS NPI EXTRACT REPORT Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUS NPI EXTRACT REPORT \[XUS NPI EXTRACT REPORT\] option compiles the NPI Extract file and emails it to:

XXX@Q-NPS.VA.GOV

The extract is sent to the specified mail group by an email message. This mail group is set up and maintained at the Austin Information Technology Center (AITC) in Austin, Texas. It is populated with members who are responsible for reviewing the contents of this file. AITC should schedule this option to run as needed. There is no further output sent to the screen, and the user is returned to the menu list.

![](kernel-8-0-systems-management-utilities-user-guide/073.png) NOTE: The TASKMAN^XUSNPIX1 routine runs this option.

### NPI (National Provider ID) Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NPI (National Provider ID) Menu \[XUS NPI MENU\] menu provides the ability to enter data for a provider related to the National Provider ID. It includes the following options:

- [Add/Edit NPI values for Providers](#addedit-npi-values-for-providers-option) \[XUS NPI ENTER NPI FOR PROVIDER\]
- [Mark/Unmark Provider Exempt from requiring an NPI](#markunmark-provider-exempt-from-requiring-an-npi-option) \[XUS NPI EXEMPT PROVIDER\]
- [Print Local NPI Reports](#print-local-npi-reports-option) \[XUS NPI LOCAL REPORTS\]

<span id="_Toc192501596" class="anchor"></span>Figure 74: NPI (National Provider ID) Menu

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">NPI \<Enter\></span>

<span class="mark">1 NPI (National Provider ID) Menu</span>

2 NPI Signon Check

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> NPI (National Provider ID) Menu

Add/Edit NPI values for Providers

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option:

The NPI (National Provider ID) Menu \[XUS NPI MENU\] menu is locked with the XUSNPIMTL security key.

![](kernel-8-0-systems-management-utilities-user-guide/074.png) REF: To allocate the XUSNPIMTL security key, see the “<u>Allocating XUSNPIMTL Security Key</u>” section.

#### Allocating XUSNPIMTL Security Key

To allocate the XUSNPIMTL security key, do the following (<u>Figure 75</u>):

<span id="_Ref174426538" class="anchor"></span>Figure 75: Allocating the XUSNPIMTL Security Key to a User

Core Applications ...

Device Management ...

FM VA FileMan ...

<span class="mark">Menu Management ...</span>

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">MENU \<Enter\></span> Management

Edit options

<span class="mark">Key Management ...</span>

Secure Menu Delegation ...

Restrict Availability of Options

Option Access By User

List Options by Parents and Use

Fix Option File Pointers

Help Processor ...

OPED Screen-based Option Editor

Display Menus and Options ...

Menu Rebuild Menu ...

Out-Of-Order Set Management ...

See if a User Has Access to a Particular Option

Show Users with a Selected primary Menu

Select Menu Management \<TEST ACCOUNT\> Option: <span class="mark">KEY \<Enter\></span> Management

<span class="mark">Allocation of Security Keys</span>

De-allocation of Security Keys

Enter/Edit of Security Keys

All the Keys a User Needs

Change user's allocated keys to delegated keys

Delegate keys

Keys For a Given Menu Tree

List users holding a certain key

Remove delegated keys

Show the keys of a particular user

Select Key Management \<TEST ACCOUNT\> Option: <span class="mark">ALLO \<Enter\></span> cation of Security Keys

Allocate key: <span class="mark">XUSNPIMTL \<Enter\></span>

Another key: <span class="mark">\<Enter\></span>

Holder of key: <span class="mark">XUUSER \<Enter\></span> XUUSER,ONE OX

Another holder: <span class="mark">\<Enter\></span>

You've selected the following keys:

XUSNPIMTL

You've selected the following holders:

XUUSER,ONE

You are allocating keys. Do you wish to proceed? YES// <span class="mark">\<Enter\></span>

XUSNPIMTL being assigned to:

XUUSER,ONEM

Allocation of Security Keys

De-allocation of Security Keys

Enter/Edit of Security Keys

All the Keys a User Needs

Change user's allocated keys to delegated keys

Delegate keys

Keys For a Given Menu Tree

List users holding a certain key

Remove delegated keys

Show the keys of a particular user

Select Key Management \<TEST ACCOUNT\> Option:

#### Add/Edit NPI values for Providers Option

Support staff use the Add/Edit NPI values for Providers \[XUS NPI ENTER NPI FOR PROVIDER\] option to enter data related to an NPI value for providers.

![](kernel-8-0-systems-management-utilities-user-guide/075.png) NOTE: The CLEREDIT^XUSNPIED routine runs this option.

This section includes the following examples using the Add/Edit NPI values for Providers \[XUS NPI ENTER NPI FOR PROVIDER\] option:

- <u>Example 1—Successfully Entering NPI Value</u> for a Provider Who Requires an NPI.
- <u>Example 2—Verifying an NPI Value</u> is Already Associated with a Provider.
- <u>Example 3—Delete NPI and Marked</u> ERROR.
- <u>Example 4—Delete NPI and Marked</u> VALID.
- <u>Example 5—Replace NPI and Marked</u> VALID.
- <u>Example 6—Adding Exemption for Requiring</u> an NPI.
- <u>Example 7—Removing Exemption for Requiring</u> an NPI.
- <u>Example 8—Generating a Test NPI</u> Value.
- <u>Example 9—Reactivating an NPI Value</u>.

#### Example 1—Successfully Entering NPI Value for a Provider Who Requires an NPI

As shown in <u>Figure 76</u>, you can enter an NPI value for a provider that requires an NPI:

<span id="_Ref174351640" class="anchor"></span>Figure 76: Using the Add/Edit NPI values for Providers Option—Successfully Entering NPI Value for a Provider Who Requires an NPI

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">PROVIDER,NEW</span><span class="mark">\<Enter\></span> NP 111 PHYSICIAN

Provider: PROVIDER,NEW XXX-XX-XXXX DOB: \*\*/\*\*/\*\*\*\*

Enter NPI (10 digits): <span class="mark">1639467649 \<Enter\></span>

Please re-enter NPI : <span class="mark">1639467649 \<Enter\></span>

For provider PROVIDER,NEW (who requires an NPI), the NPI 1639467649

was saved to VistA successfully.

In this example (<u>Figure 76</u>). the PROVIDER,NEW provider required an NPI, so the NPI value entered (such as 1639467649) was successfully saved to that provider in VistA.

#### Example 2—Verifying an NPI Value is Already Associated with a Provider

As shown in <u>Figure 77</u>, you can enter an NPI value for a provider that is now or was in the past associated with an NPI:

<span id="_Ref174352093" class="anchor"></span>Figure 77: Using the Add/Edit NPI values for Providers Option—Verifying an NPI Value is Already Associated with a Provider

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">PROVIDER,NPI \<Enter\></span> MENTAL HEALTH & BEHAVIORAL SC. PSYCHOLOGIST

Provider: PROVIDER,NPI XXX-XX-\*\*\* DOB: \*\*\*

Enter NPI (10 digits): <span class="mark">1841506847 \<Enter\></span>

The NPI of 1841506847 is now, or was in the past, associated with

PROVIDER,NPI in the NEW PERSON file.

As you can see in this example (<u>Figure 77</u>), the NPI value entered (such as 1841506847) for the PROVIDER,NPI is now, or was in the past, associated with that same provider in the NEW PERSON (#200) file.

This could indicate:

- Inactive NPI.

![](kernel-8-0-systems-management-utilities-user-guide/076.png) REF: To reactivate an NPI, see Section <u>6.3.4.2.9</u>.

- There is an issue if the NPI is not displaying correctly on reports.

#### Example 3—Delete NPI and Marked ERROR

As shown in (<u>Figure 78</u>), you can delete an NPI value, because it was entered in error:

<span id="_Ref174358447" class="anchor"></span>Figure 78: Using the Add/Edit NPI values for Providers Option—Delete NPI and Marked ERROR

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">PROVIDER,ONE \<Enter\></span> OP NURSE PRACTIONER

This provider already has an NPI value (9876543213) entered.

Select one of the following:

<span class="mark">D</span> <span class="mark">Delete</span>

R Replace

Do you want to (D)elete or (R)eplace this NPI value?: <span class="mark">DELETE \<Enter\></span>

Select one of the following:

V VALID

<span class="mark">E</span> <span class="mark">ERROR</span>

Was the original NPI (V)alid for this provider

or was it entered in (E)rror?: <span class="mark">ERROR \<Enter\></span>

Provider: PROVIDER,ONE XXX-XX-XXXX DOB: \*\*/\*\*/\*\*\*\*

Confirm that you want to \*\*DELETE\*\* this incorrectly entered NPI? NO// <span class="mark">YES \<Enter\></span>

Entry was DELETED...

As you can see in this example (<u>Figure 78</u>), the user deleted an NPI value entered in error. If you delete an NPI value that was entered in error, that deleted NPI value can be re-used in the future.

#### Example 4—Delete NPI and Marked VALID

As shown in <u>Figure 79</u>, you can delete an NPI value, even though it was a valid entry:

<span id="_Ref174358523" class="anchor"></span>Figure 79: Using the Add/Edit NPI values for Providers Option—Delete NPI and Marked VALID

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">NPIUSER, ONE \<Enter\></span> NPIUSER,ONE PINELLAS PARK FLORIDA

ON

This provider already has an NPI value (<span class="mark">1234567893</span>) entered.

Select one of the following:

<span class="mark">D Delete</span>

R Replace

Do you want to (D)elete or (R)eplace this NPI value?: <span class="mark">DELETE \<Enter\></span>

Select one of the following:

<span class="mark">V VALID</span>

E ERROR

Was the original NPI (V)alid for this provider

or was it entered in (E)rror?: <span class="mark">VALID \<Enter\></span>

<span class="mark">Entry has been marked inactive.</span>

Select Provider:

As you can see in this example (<u>Figure 79</u>), the user deleted a valid NPI value (such as 1234567893). If you delete a valid NPI value, that deleted NPI value is now invalidated and *cannot* be re-used in the future.

#### Example 5—Replace NPI and Marked VALID

As shown in <u>Figure 80</u>, you can replace an NPI value, even though it was a valid entry:

<span id="_Ref174358728" class="anchor"></span>Figure 80: Using the Add/Edit NPI values for Providers Option—Replace NPI and Marked VALID

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">NPIUSER, FIVE \<Enter\></span> NPIUSER,FIVE PINELLAS PARK FLORIDA

FN

This provider already has an NPI value (1234567893) entered.

Select one of the following:

D Delete

<span class="mark">R Replace</span>

Do you want to (D)elete or (R)eplace this NPI value?: <span class="mark">REPLACE \<Enter\></span>

Enter NPI (10 digits): <span class="mark">9876543213 \<Enter\></span>

Please re-enter NPI : <span class="mark">9876543213 \<Enter\></span>

For provider NPIUSER,FIVE the NPI 9876543213

was saved to VistA successfully.

As you can see in this example (<u>Figure 80</u>), the user replaced a valid NPI value (such as 1234567893) to another valid NPI value (such as 9876543213). If you replace a valid NPI value, that replaced NPI value (such as 1234567893) is now invalidated and *cannot* be re-used in the future.

#### Example 6—Adding Exemption for Requiring an NPI

As shown in <u>Figure 81</u>, you can add an exemption to a provider, so they do not require an NPI value:

<span id="_Ref174367092" class="anchor"></span>Figure 81: Using the Add/Edit NPI values for Providers Option—Adding Exemption for Requiring an NPI

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">PROVIDER,TWO \<Enter\></span> ...

Confirm that Provider should be Exempt from needing an NPI (Y/N)? <span class="mark">YES \<Enter\></span>

File updated

As you can see in this example (<u>Figure 81</u>), the user added an exemption to this provider, so they do not require an NPI value.

#### Example 7—Removing Exemption for Requiring an NPI

As shown in <u>Figure 82</u>, you can remove an exemption from a provider, so they require an NPI value:

<span id="_Ref174367135" class="anchor"></span>Figure 82: Using the Add/Edit NPI values for Providers Option—Removing Exemption for Requiring an NPI

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">PROVIDER,THREE \<Enter\></span> ...

Provider is currently EXEMPT from needing an NPI, set to NEEDS an NPI (Y/N)? <span class="mark">YES \<Enter\></span>

File updated

As you can see in this example (<u>Figure 82</u>), the user removed an exemption for this provider, so they now require an NPI value.

#### Example 8—Generating a Test NPI Value

As shown in <u>Figure 83</u>, you can generate a test NPI value to help you troubleshoot any NPI-related issues:

<span id="_Ref174351136" class="anchor"></span>Figure 83: Using the Add/Edit NPI values for Providers Option—Generating a Test NPI Value

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">CODER,TWO \<Enter\></span> TC

This user doesn't have a Taxonomy Code indicating a need for an NPI.

Need for an NPI value isn't indicated - but you can enter an NPI

Provider: CODER,TWO XXX-XX-9890 DOB:

Enter NPI (10 digits): <span class="mark">aaaaaaaaaaaaa \<Enter\></span>

Enter a 10 digit National Provider Identifier which is obtained

from 'https://nppes.cms.hhs.gov/NPPES'

Do you want to generate a test NPI value? <span class="mark">YES \<Enter\></span>

Enter a nine (9) digit number as the base: <span class="mark">987654321 \<Enter\></span>

The complete NPI value is: <span class="mark">9876543213</span>

Enter NPI (10 digits): <span class="mark">9876543213 \<Enter\></span>

Please re-enter NPI  : <span class="mark">9876543213 \<Enter\></span>

 

For provider CODER,TWO (who requires an NPI), the NPI 9876543213  
was saved to VistA successfully.

In this example (<u>Figure 83</u>), 1234567893 (or 9876543213) are mock-up NPI numbers used to troubleshoot NPI-related issues. They are *not* real NPI numbers for providers, so they would *not* match with any existing NPI numbers.

![](kernel-8-0-systems-management-utilities-user-guide/077.png) NOTE: The Taxonomy Code (aka X12 CODE) is stored in the PERSON CLASS (#200,8932.1) Multiple field in the NEW PERSON (#200) file, which is a pointer to the PERSON CLASS (#8932.1) file.

#### Example 9—Reactivating an NPI Value

To reactivate an NPI value, do the following (<u>Figure 84</u>):

1.  Use the Add/Edit NPI values for Providers \[XUS NPI ENTER NPI FOR PROVIDER\] option to add a “dummy” NPI (1234567893 or 9876543213) to the user.
29. Use the Add/Edit NPI values for Providers \[XUS NPI ENTER NPI FOR PROVIDER\] option to Delete as Error.

<span id="_Ref192501710" class="anchor"></span>Figure 84: Reactivating an NPI Value—Sample System Prompts and User Entries

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">XUUSER,ONE \<Enter\></span> PINELLAS PARK     FLORIDA     BT       

Enter NPI (10 digits): <span class="mark">1234567893 \<Enter\></span>

Please re-enter NPI  : <span class="mark">1234567893 \<Enter\></span>

For provider XUUSER,ONE (who requires an NPI), the NPI 1234567893

was saved to VistA successfully.

<span class="mark">Add/Edit NPI values for Providers</span>

Mark/Unmark Provider Exempt from requiring an NPI

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">ADD \<Enter\></span> /Edit NPI values for Providers

Select Provider: <span class="mark">XUUSER,ONE \<Enter\></span> PINELLAS PARK     FLORIDA     BT       

This provider already has an NPI value (1234567893) entered.

     Select one of the following:

          <span class="mark">D         Delete</span>

          R         Replace

Do you want to (D)elete or (R)eplace this NPI value?: <span class="mark">D \<Enter\></span> Delete

     Select one of the following:

          V         VALID

          <span class="mark">E         ERROR</span>

Was the original NPI (V)alid for this provider

or was it entered in (E)rror?: <span class="mark">E \<Enter\></span> ERROR

Confirm that you want to \*\*DELETE\*\* this incorrectly entered NPI? NO// <span class="mark">Y \<Enter\></span> YES

Entry was DELETED...

> **NOTE:** the previous NPI will be reactivated.

#### Mark/Unmark Provider Exempt from requiring an NPI Option

Support staff use the Mark/Unmark Provider Exempt from requiring an NPI \[XUS NPI EXEMPT PROVIDER\] option to indicate that a provider who has a Person Class entry relating to a taxonomy value that would normally require and NPI value, as not needing one (such as if the provider were doing administrative work full time).

![](kernel-8-0-systems-management-utilities-user-guide/078.png) NOTE: The CLERXMPT^XUSNPIED routine runs this option.

<span id="_Toc192501607" class="anchor"></span>Figure 85: Mark/Unmark Provider Exempt from requiring an NPI Option—Sample System Prompts and User Entries

Add/Edit NPI values for Providers

<span class="mark">Mark/Unmark Provider Exempt from requiring an NPI</span>

Print Local NPI Reports

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">MARK \<Enter\></span> /Unmark Provider Exempt from requiring an NPI

Select Provider: <span class="mark">XUPROVIDER \<Enter\></span> XUPROVIDER,ONE OX

This Provider does not appear to need an NPI or Exemption.

#### Print Local NPI Reports Option

The Print Local NPI Reports \[XUS NPI LOCAL REPORTS\] option generates reports for the local facility on those who are expected to have NPI values entered.

![](kernel-8-0-systems-management-utilities-user-guide/079.png) NOTE: The PRINTOPT^XUSNPIED routine runs this option.

<span id="_Toc192501608" class="anchor"></span>Figure 86: Print Local NPI Reports Option—Sample System Prompts and User Entries

Add/Edit NPI values for Providers

Mark/Unmark Provider Exempt from requiring an NPI

<span class="mark">Print Local NPI Reports</span>

Select NPI (National Provider ID) Menu \<TEST ACCOUNT\> Option: <span class="mark">PRINT \<Enter\></span> Local NPI Reports

Select one of the following:

<span class="mark">1 All providers</span>

2 All providers without NPI numbers

Select a report option: (1-2): 1// <span class="mark">1 \<Enter\></span>

Select one of the following:

P Providers who are not residents

R Residents only

<span class="mark">B Both</span>

Selection: : P// <span class="mark">B \<Enter\></span> oth

Select one of the following:

1 ACTIVE users only

<span class="mark">2 ACTIVE and DISUSERed users</span>

Select a report option: (1-2): 1// <span class="mark">2 \<Enter\></span>

Sort by DIVISION? NO// <span class="mark">\<Enter\></span>

Sort by SERVICE/SECTION? YES// <span class="mark">\<Enter\></span>

\>\>\> Report processing time is approximately 10 minutes.

Recommend text output be queued to a network printer.

DEVICE: HOME// <span class="mark">;;999999999 \<Enter\></span> TELNET PORT Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">Active Provider Report (includes residents) May 03, 2024@14:12 Page: 1</span>

Report Option: Provider List Active and Disuser Providers

Provider Name IEN NPI Disuser

Taxonomy

--------------------------------------------------------------------------------

SERVICE/SECTION:

RADIOLOGY,OUTSIDE SERVICE 10000000179

2085R0202X Radiology

Type \<Enter\> to continue or '^' to exit:

<span class="mark">Active Provider Report (includes residents) May 03, 2024@14:12 Page: 2</span>

Report Option: Provider List Active and Disuser Providers

Provider Name IEN NPI Disuser

Taxonomy

--------------------------------------------------------------------------------

SERVICE/SECTION: INFORMATION SYSTEMS CENTER

GARCIA,JOSE L 76

364SX0204X Clinical Nurse Specialist

PROVIDER,PRF 11597

133V00000X Dietitian, Registered

THIPPISETTY,VENKATA 1077 9876543213

TRAN,BAA 82 1234567893

183500000X Pharmacist

WARDCLERK,SEVENTYSEVEN 11289

363A00000X Physician Assistant

WARDCLERK,SIXTYTHREE 11273

363A00000X Physician Assistant

Type \<Enter\> to continue or '^' to exit:

<span class="mark">Active Provider Report (includes residents) May 03, 2024@14:12 Page: 3</span>

Report Option: Provider List Active and Disuser Providers

Provider Name IEN NPI Disuser

Taxonomy

--------------------------------------------------------------------------------

SERVICE/SECTION: LIBRARY

LU,ERIC 1111 9870654651

183500000X Pharmacist

Type \<Enter\> to continue or '^' to exit:

<span class="mark">Active Provider Report (includes residents) May 03, 2024@14:12 Page: 4</span>

Report Option: Provider List Active and Disuser Providers

Provider Name IEN NPI Disuser

Taxonomy

--------------------------------------------------------------------------------

SERVICE/SECTION: MEDICAL

PCMM-MD,ONE 10000000183

207R00000X Internal Medicine

PHYSICIAN,ASSISTANT 11820

363AM0700X Physician Assistant

Type \<Enter\> to continue or '^' to exit:

<span class="mark">Active Provider Report (includes residents) May 03, 2024@14:12 Page: 5</span>

Report Option: Provider List Active and Disuser Providers

Provider Name IEN NPI Disuser

Taxonomy

--------------------------------------------------------------------------------

SERVICE/SECTION: MEDICINE

PCMM-MD,FIVE 10000000187

207R00000X Internal Medicine

PCMM-MD,FOUR 10000000186

207R00000X Internal Medicine

PCMM-MD,THREE 10000000185

207R00000X Internal Medicine

PCMM-MD,TWO 10000000184

207R00000X Internal Medicine

PCMM-NP,FIVE 10000000192

363LP2300X Nurse Practitioner

PCMM-NP,FOUR 10000000191

363LP2300X Nurse Practitioner

PCMM-NP,ONE 10000000188

363LP2300X Nurse Practitioner

PCMM-NP,THREE 10000000190

363LP2300X Nurse Practitioner

PCMM-NP,TWO 10000000189

363LP2300X Nurse Practitioner

PCMM-PA,FIVE 10000000197

363AM0700X Physician Assistant

PCMM-PA,FOUR 10000000196

363AM0700X Physician Assistant

PCMM-PA,ONE 10000000193

363AM0700X Physician Assistant

PCMM-PA,THREE 10000000195

363AM0700X Physician Assistant

PCMM-PA,TWO 10000000194

363AM0700X Physician Assistant

PCMM-RESIDENT,FIVE 10000000202

390200000X Resident, Allopathic (includes Interns, Residents, Fellows)

PCMM-RESIDENT,FOUR 10000000201

390200000X Resident, Allopathic (includes Interns, Residents, Fellows)

PCMM-RESIDENT,ONE 10000000198

390200000X Resident, Allopathic (includes Interns, Residents, Fellows)

PCMM-RESIDENT,THREE 10000000200

390200000X Resident, Allopathic (includes Interns, Residents, Fellows)

PCMM-RESIDENT,TWO 10000000199

390200000X Resident, Allopathic (includes Interns, Residents, Fellows)

Type \<Enter\> to continue or '^' to exit:

<span class="mark">Active Provider Report (includes residents) May 03, 2024@14:12 Page: 6</span>

Report Option: Provider List Active and Disuser Providers

Provider Name IEN NPI Disuser

Taxonomy

--------------------------------------------------------------------------------

SERVICE/SECTION: PHARMACY

PHARMACIST,EIGHT 20122

183500000X Pharmacist

PHARMACIST,EIGHTEEN 20132

183500000X Pharmacist

PHARMACIST,ELEVEN 20125

183500000X Pharmacist

PHARMACIST,FIFTEEN 20129

183500000X Pharmacist

PHARMACIST,FIFTY 20164

183500000X Pharmacist

PHARMACIST,FIVE 20119

183500000X Pharmacist

PHARMACIST,FORTY 20154

183500000X Pharmacist

PHARMACIST,FORTY-EIGHT 20162

183500000X Pharmacist

PHARMACIST,FORTY-FIVE 20159

183500000X Pharmacist

PHARMACIST,FORTY-FOUR 20158

183500000X Pharmacist

PHARMACIST,FORTY-NINE 20163

183500000X Pharmacist

PHARMACIST,FORTY-ONE 20155

183500000X Pharmacist

PHARMACIST,FORTY-SEVEN 20161

183500000X Pharmacist

PHARMACIST,FORTY-SIX 20160

183500000X Pharmacist

PHARMACIST,FORTY-THREE 20157

183500000X Pharmacist

PHARMACIST,FORTY-TWO 20156

183500000X Pharmacist

PHARMACIST,FOUR 20118

183500000X Pharmacist

PHARMACIST,FOURTEEN 20128

183500000X Pharmacist

PHARMACIST,NINE 20123

183500000X Pharmacist

PHARMACIST,NINETEEN 20133

183500000X Pharmacist

PHARMACIST,ONE 10000000056

183500000X Pharmacist

PHARMACIST,SEVEN 20121

183500000X Pharmacist

PHARMACIST,SEVENTEEN 20131

183500000X Pharmacist

PHARMACIST,SIX 20120

183500000X Pharmacist

PHARMACIST,SIXTEEN 20130

183500000X Pharmacist

PHARMACIST,TEN 20124

183500000X Pharmacist

PHARMACIST,THIRTEEN 20127

183500000X Pharmacist

PHARMACIST,THIRTY 20144

183500000X Pharmacist

PHARMACIST,THIRTY-EIGHT 20152

183500000X Pharmacist

PHARMACIST,THIRTY-FIVE 20149

183500000X Pharmacist

PHARMACIST,THIRTY-FOUR 20148

183500000X Pharmacist

PHARMACIST,THIRTY-NINE 20153

183500000X Pharmacist

PHARMACIST,THIRTY-ONE 20145

183500000X Pharmacist

PHARMACIST,THIRTY-SEVEN 20151

183500000X Pharmacist

PHARMACIST,THIRTY-SIX 20150

183500000X Pharmacist

PHARMACIST,THIRTY-THREE 20147

183500000X Pharmacist

PHARMACIST,THIRTY-TWO 20146

183500000X Pharmacist

PHARMACIST,THREE 20117

183500000X Pharmacist

PHARMACIST,TWELVE 20126

183500000X Pharmacist

PHARMACIST,TWENTY 20134

183500000X Pharmacist

PHARMACIST,TWENTY-EIGHT 20142

183500000X Pharmacist

PHARMACIST,TWENTY-FIVE 20139

183500000X Pharmacist

PHARMACIST,TWENTY-FOUR 20138

183500000X Pharmacist

PHARMACIST,TWENTY-NINE 20143

183500000X Pharmacist

PHARMACIST,TWENTY-ONE 20135

183500000X Pharmacist

PHARMACIST,TWENTY-SEVEN 20141

183500000X Pharmacist

PHARMACIST,TWENTY-SIX 20140

183500000X Pharmacist

PHARMACIST,TWENTY-THREE 20137

183500000X Pharmacist

PHARMACIST,TWENTY-TWO 20136

183500000X Pharmacist

PHARMACIST,TWENTYONE 10000000070

183500000X Pharmacist

PHARMACIST,TWO 20116

183500000X Pharmacist

PHARMACY,ADPAC 10000000414

183500000X Pharmacist

RADTECH,SIXTYEIGHT 20113

183500000X Pharmacist

RADTECH,SIXTYFOUR 20108

183500000X Pharmacist

Total Billable Providers: 83

Billable Providers with an NPI: 3

EXEMPT Billable Providers: 0

Billable Providers Still Needing an NPI: 80

<span class="mark">\*\*\* End of Report \*\*\*</span>

### PROVIDER NPI SELF ENTRY Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PROVIDER NPI SELF ENTRY \[XUS NPI PROVIDER SELF ENTRY\] option allows a provider to enter their own NPI value. The system automatically sets the Effective Date to the Input Date. It is intended to be attached to the XU COMMON menu and checks whether the user selecting it has the need to enter an NPI value.

![](kernel-8-0-systems-management-utilities-user-guide/080.png) NOTE: The USEREDIT^XUSNPIED routine runs this option.

<span id="_Toc192501609" class="anchor"></span>Figure 87: Using the PROVIDER NPI SELF ENTRY Option—Sample System Prompts and User Entries

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">PROVIDER \<Enter\></span> NPI SELF ENTRY

Enter NPI (10 digits): <span class="mark">9876543213 \<Enter\></span>

Please re-enter NPI  : <span class="mark">9876543213 \<Enter\></span>

 

For provider XUUSER,ONE (who requires an NPI), the NPI 9876543213  
was saved to VistA successfully.

## NPI APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of NPI-related application programming interfaces (APIs):

- \$\$CHKDGT^XUSNPI(): Validate NPI Format
- \$\$NPI^XUSNPI(): Get NPI from Files \#200, \#4, or \#355.93
- \$\$QI^XUSNPI(): Get Provider Entities
- \$\$NPIUSED^XUSNPI1(): Returns an Error or Warning if an NPI is in Use
- \$\$TAXIND^XUSTAX(): Get Taxonomy Code from File \#200
- \$\$TAXORG^XUSTAX(): Get Taxonomy Code from File \#4

![](kernel-8-0-systems-management-utilities-user-guide/081.png) REF: For a description of these APIs, see the [*Kernel 8.0 Developer’s Guide: NPI Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_npi_ug.pdf).

## NPI RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of NPI-related remote procedure calls (RPCs):

### XUS MVI ENRICH NEW PERSON

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ICR: 1059

Tag^Routine: UPDATE^XUMVIENU

Input Parameters:

- PARAM("WHO")=Station Number of requesting station.
- PARAM("NPI")=National Provider Identifier.

Errors:

Returned, for example, if required data was not passed; entry could not be added when FLAG="A", or entry could not be found based on the NPI when FLAG="U".

## NPI Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUSNPIMTL security key allows users to access the NPI (National Provider ID) Menu \[XUS NPI MENU\] menu. This security key is normally assigned to the Local NPI Maintenance Team Leader; the person with authority to assign/edit VA Provider NPIs.

## NPI Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### XUSNPI QUALIFIED IDENTIFIER Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUSNPI QUALIFIED IDENTIFIER parameter is in the PARAMETER DEFINITION (#8989.51) file. This parameter is a mapping of NPI ID name to the files that hold the data.

# Service/Section Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*807 converted and enhanced the existing software for the Service/Section Edit menu option from Class II “R2XTAD” namespace to Class I Kernel “XUXTAD” namespace.

![](kernel-8-0-systems-management-utilities-user-guide/082.png) NOTE: Kernel Patch XU\*8.0\*807 addressed the issue described in ServiceNow (SNOW) ticket [SCTASK16043983](https://yourit.va.gov/nav_to.do?uri=sc_task.do?sys_id=07c771211bd0dad08c0a0f6fe54bcb52).

Kernel Patch XU\*8.0\*807 did the following:

- Added the Class I XUXTAD SERVICE/SECTION EDIT ScreenMan form.
- Added the Class I XUXTAD SERVICE/SECTION EDIT menu option:
- Allows editing of the Service/Section NAME field.
- Added and allows editing of the Service/Section DATE CLOSED and DATE RE-OPENED fields.
- Added a display only Service/Section Open/Closed Status field. This is a calculated field that determines the status of Service/Section.
- If the Class II R2XTAD SERVICE/SECTION EDIT option existed:

Set the field OUT OF ORDER="Replaced by SSE—Service/Section Edit".

- If the Class II R2XTAD USER INFO MENU option existed:
- Added MENU ITEM OPTION XUXTAD SERVICE/SECTION EDIT.
- Deleted MENU ITEM OPTION R2XTAD SERVICE/SECTION EDIT, if it exists.
- Updated the Data Dictionary Field-level attributes: HELP-PROMPT and DESCRIPTION for the SERVICE/SECTION (#49) file and NAME (#.01) field.
- Converted all required code associated with the R2XTAD SERVICE/SECTION EDIT menu option from Class II "R2XTAD" namespace to class I “XUXTAD” namespace.

## Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Information Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can access the User Information Menu \[R2XTAD USER INFO MENU\] as follows:

- From Programmer mode, at the ”Select OPTION NAME:” prompt, enter R2XTAD USER INFO MENU or User Information Menu (<u>Figure 88</u>).
- From the Systems Manager Menu \[EVE\] menu, at the “Select Systems Manager Menu \<TEST ACCOUNT\> Option:” prompt, by entering the synonym R2XU (<u>Figure 89</u>).

<span id="_Ref188968195" class="anchor"></span>Figure 88: Programmer Mode Menu Prompt

\><span class="mark">D ^XUP \<Enter\></span>

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT320

Select OPTION NAME: <span class="mark">R2XTAD USER INFO MENU \<Enter\></span> User Information Menu

User Inquiry

          User information for ePAS/NARS requests

          Switch Identities

   SSE    Service/Section Edit

          Person Class Information ...

          Clear User Account ...

          New Person/User Report

          Option Access By User

Select User Information Menu \<TEST ACCOUNT\> Option:

<span id="_Ref188968201" class="anchor"></span>Figure 89: EVE Menu: R2XU—User Information Menu

Core Applications ...

Device Management ...

FM VA FileMan ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

<span class="mark">R2XU User Information Menu ...</span>

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option:

### Service/Section Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can access the Service/Section Edit \[XUXTAD SERVICE/SECTION EDIT\] option as follows:

- From Programmer mode, at the ”Select OPTION NAME:” prompt, enter “XUXTAD SERVICE/SECTION EDIT” or “Service/Section Edit”.
- From the User Information Menu \[R2XTAD USER INFO MENU\] menu, at the “Select User Information Menu \<TEST ACCOUNT\> Option:”, entering the SSE synonym (<u>Figure 90</u>).

<span id="_Ref188969416" class="anchor"></span>Figure 90: R2XTAD USER INFO MENU: SSE—Service/Section Edit Option

User Inquiry

User information for ePAS/NARS requests

Switch Identities

<span class="mark">SSE Service/Section Edit</span>

Person Class Information ...

Clear User Account ...

New Person/User Report

Option Access By User

Select User Information Menu \<TEST ACCOUNT\> Option: <span class="mark">SSE \<Enter\></span>

The Service/Section Edit \[XUXTAD SERVICE/SECTION EDIT\] option allows the user to edit fields of a Service/Section record via ScreenMan, as shown in <u>Figure 91</u>. A Service/Section can be either “Open” or “Closed” and is shown in the Status field of the header section as highlighted in <u>Figure 91</u>.

<span id="_Ref188601969" class="anchor"></span>Figure 91: Service Section Edit—ScreenMan Form

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SS1 <span class="mark">Status: Open</span> PAGE 1 OF 1

----------------------------------------------------------------------------------

NAME: TEST SS1

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: RE-OPEN SERVICE SECTION:

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

DESCRIPTION (WP): +

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Service/Section TEST SS1 has no users assigned and can be Closed

Press \<PF1\>H for help Insert

## SERVICE/SECTION (#49) File Editable Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> lists a few SERVICE/SECTION (#49) file field values that you can edit with the Service/Section Edit option:

| Field                                                                                      | Description                                                                                                                                                  |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="NAME_Field" class="anchor"></span>NAME                                       | Edit the Service or Section name.<sup>\*</sup>                                                                                                               |
| ABBREVIATION                                                                           | Enter an accepted abbreviation for the Service or Section.                                                                                                   |
| MAIL SYMBOL                                                                            | Enter an accepted mail routing symbol for the Service or Section.                                                                                            |
| TYPE OF SERVICE                                                                        | Enter the type of Service or Section. Services or sub-services can be marked as Administrative or for Patient Care.                                  |
| CHIEF (or SUPERVISOR)                                                                  | Enter the name of the chief of this Service or Section.                                                                                                      |
| PARENT SERVICE                                                                         | Enter the name of the Service or Section that is “parent” to this Section.                                                                                   |
| NATIONAL SERVICE                                                                       | Enter the NATIONAL SERVICE (#730) file used to link the locally built SERVICE/SECTION (#49) file to the standardized list of nationally recognized services. |
| <span id="CLOSE_SERVICE_SECTION_Field" class="anchor"></span>CLOSE SERVICE SECTION     | Enter the DATE/TIME when this Service or Section is closed for hospital use.<sup>\*\*</sup>                                                          |
| <span id="RE_OPEN_SERVICE_SECTION_Field" class="anchor"></span>RE-OPEN SERVICE SECTION | Enter the DATE/TIME when this closed Service or Section was reopened for hospital use.<sup>\*\*</sup>                                                |
| <span id="DESCRIPTION_Field" class="anchor"></span>DESCRIPTION                         | Enter the changes that you are making to this Service or Section (e.g., Date, your name, and your changes).                                                  |

<sup>\*</sup>Service or Section name *cannot* be deleted by deleting all the characters or by using an at-sign (“@”).

<sup>\*\*</sup>You *cannot* edit the CLOSE SERVICE SECTION or RE-OPEN SERVICE SECTION fields if there are users assigned to the Service or Section.

### Service/Section Edit—Edit NAME Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit the [NAME](#NAME_Field) field in the “SERVICE/SECTION EDIT” screen, do the following:

1.  Use the Arrow keys to position the cursor at the NAME field.
30. Apply edits to the NAME field (<u>Figure 92</u>).

> <span id="_Ref188969814" class="anchor"></span>Figure 92: “Service Section Edit” ScreenMan Form—Edit NAME Field

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SS1 Status: Open PAGE 1 OF 1

----------------------------------------------------------------------------

<span class="mark">NAME:</span> TEST <span class="mark">SERVICE SECTION 2</span>

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: RE-OPEN SERVICE SECTION:

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

DESCRIPTION (WP): +

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

In this example (<u>Figure 92</u>), the user changed the NAME field from “TEST SS1” to “TEST SERVICE SECTION 2”.

31. Use the \<Down Arrow\> or \<Tab\> keys to position the cursor on the [DESCRIPTION (WP)](#DESCRIPTION_Field) field to document your changes (<u>Figure 93</u>). Press \<Enter\> to open the Edit Description WP Field screen (<u>Figure 94</u>).

> <span id="_Ref188971005" class="anchor"></span>Figure 93: “Service Section Edit” ScreenMan Form—Navigate to the DESCRIPTION (WP) Field

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SS1 Status: Open PAGE 1 OF 1

----------------------------------------------------------------------------

NAME: <span class="mark">TEST SERVICE SECTION 2</span>

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: RE-OPEN SERVICE SECTION:

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

<span class="mark">DESCRIPTION (WP):</span> <span class="mark">\<Enter\></span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

32. In the Edit Description WP Field screen (<u>Figure 94</u>):
1.  Type the following edits in the order shown:
- Date: YYYY/MM/DD
- Your Name
- Change that was made.

![](kernel-8-0-systems-management-utilities-user-guide/083.png) NOTE: Do not type over any existing description entries; make your new entry either above or below the existing entries.

4.  Press \<PF1\>E to Save and Exit the Edit Description WP Field screen.

> <span id="_Ref188970993" class="anchor"></span>Figure 94: “Service Section Edit” ScreenMan Form—Edit DESCRIPTION (WP) Field

==\[ WRAP \]==\[INSERT \]========\< DESCRIPTION \>===\[Press \<PF1\>H for help\]====

<span class="mark">2024/01/28 *\<Your Name\>* Modified Name field from TEST SS1 to TEST SERVICE SECTION 2</span>

==\[ WRAP \]==\[INSERT \]========\< DESCRIPTION \>===\[Press \<PF1\>H for help\]====

33. Press \<PF1\>E to Save and Exit the form (<u>Figure 95</u>).

> <span id="_Ref188971224" class="anchor"></span>Figure 95: “Service Section Edit” ScreenMan Form—Save and Exit Form

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SS1 Status: Open PAGE 1 OF 1

----------------------------------------------------------------------------

NAME: <span class="mark">TEST SERVICE SECTION 2</span>

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: RE-OPEN SERVICE SECTION:

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

DESCRIPTION (WP): +

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span class="mark">Service/Section edits saved</span>

Type \<Enter\> to continue or '^' to exit: <span class="mark">\<Enter\></span>

### Service/Section Edit—Edit CLOSE SERVICE SECTION Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit the [CLOSE SERVICE SECTION](#CLOSE_SERVICE_SECTION_Field) field in the “SERVICE/SECTION EDIT” screen, do the following:

1.  Use the Arrow keys to position the cursor at the CLOSE SERVICE SECTION field.
2.  Type “Y” and press \<Enter\> (<u>Figure 96</u>).

> <span id="_Ref188974542" class="anchor"></span>Figure 96: “Service Section Edit” ScreenMan Form—Edit CLOSE SERVICE SECTION Field

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SERVICE SECTION 2 Status: <span class="mark">Open</span> PAGE 1 OF 1

----------------------------------------------------------------------------

NAME: TEST SERVICE SECTION 2

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

<span class="mark">CLOSE SERVICE SECTION:</span> <span class="mark">Y</span> RE-OPEN SERVICE SECTION:

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

DESCRIPTION (WP): +

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span class="mark">Service/Section will be Closed on Save or Exit</span>

Press \<PF1\>H for help Insert

3.  Use the \<Down Arrow\> or \<Tab\> keys to position the cursor on the [DESCRIPTION (WP)](#DESCRIPTION_Field) field to document your changes (<u>Figure 97</u>). Press \<Enter\> to open the Edit Description (WP) Field screen (<u>Figure 98</u>).

> <span id="_Ref188974693" class="anchor"></span>Figure 97: “Service Section Edit” ScreenMan Form—Navigate to the DESCRIPTION (WP) Field

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SERVICE SECTION 2 Status: <span class="mark">Open</span> PAGE 1 OF 1

----------------------------------------------------------------------------

NAME: TEST SERVICE SECTION 2

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: <span class="mark">Y</span> RE-OPEN SERVICE SECTION:

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

<span class="mark">DESCRIPTION (WP):</span> <span class="mark">\<Enter\></span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press \<PF1\>H for help Insert

4.  In the Edit Description (WP) Field screen (<u>Figure 98</u>):
1.  Type the following edits in the order shown:
- Date: YYYY/MM/DD
- Your Name
- Change that was made.

![](kernel-8-0-systems-management-utilities-user-guide/084.png) NOTE: Do not type over any existing description entries; make your new entry either above or below the existing entries.

5.  Press \<PF1\>E to Save and Exit the Edit Description (WP) Field screen.

> <span id="_Ref188974700" class="anchor"></span>Figure 98: “Service Section Edit” ScreenMan Form—Edit DESCRIPTION (WP) Field

==\[ WRAP \]==\[INSERT \]========\< DESCRIPTION \>===\[Press \<PF1\>H for help\]====

2024/01/28 *\<Your Name\>* Modified Name field from TEST SS1 to TEST SERVICE SECTION 2

<span class="mark">2024/01/28 *\<Your Name\>* Closed Service Section</span>

==\[ WRAP \]==\[INSERT \]========\< DESCRIPTION \>===\[Press \<PF1\>H for help\]====

5.  Press \<PF1\>E to Save and Exit the form (<u>Figure 99</u>).

> <span id="_Ref188975575" class="anchor"></span>Figure 99: “Service Section Edit” ScreenMan Form—Save and Exit Form

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SERVICE SECTION 2 Status: <span class="mark">Closed</span> PAGE 1 OF 1

----------------------------------------------------------------------------

NAME: TEST SERVICE SECTION 2

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: RE-OPEN SERVICE SECTION:

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

DESCRIPTION (WP): +

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span class="mark">Service/Section Closed</span>

Type \<Enter\> to continue or '^' to exit: <span class="mark">\<Enter\></span>

### Service/Section—Edit RE-OPEN SERVICE SECTION Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit the [RE-OPEN SERVICE SECTION](#RE_OPEN_SERVICE_SECTION_Field) field in the “SERVICE/SECTION EDIT” screen, do the following:

1.  Use the Arrow keys to position the cursor at the RE-OPEN SERVICE SECTION field.
34. Type “Y” and press \<Enter\> (<u>Figure 100</u>).

> <span id="_Ref188981044" class="anchor"></span>Figure 100: “Service Section Edit” ScreenMan Form—Edit RE-OPEN SERVICE SECTION Field

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SERVICE SECTION 2 Status: <span class="mark">Closed</span> PAGE 1 OF 1

----------------------------------------------------------------------------

NAME: TEST SERVICE SECTION 2

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: <span class="mark">RE-OPEN SERVICE SECTION</span>: <span class="mark">Y \<Enter\></span>

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

DESCRIPTION (WP): +

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span class="mark">Service/Section will be Re-opened on Save or Exit</span>

Type \<Enter\> to continue or '^' to exit: <span class="mark">\<Enter\></span>

35. Use the \<Down Arrow\> or \<Tab\> keys to position the cursor on the [DESCRIPTION (WP)](#DESCRIPTION_Field) field to document your changes (<u>Figure 101</u>). Press \<Enter\> to open the Edit Description (WP) Field screen (<u>Figure 102</u>).

> <span id="_Ref188981485" class="anchor"></span>Figure 101: “Service Section Edit” ScreenMan Form—Navigate to the DESCRIPTION (WP) Field

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SERVICE SECTION 2 Status: <span class="mark">Closed</span> PAGE 1 OF 1

----------------------------------------------------------------------------

NAME: TEST SERVICE SECTION 2

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: Y RE-OPEN SERVICE SECTION: <span class="mark">Y</span>

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

<span class="mark">DESCRIPTION (WP):</span> <span class="mark">\<Enter\></span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press \<PF1\>H for help Insert

36. In the Edit Description (WP) Field screen (<u>Figure 102</u>):
1.  Type the following edits in the order shown:
- Date: YYYY/MM/DD
- Your Name
- Change that was made.

![](kernel-8-0-systems-management-utilities-user-guide/085.png) NOTE: Do not type over any existing description entries; make your new entry either above or below the existing entries.

6.  Press \<PF1\>E to Save and Exit the Edit Description (WP) Field screen.

> <span id="_Ref188980938" class="anchor"></span>Figure 102: “Service Section Edit” ScreenMan Form—Edit DESCRIPTION (WP) Field

==\[ WRAP \]==\[INSERT \]========\< DESCRIPTION \>===\[Press \<PF1\>H for help\]====

2024/01/28 Name Modified Name field from TEST SS1 to TEST SERVICE SECTION 2

2024/01/28 Name Closed Service Section

<span class="mark">2024/01/28 Name Re-opened Service Section</span>

==\[ WRAP \]==\[INSERT \]========\< DESCRIPTION \>===\[Press \<PF1\>H for help\]====

37. Press \<PF1\>E to Save and Exit the form (<u>Figure 103</u>).

> <span id="_Ref188980688" class="anchor"></span>Figure 103: “Service Section Edit” ScreenMan Form—Save and Exit Form

SERVICE/SECTION EDIT (for ADPACs)

NAME: TEST SERVICE SECTION 2 Status: <span class="mark">Open</span> PAGE 1 OF 1

----------------------------------------------------------------------------

NAME: TEST SERVICE SECTION 2

ABBREVIATION:

MAIL SYMBOL: MS1

TYPE OF SERVICE:

CHIEF (or SUPERVISOR): LAST NAME,FIRST NAME

PARENT SERVICE:

NATIONAL SERVICE:

CLOSE SERVICE SECTION: RE-OPEN SERVICE SECTION: Y

\*\*\* Please enter a date, your name, and document your changes clearly \*\*\*

\*\*\* after hitting \<Enter\> at the DESCRIPTION field below. \*\*\*

DESCRIPTION (WP): +

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span class="mark">Close Service/Section cancelled, Service/Section is Re-opened</span>

Type \<Enter\> to continue or '^' to exit: <span class="mark">\<Enter\></span>

When closing a Service/Section, if today's date is equal to the last Re-Open Service/Section date then the following message is displayed:

"Close Service/Section cancelled, Service/Section is Re-opened"

Otherwise, the following message is displayed:

"Service/Section Closed"

When opening a Service/Section, if today's date is equal to the last Close Service/Section date the following message is displayed:

"Re-open Service/Section is cancelled, Service/Section is closed"

Otherwise, the following message is displayed:

"Service/Section Re-opened"

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-systems-management-utilities-user-guide/086.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
|      |          |             |        |

<span id="_Toc204765471" class="anchor"></span>Glossary

![](kernel-8-0-systems-management-utilities-user-guide/087.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-systems-management-utilities-user-guide/088.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.