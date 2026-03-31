---
title: IVM Version 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: IVM
app_name: Income Verification Match
section: FIN
app_status: active
pkg_ns: IVM
patch_ver: 2
patch_id: IVM*2
group_key: "IVM:IVM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: This package contains all of the routines, files, and options necessary to support the Means Test verification process in conjunction with the IVM Center. Also included in this package are all required modifications to Patient Information Management System (PIMS) and Integrated Billing (IB) that are
audience: 
keywords: 
  - ivmin
  - filed
  - installation
  - protocol
  - blockquote
  - upload
  - routine
  - ibamtv
  - ivmld
  - test
page_count: 0
word_count: 2348
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Income_Verif_Match_(IVM)/ivm_2_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Income_Verif_Match_(IVM)/ivm_2_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=44"
---

![](ivm-version-2-installation-guide/001.png)

inCOME VERIFICATION MATCH(IVM)INSTALLATION GUIDE

October 1994

Information Systems Center

Albany, New York

Table of Contents

Introduction 1

Package Integration 2

Pre-Installation Checklist 3

Installation Instructions 4

Routine List 7

Sample Installation 8

Resource Requirements 12

Introduction

This package contains all of the routines, files, and options necessary to support the Means Test verification process in conjunction with the IVM Center. Also included in this package are all required modifications to Patient Information Management System (PIMS) and Integrated Billing (IB) that are necessary to install IVM V. 2.0.

The installation process for IVM V. 2.0 is simple and straightforward. The install should proceed quickly and there are no special jobs that need to be run in conjunction with the installation. The post-init routine contains one conversion, where all entries in the ANNUAL MEANS TEST (#408.31) file are updated with two additional fields. Even with this on-line conversion, installation times are not expected to exceed 30 minutes.

Similar to IVM V. 1.0, the user will be required in the pre-init to indicate whether the installation is occurring in the test or production account. The installation will update all of the necessary tables and parameters required to configure the software to exchange a host of unsolicited messages and queries, via Health Level 7 (HL7), with the IVM Center.

Package Integration

The following DHCP package versions (or higher) MUST be installed PRIOR to loading this version of IVM.

<table>
<colgroup>
<col style="width: 62%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Kernel</p>
</blockquote></th>
<th><blockquote>
<p>V. 7.1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA FileMan</p>
</blockquote></td>
<td><blockquote>
<p>V. 20.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>V. 5.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Integrated Billing</p>
</blockquote></td>
<td><blockquote>
<p>V. 2.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OERR</p>
</blockquote></td>
<td><blockquote>
<p>V. 2.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HL7</p>
</blockquote></td>
<td><blockquote>
<p>V. 1.5</p>
</blockquote></td>
</tr>
</tbody>
</table>

This package was created with Kernel V. 7.1 and VA FileMan V. 20.0. The IVMNTEG routine was created using the Kernel Tool Kit V. 7.2 XTSUMBLD utility.

The informational patch DG\*5.3\*33 describes all of the changes to PIMS required to run IVM V. 2.0. Please note that all of the required PIMS routines are explicitly exported with this version (that is, they are not bundled in routines of another namespace and unbundled during installation) and are listed in the Routine List section of this document. These routines are all in the DG\* and VAFHL\* namespaces.

Please note that the IB patch, IB\*2\*6, is required to be installed prior to the installation of IVM V. 2.0. The informational patch, IB\*2\*15, describes all of the changes to IB required for IVM. The IB routines, which are in the IB\* namespace, are also explicitly exported and listed in the Routine List section.

The IVM domain must be properly installed, as instructed in the FORUM patches XM\*DBA\*51, XM\*DBA\*52, and XM\*DBA\*60, in order to install IVM V. 2.0. This domain should have been established when IVM V. 1.0 was installed.

Pre-Installation Checklist

1\. Have you loaded this package into your test account?

2\. Have you reviewed the list of packages in the Package Integration section that are required for installation of IVM and confirmed that each one has been installed?

3\. Have you installed IB\*2\*6?

4\. Do you have any tasked jobs or other system processes that need to be shut down or rescheduled?

5\. Have you scheduled downtime with your users? You should schedule approximately 1 hour to install this package. Note that you may bring users on-line immediately after the installation has completed.

> Please note that you may consider installing this software with only your PIMS, IB, and Outpatient Pharmacy users logged off the system. Please refer to the discussion in Step 1 of the Installation Instructions.

6\. Have you scheduled an unattended backup prior to beginning the installation?

7\. Have you read the complete Installation Instructions?

8\. Have you coordinated the installation of this package with the respective services in your facility? These services might include MAS, Fiscal, and MCCR.

9\. Please note that this version of IVM has on-line options. Have you reviewed which menus you wish to assign to your users?

Installation Instructions

Please read all instructions carefully before beginning the installation.

Step Description

1\. Get users off system(s).

> It is recommended that all users are off the system during the installation due to the high degree of integration with PIMS and IB. Several changes to the PIMS Means Test module are released with this version of IVM, and cross-reference routines for files in both PIMS and IB will be recompiled. Use of PIMS or IB, or any package which invokes either of these packages, may cause an error or result in corrupt or incomplete file entries. If you choose to run this installation with users on the system, you must be assured that all Registration users are inactivated, and that activity in Medical Care Cost Recovery (MCCR) and Outpatient Pharmacy are minimized.

2\. Backup system(s).

3\. Disable Routine Mapping (DSM) on all systems.

4\. The global DGMT will become very active during the post-init conversion, as each entry in the ANNUAL MEANS TEST (#408.31) file will be updated. You may choose to disable journaling on that global.

5\. Sign into the UCI where the package is to be installed. It is suggested that MSM sites run the install on the print server. Use a partition of 16K for DSM or a partition of 40K for MSM.

6\. This package contains routines in the IVM\*, DG\*, VAFHL\*, and IB\* namespaces. Load the routines from the available media. See the Routine List section for a list of the distributed routines.

7\. Verify that the variables DUZ, DT, DTIME, and U are defined and that DUZ(0)="@". The DUZ variable must be defined as an active user number and the DUZ(0) variable must be set to "@" before you will be allowed to run the installation.

8\. D ^IVMINIT to begin the installation. Follow the sample installation in this guide.

> The pre-installation routine will check the current environment. You must also indicate whether the package is being installed in the test or production account. Please answer this question carefully.

> Seven IVM files will be installed along with one file from IB and four files from PIMS. Four of the IVM files and one of the PIMS files (#408.34) are new files. Options in both the IVM and IB packages will be installed.

9\. The post initialization routine will accomplish the following.

> A. Add the new mail group IVM MESSAGES to your system. Minimally, the IVM Coordinator and IRM support specialist should be added as members to this group.

> B. Update the HL7 SEGMENT NAME (#771.3) and the HL7 DHCP APPLICATION PARAMETER (#771) files in the HL7 package.

> C. Adds entries to the MEANS TEST CHANGES TYPE (#408.42) file.

> D. Add an entry to the IB ACTION STATUS (#350.21) file.

> E. Install all required protocols and list templates.

> F. Update the new fields, Source of Income Test (#.23) to "VAMC" and Primary Income Test for Year? (#2) to "YES" for all entries in the ANNUAL MEANS TEST (#408.31) file. This is the longest portion of the installation. We estimate that up to 4000 Means Tests may be updated in one minute.

> G. Send a notice of the installation to the IVM Center.

> H. Load the installation date into the IVM SITE PARAMETER (#301.9) file.

10\. The cross-reference routines for the INTEGRATED BILLING ACTION (#350) and ANNUAL MEANS TEST (#408.31) files are recompiled during the installation. If necessary, use DIKZ to recompile the cross-reference routines for these files on all CPUs.

11\. You may delete the IVMIN\*, IVMON\*, and IVM20\* routines from your system.

12\. Move all of the routines exported in this package, except those listed in step 11 which may be deleted, to all systems.

13\. Rebuild routine map sets.

> It is strongly recommended that the following routines be added to the routine map set on the volume set that they will be primarily running on.

> IVML\* IVMR\* IVMU\*

14\. You may bring users back on-line at this point.

15\. The IVM BACKGROUND JOB option should be queued to run each evening during non-peak hours. If this option is not scheduled to run, please use the Schedule/Unschedule Options option on the Task Manager Menu to schedule this task at this time. Please be sure that this option has not been scheduled to run twice!

16\. Please note that IVM V. 2.0 contains on-line options to be assigned to your users. The IVM Upload Menu is locked with the IVM UPLOAD key, and the IVM System Manager's Menu is locked with the IVM SYS key. You will need to assign these security keys to your users.

Routine List

\>D ^%RD

List all routines ? \<Yes\>

Output Device ? \< 0 \>

DSM Routine Directory 21-OCT-1994 21:07

\[TRF,FEY\]

DGMTA DGMTAUD DGMTAUD1 DGMTCOU1 DGMTDD DGMTDD2 DGMTDEL DGMTE

DGMTEO DGMTO1 DGMTOFA1 DGMTOPYT DGMTOREQ DGMTP4 DGMTSCC DGMTU

DGMTU11 DGMTU2 DGMTU21 DGMTU22 DGMTU23 DGMTU3 DGMTUB DGMTV

DGPTUTL1 DGRPU IBAERR1 IBAMTED IBAMTED1 IBAMTEDU IBAMTV IBAMTV1

IBAMTV2 IBAMTV3 IBAMTV31 IBAMTV32 IBAMTV4 IBAUTL5 IBECEA1 IBOMTP1

IVM20E IVM20P IVM20P1 IVM20P2 IVM20P21 IVM20P22 IVM20P3 IVMIN001

IVMIN002 IVMIN003 IVMIN004 IVMIN005 IVMIN006 IVMIN007 IVMIN008 IVMIN009

IVMIN00A IVMIN00B IVMIN00C IVMIN00D IVMIN00E IVMIN00F IVMIN00G IVMIN00H

IVMIN00I IVMIN00J IVMIN00K IVMIN00L IVMIN00M IVMIN00N IVMIN00O IVMIN00P

IVMIN00Q IVMIN00R IVMIN00S IVMIN00T IVMIN00U IVMIN00V IVMIN00W IVMIN00X

IVMIN00Y IVMIN00Z IVMIN010 IVMIN011 IVMIN012 IVMIN013 IVMIN014 IVMIN015

IVMIN016 IVMIN017 IVMIN018 IVMIN019 IVMIN01A IVMIN01B IVMIN01C IVMIN01D

IVMINIS IVMINIT IVMINIT1 IVMINIT2 IVMINIT3 IVMINIT4 IVMINIT5 IVMLDEM

IVMLDEM1 IVMLDEM2 IVMLDEM3 IVMLDEM4 IVMLDEM5 IVMLDEM6 IVMLDEM7 IVMLDEMU

IVMLINS IVMLINS1 IVMLINS2 IVMLINS3 IVMLINS4 IVMLINS5 IVMLSU IVMLSU1

IVMLSU2 IVMLSU3 IVMNTEG IVMON001 IVMON002 IVMON003 IVMONIT IVMONIT1

IVMONIT2 IVMONIT3 IVMPINS IVMPMTE IVMPREC IVMPREC1 IVMPREC2 IVMPREC3

IVMPREC4 IVMPREC5 IVMPREC6 IVMPREC7 IVMPREC8 IVMPREC9 IVMPRECA IVMPTRN

IVMPTRN1 IVMPTRN2 IVMPTRN3 IVMPTRN4 IVMPTRN5 IVMPTRN6 IVMPXFR IVMRBT

IVMRMCR IVMRMCR1 IVMRNQ IVMRNQ1 IVMRTSR IVMRTSR1 IVMRUTL IVMUCHK

IVMUCHK1 IVMUCHK2 IVMUCHK3 IVMUCHK4 IVMUCHK5 IVMUFNC IVMUFNC1 IVMUFNC2

IVMUFNC3 IVMUFNC4 IVMUM1 IVMUM2 IVMUM3 IVMUM4 IVMUM5 IVMUM6

IVMUM7 IVMUM8 IVMUPAR IVMUPUR IVMUTQ VAFHLFNC VAFHLZDP VAFHLZGD

VAFHLZIR VAFHLZMT

186 routines

Sample Installation

\>D ^IVMINIT

This version (#2.0) of 'IVMINIT' was created on 21-OCT-1994

(at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

Initialization Started: JUN 24, 1994@09:16:51

Select one of the following:

1 PRODUCTION

0 TEST

Enter type of account you are installing in: 1 PRODUCTION

I AM GOING TO SET UP THE FOLLOWING FILES:

301.5 IVM PATIENT

> **NOTE:** You already have the 'IVM PATIENT' File.

301.6 IVM TRANSMISSION LOG

> **NOTE:** You already have the 'IVM TRANSMISSION LOG' File.

301.61 IVM BILLING TRANSMISSION

301.9 IVM SITE PARAMETER

> **NOTE:** You already have the 'IVM SITE PARAMETER' File.

301.91 IVM REASONS FOR NOT UPLOADING INSURANCE (including data)

I will MERGE your data with mine.

301.92 IVM DEMOGRAPHIC UPLOAD FIELDS (including data)

I will MERGE your data with mine.

301.93 IVM CASE CLOSURE REASON (including data)

I will MERGE your data with mine.

350 INTEGRATED BILLING ACTION (Partial Definition)

> **NOTE:** You already have the 'INTEGRATED BILLING ACTION' File.

408.13 INCOME PERSON (Partial Definition)

> **NOTE:** You already have the 'INCOME PERSON' File.

408.31 ANNUAL MEANS TEST (Partial Definition)

> **NOTE:** You already have the 'ANNUAL MEANS TEST' File.

408.34 SOURCE OF INCOME TEST (including data)

I will MERGE your data with mine.

408.41 MEANS TEST CHANGES (Partial Definition)

> **NOTE:** You already have the 'MEANS TEST CHANGES' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// (NO)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES//

(YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...HMMM, LET ME THINK ABOUT THAT A MOMENT.......................................

...................................

Compiling Cross-Reference routine.............

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

IBXA1 routine filed

IBXA2 routine filed

IBXA routine filed

Compiling Cross-Reference routine.............

...HMMM, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

DGMTXX31 routine filed

DGMTXX32 routine filed

DGMTXX3 routine filed..................

'IB MT ON HOLD MENU' Option Filed

'IB MT REV PEND CHARGES' Option Filed

'IVM BACKGROUND JOB' Option Filed

'IVM MAIN MENU' Option Filed

'IVM OUTPUT BILL TRANS' Option Filed

'IVM OUTPUT CASE INQ' Option Filed

'IVM OUTPUT MENU' Option Filed

'IVM OUTPUT MT COMPARISON' Option Filed

'IVM SYS MGR MENU' Option Filed

'IVM SYS PAR ENTER/EDIT' Option Filed

'IVM SYS PURGE TRANSMISSIONS' Option Filed

'IVM SYS TRANSMISSION REPORT' Option Filed

'IVM UPLOAD DEM' Option Filed

'IVM UPLOAD INS' Option Filed

'IVM UPLOAD MENU' Option Filed

'IVM UPLOAD SSN' Option Filed...

NO SECURITY-CODE PROTECTION HAS BEEN MADE

\>\>\> Adding IVM MESSAGES mailgroup for sending results of data transmissions...

\>\>\> Adding 'Z' segments to HL7 SEGMENT NAME file (#771.3)...

\>\> ZIO (VA Patient Care Statistics) segment added

\>\> ZIR (VA Specific Income Information) segment added

\>\>\> Updating HL7 DHCP APPLICATION file entry for IVM...

\>\>\> Adding new entries in the MEANS TEST CHANGES TYPE (#408.42) file...

\>\>\> Adding a new status in the IB ACTION STATUS (#350.21) file...

This version of 'IVMONIT' was created on 21-OCT-1994

(at ALBANY ISC VAX DEVELOPMENT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please...........................

'IBAMTV REV CANC CHARGE' Protocol Filed

IBAMTV REV CANC CHARGE added as item to IBAMTV REV IND CHARGES.

'IBAMTV REV IND CHARGES' Protocol Filed

'IBAMTV REV PASS CHARGE' Protocol Filed

IBAMTV REV PASS CHARGE added as item to IBAMTV REV IND CHARGES.

'IBAMTV REV PATIENT' Protocol Filed

'IBAMTV SEL PATIENT' Protocol Filed

IBAMTV SEL PATIENT added as item to IBAMTV REV PATIENT.

'IVM INSURANCE EVENT' Protocol Filed

IVM INSURANCE EVENT added as item to IBCN NEW INSURANCE EVENTS.

'IVM MEANS TEST EVENT' Protocol Filed

'IVMLD DELETE FIELDS' Protocol Filed

'IVMLD DEMO UPLOAD' Protocol Filed

IVMLD SELECT UPLOADABLE added as item to IVMLD DEMO UPLOAD.

IVMLD SELECT NON-UPLOADABLE added as item to IVMLD DEMO UPLOAD.

IVMLD SELECT HELP added as item to IVMLD DEMO UPLOAD.

'IVMLD NON-UPLOADABLE FIELDS' Protocol Filed

IVMLD DELETE FIELDS added as item to IVMLD NON-UPLOADABLE FIELDS.

'IVMLD SELECT HELP' Protocol Filed

'IVMLD SELECT NON-UPLOADABLE' Protocol Filed

'IVMLD SELECT UPLOADABLE' Protocol Filed

'IVMLD UPLOAD FIELDS' Protocol Filed

'IVMLD UPLOADABLE DEMO' Protocol Filed

IVMLD UPLOAD FIELDS added as item to IVMLD UPLOADABLE DEMO.

IVMLD DELETE FIELDS added as item to IVMLD UPLOADABLE DEMO.

'IVMLI DISPLAY ENTRY' Protocol Filed

'IVMLI INSURANCE UPLOAD' Protocol Filed

IVMLI DISPLAY ENTRY added as item to IVMLI INSURANCE UPLOAD.

IVMLI SELECT HELP added as item to IVMLI INSURANCE UPLOAD.

'IVMLI SELECT HELP' Protocol Filed

'IVMLS PURGE SSN' Protocol Filed

'IVMLS SSN UPLOAD' Protocol Filed

IVMLS PURGE SSN added as item to IVMLS SSN UPLOAD.

IVMLS UPLOAD SSN added as item to IVMLS SSN UPLOAD.

'IVMLS UPLOAD SSN' Protocol Filed

OK, Protocol Installation is Complete.

\>\>\> Installing List Templates...

'IVM DEMOGRAPHIC' List Template...Filed.

'IVM DEMOGRAPHIC NON-UPLOADABLE' List Template...Filed.

'IVM DEMOGRAPHIC UPLOADABLE' List Template...Filed.

'IB MT REVIEW INDIV CHARGES' List Template...Filed.

'IB MT REVIEW PATIENT' List Template...Filed.

'IVM INSURANCE UPLOAD' List Template...Filed.

'IVM SSN UPDATE' List Template...Filed.

\>\>\> Rebuilding ^XUTL("XQORM" for protocol 'IBAMTV REV PATIENT' ...

\>\>\> Rebuilding ^XUTL("XQORM" for protocol 'IBAMTV REV IND CHARGES' ...

\>\>\> Initializing new ANNUAL MEANS TEST file (#408.31) fields for

existing entries as follows:

SOURCE OF INCOME TEST (#.23) = VAMC (value = 1)

PRIMARY INCOME TEST FOR YEAR? (#2)= YES (value = 1)

...................

\>\>\> Sending a 'completed installation' notice to the IVM Center...

\>\>\> Initialization Complete at JUN 29, 1994@21:01:02

Elapse time for initialization was: 0 Hours, 8 Minutes, 47 Seconds

The installation of Income Verification Match Version 2.0 has completed.

Please be sure that the IVM Nightly Job (option IVM BACKGROUND JOB) is

scheduled to run. If it is not, it should be scheduled to run early each morning.

Be sure that it is not scheduled twice!!

Remember to re-compile the cross reference routines for the INTEGRATED

BILLING ACTION (#350) and ANNUAL MEANS TEST (#408.31) files, using DIKZ,

on all of your systems.

\>

Resource Requirements

The installation of IVM V. 2.0 requires a very small amount of additional computer resources. Approximately 500K bytes of additional disk capacity is required to install this package. Global growth within IVM should not change with this version. Additional growth in PIMS and IB will depend upon the volume of verified Means Tests returned to the facility from the IVM Center. Our experience with our test sites indicates that this additional growth will be minimal. The mail traffic emanating from your site should not increase significantly with this version of IVM. On the average, a maximum of two MailMan messages is expected to be sent from your facility each evening, with each message containing, at a maximum, 2500 lines. The net increase in total network traffic will depend upon the volume of transmissions originating from the IVM Center. Again, our experience with our test sites has indicated that this increase will not be significant.