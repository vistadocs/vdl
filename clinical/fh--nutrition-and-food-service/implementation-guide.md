---
title: Nutrition & Food Services Version 5.5 Installation/Implementation Guide
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: anchor
doc_subject: Installation/
app_code: FH
app_name: Nutrition and Food Service
section: CLI
app_status: active
pkg_ns: FH
patch_ver: 5.5
patch_id: FH*5.5
group_key: "FH:FH:5.5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - nutrition
  - outpatient
  - service
  - installation
  - meals
  - food
  - software
  - locations
page_count: 0
word_count: 2708
section_count: 20
table_count: 13
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 02/25/2005
revision_oldest: 02/25/2005
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh5_5ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh5_5ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=67"
---

![](nutrition-food-services-version-5-5-installation-implementation-guide/001.png)

*Nutrition and Food ServiceOutpatient MealsInstallation/Implementation Guide*

![](nutrition-food-services-version-5-5-installation-implementation-guide/002.png)

*Version 5.5February 2005Department of Veterans AffairsVistA Health System Design and Development*Revision History

| Date   | Description            |
|------------|----------------------------|
| 02/25/2005 | Revised as per EVS review. |

  
Table of Contents

Notice of Service Name Change

Pursuant to Department of Veterans Affairs (VA) Veterans Health Administration (VHA) Directive 10-95-031, Nutrition and Food Service (N&FS) will be the official nomenclature used as the new service name for Dietetic Service in VHA central office and at VA healthcare facilities.

Therefore, all supporting documentation and customer education materials will use the Nutrition and Food Service nomenclature in place of the former Dietetics Service in all contexts.

The change aligns this program more closely with the nomenclature recognized by national accrediting bodies, professional organizations, and other healthcare agencies.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Recommended Users](#recommended-users)
  - [Orientation](#orientation)
  - [Software and Manual Retrieval](#software-and-manual-retrieval)
  - [VistA Intranet](#vista-intranet)
  - [Related Manuals](#related-manuals)
  - [Screen Displays](#screen-displays)
- [Pre-Installation Information](#pre-installation-information)
  - [Target Audience](#target-audience)
  - [Test Sites](#test-sites)
  - [Hardware and Operating Systems Requirements](#hardware-and-operating-systems-requirements)
  - [System Performance Capacity](#system-performance-capacity)
  - [Software Installation Time](#software-installation-time)
  - [Backup Routines](#backup-routines)
  - [Name Space](#name-space)
  - [VistA Software Requirements](#vista-software-requirements)
  - [Required Patches](#required-patches)
- [Pre-Installation Instructions](#pre-installation-instructions)
  - [Load and Install Patch FH55.KID](#load-and-install-patch-fh55kid)
  - [Routines and Checksums](#routines-and-checksums)
- [Implementation](#implementation)
  - [Site Parameters](#site-parameters)
  - [Outpatient Locations](#outpatient-locations)
- [Glossary](#glossary)
The Nutrition & Food Service (N&FS) Outpatient Meals Version 5.5 software combines the existing inpatient functionality in the Dietetics V. 5.0 software with an additional module that provides the capability of entering, tracking, and reporting outpatient meals.
- Provides electronic order entry of meals to authorized outpatients when they are kept over mealtimes.
- Enables electronic order entry of meals for other authorized users such as residents, without compensation employees and volunteers.
- Facilitates and tracks the number of meals for each Enhanced Sharing Agreement (selling of meal services), such as the Salvation Army or a Meals-on Wheels program.
- Provides tracking, reporting and projection features currently for Inpatients that will also include Outpatients.
- Provides the ability to request, authorize, print, cancel, and view status of Outpatient Special Meals.
- Provides the ability to request and print Guest Meals.
- Provides the ability to request Recurring Meals for a regularly scheduled outpatient including a patient profile, meal status, early/late trays, tube feeding, and additional orders.
- Creates new reports and modifications of some existing Nutrition options to include Outpatient data.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Preparing your site for the installation and implementation of Nutrition and Food Service Outpatient Meals v.5.5 helps to ensure a smooth integration. This installation guide is designed to help you do just that. It includes detailed information such as system requirements; installation time estimates and instructions; and procedures that will get you up and running quickly with Nutrition and Food Service Outpatient Meals v.5.5.

Target Audience

We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package.

- Information Resources Management (IRM)
- Clinical Application Coordinator (CAC) – called Applications Package Coordinator (ADPAC) at some sites
- Enterprise VistA Support (EVS)
- Software Quality Assurance (SQA)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pre-installation Information section provides information needed beforehand to install FH5_5.KID.

> Installation Instructions section contains instructions and examples of FH5_5.KID installation process.

> Implementation Instructions provides directions for implementing FH5_5.KID.

## Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software and documentation files are exported as part of this software.

|               |                    |                      |
|---------------|--------------------|----------------------|
| File Name | Contents       | Retrieval Format |
| FH5_5.KID     | KIDS Build         | ASCII                |
| FH5_5IG.PDF   | Installation Guide | BINARY               |
| FH5_5RN.PDF   | Release Notes      | BINARY               |
| FH5_5TM.PDF   | Technical Manual   | BINARY               |
| FH5_5UM.PDF   | User Manual        | BINARY               |
| FH5_5ADP.PDF  | ADPAC/Manager User | BINARY               |

The software files are available on the following OI Field Offices' \[ANONYMOUS.SOFTWARE\] directories. Use the following FTP address to connect to the first available FTP server: download.vista.med.va.gov

|                                    |                                    |                                    |
|------------------------------------|------------------------------------|------------------------------------|
| OIFO                           | FTP Address                    | Directory                      |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

## VistA Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online Documentation for this product will be available on the intranet at the following address: <http://www.va.gov/vdl/>. This address takes you to the VistA Documentation Library (VDL), which has a listing of all the clinical software manuals. Click on the Nutrition and Food Service link and it will take you to the Nutrition and Food Service Outpatient Meals v.5.5 documentation.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- *Nutrition and Food Service Outpatient Meals v.5.5 Release Notes*
- *Nutrition and Food Service Outpatient Meals v.5.5 Technical Manual and Security Guide*
- *Nutrition and Food Service Outpatient Meals v.5.5 Installation/Implementation Guide*
- *Nutrition and Food Service Outpatient Meals v.5.5 User Manual*
- *Nutrition and Food Service Outpatient Meals v.5.5 ADPAC/Manager Guide*

You can also access the Nutrition and Food Service Outpatient Meals v.5.5 home page by using the following address:

<span class="mark">REDACTED</span>

## Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing Outpatient Meals V. 5.5, review this section to learn the many conventions used throughout this guide.

- Keyboard Responses: Keys provided in boldface, within the copy, help you quickly identify what to press on your keyboard to perform an action. For example, when you see enter in the copy, press this key on your keyboard.
- Screen Captures: Provide “shaded” examples of what you will see on your computer screen, and possible user responses. The computer dialogue appears in Courier font.
- Notes: Provided within the steps, describe exceptions or special cases about the information presented. They reflect the experience of our staff, developers, and testers.

> **NOTE:** This *boxed* element highlights special details about the current topic.

- Other Names: File and field names, and Security keys provided in uppercase. For example, you may select a paitient's name from the PATIENT file (#2).
- Menu Options: Provided in italics. For example, you may establish Electronic Signatures Codes using the Kernel Electronic Signature code Edit \[XUSESIG\] option.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Preparing your site for the installation and implementation of Nutrition and Food Service Outpatient Meals v.5.5 helps to ensure a smooth integration. This Installation Guide is designed to help you do just that. It includes detailed information such as system requirements; installation time estimates and instructions; and procedures that will get you up and running quickly with Nutrition and Food Service Outpatient Meals V. 5.5.

## Target Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package.

- Development Engineering
- Information Resources Management (IRM)
- Clinical Application Coordinator (CAC) – called Applications Package Coordinator (ADPAC) at some sites
- Enterprise VistA Support (EVS)
- Software Quality Assurance (SQA)

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Nutrition and Food Service Outpatient Meals v.5.5 software was tested at the following sites:

|                                    |                                                   |                                                   |
|------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Test Sites                     | Alpha                                         | Beta                                          |
| <span class="mark">REDACTED</span> | ![](nutrition-food-services-version-5-5-installation-implementation-guide/003.png) | ![](nutrition-food-services-version-5-5-installation-implementation-guide/004.png) |
| <span class="mark">REDACTED</span> | ![](nutrition-food-services-version-5-5-installation-implementation-guide/005.png) | ![](nutrition-food-services-version-5-5-installation-implementation-guide/006.png) |
| <span class="mark">REDACTED</span> | ![](nutrition-food-services-version-5-5-installation-implementation-guide/007.png) | ![](nutrition-food-services-version-5-5-installation-implementation-guide/008.png) |
| <span class="mark">REDACTED</span> | ![](nutrition-food-services-version-5-5-installation-implementation-guide/009.png) | ![](nutrition-food-services-version-5-5-installation-implementation-guide/010.png) |
| <span class="mark">REDACTED</span> | ![](nutrition-food-services-version-5-5-installation-implementation-guide/011.png) | ![](nutrition-food-services-version-5-5-installation-implementation-guide/012.png) |
| <span class="mark">REDACTED</span> | ![](nutrition-food-services-version-5-5-installation-implementation-guide/013.png) | ![](nutrition-food-services-version-5-5-installation-implementation-guide/014.png) |
| <span class="mark">REDACTED</span> | ![](nutrition-food-services-version-5-5-installation-implementation-guide/015.png) | ![](nutrition-food-services-version-5-5-installation-implementation-guide/016.png) |

## Hardware and Operating Systems Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Nutrition and Food Service Outpatient Meals v.5.5 software runs on the standard hardware platforms used by the Department of Veterans Affairs Healthcare facilities. These systems consist of Alpha Clusters running VMS (version 7.2-1 minimum) and DSM (version 7.2.1 VA1) or an Alpha 1000A running Windows NT (service pack 6) and Cache M operating system (version 3.2.31.1)

## System Performance Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no significant changes in the performance capacity of the VistA operating system once the Nutrition and Food Service Outpatient Meals v.5.5 software is installed and after the registry has been created. The software should not create any appreciable global growth or network transmission problems. There are no memory constraints.

## Software Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The estimated installation time is less than three hours during off peak hours.

## Backup Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that a backup of the transport global be performed before installing the software.

## Name Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Nutrition and Food Service Outpatient Meals v.5.5 software name space is FH.

## VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing Nutrition and Food Service Outpatient Meals v.5.5, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).

| Application Name       | Minimum Version Needed |
|----------------------------|----------------------------|
| Allergy Tracking System    | 4.0                        |
| CPRS                       | 3.0                        |
| Kernel                     | 8.0                        |
| Nutrition and Food Service | 5.0                        |
| PIMS                       | 5.3                        |
| VA FileMan                 | 22.0                       |
| MailMan                    | 8.0                        |
| Consult Tracking           | 3.0                        |
| Dietetics                  | 5.0                        |

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the installation of Nutrition and Food Service Outpatient Meals v.5.5, the following patches must be installed.

|                            |             |
|----------------------------|-------------|
| Application Name       | Patches |
| Nutrition and Food Service | FH\*5\*41   |

Patch (v)FH\*5\*41 must be installed before \`Nutrition and Food Service v.5.5.

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- You should install the Nutrition and Food Service Outpatient Meals v.5.5 during off peak hours when there are fewer users are on the system. This build should be installed when the Nutrition users are off the system.
- Installation of this software takes less than three hours to install, depending on the number of records in NUTRITION PERSON file (#115) that need to be converted. The build contains a post-init routine which converts the NAME field (#.01) of file (#115) from a pointer to PATIENT file (#2) to a free text field that is used to point to either file (#2), or NEW PERSON file (#200).
- Nutrition options do not need to be disabled during the installation of this build.
- If the FH\* routines are mapped at your site, remember to disable mapping before installing the build and to re-enable it when you are finished.
- Nutrition and Food Service Outpatient Meals v.5.5 uses the Kernel Installation and Distribution System (KIDS). For further instructions on using KIDS, please refer to the *Kernel V. 8.0 Systems Manual*.
- Use the Install Package(s) option when prompted for INSTALL NAME select the package: DIETETICS 5.5.
- Select Installation Option: 1Load a Distribution
- Enter a Host File: FH5_5.KID

## Load and Install Patch FH5_5.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Kernel Installation and Distribution Systems (KIDS) menu, select the Installation menu \[XPD INSTALLATION MENU\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option:Installation

Load the distribution to the transport global.

This build should be installed when the NUTRITION users are off the system. No NUTRITION options need to be disabled during the installation of this build.

When installed into an account for the first time, this build could take 1-3 hours to install, depending on the number of records in file \#115, NUTRITION PERSON. The build contains a post-init routine that converts the .01 field of file \#115 from a pointer to file \#2 PATIENT to a free text field that is used to store a variable pointer to either file \#2 or file \#200 NEW PERSON.

If the FH\* routines are mapped at your site, remember to disable mapping before installing the build and to re-enable it when you are finished.

From the Kernel Installation and Distribution System Menu, select the Installation menu. Use the Load a Distribution option. When prompted for a Host File, enter the host file named FH5_5.KID. You may need to indicate the full path to the directory containing this file.

Sites may optionally use any or all of the following KIDS menu options:

- Verify Checksums in Transport Global
- Print Transport Global
- Compare Transport Global to Current System
- Backup a Transport Global

Use the Install Package(s) option, and when prompted for INSTALL NAME, select the package: DIETETICS 5.5.

The following messages may appear and are normal:

> Checking Install for Package DIETETICS 5.5

> Install Questions for DIETETICS 5.5

> Incoming Files:

> 111 DIETS

> Note: You already have the 'DIETS' File.

> 111.1 DIET PATTERNS

> Note: You already have the 'DIET PATTERNS' File.

> 112 FOOD NUTRIENTS

> Note: You already have the 'FOOD NUTRIENTS' File.

> 112.2 DRI VALUES

> Note: You already have the 'DRI VALUES' File.

> 112.6 USER MENU

> Note: You already have the 'USER MENU' File.

> 113 INGREDIENT

> Note: You already have the 'INGREDIENT' File.

> 113.1 STORAGE LOCATION

> Note: You already have the 'STORAGE LOCATION' File.

> 113.2 FH VENDOR

> Note: You already have the 'FH VENDOR' File.

> 114 RECIPE

> Note: You already have the 'RECIPE' File.

> 114.1 RECIPE CATEGORY

> Note: You already have the 'RECIPE CATEGORY' File.

> 114.2 PREPARATION AREA

> Note: You already have the 'PREPARATION AREA' File.

> 114.3 SERVING UTENSIL

> Note: You already have the 'SERVING UTENSIL' File.

> 114.4 EQUIPMENT

> Note: You already have the 'EQUIPMENT' File.

> 115 NUTRITION PERSON

> \* BUT YOU ALREADY HAVE ‘DIETETICS PATIENT’ AS FILE \#115!

> Shall I write over your DIETETICS PATIENT File? YES//

> 115.2 FOOD PREFERENCES

> Note: You already have the 'FOOD PREFERENCES' File.

> 115.3 NUTRITION CLASSIFICATION

> Note: You already have the 'NUTRITION CLASSIFICATION' File.

> 115.4 NUTRITION STATUS

> Note: You already have the 'NUTRITION STATUS' File.

> 115.5 DIETETIC NUTRITION PLAN

> Note: You already have the 'DIETETIC NUTRITION PLAN' File.

> 115.6 ENCOUNTER TYPES

> Note: You already have the 'ENCOUNTER TYPES' File.

> 115.7 DIETETIC ENCOUNTERS

> Note:  You already have the 'DIETETIC ENCOUNTERS' File.

> 116 MENU CYCLE

> Note: You already have the 'MENU CYCLE' File.

> 116.1 MEAL

> Note: You already have the 'MEAL' File.

> 116.2 PRODUCTION DIET

> Note: You already have the 'PRODUCTION DIET' File.

> 116.3 HOLIDAY MEALS

> Note: You already have the 'HOLIDAY MEALS' File.

> 117 MEALS SERVED

> Note: You already have the 'MEALS SERVED' File.

> 117.1 STAFFING DATA

> Note: You already have the 'STAFFING DATA' File.

> 117.2 DIETETIC COST OF MEALS

> Note: You already have the 'DIETETIC COST OF MEALS' File.

> 117.3 ANNUAL REPORT

> Note: You already have the 'ANNUAL REPORT' File.

> 117.4 DIETETIC REPORT CATEGORIES

> Note: You already have the 'DIETETIC REPORT CATEGORIES' File.

> 118 SUPPLEMENTAL FEEDINGS

> Note: You already have the 'SUPPLEMENTAL FEEDINGS' File.

> 118.1 SUPPLEMENTAL FEEDING MENU

> Note: You already have the 'SUPPLEMENTAL FEEDING MENU' File.

> 118.2 TUBEFEEDING

> Note: You already have the 'TUBEFEEDING' File.

> 118.3 STANDING ORDERS

> Note: You already have the 'STANDING ORDERS' File.

> 119 DIETITIAN TICKLER FILE

> Note: You already have the 'DIETITIAN TICKLER FILE' File.

> 119.1 UNITS

> Note: You already have the 'UNITS' File.

> 119.4 ISOLATION/PRECAUTION TYPE

> Note: You already have the 'ISOLATION/PRECAUTION TYPE' File.

> 119.5 DIETETIC CONSULTS

> Note: You already have the 'DIETETIC CONSULTS' File.

> 119.6 NUTRITION LOCATION

> \* BUT YOU ALREADY HAVE ‘DIETETICS WARD’ AS FILE \#199.6!

> Shall I write over your DIETETICS WARD File? YES//

> 119.71 PRODUCTION FACILITY

> Note: You already have the 'PRODUCTION FACILITY' File.

> 119.72 SERVICE POINT

> Note: You already have the 'SERVICE POINT' File.

> 119.73 COMMUNICATION OFFICE

> Note: You already have the 'COMMUNICATION OFFICE' File.

> 119.74 SUPPLEMENTAL FEEDING SITE

> Note: You already have the 'SUPPLEMENTAL FEEDING SITE' File.

> 119.8 NUTRITION EVENTS

> \* BUT YOU ALREADY HAVE ‘DIETETICS EVENTS’ AS FILE \#199.8!

> Shall I write over your DIETETICS EVENTS File? YES//

> 119.9 FH SITE PARAMETERS

> Note: You already have the 'FH SITE PARAMETERS' File.

The following is the recommended response to installation questions:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Enter YES

> Want KIDS to INHIBIT LOGONs during the install? YES//

Enter NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

Enter NO

 

The following is an example of how the installation may appear:

> Install Started for DIETETICS 5.5:

> Mar 01, 2005@12:57:55

> Build Distribution Date: Feb 02, 2005

> Installing Routines:

> Mar 01, 2005@12:58

> Running Pre-Install Routine: ^FH55PRE

> Installing Data Dictionaries:

> Mar 01, 2005@12:58:06

> Installing PACKAGE COMPONENTS:

> Installing BULLETIN

> Installing SECURITY KEY

> Installing PRINT TEMPLATE

> Installing INPUT TEMPLATE

> Installing PROTOCOL

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Located in the FH (DIETETICS) namespace.

> Installing OPTION

> Mar 01, 2005@12:58:30

> Running Post-Install Routine: ^FH55PST...........................

> .................................................................

> Updating Routine file...

> Updating KIDS files...

> DIETETICS 5.5 Installed.

> Mar 01, 2005@13:00:27

> Install Message sent \#27829

> Call MENU rebuild

> Starting Menu Rebuild: Mar 01, 2005@13:00:29

> Collecting primary menus in the New Person file...

> Primary menus found in the New Person file  
>                     ------------------------------------------

> OPTION NAME         MENU TEXT                    \# OF         LAST     LAST  
>                                                  USERS        USED     BUILT

> EVE                 Systems Manager Menu         71         08/16/04   08/10/04  
> XUCORE              Core Applications            1          02/20/94   08/10/04  
> LRMENU              Laboratory DHCP Menu         1          09/30/95   08/10/04  
> LR GET              Phlebotomy menu              1          08/03/95   08/10/04  
> LRWARDM             Ward lab menu                1          06/21/93   08/10/04  
> PSO MANAGER         Outpatient Pharmacy Manager  1          02/26/98   08/10/04  
> XMUSER              MailMan Menu                 4                     08/10/04  
> RA OVERALL          Rad/Nuc Med Total System ... 4          01/31/03   08/10/04  
> SROMENU             Surgery Menu                 1                     08/10/04  
> ORMGR               CPRS Manager Menu            1                     08/10/04  
> PSJU MGR            Unit Dose Medications        1          07/15/93   08/10/04  
> A4A0 TRNG COOR MENU ISC4 Trng Coordinator Menu   1          08/13/93   08/10/04  
>                                 Rebuilding Menus                                 
> ─────────────────────────────────────────────────────────────────  
> IMR MENU (MANAGEMENT)  
>                     Immunology Study Manageme... 1                     08/10/04  
> OR MAIN MENU CLINICIAN  
>                     Clinician Menu               3          04/02/98   08/10/04  
> IB MANAGER MENU     Integrated Billing Master... 1                     08/10/04  
> RMPR OFFICIAL       Prosthetic Official's Menu   1          10/28/03   08/10/04  
> EEO COUNSELORS MENU Counselor's Menu             4          08/22/96   08/10/04  
> FSW WORKLOAD REPORTING  
>                     Customer Service Workload... 1          11/06/95   08/10/04  
> PRCZ OVERALL        Overall IFCAP Menu For Tr... 3          08/18/04   08/10/04  
> ZZMJB               MIKE'S PRIMARY MENU          2          03/19/98   08/10/04  
> ACVSAM              SAM'S MENU                   1          07/18/02   08/10/04

> Building secondary menu trees....

> Merging.... done.

> Menu Rebuild Complete:  Aug 18, <2004@10:11:06>  
> ─────────────────────────────────────────────────────────────────  
>           ┌────────────────────────────────────────────────────────────┐  
>   100%    │             25             50             75               │  
> Complete  └────────────────────────────────────────────────────────────┘

> Install Completed

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global  
> 4 Compare Transport Global to Current System  
> 5 Backup a Transport Global  
> 6 Install Package(s)  
> Restart Install of Package(s)  
> Unload a Distribution

> Select Installation Option:

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Routines and Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The D CHECK^XTSUMBLD option determines the current checksum of selected routine (s). The checksum of the routine is determined as follows:

1.  Any comment line with a single semicolon is presumed to be followed by comments. Only the line tag will be included.
2.  Line 2 will be excluded from the count.
3.  The total value of the routine is determined by taking and multiplying the ASCII value of each character by its position on the line being checked.

Select one of the following:

- P Package
- B Build

Build from: Build

This will check the routines from a BUILD file.

The following routines are included in Nutrition and Food Service Outpatient Meals v.5.5.

|                          |                           |                          |
|--------------------------|---------------------------|--------------------------|
| FH value = 2393060       | FH55PRE value = 782079    | FH55PST value = 1820485  |
| FHADM2 value = 5099639   | FHADM21 value = 7831940   | FHADM2A value = 2679539  |
| FHADM3 value = 5873579   | FHADM4 value = 9650115    | FHADM5 value = 323152    |
| FHADR1 value = 6121234   | FHADR10 value = 2472024   | FHADR1A value = 6939546  |
| FHADR2 value = 3878014   | FHADR3 value = 1811235    | FHADR3A value = 6395711  |
| FHADR4 value = 3651849   | FHADR5 value = 3779837    | FHADR6 value = 10011048  |
| FHADR61 value = 2724873  | FHADR7 value = 6397935    | FHADR8 value = 3103134   |
| FHADR81 value = 5662701  | FHADR9 value = 7557968    | FHADR9A value = 5781384  |
| FHADRPT value = 3023478  | FHADRSY value = 1383849   | FHASC value = 1661812    |
| FHASE value = 12541703   | FHASE1 value = 4780508    | FHASE1A value = 10243736 |
| FHASE2 value = 5223034   | FHASE3 value = 1585843    | FHASM1 value = 8988353   |
| FHASM2 value = 8399539   | FHASM2A value = 2430817   | FHASM2B value = 3386101  |
| FHASM2C value = 3102927  | FHASM2D value = 2275862   | FHASM3 value = 5096802   |
| FHASM3A value = 9169407  | FHASM4 value = 7260022    | FHASM5 value = 8945494   |
| FHASM6 value = 7486877   | FHASM7 value = 9760313    | FHASMR value = 2838618   |
| FHASMR1 value = 10075474 | FHASN value = 3426921     | FHASN1 value = 3742277   |
| FHASN3 value = 6030523   | FHASN4 value = 10006482   | FHASN5 value = 8819802   |
| FHASN6 value = 7923491   | FHASN7 value = 2602313    | FHASN71 value = 9437034  |
| FHASP value = 8395017    | FHASP1 value = 8312844    | FHASP2 value = 3570450   |
| FHASXR value = 7601463   | FHASXR1 value = 9006803   | FHBIR value = 8127227    |
| FHCLN value = 756893     | FHCMS1 value = 1656360    | FHCMSR value = 4599993   |
| FHCMSR1 value = 6665228  | FHCTF value = 681451      | FHCTF1 value = 6791721   |
| FHCTF2 value = 620510    | FHCTF3 value = 14861699   | FHCTF4 value = 6582613   |
| FHCTF5 value = 6284618   | FHDCR1 value = 8735169    | FHDCR11 value = 8366643  |
| FHDCR1A value = 13255630 | FHDCR1B value = 9407007   | FHDCR1C value = 2164213  |
| FHDCR1D value = 10597102 | FHDCR2 value = 1181493    | FHDEV value = 1319169    |
| FHDMP value = 10110673   | FHDMP1 value = 3325867    | FHDMP2 value = 5924020   |
| FHDMP3 value = 4967182   | FHDMP4 value = 7899079    | FHDMP5 value = 5238764   |
| FHDPA value = 2049784    | FHDPGM value = 1667403    | FHDPSM value = 2716567   |
| FHENV value = 79312      | FHIPST6 value = 700221    | FHLABEL value = 4312884  |
| FHMADM2 value = 5973175  | FHMADM21 value = 16057620 | FHMADM2A value = 3726314 |
| FHMADM3 value = 11070198 | FHMADM4 value = 16679518  | FHMASE value = 12490277  |
| FHMASE1 value = 5823242  | FHMASE1A value = 14479670 | FHMMBRPT value = 7386602 |
| FHMMNADM value = 9459290 | FHMMNPRT value = 14742749 | FHMMNREP value = 8554301 |
| FHMNADM value = 3747789  | FHMNBRPT value = 2664485  | FHMNINQ value = 3048115  |
| FHMNPRT value = 8184781  | FHMNREP value = 5978199   | FHMTK value = 7722074    |
| FHMTK1 value = 9099540   | FHMTK11 value = 11735592  | FHMTK1A value = 5920546  |
| FHMTK1B value = 10574665 | FHMTK1C value = 8620526   | FHMTK2 value = 4933044   |
| FHMTK21 value = 5836943  | FHMTK3 value = 7184609    | FHMTK4 value = 7635361   |
| FHMTK5 value = 8493131   | FHMTK6 value = 7247131    | FHMTK7 value = 5201484   |
| FHMTK8 value = 9101726   | FHMTKO value = 8487911    | FHNO1 value = 2554062    |
| FHNO2 value = 12273770   | FHNO21 value = 6959419    | FHNO3 value = 3504490    |
| FHNO31 value = 8155360   | FHNO4 value = 1121656     | FHNO41 value = 9787088   |
| FHNO5 value = 5504124    | FHNO6 value = 9951272     | FHNO7 value = 2420941    |
| FHNO8 value = 2809367    | FHNU value = 1616737      | FHNU1 value = 4573798    |
| FHNU10 value = 5868490   | FHNU11 value = 10048442   | FHNU12 value = 5473461   |
| FHNU2 value = 12336623   | FHNU3 value = 6836253     | FHNU4 value = 11724524   |
| FHNU5 value = 10455147   | FHNU6 value = 4729663     | FHNU7 value = 5806572    |
| FHNU8 value = 7921572    | FHNU9 value = 4484537     | FHNUT value = 4384530    |
| FHOMAPI value = 763322   | FHOMDMP value = 6770629   | FHOMDPA value = 2651021  |
| FHOMELT value = 2016540  | FHOMGP1 value = 2813402   | FHOMGR1 value = 3118003  |
| FHOMIP value = 1356283   | FHOMPP value = 7069249    | FHOMPP1 value = 13298929 |
| FHOMRA1 value = 4387944  | FHOMRBL1 value = 7136445  | FHOMRBLD value = 8338364 |
| FHOMRC1 value = 4337575  | FHOMRE1 value = 7697070   | FHOMRMD value = 6282416  |
| FHOMRO1 value = 14538804 | FHOMRO2 value = 7575095   | FHOMRO3 value = 2692288  |
| FHOMRP1 value = 3934060  | FHOMRR1 value = 6837334   | FHOMRT1 value = 7938638  |
| FHOMSA1 value = 2801044  | FHOMSC1 value = 1027946   | FHOMSP1 value = 4349806  |
| FHOMSR1 value = 5776286  | FHOMSS1 value = 3045610   | FHOMTK1 value = 2915375  |
| FHOMTK2 value = 11158197 | FHOMUPD value = 463486    | FHOMUTL value = 7088027  |
| FHOMWOR value = 6693069  | FHORC value = 4195898     | FHORC1 value = 3494894   |
| FHORC2 value = 10525523  | FHORC3 value = 7628724    | FHORC4 value = 2889882   |
| FHORC5 value = 2011042   | FHORD value = 3323649     | FHORD1 value = 14039767  |
| FHORD10 value = 7252211  | FHORD11 value = 10488552  | FHORD13 value = 14504593 |
| FHORD1A value = 3682245  | FHORD2 value = 6282474    | FHORD3 value = 6791855   |
| FHORD4 value = 5234594   | FHORD41 value = 5341907   | FHORD5 value = 5803325   |
| FHORD6 value = 11581819  | FHORD61 value = 9209461   | FHORD7 value = 7938063   |
| FHORD71 value = 11410659 | FHORD72 value = 6657144   | FHORD8 value = 6666396   |
| FHORD81 value = 10578182 | FHORD82 value = 8501055   | FHORD83 value = 3783884  |
| FHORD9 value = 12903264  | FHORD91 value = 4010823   | FHORD92 value = 7776268  |
| FHORD93 value = 10944337 | FHORDR value = 3164483    | FHORE1 value = 11283169  |
| FHORE1A value = 1924514  | FHORE2 value = 5663292    | FHORE21 value = 12395288 |
| FHORE3 value = 4225419   | FHORO value = 4177668     | FHORR value = 3622408    |
| FHORT1 value = 10824538  | FHORT10 value = 15414510  | FHORT11 value = 2516946  |
| FHORT2 value = 7152566   | FHORT3 value = 3727556    | FHORT5 value = 5364727   |
| FHORT5A value = 10419764 | FHORT5B value = 2194934   | FHORT5C value = 3326328  |
| FHORT5D value = 6780132  | FHORTR value = 2509889    | FHORX value = 1435752    |
| FHORX1 value = 11587212  | FHORX1A value = 11347667  | FHORX1B value = 4383118  |
| FHORX1C value = 8113410  | FHORX2 value = 3148937    | FHORX3 value = 8920219   |
| FHPATM value = 7828345   | FHPRC value = 5655183     | FHPRC1 value = 5569532   |
| FHPRC10 value = 12085984 | FHPRC11 value = 14258256  | FHPRC12 value = 7939270  |
| FHPRC13 value = 12022196 | FHPRC14 value = 9606339   | FHPRC2 value = 5062603   |
| FHPRC3 value = 4336625   | FHPRC4 value = 2168815    | FHPRC5 value = 1913669   |
| FHPRC6 value = 4509284   | FHPRC7 value = 3360749    | FHPRC8 value = 9089015   |
| FHPRC9 value = 7552440   | FHPRF value = 1601618     | FHPRF1 value = 14232699  |
| FHPRF1A value = 4281323  | FHPRF2 value = 2930578    | FHPRF4 value = 1651329   |
| FHPRI value = 3953742    | FHPRI1 value = 4796204    | FHPRI2 value = 8125121   |
| FHPRI3 value = 1952818   | FHPRO value = 6105945     | FHPRO1 value = 10888674  |
| FHPRO2 value = 14342192  | FHPRO3 value = 2512818    | FHPRO4 value = 5871635   |
| FHPRO4A value = 3732530  | FHPRO5 value = 4997921    | FHPRO6 value = 3001322   |
| FHPRO7 value = 1861736   | FHPRR1 value = 4227166    | FHPRR2 value = 6709251   |
| FHPRW value = 11342645   | FHPRW1 value = 4137314    | FHPRW2 value = 3704446   |
| FHPRW3 value = 4037054   | FHPRW4 value = 1975449    | FHREC value = 3913108    |
| FHREC1 value = 4357665   | FHREC2 value = 5088857    | FHREC3 value = 1924284   |
| FHREC4 value = 3456680   | FHREC5 value = 2832308    | FHREC6 value = 8846440   |
| FHREC7 value = 1770111   | FHREP value = 4497192     | FHREP1 value = 11157584  |
| FHSEL1 value = 9136926   | FHSEL2 value = 11181038   | FHSEL3 value = 6642148   |
| FHSEL4 value = 6631600   | FHSP value = 962380       | FHSP1 value = 13812346   |
| FHSP11 value = 4199493   | FHSPED value = 12339211   | FHSPTAB value = 6582374  |
| FHSYSF value = 798296    | FHSYSK value = 4219367    | FHSYSP value = 1568629   |
| FHVER value = 1524619    | FHWADM value = 6861969    | FHWDIS value = 8981841   |
| FHWDISD value = 3391790  | FHWGMR value = 799404     | FHWHEA value = 13316807  |
| FHWMAS value = 1687237   | FHWOR value = 12475464    | FHWOR1 value = 2211384   |
| FHWOR2 value = 8091869   | FHWOR3 value = 10816921   | FHWOR31 value = 2183633  |
| FHWOR4 value = 5632033   | FHWOR5 value = 9021388    | FHWOR51 value = 5532779  |
| FHWOR5R value = 3603229  | FHWOR6 value = 6435773    | FHWOR61 value = 5319302  |
| FHWOR7 value = 3464456   | FHWOR71 value = 15904813  | FHWOR72 value = 11802862 |
| FHWOR8 value = 3058515   | FHWORA value = 7483815    | FHWORA1 value = 11738990 |
| FHWORI value = 3970884   | FHWORP value = 4423837    | FHWORR value = 4709359   |
| FHWTRN value = 2729798   | FHXCNV value = 3514475    | FHXDB value = 12710968   |
| FHXDB1 value = 14538448  | FHXDB2 value = 9231699    | FHXIN value = 2788331    |
| FHXMOV value = 8770539   | FHXOR value = 3928601     | FHXOR3 value = 8083732   |
| FHXUTL value = 5306970   | FHXWRD value = 3823200    | FHZDOC value = 972122    |
| FHZDOC1 value = 704051   | FHZDOC2 value = 9217684   | FHZDOC3 value = 1019133  |

# Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to using the new Nutrition and Food Service Outpatient Meals v.5.5 software there are some site parameters that need to be set up to allow the system to function properly. In addition, outpatient locations should be set up in the Nutrition Locations file (#119.6 - formerly Dietetic Ward file).

> Note: At any field you can type "??" to get more details or a list of available choices, for example at Outpatient Meals Diet1 it would show a list of all the available Diets to select from.

To set the system site parameters, use the *Modify Site Parameters* option.

1.  Select the Dietetics Management Option: System Management. The following options appear:

> DF Create Dietetic File entry for all Inpatients  
> DL Update Patient Dietetic Location  
> FP Check File Pointers  
> PD Purge Dietetic Data  
> RD Recode Diets for all Inpatients  
> RI Check Integrity of Routines  
> SP Modify Site Parameters

2.  Select the System Management Option: Modify Site Parameters by entering SP.
3.  Select a printer for printing labels

> Select LABEL PRINTERS: HPLASERJET6-LABEL//  
> LABEL PRINTERS: HPLASERJET6-LABEL//  
> SIZE OF LABELS: 2-5/8 x 1 (Laser labels - 30 labels per sheet)//

4.  Indicate whether it is a multidivisional site. The default is NO.

> MULTIDIVISIONAL SITE?: NO//

5.  Enter a diet from the Diets file (#111) for each of the five fields that follow. You can enter up to 5 diets only; one in each field. Enter the diet name or enter ?? for a list of diets to choose from. These will be the only outpatient diets that are selectable for VA-outpatient locations with the OUTPATIENT MEAL DIET1 as the default outpatient diet. Non-VA outpatient locations will be able to order any diet from the Diets file.

> OUTPATIENT MEALS DIET1:

> OUTPATIENT MEALS DIET2:

> OUTPATIENT MEALS DIET3:

> OUTPATIENT MEALS DIET4:

> OUTPATIENT MEALS DIET5:

6.  Enter users who can authorize special meals. You can enter up to 5 users; one user in each field that follows. Enter a user’s name or enter ?? for a list of users from the NEW PERSON file (#200).

> AUTHORIZER 1:

> AUTHORIZER 2:

> AUTHORIZER 3:

> AUTHORIZER 4:

> AUTHORIZER 5:

7.  Enter YES or NO at the class type field if you serve these types of meals at your facility.

> EMPLOYEE CLASS:

> PAID CLASS:

> OOD CLASS:

> VOLUNTEER CLASS:

> GRATUITOUS CLASS:

8.  Enter a dollar amount for each class type of meals that you serve at your facility. If you do not serve a particular type of meal, leave that charge-related field blank.

> EMPLOYEE BREAKFAST CHARGE:

> EMPLOYEE NOON CHARGE:

> EMPLOYEE EVENING CHARGE:

> PAID BREAKFAST CHARGE:

> PAID NOON CHARGE:

> PAID EVENING CHARGE:

> OOD BREAKFAST CHARGE:

> OOD NOON CHARGE:

> OOD EVENING MEAL:

> VOLUNTEER BREAKFAST CHARGE:

> VOLUNTEER NOON CHARGE:

> VOLUNTEER EVENING CHARGE:

> GRATUITOUS BREAKFAST CHARGE:

> GRATUITOUS NOON CHARGE:

> GRATUITOUS EVENING CHARGE:

9.  Enter YES or NO to indicate a tray ticket and whether there is a heading on the bottom of the ticket. The default is YES.

> WILL YOU USE TRAY TICKETS?: YES//

> HEADING ON BOTTOM OF TICKET?: YES//

## Outpatient Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient locations are set up in the Nutrition Locations file (#119.6 - formerly Dietetic Ward file).

To set the outpatient locations, use the *Enter/Edit Nutrition Locations* option.

1.  Select Dietetics Management Option: Dietetic Facilities. The following options appear:

> CE Enter/Edit Communication Offices  
> FE Enter/Edit Production Facilities  
> NE Enter/Edit Supplemental Fdg. Sites  
> SE Enter/Edit Service Points  
> SL List Production/Service/Communication Facilities  
> SP Modify Site Parameters  
> WE Enter/Edit Nutrition Locations  
> WL List Nutrition Locations

2.  Select Dietetic Facilities Option: Enter/Edit Nutrition Locations by entering WE.
3.  Select WARD or OUTPATIENT for the type of location you wish to create.

> WARD or OUTPATIENT LOCATION:OUTPATIENT

4.  Enter the name of the Nutrition Location. As with previous versions of the software, this can be the name you want to use for Nutrition and Food Service purposes.

> Select Dietetic Facilities Option: WE Enter/Edit Nutrition Locations

> Select WARD or OUTPATIENT Location: Outpatient Location

> Select NUTRITION LOCATION NAME: SBK TESTING LOCATION

> Are you adding ‘SBK TESTING LOCATION’ as

> A new NUTRITION LOCATION (the 34<sup>TH</sup>)? No//

5.  Enter YES, and the following appears:

> NUTRITION LOCATION NAME: SBK TESTING LOCATION Replace

6.  If desired, enter an associated Hospital Location from file \#44. It is not required to link every Nutrition Location to an associated Hospital Location. However, for VA-inpatient and VA-outpatient locations, an associated Hospital Location is needed. You can associate multiple Hospital Locations with a Nutrition Location.

> ASSOCIATED HOSPITAL LOCATION:

7.  Enter YES
8.  Enter the Tray Service Point. Type ?? to select from list of service points to choose from. If this field is populated, then the next field displays.

> TRAY FORECAST %:

9.  TRAY FORECAST %. This is the percentage of patients on the ward typically receiving tray service.
10. Enter the Cafeteria Service Point. Type ?? to select from list of service points to choose from. If this field is populated, then the next field displays.
11. CAFETERIA FORECAST %:
12. Enter the Dining Room Tray Service. Enter YES or NO for whether this location will use dining room tray service. If this field is set to YES, then the next field displays.
13. DINING ROOM FORECAST %:
14. Enter the Communication Office: Enter the Communication Office you want to link this location to, or enter ?? for list of Communication Offices.
15. Enter the Max \# of Days.

> Note: This field is optional. If used, it will be set to the maximum number of days ahead a recurring meal plan can be ordered; that is, if this field is set to 365, then when ordering a recurring meal, it cannot be ordered past one year from the ordering date. If the field is left NULL, then a default of 999 days is assumed. This field will be checked upon entering the FROM/TO dates in the order/Edit Outpatient Meals option.

16. Enter the Number of Days for Review.

> Note: This field will be used for the Outpatient Meals Print Meal Plan Expiration List option. It may be set to a number of days, which will be used for review by the Max \# of Days option; that is, if this field is set to 7, then when the Print Meal Plan Expiration List option is run, it will check for recurring meal plans that will be expiring within the next 7 days.

17. Enter the Non-VA Facility. Choose from YES (Y) or NO (N).

> Note: This will be an optional YES/NO field that may be set when setting up new outpatient locations. If the field is set to YES, the Order/Edit Recurring Meal option will use this flag to allow selection of up to 5 diets from any diet in the Diets (#111) file. If the field is blank or set to NO, then the Order/Edit option will only allow selection of 1 diet from the 5 allowable diets set up in the site parameters.

18. Enter the Inpatient/Outpatient. Enter O for Outpatient Locations.
19. Enter the Print Order. Enter a numeric for the print order value.
20. Select Bulk Nourishments

The following fields are optional.

\# DAYS TO REVIEW NPO:  
\# DAYS TO REVIEW TF:  
\# DAYS TO REVIEW SF:  
\# DAYS FOR STATUS AFTER ADMIT:  
\# DAYS TO REVIEW STATUS I:  
\# DAYS TO REVIEW STATUS II:  
\# DAYS TO REVIEW STATUS III:  
\# DAYS TO REVIEW STATUS IV:  
CAFETERIA ON TRAY TICKET:  
INACTIVE?:

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term or Acronym | Description                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------|
| API                 | Application Programmer Interface                                                                             |
| CPRS                | Computerized Patient Record System                                                                           |
| DFN                 | File Number—the local/facility patient record number (patient file internal entry number)                    |
| FDA                 | Food and Drug Administration                                                                                 |
| GUI                 | Graphical User Interface                                                                                     |
| HL7                 | Health Level 7                                                                                               |
| ICN                 | Integration Control Number, or national VA patient record number                                             |
| IMG                 | Information Management Group                                                                                 |
| HSD&D               | Health System Design and Development                                                                         |
| IRM                 | Information Resource Management                                                                              |
| KIDS                | Kernel Installation and Distribution System                                                                  |
| NNAB                | National Nutrition Advisory Board                                                                            |
| ODD                 | Officer of the Day                                                                                           |
| OINT                | Office of Information National Training and Education Office                                                 |
| PCE                 | Patient Care Encounter                                                                                       |
| PTF                 | Patient Treatment File—refers to the VistA Inpatient File in the Local Registry Report, under “Reason Added” |
| SI                  | System Implementation                                                                                        |
| VA                  | Department of Veteran Affairs                                                                                |
| VERA                | Veterans Equitable Resource Allocation                                                                       |
| VHA                 | Veterans Health Administration                                                                               |
| VISN                | Veterans Integrated Service Networks                                                                         |
| VistA               | Veterans Health Information System and Technology Architecture                                               |
| WOC                 | Without Compensation                                                                                         |
