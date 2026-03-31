---
title: LR*5.2*500 Laboratory Enhancements NDS Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Laboratory Enhancements NDS
app_code: LR
app_name: Laboratory (LA and LR)
section: CLI
app_status: active
pkg_ns: LR
patch_ver: 5.2
patch_id: LR*5.2*500
group_key: "LR:LR:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - patch
  - test
  - installation
  - back
  - laboratory
  - deployment
  - site
  - procedure
page_count: 0
word_count: 5207
section_count: 31
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lr_5_2_500_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lr_5_2_500_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=71"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Collaborative Terminology Tooling & Data Management (CTT&DM)  
  Native Domain Standardization (NDS)
---

Laboratory Enhancements (LR\*5.2\*500)

Deployment, Installation, Back-Out, and Rollback Guide

![](lr-5-2-500-laboratory-enhancements-nds-installation-guide/001.png)

May 2018

Office of Information and Technology (OI&T)

Revision History

| Date    | Version | Description          | Author                                       |
|---------|---------|----------------------|----------------------------------------------|
| 05/2018 | 1.0     | Delivery to Customer | ManTech Mission Solutions and Services Group |

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
  - [Site Readiness Assessment](#site-readiness-assessment)
    - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
    - [Site Information (Locations, Deployment Recipients)](#site-information-locations-deployment-recipients)
    - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Facility Specifics](#facility-specifics)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
    - [Creating a Local Patch Backup](#creating-a-local-patch-backup)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
    - [Routines](#routines)
    - [Data Dictionaries](#data-dictionaries)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install Labs Enhancements Native Domain Standardization (NDS) patch LR\*5.2\*500, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Labs Enhancements (NDS) patch LR\*5.2\*500 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Enhancements (NDS) patch LR\*5.2\*500 possesses a direct application dependency on the Laboratory Reports patch LR\*5.2\*468. The MASTER LABORATORY TEST File (#66.3) and LAB MLTF MANAGED ITEMS FILE (#66.4) were introduced in patch LR\*5.2\*468.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Labs Enhancements (NDS) patch LR\*5.2\*500 possesses the following constraints:

- The updates to the VistA LABORATORY TEST File (#60) shall not affect the current functionality or conflict with applications that utilize this file.
- The fields being added to this file should only be visible on the back end and to those requesting the information, not the GUI applications used by clinicians within the VA.
- Due to the complexities of the changes to the MASTER LABORATORY TEST File (#66.3), backing out the changes to the files data definition will not be possible and is therefore out of scope for this document.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Team                    | Phase / Role                      | Tasks                                                                                                               |
|-------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------|
| OIT Regional Support    | Deployment                        | Plan and schedule deployment (including orchestration with vendors)                                                 |
| CTT&DM NDS Project Team | Deployment                        | Determine and document the roles and responsibilities of those involved in the deployment.                          |
| OIT Regional Support    | Deployment                        | Test for operational readiness                                                                                      |
| OIT Regional Support    | Deployment                        | Execute deployment                                                                                                  |
| OIT Regional Support    | Installation                      | Plan and schedule installation                                                                                      |
| CTT&DM NDS Project Team | Installations                     | Coordinate training                                                                                                 |
| OIT Regional Support    | Back-out                          | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |
| CTT&DM NDS Project Team | Post Deployment – Warranty Period | Hardware, Software and System Support                                                                               |
| OIT Regional Support    | Post Deployment – Post Warranty   | Hardware, Software and System Support                                                                               |

Table 2: Software Specifications

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a concurrent online rollout. During IOC testing and after national release, patch LR\*5.2\*500 will be distributed via the FORUM Patch Module, and may be deployed at any site without regard to deployment status at other sites.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the master deployment schedule.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CTT&DM NDS patch LR\*5.2\*500 deployment.

The LR\*5.2\*500 patch must be manually installed, or manually queued for installation, at each VistA instance at which it is deployed, using the standard Kernel Installation Distribution System (KIDS) software. The LR\*5.2\*500 patch should be installed at all VA VistA instances running the VistA Laboratory v.5.2 application, and will update the MUMPS (Massachusetts General Hospital Utility Multi-Programming System) server software in each VistA instance’s Laboratory namespace.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment topology for the CTT&DM NDS patch LR\*5.2\*500, during IOC testing and after national release is described below:

Members of the Information Technology Operations and Services (ITOPS) Office of Information and Technology (OI&T) get the nationally released VistA patch from the VistA National Patch Module and install the patch in the VA facilities that are their responsibility.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, CTT&DM NDS patch LR\*5.2\*500 will be deployed at the following sites:

- <span class="mark">REDACTED</span>
- <span class="mark">REDACTED</span>

After national release, CTT&DM NDS patch LR\*5.2\*500 will be deployed at all sites running the VistA Laboratory v.5.2 application.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special preparation is required by the site prior to deployment.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of CTT&DM NDS patch LR\*5.2\*500 requires a fully patched VistA environment running the Laboratory v.5.2 application, as well as a Health Product Support (HPS) team member available to perform the patch installation.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of CTT&DM NDS patch LR\*5.2\*500.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT&DM NDS patch LR\*5.2\*500 requires no site hardware specifications during, or prior to, deployment.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software                        | Make | Version | Configuration | Manufacturer | Other |
|------------------------------------------|------|---------|---------------|--------------|-------|
| VistA Laboratory (LR) patch LR\*5.2\*468 |      | 5.2     | Standard      | VHA          |       |

Table 3: Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No notifications are required for deployment of CTT&DM NDS patch LR\*5.2\*500.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch LR\*5.2\*500, which is tracked in the National Patch Module (NPM) in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in Forum to identify when and by whom the patch was installed in the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production systems. Therefore, this information does not need to be manually tracked in the chart below.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | N/A | N/A  | N/A                           |
| Install  | N/A | N/A  | N/A                           |
| Back-Out | N/A | N/A  | N/A                           |

Deployment/Installation/Back-Out Checklist

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

Before installing LR\*.2\*500, it is recommended that a Local Patch Backup is created to save routines and data dictionaries that are modified by this patch. Backing out the patch’s new components must be done by installing ‘back-out’ KIDS build LR\*5.2\*00500, created specifically to back out all the software components newly installed by LR\*5.2\*500.

Patch Dependencies

Patch LR\*5.2\*468 must be installed prior to installing this patch.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

Pre-Installation Instructions:

### Creating a Local Patch Backup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following procedure to create a Local Patch Backup.

1.  From the KIDS (Kernel Installation & Distribution System) Menu, select ‘Edits and Distribution’.
2.  Select ‘Create a Build Using Namespace’.
3.  Enter a local patch name and identifier, suggested name ZLR\*5.2\*00500.
4.  When prompted ‘BUILD PACKAGE FILE LINK:’, press \<Enter\>.
5.  When prompted ‘BUILD TYPE: SINGLE PACKAGE//’, press \<Enter\>.
6.  When prompted ‘BUILD TRACK PACKAGE NATIONALLY: YES//’, enter NO.
7.  When prompted ‘Namespace:’, press \<Enter\>.
8.  When prompted ‘Select Edits and Distribution Option’, select: ‘Edit a Build’.
9.  Enter the local patch name from step 3 (ZLR\*5.2\*00500).
10. For the ‘Description:’ enter the following: “this is a local backup for LR\*5.2\*500. This patch should only be installed in the event that LR\*5.2\*500 needs to be backed out.”
11. In the ‘COMMAND:’ field, enter ‘Next Page’.
12. In the ‘File List’ dialog Enter 66.4 for LAB MLTF MANAGED ITEMS File.
13. In ‘Send Full or Partial DD’ field, enter FULL.
14. In the ‘Update the Data Dictionary:’ field, enter YES.
15. In the ‘Send Security Code:’ field, enter YES.
16. In the ‘Data Comes With File:’ field, enter NO.
17. In the DD Export Options dialog, move cursor to the COMMAND: prompt, enter ‘Close’
18. In the File List dialog, move cursor to the ‘COMMAND:’ prompt, enter ‘Next Page’.
19. In the Build Components section, move cursor to ROUTINE and press \<Enter\>.
20. In the first blank row in the ROUTINE dialog, enter LRMLED, and ‘Send To Site’.
21. In the next blank row in the ROUTINE dialog, enter LRMLEDA, and ‘Send to Site’.
22. In the next blank row in the ROUTINE dialog, enter LRMLWT, and ‘Send to Site’.
23. In the next blank row in the ROUTINE dialog, enter LRMLACM, and ‘Send to Site’.
24. Move cursor to the ‘COMMAND:’ prompt in the ROUTINE dialog, enter ‘Close’.
25. Move cursor to the ‘COMMAND:’ prompt in the BUILD COMPONENTS dialog, enter ‘Save’, then enter ‘Exit’.
26. When returned to the Edits and Distribution menu, select option ‘Transport a Distribution’.
27. Enter the ‘local package name and identifier’ that was created in Step 3. (ZLR\*5.2\*00500).
28. At the ‘Another Package Name:’ press \<Enter\>.
29. At the ‘OK to continue? Prompt, select YES//’ press \<Enter\>.
30. If creating a Host File transport, perform the following steps:
1.  At the ‘Transport through (HF) Host File or (PM) PackMan:’ prompt, enter HF.
2.  At the ‘Enter a Host File:’ prompt, enter the system file to which the Local Patch Backup will be saved. (ZLR_5_2_00500.KID).
3.  At the ‘Header Comment:’ Enter ‘Local Backup of LR\*5.2\*500’.
4.  At the Edits and Distribution Menu, press \<Enter\>.
5.  At the KIDS Menu press \<Enter\>.
31. If creating a PackMan transport, perform the following steps:
1.  At the ‘Transport through (HF) Host File or (PM) PackMan:’ enter PM.
6.  At the ‘Header Comment:’ enter ‘Local Backup of LR\*5.2\*500’
7.  For the description of Packman Message, Enter: ‘This is a saved backup for the Laboratory Enhancements patch install for LR\*5.2\*500. This local build will be used in the event that the above mentioned installs need to be backed out.’
2.  At ‘EDIT Option:’ press \<Enter\>.
8.  At the ‘Do you wish to secure this message? NO// prompt, Enter ‘NO’.
9.  At the ‘Send mail to:’ prompt, Enter your name.
10. At the ‘Select basket to send to: IN//’ prompt: press \<Enter\>.
11. At the ‘And Send to:’ prompt: Enter any additional persons that may need to have the local patch.
12. At The ‘Select Edits and Distribution \<TEST ACCOUNT\> Option:’ press \<Enter\>.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*500 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory patch LR\*5.2\*500 software is distributed by a Forum Kids distribution. Documentation is available on the SOFTWARE.DIR directory at one of the following Office of Information (OI) Field Offices. The preferred method is to retrieve the file using Secure File Transfer Protocol (SFTP) from download.vista.med.va.gov, which transmits files from the first available SFTP server.

Hines: fo-hines.med.va.gov

Salt Lake City: fo-slc.med.va.gov

File Name: CTT_DM_NDS_Laboratory_Enhancements_v1.zip

Contents: This zip file contains the following documents in both .docx and .pdf

- Laboratory Enhancements (LR\*5.2\*500) Deployment, Installation, Back-Out, and Rollback Guide (lr_5_2_500_ig)
- LIM NDS User Manual (lab_5_2_lim_nds_um)

Retrieval Format: BINARY

The VistA Documentation Library (VDL) web site will also contain the above referenced documents. This website is usually updated within 1-3 days of the patch release date. The VDL web address for Laboratory user documentation is: https://www.va.gov/vdl/application.asp?appid=71

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new database is required for the CTT&DM NDS patch LR\*5.2\*500.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of CTT&DM NDS patch LR\*5.2\*500.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No CRON scripts are required for installation of CTT&DM NDS patch LR\*5.2\*500.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to national VA network, as well as the local network of each site to receive CTT&DM NDS patch LR\*5.2\*500 is required to perform the installation, as well as authority to create and install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter the patch LR\*5.2\*500:
1.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of these patch routines, DDs, templates, etc.
2.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
32. Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup other changes such as DDs or templates.
33. From the Installation Menu, select the Install Package(s) option and choose the patch to install.
34. When prompted: 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond NO.
35. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
36. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' , respond NO.
37. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of routines in CTT&DM NDS patch LR\*5.2\*500 may be verified by running the Kernel checksum tool from the VistA server command line after installation:

D CHECK1^XTSUMBLD

The checksums produced by the checksum tool should match the numeric portion of the “After:” checksums in the CTT&DM NDS patch LR\*5.2\*500 patch description.

Example – Checksum for routines as displayed by Kernel checksum tool CHECK1^XTSUMBLD:

LR500PO value = 5484460

LRMLACM value = 19567721

LRMLED value = 183395899

LRMLEDA value = 165026309

LRMLWT value = 43869064

Installation of Data Dictionaries in CTT&DM NDS patch LR\*5.2\*500 may be verified by running the FileMan Data Listing tool from the VistA server command line after installation. The new fields will print in the output if installation was successful.

Example – verification of fields installed with LR\*5.2\*500 using FileMan Data Listing:

*<u>D P^DI</u>*

VA FileMan 22.2

Select OPTION: *<u>DATA DICTIONARY UTILITIES</u>*

Select DATA DICTIONARY UTILITY OPTION: *<u>LIST FILE ATTRIBUTES</u>*

START WITH What File: MASTER LABORATORY TEST// *<u>60 LABORATORY TEST</u>*

(1799 entries)

GO TO What File: *<u>LABORATORY TEST</u>*// (1799 entries)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD// *<u>BRIEF</u>*

ALPHABETICALLY BY LABEL? No// (No)

Start with field: FIRST// *<u>134 IN HOUSE TEST</u>*

Go to field: *<u>141 PERFORMING LAB</u>*

DEVICE: *<u>;;9999</u>* DEC Windows Right Margin: 80// <u>80</u>

BRIEF DATA DICTIONARY \#60 -- LABORATORY TEST FILE 2/13/18 PAGE 1

SITE: TEST.CHEYENNE.MED.VA.GOV UCI: CHEY59,ROU (VERSION 5.2)

-------------------------------------------------------------------------------

IN HOUSE TEST 60,134 SET

'1' FOR YES;

'0' FOR NO;

Tests are performed on-site using instruments or manual methods.

POC TEST 60,135 SET

'1' FOR YES;

'0' FOR NO;

Yes if tests are performed using POC equipment

CALCULATION TEST 60,136 SET

'1' FOR YES;

'0' FOR NO;

Yes if test result produced by calculation.

SCANNED IMAGE TEST 60,137 SET

'0' FOR NO;

'1' FOR YES;

Test results scanned to VistA Imaging due to complexity.

BILLABLE 60,138 SET

'0' FOR NO;

'1' FOR YES;

Yes or No\> This setting relates to Standardized Billable Tests (SBTs) for LMIP

WORKLOAD CAPTURE 60,139 SET

'0' FOR NO;

'1' FOR YES;

Yes or No. This setting relates to Managerial Cost Accounting (MCA)

...

PERFORMING LAB 60,141 60.16 SET

Multiple

PERFORMING LAB 60.16,.01 SET

'IH' FOR IN-HOUSE;

'CL' FOR CONTRACT REF LAB;

'VAL' FOR VA REFERENCE LAB;

'AL' FOR AFFILIATE REF LAB;

ORDER CODE 60.16,1 FREE TEXT

Enter the order code obtained or provided by the performing lab. If performing

lab is another VA, enter the National VA Lab Code. Needed for MLTF to assign

LOINC.

Select DATA DICTIONARY UTILITY OPTION: *<u>LIST FILE ATTRIBUTES</u>*

START WITH What File: MASTER LABORATORY TEST// *<u>66.3 MASTER LABORATORY TEST</u>*

(70 entries)

GO TO What File: MASTER LABORATORY TEST// (70 entries)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD//

Start with field: FIRST// *<u>.01 LAB TEST NAME</u>*

Go to field: *<u>1 METHOD</u>*

DEVICE: *<u>;;9999</u>* DEC Windows Right Margin: 80//

STANDARD DATA DICTIONARY \#66.3 -- MASTER LABORATORY TEST FILE 2/13/18 PAGE

1

STORED IN ^LRMLTF( (70 ENTRIES) SITE: TEST.CHEYENNE.MED.VA.GOV UCI: CHEY59,

ROU (VERSION 5.2)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

66.3,.01 LAB TEST NAME 0;1 FREE TEXT (Required) (audited)

INPUT TRANSFORM: K:\$L(X)\>230!(\$L(X)\<1) X

MAXIMUM LENGTH: 230

LAST EDITED: FEB 07, 2018

HELP-PROMPT: Answer must be 1-230 characters in length.

DESCRIPTION: This is the National Master Laboratory Test

file (MLTF)

for associating lab tests with LOINC Codes and

should not be edited.

AUDIT: YES, ALWAYS

PRE-LOOKUP: I \$G(DIC(0))\["L",'\$D(XUMF) K X D EN^DDIOL("Entr

ies must be edited via the Master File Server (

MFS).","","!?5,\$C(7)")

DELETE TEST: 1,0)= D:'\$D(XUMF) EN^DDIOL("Entries must be ina

ctivated via the Master File Server (MFS).","",

"!?5,\$C(7)") I \$D(XUMF)

LAYGO TEST: 1,0)= D:'\$D(XUMF) EN^DDIOL("Entries must be add

ed via the Master File Server (MFS).","","!?5,\$

C(7)") I \$D(XUMF)

WRITE AUTHORITY: ^

FIELD INDEX: B (#442) MUMPS IR LOOKUP & SORTINGShort Descr: New style Cross Refernce for 60 characters.Description: The 'B' cross reference is being created heredue to the 30 character limit in thetraditional 'B' cross reference. This 'B'cross reference is for a 60 character length.Set Logic: S ^LRMLTF("B",\$E(X,1,60),DA)=""Kill Logic: K ^LRMLTF("B",\$E(X,1,60),DA)X(1): LAB TEST NAME (66.3,.01) (Len 230)(forwards)

66.3,.02 ALTERNATE TEST NAME 1;1 FREE TEXT (audited)

INPUT TRANSFORM: K:\$L(X)\>230!(\$L(X)\<1) X

MAXIMUM LENGTH: 230

LAST EDITED: FEB 08, 2018

HELP-PROMPT: Answer must be 1-230 characters in length.

DESCRIPTION: This is the 'short name' for the Master

Laboratory Test file.

AUDIT: YES, ALWAYS

WRITE AUTHORITY: ^

FIELD INDEX: D (#1426) REGULAR IR LOOKUP & SORTINGShort Descr: New Style Alternate Name index for 60charactersSet Logic: S ^LRMLTF("D",\$E(X,1,60),DA)=""Kill Logic: K ^LRMLTF("D",\$E(X,1,60),DA)Whole Kill: K ^LRMLTF("D")X(1): ALTERNATE TEST NAME (66.3,.02) (Subscr 1)(Len 60) (forwards)

66.3,.04 LOINC CODE 2;2 FREE TEXT (Required) (audited)

INPUT TRANSFORM: K:\$L(X)\>20!(\$L(X)\<1) X

LAST EDITED: JAN 31, 2018

HELP-PROMPT: Answer must be 1-20 characters in length.

DESCRIPTION: This is the LOINC code that will be associated

to the lab test name and VUID.

AUDIT: YES, ALWAYS

WRITE AUTHORITY: ^

CROSS-REFERENCE: 66.3^C1)= S ^LRMLTF("C",\$E(X,1,30),DA)=""2)= K ^LRMLTF("C",\$E(X,1,30),DA)Additional lookup field for the LIMs.

66.3,.05 COMPONENT 2;3 FREE TEXT (Required) (audited)

INPUT TRANSFORM: K:\$L(X)\>230!(\$L(X)\<1) X

MAXIMUM LENGTH: 230

LAST EDITED: FEB 08, 2018

HELP-PROMPT: Answer must be 1-230 characters in length.

DESCRIPTION: This is the Lab COMPONENT value used in

matching a Lab test to a LOINC Code.

AUDIT: YES, ALWAYS

WRITE AUTHORITY: ^

66.3,.06 PROPERTY 2;4 FREE TEXT (Required) (audited)

INPUT TRANSFORM: K:\$L(X)\>230!(\$L(X)\<1) X

MAXIMUM LENGTH: 230

LAST EDITED: FEB 07, 2018

HELP-PROMPT: Answer must be 1-230 characters in length.

DESCRIPTION: This is the Lab PROPERTY value used in matching

a Lab test to a LOINC Code.

AUDIT: YES, ALWAYS

WRITE AUTHORITY: ^

66.3,.07 TIME ASPECT 3;1 FREE TEXT (Required) (audited)

INPUT TRANSFORM: K:\$L(X)\>230!(\$L(X)\<1) X

MAXIMUM LENGTH: 230

LAST EDITED: FEB 07, 2018

HELP-PROMPT: Answer must be 1-230 characters in length.

DESCRIPTION: This is the Lab TIME ASPECT value used in

matching a Lab test to a LOINC Code.

AUDIT: YES, ALWAYS

WRITE AUTHORITY: ^

66.3,.08 SPECIMEN 3;2 FREE TEXT (Required) (audited)

INPUT TRANSFORM: K:\$L(X)\>230!(\$L(X)\<1) X

MAXIMUM LENGTH: 230

LAST EDITED: FEB 07, 2018

HELP-PROMPT: Answer must be 1-230 characters in length.

DESCRIPTION: This is the Lab SPECIMEN (site/specimen) value

used in matching a Lab test to a LOINC Code.

AUDIT: YES, ALWAYS

WRITE AUTHORITY: ^

66.3,.09 SCALE 3;3 FREE TEXT (Required) (audited)

INPUT TRANSFORM: K:\$L(X)\>230!(\$L(X)\<1) X

MAXIMUM LENGTH: 230

LAST EDITED: FEB 07, 2018

HELP-PROMPT: Answer must be 1-230 characters in length.

DESCRIPTION: This is the Lab SCALE value used in matching a

Lab test to a LOINC Code.

AUDIT: YES, ALWAYS

WRITE AUTHORITY: ^

66.3,1 METHOD 3;4 FREE TEXT (audited)

INPUT TRANSFORM: K:\$L(X)\>230!(\$L(X)\<1) X

MAXIMUM LENGTH: 230

LAST EDITED: FEB 07, 2018

HELP-PROMPT: Answer must be 1-230 characters in length.

DESCRIPTION: This is the Lab METHOD value used in matching a

Lab test to a LOINC Code.

AUDIT: YES, ALWAYS

WRITE AUTHORITY: ^

Select DATA DICTIONARY UTILITY OPTION: *<u>LIST FILE ATTRIBUTES</u>*

START WITH What File: MASTER LABORATORY TEST// *<u>66.4 LAB MLTF MANAGED ITEMS</u>*

(1 entry)

GO TO What File: LAB MLTF MANAGED ITEMS// (1 entry)

Select LISTING FORMAT: STANDARD// *<u>CONDENSED</u>*

DEVICE: *<u>;;9999</u>* DEC Windows Right Margin: 80//

CONDENSED DATA DICTIONARY---LAB MLTF MANAGED ITEMS FILE (#66.4)UCI: CHEY59,ROU

VERSION: 5.2

STORED IN: ^LAB(66.4, FEB 13,2018 PAGE 1

--------------------------------------------------------------------------------

FILE SECURITY

DD SECURITY : @ DELETE SECURITY: @

READ SECURITY : @ LAYGO SECURITY : @

WRITE SECURITY : @

CROSS REFERENCED BY:

INSTITUTION POINTER(ANM) INSTITUTION POINTER(B)

FILE STRUCTURE

FIELD FIELD

NUMBER NAME

.01 INSTITUTION POINTER (RP4'X), \[0;1\]

.02 NTRT SEND METHOD (S), \[0;2\]

.03 AUTO REMINDERS PARAMETER (NJ3,0), \[0;3\]

.04 AUDIT PURGE DAYS (NJ3,0), \[0;4\]

.05 CTT TOOLING ACTIVE (S), \[0;5\]

.06 LAB IEN (NJ8,0), \[0;6\]

.07 SUBSCRIPT FOR NTRT (S), \[0;7\]

.08 LAST AUTO TEST ID (F), \[0;8\]

.1 SEND NTRT MESSAGES (S), \[0;10\]

1 DEFAULT NTRT MAIL GROUP (F), \[1;1\]

2 DEFAULT SITE LAB MAIL GROUP (F), \[2;1\]

3 SITE LAB SERVER (F), \[3;1\]

4 CTT TOOLING WEB ADDRESS (FJ100), \[4;1\]

5 CTT TOOLING PORT NUMBER (NJ10,0), \[4;2\]

6 CTT TOOLING NTRT PATH (FX), \[5;1\]

7 CTT TOOLING SCHEMA NAME (FJ60), \[6;1\]

8 CTT TOOLING SCHEMA PATH (FXJ100), \[6;2\]

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No System Configuration is required before or after deployment of CTT&DM NDS patch LR\*5.2\*500.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Database Tuning is required before or after deployment of CTT&DM NDS patch LR\*5.2\*500.

This concludes the installation process.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out of this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

Due to the complexities of the changes to the MASTER LABORATORY TEST File (#66.3) backing out the changes to the files data definition will not be possible and is out of scope for this document.

A manual procedure is provided.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-out Strategy is to install the backup patch made before installation to revert modified routines and the LAB MLTF MANAGED ITEMS File (#66.4) DD, and then follow the manual steps provided to delete and change other DD changes in the LABORATORY TEST File (#60).

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out should only be done in the event that the local facility management determines that the patch LR\*5.2\*500 is not appropriate for that facility, and should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch LR\*5.2\*500.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management would need to determine patch LR\*5.2\*500 is not appropriate for their facility.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out LR\*5.2\*500, the local facility will not be able to add the IN HOUSE TEST, POC TEST, CALCULATION TEST, SCANNED IMAGE TEST, BILLABLE, WORKLOAD CAPTURE, or PERFORMING LAB data to LABORATORY TEST (#60) file entries.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Local Facility Management has the authority to back-out patch LR\*5.2\*500.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

Perform the back-out procedure by installing the backup patch created in section 4.1.1 prior to the installation (ZLR\*5.2\*00500) and then manually removing routine and DD changes made in the LABORATORY TEST File (#60).

The back-out is to be performed by persons with programmer-level access and in conjunction with the STS Team. The following should be executed from the programmers prompt.

Manual Back-Out Procedure

First, load and install the back-out patch (ZLR\*5.2\*00500) created in step 4.1.1 before the installation of LR\*5.2\*500.

Delete routine LR500PO

The deletion of a routine is a potentially dangerous activity. This procedure must be performed by persons with programmer-level access, and in conjunction with the STS team.

1.  From the ROUTINE MANAGEMENT MENU \[XUROUTINES\], select the DELETE ROUTINES \[XTRDEL\] option.

    <u>IMPORTANT: When prompted for ‘All Routines?’, enter NO</u>.
1.  At the ‘Routine:’ prompt, enter LR500PO
2.  At the next ‘Routine:’ prompt, press \<Enter\>
3.  At the prompt ‘1 routines to DELETE, OK:’. enter YES.

Example – manual deletion of routine LR500PO using option DELETE ROUTINES \[XTRDEL\]:

Select OPTION NAME: ROUTINE MANAGEMENT MENU XUROUTINES Routine Management Menu

Bring in Sent Routines

Delete Routines

First Line Routine Print

List Routines

Move Routines across Volume Sets

Select OPTION NAME: DELETE ROUTINES XTRDEL Delete Routines

Delete Routines

ROUTINE DELETE

All Routines? No =\> No

Routine: LR500PO

Routine:

1 routine

1 routines to DELETE, OK: NO// Y

LR500PO

Done.

Then proceed with the following from the FileMan menu:

Delete New Fields in the LABORATORY TEST File (#60)

Select OPTION: MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES// NO

Modify what File: LABORATORY TEST// (3420 entries)

Select FIELD: 134 IN HOUSE TEST

LABEL: IN HOUSE TEST// @

SURE YOU WANT TO DELETE THE ENTIRE 'IN HOUSE TEST' FIELD? Y (Yes)

OK TO DELETE 'IN HOUSE TEST' FIELDS IN THE EXISTING ENTRIES? Yes// (Yes)......

Select FIELD: 135 POC TEST

LABEL: POC TEST// @

SURE YOU WANT TO DELETE THE ENTIRE 'POC TEST' FIELD? Y (Yes)

OK TO DELETE 'POC TEST' FIELDS IN THE EXISTING ENTRIES? Yes// (Yes)...........

Select FIELD: 136 CALCULATION TEST

LABEL: CALCULATION TEST// @

SURE YOU WANT TO DELETE THE ENTIRE 'CALCULATION TEST' FIELD? Y (Yes)

OK TO DELETE 'CALCULATION TEST' FIELDS IN THE EXISTING ENTRIES? Yes// (Yes)...

Select FIELD: 137 SCANNED IMAGE TEST

LABEL: SCANNED IMAGE TEST// @

SURE YOU WANT TO DELETE THE ENTIRE 'SCANNED IMAGE TEST' FIELD? Y (Yes)

OK TO DELETE 'SCANNED IMAGE TEST' FIELDS IN THE EXISTING ENTRIES? Yes// (Yes).

Select FIELD: 138 BILLABLE

LABEL: BILLABLE// @

SURE YOU WANT TO DELETE THE ENTIRE 'BILLABLE' FIELD? Y (Yes)

OK TO DELETE 'BILLABLE' FIELDS IN THE EXISTING ENTRIES? Yes// (Yes)...........

Select FIELD: 139 WORKLOAD CAPTURE

LABEL: WORKLOAD CAPTURE// @

SURE YOU WANT TO DELETE THE ENTIRE 'WORKLOAD CAPTURE' FIELD? Y (Yes)

OK TO DELETE 'WORKLOAD CAPTURE' FIELDS IN THE EXISTING ENTRIES? Yes// (Yes)...

Select FIELD: 141 PERFORMING LAB (multiple)

LABEL: PERFORMING LAB// @

SURE YOU WANT TO DELETE THE ENTIRE 'PERFORMING LAB' FIELD? Y (Yes)

OK TO DELETE 'PERFORMING LAB' FIELDS IN THE EXISTING ENTRIES? Yes// (Yes).....

Select FIELD:

Select OPTION:

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful back-out of the routines updated by the patch may be verified by running the CHECK1^XTSUMBLD utility from the programmer prompt for LR\*5.2\*500. If the backout was successful, the message “Routine not in this UCI” will display next to the LR500PO routine and the other routine checksums should be the pre-LR\*5.2\*500 values.

D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: LR\*5.2\*500 LAB SERVICE

LR500PO Routine not in this UCI.

LRMLACM value = 18901427 Missing patch number

LRMLED value = 152483182 Missing patch number

LRMLEDA value = 133294860 Missing patch number

LRMLWT value = 37343726 Missing patch number

done

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out Patch LR\*5.2\*500, successful back-out of the fields installed and modified by the patch may be verified by running a global listing from the VistA server command line after installation.

Example – global listing of backed out globals:

\>D P^DI

VA FileMan 22.2

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: LABORATORY TEST// (3412 entries)

GO TO What File: LABORATORY TEST// (3412 entries)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD// BRIEF

ALPHABETICALLY BY LABEL? No// (No)

Start with field: FIRST// 134 ??

Start with field: FIRST// 135 ??

Start with field: FIRST// 136 ??

Start with field: FIRST// 137 ??

Start with field: FIRST// 138 ??

Start with field: FIRST// 139 ??

Start with field: FIRST// 141 ??

Start with field: FIRST// ^

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: LABORATORY TEST// 66.4 LAB MLTF MANAGED ITEMS

(1 entry)

GO TO What File: LAB MLTF MANAGED ITEMS// (1 entry)

Select LISTING FORMAT: STANDARD// C

1 CONDENSED

2 CUSTOM-TAILORED

CHOOSE 1-2: 1 CONDENSED

DEVICE: ;;9999 secure Right Margin: 80//

CONDENSED DATA DICTIONARY---LAB MLTF MANAGED ITEMS FILE (#66.4)UCI: STLVETSDEV,ROU VERSION: 5.2

STORED IN: ^LAB(66.4, FEB 13,2018 PAGE 1

--------------------------------------------------------------------------------

FILE SECURITY

DD SECURITY : @ DELETE SECURITY: @

READ SECURITY : @ LAYGO SECURITY : @

WRITE SECURITY : @

CROSS REFERENCED BY:

INSTITUTION POINTER(ANM) INSTITUTION POINTER(B)

FILE STRUCTURE

FIELD FIELD

NUMBER NAME

.01 INSTITUTION POINTER (RP4'X), \[0;1\]

.02 NTRT SEND METHOD (S), \[0;2\]

.03 AUTO REMINDERS PARAMETER (NJ3,0), \[0;3\]

.04 AUDIT PURGE DAYS (NJ3,0), \[0;4\]

.05 ISAAC ACTIVE (S), \[0;5\]

.06 LAB IEN (NJ8,0), \[0;6\]

.07 SUBSCRIPT FOR NTRT (S), \[0;7\]

.08 LAST AUTO TEST ID (F), \[0;8\]

.1 SEND NTRT MESSAGES (S), \[0;10\]

1 DEFAULT NTRT MAIL GROUP (F), \[1;1\]

2 DEFAULT SITE LAB MAIL GROUP (F), \[2;1\]

3 SITE LAB SERVER (F), \[3;1\]

4 ISAAC WEB ADDRESS (F), \[4;1\]

5 ISAAC PORT NUMBER (NJ10,0), \[4;2\]

6 ISAAC NTRT PATH (FX), \[5;1\]

7 ISAAC SCHEMA NAME (F), \[6;1\]

8 ISAAC SCHEMA PATH (FX), \[6;2\]

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A