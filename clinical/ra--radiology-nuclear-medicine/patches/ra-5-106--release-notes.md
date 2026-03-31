---
title: RA*5*106 National Teleradiology Program Phase 2/Iteration 1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: National Teleradiology Program Phase 2/Iteration 1
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5*106
group_key: "RA:RA:5"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](ra-5-106-national-teleradiology-program-phase-2-iteration-1-release-notes/001.png)
audience: 
keywords: 
  - patch
  - group
  - mail
  - vista
  - member
  - radiology
  - installation
  - table
  - contents
  - postmaster
page_count: 0
word_count: 1019
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p106.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p106.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

![](ra-5-106-national-teleradiology-program-phase-2-iteration-1-release-notes/001.png)

Radiology/Nuclear Medicine 5.0

National Teleradiology Program Phase 2/Iteration 1

Release Notes

for Patch RA\*5.0\*106  
March 2011

Health Systems Design & Development

Provider Systems

# Release Notes for Patch RA\*5.0\*106


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes for Patch RA\5.0\106](#release-notes-for-patch-ra50106)
- [Enhancements for NTP Patch RA\5.0\106](#enhancements-for-ntp-patch-ra50106)
- [Prior to Patch Installation](#prior-to-patch-installation)
- [After Patch Installation](#after-patch-installation)
The objective of this project is to provide support for the national implementation of the National Teleradiology Program as the Veterans Affairs Central Office (VACO) has requested.
Patch RA\*5.0\*106 enhances the Veterans Health Information Systems and Technology Architecture (VistA) Radiology/Nuclear Medicine (Rad/Nuc Med) 5.0 Radiology Information System (VistA RIS) package for the functionality used between the NTP and the local VA sites.
The NSR number for this patch is 20080510.
Notes:
- Before you install patch 106, you must install: RA\*5\*90 and RA\*5\*94.
- The installation time for patch 106 is less than three minutes.

# Enhancements for NTP Patch RA\*5.0\*106

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To accept a new Request Status (via HL7 message) indicating that the teleradiology center is releasing the study back to the local Veterans Administration Medical Center (VAMC) for interpretation
2.  To enhance the VistA Radiology/Nuclear Medicine (VistA RIS) application to process the new request status
- For studies without images, the existing preliminary report is to be deleted.
- For studies with images, the report is to inherit the traits of an Imaging Stub Report.
3.  To notify the users in the RAD HL7 MESSAGES mail group that a study was released back to the local VAMC
- Postmaster appears as sender of the message; RAD HL7 MESSAGES is intended to be a private mail group.
- To ensure mail delivery, make sure that POSTMASTER is added as a MEMBER of the RAD HL7 MESSAGES mail group.
4.  To calculate the correct examination status of the study and to update the study to the correct exam status
- Properly defined examination status parameters improve workflow.
- There is emphasis on examination status parameter setup for patch RA\*5.0\*106, because it is the study's examination status which defines VistARad's unread worklist.
1.  Commercial PACS systems will require the unread worklist to be updated manually, based on verbal communication between personnel at the national teleradiology center and the local VAMC's radiology department.
2.  Check the EXAMINATION STATUS parameter definitions, within imaging type, to make sure the definitions are set up properly.
5.  There is a modification to the ACTIVITY LOG (#74.01) sub-file.
- The TYPE OF ACTION (#2) field is modified to accept a new set of codes value: Q for Quit.
- Q indicates that the National Teleradiology center released the study back to the local facility for interpretation.

# Prior to Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to the installation of patch 106:

1.  You must shut down
- Commercial Off the Shelf (COTS) products broadcasting to the VistA RIS, and
- VistA RIS logical links

> VistA RIS Logical Links

1.  Identify the VistA RIS logical links.

> Note: If you have questions regarding the identification of VistA RIS specific logical links, direct your questions to the national development staff responsible for the VistA RIS.

3.  Shut down the VistA RIS logical links by exercising the following option:

> Select OPTION NAME: HL7 MAIN MENU HL MAIN MENU HL7 Main Menu

> Event monitoring menu ...

> Systems Link Monitor

> Filer and Link Management Options ...

> Message Management Options ...

> Interface Developer Options ...

> Site Parameter Edit

> HLO HL7 (Optimized) MAIN MENU ...

> Select HL7 Main Menu Option: FILER and Link Management Options

> SM Systems Link Monitor

> FL Monitor, Start, Stop Filers

> LM TCP Link Manager Start/Stop

> SA Stop All Messaging Background Processes

> RA Restart/Start All Links and Filers

> DF Default Filers Startup

> SL Start/Stop Links \<-- This is the option to exercise.

> PI Ping (TCP Only)

> ED Link Edit

> ER Link Errors ...

6.  You must notify the Radiology department that to install patch 106, the VistA RIS options must be set to *out of order* and the protocols disabled.
7.  You must prohibit the ordering, registering, case editing, and interpretation of radiology studies during the installation.

# After Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use the KIDS Utilities... \[XPD UTILITY\] option, Install File Print \[XPD PRINT INSTALL FILE\], to verify that the installation of patch 106 was completed correctly; select patch RA\*5.0\*106.
8.  Restart Commercial Off the Shelf (COTS) products broadcasting to the VistA RIS.
9.  Use the Start/Stop Links option to restart the correct VistA RIS logical links.
10. Clear all Radiology users to resume normal activities.

Example: Adding POSTMASTER to the RAD HL7 MESSAGES mail groupNote: The data displayed in the example need not be the same data displayed on your screen, when you follow through on adding POSTMASTER. The Mail Group MEMBER name used in this example is fictitious.

DEVISC4A1:DEV\>D ^XUP

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT320

You have 6 new messages.

Select OPTION NAME: MANAGE MAILMAN XMMGR Manage Mailman

Check MailMan Files for Errors

Create a Mailbox for a user

Disk Space Management ...

Group/Distribution Management ... \<-- Select this option

Local Delivery Management ...

MailMan Site Parameters

Network Management ...

New Features for Managing MailMan

Remote MailLink Directory Menu ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select Manage Mailman Option: GROUP/Distribution Management

Bulletin edit

Edit Distribution List

Enroll in (or Disenroll from) a Mail Group

Mail Group Coordinator's Edit

Mail Group Coordinator's Edit W/Remotes

Mail Group Edit \<-- Select this option

Select Group/Distribution Management Option: MAIL GROUP EDIT

Select MAIL GROUP NAME: RAD HL7 MESSAGES

MAIL GROUP NAME: RAD HL7 MESSAGES//

Select MEMBER: RADPERSONNEL,ONE// ?

Answer with MEMBER

Choose from:

POSTMASTER \<-- if POSTMASTER is listed here,  
you can exit the option.

RADPERSONNEL,ONE

RADPERSONNEL,TWO

You may enter a new MEMBER, if you wish

Enter a local user who should receive mail addressed to this

group. User must have an access code and a mailbox.

Answer with NEW PERSON NAME, or INITIAL, or SSN, or VERIFY CODE, or

NICK NAME, or SERVICE/SECTION, or DEA#, or VA#, or ALIAS, or NPI

Do you want the entire NEW PERSON List? N (No)

Select MEMBER: RADPERSONNEL,ONE//

MEMBER: RADPERSONNEL,ONE//

TYPE:

Select MEMBER: postmaster POSTMASTER

Are you adding 'POSTMASTER' as a new MEMBER (the 3RD for this MAIL

GROUP)? No// y (Yes) \<-- answer 'Yes'

TYPE:

Select MEMBER:

DESCRIPTION:

This mail group is used to inform radiology users about issues regarding

the HL7 interface between the VistA Radiology/Nuclear Medicine application

and Commercial Off The Shelf (COTS) applications.

Edit? NO//

TYPE: private//

RESTRICTIONS:

ORGANIZER:

COORDINATOR:

Select AUTHORIZED SENDER:

Select MEMBER GROUP NAME:

Select REMOTE MEMBER:

Select DISTRIBUTION LIST:

Do you wish to forward past mail group messages

to the user(s) you just added to the mail group(s)? No// NO \<-- answer 'No'

Select MAIL GROUP NAME: