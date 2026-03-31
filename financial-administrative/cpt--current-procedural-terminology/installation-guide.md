---
title: CPT Version 6 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: CPT
app_name: Current Procedural Terminology
section: FIN
app_status: active
pkg_ns: CPT
patch_ver: 6
patch_id: CPT*6
group_key: "CPT:CPT:6"
file_numbers: []
security_keys: []
menu_options: 0
description: This package was created using Kernel V. 8.0 and VA FileMan V. 21.0. It was exported using the Kernel Installation and Distribution System (KIDS). You must use Kernel V. 8.0 to install this software from the ICPT6_0.KID file. Installation will take between 5 and 40 minutes.
audience: 
keywords: 
  - icpt
  - site
  - install
  - installation
  - send
  - package
  - delete
  - routines
  - patch
  - deleted
page_count: 0
word_count: 1955
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
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Current_Proc_Terminology_(CPT)/cpt6_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Current_Proc_Terminology_(CPT)/cpt6_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=33"
---

Current Procedural Terminology (CPT)V. 6.0 Installation GuideMay 1997

Introduction

List of Distributed Routines

Package Integration

Installation Steps

Introduction

This package was created using Kernel V. 8.0 and VA FileMan V. 21.0. It was exported using the Kernel Installation and Distribution System (KIDS). You must use Kernel V. 8.0 to install this software from the ICPT6_0.KID file. Installation will take between 5 and 40 minutes.

The CPT data files (#81 - \#81.3) are loaded separately to expedite the installation process. The CPT globals were saved using the %GTO utility. Using the appropriate utility for your system (%GTI or %GR), restore the CPT globals from the appropriate file(s).

Alpha sites should use the file ICPT6_0.GBL, which contains all of the files, saved using the %GTO utility.

MSM sites need to load the globals separately. The files MSM sites should use are:

ICPT6_0G1.GBL which contains the ^ICPT global

ICPT6_0G2.GBL which contains the files stored in the ^DIC global (^DIC(81.1-81.3)).

Patches DG\*5.3\*123 and PX\*1.0\*32 will be automatically installed as part of this CPT installation, along with two routines from patch SD\*5.3\*111. The Patch Application History multiple of the Package file will be updated for the DG and PX patch. The Patch Application History multiple of the Package file for the SD patch will be updated when the rest of the patch is installed in the separate installation of SD\*5.3\*111 (which must follow the installation of this package).

List of Distributed Routines

DGYACPT ICPT60PR ICPT60PT ICPTAPIU ICPTCOD

ICPTCR ICPTMOD ICPTPRN ICPTSR1 ICPTSR2

PXBUTL SDAMBAE2 SDAMBAE3 VACPT VAFHLPR1

15 routines

Package Integration

1. The following package versions (or higher) and the following patches must be installed prior to loading this version of the CPT update.

Kernel V. 8.0

VA FileMan V. 21.0

PIMS (MAS) V. 5.3

PCE V. 1.0

XU\*8.0\*51

DG\*5.3\*94

2. The following routines are included in the KIDS install and are loaded with this version of the CPT update.

Routine Checksums

DGYACPT 279218

ICPT60PR 3025554

ICPT60PT 2039236

ICPTAPIU 1872089

ICPTCOD 3761042

ICPTCR 1900266

ICPTMOD 4511692

ICPTPRN 1706506

ICPTSR1 1432053

ICPTSR2 1157028

Patch Checksums

(See descriptions of changes in Patches DG\*5.3\*123, SD\*5.3\*111 and PX\*1.0\*32)

Routine Name Before Patch After Patch Patch List

PXBUTL 8211033 7306146 32

SDAMBAE2 14775992 13627813 15,79,111

SDAMBAE3 9615951 8689707 18,29,40,111

VACPT 638691 163873 123

VAFHLPR1 4402356 4354253 94,123

Installation Steps

Before starting the installation process, it is recommended that the following files be backed up as they will all be deleted as part of the install process.

<u>Global</u> <u>File</u>

^ICPT( CPT (#81)

^DIC(81.1, CPT CATEGORY (#81.1)

^DIC(81.2, CPT COPYRIGHT (#81.2)

^DIC(81.3, CPT MODIFIER (#81.3)

^DIC(81.4, CPT MODIFIER CATEGORY (#81.4)

^DIC(81.5, CPT SOURCE (#81.5)

1. The ^ICPT global will be killed during the installation. When rebuilt, it will consume approximately 10.3 megabytes of journal space. Ensure that you have adequate journal space prior to installation.

It is recommended that those users who would be referencing CPT codes be off the system. These include users of the ambulatory procedure codes in Scheduling and those affected users in Integrated Billing, Fee Basis, Radiology, and Surgery.

2. Make certain that your DUZ variable is set to a valid user number and that DUZ(0)="@". Alpha sites sign into the UCI where the ^ICPT global is located.

MSM sites use a 40K partition.

3. Check routine mapping for SDAMBAE2, SDAMBAE3, PXBUTL, VACPT, and VAFHLPR1. (The ICPT\* routines are not recommended for mapping.) Disable mapping, if applicable.
4. Delete the DGYA\* routines from all systems prior to installing the package.
5. Using the Kernel Installation & Distribution menu \[XPD MAIN\], load, verify, and install the package as per the sample below (*4 KIDS Steps*). The sample installation dialogue that follows may vary depending on your system (Alpha or MSM).

*KIDS Step \#1*

Select Kernel Installation & Distribution System Option: Installation

Select Installation Option: LOAD a Distribution

Enter a Host File: ICPT6_0.KID\*\*\*NOTE: MSM sites will have to use the full file reference, e.g., C:\MSM\ICPT6_0.KID\*\*\*

KIDS Distribution saved on May 11, 1997@09:14:44

Comment: CPT V6.0 RELEASE

This Distribution contains Transport Globals for the following Package(s):

ICPT 6.0

Want to Continue with Load? YES// \<RET\>

Loading Distribution...

Use ICPT 6.0 to install this Distribution.

*KIDS Step \#2*

Select Installation Option: VERIFY Checksums in Transport Global

Select INSTALL NAME: ICPT 6.0 Loaded from Distribution 5/12/97@09:07:29

=\> CPT V6.0 RELEASE ;Created on May 11, 1997@09:14:44

DEVICE: HOME// \<RET\> LAT

PACKAGE: ICPT 6.0 May 12, 1997 9:08 am PAGE 1

-----------------------------------------------------------------------

15 Routine checked, 0 failed.

\*\*\*NOTE: If any routine checksums fail, contact PIMS Customer Support at a CIO Field Office and do NOT proceed with the installation process.\*\*\KIDS Step \#3*

Select Kernel Installation & Distribution System Option: Utilities

Select Utilities Option: Build File Print

Select BUILD NAME: ICPT 6.0 ICPT/HCPCS CODES

DEVICE: HOME// ;;999 LAT

PACKAGE: ICPT 6.0 May 12, 1997 8:05 am PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE

NATIONAL PACKAGE: ICPT/HCPCS CODES

DESCRIPTION:

See associated package documentation for description.

ENVIRONMENT CHECK :

PRE-INIT ROUTINE : ICPT60PR

POST-INIT ROUTINE : ICPT60PT

PRE-TRANSPORT RTN :

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# NAME DD CODE W/FILE DATA PTS RIDE

-------------------------------------------------------------------------------

81 CPT YES YES NO

81.1 CPT CATEGORY YES YES NO

81.2 CPT COPYRIGHT YES YES NO

81.3 CPT MODIFIER YES YES NO

409.5 SCHEDULING VISITS YES NO NO

Partial DD: subDD: 409.51 fld: 21

fld: 22

fld: 23

fld: 24

fld: 25

PRINT TEMPLATE:

DGYA MODIFIER DESCRIPTION FILE \#81.3 DELETE AT SITE

DGYA PRINT FILE \#81 DELETE AT SITE

ICPT MODIFIERS BY RANGE FILE \#81.3 SEND TO SITE

ICPT PRINT FILE \#81 SEND TO SITE

SORT TEMPLATE:

ICPT MODIFIERS FOR RANGE FILE \#81.3 SEND TO SITE

ICPT NEW/INACTIVE CODES FILE \#81 SEND TO SITE

INPUT TEMPLATE:

SDAMBT FILE \#409.5 SEND TO SITE

SDXACSE FILE \#409.5 SEND TO SITE

ROUTINE:

DGYACPT SEND TO SITE

DGYADSRT DELETE AT SITE

DGYANSRT DELETE AT SITE

DGYAPRN DELETE AT SITE

DGYARSR2 DELETE AT SITE

DGYARSRT DELETE AT SITE

DGYAUP DELETE AT SITE

DGYAUPAP DELETE AT SITE

DGYAUPY DELETE AT SITE

DGYAVEN DELETE AT SITE

DGYAVPR DELETE AT SITE

DGYAVPT DELETE AT SITE

ICPTAPIU SEND TO SITE

ICPTCOD SEND TO SITE

ICPTCR SEND TO SITE

ICPTMOD SEND TO SITE

ICPTPRN SEND TO SITE

ICPTSR1 SEND TO SITE

ICPTSR2 SEND TO SITE

PXBUTL SEND TO SITE

SDAMBAE2 SEND TO SITE

SDAMBAE3 SEND TO SITE

VACPT SEND TO SITE

VAFHLPR1 SEND TO SITE

OPTION:

DGYA AMBUL PROC LOCAL ACTIVE DELETE AT SITE

DGYA CPT CODES INACTIVE DELETE AT SITE

DGYA NEW CPT CODES DELETE AT SITE

DGYA OUTPUT MENU DELETE AT SITE

DGYA REVISED CPT CODES DELETE AT SITE

ICPT CPT CODES INACTIVE SEND TO SITE

ICPT MODIFIERS BY RANGE SEND TO SITE

ICPT NEW CPT CODES SEND TO SITE

ICPT OUTPUT MENU SEND TO SITE

ICPT REVISED CPT CODES SEND TO SITE

REQUIRED BUILDS: ACTION:

XU\*8.0\*51 Don't install, leave global

SD\*5.3\*79 Don't install, leave global

PCE PATIENT CARE ENCOUNTER 1.0 Don't install, leave global

DG\*5.3\*94 Don't install, leave global

\*\*\*NOTE: The CPT globals will be killed as part of this installation.\*\*\KIDS Step \#4*

Select Installation Option: Install Package(s)

Select INSTALL NAME: ICPT 6.0 Loaded from Distribution 5/12/97@11:40:55

=\> CPT PACKAGE;Created on May 11, 1997

This Distribution was loaded on May 12, 1997@11:40:55 with header of

CPT PACKAGE;Created on May 11, 1997@11:37:08

It consisted of the following Install(s):

ICPT 6.0

ICPT 6.0

Install Questions for ICPT 6.0

Incoming Files:

81 CPT

> **NOTE:** You already have the 'CPT' File.

81.1 CPT CATEGORY (including data)

> **NOTE:** You already have the 'CPT CATEGORY' File.

81.2 CPT COPYRIGHT (including data)

> **NOTE:** You already have the 'CPT COPYRIGHT' File.

81.3 CPT MODIFIER (including data)

> **NOTE:** You already have the 'CPT MODIFIER' File.

409.5 SCHEDULING VISITS (Partial Definition)

> **NOTE:** You already have the 'SCHEDULING VISITS' File.

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// \<RET\>\*\*\*NOTE: If you are installing on a MSM system, you will be asked to move routines to other CPUs.\*\*\*

Want to MOVE routines to other CPUs? NO// YES

Please enter the VOLUME SETS you want me to update.

Select Volume Set: CSA

Are you adding “CSA” as a new VOLUME SET (the 1<sup>st</sup> for this INSTALL)? YES

Select Volume Set: \<RET\>

Enter options you wish to mark as 'Out Of Order': DGYA\*\*\*\*NOTE: Include any options referencing the CPT codes in Scheduling, Integrated Billing, Fee Basis, Surgery, and Radiology.\*\*\*Enter options you wish to mark as 'Out Of Order': \<RET\>

Enter protocols you wish to mark as 'Out Of Order': \<RET\>\*\*\*NOTE: Enter the number of minutes necessary for users currently logged on to log off prior to beginning the installation.\*\*\*

Delay Install (Minutes): (0-60): 0// \<RET\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<RET\> LAT

Install Started for ICPT 6.0 :

May 12, 1997@11:42:33

Installing Routines

May 12, 1997@11:42:35

Running Pre-Install Routine: ^ICPT60PR

Both the data and data dictionary will be deleted for the following files:

81 - CPT; 81.1 - CPT CATEGORY; 81.2 - CPT COPYRIGHT; and 81.3 - CPT MODIFIER

Files 81.4 - CPT MODIFIER CATEGORY and 81.5 - CPT SOURCE will be

permanently deleted with this release.

File \#81.1, CPT CATEGORY, has been deleted

File \#81.2, CPT COPYRIGHT has been deleted

File \#81.3, CPT MODIFIER has been deleted

File \#81.4, CPT MODIFIER CATEGORY has been permanently deleted.

File \#81.5, CPT SOURCE has been permanently deleted.

\>\>\> Deleting data and data dictionary for file \#81, CPT

... File data and DD deletions complete.

Installing Data Dictionaries:

May 12, 1997@11:45:15

Installing Data: ....

May 12, 1997@11:46:10

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing SORT TEMPLATE

Installing OPTION

May 12, 1997@11:46:16

Running Post-Install Routine: ^ICPT60PT

\>\>Updating Patch Application History for PCE with PX\*1\*32

\>\>Updating Patch Application History for REGISTRATION with DG\*5.3\*123

\*\*\* YOU MUST LOAD THE CPT GLOBALS FROM THE APPROPRIATE \*\*\*

\*\*\* ICPT6\_\*.GBL UPON COMPLETION OF THIS INSTALLATION! \*\*\*

Updating Routine file...

The following Routines were created during this install:

SDXA

SDXA1

SDXA2

SDXACSE

SDXACSE1

SDXACSE2

Updating KIDS files...

ICPT 6.0 Installed.

May 12, 1997@11:46:19

Install Completed

6. Check install messages for any error messages prior to proceeding.

Sample INSTALL print

PACKAGE: ICPT 6.0 May 14, 1997 8:21 am PAGE 1

COMPLETED ELAPSED

------------------------------------------------------------------------------

STATUS: Install Completed DATE LOADED: MAY 14, 1997@07:59:59

INSTALLED BY: CPTEMPLOYEE,ONE

NATIONAL PACKAGE: ICPT/HCPCS CODES

INSTALL STARTED: MAY 14, 1997@08:01:20 08:07:25 0:06:05

ROUTINES: 08:01:24 0:00:04

PRE-INIT CHECK POINTS:

XPD PREINSTALL STARTED 08:06:46 0:05:22

XPD PREINSTALL COMPLETED 08:06:47 0:00:01

FILES:

CPT 08:06:52 0:00:05

CPT CATEGORY 08:06:53 0:00:01

CPT COPYRIGHT 08:06:54 0:00:01

CPT MODIFIER 08:06:56 0:00:02

SCHEDULING VISITS 08:07 0:00:04

PRINT TEMPLATE 08:07:02 0:00:02

SORT TEMPLATE 08:07:03 0:00:01

INPUT TEMPLATE 08:07:11 0:00:08

OPTION 08:07:18 0:00:07

POST-INIT CHECK POINTS:

XPD POSTINSTALL STARTED 08:07:20 0:00:02

XPD POSTINSTALL COMPLETED 08:07:20

INSTALL QUESTION PROMPT ANSWER

XPZ1 Want to DISABLE Scheduled Options, Menu Options, and Protocols NO

MESSAGES:

Install Started for ICPT 6.0 :

May 14, 1997@08:01:20

Installing Routines:

May 14, 1997@08:01:24

Running Pre-Install Routine: ^ICPT60PR

Both the data and data dictionary will be deleted for the following files:

81 - CPT; 81.1 - CPT CATEGORY; 81.2 - CPT COPYRIGHT; and 81.3 - CPT MODIFIER

Files 81.4 - CPT MODIFIER CATEGORY and 81.5 - CPT SOURCE will be

permanently deleted with this release.

File \#81.1, CPT CATEGORY, has been deleted

File \#81.2, CPT COPYRIGHT has been deleted

File \#81.3, CPT MODIFIER has been deleted

File \#81.4, CPT MODIFIER CATEGORY has been permanently deleted.

File \#81.5, CPT SOURCE has been permanently deleted.

\>\>\> Deleting data and data dictionary for file \#81, CPT...

... File data and DD deletions complete.

Installing Data Dictionaries:

May 14, 1997@08:07

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing SORT TEMPLATE

Installing INPUT TEMPLATE

Installing OPTION

May 14, 1997@08:07:18

Running Post-Install Routine: ^ICPT60PT

\>\>Updating Patch Application History for PCE with PX\*1\*32

\>\>Updating Patch Application History for REGISTRATION with DG\*5.3\*123

\*\*\* YOU MUST LOAD THE CPT GLOBALS FROM THE APPROPRIATE \*\*\*

\*\*\* ICPT6\_\*.GBL UPON COMPLETION OF THIS INSTALLATION! \*\*\*

Updating Routine file...

The following Routines were created during this install:

SDXA

SDXA1

SDXA2

SDXACSE

SDXACSE1

SDXACSE2

Updating KIDS files...

ICPT 6.0 Installed.

May 14, 1997@08:07:25

7. Global load. Use the appropriate utility for your system to restore the CPT globals. They were saved using ^%GTO.

> For Alpha: \>D^%GTI for file ICPT6_0.GBL

> For MSM: \>D^%GR for files ICPT6_G1.GBL and ICPT6_G2.GBL

After loading the globals, verify that the 0-nodes look like:

^ICPT(0)=CPT^81I^104646^13961

^DIC(81.1,0)=CPT CATEGORY ^81.1^198^197

^DIC(81.2,0)=CPT COPYRIGHT ^81.2^1^1

^DIC(81.3,0)=CPT MODIFIER ^81.3I^358^341

To ensure that the globals loaded correctly, use your global lister to check the following nodes of each of the four files:

^ICPT(104646,0)=Q0157^Human albumin 25% ^195^^^H

^DIC(81.1,198,0)=HEARING SERVICES^s^^V5000^V5999^H

^DIC(81.2,1,0)=CPT MESSAGE^2970602

^DIC(81.3,358,0)=YY^CWT/VI SUPPORTED EMPLOYMENT^^V

8. Move ICPT\* routines and SDAMBAE2, SDAMBAE3, PXBUTL, VACPT, VAFHLPR1 to all systems if not done via KIDS. (If ==\> Want to MOVE routines to other CPUs? NO// in installation.)
9. Re-enable mapping, if disabled.
10. If users have been taken off line, they can now be brought back on line.
11. Upon successful installation of the ICPT6_0.KID build and the ICPT6\_\*.GBL globals, routines ICPT6\* may be deleted.
12. The following two patches need to be installed at this time: IB\*2\*76 and SD\*5.3\*111. The IB patch must be installed first, as it is required by the SD patch.