---
title: VIAB*1*14 DIBRO
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: DIBRO
app_code: VIAB
app_name: VistA Integration Adapter (VIA)
section: CLI
app_status: active
pkg_ns: VIAB
patch_ver: 1
patch_id: VIAB*1*14
group_key: "VIAB:VIAB:1"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - installation
  - patch
  - viab
  - table
  - contents
  - install
  - instructions
  - procedure
  - rollback
  - description
page_count: 0
word_count: 2624
section_count: 12
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/VistA_Integration_Adapter_(VIA)/viab_1_14_installation_back-out_rollback_plan_release_notes.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/VistA_Integration_Adapter_(VIA)/viab_1_14_installation_back-out_rollback_plan_release_notes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=221"
---

VistA Integration Adapter (VIA)VIAB 1\*14

Installation, Back-out and Rollback Plan/RELEASE NOTES

![](viab-1-14-dibro/001.png)

March 2019Version 1.0

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the Installation, Back-out, Rollback Plan/RELEASE NOTES has been baselined.

| Date       | Version | Description            | Author                                                                                      |
|------------|---------|------------------------|---------------------------------------------------------------------------------------------|
| March 2019 | 1.0     | Updated for VIAB 1\*14 | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |

Revision History includes date of changes, version number, description of changes, and author of revisions.

Artifact Rationale

The Installation, Back-out, Rollback Plan/ RELEASE NOTES defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Documentation and Distribution](#documentation-and-distribution)
- [System Requirements](#system-requirements)
- [Patch description and Installation Instructions](#patch-description-and-installation-instructions)
  - [Patch Description](#patch-description)
  - [Pre-Installation Instructions](#pre-installation-instructions)
  - [Installation Instructions](#installation-instructions)
  - [Post-Installation Instructions](#post-installation-instructions)
  - [KIDS Installation Example](#kids-installation-example)
- [Backout and Rollback Procedure](#backout-and-rollback-procedure)
  - [Overview of Backout and Rollback Procedures](#overview-of-backout-and-rollback-procedures)
  - [Backout Procedure](#backout-procedure)
- [Rollback Procedure](#rollback-procedure)
- [RELEASE NOTES](#release-notes)
  - [Bed Management System (BMS) Date/Time Changes](#bed-management-system-bms-datetime-changes)
  - [VIAB GET IMMUNIZATION TYPE RPC Entry](#viab-get-immunization-type-rpc-entry)
  - [VIA WEB SERVICE OPTION (Broker) Option](#via-web-service-option-broker-option)
This document provides installation instructions for VIAB 1\*14, as managed through the VistA Integration Adapter project. All installation and back-out instructions must be documented in the Installation Plan, unless the operations documents specific tasks in Change Orders in the Change Management system and uses installation scripts to install a product. The Installation Plan always includes details of items that cannot be covered in Change Orders or installation scripts, including the criteria for determining if a back-out is necessary, the authority for making that decision, the order in which installed components will be backed out, the risks and criteria for a rollback, and authority for acceptance or rejection of the risks.
This VIAB patch introduces changes to the legacy VIA package Modules.
APPLICATION/VERSION PATCH
--------------------------------------------------------------------------------------------------------
VistA Integration Adapter V. 1.0 VIAB 1\*14
This patch (VIAB 1\*14) is being released in the Kernel Installation and Distribution System (KIDS) distribution.

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIAB 1\*14 patch is being released via the Kernel Installation and Distribution System (KIDS).

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/application.asp?appid=221>

# System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no hardware interface features introduced with this project.

These enhancements are compatible with existing hardware. No hardware issues are involved with these enhancements.

# Patch description and Installation Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=============================================================================

Run Date: MAR 13, 2019 Designation: VIAB\*1\*14 TEST v2

Package : VISTA INTEGRATION ADAPTOR Priority : EMERGENCY

Version : 1 Status : UNDER DEVELOPMENT

=============================================================================

Associated patches: (v)VIAB\*1\*13 \<\<= must be installed BEFORE \`VIAB\*1\*14'

Subject: VIAB MISCELLANEOUS MODIFICATIONS

Category: ROUTINE

OTHER

Description:

===========

The VistA integration Adaptor (VIA) system is a middleware used to

transport clinical and non-clinical electronic information between

producing and consuming applications in VA systems. VIA utilizes remote

procedure calls (RPCs) for data requested by consuming applications.

This patch contains modifications for immunization functionality for the

Customer Relationship Management (CRM) team. This patch also contains a

modification to the "LISTSCHEDULEDADMISSION" target of VIABMS, used by

the Bed Management System (BMS).

The updates for this patch are:

1\. The semantics of SDATE (start date) and EDATE (end date) in the

LISTSCHEDULEDADMISSION target of VIABMS (only) is modified as follows:

\* SDATE and EDATE are mandatory and represent date/time values, even if

the date is exact.

\* The range returned is the inclusive range of times (not days)

between SDATE and EDATE. (Note that this is different from the

behavior of some other targets of the same RPC.)

2\. VIAB GET IMMUNIZATION TYPE RPC entry in the REMOTE PROCEDURE

File (#8994) is populated with additional documentation information.

3\. Reconcile the VIAB WEB SERVICES OPTION option with the list of RPCs

that VIA has permission to use with the ICRs that were approved.

Patch Components:

-----------------

Files & Fields Associated:

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------ ------------------- --------------------

N/A

Forms Associated:

Form Name File Number New/Modified/Deleted

--------- ----------- --------------------

N/A

Mail Groups Associated:

Mail Group Name New/Modified/Deleted

--------------- --------------------

N/A

Options Associated:

Option Name Type New/Modified/Deleted

--------------- ----------- --------------------

VIAB WEB SERVICES OPTION Broker (Client/Server) Modified

Protocols Associated:

Protocol Name New/Modified/Deleted

------------- --------------------

N/A

Security Keys Associated:

Security Key Name

-----------------

N/A

Templates Associated:

Template Name Type File Name (Number) New/Modified/Deleted

------------- ---- ------------------ --------------------

N/A

Remote Procedures Associated:

Remote Procedure Name New/Modified/Deleted

--------------------- --------------------

VIAB GET IMMUNIZATION TYPE Modified

Parameter Definitions Associated:

Parameter Name New/Modified/Deleted

-------------- --------------------

N/A

Additional Information:

-----------------------

New Service Requests (NSRs):

N/A

Patient Safety Issues (PSIs):

N/A

Defect Tracking System Ticket(s) & Overview:

1\. INC3239832 - Scheduled Admissions coming over from VistA on wrong day.

Problem:

--------

When start date and end date were passing as midnight dates to return one

full days’ worth of scheduled admissions, two full days of scheduled

admissions were returning.

Resolution:

--------

Call to DTCHK^VIABMS1 has been commented out.

Test Sites:

-----------

North Texas Veterans Health Care System

Indianapolis VA Medical Center

Software and Documentation Retrieval Instructions:

--------------------------------------------------

Documentation describing the new functionality and/or a host file

containing a build may be included in this release.

The preferred method is to retrieve the files from

[*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp). This transmits the files from the first

available server. Sites may also elect to retrieve the files

directly from a specific server.

Sites may retrieve the software and/or documentation directly using

Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE

directory at the following OI Field Offices:

[*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp)

Documentation can also be found on the VA Software Documentation

Library at: http://www.va.gov/vdl/application.asp?appid=221

Documentation Title File Name FTP Mode

---------------------------------------------------------------------

N/A

Host File Name FTP Mode

---------------------------------------------------------------------

N/A

Patch Installation:

-------------------

Pre/Post Installation Overview:

This patch contains pre installation instructions.

Pre-Installation Instructions:

This patch may be installed with users on the system. This patch should

take less than 5 minutes to install.

No menu options need to be disabled.

Installation Instructions:

1\. This release is provided using PackMan, choose the PackMan

message containing this build. Select the INSTALL/CHECK MESSAGE

PackMan option to load the build.

2\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu,

A. Select the Verify Checksums in Transport Global option to

confirm the integrity of the routines that are in the transport

global. When prompted for the INSTALL NAME enter the patch or

build name VIAB\*1\*14.

B. Select the Backup a Transport Global option to create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

C. You may also elect to use the following options:

i\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

ii\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this

patch is installed. It compares all of the components of

this patch, such as routines, DDs, templates, etc.

D. Select the Install Package(s) option and choose the patch

(VIAB\*1\*14) to install.

i\. If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion

of Install? YES//', press \<ENTER\>.

ii\. When prompted 'Want KIDS to INHIBIT LOGONs during the

install? NO//', press \<ENTER\>.

iii\. When prompted 'Want to DISABLE Scheduled Options, Menu

Options and Protocols? NO//', press \<ENTER\>.

a\. When prompted 'Enter options you wish to mark as 'Out

Of Order':', press the Enter key.

b\. When prompted 'Enter protocols you wish to mark as 'Out

Of Order':', press the Enter key.

c\. When prompted 'Delay Install (Minutes): (0 - 60): 0//',

answer 0.

Post-Installation Instructions:

-------------------------------

N/A

Routine Information:

====================

The second line of each of these routines now looks like:

;;1.0;VISTA INTEGRATION ADAPTER;\*\*\[Patch List\]\*\*;06-FEB-2014;Build 17

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: VIABMS1

Before:B102618166 After:B103511639 \*\*8,11,13,14\*\*

Routine list of preceding patches: 13

=============================================================================

[*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp)

=============================================================================

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch VIAB 1\*13 must be installed prior to installation of VIAB 1\*14.

This patch may be installed with users on the system. This patch should take less than 5 minutes to install.

No menu options need to be disabled.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

1\. This release is provided using PackMan, choose the PackMan

message containing this build. Select the INSTALL/CHECK MESSAGE

PackMan option to load the build.

2\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu,

A. Select the Verify Checksums in Transport Global option to

confirm the integrity of the routines that are in the transport

global. When prompted for the INSTALL NAME enter the patch or

build name VIAB\*1\*14.

B. Select the Backup a Transport Global option to create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

C. You may also elect to use the following options:

i\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

ii\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this

patch is installed. It compares all of the components of

this patch, such as routines, DDs, templates, etc.

D. Select the Install Package(s) option and choose the patch

(VIAB\*1\*14) to install.

i\. If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion

of Install? YES//', press \<ENTER\>.

ii\. When prompted 'Want KIDS to INHIBIT LOGONs during the

install? NO//', press \<ENTER\>.

iii\. When prompted 'Want to DISABLE Scheduled Options, Menu

Options and Protocols? NO//', press \<ENTER\>.

a\. When prompted 'Enter options you wish to mark as 'Out

Of Order':', press the Enter key.

b\. When prompted 'Enter protocols you wish to mark as 'Out

Of Order':', press the Enter key.

c\. When prompted 'Delay Install (Minutes): (0 - 60): 0//',

answer 0.

Routine Information:

====================

The second line of each of these routines now looks like:

;;1.0;VISTA INTEGRATION ADAPTER;\*\*\[Patch List\]\*\*;06-FEB-2014;Build 17

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: VIABMS1

Before:B102618166 After:B103511639 \*\*8,11,13,14\*\*

Routine list of preceding patches: 13

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

------------------------------

N/A

## KIDS Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

------------------------------

Select Installation \<TEST ACCOUNT\> Option:

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INstallation

Select Installation \<TEST ACCOUNT\> Option: INstall Package(s)

Select INSTALL NAME:    VIAB\*1.0\*14    3/12/19@10:04:31

     =\> VIAB\*1\*14 TEST v2

This Distribution was loaded on Mar 12, 2019@10:04:31 with header of

   VIAB\*1\*14 TEST v2

   It consisted of the following Install(s):

    VIAB\*1.0\*14

Checking Install for Package VIAB\*1.0\*14

Install Questions for VIAB\*1.0\*14

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// Yes

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   UCX/TELNET

                                                            VIAB\*1.0\*14                                                            

------------------------------------------------------------------------------------------------------------------------------------

 Installing REMOTE PROCEDURE

 Installing OPTION

 Updating Routine file...

 Updating KIDS files...

 VIAB\*1.0\*14 Installed.

               Mar 12, 2019@10:20:45

 Not a production UCI

 NO Install Message sent

------------------------------------------------------------------------------------------------------------------------------------

          +------------------------------------------------------------+

  100%    ¦             25             50             75               ¦

Complete  +------------------------------------------------------------+

Install Completed

# Backout and Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a “one size fits all.” The general strategy for VistA rollback is to repair the code with a follow-on patch. The development team recommends that sites contact Enterprise Service Desk and log a ServiceNow ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific solutions to their unique problems.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer should have backed up the modified routines by the use of the ‘Backup a Transport Global’ action as specified in the Patch Description Installation Instructions.  The installer can restore the routines using the MailMan message that were saved prior to installing the patch.  The backout procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-on patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data.  This backout may need to include a database cleanup process.

Please contact the product development team for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to backout the patch.  If the installed patch that needs to be backed out includes a pre or post install routine please contact the product development team before attempting the backout.

From the Kernel Installation and Distribution System Menu, select

the Installation Menu.  From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch \#.

    a. Backup a Transport Global - This option will create a backup

       message of any routines exported with this patch. It will not

       backup any other changes such as DD's or templates.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for VistA patches is complicated and may require a follow-on patch to fully roll back to the pre-patch state. This is due to RPCs update and menu options updates.

Please contact the product development team for assistance if needed.

# RELEASE NOTES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following features in VIA are affected by this effort:

- Bed Management System (BMS) Date/Time Changes
- VIAB GET IMMUNIZATION TYPE RPC Entry
- VIAB WEB SERVICE OPTION (Broker)

## Bed Management System (BMS) Date/Time Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The range returned between SDATE and EDATE (which are mandatory) was modified to be an inclusive range of times (not days).

## VIAB GET IMMUNIZATION TYPE RPC Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement is the addition of documentation information entered into the REMOTE PROCEDURE File (#8994).  
  
<u>Before:</u>

NAME: VIAB GET IMMUNIZATION TYPE        TAG: IMMTYPE

  ROUTINE: VIABRPC                      RETURN VALUE TYPE: ARRAY

  AVAILABILITY: RESTRICTED              APP PROXY ALLOWED: Yes

RETURN PARAMETER DESCRIPTION:  

 Returns a list of active immunizations.

<u>After:</u>

NAME: VIAB GET IMMUNIZATION TYPE        TAG: IMMTYPE

  ROUTINE: VIABRPC                      RETURN VALUE TYPE: ARRAY

  AVAILABILITY: RESTRICTED              APP PROXY ALLOWED: Yes

DESCRIPTION:  

 Returns a list of active immunizations.

INPUT PARAMETER: RESULT                 PARAMETER TYPE: REFERENCE

  REQUIRED: YES                         SEQUENCE NUMBER: 1

DESCRIPTION:  

 This field is passed by reference and this RPC populates the field with

 immunization information.

INPUT PARAMETER: VIACVXS                PARAMETER TYPE: LITERAL

  REQUIRED: NO                          SEQUENCE NUMBER: 2

DESCRIPTION:  

 One or more CVX CODE(s) separated by commas to be retrieved.

RETURN PARAMETER DESCRIPTION:  

 Returns a list of active immunizations from IMMUNIZATIONS file

 (#9999999.14).

 

 Example:

 

   D IMMTYPE^VIABRPC(.RESULT,VIACVXS)

 

    Returns: Immunization IEN^SHORT NAME^CVX Code^CPT CODE^CPT Description

 

 RESULT(1)="71^INFLUENZA, HIGH DOSE SEASONAL^135^90662^FLU VACC PRSV FREE

 INC ANT IG"

RESULT(2)="1140^INFLUENZA, SEASONAL, INJECTABLE, PRESERVATIVE

 FREE^140^90656^FLU VACCINE NO PRESERV 3 & \>"

RESULT(3)="72^PNEUMOCOCCAL CONJUGATE PCV 13^133^90670^PNEUMOCOCCAL VACC 13

VAL I M"

VAL I M"

## VIA WEB SERVICE OPTION (Broker) Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reconcile the VIAB WEB SERVICE OPTION option with the list of RPCs that

VIA has permission to use with the ICRs that were approved.