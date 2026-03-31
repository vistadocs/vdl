---
title: GCS Version 2 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: GEN
app_name: Generic Code Sheet (GCS)
section: FIN
app_status: active
pkg_ns: GEN
patch_ver: 2
patch_id: GEN*2
group_key: "GEN:GEN:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - code
  - table
  - contents
  - sheet
  - generic
  - sheets
  - package
  - routine
  - routines
  - entry
page_count: 0
word_count: 2801
section_count: 23
table_count: 194
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1995
revision_count: 2
revision_newest: 12/22/04
revision_oldest: 12/22/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Generic_Code_Sheet_(GCS)/gcs2tech.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Generic_Code_Sheet_(GCS)/gcs2tech.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=7"
---

Decentralized Hospital Computer Program

GENERIC CODE SHEETTECHNICAL MANUAL

March 1995

Information Systems Center

Washington, D.C.

Preface

This technical manual is designed to provide the IRM Chief/Site Manager and staff with information necessary to maintain and troubleshoot problems with Version 2.0 of the Generic Code Sheet package. It has also been written to aid the programming community in designing and developing new code sheets.

Table of Contents

Introduction

Orientation

DHCP Conventions

Implementation and Maintenance

A. Naming Conventions
B. Files
C. Globals
D. Resource Requirements
E. Security Keys
F. Installation
G. Parameters
H. Mail Groups 9

Routine Descriptions

A. Descriptions
B. Mapping Recommendations
C. Callable Routines

File List

A. Overview
B. Descriptions
C. File Security
D. Overwriting Data 17
E. File Map

Templates

A. Input Templates
B. Print Templates
C. Sort Templates 26

Exported Options

A. Map of Options
B. Description of Options

Archiving and Purging

External Relations

A. Packages Needed to Run Generic Code Sheets
B. Files Needed to Run Generic Code Sheets
C. Entry Points with Open Subscriptions

1\. GECSENTR

2\. Callable Menu Options

D. Entry Points with Controlled Subscriptions 45

1\. ENTRY POINT: DO CONTROL^GECSUFMS1,2,3,4,5,6,7,8)

2\. ENTRY POINT: DO SETCS^GECSSTAA(1,2)

3\. ENTRY POINT: DO SETSTAT^GECSSTAA(1,2)

4\. ENTRY POINT: SET Y=\$\$SELECT^GECSSTAA(1,2,3,4,5)

5\. ENTRY POINT: DO SETCODE^GECSSDCT(1,2)

6\. ENTRY POINT: DO SETPARAM^GECSSDCT(1,2) 48

7\. ENTRY POINT: DO DATA^GECSSGET(1,2)

8\. ENTRY POINT: DO REBUILD^GECSUFM1(1,2,3,4,5)

9\. ENTRY POINT: DO PROCESS^GECSSDCT(1,2)

10\. ENTRY POINT: SET Y=\$\$STATUS^GECSSGET(1)

E. DBA Custodial Agreements

Procedure for Setting up New Code Sheets

A. Create the Fields for the New Code Sheet

1\. Select the Field Numbers

2\. Select the Global Location for Storing the Fields Data 54

B. Create the Fields Output Transform 56
C. Create the Input Template 57
D. Initialize the Code Sheet 58
E. Set up Menu Options

Internal Relations

A. Internal Relationships
B. Internal Calls

Package-wide Variables

On-line Documentation

A. On-line Help
B. Printing Data Dictionaries
C. How to Print the Data Dictionaries (DDs)

Index 77

Revision History

Initiated on 12/22/04

|          |                                                                  |                 |                  |
|----------|------------------------------------------------------------------|-----------------|------------------|
| Date     | Description (Patch \# if applic.)                                | Project Manager | Technical Writer |
| 12/22/04 | Updated to comply with SOP 192-352 Displaying Sensitive Data.    |                 | REDACTED         |
| 12/22/04 | Pdf file checked for accessibility to readers with disabilities. |                 | REDACTED         |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Orientation](#orientation)
  - [DHCP Conventions](#dhcp-conventions)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [A. Naming Conventions](#a-naming-conventions)
  - [B. Files](#b-files)
  - [C. Globals](#c-globals)
  - [D. Resource Requirements](#d-resource-requirements)
  - [E. Security Keys](#e-security-keys)
  - [F. Installation](#f-installation)
  - [G. Parameters](#g-parameters)
  - [H. Mail Groups](#h-mail-groups)
- [Routine Descriptions](#routine-descriptions)
  - [A. Descriptions](#a-descriptions)
  - [B. Mapping Recommendations](#b-mapping-recommendations)
  - [C. Callable Routines](#c-callable-routines)
- [File List](#file-list)
  - [A. Overview](#a-overview)
  - [<u>](#u)
*The SF CIO Field Office added hard page breaks to this document to keep the paging the same when the document was transferred and converted to a different version of MS Word. The TOC was also adjusted to coincide with the original version of this document. No other text/content changes were made.*
The Generic Code Sheet package is a Decentralized Hospital Computer Program (DHCP) software module which manages the input, editing, deletion, and transmission of code sheets from a local hospital computer system to a centralized computer system as defined by the code sheet.
The Generic Code Sheet package contains a code sheet file, GENERIC CODE SHEET (#2100), to be used to define field definitions to support the code sheets. The field definitions describe the type of data to be stored in the actual code sheet. The fields can be arranged in an input template in the order they will be used to create the code sheet.
Once the code sheet data has been created, the code sheets can be marked for batching. Batching the code sheets will group like code sheets together for transmission. When the code sheets are transmitted, all code sheets within the batch will be transmitted in the same VA MailMan message. The exception to this is the Financial Management System (FMS) code sheets. When the FMS code sheets are created they are queued for transmission using the GENERIC CODE SHEET STACK file (#2100.1), thus bypassing the batching process. The code sheets are transmitted from the stack file by a background VA TaskManager job which can be run every 2 hours, 3 hours, etc. as specified by the systems manager.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following conventions are used in this manual:

Bold Shows the User Keyboard Entry. All user entries must be

followed with a RETURN.

\<RET\> Press the Return key or Enter key to accept the default or to bypass the prompt.

Throughout the entire Generic Code Sheet package, you will always be able to enter a question mark (?) to obtain on-line information to assist you in your choice of actions at any prompt. Enter two question marks (??) for more detailed help.

## DHCP Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following conventions are used within DHCP packages:

JUMP MARK- ^

DEFAULT MARKS - //

SPACE BAR RETURN

REPLACE/WITH

EDITING

DELETE MARK - @

HALTING

a\. The JUMP MARK^ can be used in several ways:

The JUMP MARK^ used alone takes you back one menu level at a time.

The ^ used with a field name allows you to skip directly forward or backward to that field prompt within an option.

The ^ can be used with any 3-letter option code at any "Select Option" prompt to move quickly from one part of the Module to another.

A double JUMP MARK^^ allows you to "rubber band" from the option where you are working to another option and then return back to the original option/prompt.

b\. Using SPACE BAR\<RET\> at any option will pull up the last option you used. When used at a prompt, it will re-enter the last information entered at that prompt. For example, if you have just edited a record for Doe,John and wish to verify the changes, you can enter SPACEBAR\<RET\> at the "Name" prompt instead of re-entering the name.

c\. EDITING means changing or altering data already entered. It does not mean deleting data altogether, leaving the field empty. There are some places where data may be either edited or deleted; there are other places where data may be edited only, not deleted. The system will tell you which actions are appropriate.

d\. The @ DELETE MARK will delete a line of data previously entered. As a safeguard the system will always ask if you really want to delete the data.

f\. The // marks to indicate that anything immediately to the left of those marks is the DEFAULT choice; if the data is satisfactory, it can be accepted with just a \<RET\>.

If the data is not correct, simply enter replacement data to the right of the double slashes //, then the \<RET\>, and the new data will be substituted for the old.

g\. The "REPLACE...WITH" function is used to allow the correction or substitution of data in entries which are longer than 20 characters. The system allows fragmented replacement so that editing would appear as follows:

NAME: BUILDING MANAGEMENT SERVICE Replace BUILDING\<RET\> With ENVIRONMENTAL\<RET\> Replace\<RET\>

The system will then redisplay:

ENVIRONMENTAL MANAGEMENT SERVICE

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. Naming Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace assigned to the Generic Code Sheet package is GEC. All routines are located in the GECS namespace except for the initialization routines which begin with GECI. The only global exported as part of the Generic Code Sheet package is GECS. Namespaced variables of special note are listed in the Package-wide Variable section of the manual.

## B. Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Generic Code Sheet package exports and uses the following files:

2100 GENERIC CODE SHEET

2100.1 GENERIC CODE SHEET STACK

2101.1 GENERIC CODE SHEET BATCH TYPE

2101.2 GENERIC CODE SHEET TRANSACTION

TYPE/SEGMENT

2101.3 GENERIC CODE SHEET TRANSMISSION RECORD

2101.4 GENERIC CODE SHEET TEMPLATE MAPS (not used)

2101.5 GENERIC CODE SHEET COUNTER

2101.6 GENERIC CODE SHEET LOCK

2101.7 GENERIC CODE SHEET SITE

The File List section of this manual provides additional file information.

## C. Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Generic Code Sheet package uses the namespaced ^GECS global to store all data. Journalling is recommended for the ^GECS global.

## D. Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The executable routines located in the GECS namespace will take approximately 100 Kbytes of disk space. The package initialization routines located in the GECI namespace will take approximately 2600 Kbytes of disk space, and can be deleted

after package installation. Please read and carefully follow the instructions in the Installation Guide.

The GENERIC CODE SHEET file (#2100) and GENERIC CODE SHEET STACK file (#2100.1) can grow significantly depending on the number of documents entered. It is recommended that unused code sheets be purged on a regular basis using the Purge Transmission Records/Code Sheets option. For information on purging old code sheets, please refer to the Archiving and Purging chapter of this manual.

## E. Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GECS SETUP key should be given to the systems manager. This key allows access to the Initialize a Code Sheet Type and Purge Transmission Records/Code Sheets options located on the Maintenance Menu under the GECS MAIN MENU.

## F. Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For installation instructions of the Generic Code Sheet package, please refer to the Installation Guide.

## G. Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to implement the Generic Code Sheet package, you need to first set up the GENERIC CODE SHEET SITE file (#2101.7). This can be done either by using VA FileMan or through the Initialize a Code Sheet option. Below is an example of using VA FileMan:

VA FileMan 20.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: GENERIC CODE SHEET SITE

EDIT WHICH FIELD: ALL//\<RET\>

Select GENERIC CODE SHEET SITE NAME: ANYPLACE,ANYWHERE

.OK? YES// YES

NAME: ANYPLACE,ANYWHERE// \<RET\>

PRIMARY SITE?: YES// \<RET\>

If the GENERIC CODE SHEET SITE file (#2101.7) only has one site entry, the site will automatically be selected when the user uses the Generic Code Sheet package. If more than one site entry is contained in the file, the user will be asked to select the site name. If one of the entries is set up as the PRIMARY SITE, that site name will be the default selection.

## H. Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It may be necessary to create mail groups which will be used to transmit code sheets in VA MailMan messages and receive confirmation messages. The code sheets and confirmation messages are transmitted to the mail group as defined by the DOMAIN MAIL ROUTER sub-field in the GENERIC CODE SHEET BATCH file (#2101.1). For example, the VOLUNTARY batch type has the RECEIVING USER and DOMAIN MAIL ROUTER equal to XXX@Q-NST.VA.GOV. The VOLUNTARY code sheets and confirmation messages will be sent to the mail group NST.

To determine the mail groups which need to be set up, run the program GECSVFY from programmer’s mode as follows (Note: only part of the report is printed below):

\>D ^GECSVFY

Do you want to check the batch types for errors? YES//\<RET\>

When a discrepancy is found, do you want me to try and fix it? NO//\<RET\>

------------------------------------------------------------------------

checking batch type: ACCOUNTS RECEIVABLE

1\. ERROR -- THE MAIL GROUP ‘AMD’ NEEDS TO BE SET UP.

------------------------------------------------------------------------------------------------------------------------------

...

------------------------------------------------------------------------------------------------------------------------------

checking batch type: CONSULTING/ATTENDING

1\. ERROR -- THE MAIL GROUP ‘CAA’ NEEDS TO BE SET UP.

------------------------------------------------------------------------------------------------------------------------------

...

# Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Generic Code Sheet package Version 2.0 is composed of 46 executable routines in the GECS namespace and approximately 678 initialization routines in the GECI namespace. The GECI\* routines can be deleted after package installation.

The following is a list of the executable routines and descriptions:

ROUTINE DESCRIPTION

-------- ---------------------------------------------------------------

GECSA old version 1.5 routine

GECSBATC batch code sheets

GECSCALL calls to various options

GECSDG pims dggecsb patch routine (for PIMS 5.3\*47)

GECSE old version 1.5 routine

GECSE1 old version 1.5 routine

GECSE2 old version 1.5 routine

GECSEDIT create and edit code sheets

GECSENTR stuff data into template map automatically

GECSETUP initialize a code sheet

GECSLIST old version 1.5 routine

GECSMUT1 maintenance utilities (batching)

GECSMUT2 maintenance utilities

GECSNTEG Package checksum checker

GECSPOS1 version 2 post-init, install PIMS patch 5.3\*47)

GECSPOST version 2 post-init

GECSPPRE version 2 pre-init

GECSPUR1 purge code sheets (purge routine)

GECSPURG purge code sheets (ask prompts)

GECSREP0 reports

GECSRST1 stack reports (print)

GECSRSTA stack reports

GECSSCOM stacker file enter user comments

GECSSDCT dct accept, reject message utilities

GECSSGET get data from stack file

GECSSITE get site, fy, person data

GECSSTAA stacker file utilities

GECSSTT1 stacker file retransmission

GECSSTTM stacker file transmission (multi docs in a msg)

GECSSTTR stacker file transmission (one doc per msg)

GECSSTTT stacker file transmission routine

GECSTRAN transmit a batch

GECSUFM1 FMS utilities: rebuild rejects

GECSUFMS utilities

GECSULOC lock system

GECSUNUM get next counter number

GECSUSEL utility selection

GECSUSTA code sheet status utilities

GECSUTIL code sheet utilities

GECSVFY verify and check code sheet parameters

GECSVFY0 verify and check code sheet parameters

GECSVFY1 verify and check code sheet parameters (check)

GECSX5 old version 1.5 routine

GECSXBL1 ask to mark code sheets for batching

GECSXBLD map data into template map

GECSXMAP build template map

## B. Mapping Recommendations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are used extensively by the package and should be mapped if possible (a \* denotes all routines beginning with this name):

GECSBATC

GECSCALL

GECSEDIT

GECSENTR

GECSM\*

GECSPU\*

GECSR\*

GECSS\*

GECST\*

GECSU\*

GECSXB\*

## C. Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the list of callable routines, please refer to the Callable Routine Chapter of this manual.

# File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GENERIC CODE SHEET file (#2100) is used to store the actual code sheets which have been automatically created by the system (except for the Financial Management code sheets which are placed in the GENERIC CODE SHEET STACK file (#2100.1)) or manually created by the user. This file contains all the fields and input templates which are used to create the code sheets. The fields are used to define the data which appears on the code sheet. The input templates define the order the fields should appear on the code sheets and the order the fields should be asked to the user.

The GENERIC CODE SHEET STACK file (#2100.1) is used to store the Financial Management System (FMS) code sheets which are ready for transmission. When a user manually creates and marks an FMS code sheet for transmission, it is moved to the GENERIC CODE SHEET STACK file (#2100.1). When the system automatically creates an FMS code sheet, it is automatically entered into the GENERIC CODE SHEET STACK file (#2100.1) bypassing the GENERIC CODE SHEET file (#2100). The code sheets are transmitted from the stack file and the STATUS field (#3) is used to monitor the code sheet's progress.

The GENERIC CODE SHEET BATCH TYPE file (#2101.1) is used to store the name of the application, service, or code sheet type, for example Dental, MAS, Financial Management, etc. The GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT file (#2101.2) is used to store the name of each individual code sheet. The two files are linked using the BATCH TYPE Field (#.7) in the GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT file (#2101.2). This allows each individual code sheet to be grouped under an application, service, or code sheet type. Both of these files are exported with data.

The GENERIC CODE SHEET TRANSMISSION RECORD

## <u>  
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

</u>

## ## ## # ## ## |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |

## |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

# ## ## # # ## ## ## ### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |

### |     |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|-----|
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |

|     |     |     |
|-----|-----|-----|
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |
|     |     |     |

## ### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |

### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |

### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |

### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |

### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |

|     |     |     |     |
|-----|-----|-----|-----|
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |

### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |

### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |

### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |

### |     |     |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|-----|-----|
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |

### |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |

## # ## ### ### |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|
|     |

## |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|
|     |

## |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|
|     |

## |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|
|     |

## # ## ## |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |

# |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |

# ## ## ## # |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

# #
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)