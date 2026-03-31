---
title: Kernel Toolkit 7.3 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 7.3
patch_id: XU*7.3
group_key: "XU:XU:7.3"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this guide is to provide instructions for installing Kernel Toolkit (also referred to as "Toolkit") Version 7.3.
audience: 
keywords: 
  - filed
  - strong
  - table
  - xtini
  - taskman
  - routine
  - routines
  - contents
  - blockquote
  - manager
page_count: 0
word_count: 10793
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/ktk_7_3ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/ktk_7_3ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

## Table of Contents

  - [Introduction](#introduction)
    - [New Globals](#new-globals)
  - [Installing Toolkit V. 7.3](#installing-toolkit-v-73)
    - [Preliminary Considerations](#preliminary-considerations)
    - [Advance Preparation](#advance-preparation)
    - [VAX/ALPHA Installations](#vaxalpha-installations)
    - [MSM-PC Installations](#msm-pc-installations)
    - [Begin the Installation](#begin-the-installation)
    - [Read the Routines into Production](#read-the-routines-into-production)
    - [Move Routines to the Manager Account](#move-routines-to-the-manager-account)
    - [Run the Manager Setup Routine](#run-the-manager-setup-routine)
    - [Review Global Protection for ^%ZRTL](#review-global-protection-for-zrtl)
    - [Establish Global Translation](#establish-global-translation)
    - [Do the First Part of the Installation](#do-the-first-part-of-the-installation)
    - [Example of an Init done at the San Francisco ISC](#example-of-an-init-done-at-the-san-francisco-isc)
    - [Shutdown DSM and Restart to Activate Mapped Sets](#shutdown-dsm-and-restart-to-activate-mapped-sets)
    - [On the Other Toolkit V. 7.2 CPUs (MSM and M/SQL)](#on-the-other-toolkit-v-72-cpus-msm-and-msql)
    - [Delete Inits](#delete-inits)
    - [Clear Obsolete Routines](#clear-obsolete-routines)
    - [Clear Unused Routines from the Production Account](#clear-unused-routines-from-the-production-account)
    - [Install the VAX/ALPHA VMS EDT or TPU Text Editor (Optional)](#install-the-vaxalpha-vms-edt-or-tpu-text-editor-optional)
    - [Install the Kermit Protocol (Optional)](#install-the-kermit-protocol-optional)
    - [Bulletins Exported with Toolkit V. 7.3 (Not Associated with Mail Groups)](#bulletins-exported-with-toolkit-v-73-not-associated-with-mail-groups)
  - [## Index](#index)
Decentralized Hospital Computer Program
KERNEL TOOLKITINSTALLATION GUIDE
April 1995
Information Systems Center
San Francisco, California
Table of Contents
Introduction
New Globals
Installing Toolkit V. 7.3
Preliminary Considerations
MSM Sites
Advance Preparation
VAX/ALPHA Installations
Sample Dialogue of Running ^XUCMTM
MSM-PC Installations
Begin the Installation
Read the Routines into Production
Move Routines to the Manager Account
Run the Manager Setup Routine
Review Global Protection for ^%ZRTL
Establish Global Translation
Do the First Part of the Installation
Example of an Init done at the San Francisco ISC
Installing/Configuring the VAX/Alpha Performance Monitor (VPM)
Installing/Configuring the MSM Performance Monitor (MPM)
Shutdown DSM and Restart to Activate Mapped Sets
On the Other Toolkit V. 7.2 CPUs (MSM and M/SQL)
Steps that can be taken while inits run on the first CPU
After the inits have finished (VAX/Alpha)
Delete Inits
Clear Obsolete Routines
Clear Unused Routines from the Production Account
Install the VAX/ALPHA VMS EDT or TPU Text Editor (Optional)
Install the Kermit Protocol (Optional)
Bulletins Exported with Toolkit V. 7.3 (Not Associated with Mail Groups)
Index

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing Kernel Toolkit (also referred to as "Toolkit") Version 7.3.

The following minimum software versions are required to install this package:

> Kernel V. 7.1

> VA FileMan V. 20.0

> MailMan V. 7.0

> DSM for OpenVMS V. 6.2

> MSM-PC V.4.0.n

Instructions are provided for three operating systems (OS):

> DSM for OpenVMS

> MSM-PC V.4.0.n

> M/SQL

Toolkit Version 7.3 also supports MSM-UNIX and DataTree MUMPS (Massachusetts General Hospital Utility Multi-Programming System).

The installation steps provided in this guide apply to all the supported operating systems. (Global protection does not apply for DataTree systems.)

> **NOTE:** • for M11+, operating system version 3.6 or above is required

• for M/VX, version 5B or above is required (the Kernel Toolkit init will not run if previous OS versions are present).

When using this manual, it is recommended that you highlight the commands corresponding to your operating system for easy summary viewing (e.g., highlight the box labeled DSM for OpenVMS, MSM, etc.). Also note that in these instructions, "VAH" refers to the Production account and "MGR" refers to the Library or Manager account. You may use different names at your site and should pencil them in to avoid confusion later on. Also note that for M/SQL systems, a volume set is a directory set. For MSM, a volume set is called a volume group.

### New Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following global is new with Toolkit V. 7.3:

> ^XUCS The ^XUCS global houses the files for the MSM-PC Performance Monitor (MPM). This new global will not exist in non-MSM sites. Automatic purging can be enabled for this file.

The following globals were new with Toolkit V. 7.2 and must be in place for Toolkit V. 7.3:

> ^XT The ^XT global is the location for all files related to Multi-Term Look-Up (MTLU). This global should reside in the Production account (VAH).

> ^XUCM The ^XUCM global contains the files for the VAX/Alpha Performance Monitor (VPM) and can be expected to grow at approximately 80 kb/day/node until you purge. Automatic purging can be enabled for this file. This global should reside in the Production account (VAH) in a cluster-mounted volume set.

NOTE 1: During this installation, a VPM pre-init converts the first subscript of ^XUCM to match the file number.

NOTE 2: With Toolkit V. 7.3 the ^XUCP global is no longer used for storage of Resource Usage data. DSM for OpenVMS sites can remove ^XUCP from their system. Data from the Resource Usage module now stores raw data in ^XTMP("XUCP"). Global growth is dependent on the amount of activity on your system and could be substantial. If running this module for the first time, we recommend running for brief periods (1-2 hour sessions) until you are more familiar with its behavior.

## Installing Toolkit V. 7.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Preliminary Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Kernel V. 7.1 must be in place before installing Toolkit V. 7.3.

2\. Your distribution media contains the following files:

> KTK7_3.RTN (Kernel Toolkit, version 7.3)

> K71PAT40.RTN (Kernel 7.1 patch \#40)

3\. This document assumes you have not yet installed Kernel V. 8. However, for Kernel V. 8 sites the following information is important:

> a\. Do not apply the Kernel 7.1 patch (#40). These are the routines contained in the file K71PAT40.RTN.

> b\. Verify that you have cleaned up your Production account of the unused Kernel Manager Routines. In particular, remove ZTMGRSET, ZOSV\* and ZOSF\*.

> c\. When instructed to move the Z\* routines from VAH to MGR, some routines will no longer exist. This is okay.

> d\. When instructed to run TOOLKIT^ZTMGRSET, the version for Kernel V. 8 will not ask you for input. This entry point only renames Toolkit routines to their "%" names.

4\. For all Kernel V. 7.1/Toolkit V. 7.2 sites, excluding Kernel V. 8 sites: Apply Kernel 7.1 patch \#40 to your Production account of the appropriate CPUs.

> NXT,KDE\>D ^%RR

> Routine Restore

> Input Device ? \> K71PAT40.RTN

> Restoring routines from USER\$:\[KERNEL.TK73BLD\]K71PAT40.RTN;2

> Saved by %RS from \[NXT,KDE\] on 22-FEB-1995 16:31:34.25

> Header: Kernel 7.1 Patch \#40

> Restore All (A), Selected (S), or Confirm on overwrite (C) ? \<A\> \<RET\>

> XGF XGFDEMO XGFDEMO1 XGKB XGS XGSA XGSBOX XGSETUP

> XGSW XPDMENU XPDUTL ZOSV1DTM ZOSV1GTM ZOSV1VXD ZOSV2MSM ZOSV2VXD

> ZOSVDTM ZOSVGTM ZOSVM11P ZOSVMSM ZOSVMVX ZOSVVXD ZTBKC ZTBKCDTM

> ZTBKCMP ZTBKCMSM ZTBKCMVX ZTBKCVXD ZTMGRSET

> 29 routines saved

> Copy the following routines to your corresponding Manager account(s):

> ZOSV\*

> ZTBK\*

> ZTMGRSET

> These routines and others will be renamed to "%" routines later in the installation. Review and complete all other "preliminary" steps that apply to your platform, then begin the installation.

5\. Skills required to perform the installation are listed below. Instructions for performing these functions are provided in Vendor-supplied operating system manuals as well as Decentralized Hospital Computer Program (DHCP) publications.

6\. DSM for OpenVMS instruction is provided in the *VAX DSM Systems Guide (Cookbook )*

7\. MSM-PC instruction is provided in the *486 Cookbook and MSM System Managers Guide*.

8\. You need to know how to:

• Log onto the system console.

• Shutdown and bring up (boot) the system.

• Load a magtape/diskpack and use the tape drive/disk drive.

• Enable/disable routine mapping and translate/implicit/replicate globals.

• Run a system status and restore a job.

• Copy routines using: diskettes, tapes, SDP space (PDP) or VMS files (VAX).

• Backup the system.

• Global management: enable/disable journaling, global placement, protection.

• Switch User Class Identification (UCI) from Manager (MGR) to Production (VAH).

#### MSM Sites

Your MUMPS implementation includes a %INDEX utility. This utility is similar to the one by the same name that is distributed with the Kernel Toolkit. It is important to note that:

• When loading Kernel Toolkit onto an MSM system, you overwrite the MSM %INDEX utility with the Kernel Toolkit's %INDEX utility.

• Consequently, whenever you update your copy of MSM you overwrite the Kernel Toolkit's %INDEX utility with the MSM %INDEX utility.

If you prefer using the Kernel Toolkit's version of %INDEX, remember to reload it whenever you update your copy of MSM.

The Kernel Toolkit %INDEX utility is exported in the ZINDX\* routines and can be restored as follows:

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>• <u>In MGR</u>: Restore %INDEX.</strong></p>
<p>After loading a new version of MSM, restore the Kernel Toolkit's like-named utility if its functionality is preferred.</p>
</blockquote></td>
<td><blockquote>
<p><em>MSM</em></p>
<p>&gt;<strong>D RESTORE^ZINDXH</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> **NOTE:** The Kernel Toolkit's %INDEX utility accommodates VA standards as well as the 1990 ANSI MUMPS Standard.

> The XIND\* routines have been supplied to perform %INDEX on applications requiring the Type A extension to the 1990 ANSI MUMPS Standard.

> These routines can be run directly (D ^XINDEX) and should not be placed in your Manager's account.

### Advance Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• Back up your system as a safeguard before the installation. Optionally, for future reference, you may also want to save a list of your Kernel routines by running a routine directory (D ^%RD) for the Kernel namespaces (X\*, Z\* subtracting out ZZ\*).

• Load the routines into a test account and run the NTEG routine listed below. If you have received a patched routine set, those patched routines are identified as being off by the number of bits that correspond to the patch and the affected routine(s) should have been noted in a cover letter. Exceptions to this should be reported to your ISC.

> \>D ^XTNTEG• Global Placement:

> ^XT

> The ^XT global was new with Toolkit V. 7.2 and is the location for all files related to Multi-Term Look-Up (MTLU).

> <u>In VAH</u>: If ^XT is not already placed, it should be placed in the appropriate volume set. Translate ^XT across all CPUs.

> ^XUCM

> For Alpha sites only, the ^XUCM global was new with Toolkit V. 7.2 and contains the files for the VAX/Alpha Performance Monitor (VPM). It can be expected to grow at approximately 80 kb/day/node until you purge.

> <u>In VAH</u>: If ^XUCM is not already placed, it should be placed in the appropriate volume set. Translate ^XUCM across all CPUs.

> ^XUCS

> For MSM sites only, Toolkit V. 7.3 brings in a *new* global, ^XUCS. This global houses the files for the MSM-PC Performance Monitor (MPM).

> <u>In VAH</u>: MSM sites should place the ^XUCS global in an appropriate volume set. If your site has more than one volume set, translate ^XUCS across all CPUs.

> Automatic purging can be enabled for the ^XUCM and ^XUCS files.

• Global Protection:

The global ^XUCS is used only by the MSM performance monitor and is new with Toolkit V. 7.3.

For MSM, verify that protection on the globals ^XT and ^XUCS is:

System: RWD

World: RWD

Group: RWD

User: RWD

For Alpha systems, the recommended protection for the ^XT and ^XUCM globals is:

System: RWP

World: RW

Group: RW

UCI: RWP

### VAX/ALPHA Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** 486 sites may skip this topic and continue with the "MSM-PC Installations" topic that follows.

The following steps are required to support the VAX/Alpha Performance Monitor (VPM):

• TaskMan *must* be set up to run from a DCL context. When run from a DCL context TaskMan runs as a privileged VMS user. The manager runs in DSM as a job that originated in a node-specific VMS batch queue and, by default, submits new submanagers to the same queue as needed. When a program calls ^ZTLOAD it is possible to request that the job be run on a *specific* CPU/Node in your cluster. The manager "submits" the job as a new submanager to that node-specific batch queue. This allows the programmer to control which CPU is to run a given job even though TaskMan is not running on that node. These principals are applied by VPM to control the collection of performance data and manage the underlying DCL files.

> To run from DCL, TaskMan requires the following:

> a\. VMS Username: TASKMAN

> b\. VMS Batch queues for each node in cluster named "TM\$\<nodename\>"

> c\. A VMS directory to hold a LOGIN.COM, ZTMWDCL.COM, and ZTMSWDCL.COM along with TaskMan-related log files and a system-wide logical name, "DHCP\$TASKMAN," defined on all nodes pointing to this directory.

> d\. Box:Volume pairs and a DSM Environment Manager defined for all nodes in the cluster (TASKMAN SITE PARAMETERS file (#14.7)). Defining the DSM Environment, stopping and restarting TaskMan causes him to run from a DCL context. Deleting this entry, stopping and restarting TaskMan causes him to run in "normal" mode.

This task can be accomplished at any point prior to configuring and enabling VPM.

Alternatively, to assist with setting up the components needed by TaskMan *after* installing Toolkit V. 7.3, we have included the routine ^XUCMTM. To execute the routine, you should be logged in with the VMS privileges OPER and SYSPRV. Log into your DSM Production account and execute the routine from programmer mode. Again, this step must be completed *prior* to configuring and enabling VPM.

> NOTE: For complete information on configuring TaskMan to run in a DCL context see the topic entitled "Running TaskMan with a VMS DCL Context" under the "Task Manager" chapter in the *Kernel Systems Manual V. 7.1* (pp. 294-298).

#### Sample Dialogue of Running ^XUCMTM

\>D ^XUCMTM

This routine will assist you in configuring TASKMAN to run from a

DCL CONTEXT.

This procedure begins on page 294 of the Kernel 7.1 SYSTEMS MANUAL.

First, select an HFS device for writing to Taskman's home directory.

Select a HOST FILE SERVER device: HFS DISK FILE

HOST FILE NAME: TMP.TMP// \<RET\> INPUT/OUTPUT OPERATION: N

Now, let's create Taskman's home directory.

Enter the drive/path: USER\$:\[TASKMAN\] (this entry is site specific)

This step creates a new entry in UAF called TASKMAN.

You will need to provide the UIC code in the format '\[#,#\].'

Taskman will require at LEAST the following privileges:

CMKRNL, TMPMBX, OPER, NETMBX

Would you like to see a brief listing of UAF records? YES// NO

Assign TASKMAN to what UIC: \[50,20\] (this entry is site specific)

Would you like to copy an existing user over to TASKMAN? Y// NO

%UAF-I-ADDMSG, user record successfully added

%UAF-I-RDBADDMSGU, identifier TASKMAN value: \[000050,000020\] added to rights data base

%CREATE-I-EXISTS, USER\$:\[TASKMAN\] already exists

...WRITING OUT 'LOGIN.COM'

...WRITING OUT 'ZTMWDCL.COM'

...WRITING OUT 'ZTMSWDCL.COM'

The final step will be to define the TASKMAN batch queues for each node

in your cluster.

Enter the name of each node in your DHCP cluster. Press RETURN when finished.

Enter NODENAME: 612K01 (enter the nodenames at your site)

Enter NODENAME: 612K02

Enter NODENAME: \<RET\> (at this point, your queues have been created)

FINAL CHECKS:

1\. Verify that you can log in as the user TASKMAN.

2\. For each node that has the TM\$ batch queue, define the system

logical DHCP\$TASKMAN=taskman's home directory. Be sure to place

the command in your system startup procedure. (see page 295)

3\. If you have implemented ACL security for your DSM environments

log into your manager account and D ^ACL. Provide MANAGER access

for the new user TASKMAN.

4\. Using the option SITE PARAMETER EDIT, define a box-volume pair for

each node containing the TM\$NODENAME batch queue. Be sure to fill

the field VAX/ALPHA DSM ENVIRONMENT FOR DCL.

5\. STOP/RESTART TASKMAN TO ACTIVATE THE NEW SETTINGS.

Review the New VMS User, TASKMAN

KRN,KDE\>

612K01: MC AUTHORIZE

UAF\> SHO TASKMAN

Username: TASKMAN Owner:

Account: UIC: \[50,20\] (\[DEV,TASKMAN\])

CLI: DCL Tables: DCLTABLES

Default: USER\$:\[TASKMAN\]

LGICMD: LOGIN.COM

Flags: DisCtlY Restricted DisWelcome DisReport Captive

Primary days: Mon Tue Wed Thu Fri

Secondary days: Sat Sun

No access restrictions

Expiration: (none) Pwdminimum: 6 Login Fails: 0

Pwdlifetime: 180 00:00 Pwdchange: (pre-expired)

Last Login: (none) (interactive), (none) (non-interactive)

Maxjobs: 0 Fillm: 100 Bytlm: 40960

Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

Maxdetach: 0 BIOlm: 18 JTquota: 1024

Prclm: 2 DIOlm: 18 WSdef: 300

Prio: 4 ASTlm: 24 WSquo: 500

Queprio: 0 TQElm: 10 WSextent: 2048

CPU: (none) Enqlm: 300 Pgflquo: 10240

Authorized Privileges:

CMKRNL TMPMBX OPER NETMBX

Default Privileges:

CMKRNL TMPMBX OPER NETMBX

UAF\> EXIT

> **NOTE:** Password protect your new user and log in to test the password protection. If you do not use ACL protection on your MUMPS accounts, TaskMan may need to have SYSPRV privilege as well.

Grant the New User TASKMAN <u>Manager</u> Access to DSM

MGR,KDE\>D ^ACL

Environment Access Utilities

1\. ADD/MODIFY USER (ADD^ACL)

2\. DELETE USER (DELETE^ACL)

3\. MODIFY ACTIVE AUTHORIZATIONS (^ACLSET)

4\. PRINT AUTHORIZED USERS (PRINT^ACL)

Select Option \> 1. \<RET\> ADD/MODIFY USER

OpenVMS User Name: \> TASKMAN

ACCESS MODE VOL UCI ROUTINE

----------- --- --- -------

No access rights for this user.

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> M

USER ACCESS MODE VOL UCI ROUTINE

---- ----------- --- --- -------

TASKMAN MANAGER

OK to file? \<Y\> Y

Identifier DSM\$MANAGER_KDAMGR granted to user TASKMAN.

Modifications have been made to the OpenVMS rights database.

These changes will take effect the next time TASKMAN logs in to

the OpenVMS system.

OpenVMS User Name: \> \<RET\>

OK to activate changes now? \<Y\> Y

Creating access authorization file: DSA0:\[KDAMGR\]DSM\$ACCESS.DAT.

Press RETURN to continue

Verify that your Batch Queues were Created

612K01: SHO QUE/FULL TM\$\*

Batch queue TM\$612K01, idle, on 612K01::

/BASE_PRIORITY=4 /JOB_LIMIT=50 /OWNER=\[DEV,TASKMAN\] /PROTECTION=(S:E,O:D,G:R,W:W)

Batch queue TM\$612K02, idle, on 612K02::

/BASE_PRIORITY=4 /JOB_LIMIT=50 /OWNER=\[DEV,TASKMAN\] /PROTECTION=(S:E,O:D,G:R,W:W)

• Set up *two* new mail groupsREDACTED. The first should contain only local recipients for VAX/ALPHA Performance Monitor (VPM) messages and alerts. The second should contain the remote recipient, REDACTEDError! Bookmark not defined.. If your local ISC wishes to collect and file site data, enter an appropriate recipient for your local ISC as well. You are asked to enter these new mail groups in the CM SITE PARAMETERS file (#8986.095) at the conclusion of the Toolkit init.

• ISCs wishing to collect performance data from a site may request server routines from REDACTED to file the data.

Verify an Entry Exists in the DEVICE file (#3.5) for the Following Devices:

> **NOTE:** Some entries are site-specific.

NAME: HFS (*name optional*) \$I: TMP.TMP

ASK DEVICE: YES ASK PARAMETERS: NO

VOLUME SET(CPU): ISC LOCATION OF TERMINAL: HOST DISK FILE

ASK HOST FILE: YES ASK HFS I/O OPERATION: YES

MARGIN WIDTH: 132 FORM FEED: \#

PAGE LENGTH: 64 BACK SPACE: \$C(8)

SUBTYPE: P-OTHER TYPE: HOST FILE SERVER

NAME: SYS\$INPUT \$I: SYS\$INPUT:.;

ASK DEVICE: NO ASK PARAMETERS: NO

LOCATION OF TERMINAL: DISK FILE MARGIN WIDTH: 80

FORM FEED: \# PAGE LENGTH: 64

BACK SPACE: \$C(8) SUBTYPE: P-OTHER80

TYPE: TERMINAL

### MSM-PC Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSM SITES should complete the following preliminary steps to enable performance monitoring:

1\. Review the "Advance Preparation" topic in this manual for important information on Global Placement/Protection of the ^XT, ^XUCM, and ^XUCS globals.

2\. If the ^RTHIST global was established prior to installing version 4.0 of MSM, it should be deleted and re-established. To do this, on the Compute/Print Servers in the Manager UCI, use ^%GDEL and delete the ^RTHIST global and reset it to ^RTHIST="".

> NOTE: The NOKILL flag may have been set for all globals. This should be removed to avoid an ACCESS DENIED error.

3\. Prepare your other CPUs for support of TaskMan jobs. Move the following Kernel V. 7.1 and FileMan V. 20 routines to the Manager UCI of both the File and Shadow Servers:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DIDT*</p>
</blockquote></td>
<td><blockquote>
<p>ZI*</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DIRCR</p>
</blockquote></td>
<td><blockquote>
<p>-ZISL*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XUCIMSM</p>
</blockquote></td>
<td><blockquote>
<p>ZISLVR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ZUA</p>
</blockquote></td>
<td><blockquote>
<p>ZISLDIS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ZT*</p>
</blockquote></td>
<td><blockquote>
<p>ZISLSIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ZOS*</p>
</blockquote></td>
<td><blockquote>
<p>ZISLPC</p>
</blockquote></td>
</tr>
</tbody>
</table>

4\. Setup the Global Translation on the File Server.

\>D ^SYSGEN

MSM - System Generation Utility

Select SYSGEN Option: 3 - Edit Configuration Parameters

Select Configuration \<FSA\>: FSA

Select SYSGEN Option: 13 - Translation/Replication Table Maintenance

Available Functions:

1 - Edit Translation Table

2 - Enable Translation

3 - Disable Translation

4 - Edit Replication Table

5 - Translation Table List

6 - Replication Table List

Select Option: 1 - Edit Translation Table

Translation table is empty.

Enter Translation Table Index: 1

Global name: %ZOSF

Collating sequence \<NUMERIC\>: NUMERIC

Global encoding \[7=7-bit/8=8-bit\] \<8\>: 8

UCI to translate from: MGR,FSA

4\. Setup the Global Translation on the File Server (continued):

UCI to translate to: MGR,FSA

UCI for maintenance of locks \<MGR,FSA\>: MGR,FSA

Replication table index:

Enable translation \<YES\>: YES

Enable lock table translation \<YES\>: YES

Enter Translation Table Index: 2

Global name: %Z\*

Collating sequence \<NUMERIC\>: NUMERIC

Global encoding \[7=7-bit/8=8-bit\] \<8\>: 8

UCI to translate from: MGR,FSA

UCI to translate to: MGR,PSA

UCI for maintenance of locks \<MGR,PSA\>: MGR,PSA

Replication table index:

Enable translation \<YES\>: YES

Enable lock table translation \<YES\>: YES

Enter Translation Table Index: ^L

Current Translation Table:

Global Translate Lock Repl Functions Coll Global

\# Name(s) From UCI To UCI Master Ind Enabled Seq encode

------- ---------------- ------ ---- --------- ---- ------

1\* %ZOSF MGR,FSA MGR,FSA MGR,FSA TRANSLATION NUM 8-bit

LOCK MASTER

2\* %Z\* MGR,FSA MGR,PSA MGR,PSA TRANSLATION NUM 8-bit

LOCK MASTER

Entries with a '\*' have been modified since Translation was enabled.

The Translation Table in memory does not reflect these changes.

Translation is not enabled

Enter Translation Table Index:

Press \<RETURN\> to continue

Available Functions:

1 - Edit Translation Table

2 - Enable Translation

3 - Disable Translation

4 - Edit Replication Table

5 - Translation Table List

6 - Replication Table List

Select Option: 2 - Enable Translation

Enabling translation...

Press \<RETURN\> to continue

Available Functions:

1 - Edit Translation Table

2 - Enable Translation

3 - Disable Translation

4 - Edit Replication Table

5 - Translation Table List

6 - Replication Table List

Select Option: \<RET\>

5\. Run ZTMGRSET in the Manager's UCI of the File server.

6\. In MGR, rename the following FileMan routines:

> \>ZL DIDT

> \>ZS %DT

> \>ZL DIDTC

> \>ZS %DTC

> \>ZL DIRCR

> \>ZS %RCR

7\. Edit the File Servers for TASKMAN SITE PARAMETERS (#14.7), VOLUME SET (#14.5), and UCI ASSOCIATION (#14.6) files:

> NOTE: For additional information on this, please refer to page 246 of the *Kernel Systems Manual V. 7.1.*

Task Manager

Select Task Manager Option: Taskman Management Utilities

Select Taskman Management Utilities Option: Edit Taskman Parameters

Select Edit Taskman Parameters Option: SITE Parameters Edit

Select TASKMAN SITE PARAMETERS BOX-VOLUME PAIR: FSB

ARE YOU ADDING 'FSB' AS A NEW TASKMAN SITE PARAMETERS (THE 4TH)? Y (YES)

BOX-VOLUME PAIR: FSB//

LOG TASKS?: N NO

DEFAULT TASK PRIORITY: 4

TASK PARTITION SIZE:

SUBMANAGER RETENTION TIME: 0

TASKMAN JOB LIMIT: 14

TASKMAN HANG BETWEEN NEW JOBS: 1

MODE OF TASKMAN: COMPUTE SERVER \<\<\<\<\<\<\<*IMPORTANT!NOTE: This setup differs to allow MPM to initiate and run tasks on your file servers.*

VAX DSM ENVIRONMENT FOR DCL

OUT OF SERVICE: NO

LOAD BALANCE ROUTINE:

Select TASKMAN SITE PARAMETERS BOX-VOLUME PAIR:

Select Edit Taskman Parameters Option: VOLume Set Edit

Select VOLUME SET: FSB

ARE YOU ADDING 'FSB' AS A NEW VOLUME SET (THE 5TH)? Y (YES)

VOLUME SET: FSB// \<RET\>

TYPE: COMPUTE SERVER

INHIBIT LOGONS?: N NO

LINK ACCESS?: \<RET\>

OUT OF SERVICE?: N NO

REQUIRED VOLUME SET?: N NO *This field may be set to YES, if desired*

TASKMAN FILES UCI: MGR

TASKMAN FILES VOLUME SET: PSA

REPLACEMENT VOLUME SET: \<RET\>

DAYS TO KEEP OLD TASKS: 4

Select VOLUME SET: \<RET\>

Select Edit Taskman Parameters Option: UCI Association Table Edit

7\. Edit the File Servers for TASKMAN SITE PARAMETERS, VOLUME SET, and UCI ASSOCIATION files (continued):

Select UCI ASSOCIATION FROM UCI: VAH

1 VAH PSA

2 VAH CSA

3 VAH CSB

4 VAH FSA

CHOOSE 1-4:

ARE YOU ADDING 'VAH' AS A NEW UCI ASSOCIATION (THE 9TH)? Y (YES)

UCI ASSOCIATION NUMBER: 9// \<RET\>

UCI ASSOCIATION FROM VOLUME SET: FSB

UCI ASSOCIATION TO VOLUME SET: \<RET\>

UCI ASSOCIATION TO UCI: \<RET\>

FROM UCI: VAH// \<RET\>

FROM VOLUME SET: FSB// \<RET\>

TO VOLUME SET: \<RET\>

TO UCI:

Select UCI ASSOCIATION FROM UCI: MGR

1 MGR PSA

2 MGR CSA

3 MGR CSB

4 MGR FSA

CHOOSE 1-4:

ARE YOU ADDING 'MGR' AS A NEW UCI ASSOCIATION (THE 10TH)? Y (YES)

UCI ASSOCIATION NUMBER: 10// \<RET\>

UCI ASSOCIATION FROM VOLUME SET: FSB

UCI ASSOCIATION TO VOLUME SET: \<RET\>

UCI ASSOCIATION TO UCI: \<RET\>

FROM UCI: MGR// \<RET\>

FROM VOLUME SET: FSB// \<RET\>

TO VOLUME SET: \<RET\>

TO UCI: \<RET\>

Select UCI ASSOCIATION FROM UCI:

### Begin the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For VAX/ALPHA sites: Copy the contents of the media into a VMS file if you have not already done so. Later on in the installation process, the routines may then be read into production from disk which, for most configurations, is faster than reading from tape or floppy media. Also, create a large symbol table at sign-on, (\$ DSM/SYM=100000) so there is enough space to work.

For MSM sites: Be sure to run the inits on the Print Server (e.g., Production account, not Manager account), where TaskMan resides, so that tasked post-inits run. Also, when logging on, increase the symbol table size to 40K so that there is enough space to work:

> UCI,VOL:ROU:40For other sites: Be sure to run the inits with as large a partition as you can.

• Logon using the console.VAX/ALPHA sites: To maneuver without access restrictions, use a privileged VMS account.

MSM sites: log onto the print server.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Begin the installation in the Production account</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

*It is assumed that you have the capability to move back and forth from the Manager and Production accounts. After moving to another UCI, it is useful to verify your location as a safeguard (e.g., \>W \$ZU(0) or use another technique).*• <u>In VAH</u>: Logons are *not* inhibited. Users may remain on the system during installation provided they are not running any options in the following menus:

\[XUPROG\] Programmer Options

\[XUSITEMGR\] Operations Management

• VMS sites should unschedule the options, XUCM TASK VPM and XUCM TASK NIT for the duration of the installation.• If files have been configured for version 7.2 of Multi-Term Look-Up, users of MTLU may experience errors while new ^XTLK\* routines are being installed. Since installation time is brief and MTLU look-ups are infrequent, any inconvenience to users may be minimal. They should simply repeat their look-up at a later time.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Move over to the Manager (Library) account</strong></p>
<p><strong>(e.g., MGR)</strong></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>• <u>In MGR</u>: Disable routine mapping</strong> (if applicable) for Library and Production accounts.</td>
<td><p>DSM for OpenVMS</p>
<p>&gt;<strong>D ^RMAP</strong></p>
<p><em>MSM and M/SQL</em></p>
<p>Not Applicable</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Move back to the Production account</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

### Read the Routines into Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>• <u>In VAH</u>: Read Routines into Production.</strong> Load routines from the tape or, for VAX/ALPHA sites, from the VMS file created earlier from the tape.</p>
<p><em>(It is assumed that you are familiar with your operating system utilities for loading, saving, and restoring routines.)</em></p></td>
<td><p><em>M/SQL</em></p>
<p>&gt;<strong>D ^%RI</strong></p>
<p><em>ALL OTHER SYSTEMS</em></p>
<p>&gt;<strong>D ^%RR</strong></p></td>
</tr>
</tbody>
</table>

|                                                                                                                                                                                                                                                               |                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| • <u>In VAH</u>: Optionally run the NTEG routines in the Production account if you have not already done so in a test account. Report any "off-by" results to your local ISC. Discrepancies may simply indicate that your tape includes patched routines. | \>D ^XTNTEG |

Example of Routine Restore done at the San Francisco ISC.

KRN,KDE\>D ^%RR

Routine Restore

Input Device ? \> KTK7_3.RTN

Restoring routines from USER\$:\[KERNEL.TK73BLD\]KTK7_3.RTN;1

Saved by %RS from \[NXT,KDE\] on 3-APR-1995 12:00:53.50

Header: Kernel Toolkit 7.3 created by JIC at ISC-SF

Restore All (A), Selected (S), or Confirm on overwrite (C) ? \<A\> \<RET\>

XDRCNT XDRDADD XDRDADJ XDRDCOMP XDRDFPD XDRDLIST XDRDMAIN XDRDOC

XDRDOC1 XDRDOC2 XDRDPDTI XDRDPRGE XDRDQUE XDRDSCOR XDRDSTAT XDRDUP

XDREMSG XDRERR XDRHLP XDRMADD XDRMAIN XDRMAINI XDRMPACK XDRMRG

XDRMRG1 XDRMSG XDRMVFY XDRPREI XDRU1 XINDEX XINDX1 XINDX10

XINDX11 XINDX2 XINDX3 XINDX4 XINDX5 XINDX51 XINDX52 XINDX53

XINDX6 XINDX7 XINDX8 XINDX9 XTBASE XTCMFILN XTEDTVXD XTFC0

XTFC1 XTFCE XTFCE1 XTFCR XTFCR1 XTINEND XTINI001 XTINI002

XTINI003 XTINI004 XTINI005 XTINI006 XTINI007 XTINI008 XTINI009 XTINI00A

XTINI00B XTINI00C XTINI00D XTINI00E XTINI00F XTINI00G XTINI00H XTINI00I

XTINI00J XTINI00K XTINI00L XTINI00M XTINI00N XTINI00O XTINI00P XTINI00Q

XTINI00R XTINI00S XTINI00T XTINI00U XTINI00V XTINI00W XTINI00X XTINI00Y

XTINI00Z XTINI010 XTINI011 XTINI012 XTINI013 XTINI014 XTINI015 XTINI016

XTINI017 XTINI018 XTINI019 XTINI01A XTINI01B XTINI01C XTINI01D XTINI01E

XTINI01F XTINI01G XTINI01H XTINI01I XTINI01J XTINI01K XTINI01L XTINI01M

XTINI01N XTINI01O XTINI01P XTINI01Q XTINI01R XTINI01S XTINI01T XTINI01U

XTINI01V XTINI01W XTINI01X XTINI01Y XTINI01Z XTINI020 XTINI021 XTINI022

XTINI023 XTINI024 XTINI025 XTINI026 XTINI027 XTINI028 XTINI029 XTINI02A

XTINI02B XTINI02C XTINI02D XTINI02E XTINI02F XTINIS XTINIT XTINIT1

XTINIT2 XTINIT3 XTINIT4 XTINIT5 XTINITY XTINOK XTKERM1 XTKERM2

XTKERM3 XTKERM4 XTKERMIT XTLATSET XTLKDICL XTLKEFOP XTLKKSCH XTLKKWL

XTLKKWL1 XTLKKWL2 XTLKKWLD XTLKMGR XTLKPRT XTLKPST XTLKTICD XTLKTOKN

XTLKWIC XTNTEG XTNTEG0 XTNTEG01 XTRCMP XTRGRPE XTRTHV XTSPING

XTSUMBLD XTVCHG XTVGC1 XTVGC1A XTVGC2 XTVGC2A XTVGC2A1 XTVNUM

XTVRC1 XTVRC1A XTVRC1Z XTVRC2 XTVRCRES XUCIN001 XUCIN002 XUCIN003

XUCIN004 XUCIN005 XUCIN006 XUCIN007 XUCIN008 XUCIN009 XUCIN00A XUCIN00B

XUCIN00C XUCIN00D XUCIN00E XUCIN00F XUCIN00G XUCIN00H XUCIN00I XUCIN00J

XUCIN00K XUCIN00L XUCIN00M XUCIN00N XUCIN00O XUCIN00P XUCIN00Q XUCIN00R

XUCIN00S XUCIN00T XUCIN00U XUCIN00V XUCIN00W XUCIN00X XUCIN00Y XUCIN00Z

XUCIN010 XUCIN011 XUCINIS XUCINIT XUCINIT1 XUCINIT2 XUCINIT3 XUCINIT4

XUCINIT5 XUCMBR1 XUCMBR2 XUCMBR3 XUCMBRTL XUCMDSL XUCMFGI XUCMFIL

XUCMGRAF XUCMNI2A XUCMNIT XUCMNIT1 XUCMNIT2 XUCMNIT3 XUCMNIT4 XUCMNIT5

XUCMNT3A XUCMPA XUCMPA1 XUCMPA2 XUCMPA2A XUCMPA2B XUCMPOST XUCMPRE

XUCMTM XUCMTM1 XUCMVPG XUCMVPG1 XUCMVPI XUCMVPM XUCMVPM1 XUCMVPS

XUCMVPU XUCPCLCT XUCPFRMT XUCPRAW XUCS1E XUCS1R XUCS1RA XUCS1RB

XUCS1RBA XUCS2E XUCS2R XUCS2RA XUCS2RB XUCS2RBA XUCS4E XUCS4R

Example of Routine Restore done at the San Francisco ISC (continued) :

XUCS4RB XUCS5E XUCS5EA XUCS6E XUCS6R XUCS8E XUCS8R XUCS8RB

XUCS8RG XUCS8RGA XUCSCDE XUCSCDG XUCSCDGA XUCSCDR XUCSCDRB XUCSI001

XUCSI002 XUCSI003 XUCSI004 XUCSI005 XUCSI006 XUCSI007 XUCSI008 XUCSI009

XUCSI00A XUCSI00B XUCSI00C XUCSI00D XUCSI00E XUCSI00F XUCSI00G XUCSI00H

XUCSI00I XUCSI00J XUCSI00K XUCSI00L XUCSINI1 XUCSINI2 XUCSINI3 XUCSINI4

XUCSINI5 XUCSINIS XUCSINIT XUCSLOAD XUCSPRG XUCSRV XUCSTM XUCSTME

XUCSUTL XUCSUTL2 XUCSUTL3 XURTL XURTL1 XURTL2 XURTL3 XURTL4

XURTLC XURTLK ZINDEX ZINDX1 ZINDX10 ZINDX11 ZINDX2 ZINDX3

ZINDX4 ZINDX5 ZINDX51 ZINDX52 ZINDX53 ZINDX6 ZINDX8 ZINDX9

ZINDXH ZTEDIT ZTEDIT1 ZTEDIT2 ZTEDIT3 ZTEDIT4 ZTGS ZTP1

ZTPP ZTRDEL ZTRTHV

363 routines restored

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Continue working in the Production account</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

### Move Routines to the Manager Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>• <u>In VAH</u>: Move routines out to a host file.</strong></td>
<td><p><em>M/SQL</em></p>
<p>&gt;<strong>D ^%RO</strong></p>
<p><em>ALL OTHER SYSTEMS</em></p>
<p>&gt;<strong>D ^%RS</strong> (or use ^<strong>%RCOPY</strong>)</p></td>
</tr>
</tbody>
</table>

Example of Routine Save done at the San Francisco ISC

NXT,KDE\>D ^%RS

Routine Save

Output Device ? \> TKMGR.RTN

Header comment...

routine(s) ? \> ZT\*

searching directory ...

routine(s) ? \> -ZTM\*

routine(s) ? \> -ZTL\*

routine(s) ? \> -ZTER\*

routine(s) ? \> ZOS\*

searching directory ...

routine(s) ? \> ZIND\*

searching directory ...

routine(s) ? \> ZTMGRSET

routine(s) ? \> \<RET\>

Saving routines on USER\$:\[BETA\]TKMGR.RTN;3

ZINDEX ZINDX1 ZINDX10 ZINDX11 ZINDX2 ZINDX3 ZINDX4 ZINDX5

ZINDX51 ZINDX52 ZINDX53 ZINDX6 ZINDX8 ZINDX9 ZINDXH ZOSFDTM

ZOSFGTM ZOSFM11P ZOSFMSM ZOSFMVX ZOSFVXD ZOSV1DTM ZOSV1GTM ZOSV1VXD

ZOSV2MSM ZOSV2VXD ZOSVDTM ZOSVGTM ZOSVM11P ZOSVMSM ZOSVMVX ZOSVVXD

ZTBKC ZTBKCDSM ZTBKCDTM ZTBKCMP ZTBKCMSM ZTBKCMVX ZTBKCVXD ZTEDIT

ZTEDIT1 ZTEDIT2 ZTEDIT3 ZTEDIT4 ZTGS ZTMGRSET ZTP1 ZTPP

ZTRDEL ZTRTHV

50 routines saved

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Move over to the Manager (Library) account</strong></p>
<p><strong>(e.g., MGR)</strong></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>• <u>In MGR</u>: Restore routines from the</strong> <strong>host file</strong> to your MGR account<strong>.</strong></td>
<td><p><em>M/SQL</em></p>
<p>&gt;<strong>D ^%RI</strong></p>
<p><em>ALL OTHER SYSTEMS</em></p>
<p>&gt;<strong>D ^%RR</strong></p></td>
</tr>
</tbody>
</table>

### Run the Manager Setup Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 1%" />
<col style="width: 49%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><p><strong>• <u>In MGR</u>: Run the Manager Setup Routine.</strong></p>
<blockquote>
<p>Run this routine so that operating system-specific routines can be identified and renamed as "%" routines for proper functioning in the Manager account. After responding to the prompts as illustrated on the following page, ZTMGRSET loads the routines which are common to all systems and saves them as percent routines (e.g., ZINDEX is saved as %INDEX). It then installs the ^%Z editor and checks that ^%ZIS("C") only holds a call to the ^%ZISC routine. Finally, it sets up two files stored in ^%ZUA, the FAILED ACCESS ATTEMPT LOG (#3.05) and the PROGRAMMER MODE LOG (#3.07) files.</p>
<p>Enter the name of the MUMPS implementation you are running. This sets the first piece of ^%ZOSF("OS").</p>
<p>Indicate the name of your Manager account.</p>
<p>Indicate the name of your sign-on Production account.</p>
<p>Enter the name of the current volume or directory set. Notice that ^ZTMGRSET no longer asks you about the location of the ^XMB global. Instead, it deletes the obsolete ^%ZOSF("MASTER") and ^%ZOSF("SIGNOFF") nodes.</p>
</blockquote></td>
<td><p>&gt;<strong>D TOOLKIT^ZTMGRSET</strong></p>
<p><em>DSM for OpenVMS</em></p>
<p>SYSTEM: <strong>VAX DSM(V6)</strong></p>
<p>NAME OF MANAGER’S UCI: <strong>MGR,ROU</strong></p>
<p>PRODUCTION (SIGN-ON) UCI: <strong>VAH,ROU</strong></p>
<p>NAME OF VOLUME SET: <strong>ROU</strong></p>
<p><em>MSM</em></p>
<p>SYSTEM: <strong>MSM</strong></p>
<p>NAME OF MANAGER’S UCI: <strong>MGR,PSA</strong></p>
<p>PRODUCTION (SIGN-ON) UCI: <strong>VAH,PSA</strong></p>
<p>NAME OF VOLUME SET: <strong>PSA</strong></p>
<p><em>If you haven't already done so, then at this point you may load the Toolkit Manager account routines (Z*) from disk to all other CPU/volume groups for performance monitoring. Be sure to run TOOLKIT^ZTMGRSET in the MGR UCI of each CPU.</em></p>
<p><em>M/SQL</em></p>
<p>SYSTEM: <strong>M/SQL</strong></p>
<p>NAME OF MANAGER’S UCI: <strong>MG,BLUE</strong></p>
<p>PRODUCTION (SIGN-ON) UCI: <strong>VA,BLUE</strong></p>
<p>NAME OF VOLUME SET: <strong>BLUE</strong></p></td>
</tr>
<tr class="even">
<td colspan="3"><p><strong>Continue working in the Manager (Library) account</strong></p>
<p><strong>(e.g., MGR)</strong></p></td>
</tr>
</tbody>
</table>

Example of Manager Setup Routine done at the San Francisco ISC

\>D TOOLKIT^ZTMGRSET

ZTMGRSET Version 7.3

HELLO! I exist to assist you in correctly initializing the MGR account

or to update the current account.

I think you are using VAX DSM(V6)

Which MUMPS system should I install?

1 = NOT SUPPORTED

2 = M/SQL-PDP

3 = M/SQL-VAX

4 = DSM V4.1

5 = VAX DSM(V6)

6 = MSM

7 = Datatree

System: 5// \<RET\>

Removing obsolete ^%ZOSF nodes...

I will now rename a group of routines specific to your operating system.

Loading ZOSVVXD Saved as %ZOSV

Loading ZTBKC Saved as %ZTBKC

Loading ZTBKCVXD Saved as %ZTBKC1

Loading ZOSV1VXD Saved as %ZOSV1

Loading ZOSV2VXD Saved as %ZOSV2

NAME OF MANAGER'S UCI,VOLUME SET: MGR,KDE// \<RET\>

PRODUCTION (SIGN-ON) UCI,VOLUME SET: KRN,KDE// \<RET\>

NAME OF VOLUME SET: KDE// \<RET\>

Example of Manager Setup Routine done at the San Francisco ISC (continued) :

Now to load routines common to all systems.

Loaded ZINDEX Saved as %INDEX

Loaded ZINDX1 Saved as %INDX1

Loaded ZINDX10 Saved as %INDX10

Loaded ZINDX11 Saved as %INDX11

Loaded ZINDX2 Saved as %INDX2

Loaded ZINDX3 Saved as %INDX3

Loaded ZINDX4 Saved as %INDX4

Loaded ZINDX5 Saved as %INDX5

Loaded ZINDX51 Saved as %INDX51

Loaded ZINDX52 Saved as %INDX52

Loaded ZINDX53 Saved as %INDX53

Loaded ZINDX6 Saved as %INDX6

Loaded ZINDX8 Saved as %INDX8

Loaded ZINDX9 Saved as %INDX9

Loading ZTPP Saved as %ZTPP

Loading ZTP1 Saved as %ZTP1

Loading ZTRDEL Saved as %ZTRDEL

Installing ^%Z editor

ALL DONE

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Continue working in the Manager (Library) account</strong></p>
<p><strong>(e.g., MGR)</strong></p></td>
</tr>
</tbody>
</table>

### Review Global Protection for ^%ZRTL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>• <strong><u>In MGR</u>:</strong> Confirm that the ^%ZRTL global is defined in the Manager account and set with appropriate protections. (The ^%ZRTL global holds response time monitors.)</p>
<blockquote>
<p>^%ZRTL is common to all processors.</p>
</blockquote></td>
<td><p><em>DSM for OpenVMS</em></p>
<p>&gt;<strong>D ^%GLOMAN</strong></p>
<p><em>(Manage globals in which UCI?: <strong>MGR</strong>)</em></p>
<p><strong>^%ZRTL</strong></p>
<p>System) RWP World) RW Group) RW UCI) RWP</p>
<p><em>MSM</em></p>
<p>&gt;<strong>D ^%GCH</strong></p>
<p><em>(Set protection)</em></p>
<p><strong>^%ZRTL</strong></p>
<p>System) RWD World) RWD Group) RWD USER) RWD</p>
<p><em>M/SQL</em></p>
<p>&gt;<strong>D ^%PROTECT</strong></p>
<p><em>(Manage globals in which UCI?: <strong>MGR</strong>)</em></p>
<p><strong>^%ZRTL</strong></p>
<p>Network) RWD World) RW Group) RW Owner) RWD</p></td>
</tr>
</tbody>
</table>

### Establish Global Translation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 37%" />
<col style="width: 58%" />
<col style="width: 2%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>• <u>In MGR</u>:</strong> Review translation for ^XT and ^XUCM on DSM systems, ^XT and ^XUCS on MSM systems.</td>
<td colspan="2"><p><em>DSM for OpenVMS</em></p>
<p>&gt;<strong>D ^TRANTAB</strong> <em>(for DSM V4.0 or later)</em></p>
<p><em>(Be sure that ^XT and ^XUCM are translated to a cluster mounted volume set.)</em></p>
<p><em>MSM</em></p>
<p>&gt;<strong>D ^TRANSLAT</strong></p>
<p><em>(Be sure that ^XT and ^XUCS are translated across VAH UCIs.)</em></p>
<p><em>M/SQL</em></p>
<p>Not Applicable</p></td>
</tr>
<tr class="even">
<td colspan="2"><p><strong>Move back to the Production account</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Do the First Part of the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>• <u>In VAH</u>: Run the Toolkit inits.</strong></p>
<blockquote>
<p><strong>For DSM for OpenVMS</strong>: Create a large symbol table at sign-on,</p>
<p>($ DSM/UCI=VAH/SYM=100000).</p>
<p><strong>For MSM</strong>: Increase the symbol table size to 40K by responding to the UCI prompt as follows: UCI,VOL:ROU:40. Otherwise, type D ^%PARTSIZ to set the partition size.</p>
<p><strong>For M/SQL</strong>: Be sure you have at least a 16K partition. W $S to see the current size.</p>
</blockquote></td>
<td><p><em>ALL OPERATING SYSTEMS</em></p>
<p>&gt;<strong>D ^XUP</strong> <em>(To set DUZ when responding to the Access Code prompt. Press return at the OPTION prompt.)</em></p>
<p>&gt;<strong>D Q^DI</strong> <em>(To set DUZ(0)="@". Press return at the OPTION prompt.)</em></p></td>
</tr>
</tbody>
</table>

XTINITs take approximately 7-15 minutes.

If you have multiple CPUs, turn to the topic "On the Other Toolkit V. 7.2 CPUs (MSM and M/SQL)".

> **NOTE:** The text of the init dialogue may not be an exact match of what you see when running the installation. It is provided as a best approximation of a typical install. Explanatory notes are provided along with the dialogue that should give some indication why your experience may differ from the example presented here.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>From the Production account</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

### Example of an Init done at the San Francisco ISC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This is an example of an installation from the San Francisco development account. The messages at your site may look slightly different.

VAH,MTL\>D ^XTINIT

This version (#7.3) of 'XTINIT' was created on 03-APR-1995

(at NXT, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

I'm checking to see if it is OK to install Toolkit v7.3

in this account.

Everything looks OK, Lets continue.

I AM GOING TO SET UP THE FOLLOWING FILES:

3.091 RESPONSE TIME

> **NOTE:** You already have the 'RESPONSE TIME' File.

Shall I write over the existing Data Definition? YES// \<RET\>

3.092 RT DATE_UCI,VOL

> **NOTE:** You already have the 'RT DATE_UCI,VOL' File.

Shall I write over the existing Data Definition? YES// \<RET\>

3.094 RT RAWDATA

> **NOTE:** You already have the 'RT RAWDATA' File.

Shall I write over the existing Data Definition? YES// \<RET\>

15 DUPLICATE RECORD

> **NOTE:** You already have the 'DUPLICATE RECORD' File.

15.1 DUPLICATE RESOLUTION

> **NOTE:** You already have the 'DUPLICATE RESOLUTION' File.

8980 KERMIT HOLDING

> **NOTE:** You already have the 'KERMIT HOLDING' File.

Shall I write over the existing Data Definition? YES// \<RET\>

8984.1 LOCAL KEYWORD

> **NOTE:** You already have the 'LOCAL KEYWORD' File.

Shall I write over the existing Data Definition? YES// \<RET\>

Example of an Init done at the San Francisco ISC (continued):

8984.2 LOCAL SHORTCUT

> **NOTE:** You already have the 'LOCAL SHORTCUT' File.

Shall I write over the existing Data Definition? YES// \<RET\>

8984.3 LOCAL SYNONYM

> **NOTE:** You already have the 'LOCAL SYNONYM' File.

Shall I write over the existing Data Definition? YES// \<RET\>

8984.4 LOCAL LOOKUP

> **NOTE:** You already have the 'LOCAL LOOKUP' File.

Shall I write over the existing Data Definition? YES// \<RET\>

8991 XTV ROUTINE CHANGES

> **NOTE:** You already have the 'XTV ROUTINE CHANGES' File.

Shall I write over the existing Data Definition? YES// \<RET\>

8991.19 XTV VERIFICATION PACKAGE

> **NOTE:** You already have the 'XTV VERIFICATION PACKAGE' File.

Shall I write over the existing Data Definition? YES// \<RET\>

8991.2 XTV GLOBAL CHANGES

> **NOTE:** You already have the 'XTV GLOBAL CHANGES' File.

Shall I write over the existing Data Definition? YES// \<RET\>

SHALL I WRITE OVER FILE SECURITY CODES? NO// Y\<RET\> (YES)

> **NOTE:** This package also contains BULLETINS

SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains FUNCTIONS

SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains HELP FRAMES

SHALL I WRITE OVER EXISTING HELP FRAMES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<RET\> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y\<RET\> (YES)

Example of an Init done at the San Francisco ISC (continued):

...HMMM, LET ME THINK ABOUT THAT A MOMENT......................................

.

...............................................................................

.

......................

'XDR ADD VERIFIED' Help Frame filed.

'XDR AUTO MERGE' Help Frame filed.

'XDR CHECK PAIR' Help Frame filed.

'XDR DUP ALGORITHM' Help Frame filed.

'XDR DUP RESOLUTION FILE CONT' Help Frame filed.

'XDR DUPLICATE RECORD LISTINGS' Help Frame filed.

'XDR DUPLICATE RESOLUTION FILE' Help Frame filed.

'XDR EDIT DUP RESOLUTION FILE' Help Frame filed.

'XDR IDENTIFY' Help Frame filed.

'XDR IDENTIFY CONTINUE' Help Frame filed.

'XDR IDENTIFY METHODS' Help Frame filed.

'XDR MERGE PROCESS' Help Frame filed.

'XDR MERGE SELECTED PAIR' Help Frame filed.

'XDR MERGE VERIFIED DUPLICATES' Help Frame filed.

'XDR PRINTLIST' Help Frame filed.

'XDR PURGE' Help Frame filed.

'XDR VERIFY ALL' Help Frame filed.

'XDR VERIFY SELECTED PAIR' Help Frame filed.

'XURTL RESPONSE TIME LOG' Help Frame filed....

'XDR ERROR' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'XDR MERGED' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'XDR VERIFIED' BULLETIN FILED -- Remember to add mail groups for new bulletins.

.

...............................................................................

.

.

'XDR ADD VERIFIED DUPS' Option Filed

'XDR AUTO MERGE' Option Filed

'XDR CHECK PAIR' Option Filed

'XDR DISPLAY SEARCH STATUS' Option Filed

'XDR EDIT DUP RECORD STATUS' Option Filed

'XDR EDIT DUP RESOLUTION FILE' Option Filed

'XDR FIND POTENTIAL DUPLICATES' Option Filed

'XDR MAIN MENU' Option Filed

'XDR MANAGER UTILITIES' Option Filed

'XDR MERGE READY DUPLICATES' Option Filed

'XDR MERGE SELECTED PAIR' Option Filed

'XDR OPERATIONS MENU' Option Filed

'XDR PRINT LIST' Option Filed

'XDR PURGE' Option Filed

'XDR SEARCH ALL' Option Filed

'XDR TALLY STATUS FIELDS' Option Filed

Example of an Init done at the San Francisco ISC (continued):

'XDR UTILITIES MENU' Option Filed

'XDR VERIFY ALL' Option Filed

'XDR VERIFY SELECTED PAIR' Option Filed

'XDR VIEW DUPLICATE RECORD' Option Filed

'XT-KERMIT EDIT' Option Filed

'XT-KERMIT MENU' Option Filed

'XT-KERMIT RECEIVE' Option Filed

'XT-KERMIT SEND' Option Filed

'XT-NUMBER BASE CHANGER' Option Filed

'XT-OPTION TEST' Option Filed

'XT-ROUTINE COMPARE' Option Filed

'XT-VARIABLE CHANGER' Option Filed

'XT-VERSION NUMBER' Option Filed

'XTCM DISK2MAIL' Option Filed

'XTCM MAIN' Option Filed

'XTFCE' Option Filed

'XTFCR' Option Filed

'XTLKLKUP' Option Filed

'XTLKMODKY' Option Filed

'XTLKMODPARK' Option Filed

'XTLKMODPARS' Option Filed

'XTLKMODSH' Option Filed

'XTLKMODSY' Option Filed

'XTLKMODUTL' Option Filed

'XTLKPRTUTL' Option Filed

'XTLKUSER2' Option Filed

'XTLKUTILITIES' Option Filed

'XTMENU' Option Filed

'XTMOVE' Option Filed

'XTMOVE-IN' Option Filed

'XTOOLS' Option Filed

'XTQUEUABLE OPTIONS' Option Filed

'XTRDEL' Option Filed

'XTRGRPE' Option Filed

'XTSUMBLD' Option Filed

'XTSUMBLD-CHECK' Option Filed

'XTV EDIT VERIF PACKAGE' Option Filed

'XTV MENU' Option Filed

'XTVG COMPARE' Option Filed

'XTVG UPDATE' Option Filed

'XTVR COMPARE' Option Filed

'XTVR MENU' Option Filed

'XTVR MOST RECENT CHANGE DATE' Option Filed

'XTVR RESTORE PREV ROUTINE' Option Filed

'XTVR UPDATE' Option Filed

'XU FIRST LINE PRINT' Option Filed

'XUINDEX' Option Filed

'XUINDEX2' Option Filed

'XUPR RTN EDIT' Option Filed

'XUPR-ROUTINE-TOOLS' Option Filed

'XUPR-RTN-TAPE-CMP' Option Filed

Example of an Init done at the San Francisco ISC (continued):

'XUPRGL' Option Filed

'XUPRROU' Option Filed

'XUROUTINE IN' Option Filed

'XUROUTINE OUT' Option Filed

'XUROUTINES' Option Filed

'XURTL' Option Filed

'XURTLC' Option Filed

'XURTLCK' Option Filed

'XURTLK' Option Filed

'XURTLM' Option Filed

'XURTLMA' Option Filed

'XURTLP' Option Filed

'XURTLPG' Option Filed

'XURTLPL' Option Filed.........................................

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

#### Installing/Configuring the VAX/Alpha Performance Monitor (VPM)

> **NOTE:** At this point, VAX/Alpha Sites only see the following (MSM sites may skip this portion of the dialogue):

Will now install the VAX/Alpha Performance Monitor (VPM)

This version (#7.3) of 'XUCINIT' was created on 03-APR-1995

(at NXT, by VA FileMan V.20.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

8986.095 CM SITE PARAMETERS

> **NOTE:** You already have the 'CM SITE PARAMETERS' File.

8986.098 CM BERNSTEIN DATA

> **NOTE:** You already have the 'CM BERNSTEIN DATA' File.

8986.3 CM SITE NODENAMES

> **NOTE:** You already have the 'CM SITE NODENAMES' File.

8986.35 CM SITE DISKDRIVES

> **NOTE:** You already have the 'CM SITE DISKDRIVES' File.

8986.4 CM METRICS (including data)

> **NOTE:** You already have the 'CM METRICS' File.

I will OVERWRITE your data with mine.

8986.5 CM DISK DRIVE RAW DATA

> **NOTE:** You already have the 'CM DISK DRIVE RAW DATA' File.

8986.51 CM NODENAME RAW DATA

> **NOTE:** You already have the 'CM NODENAME RAW DATA' File.

8986.6 CM DAILY STATISTICS

> **NOTE:** You already have the 'CM DAILY STATISTICS' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// Y \<RET\> (YES)

> **NOTE:** This package also contains BULLETINS

SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

Installing/Configuring the VPM (continued):

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<RET\> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y\<RET\> (YES)

Starting pre-init...

The ^XUCM global will now be synchronized with VPM file numbers

8986.095...DONE

8986.098...DONE

8986.3...DONE

8986.35...DONE

8986.4...DONE

8986.5...DONE

8986.51...DONE

8986.6...DONE

...HMMM, LET ME THINK ABOUT THAT A MOMENT......................................

.

..................

'XUCMBRTL' BULLETIN FILED -- Remember to add mail groups for new bulletins.....

.

......................................

'XUCM ANALYSE' Option Filed

'XUCM COMPUTE LOCAL REFERENCES' Option Filed

'XUCM DISK' Option Filed

'XUCM DISK RAW' Option Filed

'XUCM DSK IO' Option Filed

'XUCM DSK QUE' Option Filed

'XUCM EDIT DISK THRESHOLD' Option Filed

'XUCM EDIT REF THRESH' Option Filed

'XUCM EDIT VOL SET THRESH' Option Filed

'XUCM GRAF DSK IO' Option Filed

'XUCM GRAF DSK QUE' Option Filed

'XUCM GRAF MET AVE' Option Filed

'XUCM LIST DAILY STATS' Option Filed

'XUCM LIST RAW' Option Filed

'XUCM LIST VOL SET INFO' Option Filed

'XUCM LOCKS' Option Filed

'XUCM MAIN' Option Filed

'XUCM MODES' Option Filed

'XUCM ON/OFF' Option Filed

'XUCM PA' Option Filed

'XUCM PAGE' Option Filed

'XUCM PERFORMANCE MONITOR' Option Filed

'XUCM PURGE' Option Filed

'XUCM RAW RTHIST DATA' Option Filed

'XUCM REPORTS' Option Filed

Installing/Configuring the VPM (continued):

'XUCM SERVER' Option Filed

'XUCM SET ALERTS' Option Filed

'XUCM SETUP' Option Filed

'XUCM TASK MAIN' Option Filed

'XUCM TASK NIT' Option Filed

'XUCM TASK VPM' Option Filed

'XUCMBR MENU' Option Filed

'XUCMBR2' Option Filed

'XUCMBR2A' Option Filed

'XUCMBR2B' Option Filed

'XUCMBR2C' Option Filed

'XUCPFORMATTED' Option Filed

'XUCPKILL' Option Filed

'XUCPMENU' Option Filed

'XUCPRAWPRINT' Option Filed

'XUCPSORT' Option Filed

'XUCPTOGGLE' Option Filed.................................

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

The CM METRICS file (#8986.4) is shipped with data. The metric names should not be modified.

The post-init allows you to configure the performance monitor for alpha systems.

Do not attempt to configure VPM at this point if you have not yet set up

TaskMan to run in DCL mode. The option, Setup Performance Monitor

allows you to configure VPM later.

\<\<BEGINNING VPM POST-INIT\>\>

This post-init will allow you to review and update your

VPM site file entries. Taskman will also install new VMS com files

in your VPM host directory.

TASKMAN MUST BE RUNNING FROM A DCL CONTEXT TO COMPLETE THIS STEP.

YOU CAN '^' OUT NOW IF THIS IS NOT THE CASE.

Note that VPM also requires a HFS device, SYS\$INPUT, and XUCM RESOURCE.

IF YOU EXIT NOW, RUN THE OPTION, 'SETUP PERFORMANCE MONITOR'

LATER.

The routine ^XUCMTM was written to assist with setting up Taskman

to run from DCL. Make sure you have SYSPRV and OPER before attempting

to run this routine.

This routine allows you to define the site file parameters

needed to run VPM, then instructs taskman to create the

host system directories for data files and system-specific

command procedures.

Installing/Configuring the VPM (continued):

Select CM SITE PARAMETERS:

ANSWER WITH CM SITE PARAMETERS:

ISC SAN FRANCISCO

YOU MAY ENTER A NEW CM SITE PARAMETERS, IF YOU WISH

ANSWER WITH INSTITUTION NAME

Select CM SITE PARAMETERS: ISC SAN FRANCISCO CALIFORNIA 16000

...OK? YES// \<RET\> (YES)

SITE: ISC SAN FRANCISCO// \<RET\>

CMP HOST FILE PATH: USER\$:\[CMP\]// \<RET\>

MONITOR ENABLED/DISABLED: ENABLED// \<RET\>

HFS DEVICE: HFS// \<RET\>

DAYS TO KEEP RAW DATA: 90// \<RET\>

DAYS FOR COMPUTING REFERENCES: ??

This field is used to control your local reference mean and standard

deviation. For example, if 90 is entered, then each evening your reference

range will be re-computed based on the previous 90 days. This 90-day

moving average is maintained by hardware-type in the CM METRICS file. In

this scenario, current data will always be compared with the last 90 days,

regardless of how well the system performed during that period. If this

field is blank, no updating will occur. If you enter '999', ALL data will

be used. Suggested usage: If your system appears to be functioning

normally, enter 999 to include all data until the standard deviation

appears to be stable and you are within 2 standard deviations of the VA

reference mean. After a reasonable period of monitoring, set this field to

null to 'fix' your reference ranges on a period that you consider 'normal'

for that hardware. Your local standard deviation should be considerably

smaller than those published by the VA and should be particularly useful

for monitoring the affect of tuning or capacity changes.

DAYS FOR COMPUTING REFERENCES: 999

MAILGROUP FOR REPORTS/ALERTS: VPM// \<RET\>

MAILGROUP FOR REMOTE XMITS: VPM// \<RET\>

DAYS TO KEEP DAILY AVERAGES: 999// \<RET\>

DAYS TO KEEP BRTL DATA: 365// \<RET\>

THRESHOLD (%) DSM BLOCKS FREE: 5// ??

This field will be referenced each evening to determine if there is

sufficient space remaining in your volume sets. If the PERCENTAGE of DSM

blocks free drops below this threshold for a VOLUME *SET* an alert will be

fired.

THRESHOLD (%) DSM BLOCKS FREE: 5// \<RET\>

CONFIGURATION: LAVC// \<RET\>

CRT's IN SERVICE: 3// \<RET\>

PRINTERS IN SERVICE: 15// \<RET\>

NETWORKED WORKSTATIONS: 38// \<RET\>

STANDALONE WORKSTATIONS: 20// \<RET\>

HSC NAME(S): \<RET\>

Installing/Configuring the VPM (continued):

NETWORK TOPOLOGY: \<RET\>

Edit? NO// \<RET\>

Select CM SITE NODENAMES: ISC

1 ISC6V0

2 ISC6V2

3 ISC6V4

CHOOSE 1-3: 1

NODENAME: ISC6V0// \<RET\>

*NOTE: If you have already defined all nodes in version 7.2, be sure to update the new fields under this multiple for each node. The following information is required:*

NODE-SPECIFIC BATCH QUEUE: ISC6V0\$BATCH// ??

Enter a node-specific batch queue for each node in this

configuration. You must be running the 'SETUP...' option when defining

this entry. If batch queues are defined for ALL nodes, com files will be

built that submit jobs to these queues rather than using SYSMAN. An

example of such a queue would be DSM\$BATCH\_\<nodename\>. For example:

ISC6V0: sho que/full dsm\$batch_isc6v0

Batch queue DSM\$BATCH_ISC6V0, idle, on ISC6V0::

/BASE_PRIORITY=4 /JOB_LIMIT=1 /OWNER=\[SYSTEM\]

/PROTECTION=(S:E,O:D,G:R,W:W)

or

ISC6V0: sho que/full sys\$batch

Batch queue ISC6V0\$BATCH, available, on ISC6V0::

/BASE_PRIORITY=4 /JOB_LIMIT=15 /OWNER=\[SYSTEM\]

/PROTECTION=(S:E,O:D,G:R,W:RW)

If Taskman is configured to run from a dcl context, you may enter the

queue TM\$nodename.

NODE-SPECIFIC BATCH QUEUE: ISC6V0\$BATCH// \<RET\>

USERNAME: TASKMAN// ??

Enter the name of a VMS user, such as TASKMAN, which has been

previously added to UAF with sufficient privileges.

USERNAME: TASKMAN// \<RET\>

Installing/Configuring the VPM (continued):

DSM ENVIRONMENT MANAGER: ISCMGR// ??

The DSM ENVIRONMENT name will be that which is entered when

logging into DSM. The name itself follows 'DSM/ENVIRONMENT=', ie,

\$ dsm/environment=ABCMGR

If running taskman from a DCL context, this was defined in the

TASKMAN SITE PARAMETERS as well. This field will be used by taskman when

starting new RTHIST sessions.

DSM ENVIRONMENT MANAGER: ISCMGR// \<RET\>

Select CM SITE NODENAMES: \<RET\>

Requested Start Time: NOW// \<RET\>

One moment while I check/clean up MTLU variable pointers.

Done...

TO PROTECT THE SECURITY OF DHCP SYSTEMS, DISTRIBUTION OF THIS

SOFTWARE FOR USE ON ANY OTHER COMPUTER SYSTEM IS PROHIBITED.

ALL REQUESTS FOR COPIES OF THE KERNEL FOR NON-DHCP USE SHOULD

BE REFERRED TO YOUR LOCAL ISC.

VAH,MTL\>

If the VPM global conversion fails for any reason, it can be re-started by executing the routine, ^XUCINIT.

Using the TaskMan option, Schedule/Unschedule Options \[ZTMSCHEDULE\], queue XUCM TASK VPM to run hourly. This option is the data collection driver for the VMS monitor and checks for and loads new data into the CM DISK DRIVE RAW DATA (#8986.5) and CM NODENAME RAW DATA (#8986.51) files.. Each data collection runs for 15 minutes. Queue the option XUCM TASK NIT to run in the early AM, (e.g., 0001 hours). This option compiles workday averages, mail server messages, and collects "static" information such as node and hardware types. Finally, this option files selected RTHIST data and restarts RTHIST data collections for the next 24 hours.

#### Installing/Configuring the MSM Performance Monitor (MPM)

> **NOTE:** MSM Sites see the following dialogue as the MSM Performance Monitor is installed:

This version (#7.3) of 'XUCSINIT' was created on 18-MAY-1994

(at CLARKSBURG 998, by VA FileMan V.20.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

8987.1 MSM RTHIST SITE

> **NOTE:** You already have the 'MSM RTHIST SITE' File.

8987.2 MSM RTHIST REPORT DATA

> **NOTE:** You already have the 'MSM RTHIST REPORT DATA' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES//

\<RET\> (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<RET\> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y\<RET\> (YES)

...EXCUSE ME, HOLD ON..........................................................

'XUCS MANAGER MENU' Option Filed

'XUCS MANUAL PURGE OF DATA' Option Filed

'XUCS REPORTS BY (DATE,VG)' Option Filed

'XUCS SITE EDIT' Option Filed

'XUCS SITE EDIT MENU' Option Filed

'XUCS SYS CONFIG PARMS DISPLAY' Option Filed

'XUCS VOL GROUP EDIT' Option Filed

'XUCSR REPORTS MENU' Option Filed

'XUCSRA CPU/DISK REPORT' Option Filed

'XUCSRA GREF REPORT' Option Filed

'XUCSRA REPORTS BY (VG,DATE)' Option Filed

'XUCSRA RESPONSE REPORT' Option Filed

'XUCSRA ROU CMNDS/GREF REPORT' Option Filed

'XUCSRA SYS STAT REPORT' Option Filed

'XUCSRB CPU/DISK REPORT' Option Filed

'XUCSRB GREF REPORT' Option Filed

'XUCSRB REPORTS BY (DATE,VG)' Option Filed

'XUCSRB RESPONSE REPORT' Option Filed

'XUCSRB ROU CMNDS/GREF REPORT' Option Filed

'XUCSRB SYS STAT REPORT' Option Filed

'XUCSRG CPU-DISK GRAPH' Option Filed

'XUCSRG GRAPHS MENU' Option Filed

'XUCSRG RESPONSE TIME GRAPH' Option Filed

'XUCSTASK AM RTHIST' Option Filed

Installing/Configuring the MPM (continued):

'XUCSTASK FILE UPDATE AUTO' Option Filed

'XUCSTASK PM RTHIST' Option Filed

'XUCSTASK PURGE CM DATA' Option Filed...

OK, I'M DONE.

NO SECURITY-CODE PROTECTION HAS BEEN MADE

One moment while I check/clean up MTLU variable pointers.

Done...

TO PROTECT THE SECURITY OF DHCP SYSTEMS, DISTRIBUTION OF THIS

SOFTWARE FOR USE ON ANY OTHER COMPUTER SYSTEM IS PROHIBITED.

ALL REQUESTS FOR COPIES OF THE KERNEL FOR NON-DHCP USE SHOULD

BE REFERRED TO YOUR LOCAL ISC.

NXT,KDE\>

Configuration of the MSM Performance Monitor

The following steps are needed to complete configuration of the MSM performance monitor:

1\. Distribute the following routines to the remaining COMPUTE and PRINT SERVERS:

> XUCS\*

> -XUCSI\*

> ZOSV2MSM

> Rename ZOSV2MSM to %ZOSV2

2\. Move ZOSV2MSM to the MGR UCI of the File Server(s) and rename it to %ZOSV2.

3\. Edit the MSM Site Parameters using the MSM Site Parameters Enter/Edit Menu option:

> a\. Edit MSM CM Site Parameters

> Select MSM Capacity Management Manager's Menu Option: ?

> CM Reports Menu ...

> Manually Purge CM Data

> MSM Site Parameters Enter/Edit Menu ...

> Select MSM Capacity Management Manager's Menu Option: MSM Site Parameters Enter/Edit Menu

> Select MSM Site Parameters Enter/Edit Menu Option: ?

> 1 Edit MSM CM Site Parameters

> 2 Enter/Edit Volume Group (Node)

> 3 Print/Display System Configuration Parameters

> Select MSM Site Parameters Enter/Edit Menu Option: 1 Edit MSM CM Site Parameters

> Select MSM RTHIST SITE SITE NAME: ???

> This is the name of your site. For example: SAN FRANCISCO VAMC

> Select MSM RTHIST SITE SITE NAME: CLARKSBURG VAMC

> ARE YOU ADDING 'CLARKSBURG VAMC' AS A NEW MSM RTHIST SITE (THE 1ST)? Y\<RET\> (YES)

> SITE NAME: CLARKSBURG VAMC// \<RET\>

> SITE NUMBER: 540 ???

> This is your station number. For example, 662

> SITE NUMBER: 540 \<RET\>

MSM Site Parameters Enter/Edit Menu (continued):

> DFLT ROU NAME LENGTH: ???

> This is a required field that is used by the Routine Report so

> that routines can be grouped by name. For example, if you enter a

> "3", then routine commands and routine global accesses will be grouped

> together by the first 3 characters of their name.

> DFLT ROU NAME LENGTH: 4

> DFLT GBL NAME LENGTH: ???

> This is a required field that is used by the Global Report so

> that global accesses can be grouped. For example, if you enter a "3",

> then the global names will be grouped together by the first 3

> characters of their name.

> DFLT GBL NAME LENGTH: 4

> \<thresh ROU CMDS/SEC: ???

> Some DHCP routines are executed very briefly. Therefore, the

> number of commands they execute are relativity very small for a RTHIST

> session. A "bucket" called '\<thresh' in the Routine command report is

> where all command counts for these types of routine(s) will be

> collected. For example, if routine ABC executes 976 commands for a

> RTHIST session and you specify 1000 as the thresh hold value, then

> ABC's command count will be placed in the '\<thresh' bucket.

> \<thresh ROU CMDS/SEC: 100

> \<thresh GBL GREFS/SEC: ???

> Some DHCP routines reference global(s) very little. Therefore,

> the number of global references are relativity very small for a RTHIST

> session. A "bucket" called '\<thresh' in the Global Access report is

> where all these type of global(s) will get placed. For example, if

> global ABC is referenced 109 times for a RTHIST session and you

> specify 300 as the threshold, the ABC's reference count will be placed

> in the '\<thresh' bucket.

> \<thresh GBL GREFS/SEC: ?

> Type a Number between 0 and 999999, 0 Decimal Digits

> \<thresh GBL GREFS/SEC: 100

> DAYS TO KEEP DATA: ???

> This field represents the number of days data will be kept in

> File \#8987.2. If NULL, then 45 days is the used for the default.

> DAYS TO KEEP DATA: \<RET\>

> Select LOCAL CMP RECIPIENTS: DOE,JOHN

> Select LOCAL CMP RECIPIENTS: \<RET\>

> Select REMOTE CMP RECIPIENTS: *(NOTE: Optional. You may be requested to send data to your ISC. If so, enter a mail group containing at least your ISC as a remote recipient.)*

> Select MSM RTHIST SITE SITE NAME: \<RET\>

> b\. Enter/Edit Volume Group (Node)

> Select MSM Site Parameters Enter/Edit Menu Option: 2 Enter/Edit Volume Group (Node)

> Select MSM RTHIST SITE SITE NAME: \`1 CLARKSBURG VAMC

> Select VOL GROUP (NODE): PSA

> ARE YOU ADDING 'PSA' AS A NEW VOL GROUP (NODE) (THE 1ST FOR THIS MSM RTHIST SITE)? Y \<RET\> (YES)

> SERVER TYPE: Print

> NAME OF MANAGER UCI: MGR

> NAME OF PRODUCTION UCI: VAH

> AUTO ADJUST RTHIST TABLE SIZE: ???

> Leave this field blank to AUTOMATICALLY ADJUST THE RTHIST TABLE

> SIZE. When the RTHIST job is started, it requires the number of

> table entries to be specified. If the entry for table size is too

> small, then a ~TABLE,FULL~ condition will occur. If you define this

> field (i.e. Not Null), then I will use this value for the MAXIMUM

> RTHIST table size. On the other hand, if you leave this field Null,

> then I will use the MAX AM TABLE SIZE field (#6) to adjust the AM

> RTHIST table size for the morning RTHIST session, or the MAX PM TABLE

> SIZE field (#7) to adjust the PM RTHIST table size for the afternoon

> RTHIST session.

> AUTO ADJUST RTHIST TABLE SIZE: \<RET\>

> Select MSM RTHIST SITE SITE NAME: CLARKSBURG VAMC \<RET\>

> Select VOL GROUP (NODE): PSA// CSA

> ARE YOU ADDING 'CSA' AS A NEW VOL GROUP (NODE) (THE 2ND FOR THIS MSM RTHIST SITE)? Y \<RET\> (YES)

> SERVER TYPE: Compute

> NAME OF MANAGER UCI: MGR

> NAME OF PRODUCTION UCI: VAH

> AUTO ADJUST RTHIST TABLE SIZE: \<RET\>

> **NOTE:** Repeat this procedure for all other CPUs except the shadow servers.

4\. Using the TaskMan option, Schedule/Unschedule Options \[ZTMSCHEDULE\], schedule the following options:

> XUCSTASK AM RTHIST

> XUCSTASK PM RTHIST

> XUCSTASK FILE UPDATE AUTO

> XUCSTASK PURGE CM DATA

> AM MSM RTHIST Task Option

NAME: XUCSTASK AM RTHIST MENU TEXT: AM MSM RTHIST Task Option

TYPE: run routine CREATOR: POSTMASTER

PACKAGE: MSM CAPACITY MANAGEMENT

DESCRIPTION: This option is scheduled thru TaskMan's \[ZTMSCHEDULE\] for the morning RTHIST data capture. It should be setup for a 1D rescheduling frequency. NO output device is necessary.

ROUTINE: XUCSTM

QUEUED TO RUN AT WHAT TIME: MAY 3, 1994@08:30

RESCHEDULING FREQUENCY: 1D SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: AM MSM RTHIST TASK OPTION

> PM MSM RTHIST Task Option

NAME: XUCSTASK PM RTHIST MENU TEXT: PM MSM RTHIST Task Option

TYPE: run routine CREATOR: POSTMASTER

PACKAGE: MSM CAPACITY MANAGEMENT

DESCRIPTION: This option is scheduled thru TaskMan's \[ZTMSCHEDULE\] for the afternoon RTHIST data capture. It should be setup as 1D rescheduling frequency. No output device is necessary.

ROUTINE: XUCSTM

QUEUED TO RUN AT WHAT TIME: MAY 2, 1994@14:30

RESCHEDULING FREQUENCY: 1D SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: PM MSM RTHIST TASK OPTION

> Tasked CM File Update

NAME: XUCSTASK FILE UPDATE AUTO MENU TEXT: Tasked CM File Update

TYPE: run routine CREATOR: POSTMASTER

PACKAGE: MSM CAPACITY MANAGEMENT

DESCRIPTION: This option is scheduled thru TaskMan's \[ZTMSCHEDULE\]. It gathers the data from each Vol. Group defined in the MSM Site Parameters file. It first transfers the PREVIOUS day's ^RTHIST data to the %ZRTL("XUCS", nodes. It then formats the data into FileMan compatible data, moving the data into the MSM RTHIST Data file. Finally, it creates a server message to transmit a summary of the PREVIOUS day's data to the National Data Base. It should be setup with a 1 DAY rescheduling frequency. No output device is necessary, but you might want to consider using a RESOURCE device, so that option XUCSTASK PURGE CM DATA falls after this option.

ROUTINE: XUCSTME

QUEUED TO RUN AT WHAT TIME: MAY 3, 1994@01:00

DEVICE FOR QUEUED JOB OUTPUT: ZZRES;;132;66

RESCHEDULING FREQUENCY: 1D SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: TASKED CM FILE UPDATE

> Auto Purge of CM Data;

NAME: XUCSTASK PURGE CM DATA MENU TEXT: Auto Purge of CM Data

TYPE: run routine CREATOR: POSTMASTER

PACKAGE: MSM CAPACITY MANAGEMENT

DESCRIPTION:

This is the schedulable TaskMan option to purge data from the MSM RTHIST Data file . A selectable range of days to keep old data is in the SITE file. If this is not filled in 45 days is the default. It is recommended to schedule this option so that it is run AFTER the option XUCSTASK FILE UPDATE AUTO. No output device is necessary, but might want to consider using a RESOURCE device for ease of scheduling.

ROUTINE: DEQUE^XUCSPRG

QUEUED TO RUN AT WHAT TIME: MAY 3, 1994@03:00

DEVICE FOR QUEUED JOB OUTPUT: ZZRES;;132;66

RESCHEDULING FREQUENCY: 1D SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: AUTO PURGE OF CM DATA

> NOTE: Any RTHIST that is *running* when either the AM or PM RTHIST is started will be stopped, as if it were stopped using the RTHIST - TERMINATE (SAVE).

> Any RTHIST that is *scheduled* during the time period (1 hour) that is a

> scheduled AM or PM RTHIST will be unscheduled.

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>• <u>In MGR</u>: Map routines in the Manager account.</strong></p>
<blockquote>
<p>The recommended set is listed below:</p>
<p>%ZOSV</p>
<p>%ZOSV1</p>
<p>%ZOSV2</p>
<p>The following advisory is recommended:</p>
<p>• At a future time, you should review RTHIST data to identify the set of routines that are used most frequently at your site. The set provided here is only a "best guess" of which routines might be worth mapping.</p>
<p>• To avoid potential problems, do not map %ZOSV if you are running a version of VAX DSM less than V6.</p>
</blockquote></td>
<td><p><em>DSM FOR OpenVMS</em></p>
<p>Edit your command file for building mapped routine sets, then run it.</p>
<p><em>MSM and M/SQL</em></p>
<p>Not Applicable</p></td>
</tr>
</tbody>
</table>

### Shutdown DSM and Restart to Activate Mapped Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>• Shutdown and restart DSM</strong></p>
<blockquote>
<p>Restart the configuration to activate the new set of mapped routines.</p>
</blockquote></td>
<td><p><em>DSM for OpenVMS</em></p>
<p>Shut down and restart the configuration:</p>
<p><strong>$ DSM/MAN ^SHUTDWN</strong></p>
<p>and then</p>
<p><strong>$ DSM/MAN ^STU</strong></p>
<p><em>MSM and M/SQL</em></p>
<p>(Routine mapping is not applicable)</p></td>
</tr>
</tbody>
</table>

### On the Other Toolkit V. 7.2 CPUs (MSM and M/SQL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Steps that can be taken while inits run on the first CPU

• Review the steps taken on the first CPU and repeat those that apply.

• <u>In VAH</u>: Load all Toolkit V. 7.3 routines on this CPU, as you did on the first CPU.

> Save the ZU routine corresponding to the current operating system. Move the relevant (Z\*) routines to the Manager’s account as on the first CPU. Recall that MANAGER (%) routines for Kernel and FileMan were moved to *all* MSM CPUs in preparation for the MSM Performance Monitor.• <u>In MGR</u>: Run TOOLKIT^ZTMGRSET as on the first CPU.

• <u>In VAH</u>: If the CPU runs a different MUMPS operating system, use the Reinitialize option on the VA FileMan Management Menu to identify the CPU’s operating system, and thus, set the second piece of ^%ZOSF("OS") correctly. (NOTE: This menu is locked with the XUMGR key.) This step is necessary since, if ^DD is translated, ^DD("OS", a pointer to the MUMPS OPERATING SYSTEM file (#.7), indicates the operating system of the CPU where the DINIT was run.

#### After the inits have finished (VAX/Alpha)

• Map routines: For DSM for OpenVMS systems, rebuild the mapped routine set. Map routines in the Manager and Production accounts as on the first CPU. Remember to activate the new mapped routine sets.

### Delete Inits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• <u>In VAH</u>: Optionally, delete the Toolkit init routines XUCIN\*, XUCSI\*, XTIN\* using the ^%ZTRDEL utility to delete groups of routines.

### Clear Obsolete Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines have been identified as obsolete (no longer exported by the Toolkit). Please review against your own records and confirm that they are obsolete at your site before deleting them:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ZOSFM11</p>
<p>ZOSVM11</p>
<p>ZTBKCM11</p>
</blockquote></td>
<td><blockquote>
<p>ZTCPU</p>
<p>ZTRTHM</p>
<p>ZTRTHT</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### Clear Unused Routines from the Production Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After running the Toolkit installation, the following routines may be deleted from the Production account where they were initially loaded (or any other Production account where they may have been loaded in the past):

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ZO*</p>
<p>ZTBK*</p>
<p>ZTEDIT*</p>
<p>ZTGBL</p>
</blockquote></td>
<td><blockquote>
<p>ZTMGRSET</p>
<p>ZTP1</p>
<p>ZTPP</p>
<p>ZTRDEL</p>
</blockquote></td>
<td><blockquote>
<p>ZTSYINIT</p>
</blockquote></td>
</tr>
</tbody>
</table>

These routines may be deleted since, during the initialization process, they were saved to the Manager account where they become operative.

### Install the VAX/ALPHA VMS EDT or TPU Text Editor (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites running DSM for OpenVMS may choose to install the VMS EDT and/or TPU text editors. This is accomplished by making an entry in the ALTERNATE EDITOR file (#1.2) as shown here.

\>D Q^DI This entry point may be used to maintain device handler variables.

VA FileMan 20

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 1.2 ALTERNATE EDITOR (2 entries)

EDIT WHICH FIELD: ALL// \<RET\>

Select ALTERNATE EDITOR: VMSEDT

ARE YOU ADDING 'VMSEDT' AS A NEW ALTERNATE EDITOR (THE 3RD)? Y (YES)

ACTIVATION CODE FROM DIWE: G ^XTEDTVXD (for the EDT editor)

ACTIVATION CODE FROM DIWE: G TPU^XTEDTVXD (for the TPU editor)

OK TO RUN TEST: I ^%ZOSF("OS")\["VAX"

RETURN TO CALLING EDITOR: \<RET\>

DESCRIPTION:

1\> Call to VAX/ALPHA VMS EDT editor to process VA FileMan word-processing fields.\<RET\>

2\> Creates a temporary VMS file in the default directory with a name \<RET\>

3\> of 'DIWE\$'\_\$JOB\_'.TMP'. This version will remove the two copies\<RET\>

4\> of the file that EDT leaves behind.\<RET\>

5\> \<RET\>

EDIT Option: \<RET\>

Select ALTERNATE EDITOR: \<RET\>

### Install the Kermit Protocol (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kermit may be added to the ALTERNATE EDITOR file (#1.2) as shown. This allows the transfer of files from a PC, or other system, into a mail message or other VA FileMan word-processing field. Be sure that the file to be sent is in text-only format. Be sure that if a DEC server is involved, its break character is not a printable character, like ~, since Kermit uses all the printable characters when processing.

The benefit of using the Kermit file transfer protocol is that large files can be sent faster and more easily due to the efficient Kermit error checking mechanism.

\>D Q^DI This entry point may be used to maintain device handler variables.

VA FileMan 20

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 1.2 \<RET\> ALTERNATE EDITOR (3 entries)

EDIT WHICH FIELD: ALL// \<RET\>

Select ALTERNATE EDITOR: KERMIT LOAD

ARE YOU ADDING 'KERMIT LOAD' AS A NEW ALTERNATE EDITOR (THE 4TH)? Y (YES)

ACTIVATION CODE FROM DIWE: S XTKDIC=DIC D RECEIVE^XTKERMIT

OK TO RUN TEST: \<RET\>

RETURN TO CALLING EDITOR: K XTKDIC

DESCRIPTION:

1\> This option uses the KERMIT protocol to load the word-processing field\<RET\>

2\> from another system. \<RET\>

### Bulletins Exported with Toolkit V. 7.3 (Not Associated with Mail Groups)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following three Bulletins are a part of the Duplicate Resolution Utilities exported with Toolkit V. 7.3. They do *not* come with a mail group. You may associate them with any mail group you like. They are listed as follows:

> XDR ERROR

> This bulletin is sent to a mail group of your choice when something in the merge process errors out, is missing, or simply did not complete. The following is a list of all reasons that can trigger the sending of XDR ERROR bulletins:

> • The Candidate Collection Routine is undefined.

> • The Candidate Collection Routine is not present.

> • The Potential Duplicate Threshold is undefined.

> • There are no Duplicate Tests entered for this Duplicate Resolution entry.

> • The Global root node in DIC is undefined.

> • No entry in DUPLICATE RESOLUTION (#15.1) file for this file.

> • The From and To Record are undefined.

> • The test routine is not present.

> • The routine defined as the Pre-Merge routine is not present.

> • The routine defined as the Post-Merge routine is not present.

> • The routine defined as the Verified Msg routine is not present.

> • The routine defined as the Merged Msg routine is not present.

> • You cannot have a "Non-Interactive" merge style with entries in the DINUM files multiple.

> • The file for checking duplicates is not defined (XDRFL).

> • The entry for checking duplicates is not defined (XDRCD).

> • The routine defined as the Merge Direction Input Transform routine is not present.

> • The *new* cross-reference has not been entered for this Duplicate Resolution entry.

> XDR MERGED

> This bulletin is a notification that all verified duplicate record pairs have been merged.

> XDR VERIFIED

> This bulletin is a notification that a pair of records have been verified as duplicates and are ready to be merged.

## ## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

ACL

Environment Access Utilities, 11

Alternate Editor, 61

ALTERNATE EDITOR file, 61, 62

AM MSM RTHIST Task Option, 52

Auto Purge of CM Data Option, 53

B

Batch Queues, verify created, 13

Bulletins, 63

C

CM DISK DRIVE RAW DATA file, 46

CM METRICS file, 43, 44

CM NODENAME RAW DATA file, 46

CM SITE PARAMETERS file, 13

COMPUTE SERVER

Mode of TaskMan, 17

Configuration of the MSM Performance Monitor (MPM), 49–53

Configuring TaskMan to run in a DCL Context, 10

D

DCL Context, 9, 10, 45, 46

DCL files, 9

DEVICE file, 14

Devices, 14

DINUM files

multiple, 63

DUPLICATE RESOLUTION file, 63

Duplicate Resolution Utilities, 63

E

Enter/Edit Volume Group (Node), 51

F

FAILED ACCESS ATTEMPT LOG file, 28

File/Shadow Servers, 15

G

REDACTED

Mail Group, 13

^%GDEL, 15

Global Placement, 7, 15

Global Protection, 1, 8, 15, 31

Global Translation, 15–16

H

HFS Device, 14

I

%INDEX, 6, 28, 30

Init

Example done at the San Francisco ISC, 35–39

Integrity Checking, 7, 22

K

K71PAT40.RTN file, 3

Kermit file transfer protocol, 62

Kernel 7.1 patch 40, 3, 4

KTK7_3.RTN file, 3

M

Mail Groups

REDACTED, 13

Manager Setup Routine

Example done at the San Francisco ISC, 29–30

Mapping Routines, 21, 54, 55, 57

Morning RTHIST Data Capture, 52

MSM Performance Monitor (MPM), 2, 7, 8, 15, 17, 51

Sample Install, 47–48

Multi-Term Look-Up (MTLU), 2, 7, 20, 48

MUMPS OPERATING SYSTEM file, 57

N

New Fields, 45

New Global

^XUCS, 2, 7, 8, 15, 32

New Mail Groups

REDACTED, 13

NTEG Routine, 7, 22

O

Obsolete Routines, 59

OPER

VMS Privileges, 9

P

Partition Size, 33

^%PARTSIZ, 33

PM MSM RTHIST Task Option, 52

PROGRAMMER MODE LOG file, 28

R

^%RD, 7

Routine Restore

Example done at the San Francisco ISC, 23–24

Routine Save

Example done at the San Francisco ISC, 26

RTHIST, 15, 46, 53, 54

S

Schedule/Unschedule options, 46, 51

Symbol Table Size, 19, 33

SYS\$INPUT Device, 14

SYSPRV

VMS Privileges, 9, 11

T

Tasked CM File Update Option, 53

TaskMan, 9–13, 15, 19, 43, 46, 51, 52, 53

TASKMAN SITE PARAMETERS file, 9, 17–18

Text Editor

TPU, 61

VMS EDT, 61

TOOLKIT^ZTMGRSET, 3, 28, 29, 57

TPU Text Editor, 61

U

UCI ASSOCIATION file, 17–18

Unused Routines, 3, 60

V

VAX/Alpha Performance Monitor (VPM), 2, 7, 9, 13, 41–46

Verify Created Batch Queues, 13

VMS EDT Text Editor, 61

VMS Privileges

OPER, 9

SYSPRV, 9, 11

VOLUME SET file, 17–18

X

XDR ERROR bulletins, 63

XDR MERGED bulletins, 64

XDR VERIFIED bulletins, 64

^XINDEX, 6

^XMB Global, 28

^XT, 2, 7, 8, 15, 32

^XTMP, 2

XTNTEG, 7, 22

^XUCINIT, 46

^XUCM, 2, 7, 8, 15, 32

XUCM TASK NIT, 20, 46

XUCM TASK VPM, 20, 46

^XUCMTM, 9

Example, 10

^XUCP, 2

^XUCS, 2, 7, 8, 15, 32

XUCSTASK AM RTHIST, 52

XUCSTASK FILE UPDATE AUTO, 53

XUCSTASK PM RTHIST, 52

XUCSTASK PURGE CM DATA, 53

XUMGR key, 57

XUPROG, 20

XUSITEMGR, 20

Z

^%Z editor, 28, 30

ZINDX\* Routines, 6

^%ZOSF, 3, 15, 16, 28, 29, 57, 61

%ZOSV, 3, 29, 54

ZOSV, 4

^%ZRTL, 31, 53

ZTBK, 4, 60

^ZTLOAD, 9

ZTMGRSET, 3, 4, 16, 26, 28, 29, 57, 59, 60

ZTMSCHEDULE, 46

^%ZTRDEL, 58

^%ZUA, 28