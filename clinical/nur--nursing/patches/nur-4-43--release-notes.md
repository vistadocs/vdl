---
title: NUR*4*43 PAID Enhancements for VANOD Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: PAID Enhancements for VANOD
app_code: NUR
app_name: Nursing
section: CLI
app_status: active
pkg_ns: NUR
patch_ver: 4
patch_id: NUR*4*43
group_key: "NUR:NUR:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patch
  - table
  - contents
  - nursing
  - vanod
  - span
  - installation
  - modified
  - location
  - unit
page_count: 0
word_count: 1117
section_count: 5
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nursing/nurs_4_p43_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nursing/nurs_4_p43_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=80"
---

---
title: PAID Enhancements for VANOD
---

####### RELEASE NOTES

NUR\*4\*43

March 2012

VISTA Health  
Systems Design & Development

![Table of Contents](nur-4-43-paid-enhancements-for-vanod-release-notes/001.png)

*Table of Contents*

This page intentionally left blank.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Patch Description and Installation Instructions](#patch-description-and-installation-instructions)
  - [Patch Description](#patch-description)
  - [Installation Instructions](#installation-instructions)
- [Enhancements](#enhancements)
  - [Technical Modifications](#technical-modifications)
    - [Functional Requirement: Option Enter Nurse POC Data](#functional-requirement-option-enter-nurse-poc-data)
  - [Issue Resolutions](#issue-resolutions)
This patch supports patch PRS\*4\*126--PAID ENHANCEMENTS FOR VANOD. This
Patch -- NUR\*4\*43 -- must be installed prior to patch PRS\*4\*126. This patch provides for the ability to enter and store additional information for Nursing Locations that is required by the
Veterans Affairs Nursing Outcomes Database (VANOD) in accordance with Public Law 107-135 and the OIG Recommendation 4a (annual reporting requirement).
| APPLICATION/VERSION | PATCH   |
|-------------------------|-------------|
| NURSING SERVICES v4     | NUR\*4\*43  |
| PAID v4                 | PRS\*4\*126 |
|                         |             |
This page intentionally left blank.

# Patch Description and Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc301346253" class="anchor"></span>VistA Patch Display Page: 1

=============================================================================

Run Date: FEB 29, 2012 Designation: NUR\*4\*43 TEST v19

Package : NURSING SERVICE Priority : MANDATORY

Version : 4 Status : UNDER DEVELOPMENT

=============================================================================

Subject: NEW FUNCTIONS FOR PAID ENHANCEMENTS FOR VANOD

Category: DATA DICTIONARY

INPUT TEMPLATE

ROUTINE

OTHER

ENHANCEMENT

Description:

===========

This patch supports patch PRS\*4.0\*126--PAID ENHANCEMENTS FOR VANOD. This patch--NUR\*4.0\*43--must be installed prior to patch PRS\*4.0\*126. This patch provides for the ability to enter and store additional information for Nursing Locations that is required by the VANOD (Veterans Affairs Nursing Outcomes Database) in accordance with Public Law 107-135 and the OIG Recommendation 4a (annual reporting requirement).

The enhancements made by this patch are summarized below:

---------------------------------------------------------

The option Nursing Location File, Edit \[NURSFL-LOC\] has been updated to provide entry and storage of the following additional data elements to describe a nursing location:

1.  CARE SETTING, Inpatient or Other
2.  UNIT TYPE: The unit type can be selected from a list of types defined by VANOD and stored in the new file VANOD UNIT TYPES (#212.8)
3.  INPATIENT DSS DEPARTMENT: a free text field to be defined by VANOD
4.  POC DATA ENTRY PERSONNEL: VistA User responsible for entering POC data for the Nursing Location
5.  POC DATA APPROVAL PERSONNEL: VistA User responsible for approving POC data for the Nursing Location

Patch Components

================

Files & Fields Associated:

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------ ------------------- --------------------

NURS LOCATION

(#211.4) CARE SETTING (#.5) Modified

(#211.4) UNIT TYPE (#.6) Modified

(#211.4) INPATIENT DSS

DEPARTMENT (#.7) Modified

(#211.414) POC DATA ENTRY

PERSONNEL (#.01) Modified

(#211.415) POC DATA APPROVAL

PERSONNEL (#.01) Modified

(#211.416) SERVICE DATE (#.01) Modified

(#211.416) STATUS (#1) Modified

NURS POSITION CONTROL

(#211.82) PRIMARY

ASSIGNMENT (#6) Modified

VANOD UNIT TYPES

(#212.8) UNIT TYPE

NAME (#.01) New

UNIT TYPE

DEFINITION (#1) New

SETTING (#2) New

Templates Associated:

Template Name Type File Name (Number) New/Modified/Deleted

------------- ---- ------------------ --------------------

NURS-I-PRIORITY 1A INPUT NURS LOCATION (#211.4) Modified

Test Sites:

-----------

<span class="mark">REDACTED</span>

Documentation Retrieval Instructions

------------------------------------

Updated documentation describing the new functionality introduced by this patch is available.

The preferred method is to FTP the files from <span class="mark">REDACTED</span>

. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at: http://www.va.gov/vdl/

Title File Name FTP Mode

-----------------------------------------------------------------------

Nursing User Manual NURS_4_P43_UM_CP.PDF (binary)

\- Change Pages

Release Notes NURS_4_P43_RN.PDF (binary)

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system; however, it should be installed at a non-peak time to minimize disruption to the users. It is strongly recommended that all the NURSING SERVICE options in the OPTION (#19) file be disabled to prevent possible conflicts while running the KIDS install.

All the NURSING SERVICE options can be selected by using the namespace of NUR\*, to disable all NURSING SERVICE options. Other VISTA users will not be affected.

Pre-Installation Instructions

-----------------------------

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following option. When prompted for the INSTALL enter the patch NUR\*4.0\*43:
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' Answer NO
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' Answer NO
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' Answer YES

When prompted 'Enter options you wish to mark as 'Out Of Order':' Answer NUR\*

When prompted 'Enter protocols you wish to mark as 'Out Of Order':' Press Return

8.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' Answer 0

Post-Installation Instructions

------------------------------

The post install routine NURXP43 will build the new indexes required.

Routine Information:

====================

The second line of each of these routines now looks like:

;;4.0;NURSING SERVICE;\*\*\[Patch List\]\*\*;APR 25, 1997;Build 19

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

Routine Name: NURSUT6

Before: n/a After: B967330 \*\*43\*\*

Routine Name: NURXP43

Before: n/a After: B1845464 \*\*43\*\*

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Functional Requirement: Option Enter Nurse POC Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Nursing Location File, Edit \[NURSFL-LOC\] has been updated to provide entry and storage of the following additional data elements to describe a nursing location:

1.  CARE SETTING, Inpatient or Other
2.  UNIT TYPE: The unit type can be selected from a list of types defined by VANOD and stored in the new file VANOD UNIT TYPES (#212.8)
3.  INPATIENT DSS DEPARTMENT: a free text field to be defined by VANOD
4.  POC DATA ENTRY PERSONNEL: VistA User responsible for entering POC data for the Nursing Location
5.  POC DATA APPROVAL PERSONNEL: VistA User responsible for approving POC data for the Nursing Location

## Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no New Service Requests (NSRs) or Remedy Tickets associated with this patch.