---
title: LR*5.2*468 Laboratory NDS Installation Back out  Plan
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Laboratory NDS Installation Back out  Plan
app_code: LR
app_name: Laboratory (LA and LR)
section: CLI
app_status: active
pkg_ns: LR
patch_ver: 5.2
patch_id: LR*5.2*468
group_key: "LR:LR:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: > This Backout Plan defines the ordered, technical steps required to back out the installation and to roll back to the previously installed version of the Laboratory Test File (#60), the restoration of changed Laboratory menus, and the associated routines (LRLNCV, LRSRVR, LRVER1, and LA7VHLU5). It p
audience: 
keywords: 
  - table
  - contents
  - procedure
  - installation
  - backout
  - rollback
  - press
  - patch
  - local
  - kids
page_count: 0
word_count: 2059
section_count: 22
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/la_1_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/la_1_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=71"
---

# Collaborative Terminology Tooling & Data Management (CTT & DM)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Collaborative Terminology Tooling & Data Management (CTT & DM)](#collaborative-terminology-tooling-data-management-ctt-dm)
- [Patch Installation and Back-out Plan LR\5.2\468](#patch-installation-and-back-out-plan-lr52468)
    - [December 2016 Department of Veterans Affairs](#december-2016-department-of-veterans-affairs)
    - [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Documentation and Distribution](#documentation-and-distribution)
- [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Pre-implementation Work Required and Time Allotted](#pre-implementation-work-required-and-time-allotted)
    - [Creating a Saved Local Patch File](#creating-a-saved-local-patch-file)
    - [Creating an HF Transport](#creating-an-hf-transport)
    - [Creating a PM Transport](#creating-a-pm-transport)
- [Installation Procedure](#installation-procedure)
- [Implementation Procedure](#implementation-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Backout Procedure](#backout-procedure)
  - [Backout Strategy](#backout-strategy)
  - [Backout Considerations](#backout-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Backout Criteria](#backout-criteria)
  - [Backout Risks](#backout-risks)
  - [Authority for Backout](#authority-for-backout)
  - [Backout Procedure](#backout-procedure-1)
    - [Procedure – If the KIDs File Save was HF (Host File)](#procedure-if-the-kids-file-save-was-hf-host-file)
    - [Procedure – If the KIDs File Save was PM (Pack man)](#procedure-if-the-kids-file-save-was-pm-pack-man)
    - [Installing the Local Patch](#installing-the-local-patch)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
> Native Domain Standardization (NDS) Laboratory Results

# Patch Installation and Back-out Plan LR\*5.2\*468

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> LA\*5.2\*92

![](lr-5-2-468-laboratory-nds-installation-back-out-plan/001.png)

### December 2016 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/2016</td>
<td>1.0</td>
<td>Delivery to Customer</td>
<td>Mantech Mission Solutions and Services Management</td>
</tr>
<tr class="even">
<td>12/15/2016</td>
<td>0.2</td>
<td>Technical Writer Review</td>
<td><p><mark>REDACTED</mark></p>
<p>Mantech Mission Solutions and Services</p></td>
</tr>
<tr class="odd">
<td>12/18/2016</td>
<td>0.1</td>
<td>Initial Draft</td>
<td><p><mark>REDACTED</mark></p>
<p>Mantech Mission Solutions and Services</p></td>
</tr>
</tbody>
</table>

1.  [Introduction 1](#introduction)
    1.  [Documentation and Distribution 1](#documentation-and-distribution)
2.  [Pre-installation and System Requirements 2](#pre-installation-and-system-requirements)
    1.  [Platform Installation and Preparation 2](#platform-installation-and-preparation)
    2.  [Download and Extract Files 2](#download-and-extract-files)
    3.  [Database Creation 2](#database-creation)
    4.  [Installation Scripts 2](#installation-scripts)
    5.  [Cron Scripts 2](#cron-scripts)
    6.  [Access Requirements and Skills Needed for the Installation 2](#access-requirements-and-skills-needed-for-the-installation)
    7.  [Pre-implementation Work Required and Time Allotted 2](#pre-implementation-work-required-and-time-allotted)
        1.  [Creating a Saved Local Patch File 3](#creating-a-saved-local-patch-file)
        2.  [Creating an HF Transport 4](#creating-an-hf-transport)
        3.  [Creating a PM Transport 4](#creating-a-pm-transport)
3.  [Installation Procedure 5](#installation-procedure)
4.  [Implementation Procedure 6](#implementation-procedure)
    1.  [System Configuration 6](#system-configuration)
    2.  [Database Tuning 6](#database-tuning)
5.  [Backout Procedure 7](#backout-procedure)
    1.  [Backout Strategy 7](#backout-strategy)
    2.  [Backout Considerations 7](#backout-considerations)
        1.  [Load Testing 7](#load-testing)
        2.  [User Acceptance Testing 7](#user-acceptance-testing)
    3.  [Backout Criteria 7](#backout-criteria)
    4.  [Backout Risks 7](#backout-risks)
    5.  [Authority for Backout 7](#authority-for-backout)
    6.  [Backout Procedure 7](#backout-procedure-1)
        1.  [Procedure – If the KIDs File Save was HF (Host File) 8](#procedure-if-the-kids-file-save-was-hf-host-file)
        2.  [Procedure – If the KIDs File Save was PM (Pack man) 8](#procedure-if-the-kids-file-save-was-pm-pack-man)
        3.  [Installing the Local Patch 9](#installing-the-local-patch)
6.  [Rollback Procedure 10](#rollback-procedure)
    1.  [Rollback Considerations 10](#rollback-considerations)
    2.  [Rollback Criteria 10](#rollback-criteria)
    3.  [Rollback Risks 10](#rollback-risks)
    4.  [Authority for Rollback 10](#authority-for-rollback)
    5.  [Rollback Procedure 10](#rollback-procedure-1)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This Backout Plan defines the ordered, technical steps required to back out the installation and to roll back to the previously installed version of the Laboratory Test File (#60), the restoration of changed Laboratory menus, and the associated routines (LRLNCV, LRSRVR, LRVER1, and LA7VHLU5). It provides backout instructions for Collaborative Terminology Tooling and Data Management (CTT DM) NDS Lab Results Patch LR\*5.2\*468 and patch LA\*5.2\*9 as managed through the CTT DM Native Domain Standardization (NDS) project.

> The Department of Veterans Affairs (VA) Interagency Program Office (IPO) and the Department of Defense (DoD) are tasked by its charter with leading the Departments’ efforts “to implement national health data standards for interoperability and \[be\] responsible for establishing, monitoring, and approving the clinical and technical standards profile and processes to ensure a seamless \[exchange\] of health data.” This task of NDS is aligned with achieving the goals outlined in the 2014 National Defense Authorization Act (NDAA) requiring that the

> Departments’ “healthcare data \[are\] computable in real-time and \[comply\] with existing national data standards” and that the “data \[are\] standardized as national standards continue to evolve.”

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Updated documentation describing the new functionality introduced by this patch is available at the Technical Services Project Repository (TSPR) within the Collaborative Terminology Tooling and Data Mgmt. Project Notebook.

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to have a backout path, a local patch must be created prior to the install. The local patch must contain the following:

- Data definition of the laboratory test file (#60)
- The laboratory menu where the new options will be installed by LR\*5.2\*468
- The following routines:
  - LA7VHLU5
  - LRSRVR
  - LRVER1
  - LRLNCV

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The person(s) creating the local patch must have local system access with the authority to create patches using the *KIDS Kernel Installation & Distribution System* option.

## Pre-implementation Work Required and Time Allotted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is recommended that a *Save Local Patch File* is created that can be re-installed in the event that patches LR\*5.2\*468 and LA\*5.2\*92 must be backed out.

> The Laboratory Option Menu on which the ‘LIM NDS MENU’ is placed is LRLIAISON. The approximate time to create the saved local patch is 30 minutes.

### Creating a Saved Local Patch File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Perform the following procedure to create a *Saved Local Patch File*.

1.  Create a local KIDS patch
2.  Use the KIDS (Kernel Installation & Distribution System) menu.
3.  Select ‘Edits and Distribution’.
4.  Select ‘Create a Build Using Namespace’.
5.  Enter a local patch name and identifier; (for example: ZZZ\*1.0\*004).
6.  At ‘BUILD PACKAGE FILE LINK:’ press \<Enter\>.
7.  At ‘BUILD TYPE: SINGLE PACKAGE//’ press \<Enter\>.
8.  At ‘BUILD TRACK PACKAGE NATIONALLY: YES//’ Enter NO.
9.  At ‘Namespace:’ press \<Enter\>.
10. At the menu, select: ‘Edit a Build’.
11. Enter the ‘*local package name and identifier*’ created in Step 5.
12. For the ‘Description:’ enter the following: “this is a local patch save for DD file 60, routines: LA7VHLU5, LRSRVR, LRVER1, LRLNCV. This patch is only to be reloaded in the event that the LR\*5.2\*468 and LA\*5.2\*92 patches need to be backed out.
13. Select ‘Next Page’.
14. For ‘File List’ enter 60 for LABORATORY TEST file.
15. Send Full or Partial DD...: FULL.
16. Update the Data Dictionary: YES.
17. Send Security Code: YES.
18. Data Comes With File...: NO
19. At ‘COMMAND:’ enter ‘Close’
20. Up arrow to the ‘COMMAND:’ prompt
21. Enter ‘Next Page’.
22. Down arrow to ‘ROUTINE’ and press \<Enter\>.
23. Enter LA7VHLU5 ‘Send To Site’.
24. Enter LRSRVR ‘Send To Site’.
25. Enter LRLNCV ‘Send To Site’.
26. Enter LRVER1 ‘Send To Site’.
27. Enter LRVRPOC ‘Send To Site’.
28. Down arrow to ‘OPTION’ and press \<Enter\>.
29. <span id="_bookmark11" class="anchor"></span>Enter the option name LRLIAISON. This is where the new options from LR\*5.2\*468 will be placed. This should be the Laboratory option menu as identified in Section 2.7. (E.g. LRLIAISON) ‘Send to Site’.
30. Down arrow to the ‘COMMAND:’ prompt.
31. Enter ‘Close’.
32. Down arrow to the ‘COMMAND:’ prompt.
33. Enter ‘Save’.
34. Enter ‘Exit’.
35. On the menu select ‘Transport a Distribution’.
36. Enter the ‘local package name and identifier’ created in Step 5.
37. At the ‘Another Package Name:’ press \<Enter\>.
38. At the ‘OK to continue? prompt, select YES//’ press \<Enter\>.

### Creating an HF Transport

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Perform the following procedure to create an ‘*HF’ TRANSPORT*.

39. At the ‘Transport through (HF) Host File or (PM) PackMan:’ enter HF.
40. At the ‘Enter a Host File:’ enter the system file name that will hold the local patch; (for example: ZZZ_1-0_004.KID).
41. At the ‘Header Comment:’ enter Local patch for Lab.
42. At the Edits and Distribution Menu, press \<Enter\>.
43. At the KIDS menu press \<Enter\>.

### Creating a PM Transport

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Perform the following procedure to create a ‘*PM*’ *TRANSPORT*.

44. At the ‘Transport through (HF) Host File or (PM) PackMan:’ enter PM.
45. At the ‘Header Comment:’ enter Local patch for Lab.
46. For the description of Packman Message, enter:

#### ‘This is a saved backup for the lab patch install for LR\*5.2\*468 and LA\*5.2\*92. This local build will be used in the event that the above mentioned installs need to be backed off.’

47. At ‘EDIT Option:’ press \<Enter\>.
48. At the ‘Do you wish to secure this message? NO// prompt, enter ‘NO’.
49. At the ‘Send mail to:’ prompt, Enter your name.
50. At the ‘Select basket to send to: IN//’ prompt: press \<Enter\>.
51. At the ‘And Send to:’ prompt: Enter any additional persons that may need to have the local patch.

> At The ‘Select Edits and Distribution \<TEST ACCOUNT\> Option:’ press \<Enter\>.

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

> Change Order:

> Affected Systems:

# Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

# Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Perform the backout procedure to load the locally made patch created in Section 2.7. The backout is to be performed by persons with programmer-level access and in conjunction with the STS team.

> The following is an example of the code that would be exercised for each multiple field that you are removing.

> S DIU= “multiple field DD number” DIU(0)="S" D EN^DIU2

## Backout Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The backout strategy is to load the locally made patch that was created in Section 2.7.

## Backout Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The backout should only be performed if the local facility management determines that the patches LR\*5.2\*468 and LA\*5.2\*92 are not appropriate for that facility. It should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Backout Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Local facility management needs to determine that the patches LR\*5.2\*468 and LA\*5.2\*92 are not appropriate for their facility.

## Backout Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> By backing out LR\*5.2\*468 and LA\*5.2\*92, the local facility will have to maintain the local test to LOINC Code mappings.

## Authority for Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The local facility management, in concurrence with the VHA Pathology and Laboratory Medicine Program Office, provides the authority for the backout.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Execute the following backout procedure from the programmer’s prompt.

1.  At the Programmers option, enter: DO ^XUP you may be prompted for your access code.
2.  At the Select OPTION NAME, enter ‘EVE’.
3.  At the Select Systems Manager Menu option: enter Menu Management and then press

> \<Enter\>.

4.  At the Select Menu Management option: enter Edit Options and then press \<Enter\>.
5.  At Select OPTION to edit: Enter the option used in <u>Step</u> [<u>29</u>](#_bookmark11) [<u>Creating a Saved Local</u> <u>Patch File</u>.](#creating-a-saved-local-patch-file)
6.  At NAME: optionname//, Enter : @, then press \<Enter\>.

#### At the SURE YOU WANT TO DELETE THE ENTIRE 'LRLIAISON' OPTION?

> Enter YES and press \<Enter\>.

7.  Press \<Enter\> twice to return to the System Managers Menu.

### Procedure – If the KIDs File Save was HF (Host File)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Perform the following procedure if the KIDs file save was ‘HF’ (HOST FILE).

1.  At the ‘Select Systems Manager Menu’ enter ‘Programmer Options’.
2.  At the ‘Select Programmer Options’ enter ‘KIDS’.
3.  Select ‘Installation’.
4.  At the ‘Select Installation \<TEST ACCOUNT\> option:’ enter 1.
5.  At the ‘Enter a Host File:’ enter the path and the KIDS file name. (For example: USER\$:\[save area\] ZZZ_1-0_004.KID.
6.  At the ‘Want to Continue with Load? YES//’ press \<Enter\>.

### Procedure – If the KIDs File Save was PM (Pack man)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Perform the following procedure if the KIDs File Save was ‘PM’ (PACK MAN).

7.  At the ‘Select Systems Manager Menu’, enter ‘MAIL’.
8.  At the ‘Select MailMan Menu’ enter ‘RML’.
9.  At the ‘Select message reader: Classic//’, press \<Enter\>.
10. At the ‘Read mail in basket: IN//’ press \<Enter\>.
11. At the ‘IN Basket Message:’ enter the message number for the previously created local KIDs build that was transported by means of PackMan.
12. Read the message and make sure that this is the PackMan message containing the previously saved local KIDs build.
13. After reading the message from Step 6, at the ‘Enter message action (in IN basket): Ignore//’ prompt enter ‘X’ (Xtract KIDS).
14. At the ‘Select PackMan function:’, enter ‘6’ (INSTALL/CHECK MESSAGE).
15. At the ‘OK to continue with Load? NO//’ enter ‘YES’.
16. At the ‘Want to Continue with Load? YES//’, press \<Enter\>.
17. At the ‘Select PackMan function:’ press \<Enter\>.
18. At The ‘Enter message action (in IN basket): Ignore//’ prompt press \<Enter\>.
19. At the ‘IN Basket Message:’ prompt enter ‘^’.
20. At the ‘Select MailMan Menu’ press \<Enter\>.
21. At the ‘Select Systems Manager Menu’ enter ‘Programmer Options’.
22. At the ‘Select Programmer Options’ enter ‘KIDS’.
23. Select ‘Installation’.

### Installing the Local Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Perform the following procedure to install the Local Patch.

24. On the ‘Select Edits and Distribution’ menu select Option 6 (Install Package(s))
25. At the ‘Select INSTALL NAME:’ enter the local patch name (ex: ZZZ\*1.0\*004).
26. At the ‘Want KIDS to INHIBIT LOGONs during the install? NO//’ enter NO.

#### At the ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’ Enter NO.

27. At the ‘DEVICE: HOME//’ press \<Enter\> (the patch will now install).
28. At the ‘Select Installation \<TEST ACCOUNT\> Option:’ press \<Enter\>.
29. At the ‘Select Kernel Installation & Distribution System’ option press \<Enter\>.
30. At the ‘Do you really want to halt? YES//’ press \<Enter\>.
31. At the Programmer’s Prompt, press ‘H’.

> The Laboratory Test File (#60) Data Definition is restored to what it was prior the patch load. The routines will have also been restored to their prior state.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A