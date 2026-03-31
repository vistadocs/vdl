---
title: OR*3*296  and Associated Patches Installation Guide CPRS GUI 27.9
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: and Associated Patches  CPRS GUI 27.9
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*296
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 1
description: <span class="smallcaps">CPRS Patch OR\3.0\296 (CPRS GUI V.27.90) and Associated Patches</span><span class="smallcaps">Installation Guide</span><span class="smallcaps">August 2009</span>
audience: 
keywords: 
  - install
  - site
  - cprs
  - installation
  - span
  - class
  - global
  - distribution
  - transport
  - send
page_count: 0
word_count: 3225
section_count: 0
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_296ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_296ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

![](or-3-296-and-associated-patches-installation-guide-cprs-gui-27-9/001.png)

<span class="smallcaps">CPRS Patch OR\*3.0\*296 (CPRS GUI V.27.90) and Associated Patches</span><span class="smallcaps">Installation Guide</span><span class="smallcaps">August 2009</span>

<span id="_Toc238350273" class="anchor"></span>Table of Contents

<span id="_Toc238350274" class="anchor"></span>OR\*3.0\*296 (CPRS GUI v27.90) Installation Requirements and Notes

OR\*3.0\*296 includes one host file that exports routines, two options, three Remote Procedure Calls (RPCs), and parameters. No data dictionary changes are included.

<span id="_Toc238350275" class="anchor"></span>Required Patches

Before you can install OR\*3.0\*296 (CPRS GUI v.27.90), you must verify that the following required patches are properly installed on your system:

- OR\*3.0\*283
- OR\*3.0\*292 
- OR\*3.0\*301
- OR\*3.0\*303
- OR\*3.0\*304
- YS\*5.01\*98

<span id="_Toc238350276" class="anchor"></span>Related Patches

To fully implement the new features in OR\*3.0\*296, the following related patches must be installed on your system:

- GMRC\*3.0\*65
- GMRC\*3.0\*69

<span id="_Toc238350277" class="anchor"></span>Internet Explorer Requirements

Internet Explorer v4.0 (IE4) or later is REQUIRED in order for OR\*3.0\*296 to run. However, IE5.5 or later is required for PKI functionality.

<span id="_Toc238350278" class="anchor"></span>Installation Compliance Date

The compliance period for installation of OR\*3.0\*296 is 30 days.

<span id="_Toc238350279" class="anchor"></span>Local Modifications to OR\*3.0\*296 Source Code

OR\*3.0\*296 is compiled with Delphi 2006. Modification of OR\*3.0\*296 Source Code requires Delphi 2006.

<span id="_Toc238350280" class="anchor"></span>Software Retrieval

Download the necessary files from the FTP anonymous directories: download.vista.med.va.gov.

- YS_501_98.KID
- YS_MHA_A.DLL and YS_501_98_SETUP.EXE
- OR_30_296.KID
- OR_30_296.ZIP

Software distributed via the National Patch Module (FORUM) in a packman message.

- GMRC\*3.0\*65
- GMRC\*3.0\*69

<span id="_Toc238350281" class="anchor"></span>OR\*3.0\*296 (CPRS GUI v27.90) and Associated Patches Software Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation will take approximately 15 minutes or more, depending on the menu structure at your site.

Listed below are general installation instructions for installing the OR\*3.0\*296 KIDS build and other patches. For specific installation details, refer to the software installation captures below. Additionally, review the National Patch Module messages for each patch for patch-specific information.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
2.  Use Load a Distribution. You may need to precede the host file name with a directory name.
3.  If given the option to run any Environment Check Routine(s), answer "YES."
4.  From this menu, you may then elect to use the following options:
- Backup a Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
5.  When ready, select the Install Packages option.
6.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? Yes//", respond "YES."
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond "YES."
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond YES. When prompted to select the options you would like to place out of order, enter the following:

OR OE/RR MENU CLINICIAN CPRS Clinician Menu

OR OE/RR MENU NURSE CPRS Nurse Menu

OR OE/RR MENU WARD CLERK CPRS Ward Clerk Menu

OR CPRS GUI CHART

9.  When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'

<span id="_Toc238350282" class="anchor"></span>OR\*3.0\*296 (CPRS GUI v27.90) and Associated Patches Software Installation Sequence

1.  Make sure all Nationally Released Required patches are installed—
- OR\*3\*283
- OR\*3\*292
- OR\*3\*301
- OR\*3\*303
- OR\*3\*304
2.  Install Mental Health required patch and file:
- YS\*5.01\*98.KID
- YS_MHA_A.DLL (using YS_501_98_SETUP.EXE if appropriate, see step c below)
  1.  Install YS_501_98.KID
  2.  Ensure that the option YS BROKER1 \[YS BROKER1\] is on the Mental Health users’ secondary menus, as well as the secondary menus of all users who currently have the OR CPRS GUI CHART option.
  3.  Distribute new DLL named YS_MHA_A.DLL in one of the following ways:
- Install manually on the client workstation: Run YS_501_98_Setup.exe to place the YS_MHA_A.dll in the Common Files directory.

OR

- Pushing files to the workstation over the network: If your site uses application distribution software, you can distribute the YS_MHA_A.dll to client workstations. Running the YS_501_98_Setup.exe requires two interactions with the user (to start and to signify finished). To avoid the user/install interaction, the file YS_MHA_A.dll can be copied directly to the *\<drive\>*\Programs Files\Vista\Common Files directory. This may be the more desirable way to push the dll to many workstations.

Please refer to the YS\*5.01\*98 Installation Capture below in this document for installation details.

3.  Install Patch OR\*3.0\*296:  OR_30_296.KID.

Please refer to the OR\*3.0\*296 Installation Capture for installation details.

4.  Distribute CPRSCHART.EXE, CPRS.HLP, CPRS.CNT located in OR_30_296.ZIP.

These three files should be distributed to the same directory as the borlndmm.dll. Usually, these files are located in the CPRS directory.

5.  Place the User and Technical Manual files in a location that can be accessed by CPRS users.
6.  Install Patch GMRC\*3.0\*65.

Please refer to the GMRC\*3.0\*65 Installation Capture for installation details.

7.  Install Patch GMRC\*3.0\*69.

Please refer to the GMRC\*3.0\*69 Installation Capture for installation details.

<span id="_Toc238350283" class="anchor"></span>OR\*3.0\*296 Changed Help text of Existing Parameter – ORPF ACTIVE ORDERS CONTEXT HRS

- This parameter defines the number of hours that orders remain in the "Active/Current Orders" context after they have been completed.

Updated Help Values:

Before:

VALUE HELP: Number of hours to include completed orders in Active Orders display.

After:

VALUE HELP: Enter the number of hours to include terminated orders in the Active Orders view

<span id="_Toc238350284" class="anchor"></span>OR\*3.0\*296 (CPRS GUI v27.90) Associated Software and Documentation

<span id="_Toc238350285" class="anchor"></span>Required Patches:

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PATCH</strong></th>
<th><strong>SUPPORTED FUNCTIONALITY</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR*3.0*283</td>
<td><p>--Event Delayed Orders</p>
<p>--Releases Two Copies</p></td>
</tr>
<tr class="even">
<td>OR*3.0*292</td>
<td>--Locking and Parameter Help Text Problem</td>
</tr>
<tr class="odd">
<td>OR*3*301</td>
<td><p>-- Changes the ORB PROCESSING FLAG</p>
<p>Parameter</p>
<p>-- Updates CPRS v27 Release Notes and</p>
<p>Technical Manual</p>
<p>-- Adds new option, Convert IV Inpatient QO to</p>
<p>Infusion QO [OR CONVERT INP TO QO]</p></td>
</tr>
<tr class="even">
<td>OR*3*303</td>
<td><p>--Corrects Display of DCd Med Orders</p>
<p>--Removes CR from Reason for Study field</p>
<p>--Corrects “Invalid Rate” error in Renewed Orders</p>
<p>--Fixes &lt;SUBSCRIPT&gt;GUI+13^ORCDLR2</p></td>
</tr>
<tr class="odd">
<td><p>YS*5.01*98</p>
<p>Exports three files:</p>
<p>YS_501_98.KID</p>
<p>YS_501_98_SETUP.EXE</p>
<p>YS_MHA_A.DLL</p></td>
<td><p>--Distributes new MH DLL</p>
<p>--Stores Temporary file in VistA not on Client</p></td>
</tr>
</tbody>
</table>

<span id="_Toc238350286" class="anchor"></span>Related Patches:

|             |                             |
|-------------|-----------------------------|
| PATCH   | SUPPORTED FUNCTIONALITY |
| GMRC\*3\*65 | GWOT COMBAT VET INDICATORS  |
| GMRC\*3\*69 | REFORMATS LONG COMMENTS     |

<span id="_Toc238350287" class="anchor"></span>OR_30_296.ZIP:

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 22%" />
<col style="width: 0%" />
<col style="width: 37%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>FILE</strong></td>
<td><strong>VERSION</strong></td>
<td colspan="2"><strong>CONTENTS</strong></td>
</tr>
<tr class="even">
<td>CPRSChart.exe</td>
<td>1.0.27.90</td>
<td colspan="2">CPRS GUI v27.90</td>
</tr>
<tr class="odd">
<td>CPRSGUIUM.doc</td>
<td>N/A</td>
<td colspan="2">CPRS GUI User Manual</td>
</tr>
<tr class="even">
<td>CPRSLMTM.doc</td>
<td>N/A</td>
<td colspan="2"><p>CPRS ListManager</p>
<p>Technical Manual</p></td>
</tr>
<tr class="odd">
<td>CPRSGUITM.doc</td>
<td>N/A</td>
<td colspan="2">CPRS GUI Technical Manual</td>
</tr>
<tr class="even">
<td>OR_30_296IG.doc</td>
<td>N/A</td>
<td colspan="2"><blockquote>
<p>CPRS Patch OR*3*296 (CPRS</p>
<p>GUI V.27.90) and Associated</p>
</blockquote>
<p>Patches Installation Guide</p></td>
</tr>
<tr class="odd">
<td>OR_30_296RN.doc</td>
<td>N/A</td>
<td colspan="2">OR*3.0*296 Release Notes</td>
</tr>
<tr class="even">
<td>CPRS.cnt</td>
<td colspan="2">N/A</td>
<td>CPRS help contents file</td>
</tr>
<tr class="odd">
<td>CPRS.hlp</td>
<td colspan="2">N/A</td>
<td>CPRS help file</td>
</tr>
<tr class="even">
<td>CPRSGUIUM.pdf</td>
<td colspan="2">N/A</td>
<td>CPRS GUI User Manual</td>
</tr>
<tr class="odd">
<td>CPRSLMTM.pdf</td>
<td colspan="2">N/A</td>
<td><p>CPRS ListManager</p>
<p>Technical Manual</p></td>
</tr>
<tr class="even">
<td>CPRSGUITM.pdf</td>
<td colspan="2">N/A</td>
<td>CPRS GUI Technical Manual</td>
</tr>
<tr class="odd">
<td>OR_30_296ig.pdf</td>
<td>N/A</td>
<td colspan="2"><blockquote>
<p>CPRS Patch OR*3*296 (CPRS GUI</p>
<p>V.27.90) and Associated Patches</p>
<p>Installation Guide</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OR_30_296RN.pdf</td>
<td colspan="2">N/A</td>
<td>OR*3.0*296 Release Notes</td>
</tr>
</tbody>
</table>

> YS\*5.01\*98 Installation Capture

1.  Install the YS\*5.01\*98.KID patch. See example capture below.

Example

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: YS\*5.01\*98

Select Installation Option: 1 Load a Distribution

Enter a Host File: \[LEXPLT\]YS_501_98.KID;1

KIDS Distribution saved on Aug 28, 2008@11:10:33

Comment: CPRS V27 SUPPORT

This Distribution contains Transport Globals for the following Package(s):

YS\*5.01\*98

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

YS\*5.01\*98

Use INSTALL NAME: YS\*5.01\*98 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: YS\*5.01\*98 Loaded from Distribution 6/22/09@11:52:35

=\> CPRS V27 SUPPORT ;Created on Aug 28, 2008@11:10:33

This Distribution was loaded on Jun 22, 2009@11:52:35 with header of

CPRS V27 SUPPORT ;Created on Aug 28, 2008@11:10:33

It consisted of the following Install(s):

YS\*5.01\*98

Checking Install for Package YS\*5.01\*98

Install Questions for YS\*5.01\*98

Incoming Files:

601.94 MH CR SCRATCH

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// NO

Want KIDS to INHIBIT LOGONs during the install? NO// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET TERMINAL

Complete

10. Ensure that the option YS BROKER1 \[YS BROKER1\] is on the Mental Health users’ secondary menus, as well as the secondary menus of all users who currently have the OR CPRS GUI CHART option.
11. After installation of the KIDS build, download the YS_501_98_Setup.exe and YS_MHA_A.dll file located in the Anonymous Software directory.
12. Distribute new DLL named YS_MHA_A.DLL in one of the following ways:
- Install manually on the client workstation: Run YS_501_98_Setup.exe to place the YS_MHA_A.dll in the Common Files directory.

> **NOTE:** Do NOT queue the installation, because this installation contains questions requiring a response, and queuing will stop the installation.

OR

- Pushing files to the workstation over the network: If your site uses application distribution software, you can distribute the YS_MHA_A.dll to client workstations. Running the YS_501_98_Setup.exe requires two interactions with the user (to start and to signify finished). To avoid the user/install interaction, the file YS_MHA_A.dll can be copied directly to the *\<drive\>*\Programs Files\Vista\Common Files directory. This may be the more desirable way to push the dll to many workstations.

Please refer to the YS\*5.01\*98 Installation Capture below in this document and the *MENTAL HEALTH ASSISTANT DLL used by CPRS Clinical Reminders INSTALLATION GUIDE: PATCH YS\*5.01\*98* for installation details.

> OR\*3.0\*296 Checksum Value Verification

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: OR\*3.0\*296

PACKAGE: OR\*3.0\*296 Jun 22, 2009 11:11 am PAGE 1

-----------------------------------------------------------------------------

OR3CONV Calculated 57296998

OR3CONV1 Calculated 41773160

ORB3 Calculated 93373249

ORCDLR1 Calculated 81262557

ORCDPSIV Calculated 96653807

ORCMEDT0 Calculated 17670670

ORCMEDT1 Calculated 45036674

ORCMEDT5 Calculated 35418320

ORCSEND Calculated 65578810

ORINQIV Calculated 192421660

ORMARKER Calculated 978608

ORMRA Calculated 62138554

ORPRPM Calculated 64231033

ORWDX Calculated 67409395

ORWDX1 Calculated 52053311

ORWDXM3 Calculated 72094070

ORWDXM4 Calculated 32166098

ORWOD Calculated 72302805

ORWOD1 Calculated 38695937

ORWORB Calculated 69468448

ORWTPUA Calculated 2236253

ORY296 Calculated 1180350

ORYCHKE Calculated 2490043

23 Routines checked, 0 failed.

> OR\*3.0\*296 Transport Global Print

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 3 Print Transport Global

Select INSTALL NAME: OR\*3.0\*296

PACKAGE: OR\*3.0\*296 Jun 22, 2009 11:13 am PAGE 1

-----------------------------------------------------------------------------TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: ORDER ENTRY/RESULTS REPORTING ALPHA/BETA TESTING: NO

DESCRIPTION:

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: PRE^ORY296 DELETE PRE-INIT ROUTINE: No

POST-INIT ROUTINE: POST^ORY296 DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-----------------------------------------------------------------------------

101.41 ORDER DIALOG NO NO YES OVER YES NO

DATA SCREEN: I Y=130

ROUTINE: ACTION:

OR3CONV SEND TO SITE

OR3CONV1 SEND TO SITE

ORB3 SEND TO SITE

ORCDLR1 SEND TO SITE

ORCDPSIV SEND TO SITE

ORCMEDT0 SEND TO SITE

ORCMEDT1 SEND TO SITE

ORCMEDT5 SEND TO SITE

ORCSEND SEND TO SITE

ORINQIV SEND TO SITE

ORMARKER SEND TO SITE

ORMRA SEND TO SITE

ORPRPM SEND TO SITE

ORWDX SEND TO SITE

ORWDX1 SEND TO SITE

ORWDXM3 SEND TO SITE

ORWDXM4 SEND TO SITE

ORWOD SEND TO SITE

ORWOD1 SEND TO SITE

ORWORB SEND TO SITE

ORWTPUA SEND TO SITE

ORY243 DELETE AT SITE

ORY2430 DELETE AT SITE

ORY24301 DELETE AT SITE

ORY24302 DELETE AT SITE

ORY24303 DELETE AT SITE

ORY24304 DELETE AT SITE

ORY24305 DELETE AT SITE

ORY24306 DELETE AT SITE

ORY24307 DELETE AT SITE

ORY24308 DELETE AT SITE

ORY24309 DELETE AT SITE

ORY2431 DELETE AT SITE

ORY2432 DELETE AT SITE

ORY2433 DELETE AT SITE

ORY2434 DELETE AT SITE

ORY243A DELETE AT SITE

ORY243ES DELETE AT SITE

ORY243R DELETE AT SITE

ORY296 SEND TO SITE

ORYCHKE SEND TO SITE

OPTION: ACTION:

OR CPRS GUI CHART SEND TO SITE

OR MEDICATION QO CHECKER SEND TO SITE

PARAMETER DEFINITION: ACTION:

ORPF ACTIVE ORDERS CONTEXT HRS SEND TO SITE

ORWRP TIME/OCC LIMITS INDV SEND TO SITE

REMOTE PROCEDURE: ACTION:

GMV CLOSEST READING SEND TO SITE

OR GET COMBAT VET SEND TO SITE

ORWDX UNLKOTH SEND TO SITE

INSTALL QUESTIONS:

Default Rebuild Menu Trees Upon Completion of Install: NO

Default INHIBIT LOGONs during the install: NO

Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

REQUIRED BUILDS: ACTION:

YS\*5.01\*98 Don't install, leave global

OR\*3.0\*292 Don't install, leave global

OR\*3.0\*283 Don't install, leave global

OR\*3.0\*301 Don't install, leave global

OR\*3.0\*303 Don't install, leave global

OR\*3.0\*304 Don't install, leave global

<span id="_Toc238350288" class="anchor"></span>OR\*3\*296 Installation Capture

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option: INSTALLation

   1      Load a Distribution

   2      Verify Checksums in Transport Global

   3      Print Transport Global

   4      Compare Transport Global to Current System

   5      Backup a Transport Global

   6      Install Package(s)

          Restart Install of Package(s)

          Unload a Distribution

Select Installation Option: 6  Install Package(s)

Select INSTALL NAME: or\*3.0\*296       Loaded from Distribution  6/22/09@10:50:58

     =\> OR\*3.0\*296 KIDS BUILD  ;Created on May 07, 2009@11:54:07

This Distribution was loaded on Jun 22, 2009@10:50:58 with header of

   OR\*3.0\*296 KIDS BUILD  ;Created on May 07, 2009@11:54:07

   It consisted of the following Install(s):

     OR\*3.0\*296

Checking Install for Package OR\*3.0\*296

Install Questions for OR\*3.0\*296

Incoming Files:

   101.41    ORDER DIALOG  (including data)

> **NOTE:** You already have the 'ORDER DIALOG' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// YES

Want KIDS to INHIBIT LOGONs during the install? YES//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU CLINICIAN

CPRS Clinician Menu

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU NURSE CPRS

Nurse Menu

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU WARD CLERK

CPRS Ward Clerk Menu

Enter options you wish to mark as 'Out Of Order': OR CPRS GUI CHART CPRSCh

art version 1.0.27.83

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   TELNET TERMINAL

                                   OR\*3.0\*296                                  

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

 

 Installing OPTION

 

 Installing PARAMETER DEFINITION

               Jun 22, 2009@14:05:48

 

 Running Post-Install Routine: POST^ORY296

 

 Updating Routine file...

 

 Updating KIDS files...

 

Menu Rebuild Complete: Jun 22, 2009@11:53:46



 OR\*3.0\*296 Installed.

               Jun 22, 2009@14:05:48

 

 Not a production UCI

 

 NO Install Message sent

Rebuilding Menus



WVMENU Women's Health Menu 1 03/21/06 05/27/09

LRLOINC LOINC Main Menu 1 02/27/07 05/27/09

RMPO-MENU-MAIN Home Oxygen Main Menu 2 03/05/07 05/27/09

ZPSJU DENVER RPH Inpatient Medication Menu... 29 03/05/07 05/27/09

452 CONTRACT TRANSCRIPTION

Contract Transcription Menu 11 03/05/07 05/27/09

AGING RECEIVABLE AGING RECEIVABLE 3 03/05/07 05/27/09

OIG OIG 2 07/13/06 05/27/09

NON-MCCF MENU MON-MCCF MENU 1 01/24/07 05/27/09

ASSHRCFPCC HRC First Party CC 204 03/05/07 05/27/09

MQAS AUDIT MQAS AUDIT MENU 3 02/28/06 05/27/09

ARS BRONX NURSE ARS BRONX NURSE 23 03/05/07 05/27/09

Building secondary menu trees....

Merging.... done.

          R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

  100%    .             25             50             75               .

Complete  F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

Install Completed

<span id="_Toc238350289" class="anchor"></span>GMRC\*3\*65 Installation Capture

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have 6 new messages. (Last arrival: 08/06/08@12:46)

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: GMRC\*3.0\*65      Loaded from Distribution  6/23/09@10:01:38

     =\> GMRC\*3\*65

This Distribution was loaded on Jun 23, 2009@10:01:38 with header of

   GMRC\*3\*65

   It consisted of the following Install(s):

    GMRC\*3.0\*65

Checking Install for Package GMRC\*3.0\*65

Install Questions for GMRC\*3.0\*65

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   TELNET TERMINAL

                                  GMRC\*3.0\*65                                  

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

 Install Started for GMRC\*3.0\*65 :

               Jun 23, 2009@10:02:34

 

Build Distribution Date: Sep 15, 2008

 

 Installing Routines:

               Jun 23, 2009@10:02:34

 

 Updating Routine file...

 

 Updating KIDS files...

 

 GMRC\*3.0\*65 Installed.

               Jun 23, 2009@10:02:35

 

 Not a production UCI

 

 NO Install Message sent

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

          R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

  100%    .             25             50             75               .

Complete  F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

Install Completed

> GMRC\*3\*69 Installation Capture

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: GMRC\*3.0\*69 Loaded from Distribution 3/11/09@15:24:5

2

=\> GMRC\*3\*69

This Distribution was loaded on Mar 11, 2009@15:24:52 with header of

GMRC\*3\*69

It consisted of the following Install(s):

GMRC\*3.0\*69

Checking Install for Package GMRC\*3.0\*69

Install Questions for GMRC\*3.0\*69

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME

Install Started for GMRC\*3.0\*69 :

Mar 11, 2009@15:25:45

Build Distribution Date: Mar 11, 2009

Installing Routines:

Mar 11, 2009@15:25:45

Running Pre-Install Routine: PRE^GMRCYP69

Running Post-Install Routine: POST^GMRCYP69

Post-install queued as task \#322367

If any records are locked, task will re-run 5 minutes after completion.

Updating Routine file...

Updating KIDS files...

GMRC\*3.0\*69 Installed.

Mar 11, 2009@15:25:45

Not a production UCI

NO Install Message sent

Install Completed