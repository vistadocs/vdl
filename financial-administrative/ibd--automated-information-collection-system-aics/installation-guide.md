---
title: AICS Version 3 Installation Guide
doc_type: IG
doc_label: Installation Guide
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
file_numbers: []
security_keys: []
menu_options: 0
description: - [Package Integration](#package-integration) ![](aics-version-3-installation-guide/001.png) aUTOMATED iNFORMATIONCOLLECTION SYSTEMAICSINSTALLATION GUIDE April 1997 Health Systems Design & Development (HSD&D) Table of Contents I. Introduction 1 > Package Integration 1 II\. Client 3 > Pre-Install Ste
audience: 
keywords: 
  - aics
  - your
  - ibdx
  - form
  - installation
  - scanner
  - install
  - paper
  - package
  - transport
page_count: 0
word_count: 4516
section_count: 2
table_count: 6
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics3_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics3_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=30"
---

## Table of Contents

  - [Package Integration](#package-integration)
![](aics-version-3-installation-guide/001.png)
aUTOMATED iNFORMATIONCOLLECTION SYSTEMAICSINSTALLATION GUIDE
April 1997
Health Systems Design & Development (HSD&D)
Table of Contents
I. Introduction 1
> Package Integration 1
II\. Client 3
> Pre-Install Steps 3
> Installation Activity 3
III\. Server 5
> Pre-Install Steps 5
> Installation Activity 5
IV\. Appendix A - Files Installed on Client Workstation and Sample Installation
V. Appendix B - Sample Server Installation 23
VI\. Appendix C - Checksum Values 35
VII\. Appendix D - Scanner Calibration 39
I. Introduction
This package was created using Kernel V. 8.0 and VA FileMan V. 21.0. It was exported using the Kernel Installation and Distribution System (KIDS) instead of the FileMan DIFROM utility. You must use Kernel V. 8.0 to install this software. Installation (not including the placement of globals) will take between 2 and 15 minutes.
Please review the KIDS documentation and familiarize yourself with KIDS prior to installing this package.

## Package Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following package versions (or higher) must be installed prior to loading the AICS software. AICS's environment check routine checks for certain critical patches to each of these packages. Sites should verify that all patches to these packages have been installed prior to the install of AICS.

> Kernel V. 8.0

> VA FileMan V. 21.0

> RPC Broker V. 1.0

> PCE V. 1.0

> PIMS V. 5.3

> Kernel Toolkit V. 7.3

> Clinical Lexicon Utility V. 1.0 or Lexicon Utility V. 2.0

> Problem List V. 2.0 (including patch GMP\*2\*3)

> Visit Tracking V. 2.0

> During the Post Installation routine, AICS will determine the version of the Lexicon Utility you are running and will update the data dictionary for fields that point to the EXPRESSIONS file (#757.01) to the correct global location.

> A list of the checksum values is located in Appendix C.

II\. Client

> Pre-Install Steps

> You must have a client workstation that has the RPC Broker’s Client Manager running. You must be able to run the RPC Broker Test provided by the RPC Broker in order to run AICS. The client software needs to be installed on a workstation to do the scanning functionality for AICS. Workstations should conform to the “Veterans Health Administration Recommendations to the Field - August 3, 1995” document. This document may be found on the VHA Home Page - or directly via *www.va.gov/wsnosrec.htm*. The workstations must meet the following requirements.

> 1. At a minimum, be a 80486 CPU-based PC workstation with 20 megabytes of RAM. A Pentium 100 with 32 megabytes is the recommended minimum.

> 2. Have one of the following operating systems:

- 
- 

> MS Windows for Workgroups V. 3.11,MS Windows 95.

> 3. Have Network Capability:

- 
- 

Each workstation should be networked into your V*IST*A Server through a local area network, using a network interface card and TCP/IP protocol; OR, under Windows 95, a Point-to-Point Protocol (PPP) into a Windows NT Server.Successfully run the RPC Broker’s RPC Broker Test on each client workstation. (See Section III - Server, Installation Activity.)

> Installation Activity

> Before you install AICS on a client workstation, you should have successfully run the RPC Broker Test program and executed each of its functions. You should also make sure that Paper Keyboard has been loaded. Do not proceed until this has been accomplished.

> The following steps must be taken for each workstation that will be used as an AICS workstation.

> 1. Get AICS3_0.EXE.

> This can be obtained from the appropriate anonymous software directory.

- 
- 

Make sure to set transfer as BINARY.Get the AICS3_0.EXE file. Depending on the FTP software, this file should be placed in a shared directory. If you cannot find it, use Window's File Manager's Search functionality.

> 2. Find the AICS3_0.EXE file. It is not necessary to copy the file; the file can be run from the shared directory.

> 3. Run AICS3_0.EXE (double click on it). This starts the AICS installation. See Appendix A for information on the files installed on the Client Workstation and a sample run of the installation.

- 
- 
- 

> Example: Run c:\xxx\AICS3_0.EXE from Program Manager.Take all the default prompts unless it causes a conflict.The install program creates an AICS directory, three subdirectories (unrforms, images, backup), and a new Windows Program Group. It populates the Program Group with the AICS Scanning Work Center Icon, the AICS Scanning Work Center Help Icon, and the AICS Scanning Work Center Uninstall Icon.

> \*\*\*Load Server software before continuing\*\*\*

> 4. Run the AICS Client software.

- 
- 
- 
- 
- 

> Double click on the AICS Scanning Work Center Icon.Logon either by clicking the logon speed button or by selecting Logon from the File Menu. Make entries for both access and verify codes. Note that moving the cursor over any button will display additional information on that button.Should an error dialog box appear with an ABORT or IGNORE button, clicking the ABORT will shut down the application; the IGNORE button will clear the exception and attempt to continue. If you IGNORE, you may see additional errors depending on the severity of the initial error.You have connected to the server database when you hear a bell and see the message displaying which server you are connected to at the bottom of the screen.Use the client software. Note that not all menu items are available and not all data fields have connections with the database.

> 5. Calibrate your scanner. Appendix D lists the steps to take in order to calibrate your scanner. This step must be done before scanning forms.

III\. Server

> Pre-Install Steps

> You must have all current Kernel, Kernel Toolkit, VA FileMan, PCE, PIMS, Problem List, Visit Tracking, and RPC Broker patches installed.

> *Kernel V. 8.0*

> The following patches are checked for by the environment check routine.

> XU\*8\*2

> XU\*8\*15

> XU\*8\*16

> XU\*8\*28

> XU\*8\*32

> XU\*8\*44

> Installation Activity

> 1. Install RPC Broker V. 1.0 using the RPC Broker Installation instructions.

> Loading and Installing the KIDS Distribution should be accomplished during non-peak hours to minimize disruption to users. Installation of the KIDS Distribution will take less than 30 minutes.

> a. Review your mapped set. If you map routines, you should disable routine mapping on the IBD\* routines.

> b. If you wish, you may disable journalling for IBE and IBD globals, as appropriate.

> c. From the Kernel Installation and Distribution System Menu, select the Installation menu.

> d. From this menu, select the Load a Distribution option. Enter “AICS3_0.KID” at the “Enter a Host File:” prompt. Enter YES at the “Want to Continue with Load? YES//” and “Want to RUN the Environment Check Routine? YES//” prompts.

> e. From the Installation menu, you may elect to use the following options (when prompted for INSTALL NAME, enter AICS3_0.KID.).

- 
- 
- 

Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.Compare Transport Global to Current System - this option will allow you to view all changes that will be made upon installation. It compares all components of the package (routines, DDs, templates, etc.).Verify Checksums in Transport Global - this option will allow you to ensure the integrity of the routines that are in the transport global.

> f. Use the Install Package(s) option and select the package, AICS3_0.KID.

> g. Respond to the prompts as follows:

- 
- 

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>YES</u>Disable IBD\*

> h. MSM sites: Please ensure you answer YES when asked if you want to move the routines to other systems, and indicate the appropriate CPUs.

> i. If routines were unmapped as part of Step 1a, they should be returned to the mapped set once the installation has run to completion.

> 2. Assign Security Keys.

- 
- 
- 

IBDF IRM should be assigned to those who access the IRM menu option.IBD SCAN MANAGER should be assigned to the users who will be using the scanning software.IBD MANAGER should be assigned to the user who needs to perform functions in AICS that should not be allocated to all users of the package.

> 3. The IBD SCANNING WORKSTATION option must be given as a secondary menu to users who will be using the scanning software.

> 4. OPTIONAL: Print out a copy of the AICS builds.

- 
- 
- 
- 

> Select the Kernel Installation & Distribution System menu.Select the Utilities menu.Select Install File Print.Print Automated Info Collection Sys 3.0.  
> 5. Verify that the following options are queued on the Taskmanager menu.

> Option Name Frequency Device

> ==============================================================

> IBDF AUTO PURGE FROM TRACKING 7D None

> IBDF BACKGRD EF PRINT QUEUE 1D None

> 6. Enable Journaling on IBD and IBE globals.

> 7. Reload the routine map set and enable routine mapping. Routines recommended for mapping are: IBDF1\*, IBDF2\*, IBDF5A\*, IBDF9A1\*, IBDFQSC1, IBDFU\*, IBDFDE\*, IBDFBK\*, and IBDFRPC\*.

> Note: It is necessary for all encounter forms to be recompiled due to a correction made to the narrative passed by scanning. The post init routine will uncompile all encounter forms. When printing forms, the forms will recompile in the background, invisible to the user.

> Note: Two new parameters have been added to the ENCOUNTER FORM PARAMETERS file (# 357.09). The first, STOP DEFAULTING C/O DATE/TIME field \#1.02, is an optional parameter to stop defaulting the check out date/time to the scanning date/time. The second is DAYS TO PRPINT 1010F. If choosing to print 1010F with the Encounter Forms, this is the number of days between expiration of a Means Test and the appointment date before that you want to print 1010Fs for.

> 8. A resource device, IBD Resource, is automatically added to your Device file with 1 resource slot allocated. Large sites may want to increase the number of resource slots.

> 9. Review the AICS V. 3.0 site parameters. Use the IBDF EDIT SITE PARAM option or run routine, ^IBDFESP. Enter the purge parameters. Initially, it is recommended that the RECORDS TO PURGE field be set to ALL to allow the purge utility to delete all appropriately aged records. The FORM TRACKING RETENTION DAYS field should be set to 60 to allow purging of all records at least 60 days old. After a site begins scanning the field, RECORDS TO PURGE should be set to COMPLETED to allow tracking of incomplete forms.  
> 10. If you would like to receive notification when the purge completes, set up a public mail group whose recipients will receive a message for purging of records. This is not a bulletin per say, since there is not an entry in the Bulletin file. Also, that mail group must be entered in the IBDF EDIT SITE PARAM option for the parameter, PURGE NOTIFICATION MAIL GROUP. Make sure you are a member of this mail group. This mail group will automatically receive notification of purge results. Results are also stored in the AICS PURGE LOG file and may be reviewed. Mail notification is not required.

> 11. Edit the ENCOUNTER FORM PRINTERS file (#357.94) to indicate if a printer supports PCL5. In order to print a scannable form, this file must have an entry for the terminal type being used, and it must indicate that it is a PCL5-supported printer. Use the IBDF EDIT PRINTERS option or run routine, ^IBDFDVE. This option also adds the correct printer sequences for duplex printing to PCL5 printers (if you have not already done so).

> 12. With the release of AICS V. 3.0, the scanning software will default the checkout date/time to that of the time of scanning, if there is not a checkout date/time in PCE or no checkout date/time on the Encounter Form. Any site that wishes this not to happen (especially PANDAS sites), must enter YES at the "Stop Defaulting C/O Date/Time" prompt in the ENCOUNTER FORM PARAMETERS file (#357.09).

IV\. Appendix A - Files Installed on Client Workstation and Sample Installation

C:\vista\aics\ibdscan.exe

C:\vista\aics\ibdscan.hlp

C:\vista\aics\ibdabt.dll

C:\vista\aics\unwise.exe

C:\paperkey\aicsmstr.fs

C:\paperkey\aicsscan.fs

C:\paperkey\ibdnorm.cfg

C:\paperkey\ibdrotd.cfg

C:\vista\aics\tutorials\Ibdcalib.exe

C:\vista\aics\tutorials\Ibddemo.exe

C:\vista\aics\tutorials\Ibddhcp.exe

C:\vista\aics\tutorials\Ibdpref.exe

The following series of screens are a representation of the screens the user will encounter when installing the AICS Scanning Workstation.

Initial Screen

![](aics-version-3-installation-guide/002.png)

Answer OK to start the installation of the Workstation. If you choose to cancel, the installation will abort.

Destination Directory

![](aics-version-3-installation-guide/003.png)

Choose the directory where the AICS Scanning Workstation will be installed. The default directory will be contained in the Destination Directory box. If you wish to install in another directory, choose your preference, then OK. If you choose to cancel, the installation will abort.

Backup Screen

![](aics-version-3-installation-guide/004.png)

If the user wishes to make backup copies of the files that are modified during the installation, choose YES. If backup copies are not desired, answer NO. If you choose to cancel, the installation will abort.

Backup Directory

![](aics-version-3-installation-guide/005.png)

Select the directory that will store the files that will be backed up during installation. The default will be in the Destination Directory box, choose OK or choose the directory you wish to store the files in, then choose OK. If you choose to cancel, the installation will abort.

Paper Keyboard Directory

![](aics-version-3-installation-guide/006.png)

Select the path that contains Paper Keyboard. Two Master Form Spec files will be installed there. The default will be in the C:\Paperkey box. Choose OK or choose the directory you wish to install the Master Form Spec files in, then choose OK. If you choose to cancel, the installation will abort.

Delete Old Form Specs

![](aics-version-3-installation-guide/007.png)

Answer YES to allow the automatic deletion of form specs in the Paper Keyboard directory with file names EF\*.FS. Choosing NO will not allow this to occur. If you cancel, the program will abort. Remember to make backup copies of your files if you haven’t already done so.

Deleting Old Form Specs Confirmation

![](aics-version-3-installation-guide/008.png)

Answering OK will allow the form spec deletion to occur. Those files in the Paper Keyboard directory with file names EF\*.FS will be deleted.

Select Scanner

![](aics-version-3-installation-guide/009.png)

Select the type of scanner attached to this workstation from the pull down list. The correct Paper Keyboard configuration files will be loaded by AICS. Choose OK to select the scanner listed in the box. Choose cancel to abort the installation.

HP Scanner Selected

![](aics-version-3-installation-guide/010.png)

Choose OK to verify the scanner that you chose in the previous screen.

Install Tutorials

![](aics-version-3-installation-guide/011.png)

Choose YES to install the four tutorial files for the scanning software. Choosing NO will not install these files.

Workstation ID

![](aics-version-3-installation-guide/012.png)

Choose the Workstation ID. The default ID from the installation script will be contained in the box. Each Workstation should have a unique ID. Choose one and select OK. If you choose to cancel, the installation will abort.

Setting DDE Time-out

![](aics-version-3-installation-guide/013.png)

Answering OK to this prompt allows the DDE time-out to be set to 120 seconds. This screen will only display on the first installation.

Start Menu

![](aics-version-3-installation-guide/014.png)

Choose Yes to add a shortcut for the AICS Scanning Workstation to the Start Menu. Choose No, to not do so. If you choose to cancel, the installation will abort.

V. Appendix B - Sample Server Installation

Sample FTP Download of AICS KIDS Distribution

ISC1A3\$ FTP REDACTED

220 REDACTED.GOV FTP Server (Version V4.1-12) Ready.

Connected to REDACTED

Name (REDACTED:REDACTED): ANONYMOUS

331 Guest login ok, send ident as password.

Password:

230 Guest login ok, access restrictions apply.

FTP\> cd software

250 CWD command successful.

FTP\> get aics3\*.kid

200 TYPE set to IMAGE.

200 PORT command successful.

150 Opening data connection for AICS3_0.KID;1 (REDACTED,4295)

226 Transfer complete.

local: VA3\$:\[REDACTED\]AICS3_0.KID;1 remote: AICS3_0.KID;1

2164930 bytes received in 00:00:03.38 seconds (625.12 Kbytes/s)

FTP\> binary

200 TYPE set to IMAGE.

FTP\> get aics3\*.exe

200 PORT command successful.

150 Opening data connection for AICS3_0.EXE;1 (REDACTED,4297)

226 Transfer complete.

local: VA3\$:\[REDACTED\]AICS3_0.EXE;1 remote: AICS3_0.EXE;1

1454080 bytes received in 00:00:01.71 seconds (828.47 Kbytes/s)

FTP\>bye

221 Goodbye

Sample KIDS Installation

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

Select OPTION NAME: INSTALLATION XPD INSTALLATION MENU Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: Load a Distribution

Enter a Host File: AICS3_0.KID

KIDS Distribution saved on Apr 24, 1997@11:24:33

Comment: AICS V3.0 RELEASE 4/24/97

This Distribution contains Transport Globals for the following Package(s):

AUTOMATED INFO COLLECTION SYS 3.0

Want to Continue with Load? YES// \<RET\>

Loading Distribution...

Want to RUN the Environment Check Routine? YES// \<RET\>

AUTOMATED INFO COLLECTION SYS 3.0

Will first run the Environment Check Routine, IBD3KENV

AICS 3.0 Installation Requirements:

\>\>\> Checking Environment:

Environment checks OK

\>\>\> Checking PACKAGE File Entries:

Checking for required patch XU\*8.0\*2...OK

Checking for required patch XU\*8.0\*15...OK

Checking for required patch XU\*8.0\*16...OK

Checking for required patch XU\*8.0\*28...OK

Checking for required patch XU\*8.0\*32...OK

Checking for required patch XU\*8.0\*44...OK

\>\>\> Checking BUILD File Entries:

PCE V1.0 ...Ok - in Package File

\>\>\> Environment is Ok

Use INSTALL NAME: AUTOMATED INFO COLLECTION SYS 3.0 to install this Distribution

.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: VERify Checksums in Transport Global

Select INSTALL NAME: AUTOMATED INFO COLLECTION SYS 3.0 Loaded from Distribution 4/24/97@12:58:24

=\> AICS V3.0 RELEASE 4/24/97 ;Created on Apr 24, 1997@11:24:33

DEVICE: HOME// \<RET\> LAT

PACKAGE: AUTOMATED INFO COLLECTION SYS 3.0 Apr 24, 1997 1:00 pm PAGE 1

------------------------------------------------------------------------------

213 Routine checked, 0 failed.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: Backup a Transport Global

Select INSTALL NAME: AUTOMATED INFO COLLECTION SYS 3.0 Loaded from Distribution 4/24/97@12:58:24

=\> AICS V3.0 RELEASE 4/24/97 ;Created on Apr 24, 1997@11:24:33

This Distribution was loaded on Apr 24, 1997@12:58:24 with header of

AICS V3.0 RELEASE 4/24/97 ;Created on Apr 24, 1997@11:24:33

It consisted of the following Install(s):

AUTOMATED INFO COLLECTION SYS 3.0

Subject: BACKUP AICS3_0 INSTALL

Loading Routines for AUTOMATED INFO COLLECTION SYS 3.0........

Routine IBD3KPT is not on the disk.................................

Routine IBDF18E0 is not on the disk...

Routine IBDF18E2 is not on the disk..

Routine IBDF18E3 is not on the disk.............................................

...........

Routine IBDFBKS is not on the disk..

Routine IBDFBKS1 is not on the disk..

Routine IBDFBKS2 is not on the disk..

Routine IBDFBKS3 is not on the disk..

Routine IBDFBKS4 is not on the disk...........

Routine IBDFCMP is not on the disk..

Routine IBDFCMP1 is not on the disk......

Routine IBDFDE10 is not on the disk.......

Routine IBDFDE41 is not on the disk..

Routine IBDFDE42 is not on the disk...........

Routine IBDFFRFT is not on the disk......

Routine IBDFFT3 is not on the disk..

Routine IBDFFT4 is not on the disk..............

Routine IBDFN11 is not on the disk..................

Routine IBDFOSG9 is not on the disk.......................

Routine IBDFST1 is not on the disk..................................

Send mail to:Yourself,You Last used MailMan: 13 Jun 96 08:56

Select basket to send to: IN// \<RET\>

And send to: \<RET\>

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: INStall Package(s)

Select INSTALL NAME: AUTOMATED INFO COLLECTION SYS 3.0

Loaded from Distribution 4/24/97@12:58:24

=\> AICS V3.0 RELEASE 4/24/97 ;Created on Apr 24, 1997@11:24:33

This Distribution was loaded on Apr 24, 1997@12:58:24 with header of

AICS V3.0 RELEASE 4/24/97 ;Created on Apr 24, 1997@11:24:33

It consisted of the following Install(s):

AUTOMATED INFO COLLECTION SYS 3.0

AUTOMATED INFO COLLECTION SYS 3.0

Will first run the Environment Check Routine, IBD3KENV

AICS 3.0 Installation Requirements:

\>\>\> Checking Environment:

Environment checks OK

\>\>\> Checking PACKAGE File Entries:

Checking for required patch XU\*8.0\*2...OK

Checking for required patch XU\*8.0\*15...OK

Checking for required patch XU\*8.0\*16...OK

Checking for required patch XU\*8.0\*28...OK

Checking for required patch XU\*8.0\*32...OK

Checking for required patch XU\*8.0\*44...OK

\>\>\> Checking BUILD File Entries:

PCE V1.0 ...Ok - in Package File

\>\>\> Environment is Ok

Install Questions for AUTOMATED INFO COLLECTION SYS 3.0

Incoming Files:

357 ENCOUNTER FORM

> **NOTE:** You already have the 'ENCOUNTER FORM' File.

357.08 AICS PURGE LOG

> **NOTE:** You already have the 'AICS PURGE LOG' File.

357.09 ENCOUNTER FORM PARAMETERS

> **NOTE:** You already have the 'ENCOUNTER FORM PARAMETERS' File.

357.1 ENCOUNTER FORM BLOCK

> **NOTE:** You already have the 'ENCOUNTER FORM BLOCK' File.

357.2 SELECTION LIST

> **NOTE:** You already have the 'SELECTION LIST' File.

357.3 SELECTION

> **NOTE:** You already have the 'SELECTION' File.

357.4 SELECTION GROUP

> **NOTE:** You already have the 'SELECTION GROUP' File.

357.5 DATA FIELD

> **NOTE:** You already have the 'DATA FIELD' File.

357.6 PACKAGE INTERFACE (including data)

> **NOTE:** You already have the 'PACKAGE INTERFACE' File.

I will OVERWRITE your data with mine.

357.69 TYPE OF VISIT (including data)

> **NOTE:** You already have the 'TYPE OF VISIT' File.

I will MERGE your data with mine.

357.7 FORM LINE

> **NOTE:** You already have the 'FORM LINE' File.

357.8 TEXT AREA

> **NOTE:** You already have the 'TEXT AREA' File.

357.91 MARKING AREA TYPE (including data)

> **NOTE:** You already have the 'MARKING AREA TYPE' File.

I will OVERWRITE your data with mine.

357.92 PRINT CONDITIONS (including data)

> **NOTE:** You already have the 'PRINT CONDITIONS' File.

I will OVERWRITE your data with mine.

357.93 MULTIPLE CHOICE FIELD

> **NOTE:** You already have the 'MULTIPLE CHOICE FIELD' File.

357.94 ENCOUNTER FORM PRINTERS

> **NOTE:** You already have the 'ENCOUNTER FORM PRINTERS' File.

357.95 FORM DEFINITION

> **NOTE:** You already have the 'FORM DEFINITION' File.

357.96 ENCOUNTER FORM TRACKING

> **NOTE:** You already have the 'ENCOUNTER FORM TRACKING' File.

357.97 ENCOUNTER FORM COUNTERS

\*BUT YOU ALREADY HAVE 'ENCOUNTER FORM COUNTER FILE' AS FILE \#357.97!

Shall I write over your ENCOUNTER FORM COUNTER FILE File? YES// Y

357.98 AICS DATA QUALIFIERS (including data)

\*BUT YOU ALREADY HAVE 'ENCOUNTER FORM DATA QUALIFIERS' AS FILE \#357.98!

Shall I write over your ENCOUNTER FORM DATA QUALIFIERS File? YES// Y

I will MERGE your data with mine.

357.99 PRINT MANAGER CLINIC GROUPS

> **NOTE:** You already have the 'PRINT MANAGER CLINIC GROUPS' File.

358 IMP/EXP ENCOUNTER FORM (including data)

> **NOTE:** You already have the 'IMP/EXP ENCOUNTER FORM' File.

I will OVERWRITE your data with mine.

358.1 IMP/EXP ENCOUNTER FORM BLOCK (including data)

> **NOTE:** You already have the 'IMP/EXP ENCOUNTER FORM BLOCK' File.

I will OVERWRITE your data with mine.

358.2 IMP/EXP SELECTION LIST (including data)

> **NOTE:** You already have the 'IMP/EXP SELECTION LIST' File.

I will OVERWRITE your data with mine.

358.3 IMP/EXP SELECTION (including data)

> **NOTE:** You already have the 'IMP/EXP SELECTION' File.

I will OVERWRITE your data with mine.

358.4 IMP/EXP SELECTION GROUP (including data)

> **NOTE:** You already have the 'IMP/EXP SELECTION GROUP' File.

I will OVERWRITE your data with mine.

358.5 IMP/EXP DATA FIELD (including data)

> **NOTE:** You already have the 'IMP/EXP DATA FIELD' File.

I will OVERWRITE your data with mine.

358.6 IMP/EXP PACKAGE INTERFACE (including data)

> **NOTE:** You already have the 'IMP/EXP PACKAGE INTERFACE' File.

I will OVERWRITE your data with mine.

358.7 IMP/EXP FORM LINE (including data)

> **NOTE:** You already have the 'IMP/EXP FORM LINE' File.

I will OVERWRITE your data with mine.

358.8 IMP/EXP TEXT AREA (including data)

> **NOTE:** You already have the 'IMP/EXP TEXT AREA' File.

358.91 IMP/EXP MARKING AREA (including data)

> **NOTE:** You already have the 'IMP/EXP MARKING AREA' File.

I will OVERWRITE your data with mine.

358.93 IMP/EXP MULTIPLE CHOICE FIELD (including data)

> **NOTE:** You already have the 'IMP/EXP MULTIPLE CHOICE FIELD' File.

I will OVERWRITE your data with mine.

358.94 IMP/EXP HAND PRINT FIELD (including data)

> **NOTE:** You already have the 'IMP/EXP HAND PRINT FIELD' File.

I will OVERWRITE your data with mine.

358.98 IMP/EXP AICS DATA QUALIFIERS (including data)

> **NOTE:** You already have the 'IMP/EXP AICS DATA QUALIFIERS' File.

I will OVERWRITE your data with mine.

358.99 IMP/EXP AICS DATA ELEMENTS (including data)

> **NOTE:** You already have the 'IMP/EXP AICS DATA ELEMENTS' File.

I will OVERWRITE your data with mine.

359 CONVERTED FORMS

> **NOTE:** You already have the 'CONVERTED FORMS' File.

359.1 AICS DATA ELEMENTS (including data)

> **NOTE:** You already have the 'AICS DATA ELEMENTS' File.

I will OVERWRITE your data with mine.

359.2 FORM SPECS

> **NOTE:** You already have the 'FORM SPECS' File.

359.3 AICS ERROR AND WARNING LOG

359.94 HAND PRINT FIELD

> **NOTE:** You already have the 'HAND PRINT FIELD' File.

409.95 PRINT MANAGER CLINIC SETUP

> **NOTE:** You already have the 'PRINT MANAGER CLINIC SETUP' File.

409.96 PRINT MANAGER DIVISION SETUP

> **NOTE:** You already have the 'PRINT MANAGER DIVISION SETUP' File.

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// \<RET\>

Enter options you wish to mark as 'Out Of Order': IBD\*

Enter options you wish to mark as 'Out Of Order': \<RET\>

Enter protocols you wish to mark as 'Out Of Order': IBD\*

Enter protocols you wish to mark as 'Out Of Order': \<RET\>

Delay Install (Minutes): (0-60): 0// \<RET\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<RET\> LAT

Install Started for AUTOMATED INFO COLLECTION SYS 3.0 :

Apr 24, 1997@13:05:39

Installing Routines:

Apr 24, 1997@13:06:46

Running Pre-Install Routine: ^IBDE2

Installing Data Dictionaries:

Apr 24, 1997@13:07:59

Installing Data:

Apr 24, 1997@13:08:18

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing PRINT TEMPLATE

Installing SORT TEMPLATE

Installing INPUT TEMPLATE

Installing DIALOG

Installing PROTOCOL

Installing REMOTE PROCEDURE

Installing LIST TEMPLATE

Installing OPTION

Apr 24, 1997@13:09:25

Running Post-Install Routine: ^IBD3KPT

\>\>\> Now Attempting to automatically update Tool Kit forms and Tool Kit Blocks.

Moving Block 'EYE ART I V3.0' from import/export to Tool Kit

Moving Block 'EYE ART II V3.0' from import/export to Tool Kit

Moving Block 'HIDDEN CLASSIFICATIONS (V3.0)' from import/export to Tool Kit

Moving Block 'PATIENT IMMUNIZATIONS (V3.0)' from import/export to Tool Kit

Moving Block 'PRACTITIONER(V3.0)' from import/export to Tool Kit

\>\>\> Tool Kit Forms sent (4): 0 installed

\>\>\> Tool Kit Blocks sent (28): 5 installed

\>\>\> AICS Data Dictionaries updated to use Clinical Lexicon Utility version 1.0

\>\>\> Form Specs being deleted and recreated for scanning.

\>\>\> Deleting Fields \*'d for Deletion in Package Interface file (357.6)

Updating Routine file...

The following Routines were created during this install:

IBDX0

IBDX01

IBDX02

IBDX03

IBDX04

IBDX1

IBDX11

IBDX110

IBDX12

IBDX13

IBDX14

IBDX15

IBDX16

IBDX17

IBDX18

IBDX19

IBDX2

IBDX21

IBDX22

IBDX23

IBDX24

IBDX25

IBDX26

IBDX3

IBDX31

IBDX32

IBDX33

IBDX34

IBDX4

IBDX41

IBDX42

IBDX5

IBDX51

IBDX52

IBDX53

IBDX54

IBDX95

IBDX951

IBDX9510

IBDX9511

IBDX9512

IBDX952

IBDX953

IBDX954

IBDX955

IBDX956

IBDX957

IBDX958

IBDX959

IBDXI5

IBDXI51

IBDXI52

IBDXI53

IBDXI2

IBDXI21

IBDXI22

IBDXI23

IBDXI24

IBDXI25

IBDXI26

IBDXI93

IBDXI931

IBDXI932

IBDXI933

IBDX96

IBDX961

IBDX97

Updating KIDS files...

AUTOMATED INFO COLLECTION SYS 3.0 Installed.

Apr 24, 1997@13:09:57

Install Message sent \#61805

------------------------------------------------------------------------------

+------------------------------------------------------------------+

100% \| 25 50 75 \|

Complete +------------------------------------------------------------------+

Install Completed

Load a Distribution

Verify Checksums in Transport Global

Print Transport Global

Compare Transport Global to Current System

Backup a Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: \<RET\>

Do you really want to halt? YES// \<RET\>  

VI\. Appendix C - Checksum Values

> The following are CHECK^XTSUMBLD Checksum values for AICS V. 3.0.

> IBD3KENV value = 2482893

> IBD3KPT value = 11964813

> IBD3KPT1 value = 561736

> IBDF10 value = 11871257

> IBDF10A value = 14844945

> IBDF10B value = 4334206

> IBDF10C value = 7145394

> IBDF11 value = 3746255

> IBDF11A value = 3372216

> IBDF12 value = 2449474

> IBDF13 value = 6065810

> IBDF14 value = 2806524

> IBDF14A value = 8128142

> IBDF15 value = 2835740

> IBDF15A value = 9106437

> IBDF16 value = 8212382

> IBDF17 value = 7062222

> IBDF18 value = 5760005

> IBDF18A value = 3427205

> IBDF18A1 value = 8968373

> IBDF18B value = 1183119

> IBDF18C value = 9383133

> IBDF18D value = 2224052

> IBDF18E value = 11340277

> IBDF18E0 value = 11693827

> IBDF18E1 value = 10375249

> IBDF18E2 value = 4914156

> IBDF18E3 value = 554180

> IBDF19 value = 7787654

> IBDF1A value = 6906704

> IBDF1B value = 13886733

> IBDF1B1 value = 11709608

> IBDF1B1A value = 12963462

> IBDF1B1B value = 1767481

> IBDF1B2 value = 2289984

> IBDF1B3 value = 7853311

> IBDF1B5 value = 11098411

> IBDF1BA value = 11321310

> IBDF1C value = 4183587

> IBDF2A value = 13089889

> IBDF2A1 value = 16675892

> IBDF2A2 value = 5398601

> IBDF2B value = 7733441

> IBDF2B1 value = 2426473

> IBDF2D value = 11307498

> IBDF2D1 value = 7091947

> IBDF2D2 value = 20452649

> IBDF2D3 value = 12284133

> IBDF2E value = 1625292

> IBDF2F value = 14953767

> IBDF2F1 value = 6492541

> IBDF2G value = 1305076

> IBDF2H value = 1131607

> IBDF3 value = 7478886

> IBDF4 value = 18681956

> IBDF4A value = 13810939

> IBDF5 value = 9209729

> IBDF5A value = 4140889

> IBDF5B value = 6698423

> IBDF5C value = 3822764

> IBDF5D value = 5086357

> IBDF6 value = 8604587

> IBDF6A value = 6144443

> IBDF6C value = 1009133

> IBDF7 value = 2565275

> IBDF8 value = 1630744

> IBDF9 value = 3819084

> IBDF9A value = 16913688

> IBDF9A1 value = 7479813

> IBDF9A3 value = 7052911

> IBDF9B value = 11180213

> IBDF9B1 value = 13740809

> IBDF9B2 value = 6322343

> IBDF9B3 value = 5177091

> IBDF9B4 value = 6134853

> IBDF9C value = 5406188

> IBDF9D value = 5163363

> IBDF9E value = 5934543

> IBDFBK1 value = 4906853

> IBDFBK2 value = 6362708

> IBDFBK3 value = 16698204

> IBDFBKR value = 7402561

> IBDFBKS value = 15247370

> IBDFBKS1 value = 5830972

> IBDFBKS2 value = 14974345

> IBDFBKS3 value = 12904114

> IBDFBKS4 value = 8554663

> IBDFC value = 11407114

> IBDFC1 value = 4784941

> IBDFC2 value = 8753867

> IBDFC2A value = 8223304

> IBDFC2B value = 13124658

> IBDFC3 value = 3078465

> IBDFC4 value = 60053

> IBDFCG value = 16657494

> IBDFCG1 value = 6651180

> IBDFCMP value = 10284232

> IBDFCMP1 value = 12808450

> IBDFCNOF value = 9651795

> IBDFDE value = 28292527

> IBDFDE0 value = 11338817

> IBDFDE1 value = 13698331

> IBDFDE10 value = 424026

> IBDFDE2 value = 20881171

> IBDFDE21 value = 20139881

> IBDFDE22 value = 5338516

> IBDFDE3 value = 18089819

> IBDFDE4 value = 11204271

> IBDFDE41 value = 6974404

> IBDFDE42 value = 2472593

> IBDFDE5 value = 20092356

> IBDFDE6 value = 20813168

> IBDFDE61 value = 2306021

> IBDFDE7 value = 13809118

> IBDFDE8 value = 7762272

> IBDFDE9 value = 7383712

> IBDFDEA value = 11764220

> IBDFDVE value = 392266

> IBDFESP value = 5681865

> IBDFFRFT value = 5605728

> IBDFFSMP value = 4992963

> IBDFFT value = 19343496

> IBDFFT1 value = 38001031

> IBDFFT2 value = 3352777

> IBDFFT3 value = 19870534

> IBDFFT4 value = 4158691

> IBDFFV value = 7432713

> IBDFFV1 value = 2385105

> IBDFFV2 value = 4347225

> IBDFFV3 value = 5257927

> IBDFGRP value = 9136849

> IBDFHLP value = 3402730

> IBDFLST value = 11634433

> IBDFLST1 value = 1683695

> IBDFM1 value = 13441067

> IBDFN value = 15680196

> IBDFN1 value = 1213860

> IBDFN10 value = 2765146

> IBDFN11 value = 2856878

> IBDFN12 value = 1612905

> IBDFN13 value = 66244

> IBDFN14 value = 2226507

> IBDFN2 value = 8020032

> IBDFN3 value = 2845147

> IBDFN4 value = 2973307

> IBDFN5 value = 3054776

> IBDFN6 value = 2853724

> IBDFN7 value = 1460739

> IBDFN8 value = 124808

> IBDFN9 value = 194363

> IBDFOSG value = 10173582

> IBDFOSG1 value = 7086168

> IBDFOSG2 value = 13313314

> IBDFOSG3 value = 7158757

> IBDFOSG4 value = 3710643

> IBDFPCE value = 2696567

> IBDFPE value = 12450329

> IBDFPE1 value = 8310152

> IBDFPRG value = 7553882

> IBDFPRG1 value = 2560350

> IBDFQB value = 12597674

> IBDFQEA value = 11843748

> IBDFQEA1 value = 44681

> IBDFQS value = 1334094

> IBDFQSL value = 3215307

> IBDFQSL1 value = 7683177

> IBDFQSL2 value = 5616996

> IBDFREG value = 5649578

> IBDFRPC value = 8402302

> IBDFRPC1 value = 3939573

> IBDFRPC2 value = 13348413

> IBDFRPC3 value = 5251659

> IBDFRPC4 value = 5575808

> IBDFSS value = 16958149

> IBDFSS1 value = 2595117

> IBDFST value = 11142778

> IBDFST1 value = 11299943

> IBDFU value = 15610352

> IBDFU1 value = 12896586

> IBDFU10 value = 522009

> IBDFU1A value = 1409234

> IBDFU1B value = 5339731

> IBDFU1C value = 6702058

> IBDFU2 value = 11675915

> IBDFU2A value = 14139503

> IBDFU2B value = 14408614

> IBDFU2C value = 9269483

> IBDFU3 value = 5569853

> IBDFU4 value = 3631011

> IBDFU5 value = 8489458

> IBDFU5A value = 3373891

> IBDFU6 value = 331661

> IBDFU7 value = 665770

> IBDFU8 value = 6550892

> IBDFU9 value = 2718995

> IBDFU91 value = 1874757

> IBDFUA value = 3285590

> IBDFUTI value = 3380251

> IBDFUTL value = 11719221

> IBDFUTL1 value = 21879277

> IBDFUTL2 value = 11033351

> IBDFUTL3 value = 3224598

> IBDNTEG value = 4174439

> IBDNTEG0 value = 3274825

> IBDNTEG1 value = 2444

> IBDNTEG2 value = 2452

> IBDPPRE value = 2504995

> IBDPPT value = 292463

> IBDY217 value = 1013587

VII\. Appendix D - Scanner Calibration

Paper Keyboard is the proprietary software that was chosen to interface the AICS workstation with a scanner. Many different types of scanners may be used, and as a result of the differences between them, it may be necessary to calibrate your scanner with Paper Keyboard. Calibration should only be necessary under the following circumstances.

- 
- 
- 
- 

Initial scanner hook-up on a workstation.Scanner is replaced at a workstation.Sheet feed mechanism is added or removed from the scanner.Paper Keyboard continually cannot recognize anchors on your form, forcing you to manually locate them.

In order to calibrate Paper Keyboard with your scanner, it is necessary to understand the components on a form that make it scannable. They are:

- 
- 
- 

Anchor Marks: used to align the form,Scannable Page Block: used to determine if the page is scannable,Form, ID and Page Numbers: used to recognize the form being read.

![](aics-version-3-installation-guide/015.png)

During scanning, a Form Specification file is loaded that tells Paper Keyboard where to look for the anchors and scannable page block on a form. Paper Keyboard will attempt to locate these items in order to align the form before recognizing the data on the form. Sometimes, due to variations in scanners and/or shrinkage of forms, Paper Keyboard will not be able to locate these items. Calibrating Paper Keyboard with your scanner upon initial setup should prevent this from occurring. To calibrate the scanner, you should follow these steps:

1.  
- 
- 
- 
- 
2.  
3.  
4.  
5.  
6.  
7.  
- 
- 
8.  

Select a form to calibrate from.Use a form that has actual printed patient data.Do not use a form that does not have a FORM or ID number located on the top of the form.If you are using a Bell & Howell scanner on this workstation, AND you will be using the duplex feature (reading both sides at once), select a form that has been printed duplex with a short-edge binding (form is printed head to toe on both sides of the paper.)You do NOT need to calibrate for each different form you have. You are simply selecting a form to use as a guide.Start up the AICS software.Highlight the key located in the upper left-hand corner of the AICS window. This will result in a sign-on to V*IST*A. It is necessary to be signed-on to V*IST*A to calibrate your forms, since any file specifications not already resident on the workstation will automatically be retrieved from V*IST*A during the calibration process.Select the Options menu from the menu bar located at the top of the screen.From the Options menu, select Preferences.From the Preferences screen, select the Advanced button located at the lower right hand corner of the window.You are now in the AICS Advanced Preferences window. You MUST calibrate your scanner twice. The first time through, you will calibrate for a normal page orientation, and the second time through you will calibrate for a rotated page orientation. This will allow Paper Keyboard to read your form whether it is fed in right-side-up or up-side-down. Select the page orientation you wish to calibrate for by pressing the appropriate button:Calibrate Normal Scanner Settings, orCalibrate Rotated Scanner Settings.  
You are now prompted to be sure the paper is in the scanner. To determine which way your paper should be facing, see the following chart.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>Normal Calibration</strong></th>
<th><p><strong>Rotated</strong></p>
<p><strong>Calibration</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Hewlett Packard</td>
<td>Front side of EF facing up and positioned upright in the scanner</td>
<td>Back side of EF facing up and positioned upside down in the scanner</td>
</tr>
<tr class="even">
<td>Bell &amp; Howell</td>
<td>Front side of EF facing up and positioned upright in the scanner</td>
<td>Front side of duplexed short-edge binding EF facing up and positioned upright in the scanner</td>
</tr>
</tbody>
</table>

9.  

> The Scanner Settings dialogue box should be displayed on your screen. For the time being, we will simply close this window.Click the Cancel button located at the bottom of the window.

10. 

The form image should be visible on your screen. You may maximize the window for ease of viewing.

11. 

To determine whether you need to turn off duplexing, refer to the following chart. If you do not need to turn duplexing off, proceed to the next step.

|                 | Normal Calibration | Rotated Calibration   |
|-----------------|------------------------|---------------------------|
| Hewlett Packard | Not applicable         | Not applicable            |
| Bell & Howell   | Turn off duplexing     | Do NOT turn off duplexing |

> To turn off duplexing if applicable:

- 
- 
- 
- 

Select the Edit menu from the menu bar;Choose Scanner Settings from the pop-up menu;If the Double Sided box is checked, you must click on it to turn it off;You MUST remember to turn this back on before you save your configuration. You will be alerted to turn this feature back on in a later step.

12. 
- 
- 
13. 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

If you are using a Bell and Howell scanner and you are calibrating for a rotated page orientation, you will need to click the scan button to retrieve the image of the second page.  
Click the button on the left hand side of the screen that looks like a scanner.Once the image is loaded, you will be looking at the back side of your form.What to look for on the image.On this first pass, you are working with a Master Form Specification. This file only knows about a few items on your form. They are:Anchors,Form \#,ID \#,Checksums,Page \#,Scannable page block.Be sure that you can see each of these items clearly. If they are too dark (ink appears blotted), or too light (image appears to fade out), you may need to adjust your scanner brightness. To do so:Click Edit on the menu bar,Select Scanner Settings from the pop-up window,Alter the brightness setting by dragging the center block in either direction,Click OK to accept new settings,Click on the box that looks like a scanner, located on the left side of the Paper Keyboard screen. Be sure you put the paper back into the sheet feeder of your scanner the same way you did in Step 8.Check your brightness again. If you are not satisfied, you should repeat this step until your brightness settings are acceptable.Surrounding each of the first 5 items, you should see a red box. This is the location that Paper Keyboard is looking for for these items. On the last item (Scannable page block), you should see a red square within the black block on the form.Within the boxes that surround your page anchors, you should see a red cross-hair. This cross-hair should be positioned on top of your anchors.

14. 
1)  
- 
- 
- 

> How to calibrate the Master Form Spec.Start by looking at the top-left anchor. Paper Keyboard must be able to find this anchor to position itself from when locating the remaining items on a form. If the anchor is not completely within the red box, and/or the red cross hair does not locate the anchor, you should adjust your offset units. Vertical offset units are adjusted when the image scanned too high or too low. Horizontal offset units are adjusted when the image scanned too far to the left or right. To change the offset units:  
> Click on the Edit menu located at the top of the Paper Keyboard window,Select Scanner Settings from the pop up window,Modify either the vertical or horizontal offset units:

|                 | Vertical Offset Units | Horizontal Offset Units |
|-----------------|---------------------------|-----------------------------|
| Positive Number | Moves red squares ↓       | Moves red squares →         |
| Negative Number | Moves red squares ↑       | Moves red squares ←         |

- 
- 
2)  
- 
- 
- 
3)  
- 
- 
- 

Only modify one number at a time,Look again at the top-left anchor. If changes are still required, go back to the beginning of this step.Once you are satisfied with the positioning of your top left anchor, you will need to look at the Form and ID numbers:The red boxes should completely surround each number with sufficient room at the end of the numbers for growth.If the boxes are not positioned sufficiently, you will need to adjust your offset units as you did in Step 14a.Each time you modify a value, you will need to go back to the beginning of Step 14 and proceed from there. This will allow you to be sure the changes have not had negative affects on prior steps.You should now look at the checksum number located in the top-middle portion of the page, as well as the page number and the top-right anchor. If the red boxes do not surround these items, you will need to adjust the calibrated scale. Vertical calibrated scales are adjusted when the length of the image is too short or long. Horizontal calibrated scales are adjusted when the width of the image is too fat or thin. To change the calibrated scales:Click on the Edit menu located at the top of the Paper Keyboard window,Select Scanner Settings from the pop up window,Modify either the vertical or horizontal calibrated scales as follows.

|                 | Vertical Calibrated Scale | Horizontal Calibrated Scale |
|-----------------|-------------------------------|---------------------------------|
| Positive Number | Stretches red image ↓         | Stretches red image →           |
| Negative Number | Shrinks red image ↑           | Shrinks red image ←             |

- 
- 

> Only modify one number at a time.Each time you modify a value, you will need to go back to the beginning of Step 14 and proceed from there. This will allow you to be sure the changes have not had negative affects on prior steps.

4)  
- 
- 
- 

You should now look at the anchors on the bottom of your form as well as the scannable page block. If your anchors are not found, or a red square does not fall inside the scannable page block, you will need to adjust your calibrated scale. Vertical calibrated scales are adjusted when the length of the image is too short or long. Horizontal calibrated scales are adjusted when the width of the image is too fat or thin. To change the calibrated scales:Click on the Edit menu located at the top of the Paper Keyboard window,Select Scanner Settings from the pop up window,Modify either the vertical or horizontal calibrated scales as follows.

|                 | Vertical Calibrated Scale | Horizontal Calibrated Scale |
|-----------------|-------------------------------|---------------------------------|
| Positive Number | Stretches red image ↓         | Stretches red image →           |
| Negative Number | Shrinks red image ↑           | Shrinks red image ←             |

- 
- 

Only modify one number at a time.Each time you modify a value, you will need to go back to the beginning of Step 14 and proceed from there. This will allow you to be sure the changes have not had negative affects on prior steps.

15. 
- 
- 
- 
- 
- 

> How to switch form specification files.We’re not done yet! So far, Paper Keyboard has only looked at the key items on our form. We must now allow it to see our bubbles to determine if we calibrated right!To look at the bubbles involves several steps. First we must close down the Master Form Specification file, and then we must open the Form Specification file that is specific to the form we have chosen to use. Fortunately, Paper Keyboard will do this automatically by recognizing the fields we have just allowed it to find. To do so:Click on the R button that is located on the left hand side of the Paper Keyboard screen,  
> After a few seconds, Paper Keyboard will close the Master Form Specification file and will automatically open form specific Form Specification file. You can tell that this has happened by viewing the name in the top blue bar on the Paper Keyboard screen. It will no longer say AICS Master Form Spec, but should instead say Encounter Form \#, where \# is from your form.In some instances, instead of opening the new FORM SPEC file, you will be prompted to validate some information, such as Page \#, Form \# or ID \#. This means that Paper Keyboard did not find these values where it expected to find them, or it was not confident with what it read in these fields (possibly due to a brightness issue.) If this is the case, you should:

- 
- 
- 

Click Cancel on the field value dialogue box,Click Discard when prompted with a warning,Return to Step 14 and begin the calibration process again.

16. 
1)  
- 
- 

> Checking the bubbles.Now that we are working with a new FORM SPECIFICATION file, we will need to scan the form in again. Take the same form and place it back on the scanner in the SAME position that you originally placed it in.Click on the button that looks like a scanner. It is located on the left hand side of the Paper Keyboard screen. This will feed the form through the scanner again.If you are using a Bell & Howell, and you are calibrating for a rotated page orientation, you will need to click on the scan button a second time. (You do not need to put the paper back in the scanner to do this.) This will replace the image of the front page with the image of the back page.

2)  
- 
- 
- 
- 
- 
- 
- 
- 

To see the bubbles, we must now recognize the image.Click on the R button located on the left hand side of the Paper Keyboard screen. Within a few seconds, you should see your image, with red boxes surrounding each of your bubbles.Move the field value dialogue box out of viewing range by dragging and dropping the box out of the way.You need to make sure that the red boxes surround the bubbles on top as well as those further down on your page. If you don’t feel that Paper Keyboard is locating the bubbles sufficiently, you will need to adjust your calibrated scale.Move the field value dialogue box back into view, and click on the cancel button. Discard the data when prompted to do so.Click on the Edit menu located at the top of the Paper Keyboard window.  
Select Scanner Settings from the pop up window.Modify either the vertical or horizontal calibrated scales.

|                 | Vertical Calibrated Scale | Horizontal Calibrated Scale |
|-----------------|-------------------------------|---------------------------------|
| Positive Number | Stretches red image ↓         | Stretches red image →           |
| Negative Number | Shrinks red image ↑           | Shrinks red image ←             |

- 
- 

> Only modify one number at a time.Each time you modify a value, you will need to go back to the beginning of Step 14 and proceed from there. This will allow you to be sure the changes have not had negative affects on prior steps.

17. 

To determine whether you need to turn duplexing back on, refer to the following chart. If you do not need to turn duplexing back on, proceed to the next step.

|                 | Normal Calibration | Rotated Calibration     |
|-----------------|------------------------|-----------------------------|
| Hewlett Packard | Not applicable         | Not applicable              |
| Bell & Howell   | Turn duplexing back on | Verify that duplexing is on |

- 
- 
- 
- 
18. 
- 
- 
19. 
- 
- 
- 
1.  
- 
2.  
3.  
- 
- 

To turn duplexing back on if applicable:Select the Edit menu from the menu bar,Choose Scanner Settings from the pop-up menu,If the Double Sided box is not checked, you must click on it to turn it on.Before saving your settings, you must discard the image. To do so, bring the Field Value dialog box back into view.Click on the Cancel button.Click Discard to get rid of the image.  
Leaving Paper Keyboard.Do NOT shut (X) or minimize (-) Paper Keyboard. Shutting Paper Keyboard will result in a loss of all the calibration settings you just entered, as well as prohibiting any future work from within the AICS Scanning Workstation. Minimizing Paper Keyboard will result in oddities during the scanning process.If you have maximized Paper Keyboard, you should choose the cascaded tile button located in the upper right hand corner of the screen. This will restore Paper Keyboard to its original size.Use Alt-Tab to bring the AICS Workstation screen to the foreground.Save your settings.Select the SAVE SCANNER SETTINGS button.Don’t forget that you have to calibrate twice! Once for a normal page orientation, and once for a rotated orientation. If you want to calibrate again, return to Step 7.To end the calibration process:Select the CLOSE button to return to the Preferences screen,From the Preferences screen, select the OK button.

You are now in the AUTOMATED INFORMATION COLLECTION SYSTEM screen.