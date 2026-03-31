---
title: ASISTS GUI Version 2 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: OOPS
app_name: Automated Safety Incident Surveillance Tracking System
section: FIN
app_status: active
pkg_ns: OOPS
patch_ver: 2
patch_id: OOPS*2
group_key: "OOPS:OOPS:2"
file_numbers: []
security_keys: []
menu_options: 2
description: This manual provides information about the structure of the Veterans Health Information Systems and Technology Architecture (VistA) software known as the Graphical User Interface for the Automated Safety Incident Surveillance Tracking System (also referred to as the ASISTS GUI program). This manual
audience: 
keywords: 
  - asists
  - table
  - contents
  - oops
  - employee
  - incident
  - mail
  - injury
  - codes
  - reporting
page_count: 0
word_count: 5598
section_count: 33
table_count: 13
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2018
revision_count: 3
revision_newest: 12/13/2018
revision_oldest: 11/15/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_0tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/ASISTS/oops2_0tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=56"
---

![](asists-gui-version-2-technical-manual/001.png)

Automated Safety Incident Surveillance Tracking System (ASISTS) V. 2.0Graphical User Interface (GUI)Technical ManualJune 2002

(Revised December 2018)

Office of Enterprise Development

Management & Financial Systems

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Table of Contents](#table-of-contents)
- [Orientation](#orientation)
  - [How to Use This Manual](#how-to-use-this-manual)
  - [Assumptions about the Reader](#assumptions-about-the-reader)
  - [How to Obtain Technical Information Online](#how-to-obtain-technical-information-online)
  - [List File Attributes](#list-file-attributes)
  - [KIDS Build File](#kids-build-file)
- [Introduction](#introduction)
  - [Product Overview](#product-overview)
  - [Related Manuals and Other References](#related-manuals-and-other-references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Naming Conventions](#naming-conventions)
  - [Electronic Signature](#electronic-signature)
  - [Broker Context Menu Option Assignment](#broker-context-menu-option-assignment)
  - [Security Key Assignment](#security-key-assignment)
  - [Mail Groups](#mail-groups)
  - [Bulletins](#bulletins)
  - [Equipment](#equipment)
  - [Files](#files)
  - [Server (VistA) File List](#server-vista-file-list)
  - [## ## File Flow Chart](#file-flow-chart)
  - [Pointed to by](#pointed-to-by)
  - [Cross References](#cross-references)
  - [Utilities](#utilities)
  - [Resource Requirements](#resource-requirements)
  - [Global Translation, Journaling, and Protection](#global-translation-journaling-and-protection)
  - [## Routines](#routines)
  - [Exported Options](#exported-options)
  - [Exported RPCs](#exported-rpcs)
  - [Archiving and Purging](#archiving-and-purging)
  - [Callable Routines/Entry Points/APIs](#callable-routinesentry-pointsapis)
- [# External Relations](#external-relations)
  - [DBIA](#dbia)
  - [Internal Relationships](#internal-relationships)
  - [Package-wide Variables](#package-wide-variables)
- [On-line Documentation](#on-line-documentation)
- [Software Product Security](#software-product-security)
  - [Data Management](#data-management)
  - [Remote Systems](#remote-systems)
- [# Glossary](#glossary)
This Technical Manual presents the major features of the Automated Safety Incident Surveillance Tracking System (ASISTS). This manual is intended for use by anyone having access to the system, from the novice user to system manager, as a reference text and as a guide to understanding the package as a whole.
Revision History
|            |                                                                                                                                                |                     |                             |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-----------------------------|
| Date   | Description (Patch \# if applic.)                                                                                                          | Project Manager | Technical Writer/Author |
| 6/02       | Initial Version                                                                                                                                |                     | REDACTED                    |
| 11/15/04   | Updates for Patches OOPS\*1\*1 thru OOPS\*1\*8                                                                                                 |                     | REDACTED                    |
| 09/02/08   | Enhancements from Patch OOPS\*2\*15 – Privacy Act issues, modifications to the CA-7 to meet Department of Labor changes to the form            | REDACTED            | REDACTED                    |
| 12/13/2018 | Maintenance patch, OOPS\*2.0\*32 – Update to page 5 to reflect disabling of menu options due to the decommissioning of the ASISTS application. | REDACTED            | REDACTED                    |

# Table of Contents

Orientation [1](#orientation)
How to Use This Manual [1](#how-to-use-this-manual)
Assumptions about the Reader [1](#assumptions-about-the-reader)
How to Obtain Technical Information Online [1](#how-to-obtain-technical-information-online)
List File Attributes [1](#_Toc532839428)
KIDS Build File [2](#_Toc532839429)
Introduction [3](#introduction)
Product Overview [3](#product-overview)
Related Manuals and Other References [3](#related-manuals-and-other-references)
Implementation and Maintenance [5](#implementation-and-maintenance)
Decommissioning of ASISTS [5](\l)
Naming Conventions [5](#naming-conventions)
Electronic Signature [5](#electronic-signature)
Broker Context Menu Option Assignment [6](#broker-context-menu-option-assignment)
Security Key Assignment [6](#security-key-assignment)
Mail Groups [7](#mail-groups)
Bulletins [8](#bulletins)
Equipment [15](#equipment)
Files [15](#files)
Server (VistA) File List [16](#server-vista-file-list)
File Flow Chart [19](#file-flow-chart)
Pointed to by [20](#pointed-to-by)
Cross References [22](#cross-references)
Utilities [22](#utilities)
Resource Requirements [23](#resource-requirements)
Global Translation, Journaling, and Protection [23](#global-translation-journaling-and-protection)
Routines [23](#routines)
Exported Options [27](#exported-options)
Exported RPCs [30](#exported-rpcs)
Archiving and Purging [31](#_Toc532839452)
Callable Routines/Entry Points/APIs [31](#callable-routinesentry-pointsapis)
External Relations [33](#external-relations)
DBIA [33](#dbia)
Internal Relationships [34](#internal-relationships)
Package-wide Variables [34](#package-wide-variables)
On-line Documentation [35](#on-line-documentation)
Software Product Security [37](#software-product-security)
Data Management [37](#data-management)
Remote Systems [37](#remote-systems)
Glossary [39](#glossary)

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

## Assumptions about the Reader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment (e.g., Kernel Installation and distribution System \[KIDS\])
- VA FileMan data structures and terminology
- Microsoft Windows
- M Programming language

## How to Obtain Technical Information Online

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Technical information about the ASISTS GUI program is available online. It can be obtained in a number of ways as described below.

- VistA Documentation Library (VDL) <http://vista.med.va.gov/vdl/#App56>
- PDF format from the following locations.

> <u>OI Field Office</u> FTP Address Directory

> ALBANY [REDACTED](ftp://ftp.fo-albany.med.va.gov) anonymous.software

> HINES [REDACTED](ftp://ftp.fo-hines.med.va.gov) anonymous.software

> SALT LAKE REDACTED anonymous.software

## List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA FileMan List File Attributes option allows you to generate documentation pertaining to files and file structure stored in the Data Dictionary.

Listing the data dictionary in Standard format yields the following Data Dictionary information for a specified file (e.g., ASISTS ACCIDENT REPORTING file \[#2260\]):

> File name and description

> Fields in the file, including descriptions

> Identifiers

> Cross-references

> Files pointed to by the file specified

> Files that point to the file specified

> Input templates

> Print templates

> Sort templates

Listing the data dictionary in the Global Map format generates a list of all cross-references for the file selected, global location of each file in the file, input templates, print templates, and sort templates.

## KIDS Build File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can list the server-side components that are distributed with the ASISTS GUI program by using the Build File Print option. The menu path to that option is:

Programmer Options ... \[XUPROG\]

KIDS Kernel Installation & Distribution System... \[XPD MAIN\]

Utilities... \[XPD UTILITY\]

Build File Print \[XPD PRINT BUILD\]

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides information about the structure of the Veterans Health Information Systems and Technology Architecture (VistA) software known as the Graphical User Interface for the Automated Safety Incident Surveillance Tracking System (also referred to as the ASISTS GUI program). This manual consists of technical material specifically intended for VistA systems managers and developers.

## Product Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASISTS was developed as a national extension of a local AMES-MERS modification between 1996 and 1997 and serves as a core safety tool for VHA. It represents an injury management system that forces the community of practice addressing injuries to report them, supports electronic filing of workers compensation claims, and collects pertinent safety information. It requires input from the injured employee (completion of stub record), occupational health unit (completion of pertinent information, classification of injury), supervisor (completion of the first report of injury; i.e., Report of Incident), workers’ compensation specialist (completion of CA1/2, electronic transmission to the Department of Labor), and safety manager (investigation).

With Version 2.0, the ASISTS GUI program replaced the existing roll-and-scroll version of ASISTS. Its visual point-and-click interface duplicated all existing functionality within the ASISTS package, including reading data from and writing data to the same files. In addition, several data auto-population, error checking, and reporting features are unique to the ASISTS GUI program.

ASISTS Patches 1 – 15 include both bug fixes and enhancements. The most notable enhancements include the ability to electronically complete the CA-7 Request for Compensation form, the Dual Benefits form, the OSHA 300 Log, and the Privacy Act issues.

## Related Manuals and Other References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Readers who wish to learn more about the ASISTS program should consult the current version of the following:

ASISTS V. 2.0 User Manual

ASISTS V. 2.0 Installation Guide

ASISTS V. 2.0 Release Notes

ASISTS V. 2.0 Security Guide

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the decommissioning of ASISTS, effective on January 1, 2019, functionality will be available only to the users who have the "Safety" and "Workers' Comp" secondary menu options. The following menu's will no longer be available upon the release of patch, OOPS\*2.0\*32:

| Menu Name           | Secondary Menu Option Name                                              |
|-------------------------|-----------------------------------------------------------------------------|
| Employee            | ASISTS GUI Employee Menu (Context) \[OOPS GUI EMPLOYEE\]                    |
| Supervisor          | ASISTS GUI Supervisor Menu (Context) \[OOPS GUI SUPERVISOR MENU\]           |
| Occupational Health | ASISTS GUI Employee Health Menu (Context) \[OOPS GUI EMPLOYEE HEALTH MENU\] |
| Union               | ASISTS GUI Union Menu (Context) \[OOPS GUI UNION MENU\]                     |

![](asists-gui-version-2-technical-manual/002.png)

## Naming Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace used by the ASISTS package is OOPS.

## Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Supervisors (includes voluntary supervisors), Workers’ Compensation and Employee Health personnel, employees, and Safety Officers will be using an electronic signature to sign their portion of the incident report, CA-1 or CA-2, CA-7, and the Dual Benefit form.

## Broker Context Menu Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each ASISTS GUI user must be assigned OOPS GUI EMPLOYEE (Menu Context) option.

> Employee Health and AOD

> Assign the Broker Context Menu \[OOPS GUI EMPLOYEE HEALTH MENU\]

> Supervisors

> Assign the Broker Context Menu \[OOPS GUI SUPERVISOR MENU\]

> Employees

> Assign *every* employee the Broker Context Menu \[OOPS GUI EMPLOYEE\]

> Safety Officer(s)

> Assign the Broker Context Menu \[OOPS GUI SAFETY OFFICER MENU\]

> Union Representatives

> Assign the Broker Context Menu \[OOPS GUI UNION MENU\]

## Security Key Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASISTS contains two security keys. They reside on the Server (VistA) and are still required with the implementation of ASISTS GUI.

> OOPS DOL XMIT DATA – Enables the holder of this key to manually transmit claims to the Austin Automation Center. This functionality will only be exercised if the original transmission failed or the MailMan message could not be read by the AAC.

> OOPS XMIT 2162 DATA – This key is used to manually transmit incident report data to the ASISTS National Database at the Austin Automation Center.

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail groups are created during installation. These mail groups reside on the Server (Vista) and will continue to be required with ASISTS GUI. Each needs to be populated with members as described here.

In order to accommodate multi-facility functionality, each of the mail groups, with the exception of OOPS WC MESSAGE, can have a space dash space station number (e.g., “ - 688”) appended to the end of the mail group name. Messages are then transmitted to the station specific mail group based on the station number in the ASISTS case.

> OOPS EH: Members of this group should be persons from Employee Health and Infection Control (when available). Messages are sent to this mail group every time an incident involves Exposure to Body Fluids, Needlesticks, or Sharps.

> OOPS INJURY: Members of this group should be Human Resources Management (generally compensation specialists) and the safety officer (if the safety officer wants to be notified every time a record is created). The bulletin, OOPS CASE, is sent to this group every time a record is created for an incident involving an injury or illness. The bulletin, OOPS EMPLOYEE, is sent to this group every time an employee signs a CA-1 or CA-2.

> OOPS NDB MESSAGES: This group should contain the individuals who should receive any messages regarding errors in the transmission of ASISTS incident report data to the AAC.

> OOPS SAFETY: Members of this group are the safety officers for the site. This group receives a bulletin, OOPS SAFETY, when the supervisor completes and signs an incident report.

> OOPS UNION: Members of this group are union representatives. This group receives the bulletins OOPS CASE (when an incident record is created), OOPS EMPLOYEE (when an employee signs off on a CA-1 or CA-2), and OOPS SUPERVISOR (when a supervisor signs off on a CA-1 or CA-2).

> OOPS WC MESSAGE: Members of this mail group should be the individuals who need to be notified of error messages or messages sent from the AAC. There must be at least one member in this mail group for the electronic transmission of claims to Department of Labor (DOL) to function properly.

> OOPS WCP: Members of this mail group are the Workers’ Compensation personnel. This group will receive a bulletin, OOPS WORKERS COMP. Messages will also be sent to this group during the electronic transmission of claims to DOL. One message will contain the claim numbers for the claims successfully processed in ASISTS and included in the MailMan message to DOL. The second message contains information on claims with invalid data in ASISTS and conveys the claim and field numbers that need to be corrected prior to the transmission of the claim to DOL.

> OOPS ISO NOTIFICATION: This mail group must be populated with at least one person who shall receive a bulletin if sensitive data is pulled up and a new CA1 or CA2 claim is not created. If for some reason a person is not added to this new mail group, or the mail group is removed, a bulletin will be sent to users in the mail group OOPS WC MESSAGE indicating there is a problem with the setup.

## Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OOPS BILL OF RIGHTS: This bulletin is sent to the employee when an incident record is created.

> EMPLOYEE BILL OF RIGHTS FOR ACCIDENTS AND OCCUPATIONAL ILLNESSES

> The Federal Employees' Compensation Act (FECA) describes an employee's rights and entitlements to benefits following a work-related injury or illness.

> You have the right to file a CA-1 (injury) or CA-2 (illness), to apply for compensation.

> Entitlements include the option to receive medical treatment by either the VA Employee Health Unit or by your primary care physician.

> You have the right to request union representation.

> For additional information and explanation of your rights and responsibilities, contact your Workers' Compensation Specialist/Coordinator/Manager.

OOPS CASE: This bulletin is sent to the OOPS INJURY, OOPS EH (when bodily fluid exposure), and OOPS UNION mail groups, and to the supervisor when the case is created.

> An incident (injury, illness or accident) has occurred.

> Date of incident: APR 27, 1998@09:57

> Case \#: 1998-00025

> Injury/Illness: Injury

> The 1st line supervisor is required to:

> a\. Complete a Report of Accident through the option:

> Edit Report of Incident (if using Roll and Scroll) or

> Complete/Validate/Sign Incident Report (if using GUI).

> b\. Inform the injured employee on rights and benefits

> for completing the CA-1 (Injury) or CA-2 (Illness)

> Compensation Claims.

> The supervisors on this case are:

> Supervisor: SUPERVISOR,NAME

> Secondary Supervisor: SECONDARY,SUPER

OOPS CONSENT: This bulletin is sent to the union representative if the employee consents to sending sanitized information regarding the incident to the union. The employee selects the union that the bulletin should be sent to at the time they respond to the question that asks if they desire the union to be notified.

> The employee has consented to a review of case: 2000-00098A. The following information is provided to the local bargaining unit for review.

> Dt/Time Occurrence: AUG 21, 2000@19:58

> Injury/Illness: Injury

> Personnel Status: Employee

> Type of Incident: Other

> Sex: Male

> Station Number: 500

> Education:

> Cost Center/Org: 81242150

> Grade/Step: 13/4

> Supervisor: SUPERVISOR, NAME

> Sec. Super: SECSUPER, NAME

OOPS EMPLOYEE: This bulletin is sent to supervisors, union representatives (OOPS UNION mail group), and HRM (OOPS INJURY mail group) when an employee signs a CA-1 or CA-2.

> A CA-1 or CA-2 for the following incident has been signed by the employee.

> Date of Incident

> Case#

> The Incident Report is ready for review by the supervisor. It must be completed and filed with the Agency Worker's Compensation office within 2-3 working days.

OOPS INCIDENT OUTCOME REQUIRED: This bulletin is sent to the Safety mail group if the response to the Initial Return to Work Status prompt entered in the Create Incident Report or modified in the Complete/Validate/Sign Incident Report is “Days away work” or “Job Transfer/Restriction”.

Subj: ASISTS - Incident Outcome Required \[#214\] 05/06/08@13:53 8 lines

From: ASISTS, USER In 'IN' basket. Page 1

-----------------------------------------------------------------------

A new incident has been entered or an existing incident has been

modified where the Initial Return to Work Status for the incident

is "Days Away Work" or "Job Transfer/Restriction".

The Case Number is: 2008-000XX

An entry in the Classify Incident Outcome option is required to

record the dates and the incident outcome for this case.

OOPS SAFETY: This bulletin is sent when the supervisor signs an incident report to notify the Safety Officer that a case is ready for review.

> A Report of Accident and Illness has been released for your review.

> Name of Person Involved

> Date of Injury/Illness:

> Case#

OOPS SIGNATURE SECURITY: This bulletin is sent to the employee, supervisor, and the workers’ compensation specialist if data entered by the employee has been modified after the employee electronically signed the claim. Sending the bulletin is a mechanism to assure that employee entered data is not changed using FileMan or direct MUMPS sets after the employee has signed the claim.

> This is to notify the Employee, Supervisor, and Workers' Compensation Personnel that the Employee portion of a claim has been changed since the Employee electronically signed their portion of the claim.

> The claim WAS NOT transmitted to the AAC. All electronic signatures have been removed. The claim must be reviewed, amended as required and resigned prior being transmitted to the AAC.

> The affected claim number is: 2001-00003

OOPS SUPERVISOR: This bulletin is sent to union representatives when a supervisor signs a CA-1 or CA-2.

> The supervisor has signed the CA-1 or CA-2 for the following incident:

> Date of Incident

> Case#

OOPS WC EDITED: This bulletin is sent to the supervisor if the Workers’ Compensation specialist has changed the data entered by the supervisor in fields 146 (INJURED PERFORMING DUTY), 147 (NOT INJURED PERFORMING JOB), 148 (INJURY CAUSED BY EMPLOYEE), 149 (CAUSED BY EMPLOYEE EXPLAIN), 163 (SUPERVISOR AGREE/DISAGREE), 164 (SUPERVISOR NOT AGREE EXPLAIN), or 165 (REASON FOR CONTROVERTS COP) of the ASISTS ACCIDENT REPORTING (#2260) file. This bulletin is sent to the supervisor at the same time the claim is sent to the AAC.

> The Supervisor's signature has been removed from the CA1 for the following incident:

> Date of Incident: FEB 21, 2000@23:00

> Case \#: 2000-00053

> The Worker's Compensation Manager has signed the claim.

OOPS WCPBOR: This bulletin is sent to the Workers’ Compensation specialist when the employee indicates that they do not understand the Employee Bill of Rights. The employee must indicate that they understand the Bill of Rights before they can electronically sign.

> The following individual has indicated that they do NOT understand the Employee Bill of Rights and needs assistance from their Worker's Compensation Representative.

> Individual: OOPSEMPLOYEE, ONE

OOPS WC SIGNED: This bulletin is sent to the supervisor and secondary supervisor when the Workers’ Compensation specialist signs CA1 or CA2.

> The Worker's Compensation Manager has signed the CA-1 or CA-2 for electronic transmission to DOL for the following incident:

> Date of Incident: OCT 16, 2000

> Case \#: 2001-00002

OOPS WORKERS COMP: This bulletin is sent to the Workers’ Comp specialist when the supervisor signs a CA1 or CA2.

> The Supervisor signed the CA1/CA2 for the following incident on DEC 01, 2000@10:33:39:

> Date of Incident: OCT 02, 2000@14:00

> Case \#: 2001-00001

> Note to Supervisor: A copy of the CA1/CA2 must be printed out, hand signed and dated, and sent to the Worker's Compensation Manager's Office.

This message goes to the OOPS WCP mail group and contains claims that will be transmitted to DOL.

> Subj: ASISTS Record(s) transmitted to AAC for Station 499 \[#13728231\]

> 10/24/02@14:15 4 lines

> From: SUPERVISOR, ONE - PERSONNEL SPECIALIST In 'IN' basket. Page 1

> ----------------------------------------------------------------------

> The following claims have been transmitted to the AAC:

> \> 2003-00005 OOPSEMPLOYEE, ONE

> \> 2003-00006 OOPSEMPLOYEE, TWO

> \> 2003-00007 OOPSEMPLOYEE, THREE

This message goes to the AST queue in Austin and contains the claims that are transmitted to DOL. It does not go to a mail group.

> Subj: ASISTS DOL DATA \[#13728230\] 10/24/02@14:15 32 lines

> From: SUPERVISOR, ON - PERSONNEL SPECIALIST In 'IN' basket. Page 1

> ----------------------------------------------------------------------

> 0DOL^ASISTS^0000499^20021024^00005-00007^001^\|

> OP01^200300005^ OOPSEMPLOYEE, ONE ^1^22222222^20021004^0500^2003^01^ OOPSEMPLOYEE, ONE ^F^

This message is generated by ASISTS and the claim(s) in message were not transmitted to DOL because of missing required fields. Message is sent to the OOPS WCP mail group.

> Subj: ASISTS Record(s) not transmitted for Station 499 \[#10987305\]

> 07/30/01@18:00 6 lines

> From: SUPERVISOR, ONE - IRM SITE MANAGER In 'Claims' basket. Page 1

> ----------------------------------------------------------------------

> Case: 2001-00184 has missing required data or word processing fields that are larger than DOL requirements. Please edit the case(s); and once completed, the cases will be transmitted with the next scheduled transmission.

> \>TRANSMIT TO WCMIS

> \>WC ELECTRONIC SIGNATU

This message goes to the OOPS WC Message mail group and indicates there were no claims to transmit to DOL.

> Subj: ASISTS no claims to process \[#123592319\] 29 Oct 01 15:47 3 lines

> From: ASISTS REPORT ON DAILY TRANSMISSION TO THE AAC In 'IN' basket. Page 1

> \*New\*

> ----------------------------------------------------------------------------

> There were no claims ready for transmission to the Austin Automation Center when the scheduled task last ran.

This is the incident report data that is transmitted to the ASI queue. Have your IRM make sure option OOPS SCHEDULED XMIT 2162 DATA is scheduled to run daily after hours. Check patch OOPS\*1\*11.

> Subj: ASISTS NATIONAL DATABASE \[#13394415\] 08/30/02@09:47 105 lines

> From: SUPERVISOR, ONE - PERSONNEL SPECIALIST In 'IN' basket.

> Automatic Deletion Date: Nov 23, 2002 Page 1

> ----------------------------------------------------------------------

> NDB^OOPS^0000499^20020830^09:46:36^17^00142-00194^1103^002^\|

> OP1^2002-00142^OOPSEMPLOYEE, ONE ^1^5^20020605^1100^^^1^499^82412

> 136^0621^05^07^High school graduate/equivalent^P^11^7^LZ^^B^F^N^^^^^^^^1^\|

> OP2^1^1^EMPLOYEE WAS ASSISTING PATIENT WHEN HE TRIPPED OVER CORD IN ROOM. ^\|

> OP4^1^1^INSTRUCTED EMPLOYEE TO BE AWARE OF ENVIROMENT. ^\|

> OP5^1^1^none ^\|

> OP8^^^^^\|

This message contains the incident report data that was not transmitted to the ASISTS National Database because required fields are missing on the case. Message goes to the OOPS NDB Messages mail group.

> Subj: ASISTS Records Missing Necessary Data Elements {#25574249\] 05/07/01

> From: SUPERVISOR, ONE

> ----------------------------------------------------------------------

> Case: 1999-00182 has missing data that must be entered prior to transmitting to AAC.

> Missing SSN

> Missing DOB

> Case: 1999-00198 has missing data that must be entered prior to transmitting to AAC.

> Missing DOB

Austin processes data in the ASI queue at 8am on Friday. If nothing is in the queue for your station, this warning message is generated. Message is transmitted to the OOPS NDB Messages mail group. Have IRM make sure option OOPS SCHEDULED XMIT 2162 DATA is scheduled to run daily after hours.

> Subj: ASI/RNS \#023441001752879  \[#17448704\] 10 Dec 02 10:02 CST  6 lines  
> From: \<POSTMASTER@REDACTED.VA.GOV\>  In 'IN' basket.   Page 1  \*New\*  
> ---------------------------------------------------------------------  
> 2ASI0024 RNS.  
> STATION \# 499               

> 1\. No transmissions for 2162 data were received from your site the past seven days.

> 2\. If you did not close any 2162s during the past week, no further action is necessary.

> 3\. If you did close any 2162s reports during the past week, please have OOPS SCHEDULED XMIT 2162 run nightly.

The OOPS SENSITIVE DATA bulletin accepts supervisor and employee information if sensitive data is pulled up and a new CA1 or CA2 claim is not created. This bulletin is then sent to the users defined in the new mail group, OOPS ISO NOTIFICATION.

> Subj: ASISTS Employee Sensitive data . \[#1962158\] 11/16/04@10:06

> 11 lines

> From: OOPSSUPER, ONE In 'IN' basket. Page 1

> ----------------------------------------------------------------------

> This is a notification that the following supervisor

> OOPSSUPER, ONE

> used the ASISTS software to View sensitive data for the following employee:

> OOPSEmployee, One on Nov 16, 2004@10:06:14.

> without creating an Illness or Injury case.

OOPS CASE CLOSE NOTIFICATION is a bulletin that is sent to the OOPS SAFETY and OOPS WCP mail groups whenever a case is closed. The message text is:

> Subj: ASISTS CASE CLOSED NOTIFICATION \[#1962194\] 11/16/04@16:40 6 lines

> From: OOPSCLOSER, ONE In 'IN' basket. Page 1

> ----------------------------------------------------------------------

> An ASISTS Case has been closed:

> ASISTS Case Number: 2004-00046

> Case Closed By: OOPSCLOSER, ONE

> Date Case Closed: Nov 16, 2004

## Equipment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Default PC Printer: The ASISTS GUI Employee Bill of Rights, incident report form, and other reports require that the personal computer have a valid default printer specified. See Microsoft operating system documentation for details on setting up default printers.

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASISTS GUI package contains 28 Server (VistA) files with file numbers ranging from 2260 through 2264. The File List section of this manual provides additional file information.

In addition to the Server (VistA) files, the following Client/PC files are used by ASISTS GUI.

End-User Workstation

> \Program Files\ASISTS

> ASISTS.exe The Delphi program executable.

> ASISTSHELP.chm The online Windows Help file for ASISTS.

> INETWH32.dll Setup Program to install needed online report component.

> Roboex32.Dll The Dynamic Link Library used to display the online Help.

> Serverlist.exe Program used to define broker servers.

######### OR

Consolidated Network Location

> ASISTS.exe The Delphi program executable.

> ASISTSHELP.chm The online Windows Help file for ASISTS.

> INETWH32.dll Setup Program to install needed online report component.

> Roboex32.Dll The Dynamic Link Library used to display the online Help.

> Serverlist.exe Program used to define broker servers.

## Server (VistA) File List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|             |                |                                      |                                                                                                                                                                                                                                   |
|-------------|----------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File \# | Global     | Name                             | Description                                                                                                                                                                                                                   |
| 2260        | ^OOPS(2260,    | ASISTS ACCIDENT REPORTING            | This file contains all information associated with an accident that results in injury and/or illness.                                                                                                                             |
| 2261        | ^OOPS(2261,    | ASISTS CHARACTERIZATION OF INJURY    | This file contains a list of terms used to describe or categorize the type of injury sustained by the employee. Each term is associated with a code. File data is exported with the package and should not be edited by the site. |
| 2261.1      | ^OOPS(2261.1,  | ASISTS DOL ANATOMICAL LOCATION CODES | This file contains a list of terms and codes used to describe the body part that was affected by the injury. File data is exported with the package and should not be edited by the site.                                         |
| 2261.2      | ^OOPS(2261.2,  | ASISTS CRITICAL TRACKING ISSUES      | This file contains a list of terms used to categorize the type of injury sustained by the employee. Each term is associated with a code. File data is exported with the package and should not be edited by the site.             |
| 2261.21     | ^OOPS(2261.21, | ASISTS INCIDENT WEATHER              | This file contains the weather conditions                                                                                                                                                                                         |
|             |                | FACTORS                              | that contributed to the incident.                                                                                                                                                                                                 |
| 2261.22     | ^OOPS(2261.22, | ASISTS INCIDENT SOURCE               | This file contains the list of valid sources                                                                                                                                                                                      |
|             |                |                                      | causing the incident.                                                                                                                                                                                                             |
| 2261.24     | ^OOPS(2261.24, | ASISTS PREVENTION                    | This file contains the list of prevention                                                                                                                                                                                         |
|             |                | METHODS                              | methods that could be used to avoid.                                                                                                                                                                                              |
|             |                |                                      | another incident.                                                                                                                                                                                                                 |
| 2261.3      | ^OOPS(2261.3,  | ASISTS PERSONAL PROTECTIVE EQUIPMENT | This file contains items worn for protection against body fluid exposure. File data is exported with the package and should not be edited by the site.                                                                            |
| 2261.4      | ^OOPS(2261.4,  | ASISTS SETTING OF INJURY             | This file contains a list of patient care areas and other locations where accidents occur. Each location is associated with a code. File data is exported with the package and should not be edited by the site.                  |
| 2261.45     | ^OOPS(2261.45, | ASISTS LOCATION OF INJURY DETAIL     | This file contains location of injury details which can be thought of as sub-locations where the incident occurred.                                                                                                               |
| 2261.5      | ^OOPS(2261.5,  | ASISTS PURPOSE FOR USING SHARPS      | This file contains a list of phrases describing the purpose for originally using the sharps item. Each entry is associated with a code. File data is exported with the package and should not be edited by the site.              |
| 2261.6      | ^OOPS(2261.6,  | ASISTS OCCURRENCE OF SHARPS INJURY   | This file contains a list of phrases describing how or when the injury occurred. Each entry is associated with a code. File data is exported with the package and should not be edited by the site.                               |

|             |               |                                               |                                                                                                                                                                                                                                                                         |
|-------------|---------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File \# | Global    | Name                                      | Description                                                                                                                                                                                                                                                         |
| 2261.7      | ^OOPS(2261.7, | ASISTS DEVICE/EQUIPMENT                       | This file contains a list of terms used in describing the device or item that caused the injury. File data is exported with the package and should not be edited by the site.                                                                                           |
| 2261.8      | ^OOPS(2261.8  | ASISTS RESULTS                                | This file contains a list of phrases describing the type event (e.g., spills, contaminated sheets, person contact) that resulted in a body fluid exposure. File data is exported with the package and should not be edited by the site.                                 |
| 2261.9      | ^OOPS(2261.9, | ASISTS SAFETY CHARACTERISTICS                 | This file contains valid responses for describing the safety characteristics of the device that was being used when the incident occurred.                                                                                                                              |
| 2262        | ^OOPS(2262,   | ASISTS SITE PARAMETER                         | This file contains default values for the OWCP District Office and for Physician information by Station number. If Physician information is entered for a Station number, then that data will be used as the default value for physician information in the CA1 or CA2. |
| 2262.1      | ^OOPS(2262.1, | ASISTS DOL DISTRICT OFFICE                    | This file contains the valid District Office codes that must be used for the submission of CA1/CA2 claims to DOL (Department of Labor). This file MUST NOT be altered as doing so may cause DOL to reject the submission.                                               |
| 2262.2      | ^OOPS(2262.2, | ASISTS DEVICE SIZE                            | This file contains valid device sizes for the needle or syringe, if the object causing injury were either one. Needle size would be the gauge and syringe size would be cc.                                                                                             |
| 2262.3      | ^OOPS(2262.3, | ASISTS NEEDLESTICK BRANDS                     | This file contains the brand names of devices that are used in incidents involving needlesticks and sharps.                                                                                                                                                             |
| 2262.4      | ^OOPS(2262.4  | ASISTS REASON FOR CONTROVERT                  | This file contains the list of the 9 valid Department of Labor reasons an agency may controvert a workers’ compensation claim.                                                                                                                                          |
| 2262.5      | ^OOPS(2262.5  | ASISTS ADDITIONAL PAY TYPES                   | This file contains the list of valid pay types that can be used when completing a CA7 form.                                                                                                                                                                             |
| 2262.6      | ^OOPS(2262.6  | ASISTS STANDARD INDUSTRIAL CLASS. (SIC)       | This file contains the list of industry class codes that are applicable for use by medical centers when completing an OSHA 300A Summary Log.                                                                                                                            |
| 2262.7      | ^OOPS(2262.7  | ASISTS N.A. INDUSTRIAL CLASSIFICATION (NAICS) | This file contains the list of North America industry class codes that are applicable for use by medical centers when completing an OSHA 300A Summary Log.                                                                                                              |

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 32%" />
<col style="width: 39%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File #</strong></td>
<td><strong>Global</strong></td>
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>2262.8</td>
<td>^OOPS(2262.8,</td>
<td>ASISTS REASON FOR DISPUTE CODES</td>
<td>This file contains the basic reason a CA-1 case is disputed by the agency. Once a dispute code is selected, the user adds additional text in the Reason for Dispute Comment field to further explain the reason for disputing the claim.</td>
</tr>
<tr class="odd">
<td>2263</td>
<td>^OOPS(2263,</td>
<td>ASISTS DOL TYPE OF INJURY CODES</td>
<td>This file contains the valid Type of Injury Codes and descriptions for submission of CA1/CA2 claims to DOL (Department of Labor). This file MUST NOT be altered as doing so may cause DOL to reject the submission.</td>
</tr>
<tr class="even">
<td>2263.1</td>
<td>^OOPS(2263.1</td>
<td>ASISTS DOL SOURCE OF INJURY CODES</td>
<td><p>This file contains the valid codes and descriptions for the Source of Injury codes</p>
<p>used for submitting claims to the DOL (Department of Labor). This file MUST NOT be altered as doing so may cause DOL to reject the submission.</p></td>
</tr>
<tr class="odd">
<td>2263.2</td>
<td>^OOPS(2263.2</td>
<td>ASISTS DOL CAUSE OF INJURY CODES</td>
<td>This file contains the valid codes and description for the Cause of Injury Codes for submission of a CA1/CA2 claim to DOL (Department of Labor). This file MUST NOT be altered as doing so may cause DOL to reject the submission.</td>
</tr>
<tr class="even">
<td>2263.3</td>
<td>^OOPS(2263.3</td>
<td>ASISTS DOL NATURE OF INJURY CODES</td>
<td>This file contains the valid codes and descriptions for the Nature of Injury Codes for submission of a CA1/CA2 claim to the DOL (Department of Labor). This file MUST NOT be altered as doing so may cause DOL to reject the submission.</td>
</tr>
<tr class="odd">
<td>2263.4</td>
<td>^OOPS(2263.4</td>
<td>ASISTS DOL OCCUPATION CODES</td>
<td>This file contains the valid codes and descriptions for the Occupation Codes for submission of a CA1/CA2 claim to the DOL (Department of Labor). This file MUST NOT be altered as doing so may cause DOL to reject the submission.</td>
</tr>
<tr class="even">
<td>2263.5</td>
<td>^OOPS(2263.5</td>
<td>ASISTS DOL PROVIDER TITLE</td>
<td>This file contains the valid titles that can be used for Providers for submission of CA1/CA2 claims to the DOL (Department of Labor). This file MUST NOT be altered as doing so may cause DOL to reject the submission.</td>
</tr>
<tr class="odd">
<td>2263.6</td>
<td>^OOPS(2263.6</td>
<td>ASISTS OWCP CHARGEBACK CODES</td>
<td>This file contains valid OWCP Chargeback codes that must be used in the submission of CA1/CA2 claims to the DOL (Department of Labor). This file MUST NOT be altered as doing so may cause DOL to reject the submission.</td>
</tr>
<tr class="even">
<td>2263.7</td>
<td>^OOPS(2263.7,</td>
<td>ASISTS UNION INFORMATION</td>
<td>This file contains information regarding the Union representative who should receive notification if an employee gives consent for sharing information regarding the incident.</td>
</tr>
</tbody>
</table>

|             |               |                                 |                                                                                                                                                                                                                   |
|-------------|---------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File \# | Global    | Name                        | Description                                                                                                                                                                                                   |
| 2263.8      | ^OOPS(2263.8, | ASISTS BODY PART GROUPING       | This file contains the body part grouping lists to assist the user in narrowing the search criteria for the body part affected in the incident.                                                                   |
| 2264        | ^OOPS(2264,   | ASISTS COMPENSATION CLAIM (CA7) | This file contains all information associated with a Request for Compensation (CA7) which has been completed by an employee. A pointer back to ^OOPS(2260) exists in this file to link the CA1 or CA2 to the CA7. |

## ## ## File Flow Chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>FILE \# and NAME</u> <u>POINTS TO</u>

2260

ASISTS ACCIDENT 4 INSTITUTION

REPORTING 5 STATE

49 SERVICE/SECTION

> 200 NEW PERSON

2261. ASISTS CHARACTERIZATION OF INJURY
      1.  ASISTS DOL ANATOMICAL LOCATION

> CODES

2.  ASISTS CRITICAL TRACKING ISSUE

> 2261.21 ASISTS INCIDENT WEATHER FACTOR

> 2261.22 ASISTS INCIDENT SOURCE

> 2261.24 ASISTS PREVENTION METHODS

3.  ASISTS PERSONAL PROTECTIVE

> EQUIPMENT

4.  ASISTS SETTING OF INJURY
5.  ASISTS PURPOSE FOR USING SHARPS
6.  ASISTS OCCURRENCE OF SHARPS INJURY
7.  ASISTS DEVICE/EQUIPMENT
8.  ASISTS RESULTS
9.  ASISTS SAFETY CHARACTERISTICS
1.  ASISTS DOL DISTRICT OFFICE
2.  ASISTS DEVICE SIZE
3.  ASISTS NEEDLESTICK BRANDS
4.  ASISTS REASON FOR CONTROVERT

> 2262.8 ASISTS REASON FOR DISPUTE CODE

> 2263 ASISTS DOL TYPE OF INJURY CODES

1.  ASISTS DOL SOURCE OF INJURY CODES
2.  ASISTS DOL CAUSE OF INJURY CODES
3.  ASISTS DOL NATURE OF INJURY CODES

> 2263.5 ASISTS DOL PROVIDER TYPE

6.  ASISTS OWCP CHARGEBACK CODES

> 2263.8 ASISTS BODY PART GROUPINGS

2264 5 STATE

> ASISTS COMPENSATION 200 NEW PERSON

> CLAIM (CA7) 2260 ASISTS ACCIDENT REPORTING

## Pointed to by

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>FILE \# and NAME</u> <u>POINTS TO</u> <u>POINTED TO BY</u>

> 2260 None

> ASISTS ACCIDENT

> REPORTING

2261

> ASISTS CHARACTERIZATION None 2260 ASISTS

> OF INJURY ACCIDENT

REPORTING

2261.1

ASISTS DOL ANATOMICAL 2263.8 2260 ASISTS

LOCATION CODES ASISTS BODY PART ACCIDENT

> GROUPING REPORTING

2261.2

ASISTS CRITICAL TRACKING None 2260 ASISTS

ISSUES ACCIDENT

REPORTING

2261.21

ASISTS INCIDENT WEATHER None 2260 ASISTS

FACTOR ACCIDENT

REPORTING

2261.22

ASISTS INCIDENT SOURCE None 2260 ASISTS

ACCIDENT

REPORTING

2261.24

ASISTS PREVENTION METHODS None 2260 ASISTS

ACCIDENT

REPORTING

2261.3

> ASISTS PERSONAL None 2260 ASISTS

> PROTECTIVE EQUIPMENT ACCIDENT

> REPORTING

2261.4

ASISTS SETTING OF INJURY None 2260 ASISTS

> ACCIDENT

> REPORTING

2261.5

ASISTS PURPOSE FOR USING None 2260 ASISTS

SHARPS ACCIDENT

REPORTING

<u>FILE \# and NAME</u> <u>POINTS TO</u> <u>POINTED TO BY</u>

2261.6

ASISTS OCURRENCE OF None 2260 ASISTS

SHARPS INJURY ACCIDENT

REPORTING

2261.7

ASISTS DEVICE/EQUIPMENT None 2260 ASISTS

> ACCIDENT

REPORTING

2261.8

ASISTS RESULTS None 2260 ASISTS

> ACCIDENT

REPORTING

2262

ASISTS SITE PARAMETER 4 INSTITUTION None

5.  STATE

> 200 NEW PERSON

1.  ASISTS DOL

> DISTRICT OFFICE

6.  STAND INDUSTRIAL

> CLASS (SIC)

7.  N.A. INDUSTRIAL

> CLASS (NAICS)

5.  ASISTS PROVIDER

> TITLE

6.  ASISTS OWCP

> CHARGEBACK CODES

2262.1

ASISTS DOL DISTRICT OFFICE None 2260 ASISTS

> ACCIDENT

REPORTING

2262 ASISTS SITE

> PARAMETER

2262.8

ASISTS REASON FOR DISPUTE None 2260 ASISTS

CODE ACCIDENT

REPORTING

2263

ASISTS DOL TYPE OF INJURY None 2260 ASISTS

CODES ACCIDENT

REPORTING

2263.1

ASISTS DOL SOURCE OF None 2260 ASISTS

INJURY CODES ACCIDENT

REPORTING

<u>FILE \# and NAME</u> <u>POINTS TO</u> <u>POINTED TO BY</u>

2263.2

ASISTS DOL CAUSE OF None 2260 ASISTS

INJURY CODES ACCIDENT

REPORTING

2263.3

ASISTS DOL NATURE OF None 2260 ASISTS

INJURY CODES ACCIDENT

REPORTING

2263.5

ASISTS PROVIDER TITLE OF None 2260 ASISTS

> ACCIDENT

REPORTING

2262 ASISTS SITE

PARAMETER

2263.6

ASISTS OWCP CHARGEBACK None 2260 ASISTS

CODES ACCIDENT

REPORTING

2263.7

ASISTS UNION INFORMATION 200 NEW PERSON 2260 ASISTS

> ACCIDENT

REPORTING

2263.8

ASISTS BODY PART GROUPINGS None 2261.1 ASISTS DOL

ANATOMICAL

LOCATION

2264 5 STATE

ASISTS COMPENSATION 200 NEW PERSON

CLAIM (CA7) 2260 ASISTS ACCIDENT

REPORTING

2262.5 ASISTS ADDITIONAL

PAY TYPE

## Cross References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cross-references can be retrieved using the List File Attributes option in FileMan. If further explanation is required, see the on-line documentation section in this Manual.

## Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General-purpose utility functions are contained in OOPSUTL1, OOPSUTL2, OOPSUTL3, OOPSUTL4, OOPSUTL5 and OOPSUTL6.

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASISTS GUI 2.0 (through OOPS\*2.0\*15)

The ASISTS GUI package is designed to print reports (CA1, CA2, CA7 and Dual Benefit forms included) to any windows printer defined to the personal computer running the system.

## Global Translation, Journaling, and Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special recommendations or needs for the routines and files distributed with the ASISTS GUI package.

## ## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 32 routines for the ASISTS GUI package located in the OOPS namespace. Use the option First Line Routine Print within Routine Tools under Programmer Options to obtain a list of routines and a brief description of each.

> OOPSGUI0 Retrieves Case or Person Information and sorts case listings

> OOPSGUI1 Determines Menus available, validates and files signature information and checks status of Paid Fields

> OOPSGUI2 Retrieves Case (2260) information, processes witness information, retrieves the Default Physician, and sets a single field value in file 2260

> OOPSGUI3 Controls record locking, retrieves body parts, work schedule and station information

> OOPSGUI4 Retrieves Paid file information, retrieves non Paid employee information, person information (for Supervisor and Union) and creates a new case/record

> OOPSGUI5 Saves either incident report, CA1 or CA2 data.

> OOPSGUI6 Controls Union and Site parameter file entries, changes case status and files new Amended cases

> OOPSGUI7 Entry point of GUI transmission of DOL or NDB data, clears supervisor fields if OWCP has edited case, tracks Employee Union Consent and retrieves single field information from the 2260 file

> OOPSGUI8 Validates that a claim can be signed and that none of the signatures are the same. Allows OWCP to sign for supervisor if approved to, clears a signature, and retrieves NOI codes.

> OOPSGUI9 Validates required fields for incident report, CA1 or CA2, including date validation

> OOPSGUIC The primary purpose of this routine are two subroutines that list valid CA7’s or a list of CA1’s and/or CA2’s for the user to select when entering a new CA7

> OOPSGUID Files data for the CA7 and the Dual Benefits forms

> OOPSGUIF Retrieves data for the OSHA and Needlestick log reports, retrieves Occupation Descriptions

> OOPSGUIR Retrieves data used to create miscellaneous reports including the OSHA 300 Log, OSHA 300A Summary, and the Filing Instructions report

> OOPSGUIS Validates employees’ electronic signature on the CA7. Includes subroutines to encrypt and decrypt signatures and storing checksums on employee-entered data so that data validation can be completed on that data.

> OOPSGUIT Retrieves and formats data for the Type of Incident and Incident Report Status reports

OOPSDOL Extracts CA1 and CA2 data from claims signed by the

OOPSDOL1 workers’ compensation specialist. Packages the data into

OOPSDOL2 Mailman messages that are transmitted to the Austin

OOPSDOLX Automation Center.

######### OOPSMBUL Sends Mail Bulletins to specific Mail Groups

> OOPSNDB, Extracts incident data on closed cases and transmits it to the

OOPSNDBX ASISTS National database in the AAC

OOPSUTL1 These are utility routines used in ASISTS for error

OOPSUTL2 checking and other related functions.

OOPSUTL3

OOPSUTL4

OOPSUTL5

OOPSUTL6

OOPSVAL1 Allows the Employee, Supervisor, or Workers’

> Compensation specialist to electronically sign the claim directly

OOPSWCE Worker’s Compensation Specialist data entry screen to

> complete and sign that the claim can be electronically

> transmitted to DOL

######### OOPSWCSE Employee Health and Safety giving approval for

> Workers’ Compensation specialist signing for employee

The following routines are part of the ASISTS Roll and Scroll system. These routines should not be removed from the system until the Previous Version (Roll and Scroll) of ASISTS is no longer in production or being accessed/used by anyone.

> OOPSCA Creates an amendment so that a CA1 or CA2 claim can be edited

> OOPSCA1 Displays the CA1 or CA2 data to either the CRT or to any OOPSCA2 printer

OOPSDS12

OOPSCC Creates an Incident/Illness stub record

OOPSCSN Finds and/or assigns an ASISTS case number to the

> Incident/Illness record (claim)

OOPSDIS Displays the stub record portion of the incident report

OOPSDM Prints the Employee Bill of Rights

OOPSEMP1 Employee data entry screen for CA1 and CA2 claim data

> OOPSEMP2  
> OOPSEMPB

OOPSESIG Electronic Signature code entry

OOPSESP Allows data entry/edit of the ASISTS Site Parameter File

> OOPSESR Allow selected data elements entered on the stub record (incident report) to be edited

OOPSF167 This is a temporary routine released with OOPS\*1.0\*8 that

> should be used to make changes to the PAY RATE PER Field (#167, file \#2260). This was required because the data type for this field was changed. This routine should be removed from the users menu when the data correction has been completed.

> OOPSLOG Prints the Log of Federal Occupational Injuries and Illness Report

OOPSPC10 Prints the Employee portion of the CA1 claim form

OOPSPC11

OOPSPC20 Prints the Supervisor’s portions of the CA1 claim form

OOPSPC21

OOPSPC30 Prints the Receipt portion of the CA1 claim form

OOPSPC40 Prints the Employee’s portions of the CA2 claim form

OOPSPC41

OOPSPC50 Prints the Supervisor’s portions of the CA2 claim form

OOPSPC51

OOPSPC60 Prints page 3 of the CA2 claim form

> OOPSPC70 Prints part 1 and 2 of the instructions for completing the OOPSPC71 CA1 claim form

OOPSPC80 Prints part 1 and 2 of the instructions for completing the

OOPSPC81 CA2 claim form

> OOPSPCA Called by OOPSPRT2 and is the secondary driver routine for printing the hardcopy CA1 or CA2 claim form

OOPSPI2 Pre-Install routine for OOPS\*1.0\*2

OOPSPRT Prints the Print Report of Incident Report

OOPSPRT1 Prints the Print Incident Report Status Report

> OOPSPRT2 Allow the Employee, Supervisor, or Safety Officer to print a blank CA1 or CA2 and is the driver routine for printing a hardcopy of the CA1 or CA2 claim form.

> OOPSPUT1 Utility routine for formatting fields for printing on the hardcopy CA1 or CA2 claim form

> OOPSSOF1 Allows the Safety Officer to complete the report of incident

OOPSSOF2 Allows the Safety Officer to change the status of a case

> OOPSSUP1 Supervisor data entry screen to complete the bottom portion OOPSSUP2 of the incident report and the Supervisors portion of the CA1 or

> OOPSSUP3 CA2 claim form. The Supervisor can also sign the claim from

> OOPSSUPB this routine.

> OOPSWCE1 Worker’s Compensation Specialist data entry screen to

> OOPSWCE2 complete and sign that the claim can be electronically transmitted to DOL

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are exported with the ASISTS GUI.

|                          |                                           |                        |
|--------------------------|-------------------------------------------|------------------------|
| Name                 | Menu Text                             | Type               |
| OOPS GUI EMPLOYEE        | ASISTS GUI Employee Menu (Context)        | Broker (Client/Server) |
| OOPS GUI EMPLOYEE HEALTH | ASISTS GUI Employee Health Menu (Context) | Broker (Client/Server) |
| OOPS GUI SAFETY OFFICER  | ASISTS GUI Safety Menu (Context)          | Broker (Client/Server) |
| OOPS GUI SUPERVISOR      | ASISTS GUI Supervisor Menu (Context)      | Broker (Client/Server) |
| OOPS GUI UNION           | ASISTS GUI Union Menu (Context)           | Broker (Client/Server) |
| OOPS GUI WORKERS' COMP   | ASISTS GUI Workers' Comp Menu (Context)   | Broker (Client/Server) |

Table 1: Exported Options

Client/server applications are type “B”, Broker (Client/Server), in the OPTION file (#19). The user must have the client/server application option assigned to them as with any other assigned option in VistA. The Client/server application will only run for those users who are allowed to activate it. The ASISTS GUI *REQUIRES* that *ALL* users have the OOPS GUI EMPLOYEE option as all broker calls used by the application are registered by that option. The other options only control those parts the ASISTS GUI a user can access.

> **NOTE:** The client/server application options will not be displayed in the user’s menu tree.

The following ASISTS Roll and Scroll options have been decommissioned with Patch OOPS\*2.0\*10.

> *ASISTS Employee Health Menu \[OOPS EMP HEALTH MENU\]*

> Approve Workers' Comp Signing for Employee \[OOPS EMP HLT WCP EMP SIGN\]

> Create Accident/Illness Record \[OOPS CREATE CASE\]

> Display CA1/CA2 \[OOPS EMP HLT DISP CA1/CA2\]

> Edit Stub Record \[OOPS EMP HLT EDIT STUB\]

> Log of Federal Occupational Injuries and Illnesses \[OOPS LOG\]

> Log of Needlestick Incidents \[OOPS NEEDLESTICK LOG\]

> Print Accident Report Status \[OOPS SAFETY PRINT STATUS\]

> Print CA1/CA2 \[OOPS SAFETY PRINT CA\]

> Print Employee Bill of Rights \[OOPS PRINT BILL\]

> Print Report of Accident \[OOPS SAFETY PRINT\]

*ASISTS Employee Menu \[OOPS EMP MENU\]*

> Complete Employee CA-1 & CA-2 \[OOPS EMP ENTRY\]

> Display CA1 or CA2 \[OOPS EMP DISPLAY CA1/CA2\]

> Print CA1/CA2 \[OOPS EMP PRINT CA\]

> Print Employee Bill of Rights \[OOPS PRINT BILL\]

> Validate and Sign CA-1 or CA-2 \[OOPS EMP VALIDATE\]

*ASISTS Supervisor Menu \[OOPS SUP MENU\]*

> Create Accident/Illness Record \[OOPS CREATE CASE\]

> Create Amendment \[OOPS CREATE AMENDMENT (SUP)\]

> Display CA1 or CA2 \[OOPS SUP DISPLAY CA1/CA2\]

> Edit Report of Incident \[OOPS SUP ENTRY\]

> Print Accident Report Status \[OOPS SUP PRINT STATUS\]

> Print CA1/CA2 \[OOPS SUP PRINT CA\]

> Print Employee Bill of Rights \[OOPS PRINT BILL\]

> Print Report of Accident \[OOPS SUP PRINT\]

> Validate and Sign CA1,CA2 or 2162 \[OOPS SUP VALIDATE\]

*ASISTS Safety Officers Menu \[OOPS SAFETY MENU\]*

> Create Accident/Illness Record \[OOPS CREATE CASE\]

> Approve Workers' Comp Signing for Employee \[OOPS SAFETY WCP EMP SIGN\]

> Change the Status of a Case \[OOPS SAFETY CLOSE\]

> Complete Report of Accident (2162) \[OOPS SAFETY ENTER 2162\]

> Create Amendment \[OOPS CREATE AMENDMENT (SO)\]

> Display CA1 or CA2 \[OOPS SAFETY DISPLAY CA1/CA2\]

> Edit Report of Incident \[OOPS SAFETY SUP ENTRY\]

> Edit Site Parameter \[OOPS EDIT SITE PARAMETER\]

> Edit Stub Record \[OOPS SAFETY EDIT STUB RECORD\]

> Log of Federal Occupational Injuries and Illnesses \[OOPS LOG\]

> Log of Needlestick Incidents \[OOPS NEEDLESTICK LOG\]

> Manual Transmit of National Database (2162) Data \[OOPS MANUAL 2162 DATA XMIT\]

> Print Accident Report Status \[OOPS SAFETY PRINT STATUS\]

> Print CA1/CA2 \[OOPS SAFETY PRINT CA\]

> Print Employee Bill of Rights \[OOPS PRINT BILL\]

> Print Report of Accident \[OOPS SAFETY PRINT\]

> Validate and Sign 2162 \[OOPS SAFETY VALIDATE\]

> *ASISTS Union Menu \[OOPS UNION MENU\]*

> Log of Federal Occupational Injuries and Illnesses \[OOPS UNION LOG\]

> Print Accident Report Status \[OOPS SAFETY PRINT STATUS\]

> Print Employee Bill of Rights \[OOPS PRINT BILL\]

> Print Report of Accident \[OOPS UNION PRINT\]

> *ASISTS Worker's Compensation Menu \[OOPS WORKER'S COMP MENU\]*

> Change the Status of a Case \[OOPS SAFETY CLOSE\]

> Complete Employee CA-1 & CA-2 \[OOPS SAFETY EMP ENTRY\]

> Complete Report of Accident (2162) \[OOPS SAFETY ENTER 2162\]

> Create Accident/Illness Record \[OOPS CREATE CASE\]

> Create Amendment \[OOPS CREATE AMENDMENT (SO)\]

> Display CA1 or CA2 \[OOPS SAFETY DISPLAY CA1/CA2\]

> Edit Report of Incident \[OOPS SAFETY SUP ENTRY\]

> Edit Stub Record \[OOPS SAFETY EDIT STUB RECORD\]

> Enter/Edit Union Information \[OOPS WC EDIT UNION INFO\]

> Manual Transmission of DOL Data \[OOPS DOL MANUAL XMIT DATA\]

> Print Accident Report Status \[OOPS SAFETY PRINT STATUS\]

> Print CA1/CA2 \[OOPS SAFETY PRINT CA\]

> Print Employee Bill of Rights \[OOPS PRINT BILL\]

> Print Report of Accident \[OOPS SAFETY PRINT\]

> Validate and Sign CA1 or CA2 \[OOPS WC VALIDATE\]

> Workers' Comp Elect. Sign For Employee \[OOPS WC SIGN FOR EMPLOYEE\]

> Worker's Compensation Edit CA1/CA2 \[OOPS WC EDIT CA1/CA2\]

## Exported RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A remote procedure call (RPC) is M code that can take optional parameters to perform a task and then return either a single value or an array to the client application. In the message sent to VISTA, client applications will include the name of the requested RPC to be activated. These RPCs are registered in the REMOTE PROCEDURE file (#8994) containing available and authorized RPCs.

The ASISTS GUI distributes the following remote procedure calls (RPCs).

| RPC Name                   | Line Tag | Routine | Return Value |
|--------------------------------|--------------|-------------|------------------|
| OOPS APPROVE SIGN FOR EMPLOYEE | EN1          | OOPSGUI8    | Array            |
| OOPS CHANGE CASE STATUS        | CHGCASE      | OOPSGUI6    | Single Value     |
| OOPS CHECK PAID EMP DATA       | VALEMP       | OOPSGUI1    | Single Value     |
| OOPS CLEAR SIGNATURE           | CSIGN        | OOPSGUI8    | Single Value     |
| OOPS CREATE AMENDMENT          | AMEND        | OOPSGUI6    | Single Value     |
| OOPS DELETE SITEPAR STATION    | SITEPKIL     | OOPSGUI6    | Single Value     |
| OOPS DELETE UNION              | UNIKILL      | OOPSGUI6    | Single Value     |
| OOPS DELETE WITNESS            | DELWITN      | OOPSGUI2    | Array            |
| OOPS EDIT 2260                 | EDIT         | OOPSGUI5    | Array            |
| OOPS EDIT SITE PARAMETER       | PARMEDT      | OOPSGUI6    | Single Value     |
| OOPS EDIT SITEPAR STATION      | SITEPEDT     | OOPSGUI6    | Single Value     |
| OOPS EMPLOYEE DATA             | PAID         | OOPSGUI4    | Array            |
| OOPS GET 2260 DATA             | GET          | OOPSGUI2    | Array            |
| OOPS GET ASISTS CASE           | ASISTS       | OOPSGUI4    | Array            |
| OOPS GET BODY PART             | BODY         | OOPSGUI3    | Array            |
| OOPS GET CASE NUMBERS          | GETCASE      | OOPSGUI0    | Array            |
| OOPS GET CKRANGE               | GETSCHED     | OOPSGUI3    | Array            |
| OOPS GET DATA                  | GETDATA      | OOPSGUI3    | Array            |
| OOPS GET DEFAULT MD            | DEFMD        | OOPSGUI2    | Array            |
| OOPS GET DUPLICATES            | DUP          | OOPSGUI4    | Array            |
| OOPS GET NOI CODE              | GETNOI       | OOPSGUI8    | Array            |
| OOPS GET OSHA DATA             | OSHA         | OOPSGUIF    | Global Array     |
| OOPS GET POINTED TO            | GETLIST      | OOPSGUI3    | Array            |
| OOPS GET PRT ACC STATUS RPT    | ACCID        | OOPSGUIT    | Global Array     |
| OOPS GET SINGLE FIELD          | GETFLD       | OOPSGUI7    | Single Value     |
| OOPS GET SITE PARAMETER        | SITEPGET     | OOPSGUI6    | Array            |
| OOPS GET STATION INFORMATION   | STATINFO     | OOPSGUI3    | Array            |
| OOPS GET SUPERVISOR            | SUPER        | OOPSGUI4    | Array            |
| OOPS GET UNION                 | UNIGET       | OOPSGUI6    | Array            |
| OOPS GET WITNESSES             | WITR         | OOPSGUI2    | Array            |
| OOPS INCIDENT REPORT           | ENT          | OOPSGUIT    | Array            |
| OOPS LOAD OOPS                 | LOAD         | OOPSGUI4    | Array            |
| OOPS MANUAL XMIT DATA          | ENT          | OOPSGUI7    | Array            |
| OOPS NEEDLESTICK LOG           | NSTICK       | OOPSGUIF    | Global Array     |
| OOPS NEW PERSON DATA           | PER          | OOPSGUI4    | Array            |
| OOPS PUT UNION                 | UNIEDT       | OOPSGUI6    | Single Value     |

| RPC Name                 | Line Tag | Routine | Return Value |
|------------------------------|--------------|-------------|------------------|
| OOPS RELEASE RECORD LOCK     | CLRLCK       | OOPSGUI3    | Single Value     |
| OOPS REMOTE GET USER OPTIONS | OPT          | OOPSGUI1    | Single Value     |
| OOPS REPLACE DATE/TIME       | DTFC         | OOPSGUI8    | Single Value     |
| OOPS REPLACE MULTIPLE        | REPLMULT     | OOPSGUI3    | Array            |
| OOPS REPLACE WP              | REPLWP       | OOPSGUI2    | Array            |
| OOPS SET FIELD               | SETFIELD     | OOPSGUI2    | Array            |
| OOPS SET RECORD LOCK         | SETLCK       | OOPSGUI3    | Single Value     |
| OOPS UNION CONSENT           | CONSENT      | OOPSGUI7    | Array            |
| OOPS VALIDATE AND SIGN       | SETSIGN      | OOPSGUI1    | Array            |
| OOPS VALIDATE TIME           | DTVALID      | OOPSGUI2    | Array            |
| OOPS WCEDIT                  | OWCPCLR      | OOPSGUI7    | Single Value     |
| OOPS WITNESS CREATE          | ADDWITN      | OOPSGUI2    | Array            |
| OOPS WITNESS DELETE          | DELWITN      | OOPSGUI2    | Array            |
| OOPS WITNESS EDIT            | EDTWITN      | OOPSGUI2    | Array            |
| OOPS GET INSTITUTIONS        | GETINST      | OOPSGUI7    | Global Array     |
| OOPS SENSITIVE DATA          | SENSDATA     | OOPSGUI7    | Single Value     |
| OOPS GET MISC REPORT DATA    | ENT          | OOPSGUIR    | Global Array     |
| OOPS GET FAC SHORT LIST      | STA          | OOPSGUIS    | Global Array     |
| OOPS SELECT CA7              | CA7LIST      | OOPSGUIC    | Global Array     |
| OOPS LIST CAS                | LISTCA       | OOPSGUIC    | Global Array     |
| OOPS MULTIPLE DATA           | MULTIPLE     | OOPSGUIC    | Array            |
| OOPS SIGN CA7                | SIGNCA7      | OOPSGUIS    | Single Value     |
| OOPS SIGNATURE VALIDATION    | DECODE       | OOPSGUIS    | Single Value     |
| OOPS SET OSHA300A            | OSHA300      | OOPSGUIC    | Single Value     |
| OOPS ZIP CODE MISMATCH CHECK | ZIPCHK       | OOPSGUI8    | Single Value     |

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No archiving or purging is available with this release.

## Callable Routines/Entry Points/APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines in this package.

# # External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASISTS package relies on the following external packages to run effectively.

> VA FileMan V. 21

> Kernel V. 8

> MailMan V. 7.1

> PAID V. 4

> RPC Broker V.1.1

On the Client/PC side of ASISTS GUI 2.0, the following are the system requirements.

- Intel Pentium 90 or higher (P166 recommended)
- Microsoft Windows 95, 98, NT 4.0,or Windows 2000
- Memory: 32MB of RAM (64MB or more recommended)
- Full Client Install Hard disk space: 19MB
- Reports Install (Optional) on Client Machine Hard disk space: 8MB
- VGA or higher resolution monitor
- Mouse or other pointing device
- Networks supported: Any Microsoft Windows 95, 98, Windows NT, or Windows 2000 or higher compatible network

## DBIA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two DB Integration Agreements with PAID: \#2364 and \#2923.

DBIA 2364 allows for use of the following PAID fields:

> .01 EMPLOYEE

> 6 STATION NUMBER

> 8 SSN

> 10 EDUCATION

> 13 GRADE

> 16 OCCUPATION SERIES

> 31 SEX

> 32 DATE OF BIRTH

> 38 STEP

> 458 COST CENTER/ORGANIZA

> 604 LEVEL

> 80 SEPARATION IND

> 19 PAY BASIS

> 20 PAY PLAN

> 26 RETIREMENT CODE

####### SALARY

> 186 RESIDENCE STATE

> 186.1 RESIDENCE ADDRESS LINE 1

> 186.3 RESIDENCE ADDRESS LINE 3

4.  RESIDENCE ADDRESS ZIP CODE

> 226 EGLI CODE

> 231 HEALTH INSURANCE

DBIA 2923 allows ASISTS the use of \$Order through the top level of ^PRSPC(I). ASISTS gets a count of the number of PAID employees at each facility who are not separated. That information is used in statistical analysis for blood-borne pathogen reporting. After getting the IEN of each PAID employee, the routine will use a FileMan read to determine whether the employee is separated. The routine will be executed on a monthly basis.

DBIA 936 with the KERNEL which allows for use of the routine XUSESIG. This routine, when called from the top, allows the user to setup a personal electronic signature code. It is used within application code to allow the user immediate 'on-the-fly' access to setup the electronic signature, rather than force the user to leave the application and enter a different option to do the same.

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASISTS GUI package is a full version release and requires no previous patches.

## Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables.

# On-line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASISTS GUI package has extensive online help written/compiled as a standard window help file. From any screen within the ASISTS GUI application pressing the F1 key at any time can access help. The online help is driven by screen images that match the screens in the online application. From these images context sensitive help is available. Also, included in the online help file is a table of contents, an index, and a Glossary. The majority of the Help from the Roll n Scroll system was implemented in the online version.

On-line technical documentation pertaining to the ASISTS software, in addition to that, which is located in the help prompts and on the help screens, which are found throughout the ASISTS package, may be generated through utilization of several Kernel options. These include but are not limited to %INDEX; Menu Management, Inquire option and Print Option File; VA FileMan, Data Dictionary Utilities, List File Attributes.

For a more exhaustive option listing and further information about other utilities which supply on-line technical information, please consult the DHCP Kernel Reference Manual.

%INDEX

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adhere(s) to DHCP Programming Standards. The %INDEX output may include the following components: compiled list of Errors and Warnings, Routine Listing, Local Variables, Global Variables, Naked Globals, Label References, and External References. By running %INDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from DHCP Programming Standards which exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run %INDEX for the ASISTS package, specify the following namespaces at the "routine(s) ?\>" prompt: OOPS\*.

ASISTS initialization routines which reside in the UCI in which %INDEX is being run, as well as local routines found within the ASISTS namespace, should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).

INQUIRE OPTION

This Menu Management option provides the following information about a specified option(s): option name, menu text, option description, type of option and lock, if any. In addition, all items on the menu are listed for each menu option.

To secure information about ASISTS options, the user must specify the name or namespace of the option(s) desired. The namespace associated with the ASISTS package is OOPS.

PRINT OPTION FILE

This utility generates a listing of options from the OPTION file. The user may choose to print all of the entries in this file or may elect to specify a single option or range of options. To obtain a list of ASISTS options, the following option namespace should be specified: OOPS.

LIST FILE ATTRIBUTES

This VA FileMan option allows the user to generate documentation pertaining to files and file structure. Utilization of this option via the "Standard" format will yield the following data dictionary information for a specified file(s): file name and description, identifiers, cross-references, files pointed to by the file specified, files which point to the file specified, input templates, print templates, and sort templates. In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

Using the "Global Map" format of this option generates an output which lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates. For a comprehensive listing of ASISTS files, please refer to the File Section of this manual.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Data Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information in this program is covered by the Privacy Act. The level of security for employee records will receive the same degree of protection as the Veteran patients.

Users of this package should be authorized personnel only.

See ASISTS V. 2.0 Security Manual for further information on the VA Fileman Field Protection features of ASISTS V. 2.0.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a Broker aware product written in Delphi 5, the ASISTS GUI connects to the M server from a client workstation. This connection is subject to authentication, as any normal logon requires. If the user possesses the OOPS GUI EMPLOYEE option and successfully logs on to the VistA Server, they will have the ability to run the application. Data is read from and written to the VistA Server to the ASISTS GUI client via the RPC Broker connection server connection. The ASISTS GUI client can be anywhere on the VA’s TCP/IP network.

Encryption is used when a user’s access, verify, and electronic signature codes are sent from the client to the server.

See RPC Broker V. 1.1 Technical Manual for further information on RPC Broker’s security features.

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AOD Administrative Officer of the Day

ASISTS Automated Safety Incident Surveillance Tracking System

Bulletin Message sent to mail group members

CA-1 Federal Employee's Notice of Traumatic Injury and

Claim for Continuation of Pay/Compensation. If

the injury/illness is due to a single incident, a CA-1 is filed.

CA-2 Notice of Occupational Disease and Claim for

Compensation. If the illness is a result of more than one

incident or more than a single shift, then a CA-2 is filed.

CA-7 Request for Compensation. A CA7 can be completed for

any claim that has been transmitted to Department of

Labor.

Case number A number created from the fiscal year and an incrementing

number to designate a specific incident. For example, the

89th record created in FY 1998 would be: 1998-00089.

Case status A record may be considered: Open, Closed, Deleted,

Replaced by amendment

DOI Date of injury/illness

DOL Department of Labor

Electronic signature An encrypted signature stored in VISTA to show that a

report or portion of a report is complete

GUI Graphical User Interface

Incident The action which initiates a CA1 or CA2 (formerly known as a

2162 or Accident Report).

OOPS EH Mail group comprised of personnel from Employee Health

and Infection Control

OOPS INJURY Mail group comprised of personnel from Human Resources

Management, generally compensation specialists

OOPS NDB MESSAGES Mail group comprised of individuals who should receive

messages regarding the transmission of ASISTS incident report

data to the AAC

OOPS SAFETY Mail group comprised of one or more safety officers

OOPS UNION Mail group comprised of union representatives

OOPS WC MESSAGE Mail group with individuals who need to be notified of

error messages, or messages sent from the AAC. There

must be at least one member in this mail group for the

electronic transmission of claims to Department of Labor

(DOL) to properly function.

OOPS WCP Mail group for the Workers’ Compensation personnel

OSHA Occupational Safety and Health Administration

OWCP Office of Worker's Compensation Programs

OWCP Chargeback Code Found on the CA-1 and CA-2 and indicates the Chargeback

code that the claim should be charged to

Source code Found on the CA-1 and CA-2. Code for Object or

Substance that is used along with the Type code which

stands for Action.

Type code Found on the CA-1 and CA-2. Code standing for Action

that is used along with the Source code which stands for

Object or Substance.