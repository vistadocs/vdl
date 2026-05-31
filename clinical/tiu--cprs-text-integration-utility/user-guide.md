---
title: Additional Signer Utility Guide (TIU*1.0*357)
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: null
app_code: TIU
app_name: 'CPRS: Text Integration Utility'
section: CLI
app_status: active
pkg_ns: TIU
patch_ver: 1.0
patch_id: TIU*1.0
group_key: TIU:TIU:1.0
file_numbers:
- '8925.7'
security_keys:
- PROVIDER
menu_options: 0
description: Additional Signer is a communication tool used to alert a clinician about information pertaining to the patient. This functionality is designed to allow clinicians to call attention to specific documents and the recipient to acknowledge receipt of the information. Being identified as an additional s
audience: End users and package coordinators (ADPAC)
keywords: []
page_count: 0
word_count: 1880
section_count: 6
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: December 2023
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiu_util.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiu_util.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=65
audit_applied: '2026-05-31'
master_source: Additional Signer Utility Guide (TIU*1.0*357)
master_pub_date: December 2023
consolidated_from: 2 versions
prior_versions:
- TIU*1*254 Additional Signer Utility Guide
consolidated_title: additional signer utility guide
---

![](additional-signer-utility-guide-tiu-1-0-357/001.png)

December 2023

Office of Information and Technology (OI&T)

Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/2023</td>
<td>01</td>
<td><p>Patch TIU*1.0*357</p>
<p>Updated the Additional Signer Utility to version 2.0</p></td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>6/2022</td>
<td>0.01</td>
<td>Additional Signer Utility Guide – Initial version</td>
<td>Department of Veterans Affairs</td>
</tr>
</tbody>
</table>

Table of Contents

# TIU Additional Signer Utility


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [TIU Additional Signer Utility](#tiu-additional-signer-utility)
  - [Introduction](#introduction)
  - [Version 2.0](#version-20)
  - [General Information](#general-information)
  - [Options](#options)
    - [GENERATE a Report](#generate-a-report)
    - [REMOVE Additional Signer(s)](#remove-additional-signers)
    - [BOTH \[Generate a Report & Remove Additional Signer(s)\]](#both-generate-a-report-remove-additional-signers)
    - [VIEW the Report](#view-the-report)
    - [Importing into Excel](#importing-into-excel)
  - [Terminal Settings – Logging and Terminal Display](#terminal-settings-logging-and-terminal-display)
Text Integration Utilities (TIU) is a set of software tools designed to handle clinical documents in a standardized manner, with a single interface for viewing, entering, editing, and signing clinical documents.
This document describes how to use the Additional Signer Utility.

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional Signer is a communication tool used to alert a clinician about information pertaining to the patient. This functionality is designed to allow clinicians to call attention to specific documents and the recipient to acknowledge receipt of the information. Being identified as an additional signer does not constitute a co-signature. This nomenclature in no way implies responsibility for the content of, or concurrence with the note.

## Version 2.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 2.0 is released with patch TIU\*1.0\*357. Additional Signer reports created with version 1.0 of the utility are not compatible with version 2.0 and must be removed before the new version may be used. If you would like to save any old reports, you must view them and save them to a host file or screen capture them with logging BEFORE installing TIU\*1.0\*357.

At the prompt, "Remove the old reports now? NO//", you must enter YES to continue.

\*\* WARNING \*\*

Reports generated with v1 are NOT compatible and must be removed before use.

Additional Signer data in TIU MULTIPLE SIGNATURE \[File \#8925.7\] will not be

altered.

This process may take a few minutes and only needs to be completed once.

Remove the old reports now? NO// YES

Removing entries in ^XTMP...done.

Press \<Enter\> to continue.

> **NOTE:** If there are no outstanding additional signatures or reports to view, the utility will display that information before exiting.

No outstanding signatures or reports to view.

The utility's menu is dynamically generated based on the following criteria:

> Outstanding Additional Signatures.

> Additional Signature report(s) available to view.

If there are outstanding signatures but no reports to view, the default behavior is GENERATE and the menu will display the following:

<u>Additional Signer Utility</u>

1 GENERATE a Report

2 REMOVE Additional Signer(s)

3 BOTH \[Generate a Report & Remove Additional Signer(s)\]

4 QUIT

What would you like to do? GENERATE//

If there are outstanding signatures and reports to view, the default behavior is GENERATE and the menu will display the following:

Additional Signer Utility

1 GENERATE a Report

2 REMOVE Additional Signer(s)

3 BOTH \[Generate a Report & Remove Additional Signer(s)\]

4 VIEW Generated Report(s)

5 QUIT

What would you like to do? GENERATE//

If there are no outstanding signatures and one or more reports to view, the default behavior is VIEW and the menu will display the following:

1 VIEW Generated Report(s)

2 QUIT

What would you like to do? VIEW//

## General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional Signer data is stored in the TIU MULTIPLE SIGNATURE File (#8925.7). For additional signers, this file maintains data on the following fields:

- TIU Document Number
- Additional Signer IEN
- Signature Date/Time
- Signature Block Name & Title
- Signature Mode
- Signed by Surrogate

> **IMPORTANT:** TIU does not track who assigns an additional signer to a document or when the additional signer was added. Typically, an expected signer or co-signer would be the user who assigns additional signers. However, any user in the appropriate user class permitted by business rules may assign additional signers to a document. There is also no tracking of a removed additional signer other than the reports generated by this utility.

The Additional Signer Utility allows a user to perform the following actions on the TIU MULTIPLE SIGNATURE File (#8925.7):

- Generate a report of outstanding additional signatures for a date range or a specific user.
- Remove outstanding additional signers for a date range or a specific user.
- Both actions above simultaneously.
- View a report and output to a user entered device.

Reports are generated via a task and the user will receive an email when the task has been completed and the report is ready.

The email message contains the following information:

- Mode report was generated
- Total number of outstanding signatures
- Date range or Additional Signer
- Elapsed time to gather report data

> **NOTE:** VIEW the Report will be available only after one or more reports have been completed and ready to display. Report data is stored in the ^XTMP global and is purged automatically 7 days after the utility was last used. All reports need to be printed if there is a need to EVER see them.

The new option, TIU ADD SIGN UTIL (Additional Signer Utility), should be added to the desired user's secondary menu option and should not be made available on an existing TIU menu.

The introductory display for the utility:

VHA HANDBOOK 1907.01 defines the additional signer role as follows:

"Additional signer" is a communication tool used to alert a clinician about

information pertaining to the patient. This functionality is designed to

allow clinicians to call attention to specific documents and the recipient to

acknowledge receipt of the information. Being identified as an additional

signer does not constitute a co-signature. This nomenclature in no way implies

responsibility for the content of, or concurrence with, the note."

This utility provides options to report and/or remove outstanding additional

signers and the associated alerts by either date range or additional signer.

\*\* WARNING \*\*Removing additional signers from a document is PERMANENT and cannot be undone.

\*\* WARNING \*\*

Press \<Enter\> to continue.

The main display for the utility:

Additional Signer Utility

1 GENERATE a Report  
2 REMOVE Additional Signer(s)  
3 BOTH (Generate & Remove)  
4 VIEW Report(s)  
5 QUIT

What would you like to do? GENERATE a Report// ?

Enter a code from the list.

Select one of the following:

1 GENERATE a Report

2 REMOVE Additional Signer(s)

3 BOTH (Generate & Remove)

4 VIEW Report(s)

5 QUIT

What would you like to do? GENERATE a Report//

> **NOTE:** If there are no outstanding additional signers or generated reports to view, the utility will display:

No outstanding signatures or reports to view.

Press \<Enter\> to continue.

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 4 options" GENERATE a Report, REMVOE Additional Signer(s), BOTH \[Generate a Report and Remove Additional Signer(s)\], and VIEW Generated Report(s).

### GENERATE a Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option gathers data based on the user entered date range or user. No data is altered by this action.

What would you like to do? GENERATE// 1 GENERATE a Report

Select SEARCH CRITERIA:

1 Date Range 2 Additional Signer 3 Service/Section

4 Division 5 Document Status 6 DISUSER'D

7 Terminated

Enter SELECTION: 1//

The SEARCH CRITERIA is selectable by list or range, e.g., 1,3,5 or 2-4,7. You may select any combination of criteria. By default, if you select any criteria without selecting date range, the utility will search ALL outstanding additional signatures for the entire date range available. All SEARCH CRITERIA is inclusive of each other for a given search and all entries must meet each criteria selected.

| Date Range        | The default STARTING DATE is the oldest date with at least 1 outstanding additional signature. The default ENDING DATE is TODAY. |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Additional Signer | The NEW PERSON that must be identified as the additional signer if entered.                                                      |
| Service/Section   | All additional signers must be assigned to the entered Service/Section if entered.                                               |
| Division          | All additional signers must be a member of the Division if entered.                                                              |
| Document Status   | The TIU DOCUMENT STATUS of the document to be included in the report.                                                            |
| DISUSER'D         | If selected, additional signers must DISUSER'D (Disabled User=YES).                                                              |
| Terminated        | If selected, additional signers must be terminated as of TODAY.                                                                  |

> **NOTE:** Additional Signer Report results must meet ALL entered criteria. Conflicting criteria that will yield no results will be displayed prior to initiating the search.

### REMOVE Additional Signer(s) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will permanently remove/delete additional signers from the TIU MULTIPLE SIGNATURE File that meet the entered SEARCH CRITERIA. The search function performs identically to GENERATE a Report. Once removed, the additional signer will no longer appear in the document body in CPRS and any pending alerts will be removed:

The following will no longer appear in CPRS for additional signers removed by the utility:

Receipt Acknowledged By:

\* AWAITING SIGNATURE \* PROVIDER,ONE

> **NOTE:** This action can NOT be undone or recovered.

### BOTH \[Generate a Report & Remove Additional Signer(s)\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option creates a report of outstanding additional signers that meets the search criteria and permanently removes the entries from the TIU MULTIPLE SIGNATURE File. The report output adds information to the REMOVED and REMOVED BY columns indicating that the entries in the report were removed from the TIU DOCUMENT(s) during report creation.

### VIEW the Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is only available after a task running in GENERATE or BOTH modes have completed for the same user session (by Kernel Job \#).

This option will only be visible if there are pending or existing report(s) to view.

If there is one or more reports being generated but not yet complete, the utility will display the following:

Report Generated \# Additional Date Range

<u>\# Generated By Date@Time Signatures \[Additional Criteria\]</u>

No completed report to view.

\[Report(s) currently in progress.\]

Press \<Enter\> to continue.

Once one or more report(s) have been completed, the utility will display the available report(s) for selection. Select the report by entering the desired number in the \# column.

Example: VIEW Generated Report(s) display

Report Generated \# Additional Date Range

<u>\# Generated By Date@Time Signatures \[Additional Criteria\]</u>

1 REPORT,USER 06/14/23@08:26 53088 Mar 30, 1998-Jun 14, 2023

Which report would you like to display?

The additional signer reports are designed for a 255-character wide-column display in a comma separated value (CSV) format. If your session is not configured to display 255 characters per row, see Terminal Settings – Logging and Terminal Display.

Example DEVICE setting: \<device\>; Right Margin

The utility will prompt for DEVICE:

This output is designed for 255 characters per row.

Example DEVICE setting: ;255

DEVICE: HOME// ?

Specify a device with optional parameters in the format

Device Name;Right Margin;Page Length

or

Device Name;Subtype;Right Margin;Page Length

Or in the new format

Device Name;/settings

or

Device Name;Subtype;/settings

For example

HOME;80;999

or

HOME;C-VT320;/M80L999

Enter ?? for more information

Before displaying & capturing a report, ensure that your terminal is setup for 255-character wide output and logging. There are instructions following this section provided for information purposes.

> **NOTE:** If screen capture is enabled via logging, you do not need to resize your terminal window to log the data output.

After selecting a report to view, enter the desired setting for the DEVICE. After pressing \<Enter\>, the report will pause so that you may capture the output via logging:

At the following prompt, start logging to a text file:

This output is designed for 255 characters per row.

Example DEVICE input: ;255;9999999

DEVICE: HOME// ;255 HOME

To capture the report output, start logging now and press \<Enter\> to begin.

When the display is complete, stop logging at the prompt:

9932761,"PROVIDER,ONE","BAY PINES TEST LAB","CLEVELAND VAMC",,,"AA LAD,LAKXUM (A1033)","ADDENDUM","AJB NOTE TITLE",01/17/2023,UNSIGNED,06/06/2023,06/06/2023,"BAKKE,ANDREW J",,,

<span class="mark">\[stop logging before you...\] Press \<Enter\> to continue.</span>

The text output is now ready to import for viewing the results.

### Importing into Excel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Excel, from a new sheet: Data \> From Text/CSV \> Locate & Select the Log File.

At the data window, click "Load":

![](additional-signer-utility-guide-tiu-1-0-357/002.png)

You may sort by the following fields/columns:

| Field/Column                                                                                    | Definition                                                               |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| IEN                                                                                             | Internal Entry Number. TIU DOCUMENT \# in detailed view of CPRS.             |
| ADDITIONAL SIGNER\*                                                                             | NEW PERSON in the TIU MULTIPLE SIGNATURE file.                               |
| SERVICE/SECTION\*                                                                               | Service/Section of the Additional Signer \[optional\].                       |
| DIVISION\*                                                                                      | Division of the Additional Signer \[optional\].                              |
| DISUSER                                                                                         | YES indicates the Additional Signer is currently disabled \[optional\].      |
| TERMINATED                                                                                      | Termination Date of the Additional Signer \[optional\].                      |
| PATIENT\*                                                                                       | LASTNAME,FIRSTNAME (L####) – last/first limited to 22 characters (30 total). |
| LOCAL TITLE\*                                                                                   | TIU DOCUMENT TITLE (File \#8925.1).                                          |
| PARENT TITLE\*                                                                                  | TIU DOCUMENT TITLE if LOCAL TITLE is addendum \[conditionally optional\].    |
| PARENT DATE                                                                                     | REFERENCE DATE of PARENT TITLE \[conditionally optional\].                   |
| STATUS                                                                                          | DOCUMENT STATUS.                                                             |
| ENTRY DATE                                                                                      | Actual date document is created.                                             |
| REFERENCE DATE                                                                                  | This date may differ from the ENTRY DATE. Used for sorting in CPRS.          |
| EXPECTED SIGNER\*                                                                               | File \#8925, Field \#1204.                                                   |
| EXPECTED COSIGNER\*                                                                             | File \#8925, Field \#1208.                                                   |
| REMOVED                                                                                         | Date additional signer entry was removed.                                    |
| REMOVED BY\*                                                                                    | NEW PERSON responsible for creating & removing the additional signer entry.  |
| \* Indicates this field may be truncated if the length of the data exceeds the 255-character limit. |                                                                              |

> **NOTE:** Fields are dynamically truncated in this order only as needed: REMOVED BY, EXPECTED COSIGNER, EXPECTED SIGNER, PARENT TITLE, LOCAL TITLE, DIVISION, SERVICE/SECTION, ADDITIONAL SIGNER. Once the length of data no longer exceeds 255 characters, fields will no longer be truncated.

## Terminal Settings – Logging and Terminal Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These instructions are for the Reflection Workspace software. Depending on your appearance configuration, your menus/options may not appear exactly as shown but the configuration pages should be the same.

Logging: Select File\>Logging, at the "Logging Settings" window, select "Disk" and browse to a file location & name you can easily find later.

| ![](additional-signer-utility-guide-tiu-1-0-357/003.png) | ![](additional-signer-utility-guide-tiu-1-0-357/004.png) |
|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

255-character display: Select Setup\>Terminal\> From the Terminal Window, select Display:

| ![](additional-signer-utility-guide-tiu-1-0-357/005.png) | ![](additional-signer-utility-guide-tiu-1-0-357/006.png) |
|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|

From the "Set Up Display Settings" Window, under "Dimensions", "Number of characters per row:", enter 255.:

![](additional-signer-utility-guide-tiu-1-0-357/007.png)