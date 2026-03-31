---
title: AICS Version 3 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: IBD
app_name: Automated Information Collection System (AICS)
section: FIN
app_status: active
pkg_ns: IBD
patch_ver: 3
patch_id: IBD*3
group_key: "IBD:IBD:3"
file_numbers: 
  - 357
security_keys: []
menu_options: 3
description: "<table> <colgroup> <col style=\\"width: 14%\\" /> <col style=\\"width: 14%\\" /> <col style=\\"width: 46%\\" /> <col style=\\"width: 25%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><strong>Date</strong></td> <td><strong>Version</strong></td> <td><strong>Description</strong></td> <td><strong>Author</strong></td> "
audience: 
keywords: 
  - class
  - span
  - encounter
  - aics
  - anchor
  - form
  - forms
  - print
  - package
  - options
page_count: 0
word_count: 4844
section_count: 0
table_count: 42
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics_3_0tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics_3_0tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=30"
---

aUTOMATED iNFORMATIONCOLLECTION SYSTEMAICSTECHNICALManual

![](aics-version-3-technical-manual/001.png)

April 1997

Office of Information and Technology

Product Development

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 46%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Version</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>April 2014</td>
<td><p>IBD*3.0*63</p>
<p>p. <a href="#ICDpiii">iii</a></p>
<p>p. <a href="#ICDp1">1</a></p>
<p>pp. <a href="\l">5</a>-<a href="\l">6</a></p>
<p>p. <a href="\l">7</a></p>
<p>p. <a href="#ICDp11">11</a></p>
<p>p. <a href="#ICDp25">25</a></p>
<p>p. <a href="#ICDp27">27</a></p></td>
<td><p>Updates for ICD-10 remediation.</p>
<p>Updated Table of Contents</p>
<p>Updated information in Introduction</p>
<p>Added information on ICD-10 codes</p>
<p>Added info on VA policy for printing</p>
<p>Added CODING SYSTEM UPDATES file</p>
<p>Added File #357.03 to VA FileMan Access Codes</p>
<p>Added ICD-10-CM to definition</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>April 1997</td>
<td>AICS Version 3.0</td>
<td>Initial publication of document</td>
<td></td>
</tr>
</tbody>
</table>

Preface

This is the technical manual for the Automated Information Collection System (AICS) V. 3.0 software package. It is designed to assist IRM personnel in operation and maintenance of the package.

For information regarding use of this software, please refer to the AICS User Manual. For further information on installation and maintenance of this package, Release Notes and an Installation Guide are provided.

<span id="ICDpiii" class="anchor"></span>Table of Contents

[Introduction 1](#Introduction)

[Orientation 3](#Orientation)

> [Note to Users with QUME Terminals 3](#QUME)

[General Information 5](#General)

> [Namespace Conventions 5](#Namespace)

> [Integrity Checker 5](#Integrity)

> [Resource Requirements 5](#Resource)

> [Updates for ICD-10 Codes 5](#Updates)

[Implementation and Maintenance 7](#Implementation)

> [Setting Up Workstations 8](#Setting)

[Routines 9](#Routines)

> [Routines to Map 9](#Map)

> [Obsolete Routines 9](#Obsolete)

> [Callable Routines 9](#Callable)

> [Routine List 10](#List)

[Files 11](#Files)

> [Globals to Journal 11](#Globals)

> [File List 11](#Filelist)

> [File Flow (Relationships between files) 13](#Fileflow)

> [Templates 13](#Templates)

[Exported Options 15](#Exportedoptions)

> [Menu Diagram 15](#Menu)

> [Exported Protocols 15](#Exportedprotocols)

> [Exported Options 15](#Exportedoptions2)

> [Exported Remote Procedures 16](#Remote)

> [Options without Parents 16](#Withoutparents)

[Archiving and Purging 17](#Archiving)

> [Archiving 17](#Archiving2)

> [Purging 17](#Purging)

[External Relations 19](#External)

> [Database Integration Agreements (DBIAs) 19](#DBIA)

> [Custodial Agreements 19](#Custodial)

> [Subscriber Agreements 19](#Subscriber)

> [General Security 25](#Generalsecurity)

> [Security Keys 25](#Securitykeys)

> [VA FileMan Access Codes 25](#Filemanaccess)

[Glossary 27](#Glossary)

[Index 33](#Index)

<span id="Introduction" class="anchor"></span>Introduction

<span id="ICDp1" class="anchor"></span>The encounter form is designed specifically for outpatient visits. It is used both to display relevant patient data for use during the visit, such as demographics, allergies, and problems; and to collect data about the visit, such as procedures and tests performed. Its primary focus is clinical and to collect data for the Ambulatory Care Reporting Project. It also has other purposes such as collecting data necessary for billing.

The AICS package contains all the software necessary to design, edit, and assign encounter forms to clinics. The software enables collection of outpatient clinical and administrative data and provides a more organized, less obtrusive method of data collection to the clinician and supporting clerical staff.

Many of the lists that a user sees in Computerized Patient Record System (CPRS) for input of outpatient encounter data are based on lists created when designing encounter forms for clinics.

A form generator is included, which allows sites to design forms which meet local medical facility needs. There is enough flexibility in the software so sites can build forms that meet their individual clinical, billing, and resource requirements. The encounter form may be filed in the clinical record.

A print manager is included that allows sites to print blank encounter forms, but only on a contingency basis or for non-patient uses such as employee health, since VA policy prohibits the use of printed encounter forms as a rule. Reports and Utilities options are available to assist with maintenance of the encounter forms.

Features supporting the scanning of encounter forms are no longer available, with the onset of electronic means of entering data using the lists provided in the encounter forms, such as CPRS.

<span id="Orientation" class="anchor"></span>Orientation

The AICS V. 3.0 Technical Manual is divided into major sections for general clarity and simplification of the material being presented. This manual is intended for use as a reference document by technical computer personnel.

The Implementation and Maintenance Section provides information on any aspect of the package that is site configurable. Instructions on how to obtain information about the relationships between the AICS V. 3.0 files and files external to the package are provided in Files Section. This section also includes instructions on how to obtain information on any AICS V. 3.0 input, print, and sort templates. There are also sections on archiving and purging, how to generate on-line documentation, and package-wide variables.

<span id="QUME" class="anchor"></span>Note to Users With QUME Terminals

It is very important that you set up your QUME terminal properly for this release of AICS. After entering your access and verify codes, you will see

Select TERMINAL TYPE NAME: {type}//

Please make sure that \<C-QUME\> is entered here. This entry will become the default. You can then press \<RET\> at this prompt for all subsequent log-ins. If any other terminal type configuration is set, options using the List Manager utility (such as Clinic Setup/Edit Forms option under the Edit Encounter Forms Menu) will neither display nor function properly on your terminal.

<span id="General" class="anchor"></span>General Information

<span id="Namespace" class="anchor"></span>Namespace Conventions

The namespace and file ranges assigned to the AICS package are IBD, files \#357 through \#359.94.

<span id="Integrity" class="anchor"></span>Integrity Checker

The IBDNTEG routine checks integrity for other IBD\* or AICS routines. This was built using the KERNEL utility routine, XTSUMBLD.

<span id="Resource" class="anchor"></span>Resource Requirements

AICS V. 3.0 requires a small amount of additional capacity to edit and store the format of the encounter forms. Additional disk capacity is used to store a form definition each time a form is redesigned. In addition, approximately 1K is required for each 10 appointments printed. This data can be purged after 90 days. The printing of encounter forms will require at least one dedicated printer that most sites have already received. The printing will require additional CPU capacity; however, this job may be scheduled during non-peak workload hours.

<span id="Updates" class="anchor"></span>Updates for ICD-10 Codes

Patch IBD\*3\*63 makes the following changes to the AICS package:

- Added a new “Encounter Forms ICD-10 Update” report.
  - A new menu item—Encounter Forms \> Reports and Utilities \> Encounter Forms ICD-10 Update—was introduced to run this report. This new report allows you to display a list of Encounter Forms and Clinics after making selections from several input options. When the report has been displayed, you may then update the ICD-10 Status field.
  - Two date fields show the latest dates that the form was changed. The history fields contain the user ID (DUZ) of the person who last changed the files.
- Added ICD-10 Code selections in Encounter Forms and Maintenance Utility Active/Inactive Report.
- Added ICD-10 Code wildcard search help text, including a partial code wildcard search.
- The Replace Code option in the Maintenance Utility Report uses the approved standard Lexicon partial code search.
- The Problem List Package Interfaces are obsolete; therefore, the Problem List Package Interfaces are now Unavailable.

<span id="Implementation" class="anchor"></span>Implementation and Maintenance

There are steps that the local site should take before encounter forms can be used.

First, forms must be designed and assigned to the clinics. Forms can be shared between clinics, but it is important to control who has responsibility for editing the shared forms. One important aspect of designing encounter forms is determining what codes should go on the form. Many encounter forms will have lists of CPT codes, diagnosis codes, or problems. Because space on an encounter form is at a premium, careful analysis is required to determine the codes most commonly used by the clinic before entering codes on the form. For CPT codes, the option Most Commonly Used Outpatient CPT Codes can be used to determine a clinic's most commonly used codes.

A print manager is included that allows sites to print blank encounter forms, but only on a contingency basis or for non-patient uses such as employee health, since VA policy prohibits the use of printed encounter forms as a rule. Reports and Utilities options are available to assist with maintenance of the encounter forms.

Procedures for printing the encounter forms must be determined. Following are some of the questions that must be answered.

What printers to use?

Can the printers be loaded with enough paper?

How many days in advance should the forms be printed?

What time of day to run the print job?

Should the printers be watched?

What to do if there are printer problems?

It is expected that most printing of forms will be done in batch at night for entire divisions and that forms will be printed several days in advance with only the additions printed the night before.

Then there are questions concerning what to do with the encounter forms.

How will the completed encounter forms be routed?

Data entry vs. scanning.

The Print Manager is expected to be very useful to the local sites. Sites must decide which reports should be printed. The Print Manager allows these reports to be specified along with the encounter forms. The fastest way to define the reports is at the division level, rather than at the clinic level. Individual clinics can override reports defined to print at the division level.

<span id="Setting" class="anchor"></span>Setting Up Workstations

We are recommending the following steps in implementing the Scanning Workstation software.

1.  Install the PC workstations in the area where they will be located complete with the scanners attached. This is a good time to let users become comfortable with the PC and in using a mouse, especially if they have no PC experience.
2.  Install the RPC Broker on the workstations and make sure that it is working. This will require a TCP network connection.
3.  Test the Paper Keyboard application and make sure it is loaded correctly and will run. Run a test of scanning with Paper Keyboard. There are several samples available.
4.  Make any final changes to the forms that are needed. There is one new block for the MAS classification questions that presents only those classifications that are appropriate, and allows input of yes and no. In addition, some sites will want to implement other new functionality such as CPT multipliers, multiple diagnosis codes, and a new practitioner block.
5.  Test the scannability of the encounter forms using one of the Manual Data Entry options. These options mimic scanning and can be used to see how an encounter form will behave when scanned. With functionality put in place by the Code Set Versioning project, this option is no longer in use.
6.  Plan to start small. Initially, bring up one small clinic using one of the HP single-sided scanners, and then add clinics as you become comfortable with the operation. During testing we found that implementing the single-sided HP scanners was simpler than the double-sided Bell and Howell scanners; however, the double-sided scanners are significantly faster.
7.  Install the server software. This is a kids (Kernel Installation and Distribution System) build and installs in less than 30 minutes.
8.  Install the client software on each workstation. Verify that the connect to the server is working by logging in. Follow the steps for calibrating the scanner. The directions for calibration can be found in the online help, and in the Installation Guide and Release Notes. Most users will need some IRM assistance to calibrate the scanner.

There are four short demonstrations/tutorials available through the help menu that can be used for user training.

<span id="Routines" class="anchor"></span>Routines

<span id="Map" class="anchor"></span>Routines to Map

IBDF1\* IBDF5A

IBDF2\* IBDF9A1

IBDFU\* IBDFQSC1

<span id="Obsolete" class="anchor"></span>Obsolete Routines

IBX\*

<span id="Callable" class="anchor"></span>Callable Routines

The following routines are called by supported RPCs.

CLNLSTI^IBDFRPC(RESULT,CLINIC)

FRMLSTI^IBDFRPC(RESULT,FRM,FTYP,KILL,ALLOBJ)

OBJLST^IBDFRPC1(RESULT,IBDF)

IDPAT^IBDFRPC3(RESULT,FORMID)

SEND^IBDFRPC4(RESULT,IBDF)

Other callable routines:

SEND(FORMID,PROVIDER,PROVTYPE,BUBBLES,HANDPRNT,

> CHECKOUT,PXCA,DYNAMIC)^IBDF18E ---

> (similar to SEND^IBDFRPC4)

FSCND(ID,STAT,ERR)^IBDF18C

FID(DFN,APPT,SOURCE,FORMTYPE,CLIN)^IBDF18C

FORMTYPE(SOURCE)^IBDF18D

GETPRO(CLINIC,ARY)^IBDF18B

GETLST(CLINIC,INTRFACE,ARY,FILTER,COUNT)^IBDF18A ---

(replaced by OBJLST^IBDFRPC1)

EN1(PXCA,IBDF)^IBDFDEA

<span id="List" class="anchor"></span>  
Routine List

To obtain a list of AICS routines go to:

1\. Programmer Options Menu

2\. Routine Tools Menu

3\. First Line Routine Print Option

4\. Routine Selector: IBD\*

<span id="Files" class="anchor"></span>Files

<span id="Globals" class="anchor"></span>Globals to Journal

The IBD and IBE globals must be journalled.

<span id="Filelist" class="anchor"></span>File List

<u>File \# File Name Global</u>

357 ENCOUNTER FORM ^IBE(357

<span id="ICDp11" class="anchor"></span>357.03 CODING SYSTEM UPDATES ^IBD(357.03

357.08 AICS PURGE LOG ^1BD(357.08

357.09 ENCOUNTER FORM PARAMETERS ^IBD(357.09

357.1 ENCOUNTER FORM BLOCK ^IBE(357.1

357.2 SELECTION LIST ^IBE(357.2

357.3 SELECTION ^IBE(357.3

357.4 SELECTION GROUP ^IBE(357.4

357.5 DATA FIELD ^IBE(357.5,

357.6\*\* PACKAGE INTERFACE ^IBE(357.6

357.69\*\* TYPE OF VISIT ^IBE(357.69

357.7 FORM LINE ^IBE(357.7

357.8 TEXT AREA ^IBE(357.8

357.91\* MARKING AREA TYPE ^IBE(357.91

357.92\* PRINT CONDITIONS ^IBE(357.92

This file must not be edited!

357.93 MULTIPLE CHOICE FIELD ^IBE(357.93

357.94 ENCOUNTER FORM PRINTERS ^IBE(357.94

  
File List, cont.

<u>File \# File Name Global</u>

357.95 FORM DEFINITION ^IBD(357.95

357.96 ENCOUNTER FORM TRACKING ^IBD(357.96

357.97 ENCOUNTER FORM COUNTERS ^IBD(357.97

357.98\*\* AICS DATA QUALIFIERS ^ IBD(357.98

357.99 PRINT MANAGER CLINIC GROUPS ^IBD(357.99

358 IMP/EXP ENCOUNTER FORM ^IBE(358

358.1 IMP/EXP ENCOUNTER FORM BLOCK ^IBE(358.1

358.2 IMP/EXP SELECTION LIST ^IBE(358.2

358.3 IMP/EXP SELECTION ^IBE(358.3

358.4 IMP/EXP SELECTION GROUP ^IBE(358.4

358.5 IMP/EXP DATA FIELD ^IBE(358.5

358.6 IMP/EXP PACKAGE INTERFACE ^IBE(358.6

358.7 IMP/EXP FORM LINE ^IBE(358.7

358.8 IMP/EXP TEXT AREA ^IBE(358.8

358.91 IMP/EXP MARKING AREA ^IBE(358.91

358.93 IMP/EXP MULTIPLE CHOICE FIELD ^IBE(358.93

358.94 IMP/EXP HAND PRINT FIELD ^IBE(358.94

358.98 IMP/EXP AICS DATA QUALIFIERS ^IBD(358.98

358.99 IMP/EXP AICS DATA ELEMENTS ^IBE(358.99

359 CONVERTED FORMS ^IBD(359

359.1\* AICS DATA ELEMENTS ^IBE(359.1

359.2 FORM SPECS ^IBD(359.2

359.3 AICS ERROR AND WARNING LOG ^IBD(359.3

359.94 HAND PRINT FIELD ^IBE(359.94

  
File List, cont.

The following Scheduling files are exported with, and heavily used by, AICS V. 3.0.

<u>File \# File Name Global</u>

409.95 PRINT MANAGER CLINIC SETUP ^SD(409.95

409.96 PRINT MANAGER DIVISION SETUP ^SD(409.96

\*File contains data which will overwrite existing data.

\*\*File contains data which will merge with existing data.

Following are the steps used to obtain information on AICS file relationships and templates.

<span id="Fileflow" class="anchor"></span>File Flow (Relationships between files)

1\. VA FileMan Menu

2\. Data Dictionary Utilities Menu

3\. List File Attributes Option

4\. Enter File \# or range of File \#s

5\. Select Listing Format: Standard

6\. You will see what files point to the selected file. To see what files the selected file points to, look for fields that say “Pointer to”.

<span id="Templates" class="anchor"></span>Templates

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: Print Template

Sort Template

Input Template

List template

4\. Sort by: Name

5\. Start with name: IBD to IBDZ

6\. Within name, sort by: \<RET\>

7\. First print field: Name

<span id="Exportedoptions" class="anchor"></span>Exported Options

Following are the steps needed to obtain information about AICS menus, exported protocols, exported options, and exported remote procedures.

<span id="Menu" class="anchor"></span>Menu Diagram

1\. Menu Management Menu

2\. Display Menus and Options Menu

3\. Diagram Menus

4\. Select User or Option Name: IBD

<span id="Exportedprotocols" class="anchor"></span>Exported Protocols

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: PROTOCOL

4\. Sort by: Name

5\. Start with name: IBD - IBDZ

6\. Within name, sort by: \<RET\>

7\. First print field: Name

<span id="Exportedoptions2" class="anchor"></span>Exported Options

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: OPTION

4\. Sort by: Name

5\. Start with name: IBD - IBDZ

6\. Within name, sort by: \<RET\>

7\. First print field: Name

<span id="Remote" class="anchor"></span>  
Exported Remote Procedures

1\. VA FileMan Menu

2\. Print File Entries Option

3\. Output from what File: REMOTE PROCEDURE

4\. Sort by: Name

5\. Start with name: IBD - IBDZ

6\. Within name, sort by: \<RET\>

7\. First print field: Name

<span id="Withoutparents" class="anchor"></span>Options without Parents

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Tasked purge of Form Tracking files</p>
<p>[IBDF AUTO PURGE FORM TRACKING]</p></td>
<td><p>This option should be queued to run at the sites’ convenience. It will purge old data from the ENCOUNTER FORM TRACKING file (357.96), the ENCOUNTER FORM DEFINITION file (357.95) and the FORM SPECIFICATION file (359.2). Two parameters in the ENCOUNTER FORM PARAMETERS file (357.09) control how this option works.</p>
<p>The option needs no device and has no output. It is recommended that this be tasked to run at least once weekly during a weekend or other slow time.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Background EF Print</p>
<p>[IBDF BACKGRD EF PRINT QUEUE]</p></td>
<td>This option prints Encounter Forms in the background. Jobs are run based on the queuing parameters set up using the Setup Automatic Print Queues option [IBDF SETUP AUTO CLINIC PRINT].</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="Archiving" class="anchor"></span>Archiving and Purging

<span id="Archiving2" class="anchor"></span>Archiving

There are no archiving capabilities with the AICS package.

<span id="Purging" class="anchor"></span>Purging

|                          |                                 |                            |
|--------------------------|---------------------------------|----------------------------|
| File Purged          | Option Name                 | Menu                   |
|                          |                                 |                            |
| ENCOUNTER FORM           | Purge Form Tracking files       | Encounter Form IRM Options |
| TRACKING file (357.96)   |                                 |                            |
|                          |                                 |                            |
| ENCOUNTER FORM           | Purge Form Tracking files       | Encounter Form IRM Options |
| DEFINITION file (357.95) |                                 |                            |
|                          |                                 |                            |
| FORM SPECIFICATION       | Purge Form Tracking files       | Encounter Form IRM Options |
| file (359.2)             |                                 |                            |
|                          |                                 |                            |
|                          | Conversion Utility For Scanning | Edit Encounter Forms       |
|                          | (Purge Conversion Log action)   |                            |
|                          |                                 |                            |
| AICS ERROR AND           | Purge Form Tracking files       | Encounter Form IRM Options |
| WARNING LOG file (359.3) |                                 |                            |
|                          |                                 |                            |
|                          | Conversion Utility For Scanning | Edit Encounter Forms       |
|                          | (Purge Conversion Log action)   |                            |

<span id="External" class="anchor"></span>External Relations

Your site must have the following package versions installed prior to installing AICS V. 3.0.

> Kernel V. 8.0

> PCE V. 1.0

> PIMS V. 5.3

> Problem List V. 2.0 (including patch GMP\*2\*3)

> RPC Broker V. 1.0

> VA FileMan V. 21.0

> Visit Tracking V. 2.0

> Kernel Toolkit V. 7.3

> Clinical Lexicon Utility V. 1.0 or Lexicon Utility V. 2.0

<span id="DBIA" class="anchor"></span>Database Integration Agreements (DBIAs)

Following are the steps taken to obtain the DBIA agreements for the AICS package.

<span id="Custodial" class="anchor"></span>*Custodial Agreements*

1\. FORUM

2\. DBA Menu

3\. Integration Agreements Menu

4\. Custodial Package Menu

5.  Active by Custodial Package Option
6.  Select Package Name: Automated Info Collection Sys

<span id="Subscriber" class="anchor"></span>*Subscriber Agreements*

1\. FORUM

2\. DBA Menu

3\. Integration Agreements Menu

4\. Subscriber Package Menu

5\. Print Active by Subscriber Package Option

6.  Start with subscriber package: Automated Info - Automated Infoz

<span id="Internal" class="anchor"></span>Internal Relations

All of the AICS V. 3.0 options have been designed to stand alone.

<span id="Packagewide" class="anchor"></span>Package-wide Variables

There are no package-wide variables.

How to Generate On-Line Documentation

This section describes some of the various methods by which users may secure AICS technical documentation. On-line technical documentation pertaining to the AICS software, in addition to that which is located in the help prompts and on the help screens which are found throughout the AICS package, may be generated through utilization of several Kernel options. These include but are not limited to XINDEX; Menu Management, Inquire to Option File and Print Option File; VA FileMan Data Dictionary Utilities, List File Attributes.

Entering question marks at the "Select ... Option:" prompt may also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the V*IST*A Kernel Reference Manual.

XINDEX

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adhere(s) to V*IST*A Programming Standards. The XINDEX output may include the following components: compiled list of Errors and Warnings, Routine Listing, Local Variables, Global Variables, Naked Globals, Label References, and External References. By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from V*IST*A Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the AICS package, specify the following namespace(s) at the "routine(s) ?\>" prompt: IBD.

AICS initialization routines which reside in the UCI in which XINDEX is being run, as well as local routines found within the AICS namespace, should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).  
Inquire to Option File

This Menu Management option provides the following information about a specified option(s): option name, menu text, option description, type of option and lock, if any. In addition, all items on the menu are listed for each menu option.

To secure information about AICS options, the user must specify the name or namespace of the option(s) desired. The namespace associated with the AICS package is IBD.

Print Option File

This utility generates a listing of options from the OPTION file. The user may choose to print all of the entries in this file or may elect to specify a single option or range of options. To obtain a list of AICS options, the following option namespace should be specified: IBD.

List File Attributes

This VA FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s).

File name and description

Identifiers

Cross-references

Files pointed to by the file specified

Files which point to the file specified

Input, print, and sort templates

In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates. For a comprehensive listing of AICS files, please refer to the Files Section of this manual.

<span id="Packagesecurity" class="anchor"></span>Package Security

<span id="Generalsecurity" class="anchor"></span>General Security

AICS V. 3.0 files should only be updated through distributed options.

<span id="Securitykeys" class="anchor"></span>Security Keys

IBDF IRM This key is used to prevent access to Encounter Form Utility options that are for IRM staff only.

IBD SCAN MANAGER This key is needed to use the AICS work station and to scan Encounter Form data to V*IST*A.

IBD MANAGER This key is needed to perform functions in AICS that not all users are allowed access to, such as deleting Form Tracking entries.

<span id="Filemanaccess" class="anchor"></span>VA FileMan Access Codes

Following is a list of recommended VA FileMan access codes associated with each file contained in the AICS package.

|                                                |                       |               |               |               |               |               |
|------------------------------------------------|-----------------------|---------------|---------------|---------------|---------------|---------------|
| File                                           | File                  | DD            | RD            | WR            | DEL           | LAYGO         |
| <u>Number</u>                                  | <u>Name</u>           | <u>Access</u> | <u>Access</u> | <u>Access</u> | <u>Access</u> | <u>Access</u> |
|                                                |                       |               |               |               |               |               |
| 357                                            | ENCOUNTER FORM        | @             | @             | @             | @             | @             |
| <span id="ICDp25" class="anchor"></span>357.03 | CODING SYSTEM UPDATES | @             | @             | @             | @             | @             |
| 357.08                                         | AICS PURGE LOG        | @             |               | @             | @             | @             |
| 357.09                                         | ENCOUNTER FORM PARAM  | @             |               |               | @             | @             |
| 357.1                                          | ENCOUNTER FORM BLOCK  | @             | @             | @             | @             | @             |
| 357.2                                          | SELECTION LIST        | @             | @             | @             | @             | @             |
| 357.3                                          | SELECTION             | @             | @             | @             | @             | @             |
| 357.4                                          | SELECTION GROUP       | @             | @             | @             | @             | @             |
| 357.5                                          | DATA FIELD            | @             | @             | @             | @             | @             |
| 357.6                                          | PACKAGE INTERFACE     | @             | @             | @             | @             | @             |
| 357.69                                         | TYPE OF VISIT         | @             | @             | @             | @             | @             |
| 357.7                                          | FORM LINE             | @             | @             | @             | @             | @             |
| 357.8                                          | TEXT AREA             | @             | @             | @             | @             | @             |
| 357.91                                         | MARKING AREA TYPE     | @             | @             | @             | @             | @             |
| 357.92                                         | PRINT CONDITIONS      | @             | @             | @             | @             | @             |

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 39%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr class="odd">
<td>File</td>
<td>File</td>
<td>DD</td>
<td>RD</td>
<td>WR</td>
<td>DEL</td>
<td>LAYGO</td>
</tr>
<tr class="even">
<td><u>Number</u></td>
<td><u>Name</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
<td><u>Access</u></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>357.93</td>
<td>MULTIPLE CHOICE FIELD</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>357.94</td>
<td>ENCOUNTER FORM PRINTERS</td>
<td>@</td>
<td></td>
<td>#</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>357.95</td>
<td>FORM DEFINITION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>357.96</td>
<td>ENCOUNTER FORM TRACKING</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>357.97</td>
<td>ENCOUNTER FORM COUNTERS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>357.98</td>
<td>AICS DATA QUALIFIERS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>357.99</td>
<td>PRINT MANAGER CLINIC GROUPS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>358</td>
<td>IMP/EXP ENCOUNTER FORM</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>358.1</td>
<td>IMP/EXP ENCOUNTER FORM BLOCK</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>358.2</td>
<td>IMP/EXP SELECTION LIST</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>358.3</td>
<td>IMP/EXP SELECTION</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>358.4</td>
<td>IMP/EXP SELECTION GROUP</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>358.5</td>
<td>IMP/EXP DATA FIELD</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>358.6</td>
<td>IMP/EXP PACKAGE INTERFACE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>358.7</td>
<td>IMP/EXP FORM LINE</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>358.8</td>
<td>IMP/EXP TEXT AREA</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>358.91</td>
<td>IMP/EXP MARKING AREA</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>358.93</td>
<td>IMP/EXP MULTIPLE CHOICE FIELD</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>358.94</td>
<td>IMP/EXP HAND PRINT FIELD</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>358.98</td>
<td>IMP/EXP AICS DATA QUALIFIERS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>358.99</td>
<td><p>IMP/EXP AICS</p>
<p>DATA EL</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>359</td>
<td>CONVERTED FORMS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>359.1</td>
<td>AICS DATA ELEMENTS</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

The following Scheduling files are exported with, and heavily used by, AICS V. 3.0.

|               |                              |               |               |               |               |               |
|---------------|------------------------------|---------------|---------------|---------------|---------------|---------------|
| File          | File                         | DD            | RD            | WR            | DEL           | LAYGO         |
| <u>Number</u> | <u>Name</u>                  | <u>Access</u> | <u>Access</u> | <u>Access</u> | <u>Access</u> | <u>Access</u> |
|               |                              |               |               |               |               |               |
| 359.2         | FORM SPECS                   | @             | @             | @             | @             | @             |
| 359.3         | AICS ERROR AND WARNING LOG   | @             |               |               |               | @             |
| 359.94        | HAND PRINT FIELD             | @             | @             | @             | @             | @             |
| 409.95        | PRINT MANAGER CLINIC SETUP   | @             | @             | @             | @             | @             |
| 409.96        | PRINT MANAGER DIVISION SETUP | @             | @             | @             | @             | @             |

<span id="Glossary" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<tbody>
<tr class="odd">
<td>anchor marks</td>
<td>Cross-hair or angle marks appearing on a scannable form. They are used by the commercial scanning engine to align the form.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>block</td>
<td>A form is composed of blocks. Blocks are a rectangular region on the form. Attributes include position, size, outline type, and header. All other form components are contained within a particular block, and their position is relative to the block's position.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>bubbles</td>
<td>Marking areas on a form. They are filled in to indicate a selection, and will be read by the scanner.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>column</td>
<td>A selection list contains one or more columns, a column being a rectangular area that contains a portion of the entries on a selection list. Attributes include position and height.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>comb</td>
<td>Marking areas on a form to guide a user into entering one character per box.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>conversion</td>
<td><p>Refers to the conversion of forms designed using IB</p>
<p>V. 2.0 to forms that can be scanned.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><span id="ICDp27" class="anchor"></span>CSV</td>
<td>Code Set Versioning. This package is mandated under the Health Information Portability and Accountability Act (HIPAA). It contains routines, globals and data dictionary changes to recognize code sets for the International Classification of Diseases, Clinical Modification (ICD‑9‑CM and ICD-10-CM), Current Procedural Terminology (CPT) and Health Care Financing Administration (HCFA) Common Procedure Coding System (HCPCS). When implemented, certain applications will allow users of these three code systems to select codes based upon a date that an event occurred with the Standards Development Organization (SDO)-established specific code that existed on that event date.</td>
</tr>
</tbody>
</table>

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data field              | A block component that is the means by which data from V*IST*A is printed to the form, such as the patient's name. The data is obtained at the time the form is printed (i.e., it is not stored with the form) and can be particular to the patient. A data field can have subfields, which are conceptually a collection of related data fields. Attributes include label, label type (underline, bold, invisible), position, data area, data length and position (area on the form allocated to the data), item number, and package interface (the routine used to get the data). |
|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| data qualifiers         | A selection list component. Example: with data qualifiers, a diagnosis can be designated as either primary or secondary.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| dynamic selection lists | Lists used to print the patient's active problems, insurance policies, providers assigned to the clinic, etc. Dynamic lists provide the capability of scanning data such as patient's active problems. They also provide an easier method of printing lists of data such as SC disabilities, as compared to using data fields.                                                                                                                                                                                                                                                      |
|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| encounter form          | A paper form used to display data pertaining to an outpatient visit and to collect additional data pertaining to that visit.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| entry action            | An attribute of a package interface. It is MUMPS code that is executed before the interface's entry point is executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| exit action             | An attribute of a package interface. It is MUMPS code that is executed after the interface's entry point is executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| form line               | A block component. A straight line that will be printed to the form. Attributes include orientation (horizontal, vertical), position, and length.                                                                                                                                                                                                                                                                                                                                                                                                                                   |

|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| form tracking                     | Tracks the processing status of forms. Each printed form will be assigned an ID, allowing it to be tracked while it's being processed. The lists of forms printed, their status, and statistics can be obtained from the Form Tracking option.                                                                                                                                                                                              |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| hand print field                  | Allow input of hand printing.                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| intelligent character recognition | (ICR) The ability to read hand written characters (usually printed) in combs or boxes.                                                                                                                                                                                                                                                                                                                                                      |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| item number                       | An attribute that must be specified when defining a data field if the data field's package interface returns a list. The item number is used to specify which item on the list should be printed to the data field. For example, there is a package interface for returning service connected conditions. The first data field created for a form for displaying a service connected condition would specify item number one.               |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| operator fill field               | A field that is completed by an operator once it’s scanned.                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| optical character recognition     | (OCR) The ability for scanning software to read characters printed by a printer on a form.                                                                                                                                                                                                                                                                                                                                                  |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| package interface                 | A table that is the method by which the encounter form utilities interface with other packages. Presently there are three types of package interfaces: for printing reports via the print manager, printing data to data fields, and for entering data to selection lists. Attributes include entry point, routine, entry action, exit action, protected variables, required variables, data type, data description, and custodial package. |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| place holders                     | A component of a selection list. They can contain text and serve as subheaders for the selections that follow within a group.                                                                                                                                                                                                                                                                                                               |

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| print manager   | The print manager is a utility used to define the reports and encounter forms that should be printed for clinics. It will then print the reports and forms in packets for each appointment specified.                                                                                                                                                                                                           |
|                 |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| scannable       | A form or marking area that is designed to be scanned and formatted; and defined to the scanning software.                                                                                                                                                                                                                                                                                                      |
|                 |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| selection       | A component of a selection list. It is a single entry on the list. It is stored with the form and usually consists of data taken from a file in V*IST*A such as a CPT code with its description.                                                                                                                                                                                                                |
|                 |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| selection group | A component of a selection list. It is a named group of selections on the list. Attributes include a header and the print order.                                                                                                                                                                                                                                                                                |
|                 |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| selection list  | A block component whose purpose is to contain a list; for example, a list of CPT codes. The list contains subcolumns for marking areas, which are areas meant to be marked to indicate selections being made from the list. Attributes include headers, subcolumns, subcolumn width, subcolumn type, package interface (the routine used to fill the list), and many attributes for the appearance of the list. |
|                 |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| selection rule  | There are a set of rules on the number of items that can be accepted for each list. For example, exactly one primary diagnosis and any number of secondary diagnoses can be specified.                                                                                                                                                                                                                          |
|                 |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| subcolumn       | A component of a selection list. It can contain either text, such as a CPT code, or a marking area.                                                                                                                                                                                                                                                                                                             |

|           |                                                                                                                                                                                                                                                                                                                                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| subfield  | A component of a data field. It can display a single value, whereas a data field can be used to display a collection of related values. Attributes include those for the label and the area on the form to print the data. Also, for package interfaces that return records that have multiple values, the particular data must be specified. |
|           |                                                                                                                                                                                                                                                                                                                                               |
| text area | A rectangular area in a block that is used to display a word-processing field. The text is automatically formatted to fit within the block. Attributes include the word-processing field, the position and size of the text area. The text is stored with the form.                                                                           |

<span id="Index" class="anchor"></span>Index

Archiving 17

Callable Routines 9

Custodial Agreements 19

Database Integration Agreements (DBIAs) 19

Exported Options 15

Exported Protocols 15

External Relations 19

Exported Remote Procedures 16

File Flow (Relationships between files) 13

File List 11

Files 11

General Information 5

General Security 25

Globals to Journal 11

Glossary 27

How to Generate On-Line Documentation 23

Implementation and Maintenance 7

Integrity Checker 5

Internal Relations 21

Introduction 1

Menu Diagram 15

Namespace Conventions 5

Obsolete Routines 9

Options without Parents 16

Orientation 3

Package Security 25

Package-wide Variables 21

Purging 17

Resource Requirements 5

Routine List 10

Routines 9

Routines to Map 9

Security Keys 25

Setting Up Workstations 8

Subscriber Agreements 19

Templates 13

VA FileMan Access Codes 25