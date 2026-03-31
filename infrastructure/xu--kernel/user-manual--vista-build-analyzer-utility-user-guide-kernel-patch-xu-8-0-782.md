---
title: VistA Build Analyzer Utility User Guide (Kernel Patch XU*8.0*782)
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: 
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
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - build
  - included
  - description
  - class
  - number
  - analyzer
  - routine
  - mark
  - help
page_count: 0
word_count: 26425
section_count: 15
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2023
revision_count: 1
revision_newest: 05/31/2023
revision_oldest: 05/31/2023
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/vista_build_analyzer_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/vista_build_analyzer_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  VistA Build Analyzer Utility

  Kernel Patch XU\*8.0\*782

  User Guide
---

![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/001.png)

May 2023

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Software Product Management (SPM)

<span id="_Toc123371025" class="anchor"></span>Revision History

| Date       | Revision | Description                                         | Author                                                       |
|------------|----------|-----------------------------------------------------|--------------------------------------------------------------|
| 05/31/2023 | 1.0      | Initial release of VistA Build Analyzer User Guide. | VistA Infrastructure Shared Services (VISS) Development Team |

Table details the revision history including the date, revision number, description of changes, and the author.

Table of Contents

<span id="_Toc136406908" class="anchor"></span>Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Using the VistA Build Analyzer](#using-the-vista-build-analyzer)
  - [Build Analyzer Main Menu](#build-analyzer-main-menu)
  - [KIDS Build Analyzer Option](#kids-build-analyzer-option)
    - [Analysis Results Display Choices](#analysis-results-display-choices)
    - [Incorrect or Missing Build](#incorrect-or-missing-build)
    - [Print the Report Action](#print-the-report-action)
    - [Create the Report in .TXT Files Action](#create-the-report-in-txt-files-action)
    - [Send the Report in MailMan Messages Action](#send-the-report-in-mailman-messages-action)
  - [Delete Build Analyzer Text Files Option](#delete-build-analyzer-text-files-option)
  - [KIDS Build Analyzer - Full SQA Search Option](#kids-build-analyzer-full-sqa-search-option)
- [Build Analysis](#build-analysis)
  - [Build Overview](#build-overview)
  - [General Build Checks](#general-build-checks)
  - [Build Component Analysis](#build-component-analysis)
  - [Description of Build](#description-of-build)
  - [Individual Components](#individual-components)
    - [Files](#files)
    - [Routines](#routines)
    - [Examples](#examples)
  - [All Components](#all-components)
  - [Specific Components](#specific-components)
    - [Options](#options)
    - [Remote Procedures](#remote-procedures)
    - [Bulletin](#bulletin)
    - [Dialog](#dialog)
  - [Issues](#issues)
  - [SQA Check—Full Lines](#sqa-checkfull-lines)
    - [^TMP](#tmp)
    - [^XTMP](#xtmp)
    - [U=](#u)
    - [\$I](#i)
    - [IO](#io)
    - [DIC(0)](#dic0)
  - [Text Check](#text-check)
    - [Component Descriptions/Text](#component-descriptionstext)
    - [M Routines](#m-routines)
The VistA Build Analyzer utility (aka Build Analyzer) assists developers and software quality assurance (SQA) in preparing and reviewing a new Veterans Health Information Systems and Technology Architecture (VistA) patch.
This utility analyzes all of the components included in a Kernel Installation and Distribution System (KIDS) build. It provides an assessment based on standards and best practices.
The Build Analyzer is primarily run in a Development or SQA Test accounts to verify a build meets standards prior to release into a Production account. However, it can also be run in a Production account to review an already released build to verify if any issues arise after release to confirm any build discrepancies.
The VistA Build Analyzer utility includes the Build Analyzer Main Menu \[XPDANLYZ MAIN MENU\] with the following options and actions:”
- KIDS Build Analyzer \[XPDANLYZ\] and the following actions:
  - Print the Report
  - Create the Report in .TXT Files
  - Send the Report in MailMan Messages
- Delete Build Analyzer Text Files \[XPDANLYZ_DEL\].
- KIDS Build Analyzer - Full SQA Search \[XPDANLYZ_SQA\] and the following actions:
  - Print the Report
  - Create the Report in .TXT Files
  - Send the Report in MailMan Messages
![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/002.png) REF: These options and actions are described in Section <u>2</u>, “<u>Using the VistA Build Analyzer</u>.
This tool was created to help maintain constancy between developers and catch simple errors prior to submitting a patch for further reviews. The VistA Build Analyzer utility will be continuously improved to maintain conventions and speed reviews of new VistA patches.

# Using the VistA Build Analyzer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Build Analyzer Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the VistA Build Analyzer utility, do the following (<u>Figure 1</u>):

1.  Select the Programmer Options \[XUPROG\] menu.
2.  Select the Kernel Installation & Distribution System \[XPD MAIN\] menu.
3.  Select the Utilities \[XPD UTILITY\] menu.
4.  Select the Build Analyzer Main Menu \[XPDANLYZ MAIN MENU\].

<span id="_Ref135740008" class="anchor"></span>Figure 1: Accessing the Build Analyzer Main Menu \[XPDANLYZ MAIN MENU\]—System Prompts and User Entries

Core Applications ...

Device Management ...

FM VA FileMan ...

Menu Management ...

<span class="mark">Programmer Options ...</span>

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">PROG \<Enter\></span> rammer Options

<span class="mark">KIDS Kernel Installation & Distribution System ...</span>

NTEG Build an 'NTEG' routine for a package

PG Programmer mode

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

Map Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

Select Programmer Options \<TEST ACCOUNT\> Option: <span class="mark">KIDS \<Enter\></span> Kernel Installation & Distribution System

Edits and Distribution ...

<span class="mark">Utilities ...</span>

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: <span class="mark">UTIL \<Enter\></span> ities

<span class="mark">Build Analyzer Main Menu ...</span>

Build File Print

Convert Loaded Package for Redistribution

Display Patches for a Package

Edit Install Status

Install File Print

Purge Build or Install Files

Rollup Patches into a Build

Update Routine File

Verify a Build

Verify Package Integrity

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">BUILD AN \<Enter\></span> alyzer Main Menu

1 KIDS Build Analyzer

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option:

## KIDS Build Analyzer Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the KIDS Build Analyzer \[XPDANLYZ\] option (<u>Figure 2</u>) to analyze the build components to identify adherence to standards and best practices.

<span id="_Ref127180257" class="anchor"></span>Figure 2: Running the KIDS Build Analyzer \[XPDANLYZ\] Option—System Prompts and User Entries

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">KIDS</span>

<span class="mark">1 KIDS Build Analyzer</span>

2 KIDS Build Analyzer - Full SQA Search

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze the components of a build to identify adherence to

standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688</span>

<span class="mark">1 XU\*8\*688 KERNEL</span>

2 XU\*8\*688b KERNEL

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> XU\*8.0\*688 KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing

specific code references reviewed on the SQA checklist? NO// <span class="mark">\<Enter\></span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">\<Enter\></span>

Analysis Results Display Choices:

<span class="mark">1. Print the Report</span>

<span class="mark">2. Create the Report in .TXT Files</span>

<span class="mark">3. Send the Report in MailMan Messages</span>

Select number: (1-3):

### Analysis Results Display Choices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KIDS Build Analyzer \[XPDANLYZ\] option provides the following actions to view or save the report output (<u>Figure 2</u>):

1.  [Print the Report](#print-the-report-action)—Output displayed to the screen (Default: HOME) or other specified device.
5.  [Create the Report in .TXT Files](#create-the-report-in-.txt-files-action)—Output sent to separate text files.
6.  [Send the Report in MailMan Messages](#_Toc128552312)—Output sent to email messages.

If the user chooses to see the lines with Software Quality Assurance (SQA) references or review component descriptions and text found in routines, they will be packaged in the same format as chosen with these actions.

### Incorrect or Missing Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the PACKAGE NAMESPACE OR PREFIX (#23) Multiple field of the BUILD (#9.6) file is *not*NULL and if the build does *not* include the namespace obtained from the first part of the build name; you will see the warning shown in <u>Figure 3</u>:

<span id="_Ref127183573" class="anchor"></span>Figure 3: Sample Warning Message—Build Namespace Missing or Inconsistent

Select Build Name: <span class="mark">ZZ\*1.0\*1</span>

\*\*\* Warning: BUILD namespace not consistent with PACKAGE NAMESPACE OR

PREFIX (#23) field of BUILD file.

### Print the Report Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the “Print the Report” action is selected in <u>Figure 2</u>, the user is prompted for a “Device”, as shown in  
<u>Figure 4</u>:

<span id="_Ref127179892" class="anchor"></span>Figure 4: Print Analysis Report—Sample Dialog to Choose a Device

Print Analysis to which Device: HOME//

If you choose to display the whole report without breaks (e.g., “HOME// ;;9999999”), then you will get all data scrolling on the screen. If it is a large build, this could be a lot of data and the pause above at the “Print” prompt should be used to set up to log the display into a text file. If you just accept the “HOME//” default, it will display one screen at a time for your review.

#### No SQA Checklist Items, Component Descriptions, or Routine Text

<u>Figure 5</u> shows the results when answering NO to the following prompts in the KIDS Build Analyzer \[XPDANLYZ\] option and then using the Print the Report action to see the report:

- “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” <span class="mark">NO</span>
- “Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">NO</span>

<span id="_Ref127883267" class="anchor"></span>Figure 5: Running the “KIDS Build Analyzer” Option: “Print the Report” Action: No SQA Checklist Items, Component Descriptions, or Routine Text—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

<span class="mark">1 KIDS Build Analyzer</span>

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO// <span class="mark">NO</span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">NO</span>

Analysis Results Display Choices:

<span class="mark">1. Print the Report</span>

2\. Create the Report in .TXT Files

3\. Send the Report in MailMan Messages

Select number: (1-3): <span class="mark">1 \<Enter\></span> . . .

Print Analysis to which Device: HOME// <span class="mark">;;9999999</span> TELNET PORT Right Margin:

80// <span class="mark">\<Enter\></span>

<u>Figure 6</u> shows the results from the Print the Report action from the KIDS Build Analyzer option *without* including SQA checklist items, component descriptions, and routine text:

<span id="_Ref127883282" class="anchor"></span>Figure 6: Reviewing the “Print the Report” Action Results—Output *without* SQA Checklist Items, Component Descriptions, and Routine Text

XU\*8.0\*688 BUILD OVERVIEW Jan 25, 2023@07:14:24

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date of Last ^XINDEX: JAN 24, 2023

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

Press \<Enter\> or '^' to exit:

#### Including SQA Checklist Items, Component Descriptions, and Routine Text

<u>Figure 7</u> shows the results when answering YES to the following prompts in the KIDS Build Analyzer \[XPDANLYZ\] option and then using the Print the Report action to see the report:

- “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” <span class="mark">YES</span>
- “Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">YES</span>

<span id="_Ref127883394" class="anchor"></span>Figure 7: Running the “KIDS Build Analyzer” Option: “Print the Report” Action: Including SQA Checklist Items, Component Descriptions, and Routine Text—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

<span class="mark">1 KIDS Build Analyzer</span>

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO// <span class="mark">YES</span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">YES</span>

Analysis Results Display Choices:

<span class="mark">1. Print the Report</span>

2\. Create the Report in .TXT Files

3\. Send the Report in MailMan Messages

Select number: (1-3): <span class="mark">1 \<Enter\></span> . . .

Print Analysis to which Device: HOME// <span class="mark">;;9999999</span> TELNET PORT Right Margin:

80// <span class="mark">\<Enter\></span>

<u>Figure 8</u> shows the results from the Print the Report action from the KIDS Build Analyzer option including SQA checklist items, component descriptions, and routine text:

<span id="_Ref127883420" class="anchor"></span>Figure 8: Reviewing the “Print the Report” Action Results—Output *with* SQA Checklist Items, Component Descriptions, and Routine Text

XU\*8.0\*688 BUILD OVERVIEW Jan 25, 2023@07:18:04

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date of Last ^XINDEX: JAN 24, 2023

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

ALL ^XTMP calls have zero nodes defined in this build's routines

XUSER3

^( ...........................................................................

VALN1DEA +8 I \$D(X),'F,\$D(DA(1)),\$D(^VA(200,"PS4",X)),\$O(^(X,0))'=DA(1) D

EN^DDIOL(\$C(7)\_"Provider DEA number is already associated to

another profile. Please check the number entered.") K X

Descriptions and other text associated with this build (for review and

spell check):

BUILD: XU\*8.0\*688

See FORUM Patch description.

FILE: NEW PERSON

SUBFILE 200.5321; FIELD: .01: DEA NUMBER

This field is used to enter the provider's Drug Enforcement Administration

(DEA) number(s). Enter the DEA number as two upper case letters followed

by 7 digits. e.g., AA1234567.

HELP-PROMPT:

Enter DEA number in the format 2 upper case letters followed by 7 numbers.

TECHNICAL DESCRIPTION:

This is the algorithm for the DEA number

FIELD: 53.2: DEA#

This field is used to enter the Drug Enforcement Agency (DEA) number.

Enter the DEA number as two upper case letters followed by 7 digits.

e.g., AA1234567.

HELP-PROMPT:

Enter the DEA number 2 letters 7 numbers.

TECHNICAL DESCRIPTION:

This is the algorithm for the DEA number

HELP-PROMPT: missing.

FILE: DEA BUSINESS ACTIVITY CODES

The DEA BUSINESS ACTIVITY CODES FILE is associated with the DEA numbers

and provider information in the DEA NUMBERS file. This file links a

provider with the type of service provided. It contains BUSINESS

ACTIVITY CODES that are supplied by the DOJ/DEA web service.

Field - BUSINESS ACTIVITY (#.02):

Description:

This field holds the Business Activity value used for DEA numbers. This

value can currently be one of the following:

A,B,C,D,E,F,G,H,J,K,L,M,N,P,R,S,T or U

This value, combined with a numeric business sub-type, categorizes a DEA

number.

Help-Prompt:

Enter the Business Activity value for used for DEA numbers. Answer must

be 1-3 characters in length.

Field - BUSINESS ACTIVITY DESCRIPTION (#1):

Description:

This is the description given for the Business Activity Code and Sub-code.

Help-Prompt:

Enter the Business Activity description given for the Business Activity

code and Business Activity Sub-code. Answer must be 3-60 characters in length.

Field - BUSINESS ACTIVITY SUB-CODE (#.03):

Description:

DEA uses an alpha character business activity code to identify various

categories of registrants. For example business activity code "C"

indicates a "Practitioner". DEA added a business activity sub-code field

to identify new sub-categories of registrants.

For example business activity code "C" in combination with business

activity sub-code "1" indicates a practitioner who has received a Drug

Addiction Treatment Act (DATA) Waiver (DATA Waived or DW) to provide

office based opioid treatment to 30 or 100 or 275 patients (DW/30, DW/100,

DW/275). As new sub-categories of business activities become regulated,

additional sub-code combinations (e.g. C-2, C-3, A-1, etc.) will be

assigned. MLP = Mid-Level Practitioner. NG = National Guard

Help-Prompt:

Enter the business activity sub-code associated with the Business

Activity Code. Answer must be 1-3 characters in length.

Field - FULL BUSINESS ACTIVITY CODE (#.01):

Description:

DEA uses an alpha character business activity code to identify various

categories of registrants. For example business activity code "C"

indicates a "Practitioner". DEA added a business activity sub-code field

to identify new sub-categories of registrants.

For example business activity code "C" in combination with business

activity sub-code "1" indicates a practitioner who has received a Drug

Addiction Treatment Act (DATA) Waiver (DATA Waived or DW) to provide

office based opioid treatment to 30 or 100 or 275 patients (DW/30, DW/100,

DW/275). As new sub-categories of business activities become regulated,

additional sub-code combinations (e.g. C-2, C-3, A-1, etc.) will be

assigned. MLP = Mid-Level Practitioner. NG = National Guard.

Help-Prompt:

Enter the full business activity code. This is composed of the Business

activity code and sub-code used for DEA numbers. Answer must be 2-4 characters in length.

Field - MANUAL ENTRY DATE/TIME (#2):

Description:

This field should only be populated when a new Business Activity Code

(BAC) is entered manually due to the failure of the PSO DOJ/DEA WEB

SERVICE to establish a connection to the DOJ web server.

Help-Prompt:

This is the date/time this Business Activity Code was manually entered.

FILE: DEA NUMBERS

The DEA NUMBERS FILE is designed to contain demographic and permission

information about a provider related to the ability to order controlled

substance prescriptions.

Field - ADDITIONAL COMPANY INFO (#1.2):

Description:

This is the additional company information of the person or institution

associated with this DEA Number.

Help-Prompt:

Enter additional company info for the given person/institution. Answer

must be 1-40 characters in length.

Field - BUSINESS ACTIVITY CODE (#.02):

Description:

This is the business activity code related to this DEA Number.

Help-Prompt:

Enter the Business Activity code given to this DEA Number.

Field - CITY (#1.5):

Description:

This is the city of the permanent address of the person or institution

related to this DEA Number.

Help-Prompt:

Enter the city of the permanent address of the person or institution

associated with this DEA Number. Answer must be 1-33 characters in length.

Field - DEA NUMBER (#.01):

Description:

This field is used to enter the providers' Drug Enforcement Administration

(DEA) number. Enter the DEA number as two upper case letters followed

by 7 digits. e.g., AA1234567.

Help-Prompt:

Enter the DEA number in the format of 2 letters followed by 7 numbers.

Field - DETOX NUMBER (#.03):

Description:

If the DEA provider has detox privileges, this field will be populated

with a 'VX' or 'XA' followed by the numeric portion of the DEA number.

Help-Prompt:

Enter the detox number associated with this DEA Number. Answer must be 9

characters in length.

Field - EXPIRATION DATE (#.04):

Description:

This is the date of expiration for the DEA Number.

Help-Prompt:

Enter the date this DEA Number expires.

Field - LAST DOJ UPDATE DATE/TIME (#10.3):

Description:

This is the date/time the DOJ (Department of Justice) data was used to

update this DEA record.

Help-Prompt:

Enter the date/time this DEA record was last updated by the DOJ source.

Field - LAST UPDATED BY (#10.1):

Description:

This is the person from the NEW PERSON file who last initiated an update

to this DEA record.

Help-Prompt:

Enter the person who last updated this DEA record.

Field - LAST UPDATED DATE/TIME (#10.2):

Description:

This is the date/time of the last update to this DEA record.

Help-Prompt:

Enter the date/time this DEA record was last updated.

Field - NAME (PROVIDER OR INSTITUTION) (#1.1):

Description:

This is the name of the facility or person who is associated with this

DEA Number.

Help-Prompt:

Enter the name associated with this DEA Number. Answer must be 1-40

characters in length.

Field - SCHEDULE II NARCOTIC (#2.1):

Description:

This field is used to determine if the provider has privileges for

Schedule II drugs.

Help-Prompt:

DEA number allows for schedule II drugs?

Field - SCHEDULE II NON-NARCOTIC (#2.2):

Description:

This field is used to determine if the provider has privileges for

Schedule II non-narcotic.

Help-Prompt:

Provider has privileges for schedule II non-narcotic?

Field - SCHEDULE III NARCOTIC (#2.3):

Description:

This field is used to determine if the provider has privileges for

Schedule III narcotic.

Help-Prompt:

Provider has privileges for schedule III narcotic?

Field - SCHEDULE III NON-NARCOTIC (#2.4):

Description:

This field is used to determine if the provider has privileges for

Schedule III non-narcotic.

Help-Prompt:

Provider has privileges for schedule III non-narcotic?

Field - SCHEDULE IV (#2.5):

Description:

This field is used to determine if the provider has privileges for

Schedule IV controlled substances.

Help-Prompt:

Provider has privileges for schedule IV?

Field - SCHEDULE V (#2.6):

Description:

This field is used to determine if the provider has privileges for

Schedule V controlled substances.

Help-Prompt:

Provider has privileges for schedule V?

Field - STATE (#1.6):

Description:

This is the state of the permanent address of the person or institution

associated with this DEA Number.

Help-Prompt:

Enter the state of the permanent address associated with the person or

institution associated with this DEA Number.

Field - STREET ADDRESS 1 (#1.3):

Description:

This is the first line of the street address of the permanent address of

the person or institution associated with this DEA Number.

Help-Prompt:

Enter street address line 1 for the given person/institution. Answer must

be 1-40 characters in length.

Field - STREET ADDRESS 2 (#1.4):

Description:

This is the second line of the street address of the permanent address of

the person or institution associated with this DEA Number.

Help-Prompt:

Enter street address line 2 for the given person/institution. Answer must

be 1-40 characters in length.

Field - TYPE (#.07):

Description:

This identifies whether the DEA number is an individual DEA number or an

Institutional DEA number.

Help-Prompt:

Enter the usage type for the DEA. The DEA usage type may be 'Individual',

or 'Institutional.

Field - USE FOR INPATIENT ORDERS? (#.06):

Description:

This field indicates if this DEA number can be used for inpatient orders.

Help-Prompt:

Can this DEA be used for inpatient orders? Answer 'YES' or 'NO'.

Field - ZIP CODE (#1.7):

Description:

This is the postal ZIP code of the person or institution associated with

this DEA Number.

Help-Prompt:

Enter the ZIP CODE or ZIP+4. Answer must be 5-9 characters in length.

===============================================================================

Text in ROUTINES between quotes and/or after ;;, by line number:

XUSER3

3: Per VA Directive 6402, this routine should not be modified.

10: Exceeds maximum length (9).

11: Less than minimum length (9).

12: Invalid format. Must be 2 upper case letters followed by 7 digits.

14: Provider DEA number is already associated to another profile. Please check

the number entered.

15: DEA number is invalid. Please check the number entered.

16: DEA number doesn't match provider's last name. Please verify the

information.

21: Type \<Enter\> to continue

27: Exceeds maximum length (9).

28: Less than minimum length (9).

29: Invalid format. Must be 2 upper case letters followed by 7 digits.

32: DEA number is invalid. Please check the number entered.

50: That Suffix is in use.

\*\* Analysis Complete \*\*

Press \<Enter\> or '^' to exit:

![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/003.png) REF: For a complete check of all SQA checklist items use the KIDS Build Analyzer - Full SQA Search \[XPDANLYZ_SQA\] option, see Section <u>2.4</u>, “<u>KIDS Build Analyzer - Full SQA Search Option</u>.”

#### Including SQA Checklist Items, but No Component Descriptions and Routine Text

<u>Figure 9</u> shows the results when answering YES and NO to the following prompts in the KIDS Build Analyzer \[XPDANLYZ\] option and then using the Print the Report action to see the report:

- “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” <span class="mark">YES</span>
- “Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">NO</span>

<span id="_Ref133415489" class="anchor"></span>Figure 9: Running the “KIDS Build Analyzer” Option: “Print the Report” Action: Including SQA Checklist Items, but No Component Descriptions and Routine Text—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

<span class="mark">1 KIDS Build Analyzer</span>

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO// <span class="mark">YES</span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">NO</span>

Analysis Results Display Choices:

<span class="mark">1. Print the Report</span>

2\. Create the Report in .TXT Files

3\. Send the Report in MailMan Messages

Select number: (1-3): <span class="mark">1 \<Enter\></span> . . .

Print Analysis to which Device: HOME// <span class="mark">;;9999999</span> TELNET PORT Right Margin:

80// <span class="mark">\<Enter\></span>

<u>Figure 10</u> shows the results from the Print the Report action from the KIDS Build Analyzer option including SQA checklist items, but no component descriptions and routine text:

<span id="_Ref133415488" class="anchor"></span>Figure 10: Reviewing the “Print the Report” Action Results—Output *with* SQA Checklist Items, but *without* Component Descriptions and Routine Text

XU\*8.0\*688 BUILD OVERVIEW Apr 27, 2023@14:24:02

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

ALL ^XTMP calls have zero nodes defined in this build's routines

XUSER3

^( ...........................................................................

VALN1DEA +8 I \$D(X),'F,\$D(DA(1)),\$D(^VA(200,"PS4",X)),\$O(^(X,0))'=DA(1) D

EN^DDIOL(\$C(7)\_"Provider DEA number is already associated to

another profile. Please check the number entered.") K X

\*\* Analysis Complete \*\*

![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/004.png) REF: For a complete check of all SQA checklist items use the KIDS Build Analyzer - Full SQA Search \[XPDANLYZ_SQA\] option, see Section <u>2.4</u>, “<u>KIDS Build Analyzer - Full SQA Search Option</u>.”

#### Including Component Descriptions and Routine Text, but No SQA Checklist Items

<u>Figure 11</u> shows the results when answering NO and YES to the following prompts in the KIDS Build Analyzer \[XPDANLYZ\] option and then using the Print the Report action to see the report:

- “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” <span class="mark">NO</span>
- “Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">YES</span>

<span id="_Ref133409166" class="anchor"></span>Figure 11: Running the “KIDS Build Analyzer” Option: “Print the Report” Action: Including Component Descriptions and Routine Text, but No SQA Checklist Items—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

<span class="mark">1 KIDS Build Analyzer</span>

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO// <span class="mark">NO</span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">YES</span>

Analysis Results Display Choices:

<span class="mark">1. Print the Report</span>

2\. Create the Report in .TXT Files

3\. Send the Report in MailMan Messages

Select number: (1-3): <span class="mark">1 \<Enter\></span> . . .

Print Analysis to which Device: HOME// <span class="mark">;;9999999</span> TELNET PORT Right Margin:

80// <span class="mark">\<Enter\></span>

<u>Figure 12</u> shows the results from the Print the Report action from the KIDS Build Analyzer option including component descriptions and routine text, but no SQA checklist items:

<span id="_Ref133409167" class="anchor"></span>Figure 12: Reviewing the “Print the Report” Action Results—Output *with* Component Descriptions and Routine Text, but *without* SQA Checklist Items

XU\*8.0\*688 BUILD OVERVIEW Apr 27, 2023@14:46:44

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

Descriptions and other text associated with this build (for review and

spell check):

BUILD: XU\*8.0\*688

See FORUM Patch description.

FILE: NEW PERSON

SUBFILE 200.5321; FIELD: .01: DEA NUMBER

This field is used to enter the provider's Drug Enforcement Administration

(DEA) number(s). Enter the DEA number as two upper case letters followed

by 7 digits. e.g., AA1234567.

HELP-PROMPT:

Enter DEA number in the format 2 upper case letters followed by 7 numbers.

TECHNICAL DESCRIPTION:

This is the algorithm for the DEA number

FIELD: 53.2: DEA#

This field is used to enter the Drug Enforcement Agency (DEA) number.

Enter the DEA number as two upper case letters followed by 7 digits.

e.g., AA1234567.

HELP-PROMPT:

Enter the DEA number 2 letters 7 numbers.

TECHNICAL DESCRIPTION:

This is the algorithm for the DEA number

HELP-PROMPT: missing.

FILE: DEA BUSINESS ACTIVITY CODES

The DEA BUSINESS ACTIVITY CODES FILE is associated with the DEA numbers

and provider information in the DEA NUMBERS file. This file links a

provider with the type of service provided. It contains BUSINESS

ACTIVITY CODES that are supplied by the DOJ/DEA web service.

Field - BUSINESS ACTIVITY (#.02):

Description:

This field holds the Business Activity value used for DEA numbers. This

value can currently be one of the following:

A,B,C,D,E,F,G,H,J,K,L,M,N,P,R,S,T or U

This value, combined with a numeric business sub-type, categorizes a DEA

number.

Help-Prompt:

Enter the Business Activity value for used for DEA numbers. Answer must

be 1-3 characters in length.

Field - BUSINESS ACTIVITY DESCRIPTION (#1):

Description:

This is the description given for the Business Activity Code and Sub-code.

Help-Prompt:

Enter the Business Activity description given for the Business Activity

code and Business Activity Sub-code. Answer must be 3-60 characters in length.

Field - BUSINESS ACTIVITY SUB-CODE (#.03):

Description:

DEA uses an alpha character business activity code to identify various

categories of registrants. For example business activity code "C"

indicates a "Practitioner". DEA added a business activity sub-code field

to identify new sub-categories of registrants.

For example business activity code "C" in combination with business

activity sub-code "1" indicates a practitioner who has received a Drug

Addiction Treatment Act (DATA) Waiver (DATA Waived or DW) to provide

office based opioid treatment to 30 or 100 or 275 patients (DW/30, DW/100,

DW/275). As new sub-categories of business activities become regulated,

additional sub-code combinations (e.g. C-2, C-3, A-1, etc.) will be

assigned. MLP = Mid-Level Practitioner. NG = National Guard

Help-Prompt:

Enter the business activity sub-code associated with the Business

Activity Code. Answer must be 1-3 characters in length.

Field - FULL BUSINESS ACTIVITY CODE (#.01):

Description:

DEA uses an alpha character business activity code to identify various

categories of registrants. For example business activity code "C"

indicates a "Practitioner". DEA added a business activity sub-code field

to identify new sub-categories of registrants.

For example business activity code "C" in combination with business

activity sub-code "1" indicates a practitioner who has received a Drug

Addiction Treatment Act (DATA) Waiver (DATA Waived or DW) to provide

office based opioid treatment to 30 or 100 or 275 patients (DW/30, DW/100,

DW/275). As new sub-categories of business activities become regulated,

additional sub-code combinations (e.g. C-2, C-3, A-1, etc.) will be

assigned. MLP = Mid-Level Practitioner. NG = National Guard.

Help-Prompt:

Enter the full business activity code. This is composed of the Business

activity code and sub-code used for DEA numbers. Answer must be 2-4 characters

in length.

Field - MANUAL ENTRY DATE/TIME (#2):

Description:

This field should only be populated when a new Business Activity Code

(BAC) is entered manually due to the failure of the PSO DOJ/DEA WEB

SERVICE to establish a connection to the DOJ web server.

Help-Prompt:

This is the date/time this Business Activity Code was manually entered.

FILE: DEA NUMBERS

The DEA NUMBERS FILE is designed to contain demographic and permission

information about a provider related to the ability to order controlled

substance prescriptions.

Field - ADDITIONAL COMPANY INFO (#1.2):

Description:

This is the additional company information of the person or institution

associated with this DEA Number.

Help-Prompt:

Enter additional company info for the given person/institution. Answer

must be 1-40 characters in length.

Field - BUSINESS ACTIVITY CODE (#.02):

Description:

This is the business activity code related to this DEA Number.

Help-Prompt:

Enter the Business Activity code given to this DEA Number.

Field - CITY (#1.5):

Description:

This is the city of the permanent address of the person or institution

related to this DEA Number.

Help-Prompt:

Enter the city of the permanent address of the person or institution

associated with this DEA Number. Answer must be 1-33 characters in length.

Field - DEA NUMBER (#.01):

Description:

This field is used to enter the providers' Drug Enforcement Administration

(DEA) number. Enter the DEA number as two upper case letters followed

by 7 digits. e.g., AA1234567.

Help-Prompt:

Enter the DEA number in the format of 2 letters followed by 7 numbers.

Field - DETOX NUMBER (#.03):

Description:

If the DEA provider has detox privileges, this field will be populated

with a 'VX' or 'XA' followed by the numeric portion of the DEA number.

Help-Prompt:

Enter the detox number associated with this DEA Number. Answer must be 9

characters in length.

Field - EXPIRATION DATE (#.04):

Description:

This is the date of expiration for the DEA Number.

Help-Prompt:

Enter the date this DEA Number expires.

Field - LAST DOJ UPDATE DATE/TIME (#10.3):

Description:

This is the date/time the DOJ (Department of Justice) data was used to

update this DEA record.

Help-Prompt:

Enter the date/time this DEA record was last updated by the DOJ source.

Field - LAST UPDATED BY (#10.1):

Description:

This is the person from the NEW PERSON file who last initiated an update

to this DEA record.

Help-Prompt:

Enter the person who last updated this DEA record.

Field - LAST UPDATED DATE/TIME (#10.2):

Description:

This is the date/time of the last update to this DEA record.

Help-Prompt:

Enter the date/time this DEA record was last updated.

Field - NAME (PROVIDER OR INSTITUTION) (#1.1):

Description:

This is the name of the facility or person who is associated with this

DEA Number.

Help-Prompt:

Enter the name associated with this DEA Number. Answer must be 1-40

characters in length.

Field - SCHEDULE II NARCOTIC (#2.1):

Description:

This field is used to determine if the provider has privileges for

Schedule II drugs.

Help-Prompt:

DEA number allows for schedule II drugs?

Field - SCHEDULE II NON-NARCOTIC (#2.2):

Description:

This field is used to determine if the provider has privileges for

Schedule II non-narcotic.

Help-Prompt:

Provider has privileges for schedule II non-narcotic?

Field - SCHEDULE III NARCOTIC (#2.3):

Description:

This field is used to determine if the provider has privileges for

Schedule III narcotic.

Help-Prompt:

Provider has privileges for schedule III narcotic?

Field - SCHEDULE III NON-NARCOTIC (#2.4):

Description:

This field is used to determine if the provider has privileges for

Schedule III non-narcotic.

Help-Prompt:

Provider has privileges for schedule III non-narcotic?

Field - SCHEDULE IV (#2.5):

Description:

This field is used to determine if the provider has privileges for

Schedule IV controlled substances.

Help-Prompt:

Provider has privileges for schedule IV?

Field - SCHEDULE V (#2.6):

Description:

This field is used to determine if the provider has privileges for

Schedule V controlled substances.

Help-Prompt:

Provider has privileges for schedule V?

Field - STATE (#1.6):

Description:

This is the state of the permanent address of the person or institution

associated with this DEA Number.

Help-Prompt:

Enter the state of the permanent address associated with the person or

institution associated with this DEA Number.

Field - STREET ADDRESS 1 (#1.3):

Description:

This is the first line of the street address of the permanent address of

the person or institution associated with this DEA Number.

Help-Prompt:

Enter street address line 1 for the given person/institution. Answer must

be 1-40 characters in length.

Field - STREET ADDRESS 2 (#1.4):

Description:

This is the second line of the street address of the permanent address of

the person or institution associated with this DEA Number.

Help-Prompt:

Enter street address line 2 for the given person/institution. Answer must

be 1-40 characters in length.

Field - TYPE (#.07):

Description:

This identifies whether the DEA number is an individual DEA number or an

Institutional DEA number.

Help-Prompt:

Enter the usage type for the DEA. The DEA usage type may be 'Individual',

or 'Institutional.

Field - USE FOR INPATIENT ORDERS? (#.06):

Description:

This field indicates if this DEA number can be used for inpatient orders.

Help-Prompt:

Can this DEA be used for inpatient orders? Answer 'YES' or 'NO'.

Field - ZIP CODE (#1.7):

Description:

This is the postal ZIP code of the person or institution associated with

this DEA Number.

Help-Prompt:

Enter the ZIP CODE or ZIP+4. Answer must be 5-9 characters in length.

===============================================================================

Text in ROUTINES between quotes and/or after ;;, by line number:

XUSER3

3: Per VA Directive 6402, this routine should not be modified.

10: Exceeds maximum length (9).

11: Less than minimum length (9).

12: Invalid format. Must be 2 upper case letters followed by 7 digits.

14: Provider DEA number is already associated to another profile. Please check

the number entered.

15: DEA number is invalid. Please check the number entered.

16: DEA number doesn't match provider's last name. Please verify the

information.

21: Type \<Enter\> to continue

27: Exceeds maximum length (9).

28: Less than minimum length (9).

29: Invalid format. Must be 2 upper case letters followed by 7 digits.

32: DEA number is invalid. Please check the number entered.

50: That Suffix is in use.

\*\* Analysis Complete \*\*

Press \<Enter\> or '^' to exit:

### Create the Report in .TXT Files Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you chooses the Create the Report in .TXT Files action in <u>Figure 2</u>, the report content is sent to text (.txt) files.

#### Text File Directory Path

You are asked to either accept the default directory path to place the text files, or to choose a different directory path (<u>Figure 13</u>):

- To accept the default path, press \<Enter\> at the “Replace” prompt.
- To replace or modify the path, do the following at the “Replace” prompt:
1.  Type the part of the path to replace or type three (3) dots to replace the whole path.
7.  Press \<Enter\>.
8.  Type the replaced path changes.

<span id="_Ref127179931" class="anchor"></span>Figure 13: Sending Data to Text Files—Sample Dialog to Accept or Modify the .TXT Path Directory

Set the path to place the .TXT files

or accept the standard default.

PATH: /srv/vista/ddv/user/hfs/ Replace

![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/005.png) REF: Use Secure Shell (SSH) File Transfer Protocol (SFTP) to move text documents to your PC.

#### Text File Naming Formats

#### Build Analysis

The following is the Build Analysis text file name format:

*\<Directory Path\>*/<span class="mark">XPBA_Anal\_</span>*\<Build Name: Namespace-Version-Patch ID\>*\_*\<Date Build Analysis Run: MM-DD-YY\>*.TXT

For example:

/srv/vista/oak/user/hfs/<span class="mark">XPBA_Anal_XU-8.0-688_04-27-23.TXT</span>

Where:

- Directory Path: /srv/vista/ddv/user/hfs/
- Build Name: XU-8.0-688
- Date: 04-27-23

#### SQA Checklist Review

The following is the SQA Checklist Review text file name format:

*\<Directory Path\>*/<span class="mark">XPBA_SQA\_</span>*\<Build Name: Namespace-Version-Patch ID\>*\_*\<Date Build Analysis Run: MM-DD-YY\>*.TXT

For example:

/srv/vista/oak/user/hfs/<span class="mark">XPBA_SQA_XU-8.0-688_04-27-23.TXT</span>

Where:

- Directory Path: /srv/vista/ddv/user/hfs/
- Build Name: XU-8.0-688
- Date: 04-27-23

#### Description/Routine Text Review

The following is the Description/Routine Text Review text file name format:

*\<Directory Path\>*/<span class="mark">XPBA_Spell\_</span>*\<Build Name: Namespace-Version-Patch ID\>*\_*\<Date Build Analysis Run: MM-DD-YY\>*.TXT

For example:

/srv/vista/oak/user/hfs/<span class="mark">XPBA_Spell_XU-8.0-688_04-27-23.TXT</span>

Where:

- Directory Path: /srv/vista/ddv/user/hfs/
- Build Name: XU-8.0-688
- Date: 04-27-23

#### No SQA Checklist Items, Component Descriptions, or Routine Text

<u>Figure 14</u> shows the results when answering NO to the following prompts in the KIDS Build Analyzer \[XPDANLYZ\] option and then selecting the Create the Report in .TXT Files action:

- “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” <span class="mark">NO</span>
- “Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">NO</span>

In this example (<u>Figure 14</u>) and with these prompt settings, the Create the Report in .TXT Files action produces only one text file:

<span class="mark">XPBA_Anal\_</span>XU-8.0-688_01-26-23.TXT

<span id="_Ref127883459" class="anchor"></span>Figure 14: Running the “KIDS Build Analyzer” Option: “Create the Report in .TXT Files” Action: No SQA Checklist Items, Component Descriptions, or Routine Text—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

<span class="mark">1 KIDS Build Analyzer</span>

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO// <span class="mark">NO</span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">NO</span>

Analysis Results Display Choices:

1\. Print the Report

<span class="mark">2. Create the Report in .TXT Files</span>

3\. Send the Report in MailMan Messages

Select number: (1-3): <span class="mark">2 \<Enter\></span> . . .

Set the path to place the .TXT files

or accept the standard default.

PATH: /srv/vista/oak/user/hfs/ Replace <span class="mark">\<Enter\></span>

Build Analysis file was created.

File:

/srv/vista/oak/user/hfs/<span class="mark">XPBA_Anal_XU-8.0-688_01-26-23.TXT</span>

Press \<Enter\> or '^' to exit:

#### XPBA_Anal_XU-8.0-688_01-26-23.TXT File

<u>Figure 15</u> shows the XPBA_Anal_XU-8.0-688_01-26-23.TXT file contents from the Create the Report in .TXT Files action from the KIDS Build Analyzer option *without* including SQA checklist items, component descriptions, and routine text:

<span id="_Ref127883480" class="anchor"></span>Figure 15: Reviewing the Create the Report in .TXT Files Action—Output *without* SQA Checklist Items, Component Descriptions, or Routine Text: XPBA_Anal_XU-8.0-688_01-26-23.TXT File

KIDS Kernel Installation & Distribution System ...

NTEG Build an 'NTEG' routine for a package

<span class="mark">PG Programmer mode</span>

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

Map Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

Select Programmer Options \<TEST ACCOUNT\> Option: <span class="mark">PG \<Enter\></span> Programmer mode

KRNTST1\><span class="mark">!pr /srv/vista/oak/user/hfs/XPBA_Anal_XU-8.0-688_01-26-23.TXT</span>

2023-01-26 07:39 /srv/vista/oak/user/hfs/<span class="mark">XPBA_Anal_XU-8.0-688_01-26-23.TXT</span> Page1

XU\*8.0\*688 BUILD OVERVIEW Jan 26, 2023@07:38:52

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

2023-01-26 07:39 /srv/vista/oak/user/hfs/XPBA_Anal_XU-8.0-688_01-26-23.TXT Page2

It also lists the date ^XINDEX was last run.

Routine information:

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date of Last ^XINDEX: JAN 24, 2023

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

KRNDEV\>

#### Including SQA Checklist Items, Component Descriptions, and Routine Text

<u>Figure 16</u> shows the results when answering YES to the following prompts in the KIDS Build Analyzer \[XPDANLYZ\] option and then selecting the Create the Report in .TXT Files action:

- “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” <span class="mark">YES</span>
- “Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">YES</span>

In this example (<u>Figure 16</u>) and with these prompt settings, the Create the Report in .TXT Files action produces three text files:

- XPBA_Anal_XU-8.0-688_04-27-23.TXT (<u>Figure 17</u>)
- XPBA_SQA_XU-8.0-688_04-27-23.TXT (<u>Figure 18</u>)
- XPBA_Spell_XU-8.0-688_04-27-23.TXT (<u>Figure 19</u>)

<span id="_Ref135742417" class="anchor"></span>Figure 16: Running the “KIDS Build Analyzer” Option: “Create the Report in .TXT Files” Action: Including SQA Checklist Items, Component Descriptions, and Routine Text—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

<span class="mark">1 KIDS Build Analyzer</span>

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO// <span class="mark">YES</span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">YES</span>

Analysis Results Display Choices:

1\. Print the Report

<span class="mark">2. Create the Report in .TXT Files</span>

3\. Send the Report in MailMan Messages

Select number: (1-3): <span class="mark">2 \<Enter\></span> . . .

Set the path to place the .TXT files

or accept the standard default.

PATH: /srv/vista/oak/user/hfs/ Replace <span class="mark">\<Enter\></span>

Build Analysis file was created.

File:

/srv/vista/oak/user/hfs/<span class="mark">XPBA_Anal_XU-8.0-688_04-27-23.TXT</span>

SQA Checklist review file was created.

File:

/srv/vista/oak/user/hfs/<span class="mark">XPBA_SQA_XU-8.0-688_04-27-23.TXT</span>

Description/Routine text review file was created.

File:

/srv/vista/oak/user/hfs/<span class="mark">XPBA_Spell_XU-8.0-688_04-27-23.TXT</span>

\*\* Analysis Complete \*\*

Press \<Enter\> or '^' to exit:

<span id="_Toc128552312" class="anchor"></span>

#### XPBA_Anal_XU-8.0-688_04-27-23.TXT File

<u>Figure 17</u> shows the XPBA_Anal_XU-8.0-688_04-27-23.TXT file contents from the Create the Report in .TXT Files action from the KIDS Build Analyzer option including SQA checklist items, component descriptions, and routine text:

<span id="_Ref133422916" class="anchor"></span>Figure 17: Reviewing the “Create the Report in .TXT Files” Action Results—Output *with* SQA Checklist Items, Component Descriptions, and Routine Text: XPBA_Anal_XU-8.0-688_04-27-23.TXT File

KIDS Kernel Installation & Distribution System ...

NTEG Build an 'NTEG' routine for a package

<span class="mark">PG Programmer mode</span>

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

Map Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

Select Programmer Options \<TEST ACCOUNT\> Option: <span class="mark">PG \<Enter\></span> Programmer mode

KRNTST1\><span class="mark">!pr /srv/vista/oak/user/hfs/XPBA_Anal_XU-8.0-688_04-27-23.TXT</span>

2023-04-27 14:51 /srv/vista/oak/user/hfs/<span class="mark">XPBA_Anal_XU-8.0-688_04-27-23.TXT</span> Page1

XU\*8.0\*688 BUILD OVERVIEW Apr 27, 2023@14:51:23

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

2023-04-27 14:51 /srv/vista/oak/user/hfs/XPBA_Anal_XU-8.0-688_04-27-23.TXT Page2

It also lists the date ^XINDEX was last run.

Routine information:

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

KRNTST1\>

#### XPBA_SQA_XU-8.0-688_04-27-23.TXT File

<u>Figure 18</u> shows the XPBA_SQA_XU-8.0-688_04-27-23.TXT file contents from the Create the Report in .TXT Files action from the KIDS Build Analyzer option including SQA checklist items, component descriptions, and routine text:

<span id="_Ref133503917" class="anchor"></span>Figure 18: Reviewing the “Create the Report in .TXT Files” Action Results—Output *with* SQA Checklist Items, Component Descriptions, and Routine Text: XPBA_SQA_XU-8.0-688_04-27-23.TXT File

KRNTST1\><span class="mark">!pr /srv/vista/oak/user/hfs/XPBA_SQA_XU-8.0-688_04-27-23.TXT</span>

2023-04-27 14:51 /srv/vista/oak/user/hfs/<span class="mark">XPBA_SQA_XU-8.0-688_04-27-23.TXT</span> Page 1

ALL ^XTMP calls have zero nodes defined in this build's routines

XUSER3

^( ...........................................................................

VALN1DEA +8 I \$D(X),'F,\$D(DA(1)),\$D(^VA(200,"PS4",X)),\$O(^(X,0))'=DA(1) D

EN^DDIOL(\$C(7)\_"Provider DEA number is already associated to

another profile. Please check the number entered.") K X

KRNTST1\>

#### XPBA_Spell_XU-8.0-688_04-27-23.TXT File

<u>Figure 19</u> shows the XPBA_Spell_XU-8.0-688_04-27-23.TXT file contents from the Create the Report in .TXT Files action from the KIDS Build Analyzer option including SQA checklist items, component descriptions, and routine text:

<span id="_Ref133504998" class="anchor"></span>Figure 19: Reviewing the “Create the Report in .TXT Files” Action Results—Output *with* SQA Checklist Items, Component Descriptions, and Routine Text: XPBA_Spell_XU-8.0-688_04-27-23.TXT File

KRNTST1\><span class="mark">!pr /srv/vista/oak/user/hfs/XPBA_Spell_XU-8.0-688_04-27-23.TXT</span>

2023-04-27 14:51 /srv/vista/oak/user/hfs/<span class="mark">XPBA_Spell_XU-8.0-688_04-27-23.TXT</span> Pag1

Text for Review/Spell Check, Build XU\*8.0\*688; 4/27/23

Descriptions and other text associated with this build (for review and

spell check):

BUILD: XU\*8.0\*688

See FORUM Patch description.

FILE: NEW PERSON

SUBFILE 200.5321; FIELD: .01: DEA NUMBER

This field is used to enter the provider's Drug Enforcement Administration

(DEA) number(s). Enter the DEA number as two upper case letters followed

by 7 digits. e.g., AA1234567.

HELP-PROMPT:

Enter DEA number in the format 2 upper case letters followed by 7 numbers.

TECHNICAL DESCRIPTION:

This is the algorithm for the DEA number

FIELD: 53.2: DEA#

This field is used to enter the Drug Enforcement Agency (DEA) number.

Enter the DEA number as two upper case letters followed by 7 digits.

e.g., AA1234567.

HELP-PROMPT:

Enter the DEA number 2 letters 7 numbers.

TECHNICAL DESCRIPTION:

This is the algorithm for the DEA number

HELP-PROMPT: missing.

FILE: DEA BUSINESS ACTIVITY CODES

The DEA BUSINESS ACTIVITY CODES FILE is associated with the DEA numbers

and provider information in the DEA NUMBERS file. This file links a

provider with the type of service provided. It contains BUSINESS

ACTIVITY CODES that are supplied by the DOJ/DEA web service.

Field - BUSINESS ACTIVITY (#.02):

Description:

This field holds the Business Activity value used for DEA numbers. This

value can currently be one of the following:

A,B,C,D,E,F,G,H,J,K,L,M,N,P,R,S,T or U

This value, combined with a numeric business sub-type, categorizes a DEA

number.

Help-Prompt:

Enter the Business Activity value for used for DEA numbers. Answer must

be 1-3 characters in length.

Field - BUSINESS ACTIVITY DESCRIPTION (#1):

Description:

This is the description given for the Business Activity Code and Sub-code.

Help-Prompt:

2023-04-27 14:51 /srv/vista/oak/user/hfs/XPBA_Spell_XU-8.0-688_04-27-23.TXT Pag2

Enter the Business Activity description given for the Business Activity

code and Business Activity Sub-code. Answer must be 3-60 characters in len.

Field - BUSINESS ACTIVITY SUB-CODE (#.03):

Description:

DEA uses an alpha character business activity code to identify various

categories of registrants. For example business activity code "C"

indicates a "Practitioner". DEA added a business activity sub-code field

to identify new sub-categories of registrants.

For example business activity code "C" in combination with business

activity sub-code "1" indicates a practitioner who has received a Drug

Addiction Treatment Act (DATA) Waiver (DATA Waived or DW) to provide

office based opioid treatment to 30 or 100 or 275 patients (DW/30, DW/100,

DW/275). As new sub-categories of business activities become regulated,

additional sub-code combinations (e.g. C-2, C-3, A-1, etc.) will be

assigned. MLP = Mid-Level Practitioner. NG = National Guard

Help-Prompt:

Enter the business activity sub-code associated with the Business

Activity Code. Answer must be 1-3 characters in length.

Field - FULL BUSINESS ACTIVITY CODE (#.01):

Description:

DEA uses an alpha character business activity code to identify various

categories of registrants. For example business activity code "C"

indicates a "Practitioner". DEA added a business activity sub-code field

to identify new sub-categories of registrants.

For example business activity code "C" in combination with business

activity sub-code "1" indicates a practitioner who has received a Drug

Addiction Treatment Act (DATA) Waiver (DATA Waived or DW) to provide

office based opioid treatment to 30 or 100 or 275 patients (DW/30, DW/100,

DW/275). As new sub-categories of business activities become regulated,

additional sub-code combinations (e.g. C-2, C-3, A-1, etc.) will be

assigned. MLP = Mid-Level Practitioner. NG = National Guard.

Help-Prompt:

Enter the full business activity code. This is composed of the Business

activity code and sub-code used for DEA numbers. Answer must be 2-4 charac.

Field - MANUAL ENTRY DATE/TIME (#2):

Description:

This field should only be populated when a new Business Activity Code

(BAC) is entered manually due to the failure of the PSO DOJ/DEA WEB

SERVICE to establish a connection to the DOJ web server.

Help-Prompt:

This is the date/time this Business Activity Code was manually entered.

FILE: DEA NUMBERS

The DEA NUMBERS FILE is designed to contain demographic and permission

information about a provider related to the ability to order controlled

substance prescriptions.

Field - ADDITIONAL COMPANY INFO (#1.2):

Description:

This is the additional company information of the person or institution

associated with this DEA Number.

2023-04-27 14:51 /srv/vista/oak/user/hfs/XPBA_Spell_XU-8.0-688_04-27-23.TXT Pag3

Help-Prompt:

Enter additional company info for the given person/institution. Answer

must be 1-40 characters in length.

Field - BUSINESS ACTIVITY CODE (#.02):

Description:

This is the business activity code related to this DEA Number.

Help-Prompt:

Enter the Business Activity code given to this DEA Number.

Field - CITY (#1.5):

Description:

This is the city of the permanent address of the person or institution

related to this DEA Number.

Help-Prompt:

Enter the city of the permanent address of the person or institution

associated with this DEA Number. Answer must be 1-33 characters in length.

Field - DEA NUMBER (#.01):

Description:

This field is used to enter the providers' Drug Enforcement Administration

(DEA) number. Enter the DEA number as two upper case letters followed

by 7 digits. e.g., AA1234567.

Help-Prompt:

Enter the DEA number in the format of 2 letters followed by 7 numbers.

Field - DETOX NUMBER (#.03):

Description:

If the DEA provider has detox privileges, this field will be populated

with a 'VX' or 'XA' followed by the numeric portion of the DEA number.

Help-Prompt:

Enter the detox number associated with this DEA Number. Answer must be 9

characters in length.

Field - EXPIRATION DATE (#.04):

Description:

This is the date of expiration for the DEA Number.

Help-Prompt:

Enter the date this DEA Number expires.

Field - LAST DOJ UPDATE DATE/TIME (#10.3):

Description:

This is the date/time the DOJ (Department of Justice) data was used to

update this DEA record.

Help-Prompt:

Enter the date/time this DEA record was last updated by the DOJ source.

Field - LAST UPDATED BY (#10.1):

Description:

This is the person from the NEW PERSON file who last initiated an update

to this DEA record.

Help-Prompt:

Enter the person who last updated this DEA record.

Field - LAST UPDATED DATE/TIME (#10.2):

Description:

2023-04-27 14:51 /srv/vista/oak/user/hfs/XPBA_Spell_XU-8.0-688_04-27-23.TXT Pag4

This is the date/time of the last update to this DEA record.

Help-Prompt:

Enter the date/time this DEA record was last updated.

Field - NAME (PROVIDER OR INSTITUTION) (#1.1):

Description:

This is the name of the facility or person who is associated with this

DEA Number.

Help-Prompt:

Enter the name associated with this DEA Number. Answer must be 1-40

characters in length.

Field - SCHEDULE II NARCOTIC (#2.1):

Description:

This field is used to determine if the provider has privileges for

Schedule II drugs.

Help-Prompt:

DEA number allows for schedule II drugs?

Field - SCHEDULE II NON-NARCOTIC (#2.2):

Description:

This field is used to determine if the provider has privileges for

Schedule II non-narcotic.

Help-Prompt:

Provider has privileges for schedule II non-narcotic?

Field - SCHEDULE III NARCOTIC (#2.3):

Description:

This field is used to determine if the provider has privileges for

Schedule III narcotic.

Help-Prompt:

Provider has privileges for schedule III narcotic?

Field - SCHEDULE III NON-NARCOTIC (#2.4):

Description:

This field is used to determine if the provider has privileges for

Schedule III non-narcotic.

Help-Prompt:

Provider has privileges for schedule III non-narcotic?

Field - SCHEDULE IV (#2.5):

Description:

This field is used to determine if the provider has privileges for

Schedule IV controlled substances.

Help-Prompt:

Provider has privileges for schedule IV?

Field - SCHEDULE V (#2.6):

Description:

This field is used to determine if the provider has privileges for

Schedule V controlled substances.

Help-Prompt:

Provider has privileges for schedule V?

Field - STATE (#1.6):

Description:

2023-04-27 14:51 /srv/vista/oak/user/hfs/XPBA_Spell_XU-8.0-688_04-27-23.TXT Pag5

This is the state of the permanent address of the person or institution

associated with this DEA Number.

Help-Prompt:

Enter the state of the permanent address associated with the person or

institution associated with this DEA Number.

Field - STREET ADDRESS 1 (#1.3):

Description:

This is the first line of the street address of the permanent address of

the person or institution associated with this DEA Number.

Help-Prompt:

Enter street address line 1 for the given person/institution. Answer must

be 1-40 characters in length.

Field - STREET ADDRESS 2 (#1.4):

Description:

This is the second line of the street address of the permanent address of

the person or institution associated with this DEA Number.

Help-Prompt:

Enter street address line 2 for the given person/institution. Answer must

be 1-40 characters in length.

Field - TYPE (#.07):

Description:

This identifies whether the DEA number is an individual DEA number or an

Institutional DEA number.

Help-Prompt:

Enter the usage type for the DEA. The DEA usage type may be 'Individual',

or 'Institutional.

Field - USE FOR INPATIENT ORDERS? (#.06):

Description:

This field indicates if this DEA number can be used for inpatient orders.

Help-Prompt:

Can this DEA be used for inpatient orders? Answer 'YES' or 'NO'.

Field - ZIP CODE (#1.7):

Description:

This is the postal ZIP code of the person or institution associated with

this DEA Number.

Help-Prompt:

Enter the ZIP CODE or ZIP+4. Answer must be 5-9 characters in length.

===============================================================================

Text in ROUTINES between quotes and/or after ;;, by line number:

XUSER3

3: Per VA Directive 6402, this routine should not be modified.

10: Exceeds maximum length (9).

11: Less than minimum length (9).

12: Invalid format. Must be 2 upper case letters followed by 7 digits.

14: Provider DEA number is already associated to another profile. Please check

the number entered.

15: DEA number is invalid. Please check the number entered.

2023-04-27 14:51 /srv/vista/oak/user/hfs/XPBA_Spell_XU-8.0-688_04-27-23.TXT Pag6

16: DEA number doesn't match provider's last name. Please verify the

information.

21: Type \<Enter\> to continue

27: Exceeds maximum length (9).

28: Less than minimum length (9).

29: Invalid format. Must be 2 upper case letters followed by 7 digits.

32: DEA number is invalid. Please check the number entered.

50: That Suffix is in use.

KRNTST1\>

### Send the Report in MailMan Messages Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If choosing to email the build analysis data, you get a choice of to whom or to what mail groups the emails should be sent. If you optionally include SQA checklist items, component descriptions, and routine text you will get 1-3 messages, depending on the choices made in <u>Figure 2</u>, and will be prompted for each one on where to send it.

#### No SQA Checklist Items, Component Descriptions, or Routine Text

<u>Figure 20</u> shows the results when answering NO to the following prompts in the KIDS Build Analyzer \[XPDANLYZ\] option and then selecting the Send the Report in MailMan Messages action:

- “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” <span class="mark">NO</span>
- “Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">NO</span>

In this example (<u>Figure 20</u>) and with these prompt settings, the Send the Report in MailMan Messages action produces only one email message:

Build Analysis - XU\*8.0\*688

<span id="_Ref133509618" class="anchor"></span>Figure 20: Running the KIDS Build Analyzer Option: “Send the Report in MailMan Messages” Action: No SQA Checklist Items, Component Descriptions, or Routine Text—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

<span class="mark">1 KIDS Build Analyzer</span>

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO// <span class="mark">NO</span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">NO</span>

Analysis Results Display Choices:

1\. Print the Report

2\. Create the Report in .TXT Files

<span class="mark">3. Send the Report in MailMan Messages</span>

Select number: (1-3): <span class="mark">3 \<Enter\></span>

<span class="mark">BUILD ANALYSIS email:</span>

Send mail to: XUUSER,ONE// <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

\*\* Analysis Complete \*\*

Check for email with subject of <span class="mark">Build Analysis - XU\*8.0\*688</span>

#### Build Analysis - XU\*8.0\*688 Message

<u>Figure 21</u> and <u>Figure 22</u> show the Build Analysis - XU\*8.0\*688 message contents from the Send the Report in MailMan Messages action from the KIDS Build Analyzer option *without* including SQA checklist items, component descriptions, and routine text:

<span id="_Ref133512297" class="anchor"></span>Figure 21: Retrieving the Email Sent with the “Send the Report in MailMan Messages” Action from the KIDS Build Analyzer Option—System Prompts and User Entries

Select Systems Manager Menu \<TEST ACCOUNT\> Option: <span class="mark">XMUSER \<Enter\></span> MailMan Menu

VA MailMan 8.0 service for XUUSER.ONE@\<REDACTED\>.VA.GOV

You last used MailMan: 01/30/23@06:58

You have 1 new message.

NML New Messages and Responses

<span class="mark">RML Read/Manage Messages</span>

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu \<TEST ACCOUNT\> Option: <span class="mark">RML \<Enter\></span> Read/Manage Messages

Select message reader: <span class="mark">Classic//</span> <span class="mark">\<Enter\></span>

Read mail in basket: IN// <span class="mark">\<Enter\></span> (10 messages, 1 new)

Last message number: 10 Messages in basket: 10 (1 new)

Enter ??? for help.

IN Basket Message: 1// <span class="mark">?</span>

IN Basket, 10 messages (1-10), 1 new

\*=New/!=Priority.......Subject.........................From....................

1\. ZZDAVE\*1.0\*1 v1 \<XUUSER.ONE@KRNDEV.

2\. Backup of ZZDAVE\*1.0\*1 on Feb 13, 2023 XUUSER.ONE

3\. XU\*8\*782 TEST v1 \<"NPM \[#114763033\]"@FO

4\. Backup of XU\*8.0\*782 on Feb 17, 2023 STERNGAST,DAVIDXUUSER.ONE

5\. XU\*8\*782 TEST v2 \<"NPM \[#114856013\]"@FO

6\. ZZTEST785\*1.0\*1 v1 XUUSER.ONE

7\. XU\*8\*785 TEST v1 \<"NPM \[#115262788\]"@FO

8\. Backup of XU\*8.0\*785 on Apr 10, 2023 XUUSER.ONE

9\. XU\*8\*782 TEST v4 \<"NPM \[#115347325\]"@FO

<span class="mark">\*10. Build Analysis - XU\*8.0\*688 KERNEL BUILD ANALYZER</span>

IN Basket Message: 1// <span class="mark">10</span>

<span id="_Ref135835064" class="anchor"></span>Figure 22: Reviewing the Email Sent with the “Send the Report in MailMan Messages” Action from the KIDS Build Analyzer Option—Sample Build Analysis Email

<span class="mark">Subj: Build Analysis - XU\*8.0\*688 \[#176546\] 04/13/23@05:59 76 lines</span>

From: KERNEL BUILD ANALYZER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

XU\*8.0\*688 BUILD OVERVIEW Apr 13, 2023@05:59:21

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

Type \<Enter\> to continue or '^' to exit: <span class="mark">\<Enter\></span>

Subj: Build Analysis - XU\*8.0\*688 \[#172100\] Page 2

-------------------------------------------------------------------------------

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Type \<Enter\> to continue or '^' to exit: <span class="mark">\<Enter\></span>

Subj: Build Analysis - XU\*8.0\*688 \[#172100\] Page 3

-------------------------------------------------------------------------------

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

Type \<Enter\> to continue or '^' to exit: <span class="mark">\<Enter\></span>

Subj: Build Analysis - XU\*8.0\*688 \[#172100\] Page 4

-------------------------------------------------------------------------------

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date of Last ^XINDEX: JAN 24, 2023

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

Enter message action (in IN basket): Ignore// <span class="mark">\<Enter\></span>

End reached. Begin again? No//

#### Including SQA Checklist Items, Component Descriptions, and Routine Text

<u>Figure 23</u> shows the results when answering YES to the following prompts in the KIDS Build Analyzer \[XPDANLYZ\] option and then selecting the Send the Report in MailMan Messages action:

- “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” <span class="mark">YES</span>
- “Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">YES</span>

In this example (<u>Figure 23</u>) and with these prompt settings, the Send the Report in MailMan Messages action produces three email message:

- Build Analysis - XU\*8.0\*688 (<u>Figure 24</u>)
- SQA Analysis - XU\*8.0\*688 (<u>Figure 25</u>)
- Routine and Component Text - XU\*8.0\*688 (<u>Figure 26</u>)

<span id="_Ref133512435" class="anchor"></span>Figure 23: Running the KIDS Build Analyzer Option: “Send the Report in MailMan Messages” Action: Including SQA Checklist Items, Component Descriptions, or Routine Text—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

<span class="mark">1 KIDS Build Analyzer</span>

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">1 \<Enter\></span> KIDS Build Analyzer

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO// <span class="mark">YES</span>

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">YES</span>

Analysis Results Display Choices:

1\. Print the Report

2\. Create the Report in .TXT Files

<span class="mark">3. Send the Report in MailMan Messages</span>

Select number: (1-3): <span class="mark">3 \<Enter\></span>

<span class="mark">BUILD ANALYSIS email</span>:

Send mail to: XUUSER,TWO// <span class="mark">\<Enter\></span> XUUSER,TWO

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

Check for email with subject of <span class="mark">Build Analysis - XU\*8.0\*688</span>

<span class="mark">SQA Checklist review email</span>:

Send mail to: XUUSER,TWO// <span class="mark">\<Enter\></span> XUUSER,TWO

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

Check for email with subject of:

<span class="mark">SQA Analysis - XU\*8.0\*688</span>

<span class="mark">Routine/Component Text email</span>:

Send mail to: XUUSER,TWO// <span class="mark">\<Enter\></span> XUUSER,TWO

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

Check for email with subject of:

<span class="mark">Routine and Component Text - XU\*8.0\*688</span>

\*\* Analysis Complete \*\*

1 KIDS Build Analyzer

2 Delete Build Analyzer Text Files

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option:

#### Build Analysis - XU\*8.0\*688 Message

<u>Figure 24</u> shows the Build Analysis - XU\*8.0\*688 message contents from the Send the Report in MailMan Messages action from the KIDS Build Analyzer option including SQA checklist items, component descriptions, and routine text:

![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/006.png) NOTE: To retrieve the email sent with the “Send the Report in MailMan Messages” Action from the KIDS Build Analyzer Option, follow the prompts indicated in <u>Figure 21</u>.

<span id="_Ref133513619" class="anchor"></span>Figure 24: Reviewing the Email Sent with the “Send the Report in MailMan Messages” Action Results—Output *with* SQA Checklist Items, Component Descriptions, and Routine Text: Build Analysis - XU\*8.0\*688 Message

Subj: <span class="mark">Build Analysis - XU\*8.0\*688</span> \[#176989\] 04/27/23@18:33 76 lines

From: KERNEL BUILD ANALYZER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

XU\*8.0\*688 BUILD OVERVIEW Apr 27, 2023@18:32:51

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

#### SQA Analysis - XU\*8.0\*688 Message

<u>Figure 25</u> shows the SQA Analysis - XU\*8.0\*688 message contents from the Send the Report in MailMan Messages action from the KIDS Build Analyzer option including SQA checklist items, component descriptions, and routine text:

![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/007.png) NOTE: To retrieve the email sent with the “Send the Report in MailMan Messages” Action from the KIDS Build Analyzer Option, follow the prompts indicated in <u>Figure 21</u>.

<span id="_Ref133513625" class="anchor"></span>Figure 25: Reviewing the “Send the Report in MailMan Messages” Action Results—Output *with* SQA Checklist Items, Component Descriptions, and Routine Text: SQA Analysis - XU\*8.0\*688 Message

Subj: <span class="mark">SQA Analysis - XU\*8.0\*688</span> \[#176990\] 04/27/23@18:33 9 lines

From: KERNEL BUILD ANALYZER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

ALL ^XTMP calls have zero nodes defined in this build's routines

XUSER3

^( ...........................................................................

VALN1DEA +8 I \$D(X),'F,\$D(DA(1)),\$D(^VA(200,"PS4",X)),\$O(^(X,0))'=DA(1) D

EN^DDIOL(\$C(7)\_"Provider DEA number is already associated to

another profile. Please check the number entered.") K X

#### Routine and Component Text - XU\*8.0\*688 Message

<u>Figure 26</u> shows the Routine and Component Text - XU\*8.0\*688 message contents from the Send the Report in MailMan Messages action from the KIDS Build Analyzer option including SQA checklist items, component descriptions, and routine text:

![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/008.png) NOTE: To retrieve the email sent with the “Send the Report in MailMan Messages” Action from the KIDS Build Analyzer Option, follow the prompts indicated in <u>Figure 21</u>.

<span id="_Ref133513993" class="anchor"></span>Figure 26: Reviewing the “Send the Report in MailMan Messages” Action Results—Output *with* SQA Checklist Items, Component Descriptions, and Routine Text: Routine and Component Text - XU\*8.0\*688 Message

Subj: <span class="mark">Routine and Component Text - XU\*8.0\*688</span> \[#176991\] 04/27/23@18:33

285 lines

From: KERNEL BUILD ANALYZER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Descriptions and other text associated with this build (for review and

spell check):

BUILD: XU\*8.0\*688

See FORUM Patch description.

FILE: NEW PERSON

SUBFILE 200.5321; FIELD: .01: DEA NUMBER

This field is used to enter the provider's Drug Enforcement Administration

(DEA) number(s). Enter the DEA number as two upper case letters followed

by 7 digits. e.g., AA1234567.

HELP-PROMPT:

Enter DEA number in the format 2 upper case letters followed by 7 numbers.

TECHNICAL DESCRIPTION:

This is the algorithm for the DEA number

FIELD: 53.2: DEA#

This field is used to enter the Drug Enforcement Agency (DEA) number.

Enter the DEA number as two upper case letters followed by 7 digits.

e.g., AA1234567.

HELP-PROMPT:

Enter the DEA number 2 letters 7 numbers.

TECHNICAL DESCRIPTION:

This is the algorithm for the DEA number

HELP-PROMPT: missing.

FILE: DEA BUSINESS ACTIVITY CODES

The DEA BUSINESS ACTIVITY CODES FILE is associated with the DEA numbers

and provider information in the DEA NUMBERS file. This file links a

provider with the type of service provided. It contains BUSINESS

ACTIVITY CODES that are supplied by the DOJ/DEA web service.

Field - BUSINESS ACTIVITY (#.02):

Description:

This field holds the Business Activity value used for DEA numbers. This

value can currently be one of the following:

A,B,C,D,E,F,G,H,J,K,L,M,N,P,R,S,T or U

This value, combined with a numeric business sub-type, categorizes a DEA

number.

Help-Prompt:

Enter the Business Activity value for used for DEA numbers. Answer must

be 1-3 characters in length.

Field - BUSINESS ACTIVITY DESCRIPTION (#1):

Description:

This is the description given for the Business Activity Code and Sub-code.

Help-Prompt:

Enter the Business Activity description given for the Business Activity

code and Business Activity Sub-code. Answer must be 3-60 characters in length.

Field - BUSINESS ACTIVITY SUB-CODE (#.03):

Description:

DEA uses an alpha character business activity code to identify various

categories of registrants. For example business activity code "C"

indicates a "Practitioner". DEA added a business activity sub-code field

to identify new sub-categories of registrants.

For example business activity code "C" in combination with business

activity sub-code "1" indicates a practitioner who has received a Drug

Addiction Treatment Act (DATA) Waiver (DATA Waived or DW) to provide

office based opioid treatment to 30 or 100 or 275 patients (DW/30, DW/100,

DW/275). As new sub-categories of business activities become regulated,

additional sub-code combinations (e.g. C-2, C-3, A-1, etc.) will be

assigned. MLP = Mid-Level Practitioner. NG = National Guard

Help-Prompt:

Enter the business activity sub-code associated with the Business

Activity Code. Answer must be 1-3 characters in length.

Field - FULL BUSINESS ACTIVITY CODE (#.01):

Description:

DEA uses an alpha character business activity code to identify various

categories of registrants. For example business activity code "C"

indicates a "Practitioner". DEA added a business activity sub-code field

to identify new sub-categories of registrants.

For example business activity code "C" in combination with business

activity sub-code "1" indicates a practitioner who has received a Drug

Addiction Treatment Act (DATA) Waiver (DATA Waived or DW) to provide

office based opioid treatment to 30 or 100 or 275 patients (DW/30, DW/100,

DW/275). As new sub-categories of business activities become regulated,

additional sub-code combinations (e.g. C-2, C-3, A-1, etc.) will be

assigned. MLP = Mid-Level Practitioner. NG = National Guard.

Help-Prompt:

Enter the full business activity code. This is composed of the Business

activity code and sub-code used for DEA numbers. Answer must be 2-4 characters

in length.

Field - MANUAL ENTRY DATE/TIME (#2):

Description:

This field should only be populated when a new Business Activity Code

(BAC) is entered manually due to the failure of the PSO DOJ/DEA WEB

SERVICE to establish a connection to the DOJ web server.

Help-Prompt:

This is the date/time this Business Activity Code was manually entered.

FILE: DEA NUMBERS

The DEA NUMBERS FILE is designed to contain demographic and permission

information about a provider related to the ability to order controlled

substance prescriptions.

Field - ADDITIONAL COMPANY INFO (#1.2):

Description:

This is the additional company information of the person or institution

associated with this DEA Number.

Help-Prompt:

Enter additional company info for the given person/institution. Answer

must be 1-40 characters in length.

Field - BUSINESS ACTIVITY CODE (#.02):

Description:

This is the business activity code related to this DEA Number.

Help-Prompt:

Enter the Business Activity code given to this DEA Number.

Field - CITY (#1.5):

Description:

This is the city of the permanent address of the person or institution

related to this DEA Number.

Help-Prompt:

Enter the city of the permanent address of the person or institution

associated with this DEA Number. Answer must be 1-33 characters in length.

Field - DEA NUMBER (#.01):

Description:

This field is used to enter the providers' Drug Enforcement Administration

(DEA) number. Enter the DEA number as two upper case letters followed

by 7 digits. e.g., AA1234567.

Help-Prompt:

Enter the DEA number in the format of 2 letters followed by 7 numbers.

Field - DETOX NUMBER (#.03):

Description:

If the DEA provider has detox privileges, this field will be populated

with a 'VX' or 'XA' followed by the numeric portion of the DEA number.

Help-Prompt:

Enter the detox number associated with this DEA Number. Answer must be 9

characters in length.

Field - EXPIRATION DATE (#.04):

Description:

This is the date of expiration for the DEA Number.

Help-Prompt:

Enter the date this DEA Number expires.

Field - LAST DOJ UPDATE DATE/TIME (#10.3):

Description:

This is the date/time the DOJ (Department of Justice) data was used to

update this DEA record.

Help-Prompt:

Enter the date/time this DEA record was last updated by the DOJ source.

Field - LAST UPDATED BY (#10.1):

Description:

This is the person from the NEW PERSON file who last initiated an update

to this DEA record.

Help-Prompt:

Enter the person who last updated this DEA record.

Field - LAST UPDATED DATE/TIME (#10.2):

Description:

This is the date/time of the last update to this DEA record.

Help-Prompt:

Enter the date/time this DEA record was last updated.

Field - NAME (PROVIDER OR INSTITUTION) (#1.1):

Description:

This is the name of the facility or person who is associated with this

DEA Number.

Help-Prompt:

Enter the name associated with this DEA Number. Answer must be 1-40

characters in length.

Field - SCHEDULE II NARCOTIC (#2.1):

Description:

This field is used to determine if the provider has privileges for

Schedule II drugs.

Help-Prompt:

DEA number allows for schedule II drugs?

Field - SCHEDULE II NON-NARCOTIC (#2.2):

Description:

This field is used to determine if the provider has privileges for

Schedule II non-narcotic.

Help-Prompt:

Provider has privileges for schedule II non-narcotic?

Field - SCHEDULE III NARCOTIC (#2.3):

Description:

This field is used to determine if the provider has privileges for

Schedule III narcotic.

Help-Prompt:

Provider has privileges for schedule III narcotic?

Field - SCHEDULE III NON-NARCOTIC (#2.4):

Description:

This field is used to determine if the provider has privileges for

Schedule III non-narcotic.

Help-Prompt:

Provider has privileges for schedule III non-narcotic?

Field - SCHEDULE IV (#2.5):

Description:

This field is used to determine if the provider has privileges for

Schedule IV controlled substances.

Help-Prompt:

Provider has privileges for schedule IV?

Field - SCHEDULE V (#2.6):

Description:

This field is used to determine if the provider has privileges for

Schedule V controlled substances.

Help-Prompt:

Provider has privileges for schedule V?

Field - STATE (#1.6):

Description:

This is the state of the permanent address of the person or institution

associated with this DEA Number.

Help-Prompt:

Enter the state of the permanent address associated with the person or

institution associated with this DEA Number.

Field - STREET ADDRESS 1 (#1.3):

Description:

This is the first line of the street address of the permanent address of

the person or institution associated with this DEA Number.

Help-Prompt:

Enter street address line 1 for the given person/institution. Answer must

be 1-40 characters in length.

Field - STREET ADDRESS 2 (#1.4):

Description:

This is the second line of the street address of the permanent address of

the person or institution associated with this DEA Number.

Help-Prompt:

Enter street address line 2 for the given person/institution. Answer must

be 1-40 characters in length.

Field - TYPE (#.07):

Description:

This identifies whether the DEA number is an individual DEA number or an

Institutional DEA number.

Help-Prompt:

Enter the usage type for the DEA. The DEA usage type may be 'Individual',

or 'Institutional.

Field - USE FOR INPATIENT ORDERS? (#.06):

Description:

This field indicates if this DEA number can be used for inpatient orders.

Help-Prompt:

Can this DEA be used for inpatient orders? Answer 'YES' or 'NO'.

Field - ZIP CODE (#1.7):

Description:

This is the postal ZIP code of the person or institution associated with

this DEA Number.

Help-Prompt:

Enter the ZIP CODE or ZIP+4. Answer must be 5-9 characters in length.

===============================================================================

Text in ROUTINES between quotes and/or after ;;, by line number:

XUSER3

3: Per VA Directive 6402, this routine should not be modified.

10: Exceeds maximum length (9).

11: Less than minimum length (9).

12: Invalid format. Must be 2 upper case letters followed by 7 digits.

14: Provider DEA number is already associated to another profile. Please check

the number entered.

15: DEA number is invalid. Please check the number entered.

16: DEA number doesn't match provider's last name. Please verify the

information.

21: Type \<Enter\> to continue

27: Exceeds maximum length (9).

28: Less than minimum length (9).

29: Invalid format. Must be 2 upper case letters followed by 7 digits.

32: DEA number is invalid. Please check the number entered.

50: That Suffix is in use.

## Delete Build Analyzer Text Files Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Delete Build Analyzer Text Files \[XPDANLYZ_DEL\] option to delete any previously generated .txt files.

<u>Figure 27</u> demonstrates using the Delete Build Analyzer Text Files \[XPDANLYZ_DEL\] option:

<span id="_Ref128559516" class="anchor"></span>Figure 27: Running the Delete Build Analyzer Text Files Option—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

1 KIDS Build Analyzer

<span class="mark">2 Delete Build Analyzer Text Files</span>

3 KIDS Build Analyzer - Full SQA Search

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">2 \<Enter\></span> Delete Build Analyzer

Set the path to find the .TXT files

or accept the standard default.

PATH: /srv/vista/oak/user/hfs/ Replace <span class="mark">\<Enter\></span>

Build Analyzer text files:

1\. XPBA_Anal_DI-22.0-31_04-14-22.TXT

<span class="mark">2. XPBA_Anal_XU-8.0-688_01-26-23.TXT</span>

3\. XPBA_Anal_XU-8.0-770_01-20-23.TXT

Delete all the files above? <span class="mark">NO//</span> <span class="mark">\<Enter\></span>

Select number of file or files to delete: (1-3): <span class="mark">2</span>

Deletions completed.

## KIDS Build Analyzer - Full SQA Search Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the KIDS Build Analyzer - Full SQA Search \[XPDANLYZ_SQA\] option to check the build with a full SQA check for SQA checklist items and naked references. The SQA logic in the Build Analyzer software goes through the XPDARRR array (<u>Figure 28</u>), which is set in the XPDANYLZ2 routine, and checks for occurrences in the build routines.

<span id="_Ref133401128" class="anchor"></span>Figure 28: SQA Logic—XPDARRR Array

SQA(RR) ;Sets SQA CL array XPDARRR

S XPDARRR("////",RR,0)=""  
S XPDARRR("DIC(0)",RR,0)=""  
S XPDARRR("^UTILITY",RR,0)=""  
S XPDARRR("^TMP",RR,0)=""  
S XPDARRR("^XTMP",RR,0)=""  
S XPDARRR("%",RR,0)=""  
S XPDARRR("\$I",RR,0)=""  
S XPDARRR("U=",RR,0)=""  
S XPDARRR("K ^",RR,0)=""  
S XPDARRR("K:",RR,0)=""  
S XPDARRR("K @",RR,0)=""  
S XPDARRR("^(",RR,0)=""  
S XPDARRR("IO",RR,0)=""

The KIDS Build Analyzer - Full SQA Search option goes through the contents of the build routines line-by-line and checks for the following code variables, globals, array references, commands, and other code statements:

- “////”
- “DIC(0)”
- “^UTILITY”
- “^TMP”
- “^XTMP”
- “%”
- “\$I”
- “U=”
- “K ^”
- “K:”
- “K @”
- “^(”
- “IO”
- Naked References—If found they appear in the SQA output section at the end of the report.

If there are any issues, as described in Section <u>3.9</u>, “<u>SQA Check—Full Lines</u>,” the Build Analyzer tool builds the XPDSQA array, which is set in the XPDANYLZ2 routine and contains the errors found in the build (<u>Figure 29</u>).

<span id="_Ref135839281" class="anchor"></span>Figure 29: Sample XPDSQA Array with Errors Found in a Build

XPDSQA("XUSER3","IO",10,"VALN1DEA +4")=" I \$D(X) I \$L(X)\>9 K X D EN^DDIOL(\$C(7)\_

"Exceeds maximum length (9).")"

XPDSQA("XUSER3","IO",11,"VALN1DEA +5")=" I \$D(X) I \$L(X)\<9 K X D EN^DDIOL(\$C(7)\_

"Less than minimum length (9).")"

XPDSQA("XUSER3","IO",12,"VALN1DEA +6")=" I \$D(X) I '(X?2U7N) K X D EN^DDIOL(\$C(7

)\_"Invalid format. Must be 2 upper case letters followed by 7 digits.")"

XPDSQA("XUSER3","IO",14,"VALN1DEA +8")=" I \$D(X),'F,\$D(DA(1)),\$D(^VA(200,"PS4",X

)),\$O(^(X,0))'=DA(1) D EN^DDIOL(\$C(7)\_"Provider DEA number is already associated

to another profile. Please check the number entered.") K X"

XPDSQA("XUSER3","IO",15,"VALN1DEA +9")=" I \$D(X),'\$\$DEANUM(X) D EN^DDIOL(\$C(7)\_"

DEA number is invalid. Please check the number entered.") K X"

XPDSQA("XUSER3","IO",16,"VALN1DEA +10")=" I \$D(X),'F,\$D(DA(1)),\$E(X,2)'=\$E(\$P(^V

A(200,DA(1),0),"^")) D EN^DDIOL(\$C(7)\_"DEA number doesn't match provider's last

name. Please verify the information.") D VALN1P"

XPDSQA("XUSER3","IO",27,"VALN2DEA +3")=" I \$D(X) I \$L(X)\>9 K X D EN^DDIOL(\$C(7)\_

"Exceeds maximum length (9).")"

XPDSQA("XUSER3","IO",28,"VALN2DEA +4")=" I \$D(X) I \$L(X)\<9 K X D EN^DDIOL(\$C(7)\_

"Less than minimum length (9).")"

XPDSQA("XUSER3","IO",29,"VALN2DEA +5")=" I \$D(X) I '(X?2U7N) K X D EN^DDIOL(\$C(7

)\_"Invalid format. Must be 2 upper case letters followed by 7 digits.")"

XPDSQA("XUSER3","IO",32,"VALN2DEA +8")=" I \$D(X),'\$\$DEANUM(X) D EN^DDIOL(\$C(7)\_"

DEA number is invalid. Please check the number entered.") K X"

XPDSQA("XUSER3","IO",50,"SUFCHK +4")=" I \$D(^VA(200,"F",NPDEATXT,X)) D EN^DDIOL(

\$C(7)\_"That Suffix is in use. ","","!,?5") S RESPONSE=1"

XPDSQA("XUSER3","^(",14,"VALN1DEA +8")=" I \$D(X),'F,\$D(DA(1)),\$D(^VA(200,"PS4",X

)),\$O(^(X,0))'=DA(1) D EN^DDIOL(\$C(7)\_"Provider DEA number is already associated

to another profile. Please check the number entered.") K X"

<u>Figure 30</u> shows the results when running the KIDS Build Analyzer - Full SQA Search option and answering NO to the following prompt:

“Do you want to include a section that displays the component descriptions and text found in routines? NO//” <span class="mark">NO</span>

<span id="_Ref127883584" class="anchor"></span>Figure 30: Running the KIDS Build Analyzer - Full SQA Search Option: Print Report Action—System Prompts and User Entries

Select Utilities \<TEST ACCOUNT\> Option: <span class="mark">XPDANLYZ MAIN MENU \<Enter\></span> Build Analyzer Main Menu

1 KIDS Build Analyzer

2 Delete Build Analyzer Text Files

<span class="mark">3 KIDS Build Analyzer - Full SQA Search</span>

Select Build Analyzer Main Menu \<TEST ACCOUNT\> Option: <span class="mark">3 \<Enter\></span> KIDS Build Analyzer - Full SQA Search

This tool is used to analyze and list the components of a build to identify adherence to standards and best practices.

Select Build Name: <span class="mark">XU\*8\*688 \<Enter\></span> KERNEL

Namespace: XU

Package: KERNEL

Do you want to include a section that displays the component descriptions

and text found in routines? NO// <span class="mark">NO</span>

Analysis Results Display Choices:

<span class="mark">1. Print the Report</span>

2\. Create the Report in .TXT Files

3\. Send the Report in MailMan Messages

Select number: (1-3): <span class="mark">1 \<Enter\></span> . . .

Print Analysis to which Device: HOME// <span class="mark">;;9999999</span> TELNET PORT Right Margin:

80// <span class="mark">\<Enter\></span>

<span id="_Ref135747321" class="anchor"></span>Figure 31: Reviewing the Print the Report Action—Output from the KIDS Build Analyzer - Full SQA Search Option

XU\*8.0\*688 BUILD OVERVIEW Feb 01, 2023@09:33:36

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*688 \*\*\*

-------------------------------------------------------------------------------

FILE:

NEW PERSON (#200)

Field Issues:

\* DETOX CALCULATED (#9001) - Field Description missing.

\* DETOX CALCULATED (#9001) - Help Prompt missing.

DEA BUSINESS ACTIVITY CODES (#8991.8)

No issues noted.

DEA NUMBERS (#8991.9)

No issues noted.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

XUSER3 ;ISF/RWF - New Person File Utilities ;02/01/2022

;;8.0;KERNEL;\*\*688\*\*;Jul 10, 1995;Build 58

;;Per VA Directive 6402, this routine should not be modified.

\* Date of Last ^XINDEX: JAN 24, 2023

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

ALL ^XTMP calls have zero nodes defined in this build's routines

XUSER3

IO ...........................................................................

VALN1DEA +4 I \$D(X) I \$L(X)\>9 K X D EN^DDIOL(\$C(7)\_"Exceeds maximum length

(9).")

VALN1DEA +5 I \$D(X) I \$L(X)\<9 K X D EN^DDIOL(\$C(7)\_"Less than minimum

length (9).")

VALN1DEA +6 I \$D(X) I '(X?2U7N) K X D EN^DDIOL(\$C(7)\_"Invalid format. Must

be 2 upper case letters followed by 7 digits.")

VALN1DEA +8 I \$D(X),'F,\$D(DA(1)),\$D(^VA(200,"PS4",X)),\$O(^(X,0))'=DA(1) D

EN^DDIOL(\$C(7)\_"Provider DEA number is already associated to

another profile. Please check the number entered.") K X

VALN1DEA +9 I \$D(X),'\$\$DEANUM(X) D EN^DDIOL(\$C(7)\_"DEA number is invalid.

Please check the number entered.") K X

VALN1DEA +10 I \$D(X),'F,\$D(DA(1)),\$E(X,2)'=\$E(\$P(^VA(200,DA(1),0),"^")) D

EN^DDIOL(\$C(7)\_"DEA number doesn't match provider's last name.

Please verify the information.") D VALN1P

VALN2DEA +3 I \$D(X) I \$L(X)\>9 K X D EN^DDIOL(\$C(7)\_"Exceeds maximum length

(9).")

VALN2DEA +4 I \$D(X) I \$L(X)\<9 K X D EN^DDIOL(\$C(7)\_"Less than minimum

length (9).")

VALN2DEA +5 I \$D(X) I '(X?2U7N) K X D EN^DDIOL(\$C(7)\_"Invalid format. Must

be 2 upper case letters followed by 7 digits.")

VALN2DEA +8 I \$D(X),'\$\$DEANUM(X) D EN^DDIOL(\$C(7)\_"DEA number is invalid.

Please check the number entered.") K X

SUFCHK +4 I \$D(^VA(200,"F",NPDEATXT,X)) D EN^DDIOL(\$C(7)\_"That Suffix is

in use. ","","!,?5") S RESPONSE=1

^( ...........................................................................

VALN1DEA +8 I \$D(X),'F,\$D(DA(1)),\$D(^VA(200,"PS4",X)),\$O(^(X,0))'=DA(1) D

EN^DDIOL(\$C(7)\_"Provider DEA number is already associated to

another profile. Please check the number entered.") K X

\*\* Analysis Complete \*\*

Press \<Enter\> or '^' to exit:

The KIDS Build Analyzer - Full SQA Search \[XPDANLYZ_SQA\] option (see <u>Figure 31</u>) provides more SQA data checks than the KIDS Build Analyzer \[XPDANLYZ\] option and selecting YES at the “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” prompt (see <u>Figure 10</u>).

The following are examples show the different output for the same build using either the KIDS Build Analyzer \[XPDANLYZ\] option and selecting YES at the “Do you want to include a section that displays the routine lines containing specific code references reviewed on the SQA checklist? NO//” prompt or using the KIDS Build Analyzer - Full SQA Search \[XPDANLYZ_SQA\] option.

<span id="_Toc136406999" class="anchor"></span>Figure 32: Sample Output—KIDS Build Analyzer - Full SQA Search Option: ZZDAVE\*1\*2 Build

ZZDAVE\*1.0\*2 BUILD OVERVIEW May 24, 2023@12:36:57

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Not Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

> **WARNING:** Build not set to track package nationally

Please validate that is correct.

> **WARNING:** The PACKAGE FILE LINK is missing.

This should be defined for a national VISTA product build.

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build ZZDAVE\*1.0\*2 \*\*\*

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

ZZDSTEST ;

K ^SRF K ^SRF(0) K ^SRAFY(139.9) K ^SRAFY(139.9,0)

\* ZZDSTEST is not in the Package namespace.

\* Date ^XINDEX last run was not found.

\* Missing current patch number on second line.

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

ALL ^XTMP calls have zero nodes defined in this build's routines

ZZDSTEST

K @ ..........................................................................

ZZDSTEST +2 K @^KILLME

ZZDSTEST +3 K @KILLME

K ^ ..........................................................................

ZZDSTEST +1 K ^SRF K ^SRF(0) K ^SRAFY(139.9) K ^SRAFY(139.9,0)

ZZDSTEST +4 K ^TMP(XXX,\$J) K ^UTILITY("SOMETHING")

^TMP .........................................................................

ZZDSTEST +4 K ^TMP(XXX,\$J) K ^UTILITY("SOMETHING")

^UTILITY .....................................................................

ZZDSTEST +4 K ^TMP(XXX,\$J) K ^UTILITY("SOMETHING")

\*\* Analysis Complete \*\*

<span id="_Toc136407000" class="anchor"></span>Figure 33: Sample Output—KIDS Build Analyzer Option with SQA Option: ZZDAVE\*1\*2 Build

ZZDAVE\*1.0\*2 BUILD OVERVIEW May 24, 2023@12:30:23

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Not Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

> **WARNING:** Build not set to track package nationally

Please validate that is correct.

> **WARNING:** The PACKAGE FILE LINK is missing.

This should be defined for a national VISTA product build.

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build ZZDAVE\*1.0\*2 \*\*\*

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

ZZDSTEST ;

K ^SRF K ^SRF(0) K ^SRAFY(139.9) K ^SRAFY(139.9,0)

\* ZZDSTEST is not in the Package namespace.

\* Date ^XINDEX last run was not found.

\* Missing current patch number on second line.

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

These ^TMP calls have kill statements within the included routines:

^TMP(XXX,\$J

ZZDSTEST ZZDSTEST +4

All ^TMP calls have at least one kill statement in this build's routines.

ALL ^XTMP calls have zero nodes defined in this build's routines

ZZDSTEST

K @ ..........................................................................

ZZDSTEST +2 K @^KILLME

ZZDSTEST +3 K @KILLME

K ^ ..........................................................................

ZZDSTEST +1 K ^SRF K ^SRF(0) K ^SRAFY(139.9) K ^SRAFY(139.9,0)

^UTILITY .....................................................................

ZZDSTEST +4 K ^TMP(XXX,\$J) K ^UTILITY("SOMETHING")

\*\* Analysis Complete \*\*

<span id="_Toc136407001" class="anchor"></span>Figure 34: Sample Output—KIDS Build Analyzer - Full SQA Search Option: XU\*8.0\*782 Build

XU\*8\*782 BUILD OVERVIEW May 25, 2023@14:11:17

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Not Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8\*782 \*\*\*

-------------------------------------------------------------------------------

OPTION:

XPD UTILITY

No issues noted.

XPDANLYZ

No issues noted.

XPDANLYZ_DEL

No issues noted.

XPDANLYZ_SQA

No issues noted.

XPDANLYZ MAIN MENU

\* PACKAGE field (#12) missing.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

XPDANLYZ1 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ2 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ3 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ4 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ5 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ6 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

General ^XTMP Notes

These ^XTMP calls have zero nodes defined in this build's included routines:

Routine: XPDANLYZ5 ^XTMP(".E1",0)=".E1(1"^",1"\_U\_").E D

These ^XTMP calls have no zero nodes defined in this build's included routines

Routine: XPDANLYZ5 ^XTMP("

Routine: XPDANLYZ5 ^XTMP("\_\$P(XRRR

XPDANLYZ1

% ............................................................................

START +3 N X,XPDATE,XPDLINE,XPDBN,%,%H,%I D NOW^%DTC S XPDATE=X,XPDIS=1

PME +1 I XPDIS=1 S END=0 N POP,IO,IOP,%ZIS,ZTIO D G:POP X1

PME +2 . W ! S %ZIS("A")="Print Analysis to which Device: " S %ZIS="

MQ" D ^%ZIS Q:POP Q:'\$G(ZTIO)'\]""

PME +7 .. D ^%ZTLOAD

PME +11 .. D HOME^%ZIS

PME +12 .. K %ZIS

X1 +0 X1 D ^%ZISC S:\$D(ZTQUEUED) ZTREQ="@" K DIR,DIC,XPDFARR,FLDARR,

XPDRC,Y W @IOF Q

IO ...........................................................................

START +0 START(XPDRC) ; OPTION XPDANLYZ which passes XPDRC=4 an XPDRC=5

to run initially for build

START +5 I XPDRC=6 S XPDRC=4,XTOG=1 ;SHOW SQA LINES IN ANALYSIS

SECTION (NEEDS OPTION CREATED IF WANTED)

START +6 I XPDRC=1 S XPDLINE="File Analysis" D FILENUM^XPDANLYZ4 ;

THESE THREE HAVE NOT BEEN USED RECENTLY. IF WANTED, WILL NEED

CODE CHECKED AND OPTIONS ADDED

PME +1 I XPDIS=1 S END=0 N POP,IO,IOP,%ZIS,ZTIO D G:POP X1

PME +2 . W ! S %ZIS("A")="Print Analysis to which Device: " S %ZIS="

MQ" D ^%ZIS Q:POP Q:'\$G(ZTIO)'\]""

PME +3 . I \$D(IO("Q")) D ;queue the report

PME +13 . I \$D(IO("Q")) K IO("Q") S END=1 Q

PME +16 . U IO

PME +17 . I \$E(IOST,1,2)="C-" W @IOF ;sending to screen, so clear

screen first

PNT +20 ... S:XPDCOMP="OPTION" XPDW(XPDCNT)="Option Description" S:

XPDCOMP="REMOTE PROCEDURE" XPDW(XPDCNT)="RPC Description" S:

XPDCOMP="MAIL GROUP" XPDW(XPDCNT)="Mail Group Description"

PNT +22 ... I XPDARR(XPDCOMP,XPDNUM,"DESCRIPT")="Yes" N II S II=0 F S

II=\$O(XPDARR(XPDCOMP,XPDNUM,"DESCRIPTION",II)) Q:'II S XPDCNT=

XPDCNT+1,XPDW(XPDCNT)=XPDARR(XPDCOMP,XPDNUM,"DESCRIPTION",II)

PNT +23 ... I XPDARR(XPDCOMP,XPDNUM,"DESCRIPT")="No" S XPDCNT=XPDCNT+1,

XPDW(XPDCNT)=" DESCRIPTION missing."

PNT +42 . N RR S RR=0 F S RR=\$O(XPDW(RR)) Q:'RR W !,XPDW(RR) I (\$Y+5)

\>IOSL S TMPT=XPDLINE\_" - (continued)" D HDR(TMPT) Q:END

PNT +48 . N RR S RR=0 F S RR=\$O(XPBA1(RR)) Q:'RR W !,XPBA1(RR) I \$E(

IOST,1,2)="C-",(\$Y+5)\>IOSL S LNUM=\$O(XPDHR(RR+2),-1),TMPT=

XPDARR("BUILD",XPDBB,"NAME")\_" - "\_XPDHR(LNUM)\_" (cont.)" D

HDR(TMPT) Q:END

PNT +50 . I ('XPDR)&('XPQR) S END=1 Q ;ONLY WANT TO SEE ANLYSIS

SECTION

PNT +53 .. N LL S LL=0 F S LL=\$O(XPMM(LL)) Q:'LL W !,XPMM(LL) I \$E(

IOST,1,2)="C-",(\$Y+5)\>IOSL N AA S AA=LL,AA=\$O(XPDROUT(AA),-1),

TMPT=XPDARR("BUILD",XPDBB,"NAME")\_" - SQA LINE REVIEW, "\_

XPDROUT(\$G(AA,0))\_" (cont.)" D HDR(TMPT) Q:END

PNT +55 .. W !,XPDMM(TTT) I \$E(IOST,1,2)="C-",(\$Y+5)\>IOSL S TMPT=

XPDARR("BUILD",XPDBB,"NAME")\_" - TEXT REVIEW (cont.)" D HDR(

TMPT) Q:END

PNT +70 . I ('XPDR)&('XPQR) S END=1 Q ;ONLY WANT TO SEE ANLYSIS

SECTION

PNT +86 . I ('XPDR)&('XPQR) S END=1 ;ONLY WANT TO SEE ANLYSIS SECTION

X2 +0 X2 I \$E(IOST,1,2)="C-" D

X1 +0 X1 D ^%ZISC S:\$D(ZTQUEUED) ZTREQ="@" K DIR,DIC,XPDFARR,FLDARR,

XPDRC,Y W @IOF Q

HDR +1 I \$E(IOST,1,2)="C-" D G:END X1

HDR +7 I \$E(IOST,1,2)="C-" W @IOF W !,HTXT,\$\$RJ^XLFSTR(\$\$FMTE^XLFDT(

XPDATE),79-\$L(HTXT)," ")

\<\>\<\>\<\>

XPDANLYZ2

\$I ...........................................................................

SQA +7 S XPDARRR("\$I",RR,0)=""

RLINES +35 ... I (XPD1="\$I"),'XPDIS2,RTN(K,0)\[XPD1 S TCHK=\$\$MSQA^

XPDANLYZ5(RTN(K,0),XPD1) Q:'TCHK

% ............................................................................

XREF +9 .... I JJ=\$P(^DD(LL,MM,1,PP,0),"^",2),'\$D(^DD(LL,MM,1,PP,"%D"))

S XPDARR("FILE",FXX,MM,"WARNING","XREF")=\$P(^DD(LL,MM,1,PP,0),

"^",2)\_" cross-reference ("\_RSF\_" \#"\_MM\_") - DESCRIPTION

missing."

SQA +6 S XPDARRR("%",RR,0)=""

RLINES +13 . N X S X=ROU X ^%ZOSF("TEST") Q:'\$T

RLINES +14 . K RTN S XCNP=0,DIF="RTN(" X ^%ZOSF("LOAD")

RLINES +33 ... I (XPD1="%"),'XPDIS2,RTN(K,0)\[XPD1 S TCHK=\$\$MSQA^XPDANLYZ5(

RTN(K,0),XPD1) Q:'TCHK ;\$\$GCHK^XPDANLYZ5(RTN(K,0),XPD1) D

RSPELL +1 N X S X=ROU X ^%ZOSF("TEST") Q:'\$T

RSPELL +2 K RTN S XCNP=0,DIF="RTN(" X ^%ZOSF("LOAD")

//// .........................................................................

SQA +1 S XPDARRR("////",RR,0)=""

DIC(0) .......................................................................

G1 +1 . N DIC,Y S DIC=19,DIC(0)="QEAM",DIC("A")="Select individual

options by name: "

RPC1 +1 . N DIC S DIC=8994,DIC(0)="QEAM",DIC("A")="Select individual

RPCs by name: "

SQA +2 S XPDARRR("DIC(0)",RR,0)=""

RLINES +36 ... I (XPD1="DIC(0)"),'XPDIS2,RTN(K,0)\[XPD1 S TCHK=\$\$MSQA^

XPDANLYZ5(RTN(K,0),XPD1) Q:'TCHK

RSPELL +12 ... Q:TMP\[("DIC="\_\$C(34)\_XTXT) Q:TMP\[("DIC(0)="\_\$C(34)\_XTXT)

Q:TMP\[("DR="\_\$C(34)\_XTXT) Q:TMP\[("DIE="\_\$C(34)\_XTXT) Q:TMP\[("

DIC(""S"")="\_\$C(34)\_XTXT)

IO ...........................................................................

XREF +9 .... I JJ=\$P(^DD(LL,MM,1,PP,0),"^",2),'\$D(^DD(LL,MM,1,PP,"%D"))

S XPDARR("FILE",FXX,MM,"WARNING","XREF")=\$P(^DD(LL,MM,1,PP,0),

"^",2)\_" cross-reference ("\_RSF\_" \#"\_MM\_") - DESCRIPTION

missing."

OPTME +1 N XPDOARR,KK S KK=0 ;XPDRC=2 IS OPTION

G1 +5 . I \$G(Y)\]"" S XPDOARR(\$P(Y,"^"))=\$P(Y,"^",2),KK=KK+1 ;OPTION

ien ^ NAME

G1 +16 . N JJ S JJ=0 F S JJ=\$O(XPDOARR(JJ)) Q:'JJ W !,?5,XPDOARR(JJ)

I (\$Y+5)\>IOSL D HDR^XPDANLYZ1("Options (continued): ") Q:END

OCHK +0 OCHK(XPDORR) ;setting up information to check OPTIONS ENTRY/

EXIT for files and routines.

OCHK +3 .. S XPDARR("OPTION",JJ,"NAME")=XPDORR(JJ)

OCHK +4 .. I '\$D(TARR(19,XPDIENS,3.5)) S XPDARR("OPTION",JJ,"DESCRIPT")

="No",XPDARR("OPTION",JJ,"WARNING","DESCRIPTION")="DESCRIPTION

field (#3.5) missing."

OCHK +5 .. I \$D(TARR(19,XPDIENS,3.5)) S XPDARR("OPTION",JJ,"DESCRIPT")=

"Yes" N LL S LL=0 F S LL=\$O(TARR(19,XPDIENS,3.5,LL)) Q:'LL S

XPDARR("OPTION",JJ,"DESCRIPTION",LL)=TARR(19,XPDIENS,3.5,LL)

OCHK +6 .. I \$D(TARR(19,XPDIENS,1)) S XPDARR("OPTION",JJ,"Menu")=TARR(

19,XPDIENS,1)

OCHK +7 .. I '\$D(TARR(19,XPDIENS,1)) S XPDARR("OPTION",JJ,"WARNING","

MENU TXT")="MENU TEXT field (#1) missing."

OCHK +8 .. I '\$D(TARR(19,XPDIENS,12)) S XPDARR("OPTION",JJ,"WARNING","

PKG")="PACKAGE field (#12) missing."

OCHK +9 .. I \$D(TARR(19,XPDIENS,12)) S XPDARR("OPTION",JJ,"PKG")=TARR(

19,XPDIENS,12)

OCHK +16 S XPDCS("OPTION")=19

RPC1 +15 . N JJ S JJ=0 F S JJ=\$O(XPDCARR(JJ)) Q:'JJ W !,?5,XPDCARR(JJ)

I (\$Y+5)\>IOSL D HDR^XPDANLYZ1("RPC (continued): ") Q:END

RPC2 +5 .. I '\$D(TARR(8994,XPDIENS,"DESCRIPTION")) S XPDARR("REMOTE

PROCEDURE",JJ,"DESCRIPT")="No",XPDARR("REMOTE PROCEDURE",JJ,"

WARNING","DESCRIPTION")="DESCRIPTION field (#1) missing."

RPC2 +6 .. I \$D(TARR(8994,XPDIENS,"DESCRIPTION")) S XPDARR("REMOTE

PROCEDURE",JJ,"DESCRIPT")="Yes" N LL S LL=0 F S LL=\$O(TARR(

8994,XPDIENS,"DESCRIPTION",LL)) Q:'LL S XPDARR("REMOTE

PROCEDURE",JJ,"DESCRIPTION",LL)=TARR(8994,XPDIENS,"DESCRIPTION"

,LL)

RPC2 +8 .. I \$D(TARR(8994,XPDIENS,"RETURN VALUE TYPE")),'\$D(TARR(8994,

XPDIENS,"RETURN PARAMETER DESCRIPTION")) S XPDARR("REMOTE

PROCEDURE",JJ,"WARNING","RETURN DESCRIPTION")="RPC RETURN

DESCRIPTION field (#3) missing."

RPC2 +11 ... N MM F MM=1:1:XPDIP I '\$D(TARR(8994.02,MM\_","\_XPDIENS,"

DESCRIPTION")) S XPDARR("REMOTE PROCEDURE",JJ,"WARNING","INPUT

DESCRIPTION")="RPC Input Description for "\_TARR(8994.02,MM\_","\_

XPDIENS,"INPUT PARAMETER")\_" missing."

SQA +13 S XPDARRR("IO",RR,0)=""

COMP1 +1 S XPDCS("APPLICATION ACTION")=1.61

COMP1 +6 S XPDCS("FUNCTION")=.5

COMP1 +8 S XPDCS("HL7 APPLICATION PARAMETER")=771

COMP1 +9 S XPDCS("HLO APPLICATION REGISTRY")=779.2

COMP1 +15 S XPDCS("OPTION")=19

COMP1 +16 S XPDCS("PARAMETER DEFINITION")=8989.51

COMP1 +19 S XPDCS("POLICY FUNCTION")=1.62

COMP1 +26 S XPDCS("XULM LOCK DICTIONARY")=8993

RLINES +34 ... I (XPD1="IO"),'XPDIS2,RTN(K,0)\[XPD1 S TCHK=\$\$MSQA^

XPDANLYZ5(RTN(K,0),XPD1) Q:'TCHK

RSPELL +10 ... I CLTXT\]"" I \$L(XTXT)\>(2\*\$L(CLTXT)) Q ;NUMBER,PUNCUATION,

FEW LETTERS

K @ ..........................................................................

SQA +11 S XPDARRR("K @",RR,0)=""

K ^ ..........................................................................

SQA +9 S XPDARRR("K ^",RR,0)=""

FMSG +2 K ^TMP("XPDEM",\$J)

RLINES +32 ... I (XPD1="K ^"),'XPDIS2,RTN(K,0)\[XPD1 S TCHK=\$\$KCHK^

XPDANLYZ5(RTN(K,0),XPD1) Q:TCHK'=3

U= ...........................................................................

SQA +8 S XPDARRR("U=",RR,0)=""

RLINES +2 N TCNT S (JJ,TCNT)=0 F S JJ=\$O(XPDARR("BUILD",XPDBIEN,"

ROUTINE",JJ)) Q:'JJ S ROU=XPDARR("BUILD",XPDBIEN,"ROUTINE",JJ)

D

RLINES +37 ... I XPD1="U=",'XPDIS2,(RTN(K,0)\["U=""^""")!(RTN(K,0)'?.E1P1"

U=") Q

^( ...........................................................................

SQA +12 S XPDARRR("^(",RR,0)=""

^TMP .........................................................................

SQA +4 S XPDARRR("^TMP",RR,0)=""

FMSG +2 K ^TMP("XPDEM",\$J)

FMSG +4 D LISTMSGS^XMXAPIB(XPDUZ,"\*","SUBJ;DATE;F","B",,,.XMCRIT,"^TMP(

""XPDEM"",\$J)")

FMSG +5 I \$D(^TMP("XPDEM",\$J)) D

FMSG +6 . N JKL,XPDNIEN S JKL=\$O(^TMP("XPDEM",\$J,"XMLIST",0)) Q:'\$G(

JKL) S XPDNIEN=^TMP("XPDEM",\$J,"XMLIST",JKL)

RLINES +31 ... I XPD1="^TMP",'XPDIS2,RTN(K,0)\[XPD1 D TMP^XPDANLYZ5(RTN(K,

0)) I 'XPDIS2 Q:TCHK

^UTILITY .....................................................................

SQA +3 S XPDARRR("^UTILITY",RR,0)=""

^XTMP ........................................................................

SQA +5 S XPDARRR("^XTMP",RR,0)=""

RLINES +30 ... I XPD1="^XTMP",RTN(K,0)\[XPD1 D TMPX^XPDANLYZ5(RTN(K,0)) I '

XPDIS2 Q:TCHK ;TMPX^ZZSRABA

\<\>\<\>\<\>

XPDANLYZ3

% ............................................................................

CEE +19 ... N JKL,JS S JS=1,TMP="" I \$E(TMP1,1)="%" S TMP="%",JS=2

IO ...........................................................................

OPT +1 W @IOF,"Select product to perform a basic review of components.

",!

NSST +6 . I XPDNOM="APPLICATION ACTION" S XPDCIEN=\$O(^DIAC(1.61,"B",

XPDNAM1,0))

NSST +7 . I XPDNOM="OPTION" S XPDCIEN=\$O(^DIC(19,"B",XPDNAM1,0))

NSST +14 . I XPDNOM="FUNCTION" S XPDCIEN=\$O(^DD("FUNC","B",XPDNAM1,0))

NSST +17 . I XPDNOM="HL7 APPLICATION PARAMETER" S XPDCIEN=\$O(^HL(771,"B"

,XPDNAM1,0))

NSST +18 . I XPDNOM="HLO APPLICATION REGISTRY" S XPDCIEN=\$O(^HLD(779.2,"

B",XPDNAM1,0))

NSST +22 . I XPDNOM="PARAMETER DEFINITION" S XPDCIEN=\$O(^XTV(8989.51,"B"

,XPDNAM1,0))

NSST +25 . I XPDNOM="POLICY FUNCTION" S XPDCIEN=\$O(^DIAC(1.62,"B",

XPDNAM1,0))

NSST +29 . I XPDNOM="XULM LOCK DICTIONARY" S XPDCIEN=\$O(^XLM(8993,"B",

XPDNAM1,0))

NSST +37 . I XPDNOM="OPTION" D OCHK^XPDANLYZ2(.XPDCARR) D CEE(.XPDCARR)

Q

NSST +44 . D SKEY^XPDANLYZ3(.XPDCARR,XPDNOM,XPDX1,"DESCRIPTION") ;NAME

ARRAY, COMPONENT NAME, COMPONENT FILE NUMBER

TROU +4 . N TARR S XPDIENS=JJ\_"," D GETS^DIQ(ZZ,XPDIENS,"\*","

DESCRIPTION;ROUTINE INVOKED","TARR")

TROU +5 . I '\$D(TARR) S XPDARR(XPDCX,JJ,"DESCRIPT")="No",XPDARR(ZZ,JJ,"

WARNING","DESCRIPTION")="DESCRIPTION missing."

TROU +7 .. I '\$D(TARR(ZZ,XPDIENS,"DESCRIPTION")) S XPDARR(XPDCX,JJ,"

DESCRIPT")="No",XPDARR(XPDCX,JJ,"WARNING","DESCRIPTION")="

DESCRIPTION missing."

TROU +8 .. I \$D(TARR(ZZ,XPDIENS,"DESCRIPTION")) S XPDARR(XPDCX,JJ,"

DESCRIPT")="Yes" N LL S LL=0 F S LL=\$O(TARR(ZZ,XPDIENS,"

DESCRIPTION",LL)) Q:'LL S XPDARR(XPDCX,JJ,"DESCRIPTION",LL)=

TARR(ZZ,XPDIENS,"DESCRIPTION",LL)

BULL +4 . N TARR S XPDIENS=JJ\_"," D GETS^DIQ(3.6,XPDIENS,"DESCRIPTION",

"NR","TARR")

BULL +5 . I '\$D(TARR) S XPDARR("BULLETIN",JJ,"DESCRIPT")="No",XPDARR("

BULLETIN",JJ,"WARNING","DESCRIPTION")="DESCRIPTION field (#6)

missing."

BULL +7 .. I '\$D(TARR(3.6,XPDIENS,"DESCRIPTION")) S XPDARR("BULLETIN",

JJ,"DESCRIPT")="No",XPDARR("BULLETIN",JJ,"WARNING","

DESCRIPTION")="DESCRIPTION field (#6) missing."

BULL +8 .. I \$D(TARR(3.6,XPDIENS,"DESCRIPTION")) S XPDARR("BULLETIN",

JJ,"DESCRIPT")="Yes" N LL S LL=0 F S LL=\$O(TARR(3.6,XPDIENS,"

DESCRIPTION",LL)) Q:'LL S XPDARR("BULLETIN",JJ,"DESCRIPTION",

LL)=TARR(3.6,XPDIENS,"DESCRIPTION",LL)

CEE +0 CEE(XPDOPTEE) ;CHECK OPTIONS ENTRY/EXIT FOR FILES AND ROUTINES

CEE +6 .. N XPLOC S XPLOC=\$S(XPDTST=ENT:"ENTRY ACTION field (#20):",

XPDTST=EXT:"EXIT ACTION field (#15):",1:"Entry/Exit field:")

MG1 +0 MG1(XPDMARR) ;GET MAIL GROUP DESCRIPTION

MG1 +4 . N TARR S XPDIENS=JJ\_"," D GETS^DIQ(3.8,XPDIENS,"DESCRIPTION",

"NR","TARR")

MG1 +5 . I '\$D(TARR) S XPDARR("MAIL GROUP",JJ,"DESCRIPT")="No",XPDARR(

"MAIL GROUP",JJ,"WARNING","DESCRIPTION")="MAIL GROUP "\_XPDMARR(

JJ)\_"("\_JJ\_") - DESCRIPTION field (#3) missing."

MG1 +7 .. I '\$D(TARR(3.8,XPDIENS,"DESCRIPTION")) S XPDARR("MAIL GROUP"

,JJ,"DESCRIPT")="No",XPDARR("MAIL GROUP",JJ,"WARNING","

DESCRIPTION")="MAIL GROUP "\_XPDMARR(JJ)\_"("\_JJ\_") -

DESCRIPTION field (#3) missing."

MG1 +8 .. I \$D(TARR(3.8,XPDIENS,"DESCRIPTION")) S XPDARR("MAIL GROUP",

JJ,"DESCRIPT")="Yes" N LL S LL=0 F S LL=\$O(TARR(3.8,XPDIENS,"

DESCRIPTION",LL)) Q:'LL S XPDARR("MAIL GROUP",JJ,"DESCRIPTION"

,LL)=TARR(3.8,XPDIENS,"DESCRIPTION",LL)

DIA +5 . I '\$D(TARR) S XPDARR("DIALOG",JJ,"DESCRIPT")="No",XPDARR("

DIALOG",JJ,"WARNING","DESCRIPTION")="DIALOG "\_XPDIA(JJ)\_"("\_JJ\_

") - TEXT field (#4) missing."

DIA +7 .. I '\$D(TARR(.84,XPDIENS,"TEXT")) S XPDARR("DIALOG",JJ,"

DESCRIPT")="No",XPDARR("DIALOG",JJ,"WARNING","DESCRIPTION")="

DIALOG "\_XPDIA(JJ)\_"("\_JJ\_") - TEXT field (#4) missing."

DIA +8 .. I \$D(TARR(.84,XPDIENS,"TEXT")) S XPDARR("DIALOG",JJ,"

DESCRIPT")="Yes" N LL S LL=0 F S LL=\$O(TARR(.84,XPDIENS,"TEXT"

,LL)) Q:'LL S XPDARR("DIALOG",JJ,"DESCRIPTION",LL)=TARR(.84,

XPDIENS,"TEXT",LL)

SKEY +0 SKEY(XPDGC,XPDCX,XPDXN,DES) ;GENERIC COMPONENT INFO RECEIVING:

NAME ARRAY, COMPONENT NAME, COMPONENT FILE NUMBER, DES=

DESCRIPTION OR TEXT

SKEY +5 . I '\$D(TARR) S XPDARR(XPDCX,JJ,"DESCRIPT")="No",XPDARR(XPDCX,

JJ,"WARNING","DESCRIPTION")=DES\_" missing."

SKEY +7 .. I '\$D(TARR(XPDXN,XPDIENS,DES)) S XPDARR(XPDCX,JJ,"DESCRIPT")

="No",XPDARR(XPDCX,JJ,"WARNING","DESCRIPTION")=DES\_" missing."

SKEY +8 .. I \$D(TARR(XPDXN,XPDIENS,DES)) S XPDARR(XPDCX,JJ,"DESCRIPT")=

"Yes" N LL S LL=0 F S LL=\$O(TARR(XPDXN,XPDIENS,DES,LL)) Q:'LL

S XPDARR(XPDCX,JJ,"DESCRIPTION",LL)=TARR(XPDXN,XPDIENS,DES,LL)

PDESC +6 I Y D PRNTME("DESCRIPTION")

PRNTME +2 W @IOF

PRNTME +5 I XPDRC=2 S XPDTYP="OPTION" W "Option Descriptions:"

PM1 +3 . I PTRM="DESCRIPTION",XPDARR(XPDTYP,TT,"DESCRIPT")="No" W !,

XPDTYP\_" missing." Q

PM1 +5 . I \$D(XPDARR("FILE",TT,"FIELD DESCRIPTIONS")) D

PM1 +6 .. N UU,PP S (PP,UU)=0 F S UU=\$O(XPDARR(XPDTYP,TT,UU)) Q:'UU

F S PP=\$O(XPDARR(XPDTYP,TT,UU,"DESCRIPTION",PP)) Q:'PP W !,

XPDARR(XPDTYP,TT,UU,"DESCRIPTION",PP)

MMT +7 .. N QQ S QQ=0 F S QQ=\$O(XPDARR(XPDTYP,TT,"DESCRIPTION",QQ))

Q:'QQ S XCNT=XCNT+1,XPDMM(XCNT)=XPDARR(XPDTYP,TT,"DESCRIPTION"

,QQ)

MMT +11 .. I \$D(XPDARR("FILE",TT,"FIELD DESCRIPTIONS")) D

MMT +12 ... N UU,PP S (PP,UU)=0 F S UU=\$O(XPDARR(XPDTYP,TT,UU)) Q:'UU

F S PP=\$O(XPDARR(XPDTYP,TT,UU,"DESCRIPTION",PP)) Q:'PP S

XCNT=XCNT+1,XPDMM(XCNT)=XPDARR(XPDTYP,TT,UU,"DESCRIPTION",PP)

U= ...........................................................................

PM1 +6 .. N UU,PP S (PP,UU)=0 F S UU=\$O(XPDARR(XPDTYP,TT,UU)) Q:'UU

F S PP=\$O(XPDARR(XPDTYP,TT,UU,"DESCRIPTION",PP)) Q:'PP W !,

XPDARR(XPDTYP,TT,UU,"DESCRIPTION",PP)

MMT +9 ... N UU,PP,YY S (UU,PP)=" ",YY=-1 F S UU=\$O(XPDARR("FILE",TT,

"FIELD",UU)) Q:UU'\]"" S XCNT=XCNT+1,XPDMM(XCNT)="" D

MMT +12 ... N UU,PP S (PP,UU)=0 F S UU=\$O(XPDARR(XPDTYP,TT,UU)) Q:'UU

F S PP=\$O(XPDARR(XPDTYP,TT,UU,"DESCRIPTION",PP)) Q:'PP S

XCNT=XCNT+1,XPDMM(XCNT)=XPDARR(XPDTYP,TT,UU,"DESCRIPTION",PP)

\<\>\<\>\<\>

XPDANLYZ4

IO ...........................................................................

FSEQ +3 D FILE^DID(FXX,"","NAME;GLOBAL NAME;DESCRIPTION;DISTRIBUTION

PACKAGE","XPDFARR")

FSEQ +13 N XT S XT=\$O(XPDFARR("DESCRIPTION"," "),-1) S:'\$G(XT) XT=0

FSEQ +14 N JJ S JJ=0 F S JJ=\$O(XPDFARR("DESCRIPTION",JJ)) Q:'JJ S

XPDARR("FILE",FXX,"DESCRIPTION",JJ)=XPDFARR("DESCRIPTION",JJ)

FSEQ +15 I XT=0 S XPDARR("FILE",FXX,"WARNING","DESCRIPTION")="File

DESCRIPTION missing.",XPDARR("FILE",FXX,"DESCRIPT")="No"

FSEQ +16 S:XT=1 XPDARR("FILE",FXX,"WARNING","DESCRIPTION")="File has

minimal File description."

FSEQ +18 I \$G(XPDFARR("DISTRIBUTION PACKAGE"))\]"" S XPDARR("FILE",FXX,"

PKG")=XPDFARR("DISTRIBUTION PACKAGE")

FSEQ +19 I \$G(XPDFARR("DISTRIBUTION PACKAGE"))'\]"" S XPDARR("FILE",FXX,"

WARNING","PACKAGE")="DISTRIBUTION PACKAGE is not defined for

this file."

FSEQ +24 . N XPFF1 D FIELD^DID(FXX,FLD1,"","LABEL;HELP-PROMPT;

DESCRIPTION","XPFF1") Q:'\$D(XPFF1)

FSEQ +27 . I '\$D(XPFF1("DESCRIPTION")) S XPDARR("FILE",FXX,"FIELD",FNN,"

DESCRIPTION",0)=" Description missing."

FSEQ +28 . I \$D(XPFF1("DESCRIPTION")) S XPDARR("FILE",FXX,"FIELD",FNN,"

DESCRIPTION",0)=" Description:" D

FSEQ +29 .. N JJ S JJ=0 F S JJ=\$O(XPFF1("DESCRIPTION",JJ)) Q:'JJ S

XPDARR("FILE",FXX,"FIELD",FNN,"DESCRIPTION",JJ)=\$J(" ",5)\_

XPFF1("DESCRIPTION",JJ)

FSEQ +40 .. D FIELD^DID(XPDSUB,FLDNUM,"","LABEL;HELP-PROMPT;DESCRIPTION;

EXECUTABLE HELP","FLDARR") Q:'\$D(FLDARR)

FSEQ +45 .. S:FLDARR("DESCRIPTION")'\]"" XPDARR("FILE",FXX,FLDNUM,"

WARNING","DESCRIPTION")=FNAME\_" (#"\_FLDNUM\_") - Field

Description missing.",XPDARR("FILE",FXX,"FIELD",FNAME,"

DESCRIPTION",0)=" Description missing."

FSEQ +50 .. I FLDARR("DESCRIPTION")\]"" S XPDARR("FILE",FXX,"FIELD",

FNAME,"DESCRIPTION",0)=" Field Description:" D

FSEQ +51 ... N JJ S JJ=0 F S JJ=\$O(FLDARR("DESCRIPTION",JJ)) Q:'JJ S

XPDARR("FILE",FXX,"FIELD",FNAME,"DESCRIPTION",JJ)=\$J(" ",5)\_

FLDARR("DESCRIPTION",JJ)

FSEQ +52 .. I FLDARR("HELP-PROMPT")\]"",FLDARR("DESCRIPTION")\]"" D

FSEQ +54 ... N KK S KK=0 F S KK=\$O(FLDARR("DESCRIPTION",KK)) Q:'KK S

SDES=SDES\_" "\_FLDARR("DESCRIPTION",KK)

TA +4 K FLDARR D FIELD^DID(FXX1,FLDNUM,"","\*","FLDARR") ;D FIELD^

DID(FXX,FLDNUM,"","LABEL;HELP-PROMPT;DESCRIPTION","FLDARR")

TA +10 S:FLDARR("DESCRIPTION")'\]"" XPDARR("FILE",FXX,FLDNUM,"WARNING",

"DESCRIPTION")=FNN\_" - Field Description missing.",XPDARR("

FILE",FXX,"DESCRIPT")="No",XPDARR("FILE",FXX,"FIELD-WARNING")="

"

TA +11 I FLDARR("HELP-PROMPT")\]"",FLDARR("DESCRIPTION")\]"" D

TA +13 . N KK S KK=0 F S KK=\$O(FLDARR("DESCRIPTION",KK)) Q:'KK S

SDES=SDES\_" "\_FLDARR("DESCRIPTION",KK)

TA +16 I FLDARR("DESCRIPTION")\]"" D

TA +18 . S XPDARR("FILE",FXX,FLDNUM,"DESCRIPTION",.1)=""

TA +20 . S XPDARR("FILE",FXX,FLDNUM,"DESCRIPTION",.5)=XTXT_FLDNUM\_": "

\_FLDARR("LABEL"),XPDARR("FILE",FXX,"DESCRIPT")="Yes"

TA +21 . N JJ S JJ=0 F S JJ=\$O(FLDARR("DESCRIPTION",JJ)) Q:'JJ S

XPDARR("FILE",FXX,FLDNUM,"DESCRIPTION",JJ)=FLDARR("DESCRIPTION"

,JJ)

TA +23 N XXP S XXP=\$O(XPDARR("FILE",FXX,FLDNUM,"DESCRIPTION",999),-1)

I '\$G(XXP) S XXP=0

TA +24 I FLDARR("HELP-PROMPT")'\]"" S XXP=XXP+1,XPDARR("FILE",FXX,

FLDNUM,"DESCRIPTION",XXP)="HELP-PROMPT: missing."

TA +26 . S XXP=XXP+1,XPDARR("FILE",FXX,FLDNUM,"DESCRIPTION",XXP)="

HELP-PROMPT:",XXP=XXP+1,XPDARR("FILE",FXX,FLDNUM,"DESCRIPTION",

XXP)=FLDARR("HELP-PROMPT")

TA +27 I XXP\>0 S XPDARR("FILE",FXX,"FIELD DESCRIPTIONS")=""

TA +28 I FLDARR("TECHNICAL DESCRIPTION")\]"" D

TA +29 . S XXP=XXP+1,XPDARR("FILE",FXX,FLDNUM,"DESCRIPTION",XXP)="

TECHNICAL DESCRIPTION:" D

TA +30 .. N JJ S JJ=0 S JJ=\$O(FLDARR("DESCRIPTION",JJ)) Q:'JJ S XXP=

XXP+JJ,XPDARR("FILE",FXX,FLDNUM,"DESCRIPTION",XXP)=FLDARR("

TECHNICAL DESCRIPTION",JJ)

\<\>\<\>\<\>

XPDANLYZ5

\$I ...........................................................................

MSQA +0 MSQA(XLINE,SQAT) ;IO, %, \$I

MSQA +19 . I SQAT="\$I" N SP1 S SP1=(POS-SL) I (\$E(XLINE,SP1,(SL+1))="\$\$"

)!(\$E(XLINE,POS)?1A) S XT=1 Q

% ............................................................................

FILEME +7 D OPEN^%ZISH("XPBA",XPPATH,XPFNAME,"W")

FILEME +14 D CLOSE^%ZISH("XPBA")

FSHOW +1 N XPPATH,XPDEL,J,END S XPPATH=\$\$PWD^%ZISH(),END=0

FSHOW +10 S Y=\$\$LIST^%ZISH("","FILESPEC","XPFILE")

FSHOW +18 . S J=\$\$DEL^%ZISH("",\$NA(XPDEL))

FSHOW +26 I \$D(DARR) N J S J=\$\$DEL^%ZISH(XPPATH,\$NA(DARR))

MSQA +0 MSQA(XLINE,SQAT) ;IO, %, \$I

MSQA +5 . I SQAT="%" D Q:XT Q:END

MSQA +6 .. I \$E(XLINE,POS)?1P,\$E(XLINE,(POS-SL))?1P S XT=1 Q ;IF ITEM

SURRONDED BY PUNCTUATION (like "%"), SKIP IT

MSQA +7 .. I \$E(XLINE,POS)'?1U I \$E(XLINE,(POS-SL))="=" S XT=1 Q ;Q

IF SOMETHING = %

MSQA +8 .. I \$E(XLINE,POS)="=",\$E(XLINE,-SL)?1P S XT=1 Q ;%= ALLOWED

MSQA +10 .. N PCT S PCT="" F AA=POS:1:\$L(XLINE) Q:\$E(XLINE,AA)'?1U S

PCT=PCT\_\$E(XLINE,AA) ;GETS THE LETERS AFTER THE % LIKE %ZIS

MSQA +12 ... I PCT="%ZIS" S XT=1 Q

DIC(0) .......................................................................

MSQA +20 . I SQAT="DIC(0)" D

MSQA +28 ... N DO1,D1 S D1="",DO1=\$F(XLINE,"DIC(0)=") F AA=DO1:1:\$L(

XLINE) Q:(\$E(XLINE,AA)=\$C(32))!(\$E(XLINE,AA)=",") S D1=D1\_\$E(

XLINE,AA)

IO ...........................................................................

FILEME +10 U IO

FSHOW +2 W @IOF S DIR(0)="F",DIR("A",1)="Set the path to find the .TXT

files",DIR("A",2)="or accept the standard default."

FSHOW +12 I \$G(L)\<1 W @IOF,"There are no Build Analyzer files to delete."

,!! Q

MSQA +0 MSQA(XLINE,SQAT) ;IO, %, \$I

MSQA +6 .. I \$E(XLINE,POS)?1P,\$E(XLINE,(POS-SL))?1P S XT=1 Q ;IF ITEM

SURRONDED BY PUNCTUATION (like "%"), SKIP IT

MSQA +15 . I SQAT="IO" D

K ^ ..........................................................................

TMP +9 . I XLINE\["K ^TMP("\_FMTY\_")" D

^( ...........................................................................

K1 +7 .. I XPCON\["^(" S END=1 Q

^TMP .........................................................................

SQAMM +7 . S MR1=MR1+2,MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)=

"",MCNT=MCNT+1,XPMM(MCNT)="These ^TMP calls have kill

statements within the included routines:" D

SQAMM +13 .. S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="",MCNT=

MCNT+1,XPMM(MCNT)="These ^TMP calls have no associated kill in

this build's included routines:"

SQAMM +15 . I '\$D(XPDTRR) S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(

MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="All ^TMP calls have at least

one kill statement in this build's routines."

TMP +2 N FMTY,NSP,NSPT,PX,TLINE,T9,FTWP,EXT S PX=\$L(XLINE,"^TMP(") F

I=2:1:PX D Q:EXT

TMP +5 . S FMTY=\$P(\$P(XLINE,"^TMP(",I),")"),NSP=\$\$TRIM^XLFSTR(\$P(FMTY,

","),"LR",\$C(34)),NSPT=T9\_"^TMP("\_FMTY\_")"

TMP +9 . I XLINE\["K ^TMP("\_FMTY\_")" D

TMP +10 .. S FTWP="^TMP("\_NSP\_","\_TWOP S:\$D(XPTK(FTWP)) XPTK(FTWP)=

XPTK(FTWP)\_"^"\_ROU\_" "\_TAGME S:'\$D(XPTK(FTWP)) XPTK(FTWP)=ROU\_"

"\_TAGME

K1 +8 .. I (XPCON\["^TMP")!(XPCON\["^UTILITY") S END=1 Q

^UTILITY .....................................................................

K1 +8 .. I (XPCON\["^TMP")!(XPCON\["^UTILITY") S END=1 Q

^XTMP ........................................................................

SQAMM +19 . S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="",MCNT=

MCNT+1,XPMM(MCNT)="General ^XTMP Notes"

SQAMM +20 . S MCNT=MCNT+1,XPMM(MCNT)="These ^XTMP calls have zero nodes

defined in this build's included routines:"

SQAMM +25 I XRRR\]"" S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="

These ^XTMP calls have no zero nodes defined in this build's

included routines" D

SQAMM +26 . N LLL F LLL=2:1:\$L(XRRR,"^") S MCNT=MCNT+1,XPMM(MCNT)=\$J(" ",

5)\_"Routine: "\_XPDXRR(\$P(XRRR,"^",LLL))\_\$J(" ",5)\_"^XTMP("\_\$P(

XRRR,"^",LLL)

SQAMM +27 I XRRR'\]"" S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="

ALL ^XTMP calls have zero nodes defined in this build's

routines"

TMPX +1 N NSP,PX,EXT S EXT=0,PX=\$L(XLINE,"^XTMP(") F I=2:1:PX D

TMPX +2 . S NSP=\$P(\$P(\$P(XLINE,"^XTMP(",I),")"),",") I NSP\]"" S XPDXRR(

NSP)=ROU I \$\$NSPACE^XPDANLYZ6(\$\$TRIM^XLFSTR(NSP,"LR",\$C(34)))

S TCHK=1

TMPX +3 N ZN,JJ,POS,QNUM S JJ=1,ZN="" I XLINE?.E1"S ".E1"^XTMP(".E1",0)

=".E1(1"^",1"\_U\_").E D

\<\>\<\>\<\>

XPDANLYZ6

% ............................................................................

BUILDME +3 S XPPATH=\$\$PWD^%ZISH()

DIC(0) .......................................................................

BUILDME +6 N DIRUT,DIC S DIC=9.6,DIC(0)="QEAM",DIC("A")="Select Build

Name: "

IO ...........................................................................

BUILDME +4 W @IOF,!,"This tool is used to analyze and list the components

of a build to identify",!,"adherence to standards and best

practices.",!! ;p732

TX1 +18 N TARR D GINFO("9.6",XPDIENS,"3","TARR") ;GET DESCRIPTION

ARRAY

TX1 +19 I '\$D(TARR(9.6,XPDIENS,3)) S XPDARR("BUILD",XPDBIEN,"DESCRIPT")

="No",XPDARR("BUILD",XPDBIEN,"WARNING","DESCRIPTION")="BUILD "\_

\$P(XPDTOP,"^",2)\_"("\_XPDBIEN\_") - DESCRIPTION field (#3)

missing."

TX1 +21 . S XPDARR("BUILD",XPDBIEN,"DESCRIPT")="Yes" N LL S LL=0 F S

LL=\$O(TARR(9.6,XPDIENS,3,LL)) Q:'LL S XPDARR("BUILD",XPDBIEN,"

DESCRIPTION",LL)=TARR(9.6,XPDIENS,3,LL)

BTXT +36 . I XPOPT(LKJ,EE1,ROU6)\["file:" S XPDARR("OPTION",LKJ,"WARNING"

,TMK_ROU6)=XPOPT(LKJ,EE1,ROU6) Q

BTXT +37 . I XPOPT(LKJ,EE1,ROU6)\["global" S XPDARR("OPTION",LKJ,"

WARNING",TMK_ROU6)=XPOPT(LKJ,EE1,ROU6) Q

BTXT +44 . I INCL,NSP S XPDARR("OPTION",LKJ,"WARNING",TMK_ROU6)=T1\_"

Calls routine "\_ROU6\_" not in build or namespace." Q

BTXT +45 . I 'INCL,NSP S XPDARR("OPTION",LKJ,"WARNING",TMK_ROU6)=T1\_"

Calls routine "\_ROU6\_" not in patch namespace." Q

BTXT +46 . I INCL,'NSP S XPDARR("OPTION",LKJ,"WARNING",TMK_ROU6)=T1\_"

Calls routine "\_ROU6\_" not in build." Q

BTXT +49 . N LKJ S LKJ=0 F S LKJ=\$O(XPDARR("OPTION",LKJ)) Q:'LKJ I \$D(

XPDARR("OPTION",LKJ,"WARNING",FN1)) K XPDARR("OPTION",LKJ,"

WARNING",FN1)

\*\* Analysis Complete \*\*

<span id="_Toc136407002" class="anchor"></span>Figure 35: Sample Output—KIDS Build Analyzer Option with SQA Option: XU\*8.0\*782 Build

XU\*8.0\*782 BUILD OVERVIEW May 25, 2023@14:15:50

-------------------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Not Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Not Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

Package File link: KERNEL

-------------------------------------------------------------------------------

\*\*\* Detailed results for components included in build XU\*8.0\*782 \*\*\*

-------------------------------------------------------------------------------

OPTION:

XPD UTILITY

No issues noted.

XPDANLYZ

No issues noted.

XPDANLYZ_DEL

No issues noted.

XPDANLYZ_SQA

No issues noted.

XPDANLYZ MAIN MENU

\* PACKAGE field (#12) missing.

-------------------------------------------------------------------------------

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run.

Routine information:

XPDANLYZ1 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ2 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ3 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ4 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ5 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

XPDANLYZ6 ;OAK/RSF- BUILD ANALYZER ;10/28/22

;;8.0;KERNEL;\*\*782\*\*;Jul 10, 1995;Build 4

;;Per VHA Directive 2004-038, this routine should not be modified.

\* Date ^XINDEX last run was not found.

\<\>\<\>\<\>

===============================================================================

This build may include references to components (i.e. Routines,

Globals, etc.) outside the build namespace. Review and validate

that all appropriate Integration Control Registrations (ICRs)

exist for each external reference.

===============================================================================

These ^TMP calls have kill statements within the included routines:

^TMP(XPDEM,\$J

XPDANLYZ2 FMSG +2

^TMP(\_FMTY\_,0

XPDANLYZ5 TMP +9

These ^TMP calls have no associated kill in this build's included routines:

XPDANLYZ5 TMP +10 ^TMP("\_NSP\_","\_TWOP S:\$D(XPTK(FTWP)

General ^XTMP Notes

These ^XTMP calls have zero nodes defined in this build's included routines:

Routine: XPDANLYZ5 ^XTMP(".E1",0)=".E1(1"^",1"\_U\_").E D

These ^XTMP calls have no zero nodes defined in this build's included routines

Routine: XPDANLYZ5 ^XTMP("

Routine: XPDANLYZ5 ^XTMP("\_\$P(XRRR

XPDANLYZ1

% ............................................................................

START +3 N X,XPDATE,XPDLINE,XPDBN,%,%H,%I D NOW^%DTC S XPDATE=X,XPDIS=1

IO ...........................................................................

PME +1 I XPDIS=1 S END=0 N POP,IO,IOP,%ZIS,ZTIO D G:POP X1

PME +13 . I \$D(IO("Q")) K IO("Q") S END=1 Q

\<\>\<\>\<\>

XPDANLYZ2

\$I ...........................................................................

SQA +7 S XPDARRR("\$I",RR,0)=""

RLINES +35 ... I (XPD1="\$I"),'XPDIS2,RTN(K,0)\[XPD1 S TCHK=\$\$MSQA^

XPDANLYZ5(RTN(K,0),XPD1) Q:'TCHK

//// .........................................................................

SQA +1 S XPDARRR("////",RR,0)=""

DIC(0) .......................................................................

SQA +2 S XPDARRR("DIC(0)",RR,0)=""

RLINES +36 ... I (XPD1="DIC(0)"),'XPDIS2,RTN(K,0)\[XPD1 S TCHK=\$\$MSQA^

XPDANLYZ5(RTN(K,0),XPD1) Q:'TCHK

IO ...........................................................................

SQA +13 S XPDARRR("IO",RR,0)=""

K @ ..........................................................................

SQA +11 S XPDARRR("K @",RR,0)=""

K ^ ..........................................................................

SQA +9 S XPDARRR("K ^",RR,0)=""

RLINES +32 ... I (XPD1="K ^"),'XPDIS2,RTN(K,0)\[XPD1 S TCHK=\$\$KCHK^

XPDANLYZ5(RTN(K,0),XPD1) Q:TCHK'=3

^( ...........................................................................

SQA +12 S XPDARRR("^(",RR,0)=""

^TMP .........................................................................

RLINES +31 ... I XPD1="^TMP",'XPDIS2,RTN(K,0)\[XPD1 D TMP^XPDANLYZ5(RTN(K,

0)) I 'XPDIS2 Q:TCHK

^UTILITY .....................................................................

SQA +3 S XPDARRR("^UTILITY",RR,0)=""

^XTMP ........................................................................

RLINES +30 ... I XPD1="^XTMP",RTN(K,0)\[XPD1 D TMPX^XPDANLYZ5(RTN(K,0)) I '

XPDIS2 Q:TCHK ;TMPX^ZZSRABA

\<\>\<\>\<\>

XPDANLYZ5

\$I ...........................................................................

MSQA +0 MSQA(XLINE,SQAT) ;IO, %, \$I

MSQA +19 . I SQAT="\$I" N SP1 S SP1=(POS-SL) I (\$E(XLINE,SP1,(SL+1))="\$\$"

)!(\$E(XLINE,POS)?1A) S XT=1 Q

% ............................................................................

MSQA +7 .. I \$E(XLINE,POS)'?1U I \$E(XLINE,(POS-SL))="=" S XT=1 Q ;Q

IF SOMETHING = %

DIC(0) .......................................................................

MSQA +20 . I SQAT="DIC(0)" D

IO ...........................................................................

MSQA +0 MSQA(XLINE,SQAT) ;IO, %, \$I

^( ...........................................................................

K1 +7 .. I XPCON\["^(" S END=1 Q

^TMP .........................................................................

SQAMM +7 . S MR1=MR1+2,MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)=

"",MCNT=MCNT+1,XPMM(MCNT)="These ^TMP calls have kill

statements within the included routines:" D

SQAMM +13 .. S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="",MCNT=

MCNT+1,XPMM(MCNT)="These ^TMP calls have no associated kill in

this build's included routines:"

SQAMM +15 . I '\$D(XPDTRR) S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(

MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="All ^TMP calls have at least

one kill statement in this build's routines."

TMP +2 N FMTY,NSP,NSPT,PX,TLINE,T9,FTWP,EXT S PX=\$L(XLINE,"^TMP(") F

I=2:1:PX D Q:EXT

TMP +5 . S FMTY=\$P(\$P(XLINE,"^TMP(",I),")"),NSP=\$\$TRIM^XLFSTR(\$P(FMTY,

","),"LR",\$C(34)),NSPT=T9\_"^TMP("\_FMTY\_")"

K1 +8 .. I (XPCON\["^TMP")!(XPCON\["^UTILITY") S END=1 Q

^UTILITY .....................................................................

K1 +8 .. I (XPCON\["^TMP")!(XPCON\["^UTILITY") S END=1 Q

^XTMP ........................................................................

SQAMM +19 . S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="",MCNT=

MCNT+1,XPMM(MCNT)="General ^XTMP Notes"

SQAMM +20 . S MCNT=MCNT+1,XPMM(MCNT)="These ^XTMP calls have zero nodes

defined in this build's included routines:"

SQAMM +25 I XRRR\]"" S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="

These ^XTMP calls have no zero nodes defined in this build's

included routines" D

SQAMM +26 . N LLL F LLL=2:1:\$L(XRRR,"^") S MCNT=MCNT+1,XPMM(MCNT)=\$J(" ",

5)\_"Routine: "\_XPDXRR(\$P(XRRR,"^",LLL))\_\$J(" ",5)\_"^XTMP("\_\$P(

XRRR,"^",LLL)

SQAMM +27 I XRRR'\]"" S MCNT=MCNT+1,XPMM(MCNT)="",MCNT=MCNT+1,XPMM(MCNT)="

ALL ^XTMP calls have zero nodes defined in this build's

routines"

TMPX +1 N NSP,PX,EXT S EXT=0,PX=\$L(XLINE,"^XTMP(") F I=2:1:PX D

TMPX +2 . S NSP=\$P(\$P(\$P(XLINE,"^XTMP(",I),")"),",") I NSP\]"" S XPDXRR(

NSP)=ROU I \$\$NSPACE^XPDANLYZ6(\$\$TRIM^XLFSTR(NSP,"LR",\$C(34)))

S TCHK=1

TMPX +3 N ZN,JJ,POS,QNUM S JJ=1,ZN="" I XLINE?.E1"S ".E1"^XTMP(".E1",0)

=".E1(1"^",1"\_U\_").E D

\*\* Analysis Complete \*\*

# Build Analysis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Build Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all display formats, the VistA Build Analyzer utility first lists the build overview; identifying components included in the build, as shown in <u>Figure 36</u>:

<span id="_Ref127179776" class="anchor"></span>Figure 36: Sample Build Overview—List of Build Components

Analysis of a KIDS BUILD Feb 25, 2021

=============================================================================

SR\*3.0\*200 BUILD OVERVIEW

----------------------------------------------------------------------

APPLICATION ACTION Not Included

BULLETIN Not Included

DIALOG Not Included

ENTITY Not Included

FILES Included

FORM Not Included

FUNCTION Not Included

HELP FRAME Not Included

HL LOGICAL LINK Not Included

HL7 APPLICATION PARAMETER Not Included

HLO APPLICATION REGISTRY Not Included

INPUT TEMPLATE Included

LIST TEMPLATE Not Included

MAIL GROUP Not Included

OPTION Not Included

PARAMETER DEFINITION Not Included

PARAMETER TEMPLATE Not Included

POLICY Not Included

POLICY FUNCTION Not Included

PRINT TEMPLATE Not Included

PROTOCOL Not Included

REMOTE PROCEDURE Not Included

ROUTINE Included

SECURITY KEY Not Included

SORT TEMPLATE Not Included

XULM LOCK DICTIONARY Not Included

## General Build Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the patch is sending components that are set to DELETE AT SITE, the Build Analyzer lists them here (<u>Figure 37</u>):

<span id="_Ref127179672" class="anchor"></span>Figure 37: Sample List of Patch Components that are set to DELETE AT SITE

The following components are listed as "DELETE AT SITE".

Review to validate these are accurately identified.

Component Name

========================================

ROUTINE OR3CONV

ROUTINE OR3CONV1

If the patch is *not* set to track nationally, you get the warning shown in <u>Figure 38</u>:

<span id="_Ref127179082" class="anchor"></span>Figure 38: Sample Warning Message—Patch Not Set to Track Nationally

> **WARNING:** Build not set to track package nationally;

Please validate that is correct.

If a build does *not* have a PACKAGE LINE, you get the warning shown in <u>Figure 39</u>:

<span id="_Ref127179285" class="anchor"></span>Figure 39: Sample Warning Message—Build Missing PACKAGE LINE

> **WARNING:** The PACKAGE FILE LINK is missing.

This should be defined for a national VISTA product build.

If patch contain an environment check routine and it is *not* set as DELETE AT SITE, the Build Analyzer displays the warning shown in <u>Figure 40</u>:

<span id="_Ref127179487" class="anchor"></span>Figure 40: Sample Warning Message—Patch Contain an Environment Check Routine and it is Not Set as DELETE AT SITE

> **WARNING:** ENVIRONMENT CHECK routine is NOT set to DELETE AT SITE

If the patch contain a POST-INSTALL routine and it is *not* set as DELETE AT SITE, the Build Analyzer displays the warning shown in <u>Figure 41</u>:

<span id="_Ref127179537" class="anchor"></span>Figure 41: Sample Warning Message—Patch Contain a Post-Install Routine and it is Not Set as DELETE AT SITE

> **WARNING:** POST-INSTALL routine is NOT set to DELETE AT SITE.

If the patch contain a PRE-INSTALL routine and it is *not* set as DELETE AT SITE, the Build Analyzer displays the warning shown in <u>Figure 42</u>:

<span id="_Ref127179589" class="anchor"></span>Figure 42: Sample Warning Message—Patch Contain a Pre-Install Routine and it is Not Set as DELETE AT SITE

> **WARNING:** PRE-INSTALL routine is NOT set to DELETE AT SITE.

## Build Component Analysis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Build Analyzer utility report displays analysis of each component included in the build, as shown in <u>Figure 43</u>:

<span id="_Ref127184038" class="anchor"></span>Figure 43: Sample Report Displaying Build Component Analysis

\*\*\* Detailed results for selected components of build SR\*3.0\*200 \*\*\*

-----------------------------------------------------------------------------

FILE:

SURGERY

No issues noted.

LOCAL SURGICAL SPECIALTY

No issues noted.

INPUT TEMPLATE:

SROMEN-OUT

\* DESCRIPTION missing.

SROMEN-OPER

\* DESCRIPTION missing.

SRONRPT

\* DESCRIPTION missing.

SRONRPT1

\* DESCRIPTION missing.

SRONRPT2

\* DESCRIPTION missing.

-----------------------------------------------------------------------------

If routines are included in the build, the Build Analyzer prints information about the routine checks:

<span id="_Toc136407011" class="anchor"></span>Figure 44: Sample List of Build Routine Checks

ROUTINES

Routines can be analyzed using ^XINDEX. This section displays

first two lines of routines so they can be validated.

The third line will be included if it begins with a ";"

It also lists the date ^XINDEX was last run and potential issues

that would be identified in an SQA Checklist Review.

Routine information:

SRONIN ;BIR/MAM,ADM - NURSE INTRAOPERATIVE REPORT ;10/24/2011

;;3.0;Surgery;\*\*68,50,100,129,134,153,157,175,176,182,184,200\*\*;24 Jun 93;Build 35

\* Date ^XINDEX last run was not found.

\* The SQA Checklist identifies the following specific code

references to check:

% Lines: 22, 23, 27, 37, 38

K ^ Lines: 47, 89

U= Lines: 15, 21, 73, 108, 173

^TMP Lines: 33, 36, 47, 89, 110

\$I Reference not found in this routine

//// Reference not found in this routine

DIC(0) Reference not found in this routine

^( Reference not found in this routine

^UTILITY Reference not found in this routine

^XTMP Reference not found in this routine

\<\>\<\>\<\>

DGPFHLU ;ALB/RPM - PRF HL7 ORU/ACK PROCESSING ; 6/21/06 10:27am

;;5.3;Registration;\*\*425,718,650,951\*\*;Aug 13, 1993;Build 135

;;Per VA Directive 6402, this routine should not be modified.

\* DGPFHLU is not in the Package namespace.

\* Date of Last ^XINDEX: APR 09, 2021

\* Missing current patch number on second line.

\* The SQA Checklist identifies the following specific code

references to check in this routine:

\- No specific code references from the SQA Checklist were found.

\<\>\<\>\<\>

*<span class="mark">\[display cut here\]</span>*

If the user included descriptions of the components/routine text (to have in one place so that they can copy/paste them into a spellcheck program), the output will look like the example in <u>Figure 45</u>:

<span id="_Ref127198036" class="anchor"></span>Figure 45: Sample Output Showing the Build Components and Routine Descriptions

Descriptions associated with this build:

BUILD: SR\*3.0\*200 (#11341)

This enhancement to the VISTA Surgery package includes a new field

ROBOTIC ASSISTANCE (Y/N) for tracking whether robotic assistance was used

when completing a surgery procedure. The new field is included on the

Operation, Operation Short Screen, and Nurse Intraoperative Report

options within the Operation Menu and is required to be entered prior to

signing the Nurse Intraoperative Report. The field is also included on

Non-Cardiac and Cardiac Risk Assessment data entry options. This

indicator is transmitted to VASQIP for all cases. A new field, ROBOTIC

DEFAULT (#12) has been added to the LOCAL SURGICAL SPECIALTY file

(137.45). If defined for a local specialty, the software will

automatically enter NO in the ROBOTIC ASSISTANCE (Y/N) field when

a surgery case is created for the selected specialty.

Update to transmission code to restrict date/time field 613 to 12

characters.

FILE: SURGERY (#130)

FIELD: .04: SURGERY SPECIALTY

Definition Revised (2007):

This is the surgical specialty credited for doing this operative

procedure. Many reports, including the Annual Report of Surgical

Procedures, are sorted by the surgical specialty. This field should be

entered prior to completion of this case. (If you enter '?' in the

surgical package, it will display the entire local surgical specialty

list and a copy of the national list can be found in the Operations

Manual.)

HELP-PROMPT:

Enter the assigned surgical specialty, or section, of the surgeon.

FIELD: 2006: ROBOTIC ASSISTANCE (Y/N)

This field indicates whether robotic assistance was used for any portion

of the procedure. It must be entered prior to signing the Nurse

Intraoperative Report. Enter YES if robotic assistance was used during

the procedure. Otherwise, enter NO.

HELP-PROMPT:

Enter YES if robotic assistance was used for any part of the procedure.

FILE: LOCAL SURGICAL SPECIALTY (#137.45)

FIELD: 12: ROBOTIC DEFAULT

Setting this field to NO - ROBOTICS NOT USED will cause the software

to automatically set the ROBOTIC ASSISTANCE (Y/N) field to NO when

a surgical case is created and this specialty is selected. The value of

the ROBOTIC ASSISTANCE (Y/N) for the case can still be modified for the

case later.

Leave this field blank if the specialty uses robotics for any procedures.

HELP-PROMPT:

Enter NO to automatically set the ROBOTIC ASSISTANCE (Y/N) field to NO when cases are created for this specialty.

INPUT TEMPLATE: SROMEN-OUT

\* Description missing.

INPUT TEMPLATE: SROMEN-OPER

\* Description missing.

INPUT TEMPLATE: SRONRPT

\* Description missing.

INPUT TEMPLATE: SRONRPT1

\* Description missing.

INPUT TEMPLATE: SRONRPT2

     \* Description missing.

===============================================================================

Text in ROUTINES between quotes and/or after ;;, by line number:

DENTAR

3: OPT

3: VERSION

3: VERSION

6: VERSION

12: Select

12: : EXIT//

18: Select STATION.DIVISION:

22: ^DENTAR

23: QUE^DENTAR

25: Okay to release this report for transmission to Austin

25: Nothing released

31: Report released for transmission to Austin

33: Stations have not been entered in the Dental Site Parameter file.

33: You must enter a station before you can use this option

34: JANUARY;FEBRUARY;MARCH;APRIL;MAY;JUNE;JULY;AUGUST;SEPTEMBER;OCTOBER;

NOVEMBER;DECEMBER

37: RELEASE SERVICE REPORTS;OPTION;DENTAR

38: TREATMENT DATA REVIEW/RELEASE MENU;^DENTAR1

39: CLASS I-VI ADMIN INFO (TYPE 3);ADM

40: PERSONNEL INFO (TYPE 4);PERS

41: APPLICATIONS AND DENTAL FEE (TYPE 5);FEE

42: RELEASE ALL SERVICE REPORTS;ALL

43: CHECK DUPLICATE FOR SITTINGS;^DENTDUP

*<span class="mark">\[display cut here\]</span>*

\*\* Analysis Complete \*\*

## Description of Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section parses the build from the BUILD (#9.6) file into its included components among the list of all potential components for a build, such as <u>Figure 46</u>:

<span id="_Ref127198888" class="anchor"></span>Figure 46: Sample List of Build Components

DIALOG Not Included

ENTITY Not Included

FILES Included

The VistA Build Analyzer utility does the following:

- Checks if the “Track Package Nationally” is *not* set to YES.
- Looks for a PACKAGE LINK.
- Looks for Environmental, Pre-Install, and Post-Install routines and warns if not set to DELETE AT SITE.
- Checks for and lists any components designated DELETE AT SITE for reviewer to be able to confirm.

## Individual Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Build Analyzer utility checks component and routine names to determine if the package is in the correct namespace. It does this by potentially checking against an array of acceptable namespaces derived from the first part of the build name, and, if found, any ADDITIONAL PREFIXES (#14) Multiple field from the PACKAGE (#9.4) file. If there are excluded name spaces (#919) listed in the PACKAGE (#9.4) file, it checks the namespace of the component/routine against those as well.

This section looks for certain aspects of the included components and notes if something does *not* seem to be in order. Files and Routines are handled differently from the other components.

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For files, the VistA Build Analyzer utility display differs depending on if the build includes the full Data Dictionary (DD) or a partial DD of the file.

- Full DD with *new* file, it checks the following:
  - File name is in uppercase.
  - If the new file uses the ^DIC global.
  - If tracked nationally, checks if the ^DIZ global is used.
  - For a file description, notes if it is minimal or missing.
- Full DD with *existing* file, it checks each field and subfield for the following:
  - Name is in uppercase.
  - Description is present.
  - Help-Prompt is present. If present, it also checks if the Help-Prompt and Description are the same.
- Partial DD with *existing* file, it only checks the specific fields being sent for the following:
  - Name is in uppercase.
  - Description is present.
  - Help-Prompt is present. If present, it also checks if the Help-Prompt and Description are the same.

For partial DDs, It does *not* check the attributes at the file level (e.g., file description or name), or other fields.

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For routines included in the build, the VistA Build Analyzer utility prints out the first two lines of each routine allowing the user to easily confirm that they are set correctly. It includes the third line if it starts with a “;”.

The Build Analyzer also checks for the following:

- Current patch number is the last patch listed on the second line of the routine (between the set of double asterisks).
- Date of the last XINDEX. The last XINDEX date is only populated if the question in <u>Figure 47</u> was answered YES when XINDEX was performed:

> <span id="_Ref127201046" class="anchor"></span>Figure 47: XINDEX Question—Answering YES Adds a Date for the Last XINDEX

Save parameters in ROUTINE file? NO//

When the user enters YES at this prompt, the last XINDEX date run gets stored with that Build, so the VistA Build Analyzer utility can check for this date.

- Reviews the BUILD (#9.6) file and looks for this routine to make sure all patch numbers are current on the second line.
- If the routine appears to be in the same namespace and if the routine name is uppercase.

The example in <u>Figure 48</u> shows some of the routine-related issues found by the VistA Build Analyzer utility:

<span id="_Ref127276077" class="anchor"></span>Figure 48: Sample Build Routine Output

SRZZUTL ;BIR/ADM,SBW - UTILITY ROUTINE ;10/21/2019

;;3.0;SURGERY RISK ASSESSMENT;;23 Sep 91

\* SRZZUTL is not in the Package namespace.

\* Missing current patch number on second line.

\* Date ^XINDEX last run was not found.

\* BUILD file also lists this routine in these patches:

SRA\*3.0\*1

XUSER3   ;ISF/RWF - New Person File Utilities History ;08/11/08  14:18  
         ;;8.0;KERNEL;\*\*492,500\*\*;Jul 10, 1995  
         ;Per VHA Directive 2004-038, this routine should not be modified.

The Build Analyzer then checks each line of the routine for existence of questionable<sup>\*</sup> code snippets; if found, it indicates the line number(s).

<sup>\*</sup>These are *not* contraindicated for use, but SQA checks how they are used.

The following lists the code that the SQA checklist indicates to check, and what the VistA Build Analyzer utility looks for in a build:

- ////
- DIC(0)
- ^UTILITY
- ^TMP
- ^XTMP
- %
- \$I
- U=
- K ^
- ^(
- K:
- K @
- IO

The VistA Build Analyzer utility shows line numbers for each of those codes.

It also checks for variations of the KILL statement in the search:

- Conditional KILL (K:).
- KILL with indirection (K @).
- Added KILL: For the added KILL statements, the Build Analyzer checks if KILLs go to a caret (^) or an at-sign (@). For example, these would be flagged:

<span id="_Toc136407016" class="anchor"></span>Figure 49: Sample Variations of KILL Statements

D UTIL <span class="mark">K:SRK ^SRF("APCE",SRTN)</span> I 'SRK D PCE

<span class="mark">K:N'="KEY"&(N'="OPT") @(DIC\_"+Y)")</span>

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc136407017" class="anchor"></span>Figure 50: Two Examples of Routine Output

<span class="mark">SROACL1</span> ;BIR/MAM - CARDIAC PREOP CLINICAL DATA ; AUGUST 11, 2011

;;3.0;Surgery;\*\*38,71,95,125,153,160,174,176,182,184,200\*\*;24 Jun 93;Build 35

\* Date of Last ^XINDEX: APR 09, 2021

\* The SQA Checklist identifies the following specific code

references to check in this routine:

K ^ Lines: 80

^UTILITY Lines: 80, 81, 82, 83, 84, 85

\<\>\<\>\<\>

<span class="mark">SROACL2</span> ;BIR/SJA - CLINICAL DATA ; JULY 12, 2011

;;3.0;Surgery;\*\*125,160,176,182,184,200\*\*;24 Jun 93;Build 35

\* Date of Last ^XINDEX: APR 09, 2021

\* The SQA Checklist identifies the following specific code

references to check in this routine:

\-  No specific code references from the SQA Checklist were found.

## All Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following components are checked by the VistA Build Analyzer utility:

- APPLICATION ACTION (#1.61)
- BULLETIN (#3.6)
- DIALOG (#.84)
- ENTITY (#1.5)
- FORM (#.403)
- FUNCTION (#.5)
- HELP FRAME (#9.2)
- HL7 APPLICATION PARAMETER (#771)
- HLO APPLICATION REGISTRY (#779.2)
- HL LOGICAL LINK (#870)
- INPUT TEMPLATE (#.402)
- LIST TEMPLATE (#409.61)
- MAIL GROUP (#3.8)
- OPTION (#19)
- PARAMETER DEFINITION (#8989.51)
- PARAMETER TEMPLATE (#8989.52)
- POLICY (#1.6)
- POLICY FUNCTION (#1.62)
- PRINT TEMPLATE (#.4)
- PROTOCOL (#101)
- REMOTE PROCEDURE (#8994)
- ROUTINE (#9.8)
- SECURITY KEY (#19.1)
- SORT TEMPLATE (#.401)
- XULM LOCK DICTIONARY (#8993)

All component checks include:

- Validates that the Name is uppercase.
- Validates that the Name is in the same namespace.
- Validates the component has a Description.

## Specific Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific Components have the same checks as indicated in the “<u>All Components</u>” section, plus component-specific checks:

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the OPTIONS (#19) file, the VistA Build Analyzer utility checks for the following:

- Validates that the MENU TEXT (#1) field is defined.
- Validates that the PACKAGE (#12) field is defined.
- Checks to determine whether routines referenced in the following fields are included in the build/namespace:
  - ROUTINE (#25)
  - ENTRY ACTION (#20)
  - EXIT ACTION (#15)

### Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the REMOTE PROCEDURE (#8994) file, the VistA Build Analyzer utility checks for the following:

- If the RETURN VALUE TYPE (#.04) field exists, it checks for data in the RETURN PARAMETER DESCRIPTION (#3).
- If it has input variables, it validates that a description exists for each input variable.
- Check if routine it calls is included in the build/namespace.

### Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the BULLETIN (#3.6) file, the VistA Build Analyzer utility checks for the following:

Validates that the MAIL GROUP (#4) field is listed.

### Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the DIALOG (#.84) file, the VistA Build Analyzer utility checks for the following:

If it calls a routine, it checks if the ROUTINE NAME (#8,.01) field is in the build/namespace.

## Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Issues for each component are noted in the Build Analyzer output, as shown in <u>Figure 51</u>:

<span id="_Ref127280733" class="anchor"></span>Figure 51: Sample Output from the Build Analyzer for Each Component

FILE:

TRANSMISSION LAYOUTS

\* No PACKAGE identified.

\* AC cross-reference (field \#4) - DESCRIPTION missing.

BULLETIN:

LA7 ABNORMAL RESULTS RECEIVED

\* Might be incorrect name space

\* No MAIL GROUP

DIALOG:

210

\* PACKAGE VA FILEMAN is not the build namespace.

\* ROUTINE NAME (subfield \#.01) within the CALLED FROM ENTRY POINTS sub-file

(#8) calls DIR3 not found in build.

\* ROUTINE NAME (subfield \#.01) within the CALLED FROM ENTRY POINTS sub-file

(#8) calls DIR3 not in the patch namespace.

OPTION:

A1AX EDIT PARAMETER FILE

\* The OPTION name might be incorrectly namespaced

\* PACKAGE field (#12) missing.

\* ENTRY ACTION field (#20): Calls routine DIC not in build or namespace.

\* Calls routine DIE not in build or namespace.

\* ENTRY ACTION field (#20): Calls file: EXT REV REGION PARAMETER.

If a component passes all these checks, the Build Analyzer report displays “No issues noted”, as shown in <u>Figure 52</u>:

<span id="_Ref127280870" class="anchor"></span>Figure 52: Sample Report Output with No Issues Found

ZZSRA VISN RN LIST

No issues noted

## SQA Check—Full Lines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can choose to do a full SQA check when you answer YES at the prompt shown in <u>Figure 53</u>:

<span id="_Ref135748557" class="anchor"></span>Figure 53: Performing a Full SQA Check—System Prompts and User Entries

Do you want to include a section that displays the routine lines containing

specific code references reviewed on the SQA checklist? NO// <span class="mark">YES</span>

If you answer YES at the prompt shown in <u>Figure 53</u>, SQA checklist items will be included in the screen display output, as an additional text file, or a mail message that lists the line content, by line tag, of lines with SQA checklist items. The VistA Build Analyzer utility attempts to reduce the number of these lines by removing clearly inconsequential entries; hoping to better target the response to what is concerning. This is a growing field, but currently this is what is screened out:

- If line has multiple uses of the text in question, if one is *not* excluded, the whole line is shown, not just the questionable code usage.
- K ^

It will show if:

- There are references, such as: K ^SRF, K ^SRF(0), K ^SRAFY(139.9), or K ^SRAFY(139.9,0).
- There is an indirection KILL, such as: K ^@KILLME.

It will *not* show if:

- First piece in parentheses is *not* a number (e.g., ^SRF(SRIEN).
- TMP, UTILITY (K ^TMP(XXX,\$J), or K ^UTILITY(“SOMETHING”)).
- Naked reference (shows in the “^” section).

Added a conditional KILL check (K:) that shows if the first section after the conditional meets the prior requirements.

### ^TMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^TMP does *not* show if:

- First piece in the parenthesis is a \$J.
- If *not*\$J, it does *not* show if the first piece is NAMESPACED and the second piece is \$J.

Also, at the beginning of the “SQA” section it lists the locations of ^TMP KILL statements and ^TMPs used that do *not* have a KILL in the included build routines.

These ^TMP calls have KILL statements within the included routines:

<span id="_Toc136407021" class="anchor"></span>Figure 54: Sample ^TMP Calls with an Associated KILL Statement

  ZZSRAT2 PTEST +16       K ^TMP("SRATEST"),SRA

  ZZSRAT2 TCAS +1         K ^TMP("SRATEST")

  SRZZUTL ZDNLDED +11     K ^TMP("SRLIST",\$J)

  SRZZUTL DNLDED +14      S SRTOT=0 K ^TMP("SRLIST",\$J)

  SRZZUTL DNLDED +24      K ^TMP("SRLIST",\$J)

  SRZZUTL DNLDED2 +5      S SRTOT=0 K ^TMP("SRLIST",\$J)

These ^TMP calls have no associated KILL in this build's included routines:

<span id="_Toc136407022" class="anchor"></span>Figure 55: Sample ^TMP Calls with No Associated KILL Statement

ZSROPCE NITE +4          S SRS="SURGERY DATA",SRFILE=0,^TMP("SRPXAPI",\$J)=””

### ^XTMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, *not* restricting XTMP, but it looks for any ^XTMPzero nodes in the included routines, and in addition to the line tags, lists which ones it found and which it did *not*, such as <u>Figure 56</u>:

<span id="_Ref127283911" class="anchor"></span>Figure 56: Sample ^XTMP Report Output

General ^XTMP Notes

These ^XTMP calls have zero nodes defined in this build's included routines:

Routine: ZZSRAT2 ^XTMP("SSNINQ",\$J,0)=SRNOW\_"^"\_SRNOW\_"^SSN CHECK"

These XTMP calls have no zero nodes defined in this build's included routines

Routine: ZZSRAT2 ^XTMP("SRPARSE"

### U=

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

U= does *not* show a line if:

- U=“^”.
- If part of another variable, such as SRAU=.

### %

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

% does *not* show a line if:

- Variable = “%” or % (standalone %, with or without quotes)
- %=something
- % is part of a quote, such as “rejected by 10% rule”
- If %XXX is part of a DO, IF, eXecute statement
- %DT.
- %DTC
- %RCR
- %ZIS
- %ZTLOAD
- %ZOSF% shows if:
- If %XXX is part of a SET, NEW, or KILL statement.
- If *not* skipped due to the above exclusions.

### \$I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$I does *not* show a line if:

Part of longer code, such as \$\$ICDX= or \$ISD

### IO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IO does *not* show a line if:

- IO\* (\* = a letter), such as: “IOF”
- \*IO (\* = a letter), such as “S SRIO=”
- U IO
- I IOIO shows if:
- K IO
- S IO
- N IO
- G IO

### DIC(0)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DIC(0) does *not* show a line if:

- It also has a FILE^DICN call with twoKILL DOs found on the line.
- If there is no FILE^DICN call, it checks for DIC(0) containing an L parameter. If so, it *must* have a DLAYGO defined.
- No FILE^DICN call and DIC(0) does *not* contain “L”.

DIC(0) shows if:

- If FILE^DICN but cannot find the K DO statements on the same line.
- No FILE^DICN, DIC(0) contains an L, but no DLAYGO defined.

## Text Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Component Descriptions/Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a user chooses to show descriptions/text, they appear following the “Detailed Build Analysis” section when displayed to the screen, or in a separate email or text file. The descriptions can be reviewed, and the text copied and pasted into a spellcheck document. If displayed to the screen, it is easy to capture the information by setting it up to log the display. The display shows the component description or notes if it is missing. If a partial DD file is included, it includes, if present, the field description, help-prompt ,and Tech description for the spellcheck (<u>Figure 57</u>).

<span id="_Ref127358921" class="anchor"></span>Figure 57: Sample Partial DD Output

FILE: SURGERY (#130)

FIELD: .04: SURGERY SPECIALTY

Definition Revised (2007):

This is the surgical specialty credited for doing this operative

procedure. Many reports, including the Annual Report of Surgical

Procedures, are sorted by the surgical specialty. This field should be

entered prior to completion of this case. (If you enter '?' in the

surgical package, it will display the entire local surgical specialty

list and a copy of the national list can be found in the Operations

Manual.)

HELP-PROMPT:

Enter the assigned surgical specialty, or section, of the surgeon.

Other examples in description section (<u>Figure 58</u>):

<span id="_Ref127358878" class="anchor"></span>Figure 58: Sample Description Output

FILE: EXT REV REGION PARAMETER

No description.

MAIL GROUP: SRA OIT SUPPORT

This mailgroup receives SURGERY RISK ASSESSMENT transmission messages from

the medical centers.

### M Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section displays text that is presented to users in a WRITE statement or a \$text (“;;”) from routines included in the build.

Text displayed meets the following requirements:

- Text between quotes or following a “;;” (does *not* include the second line of the routine).
- Text between quotes contains at least three consecutive letters.
- Text after “;;” of at least three characters.
- Routine line does *not* begin with a semicolon.

Text that meets these requirements is excluded if:

- If has 15 or more characters *without* a space.
- If a section has no space and letters that make up less than half of the characters.
- If no space and ends in a “(”.
- If the quoted text follows:
  - DIC=
  - DIC(0)=
  - DR=
  - DIE=
  - DIC("S")=
  - \$J,
  - “(“. For example: ^XTMP(“SRAM” would be skipped. Or, if “,\$J” follows quoted text

The information is displayed for each routine and identifies the line number where found (<u>Figure 59</u>):

<span id="_Ref127359041" class="anchor"></span>Figure 59: Sample Routine with Line Number Output

SRONIN

14: Nurse Intraoperative Report

15: TIU

21: TIU

23: PRNT^SRONIN

26: ) Case \#

27: Printed:

28: Pt Loc:

44: ) Case \#

54: FOA

54: Press \<return\> to continue, 'A' to access Nurse Intraoperative Report

54: functions, or '^' to exit:

62: Age:

62: Vice SF 509

68: MEDICAL RECORD NURSE INTRAOPERATIVE REPORT - CASE \#

73: TIU

75: \* \* The Nurse Intraoperative Report has been electronically signed. \* \*

76: Nurse Intraoperative Report Functions:

Remember, if pasting into a Microsoft<sup>© (MS)</sup> Word or other word-processing application with spellcheck, be sure that the option to “Ignore words in UPPERCASE” is unchecked (<u>Figure 60</u>):

MS Word à File à Option à Proofing

<span id="_Ref127359268" class="anchor"></span>Figure 60: Setting Up Microsoft Word Proofing Checks—Ignore words in UPPERCASE

![](vista-build-analyzer-utility-user-guide-kernel-patch-xu-8-0-782/009.png)