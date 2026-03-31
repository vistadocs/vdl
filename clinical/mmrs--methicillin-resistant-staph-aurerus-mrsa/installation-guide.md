---
title: MRSA Program Tools Version 1 Installation Manual
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Installation Manual
app_code: MMRS
app_name: Methicillin Resistant Staph Aurerus (MRSA)
section: CLI
app_status: active
pkg_ns: MMRS
patch_ver: 1
patch_id: MMRS*1
group_key: "MMRS:MMRS:1"
file_numbers: 
  - 42
  - 60
  - 61
  - 62
  - 63
security_keys: []
menu_options: 0
description: [![](mrsa-program-tools-version-1-installation-manual/001.png)](#table-of-contents)
audience: 
keywords: 
  - mrsa
  - class
  - strong
  - span
  - table
  - tools
  - setup
  - report
  - anchor
  - unit
page_count: 0
word_count: 17717
section_count: 18
table_count: 43
figure_count: 0
appendix_count: 6
has_toc: False
is_stub: False
pub_date: January 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/mrsa1_0_im.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/mrsa1_0_im.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=189"
---

[![](mrsa-program-tools-version-1-installation-manual/001.png)](#table-of-contents)

MRSA PROGRAM TOOLSVersion 1.0

Patch MMRS\*1.0\*1

Installation Manual

January 2010 (Revised July 2010)

Office of Enterprise Development (OED)

Field Development

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [# List of Tables](#list-of-tables)
- [List of Figures](#list-of-figures)
  - [Text Conventions](#text-conventions)
  - [Graphic Conventions](#graphic-conventions)
  - [Keyboard Conventions](#keyboard-conventions)
  - [IRM Staff](#irm-staff)
  - [Laboratory Staff](#laboratory-staff)
  - [MRSA Prevention Coordinator](#mrsa-prevention-coordinator)
- [Release Notes](#release-notes)
- [Pre-Installation](#pre-installation)
  - [Test Account](#test-account)
  - [MRSA Program Tools Pre-Application Check List](#mrsa-program-tools-pre-application-check-list)
  - [Laboratory Requirements](#laboratory-requirements)
  - [Transition Guidance](#transition-guidance)
- [Installation](#installation)
  - [Software and Manual Retrieval](#software-and-manual-retrieval)
  - [Installation Process](#installation-process)
  - [Sample Installation Process](#sample-installation-process)
- [Implementation & Setup](#implementation-setup)
  - [Assign Menus and Security Key](#assign-menus-and-security-key)
  - [Set Up Parameters](#set-up-parameters)
  - [MRSA-PT Setup Menu Options](#mrsa-pt-setup-menu-options)
    - [MRSA Tools Parameter Setup (Main)](#mrsa-tools-parameter-setup-main)
  - [MRSA-PT Laboratory Parameter Screen and Help Prompts](#mrsa-pt-laboratory-parameter-screen-and-help-prompts)
    - [Conclusion](#conclusion)
- [MRSA Program Tools Pre-Application Checklist](#mrsa-program-tools-pre-application-checklist)
- [# Laboratory Parameter Setup for MDROs](#laboratory-parameter-setup-for-mdros)
- [# Business Rules for Nares Screening (Examples)](#business-rules-for-nares-screening-examples)
- [# Schedule TaskMan Tasks (Optional)](#schedule-taskman-tasks-optional)
- [# Test Scripts](#test-scripts)
- [# Laboratory Reporting of MRSA Test](#laboratory-reporting-of-mrsa-test)
| Date      | Description                                                                                           | Author                             |
|-----------|-------------------------------------------------------------------------------------------------------|------------------------------------|
| July 2010 | Updated for Patch MMRS\*1.0\*1. Adds Release Notes under the INSTALLATION AND IMPLEMENTATION section. | <span class="mark">REDACTED</span> |
| July 2010 | Initial Release. MMRS Package 1.0 installs the MRSA Program Tools software                            | <span class="mark">REDACTED</span> |
<span id="_Toc268767743" class="anchor"></span>Table 1 – Text Conventions

# # List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc268767692" class="anchor"></span>ORIENTATION

## Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other text conventions are used:
| Font                       | Used for…                             | Examples:                                                                                                                                          |
|--------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined          | Hyperlink to another document or URL      | “For further instructions on using KIDS, please refer to the [*Kernel Version 8.0 Systems Manual*](http://www.hardhats.org/kernel/docs/KRN8_0SM.PDF).” |
| Green text, dotted underlining | Hyperlink within this document            | “For instructions on how to set task these reports, see Print Isolation Report (Tasked).”                                                              |
| Arial                          | Text inside tables                        | (This table)                                                                                                                                           |
| Courier New                    | Menu options                              | MRSA Tools Parameter Setup                                                                                                                             |
|                                | Screen prompts                            | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                                                  |
|                                | Patch names                               | MMMS\*1.0\*1                                                                                                                                           |
|                                | VistA filenames                           | XYZ file \#798.1                                                                                                                                       |
|                                | VistA field names                         | “In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO.”                              |
| Courier New, bold              | User responses to screen prompts          | NO                                                                                                                                                 |
| Franklin Gothic Demi           | Keyboard keys                             | \< F1 \>, \< Alt \>, \< L \>, \<Tab\>, \<Enter\>                                                                                                       |
| Microsoft Sans Serif           | Software Application names                | MRSA Program Tools                                                                                                                                     |
|                                | Report names                              | Procedures report                                                                                                                                      |
| Times New Roman                | Body text (Normal text)                   | “There are no changes in the performance of the system once the installation process is complete.”                                                     |
| Times New Roman Italic         | Text emphasis                             | “It is *very* important…”                                                                                                                              |
|                                | National and International Standard names | *International Statistical Classification of Diseases and Related Health Problems*                                                                     |
|                                | Document names                            | *MRSA Program Tools Installation Manual*                                                                                                               |
<span id="_Toc268767744" class="anchor"></span>Table 2 – Graphic Conventions

## Graphic Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following graphic symbols are used throughout this document, usually in a boxed note or the equivalent.
| Graphic                                        | Used for…                                                           |
|----------------------------------------------------|-------------------------------------------------------------------------|
| ![](mrsa-program-tools-version-1-installation-manual/002.png)  | Information of particular interest regarding the current subject matter |
| ![](mrsa-program-tools-version-1-installation-manual/003.png) | A tip or additional information that may be helpful to you              |
| ![](mrsa-program-tools-version-1-installation-manual/004.png) | A warning concerning the current subject matter                         |
<span id="_Ref251670564" class="anchor"></span>Table 3 – Business Rules for Nares Screening Compliance

## Keyboard Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Text centered between arrows represents a keyboard key that should be pressed in order for the system to capture a user response or to move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.
*Example:* Press \<Tab\> to move the cursor to the next field.
Press \<Enter\> to select the default.
- One, two, or three question marks can be entered at any of the prompts for online help.
| ?   | One question mark displays a brief statement of what information is appropriate for the prompt.             |
|-----|-------------------------------------------------------------------------------------------------------------|
| ??  | Two question marks provide more help, plus any hidden actions.                                              |
| ??? | Three question marks will provide more detailed help, including a list of possible answers, if appropriate. |
<span id="_Ref251670457" class="anchor"></span>Table 4 – MRSA-PT Laboratory Parameter Options
- The caret ^ (also called the “up arrow” or circumflex) plus \<Enter\> can be used to exit the current option.
<span id="_Toc232559630" class="anchor"></span>
INTRODUCTION
<span id="_Toc268767697" class="anchor"></span>About the MRSA Program Tools Application
Manual data collection for the MRSA Prevention Initiative is time consuming. The MRSA Program Tools (MRSA-PT) application provides a method to extract data related to MRSA nares screening, clinical cultures, and patient movements within the selected facility. MRSA-PT contains reports that will extract and consolidate required data for entry into the [Inpatient Evaluation Center](#Glos_IEPC) (IPEC). Reports can also be generated to display real-time patient specific information, and can be used to identify patients that have a selected multi-drug resistant organism (MDRO) and to identify patients who did or did not receive a MRSA nares screen upon admission to the unit.
<span id="_Toc268767698" class="anchor"></span>Intended Audience

## IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is required for:
- Installing MRSA-PT
- Assigning menu and [Security Keys](#Glos_Sec_Key)
- Adding new divisions to the parameters
- Tasking the Print Isolation Report (Tasked)
- Tasking the Print Nares Screen Compliance List (Tasked)

## Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *highly recommended* that the Laboratory Information Manager (LIM) and/or Laboratory Automated Data Processing Application Coordinator (ADPAC), and a representative from the Microbiology section (director, supervisor, or technologist) *jointly* participate in reviewing the parameter set-up for historical MRSA laboratory reporting, as well as the laboratory parameter setup for other multi-drug resistant organisms, as appropriate.

## MRSA Prevention Coordinator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA Prevention Coordinator is required to participate in the parameter set-up due to the multi-disciplinary nature of the information to be retrieved by MRSA-PT. This will facilitate coordination of subsequent site interactions once the actual patch has been installed (*i.e.,* to be responsible for validation of reports).
<span id="_Toc249158589" class="anchor"></span>INSTALLATION AND IMPLEMENTATION

# Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch MMRS\*1.0\*1 updates the MRSA IPEC Admission Report and the MRSA IPEC Discharge/ Transmission Report to show an asterisk (\*) before the patient name if the patient was indicated for nasal screen upon admission to unit, based on site’s business rules. The revised documentation also corrects hyperlink errors in initial documentation release and clarifies the usual start and end dates for the MRSA IPEC Report. In addition, the *User Manual* Appendix D, Business Rules for Nares Screening (Examples) was deleted and appendixes following were renumbered.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Test Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *strongly* recommended that MRSA-PT be installed into a Test Account before installing into a Production Account.

## MRSA Program Tools Pre-Application Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA Program Tools Pre-Application Checklist ([Attachment A](#AppA)) should be used when installing the MRSA Program Tools Software package.

## Laboratory Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

"The Standardization of MRSA Laboratory Reporting" memorandum dated January 14, 2010 and the accompanying document "Laboratory Reporting of MRSA Test" describes how to set up and report MRSA lab tests. This process must be implemented in VistA to ensure successful installation of this package. Failure to implement these standards correctly might prevent user from running reports included in this package, and can cause the data on the reports to be inaccurate. A copy of the guidance for laboratory standardization can be found in [Appendix F](#_Toc266960404).

## Transition Guidance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product was initially developed at the XXXXX VA hospital as a Class III product. For sites using the XXXXX Class III version of the software there may be old options that are best if they are disabled once the MRSA Program Tools software is installed. Sites using the Class III version need to be aware that previously defined local option names may vary, and what follows is only an example.

To disable the options, IRM needs to edit the Out of Order Message field (#2) in the Option File (#19).

VA FileMan 22.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: OPTION// OPTION

EDIT WHICH FIELD: ALL// OUT OF ORDER MESSAGE

THEN EDIT FIELD:

Select OPTION NAME: AGJMRSA

1 AGJMRSA Print MRSA report

2 AGJMRSA SUMMARY Print MRSA Summary Report

3 AGJMRSA2 Print Ward List and MRSA History

4 AGJMRSA3 Print Ward List and Lab History

CHOOSE 1-4: 1 AGJMRSA Print MRSA report

OUT OF ORDER MESSAGE: Option disabled. Use Class I option.

Select OPTION NAME: AGJMRSA SUMMARY Print MRSA Summary Report

OUT OF ORDER MESSAGE: Option disabled. Use MRSA Program Tools option.

Select OPTION NAME: AGJ MRSA PARAMETERS Enter\Edit MRSA screen parameters

OUT OF ORDER MESSAGE: Option disabled. Use MRSA Program Tools option.

Select OPTION NAME: AGJMRSA2 Print Ward List and MRSA History

OUT OF ORDER MESSAGE: Option disabled. Use MRSA Program Tools option.

Select OPTION NAME: AGJMRSA3 Print Ward List and Lab History

OUT OF ORDER MESSAGE: Option disabled. Use MRSA Program Tools option.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA-PT software distributives and documentation are available on the following Office of Information Field Offices (OIFOs) \[ANONYMOUS SOFTWARE\] directories. The preferred method is to FTP the file from download.vista.med.va.gov, which will transmit the file from the first available server. Alternatively, sites may elect to retrieve the file from a specific OIFO.

<u>OIFO FTP Address Directory</u>

<span class="mark">REDACTED</span>

The Installation will create four new files in one new Global :^MMRS( . Please consult the *Technical Manual and Security Guide* and your System Manager with this information before proceeding.

## Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The actual installation time for this package should take no more than ten minutes. Although users may remain on the system, it is recommended that IRM install this patch during off-peak hours.

1.  From the Kernel Installation & Distribution System menu, select the Installation menu.
2.  From the Kernel Installation & Distribution System menu, select the LOAD DISTRIBUTION option and load MMRS_1.KID.
3.  From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter MMRS 1.0):
1.  You do not need to Backup a Transport Global – this patch contains routines in a new namespace; therefore, there are no routines to back up.
2.  You do not need to Compare Transport Global to Current System – this patch only contains new components not previously released; therefore, there is nothing to compare.
3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global – this option allows you to view the contents of the transport global.
4.  Use the Install Package(s) option and select the package MMRS 1.0.
5.  When prompted:

| Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO |
|--------------------------------------------------------------------------|

6.  When prompted:

| Want KIDS to INHIBIT LOGONs during the install? YES// NO |
|--------------------------------------------------------------|

7.  When prompted:

| Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO |
|------------------------------------------------------------------------------|

## Sample Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is an example of the installation process.

| ![](mrsa-program-tools-version-1-installation-manual/005.png) | Important Note: This MRSA-PT is a first-time installation. |
|----------------------------------------------------|----------------------------------------------------------------|

Select Installation Option: Install Package(s)

Select INSTALL NAME: MMRS 1.0 Loaded from Distribution 1/5/10@16:59:28

=\> MMRS 1.0 ;Created on Oct 30, 2009@09:17:48

This Distribution was loaded on Jan 05, 2010@16:59:28 with header of

MMRS 1.0 ;Created on Oct 30, 2009@09:17:48

It consisted of the following Install(s):

MMRS 1.0

Checking Install for Package MMRS 1.0

Install Questions for MMRS 1.0

Incoming Files:

104 MRSA SITE PARAMETERS

104.1 MRSA TOOLS LAB SEARCH/EXTRACT

104.2 MDRO TYPES (including data)

104.3 MRSA WARD MAPPINGS

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// NO

Want KIDS to INHIBIT LOGONs during the install? NO// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TNA

Install Started for MMRS 1.0 :

Jan 05, 2010@17:00:17

Build Distribution Date: Oct 30, 2009

Installing Routines:

Jan 05, 2010@17:00:17

Installing Data Dictionaries:

Jan 05, 2010@17:00:17

Installing Data:

Jan 05, 2010@17:00:17

Installing PACKAGE COMPONENTS:

MMRS 1.0

Installing SECURITY KEY

Installing FORM

Installing OPTION

Jan 05, 2010@17:00:17

Updating Routine file...

Updating KIDS files...

MMRS 1.0 Installed.

Jan 05, 2010@17:00:17

Not a production UCI

NO Install Message sent

---------------------------------------------------------------------------

--------------------------------------------------------------

100% \| 25 50 75 \|

Complete --------------------------------------------------------------

Install Completed

# Implementation & Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides all the necessary information, instructions, illustrations, and examples required for the MRSA Prevention Coordinators, Laboratory Personnel, Information & Resource Management personnel, and other users to implement and maintain the MRSA-PT software package. This information should be *adhered to as recommended* to ensure successful implementation.

| ![](mrsa-program-tools-version-1-installation-manual/006.png) | Important Note: *It is highly recommended* that the MRSA Prevention Coordinator, Laboratory Information Manager (LIM) and/or Laboratory Automated Data Processing Application Coordinator (ADPAC), and a representative from the Microbiology section (director, supervisor, or technologist) *jointly* participate in reviewing descriptions and entering of data for the MRSA-PT software package. These individual(s) will be responsible for initially setting the parameters, and validation of reports to ensure accuracy. |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Assign Menus and Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ACTION:    | Assign the MRSA Tools Setup Menu, the MRSA Tools Reports Menu*,* and the MMRS SETUP security key to the appropriate users. |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| ACTION BY: | Information Resource Management (IRM) personnel.                                                                           |

## Set Up Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ACTION:    | Set up the parameters by running the options in the MRSA Tools Setup Menu*.* For instructions, see [MRSA-PT Setup Menu Options](#_MRSA-PT_Setup_Menu), page [11](#mrsa-pt-setup-menu-options). |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACTION BY: | Information Resource Management, Laboratory Information Manager/Lab ADPAC, and MRSA Prevention Coordinator.                                                                                    |

## MRSA-PT Setup Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes the parameter descriptions and screen displays for the five options listed under the MRSA Program Tools Menu. The screen displays contain examples of the pre-populated fields. In order for the user to access the menu, IRM will need to assign the appropriate user(s) the MRSA Program Tools Menu and the MMRS SETUP key.

<span id="_Toc249158678" class="anchor"></span>Figure 1 – MRSA Tools Setup Menu Options

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option:</p>
<p>1 MRSA Tools Parameter Setup (Main)</p>
<p>2 MRSA Tools Lab Parameter Setup</p>
<p>3 MRSA Tools Ward Mapping Setup</p>
<p>4 MDRO Historical Days Edit</p>
<p>5 Isolation Orders Add/Edit</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MRSA Tools Parameter Setup (Main)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu option allows the user to setup divisions for their facility and setup business rules for nares screening for each division.

When adding divisions, include *only* acute care hospital(s) and Community Living Centers; do *not* include Community Based Outreach Clinics (CBOC), behavioral/mental health facilities, [domiciliary](#Glos_Domicilliary) facilities, etc.

During parameter setup, the user will have to answer prompts regarding business rules for nares screening on transfer and discharge. Based on the business rules at the facility please enter either YES or NO in the prompts.

Business rules for nares screening on transfer and/or discharge instituted by facilities are listed in Table 3. Answer either YES or NO if the following prompt/statement is true for your facility.

| Business Rules Prompts:                                          | Answer ‘Yes’ |                                                                                                  |                                                                                                                                                                                                                                                                                          | Answer ‘No’ |
|------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Receiving unit screen on unit-to-unit transfers                  |              | The receiving unit is responsible for nares screening for unit-to-unit transfers                 | Only the discharging/sending unit is responsible for screening for unit-to-unit transfers, and not the receiving unit.                                                                                                                                                                   |             |
| Discharging unit screen on unit-to-unit transfers                |              | The discharging/sending unit is responsible for nares screening on unit-to-unit transfers        | Only the receiving unit is responsible for nares screening on unit-to-unit transfers, and not the discharging unit,                                                                                                                                                                      |             |
| Screen patients with MRSA history on transfer-in                 |              | Patients are screened for MRSA on all transfer-ins, regardless of MRSA status                    | Nares screens are not required for known MRSA positive patients (*i.e.*, patients with a history of MRSA in the past year) for any transfer-in, via an interward transfer. To be considered ‘known positive’ the lab result must have been verified before the patient entered the unit. |             |
| Screen patient with MRSA history on discharge/death/transfer-out |              | Patients are screened for MRSA on all discharges/deaths/transfer-outs, regardless of MRSA status | Nares screens are not required for known MRSA positive patients (*i.e.*, patients with a history of MRSA in the past year) for any discharge/death/transfer-out. To be considered ‘known positive’ the lab result must have been verified before the patient left the unit.              |             |

<span id="_Toc249158679" class="anchor"></span>Figure 2 – MRSA Tools Parameter Setup (Main)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MRSA Tools Parameter Setup (Main)</strong></p>
<p>Select MRSA SITE PARAMETERS DIVISION: <strong>XXXXX VAMC</strong></p>
<p>Are you adding ‘XXXXX VAMC’ as</p>
<p>a new MRSA SITE PARAMETERS (the 1ST)? No// <strong>Y</strong> (Yes)</p>
<p>1. Receiving unit screen on unit-to-unit transfers: <strong>YES</strong></p>
<p>2. Discharging unit screen on unit-to-unit transfers: <strong>YES</strong></p>
<p>3. Screen patients with MRSA history on transfer-in: <strong>YES</strong></p>
<p>4. Screen patients with MRSA history on discharge/death/transfer-out: <strong>YES</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/007.png) | Important Note: There should never be a NO listed for both the ‘Receiving unit screen on unit-to-unit transfers’ and ’Discharging unit screen on unit-to-unit transfers’ prompts. This would indicate to the program that neither the Receiving nor Discharging Unit is screening the patients on unit-to-unit transfers. |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/008.png) | Important Note: Business rules will have to be added for each division. |
|----------------------------------------------------|-----------------------------------------------------------------------------|

Examples of business rules for nares for screening can be found in Business Rules for Nares Screening (Examples) (Appendix C).

## MRSA-PT Laboratory Parameter Screen and Help Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MRSA-PT Laboratory Parameter option screen prompts and help prompts definitions:

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th>MRSA-PT Parameter Screen Prompt</th>
<th>MRSA Program Tools Parameter Screen Help Prompt</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Laboratory Tests(s)</td>
<td>Used only for Chemistry tests. This is the test name to identify MRSA nares screen. Select from the LABORATORY TEST file #60.</td>
</tr>
<tr class="even">
<td>Indicator (for Laboratory Test(s) only)</td>
<td><p>Select the code that will determine how to match lab results:</p>
<p>1 = Use Reference Ranges</p>
<p>2 = Contains</p>
<p>3 = Greater Than</p>
<p>4 = Less Than</p>
<p>5 = Equal To</p></td>
</tr>
<tr class="odd">
<td>Value</td>
<td>POS, Positive, etc. Answers must be 1-30 characters in length. This is a <a href="#Glos_FreeTextField">FREE TEXT</a> field. It is not case-sensitive, <em>e.g.</em>, entering ‘POS’ or ‘pos’ are equivalent.</td>
</tr>
<tr class="even">
<td>Selected Etiology</td>
<td>Consider synonymous with organism, final microbial diagnosis/<a href="#Glos_isolate">isolate</a>. Select from the ETIOLOGY FIELD file #61.2.</td>
</tr>
<tr class="odd">
<td>Antimicrobial Susceptibility</td>
<td>Enter the antimicrobial that will be used in screening out sensitive Etiologies (<em>e.g.</em>, “Oxacillin” for <em>Staphylococcus aureus</em>). Select from the ANTIMICROBIAL SUSCEPTIBILITY file #62.06.</td>
</tr>
<tr class="even">
<td>Indicator (for Antimicrobial Susceptibility only)</td>
<td><p>Select the code that will determine how to match susceptibility interpretations:</p>
<p>1 = Contains</p>
<p>2 = Greater Than</p>
<p>3 = Less Than</p>
<p>4 = Equal To</p></td>
</tr>
<tr class="odd">
<td>Indicated Value</td>
<td>Enter the data to be compared using the Indicator field. For example, ‘<strong>R</strong>’.</td>
</tr>
<tr class="even">
<td>Include (for Bacteriology Report Remarks)</td>
<td>Enter the phrase to be used to search for positive results. Answers must be 1-68 characters in length. This is a <a href="#Glos_FreeTextField">FREE TEXT</a> field.</td>
</tr>
<tr class="odd">
<td>Exclude (for Bacteriology Report Remarks)</td>
<td>Only to be used in cases where the phrases used to indicate a positive result is also contained in the phrases used to indicate a negative result. Answers must be 1-68 characters in length. This is a <a href="#Glos_FreeTextField">FREE TEXT</a> field.</td>
</tr>
</tbody>
</table>

#### MRSA Tools Lab Parameter Setup

This option allows the user to enter laboratory parameters for historical reporting of MRSA in the past 12 months. In addition, the user can enter parameters for laboratory reporting of other multi-drug resistant organisms (MDROs) (*Carbapenem*-resistance, Vancomycin-Resistant *Enterococcus* , *Clostridium difficile*, and Extended-Spectrum *beta-lactamase*). The new laboratory standardizations for MRSA reporting have been hard-coded into the program to pick up current MRSA results and do *not* need to be entered into the parameters. The data entered in using this option will be used by the MRSA IPEC Reports and the MDRO Isolation Report to pull laboratory information.

| ![](mrsa-program-tools-version-1-installation-manual/009.png) | Important Note: The following Laboratory Tests do not need to be added to the laboratory parameters setup: MRSA SURVL NARES DNA, MRSA SURVL NARES AGAR, MURSL SURVL OTHER DNA, AND MRSA SURVL OTHER AGAR. In addition, do *not* add STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) to the Selected Etiology section. This information has been hard coded into the program. |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The user will be prompted to enter the division (if only one division has been set up at the site, this prompt will be skipped). The user will then be prompted to select the MDRO for which the parameters are being set. The five MDROs listed (Methicillin-resistant *Staphylococcous aureus*, *Carbapenem*-resistance, Vancomycin-Resistant *Enterococcus* , *Clostridium difficile*, and Extended-Spectrum *beta-lactamase*) are the only MDROs that can be chosen. The user can choose to define all five or just MRSA. All users will have to identify how MRSA was previously reported (before the new laboratory standards were implemented) in order to gather the relevant information for the MRSA IPEC Report. The other MDRO(s) are optional and only need to be defined if the user will be running the Print Isolation Report option.

<span id="_Toc249158680" class="anchor"></span>Figure 3 – MRSA Tools Lab Parameter Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MRSA Tools Lab Parameter Setup</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Select the MDRO: ?</p>
<p>Answer with MDRO TYPES NUMBER, or ABBREVIATION</p>
<p>Choose from:</p>
<p>1 MRSA Methicillin-resistant Staphylococcus aureus</p>
<p>2 CRB-R Carbapenem-Resistance</p>
<p>3 VRE Vancomycin-Resistant Enterococcus</p>
<p>4 C. diff Clostridium difficile</p>
<p>5 ESBL Extended-spectrum beta-lactamase</p>
<p>Select the MDRO: <strong>MRSA</strong></p>
<p>Do you want to see a description for MRSA? YES//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

For CH-subscripted tests *only*, Laboratory Test(s) field will be used (see Figure 4).

- Select the CH-subscripted test from the LABORATORY TEST file (#60) (the system will not let you choose a Test whose Subscript field (Field \#4 in File \#60) is set to anything other than ‘CH’).
- In the Indicator field, enter the logic that is to be used to determine if the test was positive. This field is a set of codes. See Table 4 to determine the correct code that is used to denote a positive test result.
- In the Value field, enter how to search for positive results ONLY. This is a [free text](#Glos_FreeTextField) field. Do <u>*not*</u> enter how negative results are entered. (The comparison is not case-sensitive, *e.g.*, entering ‘POS’ or ‘pos’ will not make a difference).

| ![](mrsa-program-tools-version-1-installation-manual/010.png) | Important Note: When entering Value for Laboratory Test(s), the Internal Value that is used to report laboratory results has to be added. Value can be a set of codes and the program looks at the internal value for data extraction. For example, if the site uses a set of codes in which 1 = POS and 0 = NEG, then the user will have to add “1” to the value field. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc249158681" class="anchor"></span>Figure 4 – MRSA Tools Lab Parameter Display for MDRO

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p><strong>MRSA (BY PCR) SCREEN Contains POS</strong></p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

For Microbiology-subscripted tests *only*, the Selected Etiology field will be used.

- Select from the ETIOLOGY FIELD file (#61.2).

<span id="_Toc249158682" class="anchor"></span>Figure 5 – MRSA Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>MRSA (BY PCR) SCREEN Contains POS</p>
<p>Selected Etiology</p>
<p><strong>STAPHYLOCOCCUS AUREUS</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After selecting the desired etiology, the user will be prompted to enter Antimicrobial Susceptibility for the organism and how to search for the result by entering information into the Indicator and Indicated Value fields. If no antimicrobials are entered, the program will consider the result positive as long as the result contains that organism, regardless of susceptibility. However, if an antimicrobial is entered, the program will not consider the result positive unless the Organism meets the condition that is entered for one of the antimicrobials (for *e.g.*, if ‘Oxacillin Contains R’ is entered in the Antimicrobial Susceptibility section for the ‘Staphylococcus Aureus’ organism, then the test result will only be considered positive if it contains that organism, and it is Oxacillin Resistant). If more than one Antimicrobial Susceptibility is entered, the program will consider the result positive as long as one of the Antimicrobial Susceptibility entered matched the indicated value.

<span id="_Toc249158683" class="anchor"></span>Figure 6 – MRSA Tools Parameter Setup for Antimicrobial Susceptibility

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>MRSA (BY PCR) SCREEN Contains POS</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected Etiology</p>
<p>STAPHYLOCOCCUS AUREUS</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>OXACILLIN Contains R</strong></td>
</tr>
</tbody>
</table>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></td>
</tr>
</tbody>
</table>

After entering the required information for CH- and MI-subscripted tests, the user can go to the second page of the form to enter information concerning the Bacteriology Report Remarks. If the site reported positives by entering in certain comments under the BACT RPT REMARK fields, this option will allow the sites to enter those comments here. The form will also allow the user to exclude certain comments. The “exclude” functionality only needs to be used in cases where the phrase used to denote a positive result is also contained in the phrase used to denote a negative result. For example, for molecular based tests, the following two phrases are commonly used: “MRSA DNA DETECTED” for positive results and “NO MRSA DNA DETECTED” for negative results. The program is only looking for positive results. However, in this example, if nothing is entered in the Exclude section, then a result that has the remark ‘NO MRSA DNA DETECTED’ will be considered positive (because it also contains the text ‘MRSA DNA DETECTED’). To prevent this, the user will want to *include the positiveandexclude the negative* test results.

Sites need to be very cautious when using the Bacteriology Report Remarks. Since laboratory has the option to use free-text when entering the report, it is possible for the reporting text not to be consistent, or even contain spelling mistakes. In this case, it would be almost impossible to enter all possible variations into the Include parameters. Even if the site uses canned-comments there is possibility for error. This functionality (to search the Bacteriology Report Remarks) was mostly included to accommodate sites who in the past were using bacteriology report remarks to denote MRSA positives, so that at least the program can pick up as many historical positives as possible.

<span id="_Toc249158684" class="anchor"></span>Figure 7 – Bacteriology Report Remarks

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 2 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>________________________________________________________________________</p>
<p>BACTERIOLOGY REPORT REMARKS</p>
<p>Include Exclude</p>
<p><strong>MRSA DNA DETECTED NO MRSA DNA DETECTED</strong></p>
<p>________________________________________________________________________</p>
<p>Exit Save Next Page Refresh</p>
<p>Enter a command or '^' followed by a caption to jump to a specific field.</p>
<p>Save changes before leaving form (Y/N)? Y Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/011.png) | Important Note: Please be consistent with site specific data spelling or alternate spelling to ensure accurate data capture. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/012.png) | Important Note: If the facility records MRSA results under Chemistry and Microbiology then information for all tests needs to be entered under their respective fields. |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/013.png) | Important Note: Before exiting the menu, save changes. |
|----------------------------------------------------|------------------------------------------------------------|

Facilities can delete information in the field(s): Selected Test(s), Selected Etiology, Antimicrobial Susceptibility or Bacteriology Report Remarks, if something was added in error. To do so, the user will have to go to the field where the change needs to occur and place an “@” symbol in the desired field. (Example: Removing Oxacillin from Antimicrobial Susceptibility). When prompted, select “Y” to delete the desired field. See Figure 8 below. he prograhe program will ask if the desired field shoulto beuser can delete this information. To do so,

<span id="_Ref251670618" class="anchor"></span>Figure 8 – MRSA Tools Parameter Setup for Antimicrobial Susceptibility – Deleting an Entry

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>MRSA (BY PCR) SCREEN Contains POS</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected</p>
<p>STAPHYLOCOCCUS AUREUS</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>@</strong> Contains R</td>
</tr>
</tbody>
</table>
<p>WARNING: DELETIONS ARE DONE IMMEDIATELY!</p>
<p>(EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)</p>
<p>Are you sure you want to delete this entire Subrecord (Y/N)? <strong>Y</strong></p></td>
</tr>
</tbody>
</table>

For information about setting up the Laboratory Parameter Setup for *Carbapenem*-resistance, Vancomycin-Resistant *Enterococcus*, *Clostridium difficile*, and Extended-Spectrum *beta-lactamase*, please refer to [Appendix B](#_Toc249158642).

#### #### MRSA Tools Ward Mapping Setup

This option allows the user to define geographical units within each division to run reports. A geographical unit can consist of one or more wards listed in VistA, and for all intents and purposes in considered one unit. The user can “map/group” units together for reporting purposes. For example, one unit may be divided into Unit X Medicine and Unit X Surgery, but is one geographical unit. By mapping the wards (*e.g.*, Unit X Med-Surg), the report will consider all the wards mapped together as one location, and all transfers between Unit X Medicine and Unit X Surgery will be ignored.

The ward mappings must be created for every unit you would like to run the reports for (even if there is only one VistA ward for the unit).

Upon running the option, the user will be prompted to create a new Geographical Location, or edit an existing one. When adding a new location, the user can name the location whatever they want, but common sense should be used. The user will then be prompted to enter the MRSA Ward Mappings Type and IPEC Unit ID. This information is required for the program to extract the data for upload to the IPEC website for data reporting purposes. For the location Type, the user has the choice of the following: Acute Care, CLC, OBS and Other. The user will then be prompted for the location’s IPEC Unit ID. This is the ID number that identifies this unit in IPEC. This is only for Acute Care and CLC units reported to IPEC. Do *not* assign a Unit ID to any unit that is classified as ‘OBS’ or ‘Other’. IPEC Unit IDs are available from the VHA MRSA Program Office and/or the [Inpatient Evaluation Center](#Glos_IEPC) (IPEC). The user will then be prompted to select from existing wards in VistA to be included in the Geographical Location that was defined.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](mrsa-program-tools-version-1-installation-manual/014.png)</th>
<th><p><strong>Important Note:</strong> Observation (OBS) patients should <em>not</em> be included in the number of admissions, discharges, and bed days of care that is reported to IPEC for the inpatient units; these patients are considered outpatients. Therefore, sites should not generate a MRSA IPEC Report for any OBS units. However, if the site chooses to run the Isolation Report or Nares Screen Compliance List for an OBS unit, they are free to do so.</p>
<p>In order to prevent data from OBS wards accidentally being reported to IPEC, sites should <em>not</em> map any OBS wards together with an inpatient ward (acute care or CLC). If the site wishes to run</p>
<p>the Isolation Report or Nares Screen Compliance List for an OBS unit, they can create a separate Geographical Location that only includes the OBS ward.</p>
<p>Example: The site has three wards in VistA: 4West Medicine, 4West Surgery and 4West OBS. The site needs to create a Geographical Location 4West, which consists of 4West Medicine and 4West Surgery. The site can optionally create a separate geographical location called 4West OBS that contains just the 4West OBS ward. However, under no circumstances should the 4West OBS ward be mapped together with the 4West Medicine and 4West Surgery wards under the same geographical location.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc249158686" class="anchor"></span>Figure 9 – MRSA Tools Ward Mapping Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MRSA Tools Ward Mapping Setup</strong></p>
<p>Select Geographical Unit: <strong>11AB</strong></p>
<p>  Are you adding '11AB' as a new MRSA WARD MAPPINGS (the 2ND)? No// <strong>Y</strong>  (Yes)</p>
<p>   MRSA WARD MAPPINGS TYPE: <strong>ACUTE CARE</strong></p>
<p>   MRSA WARD MAPPINGS IPEC UNIT ID: <strong>999</strong></p>
<p>MRSA TOOLS WARD MAPPING SETUP</p>
<p>DIVISION: XXXXX VAMC                        </p>
<p>GEOGRAPHICAL UNIT: 11AB                         </p>
<p>_____________________________________________________________________________</p>
<p>WARD LOCATIONS:</p>
<p><strong>11AB                         </strong></p>
<p><strong>11ASURG                      </strong></p>
<p>                   </p>
<p>                                      </p>
<p>_____________________________________________________________________________</p>
<p>COMMAND:                                                Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Facilities can delete a Geographical Unit. To do so select the desired geographical unit (*e.g.*,PACU) and enter “@” and press enter. Select “Y” to delete the entire geographical unit from the setup. See Figure 10 below.

he prograhe program will ask if the desired field shoulto beuser can delete this information. To do so,

<span id="_Ref251670652" class="anchor"></span>Figure 10 – MRSA Tools Ward Mapping Setup: Deleting a Geographical Unit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MRSA Tools Ward Mapping Setup</strong></p>
<p>DIVISION: <strong>XXXXX VAMC</strong>                        </p>
<p>SELECT GEOGRAPHICAL UNIT: <strong>PACU</strong>                         </p>
<p>_____________________________________________________________________________</p>
<p>NAME: PACU//<strong>@</strong></p>
<p>SURE YOU WANT TO DELETE THE ENTIRE ‘PACU’ MRSA WARD MAPPINGS? <strong>Y</strong> (Yes)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### MDRO Historical Days Edit

This option allows the user to define the time frame selected for each MDRO defined in the MRSA Tools Lab Parameter Setup. The information entered in this menu provides information for the Print Isolation Report option (that report displays patient’s historical lab data for certain MDROs). The user will be asked to enter the number of historical days the program should search for a positive result for each MDRO. This information can only be entered in *days* (*e.g.*, 30 for 1 month; 90 for 1 quarter; 365 for 1 year). If no response is entered, the program will not display that MDRO on the Isolation Report.

| ![](mrsa-program-tools-version-1-installation-manual/015.png) | Warning: All sites must enter the following for MRSA in historical days: 365. This is to ensure that history of MRSA within the past year is identified for prevalence and transmission purposes. |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

For other MDROs selected, it is at the discretion of the facility to determine the time frame to search for the last positive MDRO result.

<span id="_Toc249158688" class="anchor"></span>Figure 11 – MDRO Historical Days Edit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MDRO Historical Days Edit</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Enter the number of days to search for MRSA: <strong>365</strong></p>
<p>Enter the number of days to search for IMP: <strong>365</strong></p>
<p>Enter the number of days to search for VRE: <strong>365</strong></p>
<p>Enter the number of days to search for C. diff: <strong>28</strong></p>
<p>Enter the number of days to search for ESBL: <strong>365</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Isolation Orders Add/Edit

This option allows the user to enter the orderable item(s) at their site that are used for isolation purposes. Each Isolation Order added has to be mapped to one of the following Expanded Precaution Types (Contact Precautions, Contact Precautions Special, Airborne Infection, Droplet, Protective Environment, and Isolation Order). The information entered will be used to populate the Print Isolation Report option.

| ![](mrsa-program-tools-version-1-installation-manual/016.png) | Important Note: This option should only be used if the site uses orderable items when a patient needs to be in isolation. |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc249158689" class="anchor"></span>Figure 12 – MRSA Tools Isolation Orders Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS ISOLATION ORDERS SETUP</p>
<p>DIVISION: XXXXX VAMC</p>
<p>___________________________________________________________________________</p>
<p>Isolation Orders Expanded Precaution Type</p>
<p><strong>CONTACT PRECAUTIONS CONTACT PRECAUTIONS</strong></p>
<p><strong>CONTACT PRECAUTIONS SPECIAL CONTACT PRECAUTIONS SPECIAL</strong></p>
<p><strong>AIRBORNE INFECTION ISOLATIOTI AIRBORNE INFECTION</strong></p>
<p><strong>DROPLET PRECAUTIONS DROPLET</strong></p>
<p><strong>PROTECTIVE ENVIRONMENT PROTECTIVE ENVIRONMENT</strong></p>
<p><strong>ISOLATION ORDER ISOLATION ORDER</strong></p>
<p>__________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Conclusion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the user has finished entering the information as directed, the MRSA Tools parameters should not be changed except under the following conditions:

- Changes in business rules for nares screening upon transfer or discharge to ensure the program captures the most current practices
- Adding/Removing a ward/unit from the program
- Ward mapping
- Lab changes how they report results for the specified MDROs
- Changes the Orderable Items used for isolation purposes

The MRSA-PT national package materials (*i.e.*, IPEC Reports) should be reviewed periodically by the sites for data validation.

<span id="_MRSA-PT_Setup_Menu" class="anchor"></span>

APPENDIX A

# MRSA Program Tools Pre-Application Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following checklist should be used when installing the MRSA Program Tools Software package. The laboratory standardization section should be completed prior to installing the package. The parameter setup section should be completed prior to running any reports.

| Item                               | Checklist Question                                                                                                                                                                                                                                                                                     |                  | Responsibility | Completed |     |         |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|--------------------|---------------|-----|---------|
|                                        |                                                                                                                                                                                                                                                                                                            |                  |                    | Yes       |     | N/A |
| LABORATORY STANDARDIZATION         |                                                                                                                                                                                                                                                                                                            |                  |                    |               |     |         |
| 1                                      | Add organism ‘STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)’ to the Etiology Field file (#61.2).                                                                                                                                                                                                      | LIM or Lab ADPAC |                    |               |     |         |
| 2                                      | Add test ‘MRSA SURVL NARES DNA’ with LOINC Code 35492-8. (Applies only to sites performing molecular testing for nares screening).                                                                                                                                                                         | LIM or Lab ADPAC |                    |               |     |         |
| 3                                      | Add test ‘MRSA SURVL OTHER DNA’ with LOINC Code 35492-8. (Applies only to sites performing surveillance screening (*e.g.*, axilla, perineum) using molecular testing).                                                                                                                                     | LIM or Lab ADPAC |                    |               |     |         |
| 4                                      | Add test ‘MRSA SURVL NARES AGAR’ with LOINC Code 13317-3. (Applies only to sites performing chromogenic media for nares screening).                                                                                                                                                                        | LIM or Lab ADPAC |                    |               |     |         |
| 5                                      | Add test ‘MRSA SURVL OTHER AGAR’ with LOINC Code 13317-3. (Applies only to sites performing surveillance screening (*e.g.*, axilla, perineum) using chromogenic media).                                                                                                                                    | LIM or Lab ADPAC |                    |               |     |         |
| 6                                      | Add modifiers to the end of the test name if need to offer site/division specific tests. (Applies only to integrated or co-located sites).                                                                                                                                                                 | LIM or Lab ADPAC |                    |               |     |         |
| 7                                      | When setting up the Data Name for the MRSA CH-subscripted tests added above (Item \# 2 – 5), make sure to use the data type Set of Codes. (Negative is to Negative, Positive is to Positive and Invalid is to Invalid Inhibitors Present).                                                                 | LIM or Lab ADPAC |                    |               |     |         |
| 8                                      | Update EPI parameters with the changes made while standardizing MRSA laboratory reporting.                                                                                                                                                                                                                 | LIM or Lab ADPAC |                    |               |     |         |
| MRSA PROGRAM TOOLS PARAMETER SETUP |                                                                                                                                                                                                                                                                                                            |                  |                    |               |     |         |
| 9                                      | Install Patch MMRS 1.0.                                                                                                                                                                                                                                                                                    | IRM              |                    |               |     |         |
| 10                                     | Assign users the appropriate menus and keys.                                                                                                                                                                                                                                                               | IRM              |                    |               |     |         |
| 11                                     | Using option ‘MRSA Tools Parameter Setup (Main)’, add the division(s) that the facility will require. For integrated or co-located sites more than one division will most likely need to be added. After the division is added, answer the prompts based on the business rules in place for that division. | MPC/IRM          |                    |               |     |         |
| 12                                     | Using option ‘MRSA Tools Lab Parameter Setup’, add the appropriate lab parameters for the different MDROs.                                                                                                                                                                                                 | MPC/LIM          |                    |               |     |         |
| 13                                     | Using option ‘MRSA Tools Ward Mapping Setup’, setup the ward mappings. (Remember to separate out OBS units from the geographical units and to create all OBS units as separate units).                                                                                                                     | MPC              |                    |               |     |         |
| 14                                     | Using option ‘MDRO Historical Days Edit’, enter the time frame to search for the last positive MDRO result?                                                                                                                                                                                                | MPC              |                    |               |     |         |
| 15                                     | Using option ‘Isolation Orders Add/Edit’ add the orders that are used for isolation purposes. (Only needed if the site uses Isolation Orders).                                                                                                                                                             | MPC              |                    |               |     |         |
| 16                                     | Setup the tasked options: ‘Print Isolation Report (Tasked)’ and ‘Print Nares Screen Compliance List (Tasked)’ to the appropriate printers (optional).                                                                                                                                                      | IRM/MPC          |                    |               |     |         |

IRM: Information Resource Management

LIM: Laboratory Information Manager

MPC: MRSA Prevention Coordinator

<span id="_Toc249158642" class="anchor"></span>APPENDIX B

# # Laboratory Parameter Setup for MDROs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA Program Tools software allows facilities to add several MDROs for purposes of gathering information for the Isolation Report. The following can be used to help setup laboratory parameters for *Carbapenem-*resistance, Vancomycin Resistant *Enterococcus*, *Clostridium difficile*, and Extended-Spectrum *beta-lactamase.*

#### #### *Carbapenem-*Resistance

Adding *Carbapenem*-resistance to the MRSA Tools Lab Parameter Setup is optional. The purpose of adding this resistance marker for numerous pathogens is to identify a patient’s current or prior history of *carbapenem*-resistance based on laboratory reporting and the time frames that are entered to search for the patient’s status. This information is displayed on the Isolation Report. To display this information, please enter the appropriate etiology (or etiologies) to search for and select the appropriate Antimicrobial Susceptibility for the organism and how to search for the results. The user can add multiple etiologies with different antimicrobial susceptibilities to search for *carbapenem*-resistance. For example, the user can add the etiology *Klebsiella* and set the antimicrobial susceptibility for resistance to *Meropenem*. The user can then add the etiology *Pseudomonas* and set the antimicrobial susceptibility for resistance to *Imipenem*. The user will need to enter all etiologies to be searched for and the appropriate antimicrobial susceptibility.

<span id="_Toc249158698" class="anchor"></span>Figure 13 – MRSA Tools Lab Parameter Display for MDRO

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Selected Etiology will only be used for test results reported under Microbiology. Select from the ETIOLOGY FIELD file \#61.2.

<span id="_Toc249158699" class="anchor"></span>Figure 14 – MRSA Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p><strong>KLEBSIELLA PNEUMONIAE</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After selecting the desired etiology, the user will be prompted to enter Antimicrobial Susceptibility for the organism and how to search for the result by entering information into the Indicator and Indicated Value fields.

<span id="_Toc249158700" class="anchor"></span>Figure 15 – MRSA Tools Parameter Setup for Antimicrobial Susceptibility

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected</p>
<p>KLEBSIELLA PNEUMONIAE</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MEROPENEM Contains R</strong></td>
</tr>
</tbody>
</table>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></td>
</tr>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/017.png) | Important Note: If multiple organisms and/or antimicrobial susceptibilities are needed for identification then each organism and/or antimicrobial susceptibility has to be added to the laboratory parameter setup. |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

After entering the required information for Microbiology subscripted tests, the user can go to the second page of the form to enter information concerning the Bacteriology Report Remarks. If the site reported positives by entering in certain comments under the BACT RPT REMARK fields, this option will allow the sites to enter those comments here. The form will also allow the user to exclude certain comments. The “exclude” functionality only needs to be used in cases where the phrase used to denote a positive result is also contained in the phrase used to denote a negative result. For example, the following two phrases could be used: “CARBAPENEM RESISTANCE DETECTED” for positive results and “NO CARBAPENEM RESISTANCE DETECTED” for negative results. The program is looking for positive results. The user will want to *include the positiveandexclude the negative* test results. See below for example.

<span id="_Toc249158701" class="anchor"></span>Figure 16 – Bacteriology Report Remarks

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 2 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>________________________________________________________________________</p>
<p>BACTERIOLOGY REPORT REMARKS</p>
<p>Include Exclude</p>
<p><strong>CARBAPENEM RESISTANCE DETECTED NO CARBAPENEM RESISTANCE DETECTED</strong></p>
<p>________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/018.png) | Important Note: Please be consistent with site specific data spelling or alternate spelling to ensure accurate data capture. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/019.png) | Important Note: If “BACT RPT REMARK” is used, it is important that a consistent method of reporting is used to identify results (*i.e.*, canned comments). If Free-Text is used, it is likely the report will not display accurate information. |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/020.png) | Important Note: Before exiting the menu, save changes. |
|----------------------------------------------------|------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/021.png) | Important Note: This is only a suggestion. Please add accordingly to your site definition. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------|

#### Vancomycin-Resistant *Enterococcus*

Adding Vancomycin-resistant *Enterococcus* to the MRSA Tools Lab Parameter Setup is optional. The purpose of adding this pathogen to the parameter set-up is to identify a patient’s current or prior history of VRE based on laboratory reporting and the time frames that are entered to search for the patient’s status. This information can optionally be displayed on the Isolation Report. This includes cultures positive for prevalence and surveillance review, including specimens of stool and rectal swabs. It is important to search for all vancomycin resistant enterococci, whether speciated or not. It is important to be sure to list all the places in the Microbiology Laboratory package where Enterococcus are found, either as Enterococcus, E. (sp.), Group D-Streptococcus, *E. faecalis*, *E. faecium*, *E. durans, E. gallinarum, E. casseliflavus*, etc. The laboratory parameter setup for the MRSA Program Tools should match the same parameter setup for the EPI (Emerging Pathogens Initiative). If changes are made to how Vancomycin-resistant Enterococcus is reported it should also be changed in EPI parameter setup.

<span id="_Toc249158702" class="anchor"></span>Figure 17 – MRSA Tools Lab Parameter Display for MDRO

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: VRE</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Selected Etiology will only be used for test results reported under Microbiology. Select from the ETIOLOGY FIELD file \#61.2.

<span id="_Toc249158703" class="anchor"></span>Figure 18 – MRSA Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p><strong>ENTEROCOCCUS</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After selecting the desired etiology, the user will be prompted to enter Antimicrobial Susceptibility for the organism and how to search for the result by entering information into the Indicator and Indicated Value fields.

<span id="_Toc249158704" class="anchor"></span>Figure 19 – MRSA Tools Parameter Setup for Antimicrobial Susceptibility

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected</p>
<p>ENTEROCOCCUS</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VANCOMYCIN Contains R</strong></td>
</tr>
</tbody>
</table>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></td>
</tr>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/022.png) | Important Note: Please be consistent with site specific data spelling or alternate spelling to ensure accurate data capture. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/023.png) | Important Note: Before exiting the menu, save changes. |
|----------------------------------------------------|------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/024.png) | Important Note: This is only a suggestion. Please add accordingly to your site definition. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------|

#### *Clostridium difficile*

Adding *Clostridium difficile* to the MRSA Tools Lab Parameter Setup is optional. The purpose of adding this pathogen to the parameter set-up is to identify a patient’s current or prior history of *Clostridium difficile* based on laboratory reporting and the time frames that are entered to search for the patient’s status. This information can optionally be displayed on the Isolation Report. The laboratory parameter setup for the MRSA Program Tools should match the same parameter setup for the EPI (Emerging Pathogens Initiative). If changes are made to how *Clostridium difficile* is reported it should also be changed in EPI parameter setup. The result must occur as a “bacterial etiology” or as a retrievable positive result for a chemistry/serology laboratory test. Any results contained in a “Free-Text” section will not allow incorporation of *Clostridium difficile* into the MRSA Program Tools software Isolation Report format.

<span id="_Toc249158705" class="anchor"></span>Figure 20 – MRSA Tools Lab Parameter Display for MDRO

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: C.diff</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p><strong>CLOSTRIDUM DIFFICILE TOXIN CONTAINS POS</strong></p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Laboratory Test(s) can only be used for test results reported under Chemistry.

- Select the test name from the LABORATORY TEST file \#60.
- In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO. This field is a set of codes.
- In the Value field, enter how to search for positive results ONLY. This is a [free text](#Glos_FreeTextField) field. Do <u>not enter how negative results are entered.</u>

| ![](mrsa-program-tools-version-1-installation-manual/025.png) | Important Note: When entering Value for Laboratory Test(s), the Internal Value that is used to report laboratory results has to be added. Value can be a set of codes and the program looks at the internal value for data extraction. For example, if the site uses a set of codes in which 1 = POS and 0 = NEG, then the user will have to add “1” to the value field. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Selected Etiology will only be used for test results reported under Microbiology. Select from the ETIOLOGY FIELD file \#61.2.

<span id="_Toc249158706" class="anchor"></span>Figure 21 – MRSA Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: C.diff</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>CLOSTRIDUM DIFFICILE TOXIN CONTAINS POS</p>
<p>Selected Etiology</p>
<p><strong>CLOSTRIDIUM DIFFICILE TOXIN POSITIVE</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/026.png) | Important Note: Please be consistent with site specific data spelling or alternate spelling to ensure accurate data capture. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/027.png) | Important Note: Before exiting the menu, save changes. |
|----------------------------------------------------|------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/028.png) | Important Note: This is only a suggestion. Please add accordingly to your site definition. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------|

#### Extended-Spectrum *Beta-Lactamase*

Adding Extended-Spectrum Beta Lactamase to the MRSA Tools Lab Parameter Setup is optional. The purpose of adding pathogens containing this form of antimicrobial resistance to the parameter set-up is to identify a patient’s current or prior history of ESBL based on laboratory reporting and the time frames that are entered to search for the patient’s status. This information can optionally be displayed on the Isolation Report. If you would like to incorporate ESBL into the Isolation report, the result must occur as a retrievable result as a “bacterial etiology” or in the “BACT RPT REMARK” field. It is appropriate to used Canned Comments versus Free Text to retrieve results. If free-text is used, it is likely the report will not display accurate information. Any results contained in the “Comments” section will not allow incorporation of ESBL into the MRSA Program Tools software Isolation Report format.

<span id="_Toc249158707" class="anchor"></span>Figure 22 – MRSA Tools Lab Parameter Display for MDRO

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: ESBL</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Selected Etiology will only be used for test results reported under Microbiology. Select from the ETIOLOGY FIELD file \#61.2.

<span id="_Toc249158708" class="anchor"></span>Figure 23 – MRSA Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: ESBL</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p><strong>ESCHERICHIA COLI</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After selecting the desired etiology, the user will be prompted to enter Antimicrobial Susceptibility for the organism and how to search for the result by entering information into the Indicator and Indicated Value fields.

<span id="_Toc249158709" class="anchor"></span>Figure 24 – MRSA Tools Parameter Setup for Antimicrobial Susceptibility

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: ESBL</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected</p>
<p>ESCHERICHIA COLI</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CEFPODOXIME Contains R</strong></td>
</tr>
</tbody>
</table>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></td>
</tr>
</tbody>
</table>

<span id="_Toc249158710" class="anchor"></span>Figure 25 – MRSA Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: ESBL</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p>ESCHERICHIA COLI</p>
<p><strong>KLEBSIELLA PNEUMONIAE</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/029.png) | Important Note: If multiple organisms and/or antimicrobial susceptibilities are needed for identification then each organism and/or antimicrobial susceptibility has to be added to the laboratory parameter setup. |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

After entering the required information for Microbiology subscripted tests, the user can go to the second page of the form to enter information concerning the Bacteriology Report Remarks. If the site reported positives by entering in certain comments under the BACT RPT REMARK fields, this option will allow the sites to enter those comments here. The form will also allow the user to exclude certain comments. The “exclude” functionality only needs to be used in cases where the phrase used to denote a positive result is also contained in the phrase used to denote a negative result. For example, the following two phrases could be used: “ESBL POSITIVE” for positive results and “NOT ESBL POSITIVE” for negative results. The program is looking for positive results. The user will want to *include the positiveandexclude the negative* test results. See below for example.

<span id="_Toc249158711" class="anchor"></span>Figure 26 – Bacteriology Report Remarks

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 2 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>________________________________________________________________________</p>
<p>BACTERIOLOGY REPORT REMARKS</p>
<p>Include Exclude</p>
<p><strong>ESBL POSITIVE NOT ESBL POSITIVE</strong></p>
<p>________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/030.png) | Important Note: Please be consistent with site specific data spelling or alternate spelling to ensure accurate data capture. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/031.png) | Important Note: If “BACT RPT REMARK” is used, it is important that a consistent method of reporting is used to identify results (*i.e.*, canned comments). If Free-Text is used, it is likely the report will not display accurate information. |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/032.png) | Important Note: Before exiting the menu, save changes. |
|----------------------------------------------------|------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/033.png) | Important Note: This is only a suggestion. Please add accordingly to your site definition. |
|----------------------------------------------------|------------------------------------------------------------------------------------------------|

<span id="AppD" class="anchor"></span>

APPENDIX C

# # Business Rules for Nares Screening (Examples)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user will need to define business rules for nares screening during the parameter setup. The following are several examples of business rules for nares screening.

Example: The facility has adopted the policy that on unit-to-unit transfers, only the receiving unit will obtain the nares screen (and not the discharging unit). In addition, patients with a known history of MRSA are screened on transfer and discharge. The user will define the parameters noted below for this example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MRSA Tools Parameter Setup (Main)</strong></p>
<p>Select MRSA SITE PARAMETERS DIVISION: <strong>XXXXX VAMC</strong></p>
<p>Are you adding ‘XXXXX VAMC’ as</p>
<p>a new MRSA SITE PARAMETERS (the 1ST)? No// <strong>Y</strong> (Yes)</p>
<p>1. Receiving unit screen on unit-to-unit transfers: <strong>YES</strong></p>
<p>2. Discharging unit screen on unit-to-unit transfers: <strong>NO</strong></p>
<p>3. Screen patients with MRSA history on transfer-in: <strong>YES</strong></p>
<p>4. Screen patients with MRSA history on discharge/death/transfer-out: <strong>YES</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: The facility has adopted the policy that on unit-to-unit transfers, only the receiving unit will obtain the nares screen (and not the discharging unit). In addition, patients with a known history of MRSA are *<u>not</u>* screened on transfer and discharge. The user will define the parameters noted below for this example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MRSA Tools Parameter Setup (Main)</strong></p>
<p>Select MRSA SITE PARAMETERS DIVISION: <strong>XXXXX VAMC</strong></p>
<p>Are you adding ‘XXXXX VAMC’ as</p>
<p>a new MRSA SITE PARAMETERS (the 1ST)? No// <strong>Y</strong> (Yes)</p>
<p>1. Receiving unit screen on unit-to-unit transfers: <strong>YES</strong></p>
<p>2. Discharging unit screen on unit-to-unit transfers: <strong>NO</strong></p>
<p>3. Screen patients with MRSA history on transfer-in: <strong>NO</strong></p>
<p>4. Screen patients with MRSA history on discharge/death/transfer-out: <strong>NO</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: The facility has adopted the policy that on unit-to-unit transfers, only the discharging unit will obtain the nares screen (and not the receiving unit). In addition, patients with a known history of MRSA are screened on transfer-outs and discharge. The user will define the parameters noted below for this example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MRSA Tools Parameter Setup (Main)</strong></p>
<p>Select MRSA SITE PARAMETERS DIVISION: <strong>XXXXX VAMC</strong></p>
<p>Are you adding ‘XXXXX VAMC’ as</p>
<p>a new MRSA SITE PARAMETERS (the 1ST)? No// <strong>Y</strong> (Yes)</p>
<p>1. Receiving unit screen on unit-to-unit transfers: <strong>NO</strong></p>
<p>2. Discharging unit screen on unit-to-unit transfers: <strong>YES</strong></p>
<p>3. Screen patients with MRSA history on transfer-in: <strong>NO</strong></p>
<p>4. Screen patients with MRSA history on discharge/death/transfer-out: <strong>YES</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example: The facility has adopted the policy that on unit-to-unit transfers, only the discharging unit will obtain the nares screen (and not the receiving unit). In addition, patients with a known history of MRSA are *<u>not</u>* screened on transfer and discharge. The user will define the parameters noted below for this example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Setup Menu Option: <strong>MRSA Tools Parameter Setup (Main)</strong></p>
<p>Select MRSA SITE PARAMETERS DIVISION: <strong>XXXXX VAMC</strong></p>
<p>Are you adding ‘XXXXX VAMC’ as</p>
<p>a new MRSA SITE PARAMETERS (the 1ST)? No// <strong>Y</strong> (Yes)</p>
<p>1. Receiving unit screen on unit-to-unit transfers: <strong>NO</strong></p>
<p>2. Discharging unit screen on unit-to-unit transfers: <strong>YES</strong></p>
<p>3. Screen patients with MRSA history on transfer-in: <strong>NO</strong></p>
<p>4. Screen patients with MRSA history on discharge/death/transfer-out: <strong>NO</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc268767734" class="anchor"></span>APPENDIX D

# # Schedule TaskMan Tasks (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the clinical staff wants to schedule the Isolation Report and Nares Compliance List to automatically print to designated printers at specified times during the day, schedule these tasks in TaskMan.

#### Print Isolation Report (Tasked)

This option should *not* be run interactively. It should only be scheduled by IRM staff to run via TaskMan using option Schedule/Unschedule Options \[XUTM SCHEDULE\]. This option will print the Isolation Report at the times specified.

<span id="_Toc268767773" class="anchor"></span>Figure 27 – Print Isolation Report (Tasked)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select TaskMan Management Option: <strong>Schedule/Unschedule Options</strong></p>
<p>Select OPTION to schedule or reschedule: <strong>"MMRS ISOLATION REPORT (TASKED)"</strong></p>
<p>Are you adding 'MMRS ISOLATION REPORT (TASKED)' as</p>
<p>a new OPTION SCHEDULING (the 329TH)? No// <strong>Y</strong> (Yes)</p>
<p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED</p>
<p>Menu Text: Print Isolation Report (Tasked) TASK ID:</p>
<p>_______________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: <strong>MAR 5,2009@15:50</strong></p>
<p>DEVICE FOR QUEUED JOB OUTPUT: <strong>IDM1$PRT LANDSCAPE;P-TCP LANDS</strong></p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 12H</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule/Unschedule Options \[XUTM SCHEDULE\], several variables need to be setup on page 2 of the form.

- The Variable Name MMRSDIV should be added, and its value should be set to the IEN in File \#104 for the Division this option is being run for.
- If the option will print the report for all locations, then MMRSLOC should be added as a Variable Name and its Value should be set to "ALL" (The quotes need to be entered in the Value). If the option will only print for a few locations, then for each location that will be printed, a Variable Name should be added as follows: MMRSLOC(LOCIEN), where LOCIEN is the geographical unit IEN from File \#104.3), and its value should be set to "" (the two double quotes need to be entered for the Value; do not leave the Value blank).

A sample screen shot on how to get the IEN for a Division follows (Figure 28). The number highlighted in yellow is the IEN.

<span id="_Ref266977107" class="anchor"></span>Figure 28 – Get MRSA Division IEN

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: MRSA SITE PARAMETERS

Select MRSA SITE PARAMETERS DIVISION: XXXXX VAMC

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// Record Number (IEN)

<span class="mark">NUMBER: 1</span> DIVISION: XXXXX VAMC

RECEIVING UNIT SCREEN: YES DISCHARGING UNIT SCREEN: YES

SCREEN POS ON TRANSFER IN: YES SCREEN POS ON DISCHARGE: YES

A sample screen shot on how to get the IEN for a Geographical Location follows (Figure 29). The number highlighted in yellow is the IEN.

<span id="_Ref266977171" class="anchor"></span>Figure 29 – Get Geographical Location IEN

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: MRSA WARD MAPPINGS

Select MRSA WARD MAPPINGS NAME: 11AB

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// Record Number (IEN)

<span class="mark">NUMBER: 5</span> NAME: 11AB

DIVISION: XXXXX VAMC TYPE: ACUTE CARE

IPEC UNIT ID: 726

WARD LOCATION: 11AB

WARD LOCATION: 11ASURG

A sample screen shot for running the option for Division 1, and geographical locations 3 and 5 is shown in Figure 30.

<span id="_Ref266977231" class="anchor"></span>Figure 30 – Print Isolation Report (Tasked) (Division 1 & Geographical Locations 3 & 5)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED)</p>
<p>______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC(3) VALUE: ""</p>
<p>VARIABLE NAME: MMRSLOC(5) VALUE: ""</p>
<p>VARIABLE NAME: VALUE:</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Sample screen shot for running the option for Division 1 and all Geographical Locations is shown in Figure 31.

<span id="_Ref266977277" class="anchor"></span>Figure 31 – Print Isolation Report (Tasked) (Division 1 & All Geographical Locations)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED)</p>
<p>______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC VALUE: "ALL"</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>­­­­­­­­­­­­­­­­­­­_________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/034.png) | Tip: To schedule the option more than once (for example, if the site wants to schedule the report to print at different printers for different locations), put the option name in quotes. This will allow you to schedule the option more than once. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/035.png) | Tip: When tasking options, ALL has to be in quotations (“ALL”). |
|----------------------------------------------------|---------------------------------------------------------------------|

#### Print Nares Screen Compliance List (Tasked)

This option should *not* be run interactively. It should only be scheduled by IRM staff to run via TaskMan using option 'Schedule/Unschedule Options' \[XUTM SCHEDULE\]. This option will print the Nares Compliance List at the times specified.

<span id="_Toc268767778" class="anchor"></span>Figure 32 – Print Nares Screen Compliance List (Tasked)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select TaskMan Management Option: <strong>Schedule/Unschedule Options</strong></p>
<p>Select OPTION to schedule or reschedule: <strong>“MMRS NARES SWAB LIST (TASKED)”</strong></p>
<p>Are you adding ‘MMRS NARES SWAB LIST (TASKED)’ as</p>
<p>a new OPTION SCHEDULING (the 329TH)? No// <strong>Y</strong> (Yes)</p>
<p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED</p>
<p>Menu Text: Print Nares Screen Compliance List (Tasked) TASK ID:</p>
<p>_______________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: MAR 5,2009@15:50</p>
<p>DEVICE FOR QUEUED JOB OUTPUT: IDM1$PRT LANDSCAPE;P-TCP LANDS</p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 12H</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule/Unschedule Options \[XUTM SCHEDULE\], several variables need to be setup on Page 2 of the form.

- The Variable Name MMRSDIV should be added, and its value should be set to the IEN in File \#104 for the Division this option is being run for.
- If the option will print the report for all locations, then MMRSLOC should be added as a Variable Name and its Value should be set to ALL. If the option will only print for a few locations, then for each location that will be printed, a Variable Name should be added as follows: MMRSLOC(LOCIEN) (where LOCIEN is the geographical unit IEN from File \#104.3) and its Value should be set to "" (the two double quotes need to be entered for the Value; do not leave the Value blank).

Sample screen shot for running the option for Division 1, and geographical locations 3 and 5.

<span id="_Toc268767779" class="anchor"></span>Figure 33 – Print Nares Swab List (Tasked) (Div 1 & Geographical Locations 3 & 5)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC(3) VALUE: ""</p>
<p>VARIABLE NAME: MMRSLOC(5) VALUE: ""</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Sample screen shot for running the option for Division 1 and all Geographical Locations.

<span id="_Toc268767780" class="anchor"></span>Figure 34 – Print Nares Swab List (Tasked) (Div 1 & All Geographical Locations)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC VALUE: "ALL"</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ![](mrsa-program-tools-version-1-installation-manual/036.png) | Tip: To schedule the option more than once (for example, if the site wants to schedule the report to print at different printers for different locations), put the option name in quotes. This will allow you to schedule the option more than once. |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](mrsa-program-tools-version-1-installation-manual/037.png) | Tip: When tasking options, ALL has to be in quotations (“ALL”). |
|----------------------------------------------------|---------------------------------------------------------------------|

<span id="_Toc249158660" class="anchor"></span>APPENDIX E

# # Test Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test scripts were used by the beta sites to validate data generated by the reports. Facilities may find the test scripts useful to validate reports generated by the MRSA-PT software.

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 46%" />
<col style="width: 9%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Test Scenarios</th>
<th><p>Date</p>
<p>Tested</p></th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">Note: Test the implementation instructions for site implementation type</td>
</tr>
<tr class="even">
<td>1</td>
<td>In a test account, did the program install without impacting other VistA applications?</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Compare the MRSA IPEC Report generated by the MRSA Program Tools software to your current reports. Were there any differences between the two reports? If so what were the differences?</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>3</td>
<td>Run the “Admission Report” for the month of August for an ICU, non-ICU and CLC unit. Did the report accurately report the IPEC data elements?</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>4</td>
<td>Run the “Discharge/Transmission Report” for the month of August for an ICU, non-ICU and CLC unit. Did the report accurately report the IPEC data elements?</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>5</td>
<td>Run the “Admission Report” for the month of August for the Facility. Did the report accurately report the IPEC data elements?</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6</td>
<td>On a production account, identify 5 acute care inpatient admissions that was admitted, transferred and discharged. (The 5 patients should have different types of movements.) Review the patient’s medical record to see the results of the nares screen and the patient’s MRSA status in the past 12 months. Did the report the program generated accurately pick up the admission, transfer and discharge? Did the report display the correct movement for the patient? Did it provide the correct information for that patient? Please review at least one ASIH movement to review the data is captured accurately between CLC and acute care (discharge and admission, opposed to transfer).</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>7</td>
<td>On a production account, identify 5 CLC admissions that was admitted, transferred and discharged. (The 5 patients should have different types of movements.) Review the patient’s medical record to see the results of the nares screen and the patient’s MRSA status in the past 12 months. Did the report the program generated accurately pick up the admission, transfer and discharge? Did the report display the correct movement for the patient? Did it provide the correct information for that patient? Please review at least one ASIH movement to review the data is captured accurately between CLC and acute care (discharge and admission, opposed to transfer).</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>8</td>
<td>On a production account, identify an acute care inpatient admission that had multiple admissions to the unit for the calendar month. Did the reports for the units the patient was admitted and transfer to show the appropriate movements for the patient? Did the report show the patient’s MRSA results accurately for this admission? Previous history?</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>On a production account, identify an acute care inpatient admission that was admitted to acute care from the CLC and then discharged back to the CLC for the month of August – this patient was discharged from the CLC, admitted to acute care and then discharged back to the CLC for the month of June. Did the program display the following movements: discharge from CLC, admission to acute care, discharge from acute care and admission to CLC?</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>10</td>
<td>On a production account, identify an acute care inpatient admission that had a positive nares screen <strong>and</strong> positive clinical culture upon admission. Did the clinical culture get reported in the IPEC report? Did the report accurately not count the positive nares screen?</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>On a production account, identify an acute care inpatient admission that met the criteria for a transmission through positive nares screen on transfer/discharge. Did the transmission get reported? Was the transmission assigned to the correct unit for the patient?</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>12</td>
<td>On a production account, identify an acute care inpatient admission that met the criteria for a transmission through positive clinical culture. Did the transmission get reported? Was the transmission assigned to the correct unit for the patient?</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>13</td>
<td>On a production account, identify a CLC admission that met the criteria for a transmission through positive nares screen on transfer/discharge. Did the transmission get reported? Was the transmission assigned to the correct unit for the patient?</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>14</td>
<td>On a production account, identify a CLC admission that met the criteria for a transmission through positive clinical culture. Did the transmission get reported? Was the transmission assigned to the correct unit for the patient?</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>15</td>
<td>On a production account, identify an acute care inpatient admission that has a MRSA positive status and another positive MDRO (that was added in the parameters). Did the Isolation Report display both the positive MRSA and the other positive MDRO, according to the parameters entered?</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>If your facility uses Isolation Orders complete the following: On a production account, identify an acute care inpatient admission that is on Contact Precautions. Did the Isolation Report generate this order on the report? Did the report generate the correct start date for the Isolation Order?</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>17</td>
<td>If your facility uses Isolation Orders complete the following: On a production account, identify an acute care inpatient admission that has more than one active isolation order. Did the report generate the correct start date for the Isolation Orders? Did the patient appear on the report multiple times, dependent on the number of active isolation orders for the patient?</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>18</td>
<td>On a production account, verify the Nares Compliance report for an ICU, non-ICU, OBS and CLC unit for a specific day. Did the report generate all patient movements into the unit correctly (Admission or Transfer)? Did the report identify the patient’s MRSA history in the past 12 months correctly? Did the report generate if a nares screen was ordered and the order date/time correctly? Did the report display correctly if the nares screen was received in the lab?</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>19</td>
<td>On a production account, verify that a pending bacteriology report for Culture &amp; Susceptibility (C&amp;S) is picked up on the Isolation Report.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>20</td>
<td>Contact the Emerging Pathogens Initiative (EPI) POC, and ask them to verify the EPI report for the month of August. Is the report that was submitted to Austin accurate?</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc266960404" class="anchor"></span>APPENDIX F

# # Laboratory Reporting of MRSA Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Each VA facility is to implement the following test names and laboratory reporting for MRSA tests. This standardization allows for national collection of data on MRSA nares screening and culture-positive results. VHA Laboratory Services must record results of MRSA Tests performed within a VA laboratory using the following methodology:
1.  MI-subscripted tests will be used for clinical culture based tests; A clinical culture is ordered by the provider for clinical reasons (e.g., patient is sick, presents clinical symptoms) to determine if a pathogenic organism is present and the appropriate antibiotics for treatment.
2.  CH-subscripted tests will be used for nares screening or other types of surveillance screening because they have limited defined values. Surveillance cultures are used to establish prevalence, or monitor and control a situation (i.e., identification of asymptomatic individuals or carriers).
2.  Implementation Notes
    1.  MI-Subscripted Tests:
        1.  <u>ONLY</u> clinical cultures (C&S) will be reported using MI-subscript.
        2.  STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) is the <u>only</u> etiology that will be used to report positive clinical cultures.
        3.  Emerging Pathogens Initiative (EPI) will use the etiology listed above for its data pull.
    2.  CH-Subscripted Tests:
        1.  MRSA nares screens or MRSA surveillance cultures (e.g., perineum, axilla, etc.) will be reported using CH-subscript.
        2.  The following Test Names and Logical Observation Identifiers Names & Codes (LOINC) will be used:
            1.  MRSA SURVL NARES DNA
                1.  35492-8 MRSA DNA XXX Q1 PCR, Staphylococcus aureus.methicillin resistant DNA
                2.  SITE/SPECIMEN is limited to “Nares”; no other SITE/SPECIMEN can be used with this test name
            2.  MRSA SURVL OTHER DNA
                1.  35492-8 MRSA DNA XXX Q1 PCR, Staphylococcus aureus.methicillin resistant DNA
                2.  Test is for MRSA Surveillance Screening other than “Nares”. SITE/SPECIMEN could be “Axilla” or “Perineum” or other surveillance testing done locally.
            3.  MRSA SURVL NARES AGAR
                1.  13317-3 MRSA XXX Q1 Cult, Staphylococcus aureus.methicillin resistant isolate
                2.  52969-3\* MRSA Nose Q1 Cult, Staphylococcus aureus.methicillin resistant isolate (*\*will be available when File 95.3 is updated; until then 13317-3 is to be used*)
                3.  SITE/SPECIMEN is limited to “Nares”; no other SITE/SPECIMEN can be used with this test name
            4.  MRSA SURVL OTHER AGAR
                1.  13317-3 MRSA XXX Q1 Cult, Staphylococcus aureus.methicillin resistant isolate
                2.  Test is for MRSA Surveillance Screening other than “Nares”. SITE/SPECIMEN could be “Axilla” or “Perineum” or other surveillance testing done locally.
        3.  For integrated or co-located sites that need to offer site/division specific tests, the test name has to start with “MRSA SURVL NARES DNA” (or any other standard test name listed above) and modifiers are added at the end of the name. For example, MRSA SURVL NARES DNA Site 1 and MRSA SURVL NARES DNA Site 2, etc.
        4.  To standardize data entry format, when the Data name is created for each test the CH-subscript test input transform needs to be Set of Codes:

> Negative is to Negative

> POSITIVE is to POSITIVE

> Invalid is to Invalid Inhibitors Present.

> *NOTE:Positive is intentionally in uppercase for impact.*

1.  Enter data type of MRSA SURVL NARES DNA: (N)umeric, (S)et of Codes, or (F)ree text ? S
    1.  INTERNALLY-STORED CODE://Negative WILL STAND FOR:// Negative
    2.  INTERNALLY-STORED CODE://POSITIVE WILL STAND FOR:// POSITIVE
    3.  INTERNALLY-STORED CODE://Invalid WILL STAND FOR:// Invalid Inhibitors Present
2.  Enter data type of MRSA SURVL NARES AGAR: (N)umeric, (S)et of Codes, or (F)ree text ? S
1.  INTERNALLY-STORED CODE://Negative WILL STAND FOR:// Negative
2.  INTERNALLY-STORED CODE://POSITIVE WILL STAND FOR:// POSITIVE
3.  Enter data type of MRSA SURVL OTHER DNA: (N)umeric, (S)et of Codes, or (F)ree text ? S
    1.  INTERNALLY-STORED CODE://Negative WILL STAND FOR:// Negative
    2.  INTERNALLY-STORED CODE://POSITIVE WILL STAND FOR:// POSITIVE
    3.  INTERNALLY-STORED CODE://Invalid WILL STAND FOR:// Invalid Inhibitors Present
4.  Enter data type of MRSA SURVL OTHER AGAR: (N)umeric, (S)et of Codes, or (F)ree text? S
    1.  INTERNALLY-STORED CODE://Negative WILL STAND FOR:// Negative
    2.  INTERNALLY-STORED CODE://POSITIVE WILL STAND FOR:// POSITIVE
5.  To standardize the interpretation of the test result, VHA Laboratory Services will need to add a “Comment” to each invalid PCR test result. This is a new entry in the Lab Description File (File 62.5).
    1.  NAME: MRSAIR
        1.  Expansion: Inhibitors Present, Please Repeat
    2.  NAME: MRSAIC
        1.  Expansion: Inhibitors Present, Culture Is Being Performed
        2.  NOTE: This comment should be used if the first swab is invalid and the laboratory uses agar to process the second swab.
6.  The results must be documented under a specifically created MRSA Section of Laboratory Results display in Computerized Patient Record System (CPRS) Graphic User Interface (GUI). The report sections must be set up in the Lab Reports File (File 64.5) under the Cumulative Report name.
    1.  VistA GUI Cumulative View will need to be set-up for Horizontal Format reporting to ensure that test results will be easily accessible.
    2.  At least one Major Header will need to be created. To ensure that all test results are displayed appropriately, it is important to work with Infection Control to ascertain if MRSA screens are performed for sites other than the Nares. In this display format, Minor headers will need to be created for each specimen type and test type to display all of the appropriate tests by specimen type (Nares, Perineum, Axilla, etc.) and to ensure the results are displayed legibly.
    3.  Only the Minor Headers show in the CPRS Cumulative View but they are grouped together by the Major Header.
    4.  Sample Major Header: SURVEILLANCE TESTING
    5.  Sample Minor Headers appear below:
        1.  MRSA Surveillance DNA Nares
        2.  MRSA Surveillance DNA Axilla
        3.  MRSA Surveillance DNA Perineum
        4.  MRSA Surveillance AGAR Nares
        5.  MRSA Surveillance AGAR Axilla
        6.  MRSA Surveillance AGAR Perineum

> etc.....

> *\*NOTE: In the Horizontal format the Major header does not need to be specific to DNA or Agar based CH-subscripted tests. A combined major header like the Surveillance Testing Header suggested can be created. However, for the Minor headers it is recommended that separate Minor headers be created for each SITE/SPECIMEN and TEST type (DNA and Agar based CH-subscripted test otherwise the results display will suffer in the horizontal format recommended.*

> NOTE: The previous laboratory test names can be updated for the new test names. However, certain cross-references need to be updated and there can be issues for data objects in CPRS; coordination is required. A new test should be created <u>only</u> if the original test and the new test are vastly different (i.e., methodology is different, new reference ranges that are clinically significant, etc.).

3.  Critical View Alert: A delta check can be created to provide a mechanism to alert providers if a patient is MRSA positive. When the test is resulted as POSITIVE it will set the flag to a CRITICAL high to generate a View Alert to the provider. The test must be set up as a Set of Codes with POSITIVE stands for POSITIVE to ensure consistency of reporting and flagging. If sites need to generate a Critical View Alert the following Delta Check can be created in File 62.1. It will then need to be added to the File 60 test set up in the Site/Specimen (field 100) multiple subfield 7, Type of Delta Check. This mechanism is case-sensitive so the Set of Codes (POSITIVE) and the Delta check (POSITIVE) should match if this specific coding is utilized.

> NAME: TEXT ALERT POS \*H

> XECUTABLE CODE: Q:\$D(LRGVP) I X\["POSITIVE" S LRFLG="H\*"

4.  Laboratory Management Index Program (LMIP): MRSA Surveillance testing is countable (billable) for the LMIP program. The National Laboratory Test (NLT) code chosen is based on the methodology used to perform the test at the site and must be marked billable in File 64 for workload recording purposes. Since method specific NLT codes are not available in File 64 for MRSA then the following NLT codes will need to be created by adding a method specific suffix from the WKLD Suffix codes file (File 64.2) to the WKLD Code file (File 64) NLT code, based on the methodology used to perform the test at the site. Create the suffixed workload code necessary using "Add a new WKLD code to file \[LRCAP CODE ADD\]". The recommended suffixed NLT codes for MRSA are as follows:
    1.  Staphylococcus Aureus Meth Resist~ORGANISM SPECIFIC CULTURE 87293.7059 for CH-subscripted “Agar” based culture tests.
    2.  Staphylococcus Aureus Meth Resist~PCR 87293.4451 for CH-subscripted “DNA” based tests.
    3.  For MI-Subscripted culture tests that have an MRSA organism identified and a sensitivity performed will require both the Etiology and Sensitivity LMIP NLT workload codes added to the Etiology Field organism entry: STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) referred to in section a.ii MI-subscripted tests.

> ETIOLOGY WKLD CODE: Sensitivity Testing or MIC

> ETIOLOGY WKLD CODE \#: 87954.0000

> ETIOLOGY WKLD CODE: Bacti Organism ID

> ETIOLOGY WKLD CODE \#: 87570.0000

> *\*NOTE:* See example in Sectionf. Organisms in the Etiology Field File. These codes may need to be suffixed with the methodology used if applicable.

5.  Current Procedural Terminology (CPT): At this point in time, MRSA surveillance tests are not usually billable to a third party payer for reimbursement (versus a normal culture test or PCR test not used for MRSA surveillance which are billable). Therefore, these MRSA surveillance tests should not be passing CPT codes to the Patient Care Encounter (PCE) application.

> *\*NOTE: Refer to the Additional Notes section under LEDI and HDR for related information if your site sends this testing to a reference lab.*

6.  Organisms in the Etiology Field File: The following etiology will have to be added to the Etiology Field File (File 61.2), if this separate organism is not currently in the file. The following SNOMED CT code needs to be used when SNOMED CT coding is available in the VISTA system (Lab patches LA\*5.2\*68, LR\*5.2\*350, and LA\*5.2\*74).

NAME: STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)SNOMED CODE: *(Local entry code in the format \###XXX where \### is the station ID and XXX is the next local code suffix available: example: 523001)*

GRAM STAIN: GRAM POSITIVE IDENTIFIER: BACTERIUM

ABBREVIATION: MRSA

\*SENSITIVITY DISPLAY

HEALTH DATA REPORT: YES

SNOMED CT ID: 115329001 *(Methicillin resistant Staphylococcus aureus (organism) specific SCT code)*

SCT CODE STATUS: PREFERRED TERM

SCT TOP CONCEPT: SCT Organism

Example:

> NAME: STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)

> SNOMED CODE: 523700 GRAM STAIN: GRAM POSITIVE

> IDENTIFIER: BACTERIUM ABBREVIATION: MRSA

> HEALTH DEPT REPORT: YES

> SYNONYM: METHICILLIN RESISTANT STAPH AUREUS

> SYNONYM: MRSA

> ETIOLOGY WKLD CODE: Sensitivity Testing or MIC

> ETIOLOGY WKLD CODE \#: 87954.0000

> ETIOLOGY WKLD CODE: Bacti Organism ID

> ETIOLOGY WKLD CODE \#: 87570.0000

> SNOMED CT ID: 115329001

> SCT CODE STATUS: PREFERRED TERM

> SCT TOP CONCEPT: SCT Organism

> NOTE: Sites should not change the existing Etiology field entries <u>unless</u> the previous etiology and the new standardized etiology are synonymous. For example, a site used the etiology “Meth Res Staph Aureus” for positive MRSA. It would be appropriate to update the field entry to “STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)” since they are considered the same organism. Sites can add “Meth Res Staph Aureus” as a synonym for historical look back. This is only appropriate if the etiology previously used was to denote MRSA.

> If the site used the etiology “Staphylococcus Aureus” and set the Antimicrobial Susceptibility resistant to Oxacillin then it would not be appropriate to modify the existing Etiology field entry. Sites will have to add the etiology “STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)” to File 61.2

3.  Additional Notes for Sites:
    1.  Lab Electronic Data Interchange (LEDI) and Health Data Repository (HDR):

> Tests require National VA Lab codes for the HDR (the CH-subscripted tests need this information) and if LEDI is used by a site and they send their testing to another lab then the tests need National VA Lab codes as Order NLT codes and Result NLT codes as Result codes.  So there is an issue that it would be good to have National codes assigned to tests BUT the lab shouldn't pass CPT codes for surveillance issues.  Since the National VA Lab code field is one of the mechanisms the lab uses to pass CPT coding to PCE this needs to be considered. The way to handle this is to leave the field blank if LEDI is not an issue or have a generic NLT code that doesn’t carry any CPT code in it and/or remove the CPT code if one is there.  This is not a critical issue at this point as long as these tests are not passing CPT codes to billing. So sites may need to address this issue at some point for LEDI issues and HDR issues. This is more important in CH-subscripted tests at the moment but with LEDI IV (Patches LR\*5.2\*350 and LA\*5.2\*74) Micro tests will be passing info across LEDI so it will be more important in the near future.

2.  EPI, LOINC, and LEDI TOPOGRAPHY FILE 61 set-up issue:

> EPI, LOINC, and LEDI all use topography file information. The topography file entry is the SITE/SPECIMEN associated with a file 60 test. Two fields in the topography entries should be mapped to avoid errors for EPI and LEDI. LOINC mapping requires these as well, they are the HL7 CODE and the LEDI HL7 CODE fields in FILE 61. If the specimen code is missing in any topography reported in the EPI a W07 error is generated. These W07 errors usually occur in culture test site specimens that weren’t mapped. All possible topographies that could be used by a site for the MRSA testing should be mapped for these two fields. The following are examples of topographies that sites may use but this is applicable for ALL topographies that are used for any MI-Culture based tests or CH-subscripted tests that are captured in EPI, have LOINC codes, and/or are available for LEDI testing in a site. If “NARES” is not an option in the Topography file then the site will have to create a new entry for the SITE/SPECIMEN. See example below for new entries in the Topography file.

Examples:

> NAME: NARESSNOMED CODE: *(Local entry code in the format \###XXX where \### is the station ID and XXX is the next local code suffix available: example: 523001)*

> HL7 CODE: ORH LEDI HL7: Nose (nasal passage)

> SNOMED CT ID: 363538002

> SCT CODE STATUS: LOCAL

> SCT TOP CONCEPT: SCT Body Structure

NAME: AXILLA SNOMED CODE: Y8100

WEIGH: YES

HL7 CODE: ORH LEDI HL7: Other

SYNONYM: AXI

SNOMED CT ID: 34797008 SCT CODE STATUS: SYNONYM

SCT TOP CONCEPT: SCT Body Structure

NAME: PERINEUM SNOMED CODE: Y1700

HL7 CODE: ORH LEDI HL7: Other

SYNONYM: PERI

SNOMED CT ID: 38864007 SCT CODE STATUS: SYNONYM

SCT TOP CONCEPT: SCT Body Structure

<span id="_Toc232405454" class="anchor"></span>GLOSSARY

[![](mrsa-program-tools-version-1-installation-manual/038.png)](\l) [![](mrsa-program-tools-version-1-installation-manual/039.png)](#G_B) [![](mrsa-program-tools-version-1-installation-manual/040.png)](#G_C) [![](mrsa-program-tools-version-1-installation-manual/041.png)](#G_D) [![](mrsa-program-tools-version-1-installation-manual/042.png)](#G_E) [![](mrsa-program-tools-version-1-installation-manual/043.png)](#G_F) [![](mrsa-program-tools-version-1-installation-manual/044.png)](#G_G) [![](mrsa-program-tools-version-1-installation-manual/045.png)](#G_I) [![](mrsa-program-tools-version-1-installation-manual/046.png)](#G_K) [![](mrsa-program-tools-version-1-installation-manual/047.png)](#G_L) [![](mrsa-program-tools-version-1-installation-manual/048.png)](#G_M) [![](mrsa-program-tools-version-1-installation-manual/049.png)](#G_N) [![](mrsa-program-tools-version-1-installation-manual/050.png)](#G_P) [![](mrsa-program-tools-version-1-installation-manual/051.png)](#G_S) [![](mrsa-program-tools-version-1-installation-manual/052.png)](#G_T) [![](mrsa-program-tools-version-1-installation-manual/053.png)](#G_V) [![](mrsa-program-tools-version-1-installation-manual/054.png)](#G_W)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Term or Acronym</th>
<th colspan="3">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"></td>
<td><strong>A</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/055.png)</a></td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td colspan="3"><em>See</em> <a href="#Glos_ADPAC">Automated Data Processing Application Coordinator</a></td>
</tr>
<tr class="odd">
<td>ANTIMICROBIAL SUSCEPTIBILITY file #62.6</td>
<td colspan="3">Antimicrobial used to determine sensitive/resistant <a href="#Glos_etiology">etiologies</a>.</td>
</tr>
<tr class="even">
<td><span id="Glos_ADPAC" class="anchor"></span>Automated Data Processing Application Coordinator (ADPAC)</td>
<td colspan="3">The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or <a href="#Glos_IRM">Information Resource Management</a> (IRM). Also, the designated individual responsible for user-level management and maintenance of an application package (<em>e.g.</em>, Laboratory).</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_B" class="anchor"></span><strong>B</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/056.png)</a></td>
</tr>
<tr class="even">
<td>Begin Date/Time</td>
<td colspan="3">The date that the report is to start.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_C" class="anchor"></span><strong>C</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/057.png)</a></td>
</tr>
<tr class="even">
<td>CLC</td>
<td colspan="3"><em>See</em> <a href="#Glos_CLC">Community Living Center</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_ClientServer" class="anchor"></span>Client-server</td>
<td colspan="3">A common form of distributed system in which software is split between server tasks and client tasks. A client sends requests to a server, according to some protocol, asking for information or action, and the server responds. This is analogous to a customer (client) who sends an order (request) on an order form to a supplier (server) who dispatches the goods and an invoice (response). The order form and invoice are part of the “protocol” used to communicate in this case.</td>
</tr>
<tr class="even">
<td><span id="Glos_CLC" class="anchor"></span>Community Living Center (CLC)</td>
<td colspan="3"><p>A CLC provides a dynamic array of services in person-centered environments that meet the individual needs of residents, providing excellent health care and quality of life.</p>
<p><em>Formerly known as</em> VA Nursing Home Care Units (NHCU).</p></td>
</tr>
<tr class="odd">
<td><span id="Glos_CPRS" class="anchor"></span>Computerized Patient Record System (CPRS)</td>
<td colspan="3">A Computerized Patient Record (CPR) is a comprehensive database system used to store and access patients’ healthcare information. CPRS is the Department of Veteran’s Affairs electronic health record software. The CPRS organizes and presents all relevant data on a patient in a way that directly supports clinical decision making. This data includes medical history and conditions, problems and diagnoses, diagnostic and therapeutic procedures and interventions. Both a graphic user interface version and a character-based interface version are available. CPRS provides a single interface for health care providers to review and update a patient’s medical record, and to place orders, including medications, special procedures, x-rays, patient care nursing orders, diets, and laboratory tests. CPRS is flexible enough to be implemented in a wide variety of settings for a broad spectrum of health care workers, and provides a consistent, event-driven, Windows-style interface.</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td colspan="3"><em>See</em> <a href="#Glos_CPRS">Computerized Patient Record System</a></td>
</tr>
<tr class="odd">
<td>CPT</td>
<td colspan="3"><em>See</em> <a href="#Glos_CPT">Current Procedural Terminology</a></td>
</tr>
<tr class="even">
<td><span id="Glos_CPT" class="anchor"></span>Current Procedural Terminology (CPT)</td>
<td colspan="3"><p>CPT® is the most widely accepted medical nomenclature used to report medical procedures and services under public and private health insurance programs. CPT codes describe a procedure or service identified with a five-digit CPT code and descriptor nomenclature. The CPT code set accurately describes medical, surgical, and diagnostic services and is designed to communicate uniform information about medical services and procedures among physicians, coders, patients, accreditation organizations, and payers for administrative, financial, and analytical purposes. The current version is the CPT 2009.</p>
<p><em>Note:</em> CPT® is a registered trademark of the American Medical Association.</p>
<p><em>See also</em> <a href="#Glos_ICD9">ICD-9</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_D" class="anchor"></span><strong>D</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/058.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_DBIA" class="anchor"></span>Database Integration Agreement (DBIA)</td>
<td colspan="3">A formal understanding between two or more application packages which describes how data is shared or how packages interact. This agreement maintains information between package Developers, allowing the use of internal entry points or other package-specific features.</td>
</tr>
<tr class="odd">
<td>DBIA</td>
<td colspan="3">See <a href="#Glos_DBIA">Database Integration Agreement</a></td>
</tr>
<tr class="even">
<td><span id="Glos_Domicilliary" class="anchor"></span>Domiciliary</td>
<td colspan="3">The VHA Domiciliary Residential Rehabilitation and Treatment program provides coordinated, integrated rehabilitative and restorative clinical care in a bed-based program, with the goal of helping eligible veterans achieve and maintain the highest level of functioning and independence possible. Domiciliary Care, as an integral component of VHA's continuum of health care services, is committed to providing the highest quality of clinical care in a coordinated, integrated fashion within that continuum.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_E" class="anchor"></span><strong>E</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/059.png)</a></td>
</tr>
<tr class="even">
<td>End Date/Time</td>
<td colspan="3">The date the report is to stop.</td>
</tr>
<tr class="odd">
<td><span id="Glos_etiology" class="anchor"></span>Etiology</td>
<td colspan="3">The cause or causes of a disease or abnormal condition; also, a branch of medical science dealing with the causes and origin of diseases.</td>
</tr>
<tr class="even">
<td>ETIOLOGY FIELD file #61.2</td>
<td colspan="3">This file is used to select the etiology/organism.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_F" class="anchor"></span><strong>F</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/060.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_FileMan" class="anchor"></span>FileMan</td>
<td colspan="3"><p>FileMan is a set of <a href="#Glos_M">M</a> utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p></td>
</tr>
<tr class="odd">
<td><span id="Glos_FTP" class="anchor"></span>File Transfer Protocol (FTP)</td>
<td colspan="3">A <a href="#Glos_ClientServer">client-server</a> protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in <a href="http://www.ietf.org/rfc/rfc959.txt">Internet Standard 9, Request for Comments 959</a>.</td>
</tr>
<tr class="even">
<td><span id="Glos_FreeTextField" class="anchor"></span>FREE TEXT field</td>
<td colspan="3"><p>You can enter almost any character from your keyboard in a FREE TEXT-type field. The program will accept numbers, letters, and most of the symbols that can be entered. The FREE TEXT field places a restriction on the number of characters that you can enter. If you enter a question mark ("<strong>?</strong>") in response to the prompt for a FREE TEXT field, you'll learn how many characters you are allowed to enter.</p>
<p>For example, a FREE TEXT field would probably be used to hold a patient's street address:</p>
<p>ADDRESS: <strong>235 Begonia Street</strong></p>
<p>In some places, even though the field is FREE TEXT, checks are applied to make sure what is entered matches a certain format. For example, if you're entering a Social Security Number (which is stored as a FREE TEXT, not NUMERIC, field), your input would typically be checked to make sure it is nine characters in length, and contains all digits:</p></td>
</tr>
<tr class="odd">
<td>FTP</td>
<td colspan="3"><em>See</em> <a href="#Glos_FTP">File Transfer Protocol</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_G" class="anchor"></span><strong>G</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/061.png)</a></td>
</tr>
<tr class="odd">
<td>Geographical Unit</td>
<td colspan="3">A field in the <a href="#Glos_Ward_Mapping">Ward Mapping</a> setup file used to assign an arbitrary name to a group of units (wards) to run the reports.</td>
</tr>
<tr class="even">
<td><span id="Glos_Global" class="anchor"></span>Global</td>
<td colspan="3"><p><a href="#Glos_M">M</a> uses <em>globals</em>: variables which are intrinsically stored in files and which persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the M statement…</p>
<p><strong>SET ^A(“first_name”)=”Bob”</strong></p>
<p>…will result in a new record being created and inserted in the persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as M globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of M is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>For all of these reasons, one of the most common M programs is a database management system. <a href="#Glos_FileMan">FileMan</a> is one such example. M allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_I" class="anchor"></span><strong>I</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/062.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_ICD9" class="anchor"></span>ICD-9</td>
<td colspan="3"><p><em>International Statistical Classification of Diseases and Related Health Problems</em>, ninth edition (commonly abbreviated as “ICD-9”) provides numeric codes to classify diseases and a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances and external causes of injury or disease. Every health condition can be assigned to a unique category and given a code, up to six characters long. Such categories can include a set of similar diseases. The “9” refers to the ninth edition of these codes; the tenth edition has been published, and VA expects to begin using ICD-10 in the future. On January 15, 2009, the U.S. Department of Health and Human Services (HHS) published a final rule establishing ICD-10 as the new national coding standard. The implementation date, initially proposed for October 2011, has been set for October 1, 2013.</p>
<p><em>See also</em> <a href="#Glos_CPT">Current Procedural Terminology</a></p></td>
</tr>
<tr class="odd">
<td>Indicated Value</td>
<td colspan="3">Code to determine how to compare data (<em>e.g.</em>, “<strong>R</strong>” equals “resistant”).</td>
</tr>
<tr class="even">
<td>Indicator</td>
<td colspan="3">Code to determine how to match results/interpretations.</td>
</tr>
<tr class="odd">
<td><span id="Glos_IRM" class="anchor"></span>Information Resources Management (IRM)</td>
<td colspan="3">The service which is involved in planning, budgeting, procurement and management-in-use of VA's information technology investments.</td>
</tr>
<tr class="even">
<td><span id="Glos_IEPC" class="anchor"></span>Inpatient Evaluation Center (IPEC)</td>
<td colspan="3">The IPEC is a national program to improve outcomes (risk adjusted mortality and length of stay) in VA Intensive Care Units (ICUs) and eventually in inpatient care through feedback of outcomes and implementation of evidenced-based practices. Currently two of the initiatives deal with issues related to infection prevention— catheter-related bloodstream infections and ventilator-associated pneumonias— both of which may involve resistant organisms. These data are reported back immediately to the local facilities who can track their rates over time and compliance with performance, as well as see the national mid-range statistical analysis results.</td>
</tr>
<tr class="odd">
<td>IPEC</td>
<td colspan="3"><em>See</em> <a href="#Glos_IEPC">Inpatient Evaluation Center</a></td>
</tr>
<tr class="even">
<td>IRM</td>
<td colspan="3"><em>See</em> <a href="#Glos_IRM">Information Resources Management</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_isolate" class="anchor"></span>Isolate</td>
<td colspan="3">(noun) An individual (as a spore or single organism), a viable part of an organism (as a cell), or a strain that has been isolated (as from diseased tissue, contaminated water, or the air); also: a pure culture produced from such an isolate.</td>
</tr>
<tr class="even">
<td>Isolation Order</td>
<td colspan="3">Ordered by the provider to place a patient in a certain type of precaution (<em>e.g.</em>, Contact Precautions, Airborne Precautions, etc.) based on the patient’s clinical status.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_K" class="anchor"></span><strong>K</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/063.png)</a></td>
</tr>
<tr class="even">
<td><span id="Glos_KIDS" class="anchor"></span>Kernel Installation and Distribution System (KIDS)</td>
<td colspan="3">The Kernel system permits any <a href="#Glos_VistA">VistA</a> software application to run without modification to its base structure no matter what hardware or software vendor the application was built on. The Kernel contains a number of building management supplies which provide its foundation, including device, menu, programming, operations, security/auditing, task, user, and system management. Its framework provides a structurally sound computing environment that permits controlled user access, menus for choosing various computing activities, the ability to schedule tasks, application development tools, and numerous other management and operation tools.</td>
</tr>
<tr class="odd">
<td>Keys</td>
<td colspan="3"><em>See</em> <a href="#Glos_Sec_Key">Security Keys</a></td>
</tr>
<tr class="even">
<td>KIDS</td>
<td colspan="3"><em>See</em> <a href="#Glos_KIDS">Kernel Installation and Distribution System</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_L" class="anchor"></span><strong>L</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/064.png)</a></td>
</tr>
<tr class="even">
<td>LAB DATA file #63</td>
<td colspan="3">This file is used to store the patient’s laboratory data.</td>
</tr>
<tr class="odd">
<td><span id="Glos_LIM" class="anchor"></span>Laboratory Information Manager</td>
<td colspan="3">The LIM manages the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other <a href="#Glos_CPRS">Computerized Patient Record System</a> (CPRS) functions.</td>
</tr>
<tr class="even">
<td>LABORATORY TEST file #60</td>
<td colspan="3">This is the file that holds the names and ordering, display of tests.</td>
</tr>
<tr class="odd">
<td>LIM</td>
<td colspan="3"><em>See</em> <a href="#Glos_LIM">Laboratory Information Manager</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_M" class="anchor"></span><strong>M</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/065.png)</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_M" class="anchor"></span>M</td>
<td colspan="3"><p>M is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. MUMPS data structures are sparse, using strings of characters as subscripts.</p>
<p>M was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.</p></td>
</tr>
<tr class="even">
<td>MAS</td>
<td colspan="3">See <a href="#Glos_MAS">Medical Administration Service</a></td>
</tr>
<tr class="odd">
<td>Massachusetts General Hospital Utility Multi-Programming System (MUMPS)</td>
<td colspan="3">See <a href="#Glos_M">M</a></td>
</tr>
<tr class="even">
<td><span id="Glos_MailMan" class="anchor"></span>MailMan</td>
<td colspan="3">MailMan is an electronic messaging system that transmits messages, computer programs, data dictionaries, and data between users and applications located at the same or at different facilities. Network MailMan disseminates information across any communications medium.</td>
</tr>
<tr class="odd">
<td>MDRO</td>
<td colspan="3"><em>See</em> <a href="#Glos_MDRO">Multi-Drug Resistant Organism</a></td>
</tr>
<tr class="even">
<td><span id="Glos_MAS" class="anchor"></span>Medical Administration Service (MAS)</td>
<td colspan="3">The Chief, MAS at health care facilities is responsible for administrative aspects of the hospital including determination of eligibility, maintenance and reconciliation of records, review of claims for payment, and compliance with VA Regulations.</td>
</tr>
<tr class="odd">
<td><span id="Glos_MRSA" class="anchor"></span>Methicillin-resistant <em>Staphylococcus aureus</em> (MRSA)</td>
<td colspan="3">A type of bacterium that is resistant to certain antibiotics.</td>
</tr>
<tr class="even">
<td>Methicillin-Resistant <em>Staphylococcus aureus</em> Prevention Initiative</td>
<td colspan="3">The initiative involves establishment of a national MRSA Prevention Initiative for all VA Medical Centers. In January 2007 VHA administration took strong directive action in plan to address infection with MRSA nationwide as a prototype agent for multidrug resistance issues; this national plan employs a bundle approach which includes hand hygiene, contact precautions, active surveillance culturing and cultural change. Seventeen VA medical centers ("beta-sites") across the country are also participating in a cooperative evaluation of this process with the Centers for Disease Control and Prevention (CDC). The initiative was implemented in January 2007; by December 31, 2007 all inpatient acute care units nationwide in VHA had begun the initiative. This work is ongoing, with evaluation for expansion into additional settings such as the long-term care/nursing home/community living center area. National data collection has begun for areas of prevalence of MRSA infection/colonization on admission, healthcare-associated infection with MRSA and MRSA transmission.</td>
</tr>
<tr class="odd">
<td>MMRS SETUP</td>
<td colspan="3">The name of the key that is given to a user to lock the MRSA Tools Setup Menu and all its options. The user(s) assigned to this key is allowed to run the MRSA Tools Parameter Setup Menu and setup/change the system parameters.</td>
</tr>
<tr class="even">
<td>MPC</td>
<td colspan="3">See <a href="#Glos_MPC">MRSA Prevention Coordinator</a></td>
</tr>
<tr class="odd">
<td>MRSA</td>
<td colspan="3">See <a href="#Glos_MRSA">Methicillin-resistant <em>Staphylococcus aureus</em></a></td>
</tr>
<tr class="even">
<td><span id="Glos_MPC" class="anchor"></span>MRSA Prevention Coordinator (MPC)</td>
<td colspan="3">Individual responsible with oversight of the MRSA Prevention Program at their facility.</td>
</tr>
<tr class="odd">
<td><span id="Glos_MDRO" class="anchor"></span>Multi-Drug Resistant Organism</td>
<td colspan="3">A bacterium that is resistant to multiple antibiotics.</td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td colspan="3">See <a href="#Glos_M">M</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_N" class="anchor"></span><strong>N</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/066.png)</a></td>
</tr>
<tr class="even">
<td>Namespace</td>
<td colspan="3">A logical partition on a physical device that contains all the artifacts for a complete <a href="#Glos_M">M</a> system, including <a href="#Glos_Global">globals</a>, routines, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In <a href="#Glos_VistA">VistA</a>, namespaces are usually dedicated to a particular function. The MMMS namespace, for example, is designed for use by MRSA-PT.</td>
</tr>
<tr class="odd">
<td>Nares Screening</td>
<td colspan="3">One method used to detect the presence of MRSA in humans is by means of a sample taken from the nares (nose) using a swab. The sample taken is then tested for the presence of MRSA.</td>
</tr>
<tr class="even">
<td>NHCU</td>
<td colspan="3"><em>See</em> <a href="#Glos_CLC">Community Living Centers</a></td>
</tr>
<tr class="odd">
<td>Nursing Home Care Units (NHCU)</td>
<td colspan="3"><em>See</em> <a href="#Glos_CLC">Community Living Centers</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_P" class="anchor"></span><strong>P</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/067.png)</a></td>
</tr>
<tr class="odd">
<td>PackMan</td>
<td colspan="3">A specific type of <a href="#Glos_MailMan">MailMan</a> message used to distribute <a href="#Glos_KIDS">KIDS</a> builds.</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_S" class="anchor"></span><strong>S</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/068.png)</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_Sec_Key" class="anchor"></span>Security Keys</td>
<td colspan="3">Codes which define the characteristic(s), authorization(s), or privilege(s) of a specific user or a defined group of users. The <a href="#Glos_VistA">VistA</a> option file refers to the security key as a “lock.” Only those individuals assigned that “lock” can use a particular VistA option or perform a specific task that is associated with that security key/lock. In MRSA-PT, keys are used to access specific options that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.</td>
</tr>
<tr class="even">
<td>Selected Etiology</td>
<td colspan="3">Organism or final microbial diagnosis/<a href="#Glos_isolate">isolate</a>.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><span id="G_T" class="anchor"></span><strong>T</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/069.png)</a></td>
</tr>
<tr class="even">
<td>Tasked Report</td>
<td colspan="3">Reports that can be scheduled via <a href="#Glos_TaskMan">TaskMan</a>.</td>
</tr>
<tr class="odd">
<td><span id="Glos_TaskMan" class="anchor"></span>TaskMan</td>
<td colspan="3">The Kernel module that schedule and processes background tasks (aka Task Manager)</td>
</tr>
<tr class="even">
<td>TCP/IP</td>
<td colspan="3"><em>See</em> <a href="#Glos_TCPIP">Transmission Control Protocol over Internet Protocol</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_TCPIP" class="anchor"></span>Transmission Control Protocol over Internet Protocol (TCP/IP)</td>
<td colspan="3">The <em>de facto</em> standard Ethernet protocols, TCP/IP was developed for internetworking and encompasses both network layer and transport layer protocols. While TCP and IP specify two protocols at specific protocol layers, TCP/IP is often used to refer to the entire Department of Defense protocol suite based upon these, including telnet, File Transfer Protocol (FTP), User Datagram Protocol (UDP), and Reliable Data Protocol (RDP).</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_V" class="anchor"></span><strong>V</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/070.png)</a></td>
</tr>
<tr class="odd">
<td>Value</td>
<td colspan="3">Code used to determine how to compare results.</td>
</tr>
<tr class="even">
<td><span id="Glos_VistA" class="anchor"></span>Veterans Health Information Systems and Technology Architecture (VistA)</td>
<td colspan="3">VistA is a comprehensive, integrated health care information system composed of numerous software modules. <em>See</em> <a href="http://www.va.gov/vista_monograph/docs/2008VistAHealtheVet_Monograph.pdf">http://www.va.gov/VistA_monograph/docs/2008VistAHealtheVet_Monograph.pdf</a> and <a href="http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm">http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm</a>.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><span id="G_W" class="anchor"></span><strong>W</strong></td>
<td><a href="#G_Top">![](mrsa-program-tools-version-1-installation-manual/071.png)</a></td>
</tr>
<tr class="odd">
<td>WARD LOCATION File #42</td>
<td colspan="3">This file contains all of the facility ward locations and their related data (<em>e.g.</em>, operating beds, bed section, etc.). The wards are created/edited using the Ward Definition option of the ADT module.</td>
</tr>
<tr class="even">
<td><span id="Glos_Ward_Mapping" class="anchor"></span>Ward Mapping</td>
<td colspan="3">Ward mapping indicated inpatient units (wards) that have been mapped together to create one geographical unit to facilitate data collection.</td>
</tr>
</tbody>
</table>