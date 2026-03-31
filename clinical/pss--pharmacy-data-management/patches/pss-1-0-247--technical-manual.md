---
title: Pharmacy Data Management Technical Manual / Security Guide (PSS_1_0_P247)
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Pharmacy Data Management  / Security Guide (PSS_1_0_P247)
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: archive
pkg_ns: PSS
patch_ver: 1.0
patch_id: PSS*1.0*247
group_key: "PSS:PSS:1.0"
file_numbers: 
  - 50
security_keys: []
menu_options: 7
description: 
audience: 
keywords: 
  - class
  - strong
  - drug
  - pharmacy
  - table
  - contents
  - orderable
  - even
  - management
  - medication
page_count: 0
word_count: 12813
section_count: 36
table_count: 14
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: June 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)_Archive/PSS_1_0_p247_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)_Archive/PSS_1_0_p247_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=392"
---

![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/001.png)

PHARMACY DATA MANAGEMENT

TECHNICAL MANUAL/  
SECURITY GUIDE

June 2012

(Revised July 2021)

Product Development

Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/21</td>
<td>i, 4, 10, 13</td>
<td>PSS*1.0*247</td>
<td><ul>
<li><blockquote>
<p><a href="#P4_Tx_of_Pain">Replaced menu option,</a> Manage Buprenorphine Tx of Pain Dosage Forms [PSS BUPRENORPHINE DOSAGE FORMS] with new option ‘Manage Buprenorphine Tx of Pain <a href="#page9">- VA Products’ [PSS BUPRENORPHINE VAPRODS].</a></p>
</blockquote></li>
<li><blockquote>
<p><a href="#P13_XPAR_Parameter">Added new XPAR Parameters section.</a></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>08/20</td>
<td>Title, i, 5, 10, 11, 13, Footers</td>
<td>PSS*1.0*245</td>
<td><ul>
<li><blockquote>
<p>Added <strong><u>PSS MED INST MED ROUTE REPORT</u></strong> option for Medication Instruction Management</p>
</blockquote></li>
<li><blockquote>
<p>Added <strong><u>PSS MED INST MED ROUTE REPORT</u></strong> option for Medication Routes Management</p>
</blockquote></li>
<li><blockquote>
<p>Added the item <strong><u>PSS MED INST MED ROUTE REPORT</u></strong></p>
</blockquote></li>
<li><blockquote>
<p>Added the item <strong><u>PSS MED INST MED ROUTE REPORT</u></strong></p>
</blockquote></li>
<li><blockquote>
<p>Added routine <strong><u>PSSINSTR</u></strong></p>
</blockquote></li>
<li><blockquote>
<p>Updated Title page, Revision History, and Footers</p>
</blockquote></li>
</ul>
<p>(<mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/18</td>
<td>3</td>
<td>PSS*1.0*215</td>
<td><p>Added Section 2.1.1 <em>Data Dictionary Changes</em> to include information about the RX# UPPER BOUND WARNING LIMIT field (#48) added to the PHARMACY SYSTEM file (#59.7), and the CLINICAL ALERT multiple field (#109) added to the PHARMACY PATIENT file (#55).</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/18</td>
<td>12-13, 30</td>
<td>PSS*1.0*227</td>
<td><p>Added XPAR Parameters section.</p>
<p>Added new routines PSSDEEA, PSSP227, and PSSPRICE to Routines List.</p>
<p>Added entry for PSS DEE AUDIT mail group.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>8/18</td>
<td><a href="#p4">4</a>, <a href="#page9">9</a></td>
<td>PSS*1*219</td>
<td><p>Added new menu option under the ‘Dosages’ menu [PSS DOSAGES MANAGEMENT[</p>
<p>Added new option ‘Manage Buprenorphine Tx of Pain Dosage Forms’ [PSS BUPRENORHINE DOSAGE FORMS].</p>
<p>Added missing options to item multiple under the ‘Dosages’ menu option [PSS DOSAGES MANAGEMENT].</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/18</td>
<td>12-13</td>
<td>PSS*1*224</td>
<td><p>Updated Routine List - adding new routines PSSDSEXF and PSS224PI</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/18</td>
<td>2, 11</td>
<td>PSS*1.0*211</td>
<td><p>Updated File List to include file #50.60699</p>
<p>Updated Routine List with PSSNDSU and PSS211PO</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/18</td>
<td>12-13</td>
<td>PSS*1*178</td>
<td><p>Updated Routine List</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/17</td>
<td>2, 12, 34</td>
<td>PSS*1*201</td>
<td><p>Updated File List</p>
<p>Updated Routine List</p>
<p>Added new routine PSSOAS</p>
<p>Updated File Security</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/16</td>
<td><p>12</p>
<p>34-37</p></td>
<td>PSS*1*193</td>
<td><p>Added new routine PSSHLDFS to the Routines section.</p>
<p>Added Appendix A for Pharmacy Interface Automation.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>4/16</td>
<td><p>i-ii,</p>
<p>11-12, 22-23</p></td>
<td>PSS*1*175</td>
<td><p>Add 2 new Routines: PSSCKOS &amp; PSSDIUTX, Updated Additional Information section</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>3/16</td>
<td><p>i-ii,</p>
<p>11-12</p></td>
<td>PSS*1*191</td>
<td><p>Updated Revision History</p>
<p>Added new routines to routine list:</p>
<p>PSS1P191, PSSHRHAI, PSSMRRDG, PSSMRRI</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>3/14</td>
<td><p>All</p>
<p>i - iii, 2, 7-13, 33, 37</p></td>
<td>PSS*1*172</td>
<td><p>Renumbered all pages.</p>
<p>Updated Revision History and Table of Contents.</p>
<p>Updated the Glossary section by putting definitions in a table format.</p>
<p>New menu, options, file and routines added.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>9/13</td>
<td>i - iii, 3, 7 – 13a, 30, 34 - 35</td>
<td>PSS*1*160</td>
<td><p>Updated Revision History</p>
<p>Updated Table of Contents with Exported Options and Routines sections</p>
<p>Added Lookup Dosing Check Info for Drug [PSS DRUG DOSING LOOKUP] OPTION to the Dosages [PSS DOSAGES MANAGEMENT] MENU OPTION and Drug Names with Trailing Spaces Report</p>
<p>[PSS TRAILING SPACES REPORT].</p>
<p>Added PSS DOSING ORDER CHECKS option</p>
<p>Also added the following routines to the routine list:</p>
<p>PSS160EN</p>
<p>PSS160PO</p>
<p>PSSDRDOS</p>
<p>PSSFDBDI</p>
<p>PSSDSONF</p>
<p>Added Web Servers, Web Services, and Cache Class section</p>
<p>Added text to the Security Keys section</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>01/13</td>
<td>i-iv, 3, 6-6b, 7, 10 - 13</td>
<td><p>PSS*1*164</p>
<p>PSS*1*169</p></td>
<td><p>Removed reference to patch PSS*1*146 in the menu options section</p>
<p>Added Print Interface Data File option to the Pharmacy Data Management [PSS MGR] menu</p>
<p>Added Check Drug Interaction option to the Pharmacy Data Management [PSS MGR] menu</p>
<p>Moved Menu/Option items from page 7 to page 6a</p>
<p>Added Print Interface Data File option to the PEPS Services menu under the Option Descriptions section</p>
<p>Added Check Drug Interaction option to the Option Descriptions section</p>
<p>Added routine PSSDIUTL</p>
<p>Added Find Unmapped Local Possible Dosages option to the Stand Alone Options section</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/12</td>
<td>All</td>
<td>PSS*1*146</td>
<td><p>Reissued document. Removed redundancies due to MOCHA V.1.0 incremental release; updated formatting and page numeration.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

Table of Contents

Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [File List](#file-list)
  - [File Descriptions](#file-descriptions)
    - [Data Dictionary Changes](#data-dictionary-changes)
  - [Menu/Options](#menuoptions)
- [Option Descriptions](#option-descriptions)
  - [Orderable Items Option](#orderable-items-option)
  - [XPAR Parameters](#xpar-parameters)
  - [Routines](#routines)
  - [Exported Options](#exported-options)
    - [Stand-Alone Options](#stand-alone-options)
  - [Protocols](#protocols)
  - [Bulletins](#bulletins)
  - [Web Servers](#web-servers)
  - [Web Services](#web-services)
  - [Cache Class](#cache-class)
  - [HL7 Messaging with an External System](#hl7-messaging-with-an-external-system)
    - [HL7 Drug Message Segment Definition Table](#hl7-drug-message-segment-definition-table)
    - [HL7 Drug Message Segment Definition Table](#hl7-drug-message-segment-definition-table-1)
  - [Data Archiving and Purging](#data-archiving-and-purging)
  - [Callable Routines/Entry Points/Application Program Interfaces (APIs)](#callable-routinesentry-pointsapplication-program-interfaces-apis)
  - [Medication Routes](#medication-routes)
  - [Administration Scheduling](#administration-scheduling)
  - [External Relations](#external-relations)
  - [Internal Relations](#internal-relations)
  - [Package-Wide Variables](#package-wide-variables)
- [Package Requirements](#package-requirements)
  - [Additional Information](#additional-information)
- [Security Management](#security-management)
  - [Mail Groups](#mail-groups)
  - [Alerts](#alerts)
  - [Bulletins](#bulletins-1)
  - [Remote Systems](#remote-systems)
  - [Archiving/Purging](#archivingpurging)
  - [Contingency Planning](#contingency-planning)
  - [Interfacing](#interfacing)
  - [Electronic Signatures](#electronic-signatures)
  - [Locked Menu Options](#locked-menu-options)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
    - [PDM Files](#pdm-files)
    - [Non-PDM Files](#non-pdm-files)
  - [References](#references)
- [Appendix A: Pharmacy Interface Automation](#appendix-a-pharmacy-interface-automation)
  - [New Functionality](#new-functionality)
  - [Options and Build Components](#options-and-build-components)
  - [Modified and New Routines](#modified-and-new-routines)
- [Glossary](#glossary)
Pharmacy Data Management (PDM) provides tools for managing Pharmacy data. It includes tools for creating Pharmacy Orderable Items and maintaining files necessary for the Computer Patient Record System (CPRS). PDM consolidates tools for managing the various Pharmacy software products. It provides Pharmacy Supervisors, in one location, the capability to enter and edit data from the local DRUG file (#50) for all Pharmacy related packages.
The PDM Technical Manual is designed to acquaint the user with the various PDM options and offer specific guidance on the maintenance and use of the PDM package. Documentation concerning the PDM package, including any subsequent change pages affecting this documentation, can be found at the VistA Documentation Library (VDL) on the Veterans Administration Intranet.
Notations that will be used consistently throughout this PDM Technical Manual are outlined below.
- Menu options will be italicized.
> Example: The *Drug Enter/Edit* option permits you to enter or edit a drug.
- Screen prompts will be denoted with quotation marks around them.
> Example: the "SELECT DRUG" prompt will display next.
- Responses in bold face indicate user input.
> Example: DRUG GENERIC NAME: ACETA
- Text centered between bent parentheses represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field.
> \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed.
> Example: Type Y for Yes or N for No and press \<Enter\>
> \<Tab\> indicates that the Tab key must be pressed.
> Example: Press \<Tab\> to move the cursor to the next field.
- ![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/002.png) Indicates especially important or helpful information.
- ![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/003.png) Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.
> Example: ![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/004.png) Without the PSXCOMPMGR key, the Consolidated Mail Outpatient Pharmacy options cannot be accessed.
- □ The page symbol indicates a referral to a diagram.
- ?, ??, ??? One, two or three question marks can be entered at any of the prompts for online help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions, and three question marks will provide more detailed help, including a list of possible answers, if appropriate.
- ^ Up arrow (caret or a circumflex) and pressing \<Enter\> can be used to exit the present option.

# File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following PDM files are exported with the PDM package.

File# NAME UPDATE DATA COMES USER<u>DD WITH FILE OVERRIDE</u>

50 DRUG FULL NO

50.4 DRUG ELECTROLYTES FULL NO

50.606 DOSAGE FORM FULL YES (MERGE) NO

50.60699 MASTER DOSAGE FORM FULL NO

50.7 PHARMACY ORDERABLE ITEM FULL NO

51 MEDICATION INSTRUCTION FULL NO

51.1 ADMINISTRATION SCHEDULE FULL YES (MERGE) YES

51.2 MEDICATION ROUTES FULL YES (MERGE) YES

51.23 STANDARD MEDICATION ROUTES FULL YES NO

(OVERWRITE)

51.24 DOSE UNITS FULL YES NO

(OVERWRITE)

51.25 DOSE UNIT CONVERSION FULL YES NO

(OVERWRITE)

51.5 ORDER UNIT FULL NO

51.7 DRUG TEXT FULL YES YES

(OVERWRITE)

52.6 IV ADDITIVES FULL NO

52.7 IV SOLUTIONS FULL NO

53.47 INFUSION INSTRUCTIONS FULL NO

54 RX CONSULT FULL (SCREEN) NO

55 PHARMACY PATIENT (Partial DD) PARTIAL NO

59.7 PHARMACY SYSTEM FULL NO

59.73 VENDOR DISABLE/ENABLE FULL NO

59.74 VENDOR INTERFACE DATA FULL NO

The following non-PDM files are exported with the PDM package.

File# NAME UPDATE DATA COMES USER<u>DD WITH FILE OVERRIDE</u>

200 NEW PERSON (Partial DD) PARTIAL NO

9009032.3 APSP INTERVENTION TYPE FULL YES NO

(OVERWRITE)

9009032.4 APSP INTERVENTION FULL NO

9009032.5 APSP INTERVENTION RECOMMENDATION FULL YES NO

(OVERWRITE)

## File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package requires the files listed below. Information about the files can be obtained by using the VA FileMan to generate a list of file attributes.

The Data Dictionaries (DDs) are considered part of the online documentation for this software application. Use the VA FileMan *List File Attributes* \[DILIST\] option*,* under the *Data Dictionary Utilities* \[DI DDU\] option, to view/print the DDs.

### Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1.0\*215 adds the RX# UPPER BOUND WARNING LIMIT field (#48) to the PHARMACY SYSTEM file (#59.7). The value stored in this field determines when an early warning message is sent to members of a new PHARMACY SUPERVISORS MailMan group.

This patch is a companion patch to PSO\*7.0\*452, which implements an early warning message to notify mail group recipients that one or more Outpatient Pharmacy sites are approaching the upper limit of the defined prescription numbering series. If no custom value is entered in this field, then the message will be sent when 1000 numbers remain in the series, and again each time the associated background job runs and less than 1000 numbers remain in the series. Refer to the *Outpatient Pharmacy (PSO) Manager’s User Guide* for more information about the early warning functionality that uses this new field.

Patch PSS\*1.0\*215 also adds a CLINICAL ALERT multiple field (#109) to the PHARMACY PATIENT file (#55). This field stores the date and time of the Clinical Alert and provides a free-text field for the alert text, which is displayed when using certain Outpatient Pharmacy \[PSO\] options. Pharmacy Supervisors can use Clinical Alerts to make Pharmacy staff aware of information such as drug interactions or the patient’s participation in clinical trials. Refer to the *Outpatient Pharmacy (PSO) Manager’s User Guide* for more information about the Clinical Alert functionality that uses this new field.

> ![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/005.png) Note: The Clinical Alert Enter/Edit \[PSO CLINICAL ALERT ENTER/EDIT\] option in the Outpatient Pharmacy package is used to add, modify, or delete Clinical Alerts.

Patch PSS\*1\*247 adds a new parameter, the PHARMACY OPERATING MODE field (#102) in the PHARMACY SYSTEM file (#59.7). This field may be set to "VAMC", for traditional VA Medical Center pharmacy mode, or "MBM", for Meds By Mail pharmacy mode. Only the Meds By Mail Pharmacy should set this parameter to “MBM”. If this parameter is left empty, it will default to “VAMC”. Functionality is being released in patch PSO\*7.0\*630 that uses this parameter to help determine whether or not a provider's DEA related information may be edited at the facility. (see the PSO\*7.0\*630 patch description for more details).

## Menu/Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PDM options listed below show the PSS MGR Menu structure.

*Pharmacy Data Management* \[PSS MGR\] menu:

> *CMOP Mark/Unmark (Single drug)* ![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/006.png)

> \[PSSXX MARK\]

> *Dosages…*

> \[PSS DOSAGES MANAGEMENT\]

> *Dosage Form File Enter/Edit*

> \[PSS DOSAGE FORM EDIT\]

> *Enter/Edit Dosages*

> \[PSS EDIT DOSAGES\]

> *Most Common Dosages Report*

> \[PSS COMMON DOSAGES\]

> *Noun/Dosage Form Report*

> \[PSS DOSE FORM/ NOUN REPORT\]

> *Review Dosages Report*

> \[PSS DOSAGE REVIEW REPORT\]

> *Local Possible Dosages Report*

> \[PSS LOCAL POSSIBLE DOSAGES\]

> *Request Change to Dose Unit*

> \[PSS DOSE UNIT REQUEST\]

> *Lookup Dosing Check Info for Drug*

> \[PSS DRUG DOSING LOOKUP\]

> *Drug Names with Trailing Spaces Report*

> \[PSS TRAILING SPACES REPORT\]

> <span id="P4_Tx_of_Pain" class="anchor"></span>*Manage Buprenorphine Tx of Pain - VA Products*

> \[PSS BUPRENORPHINE VAPRODS\]

> *Drug Enter/Edit*

> \[PSS DRUG ENTER/ EDIT\]

> *Order Check Management…*

> \[PSS ORDER CHECK MANAGEMENT\]

> *Request Changes to Enhanced Order Check Database*

> \[PSS ORDER CHECK CHANGES\]

> *Report of Locally Entered Interactions*

> \[PSS REPORT LOCAL INTERACTIONS\]

*Electrolyte File (IV)*

> \[PSSJI ELECTROLYTE FILE\]

> *Lookup into Dispense Drug File*

> \[PSS LOOK\]

> *Medication Instruction Management...*

> \[PSS MED INSTRUCTION MANAGEMENT\]

> *Medication Instruction File Add/Edit*

> \[PSSJU MI\]

> *Medication Instruction File Report*

> \[PSS MED INSTRUCTION REPORT\]

> *Med Instruction Med Term Route Report*

> \[PSS MED INST MED ROUTE REPORT\]

> *Medication Routes Management...*

> \[PSS MEDICATION ROUTES MGMT\]

> *Medication Route File Enter/Edit*

> \[PSS MEDICATION ROUTES EDIT\]

> *Medication Route Mapping Report*

> \[PSS MED ROUTE MAPPING REPORT\]

> *Medication Route Mapping History Report*

> \[PSS MED ROUTE MAPPING CHANGES\]

> *Med Instruction Med Term Route Report*

> \[PSS MED INST MED ROUTE REPORT\]

> *Request Change to Standard Medication Route*

> \[PSS MEDICATION ROUTE REQUEST\]

> *Default Med Route for OI Report*

> \[PSS DEF MED ROUTE OI RPT\]

> *Orderable Item Management…*

> \[PSS ORDERABLE ITEM MANAGEMENT\]

> *Edit Orderable Items*

> \[PSS EDIT ORDERABLE ITEMS\]

> *Dispense Drug/Orderable Item Maintenance*

> \[PSS MAINTAIN ORDERABLE ITEMS\]

> *Orderable Item/Dosages Report*

> \[PSS ORDERABLE ITEM DOSAGES\]

> *Patient Instructions Report*

> \[PSS INSTRUCTIONS/ ITEMS REPORT\]

> *Orderable Item Report*

> \[PSS ORDERABLE ITEM REPORT\]

> *Orderable Items that Require Removal Report*

\[PSS MRR ORDERABLE ITEMS RPT\]

> *Orderable Items for High Risk\High Alert*

\[PSS HR/HA ORDERABLE ITEMS RPT\]

> *Formulary Information Report*

> \[PSSNFI\]

> *Drug Text Management...*

> \[PSS DRUG TEXT MANAGEMENT\]

> *Drug Text Enter/Edit*

> \[PSS EDIT TEXT\]

> *Drug Text File Report*

> \[PSS DRUG TEXT FILE REPORT\]

> *Pharmacy System Parameters Edit*

> \[PSS SYS EDIT\]

> *Standard Schedule Management...*

> \[PSS SCHEDULE MANAGEMENT\]

> *Standard Schedule Edit*

> \[PSS SCHEDULE EDIT\]

> *Administration Schedule File Report*

> \[PSS SCHEDULE REPORT\]

> *Synonym Enter/Edit*

> \[PSS SYNONYM EDIT\]

> *Controlled Substances/PKI Reports…*

> \[PSS CS/PKI REPORTS\]

> *DEA Spec Hdlg & CS Fed Sch Discrepancy*

> \[PSS DEA VS CS FED. SCH. DISCR.\]

> *Controlled Substances Not Matched to NDF*

> \[PSS CS NOT MATCHED TO NDF\]

> *CS (DRUGS) Inconsistent with DEA Spec Hdlg*

> \[PSS CS DRUGS INCON WITH DEA\]

> *CS (Ord. Item) Inconsistent with DEA Spec Hdlg*

> \[PSS CS (OI) INCON WITH DEA\]

> *Send Entire Drug File to External Interface*

> \[PSS MASTER FILE ALL\]

> *IV Additive/Solution …*

> \[PSS ADDITIVE/SOLUTION\]

> *IV Additive Report*

> \[PSS IV ADDITIVE REPORT\]

> *IV Solution Report*

> \[PSS IV SOLUTION REPORT\]

> *Mark PreMix Solutions*

> \[PSS MARK PREMIX SOLUTIONS\]

> *Warning Builder*

> \[PSS WARNING BUILDER\]

> *Warning Mapping*

> \[PSS WARNING MAPPING\]

> *PEPS Services…*

> \[PSS PEPS SERVICES\]

> *Check Vendor Database Link*

\[PSS CHECK VENDOR DATABASE LINK\]

> *Check PEPS Services Setup*

\[PSS CHECK PEPS SERVICES SETUP\]

> *Schedule/Reschedule Check PEPS Interface*

\[PSS SCHEDULE PEPS INTERFACE CK\]

> *Print Interface Data File*

\[PSS VENDOR INTERFACE REPORT\]

> *Inpatient Drug Management…*

> \[PSS INP MGR\]

> *ADditives File*

> \[PSSJI DRUG\]

> *Dispense Drug Fields*

> \[PSSJU DRG\]

> *Dispense Drug/ATC Set Up*

> \[PSSJU DRUG/ATC SET UP\]

> *Edit Cost Data*

> \[PSSJU DCC\]

> *EDit Drug Cost (IV)*

> \[PSSJI EDIT DRUG COST\]

> *MARk/Unmark Dispense Drugs For Unit Dose*

> \[PSSJU MARK UD ITEMS\]

> *PRimary Solution File (IV)*

> \[PSSJI SOLN\]

> *Check Drug Interaction*

> \[PSS CHECK DRUG INTERACTION\]

> *Infusion Instruction Management …*

> \[PSS INFINS MGR\]

> *Infusion Instructions Add/Edit*

> \[PSS INFINS ADED\]

> *Infusion Instruction Report*

> \[PSS INFINS RPT\]

> *Orders for MRRs With Removal Properties*

> \[PSS MRR ORDERS DIAGNOSTIC RPT\]

![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/007.png) Locked: PSXCMOPMGR

Without the PSXCMOPMGR key, =the *CMOP Mark/Unmark (Single drug)=* option will not appear on your menu.

# Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option descriptions below were retrieved from VA FileMan and provide the PDM options following the initial installation of the PDM package.

PSS MGR Pharmacy Data Management

This menu contains the options necessary to build and maintain the PHARMACY ORDERABLE ITEM file (#50.7), and to also build and maintain the Med. Route/Instructions table.

ITEM: PSS DRUG ENTER/EDIT

ITEM: PSS LOOK

ITEM: PSSJI ELECTROLYTE FILE

ITEM: PSSXX MARK

ITEM: PSS SYS EDIT

ITEM: PSS ORDERABLE ITEM MANAGEMENT

ITEM: PSSNFI

ITEM: PSS SYNONYM EDIT

ITEM: PSS DOSAGES MANAGEMENT

ITEM: PSS CS/PKI REPORTS

ITEM: PSS MASTER FILE ALL

ITEM: PSS MEDICATION ROUTES MGMT

ITEM: PSS SCHEDULE MANAGEMENT

ITEM: PSS DRUG TEXT MANAGEMENT

ITEM: PSS MED INSTRUCTION MANAGEMENT

ITEM: PSS ORDER CHECK MANAGEMENT

ITEM: PSS ADDITIVE/SOLUTION

ITEM: PSS WARNING BUILDER

ITEM: PSS WARNING MAPPING

ITEM: PSS PEPS SERVICES

ITEM: PSS INP MGR

ITEM: PSS Check Drug Interaction

ITEM: PSS INFINS MGR

ITEM: PSS MRR ORDERS DIAGNOSTIC RPT

-----------------------------------------------------------------------------

PSS DRUG ENTER/EDIT  
Drug Enter/Edit

This option allows the user to edit fields for ALL pharmacy packages if they possess the proper package key. It also will allow the user to match to NDF and Orderable Item.

TYPE: run routine ROUTINE: PSSDEE

-----------------------------------------------------------------------------

PSS LOOK

Lookup into Dispense Drug File

This option provides a report of all information regarding the dispense drug.

TYPE: run routine ROUTINE: PSSLOOK

-----------------------------------------------------------------------------

PSSJI ELECTROYLYTE FILE  
Electrolyte File (IV)

This option will allow you to alter the contents of the DRUG ELECTORYLYTES file (#50.4). This is the file that is pointed to by the ELECTROLYTE field in both the IV ADDITIVES (#52.6) and IV SOLUTIONS (#52.7) files.

TYPE: run routine ROUTINE: ELECTRO^PSSIVDRG

-----------------------------------------------------------------------------

PSSXX MARK

CMOP Mark/Unmark (Single drug)

This option allows the user to mark/unmark a single drug for transmission to the CMOP.

TYPE: run routine ROUTINE: PSSMARK

-----------------------------------------------------------------------------

PSS SYS EDIT

Pharmacy System Parameters Edit

This option allows the user to edit the Pharmacy System parameters used in Pharmacy Data Management.

TYPE: run routine ROUTINE: PSSYSP

-----------------------------------------------------------------------------

PSS ORDERABLE ITEM MANAGEMENT

Orderable Item Management

This is the sub-menu driver for Orderable Item maintenance.

ITEM: PSS MAINTAIN ORDERABLE ITEMS

ITEM: PSS EDIT ORDERABLE ITEMS

ITEM: PSS ORDERABLE ITEM DOSAGES

ITEM: PSS INSTRUCTIONS/ITEMS REPORT

ITEM: PSS ORDERABLE ITEM REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSSNFI

Formulary Information Report

This option provides a listing of pertinent pharmacy formulary information.

TYPE: run routine ROUTINE: PSSNFI

-----------------------------------------------------------------------------

PSS SYNONYM EDIT

Synonym Enter/Edit

The option provides easy access to update the synonym information for an entry in the local DRUG file.

TYPE: run routine ROUTINE: PSSSEE

-----------------------------------------------------------------------------

PSS DOSAGES MANAGEMENT

Dosages

This menu option contains options that control the editing of dosages.

ITEM: PSS DOSAGE FORM EDIT

ITEM: PSS EDIT DOSAGES

ITEM: PSS COMMON DOSAGES

ITEM: PSS DOSE FORM/NOUN REPORT

ITEM: PSS DOSAGE REVIEW REPORT

ITEM: PSS LOCAL POSSIBLE DOSAGES

ITEM: PSS DOSE UNIT REQUEST

ITEM: PSS DRUG DOSING LOOKUP

ITEM: PSS TRAILING SPACES REPORT

<span id="page9" class="anchor"></span>ITEM: PSS BUPRENORPHINE VAPRODS

TYPE: menu

-----------------------------------------------------------------------------

PSS CS/PKI REPORTS

Controlled Substances/PKI Reports

PKI POST-INSTALL REPORTS PROVIDED AS OPTIONS.

ITEM: PSS DEA VS CS FED. SCH. DISCR.

ITEM: PSS CS NOT MATCHED TO NDF

ITEM: PSS CS DRUGS INCON WITH DEA

ITEM: PSS CS (OI) INCON WITH DEA

TYPE: menu

-----------------------------------------------------------------------------

PSS MASTER FILE ALL

Send Entire Drug File to External Interface

TYPE: run routine ROUTINE: PSSMSTR

-----------------------------------------------------------------------------

PSS MEDICATION ROUTES MGMT

Medication Routes Management

This Sub-Menu contains options related to Medication Routes in both the MEDICATION ROUTES (#51.2) File and the STANDARD MEDICATION ROUTES (#51.23) File.

ITEM: PSS MEDICATION ROUTES EDIT

ITEM: PSS MED ROUTE MAPPING REPORT

ITEM: PSS MED ROUTE MAPPING CHANGES

ITEM: PSS MED INST MED ROUTE REPORT

ITEM: PSS MEDICATION ROUTE REQUEST

ITEM: PSS DEF MED ROUTE OI RPT

TYPE: menu

-----------------------------------------------------------------------------

PSS SCHEDULE MANAGEMENT

Standard Schedule Management

This Sub-Menu contains options needed for Schedule maintenance.

ITEM: PSS SCHEDULE EDIT

ITEM: PSS SCHEDULE REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSS DRUG TEXT MANAGEMENT

Drug Text Management

This Sub-Menu contains options concerning Drug Text.

ITEM: PSS EDIT TEXT

ITEM: PSS DRUG TEXT FILE REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSS MED INSTRUCTION MANAGEMENT

Medication Instruction Management

The Sub-Menu contains options related to the MEDICATION INSTRUCTION (#51) File.

ITEM: PSSJU MI

ITEM: PSS MED INSTRUCTION REPORT

ITEM: PSS MED INST MED ROUTE REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSS ORDER CHECK MANAGEMENT

Order Check Management

This is the sub-menu for functionality related to managing medication order checks.

ITEM: PSS ORDER CHECK CHANGES

ITEM: PSS REPORT LOCAL INTERACTIONS

TYPE: menu

-----------------------------------------------------------------------------

PSS ADDITIVE/SOLUTION

IV Additive/Solution

This Sub-Menu contains options that can be used to run reports from the IV ADDITIVES (#52.6) File and the IV SOLUTIONS (#52.7) File. It also provides an option to edit the PREMIX (#18) Field in the IV SOLUTIONS (#52.7) File.

ITEM: PSS IV ADDITIVE REPORT

ITEM: PSS IV SOLUTION REPORT

ITEM: PSS MARK PREMIX SOLUTIONS

TYPE: menu

-----------------------------------------------------------------------------

PSS WARNING BUILDER

Warning Builder

This option will allow you to define a custom warning label list containing entries from both the new warning label source and the old Rx Consult file entries.

TYPE: run routine ROUTINE: PSSWRNB

-----------------------------------------------------------------------------

PSS WARNING MAPPING

Warning Mapping

This option is used to match an entry from the old Rx Consult file to the new commercial data source warning file to aid in using the Warning Builder (to identify local warnings that do not have an equivalent entry in the new commercial data source). The user can also enter a Spanish translation for an Rx Consult file entry, if desired, but whenever possible, the new commercial data source's warnings (English or Spanish depending on the patient setting) should be used.

TYPE: run routine ROUTINE: EDIT^PSSWMAP

-----------------------------------------------------------------------------

PSS PEPS SERVICES

PEPS

ITEM: PSS CHECK VENDOR DATABASE LINK

ITEM: PSS CHECK PEPS SERVICES SETUP

ITEM: PSS SCHEDULE PEPS INTERFACE CK

ITEM: PSS VENDOR INTERFACE REPORT

TYPE: menu

-----------------------------------------------------------------------------

PSS INP MGR

Inpatient Drug Management

This Sub-Menu contains options related to INPATIENT DRUG MANAGEMENT.

ITEM: PSSJI DRUG

ITEM: PSSJU DRG

ITEM: PSSJU DRUG/ATC SET UP

ITEM: PSSJU DCC

ITEM: PSSJI EDIT DRUG COST

ITEM: PSSJU MARK UD ITEMS

ITEM: PSSJI SOLN

TYPE: Menu

-----------------------------------------------------------------------------

PSS CHECK DRUG INTERACTION

Check Drug Interaction

This menu contains options pertaining to maintaining pharmacy

data files, creating Pharmacy Orderable Items, and the Medication Route/

Instructions table among other assorted functions.

TYPE: run routine ROUTINE: PSSDIUTL

PSS INFINS MGR

Infusion Instruction Management

Menu containing options related to the INFUSION INSTRUCTIONS (#53.47) file.

TYPE: menu

PSS INFINS ADED 

Infusion Instructions Add/Edit

Allows users to enter and edit abbreviations and expansions in the INFUSION INSTRUCTIONS (#53.47) file.

TYPE: run routine ROUTINE: ENII^PSSFILED

PSS INFINS RPT

Infusion Instructions Report

Provides a report of entries from the INFUSION INSTRUCTIONS(#53.47) file

TYPE: run routine ROUTINE: EN^PSSIIRPT

-----------------------------------------------------------------------------

PSS MRR ORDERS DIAGNOSTIC RPT

Orders for MRRs With Removal Properties

## Orderable Items Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option enables you to determine which active orders contain Orderable Items that have the new "Prompt for Removal in BCMA" flag value set to 1, 2 or 3 that need to be discontinued and entered as New (not copied, edited or renewed) AFTER the installation of Pharmacy Inpatient

Medications PSJ\*5.0\*315. Failure to re-create these orders could result in confusing information to display on the BCMA VDL if displayed alongside newer MRR orders that do have the updated removal information.

TYPE: run routine ROUTINE: EN^PSSMRRDG

## XPAR Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*227 adds XPAR parameter PSS DRUG AUDIT RETENTION MOS to the PARAMETER DEFINITION file (#8989.51). See the *Pharmacy Data Management Manager’s User Manual* for information on how this parameter is used. To set the parameter, follow the steps below. You must be a VistA programmer, Pharmacy Informaticist, Clinical Application Coordinator (CAC), or other user with access to the General Parameter Tools \[XPAR MENU TOOLS\] option in VistA.

1\. Log in to VistA.

2\. At the "Select OPTION NAME:" prompt, type XPAR MENU TOOLS and then press Enter.

3\. At the "Select General Parameter Tools Option:" prompt, type EP and then press Enter.

4\. At the "Select PARAMETER DEFINITION NAME:" prompt, type PSS DRUG AUDIT RETENTION MOS and then press Enter.

5\. At the "Drug Audit Retention MOS:" prompt, type the number of retention months and then press Enter.

<span id="P13_XPAR_Parameter" class="anchor"></span>Patch PSS\*1\*247 replaces the existing parameter, PSS BUPRENORPHINE PAIN DFS, with a new XPAR parameter PSS BUPRENORPHINE PAIN VAPRODS to the PARAMETER DEFINITION file (#8989.51). To set the parameter, follow the steps below. You must be a VistA programmer, Pharmacy Informaticist, Clinical Application Coordinator (CAC), or other user with access to the General Parameter Tools \[XPAR MENU TOOLS\] option in VistA.

1\. Log in to VistA.

2\. At the "Select OPTION NAME:" prompt, type XPAR MENU TOOLS and then press Enter.

3\. At the "Select General Parameter Tools Option:" prompt, type EP and then press Enter.

4\. At the "Select PARAMETER DEFINITION NAME:" prompt, type PSS BUPRENORPHINE PAIN VAPRODS and then press Enter.

5\. At the "Select Sequence:" prompt, type the sequence number and then press Enter.

Patch PSS\*1\*247 automatically populuated these products in XPAR “PSS BUPRENORPHINE PAIN VAPRODS” at the Package level during installation:

- BUPRENORPHINE 10MCG/HR PATCH
- BUPRENORPHINE 15MCG/HR PATCH
- BUPRENORPHINE 20MCG/HR PATCH
- BUPRENORPHINE 5MCG/HR PATCH
- BUPRENORPHINE 7.5MCG/HR PATCH
- BUPRENORPHINE 150MCG FILM,BUCCAL
- BUPRENORPHINE 300MCG FILM,BUCCAL
- BUPRENORPHINE 450MCG FILM,BUCCAL
- BUPRENORPHINE 600MCG FILM,BUCCAL
- BUPRENORPHINE 750MCG FILM,BUCCAL
- BUPRENORPHINE 75MCG FILM,BUCCAL
- BUPRENORPHINE 900MCG FILM,BUCCAL

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are used by the Pharmacy Data Management package.

| PSS0052  | PSS0093  | PSS0114  | PSS102RP | PSS117EN | PSS117PO |
|----------|----------|----------|----------|----------|----------|
| PSS127PI | PSS127PT | PSS129EN | PSS147EN | PSS147PO | PSS160EN |
| PSS160PO | PSS172PO | PSS1P135 | PSS1P154 | PSS1P178 | PSS1P201 |
| PSS1P23  | PSS1P43  | PSS211PO | PSS224PI | PSS32P3  | PSS32P5  |
| PSS50    | PSS50A   | PSS50A1  | PSS50AQM | PSS50ATC | PSS50B   |
| PSS50B1  | PSS50B2  | PSS50C   | PSS50C1  | PSS50CMP | PSS50D   |
| PSS50DAT | PSS50DOS | PSS50E   | PSS50F   | PSS50F1  | PSS50LAB |
| PSS50NDF | PSS50P4  | PSS50P66 | PSS50P7  | PSS50P7A | PSS50TMP |
| PSS50WS  | PSS51    | PSS51P1  | PSS51P15 | PSS51P1A | PSS51P1B |
| PSS51P1C | PSS51P2  | PSS51P5  | PSS51P5  | PSS52P6  | PSS52P6A |
| PSS52P6B | PSS52P7  | PSS52P7A | PSS54    | PSS55    | PSS551   |
| PSS55MIS | PSS59P7  | PSS70UTL | PSS781   | PSSADDIT | PSSADRPT |
| PSSAUTL  | PSSBPSUT | PSSCHENV | PSSCHPRE | PSSCHPST | PSSCLDRG |
| PSSCLINR | PSSCLOZ  | PSSCMOPE | PSSCOMMN | PSSCPRS  | PSSCPRS1 |
| PSSCREAT | PSSCSPD  | PSSCUSRQ | PSSDACS  | PSSDAWUT | PSSDDUT  |
| PSSDDUT2 | PSSDDUT3 | PSSDEE   | PSSDEE1  | PSSDEE2  | PSSDEEA  |
| PSSDELOI | PSSDENT  | PSSDFEE  | PSSDGUPD | PSSDI    | PSSDIN   |
| PSSDINT  | PSSDFEE  | PSSDIUTL | PSSDOS   | PSSDOSED | PSSDOSER |
| PSSDOSLZ | PSSDOSRP | PSSDRINT | PSSDRDOS | PSSDSAPA | PSSDSAPD |
| PSSDSAPI | PSSDSAPK | PSSDSAPL | PSSDSAPM | PSSDSBBP | PSSDSBDA |
| PSSDSBDB | PSSDSBPA | PSSDSBPB | PSSDSBPC | PSSDSBPD | PSSDSDAT |
| PSSDSEXC | PSSDSEXD | PSSDSEXE | PSSDSFDB | PSSDSONF | PSSDSPON |
| PSSDSPOP | PSSDSUTA | PSSDSUTL | PSSDTR   | PSSEC123 | PSSENV   |
| PSSDSEXF | PSSENVN  | PSSFDBDI | PSSFDBRT | PSSFIL   | PSSFILED |
| PSSFILES | PSSGENM  | PSSGIU   | PSSGMI   | PSSGS0   | PSSGSGUI |
| PSSGSH   | PSSHELP  | PSSHFREQ | PSSHL1   | PSSHLDFS | PSSHLSCH |
| PSSHLU   | PSSHRCOM | PSSHRENV | PSSHREQ  | PSSHRIT  | PSSHRPST |
| PSSHRQ2  | PSSHRQ22 | PSSHRQ23 | PSSHRQ24 | PSSHRQ25 | PSSHRQ2D |
| PSSHRQ2O | PSSHRVAL | PSSHRVL1 | PSSHTTP  | PSSHUIDG | PSSIIRPT |
| PSSINSTR | PSSJEEU  | PSSJORDF | PSSJSPU  | PSSJSPU0 | PSSJSV   |
| PSSJSV0  | PSSJXR   | PSSJXR1  | PSSJXR10 | PSSJXR11 | PSSJXR12 |
| PSSJXR13 | PSSJXR14 | PSSJXR15 | PSSJXR16 | PSSJXR17 | PSSJXR18 |
| PSSJXR19 | PSSJXR2  | PSSJXR20 | PSSJXR21 | PSSJXR22 | PSSJXR23 |
| PSSJXR24 | PSSJXR25 | PSSJXR26 | PSSJXR27 | PSSJXR28 | PSSJXR29 |
| PSSJXR3  | PSSJXR30 | PSSJXR31 | PSSJXR32 | PSSJXR33 | PSSJXR34 |
| PSSJXR4  | PSSJXR5  | PSSJXR6  | PSSJXR7  | PSSJXR8  | PSSJXR9  |
| PSSLAB   | PSSLDALL | PSSLDEDT | PSSLDOSE | PSSLOCK  | PSSLOOK  |
| PSSMARK  | PSSMATCH | PSSMEDCH | PSSMEDRQ | PSSMEDRT | PSSMEDX  |
| PSSMIRPT | PSSMONT  | PSSMRTUP | PSSMRTUX | PSSMSTR  | PSSNCPDP |
| PSSNDCUT | PSSNDSU  | PSSNFI   | PSSNFIP  | PSSNOD2  | PSSNOUNR |
| PSSNTEG  | PSSOAS   | PSSOICT  | PSSOICT1 | PSSOIDOS | PSSOPKI  |
| PSSOPKI1 | PSSORPH  | PSSORPH1 | PSSORPHZ | PSSORUTE | PSSORUTL |
| PSSORUTZ | PSSOUTSC | PSSP110  | PSSP130  | PSSP134  | PSSP227  |
| PSSPCH13 | PSSPI89  | PSSPKIPI | PSSPKIPR | PSSPNSRP | PSSPO129 |
| PSSPOI   | PSSPOIC  | PSSPOID1 | PSSPOID2 | PSSPOID3 | PSSPOIDT |
| PSSPOIKA | PSSPOIM  | PSSPOIM1 | PSSPOIM2 | PSSPOIM3 | PSSPOIMN |
| PSSPOIMO | PSSPOIMP | PSSPOST  | PSSPOST2 | PSSPOST5 | PSSPOST6 |
| PSSPRE   | PSSPRE38 | PSSPRETR | PSSPRICE | PSSPRMIX | PSSPRUTL |
| PSSQOC   | PSSQORD  | PSSREF   | PSSREMCH | PSSRXACT | PSSSCHED |
| PSSSCHMS | PSSSCHRP | PSSSEE   | PSSSUTIL | PSSSXRD  | PSSSYN   |
| PSSTRENG | PSSTXT   | PSSUNMSI | PSSUTIL  | PSSUTIL1 | PSSUTIL3 |
| PSSUTLA1 | PSSUTLA2 | PSSUTLAZ | PSSUTLPR | PSSUTLPZ | PSSVIDRG |
| PSSVX6   | PSSVX61  | PSSVX62  | PSSVX63  | PSSVX64  | PSSVX65  |
| PSSVX66  | PSSWMAP  | PSSWRNA  | PSSWRNB  | PSSWRNC  | PSSWRNE  |
| PSSXDIC  | PSSXREF  | PSSXRF1  | PSSYSP   |          |          |

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Stand-Alone Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of all stand-alone options that are NOT exported as part of the main PDM menu \[PSS MGR\]:

> *Other Language Translation Setup*

> \[PSS OTHER LANGUAGE SETUP\]

> *Drug Inquiry (IV)*

> \[PSSJI DRUG INQUIRY\]

> *Electrolyte File (IV)*

> \[PSSJI ELECTROLYTE FILE\]

> *Enable/Disable Vendor Database Link*

> \[PSS ENABLE/DISABLE DB LINK\]

> *Add Default Med Route*

> \[PSS ADD DEFAULT MED ROUTE\]

> *Find Unmapped Local Possible Dosages*

> \[PSS LOCAL DOSAGES EDIT ALL\]

![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/008.png)The *Enable/Disable Vendor Database Link* option exists ONLY as a way for technical personnel to turn on/off the database connection if required for debugging. Normally, it is enabled and the Vendor Database updates are performed centrally on the MOCHA Servers, not at the individual sites. It is NOT exported as part of the main PDM menu \[PSS MGR\].

> In the rare case where this option is used and the database link is disabled, NO drug-drug interaction, duplicate therapy, or dosing order checks will be performed in Pharmacy or in the Computerized Patient Record System (CPRS).

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: PSS EXT MFU CLIENT

 DESCRIPTION:   This protocol will be used as the ACK from the external

 interface for a MFN_M01 message. 

NAME: PSS EXT MFU SERVER

 DESCRIPTION:   This protocol will be used to send event notification and data

 when new drugs are added to the DRUG file (#50) and when certain fields are

 updated in the same file. This information will be sent to the automated

 dispensing machines through HL7 V.2.4 formatted messages. 

 

NAME: PSS HUI DRUG UPDATE

 DESCRIPTION:   This protocol will be used to send event notification and data

 when new drugs are added to the Drug file (#50) and when certain fields are

 updated in same file. 

NAME: PSS MED ROUTE RECEIVE

 DESCRIPTION:   This protocol processes updates to the Standard Medication

 Routes (#51.23) File. 

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: PSS FDB INTERFACE

SUBJECT: ORDER CHECK DATABASE DOWN

RETENTION DAYS: 3

PRIORITY?: YES

NAME: PSS FDB INTERFACE RESTORED

SUBJECT: ORDER CHECK DATABASE IS BACK UP

RETENTION DAYS: 3

PRIORITY?: YES

## Web Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PEPS

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DOSING_INFO

DRUG_INFO

ORDER_CHECKS

## Cache Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XMLHandler

## HL7 Messaging with an External System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A protocol, PSS HUI DRUG UPDATE, is exported and has been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. This protocol is exported with the text “DELETE ONLY TO SEND DRUG UPDATE MESSAGES” in the DISABLE field (#2) of the PROTOCOL file (#101). To activate the sending of these HL7 messages, the text from the DISABLE field (#2) of the PROTOCOL file (#101) must be deleted and at least one receiving protocol added as a subscriber. The drug data elements included in the HL7 message are defined in the following HL7 Drug Message Segment Definition table.

### HL7 Drug Message Segment Definition Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the PSS HUI DRUG UPDATE protocol is enabled, the following table defines the data elements sent in each segment of the HL7 drug message.

| Segment | Piece | Field Name          | HL7 TBL \# or Data Type | Description                         |
|-------------|-----------|-------------------------|-----------------------------|-----------------------------------------|
| MSH     | 1         | \|                      | ST                          | Field Separator                         |
|             | 2         | ^~\\                    | ST                          | Encoding Characters                     |
|             | 3         | Pharmacy                | No suggested value          | Sending Application                     |
|             | 9         | MFN                     | 0076                        | Message Type                            |
|             |           |                         |                             |                                         |
| MFI     | 1         | 50^DRUG^99PSD           | 0175                        | Master File ID                          |
|             | 3         | UPD                     | 0178                        | File-Level Event Code                   |
|             | 6         | NE                      | 0179                        | Response Level Code                     |
|             |           |                         |                             |                                         |
| MFA     | 1         | MUP/MAD                 | 0180                        | UPDATE/ADD                              |
|             |           |                         |                             |                                         |
| MFE     | 1         | MUP/MAD                 | 0180                        | UPDATE/ADD                              |
|             | 4         | IEN^DRUG NAME^99PSD     |                             | File 50 Entry                           |
|             |           |                         |                             |                                         |
| ZPA     | 1         | NDC                     | ST                          | National Drug Code                      |
|             | 2         | LOCAL NON-FORMULARY     | CE                          | If “1” true                             |
|             | 3         | INACTIVE DATE           | DT                          | HL7 Format (YYYYMMDD)                   |
|             | 4         | APPLICATION PACKAGE USE | ST                          | Used by what packages                   |
|             | 5         | MESSAGE                 | ST                          | Info on drug                            |
|             | 6         | VA CLASSIFICATION       | ST                          | VA Class                                |
|             | 7         | DEA SPECIAL HDLG        | ST                          | How drug is dispense based on DEA codes |
|             | 8         | FSN                     | ST                          | Federal Stock \#                        |
|             | 9         | WARNING LABEL           | ST                          | Drug Warnings for patient               |
|             | 10        | VISN NON-FORMULAR       | CE                          | If ‘1’ true                             |
|             |           |                         |                             |                                         |

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ZPB</strong></th>
<th>1</th>
<th>PHARMACY ORDERABLE ITEM</th>
<th>CE</th>
<th>IEN^OI tied to dispense drug^PSD50.7</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>2</td>
<td>DOSAGE FORM</td>
<td>ST</td>
<td>IEN^Dosage Form associated with OI^PSD50.606</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>MEDICATION ROUTE</td>
<td>ST</td>
<td>IEN^Med Route associated with OI^PSD51.2</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>PSNDF VA PRODUCT NAME ENTRY</td>
<td>CE</td>
<td>IEN^VA PRODUCT NAMES^PSD50.68</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>DISPENSE UNIT</td>
<td>ST</td>
<td>Dispense Unit for a drug</td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td>CMOP DISPENSE</td>
<td>CE</td>
<td>1 or 0</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>OP EXTERNAL DISPENSE</td>
<td>CE</td>
<td>1 or 0</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>EXPIRATION DATE</td>
<td>DT</td>
<td>HL7 Format (YYYYMMDD)</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>LAB TEST MONITOR</td>
<td>CE</td>
<td>IEN^Lab Test^LAB60</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>ZPC</strong></td>
<td>1</td>
<td>SPECIMEN TYPE</td>
<td>CE</td>
<td>IEN^ SPECIMEN TYPE^LAB61</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>MONITOR ROUTINE</td>
<td>ST</td>
<td>Program that runs to find lab test and results</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>LAB MONITOR MARK</td>
<td>CE</td>
<td>If ‘1’ true</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>STRENGTH</td>
<td>NM</td>
<td>Dose of drug</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>UNIT</td>
<td>CE</td>
<td>IEN^Unit of measure^PSD50.607</td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td>PRICE PER ORDER UNIT</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>PRICE PER DISPENSE UNIT</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>[{ZPD}]</strong></td>
<td>1</td>
<td>SYNONYM</td>
<td>ST</td>
<td>Trade Name</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>NDC CODE</td>
<td>ST</td>
<td>National Drug Code</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>INTENDED USE</td>
<td>CE</td>
<td>CE^INTENTED USE</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>VSN</td>
<td>ST</td>
<td>Vendor Stock Number</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>ORDER UNIT</td>
<td>CE</td>
<td><p>IEN^ABBREVIATION^EXPANSION</p>
<p>^PSD51.5</p></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td>PRICE PER ORDER UNIT</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>DISPENSE UNITS PER ORDER UNIT</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>PRICE PER DISPENSE UNIT</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>VENDOR</td>
<td>ST</td>
<td>Vendor</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>[{ZPE}]</strong></td>
<td>1</td>
<td>ACTIVITY LOG</td>
<td>DT</td>
<td>HL7 Format YYYYMMDDHHMM[SS]-ZZZZ</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>REASON</td>
<td>CE</td>
<td>E^EDIT</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>INITIATOR OF ACTIVITY</td>
<td>CE</td>
<td>IEN^NEW PERSON^VA200</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>FIELD EDITED</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>NEW VALUE</td>
<td>ST</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td>NDF UPDATE</td>
<td>ST</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>[{ZPF}]</strong></td>
<td>1</td>
<td>DISPENSE UNITS PER DOSE</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>DOSE</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>PACKAGE</td>
<td>CE</td>
<td>CE^PACKAGE(S)</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>BCMA UNITS PER DOSE</td>
<td>NM</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>[{ZPG}]</strong></td>
<td>1</td>
<td>CLOZAPINE LAB TEST</td>
<td>CE</td>
<td>IEN^LAB TEST^LAB60</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>MONITOR MAX DAYS</td>
<td>NM</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>SPECIMEN TYPE</td>
<td>CE</td>
<td>IEN^ SPECIMEN TYPE^LAB61</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>TYPE OF TEST</td>
<td>CE</td>
<td>1^WBC or 2^ANC</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>[{ZPH}]</strong></td>
<td>1</td>
<td>LOCAL POSSIBLE DOSAGE</td>
<td>ST</td>
<td>FREE TEXT</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>PACKAGE</td>
<td>CE</td>
<td>CE^PACKAGE(S)</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>BCMA UNITS PER DOSE</td>
<td>NM</td>
<td></td>
</tr>
</tbody>
</table>

Two protocols, PSS EXT MFU CLIENT and PSS EXT MFU SERVER, are exported and have been created to generate HL7 messages when new drugs are added to the DRUG file (#50) and existing entries are updated. These protocols can only be activated by setting the following parameters in the OUTPATIENT SITE file (#59):

- AUTOMATED DISPENSE field (#105) needs to be set to 2.4.
- ENABLE MASTER FILE UPDATE field (#105.2) needs to be set to YES.
- LOGICAL LINK field (#2005) needs to be set to PSO DISP.
- DISPENSE DNS NAME field (#2006) needs to be set to the dispensing system DNS name (for example, dispensemachine1.vha.med.va.gov).
- DISPENSE DNS PORT field (#2007) needs to be set to the dispensing system port number.

Specific Transaction

The Pharmacy/Treatment Encoded Order Message is as follows:

> <u>MFN Master File Notification Message</u>

> MSH Message Header

> MFI Master File Identifier

> {MFE Master File Entry

> {{ZPA} Drug File Information

> {RXD} Pharmacy/Treatment Dispense

> {OBR}} Observation Request

> }

Example:

MSH\|~^\\\|PSS VISTA\|521~FO-BIRM.VHA.MED.VA.GOV~DNS\|PSS DISPENSE\|~DISPENSE1.VHA.MED.VA.GOV:9300~DNS\|20030701\|\|MFN~M01~MFN_M01\|10001\|P\|2.4\|\|\|AL\|AL

MFI\|50~DRUG~99PSD\|\|UPD\|\|\|NE

MFE\|MUP\|\|\|PROPANTHELINE 15MG TAB

ZPA\|PROPANTHELINE 15MG TAB\|N\|LFN~Local Non-Formulary~Pharm Formulary Listing\|20031226\|Take with food\|DE200\|6\|P\|50~6505-00-960-8383~LPS50\|8~NO ALCOHOL~LPS54\|229~Bacitracin~LPSD50.7\|3~CAP,ORAL~LPSD50.606\|15~IV PUSH~LPSD51.2\|3643~ATROPINE SO4 0.4MG TAB~LPSD50.68\|OP~OP Dispense~99OP\|20030830\|9~Rubella~LLAB60\|72~Hair of Scalp~LLAB61\|PSOCLO1\|N\|100\|20~MG~LPSD50.607\|4.28&USD~UP\|15.64&USD~UP\|TAB\|2\|BLUE HOUSE VENDOR\|0010-0501-33\|TRADENAME

RXD\|\|\|\|1\|\|\|\|\|1\|\|\|~P&200&LPSD50.0903\|\|\|\|\|\|\|\|\|\|\|\|O

OBR\|\|\|\|1102~ACETAZOLAMIDE~LLAB60\|\|\|\|\|\|\|\|\|\|\|70&NECK&LLAB61\|\|\|\|\|\|\|\|\|WBC\|\|\|7

### HL7 Drug Message Segment Definition Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the PSS EXT MFU SERVER protocol is enabled, the following table defines the data elements sent in each segment of the HL7 drug message.

Segments Used in the Master File Update Message

| SEGMENT | SEQ# | LEN | DT | R/O | RP/# | TBL# | ELEMENT NAME                                             | EXAMPLE                                     |
|-------------|----------|---------|--------|---------|----------|----------|--------------------------------------------------------------|-------------------------------------------------|
| MSH         | 1        | 1       | ST     | R       |          |          | Field Separator                                              | \|                                              |
|             | 2        | 4       | ST     | R       |          |          | Encoding Characters                                          | ~^\\                                            |
|             | 3        | 180     | HD     | R       |          | 0361     | Sending Application                                          | PSS VISTA                                       |
|             | 4        | 180     | HD     | R       |          | 0362     | Sending Facility – station ID and station DNS name           | 521~FO-BIRM.MED.VA.GOV~DNS                      |
|             | 5        | 180     | HD     | R       |          | 0361     | Receiving Application                                        | PSS DISPENSE                                    |
|             | 6        | 180     | HD     | R       |          | 0362     | Receiving Facility – DNS name and port of dispensing machine | ~DISPENSE.VHA.MED.VA.GOV:9300~DNS               |
|             | 7        | 26      | TS     |         |          |          | Date/Time of Message                                         | 20040405152416                                  |
|             | 9        | 15      | CM     | R       | 0076     |          | Message Type                                                 | MFN_M01                                         |
|             | 10       | 20      | ST     | R       |          |          | Message Control ID                                           | 10001                                           |
|             | 11       | 3       | PT     | R       | 0103     |          | Processing ID                                                | P                                               |
|             | 12       | 3       | VID    | R       | 0104     |          | Version ID                                                   | 2.4                                             |
|             | 15       | 2       | ID     |         |          | 0155     | Accept Ack. Type                                             | AL                                              |
|             | 16       | 2       | ID     |         |          | 0155     | Application Ack Type                                         | AL                                              |
|             |          |         |        |         |          |          |                                                              |                                                 |
| MFI         | 1        | 250     | CE     | R       |          | 0175     | Master File Identifier                                       | 50^DRUG^99PSD                                   |
|             | 3        | 3       | ID     | R       |          | 0178     | File-Level Event Code                                        | UPD                                             |
|             | 6        | 2       | ID     | R       |          | 0179     | Response Level Code                                          | NE                                              |
|             |          |         |        |         |          |          |                                                              |                                                 |
| MFE         | 1        | 3       | ID     | R       |          | 0180     | Record-Level Event Code                                      | MUP                                             |
|             | 4        | 200     | Varies | R       |          |          | Primary Key Value – MFE                                      | PROPANTHELINE 15MG TAB                          |
|             |          |         |        |         |          |          |                                                              |                                                 |
| ZPA         | 1        | 200     | Varies | R       |          |          | Primary Key Value – ZPA                                      | PROPANTHELINE 15MG TAB                          |
|             | 2        | 1       | ID     | R       |          | 0136     | Is Synonym                                                   | N                                               |
|             | 3        | 200     | CE     | R       |          |          | Formulary Listing                                            | LFN~Local Non-Formulary~Pharm Formulary Listing |
|             | 4        | 10      | DT     | O       |          |          | Inactive Date                                                | 20031226                                        |
|             | 5        | 200     | ST     | O       |          |          | Drug Message                                                 | Take with Food                                  |
|             | 6        | 30      | ST     | O       |          |          | Drug Classification                                          | DE200                                           |
|             | 7        | 10      | ST     | O       |          |          | DEA-Schedule Code                                            | 6                                               |
|             | 8        | 1       | ST     | O       |          |          | DEA-Drug Type                                                | P                                               |
|             | 9        | 100     | CE     | R       |          |          | Stock Number                                                 | 50~6505-00-960-8383~LPS50                       |
|             | 10       | 100     | CE     | O       |          |          | Warning Label                                                | 8~NO ALCOHOL~LPS54                              |
|             | 11       | 100     | CE     | O       |          |          | Pharmacy Orderable Item                                      | 229~Bacitracin~LPSD50.7                         |
|             | 12       | 100     | CE     | O       |          |          | Dosage Form                                                  | 3~CAP,ORAL~LPSD50.606                           |
|             | 13       | 100     | CE     | O       |          |          | Medication Route                                             | 15~IV PUSH~LPSD51.2                             |
|             | 14       | 100     | CE     | O       |          |          | Drug Name Identifiers                                        | 3643~ATROPINE SO4 0.4MG TAB~LPSD50.68           |
|             | 15       | 100     | CE     | O       |          |          | Dispense Flags                                               | OP~OP Dispense~99OP                             |
|             | 16       | 15      | DT     | O       |          |          | Drug Expiration Date                                         | 20030830                                        |
|             | 17       | 100     | CE     | O       |          |          | Lab Test Monitor                                             | 9~Rubella~LLAB60                                |
|             | 18       | 100     | CE     | O       |          |          | Specimen Type                                                | 72~Hair of Scalp~LLAB61                         |
|             | 19       | 10      | CE     | O       |          |          | Monitor Routine                                              | PSOCLO1                                         |
|             | 20       | 1       | ID     | O       |          |          | Lab Monitor Mark                                             | N                                               |
|             | 21       | 50      | NM     | O       |          |          | Strength                                                     | 100                                             |
|             | 22       | 250     | CE     | R       |          |          | Unit                                                         | 20~MG~LPSD50.607                                |
|             | 23       | 50      | CP     | R       |          |          | Price Per Order Unit                                         | 4.28&USD~UP                                     |
|             | 24       | 50      | CP     | R       |          |          | Price Per Dispense Unit                                      | 15.64&USD~UP                                    |
|             | 25       | 25      | ST     | O       |          |          | Dispense Unit                                                | TAB                                             |
|             | 26       | 50      | NM     | O       |          |          | Dispense Units Per Order Unit                                | 2                                               |
|             | 27       | 50      | ST     | O       |          |          | Vendor                                                       | BLUE HOUSE VENDOR                               |
|             | 28       | 12      | ST     | O       |          |          | NDC Code                                                     | 0010-0501-33                                    |
|             | 29       | 25      | ST     | O       |          |          | Intended Use                                                 | TRADE NAME                                      |
|             |          |         |        |         |          |          |                                                              |                                                 |
| RXD         | 4        | 20      | NM     | R       |          |          | Actual Dispense Amount                                       | 1                                               |
|             | 8        | 20      | NM     | R       |          |          | Dispense Notes                                               | 1                                               |
|             | 12       | 10      | CQ     | O       |          |          | Total Daily Dose                                             | ~P&200&LPSD50.0903                              |
|             | 24       | 2       | ID     | R       |          |          | Dispense Package Method                                      | O                                               |
|             |          |         |        |         |          |          |                                                              |                                                 |
| OBR         | 4        | 250     | CE     | O       |          |          | Universal Service Identifier                                 | 1102~ACETAZOLAMIDE~LLAB60                       |
|             | 15       | 300     | CM     | O       |          |          | Specimen Source                                              | 70&NECK&LLAB61                                  |
|             | 24       | 3       | ID     | R       |          |          | Diagnostic Serv Sect ID                                      | WBC                                             |
|             | 27       | 200     | TQ     | O       |          |          | Quantity/Timing                                              | 7                                               |

Notes Pertaining to Some of the Data Elements:

> \[MSH-3\] Sending Application is the station ID along with the DNS name of the sending facility.

> \[MSH-5\] Receiving Application is the DNS name and DNS port number of the dispensing application.

> \[MSH-10\] Message Control ID is the number that uniquely identifies the message. It is returned in MSA-2 of the dispense completion message.

> \[MFI-1\] Master File Identifier is hard-coded to 50~DRUG~99PSD.

> \[MFE-1\] Record-Level Event Code can be either MUP for Update or MAD for Add.

> \[MFE-4\] Primary Key Value – MFE is the GENERIC NAME field (#.01) from the DRUG file (#50).

> \[ZPA-1\] Primary Key Value – ZPA will be the generic name of the drug first and then all synonyms will follow in consecutive ZPA segments.

> \[ZPA-2\] Is Synonym is set to Y or N depending on whether the primary key is a synonym.

> \[ZPA-3\] Formulary Listing will contain LFN and/or VISN is the formulary is not to appear on the Local or VISN formulary.

> \[ZPA-9\] Stock Number is the FSN field (#6) from the DRUG file (#50) or the VSN field (#400) from the SYNONYM subfile (#50.1) of the PRESCRIPTION file (#50).

> \[ZPA-15\] Dispense Flags will indicate if this drug may be dispensed to an external interface and if it is marked to be dispensed at a Consolidated Outpatient Pharmacy (CMOP). If both are yes, the answer would be OP~OP Dispense~Pharm dispense^CMOP~CMOP dispense~Pharm dispense flag.

> \[ZPA-29\] Intended User will be TRADE NAME, QUICK CODE, DRUG ACCOUNTABILITY or CONTROLLED SUBSTANCES.

> \[RXD-4\] Actual Dispense Amount is the BCMA UNITS PER DOSE field (#3) from the POSSIBLE DOSAGES file (#50.0903).

> \[RXD-9\] Dispense Notes is the DISPENSE UNITS PER DOSE field (#.01) from the POSSIBLE DOSAGES file (#50.0903).

> \[RXD-12\] Total Daily Dose will be either P for Possible Dosages or LP for Local Possible Dosages.

> \[OBR-4\] Universal Service Identifier is used for Clozapine Lab Test.

> \[OBR-15\] Specimen Source is used for Clozapine Specimen Type.

> \[OBR-24\] Diagnostic Serv Sect ID is used for Clozapine Type of Test.

> \[OBR-27\] Quantity/Timing is used to encode Monitor Max days from the CLOZAPINE LAB TEST file (#50.02).

## Data Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving and purging functions necessary with this release of the PDM package.

## Callable Routines/Entry Points/Application Program Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

APIs, callable routines, and entry points can be viewed by first choosing the *DBA* menu option on FORUM and then choosing the *Integration Agreement*s *Menu* option:

IAs    INTEGRATION CONTROL REGISTRATIONS ...

For detailed information on all supported Pharmacy Data Management APIs, see the *Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual* posted on the VistA Documentation Library (VDL).

## Medication Routes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following paragraphs provide an explanation of medication route information.

For Outpatient Pharmacy & Inpatient Medication Unit Dose Orders:

The Default med route will be returned from the DEFAULT MED ROUTE field (#.06) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated, or from the POSSIBLE MED ROUTES multiple (#50.711) of the PHARMACY ORDERABLE ITEM file (#50.7) if it is populated with a single entry and the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO." The med route selection list will be returned with entries from the POSSIBLE MED ROUTES multiple (#50.711) if the USE DOSAGE FORM MED ROUTE LIST field (#10) is set to "NO." Otherwise, the med routes associated with the orderable item's dosage form, MED ROUTE FOR DOSAGE FORM multiple (#50.6061) of the DOSAGE FORM file (#50.606), will be returned.

For IV Fluids Orders:

If there is only one orderable item in the IV order request, the same logic as defined above under ‘For Outpatient Pharmacy & Inpatient Medication Unit Dose Orders’ will be used to return the default med route from the DEFAULT MED ROUTE field (#.06) and the med route selection list from the PHARMACY ORDERABLE ITEM file (#50.7).

If there is more than one orderable item on the IV order request, the PHARMACY ORDERABLE ITEM file (#50.7) will be checked for each orderable item for the default med route and med route selection list as defined above under ‘For Outpatient Pharmacy & Inpatient Medication Unit Dose Orders.’ If there is a default med route common with every orderable item, that default med route will be returned. Similarly, the list of possible med routes that are common with every orderable item will be returned.

## Administration Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following rules apply to administration scheduling.

If there is a duplicate schedule, and if one of them contains ward-specific administration times for the ward location of the patient, the schedule returned for inclusion in the array of selectable schedules in CPRS will be the one with the ward-specific administration times.

If no duplicate has ward-specific administration times for the ward location of the patient, the schedule with the lowest IEN number will be returned. If both (or more than one) duplicate schedules have ward-specific administration times for the ward location of the patient, the schedule with the lowest IEN number in the ADMINISTRATION SCHEDULE file \#51.1 will be the schedule in the array returned to CPRS.

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Agreements

IAs can be viewed by first choosing the *DBA* option on FORUM and then the *Integration Agreement*s *Menu* option.

Example: DBA Option  

Select Primary Menu Option: DBA

Select DBA Option: INTEGration Agreements Menu

Select Integration Agreements Menu Option: Custodial Package Menu

Select Custodial Package Menu Option: ACTIVE by Custodial Package

Select PACKAGE NAME: PHARMACY DATA MANAGEMENT PSS

DEVICE: HOME//

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All PDM options can function independently.

## Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables for this version.

# Package Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PDM module relies on, at least, the following external packages to run effectively.

<u>Package</u><u>Minimum version needed</u>

National Drug File V. 4.0

Outpatient Pharmacy V. 7.0

Inpatient Medications V. 5.0

Kernel V. 8.0

VA FileMan V. 22.0

<u>Package</u><u>Minimum version needed</u>

HealtheVet Web Services Client (HWSC) V. 1.0

VistALink V. 1.6

## Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Standards and Conventions Committee (SACC) Exemptions

The following PSS routines will generate errors reported in the XINDEX utility from using non-standard M syntax, due to the need to consume external web services.

PSSFDBDI

PSSFDBRT

PSSHRPST

PSSHTTP

The following waiver permits the use of this non-standard M syntax to allow the use of Cache features to consume external web services. This waiver is located in the HealtheVet Web Services Client (HWSC) Developer Guide.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>OITIMB33554520 - Migration from M2J to VistA Web Services Client (VWSC)</strong></td>
</tr>
<tr class="even">
<td><strong>Keywords</strong></td>
<td>M2J,VWSC,J2EE</td>
</tr>
<tr class="odd">
<td><strong>Decision Date</strong></td>
<td>12/1/2006</td>
</tr>
<tr class="even">
<td><strong>Decision Type</strong></td>
<td>Architecture</td>
</tr>
<tr class="odd">
<td><strong>Decision Making Body</strong></td>
<td>HPMO CCB</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td>On December 1, 2006, the HPMO Change Control Board voted to accept the migration of VistA from the current M2J solution to the VistA Web Services Client (VWSC). This decision was made for a number of reasons, in particular the fact that the existing 12-year-old M standard has been surpassed by evolving technologies and can no longer address today’s requirements. Additionally, we are no longer required to support DSM, previously the primary VistA/M hosting environment. Today, all sites are standardized on Caché 5.0 systems. As such, approvals were granted as follows: Waiver of the requirement to adhere to the existing 1995 M standard (that does not address the implementation of web services); Implementation of an industry standard such as web services for VistA/M to J2EE calls using Caché’s built in HTTP and web service client feature; Use of VWSC as an interim solution that ensures continuity of integration between VistA/M applications and migrated J2EE applications as HealtheVet evolves by enabling the consumption of external web services by legacy VistA applications; and Deprecation of the original M2J approach.</td>
</tr>
<tr class="odd">
<td><strong>Rationale</strong></td>
<td>This architectural change allows for a number of improvements, including better scalability, resilience, and performance. Deployment and configuration is far less complicated for administrators, and the APIs can be used by a variety of clients rather than solely M-based. It also places responsibility for support, maintenance, etc. with the vendor rather than OI&amp;T.</td>
</tr>
<tr class="even">
<td><strong>Record Type</strong></td>
<td>TDR</td>
</tr>
<tr class="odd">
<td><strong>State</strong></td>
<td>Approved</td>
</tr>
<tr class="even">
<td><strong>Date Submitted</strong></td>
<td>2/14/2007 8:37:24 AM</td>
</tr>
</tbody>
</table>
<p><strong>Supporting Documentation</strong></p>
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 44%" />
<col style="width: 36%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Link</td>
<td>Document Title</td>
<td>Description</td>
<td>Date</td>
</tr>
<tr class="even">
<td>Download</td>
<td>Migration from M2J to VistA Web Services Client (VWSC) Email Notification</td>
<td>Email notification alerting of the decision</td>
<td>2/13/2007</td>
</tr>
<tr class="odd">
<td>Download</td>
<td>VWSC Architecture</td>
<td>Proposed architecture view of VWSC</td>
<td>12/1/2006</td>
</tr>
<tr class="even">
<td>Download</td>
<td>VWSC Proposed View</td>
<td>Proposed logical view of VistA Web Services Client (VWSC)</td>
<td>12/1/2006</td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Cross-Reference Logic to Keep Orderable Items Up To Date

With the introduction of PSS\*1\*38, a new process for keeping Orderable Items updated was implemented. The process is explained in detail in the section below.

Anytime specific fields are edited, or a pointer to the PHARMACY ORDERABLE ITEM file (#50.7) changes, the Orderable Item (OI) must be updated and sent to CPRS. Two different situations can precipitate these changes. Both situations are explained in detail here.

The first situation occurs when a field is edited that can possibly affect the status of the Orderable Item, but no Orderable Item pointers change. In this situation, the old Orderable Item is the same as the new Orderable Item. In these cases, the kill logic will be the same as the set logic. The kill and set logic will simply pass in the Orderable Item to the routine that checks all IV Additives/IV Solutions/Dispense Drugs matched to the Orderable Item, does all the necessary updates (Inactivation date, Supply flag, Non-formulary, Base, Additive), and then sends the Master File Update to CPRS on that Orderable Item. This type of update occurs when the fields listed below are edited.

File 50: DEA Special Hdlg

File 50: Inactivation Date

File 50: Application Packages’ Use

File 50: Local Non-Formulary

File 50.7: Inactivation Date

File 52.6: Inactivation Date

File 52.6: Used in IV Fluid Order Entry

File 52.7: Inactivation Date

File 52.7: Used in IV Fluid Order Entry

The second situation occurs when pointers to the PHARMACY ORDERABLE ITEM file (#50.7) are changed. IV Additives, IV Solutions and the Dispense Drug always point to the same Orderable Item. That Orderable Item is, in turn, pointed to by the IV Additive or IV Solution. So, the fields that may be affected include the Orderable Item pointer in the DRUG file (#50) and the Generic Drug pointer in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7).

File 50: Orderable Item Pointer

File 52.6: Generic Drug Pointer

File 52.7: Generic Drug Pointer

The initial change is to make the Orderable Item pointers in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7) uneditable. The software will now control those pointers.

Scenario 1: The Orderable Item Pointer Is Changed For A Dispense Drug

In Example 1, the Orderable Item pointer is changed for a Dispense Drug. In this case, any Orderable Item pointers must be updated for entries in the IV ADDITIVES file (#52.6) and the IV SOLUTIONS file (#52.7) that point to that Dispense Drug. After these pointers have been updated, the Orderable Item must be updated for the old Orderable Item with what will point to it after the matching. The Orderable Item must also be updated for the new Orderable Item after the matching. And these pharmacy Orderable Item updates must be sent to CPRS as part of the Master File Update. To accomplish this, the following steps must be completed:

1.  Add a Cross-Reference on the Orderable Item pointer in the DRUG file (#50) that will hard set one Cross-Reference in the ORDERABLE ITEM file (#50.7) and two Cross-References in the DRUG file (#50) as follows.

> Orderable Item: ^PS(50.7,"A50",Orderable Item IEN, Dispense Drug IEN)=""

> Drug file: ^PSDRUG("A526", Dispense Drug IEN, Additive IEN,)=""

> Drug file: ^PSDRUG("A527", Dispense Drug IEN, Solution IEN,)=""

> The Orderable Item Cross-Reference allows access to Dispense Drugs matched to an Orderable Item. The two DRUG file (#50) Cross-References allow access to Solutions and Additives linked to Dispense Drugs. An "A50" Cross-Reference will also be added on the NAME field (# .01) of the PHARMACY ORDERABLE ITEM file (#50.7) containing a "Quit" command for the set and kill logic for documentation purposes only.

> When the Orderable Item pointer of a Dispense Drug changes, only one Cross-Reference is needed on that field to perform the following actions:

- Kill Logic: This command performs a hard kill of the "A50" Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7) for that Dispense Drug using old value (X) and DA, where X equals the OI IEN and DA equals the Dispense Drug IEN. The two DRUG file (#50) Cross-References will not change.

> After the hard kill is completed, a Master File Update is performed for the old Orderable Item. The logic for all Dispense Drugs/IV Additives/IV Solutions matched to the Orderable item is executed by looping the three Cross-References to find all entries in all three files matched to the Orderable Item. Also in the Kill logic, the Orderable Item pointer is set to null and the Orderable Item pointer Cross-Reference is killed for any IV Additives or IV Solutions matched to the Dispense Drug.

- Set Logic: Using the New Value (X), where X equals the OI IEN, the "A50" Cross-Reference is hard set in the PHARMACY ORDERABLE ITEM file (#50.7). The Master File Update is then performed for the new Orderable Item. The logic for all Dispense Drugs/IV Additives/IV Solutions matched to the Orderable Item is executed by looping on the three Cross-References to find all entries in all three files matched to the Orderable Item. The Orderable Item pointer and the Orderable Item pointer Cross-References are then hard set for all IV Additives and IV Solutions that have been matched to the Dispense Drug with new value (X).

> Example 1:

> Additives/Solution Dispense Drugs: Orderable Item:

> IEN 3 points to =\> IEN 100 points to =\> 500

> IEN 4 points to =\> IEN 100 points to =\> 500

> IEN 5 points to =\> IEN 100 points to =\> 500

> IEN 10 points to =\> IEN 200 points to =\> 500

> Cross-References are: ^PS(50.7,"A50",500,100)=""

> ^PS(50.7,"A50",500,200)=""

> ^PSDRUG("A526",100,3)=""

> ^PSDRUG("A526",100,4)=""

> ^PSDRUG("A526",100,5)=""

> ^PSDRUG("A527",200,10)=""

> Orderable Item 500 is pointed to by Dispense Drugs 100 and 200, and by IV Additives 3, 4, and 5, and IV Solution 10.

> (If the LOCAL NON-FORMULARY field (#51) in the DRUG file (#50) is edited, the software will obtain the OI pointer 500 and execute the OI logic by looping on 500 in the "A50" Cross-Reference of the PHARMACY ORDERABLE ITEM file (#50.7). As it references each entry, the OI logic is executed by looping on the “A526” and “A527” Cross-references on the DRUG file (#50) before going to the next Orderable Item pointer in the "A50" Cross-reference in the PHARMACY ORDERABLE ITEM file (#50.7). For Example 1 above, the software will find in the first "A50" Cross-Reference for OI 500, Dispense Drug 100. The software will then loop through all the “A526” and “A527” Cross-References in the DRUG file (#50) to find the IV Additives 3, 4 and 5. In the second “A50” Cross-Reference for OI 500, Dispense Drug 200 is identified. The software will again loop through any existing “A526” and “A527” Cross-references in the DRUG file (#50) to find IV Solution 10.

If the Orderable Item pointer for Dispense Drug 100 is edited from 500 to 600, the Cross-Reference in the DRUG file (#50) the following logic will be performed.

- Kill Logic

> Kill the Cross-Reference ^PS(50.7,"A50",500,100) using DA and old value (X=500), where DA equals the IEN of the Dispense Drug and X equals the IEN of the Orderable Item

> The Cross-References would now be as follows.

> ^PS(50.7,"A50",500,200)=""

> ^PSDRUG("A526",100,3)=""

> ^PSDRUG("A526",100,4)=""

> ^PSDRUG("A526",100,5)=""

> ^PSDRUG("A527",200,10)=""

> The ‘A50” and “A527” Cross-references now identify Orderable Item 500 to be pointed to by Dispense Drug 200 and IV Solution 10. The Orderable Item update for OI 500 is then performed for Dispense Drug 200 and IV solution 10.

> While still in the Kill logic, the PHARMACY ORDERABLE ITEM field (#15) in the IV ADDITIVES file (#52.6) is set to null for IV Additives 3, 4, and 5. This action results in the deletion of Cross-References on the PHARMACY ORDERABLE ITEM field (#15) of the IV ADDITIVES file (#52.6).

- Set Logic

> The “A50” Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7) for the new Orderable Item 600 is set as follows.

> ^PS(50.7,"A50",500,200)=""

> ^PS(50.7,"A50",600,100)=""

> ^PSDRUG("A526",100,3)=""

> ^PSDRUG("A526",100,4)=""

> ^PSDRUG("A526",100,5)=""

> ^PSDRUG("A527",200,10)=""

> The Orderable Item logic is executed on the new OI 600 by looping on the "A50" Cross-Reference, to get the Dispense Drug pointer of 100. The software then loops through any existing “A526” and “A527” Cross-References to get IV Additives 3, 4 and 5.

> The value of the PHARMACY ORDERABLE ITEM (#15) field in the IV ADDITIVES file (#52.6) for IV Additives 3, 4, and 5 is set to 600. Existing Cross-References are also set to reflect this change.

Scenario 2: The Dispense Drug Pointer Is Edited For An IV Additive Or IV Solution

If the Dispense Drug is changed for an IV Additive or IV Solution, the Cross-References on the PHARMACY ORDERABLE ITEM field in the IV ADDITIVES file (#52.6) and IV SOLUTION file (#52.7) will perform the following set and kill logic.

- Kill Logic

> First, the "A526" or "A527" Cross-References in the DRUG file (#50) will be killed. Then, using DA, which is equal to the Orderable Item IEN, the software will get the old Orderable Item pointer value and perform the Orderable Item logic on the old Orderable Item. Subsequently, the value in the PHARMACY ORDERABLE ITEM field for the IV Additive and/or IV Solution will be set to null and the existing Cross-References on this field will be killed.

- Set Logic

> First, the "A526" or "A527" Cross-References in the DRUG file (#50) will be set. Then Using X, which is equal to the Dispense Drug IEN, the software will identify the new Orderable Item in the DRUG file (#50) and perform the OI logic on that Orderable Item. The PHARMACY ORDERABLE ITEM field in the IV ADDITIVES file (#52.6) and IV SOLUTION file (#52.7) will be set to the new value and existing Cross-References will be also set.

![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/009.png)Users can first check the new Dispense Drug, and if the Orderable Item does not change by rematching the Additive/Solution to the new Dispense Drug, they can choose the QUIT command.

Example 2:IV Additives/IV Solution Dispense Drugs Orderable Item

IEN 3 points to =\> IEN 100 points to =\> 500

IEN 4 points to =\> IEN 100 points to =\> 500

IEN 5 points to =\> IEN 100 points to =\> 500

IEN 10 points to =\> IEN 200 points to =\> 500

Cross-References ^PS(50.7,"A50",500,100)=""

> ^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,3)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

> ^PSDRUG("A527",200,10)=""

For example, the USED IN IV FLUID ORDER ENTRY field (#17) in the IV ADDITIVES file (#52.6) for IV Additive 3 could be edited. The Orderable Item that the IV Additive points to in this case, is 500. Both the Kill and Set logic (same logic) for the OI 500 is updated by looping through the "A50" Cross-Reference in the PHARMACY ORDERABLE ITEM file (#50.7), finding each Dispense Drug IEN, and going through the "A526" and "A527" Cross-References in the DRUG file (#50) for that Dispense Drug. This process is then repeated for the next Dispense drug identified in the “A50” Cross-Reference

If the DRUG file (#50) pointer for IV Additive 3 were changed from Dispense Drug 100 to Dispense Drug 900, the Cross-Reference on the Dispense Drug Pointer would be killed.

- Kill Logic

> Using old value of X, which equals the Dispense Drug 100 and DA, which equals the IV ADDITIVE 3, the software would kill Cross-Reference ^PSDRUG("A526",100,3) with the following Cross-References remaining.

^PS(50.7,"A50",500,100)=""

> ^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

^PSDRUG("A527",200,10)=""

> Using DA, the software would get the old Orderable Item pointer of 500 and execute the Orderable Item logic for Dispense Drugs 100, IV Additives 4 and 5, Dispense Drug 200, and IV Solution 10.

> The value for the PHARMACY ORDERABLE ITEM field (#15) in the IV ADDITIVES file (#52.6) would be set to null and Cross-References on this field would be deleted.

- Set Logic

> Using new value X, where X equals the Dispense Drug 900, the software would set the new "A526" Cross Reference as ^PSDRUG("A526",900,3)="", The updated Cross-References are as follows

^PS(50.7,"A50",500,100)=""

> ^PS(50.7,"A50",500,200)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

> ^PSDRUG("A526",900,3)=""

^PSDRUG("A527",200,10)=""

> Using new value of X, where X equals the Dispense Drug 900, the software gets the Orderable Item pointer for Dispense Drug 900, in this example, Orderable Item 2000. The applicable Cross-References would be the following.

^PS(50.7,"A50",500,100)=""

> ^PS(50.7,"A50",500,200)=""

> ^PS(50.7,"A50",2000,900)=""

^PSDRUG("A526",100,4)=""

^PSDRUG("A526",100,5)=""

> ^PSDRUG("A526",900,3)=""

^PSDRUG("A527",200,10)=""

> The software performs the OI update for Orderable Item 2000, with Dispense Drug 900 and IV Additive 3. The PHARMACY ORDERABLE ITEM field (#15) value in the IV ADDITIVES file (#52.6) is set to 2000. The corresponding Cross-References on this field are also set.

# Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PDM package does not contain any VA FileMan security codes except for programmer security (@) on the data dictionaries for the PDM files. Security with respect to standard options in the module is implemented by carefully assigning options to users and by the use of security keys.

## Mail Groups 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*147 creates a new mail group called PSS ORDER CHECKS. The mail group description below was retrieved from VA FileMan. The IRM Pharmacy support and Pharmacy ADPACs (and backups) should at a minimum be added to this mail group.

NAME: PSS ORDER CHECKS

TYPE: public

DESCRIPTION: Members of this mail group will receive various notifications

that impact Enhanced Order Checks (drug-drug interactions, duplicate therapy

and dosing checks) introduced with PRE V. 0.5 utilizing a COTS database.

Patch PSS\*1\*227 creates a new mail group called PSS DEE AUDIT. The mail group description below was retrieved from VA FileMan. This mail group should include anyone who should be notified when changes are made to the DRUG file (#50). For more information on this mail group, refer to the *Pharmacy Data Management Manager’s User Manual*.

NAME: PSS DEE AUDIT

TYPE: public

DESCRIPTION: Members of this mail group will receive audit notifications

when certain fields are viewed or changed in the DRUG file (#50).

## Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no alerts in the PDM package.

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bulletins are 'Super' messages. Each Bulletin has a text and a subject just like a normal message. But embedded within either the subject or the text can be variable fields that can be filled in with parameters. There is also a standard set of recipients in the form of a Mail Group that is associated with the bulletin.

Bulletins are processed by MailMan either because of either a special type of cross reference or a direct call in a routine. The interface for the direct call is described in the documentation on programmer entry points. FileMan sets up code that will issue a bulletin automatically when the special cross reference type is created. In either case the parameters that go into the text and/or the subject make each bulletin unique.

NAME: PSS FDB INTERFACE

SUBJECT: ORDER CHECK DATABASE DOWN

RETENTION DAYS: 3

PRIORITY?: YES

NAME: PSS FDB INTERFACE RESTORED

SUBJECT: ORDER CHECK DATABASE IS BACK UP

RETENTION DAYS: 3

PRIORITY?: YES

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PDM does not transmit data to any remote system or facility.

## Archiving/Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving and purging functions necessary with the PDM package.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites utilizing the PDM package should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Security Officer (RISO).

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specialized products embedded within or required by the PDM package.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No electronic signatures are utilized in the PDM package.

## Locked Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section relates only to options that are locked. For a complete listing of The PDM options listed in the PSS MGR Menu structure, refer to the [Menu/Options](#menuoptions) section of this document.

![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/010.png) Locked: PSXCMOPMGR

Without the PSXCMOPMGR key the *CMOP Mark/Unmark (Single drug)* option will not appear on your menu.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PSS ORDER CHECKS security key is used to control access to the Enable/Disable Dosing Order Checks \[PSS DOSING ORDER CHECKS\] option.

In order to mark or edit package specific fields in a DRUG file (#50) entry, the user must hold the corresponding package key. The keys are assigned for the individual packages. PDM does not export any of these keys.

<u>Package</u><u>Keys</u>

> Outpatient Pharmacy PSORPH

> Inpatient Medications PSJU MGR

> Inpatient Medications PSJI MGR

> Automatic Replenishment/Ward Stock PSGWMGR

> Drug Accountability/Inventory Interface PSAMGR

> Drug Accountability/Inventory Interface PSA ORDERS

> Controlled Substances PSDMGR

> National Drug File PSNMGR

> Consolidated Mail Outpatient Pharmacy PSXCMOPMGR

Patch PSS\*1\*147 exports the following four security keys, that will be used by the Pharmacy Enterprise Customization System (PECS) application. Only a few users who will be granted access to the PECS application will need one or more keys assigned based on their role. Assignment of these keys should be by request only. The security key descriptions were retrieved from VA FileMan.

NAME: PSS_CUSTOM_TABLES_ADMIN

DESCRIPTIVE NAME: ADMINISTRATOR

DESCRIPTION: This key is used by the Pharmacy Enterprise Customization System (PECS) web application. Holders of this key will have the ability to perform configuration and administrative tasks for the application. They will also have querying capabilities.

NAME: PSS_CUSTOM_TABLES_APPROVER

DESCRIPTIVE NAME: APPROVER

DESCRIPTION: This key is used by the Pharmacy Enterprise Customization System (PECS) web application. Holders of this key will have the same privileges as those with the PSS CUSTOM TABLES REQUESTOR key. Additional capabilities will be to review, approve, delete or reject customization requests and to view and generate reports.

NAME: PSS_CUSTOM_TABLES_REL_MAN

DESCRIPTIVE NAME: RELEASE MANAGER

DESCRIPTION: This key is used by the Pharmacy Enterprise Customization System (PECS) web application. Holders of this key will have the ability to create file updates for FDB database tables to be applied at local facilities. They will also have querying capabilities.

NAME: PSS_CUSTOM_TABLES_REQUESTOR

DESCRIPTIVE NAME: REQUESTOR

DESCRIPTION: This key is used by the Pharmacy Enterprise Customization System (PECS) web application. Holders of this key will be allowed to enter customization requests, display and view the status of their own requests. They will also have limited querying capabilities

Five security keys were introduced with Patch PSS\*1\*167 that will be used to authenticate users accessing the Pharmacy Product System-National (PPS-N) using Kernel Authentication and Authorization for J2EE (KAAJEE). Users requiring access to the Pharmacy Product System-National should be assigned these keys as appropriate to their level of approved access. PPS-N is a reengineered product that will replace the National Drug File Management System (NDFMS). Site users may be assigned the PSS_PPSN_VIEWER key only. The other four security keys are only to be assigned to members of the National NDF Management Group.

NAME: PSS_PPSN_MANAGER

DESCRIPTIVE NAME: PPS-National Manager

DESCRIPTION: This role can perform the operational functions in PPS-N but doesn't have the administrative rights of the PPS-N National Supervisor.

NAME: PSS_PPSN_MIGRATOR

DESCRIPTIVE NAME: PPS-National Migration User

DESCRIPTION: This role has the ability to run the PPS-N Migration.

NAME: PSS_PPSN_SECOND_APPROVER

DESCRIPTIVE NAME: PPS-National Second Approver

DESCRIPTION: This role has the ability to do a second approval on items that are in the pending second approval state.

NAME: PSS_PPSN_SUPERVISOR

DESCRIPTIVE NAME: PPS-National Supervisor

DESCRIPTION: This role has the ability to perform all actions in the PPS-N application, including Administration and Configuration.

NAME: PSS_PPSN_VIEWER

DESCRIPTIVE NAME: PPS-National Viewer

DESCRIPTION: This role has the ability to log in and view items in the PPS-N Application but cannot modify any of the items.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information about all files, including these, can be obtained by using the VA FileMan to generate a list of file attributes.

### PDM Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 44%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong><u>File Names</u></strong></th>
<th><strong><u>DD</u></strong></th>
<th><strong><u>RD</u></strong></th>
<th><strong><u>WR</u></strong></th>
<th><strong><u>DEL</u></strong></th>
<th><strong><u>LAYGO</u></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>50</td>
<td>DRUG</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>50.4</td>
<td>DRUG ELECTROLYTES</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>50.606</td>
<td>DOSAGE FORM</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>50.7</td>
<td>PHARMACY ORDERABLE ITEM</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>51</td>
<td>MEDICATION INSTRUCTION</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>51.1</td>
<td>ADMINISTRATION SCHEDULE</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>51.2</td>
<td>MEDICATION ROUTES</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>51.23</td>
<td>STANDARD MEDICATION ROUTES</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>51.24</p>
<p>51.25</p></td>
<td><p>DOSE UNITS</p>
<p>DOSE UNIT CONVERSION</p></td>
<td><p>@</p>
<p>@</p></td>
<td><p>Pp</p>
<p>Pp</p></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>51.5</td>
<td>ORDER UNIT</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>51.7</td>
<td>DRUG TEXT</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>52.6</td>
<td>IV ADDITIVES</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>52.7</td>
<td>IV SOLUTIONS</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>53.47</td>
<td>IFUSION INSTRUCTIONS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>54</td>
<td>RX CONSULT</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>55</td>
<td>PHARMACY PATIENT (Partial ID)</td>
<td>@</td>
<td>P</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^</td>
<td>^</td>
<td>^</td>
<td>^</td>
<td>^</td>
</tr>
<tr class="odd">
<td>59.7</td>
<td>PHARMACY SYSTEM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>59.73</td>
<td>VENDOR DISABLE/ENABLE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>59.74</td>
<td>VENDOR INTERFACE DATA</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Non-PDM Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 44%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>File</u></strong></p>
<p><strong><u>Numbers</u></strong></p></th>
<th><strong><u>File Names</u></strong></th>
<th><strong><u>DD</u></strong></th>
<th><strong><u>RD</u></strong></th>
<th><strong><u>WR</u></strong></th>
<th><strong><u>DEL</u></strong></th>
<th><strong><u>LAYGO</u></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>200</td>
<td>NEW PERSON (Partial DD)</td>
<td>#</td>
<td>#</td>
<td>#</td>
<td>#</td>
<td>#</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>9009032.3</td>
<td>APSP INTERVENTION TYPE</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>9009032.4</td>
<td>APSP INTERVENTION</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>9009032.5</td>
<td>APSP INTERVENTION RECOMMENDATION</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](pharmacy-data-management-technical-manual-security-guide-pss-1-0-p247/011.png)Please refer to the "Sending Security Codes." section of the Kernel V. 8.0 Systems Manual for more information concerning installation of security codes.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no regulations or directives related to the Pharmacy Data Management package. Additional manuals related to the Pharmacy Data Management package can be found at the VistA Documentation Library (VDL) on the Internet.

# Appendix A: Pharmacy Interface Automation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction appendix provides a brief description of the new features and functions of the Pharmacy Interface Automation project. This projects consist of multiple patches, which must be installed for the functionality to perform.

The Clinical Ancillary Services (CAS) Development Delivery of Pharmacy enhancements (DDPE) Pharmacy Interface Automation project supports the initiative to create an automated interface between the Pharmacy Automated Dispensing Equipment (PADE) used in the inpatient and outpatient care settings and VistA Pharmacy and Admission Discharge Transfer (ADT) applications. This will allow VA health care users the ability to access, transmit, receive alerts, and generate reports on medication transactions.

Pharmacy Interface Automation is a vital enhancement to the medication transaction functions of the PADE. It allows pharmacists to access dispensing equipment remotely; keep a perpetual inventory of all medication received, dispensed, and wasted; alert the pharmacy of medication removed from the devices without orders; and establishes monitors for potentially inappropriate electronic pharmacy transactions.

This product shall run on standard hardware platforms used by the Department of Veterans Affairs (VA) Healthcare facilities.

The minimum required VistA software is:

| Package                                        | Minimum Version Needed |
|----------------------------------------------------|----------------------------|
| Adverse Reaction Tracking (ART)                    | 4.0                        |
| BCMA                                               | 3.0                        |
| Computerized Patient Record System (CPRS)          | 3.0                        |
| Controlled Substance                               | 3.0                        |
| Drug Accountability                                | 3.0                        |
| VA FileMan                                         | 22.0                       |
| HL7                                                | 2.4                        |
| Inpatient Medications (IP)                         | 5.0                        |
| Kernel                                             | 8.0                        |
| MailMan                                            | 7.1                        |
| Master Patient Index/Patient Demographics (MPI/PD) | 1.0                        |
| National Drug File (NDF)                           | 4.0                        |
| Nursing Service                                    | 4.0                        |
| Order Entry/Results Reporting (OERR)               | 3.0                        |
| Registration                                       | 5.3                        |
| Pharmacy Data Management (PDM)                     | 1.0                        |
| Remote Procedure Call (RPC) Broker                 | 1.1                        |
| Scheduling                                         | 5.3                        |

## New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new automated bidirectional interface between VistA and PADE has been designed and developed utilizing VIE as the middleware component for communication of HL7 messages and error handling. The added functional components are:

- Provide pharmacists the capability to remotely access dispensing equipment to provide the pharmacist the status of drugs: whether they have been dispensed, or in the queue or some error condition that may have been encountered by the dispensing equipment.
- Provide PADE the capability to transmit dispensing information to VistA Pharmacy to keep a perpetual inventory of all drugs/medications received, dispensed, and wasted.
- Provide PADE the capability to alert VistA Pharmacy of medication removal from PADE without orders.
- Establish monitors of all potentially inappropriate electronic pharmacy transactions. Implement trending reports in order to address and detect potentially inappropriate pharmacy transactions, such as drug diversion. For example, reports include the ability to sort transactions by nursing, user, drug, etc., and from the VA-side of the interface.

Refer to the following Pharmacy Interface Automation documents for additional information:

(will add hyperlinks once these are in final folder or on TSPR)

- Pharmacy Interface Automation Installation Guide
- Pharmacy Interface Automation User Guide
- Pharmacy Interface Automation System Design Document
- Pharmacy Interface Automation Data Dictionary

## Options and Build Components 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the options and build components for Pharmacy Interface Automation for PSS\*1.0\*193:

Select OPTION NAME:    XPD PRINT BUILD     Build File Print

Build File Print

Select BUILD NAME: PSS\*1.0\*193       PHARMACY DATA MANAGEMENT

DEVICE: HOME// ;;99999  SSH VIRTUAL TERMINAL

PACKAGE: PSS\*1.0\*193     Nov 25, 2015 10:27 am                           PAGE 1

-------------------------------------------------------------------------------SINGLE PACKAGE                               TRACK NATIONALLY: YES

NATIONAL PACKAGE: PHARMACY DATA MANAGEMENT       ALPHA/BETA TESTING: NO

As part of this patch PSS\*1\*193, the following enhancements were made:

1.  Two new protocols PSS MFNM01 CLIENT and PSS MFNM01 SERVER were added to facilitate sending MFN HL7 drug messages to PADE.
2.  The Send Entire Drug File to External Interface \[PSS MASTER FILE ALL\]  option was modified to allow transmission of the drug file to an Inpatient Interface (PADE) depending on the PADE setup. It also provides the flexibility of sending all drugs marked for Unit Dose, IV or Ward Stock or send selected drugs to PADE.

> Since this option now allows to send all or selected drugs to PADE, the option name "Send Entire Drug File to External Interface" was changed  to "Send Drug File Entries to External Interface"

3.  A new PSS PADE INIT security key was added so that holders of this key can only send "all" drugs to PADE noted in item 2.
4.  Option Drug Enter/Edit \[PSS DRUG ENTER/EDIT\] was modified to send an addition/update/both or none to PADE provided it is setup to receive such updates.

ENVIRONMENT CHECK:                               DELETE ENV ROUTINE:

 PRE-INIT ROUTINE:                          DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE:                         DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

ROUTINE:                                       ACTION:

   PSSDEE                                         SEND TO SITE

   PSSHLDFS                                       SEND TO SITE

   PSSMSTR                                        SEND TO SITE

OPTION:                                        ACTION:

   PSS MASTER FILE ALL                            SEND TO SITE

SECURITY KEY:                                  ACTION:

   PSS PADE INIT                                  SEND TO SITE

PROTOCOL:                                      ACTION:

   PSS MFNM01 CLIENT                              SEND TO SITE

   PSS MFNM01 SERVER                              SEND TO SITE

REQUIRED BUILDS:                               ACTION:

   PSS\*1.0\*180                                    Don't install, leave global

CDEVISC1A2:DVA\>

## Modified and New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are for PSS\*1\*193:

PSSDEE 

PSSHLDFS

PSSMSTR

*(This page included for two-sided copying.)*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Administration Schedule File</strong></th>
<th>The ADMINISTRATION SCHEDULE file (#51.1) contains administration schedule names and standard dosage administration times. The name is a common abbreviation for an administration schedule (e.g., QID, Q4H, PRN). The administration time is entered in military time.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CPRS</strong></td>
<td>A VistA computer software package called Computerized Patient Record System. CPRS is an application in VistA that allows the user to enter all necessary orders for a patient in different packages from a single application.</td>
</tr>
<tr class="even">
<td><strong>DATUP</strong></td>
<td>Functionality that allows the Pharmacy Enterprise Customization System (PECS) to send out custom and standard commercial-off-the-shelf (COTS) vendor database changes to update the two centralized databases at Austin and Martinsburg.</td>
</tr>
<tr class="odd">
<td><strong>Dispense Drug</strong></td>
<td>The Dispense Drug is pulled from DRUG file (#50) and usually has the strength attached to it (e.g., Acetaminophen 325 mg). Usually, the name alone without a strength attached is the Pharmacy Orderable Item name.</td>
</tr>
<tr class="even">
<td><p><strong>Dosage Form File</strong></p>
<p><strong>Dose Unit Conversion File</strong></p></td>
<td><p>The DOSAGE FORM file (#50.606) contains all dosage forms and associated data that are used by Pharmacy packages and CPRS. The dosage form is used in SIG construction, default values and in the determination of the type of each dosage created for each application.</p>
<p>The DOSE UNIT CONVERSION file (#51.25) was created to convert one dose unit to another using a conversion factor so that a comparison can be made between two dose units when they are not equivalent.  The dose unit used for the Dosing Order Check may not be the same dose unit First Databank (FDB) returns with the Dosing Order Check results.</p></td>
</tr>
<tr class="odd">
<td><strong>Dose Unit File</strong></td>
<td>The DOSE UNIT file (#51.24) was created to accomplish the mapping to First Data Bank (FDB). All entries in this file have been mapped to an FDB Dose Unit. Although this file has not yet been standardized by Standards and Terminology Services (STS), no local editing will be allowed. When populating the Dose Unit field for a Local Possible Dosage in the DRUG file (#50), selection will be from this new file.</td>
</tr>
<tr class="even">
<td><strong>Drug Electrolytes File</strong></td>
<td>The DRUG ELECTROLYTES file (#50.4) contains the names of anions/cations, and their cations and concentration units.</td>
</tr>
<tr class="odd">
<td><strong>Drug File</strong></td>
<td>The DRUG file (#50) holds the information related to each drug that can be used to fill a prescription or medication order. It is pointed to from several other files and should be handled carefully, usually only by special individuals in the Pharmacy Service. Entries are not typically deleted, but rather made inactive by entering an inactive date.</td>
</tr>
<tr class="even">
<td><strong>Drug Text File</strong></td>
<td>The DRUG TEXT file (#51.7) stores rapidly changing drug restrictions, guidelines, and protocols to help assure medications are being used according to defined specifications.</td>
</tr>
<tr class="odd">
<td><strong>Infusion Instructions File</strong></td>
<td>The INFUSION INSTRUCTIONS file (#53.47) holds abbreviations used when entering the Infusion Rate (#.08) field in the IV (#100) multiple of the PHARMACY PATIENT (#55) FILE, AND THE infusion rate (#59) FIELD IN THE non-verified orders (#53.1) file. Each record holds an expansion of the abbreviation which replaces the abbreviation in the Infusion Rate at the time the IV order is created.</td>
</tr>
<tr class="even">
<td><strong>IV Additives File</strong></td>
<td>The IV ADDITIVES file (#52.6) contains drugs that are used as Additives in the IV room. Data entered includes drug generic name, print name, drug information, synonym(s), dispensing units, cost per unit, days for IV order, usual IV schedule, administration times, electrolytes, and quick code information.</td>
</tr>
<tr class="odd">
<td><strong>IV Solutions File</strong></td>
<td>The IV SOLUTIONS file (#52.7) contains drugs that are used as primary solutions in the IV room. The solution must already exist in the Drug file (#50) to be selected. Data in this file includes: drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.</td>
</tr>
<tr class="even">
<td><strong>Local Possible Dosages</strong></td>
<td>Local Possible Dosages are free text dosages that are associated with drugs that do not meet all of the criteria for Possible Dosages.</td>
</tr>
<tr class="odd">
<td><strong>Medication Instruction File</strong></td>
<td>The MEDICATION INSTRUCTION file (#51) is used by Unit Dose and Outpatient Pharmacy. It contains the medication instruction name, expansion and intended use.</td>
</tr>
<tr class="even">
<td><strong>Medication Routes File</strong></td>
<td>The MEDICATION ROUTES file (#51.2) contains medication route names. The user can enter an abbreviation for each route to be used at their site. The abbreviation will most likely be the Latin abbreviation for the term.</td>
</tr>
<tr class="odd">
<td><strong>Medication Routes/Abbreviations</strong></td>
<td>The Medication RouteS file (#51.2) contains the medication routes and abbreviations, which are selected by each Department of Veterans Affairs Medical Centers (VAMC). The abbreviation cannot be longer than five characters to fit on labels and the Medical Administration Record (MAR). The user can add new routes and abbreviations as appropriate.</td>
</tr>
<tr class="even">
<td><strong>MOCHA</strong></td>
<td>Medication Order Check Healthcare Application.</td>
</tr>
<tr class="odd">
<td><strong>National Drug File</strong></td>
<td>The National Drug File provides standardization of the local drug files in all VA medical facilities. Standardization includes the adoption of new drug nomenclature and drug classification and links the local drug file entries to data in the National Drug File. For drugs approved by the Food and Drug Administration (FDA), VA medical facilities have access to information concerning dosage form, strength and unit; package size and type; manufacturer’s trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among medical facilities.</td>
</tr>
<tr class="even">
<td><strong>Non-Formulary Drugs</strong></td>
<td>Drugs that are not available for use by all providers.</td>
</tr>
<tr class="odd">
<td><strong>Orderable Item</strong></td>
<td>An Orderable Item is pulled from the PHARMACY ORDERABLE ITEM file (#50.7) and usually has no strength attached to it (e.g., Acetaminophen). The name, with a strength attached, is the Dispense Drug name (e.g., Acetaminophen 325mg).</td>
</tr>
<tr class="even">
<td><strong>Orderable Item File</strong></td>
<td>The ORDERABLE ITEM file (#101.43) is a CPRS file that provides the Orderable Items for selection within CPRS. Pharmacy Orderable Items are a subset of this file.</td>
</tr>
<tr class="odd">
<td><strong>PECS</strong></td>
<td>Pharmacy Enterprise Customization System. A Graphical User Interface (GUI) web-based application used to research, update via DATUP, maintain, and report VA customizations of the commercial-off-the-shelf (COTS) vendor database used to perform Pharmacy order checks such as drug-drug interactions, duplicate therapy, and dosing.</td>
</tr>
<tr class="even">
<td><strong>PEPS</strong></td>
<td>Pharmacy Enterprise Product Services. A suite of services that includes Outpatient and Inpatient services.</td>
</tr>
<tr class="odd">
<td><strong>Pending Order</strong></td>
<td>A pending order is one that has been entered by a provider through CPRS without Pharmacy finishing the order. Once Pharmacy has finished (and verified for Unit Dose only) the order, it will become active.</td>
</tr>
<tr class="even">
<td><strong>Pharmacy Orderable Item</strong></td>
<td>The Pharmacy Orderable Item is used through CPRS to order Inpatient Medications and Outpatient Pharmacy prescriptions.</td>
</tr>
<tr class="odd">
<td><strong>Pharmacy Orderable Item File</strong></td>
<td>The PHARMACY ORDERABLE ITEM file (#50.7) contains the Order Entry name for items that can be ordered in the Inpatient Medications and Outpatient Pharmacy packages.</td>
</tr>
<tr class="even">
<td><strong>Possible Dosages</strong></td>
<td>Dosages that have a numeric dosage and numeric Dispense Units Per Dose appropriate for administration. For a drug to have possible dosages, it must be a single ingredient product that is matched to VA PRODUCT file (#50.68). The VA PRODUCT file (#50.68) entry must have a numeric strength and the dosage form/unit combination must be such that a numeric strength combined with the unit can be an appropriate dosage selection.</td>
</tr>
<tr class="odd">
<td><strong>Prompt</strong></td>
<td>A point at which the system questions the user and waits for a response.</td>
</tr>
<tr class="even">
<td><strong>Standard Medication Route File</strong></td>
<td>The STANDARD MEDICATION ROUTE file (#51.23) was created to map Local Medication Routes in VistA to an FDB Route in order to perform dosage checks in PRE V.0.5. This file has been standardized by Standards and Terminology Service (STS) and is mapped to an FDB Route. It cannot be edited locally.</td>
</tr>
<tr class="odd">
<td><strong>Standard Schedule</strong></td>
<td>Standard medication administration schedules are stored in the Administration Schedule file (#51.1).</td>
</tr>
<tr class="even">
<td><strong>Units Per Dose</strong></td>
<td>The Units Per Dose is the number of Units (tablets, capsules, etc.) to be dispensed as a dose for an order. Fractional numbers will be accepted.</td>
</tr>
<tr class="odd">
<td><strong>VA Drug Class Code</strong></td>
<td>A drug classification system used by VA that separates drugs into different categories based upon their characteristics. Some cost reports can be run for VA Drug Class Codes.</td>
</tr>
<tr class="even">
<td><strong>VA Product File</strong></td>
<td>The VA PRODUCT file (#50.68) contains a list of available drug products.</td>
</tr>
</tbody>
</table>
