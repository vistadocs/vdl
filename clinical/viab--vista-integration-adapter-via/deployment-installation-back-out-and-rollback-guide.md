---
consolidated_title: "dibr"
app_code: VIAB
doc_type: DIBR
master_source: "VIAB*1*9 DIBR"
master_pub_date: April 2017
consolidated_from: 2 versions
prior_versions:
  - "VIAB*1*15 DIBR"
---

VistA Integration Adapter (VIA)VIAB 1\*9

Installation, Back-out, and Rollback Plan

![](viab-1-9-dibr/001.png)

April 2017Version 0.3

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the Installation, Back-out, Rollback Plan has been baselined.

| Date       | Version | Description            | Author                                                                                      |
|------------|---------|------------------------|---------------------------------------------------------------------------------------------|
| April 2017 | 0.3     | Updated for VIAB 1\*9  | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| March 2017 | 0.2     | Updated for VIAB 1\*10 | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| March 2017 | 0.1     | Initial Version        | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |

Revision History includes date of changes, version number, description of changes, and author of revisions.

Artifact Rationale

The Installation, Back-out, Rollback Plan defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product.

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
- [Backout and Rollback Procedure](#backout-and-rollback-procedure)
  - [Overview of Backout and Rollback Procedures](#overview-of-backout-and-rollback-procedures)
  - [Backout Procedure](#backout-procedure)
- [Rollback Procedure](#rollback-procedure)
This document provides installation instructions for VIAB 1\*9, as managed through the VistA Integration Adapter project. All installation and back-out instructions must be documented in the Installation Plan, unless the operations shop documents specific tasks in Change Orders in the Change Management system and uses installation scripts to install a product. The Installation Plan always includes details of items that cannot be covered in Change Orders or installation scripts, including the criteria for determining if a back-out is necessary, the authority for making that decision, the order in which installed components will be backed out, the risks and criteria for a rollback, and authority for acceptance or rejection of the risks.
> **NOTE:** If any section of this template does not apply to the product, please indicate N/A in that section.
This VIAB patch introduces changes to the legacy VIA package Modules.
APPLICATION/VERSION PATCH
--------------------------------------------------------------------------------------------------------
VistA Integration Adapter V. 1.0 VIAB 1\*9
This patch (VIAB 1\*9) is being released in the Kernel Installation and Distribution System (KIDS) distribution.

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIAB 1\*9 patch is being released via the Kernel Installation and Distribution System (KIDS).

<span id="_Toc469313774" class="anchor"></span>

# System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no hardware interface features introduced with this project.

These enhancements are compatible with existing hardware. No hardware issues are involved with these enhancements.

# Patch description and Installation Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch Display Page: 1

=============================================================================

Run Date: APR 03, 2017 Designation: VIAB 1\*9 TEST v

Package : VISTA INTEGRATION ADAPTOR Priority : MANDATORY

Version : 1 Status : UNDER DEVELOPMENT

=============================================================================

Subject: VIA INCREMENT 5 UPDATES

Category: ROUTINE

Description:

===========

The VistA integration Adaptor (VIA) system is a middleware used to transport

clinical and non-clinical electronic information between producing and

consuming applications in VA systems. VIA utilizes remote procedure calls

(RPCs) for data requested by consuming applications.

The purpose of this patch is to publish RPCs that were added to the VIAB WEB

SERVICES OPTION in the OPTION file (#19), RPC field (#320).

Several new RPCs were created to meet the needs of consuming applications.

VIAB ADMIN This RPC returns administration time information: -

StartText^StartTime^Duration^FirstAdmin

VIAB ALLSAMP This RPC returns all collection samples in the format:

n^SampIEN^SampName^SpecPtr^TubeTop^^^LabCollect^^SpecName

VIAB ALLSPEC This RPC returns a list of specimens from the TOPOGRAPHY

FIELD file (#61).

VIAB DEA SIGINFO This RPC returns provider/patient info that must be

displayed when signing a controlled substance order(s).

VIAB DEATEXT This RPC returns the text to show on the signature

dialog mandated by DEA for when a controlled substance

order is selected to be signed.

VIAB DEVICE This RPC returns a list of print devices.

VIAB DFLTSPLY This RPC returns days supply given quantity.

VIAB DOWSCH This RPC returns a list of schedule that have a frequency

defined and the frequency is less than or equal to 1440

minutes.

VIAB EFR This RPC supports request for data from the Embedded

Fragment Registry (EFR) project. Data is returned from

RESEARCH File \#67.1 and LAB DATA File \#63.04.

VIAB FUTURE LAB This RPC returns the number of days in the future to

COLLECTS allow lab collects.

VIAB GET IMMUNIZATION TYPE

This RPC returns a list of active immunizations.

VIAB GET LAB This RPC returns a list of lab collect times for a date

TIMES and location.

VIAB IC VALID This RPC determines whether the supplied time is a valid

lab immediate collect time.

VIAB IMMED COLLECT This RPC returns help text showing lab immediate collect

times for the user's division.

VIAB IMOLOC This RPC returns - Is it an IMO order?

VIAB IMTYPSEL This RPC returns data associated with imaging types.

VIAB INPLOC This RPC returns a list of wards from the HOSPITAL

LOCATION file.

VIAB ISPROSVC This RPC returns 1 or 0 if the input IEN in File \#123.5

is marked as part of the Consults-Prosthetics interface.

VIAB LOAD This RPC returns sample, specimen, & urgency info about

a lab test.

VIAB LOC TYPE This RPC returns C for a Clinic and W for a Ward or -1

if not a clinic or ward type.

VIAB MAXDAYS This RPC returns the maximum number of days for a

continuous lab order.

VIAB MEDHIST This RPC returns Medication Administration History.

VIAB PROVDX This RPC returns provisional diagnosis prompting

information for service.

VIAB SCDIS This RPC returns service connected percentage and rated

disabilities for a patient.

VIAB SCHALL This RPC returns a list of schedules for a location.

VIAB SCSEL This RPC returns a list of the patient's service connected

conditions.

VIAB SRGY RPTLIST This RPC returns a list of surgery data for a patient.

VIAB TIU SECVST This RPC save the secondary visit in TIU, if inpatient.

VIAB VALSCH This RPC returns 1 if valid, 0 if not for a schedule.

VIAB VISIT This RPC returns a list of visit types for a clinic.

VIABDPS2 OISLCT This RPC returns the defaults for a pharmacy orderable

item.

VIABDXC ON This RPC returns E if order checking enabled, otherwise D.

The following existing RPCs were added to VIAB WEB SERVICES OPTION.

MD CLIO

PX SAVE DATA

This patch corrects an error found by Bed Management System (BMS) while

testing the "ListPatient" service. When an invalid patient number is passed in

as the input parameter, an error occurs LSTPAT+19^VIABMS \*RESULT(3). Routine

VIABMS was modified to prevent a hard error.

Patch Components:

-----------------

Files & Fields Associated:

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------ ------------------- --------------------

N/A

Forms Associated:

Form Name File \# New/Modified/Deleted

--------- ------ --------------------

N/A

Mail Groups Associated:

Mail Group Name New/Modified/Deleted

--------------- --------------------

N/A

Options Associated:

Option Name Type New/Modified/Deleted

----------- ---- --------------------

VIAB WEB SERVICES OPTION Broker (Client/Server) Modified

RPCs added to VIAB WEB SERVICES option by this patch:

MD CLIO SEND TO SITE

PX SAVE DATA SEND TO SITE

VIAB ADMIN SEND TO SITE

VIAB ALLSAMP SEND TO SITE

VIAB ALLSPEC SEND TO SITE

VIAB DEA SIGINFO SEND TO SITE

VIAB DEATEXT SEND TO SITE

VIAB DEVICE SEND TO SITE

VIAB DFLTSPLY SEND TO SITE

VIAB DOWSCH SEND TO SITE

VIAB EFR SEND TO SITE

VIAB FUTURE LAB COLLECTS SEND TO SITE

VIAB GET IMMUNIZATION TYPE SEND TO SITE

VIAB GET LAB TIMES SEND TO SITE

VIAB IC VALID SEND TO SITE

VIAB IMMED COLLECT SEND TO SITE

VIAB IMOLOC SEND TO SITE

VIAB IMTYPSEL SEND TO SITE

VIAB INPLOC SEND TO SITE

VIAB ISPROSVC SEND TO SITE

VIAB LOAD SEND TO SITE

VIAB LOC TYPE SEND TO SITE

VIAB MAXDAYS SEND TO SITE

VIAB MEDHIST SEND TO SITE

VIAB PROVDX SEND TO SITE

VIAB SCDIS SEND TO SITE

VIAB SCHALL SEND TO SITE

VIAB SCSEL SEND TO SITE

VIAB SRGY RPTLIST SEND TO SITE

VIAB TIU SECVST SEND TO SITE

VIAB VALSCH SEND TO SITE

VIAB VISIT SEND TO SITE

VIABDPS2 OISLCT SEND TO SITE

VIABDXC ON SEND TO SITE

Option Details:

Field Value

----- -----

NAME (#.01): VIAB WEB SERVICES OPTION

MENU TEXT (#1): VIAB Web Services Option

DESCRIPTION (#3.5): This option is required by the Kernel Broker

to give access to the RPCs used by the Vista

Integration Adapter (VIA) team.

New Remote Procedure Calls:

--------------------------

VIAB ADMIN

VIAB ALLSAMP

VIAB ALLSPEC

VIAB DEA SIGINFO

VIAB DEATEXT

VIAB DEVICE

VIAB DFLTSPLY

VIAB DOWSCH

VIAB EFR

VIAB FUTURE LAB COLLECTS

VIAB GET IMMUNIZATION TYPE

VIAB GET LAB TIMES

VIAB IC VALID

VIAB IMMED COLLECT

VIAB IMOLOC

VIAB IMTYPSEL

VIAB INPLOC

VIAB ISPROSVC

VIAB LOAD

VIAB LOC TYPE

VIAB MAXDAYS

VIAB MEDHIST

VIAB PROVDX

VIAB SCDIS

VIAB SCHALL

VIAB SCSEL

VIAB SRGY RPTLIST

VIAB TIU SECVST

VIAB VALSCH

VIAB VISIT

VIABDPS2 OISLCT

VIABDXC ON

New Service Requests (NSRs):

----------------------------

N/A

Patient Safety Issues (PSIs):

-----------------------------

N/A

Remedy Ticket(s) & Overview:

----------------------------

N/A

Test Sites:

-----------

Central Alabama Veterans Health Care System

VA Gulf Coast Veterans Health Care System

Patch Installation:

-------------------

Pre/Post Installation Overview:

-------------------------------

Patch VIAB 1\*8 must be installed prior to installation of VIAB 1\*9.

Pre-Installation Instructions:

-----------------------------

This patch may be installed with users on the system. This patch should

take less than 5 minutes to install.

No menu options need to be disabled.

Installation Instructions:

--------------------------

This installation will install modified Remote Procedure Calls (RPCs).

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the

patch VIAB 1\*9:

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch (VIAB 1\*9) to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//', press \<ENTER\>.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//', press \<ENTER\>.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//', press \<ENTER\>.

8\. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

Post-Installation Instructions:

-------------------------------

N/A

Routine Information:

====================

Routine Information:

====================

No routines included.

=============================================================================

User Information:

Entered By : [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) Date Entered : SEP 21,2016

Completed By: Date Completed:

Released By : Date Released :

=============================================================================

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch VIAB 1\*8 must be installed prior to installation of VIAB 1\*9.

This patch may be installed with users on the system. This patch should take less than 5 minutes to install.

No menu options need to be disabled.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

--------------------------

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the

patch VIAB 1\*9:

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch (VIAB 1\*9) to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//', press \<ENTER\>.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//', press \<ENTER\>.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//', press \<ENTER\>.

8\. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

------------------------------

N/A

# Backout and Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a “one size fits all.” The general strategy for VistA rollback is to repair the code with a follow-on patch. The development team recommends that sites log a Remedy ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific solutions to their unique problems.

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

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VIAB*1*15 DIBR

## KIDS Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s) Select INSTALL NAME: VIAB\*1.0\*15 3/20/19@08:58:16

> =\> VIAB\*1\*15 TEST v1

This Distribution was loaded on Mar 20, 2019@08:58:16 with header of VIAB\*1\*15 TEST v1

> It consisted of the following Install(s):

> VIAB\*1.0\*15

Checking Install for Package VIAB\*1.0\*15 Install Questions for VIAB\*1.0\*15

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

## CURRENT ACTION Field of the Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CURRENT ACTION field of the Order is the only ORDER ACTION sub-entry evaluated.

## DATE/TIME ORDERED Sub-field of the ORDER ACTION Sub-entry of the Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DATE/TIME ORDERED sub-field of the ORDER ACTION sub-entry of the Order is the field value used between the evaluating BMS start and end times.
