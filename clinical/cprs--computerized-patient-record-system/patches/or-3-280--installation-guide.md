---
title: OR*3*280 and Associated Patches Installation Guide CPRS GUI 28
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: and Associated Patches  CPRS GUI 28
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*280
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: <span class="smallcaps">CPRS GUI version 28</span><span class="smallcaps">(Patch# OR\3\280) and Associated Patches</span><span class="smallcaps">Installation Guide</span>
audience: 
keywords: 
  - site
  - install
  - send
  - calculated
  - cprs
  - package
  - span
  - pxrm
  - installing
  - order
page_count: 0
word_count: 5820
section_count: 0
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_280ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_280ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

![](or-3-280-and-associated-patches-installation-guide-cprs-gui-28/001.png)

<span class="smallcaps">CPRS GUI version 28</span><span class="smallcaps">(Patch# OR\*3\*280) and Associated Patches</span><span class="smallcaps">Installation Guide</span>

<span id="_Toc283725428" class="anchor"></span>Revision History

The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.

|     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |
|     |     |     |     |     |     |
|     |     |     |     |     |     |

<span id="_Toc283725429" class="anchor"></span>Table of Contents

<span id="_Toc283725430" class="anchor"></span>CPRS GUI v28 Installation Requirements and Notes

CPRS GUI version 28 consists of five host files: PSS_1_151.KID, PSS_1_142.KID, CPRS28_REQUIRED.KID, OR_PSJ_PXRM_28.KID and CPRS28_RELATED.KID. These five host files contain software that support CPRS GUI v28 functionality. The host files were created to simplify installation at Veterans Health Administration (VHA) facilities and to assist in the phased implementation release method for CPRS v28. CPRS v28 will follow a phase implementation. To see current status and target dates for sites/VISN please refer to the following site:

[<span class="mark">REDACTED</span>](http://vaww.itfo.portal.va.gov/svcs/itfopmo/pre05/default.aspx)

<span id="_Toc287445009" class="anchor"></span>Required Patches

Before you can install CPRS GUI v.28, you must verify that the following required patches are properly installed on your system:

- OR\*3.0\*67
- OR\*3.0\*181
- OR\*3.0\*293 (Released in CPRS28_REQUIRED.KID with CPRS v28)
- OR\*3.0\*295
- OR\*3.0\*296
- OR\*3.0\*302
- OR\*3.0\*307
- OR\*3.0\*316
- OR\*3.0\*330
- GMRC\*3.0\*66 (Released in CPRS28_REQUIRED.KID with CPRS v28)
- GMRC\*3.0\*68
- LR\*5.2\*395
- PSS\*1.0\*142 (Released as a host file PSS_1_142.KID with CPRS v28)
- PSS\*1.0\*147
- PSS\*1.0\*151 (Released as a host file PSS_1_151.KID with CPRS v28)
- SD\*5.3\*536
- XU\*8.0\*474
- POLYTRAUMA MARKER 1.0
- PXRM\*2.0\*17
- USR\*1.0\*33

<span id="_Toc283725433" class="anchor"></span>Required Patches Distributed in the CPRS v28

These patches are required for OR\*3.0\*280 installation and should be installed prior to the Primary Bundle of CPRS v28. These patches will be released in conjunction with CPRS v28.

- PSS\*1.0\*151 (Released as a host file PSS_1_151.KID)
- PSS\*1.0\*142 (Released as a host file PSS_1_142.KID)

  Released in CPRS28_REQUIRED.KID
- OR\*3.0\*293
- GMRC\*3.0\*66
- GMRA\*4\*45

<span id="_Toc283725434" class="anchor"></span>Patches Distributed in the CPRS v28 Primary Bundle (OR_PSJ_PXRM_28.KID)

This host file, OR_PSJ_PXRM_28.KID, contains the CPRS GUI v.28 patch (OR\*3.0\*280) and a required Inpatient Pharmacy and Clinical Reminders patch. When you install this host file, the three patches listed below will be installed on your system.

- PSJ\*5.0\*226
- PXRM\*2.0\*16
- OR\*3.0\*280

<span id="_Toc283725435" class="anchor"></span>Related Patches to Be Installed after CPRS v28

The following patches support functionality in CPRS v28. These patches will be released in conjunction with CPRS v28.

Released in CPRS28_RELATED.KID

- GMRC\*3.0\*64
- GMTS\*2.7\*90
- OR\*3.0\*337

<span id="_Toc283725436" class="anchor"></span>Software Retrieval

Your site will be contacted when to download the necessary files from a FTP directory. CPRS v28 is following a phased implementation. Please reference the following site for information on when your site is targeted for installation

[<span class="mark">REDACTED</span>](http://vaww.itfo.portal.va.gov/svcs/itfopmo/pre05/default.aspx)

PSS_1_151.KID

PSS_1_142.KID

CPRS28_REQUIRED.KID

OR_PSJ_PXRM_28.KID

CPRS28_RELATED.KID

OR_30_280.ZIP

<span id="_Toc283725437" class="anchor"></span>CPRS GUI v28 Software Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation will take approximately 15 minutes or more, depending on the menu structure at your site.

Listed below are general installation instructions for installing the CPRS GUI v28 KIDS builds and other patches. For specific installation details, refer to the CPRS GUI v28 Software Installation Capture. Additionally, review the National Patch Module messages for each patch for patch-specific information.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
2.  Use Load a Distribution. You may need to prepend a directory name.
3.  If given the option to run any Environment Check Routine(s), answer "YES."
4.  From this menu, you may then elect to use the following options:
- Backup a Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
5.  When ready, select the Install Packages option.
6.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? Yes//", respond "YES."
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond "YES."
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond YES. When prompted to select the options you would like to place out of order, enter the following:

> OR OE/RR MENU CLINICIAN CPRS Clinician Menu

> OR OE/RR MENU NURSE CPRS Nurse Menu

> OR OE/RR MENU WARD CLERK CPRS Ward Clerk Menu

> OR CPRS GUI CHART

9.  When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'
10. Move the routines to other CPUs if appropriate.

<span id="_Toc283725438" class="anchor"></span>CPRS GUI v28 Software Installation Sequence

1.  Make sure all Nationally Released Required patches are installed.
- 
- OR\*3.0\*67
- OR\*3.0\*181
- OR\*3.0\*295
- OR\*3.0\*296
- OR\*3.0\*302
- OR\*3.0\*307
- OR\*3.0\*316
- OR\*3.0\*330
- GMRC\*3.0\*68
- LR\*5.2\*395
- PSS\*1.0\*147
- SD\*5.3\*536
- XU\*8.0\*474
- POLYTRAUMA MARKER 1.0
- PXRM\*2.0\*17
- USR\*1.0\*33
2.  Install PSS\*1.0\*151. Distributed as PSS_1_151.KID host file.

    Please refer to the CPRS GUI v28 Installation Capture for installation details.
3.  Install PSS\*1.0\*142. Distributed as PSS_1_142.KID host file.

    Please refer to the CPRS GUI v28 Installation Capture for installation details.
4.  Install OR\*3.0\*293, GMRC\*3.0\*66 and GMRA\*4.0\*45. Distributed in CPRS28_REQUIRED.KID host file.

> **NOTE:** The OR\*3\*293 patch schedules a task which converts the entries that are currently in file 100 on node 9 of each order and puts them into the new file 100.05.  This process may take a long time and thus the patch should be installed when the system is not highly loaded.  Also, since the task takes the current data from file 100 it is possible that control characters that existed there could get copied over into the new file as well.

 

Further Note:

As the above said task will create new entries in file 100.05 based off of existing order checks in file 100, file 100.05 has the potential to grow to a large size.  Depending on your system configuration, this may cause you to need extra journal files.  If you are monitoring the system and notice you need to allocate additional system resources for this task/process you may kill off the task in order to perform the necessary tasks. Once you are ready you will then need to restart the process by running the following at programmer prompt:

 

D TASK^ORY293

> The task will pick back up where it left off when you killed off the original task.

Please refer to the CPRS GUI v28 Installation Capture for installation details.

5.  Install OR\*3.0\*280 (CPRS GUI v28), PSJ\*5.0\*226 and PXRM\*2.0\*16:  Distributed in OR_PSJ_PXRM_28.KID host file.

Please refer to the CPRS GUI v28 Installation Capture for installation details.

6.  Install GMRC\*3.0\*64, GMTS\*2.7\*90 and OR\*3.0\*337. Distributed as CPRS28_RELATED.KID host file.

Please refer to the CPRS GUI v28 Installation Capture for installation details.

> **NOTE:** The OR\*3\*337 patch adds a new option, IV Additive Frequency Utility

\[OR IV ADD FREQ UTILITY\] to the existing ORDER MENU MANAGEMENT \[ORCM MENU\]. This new option allows the Clinical Application Coordinators (CACs) to define an additive frequency value to existing Continuous IV Quick Orders. Input from Pharmacy ADPAC is recommended.

7.  Distribute CPRSCHART.EXE, CPRS.HLP, CPRS.CNT located in OR_30_280.ZIP.

These three files should be distributed to the same directory as the borlndmm.dll. Usually, these files are located in the CPRS directory.

8.  Place the User and Technical Manual files in a location that can be accessed by CPRS users.
9.  After CPRS v28 is installed into production, do the following:

> a\) Review the new or changed Parameters exported with CPRS GUI v28 (see listing below). You will need to set the values for all new parameters.

> b\) Review the Quick Orders Mail Man message generated when you installed OR\*3.0\*280 (Subj: Order Check Compiler Status) or generate a new message by running the following option:

MR Medication Quick Order Report \[OR MEDICATION QO CHECKER\] which is located on ORDER MENU MANAGEMENT \[ORCM MGM\]

> c\) Correct the Continuous IV quick orders you have identified. Use the utility provided with patch OR\*3.0\*337.<span id="Evalute_IV_Additives_and_solutions" class="anchor"></span>

Parameters Introduced/Changed with CPRS GUI v28

- Enhance ORWOR CATEGORY SEQUENCE Parameter Definition to Include USER as a Selection (Remedy 105173, CQ 16601) – Developers added the User-level setting for the parameter.
- Modify the OR RA RFS CARRY ON Parameter to Include Division, Location, User, Service, System and Package Levels (CQ 16920) –As requested, this parameter was expanded to have more levels at which it can be set: Package, System, Division, Service, and User.
- Two CPRS Parameters Have the Same Parameter Description (Remedy 69631, CQ 17700) –While researching the similar descriptions, developers discovered that the parameter ORW ADDORD INPT was no longer in use. The CPRS GUI v.28 installation will delete this parameter at sites. In addition, the developers added to the ORWOR WRITE ORDER LIST parameter description that it has been superseded by the parameter ORWDX WRITE ORDERS LIST and that it is there only for backwards compatibility.
- VBECS: Test Site Wants a Parameter for Changing Order of Diagnostic Tests (Remedy 380789, CQ 18426) – Developers added a new parameter OR VBECS DIAGNOSTIC TEST ORDER to enable sites to rearrange the order of diagnostic tests at the System, Division, or User level. Sites can change sequence numbers to put the list of tests in whatever order the site chooses. The site can also remove a test from the list by deleting the corresponding sequence number.
- Need Parameter ORWT TOOLS MENU Description Updated for Submenu Info (Remedy 162367, CQ 19054) – Developers changed the description to reflect the changes to this parameter.
- VBECS QO without a Start Date Is Rejected by VBECS with a Message Sent to Provider (Remedy 379127, CQ 19097) – Developers corrected the problem and the start date will now be stored and sent correctly. Based on the collection type, the start date will have a default value, which the user can change if needed.
-   
  > VBECS: A Site Requested a Parameter that Removes Collection Date/Time Defaults e.g., NOW (CQ 19167) – CPRS developers created a new parameter OR VBECS REMOVE COLL TIME to enable the sites to remove the Collection Time Default when entering Diagnostic Test orders. The parameter has no affect on Quick orders. Quick order values will be displayed.
- VBECS Create a Parameter that Would Allow Sites to Change Diagnostic Side with Blood Component Side (CQ 19266) – Developers created a new parameter, OR VBECS DIAGNOSTIC PANEL 1ST, to enable users to switch the location of the panels. This parameter can be set at the Package, System, and Division levels.

<span id="_Toc283725440" class="anchor"></span>CPRS GUI v28 Software

<span id="_Toc283725655" class="anchor"></span>Patches Not Included in a bundle

| PATCH     | SUPPORTED FUNCTIONALITY |
|---------------|-----------------------------|
| PSS\*1.0\*151 | API for IV bag value        |
| PSS\*1.0\*142 | IV route changes            |

> CPRS28_REQUIRED.KID

| PATCH     | SUPPORTED FUNCTIONALITY           |
|---------------|---------------------------------------|
| OR\*3.0\*293  | Centralize repository for Oder Checks |
| GMRA\*4.0\*45 | Update for Allergy Order Check        |
| GMRC\*3.0\*66 | Addition of earliest appropriate date |

<span id="_Toc287445019" class="anchor"></span>OR_PSJ_PXRM_28.KID-- PRIMARY BUILD

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PATCH</strong></th>
<th><strong>SUPPORTED FUNCTIONALITY</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR*3.0*280</td>
<td>Primary OR patch for CPRS GUI v28</td>
</tr>
<tr class="even">
<td>PSJ*5.0*226</td>
<td><p>Primary Inpatient Medications patch</p>
<p>supporting IV bag information in medical dialog</p></td>
</tr>
<tr class="odd">
<td>PXRM*2.0*16</td>
<td><p>Primary Clinical Reminders patch</p>
<p>supporting reminders order checks</p></td>
</tr>
</tbody>
</table>

> CPRS28_RELATED.KID

| PATCH     | SUPPORTED FUNCTIONALITY               |
|---------------|-------------------------------------------|
| GMRC\*3.0\*64 | Support Attention Line Audit Trail        |
| GMTS\*2.7\*90 | Update to Health Summary to support (EAD) |
| OR\*3.0\*337  | Update IV Quick Order utility             |

  
OR_30_280.ZIP

|                 |             |                                                                        |
|-----------------|-------------|------------------------------------------------------------------------|
| FILE        | VERSION | CONTENTS                                                           |
| CPRSChart.exe   | 1.0.28.24   | CPRS GUI v28.24                                                        |
| CPRS.CNT        | N/A         | CPRS help contents file                                                |
| CPRS.HLP        | N/A         | CPRS help file                                                         |
| CPRSGUITM.PDF   | N/A         | CPRS GUI Technical Manual                                              |
| CPRSGUITM.DOC   | N/A         | CPRS GUI Technical Manual (Word version)                               |
| CPRSGUIUM.PDF   | N/A         | CPRS GUI User Manual                                                   |
| CPRSGUIUM.DOC   | N/A         | CPRS GUI User Manual (Word version)                                    |
| CPRSLMTM.PDF    | N/A         | CPRS LM Technical Manual                                               |
| CPRSLMTM.doc    | N/A         | CPRS LM Technical Manual (Word version)                                |
| OR_30_280IG.PDF | N/A         | CPRS GUI v.28 and Associated Patches Installation Guide                |
| OR_30_280IG.DOC | N/A         | CPRS GUI v.28 and Associated Patches Installation Guide (Word Version) |
| OR_30_280RN.PDF | N/A         | CPRS v28 Release Notes                                                 |
| OR_30_280RN.doc | N/A         | CPRS GUI V28 Release Notes (Word Version)                              |

<span id="_Toc283725442" class="anchor"></span>CPRS GUI v28 and Associated Patches Software Installation Captures

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option: INSTALLation

<span id="_Toc283725443" class="anchor"></span>PSS\*1\*151 Installation Capture

6 Install Package(s)

Select INSTALL NAME: PSS\*1.0\*151 1/11/11@14:52:52

=\> PSS\*1\*151

This Distribution was loaded on Jan 11, 2011@14:52:52 with header of

PSS\*1\*151

It consisted of the following Install(s):

PSS\*1.0\*151

Checking Install for Package PSS\*1.0\*151

Install Questions for PSS\*1.0\*151

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET TERMINAL

25 50 75

PSS\*1.0\*151

Install Started for PSS\*1.0\*151 :

Jan 11, 2011@14:54:39

Build Distribution Date: Oct 28, 2009

Installing Routines

25 50 75

Updating Routine file...

25 50 75

Updating KIDS files...

25 50 75 100

PSS\*1.0\*151 Installed.

Jan 11, 2011@14:54:39

Not a production UCI

NO Install Message sent

Install Completed

<span id="_Toc287445022" class="anchor"></span>PSS\*1\*142 Installation Capture

6 Install Package(s)

Select INSTALL NAME: PSS\*1.0\*142 1/11/11@14:55:48

=\> PSS\*1\*142

This Distribution was loaded on Jan 11, 2011@14:55:48 with header of

PSS\*1\*142

It consisted of the following Install(s):

PSS\*1.0\*142

Checking Install for Package PSS\*1.0\*142

Install Questions for PSS\*1.0\*142

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET TERMINAL

25 50 75

Complete

PSS\*1.0\*142

Install Started for PSS\*1.0\*142 :

Jan 11, 2011@14:57:08

Build Distribution Date: Oct 08, 2009

Installing Routines:

25 50 75 100

Jan 11, 2011@14:57:08

Updating Routine file...

25 50 75 100

Updating KIDS files...

25 50 75 100

PSS\*1.0\*142 Installed.

Jan 11, 2011@14:57:08

Not a production UCI

NO Install Message sent

Install Completed

<span id="_Toc287445023" class="anchor"></span>CPRS28_REQUIRED.KID Installation Capture

Select INSTALL NAME: CPRS28 REQUIRED 1.0 2/10/11@14:08:39

=\> CPRS28 REQUIRED PATCHES ;Created on Feb 10, 2011@10:53:25

This Distribution was loaded on Feb 10, 2011@14:08:39 with header of

CPRS28 REQUIRED PATCHES ;Created on Feb 10, 2011@10:53:25

It consisted of the following Install(s):

CPRS28 REQUIRED 1.0 OR\*3.0\*293 GMRA\*4.0\*45 GMRC\*3.0\*66

Checking Install for Package CPRS28 REQUIRED 1.0

Install Questions for CPRS28 REQUIRED 1.0

Checking Install for Package OR\*3.0\*293

Install Questions for OR\*3.0\*293

Incoming Files:

100.05 ORDER CHECK INSTANCES

Checking Install for Package GMRA\*4.0\*45

Install Questions for GMRA\*4.0\*45

Checking Install for Package GMRC\*3.0\*66

Install Questions for GMRC\*3.0\*66

Incoming Files:

123 REQUEST/CONSULTATION (Partial Definition)

> **NOTE:** You already have the 'REQUEST/CONSULTATION' File.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET TERMINAL

25 50 75 Complete

CPRS28 REQUIRED 1.0

Install Started for CPRS28 REQUIRED 1.0 :

Feb 10, 2011@14:12

Build Distribution Date: Feb 10, 2011

Installing Routines

25 50 75

Feb 10, 2011@14:12

OR\*3.0\*293

Install Started for OR\*3.0\*293 :

Feb 10, 2011@14:12

Build Distribution Date: Feb 10, 2011

Installing Routines:

25 50 75

Feb 10, 2011@14:12

Installing Data Dictionaries:

25 50 75 100

Feb 10, 2011@14:12

Running Post-Install Routine: POST^ORY293

25 50 75

A background job has been queued to convert order checks from file 100 to file 100.05.

Task \#4301 started.

Updating Routine file:

25 50 75 100

Updating KIDS files:

25 50 75 100

OR\*3.0\*293 Installed.

Feb 10, 2011@14:12

Not a production UCI

NO Install Message sent

GMRA\*4.0\*45

Install Started for GMRA\*4.0\*45 :

Feb 10, 2011@14:12

Build Distribution Date: Feb 10, 2011

Installing Routines:

25 50 75 100

Feb 10, 2011@14:12

Updating Routine file:

25 50 75 100

Updating KIDS files...

25 50 75 100

GMRA\*4.0\*45 Installed.

Feb 10, 2011@14:12

Not a production UCI

NO Install Message sent

GMRC\*3.0\*66

Install Started for GMRC\*3.0\*66 :

Feb 10, 2011@14:12

Build Distribution Date: Feb 10, 2011

Installing Routines:

25 50 75 100

Feb 10, 2011@14:12:01

Installing Data Dictionaries:

25 50 75 100

Feb 10, 2011@14:12:01

Updating Routine file...

25 50 75 100

Updating KIDS files...

25 50 75 100

GMRC\*3.0\*66 Installed.

Feb 10, 2011@14:12:01

Not a production UCI

NO Install Message sent

Updating Routine file...

25 50 75 100

CPRS28 REQUIRED 1.0 Installed.

Feb 10, 2011@14:12:01

No link to PACKAGE file

NO Install Message sent

Install Completed

> **NOTE:** The OR\*3\*293 patch schedules a task that converts the entries currently in file 100 on node 9 of each order and puts them into the new file 100.05. This process may take a long time and thus the patch should be installed when the system is not highly loaded. Also, since the task takes the current data from file 100 it is possible that control characters that existed there could get copied over into the new file as well.

 

Further Note:

As the above said task will create new entries in file 100.05 based off of existing order checks in file 100, file 100.05 has the potential to grow to a large size.  Depending on your system configuration, this may cause you to need extra journal files.  If you are monitoring the system and notice you need to allocate additional system resources for this task/process you may kill off the task in order to perform the necessary tasks. Once you are ready you will then need to restart the process by running the following at programmer prompt:

 

D TASK^ORY293

> The task will pick back up where it left off when you killed off the original task.

<span id="_Toc287445024" class="anchor"></span>OR_PSJ_PXRM_28.KID Installation Capture

<span id="_Toc283725444" class="anchor"></span>Checksum Value Verification

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

2 Verify Checksums in Transport GlobalSelect INSTALL NAME: OR PSJ PXRM 280 1.0 1/11/11@15:08:19=\> CPRS28 AND REQUIRED PATCHES ;Created on Dec 07, 2010@11:59:33This Distribution was loaded on Jan 11, 2011@15:08:19 with header ofCPRS28 AND REQUIRED PATCHES ;Created on Dec 07, 2010@11:59:33It consisted of the following Install(s):OR PSJ PXRM 280 1.0 OR\*3.0\*280 PSJ\*5.0\*226 PXRM\*2.0\*16Want each Routine Listed with Checksums: Yes// YESDEVICE: HOME// TELNET TERMINALPACKAGE: OR PSJ PXRM 280 1.0 Jan 11, 2011 3:09 pm PAGE 1-------------------------------------------------------------------------0 Routine checked, 0 failed.PACKAGE: OR\*3.0\*280 Jan 11, 2011 3:09 pm PAGE 1-------------------------------------------------------------------------ORB3SPEC Calculated 89326077ORCDPS1 Calculated 78578103ORCDPSIV Calculated 121037905ORCHECK Calculated 109684735ORCMEDT8 Calculated 78288682ORCNOTE Calculated 59596403ORCSAVE Calculated 92624396ORCSAVE1 Calculated 34248374ORCSAVE2 Calculated 84878914ORCSEND3 Calculated 25737895ORCXPND1 Calculated 72214647ORCXPND3 Calculated 43846714ORDSGCHK Calculated 89700507OREVNTX Calculated 77019944OREVNTX1 Calculated 75868849ORKCHK Calculated 42414888Enter RETURN to continue or '^' to exit:PACKAGE: OR\*3.0\*280 Jan 11, 2011 3:09 pm PAGE 2-------------------------------------------------------------------------ORKCHK5 Calculated 45867526ORKCHK6 Calculated 31072886ORMBLDGM Calculated 5247581ORMBLDP1 Calculated 5382020ORMBLDPS Calculated 86048776ORMFN Calculated 37182976ORMGMRC Calculated 44816636ORMPS1 Calculated 70284401ORMPS2 Calculated 47758235ORORDDSC Calculated 13143468ORQ2 Calculated 52016905ORQQCN2 Calculated 33486661ORQQPL1 Calculated 62165510ORQQPL3 Calculated 54712722ORTSKLPS Calculated 6566762ORUTL Calculated 8567087ORWCV Calculated 80219268Enter RETURN to continue or '^' to exit:PACKAGE: OR\*3.0\*280 Jan 11, 2011 3:09 pm PAGE 3-------------------------------------------------------------------------ORWD Calculated 39271044ORWDPS3 Calculated 20975704ORWDPS33 Calculated 40244944ORWDRA32 Calculated 21891696ORWDX Calculated 66882759ORWDX2 Calculated 17614403ORWDXA Calculated 82710229ORWDXC Calculated 52838872ORWDXM1 Calculated 71014486ORWDXM2 Calculated 76107854ORWDXM3 Calculated 104533418ORWDXM4 Calculated 37881489ORWDXR01 Calculated 20020938ORWDXVB3 Calculated 1399631ORWGAPI3 Calculated 30897218ORWGAPIR Calculated 41610059ORWGAPIU Calculated 23850893Enter RETURN to continue or '^' to exit:PACKAGE: OR\*3.0\*280 Jan 11, 2011 3:09 pm PAGE 4-------------------------------------------------------------------------ORWIB Calculated 5804851ORWLRR Calculated 12620243ORWLRRG Calculated 24435305ORWLRRG1 Calculated 42759995ORWOD Calculated 75747824ORWOD1 Calculated 41715088ORWOR Calculated 42631980ORWORR Calculated 67327939ORWPCE Calculated 60867098ORWPCE1 Calculated 63538675ORWPCE3 Calculated 43187706ORWPS Calculated 65159605ORWPT Calculated 60483737ORWPT1 Calculated 15675921ORWRP Calculated 77042419ORWTPR Calculated 16455738ORY280 Calculated 95955808Enter RETURN to continue or '^' to exit:PACKAGE: OR\*3.0\*280 Jan 11, 2011 3:09 pm PAGE 5-------------------------------------------------------------------------ORY2800 Calculated 15643771ORY28001 Calculated 71483826ORY28002 Calculated 78087672ORY28003 Calculated 89106334ORY28004 Calculated 57739965ORY28005 Calculated 65374324ORY28006 Calculated 62557827ORY28007 Calculated 55829468ORY2801 Calculated 40551743ORY2802 Calculated 26766910ORY2803 Calculated 12996879ORY2804 Calculated 13526807ORY280ES Calculated 12630040ORY280P Calculated 3900420ORYDLG Calculated 1451530582 Routines checked, 0 failed.PACKAGE: PSJ\*5.0\*226 Jan 11, 2011 3:09 pm PAGE 1-------------------------------------------------------------------------PSJHL3 Calculated 66158358PSJHL4 Calculated 75570898PSJHL4A Calculated 580722193 Routines checked, 0 failed.PACKAGE: PXRM\*2.0\*16 Jan 11, 2011 3:09 pm PAGE 1-------------------------------------------------------------------------PXRM Calculated 34249926PXRMDEDT Calculated 86324286PXRMDEV Calculated 28974848PXRMDLG4 Calculated 92764011PXRMDLLB Calculated 39413514PXRMEXIC Calculated 65705401PXRMEXPD Calculated 192354344PXRMEXPS Calculated 186431616PXRMEXU1 Calculated 36300309PXRMEXU5 Calculated 39432783PXRMFNFT Calculated 58241703PXRMFRPT Calculated 103832616PXRMINTR Calculated 37092667PXRMORCH Calculated 212664484PXRMORHL Calculated 9594664PXRMORXR Calculated 75991552Enter RETURN to continue or '^' to exit:PACKAGE: PXRM\*2.0\*16 Jan 11, 2011 3:09 pm  
PAGE 2-------------------------------------------------------------------------PXRMP16I Calculated 422881PXRMPSN Calculated 28129650PXRMREV Calculated 12256539PXRMRPCA Calculated 64569743PXRMRPCD Calculated 1106007521 Routines checked, 0 failed.

<span id="_Toc283725445" class="anchor"></span>Transport Global Print

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

3 Print Transport Global

Select INSTALL NAME: OR PSJ PXRM 280 1.0 1/11/11@15:08:19

=\> CPRS28 AND REQUIRED PATCHES ;Created on Dec 07, 2010@11:59:33

This Distribution was loaded on Jan 11, 2011@15:08:19 with header of

CPRS28 AND REQUIRED PATCHES ;Created on Dec 07, 2010@11:59:33

It consisted of the following Install(s):

OR PSJ PXRM 280 1.0 OR\*3.0\*280 PSJ\*5.0\*226 PXRM\*2.0\*16

Select one of the following:

1 Print Summary

2 Print Summary and Routines

3 Print Routines

What to Print: 1 Print Summary

DEVICE: HOME// ;;9999 TELNET TERMINAL

PACKAGE: OR PSJ PXRM 280 1.0 Jan 11, 2011 3:09 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: MULTI-PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: ALPHA/BETA TESTING: NO

DESCRIPTION:

SEQUENCE OF BUILDS:

1 OR\*3.0\*280 Required to Continue

2 PSJ\*5.0\*226 Required to Continue

3 PXRM\*2.0\*16 Required to Continue

Enter RETURN to continue or '^' to exit: PACKAGE: OR\*3.0\*280 Jan 11, 2011 3:09 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: ORDER ENTRY/RESULTS REPORTING ALPHA/BETA TESTING: NO

DESCRIPTION:

The description of this patch may be found in the National Patch Module

under OR\*3\*280.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: POST^ORY280 DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

100 ORDER YES NO NO

100.05 ORDER CHECK INSTANCES YES YES NO

100.5 OE/RR RELEASE EVENTS YES NO NO NO

Partial DD: subDD: 100.5 fld: 2

101.41 ORDER DIALOG NO NO YES REPL YES NO

DATA SCREEN: I \$\$SENDDLG^ORY280(\$P(^(0),U))

101.43 ORDERABLE ITEMS YES NO NO

BULLETIN: ACTION:

OR PROBLEM NTRT BULLETIN SEND TO SITE

MAIL GROUP: ACTION:

OR CACS SEND TO SITE

ROUTINE: ACTION:

ORB3SPEC SEND TO SITE

ORCDPS1 SEND TO SITE

ORCDPSIV SEND TO SITE

ORCHECK SEND TO SITE

ORCMEDT8 SEND TO SITE

ORCNOTE SEND TO SITE

ORCSAVE SEND TO SITE

ORCSAVE1 SEND TO SITE

ORCSAVE2 SEND TO SITE

ORCSEND3 SEND TO SITE

ORCXPND1 SEND TO SITE

ORCXPND3 SEND TO SITE

ORDSGCHK SEND TO SITE

OREVNTX SEND TO SITE

OREVNTX1 SEND TO SITE

ORKCHK SEND TO SITE

ORKCHK5 SEND TO SITE

ORKCHK6 SEND TO SITE

ORMBLDGM SEND TO SITE

ORMBLDP1 SEND TO SITE

ORMBLDPS SEND TO SITE

ORMFN SEND TO SITE

ORMGMRC SEND TO SITE

ORMPS1 SEND TO SITE

ORMPS2 SEND TO SITE

ORORDDSC SEND TO SITE

ORQ2 SEND TO SITE

ORQQCN2 SEND TO SITE

ORQQPL1 SEND TO SITE

ORQQPL3 SEND TO SITE

ORTSKLPS SEND TO SITE

ORUTL SEND TO SITE

ORWCV SEND TO SITE

ORWD SEND TO SITE

ORWDPS3 SEND TO SITE

ORWDPS33 SEND TO SITE

ORWDRA32 SEND TO SITE

ORWDX SEND TO SITE

ORWDX2 SEND TO SITE

ORWDXA SEND TO SITE

ORWDXC SEND TO SITE

ORWDXM1 SEND TO SITE

ORWDXM2 SEND TO SITE

ORWDXM3 SEND TO SITE

ORWDXM4 SEND TO SITE

ORWDXR01 SEND TO SITE

ORWDXVB3 SEND TO SITE

ORWGAPI3 SEND TO SITE

ORWGAPIR SEND TO SITE

ORWGAPIU SEND TO SITE

ORWIB SEND TO SITE

ORWLRR SEND TO SITE

ORWLRRG SEND TO SITE

ORWLRRG1 SEND TO SITE

ORWOD SEND TO SITE

ORWOD1 SEND TO SITE

ORWOR SEND TO SITE

ORWORR SEND TO SITE

ORWPCE SEND TO SITE

ORWPCE1 SEND TO SITE

ORWPCE3 SEND TO SITE

ORWPS SEND TO SITE

ORWPT SEND TO SITE

ORWPT1 SEND TO SITE

ORWRP SEND TO SITE

ORWTPR SEND TO SITE

ORY280 SEND TO SITE

ORY2800 SEND TO SITE

ORY28001 SEND TO SITE

ORY28002 SEND TO SITE

ORY28003 SEND TO SITE

ORY28004 SEND TO SITE

ORY28005 SEND TO SITE

ORY28006 SEND TO SITE

ORY28007 SEND TO SITE

ORY2801 SEND TO SITE

ORY2802 SEND TO SITE

ORY2803 SEND TO SITE

ORY2804 SEND TO SITE

ORY280ES SEND TO SITE

ORY280P SEND TO SITE

ORYDLG SEND TO SITE

OPTION: ACTION:

OR CPRS GUI CHART SEND TO SITE

PROTOCOL: ACTION:

OR ITEM RECEIVE SEND TO SITE

PARAMETER DEFINITION: ACTION:

OR RA RFS CARRY ON SEND TO SITE

OR RADIOLOGY ISSUES SEND TO SITE

OR RADIOLOGY MAILGROUP DELETE AT SITE

OR VBECS COMPONENT ORDER SEND TO SITE

OR VBECS DIAGNOSTIC PANEL 1ST SEND TO SITE

OR VBECS DIAGNOSTIC TEST ORDER SEND TO SITE

OR VBECS REMOVE COLL TIME SEND TO SITE

ORW ADDORD INPT DELETE AT SITE

ORWOR CATEGORY SEQUENCE SEND TO SITE

ORWOR WRITE ORDERS LIST SEND TO SITE

ORWT TOOLS MENU SEND TO SITE

REMOTE PROCEDURE: ACTION:

ORCHECK DELMONO SEND TO SITE

ORCHECK GETMONO SEND TO SITE

ORCHECK GETMONOL SEND TO SITE

ORCHECK GETXTRA SEND TO SITE

ORCHECK ISMONO SEND TO SITE

ORCNOTE GET TOTAL SEND TO SITE

ORQQCN ISPROSVC SEND TO SITE

ORQQPL PROBLEM NTRT BULLETIN SEND TO SITE

ORWDPS33 GETADDFR SEND TO SITE

ORWDPS33 IVDOSFRM SEND TO SITE

ORWDXVB3 COLLTIM SEND TO SITE

ORWDXVB3 DIAGORD SEND TO SITE

ORWDXVB3 SWPANEL SEND TO SITE

ORWPCE GET DX TEXT SEND TO SITE

INSTALL QUESTIONS:

Default Rebuild Menu Trees Upon Completion of Install: YES

Default INHIBIT LOGONs during the install: NO

Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

REQUIRED BUILDS: ACTION:

OR\*3.0\*67 Don't install, leave global

OR\*3.0\*181 Don't install, leave global

PSS\*1.0\*142 Don't install, leave global

OR\*3.0\*295 Don't install, leave global

OR\*3.0\*302 Don't install, leave global

OR\*3.0\*293 Don't install, leave global

PSS\*1.0\*147 Don't install, leave global

SD\*5.3\*536 Don't install, leave global

PSS\*1.0\*151 Don't install, leave global

LR\*5.2\*395 Don't install, leave global

OR\*3.0\*307 Don't install, leave global

OR\*3.0\*330 Don't install, leave global

Enter RETURN to continue or '^' to exit: \[H\[J\[2J\[HPACKAGE: PSJ\*5.0\*226 Jan 11, 2011 3:09 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: INPATIENT MEDICATIONS ALPHA/BETA TESTING: NO

DESCRIPTION:

Provide dosing checks for Unit Dose and IV orders.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

ROUTINE: ACTION:

PSJHL3 SEND TO SITE

PSJHL4 SEND TO SITE

PSJHL4A SEND TO SITE

INSTALL QUESTIONS:

Default Rebuild Menu Trees Upon Completion of Install: NO

Default INHIBIT LOGONs during the install: NO

Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

REQUIRED BUILDS: ACTION:

PSJ\*5.0\*197 Don't install, leave global

Enter RETURN to continue or '^' to exit: PACKAGE: PXRM\*2.0\*16 Jan 11, 2011 3:09 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: CLINICAL REMINDERS ALPHA/BETA TESTING: NO

DESCRIPTION:

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: PRE^PXRMP16I DELETE PRE-INIT ROUTINE: No

POST-INIT ROUTINE: DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

801 REMINDER ORDERABLE ITEM GROUP YES NO NO

811.9 REMINDER DEFINITION YES NO NO

PRINT TEMPLATE: ACTION:

PXRM ORDERABLE ITEM GROUP LIST FILE \#801 SEND TO SITE

INPUT TEMPLATE: ACTION:

PXRM EDIT ORDER CHECK FILE \#801 SEND TO SITE

ROUTINE: ACTION:

PXRM SEND TO SITE

PXRMDEDT SEND TO SITE

PXRMDEV SEND TO SITE

PXRMDLG4 SEND TO SITE

PXRMDLLB SEND TO SITE

PXRMEXIC SEND TO SITE

PXRMEXPD SEND TO SITE

PXRMEXPS SEND TO SITE

PXRMEXU1 SEND TO SITE

PXRMEXU5 SEND TO SITE

PXRMFNFT SEND TO SITE

PXRMFRPT SEND TO SITE

PXRMINTR SEND TO SITE

PXRMORCH SEND TO SITE

PXRMORHL SEND TO SITE

PXRMORXR SEND TO SITE

PXRMP16I SEND TO SITE

PXRMPSN SEND TO SITE

PXRMREV SEND TO SITE

PXRMRPCA SEND TO SITE

PXRMRPCD SEND TO SITE

OPTION: ACTION:

PXRM MANAGERS MENU USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PXRM ORDERABLE ITEM GROUP EDIT SEND TO SITE

PXRM ORDERABLE ITEM GROUP INQ SEND TO SITE

PXRM ORDERABLE ITEM GROUP MENU SEND TO SITE

PXRM ORDERABLE ITEM TESTER SEND TO SITE

PROTOCOL: ACTION:

OR ITEM RECEIVE USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PXRM ORDER CHECK UPDATES SEND TO SITE

INSTALL QUESTIONS:

Default Rebuild Menu Trees Upon Completion of Install: NO

Default INHIBIT LOGONs during the install: NO

Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

REQUIRED BUILDS: ACTION:

PXRM\*2.0\*17 Don't install, leave global

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option:

<span id="_Toc287445027" class="anchor"></span>OR_PSJ_PXRM_28.KID Installation Capture

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

6 Install Package(s)

Select INSTALL NAME: OR PSJ PXRM 280 1.0 1/11/11@15:08:19

=\> CPRS28 AND REQUIRED PATCHES ;Created on Dec 07, 2010@11:59:33

This Distribution was loaded on Jan 11, 2011@15:08:19 with header of

CPRS28 AND REQUIRED PATCHES ;Created on Dec 07, 2010@11:59:33

It consisted of the following Install(s):

OR PSJ PXRM 280 1.0 OR\*3.0\*280 PSJ\*5.0\*226 PXRM\*2.0\*16

Checking Install for Package OR PSJ PXRM 280 1.0

Install Questions for OR PSJ PXRM 280 1.0

Checking Install for Package OR\*3.0\*280

Install Questions for OR\*3.0\*280

Incoming Files:

100 ORDER

> **NOTE:** You already have the 'ORDER' File.

100.05 ORDER CHECK INSTANCES

> **NOTE:** You already have the 'ORDER CHECK INSTANCES' File.

100.5 OE/RR RELEASE EVENTS (Partial Definition)

> **NOTE:** You already have the 'OE/RR RELEASE EVENTS' File.

101.41 ORDER DIALOG (including data)

> **NOTE:** You already have the 'ORDER DIALOG' File.

I will REPLACE your data with mine.

101.43 ORDERABLE ITEMS

> **NOTE:** You already have the 'ORDERABLE ITEMS' File.

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'OR CACS': CPRSIRM, STAFF JS 192

OI&T STAFF

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Checking Install for Package PSJ\*5.0\*226

Install Questions for PSJ\*5.0\*226

Checking Install for Package PXRM\*2.0\*16

Install Questions for PXRM\*2.0\*16

Incoming Files:

801 REMINDER ORDERABLE ITEM GROUP

811.9 REMINDER DEFINITION

> **NOTE:** You already have the 'REMINDER DEFINITION' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Want KIDS to INHIBIT LOGONs during the install? YES//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU CLINICIAN      

CPRS Clinician Menu

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU NURSE       CPRS

 Nurse Menu

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU WARD CLERK     

 CPRS Ward Clerk Menu

Enter options you wish to mark as 'Out Of Order': OR CPRS GUI CHART       CPRSCh

art version 1.0.27.90

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes):  (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET TERMINAL

Complete

OR PSJ PXRM 280 1.0

Install Started for OR PSJ PXRM 280 1.0 :

Jan 11, 2011@15:11:47

Build Distribution Date: Dec 07, 2010

Installing Routines:

25 50 75

Jan 11, 2011@15:11:47 OR\*3.0\*280

Install Started for OR\*3.0\*280 :

Jan 11, 2011@15:11:47

Build Distribution Date: Dec 07, 2010

Installing Routines

25 50 75 100

Jan 11, 2011@15:11:48

Installing Data Dictionaries:

25 50 75 100

Jan 11, 2011@15:11:49

Installing Data: ......................................

Jan 11, 2011@15:11:53

Installing PACKAGE COMPONENTS:

Installing BULLETIN

25 50 75 100

Installing MAIL GROUP

25 50 75 100

Installing PROTOCOL

25 50 75 100

Installing REMOTE PROCEDURE

25 50 75 100

Installing OPTION

25 50 75 100

Installing PARAMETER DEFINITION

25 50 75 100

Jan 11, 2011@15:12:09

Running Post-Install Routine: POST^ORY280

25 50 75

Nature of Order file entry 'Service Reject' renamed to 'Rejected by Service'.

Session Order Dialog setting update has been queued, task number 4012 .

Order Check Expert System Rule Transporter

Created: MAR 3,2010 at 07:20 at CPRS28.FO-SLC.MED.VA.GOV

Current Date: JAN 11,2011 at 15:12 at CHY1K.FO-BAYPINES.MED.VA.GOV

Loading Data . . . . . . .

Installing '863.8 OCX MDD PARAMETER' records... .

25 50 75

. .

Installing '864.1 OCX MDD DATATYPE' records....

Installing '863.7 OCX MDD PUBLIC FUNCTION' records...

25 50 75

Installing '863.9 OCX MDD CONDITION/FUNCTION' records... . . .

25 50 75

Installing '863.4 OCX MDD ATTRIBUTE' records... . . . .

25 50 75

Installing '863.2 OCX MDD SUBJECT' records... .

Installing '863.3 OCX MDD LINK' records... .

25 50 75

Installing '860.9 ORDER CHECK NATIONAL TERM' records... . . . . . .

25 50 75

Installing '860.8 ORDER CHECK COMPILER FUNCTIONS' records... .

25 50 75

------------Inconsistent word Data---------------------------------

ORDER CHECK COMPILER FUNCTIONS: OPIOID MEDICATIONS \[56\]

CODE field \[100\] Line \#23

\(R\) CPRS28.FO-SLC.MED.VA.GOV: ; .;S DUPLEN=\$P(215/DUPI,".")

\(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: ; .S DUPLEN=\$P(215/DUPI,".")

Installing '860.6 ORDER CHECK DATA CONTEXT' records...

25 50 75

Installing '860.5 ORDER CHECK DATA SOURCE' records... . .

25 50 75

Installing '860.4 ORDER CHECK DATA FIELD' records... .

25 50 75

Installing '860.3 ORDER CHECK ELEMENT' records...

25 50 75

------------Inconsistent Data--------------------------------------

ORDER CHECK ELEMENT: NO ALLERGY ASSESSMENT \[136\]

CONDITIONAL EXPRESSION: 2 \[2\]

OPERATOR/FUNCTION field \[2\]

\(R\) CPRS28.FO-SLC.MED.VA.GOV: CONTAINS ELEMENT IN SET

\(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: EQ FREE TEXT

OPERATOR/FUNCTION: CONTAINS ELEMENT IN SET ...Correct data Filed

------------Inconsistent Data--------------------------------------

ORDER CHECK ELEMENT: NO ALLERGY ASSESSMENT \[136\]

CONDITIONAL EXPRESSION: 2 \[2\]

CONDITIONAL VALUE 1 field \[3\]

\(R\) CPRS28.FO-SLC.MED.VA.GOV: SELECT,SESSION

\(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: SELECT

CONDITIONAL VALUE 1: SELECT,SESSION ...Correct data Filed .

25 50 75

Installing '860.2 ORDER CHECK RULE' records... .

No data filing errors.

Transport Finished...

---Creating Order Check Routines-----------------------------------

25 50 75

Build list of Active Rules, Elements and Datafields

25 50 75

95 DATA FIELDS

78 ELEMENTS

38 RULES

25 50 75

Compile DataField Navigation code

25 50 75

100 DataField Navigation Code Arrays

25 50 75

Compile Element Evaluation code

25 50 75

72 Event Evaluation Code Arrays

25 50 75

Compile Element MetaCode

25 50 75

78 Element Metacode Arrays

25 50 75

Get Compiler Function Code...

25 50 75

51 Compiler Include Functions

25 50 75

Compile Rule Element Relation code...

25 50 75

54 Rule Element Relation Code Arrays

25 50 75

Construct Decision Tree...

25 50 75

699 Sub-Routines

25 50 75

Optimize Sub-Routines...

25 50 75

279 Sub-Routines

60.1% Optimization

25 50 75

Assemble Routines...

25 50 75

39 OCXOZ\* Routines

25 50 75 100

Updating Routine file...

25 50 75

The following Routines were created during this install:

ORD2

ORD21

ORD210

ORD211

ORD212

ORD213

ORD214

ORD22

ORD23

ORD24

ORD25

ORD26

ORD27

ORD28

ORD29

25 50 75 100

Updating KIDS files...

25 50 75 100

OR\*3.0\*280 Installed.

Jan 11, 2011@15:12:12

Not a production UCI

NO Install Message sent

PSJ\*5.0\*226

Install Started for PSJ\*5.0\*226 :

Jan 11, 2011@15:12:12

Build Distribution Date: Dec 07, 2010

Installing Routines

25 50 75 100

Jan 11, 2011@15:12:12

Updating Routine file...

25 50 75 100

Updating KIDS files...

25 50 75 100

PSJ\*5.0\*226 Installed.

Jan 11, 2011@15:12:12

Not a production UCI

NO Install Message sent

PXRM\*2.0\*16

Install Started for PXRM\*2.0\*16 :

Jan 11, 2011@15:12:12

Build Distribution Date: Dec 07, 2010

Installing Routines:

25 50 75 100

Jan 11, 2011@15:12:13

Running Pre-Install Routine: PRE^PXRMP16

25 50 75

Installing Data Dictionaries:

25 50 75 100

Jan 11, 2011@15:12:13

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

25 50 75 100

Installing INPUT TEMPLATE

25 50 75 100

Installing PROTOCOL

25 50 75

Located in the PXRM (CLINICAL REMINDERS) namespace.

25 50 75 100

Installing OPTION

25 50 75 100

Jan 11, 2011@15:12:13

Updating Routine file...

25 50 75 100

Updating KIDS files...

25 50 75 100

PXRM\*2.0\*16 Installed.

Jan 11, 2011@15:12:13

Not a production UCI

NO Install Message sent

Updating Routine file...

25 50 75

Updating KIDS files...

25 50 75 100

OR PSJ PXRM 280 1.0 Installed.

Jan 11, 2011@15:12:14

No link to PACKAGE file

NO Install Message sent

Call MENU rebuild

Rebuilding Menus

25 50 75

Starting Menu Rebuild: Jan 11, 2011@15:12:16

Collecting primary menus in the New Person file...

Primary menus found in the New Person file

------------------------------------------

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

XMUSER MailMan Menu 56 03/06/07 09/30/10

25 50 75

EVE Systems Manager Menu 19 01/11/11 09/30/10

25 50 75

XUCORE Core Applications 3 03/05/07 09/30/10

25 50 75

SDMGR Scheduling Manager's Menu 6 03/05/07 09/30/10

25 50 75

YSUSER Mental Health 5 03/05/07 09/30/10

25 50 75

SDAPP Appointment Menu 3 03/05/07 09/30/10

25 50 75

DOC Doctors' Special Menu 116 03/05/07 09/30/10

25 50 75

DGZMGR MAS MANAGER 58 03/05/07 09/30/10

25 50 75

WARD CLERK Ward Clerk 1 08/26/05 09/30/10

25 50 75

PSMENU Pharmacy 20 03/05/07 09/30/10

25 50 75

FHMGR Dietetics Management 7 03/05/07 09/30/10

25 50 75

RA TECHMENU Rad/Nuc Med Technologist ... 2 03/05/07 09/30/10

25 50 75

RA CLERKMENU Rad/Nuc Med Clerk Menu 1 02/28/07 09/30/10

25 50 75

RA TRANSCRIPTIONIST Rad/Nuc Med Transcription... 5 03/06/07 09/30/10

25 50 75

RA RADIOLOGIST Interpreting Physician Menu 18 03/05/07 09/30/10

25 50 75

RADIOLOGY SYSTEM Radiology 6 03/05/07 09/30/10

25 50 75

ENMGR Engineering Main Menu 9 03/05/07 09/30/10

25 50 75

ENPMINSP Engineering PM Clerk Main... 1 03/05/07 09/30/10

25 50 75

ENEVE Site Manager's Main Menu 2 03/05/07 09/30/10

25 50 75

LRZMENU Laboratory 10 03/05/07 09/30/10

25 50 75

NURSE INQUIRY Nurse Inquiry 84 03/06/07 09/30/10

25 50 75

XUSPY Information Security Offi... 2 03/05/07 09/30/10

25 50 75

PSCLERKSHIP Pharmacy Clerkship 1 02/28/07 09/30/10

25 50 75

FHUSR Dietetic User 1 03/05/07 09/30/10

25 50 75

FHTECH Clinical Dietetics 6 03/05/07 09/30/10

25 50 75

PERSONNEL MENU PERSONNEL MENU 2 03/05/07 09/30/10

25 50 75

COS MENU COS MENU 8 03/05/07 09/30/10

25 50 75

NURS-HN Head Nurse's Menu 8 03/05/07 09/30/10

25 50 75

NURS-QA QA Coordinator's Menu 1 03/05/07 09/30/10

25 50 75

NURS-RN Staff Nurse Menu 217 03/06/07 09/30/10

25 50 75

NURS-ALL Nursing Features (all opt... 2 03/05/07 09/30/10

25 50 75

LBRYZ MANAGER Library Management 2 03/05/07 09/30/10

25 50 75

SDZ OUTSIDESCHED SCHEDULING APPOINTMENTS (... 5 03/05/07 09/30/10

25 50 75

SDZ OUTSIDEAPPT APPOINTMENT MENU (NON MAS) 1 03/05/07 09/30/10

25 50 75

DGMGR MAS MANAGER 2 03/05/07 09/30/10

25 50 75

IB BILLING SUPERVISOR MENU

Billing Supervisor Menu 1 02/26/07 09/30/10

25 50 75

SOWK Information Management Sy... 11 03/05/07 09/30/10

25 50 75

VSMENU Voluntary Services' Menu 2 03/02/07 09/30/10

25 50 75

PRCHUSER MASTER Combined A&MM Menus 1 01/26/07 09/30/10

25 50 75

PRCHUSER PA Purchasing Agent 2 03/05/07 09/30/10

25 50 75

PRCHUSER PPM Accountable Officer Menu 1 03/02/07 09/30/10

25 50 75

PRCHUSER WHSE Warehouse 7 03/05/07 09/30/10

25 50 75

PRCF MASTER Funds Distribution & Acco... 1 03/01/07 09/30/10

25 50 75

PRCSCP OFFICIAL Control Point Official's ... 1 03/05/07 09/30/10

25 50 75

PRCSCP CLERK Control Point Clerk's Menu 5 03/05/07 09/30/10

25 50 75

PRCHPC PO Purchase Orders Menu 1 10/19/06 09/30/10

25 50 75

FHMGRC Clinical Management 1 03/05/07 09/30/10

25 50 75

ZCARDIOPULMONARY Cardiopulmonary Main Menu 6 03/05/07 09/30/10

25 50 75

FBAA MAIN MENU Fee Basis Main Menu 43 03/05/07 09/30/10

25 50 75

YSMANAGER MHS Manager 4 03/05/07 09/30/10

25 50 75

SROMENU Surgery Menu 11 03/05/07 09/30/10

25 50 75

DENTMANAGER Dental 4 03/05/07 09/30/10

25 50 75

CHAP MAIN MENU CHAPLAIN MAIN MENU 4 03/05/07 09/30/10

25 50 75

DGZ ADJ MAIN MENU ADJUDICATION MAIN MENU 3 09/07/04 09/30/10

25 50 75

PRCHPM RA MENU RA (Requirements Analyst)... 2 03/05/07 09/30/10

25 50 75

IB MANAGER MENU Integrated Billing Master... 5 03/05/07 09/30/10

25 50 75

XUSERTOOLS User's Toolbox 1 02/21/07 09/30/10

25 50 75

PRSD 05 EMPLOYEE INQUIRY MENU

Employee Inquiry/Reports ... 1 03/05/07 09/30/10

25 50 75

RMPR OFFICIAL Prosthetic Official's Menu 1 10/02/06 09/30/10

25 50 75

RMPR CLERK Prosthetic Clerk's Menu 4 03/05/07 09/30/10

25 50 75

ZQA MAIN QUALITY ASSURANCE MAIN MENU 1 03/05/07 09/30/10

25 50 75

AFQB USER BUILDING MANAGEMENT MENU 1 03/05/07 09/30/10

25 50 75

HL MAIN MENU HL7 Main Menu 1 06/08/05 09/30/10

25 50 75

PSO BINGO BOARD Bingo Board 1 03/05/07 09/30/10

25 50 75

ZKEY CONTROL MENU Key Control Menu 1 03/02/07 09/30/10

25 50 75

PRSA TK MENU TimeKeeper Main Menu 1 04/13/06 09/30/10

25 50 75

PRSA EMP MENU Employee Menu 46 03/05/07 09/30/10

25 50 75

PRSA SUP MENU T&A Supervisor Menu 1 03/01/07 09/30/10

25 50 75

PRSA ALL PAID 3.5 ALL OPTIONS 2 03/05/07 09/30/10

25 50 75

ENZ WORKORDER & MERS USERS MENU 12 03/05/07 09/30/10

25 50 75

ZMCCR PAT MENU MCCR Patients (local) 1 03/02/07 09/30/10

25 50 75

OR MAIN MENU CLINICIAN

Clinician Menu 1 03/02/07 09/30/10

25 50 75

ESP POLICE & SECURITY MENU

Police Menu 2 03/05/07 09/30/10

25 50 75

ESP POLICE OFFICER MENU

Police Officer 9 03/05/07 09/30/10

25 50 75

ECXMGR Extract Manager's Options 1 03/02/07 09/30/10

25 50 75

COS 1 CHIEF OF STAFF 3 03/05/07 09/30/10

25 50 75

ZCMOP CMOP Director Menu 1 08/20/03 09/30/10

25 50 75

ECMGR Event Capture Management ... 6 03/05/07 09/30/10

25 50 75

PRCH PURCHASE CARD MENU

Purchase Card Menu 1 03/05/07 09/30/10

25 50 75

ZPSO PHARM VOLUNTEERPharmacy Volunteer Menu 1 02/28/07 09/30/10

25 50 75

TIU UPLOAD MENU Upload Menu 5 10/16/06 09/30/10

25 50 75

TIU MAIN MENU PN CLINICIAN

Progress Notes User Menu 1 03/05/07 09/30/10

25 50 75

DVBA VARO REMOTE Cheyenne VA Regional Offi... 45 03/05/07 09/30/10

25 50 75

WVMENU Women's Health Menu 1 03/21/06 09/30/10

25 50 75

LRLOINC LOINC Main Menu 1 02/27/07 09/30/10

25 50 75

RMPO-MENU-MAIN Home Oxygen Main Menu 2 03/05/07 09/30/10

25 50 75

ZPSJU DENVER RPH Inpatient Medication Menu... 29 03/05/07 09/30/10

25 50 75

452 CONTRACT TRANSCRIPTION

Contract Transcription Menu 11 03/05/07 09/30/10

25 50 75

AGING RECEIVABLE AGING RECEIVABLE 3 03/05/07 09/30/10

25 50 75

OIG OIG 2 07/13/06 09/30/10

25 50 75

NON-MCCF MENU MON-MCCF MENU 1 01/24/07 09/30/10

25 50 75

ASSHRCFPCC HRC First Party CC 204 03/05/07 09/30/10

25 50 75

MQAS AUDIT MQAS AUDIT MENU 3 02/28/06 09/30/10

25 50 75

ARS BRONX NURSE ARS BRONX NURSE 23 03/05/07 09/30/10

25 50 75

Building secondary menu trees....

25 50 75

Merging.... done.

25 50 75

Menu Rebuild Complete: Jan 11, 2011@15:12:33

Install Completed

<span id="_Toc287445028" class="anchor"></span>CPRS28_RELATED.KID Installation Capture

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Installation option: 6 Install Package(s)

Select INSTALL NAME: CPRS28 RELATED 1.0 2/10/11@14:48:09

=\> CPRS28 RELATED PATCHES ;Created on Feb 10, 2011@12:37:10

This Distribution was loaded on Feb 10, 2011@14:48:09 with header of

CPRS28 RELATED PATCHES ;Created on Feb 10, 2011@12:37:10

It consisted of the following Install(s):

CPRS28 RELATED 1.0 GMRC\*3.0\*64 GMTS\*2.7\*90 OR\*3.0\*337

Checking Install for Package CPRS28 RELATED 1.0

Install Questions for CPRS28 RELATED 1.0

Checking Install for Package GMRC\*3.0\*64

Install Questions for GMRC\*3.0\*64

Incoming Files:

123 REQUEST/CONSULTATION (Partial Definition)

> **NOTE:** You already have the 'REQUEST/CONSULTATION' File.

Checking Install for Package GMTS\*2.7\*90

Install Questions for GMTS\*2.7\*90

Checking Install for Package OR\*3.0\*337

Install Questions for OR\*3.0\*337

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// YES

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET TERMINAL

25 50 75

Complete

CPRS28 RELATED 1.0

Install Started for CPRS28 RELATED 1.0 :

Feb 10, 2011@14:52:18

Build Distribution Date: Feb 10, 2011

Installing Routines

25 50 75

Feb 10, 2011@14:52:18GMRC\*3.0\*64

Install Started for GMRC\*3.0\*64 :

Feb 10, 2011@14:52:18

Build Distribution Date: Feb 10, 2011

Installing Routines:

25 50 75 100

Feb 10, 2011@14:52:18

Installing Data Dictionaries:

25 50 75 100

Feb 10, 2011@14:52:19

Updating Routine file...

25 50 75 100

Updating KIDS files...

25 50 75 100

GMRC\*3.0\*64 Installed.

Feb 10, 2011@14:52:19

Not a production UCI

NO Install Message sent

GMTS\*2.7\*90

Install Started for GMTS\*2.7\*90 :

Feb 10, 2011@14:52:19

Build Distribution Date: Feb 10, 2011

Installing Routines:

25 50 75 100

Feb 10, 2011@14:52:19

Updating Routine file...

25 50 75 100

Updating KIDS files...

25 50 75 100

GMTS\*2.7\*90 Installed.

Feb 10, 2011@14:52:19

Not a production UCI

NO Install Message sent

OR\*3.0\*337

Install Started for OR\*3.0\*337 :

Feb 10, 2011@14:52:19

Build Distribution Date: Feb 10, 2011

Installing Routines:

25 50 75 100

Feb 10, 2011@14:52:20

Installing PACKAGE COMPONENTS:

Installing OPTION

25 50 75 100

Feb 10, 2011@14:52:20

Updating Routine file...

25 50 75 100

Updating KIDS files...

25 50 75 100

OR\*3.0\*337 Installed.

Feb 10, 2011@14:52:20

Not a production UCI

NO Install Message sent

Updating Routine file...

25 50 75 100

Updating KIDS files...

25 50 75 100

CPRS28 RELATED 1.0 Installed.

Feb 10, 2011@14:52:20

No link to PACKAGE file

NO Install Message sent

Install Completed

> **NOTE:** The OR\*3\*337 patch adds a new option, IV Additive Frequency Utility \[OR IV ADD FREQ UTILITY\] to the existing ORDER MENU MANAGEMENT \[ORCM MENU\]. This new option allows the Clinical Application Coordinators (CACs) to define an additive frequency value to existing Continuous IV Quick Orders. Input from Pharmacy ADPAC is recommended.

> **NOTE:** Checksums values for the following routines (ORCHECK, ORCSAVE, ORCSAVE2, ORMBLDPS and ORQ2) have been updated by both OR\*3\*293 and OR\*3\*280 patches; therefore, when validating checksums against OR\*3\*293 patch, the above mentioned routines values have been updated to OR\*3\*280 checksums.