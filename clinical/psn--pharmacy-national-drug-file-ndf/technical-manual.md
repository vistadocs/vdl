---
consolidated_title: "national drug file technical manual"
app_code: PSN
doc_type: TM
master_source: "National Drug File Version 4 Technical Manual (Updated PSN*4*575)"
master_pub_date: October 1998
consolidated_from: 3 versions
prior_versions:
  - "National Drug File Version 4 Technical Manual (Updated PSN*4.0*576)"
  - "National Drug File Version 4 Technical Manual (Updated PSN*4*218)"
---

> ![](national-drug-file-version-4-technical-manual-updated-psn-4-575/001.png)

National Drug File  
(NDF)

Technical Manual

October 1998

(Revised July 2024)

Office of Enterprise Development

Revision History

The table below lists changes made since the initial release of this manual. Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. Either update the existing manual with the Change Pages document, or replace it with the updated manual.

<table style="width:100%;">
<colgroup>
<col style="width: 1%" />
<col style="width: 10%" />
<col style="width: 1%" />
<col style="width: 14%" />
<col style="width: 1%" />
<col style="width: 15%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 53%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Date</th>
<th colspan="2">Revised Pages</th>
<th colspan="2">Patch Number</th>
<th colspan="3">Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">07/24</td>
<td colspan="2"><a href="#p035">35</a>, <a href="#p039">39</a> <a href="#p040">40</a> - <a href="#p041">41</a></td>
<td colspan="3">PSN*4.0*575</td>
<td colspan="3">Added reference to ECDSA encryption key, removed reference to DSA encryption key which is no longer supported</td>
</tr>
<tr class="even">
<td colspan="2">11/17</td>
<td colspan="2"><p>I, 6-10,</p>
<p>16-49, 56-57</p></td>
<td colspan="2">PSN*4*513</td>
<td colspan="3"><p>Updated Revision History and Glossary.</p>
<p>Added new routines and related menu options.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">08/17</td>
<td colspan="2"><p>i-vi,</p>
<p>1-2</p>
<p>5</p>
<p>6</p>
<p>59</p></td>
<td colspan="2">PSN*4*396</td>
<td colspan="3"><p>Updated Revision History &amp; TOC</p>
<p>Add CLNICAL EFFECTS OF DRUGS file additions to VA PRODUCT FILE #50.68</p>
<p>Added PPS-N information</p>
<p>Added PPS-N UPDATE CONTROL FILE</p>
<p>Add Routine PSNCLEHW</p>
<p>Updated Index</p>
<p><mark>REDACTED</mark></p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">05/10</td>
<td colspan="2">i-ii, 6, 7,<br />
17-18</td>
<td colspan="2">PSN*4*108</td>
<td colspan="3"><p>Added routines PSNFDAMG, and PSNMEDG to the list of routines. Routine PSNAPIS was modified.</p>
<p>Added new option Display FDA Medication Guide [PSN MED GUIDE].</p>
<p>Added FDA Medication Guide to the Glossary.</p>
<p><mark>REDACTED</mark></p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">02/09</td>
<td colspan="2">6, 10, 10b, 12e-f</td>
<td colspan="2">PSN*4*169</td>
<td colspan="3"><p>Added routines PSNEN169 and PSNPO169.</p>
<p>Described section added to the VA Product message as part of an NDF Management System change.</p>
<p>Updated Notes Regarding Patches section.</p>
<p><mark>REDACTED</mark></p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">02/06</td>
<td colspan="2">6</td>
<td colspan="2">PSN*4*109</td>
<td colspan="3">Added routine PSN5067 to the list of routines. <mark>REDACTED</mark></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">08/05</td>
<td colspan="2">iii, 6, 10b, 12c-d, 15, 21, 22</td>
<td colspan="2">PSN*4*101</td>
<td colspan="3">Added routines PSNVUID and PSNPREDS, an explanation of the data standardization project in a new section called Notes regarding Patches; moved changes to CS Federal Schedule field (patch PSN*4*65) to new section; updated Table of Contents, Glossary and Index. <mark>REDACTED</mark></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">10/04</td>
<td colspan="2">i, 2, 6, 8</td>
<td colspan="2">PSN*4*80</td>
<td colspan="3">Added routines and a reference to the <em>Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual</em> created for the Pharmacy Re-Engineering (PRE) project Encapsulation cycle 1</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">09/03</td>
<td colspan="2">7</td>
<td colspan="2">PSN*4*70</td>
<td colspan="3">Added two new options to the list of exported options.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">07/03</td>
<td colspan="2">Title Page, i-ii, 10b</td>
<td colspan="2">PSN*4*65</td>
<td colspan="3">Noted changes to CS Federal Schedule field.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">04/03</td>
<td colspan="2">Title Page, i, 15</td>
<td colspan="2">PSN*4*20</td>
<td colspan="3">Changed the RD access on several files.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">04/03</td>
<td colspan="2">Title Page, i, 6</td>
<td colspan="2">PSN*4*68</td>
<td colspan="3">Added the PSNPPIO routine to the list of routines.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">02/03</td>
<td colspan="2">Title Page, i-iv, 4a-4d, 6</td>
<td colspan="2">PSN*4*62</td>
<td colspan="3"><p>-Replaced the Title Page, Revision History Page, and Table of Contents.</p>
<p>-Added the Patient Medication Information (PMI) Sheet enhancement files and printer set-up.</p>
<p>-Added print routine to the list of routines.</p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">10/02</td>
<td colspan="2">Title Page, i-iv, 12, 12a, 12b</td>
<td colspan="2">PSN*4*64</td>
<td colspan="3"><p>-Replaced the Title Page (and associated blank page) and the Revision History Page (and associated blank page).</p>
<p>-Added page numbers to the Revision History Pages and Table of Contents Pages.</p>
<p>- Updated the Electronic MailMan Messages for Drugs Unmatched from the National Drug File.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">10/02</td>
<td colspan="2">Title Page 10, 10a, 10b, 11, 12, 12a, 12b</td>
<td colspan="2">PSN*4*58</td>
<td colspan="3"><p>- Replaced the Title Page (and associated blank page) and the Revision History page (and associated blank page after it.)</p>
<p>- Updated the Electronic MailMan Messages for Data Update for NDF, Updated Interactions, and Drugs Unmatched from National Drug File. This included new screen captures and required the addition of new pages.</p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">09/01</td>
<td colspan="2">Title Page 10-12</td>
<td colspan="2">PSN*4*53</td>
<td colspan="3"><p>- Replaced the Title Page (and associated blank page) and the Revision History page (and associated blank page after it.)</p>
<p>- Added a new Electronic Mail Message for Updated Interactions and added new screen captures for the Electronic Mail Messages for Data Update and Drugs Unmatched from National Drug File.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">02/00</td>
<td colspan="2">6,7,9</td>
<td colspan="2">PSN*4*22</td>
<td colspan="3">Added a new option called <em>Inquire to National Files.</em></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">10/98</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="3">Original Released Technical Manual.</td>
<td></td>
</tr>
</tbody>
</table>

(This page included for two-sided copying.)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Pharmacy Product System – National (PPS-N)](#pharmacy-product-system-national-pps-n)
  - [Related Manuals](#related-manuals)
  - [Icons](#icons)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [The VA Drug Classification System](#the-va-drug-classification-system)
  - [Resource Requirements](#resource-requirements)
  - [Implementation Requirements](#implementation-requirements)
  - [System Configuration](#system-configuration)
  - [Assigning Keys, Menus, and Options](#assigning-keys-menus-and-options)
  - [Patient Medication Information (PMI) Sheet Redesign Enhancement](#patient-medication-information-pmi-sheet-redesign-enhancement)
- [Files](#files)
  - [Templates](#templates)
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [National Drug File V. 4.0 Menu](#national-drug-file-v-40-menu)
- [Archiving and Purging](#archiving-and-purging)
- [Callable Routines](#callable-routines)
- [External Interfaces](#external-interfaces)
- [External Relations](#external-relations)
  - [Data Base Integration Agreements (DBIAs)](#data-base-integration-agreements-dbias)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Electronic MailMan Messages](#electronic-mailman-messages)
- [Notes Regarding Patches](#notes-regarding-patches)
  - [## Note on CS Federal Schedule](#note-on-cs-federal-schedule)
- [Security Management](#security-management)
  - [PSNMGR Key](#psnmgr-key)
  - [Precautions and Potential Problems](#precautions-and-potential-problems)
  - [PSN PPS ADMIN Key](#psn-pps-admin-key)
  - [PSN PPS COORD Key](#psn-pps-coord-key)
- [Appendix A: PPS-N Update file configuration and specifications](#appendix-a-pps-n-update-file-configuration-and-specifications)
  - [Required Packages](#required-packages)
  - [Configuration](#configuration)
    - [Web Server and Service](#web-server-and-service)
    - [Secure Shell (SSH) protocol and Secure File Transfer Protocol (SFTP)](#secure-shell-ssh-protocol-and-secure-file-transfer-protocol-sftp)
    - [VMS Directory](#vms-directory)
    - [Linux Directories](#linux-directories)
    - [<u>PPS-N Site Parameters</u>](#upps-n-site-parametersu)
  - [## PPS-N Update file structure](#pps-n-update-file-structure)
    - [PMIDATA](#pmidata)
    - [DATA](#data)
    - [DATANT](#datant)
    - [DATAN](#datan)
    - [DATAO](#datao)
    - [PRODUCT](#product)
    - [GENERIC](#generic)
    - [POE](#poe)
    - [CMOP -](#cmop)
    - [NFI](#nfi)
    - [CLASS](#class)
    - [REM](#rem)
    - [MESSAGE](#message)
    - [MESSAGE2](#message2)
    - [TEXT](#text)
- [Glossary](#glossary)
- [Index](#index)
> The National Drug File (NDF) V. 4.0 software module provides standardization of the local drug files in all Department of Veterans Affairs Medical Centers (VAMCs). Standardization includes the adoption of new drug nomenclature and drug classification, and links the local drug file entries to data in the National Drug files.
> For drugs approved by the Food and Drug Administration (FDA), VAMCs have access to information concerning dosage form, strength and unit; package size and type; manufacturer’s trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among VAMCs.
> The NATIONAL DRUG file (#50.6) has been redesigned from a file seven multiples deep to a new file structure of four separate files. The new files are the VA PRODUCT file (#50.68), the NDC/UPN file (#50.67), the VA DISPENSE UNIT file (#50.64), and File \#50.6, which is now the VA GENERIC file.
> With this version of NDF, the new design of the NATIONAL DRUG file (#50.6) will lay the foundation for timely data releases by Pharmacy Benefits Management (PBM) personnel to field facilities using the NDF Management System. As new drug products are released, this information can be quickly sent to facilities. Pharmacy end users will be able to match (classify) a greater percentage of their local drug files for new products. Update/delivery of data will be controlled by PBM personnel. Frequent updating of NDF will be possible with minimal time for installation and downtime.
> In addition to the redesign of NATIONAL DRUG file (#50.6), Version 4.0 will provide the following enhancements:
- Addition of new fields to NDF, such as National Formulary and restriction indicators.
- Lay foundation for interfaces to other Commercial Off The Shelf (COTS) software to update NDF fields for new/revised drug information.
- Update current NDF with new/revised product information.
- Creation of an Application Programmer’s Interface (API) to accommodate all existing VistA software Database Integration Agreements (DBIAs) with NDF.
- A clean-up of associated files, such as DRUG MANUFACTURER (#55.95), DRUG UNITS (#50.607), etc.
- Incorporation of approved enhancement requests by Pharmacy/Information Resources Management (IRM) end users.
Patch PSN\*4\*396 added new fields for CLINICAL EFFECT OF DRUGS to the VA PRODUCT FILE (#50.68). These fields are in the multiple \#50.68108 and include PACKAGE (#.01), OMIT EXP/DC ORDER CHECK (#1), DURATION LIMIT (#2), WASTE SORT CODE (#104) and DOT SHIPPING CODE (#105).

## Pharmacy Product System – National (PPS-N)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With the release of PPS-N v3.0, the PPS-N system will provide update files for the National Drug File instead of the current Kernel Installation & Distribution System process. The update file names will be in the form PPS_xxPRV_xxNEW.DAT where xxPRV is the previous file number installed and xxNEW is the file number to be installed. For example, PPS_24PRV_25NEW.DAT would indicate that the 24 was the previous update file installed and 25 is the new one to be installed.

> National SQA and local sites will need to perform configuration activities prior to initiating the PPS-N/NDF Update process. This is discussed in detail under the *PPS-N Site Parameters (Enter/Edit) \[PSN PPS PARAM\]* option that is located in the National Drug File V. 4.0 User Manual. See Appendix A in this document for configuration and specifications for communications with PPS-N.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *National Drug File V. 4.0 Release Notes*

> *National Drug File V. 4.0 Installation Guide*

> *National Drug File V. 4.0 User Manual*

> *Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual*

## Icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Icons used to highlight key points in this manual are defined as follows:

![](national-drug-file-version-4-technical-manual-updated-psn-4-575/002.png) Indicates the user should take note of the information.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The VA Drug Classification System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Department of Veterans Affairs Drug Classification system was developed to provide a systematic management approach to the classification of medications, including investigational and over-the counter drugs, prosthetic items, and expendable supplies. The system was designed to do the following:

- Support the inpatient and outpatient pharmacy activities;
- Facilitate the identification of drug-drug, drug-allergy, drug-lab, and drug-food interactions;
- Uphold the requirements for inventory accountability; substantiate and improve all patient medication-related activity;
- Provide an improved database to assist the health care provider;
- Provide a coordinated method of database communication for VA management;
- Facilitate the monitoring of investigational drugs; and
- Facilitate the control of prosthetic and supply items.

> Each five-character alpha-numeric code specifies a broad classification and a specific type of product. The first two characters are letters and form the mnemonic for the major classification (e.g., AM for antimicrobials). Characters 3 through 5 are numbers and form the basis for sub-classification. For example, the classification system for the penicillin is as follows:

> AM000 ANTIMICROBIALS

> AM050 Penicillins

> AM051 Penicillin-G Related Penicillins

> AM052 Penicillins, Amino Derivatives

> AM053 Penicillinase-Resistant Penicillins

> AM054 Extended spectrum Penicillins

> The VA Drug Classification system classifies drug products, not generic ingredients. Drug products with local effects are classified by route of administration (e.g., dermatological, ophthalmic). If a product is not classified by route of administration, in most cases, it is classified under a specific chemical or pharmacological classification (e.g., beta-blockers, cephalosporin). If a product is not classified by route of administration, or chemical or pharmacological sub-classification, it may be classified under a therapeutic category (e.g., antilipemic agents, antiparkinson agents).

Most combination products are found in the “other” sub-classification under each major classification unless a specific subcategory for combination products has been added or a descriptive comment indicates inclusion elsewhere. In addition, products which are not adequately described by a minor category or subcategory within the major classification are classified as “other” (e.g., metronidazole and vancomycin are classified as “Anti-Infectives, Other”).

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following resources are required for the National Drug File software package:

> Routines

> PSN\* routines approx. 4636 bytes

## Implementation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no configurable site parameters involved in the implementation of this product. This module will not be distributed to field facilities. This module will only be installed on the system where the master National Drug files reside.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no site-specific parameters associated with NDF.

## Assigning Keys, Menus, and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The installer must enter users into the test and production accounts, assigning the PSNMGR option as the primary menu option. The PSNMGR key must be assigned to the package coordinator and/or their designee. This key unlocks the *Allow Unmatched Drugs To Be Classed* \[PSNSTCL\] and *LocalFormulary Report* \[PSNFRMLY\] menu options. Only users having this key will see these options on their menus.

## Patient Medication Information (PMI) Sheet Redesign Enhancement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PMI Sheet redesign is an enhancement to the NDF package V. 4.0. These enhancements support a new contract data source for Patient Medication Information that includes a new file structure.

> <u>Files</u>

> These files are part of a proprietary vendor database and are not part of the NDF core package. Patches PSN\*4\*67 and PSN\*4\*62 must be installed for the system to have access to these files.

| File Number | File Name             | Description                                                                                                                                                                                                                                |
|-------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 50.621      | PMI-ENGLISH           | This file contains the data provided by the vendor for PMIS monograph text entries in the English language. This file cannot be edited using FileMan options.                                                                              |
| 50.622      | PMI-SPANISH           | This file contains the data provided by the vendor for PMIS monograph text entries in the Spanish language. This file cannot be edited using FileMan options.                                                                              |
| 50.623      | PMI-MAP-ENGLISH       | This file contains data provided by the vendor required to map GCNSEQNO numbers to PMI-ENGLISH file (#50.621) monograph entries. This file cannot be edited using FileMan options.                                                         |
| 50.624      | PMI-MAP-SPANISH       | This file contains data provided by the vendor required to map GCNSEQNO numbers to PMI-SPANISH file (#50.622) monograph entries. This file cannot be edited using FileMan options.                                                         |
| 50.625      | WARNING LABEL-ENGLISH | This file contains the data provided by the vendor for WARNING LABEL monograph text entries in the English language. This file cannot be edited using FileMan options.                                                                     |
| 50.626      | WARNING LABEL-SPANISH | This file contains the data provided by the vendor for WARNING LABEL monograph text entries in the Spanish language. This file cannot be edited using FileMan options.                                                                     |
| 50.627      | WARNING LABEL MAP     | This file contains the data provided by the vendor, required to map GCNSEQNO numbers to WARNING LABEL-ENGLISH file (#50.625) and WARNING LABEL-SPANISH file (#50.626) monograph entries. This file cannot be edited using FileMan options. |

Set Up of the Patient Medication Information (PMI) Sheet Printers

> The installer must enter information for each printer that will be used to print PMI Sheets. This information controls the bolding of the sub-headings on the sheets.

> <u>Hardware Set Up</u>

> The printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.

> <u>Software Set Up</u>

> The type of printer will determine the next step. Please refer to the User’s Manual for each printer to establish the correct escape sequences for turning bolding on and off. These escape sequences are input to the following fields in the TERMINAL TYPE (#3.2) file:

> HIGH INTENSITY (BOLD) (#27) field

> NORMAL INTENSITY (RESET) (#29) field

<u>If these fields do not contain escape sequences, then the bolding of the sub-headings on the PMI Sheets will not be displayed.</u>

> <u>Example Set Up</u>

> The following is a set up example that was used in the development process. This example is provided to guide the user in this set up. Please note that it is only an example and may not hold true in all cases.  

> Example: Hewlett Packard or LexMark Example Set Up

> From the printer technical manual the following are the escape sequences:

> Bold On: \$C(27)\_”(s3B”

> Bold Off: \$C(27)\_”(s0B”

> In the TERMINAL TYPE (#3.2) file:

> To turn the bold on in the HIGH INTENSITY (BOLD) field (#27):

HIGH INTENSITY (BOLD) = \$C(27)\_”(s3B”

To turn the bold off in the NORMAL INTENSITY (RESET) field (#29):

NORMAL INTENSITY (RESET) = \$C(27)\_”(s0B”

(This page included for two-sided copying.)

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The NATIONAL DRUG file (#50.6) has been redesigned from a file of seven multiples deep to a new file structure of four separate files. The new files are the VA PRODUCT file (#50.68), the NDC/UPN file (#50.67), the VA DISPENSE UNIT file (#50.64), and File \#50.6, which is now the VA GENERIC file.

> The files required to run the NDF software are listed below.

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# NAME DD CODE W/FILE DATA PTS RIDE

-----------------------------------------------------------------------------

50.416 DRUG INGREDIENT YES YES YES OVER NO NO

50.6 VA GENERIC YES YES NO

50.605 VA DRUG CLASS YES YES YES OVER NO NO

50.606 DOSAGE FORM YES YES YES OVER NO NO

Partial DD: subDD 50.606 fld: .01

50.607 DRUG UNITS YES YES YES OVER NO NO

50.608 PACKAGE TYPE YES YES YES OVER NO NO

50.609 PACKAGE SIZE YES YES YES OVER NO NO

50.612 NATIONAL DRUG TRANSLATION YES YES NO

50.64 VA DISPENSE UNIT YES YES NO OVER NO NO

50.67 NDC/UPN YES YES NO

50.68 VA PRODUCT YES YES NO

51.2 MEDICATION ROUTES YES YES NO MERG NO YES

Partial DD: subDD 51.2 fld: .01

55.95 DRUG MANUFACTURER YES YES YES OVER NO NO

56 DRUG INTERACTION YES YES NO OVER NO NO

57.23 PPS-N UPDATE CONTROL FILE YES YES NO NO

59.7 PHARMACY SYSTEM YES YES NO

Partial DD: subDD 59.7 fld: 10

fld: 10.1

fld: 10.2

fld: 11

fld: 12

This PPS-N UPDATE CONTROL file (#57.23) contains configuration and installation information for the Pharmacy Product System - National (PPS-N) file retrieval and installation process.

57.23 PPS-N UPDATE CONTROL FILE YES YES NO NO

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Sort      | File |
|-----------|------|
| PSNFRMSRT | 50   |

| Print     | File   |
|-----------|--------|
| PSNFRMPRT | 50     |
| PSNHEAD   | 50     |
| PSNLDG1   | 50     |
| PSNPRINT  | 50.605 |
| PSNRPT4   | 50     |
| PSNACTION | 56     |

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of routines you will see for NDF when you load the new routine set. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (*First Line Routine Print*) to print a list of just the first line of each PSN\* routine.

| PSN4P4   | PSN4POST | PSN4PRE  | PSN50612 | PSN50625 |
|----------|----------|----------|----------|----------|
| PSN50626 | PSN50627 | PSN5067  | PSN50P41 | PSN50P4A |
| PSN50P6  | PSN50P65 | PSN50P67 | PSN50P68 | PSN56    |
| PSNACT   | PSNAPIS  | PSNAUTO  | PSNBLD   | PSNCLEAN |
| PSNCLEHW | PSNCLS   | PSNCMOP  | PSNCOMP  | PSNCLPR  |
| PSNDEX   | PSNDDI1  | PSNDEA   | PSNDI    | PSNDINT  |
| PSNDRUG  | PSNEN169 | PSNEXC   | PSNFDAMG | PSNFRMLY |
| PSNHEADR | PSNHELP  | PSNHELP1 | PSNHRFM  | PSNHRFM1 |
| PSNHIT   | PSNLDG   | PSNLOOK  | PSNMCLS  | PSNMEDG  |
| PSNMRG   | PSNNDC   | PSNNDC1  | PSNNFL   | PSNNFL1  |
| PSNNGR   | PSNOCLS  | PSNONDF  | PSNOUT   | PSNPFN   |
| PSNPO169 | PSNPPIO  | PSNPPIP  | PSNPPIP1 | PSNPSS   |
| PSNPST   | PSNRPT3  | PSNSTCK  | PSNPRE   | PSNPRE1  |
| PSNPREDS | PSNUPN   | PSNVAGN  | PSNQA    | PSNRPT   |
| PSNRPT2  | PSNVUIE  | PSNXREF  | PSNSTCL  | PSNSUPLY |
| PSNTER   | PSNVER   | PSNVFY   | PSNVIEW  | PSNCFINQ |
| PSNFTP   | PSNFTP2  | PSNFTP3  | PSNOSKEY | PSNPARM  |
| PSNPPSCL | PSNPPSDL | PSNPPSI1 | PSNPPSI2 | PSNPPSI3 |
| PSNPPSME | PSNPPSMG | PSNPPSMS | PSNPPSNC | PSNPPSNF |
| PSNPPSNK | PSNPPSNR | PSNPPSNU | PSNPPSNV | PSNPPSNW |
| PSNPPSNP | PSNVCR   | PSNVCR1  | PSNVCR2  |          |
|          |          |          |          |          |

84 Routines

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Drug File \[PSNMGR\] menu, assigned to all users, contains two locked options — *Allow Unmatched Drugs to Be Classed* \[PSNSTCL\] and *Formulary Report* \[PSNFRMLY\]. These options are unlocked by the PSNMGR key. This key must be assigned to the package coordinator or his/her designee. Only users that have this key will see these options on their menu.

> The following are the options exported with NDF version 4.0:

## National Drug File V. 4.0 Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REMA Rematch/Match Single Drugs \[PSNDRUG\]

> VER Verify Matches \[PSNVFY\]

> SVER Verify Single Match \[PSNVER\]

> MERG Merge National Drug File Data Into Local File \[PSNMRG\]

> AUTO Automatic Match of Unmatched Drugs \[PSNAUTO\]

> CLAS Allow Unmatched Drugs to be Classed \[PSNSTCL\]

> \[Locked: PSNMGR\]

> RPRT National Drug File Reports \[PSNSUBM\]

> LDF Local Drug File Report \[PSNLDG\]

> VAGN Report of VA Generic Names from National Drug \[PSNVAGN\]

> ATMP Report of Attempted Match Drugs \[PSNEXC\]

> PROD VA Product Names Matched Report \[PSNPFN\]

> NOCL Local Drugs with No VA Drug Class Report \[PSNOCLS\]

> CLVA VA Drug Classification \[PSNCLS\]

> DFL NDF Info from Your Local Drug File \[PSNRPT\]

> SUPL Supply (XA000) VA Class Report \[PSNSUPLY\]

> MANC Manually Classed Drugs Report \[PSNMCLS\]

> NMAT Local Drugs with NO Match to NDF Report \[PSNONDF\]

> \*LOCF Local Formulary Report \[PSNFRMLY\] \[Locked: PSNMGR\]

> NATF National Formulary Report \[PSNNFL\]

> DDIN Drug-Drug Interaction Report \[PSNTER\]

> CMOP VA Products Marked for CMOP Transmission \[PSNCMOP\]

> PNCL VA Product Names By Class Report \[PSNCLPR\]

LDRG Local Drugs Excluded from Drug-Drug Interactions \[PSNODDI\]

VDRG VA Products Excluded from Drug-Drug Interactions \[PSNEXMPT\]

> INQ Inquiry Options \[PSNQUER\]

> LINQ Inquire to Local Drug File \[PSNVIEW\]

> \*\*PNIN Inquire to VA Product Info For Local Drug \[PSNLOOK\]

> NDCU NDC/UPN Inquiry \[PSNUPN\]

> NAT Inquire to National Files \[PSNACT\]

> PMIS Print a PMI Sheet \[PSNPMIS\]

> FDA Display FDA Medication Guide \[PSN MED GUIDE\]

> PPS PPS-N Menu \[PSN PPS MENU\] \[Locked with PSN PPS ADMIN\]

> SD Schedule download of NDF update file \[PSN PPS SCHEDULE DOWNLOAD\]

> SI Schedule Install of NDF Update file \[PSN PPS SCHEDULE INSTALL\]

> MD Manual Download of NDF Update file \[PSN PPS MANUAL DOWNLOAD\]

> MI Manual Install of NDF Update file \[PSN PPS MANUAL INSTALL\]

> RJ Reject/Complete of NDF Update file \[PSN PPS REJECT FILE\]

> SP PPS-N Site Parameters (Enter/Edit) \[PSN PPS PARAM\]

> VC Vista Comparison Report \[PSN PPS VISTA COMPARISON RPT\]

> DIS Download/Install Status Report \[PSN PPS DNLD/INST STATUS REP\]

SSH Manage Secure Shell (SSH) Keys \[PSN PPS SSH KEY MANAGEMENT\]

> \* Formerly *Formulary Report*

> \*\* Formerly *Lookup National Drug Info in Local File.*

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The NDF software contains no archiving or purging capabilities. It is recommended that National Drug File remain online.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Drug File contains one callable routine at the present time. This routine, PSNNGR, is used by the Allergy Tracking System software package. The routine is the actual point of entry.

> This routine is to be used in conjunction with the allergies package. It expects an input of PSNDA=internal number in File 50.6 (VA GENERIC file). The routine returns ^TMP("PSN",\$J,IFN)=Primary Ingredient. The IFN is the Internal number from File \#50.416 (DRUG INGREDIENTS file) of Primary Ingredient. If PSNDA doesn’t exist, PSNID and ^TMP("PSN",\$J) are killed. The variables X,J,K,PSNPN are used and are killed before exiting.

> For detailed information on all supported National Drug File APIs, see the *Pharmacy Re-Engineering (PRE) Application Program Interface (API) Manual* posted on the VistA Documentation Library (VDL) at <http://www.va.gov/vdl/>.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Drug File V. 4.0 relies (minimum) on the following external packages. This software is not included in this package and must be installed before this version of NDF is completely functional.

> <u>Package</u> <u>Minimum Version Needed</u>

> VA FileMan 21.0

> Kernel 8.0

> MailMan 7.1

> Pharmacy Data Management 1.0

> National Drug File 3.18

> Adverse Reaction Tracking 4.0

> Consolidated Mail Outpatient Pharmacy 2.0

> Decision Support System 3.0

> Drug Accountability 3.0

> Immunology Case Registry 2.1

> Inpatient Medications 4.5 or greater

> Order Entry/Results Reporting 2.5 or greater

> Outpatient Pharmacy 6.0 or greater

> Web Services Client (HWSC) 1.0 or greater

> \*XOBW\*1\*4 patch must be installed.

The build will check to make sure that the site has the following patches installed:

> <u>Package</u> <u>Patch Needed</u>

Adverse Reaction Tracking V. 4.0 GMRA\*4\*13

> Consolidated Mail Outpatient Pharmacy V. 2.0 PSX\*2\*18

> Decision Support System V. 3.0 ECX\*3\*10

> Drug Accountability V. 3.0 PSA\*3\*8

> Immunology Case Registry V. 2.1 IMR\*2.1\*3

> Inpatient Medications V. 4.5 PSJ\*4.5\*59

> Inpatient Medications V. 5.0 PSJ\*5\*11, PSJ\*5\*14

> Order Entry/Results Reporting V. 3.0 OR\*3\*33 *\[CPRS sites only\]*

> Outpatient Pharmacy V. 6.0 PSO\*6\*173

> Outpatient Pharmacy V. 7.0 PSO\*7\*10, PSO\*7\*11

> Pharmacy Data Management V. 1.0 PSS\*1\*29

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Data Base Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the National Drug File software package options have been designed to stand-alone.

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Drug File routines do not use package-wide variables.

# Electronic MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the data patches have been sent, you and holder(s) of the PSNMGR key will receive Mailman messages similar to the following examples.

> The first MailMan message lists new VA products that have been added to the National Drug File, the active VA products that are unmarked for CMOP, the VA products for which the National Formulary Indicator is changed, and the VA products that have had the OVERRIDE dosage form excluded from dosage checks flag edited. The second MailMan message lists the interactions that have been added, edited, or inactivated in the National Drug File. The third MailMan message contains a list of drugs unmatched from the National Drug File.

MailMan Message 1: Data Update for NDF

Subj: DATA UPDATE FOR NDF \[#112345\] 03 May 02 11:31 420 lines

From: NDF MANAGER In 'IN' basket. Page 1

-----------------------------------------------------------------------

The following VA Products have been added to the National

Drug File. You may wish to review, then match or unmatch

local drug file entries based on this updated information.

ACCU-CHEK ACTIVE (GLUCOSE) TEST STRIP

(CMOP - XZ355) (DISPENSE UNIT - EA)

050924-0681-01 050924-0475-50

BOSENTAN 125MG TAB

(CMOP - B0477) (DISPENSE UNIT - TAB)

066215-0102-06

CHONDROITIN NA 40MG/HYALURONATE 30MG/ML INJ,OPH,SYRINGE,0.75ML

(CMOP - C1041) (DISPENSE UNIT - SYRINGE)

008065-1839-75

DIGOXIN (LANOXIN) 0.125MG TAB

(CMOP - D0080) (DISPENSE UNIT - TAB)

000173-0242-75 000173-0242-30 000173-0242-55

ESTRADIOL 25MCG TAB,VAG,APPLICATOR

(CMOP - E0335) (DISPENSE UNIT - EA)

000009-5173-03 000009-5173-02 000009-5173-04

FERROUS SO4 325MG TAB,EC,UD

(CMOP - F0297) (DISPENSE UNIT - TAB)

000574-0608-11

GLYCERIN 3%/SODIUM CL 0.75% SOLN,NASAL

(CMOP - G0220) (DISPENSE UNIT - ML)

050930-0280-50 050930-0280-32

HYDROGEN PEROXIDE 1.5% RINSE,ORAL

(CMOP - H0408) (DISPENSE UNIT - ML)

010310-3186-00 038341-0800-80 038341-0801-60

IBRITUMOMAB TIUXETAN IN-111 INJ,KIT

(CMOP - I0336) (DISPENSE UNIT - KIT)

064406-0104-04

-----------------------------------------report continues----------------------------------------

#####################  MailMan Message 1: Data Update for NDF (continued)

The National Formulary Indicator has changed for the following

VA Products. The National Formulary Indicator will automatically

be changed in your local DRUG file (#50). Please review the

VISN and Local Formulary designations of these products and

make appropriate changes.

FORMULARY ITEMS

ACCU-CHEK ACTIVE (GLUCOSE) TEST STRIP

AL OH 500MG/MG OH 400MG/SIMETHICONE 40MG/5ML LIQUID(ML)

ALBUTEROL SO4 0.5% SOLN,INHL,5ML

CLARITHROMYCIN 500MG TAB,SA,PKT,14

EFAVIRENZ 600MG TAB

ENOXAPARIN 120MG/0.8ML INJ,SYRINGE,0.8ML

FOLIC ACID 1MG TAB,UD

GUAIFENESIN 100MG/5ML (AF) LIQUID

HEPATITIS A 720 EL.U/HEPATITIS B 20MCG/1ML VACCINE INJ

HEPATITIS A 720 EL.U/HEPATITIS B 20MCG/ML VACCINE INJ,SYR,1ML

NON-FORMULARY ITEMS

OPIUM 10% TINCTURE

PROCAINAMIDE HCL 1000MG TAB,SA

PROCAINAMIDE HCL 250MG CAP

PROCAINAMIDE HCL 250MG TAB

The following active VA Products are no longer marked for CMOP.

All local drug file entries matched to these VA Products will

be UNMARKED for CMOP. In order to have these entries dispensed

by CMOP any local DRUG file (#50) entries matched to these

products must be re-matched to another VA product that is actively

marked for CMOP dispensing.

ANTI-THYMOCYTE GLOBULIN (RABBIT) 25MG/VIL INJ A1108

BANDAGE,PROFORE FOUR LAYER SYSTEM,S-N \#66000016 XX199

ISOTRETINOIN 10MG CAP I0085

ISOTRETINOIN 20MG CAP I0086

ISOTRETINOIN 40MG CAP I0087

The National Formulary Restriction has changed for the following VA Products.

MONTELUKAST NA 10MG TAB

Refer to leukotriene inhibitor criteria for use.

MONTELUKAST NA 10MG TAB,UD

Refer to leukotriene inhibitor criteria for use.

PROCAINAMIDE HCL(PROCANBID)500MG TAB,SA

Refer to Procainamide drug monitoring recommendations.

#####################  MailMan Message 1: Data Update for NDF (continued)

##################### 

For the following VA Products, the OVERRIDE dosage form exclude from

dosage checks flag has been edited.

INSULIN HUMULIN 70/30 (NPH/REG) INJ PEN,3ML Yes

DOSAGE FORM: INJ (excluded)

TIOTROPIUM 18MCG CAP,INHL,5 No

DOSAGE FORM: CAP,INHL (not excluded)

TIOTROPIUM 18MCG CAP,INHL,90 No

DOSAGE FORM: CAP,INHL (not excluded)

ZER VACCINE LIVE (OKA/MERCK) INJ Yes

DOSAGE FORM: INJ,LYPHL (not excluded)

  
MailMan Message 2: Updated Interactions

Subj: UPDATED INTERACTIONS \[#112242\] 31 Jul 01 10:30 17 lines

From: NDF MANAGER In 'IN' basket. Page 1

-----------------------------------------------------------------------

The following interactions in National Drug File (NDF) have been added,

edited or inactivated. These changes are the result of review and

recommendations from the NDF support group.

ADDED INTERACTIONS

ALPRAZOLAM/NEFAZODONE Significant

BUSPIRONE/NEFAZODONE Significant

NEFAZODONE/TRIAZOLAM Significant

EDITED INTERACTIONS

NONE

INACTIVATED INTERACTIONS

NONE

  
MailMan Message 3: Drugs Unmatched from National Drug File

Subj: DRUGS UNMATCHED FROM NATIONAL DRUG FILE \[#1970\] 03 Apr 02 13:55

137 lines

From: NDF MANAGER In 'IN' basket. Page 1

-----------------------------------------------------------------------------

The following active entries in your DRUG file (#50) have been

unmatched from the National Drug File (NDF). The VA Product

name and CMOP ID corresponding to the unmatched local drug file

names are listed on the indented line beneath each entry. An

Inactivation Date may be listed for entries when this reason

applies. Until you rematch these entries to NDF, they will not

transmit to CMOP and drug-drug interaction checks will not check

for these products. It is critical that you rematch these

products immediately. You may also need to match a new

orderable item. Any possible dosages and local possible

dosages for these unmatched products have been deleted.

Therefore, the dosages for each unmatched product should

be reviewed after the rematch or recreated if the product

cannot be rematched to a VA Product through the NDF

matching process.

DRUG IEN INACTIVATION

DATE

CYCLOPHOSPHAMIDE 50MG C.T. 6

(CMOP C0332) CYCLOPHOSPHAMIDE 50MG TAB 3/4/2002

STRENGTH: 50 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 50 IO

2 100 IO

HYDROMORPHONE 2MG C.T. 301

(CMOP H0297) HYDROMORPHONE HCL 2MG TAB

STRENGTH: 2 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 2 O

2 4 IO

LOCAL POSSIBLE DOSES

DOSE PACKAGE BCMA UNITS/DOSE

TEST O

METHOCARBAMOL 750MG TAB 132

(CMOP M0055) METHOCARBAMOL 750MG TAB

STRENGTH: 500 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 500 IO

2 1000 IO

3 1500 IO

LOCAL POSSIBLE DOSES

DOSE PACKAGE BCMA UNITS/DOSE

-----------------------------------------report continues----------------------------------------

  
MailMan Message 3: Drugs Unmatched from National Drug File (continued)

The following investigational entries in your DRUG file (#50) have been

unmatched from the National Drug File (NDF). The VA Product

name and CMOP ID corresponding to the unmatched local drug file

names are listed on the indented line beneath each entry. An

Inactivation Date may be listed for entries when this reason

applies. Until you rematch these entries to NDF, they will not

transmit to CMOP and drug-drug interaction checks will not check

for these products. It is critical that you rematch these

products immediately. You may also need to match a new

orderable item. Any possible dosages and local possible

dosages for these unmatched products have been deleted.

Therefore, the dosages for each unmatched product should

be reviewed after the rematch or recreated if the product

cannot be rematched to a VA Product through the NDF

matching process.

DRUG IEN INACTIVATION

DATE

CHLORAMBUCIL 2MG TAB. 5

(CMOP C0551) CHLORAMBUCIL 2MG TAB

STRENGTH: 2 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 2 IO

2 4 IO

3 6 IO

NITROGLYCERIN 0.3MG S.L.T. 245

(CMOP N0056) NITROGLYCERIN 0.3MG TAB,SUBLINGUAL

STRENGTH: .3 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 .3 IO

2 .6 IO

LOCAL POSSIBLE DOSES

DOSE PACKAGE BCMA UNITS/DOSE

1 PATCH I

TEST DRUG IV 44

(CMOP N0147) NIZATIDINE 150MG CAP

STRENGTH: 150 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 150 IO

2 300 IO

LOCAL POSSIBLE DOSES

DOSE PACKAGE BCMA UNITS/DOSE

-----------------------------------------report continues----------------------------------------

  
MailMan Message 3: Drugs Unmatched from National Drug File (continued)

The following inactive entries in your DRUG file (#50) have been

unmatched from the National Drug File (NDF). The VA Product

name and CMOP ID corresponding to the unmatched local drug file

names are listed on the indented line beneath each entry. An

Inactivation Date may be listed for entries when this reason

applies. Until you rematch these entries to NDF, they will not

transmit to CMOP and drug-drug interaction checks will not check

for these products. It is critical that you rematch these

products immediately. You may also need to match a new

orderable item. Any possible dosages and local possible

dosages for these unmatched products have been deleted.

Therefore, the dosages for each unmatched product should

be reviewed after the rematch or recreated if the product

cannot be rematched to a VA Product through the NDF

matching process.

DRUG IEN INACTIVATION

DATE

AZATHIOPRINE 50MG TAB 1 2/2/1994

(CMOP A0478) AZATHIOPRINE 50MG TAB

STRENGTH: 50 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 50 IO

2 100 IO 3

LOCAL POSSIBLE DOSES

DOSE PACKAGE BCMA UNITS/DOSE

DOSE IO 2

BUSULFAN 2MG TAB 4 3/4/2002

(CMOP B0232) BUSULFAN 2MG TAB

STRENGTH: 2 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 2 IO

2 4 IO

CLOFIBRATE 500MG CAP 189 3/4/2002

(CMOP C0284) CLOFIBRATE 500MG CAP

STRENGTH: 500 UNITS: MG

POSSIBLE DOSES

DISP UNITS/DOSE DOSE PACKAGE BCMA UNITS/DOSE

1 500 IO

2 1000 IO

LOCAL POSSIBLE DOSES

DOSE PACKAGE BCMA UNITS/DOSE

TEST IO 2

# Notes Regarding Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Note on CS Federal Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patches PSN\*4\*64 and PSN\*4\*66 assign a CS Federal Schedule to controlled substances and identify controlled substances as narcotic or non-narcotic by populating the CS FEDERAL SCHEDULE field (#19) of the VA PRODUCT file (#50.68). Patch PSN\*4\*65 changes the *Merge National Drug File Data Into Local File* \[PSNMRG\] option so that the software checks each entry to see if the CS FEDERAL SCHEDULE field contains data. If an entry has a value for the CS FEDERAL SCHEDULE but its corresponding DEA, SPECIAL HDLG field (#3) of the DRUG file (#50) is blank, the DEA, SPECIAL HDLG field will be populated with the corresponding value using the following table:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 28%" />
<col style="width: 37%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>If a drug entry has a CS FEDERAL SCHEDULE of:</p>
</blockquote></td>
<td><blockquote>
<p>And its corresponding DEA, SPECIAL HDLG field is blank, the following DEA, SPECIAL HDLG code will be inserted:</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Schedule I narcotics</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Schedule II narcotics</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2A</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Schedule II non-narcotics</p>
</blockquote></td>
<td><blockquote>
<p>2n</p>
</blockquote></td>
<td><blockquote>
<p>2C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Schedule III narcotics</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>3A</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Schedule III non-narcotics</p>
</blockquote></td>
<td><blockquote>
<p>3n</p>
</blockquote></td>
<td><blockquote>
<p>3C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Schedule IV narcotics</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Schedule V narcotics</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Patch PSN\*4\*65 ensures that the newly populated CS FEDERAL SCHEDULE field is included as part of the National Drug File details in the *Inquire to National Files* \[PSNACT\], *NDF Info From Your Local Drug File* \[PSNRPT\], *Verify Matches* \[PSNVFY\] and *Verify Single Match* \[PSNVER\] options.

Note regarding Patch PSN\*4\*101 Pharmacy Data Standardization

This patch does not affect any Pharmacy functionality or end-users. This patch requires the HEALTH DATA & INFORMATICS (HDI) 1.0 package in addition to required patch release checks.

The scope of Data Standardization - Pharmacy enhancement project is to modify the VISTA Pharmacy National Drug File (NDF) structures in order to meet the established standards for elements required by Data Standardization to implement a common set of standards for Clinical Health Data Repository (CHDR) and the Health Data Repository (HDR).

To accomplish data standardization with VISTA Pharmacy and data flow to CHDR and HDR, a Veterans Health Administration Unique Identifier (VUID) and the

TERMSTATUS subscript Effective Date/Status will be populated in four files within the VISTA Pharmacy National Drug File package. VUID numbers will be generated dynamically and programmatically for each product. The VUID numbers have been assigned to National Drug File with a predetermined range (4000624- 4500623). There will be a one-time conversion to update the National Drug File package files. Once the Application Patch (PSN\*4\*101) and the VUID data have been installed in the four Globals for the Data Domain (NDF), the Application Post-install routine calls an API in the HDI package to update the VUID Seeding Process as Complete.

The four VISTA Pharmacy files being "standardized" are:

VA PRODUCT file (#50.68)

DRUG INGREDIENTS file (#50.416)

VA DRUG CLASS file (#50.605)

VA GENERIC file (#50.6)

Note regarding Patch PSN\*4\*169

This patch makes these corrections to the INQUIRE TO VA PRODUCT INFO FOR LOCAL DRUG \[PSNLOOK\] option:

> Problem: Sometimes the Active Ingredients would not display.

> Solution: The Active Ingredients will now always display.

> Problem: Sometimes the Strength that is displayed next to the Active

> Ingredient is actually the Strength of the VA Product.

> Solution: The Strength of the Active Ingredient will now accurately display.

> Problem: The Drug Unit was not always displaying.

> Solution: The Drug Unit will now always display.

> Problem: Only the CS FEDERAL SCHEDULE code was displaying, and

> not the text.

> Solution: For the CS FEDERAL SCHEDULE, both the code and text will

> now display.

> Problem: When displaying the Active Ingredients, the text (Primary) will

> no longer display next to an Active Ingredient that is a Primary

> Ingredient.

> Solution: The Primary Ingredient will now display if the Ingredient of the

> VA Product has a Primary Ingredient.

This patch makes these corrections to the INQUIRE TO NATIONAL FILES \[PSNACT\] option:

> Problem: Only the CS FEDERAL SCHEDULE code was displaying, and

> not the text.

> Solution: For the CS FEDERAL SCHEDULE, both the code and text will

> now display.

> Problem: The National Formulary Restriction display was being truncated

> after one line if it was two or more lines in length.

> Solution: The entire text entered for the National Formulary Restriction

> will now display.

(This page included for two-sided copying.)

Software Product Security

# Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> National Drug File V. 4.0 does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements.

## PSNMGR Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PSNMGR key is assigned to the package coordinator or his/her designee. This key unlocks the *Allow Unmatched Drugs to be Classed* \[PSNSTCL\] and the *LocalFormulary Report* \[PSNFRMLY\] options. Only users having this key will see these options on their menu.

> These menu options are locked because the first allows you to assign a VA classification to an unmatched or unmatchable drug in the local DRUG file (#50), and the second allows you to print a Hospital Formulary Report.

> The NATIONAL DRUG CLASS field (Field 25 of File 50) cannot be edited through VA FileMan, so *<u>only</u>* designated holders of the PSNMGR key can directly alter this field. The field may be altered in one of the following ways:

> If the drug is matched to the National Drug files, the field is edited through the matching process in the National Drug File software. This change is automatic and not under user control.

> If the drug is not matched, the NATIONAL DRUG CLASS field may be edited through the menu option *Allow Unmatched Drugs To Be Classed*, accessible only to users with the PSNMGR key.

## Precautions and Potential Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is strongly recommended that the DRUG file (#50) and the NATIONAL DRUG TRANSLATION file (#50.612) be included in the facility’s backup procedures on a periodic and systematic basis. It is important to back up these two files before the option, *Merge National Drug File Data Into Local File,* is executed. The Information Resources Management (IRM) staff must be advised before this option is executed to ensure that appropriate back up is done prior to execution.

## PSN PPS ADMIN Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This key will be required for the PPS-N Menu of the National Drug file package.

## PSN PPS COORD Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This key is used by the National Drug File (PSN) package to grant certain

users privileges to perform configuration updates.  
File Security

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 43%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>File</strong></p>
<p><strong>Numbers</strong></p></td>
<td><strong>File Names</strong></td>
<td><strong>DD</strong></td>
<td><strong>RD</strong></td>
<td><strong>WR</strong></td>
<td><strong>DEL</strong></td>
<td><strong>LAYGO</strong></td>
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
<td>*50.416</td>
<td>DRUG INGREDIENTS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>*50.6</td>
<td>VA GENERIC</td>
<td>@</td>
<td>Pp</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>*50.605</td>
<td>VA DRUG CLASS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>50.606</td>
<td>DOSAGE FORM</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>50.607</td>
<td>DRUG UNITS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>50.608</td>
<td>PACKAGE TYPE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>50.609</td>
<td>PACKAGE SIZE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>50.612</td>
<td>NATIONAL DRUG TRANSLATION</td>
<td>@</td>
<td></td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>50.64</td>
<td>VA DISPENSE UNIT</td>
<td>@</td>
<td>Pp</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>50.67</td>
<td>NDC/UPN</td>
<td>@</td>
<td>Pp</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>*50.68</td>
<td>VA PRODUCT</td>
<td>@</td>
<td>Pp</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>51.2</td>
<td>MEDICATION ROUTES</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>55.95</td>
<td>DRUG MANUFACTURER</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>56</td>
<td>DRUG INTERACTION</td>
<td>@</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>57.23</td>
<td>PPS-N UPDATE CONTROL FILE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>59.7</td>
<td>PHARMACY SYSTEM</td>
<td>^</td>
<td>@</td>
<td>^</td>
<td>^</td>
<td>^</td>
</tr>
</tbody>
</table>

\*Denotes files that have been standardized by Patch PSN\*4\*101.

The four VistA Pharmacy files being "standardized" are:

VA PRODUCT file (#50.68)

DRUG INGREDIENTS file (#50.416)

VA DRUG CLASS file (#50.605)

VA GENERIC file (#50.6)

For more information regarding Pharmacy Data Standardization, please refer to page 14d.

# Appendix A: PPS-N Update file configuration and specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the minimum packages indicated under the External Interfaces section, the following packages must be installed in order to communicate with PPS-N.

> <u>Package</u> <u>Minimum Version Needed</u>

> VISTALINK (XOBV) 1.6

> FOUNDATIONS (XOBU) 1.6

> WEB SERVICE CLIENT (XOBW) 1.0

## Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe configuring VistA to communicate with PPS-N. The information listed is defined upon installation of PSN\*4\*513.

### Web Server and Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon installation of patch of PSN\*4\*513, the ADPAC or IRM personnel need to make sure the Web Server and Web Services are updated correctly as shown below. Sites will be given the correct server to enter as they are brought on-board with PPS-N processing.

Select OPTION NAME: XOBW WEB SERVER MANAGER Web Server Manager

Web Server Manager

Web Server Manager Jul 20, 2017@16:48:36 Page: 1 of 1

HWSC Web Server Manager

Version: 1.0 Build: 9

ID Web Server Name IP Address or Domain Name:Port

1 \*PPSN <span class="mark">REDACTED</span>

Legend: \*Enabled

AS Add Server TS (Test Server)

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit// ES Edit Server

Select Web Server: 1

NAME: PPSN//

SERVER: <span class="mark">REDACTED</span> Replace \>\>\> Make sure you have the correct

server address.

PORT: 443// \>\>\> Make sure port number is 443.

DEFAULT HTTP TIMEOUT: 30//

STATUS: ENABLED//

Security Credentials

====================

LOGIN REQUIRED:

SSL Setup

=========

SSL ENABLED: TRUE// \>\>\> SSL Setup will not be available unless you

have XOBW\*1\*4 patch installed.

SSL CONFIGURATION: encrypt_only// \>\>\> The SSL CONFIGURATION must be set to

"encrypt_only".

SSL PORT: 443// \>\>\> The SSL PORT must be 443.

Authorize Web Services

======================

Select WEB SERVICE: UPDATE_STATUS//

WEB SERVICE: UPDATE_STATUS//

STATUS: ENABLED//

Web Service validation:

Web Server Manager Jul 20, 2017@16:54:15 Page: 1 of 1

HWSC Web Server Manager

Version: 1.0 Build: 9

ID Web Server Name IP Address or Domain Name:Port

1 \*PPSN <span class="mark">REDACTED</span>

Legend: \*Enabled

AS Add Server TS (Test Server)

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit// WS Web Service Manager

Web Service Manager Jul 20, 2017@16:54:18 Page: 1 of 1

HWSC Web Service Manager

Version: 1.0 Build: 9

ID Web Service Name Type URL Context Root

1 UPDATE_STATUS REST /PRE/ndf/update/

Enter ?? for more actions

AS Add Service

ES Edit Service

DS Delete Service

EP Expand Entry

Select Action:Quit// ES Edit Service

Select Web Service: 1

=============================================================================

5 UPDATE_STATUS REST /PRE/ndf/update/

-----------------------------------------------------------------------------

Name: UPDATE_STATUS

Type: REST

Registered Date/Time:

Context Root: /PRE/ndf/update/

Availability Resource: status

----------- Web servers 'UPDATE_STATUS' is authorized to: ------------------

\- PPSN

-----------------------------------------------------------------------------

NAME: UPDATE_STATUS//

DATE REGISTERED:

TYPE: REST//

CONTEXT ROOT: /PRE/ndf/update///

AVAILABILITY RESOURCE: status//

### Secure Shell (SSH) protocol and Secure File Transfer Protocol (SFTP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SSH and SFTP are protocols used to retrieve the PPS-N update files from the PPS-N SFTP server. They provide a secure encrypted method of transferring files from one computer system to another.

SSH keys are used during the authentication process for downloading the .DAT file from the PPS-N SFTP server. Once the SSH keys have been created and the public key is installed at the PPS-N server, the data file can be downloaded using the options *Schedule download of NDF update file* \[PSN PPS SCHEDULE DOWNLOAD\] or *Manual Download of NDF Update file* \[PSN DOWNLOAD NDF UPDATES\] as described in the NDF user manual.

Select PPS-N Menu \<FLD DDEV\> Option: SSH Manage Secure Shell (SSH) Keys

Select one of the following:

V View Public SSH Key

C Create New SSH Key Pair

D Delete SSH Key Pair

H Help with SSH Keys

Action: V// Create New SSH Key Pair

Enter your Current Signature Code: SIGNATURE VERIFIED

Select one of the following:

RSA Rivest, Shamir & Adleman (RSA)

<span id="p035" class="anchor"></span> ECDSA Elliptic Curve Digital Signature Algorithm

SSH Key Encryption Type: RSA// Rivest, Shamir & Adleman (RSA)

Confirm Creation of SSH Keys? NO// YES

Creating New SSH Keys, please wait...Done

Select one of the following:

V View Public SSH Key

C Create New SSH Key Pair

D Delete SSH Key Pair

H Help with SSH Keys

Action: V// View Public SSH Key

Public SSH Key (RSA) content (does not include dash lines):

----------------------------------------------------------------------------------------------------------------------------------------------

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsEikSHjQYXUTWVIlMp4KyabnAftBgwLKSnwYp51TG

9FW60ngoI6hnfGUehuGrkBWcrxN3AJUJNsGTDz/CqWQ4+OmLNZxH7N6RVGcYyAiWYF9CiE7+gqHEOKPc

B5/94ZuyTvn2cr0n+sZVTWklMqyAb0qqFR7xwY9jJrr22llN/YdE7CB0opPSnmK0FZ9fWPW9I+BNibnJ

fHMhmhRglv5qSjLhZyKuZa26y9fLCJp+LohHR+cA2dqFsDH0FbCksz2kwcyW4qin9IkK9vKWPGr30mK3

QmZdfqcskZdXD05QE9rQMrpK1nzWP2rS46NqQ7eukRYSmoJDb3Avgok9JHJj

-----------------------------------------------------------------------------------------------------------------------------------------------

Press Return to continue:

Select one of the following:

V View Public SSH Key

C Create New SSH Key Pair

D Delete SSH Key Pair

H Help with SSH Keys

Action: V// ^

### VMS Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site has not fully migrated to Linux you will need a new OpenVMS directory (e.g. USER\$:\[SFTP.PPSN\]) to be used by the data download process. The proposed naming convention is only a recommendation, and a more knowledgeable and experienced System Manager may choose to setup the extract directory using existing drives and definitions. The directory name chosen must have the appropriate READ, WRITE, EXECUTE, and DELETE privileges. You must have administrator privileges when you perform this task in order to assure the directory is set up/created with the necessary permissions.

The following is an example to create the file transmission directory.

\$ CREATE/DIRECTORY USER\$:\[SFTP.PPSN\] /own=CACHEMGR /PROTECTION=(S:RWED,O:RWED,G:RWED,W:RWED)/LOG

<u>NOTE:</u>

• The owner of the directory should be CACHEMGR.

• Where USER\$=the disk of your choice (e.g. USER\$, PQ\$, etc.), however - SYS\$ is not recommended.

• Confirm that the extract directory has similar protections and permissions.

\$DIR/PROT/OWNER PPSN.DIR

Directory USER\$:\[000000\]

PPSN.DIR;1 \[CACHEMGR\] (RWED,RWED,RWED,RWED)

| ![](national-drug-file-version-4-technical-manual-updated-psn-4-575/003.png) | Action: Once the directory has been created, please pass this directory name (e.g., “USER\$:\[SFTP.PPSN\]”) to the ADPAC/Pharmacy Chief/Pharmacy Informaticist. This will be used in the PPS-N Site parameters (Enter/Edit) “Outlined Below”. |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Linux Directories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have a LINUX operating system, the PPS-N download process will automatically create a directory to be used by the data download process. However, a more knowledgeable and experienced System Manager may choose to setup the extract directory using existing drives and definitions. The directory name chosen must have the appropriate READ, WRITE, EXECUTE, and DELETE privileges. You must have administrator privileges when you perform this task in order to assure the directory is set up/created with the necessary permissions.

The following is an example to create the file transmission directory. The field “directoryPath/Name” is where you would enter the path to the directory and the new directory name (i.e. /srv/vista/bham/user/sftp/PPSN/ where bham is the site specific folder).

\$mkdir /srv/vista/bham/user/sftp/PPSN/

\$chmod 777 /srv/vista/bham/user/sftp/PPSN/

\$ls –l

1 drwxrwxrwx. 5 cheyl200 cacheusr 4096 Aug 4 11:13 PPSN

<u>NOTE:</u>

• The owner of the directory should be CACHEMGR.

• Where USER\$=the disk of your choice (e.g. USER\$, PQ\$, etc.), however - SYS\$ is not recommended.

• Confirm that the extract directory has similar protections and permissions.

| ![](national-drug-file-version-4-technical-manual-updated-psn-4-575/004.png) | Action: Once the directory has been created, please pass this directory name (e.g., “USER\$:\[SFTP.PPSN\]”) to the ADPAC/Pharmacy Chief/Pharmacy Informaticist. This will be used in the PPS-N Site parameters (Enter/Edit) “Outlined Below”. |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### <u>PPS-N Site Parameters</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Version Number

This field contains the current version number of the last successful Pharmacy Product System - National (PPS-N) Update file that was installed. For example if the last PPS-N Update file installed was PPS_25PRV_26NEW.DAT, this field would contain 26.

Download Version Number

This field contains the version number for the last Pharmacy Product System - National (PPS-N) Update file downloaded. For example if the last PPS-N Update file downloaded was PPS_25PRV_26NEW.DAT, this field would contain 26.

Open VMS Local Directory

This field contains the name of the local Open VMS directory where the Pharmacy Product System - National (PPS-N) Update file will be stored on the local system after it is downloaded from the PPS-N server (e.g., USER\$:\[SFTP.PPSN\]).

Unix/Linux Local Directory

This field contains the name of the local Unix/Linux directory where the Pharmacy Product System - National (PPS-N) Update file will be stored on the local system after download from the PPS-N server (e.g. /user/sftp/PPSN/) and the option may prompt you for the following after enter the data and press \<Enter\> through it:

> The directory above could not be found.

Would you like to create it now? N// \<\<\<\<Answer YES\>\>\>

Remote Server Address

This is the secure FTP IP address of the Pharmacy Product System-National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

Remote Server Directory

This is the directory name at the Pharmacy Product System-National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

Remote SFTP User ID

This field contains the secure FTP username at the Pharmacy Product System – National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

Primary PPS-N Mail Group

This field is used to store the MS Outlook email group that will receive a copy of the PPS-N update messages. These messages include download and install information, the Data Update for NDF report message, Updated Interactions and FDA Med Guide, Drugs Unmatched from National Drug file, Local Drugs Re-matched to NDF, Interactions and Allergies Updated, and error messages.

Secondary PPS-N Mail group

This field is used to store the secondary MS Outlook email group that will receive a copy of

the PPS-N update messages. These messages include download and install information, the Data

Update for NDF report message, Updated Interactions and FDA Med Guide, Drugs Unmatched

from National Drug file, Local Drugs Re-matched to NDF, Interactions and Allergies Updated, and error messages.

PPS-N Account Type

This field defines the type of Pharmacy Product System - National (PPS-N) account. The account type can be one of the following: "Q" for National Test SQA system, "T" for

Test/Mirror account, "S" for Product Support, "N" for QA NDFMS account, or "P" for Production account. Local VA sites will use "P" for their production accounts and "T" for their test/mirror accounts.

Legacy Update Processing

This field denotes YES or NO if the National Drug File will be updated by the legacy FORUM patch release process or the Pharmacy Product System - National 3.0 Update file process.

The following selection options will be available to the user based on the PPS-N Account Type field as follows:

If Account Type is 'Q' or 'N', only the NO option will be available. Otherwise, YES and NO options will be available for selection.

Download Status

This field is used to track the status of a PPS-N/NDF Update file download from the PPS-N sftp server. The possible values for this field are:

> IN PROGRESS - PPS-N/NDF file is currently being downloaded

> NOT IN PROGRESS - PPS-N/NDF file is not being downloaded

Install Status

This field is used to track the status of a PPS-N/NDF Update file install into the National Drug file package. The possible values for this field are:

> IN PROGRESS - PPS-N/NDF file is currently being installed

> NOT IN PROGRESS - PPS-N/NDF file is not being installed

DISABLE Scheduled Options, Menu Options and Protocols

Under this field, the site will select scheduled options, menu options, and protocols that needs be marked out of order during the data file installation process.

<span id="p039" class="anchor"></span>ECDSA keys:

This field is used to allow the creation of the ECDSA keys. If this parameter is set to NOT ALLOWED users will not have the option of creating ECDSA keys under option Manage Secure Shell (SSH) Keys.

#### QA account example

Pharmacy Product System-National(PPS-N) Site Parameters

-------------------------------------------------------------------------------

1\. PPS-N Install Version : 0

2\. PPS-N Download Version : 0

3\. \*Open VMS Local Directory : USER\$:\[ <span class="mark">REDACTED</span> USER.PPSN.NDFE\]

4\. \*Unix/Linux Local Directory :

5\. \*Remote Server Address : <span class="mark">REDACTED</span>

6\. \*Remote Server Directory : /u01/app/pps/staging/pending/

7\. \*Remote SFTP Username : presftp

8\. Primary PPS-N Mail Group : <span class="mark">REDACTED</span>

9\. Secondary PPS-N Mail group : <span class="mark">REDACTED</span>

10\. \*PPS-N Account Type : Q - National SQA Testing

11\. \*Legacy Update Processing : NO

12\. \*Download Status : NOT IN PROGRESS

13\. \*Install Status : NOT IN PROGRESS

14\. Disable Menus, Options, etc :

15\. \*<span id="p040" class="anchor"></span>ECDSA keys : NOT ALLOWED

-------------------------------------------------------------------------------

Select field number to Edit:

#### NDFMS account example

Pharmacy Product System-National(PPS-N) Site Parameters

-------------------------------------------------------------------------------

1\. PPS-N Install Version : 0

2\. PPS-N Download Version : 0

3\. \*Open VMS Local Directory : USER\$:\[ <span class="mark">REDACTED</span> MUSER.PPSN.BTN\]

4\. \*Unix/Linux Local Directory :

5\. \*Remote Server Address : <span class="mark">REDACTED</span>

6\. \*Remote Server Directory : <span class="mark">REDACTED</span>

7\. \*Remote SFTP Username : presftp

8\. Primary PPS-N Mail Group : <span class="mark">REDACTED</span>

9\. Secondary PPS-N Mail group : <span class="mark">REDACTED</span>

10\. \*PPS-N Account Type : N - QA NDFMS

11\. \*Legacy Update Processing : NO

12\. \*Download Status : NOT IN PROGRESS

13\. \*Install Status : NOT IN PROGRESS

14\. Disable Menus, Options, etc :

15\. \*ECDSA keys : NOT ALLOWED

-------------------------------------------------------------------------------

Select field number to Edit:

#### Site Production Account example

Pharmacy Product System-National(PPS-N) Site Parameters

-----------------------------------------------------------------------------

1\. PPS-N Install Version : 0

2\. PPS-N Download Version : 0

3\. \*Open VMS Local Directory : USER\$:\[ <span class="mark">REDACTED</span> USER.PPSN.DMS\]

4\. \*Unix/Linux Local Directory :

5\. \*Remote Server Address : <span class="mark">REDACTED</span>

6\. \*Remote Server Directory : <span class="mark">REDACTED</span>

7\. \*Remote SFTP Username : <span class="mark">REDACTED</span>

8\. Primary PPS-N Mail Group : <span class="mark">REDACTED</span>

9\. Secondary PPS-N Mail group : <span class="mark">REDACTED</span>

10\. \*PPS-N Account Type : P - Production

11\. \*Legacy Update Processing : NO

12\. \*Download Status : NOT IN PROGRESS

13\. \*Install Status : NOT IN PROGRESS

14\. Disable Menus, Options, etc :

15\. \*<span id="p041" class="anchor"></span>ECDSA keys : NOT ALLOWED

-------------------------------------------------------------------------------

Select field number to Edit:

## ## PPS-N Update file structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PPS-N update file is structured like the Kernel Distribution & Installation (KIDS) builds and has the same types of records. The following gives an overview of the file.

### PMIDATA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example record from the .DAT file

PMIDATA^50.621^0

PMI-ENGLISH^50.621^9385^2551

PMIDATA^50.621^.5^0

3160223

PMIDATA^50.621^1^0

ALLOPURINOL - ORAL

PMIDATA^50.621^1^B^0

^^1^1^3160223

PMIDATA^50.621^1^B^1^0

PMIDATA^50.621^1^F^0

^^1^1^3160223

PMIDATA^50.621^1^F^1^0

(AL-oh-PURE-i-nol)

PMIDATA^50.621^1^C^0

^^1^1^3160223

PMIDATA^50.621^1^C^1^0

COMMON BRAND NAME(S): Zyloprim

PMIDATA^50.621^1^U^0

^^7^7^3160223

PMIDATA^50.621^1^U^1^0

USES: Allopurinol is used to treat gout and certain types of

PMIDATA^50.621^1^U^2^0

kidney stones. It is also used to prevent increased uric acid

PMIDATA^50.621^1^U^3^0

levels in patients receiving cancer chemotherapy. These patients

PMIDATA^50.621^1^U^4^0

can have increased uric acid levels due to release of uric acid

PMIDATA^50.621^1^U^5^0

from the dying cancer cells. Allopurinol works by reducing the

PMIDATA^50.621^1^U^6^0

amount of uric acid made by the body. Increased uric acid levels

PMIDATA^50.621^1^U^7^0

can cause gout and kidney problems.

PMIDATA^50.621^1^H^0

^^23^23^3160223

PMIDATA^50.621^1^H^1^0

HOW TO USE: Take this medication by mouth, usually once daily or

PMIDATA^50.621^1^H^2^0

as directed by your doctor. Take this medication after a meal to

PMIDATA^50.621^1^H^3^0

reduce stomach upset. If your dose is more than 300 milligrams a

PMIDATA^50.621^1^H^4^0

day, you will need to take several smaller doses during the day

PMIDATA^50.621^1^H^5^0

to get this amount (ask your doctor for directions).

PMIDATA^50.621^1^H^6^0

It is best to drink a full glass of water with each dose and

PMIDATA^50.621^1^H^7^0

at least 8 more glasses (8 ounces each) of fluid a day. If your

PMIDATA^50.621^1^H^8^0

doctor has directed you to drink less fluid for other medical

PMIDATA^50.621^1^H^9^0

reasons, consult your doctor for further instructions. Your

PMIDATA^50.621^1^H^10^0

doctor may also instruct you on how to decrease acid in your

PMIDATA^50.621^1^H^11^0

urine (e.g., avoiding large amounts of ascorbic acid/vitamin C).

PMIDATA^50.621^1^H^12^0

Dosage is based on your medical condition and response to

PMIDATA^50.621^1^H^13^0

treatment. Use this medication regularly to get the most benefit

PMIDATA^50.621^1^H^14^0

from it. To help you remember, take it at the same time(s) each

PMIDATA^50.621^1^H^15^0

day.

PMIDATA^50.621^1^H^16^0

For the treatment of gout, it may take up to several weeks for

PMIDATA^50.621^1^H^17^0

this medicine to have an effect. You may have more gout attacks

PMIDATA^50.621^1^H^18^0

for several months after starting this medicine while the body

PMIDATA^50.621^1^H^19^0

removes extra uric acid. Allopurinol is not a pain reliever. To

PMIDATA^50.621^1^H^20^0

relieve pain from gout, continue to take your prescribed

PMIDATA^50.621^1^H^21^0

medicines for gout attacks (e.g., colchicine, ibuprofen,

PMIDATA^50.621^1^H^22^0

indomethacin) as directed by your doctor.

PMIDATA^50.621^1^H^23^0

Tell your doctor if your condition persists or worsens.

PMIDATA^50.621^1^S^0

^^29^29^3160223

PMIDATA^50.621^1^S^1^0

SIDE EFFECTS: Stomach upset, nausea, diarrhea, or drowsiness may

PMIDATA^50.621^1^S^2^0

occur. If any of these effects persist or worsen, tell your

PMIDATA^50.621^1^S^3^0

doctor or pharmacist promptly.

PMIDATA^50.621^1^S^4^0

Remember that your doctor has prescribed this medication

PMIDATA^50.621^1^S^5^0

because he or she has judged that the benefit to you is greater

PMIDATA^50.621^1^S^6^0

than the risk of side effects. Many people using this medication

PMIDATA^50.621^1^S^7^0

do not have serious side effects.

PMIDATA^50.621^1^S^8^0

Tell your doctor right away if any of these rare but very

PMIDATA^50.621^1^S^9^0

serious side effects occur: numbness/tingling of arms/legs, easy

PMIDATA^50.621^1^S^10^0

bleeding/bruising, signs of infection (e.g., fever, persistent

PMIDATA^50.621^1^S^11^0

sore throat), unusual tiredness, painful/bloody urination, change

PMIDATA^50.621^1^S^12^0

in the amount of urine, yellowing eyes/skin, severe

PMIDATA^50.621^1^S^13^0

stomach/abdominal pain, persistent nausea/vomiting, dark urine,

PMIDATA^50.621^1^S^14^0

unusual weight loss, eye pain, vision changes.

PMIDATA^50.621^1^S^15^0

A very serious (possibly fatal) allergic reaction to this drug

PMIDATA^50.621^1^S^16^0

is rare. However, seek immediate medical attention if you notice

PMIDATA^50.621^1^S^17^0

any symptoms of a serious allergic reaction, including: rash,

PMIDATA^50.621^1^S^18^0

itching/swelling (especially of the face/tongue/throat), severe

PMIDATA^50.621^1^S^19^0

dizziness, trouble breathing.

PMIDATA^50.621^1^S^20^0

This is not a complete list of possible side effects. If you

PMIDATA^50.621^1^S^21^0

notice other effects not listed above, contact your doctor or

PMIDATA^50.621^1^S^22^0

pharmacist.

PMIDATA^50.621^1^S^23^0

In the US -

PMIDATA^50.621^1^S^24^0

Call your doctor for medical advice about side effects. You

PMIDATA^50.621^1^S^25^0

may report side effects to FDA at 1-800-FDA-1088 or at

PMIDATA^50.621^1^S^26^0

www.fda.gov/medwatch.

PMIDATA^50.621^1^S^27^0

In Canada - Call your doctor for medical advice about side

PMIDATA^50.621^1^S^28^0

effects. You may report side effects to Health Canada at

PMIDATA^50.621^1^S^29^0

1-866-234-2345.

PMIDATA^50.621^1^P^0

^^22^22^3160223

PMIDATA^50.621^1^P^1^0

PRECAUTIONS: Before taking allopurinol, tell your doctor or

PMIDATA^50.621^1^P^2^0

pharmacist if you are allergic to it; or if you have had a severe

PMIDATA^50.621^1^P^3^0

reaction to it; or if you have any other allergies. This product

PMIDATA^50.621^1^P^4^0

may contain inactive ingredients, which can cause allergic

PMIDATA^50.621^1^P^5^0

reactions or other problems. Talk to your pharmacist for more

PMIDATA^50.621^1^P^6^0

details.

PMIDATA^50.621^1^P^7^0

Before using this medication, tell your doctor or pharmacist

PMIDATA^50.621^1^P^8^0

your medical history, especially of: liver disease, kidney

PMIDATA^50.621^1^P^9^0

disease, diabetes, high blood pressure (hypertension), unusual

PMIDATA^50.621^1^P^10^0

diets (e.g., fasting).

PMIDATA^50.621^1^P^11^0

This drug may make you drowsy. Do not drive, use machinery, or

PMIDATA^50.621^1^P^12^0

do any activity that requires alertness until you are sure you

PMIDATA^50.621^1^P^13^0

can perform such activities safely.

PMIDATA^50.621^1^P^14^0

Alcohol may decrease the effectiveness of this drug. Limit

PMIDATA^50.621^1^P^15^0

alcoholic beverages.

PMIDATA^50.621^1^P^16^0

Kidney function declines as you grow older. This medication is

PMIDATA^50.621^1^P^17^0

removed by the kidneys. Therefore, older adults may be at greater

PMIDATA^50.621^1^P^18^0

risk for side effects while using this drug.

PMIDATA^50.621^1^P^19^0

During pregnancy, this medication should be used only when

PMIDATA^50.621^1^P^20^0

clearly needed. Discuss the risks and benefits with your doctor.

PMIDATA^50.621^1^P^21^0

Allopurinol passes into breast milk. Consult your doctor

PMIDATA^50.621^1^P^22^0

before breast-feeding.

PMIDATA^50.621^1^I^0

^^19^19^3160223

PMIDATA^50.621^1^I^1^0

DRUG INTERACTIONS: Your doctor or pharmacist may already be

PMIDATA^50.621^1^I^2^0

aware of any possible drug interactions and may be monitoring you

PMIDATA^50.621^1^I^3^0

for them. Do not start, stop, or change the dosage of any

PMIDATA^50.621^1^I^4^0

medicine before checking with your doctor or pharmacist first.

PMIDATA^50.621^1^I^5^0

This drug should not be used with the following medication

PMIDATA^50.621^1^I^6^0

because very serious interactions may occur: didanosine.

PMIDATA^50.621^1^I^7^0

If you are currently using this medication, tell your doctor

PMIDATA^50.621^1^I^8^0

or pharmacist before starting allopurinol.

PMIDATA^50.621^1^I^9^0

Before using this medication, tell your doctor or pharmacist

PMIDATA^50.621^1^I^10^0

of all prescription and nonprescription/herbal products you may

PMIDATA^50.621^1^I^11^0

use, especially of: certain asthma drugs (aminophylline,

PMIDATA^50.621^1^I^12^0

theophylline), azathioprine, "blood thinners" (e.g., warfarin),

PMIDATA^50.621^1^I^13^0

chlorpropamide, cyclosporine, mercaptopurine, "water pills"

PMIDATA^50.621^1^I^14^0

(e.g., thiazide diuretics such as hydrochlorothiazide).

PMIDATA^50.621^1^I^15^0

This document does not contain all possible interactions.

PMIDATA^50.621^1^I^16^0

Therefore, before using this product, tell your doctor or

PMIDATA^50.621^1^I^17^0

pharmacist of all the products you use. Keep a list of all your

PMIDATA^50.621^1^I^18^0

medications with you, and share the list with your doctor and

PMIDATA^50.621^1^I^19^0

pharmacist.

PMIDATA^50.621^1^O^0

^^4^4^3160223

PMIDATA^50.621^1^O^1^0

OVERDOSE: If overdose is suspected, contact a poison control

PMIDATA^50.621^1^O^2^0

center or emergency room right away. US residents can call their

PMIDATA^50.621^1^O^3^0

local poison control center at 1-800-222-1222. Canada residents

PMIDATA^50.621^1^O^4^0

can call a provincial poison control center.

PMIDATA^50.621^1^N^0

^^8^8^3160223

PMIDATA^50.621^1^N^1^0

NOTES: Do not share this medication with others.

PMIDATA^50.621^1^N^2^0

Laboratory and/or medical tests (e.g., uric acid blood levels,

PMIDATA^50.621^1^N^3^0

liver/kidney function tests, complete blood count) may be

PMIDATA^50.621^1^N^4^0

performed periodically to monitor your progress or check for side

PMIDATA^50.621^1^N^5^0

effects. Consult your doctor for more details.

PMIDATA^50.621^1^N^6^0

If you are taking allopurinol to treat kidney stones, you may

PMIDATA^50.621^1^N^7^0

benefit from a special diet. Consult your doctor for more

PMIDATA^50.621^1^N^8^0

details.

PMIDATA^50.621^1^D^0

^^4^4^3160223

PMIDATA^50.621^1^D^1^0

MISSED DOSE: If you miss a dose, take it as soon as you

PMIDATA^50.621^1^D^2^0

remember. If it is near the time of the next dose, skip the

PMIDATA^50.621^1^D^3^0

missed dose and resume your usual dosing schedule. Do not double

PMIDATA^50.621^1^D^4^0

the dose to catch up.

PMIDATA^50.621^1^R^0

^^11^11^3160223

PMIDATA^50.621^1^R^1^0

STORAGE: Store the US product at room temperature between 59-77

PMIDATA^50.621^1^R^2^0

degrees F (15-25 degrees C) away from light and moisture. Do not

PMIDATA^50.621^1^R^3^0

store in the bathroom.

PMIDATA^50.621^1^R^4^0

Store the Canadian product at room temperature between 59-86

PMIDATA^50.621^1^R^5^0

degrees F (15-30 degrees C) away from light and moisture.

PMIDATA^50.621^1^R^6^0

Keep all medicines away from children and pets.

PMIDATA^50.621^1^R^7^0

Do not flush medications down the toilet or pour them into a

PMIDATA^50.621^1^R^8^0

drain unless instructed to do so. Properly discard this product

PMIDATA^50.621^1^R^9^0

when it is expired or no longer needed. Consult your pharmacist

PMIDATA^50.621^1^R^10^0

or local waste disposal company for more details about how to

PMIDATA^50.621^1^R^11^0

safely discard your product.

Data Values

The following is an example for file 50.621 and the entries are in order of the example above. The same types of entries are present for files 50.622 – 56.628.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 34%" />
<col style="width: 25%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Piece</strong></th>
<th><strong>Node</strong></th>
<th><strong>Description/Field Name</strong></th>
<th><strong>Data</strong></th>
<th><strong>Data Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>0</td>
<td>Node level</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>0</td>
<td>File Name</td>
<td>PMI-ENGLISH</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td>0</td>
<td>File Number</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>0</td>
<td># of entries in the file</td>
<td>9385</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>0</td>
<td>Last entry</td>
<td>2551</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td></td>
<td>Field</td>
<td>.5</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>.5,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>.5,0</td>
<td>Date</td>
<td>316223</td>
<td>Date</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,0</td>
<td>TITLE field (#.01)</td>
<td>ALLOPURINOL – ORAL</td>
<td>Text</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,B</td>
<td>Node</td>
<td>B</td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,B,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,B,0</td>
<td><p>Value for zero node of the word processing field</p>
<p>^PS(50.621,1,"B",0)=</p>
<p>"^^1^1^3160223"</p></td>
<td>^^1^1^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,B</td>
<td>Node for word processing field</td>
<td>B</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,B,1</td>
<td>BLANK LINE field (#2) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1,B,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,B,1,0</td>
<td>BLANK LINE field (#2) value. ^PS(50.621,1,"B",1,0)=" "</td>
<td>Null</td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATE</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,F</td>
<td>Node for word processing field</td>
<td>F</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,F,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,F,0</td>
<td><p>Value for zero node of the word processing field</p>
<p><strong>^PS(50.621,1,"F",0)=</strong></p>
<p><strong>"^^1^1^3160223"</strong></p></td>
<td>^^1^1^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,F</td>
<td>Node for word processing field</td>
<td>F</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,F,1</td>
<td>PHONENETICS field (#3) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>6</td>
<td>1,F,1,0</td>
<td>Sequence</td>
<td><strong>0</strong></td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,F,1,0</td>
<td><p>PHONENETICS field (#3) value.</p>
<p>^PS(50.621,1,"F",1,0)="(AL-oh-PURE-i-nol)"</p></td>
<td>AL-oh-PURE-i-nol</td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,C</td>
<td>Node for word processing field</td>
<td>C</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,C,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,C,0</td>
<td><p>Value for zero node of the word processing field</p>
<p>node. <strong>^PS(50.621,1,"C",0)=</strong></p>
<p><strong>"^^1^1^3160307"</strong></p></td>
<td>^^1^1^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,C</td>
<td>Node for word processing field</td>
<td>C</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,C,1</td>
<td>COMMON BRAND NAMES field (#1) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1,C,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,C,1,0</td>
<td>Sequence 1 for COMMON BRAND NAMES field (#1) value. ^PS(50.621,1,"C",1,0)="COMMON BRAND NAME(S): Zyloprim"</td>
<td>COMMON BRAND NAME(S): Zyloprim</td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,U</td>
<td>Node for word processing field</td>
<td>U</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,U,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,U,0</td>
<td><p>Value for zero node of the word processing field</p>
<p>node.</p></td>
<td>^^1^1^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,U</td>
<td>Node for word processing field</td>
<td>U</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,U,1</td>
<td>USES field (#5) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>6</td>
<td>1,U,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,U,1 – 7,0</td>
<td>USES field (#5) sequence number 1 value</td>
<td><p>Example, sequence 1 is:</p>
<p>Sequence 1 = USES: Allopurinol is used to treat gout and certain types of</p></td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,H</td>
<td>Node for word processing field</td>
<td>H</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,H,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,H,0</td>
<td>HOW TO TAKE field (#4) zero node.</td>
<td>^^23^23^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,H</td>
<td>Node for word processing field</td>
<td>H</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,H,1</td>
<td>HOW TO TAKE field (#4) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1,H,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td></td>
<td>1,H,1 – 23,0</td>
<td>HOW TO TAKE field (#4) sequence 1 – 23.</td>
<td><p>Example, sequence 1 is:</p>
<p>Sequence 1 = For the treatment of gout, it may take up to several weeks for</p></td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,S</td>
<td>Node for word processing field</td>
<td>S</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,S,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,S,0</td>
<td>SIDE EFFECTS field (#6) zero node</td>
<td>^^29^29^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,S</td>
<td>Node for word processing field</td>
<td>S</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,S,1</td>
<td>SIDE EFFECTS field (#6) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>6</td>
<td>1,S,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td></td>
<td>1,S,1 – 29,0</td>
<td>SIDE EFFECTS field (#6) sequence 1 – 29.</td>
<td><p>Example, sequence 1 is:</p>
<p>Sequence 1 = For the treatment of gout, it may take up to several weeks for</p></td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,P</td>
<td>Node for word processing field</td>
<td>P</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,P,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,P,0</td>
<td>PRECAUTIONS field (#11) zero node</td>
<td>^^22^22^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,P</td>
<td>Node for word processing field</td>
<td>P</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,P,1</td>
<td>SIDE EFFECTS field (#6) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1,P,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,P,1 – 22</td>
<td>PRECAUTIONS field (#11) sequence numbers 1-22</td>
<td><p>Example, sequence 1 is:</p>
<p>PRECAUTIONS: Before taking allopurinol, tell your doctor or</p></td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,I</td>
<td>Node for word processing field</td>
<td>I</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,I,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,I,0</td>
<td>DRUG INTERACTIONS field (#10) zero node.</td>
<td>^^19^19^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,I</td>
<td>Node for word processing field</td>
<td>I</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,I,1</td>
<td>DRUG INTERACTIONS field (#10) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>6</td>
<td>1,I,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,I,1 - 19</td>
<td>DRUG INTERACTIONS field (#10) sequence 1-19.</td>
<td><p>Example, sequence 1 is:</p>
<p>DRUG INTERACTIONS: Your doctor or pharmacist may already be</p></td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,O</td>
<td>Node for word processing field</td>
<td>O</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,O,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td></td>
<td>1,O,0</td>
<td>OVERDOSE field (#8) zero node</td>
<td>^^4^4^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,O</td>
<td>Node for word processing field</td>
<td>O</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,O,1</td>
<td>DRUG INTERACTIONS field (#10) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1,O,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td></td>
<td>1,O,1 – 4</td>
<td>OVERDOSE field (#8) sequence 1 – 4</td>
<td><p>Example, sequence 1 is:</p>
<p>OVERDOSE: If overdose is suspected, contact a poison control</p></td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,N</td>
<td>Node for word processing field</td>
<td>N</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,N,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,N,0</td>
<td>NOTES field (#14) zero node.</td>
<td>^^8^8^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,N</td>
<td>Node for word processing field</td>
<td>N</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,N,1</td>
<td>NOTES field (#14) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>6</td>
<td>1,N,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,N,1 – 8</td>
<td>NOTES field (#14) sequence 1-8)</td>
<td><p>Example, sequence 1 is:</p>
<p>NOTES: Do not share this medication with others.</p></td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,D</td>
<td>Node for word processing field</td>
<td>D</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,D,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,D,0</td>
<td>MISSED DOSE field (#9) zero node.</td>
<td>^^8^8^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="even">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,D</td>
<td>Node for word processing field</td>
<td>D</td>
<td>Text</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,D,1</td>
<td>MISSED DOSE field (#9) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1,D,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,D,1 – 8</td>
<td>MISSED DOSE field (#9) sequence 1-8.</td>
<td><p>Example, sequence 1 is:</p>
<p>MISSED DOSE: If you miss a dose, take it as soon as you</p></td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>IEN for PMI-ENGLISH file (#50.621)</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,R</td>
<td>Node for word processing field</td>
<td>R</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,R,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>1,R,0</td>
<td>STORAGE field (#12) zero node.</td>
<td>^^11^11^3160223</td>
<td>Word Processing</td>
</tr>
<tr class="odd">
<td>1</td>
<td></td>
<td>SEGMENT</td>
<td>PMIDATA</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td></td>
<td>File</td>
<td>50.621</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>Field</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>1,R</td>
<td>Node for word processing field</td>
<td>R</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1,R,1</td>
<td>STORAGE field (#12) sequence number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>6</td>
<td>1,R,1,0</td>
<td>Sequence</td>
<td>0</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1,R,1-11</td>
<td>STORAGE field (#12) sequence 1-11.</td>
<td><p>Example, sequence 1 is:</p>
<p>STORAGE: Store the US product at room temperature between 59-77</p></td>
<td>Word Processing</td>
</tr>
</tbody>
</table>

### DATA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information in this section provides the GCNSEQNO information.

Example record from the .DAT file

DATA^196

2834^000266^000266^051079090620\|2835^062407^062407^049708041988\|2836^003693^003693^000054485851\|2837^003694^003694^000009001755\|2842^005020^005020^066992039910\|2843^005021^005021^000009002401\|

Data Values

| Piece | Description/Field Name                                | Data     | Data Type |
|-----------|-----------------------------------------------------------|--------------|---------------|
| 1         | Field Separator                                           | DATA         | String        |
| 2         | Sequence Number                                           | 195          | Number        |
| 1         | Internal Entry Number (IEN) for VA Product file (#50.68)  | 2834         | Pointer       |
| 2         | GCNSEQNO field (#12) of VA Product file (#50.68)          | 000266       | Number        |
| 3         | PREVIOUS GCNSEQNO field (#12) of VA Product file (#50.68) | 000266       | Number        |
| 4         | NDC LINK TO GCNSEQNO field (#13)                          | 051079090620 | Free Text     |

### DATANT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new entries at the file level for .01 fields. The file can be any NDF file, but the structure is the same.

Example record from the .DAT file

DATANT^50.416^1

10014^3141218.24535^.01^360^A

DATANT^50.416^2

ABSORPTION EIGHT

DATANT^50.416^1

Data Values

| Piece | Description/Field Name | Data         | Data Type |
|-----------|----------------------------|------------------|---------------|
| 1         | SEGMENT NAME               | DATANT           | String        |
| 2         | FILE NUMBER                | 50.416           | Number        |
| 3         | SEQUENCE NUMBER            | 1                | Number        |
| 1         | IEN for the file           | 10014            | Pointer       |
| 2         | DATE/TIME                  | 3141218.24535    | Date          |
| 3         | FIELD NUMBER               | .01              |               |
| 4         | PPS-N User ID              | 360              | Number        |
| 5         | A = Addition to the file   | A                | Free Text     |
| 1         | SEGMENT NAME               | DATANT           | Free Text     |
| 2         | FILE NUMBER                | 50.416           | Number        |
| 3         | SEQUENCE NUMBER            | 2                | Number        |
| 1         | DATA VALUE                 | ABSORPTION EIGHT | Free Text     |

### DATAN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the new entries for multiple type fields. The file can be any NDF file, but the structure is the same.

Example record from the .DAT file

DATAN^50.68^1

5217,129^3150427.29014^14,.01^360^A

DATAN^50.68^2

129

Data Values

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 46%" />
<col style="width: 23%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Piece</strong></th>
<th><strong>Description/Field Name</strong></th>
<th><strong>Data</strong></th>
<th><strong>Data Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>SEGMENT NAME</td>
<td>DATAN</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td>IEN for VA GENERIC file (#50.6)</td>
<td>50.68</td>
<td>Pointer</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sequence Number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>IEN to the file, IEN to the multiple fields.</td>
<td>5217,129</td>
<td>Pointer</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Date.Time</td>
<td>3150427.29014</td>
<td>Date</td>
</tr>
<tr class="even">
<td>3</td>
<td><p>Multiple field number, field number within the multiple.</p>
<p>In this example, it’s ACTIVE INGREDIENTS multiple field (#14) and ACTIVE INGREDIENTS field (#.01).</p></td>
<td>14,.01</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>PPS-N user ID</td>
<td>360</td>
<td>Number</td>
</tr>
<tr class="even">
<td>5</td>
<td>A = Addition to the file</td>
<td>A</td>
<td>Text</td>
</tr>
<tr class="odd">
<td>1</td>
<td>Segment Name</td>
<td>DATAN</td>
<td>Text</td>
</tr>
<tr class="even">
<td>2</td>
<td>File</td>
<td>50.68</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sequence</td>
<td>2</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>Data Value. In this case, it’s the</td>
<td>129</td>
<td>Free Text</td>
</tr>
</tbody>
</table>

### DATAO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the edits to any NDF file for single and multiple fields. The file can be any NDF file, but the structure is the same.

Example record from the .DAT file

DATAO^50.416^1

10013,1^3141218.24481^99.991,.02^360

DATAO^50.416^2

1

DATAO^50.68^1

22780^3141218.24481^101^360

DATAO^50.68^2

1

DATAO^50.67^1

222551^3160219.32985^1^360

DATAO^50.67^2

068094010961

DATAO^50.67^1

222551^3160219.32985^10^360

DATAO^50.67^2

O

DATAO^50.67^1

222551^3160219.32985^3^360

DATAO^50.67^2

3500

DATAO^50.67^1

222551^3160219.32985^4^360

DATAO^50.67^2

FISH OIL

DATAO^50.67^1

222551^3160219.32985^5^360

DATAO^50.67^2

26193

DATAN^50.67^1

222551,1^3160219.32985^6,.01^360^A

DATAN^50.67^2

N/A

DATAO^50.67^1

222551^3160219.32985^8^360

DATAO^50.67^2

953

DATAO^50.67^1

222551^3160219.32985^9^360

DATAO^50.67^2

974

Data Values

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 45%" />
<col style="width: 23%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Piece</strong></th>
<th><strong>Description/Field Name</strong></th>
<th><strong>Data</strong></th>
<th><strong>Data Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>SEGMENT NAME</td>
<td>DATAO</td>
<td>Free Text</td>
</tr>
<tr class="even">
<td>2</td>
<td>File - In this case, it’s DRUG INGREDIENTS file (#50.416)</td>
<td>50.416</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sequence Number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>IEN to the file, IEN to the multiple fields.</td>
<td>10013,1</td>
<td>Pointer</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Date</td>
<td>3141218.24481</td>
<td>Date</td>
</tr>
<tr class="even">
<td>3</td>
<td><p>Multiple field number, field number within the multiple.</p>
<p>In this example, it’s EFFECTIVE DATE/TIME multiple field (#99.991) and STATUS field (#.02).</p></td>
<td>99.991,.02</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>PPS-N user ID</td>
<td>360</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>Value for the field. In this case, its 1 for ACTIVE for STATUS field (#.02) of the EFFECTIVE DATE/TIME multiple (#99.991).</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>SEGMENT NAME</td>
<td>DATAO</td>
<td>Free Text</td>
</tr>
<tr class="even">
<td>2</td>
<td>FILE - In this case, it’s VA PRODUCT file (#50.68)</td>
<td>50.68</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sequence Number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>IEN to the file</td>
<td>22780</td>
<td>Pointer</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Date</td>
<td>3141218.24481</td>
<td>Date</td>
</tr>
<tr class="even">
<td>3</td>
<td>Field IEN for the file. In this case, it’s the HAZARDOUS TO HANDLE field (#101) for VA PRODUCT file (#50.68)</td>
<td>101</td>
<td>Pointer</td>
</tr>
<tr class="odd">
<td>4</td>
<td>PPS-N user ID</td>
<td>360</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>Value. In this case, it’s 1 for YES</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>SEGMENT NAME</td>
<td>DATAO</td>
<td>Free Text</td>
</tr>
<tr class="even">
<td>2</td>
<td>File. In this case, NDC/UPN file (#50.67)</td>
<td>50.67</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sequence Number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>IEN for the file</td>
<td>222551</td>
<td>Pointer</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Date</td>
<td>3160219.32985</td>
<td>Date</td>
</tr>
<tr class="even">
<td>3</td>
<td>Field Number</td>
<td>1</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>4</td>
<td>PPS-N user ID</td>
<td>360</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>SEGMENT NAME</td>
<td>DATAO</td>
<td>Free Text</td>
</tr>
<tr class="odd">
<td>2</td>
<td>File. In this case, NDC/UPN file (#50.67)</td>
<td>50.67</td>
<td>Number</td>
</tr>
<tr class="even">
<td>3</td>
<td>Sequence Number</td>
<td>1</td>
<td>Free Text</td>
</tr>
<tr class="odd">
<td>1</td>
<td>IEN for the file</td>
<td>222551</td>
<td>Pointer</td>
</tr>
<tr class="even">
<td>2</td>
<td>Date</td>
<td>3160219.32985</td>
<td>Date</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Field number for the file</td>
<td>10</td>
<td>Number</td>
</tr>
<tr class="even">
<td>4</td>
<td>PPS-N user ID</td>
<td>360</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>1</td>
<td>SEGMENT NAME</td>
<td>DATAO</td>
<td>Free Text</td>
</tr>
<tr class="even">
<td>2</td>
<td>File</td>
<td>50.67</td>
<td>Number</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sequence Number</td>
<td>2</td>
<td>Number</td>
</tr>
<tr class="even">
<td>1</td>
<td>NDC</td>
<td>068094010961</td>
<td>Number</td>
</tr>
</tbody>
</table>

### PRODUCT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains all of the products defined.

Example record from the .DAT file

PRODUCT^2830

PRODUCT^2831

Data Values

| Piece | Description/Field Name       | Data | Data Type |
|-----------|----------------------------------|----------|---------------|
| 1         | SEGMENT NAME                     | PRODUCT  | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 2830     | Pointer       |
| 1         | SEGMENT NAME                     | PRODUCT  | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 2831     | Pointer       |

### GENERIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the VA Generic entries that were modified.

Example record from the .DAT file

GENERIC^10003

GENERIC^10004

Data Values

| Piece | Description/Field Name      | Data | Data Type |
|-----------|---------------------------------|----------|---------------|
| 1         | SEGMENT NAME                    | GENERIC  | Text          |
| 2         | IEN for VA GENERIC file (#50.6) | 10003    | Pointer       |
| 1         | SEGMENT NAME                    | GENERIC  | Text          |
| 2         | IEN for VA GENERIC file (#50.6) | 10004    | Pointer       |

### POE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the copay related reference.

Example record from the .DAT file

POE^12994

POE^13576

Data Values

| Piece | Description/Field Name       | Data | Data Type |
|-----------|----------------------------------|----------|---------------|
| 1         | SEGMENT NAME                     | POE      | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 12995    | Pointer       |
| 1         | SEGMENT NAME                     | POE      | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 13576    | Pointer       |

### CMOP - 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example record from the .DAT file

CMOP^10025

CMOP^23841

Data Values

| Piece | Description/Field Name       | Data | Data Type |
|-----------|----------------------------------|----------|---------------|
| 1         | SEGMENT NAME                     | CMOP     | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 10025    | Pointer       |

### NFI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the National Formulary reference.

Example record from the .DAT file

NFI^1668

NFI^4657

Data Values

| Piece | Description/Field Name       | Data | Data Type |
|-----------|----------------------------------|----------|---------------|
| 1         | SEGMENT NAME                     | NFI      | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 1668     | Pointer       |
| 1         | SEGMENT NAME                     | NFI      | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 1668     | Pointer       |

### CLASS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the VA Drug class references.

Example record from the .DAT file

CLASS^25303^0

25303^319^4977

CLASS^25304^0

25304^319^4977

Data Values

| Piece | Description/Field Name           | Data | Data Type |
|-----------|--------------------------------------|----------|---------------|
| 1         | SEGMENT NAME                         | CLASS    | Text          |
| 2         | IEN for VA PRODUCT file (#50.68)     | 13018    | Pointer       |
| 3         | Sequence                             | 0        | Number        |
| 1         | IEN for VA PRODUCT file (#50.68)     | 13018    | Pointer       |
| 2         | IEN for VA DRUG CLASS file (#50.605) | 319      | Pointer       |
| 3         | IEN for VA GENERIC file (#50.6)      | 4977     | Pointer       |
| 1         | SEGMENT NAME                         | CLASS    | Text          |
| 2         | IEN for VA PRODUCT file (#50.68)     | 25304    | Pointer       |
| 3         | Sequence                             | 0        | Number        |
| 1         | IEN for VA PRODUCT file (#50.68)     | 25304    | Pointer       |
| 2         | IEN for VA DRUG CLASS file (#50.605) | 319      | Pointer       |
| 3         | IEN for VA GENERIC file (#50.6)      | 4977     | Pointer       |

### REM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains products that require re-matching.

Example record from the .DAT file

REM^1784

1785

REM^5153

5154

Data Values

| Piece | Description/Field Name       | Data | Data Type |
|-----------|----------------------------------|----------|---------------|
| 1         | SEGMENT NAME                     | REM      | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 1784     | Pointer       |
| 1         | SEGMENT NAME                     | REM      | Text          |
| 2         | IEN for VA PRODUCT file (#50.68) | 5154     | Pointer       |

### MESSAGE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the information for the DATA UPDATE FOR NDF report email.

Example record from the .DAT file

MESSAGE^0^0

^^157^157^3150429

MESSAGE^1^0

MESSAGE^2^0

The following VA Products have been added to the National

MESSAGE^3^0

Drug File.You may wish to review, then match or unmatch

MESSAGE^4^0

local drug file entries based on this updated information.

MESSAGE^5^0

MESSAGE^6^0

ALCLOMETASONE 0.02% CREAM,TOP \[A1745\]

MESSAGE^7^0

(DISPENSE UNIT - 0.2ML EACH)

MESSAGE^8^0

ALCLOMETASONE 0.05% CREAM,TOP \[A1746\]

MESSAGE^9^0

(DISPENSE UNIT - GM)

MESSAGE^10^0

ALCLOMETASONE 0.06% CREAM,TOP \[A1748\]

MESSAGE^11^0

(DISPENSE UNIT - GM)

MESSAGE^12^0

ALCLOMETASONE 0.08% CREAM,TOP \[A1747\]

MESSAGE^13^0

(DISPENSE UNIT - GM)

MESSAGE^14^0

ALFALFA 500MG TAB \[A1403\]

MESSAGE^15^0

(DISPENSE UNIT - TAB)

MESSAGE^16^0

12534-0369-03 12634-0369-03 77273-0700-25 77273-0700-50

MESSAGE^17^0

00761-0183-20

MESSAGE^18^0

AMYLASE 60MG/PAPAIN 60MG TAB,CHEW \[null\]

MESSAGE^19^0

(DISPENSE UNIT - null)

MESSAGE^20^0

ASPIRIN 150MG TAB \[A1749\]

MESSAGE^21^0

(DISPENSE UNIT - CAP/TAB)

MESSAGE^22^0

ASPIRIN 200MG TAB \[A1750\]

MESSAGE^23^0

(DISPENSE UNIT - CAP/TAB)

MESSAGE^24^0

ASPIRIN 250MG TAB \[A1751\]

MESSAGE^25^0

(DISPENSE UNIT - CAP/TAB)

MESSAGE^26^0

BI SUBCARBONATE 260MG/KAOLIN 5.2GM/PECTIN 260MG/30ML SUSP \[B0171\]

MESSAGE^27^0

(DISPENSE UNIT - ML)

MESSAGE^28^0

IV INFUSION SET (WINTHROP) \[null\]

MESSAGE^29^0

(DISPENSE UNIT - null)

MESSAGE^30^0

00074-9245-68 00074-6646-01 00074-6516-01 00074-6480-02

MESSAGE^31^0

00074-1169-01 08290-3872-26 00074-9247-68 00074-9246-68

MESSAGE^32^0

00074-6517-03 00074-6517-01 00074-6516-03 00074-6462-01

MESSAGE^33^0

00074-6440-12 00074-3559-03 00074-1877-68 00074-1753-02

MESSAGE^34^0

00074-1642-48 08024-3900-01 00074-9252-68

MESSAGE^35^0

MENTHOL 1.25%/ME NICOTINATE 0.7%/ME SALICYLATE 30% OINT,TOP \[null\]

MESSAGE^36^0

(DISPENSE UNIT - null)

MESSAGE^37^0

MENTHOL 3%/ME NICOTINATE 0.5%/ME SALICYLATE 30% GEL,TOP \[A0515\]

MESSAGE^38^0

(DISPENSE UNIT - GM)

MESSAGE^39^0

41100-0078-72 41100-0080-29 41100-0079-48 41100-0081-36

MESSAGE^40^0

41100-0079-63 41100-0080-52

MESSAGE^41^0

TRICLOSAN 0.1%/ZINC OXIDE 10.8% PWDR,TOP \[T0205\]

MESSAGE^42^0

(DISPENSE UNIT - GM)

MESSAGE^43^0

41100-0087-25

MESSAGE^44^0

UNIBASE OINT \[null\]

MESSAGE^45^0

(DISPENSE UNIT - null)

MESSAGE^46^0

00047-3122-23

MESSAGE^47^0

VISHNU WARFARIN 150MG TAB \[V0251\]

MESSAGE^48^0

(DISPENSE UNIT - TAB)

MESSAGE^49^0

MESSAGE^50^0

The following active VA Products are no longer marked for CMOP.

MESSAGE^51^0

All local drug file entries matched to these VA Products will

MESSAGE^52^0

be UNMARKED for CMOP. In order to have these entries dispensed

MESSAGE^53^0

by CMOP any local DRUG file (#50) entries matched to these

MESSAGE^54^0

products must be re-matched to another VA product that is actively

MESSAGE^55^0

marked for CMOP dispensing.

MESSAGE^56^0

MESSAGE^57^0

AMYLASE 60MG/PAPAIN 60MG TAB,CHEW \[null\]

MESSAGE^58^0

ASPIRIN 250MG TAB \[A1751\]

MESSAGE^59^0

ASPIRIN 500MG/CAFFEINE 32MG TAB \[A1707\]

MESSAGE^60^0

MESSAGE^61^0

The following products will be inactivated on the date listed. No alternative

MESSAGE^62^0

products have been found.

MESSAGE^63^0

MESSAGE^64^0

DRESSING,PROMOGRAN MATRIX 19.1IN X 19.1IN JJ#PG019 \[XU657\]

MESSAGE^65^0

02/15/2014

MESSAGE^66^0

DRESSING,PROMOGRAN PRISMA MATRIX 4.34SQ IN JJ#MA028 \[XT106\]

MESSAGE^67^0

02/15/2014

MESSAGE^68^0

EPOPROSTENOL NA 1.5MG/VIL INJ \[E0217\]

MESSAGE^69^0

02/10/2014

MESSAGE^70^0

DRESSING,PROMOGRAN PRISMA MATRIX 19.1SQ IN JJ#MA123 \[XT105\]

MESSAGE^71^0

02/15/2014

MESSAGE^72^0

EPOPROSTENOL NA 0.5MG/VIL INJ \[E0216\]

MESSAGE^73^0

02/10/2014

MESSAGE^74^0

DRESSING,PROMOGRAN MATRIX 4.34IN X 4.34IN JJ#PG004 \[XU658\]

MESSAGE^75^0

02/15/2014

MESSAGE^76^0

MESSAGE^77^0

The following product(s) have been inactivated. No alternative products have

MESSAGE^78^0

been found.

MESSAGE^79^0

MESSAGE^80^0

AMYLASE 60MG/PAPAIN 60MG TAB,CHEW \[null\]

MESSAGE^81^0

ASPIRIN 150MG TAB \[A1749\]

MESSAGE^82^0

ASPIRIN 200MG TAB \[A1750\]

MESSAGE^83^0

ASPIRIN 250MG TAB \[A1751\]

MESSAGE^84^0

IV INFUSION SET (WINTHROP) \[null\]

MESSAGE^85^0

NIACIN 1000MG/SIMVASTATIN 40MG TAB,SA \[N0627\]

MESSAGE^86^0

UNIBASE OINT \[null\]

MESSAGE^87^0

MESSAGE^88^0

The National Formulary Indicator has changed for the following

MESSAGE^89^0

VA Products. The National Formulary Indicator will automatically

MESSAGE^90^0

be changed in your local DRUG file (#50). Please review the

MESSAGE^91^0

VISN and Local Formulary designations of these products and

MESSAGE^92^0

make appropriate changes.

MESSAGE^93^0

MESSAGE^94^0

FORMULARY ITEMS

MESSAGE^95^0

NONE

MESSAGE^96^0

MESSAGE^97^0

NON-FORMULARY ITEMS

MESSAGE^98^0

NONE

MESSAGE^99^0

MESSAGE^100^0

The following VA Generic Name(s) have been edited or added. Any product

MESSAGE^101^0

matched to these products will be unmatched. If site wants to continue to use

MESSAGE^102^0

the product the site must rematch to local file \#50 entries to the listed VA

MESSAGE^103^0

product.

MESSAGE^104^0

MESSAGE^105^0

BANDAGE TUBULAR ELASTIC NET SZ 0.5 X25YD \[XS807\]

MESSAGE^106^0

Old Value: BANDAGE

MESSAGE^107^0

New Value: BANDAGE,STRETCH

MESSAGE^108^0

BANDAGE TUBULAR ELASTIC NET SZ 10 X 25YD \[XS854\]

MESSAGE^109^0

Old Value: BANDAGE

MESSAGE^110^0

New Value: BANDAGE TUBULAR

MESSAGE^111^0

MESSAGE^112^0

The following VA Print Name(s) have been edited or added. Any product matched

MESSAGE^113^0

to these products will be unmatched. If site wants to continue to use the

MESSAGE^114^0

product the site must rematch to local file \#50 entries to the listed VA product.

MESSAGE^115^0

MESSAGE^116^0

AMINOCAPROIC ACID 500MG TAB \[A1744\]

MESSAGE^117^0

Old Value: AMINOCAPROIC ACID 500MG TAB

MESSAGE^118^0

New Value: AMINOCAPROIC ACID 500MG TAB-TEST3

MESSAGE^119^0

ASPIRIN 325MG TAB,EC,UD \[A1752\]

MESSAGE^120^0

Old Value: ASPIRIN 325MG EC TAB UD

MESSAGE^121^0

New Value: ASPIRIN 325MG EC TAB UD1

MESSAGE^122^0

MESSAGE^123^0

The following VA Product Identifier(s) have been edited or added. Any product

MESSAGE^124^0

matched to these products will be unmatched. If site wants to continue to use

MESSAGE^125^0

the product the site must rematch to local file \#50 entries to the listed VA

MESSAGE^126^0

product.

MESSAGE^127^0

MESSAGE^128^0

AMINOCAPROIC ACID 500MG TAB \[A1744\]

MESSAGE^129^0

Old Value: A0196

MESSAGE^130^0

New Value: A1744

MESSAGE^131^0

ASPIRIN 325MG TAB,EC,UD \[A1752\]

MESSAGE^132^0

Old Value: A0982

MESSAGE^133^0

New Value: A1752

MESSAGE^134^0

MESSAGE^135^0

The override dose form checks field has changed for the following products.

MESSAGE^136^0

MESSAGE^137^0

ASPIRIN 325MG/CARISOPRODOL 200MG TAB \[A0415\]

MESSAGE^138^0

changed from NO to YES

MESSAGE^139^0

MESSAGE^140^0

The following VA Drug Class(es) have been edited or added. The VA Class

MESSAGE^141^0

for this product will be automatically updated in file \#50.

MESSAGE^142^0

MESSAGE^143^0

ABACAVIR SO4 300MG TAB,UD \[A1010\]

MESSAGE^144^0

Old Value: AD200

MESSAGE^145^0

New Value: AM111

MESSAGE^146^0

ASPIRIN 325MG TAB,UD \[A1740\]

MESSAGE^147^0

Old Value: CN103

MESSAGE^148^0

New Value: CN104

MESSAGE^149^0

MESSAGE^150^0

The following product(s) have been unmatched. No alternative products

MESSAGE^151^0

have been found.

MESSAGE^152^0

MESSAGE^153^0

AMINOCAPROIC ACID 500MG TAB \[A1744\]

MESSAGE^154^0

ASPIRIN 325MG TAB,EC,UD \[A1752\]

MESSAGE^155^0

BANDAGE TUBULAR ELASTIC NET SZ 0.5 X25YD \[XS807\]

MESSAGE^156^0

BANDAGE TUBULAR ELASTIC NET SZ 10 X 25YD \[XS854\]

MESSAGE^157^0

Data Values

| Piece | Node            | Description/Field Name                        | Data                                                  | Data Type   |
|-----------|---------------------|---------------------------------------------------|-----------------------------------------------------------|-----------------|
| 1         |                     | SEGMENT                                           | MESSAGE                                                   | Text            |
| 2         | 1,2                 | Zero node for UPDATE CONTROL file (#5000)         | 0                                                         | Number          |
| 3         | 1,2,0               | Sequence                                          | 0                                                         | Number          |
| 1         | 1,2,0               | Data value for the zero node                      | ^^157^157^3150429                                         | Word Processing |
| 1         |                     | SEGMENT                                           | MESSAGE                                                   | Text            |
| 2         | 1,2                 | MESSAGE field (#2) node for word processing field | 1                                                         | Number          |
| 3         | 1,2,1               | Sequence                                          | 0                                                         | Number          |
| 1         | 1,2,1,0             | Data value                                        | Null                                                      | Text            |
| 1         |                     | SEGMENT                                           | MESSAGE                                                   | Text            |
| 2         | 1,2                 | MESSAGE field (#2) node for word processing field | 2                                                         | Number          |
| 3         | 1,2,2,0             | Sequence                                          | 0                                                         | Number          |
| 1         | 1,2,2,0 – 1,2,157,0 | MESSAGE field (#2) Data Value                     | The following VA Products have been added to the National | Word Processing |

### MESSAGE2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the information for the UPDATED INTERACTIONS AND FDA MED GUIDE report email.

Example record from the .DAT file

MESSAGE2^0^0

^^24^24^3150429

MESSAGE2^1^0

MESSAGE2^2^0

The following interactions in National Drug File (NDF) have been added,

MESSAGE2^3^0

edited or inactivated. These changes are the result of review and

MESSAGE2^4^0

recommendations from the NDF support group.

MESSAGE2^5^0

MESSAGE2^6^0

ADDED INTERACTION

MESSAGE2^7^0

MESSAGE2^8^0

NONE

MESSAGE2^9^0

MESSAGE2^10^0

EDITED INTERACTIONS

MESSAGE2^11^0

MESSAGE2^12^0

CARBAMAZEPINE/TASIMELTEON CRITICAL

MESSAGE2^13^0

CIPROFLOXACIN/TASIMELTEON SIGNIFICANT

MESSAGE2^14^0

MESSAGE2^15^0

INACTIVATED INTERACTIONS

MESSAGE2^16^0

MESSAGE2^17^0

NONE

MESSAGE2^18^0

MESSAGE2^19^0

The following products have been flagged for exclusion from drug-drug

MESSAGE2^20^0

interaction checks.

MESSAGE2^21^0

MESSAGE2^22^0

ACETAMINOPHEN 325MG TAB \[A0022\]

MESSAGE2^23^0

ASPIRIN 325MG TAB,EC,UD \[A1752\]

MESSAGE2^24^0

Data Values

| Piece | Node           | Description/Field Name                               | Data                                                                | Data Type   |
|-----------|--------------------|----------------------------------------------------------|-------------------------------------------------------------------------|-----------------|
| 1         |                    | SEGMENT                                                  | MESSAGE2                                                                | Text            |
| 2         | 1,3                | Zero node for UPDATE CONTROL file (#5000)                | 0                                                                       | Number          |
| 3         | 1,3,0              | Sequence                                                 | 0                                                                       | Number          |
| 1         | 1,3,0              | Data value for the zero node                             | ^^24^24^3150429                                                         | Word Processing |
| 1         |                    | SEGMENT                                                  | MESSAGE2                                                                | Text            |
| 2         | 1,3                | SECOND MESSAGE field (#6) node for word processing field | 1                                                                       | Number          |
| 3         | 1,3,1              | Sequence                                                 | 0                                                                       | Number          |
| 1         | 1,3,1,0            | Data value                                               | Null                                                                    | Text            |
| 1         |                    | SEGMENT                                                  | MESSAGE2                                                                | Text            |
| 2         | 1,3                | SECOND MESSAGE field (#6) node for word processing field | 2                                                                       | Number          |
| 3         | 1,3,2,0            | Sequence                                                 | 0                                                                       | Number          |
| 1         | 1,3,2,0 – 1,3,24,0 | SECOND MESSAGE field (#6) Data Value                     | The following interactions in National Drug File (NDF) have been added, | Word Processing |

### TEXT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the information for the header portion of the DRUGS UNMATCHED FROM NDF report email. The first sentence is generated by Vista and the following message text is the remainder of the header. This data is not stored in a file.

Example record from the .DAT file

TEXT^1

unmatched from the National Drug File (NDF). The VA Product

TEXT^2

name and CMOP ID corresponding to the unmatched local drug file

TEXT^3

names are listed on the indented line beneath each entry. An

TEXT^4

Inactivation Date may be listed for entries when this reason

TEXT^5

applies. Until you rematch these entries to NDF, they will not

TEXT^6

transmit to CMOP and drug-drug interaction checks will not check

TEXT^7

for these products. It is critical that you rematch these

TEXT^8

products immediately. You may also need to match a new

TEXT^9

orderable item. Any possible dosages and local possible

TEXT^10

dosages for these unmatched products have been deleted.

TEXT^11

Therefore, the dosages for each unmatched product should

TEXT^12

be reviewed after the rematch or recreated if the product

TEXT^13

cannot be rematched to a VA Product through the NDF

TEXT^14

Data Values

| Piece | Node | Description/Field Name | Data                                                    | Data Type |
|-----------|----------|----------------------------|-------------------------------------------------------------|---------------|
| 1         |          | SEGMENT                    | TEXT                                                        | Text          |
| 2         |          | Sequence 1-14              | 1 -14                                                       | Number        |
| 1         |          | Header line value          | unmatched from the National Drug File (NDF). The VA Product | Text          |

(This page included for two-sided copying.)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Automatic Match by NDC Matching Pairing of a drug from the local DRUG file (#50) with a drug in the National Drug File with the same NDC number. This matching will be accomplished when the option *Automatic Match of Unmatched Drugs* is executed for the first time.
Active Drug Drugs which contain no inactivation date in the INACTIVE DATE field (#100) local DRUG file (#50).
API Application Programmer Interface.
DEA, SPECIAL HDLG Field Field \#3. A field in the local DRUG file (#50). It contains one or more codes representing special characteristics of a product.
DRUG File See Local DRUG file.
DRUG INGREDIENTS File File \#50.416. A file that contains individual generic drugs which are components of various drug products.
Error In the National Drug File (NDF) software, an error is an entry in the NATIONAL DRUG TRANSLATION file (#50.12) that does not have a match in the local DRUG file (#50).
FDA Medication Guide Paper handouts that come with many prescription medicines given to the patient. The guides address issues that are specific to particular drugs and drug classes, and contain FDA-approved information that can help patients avoid serious adverse events.
FSN Federal Stock Number. A unique identifying number assigned by the Federal Supply System to a product (drug, supply, food item, etc.) for ordering and accounting purposes. Synonymous with the National Stock Number (NSN). This is one of the fields in the local DRUG file (#50).
Local DRUG File (#50) This file contains the local GENERIC NAME (#.01), INACTIVE DATE (#100), DEA, SPECIAL HDLG (#3), and NDC fields, as well as others. NDF software attempts to match products from this file with products in the VA GENERIC file (#50.6) and the VA PRODUCT file (#50.58).
Manually Classed Drug A drug from the local DRUG file (#50) which could not be matched, but has been assigned a VA Drug Classification through the use of the *Allow Unmatched Drugs to Be Classed* menu option.
Manufacturer Code The first portion of the NDC Number (the first 4-6 digits). Identifies the manufacturer of the product.
NATIONAL DRUG File (#50.6) This file contains a list of available drug products. It includes specific information for each product, including trade name, NDC number, manufacturer, VA Drug Class code, dosage form, route of administration, strength, units, ingredients, ingredient strength and units, package code, package size, package type, VA Product Name, and VA generic name. NDF software attempts to match products from this file with products in the local DRUG file (#50).
National Drug Identifier A unique, HL7 compatible code assigned to all products marked for CMOP transmission. This code is utilized to transmit VA Print name and dispense unit from VistA to the vendor system.
NATIONAL DRUG File (#50.6) This file contains a list of available drug products. It includes specific information for each product, including trade name, NDC number, manufacturer, VA Drug Class code, dosage form, route of administration, strength, units, ingredients, ingredient strength and units, package code, package size, package type, VA product name, and VA generic name. NDF software attempts to match products from this file with products in the local DRUG file (#50).
NATIONAL DRUG A temporary file that is created by the
TRANSLATION File (#50.612) NDF software. This file will contain information on drugs that have been matched, or for which a match was attempted.
NDC (NDC Number) National Drug Code. A unique number assigned to a drug by the manufacturer for identification purposes. The NDC is in one of three formats: 4-4-2, 5-3-2, or 5-4-1. The first part is the manufacturer’s code, the second part is the product number, and the last is the code for the package size and type. This is one of the fields in the local DRUG file (#50).
NDF National Drug File. Refers to the National Drug File software.
Package Code The last portion of the NDC number (the last two digits). This identifies the package type and size in which the product is supplied.
Package Size The actual (physical) amount of a drug in the individual package (i.e., 5000 capsules per bottle).
Package Type The physical container in which a drug is supplied (i.e., bottle, vial).
PPS-N The Pharmacy Product System-National (PPS-N) is a Web-based application that provides the ability to manage pharmacy-specific data across the VA enterprise, ensuring that all facilities are using the same base data for their operations. It allows approved national VA personnel to easily, quickly, and safely manage the VA National Formulary which directs which products (such as medications and supplies) are to be purchased and used by the VA hospital system.
Product Code The second portion of the NDC number (the second four digits) that identifies the specific drug.
PSNMGR The name of the primary menu option and of the key that must be assigned to the pharmacy coordinator and supervisors using the National Drug File software.
Supply Item A non-drug item entered into the GENERIC NAME field (# .01) of the local DRUG file (#50) that may be a prosthetic or expendable item such as ostomy supply, alcohol pads, syringes, bed pans, etc. identified by the code “S” in the DEA/SPECIAL HDLG field (#3) of the local DRUG file (#50).
Trade Name This is the brand name. The name given to a generic product to distinguish it as one produced and sold by a specific manufacturer.
UPC Universal Product Code. A unique number assigned to a product by a manufacturer commonly used for supply items. These may be found in the NDC/UPN file (#50.67).
VA Dispense Unit The standardized unit assigned to a product when the product is marked for CMOP transmission.
VA DRUG CLASS File (#50.605) This file contains the VA Drug Classification codes and their descriptions. Each product has one of these codes assigned to it and stored with it.
VA Generic Name A name given to an item (drug, supply, etc. in the VA GENERIC file (#50.6)). It is this name which is matched with the entry in the GENERIC NAME (local generic name) field (#.01) of the local DRUG file (#50). This name does not contain strength, unit, or dosage form.
VA Print Name The forty character name assigned as the name which prints on all prescription labels for products marked for CMOP transmission.
VA Product Name The unique name assigned to each drug product in the National Drug File. This name comes from the VA PRODUCT file (#50.68) and includes strength, unit, and dosage form.
VHA Veterans Healthcare Administration
VistA Veterans Health Information Systems and Technology Architecture.
VUID VHA Unique Identifier. A unique integer assigned to reference terms VHA wide.
(This page included for two-sided copying.)

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Archiving and Purging · 14
C
Callable Routines · 14
E
External Interfaces · 14
External Relations · 16
F
File Security · 31
Files · 9
I
Internal Relations · 16
N
National Drug File V. 4.0 Menu · 12
P
Package-Wide Variables · 16
Pharmacy Product System – National (PPS-N) · 2
Precautions and Potential Problems · 29
PSNMGR Key · 29, 30
R
Resource Requirements · 4
S
Security Management · 29, 32
Software Product Security · 28


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: National Drug File Version 4 Technical Manual (Updated PSN*4*218)

## Note regarding Patch PSN\*4\*101 Pharmacy Data Standardization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch does not affect any Pharmacy functionality or end-users. This patch requires the HEALTH DATA & INFORMATICS (HDI) 1.0 package in addition to required patch release checks.

The scope of Data Standardization - Pharmacy enhancement project is to modify the VISTA Pharmacy National Drug File (NDF) structures in order to meet the established standards for elements required by Data Standardization to implement a common set of standards for Clinical Health Data Repository (CHDR) and the Health Data Repository (HDR).

To accomplish data standardization with VISTA Pharmacy and data flow to CHDR and HDR, a Veterans Health Administration Unique Identifier (VUID) and the

TERMSTATUS subscript Effective Date/Status will be populated in four files within the VISTA Pharmacy National Drug File package. VUID numbers will be generated dynamically and programmatically for each product. The VUID numbers have been assigned to National Drug File with a predetermined range (4000624- 4500623). There will be a one-time conversion to update the National Drug File package files. Once the Application Patch (PSN\*4\*101) and the VUID data have been installed in the four Globals for the Data Domain (NDF), the Application Post-install routine calls an API in the HDI package to update the VUID Seeding Process as Complete.

The four VISTA Pharmacy files being "standardized" are:

VA PRODUCT file (#50.68)

DRUG INGREDIENTS file (#50.416)

VA DRUG CLASS file (#50.605)

VA GENERIC file (#50.6)

## Note regarding Patch PSN\*4\*169 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch makes these corrections to the INQUIRE TO VA PRODUCT INFO FOR LOCAL DRUG \[PSNLOOK\] option:

> Problem: Sometimes the Active Ingredients would not display.

> Solution: The Active Ingredients will now always display.

> Problem: Sometimes the Strength that is displayed next to the Active

> Ingredient is actually the Strength of the VA Product.

> Solution: The Strength of the Active Ingredient will now accurately display.

> Problem: The Drug Unit was not always displaying.

> Solution: The Drug Unit will now always display.

> Problem: Only the CS FEDERAL SCHEDULE code was displaying, and

> not the text.

> Solution: For the CS FEDERAL SCHEDULE, both the code and text will

> now display.

> Problem: When displaying the Active Ingredients, the text (Primary) will

> no longer display next to an Active Ingredient that is a Primary

> Ingredient.

> Solution: The Primary Ingredient will now display if the Ingredient of the

> VA Product has a Primary Ingredient.

This patch makes these corrections to the INQUIRE TO NATIONAL FILES \[PSNACT\] option:

> Problem: Only the CS FEDERAL SCHEDULE code was displaying, and

> not the text.

> Solution: For the CS FEDERAL SCHEDULE, both the code and text will

> now display.

> Problem: The National Formulary Restriction display was being truncated

> after one line if it was two or more lines in length.

> Solution: The entire text entered for the National Formulary Restriction

> will now display.

(This page included for two-sided copying.)

Software Product Security
