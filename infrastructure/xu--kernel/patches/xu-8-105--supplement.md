---
title: XU*8*105 VistA State Patch Follow-Up
doc_type: SUP
doc_label: Supplement
doc_layer: patch
doc_subject: VistA State Patch Follow-Up
app_code: XU
app_name: Standard Files and Tables
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*105
group_key: "XU:XU:8"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - xtmp
  - xuxtmp
  - routine
  - global
  - site
  - patch
  - county
  - exceptions
  - your
  - xuxcty
page_count: 0
word_count: 718
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Standard_Files_Tables/state_patch_follow_up_xu_8_105.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Standard_Files_Tables/state_patch_follow_up_xu_8_105.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=26"
---

=============================================================================

Run Date: MAR 31, 1999 Designation: XU\*8\*105

Package : KERNEL Priority : MANDATORY

Version : 8 SEQ \#89 Status : RELEASED

=============================================================================

Subject: Cleanup and Identification of Dangling Pointers with County Codes

Category: ROUTINE

Description:

===========

Patch XU\*8\*105 is designed to identify and correct two data problems

associated with the following files:

1\. Patient (File \#2)

2\. Fee Basis Vendor (File \#161.2)

3\. Person (File \#16)

4\. HBHC Patient (File \#631)

The two problems being addressed and corrected with this patch are

described below:

1\. Dangling pointers associated with the County Fields in the

aforementioned files are identified and cleaned up. (set to null)

2\. State and County entries that are currently null are identified

and listed as exceptions. The exceptions are listed in the temporary

global ^XTMP("XUXTMP") This is a new temporary global created by the

patch. These exceptions are identified to provide a list of current state

and county entry errors at each site. They will need to be addressed on a

site-to-site basis.

These problems were discovered during installation of patch XU\*DBA\*3,

which was an effort to cleanup some entries in the County and State codes

in the State File.

Once your site installs this patch, you must run the routine ^XUXCTY. This

routine performs the identification and cleanup of these exceptions. When

this routine has run to completion, the temporary global ^XTMP("XUXTMP")

will exist at your site. This global contains the zero node of all

records found that were either changed or that contain exceptions to be

addressed. The global looks like this:

^XTMP("XUXTMP",0) = 2981106^2981030

^XTMP("XUXTMP",1) = PATIENT FILE RECORDS CLEANED

^XTMP("XUXTMP",2) = BLOW,JOE P.^M^2350303^E^6^6^MEDICINE^99^444556677^THIS

IS TESTING CLASSMAN SOFTWARE^DALY CITY^6^^^53^2891117^^^^1

^XTMP("XUXTMP",3)=SNERD,MORTIMER^M^2560505^E^2^^TRUCKER^4^234567890^^MADER

A^6^^^53^2891117^^^^1

^XTMP("XUXTMP",4) =

^XTMP("XUXTMP",5) = PERSON FILE RECORDS CLEANED

^XTMP("XUXTMP",6) = TRAINING,MANAGER^M^2380731^^2^^^^123456789

^XTMP("XUXTMP",7) = SOUTHERN,MYRNA^F

^XTMP("XUXTMP",8) = JONES,JOAN^^2560506^^^^^^012345678

^XTMP("XUXTMP",9) =

^XTMP("XUXTMP",10) = FEE BASIS VENDOR RECORDS CLEANED

^XTMP("XUXTMP",11) = DING DONG M.D.^222334444^^^^^2^^1^^^^

^XTMP("XUXTMP",12) =

^XTMP("XUXTMP",13) = HBHC PATIENT FILE RECORDS CLEANED

Sites can use the routine ^XUXPRT to print this new global. It may be

quite large, thus your site may want to queue the job for later. Once the

hardcopy of ^XTMP("XUXTMP") has been printed, your site can use the

FileMan option ENTER OR EDIT FILE ENTRIES to enter the correct State

and/or County data.

Routine Information

===================

Routine name Before Checksum After Checksum

XUXCTY N/A 5011240

XUXPRT N/A 293411

Installation:

=============

This patch can be loaded with users on the system. Installation will take

less than 2 minutes.

1\. Use the 'INSTALL/CHECK MESSAGE' option on the PackMan menu.

2\. New routines will not be mapped.

3\. On the KIDS menu under the 'INSTALLATION' menu, use the following

options as desired:

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Backup a Transport Global

4\. On the KIDS menu under the 'INSTALLATION' menu, use the following

option to install the patch:

Install Package(s) (XU\*8.0\*105)

5\. When prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? YES//," respond 'NO'.

6\. Routines were not unmapped as part of step 2, because these are new

routines.

Post Installation

=================

> **NOTE:** GLOBAL ^XTMP("XUXTMP") WILL ONLY EXIST ON YOUR SYSTEM FOR SEVEN

DAYS FROM THE DATE YOU RUN THE ROUTINE ^XUXCTY. THUS, IT IS IMPORTANT

THAT YOU RUN THE PRINT ROUTINE PRIOR TO THE KILL DATE FOR THIS TEMP

GLOBAL. IF YOU MISS HOWEVER, ALL YOU NEED TO DO IS RERUN THE ROUTINE

^XUXCTY.

Once your site installs this patch, you must execute the following to

fully implement the desired functionality:

1 Go into programmers mode D ^XUP

2 From programmers mode run the routine ^XUXCTY. D ^XUXCTY

This routine will perform the identification and cleanup of these

exceptions

3 Examine the global ^XTMP("XUXTMP") which now exists at your site.

To examine the global, its best to use D ^%G. This global contains the

zero node of all the records found to be exceptions or that were changed.

4 Sites use routine ^XUXPRT to print the global. The global maybe

quite large, thus your site may want to queue the job for later.

5 Once the hardcopy of ^XTMP("XUXTMP") has been printed, use the

FileMan option ENTER OR EDIT FILE ENTRIES to enter the correct State

and/or County data.

Routine Information:

====================

Routine Name: XUXCTY

Description of Changes:

Routine Checksum:

Routine Name: XUXPRT

Description of Changes:

Routine Checksum:

=============================================================================

User Information:

Entered By : REDACTED . Date Entered : OCT 30,1998

Completed By: REDACTED Date Completed: NOV 24,1998

Released By : REDACTED Date Released : NOV 25,1998

=============================================================================