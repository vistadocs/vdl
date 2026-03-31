---
title: Nutrition & Food Services Version 5.5 Technical Manual and Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: and Security Guide
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
menu_options: 24
description: 
audience: 
keywords: 
  - blockquote
  - class
  - colspan
  - even
  - table
  - style
  - width
  - diet
  - contents
  - meals
page_count: 0
word_count: 19198
section_count: 27
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh5_5tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nutrition_Food_Service_(NFS)/fh5_5tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=67"
---

> ![](nutrition-food-services-version-5-5-technical-manual-and-security-guide/001.png)

> Nutrition and Food Service Outpatient Meals

Technical Manual and Security Guide

![](nutrition-food-services-version-5-5-technical-manual-and-security-guide/002.png)

### Version 5.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### February 2005 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA Health System Design and Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>02/25/2005</p>
</blockquote></td>
<td><blockquote>
<p>Revised as per EVS review.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark0" class="anchor"></span>Notice of Service Name Change

> Pursuant to Department of Veterans Affairs (VA) Veterans Health Administration (VHA) Directive 10- 95-031, Nutrition and Food Service (N&FS) will be the official nomenclature used as the new service name for Dietetic Service in Veterans Health Administration (VHA) central office and at VA healthcare facilities.

> Therefore, all supporting documentation and customer education materials will use the Nutrition and Food Service nomenclature in place of the former Dietetics Service in all contexts.

> The change aligns this program more closely with the nomenclature recognized by national accrediting bodies, professional organizations, and other healthcare agencies..

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Version 5.5](#version-55)
    - [February 2005 Department of Veterans Affairs](#february-2005-department-of-veterans-affairs)
    - [VistA Health System Design and Development](#vista-health-system-design-and-development)
- [Introduction](#introduction)
  - [Recommended Users](#recommended-users)
  - [Orientation](#orientation)
  - [Software and Manual Retrieval](#software-and-manual-retrieval)
  - [VistA Intranet](#vista-intranet)
  - [Related Manuals](#related-manuals)
  - [Screen Displays](#screen-displays)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Minimum Requirements](#minimum-requirements)
  - [Required Patches](#required-patches)
- [Pre-Installation Instructions](#pre-installation-instructions)
  - [Load and Install Patch FH55.KID](#load-and-install-patch-fh55kid)
  - [Routines and Checksums](#routines-and-checksums)
- [Files](#files)
  - [Modified Files](#modified-files)
  - [Existing Files](#existing-files)
  - [Pointer Relations](#pointer-relations)
  - [Exported Options](#exported-options)
  - [XINDEX](#xindex)
- [Protocols](#protocols)
- [Callable Routines/Entry Points/Application Programmer Interfaces](#callable-routinesentry-pointsapplication-programmer-interfaces)
- [External Interfaces](#external-interfaces)
- [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
- [Internal Relations](#internal-relations)
- [Package Wide Variables](#package-wide-variables)
  - [Mail Groups and Alerts](#mail-groups-and-alerts)
  - [Remote Systems](#remote-systems)
  - [Archiving](#archiving)
  - [Contingency Planning](#contingency-planning)
  - [Interfacing](#interfacing)
  - [Electronic Signatures](#electronic-signatures)
  - [Menu Assignments](#menu-assignments)
- [Package Security](#package-security)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
  - [Official Policy](#official-policy)
- [Glossary](#glossary)
  - [Acronyms and Descriptions](#acronyms-and-descriptions)
> The Nutrition & Food Service (N&FS) Outpatient Meals Version 5.5 software combines the existing inpatient functionality in the Dietetics V. 5.0 software with an additional module that provides the capability of entering, tracking, and reporting outpatient meals.
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

> We have developed this guide for members of the Automated Data Processing (ADP) group and the Information Resources Management (IRM) group who are responsible for maintaining and supporting this package.

> We assume that individuals within these groups have the following experience or skills.

- Experienced with other Veterans Health Information Systems and Technology Architecture (VistA) software
- Have worked with or will work with an Applications Package Coordinator (ADPAC) or Clinical Applications Coordinator (CAC) familiar with the medication administration process in a VAMC.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following software and documentation files are exported as part of this package.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contents</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Retrieval Format</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FH5_5.KID</p>
</blockquote></td>
<td><blockquote>
<p>KIDS Build</p>
</blockquote></td>
<td><blockquote>
<p>ASCII</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FH5_5IG.PDF</p>
</blockquote></td>
<td><blockquote>
<p>Installation Guide</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FH5_5RN.PDF</p>
</blockquote></td>
<td><blockquote>
<p>Release Notes</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FH5_5TM.PDF</p>
</blockquote></td>
<td><blockquote>
<p>Technical Manual</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FH5_5UM.PDF</p>
</blockquote></td>
<td><blockquote>
<p>User Manual</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FH5_5ADP.PDF</p>
</blockquote></td>
<td><blockquote>
<p>ADPAC/Manager User</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The software files are available on the following OI Field Offices' \[ANONYMOUS.SOFTWARE\] directories. Use the following FTP address to connect to the first available FTP server: download.vista.med.va.gov

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 33%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>OIFO</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP Address</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Directory</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

## VistA Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the Web sites listed below when you want to receive more background and technical information about Nutrition and Food Service Outpatient Meals v. 5.5, and to download this manual and related documentation.

> Online Documentation for this product is available on the intranet at the following address: [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/). This address takes you to the VistA Documentation Library (VDL), which has a

> <span id="_bookmark2" class="anchor"></span>listing of all the clinical software manuals. Click on the Nutrition and Food Service link, and it will take you to the Nutrition and Food Service Outpatient Meals v. 5.5 documentation.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- *Nutrition and Food Service Outpatient Meals v.5.5 Release Notes*
- *Nutrition and Food Service Outpatient Meals v.5.5 Technical Manual and Security Guide*
- *Nutrition and Food Service Outpatient Meals v.5.5 Installation/Implementation Guide*
- *Nutrition and Food Service Outpatient Meals v.5.5 User Manual*
- *Nutrition and Food Service Outpatient Meals v.5.5 ADPAC/Manager Guide*

> You can also access the Outpatient Meals home page by using the following address: <span class="mark">REDACTED</span>

## Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before installing Nutrition and Food Service Outpatient Meals v. 5.5, review this section to learn the many conventions used throughout this guide.

- Keyboard Responses: Keys provided in boldface, within the copy, help you quickly identify what to press on your keyboard to perform an action. For example, when you see enter in the copy, press this key on your keyboard.
- Screen Captures: Provide “shaded” examples of what you will see on your computer screen, and possible user responses. The computer dialogue appears in Courier font.
- Notes: Provided within the steps, describe exceptions or special cases about the information presented. They reflect the experience of our staff, developers, and testers.

> Note: This *boxed* element highlights special details about the current topic.

- Other Names: File and field names, and Security keys provided in uppercase. For example, you may select a patient’s name from the PATIENT file (#2).
- Menu Options: Provided in italics. For example, you may establish Electronic Signatures Codes using the Kernel Electronic Signature code Edit \[XUSESIG\] option.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Minimum Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before installing Nutrition and Food Service Outpatient Meals v. 5.5, make sure that your system includes the following Department of Veterans Affairs (VA) software packages and versions (those listed or higher).

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Application Name</p>
</blockquote></th>
<th><blockquote>
<p>Minimum Version Needed</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Allergy Tracking System</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Kernel</p>
</blockquote></td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Nutrition and Food Service</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA FileMan</p>
</blockquote></td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MailMan</p>
</blockquote></td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Consult Tracking</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Dietetics</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before the installation of Nutrition and Food Service Outpatient Meals v.5.5, the following patches must

> be installed.

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Application Name</p>
</blockquote></th>
<th><blockquote>
<p>Patches</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Nutrition and Food Service</p>
</blockquote></td>
<td><blockquote>
<p>FH*5*41</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Patch (v)FH\*5\*41 must be installed before \`Nutrition and Food Service v.5.5.

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- You should install the Nutrition and Food Service Outpatient Meals v.5.5 during off peak hours when there are fewer users are on the system. This build should be installed when the Nutrition users are off the system.
- Installation of this software takes less than three hours to install, depending on the number of records in NUTRITION PERSON file (#115) that need to be converted. The build contains a post-init routine which converts the NAME field (#.01) of file (#115) from a pointer to PATIENT file (#2) to a free text field that is used to point to either file (#2), or NEW PERSON file (#200).
- Nutrition options do not need to be disabled during the installation of this build.
- If the FH\* routines are mapped at your site, remember to disable mapping before installing the build and to re-enable it when you are finished.
- Nutrition and Food Service Outpatient Meals v.5.5 uses the Kernel Installation and Distribution System (KIDS). For further instructions on using KIDS, please refer to the *Kernel V. 8.0 Systems Manual*.
- Use the Install Package(s) option when prompted for INSTALL NAME select the package:

#### DIETETICS 5.5.

- Select Installation Option: 1 Load a Distribution
- Enter a Host File: FH5_5.KID

## Load and Install Patch FH5_5.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Kernel Installation and Distribution Systems (KIDS) menu, select the Installation menu \[XPD INSTALLATION MENU\]:

> Load the distribution to the transport global.

> This build should be installed when the NUTRITION users are off the system. No NUTRITION options need to be disabled during the installation of this build.

> When installed into an account for the first time, this build could take 1-3 hours to install, depending on the number of records in file \#115. The build contains a post-init routine which converts the .01 field of file \#115 from a pointer to file \#2 to a free text field which is used to point to either file \#2 or file \#200.

> If the FH\* routines are mapped at your site, remember to disable mapping before installing the build and to re-enable it when you are finished.

> From the Kernel Installation and Distribution System Menu, select the Installation menu. Use the Load a Distribution option. When prompted for a Host File, enter the host file named FH5_5.KID. You may need to indicate the full path to the directory containing this file.

> Sites may optionally use any or all of the following KIDS menu options:

- Verify Checksums in Transport Global
- Print Transport Global
- Compare Transport Global to Current System
- Backup a Transport Global

> Use the Install Package(s) option, and when prompted for INSTALL NAME, select the package:

> DIETETICS 5.5.

> The following messages may appear and are normal:

> Incoming Files:

111. DIETS

> Note: You already have the 'DIETS' File.

1.  DIET PATTERNS

> Note: You already have the 'DIET PATTERNS' File.

112. FOOD NUTRIENTS

> Note: You already have the 'FOOD NUTRIENTS' File.

> 112.2 DRI VALUES

> Note: You already have the 'DRI VALUES' File.

> 112.6 USER MENU

> Note: You already have the 'USER MENU' File.

113. INGREDIENT

> Note: You already have the 'INGREDIENT' File.

1.  STORAGE LOCATION

> Note: You already have the 'STORAGE LOCATION' File.

2.  FH VENDOR

> Note: You already have the 'FH VENDOR' File.

114. RECIPE

> Note: You already have the 'RECIPE' File.

1.  RECIPE CATEGORY

> Note: You already have the 'RECIPE CATEGORY' File.

2.  PREPARATION AREA

> Note: You already have the 'PREPARATION AREA' File.

3.  SERVING UTENSIL

> Note: You already have the 'SERVING UTENSIL' File.

4.  EQUIPMENT

> Note: You already have the 'EQUIPMENT' File.

115. NUTRITION PERSON

> Note: You already have the 'NUTRITION PERSON' File.

2.  FOOD PREFERENCES

> Note: You already have the 'FOOD PREFERENCES' File.

3.  NUTRITION CLASSIFICATION

> Note: You already have the 'NUTRITION CLASSIFICATION' File.

4.  NUTRITION STATUS

> Note: You already have the 'NUTRITION STATUS' File.

5.  DIETETIC NUTRITION PLAN

> Note: You already have the 'DIETETIC NUTRITION PLAN' File.

6.  ENCOUNTER TYPES

> Note: You already have the 'ENCOUNTER TYPES' File.

7.  DIETETIC ENCOUNTERS

> Note: You already have the 'DIETETIC ENCOUNTERS' File.

116. MENU CYCLE

> Note: You already have the 'MENU CYCLE' File.

1.  MEAL

> Note: You already have the 'MEAL' File.

2.  PRODUCTION DIET

> Note: You already have the 'PRODUCTION DIET' File.

3.  HOLIDAY MEALS

> Note: You already have the 'HOLIDAY MEALS' File.

117. MEALS SERVED

> Note: You already have the 'MEALS SERVED' File.

1.  STAFFING DATA

> Note: You already have the 'STAFFING DATA' File.

2.  DIETETIC COST OF MEALS

> Note: You already have the 'DIETETIC COST OF MEALS' File.

3.  ANNUAL REPORT

> Note: You already have the 'ANNUAL REPORT' File.

4.  DIETETIC REPORT CATEGORIES

> Note: You already have the 'DIETETIC REPORT CATEGORIES' File.

118. SUPPLEMENTAL FEEDINGS

> Note: You already have the 'SUPPLEMENTAL FEEDINGS' File.

1.  SUPPLEMENTAL FEEDING MENU

> Note: You already have the 'SUPPLEMENTAL FEEDING MENU' File.

2.  TUBEFEEDING

> Note: You already have the 'TUBEFEEDING' File.

3.  STANDING ORDERS

> Note: You already have the 'STANDING ORDERS' File.

119. DIETITIAN TICKLER FILE

> Note: You already have the 'DIETITIAN TICKLER FILE' File.

1.  UNITS

> Note: You already have the 'UNITS' File.

4.  ISOLATION/PRECAUTION TYPE

> Note: You already have the 'ISOLATION/PRECAUTION TYPE' File.

5.  DIETETIC CONSULTS

> Note: You already have the 'DIETETIC CONSULTS' File.

6.  NUTRITION LOCATION

> Note: You already have the 'NUTRITION LOCATION' File.

71. PRODUCTION FACILITY

> Note: You already have the 'PRODUCTION FACILITY' File.

72. SERVICE POINT

> Note: You already have the 'SERVICE POINT' File.

73. COMMUNICATION OFFICE

> Note: You already have the 'COMMUNICATION OFFICE' File.

74. SUPPLEMENTAL FEEDING SITE

> Note: You already have the 'SUPPLEMENTAL FEEDING SITE' File.

8.  DIETETIC EVENTS

> Note: You already have the 'DIETETIC EVENTS' File.

9.  FH SITE PARAMETERS

> Note: You already have the 'FH SITE PARAMETERS' File.

> The following is the recommended response to installation questions:

> Enter YES

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

> Enter NO

> Want KIDS to INHIBIT LOGONs during the install? YES//

> Enter NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

> The following is an example of how the installation may appear:

> Install Started for DIETETICS 5.5:

> Nov 02, 2004@15:10:01

> Build Distribution Date: Nov 02, 2004 Installing Routines:Nov 02, 2004@15:10:08 Running Pre-Install Routine: ^FH55PRE

> Installing Data Dictionaries: Nov 02, 2004@15:10:09 Installing PACKAGE COMPONENTS:

> Installing BULLETIN Installing SECURITY KEY Installing PRINT TEMPLATE Installing INPUT TEMPLATE Installing PROTOCOL

> Installing OPTION

> Nov 02, 2004@15:10:27

> Running Post-Install Routine: ^FH55PST Updating Routine file...

> Updating KIDS files... DIETETICS 5.5 Installed.

> Nov 02, 2004@15:10:29

> Not a production UCI

> NO Install Message sent

> Call MENU rebuild

> Starting Menu Rebuild: Nov 02, 2004@15:10:29 Collecting primary menus in the New Person file... Primary menus found in the New Person file

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 35%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OPTION</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>NAME</p>
</blockquote></th>
<th>MENU TEXT</th>
<th colspan="2"><blockquote>
<p># OF USERS</p>
</blockquote></th>
<th>LAST USED</th>
<th><blockquote>
<p>LAST BUILT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>EVE</p>
</blockquote></td>
<td></td>
<td>Systems Manager Menu</td>
<td><blockquote>
<p>71</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/16/04</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>XUCORE</p>
</blockquote></td>
<td></td>
<td>Core Applications</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>02/20/94</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>LRMENU</p>
</blockquote></td>
<td></td>
<td>Laboratory DHCP Menu</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>09/30/95</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>LR GET</p>
</blockquote></td>
<td></td>
<td>Phlebotomy menu</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/03/95</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>LRWARDM</p>
</blockquote></td>
<td></td>
<td>Ward lab menu</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>06/21/93</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PSO MANAGER</p>
</blockquote></td>
<td></td>
<td>Outpatient Pharmacy Manager</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>02/26/98</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>XMUSER</p>
</blockquote></td>
<td></td>
<td>MailMan Menu</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td colspan="2"></td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>RA OVERALL</p>
</blockquote></td>
<td></td>
<td>Rad/Nuc Med Total System ...</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>01/31/03</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>SROMENU</p>
</blockquote></td>
<td></td>
<td>Surgery Menu</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"></td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>ORMGR</p>
</blockquote></td>
<td></td>
<td>CPRS Manager Menu</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"></td>
<td>08/10/04</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PSJU MGR</p>
</blockquote></td>
<td></td>
<td>Unit Dose Medications</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>07/15/93</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>A4A0 TRNG COOR</p>
</blockquote></td>
<td><blockquote>
<p>MENU</p>
</blockquote></td>
<td>ISC4 Trng Coordinator Menu</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/13/93</p>
</blockquote></td>
<td>08/10/04</td>
</tr>
</tbody>
</table>

> Rebuilding Menus

> ─────────────────────────────────────────────────────────────────

> IMR MENU (MANAGEMENT)

> Immunology Study Manageme... 1 08/10/04 OR MAIN MENU CLINICIAN

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Clinician Menu</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th>04/02/98</th>
<th>08/10/04</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IB MANAGER MENU Integrated Billing Master...</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td><blockquote>
<p>RMPR OFFICIAL Prosthetic Official's Menu</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>10/28/03</td>
<td>08/10/04</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EEO COUNSELORS MENU Counselor's Menu</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>08/22/96</td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td><blockquote>
<p>FSW WORKLOAD REPORTING</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Customer Service Workload...</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>11/06/95</td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td>PRCZ OVERALL Overall IFCAP Menu For Tr...</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>08/18/04</td>
<td>08/10/04</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ZZMJB MIKE'S PRIMARY MENU</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>03/19/98</td>
<td>08/10/04</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACVSAM SAM'S MENU</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>07/18/02</td>
<td>08/10/04</td>
</tr>
</tbody>
</table>

> Building secondary menu trees....

> Merging. done.

> Menu Rebuild Complete: Aug 18, 2004@10:11:06

> ─────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

> Install Completed

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option:

## Routines and Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The D CHECK^XTSUMBLD option determines the current checksum of selected routine (s). The checksum of the routine is determined as follows:

1.  Any comment line with a single semicolon is presumed to be followed by comments. Only the line tag will be included.
2.  Line 2 will be excluded from the count.
3.  The total value of the routine is determined by taking and multiplying the ASCII value of each character by its position on the line being checked.

Select one of the following:

- P Package
- B Build Build from: Build

> This will check the routines from a BUILD file.

> The following routines are included in Nutrition and Food Service Outpatient Meals v.5.5.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 32%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FH value = 2393060</p>
</blockquote></th>
<th><blockquote>
<p>FH55PRE value = 782079</p>
</blockquote></th>
<th><blockquote>
<p>FH55PST value = 1820485</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FHADM2 value = 5099639</p>
</blockquote></td>
<td><blockquote>
<p>FHADM21 value = 7831940</p>
</blockquote></td>
<td><blockquote>
<p>FHADM2A value = 2679539</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHADM3 value = 5873579</p>
</blockquote></td>
<td><blockquote>
<p>FHADM4 value = 9650115</p>
</blockquote></td>
<td><blockquote>
<p>FHADM5 value = 323152</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHADR1 value = 6121234</p>
</blockquote></td>
<td><blockquote>
<p>FHADR10 value = 2472024</p>
</blockquote></td>
<td><blockquote>
<p>FHADR1A value = 6939546</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHADR2 value = 3878014</p>
</blockquote></td>
<td><blockquote>
<p>FHADR3 value = 1811235</p>
</blockquote></td>
<td><blockquote>
<p>FHADR3A value = 6395711</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHADR4 value = 3651849</p>
</blockquote></td>
<td><blockquote>
<p>FHADR5 value = 3779837</p>
</blockquote></td>
<td><blockquote>
<p>FHADR6 value = 10011048</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHADR61 value = 2724873</p>
</blockquote></td>
<td><blockquote>
<p>FHADR7 value = 6397935</p>
</blockquote></td>
<td><blockquote>
<p>FHADR8 value = 3103134</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHADR81 value = 5662701</p>
</blockquote></td>
<td><blockquote>
<p>FHADR9 value = 7557968</p>
</blockquote></td>
<td><blockquote>
<p>FHADR9A value = 5781384</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHADRPT value = 3023478</p>
</blockquote></td>
<td><blockquote>
<p>FHADRSY value = 1383849</p>
</blockquote></td>
<td><blockquote>
<p>FHASC value = 1661812</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHASE value = 12541703</p>
</blockquote></td>
<td><blockquote>
<p>FHASE1 value = 4780508</p>
</blockquote></td>
<td><blockquote>
<p>FHASE1A value = 10243736</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHASE2 value = 5223034</p>
</blockquote></td>
<td><blockquote>
<p>FHASE3 value = 1585843</p>
</blockquote></td>
<td><blockquote>
<p>FHASM1 value = 8988353</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHASM2 value = 8399539</p>
</blockquote></td>
<td><blockquote>
<p>FHASM2A value = 2430817</p>
</blockquote></td>
<td><blockquote>
<p>FHASM2B value = 3386101</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHASM2C value = 3102927</p>
</blockquote></td>
<td><blockquote>
<p>FHASM2D value = 2275862</p>
</blockquote></td>
<td><blockquote>
<p>FHASM3 value = 5096802</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHASM3A value = 9169407</p>
</blockquote></td>
<td><blockquote>
<p>FHASM4 value = 7260022</p>
</blockquote></td>
<td><blockquote>
<p>FHASM5 value = 8945494</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHASM6 value = 7486877</p>
</blockquote></td>
<td><blockquote>
<p>FHASM7 value = 9760313</p>
</blockquote></td>
<td><blockquote>
<p>FHASMR value = 2838618</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHASMR1 value = 10075474</p>
</blockquote></td>
<td><blockquote>
<p>FHASN value = 3426921</p>
</blockquote></td>
<td><blockquote>
<p>FHASN1 value = 3742277</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHASN3 value = 6030523</p>
</blockquote></td>
<td><blockquote>
<p>FHASN4 value = 10006482</p>
</blockquote></td>
<td><blockquote>
<p>FHASN5 value = 8819802</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHASN6 value = 7923491</p>
</blockquote></td>
<td><blockquote>
<p>FHASN7 value = 2602313</p>
</blockquote></td>
<td><blockquote>
<p>FHASN71 value = 9437034</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHASP value = 8395017</p>
</blockquote></td>
<td><blockquote>
<p>FHASP1 value = 8312844</p>
</blockquote></td>
<td><blockquote>
<p>FHASP2 value = 3570450</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHASXR value = 7601463</p>
</blockquote></td>
<td><blockquote>
<p>FHASXR1 value = 9006803</p>
</blockquote></td>
<td><blockquote>
<p>FHBIR value = 8127227</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHCLN value = 756893</p>
</blockquote></td>
<td><blockquote>
<p>FHCMS1 value = 1656360</p>
</blockquote></td>
<td><blockquote>
<p>FHCMSR value = 4599993</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHCMSR1 value = 6665228</p>
</blockquote></td>
<td><blockquote>
<p>FHCTF value = 681451</p>
</blockquote></td>
<td><blockquote>
<p>FHCTF1 value = 6791721</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHCTF2 value = 620510</p>
</blockquote></td>
<td><blockquote>
<p>FHCTF3 value = 14861699</p>
</blockquote></td>
<td><blockquote>
<p>FHCTF4 value = 6582613</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHCTF5 value = 6284618</p>
</blockquote></td>
<td><blockquote>
<p>FHDCR1 value = 8735169</p>
</blockquote></td>
<td><blockquote>
<p>FHDCR11 value = 8366643</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHDCR1A value = 13255630</p>
</blockquote></td>
<td><blockquote>
<p>FHDCR1B value = 9407007</p>
</blockquote></td>
<td><blockquote>
<p>FHDCR1C value = 2164213</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHDCR1D value = 10597102</p>
</blockquote></td>
<td><blockquote>
<p>FHDCR2 value = 1181493</p>
</blockquote></td>
<td><blockquote>
<p>FHDEV value = 1319169</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHDMP value = 10110673</p>
</blockquote></td>
<td><blockquote>
<p>FHDMP1 value = 3325867</p>
</blockquote></td>
<td><blockquote>
<p>FHDMP2 value = 5924020</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHDMP3 value = 4967182</p>
</blockquote></td>
<td><blockquote>
<p>FHDMP4 value = 7899079</p>
</blockquote></td>
<td><blockquote>
<p>FHDMP5 value = 5238764</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHDPA value = 2049784</p>
</blockquote></td>
<td><blockquote>
<p>FHDPGM value = 1667403</p>
</blockquote></td>
<td><blockquote>
<p>FHDPSM value = 2716567</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHENV value = 79312</p>
</blockquote></td>
<td><blockquote>
<p>FHIPST6 value = 700221</p>
</blockquote></td>
<td><blockquote>
<p>FHLABEL value = 4312884</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHMADM2 value = 5973175</p>
</blockquote></td>
<td><blockquote>
<p>FHMADM21 value = 16057620</p>
</blockquote></td>
<td><blockquote>
<p>FHMADM2A value = 3726314</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHMADM3 value = 11070198</p>
</blockquote></td>
<td><blockquote>
<p>FHMADM4 value = 16679518</p>
</blockquote></td>
<td><blockquote>
<p>FHMASE value = 12490277</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHMASE1 value = 5823242</p>
</blockquote></td>
<td><blockquote>
<p>FHMASE1A value = 14479670</p>
</blockquote></td>
<td><blockquote>
<p>FHMMBRPT value = 7386602</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHMMNADM value = 9459290</p>
</blockquote></td>
<td><blockquote>
<p>FHMMNPRT value = 14742749</p>
</blockquote></td>
<td><blockquote>
<p>FHMMNREP value = 8554301</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHMNADM value = 3747789</p>
</blockquote></td>
<td><blockquote>
<p>FHMNBRPT value = 2664485</p>
</blockquote></td>
<td><blockquote>
<p>FHMNINQ value = 3048115</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHMNPRT value = 8184781</p>
</blockquote></td>
<td><blockquote>
<p>FHMNREP value = 5978199</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK value = 7722074</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHMTK1 value = 9099540</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK11 value = 11735592</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK1A value = 5920546</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHMTK1B value = 10574665</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK1C value = 8620526</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK2 value = 4933044</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHMTK21 value = 5836943</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK3 value = 7184609</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK4 value = 7635361</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHMTK5 value = 8493131</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK6 value = 7247131</p>
</blockquote></td>
<td><blockquote>
<p>FHMTK7 value = 5201484</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHMTK8 value = 9101726</p>
</blockquote></td>
<td><blockquote>
<p>FHMTKO value = 8487911</p>
</blockquote></td>
<td><blockquote>
<p>FHNO1 value = 2554062</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHNO2 value = 12273770</p>
</blockquote></td>
<td><blockquote>
<p>FHNO21 value = 6959419</p>
</blockquote></td>
<td><blockquote>
<p>FHNO3 value = 3504490</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHNO31 value = 8155360</p>
</blockquote></td>
<td><blockquote>
<p>FHNO4 value = 1121656</p>
</blockquote></td>
<td><blockquote>
<p>FHNO41 value = 9787088</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHNO5 value = 5504124</p>
</blockquote></td>
<td><blockquote>
<p>FHNO6 value = 9951272</p>
</blockquote></td>
<td><blockquote>
<p>FHNO7 value = 2420941</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHNO8 value = 2809367</p>
</blockquote></td>
<td><blockquote>
<p>FHNU value = 1616737</p>
</blockquote></td>
<td><blockquote>
<p>FHNU1 value = 4573798</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHNU10 value = 5868490</p>
</blockquote></td>
<td><blockquote>
<p>FHNU11 value = 10048442</p>
</blockquote></td>
<td><blockquote>
<p>FHNU12 value = 5473461</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHNU2 value = 12336623</p>
</blockquote></td>
<td><blockquote>
<p>FHNU3 value = 6836253</p>
</blockquote></td>
<td><blockquote>
<p>FHNU4 value = 11724524</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHNU5 value = 10455147</p>
</blockquote></td>
<td><blockquote>
<p>FHNU6 value = 4729663</p>
</blockquote></td>
<td><blockquote>
<p>FHNU7 value = 5806572</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHNU8 value = 7921572</p>
</blockquote></td>
<td><blockquote>
<p>FHNU9 value = 4484537</p>
</blockquote></td>
<td><blockquote>
<p>FHNUT value = 4384530</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHOMAPI value = 763322</p>
</blockquote></td>
<td><blockquote>
<p>FHOMDMP value = 6770629</p>
</blockquote></td>
<td><blockquote>
<p>FHOMDPA value = 2651021</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHOMELT value = 2016540</p>
</blockquote></td>
<td><blockquote>
<p>FHOMGP1 value = 2813402</p>
</blockquote></td>
<td><blockquote>
<p>FHOMGR1 value = 3118003</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHOMIP value = 1356283</p>
</blockquote></td>
<td><blockquote>
<p>FHOMPP value = 7069249</p>
</blockquote></td>
<td><blockquote>
<p>FHOMPP1 value = 13298929</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 32%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FHOMRA1 value = 4387944</p>
</blockquote></th>
<th><blockquote>
<p>FHOMRBL1 value = 7136445</p>
</blockquote></th>
<th><blockquote>
<p>FHOMRBLD value = 8338364</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FHOMRC1 value = 4337575</p>
</blockquote></td>
<td><blockquote>
<p>FHOMRE1 value = 7697070</p>
</blockquote></td>
<td><blockquote>
<p>FHOMRMD value = 6282416</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHOMRO1 value = 14538804</p>
</blockquote></td>
<td><blockquote>
<p>FHOMRO2 value = 7575095</p>
</blockquote></td>
<td><blockquote>
<p>FHOMRO3 value = 2692288</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHOMRP1 value = 3934060</p>
</blockquote></td>
<td><blockquote>
<p>FHOMRR1 value = 6837334</p>
</blockquote></td>
<td><blockquote>
<p>FHOMRT1 value = 7938638</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHOMSA1 value = 2801044</p>
</blockquote></td>
<td><blockquote>
<p>FHOMSC1 value = 1027946</p>
</blockquote></td>
<td><blockquote>
<p>FHOMSP1 value = 4349806</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHOMSR1 value = 5776286</p>
</blockquote></td>
<td><blockquote>
<p>FHOMSS1 value = 3045610</p>
</blockquote></td>
<td><blockquote>
<p>FHOMTK1 value = 2915375</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHOMTK2 value = 11158197</p>
</blockquote></td>
<td><blockquote>
<p>FHOMUPD value = 463486</p>
</blockquote></td>
<td><blockquote>
<p>FHOMUTL value = 7088027</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHOMWOR value = 6693069</p>
</blockquote></td>
<td><blockquote>
<p>FHORC value = 4195898</p>
</blockquote></td>
<td><blockquote>
<p>FHORC1 value = 3494894</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORC2 value = 10525523</p>
</blockquote></td>
<td><blockquote>
<p>FHORC3 value = 7628724</p>
</blockquote></td>
<td><blockquote>
<p>FHORC4 value = 2889882</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORC5 value = 2011042</p>
</blockquote></td>
<td><blockquote>
<p>FHORD value = 3323649</p>
</blockquote></td>
<td><blockquote>
<p>FHORD1 value = 14039767</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORD10 value = 7252211</p>
</blockquote></td>
<td><blockquote>
<p>FHORD11 value = 10488552</p>
</blockquote></td>
<td><blockquote>
<p>FHORD13 value = 14504593</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORD1A value = 3682245</p>
</blockquote></td>
<td><blockquote>
<p>FHORD2 value = 6282474</p>
</blockquote></td>
<td><blockquote>
<p>FHORD3 value = 6791855</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORD4 value = 5234594</p>
</blockquote></td>
<td><blockquote>
<p>FHORD41 value = 5341907</p>
</blockquote></td>
<td><blockquote>
<p>FHORD5 value = 5803325</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORD6 value = 11581819</p>
</blockquote></td>
<td><blockquote>
<p>FHORD61 value = 9209461</p>
</blockquote></td>
<td><blockquote>
<p>FHORD7 value = 7938063</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORD71 value = 11410659</p>
</blockquote></td>
<td><blockquote>
<p>FHORD72 value = 6657144</p>
</blockquote></td>
<td><blockquote>
<p>FHORD8 value = 6666396</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORD81 value = 10578182</p>
</blockquote></td>
<td><blockquote>
<p>FHORD82 value = 8501055</p>
</blockquote></td>
<td><blockquote>
<p>FHORD83 value = 3783884</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORD9 value = 12903264</p>
</blockquote></td>
<td><blockquote>
<p>FHORD91 value = 4010823</p>
</blockquote></td>
<td><blockquote>
<p>FHORD92 value = 7776268</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORD93 value = 10944337</p>
</blockquote></td>
<td><blockquote>
<p>FHORDR value = 3164483</p>
</blockquote></td>
<td><blockquote>
<p>FHORE1 value = 11283169</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORE1A value = 1924514</p>
</blockquote></td>
<td><blockquote>
<p>FHORE2 value = 5663292</p>
</blockquote></td>
<td><blockquote>
<p>FHORE21 value = 12395288</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORE3 value = 4225419</p>
</blockquote></td>
<td><blockquote>
<p>FHORO value = 4177668</p>
</blockquote></td>
<td><blockquote>
<p>FHORR value = 3622408</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORT1 value = 10824538</p>
</blockquote></td>
<td><blockquote>
<p>FHORT10 value = 15414510</p>
</blockquote></td>
<td><blockquote>
<p>FHORT11 value = 2516946</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORT2 value = 7152566</p>
</blockquote></td>
<td><blockquote>
<p>FHORT3 value = 3727556</p>
</blockquote></td>
<td><blockquote>
<p>FHORT5 value = 5364727</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORT5A value = 10419764</p>
</blockquote></td>
<td><blockquote>
<p>FHORT5B value = 2194934</p>
</blockquote></td>
<td><blockquote>
<p>FHORT5C value = 3326328</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORT5D value = 6780132</p>
</blockquote></td>
<td><blockquote>
<p>FHORTR value = 2509889</p>
</blockquote></td>
<td><blockquote>
<p>FHORX value = 1435752</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHORX1 value = 11587212</p>
</blockquote></td>
<td><blockquote>
<p>FHORX1A value = 11347667</p>
</blockquote></td>
<td><blockquote>
<p>FHORX1B value = 4383118</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHORX1C value = 8113410</p>
</blockquote></td>
<td><blockquote>
<p>FHORX2 value = 3148937</p>
</blockquote></td>
<td><blockquote>
<p>FHORX3 value = 8920219</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHPATM value = 7828345</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC value = 5655183</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC1 value = 5569532</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHPRC10 value = 12085984</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC11 value = 14258256</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC12 value = 7939270</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHPRC13 value = 12022196</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC14 value = 9606339</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC2 value = 5062603</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHPRC3 value = 4336625</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC4 value = 2168815</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC5 value = 1913669</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHPRC6 value = 4509284</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC7 value = 3360749</p>
</blockquote></td>
<td><blockquote>
<p>FHPRC8 value = 9089015</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHPRC9 value = 7552440</p>
</blockquote></td>
<td><blockquote>
<p>FHPRF value = 1601618</p>
</blockquote></td>
<td><blockquote>
<p>FHPRF1 value = 14232699</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHPRF1A value = 4281323</p>
</blockquote></td>
<td><blockquote>
<p>FHPRF2 value = 2930578</p>
</blockquote></td>
<td><blockquote>
<p>FHPRF4 value = 1651329</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHPRI value = 3953742</p>
</blockquote></td>
<td><blockquote>
<p>FHPRI1 value = 4796204</p>
</blockquote></td>
<td><blockquote>
<p>FHPRI2 value = 8125121</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHPRI3 value = 1952818</p>
</blockquote></td>
<td><blockquote>
<p>FHPRO value = 6105945</p>
</blockquote></td>
<td><blockquote>
<p>FHPRO1 value = 10888674</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHPRO2 value = 14342192</p>
</blockquote></td>
<td><blockquote>
<p>FHPRO3 value = 2512818</p>
</blockquote></td>
<td><blockquote>
<p>FHPRO4 value = 5871635</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHPRO4A value = 3732530</p>
</blockquote></td>
<td><blockquote>
<p>FHPRO5 value = 4997921</p>
</blockquote></td>
<td><blockquote>
<p>FHPRO6 value = 3001322</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHPRO7 value = 1861736</p>
</blockquote></td>
<td><blockquote>
<p>FHPRR1 value = 4227166</p>
</blockquote></td>
<td><blockquote>
<p>FHPRR2 value = 6709251</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHPRW value = 11342645</p>
</blockquote></td>
<td><blockquote>
<p>FHPRW1 value = 4137314</p>
</blockquote></td>
<td><blockquote>
<p>FHPRW2 value = 3704446</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHPRW3 value = 4037054</p>
</blockquote></td>
<td><blockquote>
<p>FHPRW4 value = 1975449</p>
</blockquote></td>
<td><blockquote>
<p>FHREC value = 3913108</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHREC1 value = 4357665</p>
</blockquote></td>
<td><blockquote>
<p>FHREC2 value = 5088857</p>
</blockquote></td>
<td><blockquote>
<p>FHREC3 value = 1924284</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHREC4 value = 3456680</p>
</blockquote></td>
<td><blockquote>
<p>FHREC5 value = 2832308</p>
</blockquote></td>
<td><blockquote>
<p>FHREC6 value = 8846440</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHREC7 value = 1770111</p>
</blockquote></td>
<td><blockquote>
<p>FHREP value = 4497192</p>
</blockquote></td>
<td><blockquote>
<p>FHREP1 value = 11157584</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHSEL1 value = 9136926</p>
</blockquote></td>
<td><blockquote>
<p>FHSEL2 value = 11181038</p>
</blockquote></td>
<td><blockquote>
<p>FHSEL3 value = 6642148</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHSEL4 value = 6631600</p>
</blockquote></td>
<td><blockquote>
<p>FHSP value = 962380</p>
</blockquote></td>
<td><blockquote>
<p>FHSP1 value = 13812346</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHSP11 value = 4199493</p>
</blockquote></td>
<td><blockquote>
<p>FHSPED value = 12339211</p>
</blockquote></td>
<td><blockquote>
<p>FHSPTAB value = 6582374</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHSYSF value = 798296</p>
</blockquote></td>
<td><blockquote>
<p>FHSYSK value = 4219367</p>
</blockquote></td>
<td><blockquote>
<p>FHSYSP value = 1568629</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHVER value = 1524619</p>
</blockquote></td>
<td><blockquote>
<p>FHWADM value = 6861969</p>
</blockquote></td>
<td><blockquote>
<p>FHWDIS value = 8981841</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHWDISD value = 3391790</p>
</blockquote></td>
<td><blockquote>
<p>FHWGMR value = 799404</p>
</blockquote></td>
<td><blockquote>
<p>FHWHEA value = 13316807</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHWMAS value = 1687237</p>
</blockquote></td>
<td><blockquote>
<p>FHWOR value = 12475464</p>
</blockquote></td>
<td><blockquote>
<p>FHWOR1 value = 2211384</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHWOR2 value = 8091869</p>
</blockquote></td>
<td><blockquote>
<p>FHWOR3 value = 10816921</p>
</blockquote></td>
<td><blockquote>
<p>FHWOR31 value = 2183633</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHWOR4 value = 5632033</p>
</blockquote></td>
<td><blockquote>
<p>FHWOR5 value = 9021388</p>
</blockquote></td>
<td><blockquote>
<p>FHWOR51 value = 5532779</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHWOR5R value = 3603229</p>
</blockquote></td>
<td><blockquote>
<p>FHWOR6 value = 6435773</p>
</blockquote></td>
<td><blockquote>
<p>FHWOR61 value = 5319302</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 32%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FHWOR7 value = 3464456</p>
</blockquote></th>
<th><blockquote>
<p>FHWOR71 value = 15904813</p>
</blockquote></th>
<th><blockquote>
<p>FHWOR72 value = 11802862</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FHWOR8 value = 3058515</p>
</blockquote></td>
<td><blockquote>
<p>FHWORA value = 7483815</p>
</blockquote></td>
<td><blockquote>
<p>FHWORA1 value = 11738990</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHWORI value = 3970884</p>
</blockquote></td>
<td><blockquote>
<p>FHWORP value = 4423837</p>
</blockquote></td>
<td><blockquote>
<p>FHWORR value = 4709359</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHWTRN value = 2729798</p>
</blockquote></td>
<td><blockquote>
<p>FHXCNV value = 3514475</p>
</blockquote></td>
<td><blockquote>
<p>FHXDB value = 12710968</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHXDB1 value = 14538448</p>
</blockquote></td>
<td><blockquote>
<p>FHXDB2 value = 9231699</p>
</blockquote></td>
<td><blockquote>
<p>FHXIN value = 2788331</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHXMOV value = 8770539</p>
</blockquote></td>
<td><blockquote>
<p>FHXOR value = 3928601</p>
</blockquote></td>
<td><blockquote>
<p>FHXOR3 value = 8083732</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHXUTL value = 5306970</p>
</blockquote></td>
<td><blockquote>
<p>FHXWRD value = 3823200</p>
</blockquote></td>
<td><blockquote>
<p>FHZDOC value = 972122</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHZDOC1 value = 704051</p>
</blockquote></td>
<td><blockquote>
<p>FHZDOC2 value = 9217684</p>
</blockquote></td>
<td><blockquote>
<p>FHZDOC3 value = 1019133</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a listing of the files exported with Nutrition and Food Service Outpatient Meals V. 5.5

## Modified Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File Number</p>
</blockquote></th>
<th><blockquote>
<p>File Name</p>
</blockquote></th>
<th><blockquote>
<p>Global</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>115</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION PERSON</p>
</blockquote></td>
<td><blockquote>
<p>^FHPT(</p>
</blockquote></td>
<td><blockquote>
<p>This file contains all dietetic orders for each admission of a patient. It includes diet orders, consult requests, supplemental feedings, early/late tray requests, and tube feedings. It also contains any food allergies entered for the patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>119.8</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION EVENTS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.8</p>
</blockquote></td>
<td><blockquote>
<p>This file contains entries for all patient movements, diet changes, and tube feeding orders, additional orders, food preferences, standing orders, and patient isolation orders requiring action by the Dietetic Service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>119.6</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.6</p>
</blockquote></td>
<td><blockquote>
<p>This file is a list of wards in the hospital and associated room-beds and contains various dietetic specific information, such as the assigned clinician, bulk nourishments for the ward, and which Service Point, Communication Office, and Supplemental Feeding Site is assigned responsibility for the ward.</p>
<p>This file is also used to store outpatient locations necessary for the outpatient meals enhancement.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>119.9</p>
</blockquote></td>
<td><blockquote>
<p>FH SITE PARAMETERS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.9</p>
</blockquote></td>
<td><blockquote>
<p>This file contains an extensive set of site parameters designed to indicate characteristics of the Nutrition and Food Service and/or different methods that the Service wishes the program to perform.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Existing Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File Number</p>
</blockquote></th>
<th><blockquote>
<p>File Name</p>
</blockquote></th>
<th><blockquote>
<p>Global</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>111</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(111</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a list of all of the diet modifications allowed by the using facility. Associated with each diet are characteristics, such as alternate names, an abbreviated name, whether a clinician is to be bulletined when ordered, and a diet precedence that is used to prevent diet conflicts and as a printing sequence order.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>111.1</p>
</blockquote></td>
<td><blockquote>
<p>DIET PATTERNS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(111.1</p>
</blockquote></td>
<td><blockquote>
<p>This file contains diet patterns. The entries for a specific pattern represent changes from the production diet for this particular pattern.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>112</p>
</blockquote></td>
<td><blockquote>
<p>FOOD NUTRIENTS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(112</p>
</blockquote></td>
<td><blockquote>
<p>This file contains both standard USDA nutrient data based upon Handbook 456 and Revised Handbook 8, as well as user entered data. The standard data includes 32 common nutrients.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>112.2</p>
</blockquote></td>
<td><blockquote>
<p>DRI VALUES</p>
</blockquote></td>
<td><blockquote>
<p>^FH(112.2</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the values of the Dietary Reference Intakes (DRI). In 1997, the Food and Nutrition Board began releasing updated recommendations for nutrient intake levels that apply to healthy individuals under a new framework called Dietary Reference Intakes. For nutrients that have not yet been revised as DRI (protein, for example), the 1989 RDA values are the most current recommendations and are used here.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>112.6</p>
</blockquote></td>
<td><blockquote>
<p>USERMENU</p>
</blockquote></td>
<td><blockquote>
<p>^FHUM(112.6</p>
</blockquote></td>
<td><blockquote>
<p>This file contains menus of food items, classified by day and meal, that are saved for nutrient analysis.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>113</p>
</blockquote></td>
<td><blockquote>
<p>INGREDIENT</p>
</blockquote></td>
<td><blockquote>
<p>^FHING(113</p>
</blockquote></td>
<td><blockquote>
<p>This file is the master list of ingredients used in preparing recipes. It contains purchasing information, such as stock number and vendor, issuance data such as the issuing unit, and various conversion factors. Nutritive data, such as food group, poundage factors, and a pointer to the analogous food nutrient item in File 112 are also included.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>113.1</p>
</blockquote></td>
<td><blockquote>
<p>STORAGE LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>^FH(113.1</p>
</blockquote></td>
<td><blockquote>
<p>This is the file of storage locations where ingredients are stored by the dietetic service. It is primarily used to sort various ingredient pull lists</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File Number</p>
</blockquote></th>
<th><blockquote>
<p>File Name</p>
</blockquote></th>
<th><blockquote>
<p>Global</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>113.2</p>
</blockquote></td>
<td><blockquote>
<p>FH VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>^FH(113.2</p>
</blockquote></td>
<td><blockquote>
<p>This file contains basic data on the various vendors supplying ingredients to the Dietetic Service. It contains address, telephone numbers and name of contacts.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>114</p>
</blockquote></td>
<td><blockquote>
<p>RECIPE</p>
</blockquote></td>
<td><blockquote>
<p>^FH(114</p>
</blockquote></td>
<td><blockquote>
<p>This file contains all recipes necessary to build meals. Each recipe consists of basic data concerning the recipe, various ingredients, and may also contain 'embedded' recipes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>114.1</p>
</blockquote></td>
<td><blockquote>
<p>RECIPE CATEGORY</p>
</blockquote></td>
<td><blockquote>
<p>^FH(114.1</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a basic list of categorizations which may be applied to recipes. It is primarily used to sort and/or determine the order in which lists of recipes will print.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>114.2</p>
</blockquote></td>
<td><blockquote>
<p>PREPARATION AREA</p>
</blockquote></td>
<td><blockquote>
<p>^FH(114.2</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a list of areas in which food is prepared. Recipes may be classified by preparation area and this file is used to sort recipes into the various preparation areas as well as determine the order in which various lists will print.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>114.3</p>
</blockquote></td>
<td><blockquote>
<p>SERVING UTENSIL</p>
</blockquote></td>
<td><blockquote>
<p>^FH(114.3</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a list of basic serving utensils. Recipes use this file to indicate the most appropriate serving utensil. The utensil name is printed on various reports for use by serving personnel</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>114.4</p>
</blockquote></td>
<td><blockquote>
<p>EQUIPMENTT</p>
</blockquote></td>
<td><blockquote>
<p>^FH(114.4</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a list of basic equipment used in the preparation of recipes. A recipe may point to this list to indicate the primary type of equipment used in the recipe preparation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>115.2</p>
</blockquote></td>
<td><blockquote>
<p>FOOD PREFERENCES</p>
</blockquote></td>
<td><blockquote>
<p>^FH(115.2</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the items which can be selected as patient preference items. It contains both items which can be selected, such as coffee or tea, as well as food preferences (such as no liver) which will result in certain recipes being excluded for the patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>115.3</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION CLASSIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>^FH(115.3</p>
</blockquote></td>
<td><blockquote>
<p>This file contains site-specific nutrition classifications used in nutrition assessment and screening.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>115.4</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION STATUS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(115.4</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the four nutrition statuses of the established guidelines that are used in nutrition assessment and screening.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>115.5</p>
</blockquote></td>
<td><blockquote>
<p>DIETETIC NUTRITION PLAN</p>
</blockquote></td>
<td><blockquote>
<p>^FH(115.5</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a list of nutrition plan actions which are listed on the Nutrition Screening form.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File Number</p>
</blockquote></th>
<th><blockquote>
<p>File Name</p>
</blockquote></th>
<th><blockquote>
<p>Global</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>115.6</p>
</blockquote></td>
<td><blockquote>
<p>ENCOUNTER TYPES</p>
</blockquote></td>
<td><blockquote>
<p>^FH(115.6</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a list of types of dietetic encounters, or events, which are used to account for many of the professional activities of dietetic personnel.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>115.7</p>
</blockquote></td>
<td><blockquote>
<p>DIETETIC ENCOUNTERS</p>
</blockquote></td>
<td><blockquote>
<p>^FHEN(</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the various dietetic encounters entered by dietetics personnel. It includes patient-related events, such as diet instructions, as well as non-patient-related events such as talks to the community.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>116</p>
</blockquote></td>
<td><blockquote>
<p>MENU CYCLE</p>
</blockquote></td>
<td><blockquote>
<p>^FH(116</p>
</blockquote></td>
<td><blockquote>
<p>A menu cycle consists of some specified number of days each day of which is associated with a breakfast, noon, and evening meal. An effective date determines the start of the cycle and it will repeat until the effective date of another menu cycle begins.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>116.1</p>
</blockquote></td>
<td><blockquote>
<p>MEAL</p>
</blockquote></td>
<td><blockquote>
<p>^FH(116.1</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the various meals served by the institution. A meal consists of all recipes prepared for a breakfast, noon, or evening meal as well as the production diets associated with each recipe. In turn, the production diet entry may indicate the percentage of that recipe that is to be served in a cafeteria or by tray.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>116.2</p>
</blockquote></td>
<td><blockquote>
<p>PRODUCTION DIETT</p>
</blockquote></td>
<td><blockquote>
<p>^FH(116.2</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a list of the production diets which are the basic diets actually prepared and from which the wide variety of clinical diet modifications are derived.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>116.3</p>
</blockquote></td>
<td><blockquote>
<p>HOLIDAY MEALS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(116.3</p>
</blockquote></td>
<td><blockquote>
<p>This file consists of a list of holiday dates for which special meals are prepared. It consists of the holiday date, name, and allows for entry of a breakfast, noon, and/or evening meal which, if present, will override the normal menu cycle meals on that date.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>117</p>
</blockquote></td>
<td><blockquote>
<p>MEALS SERVED</p>
</blockquote></td>
<td><blockquote>
<p>^FH(117</p>
</blockquote></td>
<td><blockquote>
<p>This file consists of a list of holiday dates for which special meals are prepared. It consists of the holiday date, name, and allows for entry of a breakfast, noon, and/or evening meal which, if present, will override the normal menu cycle meals on that date.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>117.1</p>
</blockquote></td>
<td><blockquote>
<p>STAFFING DATA</p>
</blockquote></td>
<td><blockquote>
<p>^FH(117.1</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the statistical data necessary to prepare the Staffing Data report. Data is saved for each date.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>117.2</p>
</blockquote></td>
<td><blockquote>
<p>DIETETIC COST OF MEALS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(117.2</p>
</blockquote></td>
<td><blockquote>
<p>This file is used to store the monthly costs of the various food groups. Data is used to</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File Number</p>
</blockquote></th>
<th><blockquote>
<p>File Name</p>
</blockquote></th>
<th><blockquote>
<p>Global</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>calculate the cost of meals served as well as ensure an adequate distribution of food across the food groups.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>117.3</p>
</blockquote></td>
<td><blockquote>
<p>ANNUAL REPORT</p>
</blockquote></td>
<td><blockquote>
<p>^FH(117.3</p>
</blockquote></td>
<td><blockquote>
<p>The Annual Dietetic Report is designed to facilitate data gathering and to eliminate information that has been discontinued or deemed irrelevant. The report is compiled manually and submitted to Central office Dietetics through regular mail.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>117.4</p>
</blockquote></td>
<td><blockquote>
<p>DIETETIC REPORT CATEGORIES</p>
</blockquote></td>
<td><blockquote>
<p>^FH(117.4</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the categories, Specialized Medical Programs, Primary Delivery System, Primary Production System, and the Dietetic Service Equipment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>118</p>
</blockquote></td>
<td><blockquote>
<p>SUPPLEMENTAL FEEDINGS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(118</p>
</blockquote></td>
<td><blockquote>
<p>This file contains all items served as supplemental feedings. When appropriate, it may include combinations such as ice cream with spoon. Items designed for bulk delivery to the wards are also contained in this file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>118.1</p>
</blockquote></td>
<td><blockquote>
<p>SUPPLEMENTAL FEEDING MENU</p>
</blockquote></td>
<td><blockquote>
<p>^FH(118.1</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a pattern of supplemental feedings (up to four items for each of three time periods) which are often requested in common situations (e.g., a diabetic patient) and avoids the necessity of individually selecting the various items when ordering supplemental feedings.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>118.2</p>
</blockquote></td>
<td><blockquote>
<p>TUBEFEEDING</p>
</blockquote></td>
<td><blockquote>
<p>^FH(118.2</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the products commonly used for tube-feedings as well as their characteristics such as Kcals/cc, cost, and synonyms.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>118.3</p>
</blockquote></td>
<td><blockquote>
<p>STANDING ORDERS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(118.3</p>
</blockquote></td>
<td><blockquote>
<p>This is a list of the common standing orders (often called add-ons or specials) which may be ordered for a patient. It may include such things as 'double portions' or preferences such as 'no fish.'</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>119</p>
</blockquote></td>
<td><blockquote>
<p>DIETITIAN TICKLER FILE</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119</p>
</blockquote></td>
<td><blockquote>
<p>This file contains entries relating to required reviews for each dietitian response for a ward or group of wards. It can also be used to record personal or non-patient related entries.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>119.1</p>
</blockquote></td>
<td><blockquote>
<p>UNITS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.1</p>
</blockquote></td>
<td><blockquote>
<p>This file consists of a list of units used by the ingredient file to indicate the dietetic issue unit.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>119.4</p>
</blockquote></td>
<td><blockquote>
<p>ISOLATION/PRECAUTION TYPE</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.4</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the list of isolation/precaution types, as commonly identified by medical personnel, and</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 15%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>File Number</p>
</blockquote></th>
<th><blockquote>
<p>File Name</p>
</blockquote></th>
<th><blockquote>
<p>Global</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>indicates the characteristics of those types important to the Dietetic Service such as type of china and appropriate tray delivery person.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>119.5</p>
</blockquote></td>
<td><blockquote>
<p>DIETETIC CONSULTS</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.5</p>
</blockquote></td>
<td><blockquote>
<p>This file contains the list of types of dietetic consultations performed as well as 'time- units' necessary to complete such consultations for workload purposes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>119.71</p>
</blockquote></td>
<td><blockquote>
<p>PRODUCTION FACILITY</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.71</p>
</blockquote></td>
<td><blockquote>
<p>This file is a list of Production Facilities and associated parameters. A Production Facility is generally a main kitchen where bulk food is prepared for use by Service Points.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>119.72</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE POINT</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.72</p>
</blockquote></td>
<td><blockquote>
<p>This file is a list of Service Points and associated parameters. A Service Point is a tray assembly line or cafeteria where bulk food from a Production Facility is served</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>119.73</p>
</blockquote></td>
<td><blockquote>
<p>COMMUNICATION OFFICE</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.73</p>
</blockquote></td>
<td><blockquote>
<p>This file is a list of Communication Offices and associated parameters. A Communication Office has responsibility for processing diet orders for a group of wards.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>119.74</p>
</blockquote></td>
<td><blockquote>
<p>SUPPLEMENTAL FEEDING SITE</p>
</blockquote></td>
<td><blockquote>
<p>^FH(119.74</p>
</blockquote></td>
<td><blockquote>
<p>This file contains a list of Supplemental Feeding Sites and associated parameters. A Supplemental Feeding Site prepares orders for a group of wards for which it is responsible</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Pointer Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> File/Package: DIETETICS Date: AUG 16,2004

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 22%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>FILE (#)</p>
</blockquote></th>
<th><blockquote>
<p>POINTER</p>
</blockquote></th>
<th><blockquote>
<p>(#) FILE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>POINTER FIELD</p>
</blockquote></td>
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td><blockquote>
<p>POINTER FIELD FILE POINTED TO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> L=Laygo S=File not in set N=Normal Ref. C=Xref.

> \*=Truncated m=Multiple v=Variable Pointer

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 2%" />
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>DIET PATTERNS (#111.1)</p>
<p>DIET1 (N</p>
</blockquote></th>
<th><blockquote>
<p>)-&gt;</p>
</blockquote></th>
<th><p>|</p>
<p>|</p></th>
<th colspan="2"><blockquote>
<p>111 DIETS</p>
</blockquote></th>
<th></th>
<th colspan="2"><blockquote>
<p>|</p>
<p>|</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>DIET2 (N</p>
<p>DIET3 (N</p>
<p>DIET4 (N</p>
<p>DIET5 (N</p>
<p>NUTRITION PERSON (#115.016) RECURRING MEALS:DIET . (N RECURRING MEALS:DIET1 (N RECURRING MEALS:DIET2 (N RECURRING MEALS:DIET3 (N RECURRING MEALS:DIET4 (N RECURRING MEALS:DIET5 (N SPECIAL MEALS:DIET (N</p>
<p>GUEST MEALS:DIET (N</p>
<p>ADMISSION:DIET:DIET1 . (N ADMISSION:DIET:DIET2 . (N ADMISSION:DIET:DIET3 . (N ADMISSION:DIET:DIET4 . (N ADMISSION:DIET:DIET5 . (N</p>
<p>NUTRITION LOCATION (#119.6) DEFAULT ADMISSION DIET (N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>PRODUCTION</p>
</blockquote></td>
<td><blockquote>
<p>DIET</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt; PRODUCTION DIET</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>FH SITE PARAMETERS</p>
<p>OUTPATIENT MEALS</p></td>
<td><blockquote>
<p>(#119.9)</p>
<p>DIET1 (N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="3"></td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OUTPATIENT MEALS OUTPATIENT MEALS OUTPATIENT MEALS OUTPATIENT MEALS</p>
</blockquote></td>
<td><blockquote>
<p>DIET2 (N</p>
<p>DIET3 (N</p>
<p>DIET4 (N</p>
<p>DIET5 (N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="3"></td>
<td><blockquote>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="3"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>111.1 DIET PATT*</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DIET1</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DIET2</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DIET3</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DIET4</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DIET5</p>
<p>PRODUCTION DIET</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
<p>PRODUCTION DIET</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>m</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ASSOCIATED SF * ASSOCI:ASSOCI*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>SUPPLEMENTAL FE* STANDING ORDERS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td><blockquote>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
</blockquote></td>
<td><blockquote>
<p>m m m m m m</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>BREAKF:BREAKF* NOON M:NOON M* EVENIN:EVENIN* DIET R:DIET R* ASSOCI:ASSOCI* ASSOCI:ASSOCI*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>RECIPE CATEGORY RECIPE CATEGORY RECIPE CATEGORY FOOD PREFERENCES STANDING ORDERS STANDING ORDERS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>USER MENU (#112.63)</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DAY N:MEAL NU:FOOD IT* INGREDIENT (#113)</p>
<p>NUTRIENT DATA REFERENCE</p>
</blockquote></th>
<th><blockquote>
<p>(N</p>
<p>(N</p>
</blockquote></th>
<th><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></th>
<th><p>|</p>
<p>|</p>
<p>|</p></th>
<th><blockquote>
<p>112</p>
</blockquote></th>
<th><blockquote>
<p>FOOD</p>
</blockquote></th>
<th><blockquote>
<p>NUTRIE*</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>|</p>
<p>|</p>
<p>|</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>RECIPE (#114)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ASSOCIATED NUTRIENT AN* INGREDIEN:ASSOCIATED *</p>
</blockquote></td>
<td><blockquote>
<p>(N</p>
<p>(N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="4"><p>|</p>
<p>|</p></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="4"><blockquote>
<p>112.6 USER MENU | USER |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="4"><blockquote>
<p>DAY :MEAL:MEAL* |-&gt; DAY :MEAL:PROD* |-&gt;</p>
<p>m DA:ME:FO:FO* |-&gt; m DA:ME:RE:RE* |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>MEAL</p>
<p>PRODUCTION DIET FOOD NUTRIENTS RECIPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RECIPE (#114.01) INGREDIENT ...........</p>
</blockquote></td>
<td><blockquote>
<p>(N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="4"><p>|</p>
<blockquote>
<p>113 INGREDIENT | VENDOR |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>FH VENDOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="4"><blockquote>
<p>DIETETIC UNIT * |-&gt; STORAGE LOCATI* |-&gt; NUTRIENT DATA * |-&gt; MASTER ITEM # |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>UNITS</p>
<p>STORAGE LOCATION FOOD NUTRIENTS ITEM MASTER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INGREDIENT (#113) STORAGE LOCATION .....</p>
</blockquote></td>
<td><blockquote>
<p>(N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="4"><p>|</p>
<blockquote>
<p>113.1 STORAGE L* |</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INGREDIENT (#113)</p>
<p>VENDOR ...............</p>
</blockquote></td>
<td><blockquote>
<p>(N</p>
</blockquote></td>
<td><blockquote>
<p>L)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="4"><p>|</p>
<blockquote>
<p>113.2 FH VENDOR |</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>USER MENU (#112.64)</p>
<p>DAY N:MEAL NU:RECIPE* RECIPE (#114.03)</p>
<p>EMBEDDED RECIPE ......</p>
<p>FOOD PREFERENCES (#115.2) RECIPE ...............</p>
</blockquote></td>
<td><blockquote>
<p>(N</p>
<p>(N</p>
<p>(N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="4"><p>|</p>
<blockquote>
<p>114 RECIPE |</p>
<p>| SERVING UTENSIL |-&gt;</p>
<p>| DEFAULT CATEGO* |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>SERVING UTENSIL RECIPE CATEGORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EXCLUDED RECIPES .....</p>
<p>MEAL (#116.11)</p>
<p>RECIPE ...............</p>
</blockquote></td>
<td><blockquote>
<p>(N</p>
<p>(N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="4"><blockquote>
<p>PREPARATION AR* |-&gt;</p>
<p>| ASSOCIATED NUT* |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>PREPARATION AREA</p>
<p>FOOD NUTRIENTS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>SUPPLEMENTAL FEEDING (#118) CORRESPONDING RECIPE . (N</p>
<p>TUBEFEEDING (#118.2)</p>
<p>CORRESPONDING RECIPE . (N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="3"><blockquote>
<p>m INGRED:INGRED* INGRED:ASSOCI*</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
<p>|-&gt;</p>
<p>|</p>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>INGREDIENT FOOD NUTRIENTS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="3"><blockquote>
<p>m DIABET:DIABET* m EMBEDD:EMBEDD* m EQUIPM:EQUIPM*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>RECIPE CATEGORY RECIPE EQUIPMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="3"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>DIET PATTERNS (#111.115) BREAKFAST MODIFICATIONS (N</p>
</blockquote></td>
<td><blockquote>
<p>C )-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="3"><blockquote>
<p>114.1 RECIPE CA*</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NOON MODIFICATIONS ... (N EVENING MODIFICATIONS (N</p>
<p>RECIPE (#114)</p>
<p>DEFAULT CATEGORY (N</p>
<p>DIABETIC EXCHANGE (N</p>
<p>MEAL (#116.11) RECIPE:CATEGORY (N</p>
<p>RECIPE:RECIPE CATEGORY (N</p>
</blockquote></td>
<td><blockquote>
<p>C )-&gt;</p>
<p>C )-&gt;</p>
<p>)-&gt;</p>
<p>C )-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="3"></td>
<td><blockquote>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="3"></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> RECIPE (#114) \| \| PREPARATION AREA ..... (N )-\> \| 114.2 PREPARATI\* \|

> RECIPE (#114) \| \| SERVING UTENSIL ...... (N )-\> \| 114.3 SERVING U\* \|

> RECIPE (#114.05) \| \| EQUIPMENT ............ (N L)-\> \| 114.4 EQUIPMENT \|

> DIETETIC EVENTS (#119.8) \| \|

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 5%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT ..............</p>
</blockquote></th>
<th><blockquote>
<p>(N</p>
</blockquote></th>
<th><blockquote>
<p>C</p>
</blockquote></th>
<th><blockquote>
<p>)-&gt;</p>
</blockquote></th>
<th>|</th>
<th>115 NUTRITION P*</th>
<th><blockquote>
<p>|</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4" rowspan="49"></td>
<td>|</td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td>ISOLATION/PREC*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ISOLATION/PRECA*</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td>IP OE/RR ORDER*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>ADMISS:ISOLAT*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ISOLATION/PRECA*</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>ADMISS:OE/RR *</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>ADMISS:LAST L*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION LOCAT*</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>ADMISS:DIETET*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION LOCAT*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>ADMISS:ROOM-B*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ROOM-BED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>NUTRIT:RISK C*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION STATUS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>NUTRIT:NUTRIT*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION CLASS*</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>NUTRIT:ENTERI*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>NUTRIT:STATUS*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION STATUS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>NUTRIT:ENTRY *</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>NUTRIT:REVIEW*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>NUTRIT:DIETET*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION LOCAT*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>RECURR:RECURR*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>RECURR:DIET*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>RECURR:OUTPAT*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION LOCAT*</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>RECURR:DIET1*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>RECURR:DIET2*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>RECURR:DIET3*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>RECURR:DIET4*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>RECURR:DIET5*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>RECURR:ADDITI*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>RECURR:ADDITI*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>RECURR:EARLY/*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>RECURR:EARLY/*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>RECURR:TUBEFE*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>SPECIA:LOCATI*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION LOCAT*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>SPECIA:DIET*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>SPECIA:REQUES*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>SPECIA:AUTHOR*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>SPECIA:EARLY/*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>SPECIA:SPECIA*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td><blockquote>
<p>GUEST :LOCATI*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NUTRITION LOCAT*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td><blockquote>
<p>GUEST :DIET*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td>ADMI:DIET:DIET*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td>ADMI:DIET:DIET*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td>ADMI:DIET:DIET*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td>ADMI:DIET:DIET*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td>ADMI:DIET:DIET*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td>ADMI:DIET:CLER*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td>ADMI:DIET:PROD*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>PRODUCTION DIET</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td>ADMI:DIET:OE/R*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td>ADMI:DIET:CURR*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>ORDER STATUS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td>ADMI:DIET:REVI*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td>|</td>
<td>ADMI:DIET:CANC*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>|</td>
<td>ADMI:DIET:PATT*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \| NUTR:LAB :LAB \* \|-\> LABORATORY TEST

> \| ADMI:CONS:CONS\* \|-\> DIETETIC CONSUL\*

> \| ADMI:CONS:CLIN\* \|-\> NEW PERSON

> \| ADMI:CONS:CLER\* \|-\> NEW PERSON

> \| ADMI:CONS:CLER\* \|-\> NEW PERSON

> \| ADMI:CONS:OE/R\* \|-\> ORDER

> \| ADMI:CONS:OE/R\* \|-\> ORDER

> \| ADMI:TUBE:ENTE\* \|-\> NEW PERSON

> \| ADMI:TUBE:CANC\* \|-\> NEW PERSON

> \| ADMI:TUBE:OE/R\* \|-\> ORDER

> \| ADMI:TUBE:REVI\* \|-\> NEW PERSON

> \| ADMI:EARL:CLER\* \|-\> NEW PERSON

> \| ADMI:EARL:OE/R\* \|-\> ORDER

> \| ADMI:ADDI:CLER\* \|-\> NEW PERSON

> \| ADMI:ADDI:CLER\* \|-\> NEW PERSON

> \| ADMI:ADDI:OE/R\* \|-\> ORDER

> \| ADMI:SUPP:ENTE\* \|-\> NEW PERSON

> \| ADMI:SUPP:SF M\* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:10AM\* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:10AM\* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:10AM\* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:10AM\* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:2PM \* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:2PM \* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:2PM \* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:2PM \* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:8PM \* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:8PM \* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:8PM \* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:8PM \* \|-\> SUPPLEMENTAL FE\*

> \| ADMI:SUPP:REVI\* \|-\> NEW PERSON

> \| ADMI:SUPP:CANC\* \|-\> NEW PERSON

> \| ADMI:STAN:ORDE\* \|-\> STANDING ORDERS

> \| ADMI:STAN:ENTE\* \|-\> NEW PERSON

> \| ADMI:STAN:CANC\* \|-\> NEW PERSON

> \| m FOOD P:FOOD P\* \|-\> FOOD PREFERENCES

> \| m AD:TU:TF:TF\* \|-\> TUBEFEEDING

> \| ADMI:Moni:CLEA\* \|-\> NEW PERSON

> \| m RECU:TUBE:TUBE\* \|-\> TUBEFEEDING

> DIET PATTERNS (#111.119) \| \| DIET RESTRICTION ..... (N C )-\> \| 115.2 FOOD PREF\* \| NUTRITION PERSON (#115.09) \| \|

FOOD PREFERENCES ..... (N )-\> \| RECIPE \|-\> RECIPE

\| m EXCLUD:EXCLUD\* \|-\> RECIPE

> NUTRITION PERSON (#115.011) \| \|

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 15%" />
<col style="width: 3%" />
<col style="width: 10%" />
<col style="width: 18%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th>NUTRITION:NUTRITION P* (N</th>
<th><blockquote>
<p>)-&gt;</p>
</blockquote></th>
<th>|</th>
<th>115.3</th>
<th>NUTRITION*</th>
<th>|</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUTRITION PERSON (#115.011) NUTRITION:RISK CATEGO* (N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td>115.4</td>
<td>NUTRITION*</td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>NUTRITION STATUS:STATUS (N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td></td>
<td>|</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DIETETIC ENCOUNTERS (#115.7) ENCOUNTER TYPE (N</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td>115.6</td>
<td>ENCOUNTER*</td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>|</td>
<td>115.7</td>
<td>DIETETIC *</td>
<td>|</td>
</tr>
</tbody>
</table>

> \| CLINICIAN \|-\> NEW PERSON

<table style="width:100%;">
<colgroup>
<col style="width: 33%" />
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 22%" />
<col style="width: 5%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3" rowspan="13"></th>
<th>|</th>
<th><blockquote>
<p>ENCOUNTER TYPE</p>
</blockquote></th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>ENCOUNTER TYPES</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>|</th>
<th><blockquote>
<p>EVENT LOCATION</p>
</blockquote></th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>HOSPITAL LOCATI*</p>
</blockquote></th>
</tr>
<tr class="header">
<th>|</th>
<th>COMMUNICATIONS*</th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>COMMUNICATION O*</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>|</th>
<th><blockquote>
<p>ENTERING CLERK</p>
</blockquote></th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>NEW PERSON</p>
</blockquote></th>
</tr>
<tr class="header">
<th>|</th>
<th><blockquote>
<p>REVIEW CLERK</p>
</blockquote></th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>NEW PERSON</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>|</th>
<th>m PATIENT:PATIENT</th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
</tr>
<tr class="header">
<th>|</th>
<th><blockquote>
<p>PATIEN:LOCATI*</p>
</blockquote></th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>HOSPITAL LOCATI*</p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th>|</th>
<th><blockquote>
<p>116 MENU CYCLE</p>
</blockquote></th>
<th><blockquote>
<p>|</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th>|</th>
<th><blockquote>
<p>DAY:BREAKF*</p>
</blockquote></th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>MEAL</p>
</blockquote></th>
</tr>
<tr class="header">
<th>|</th>
<th><blockquote>
<p>DAY:NOON MEAL</p>
</blockquote></th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>MEAL</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>|</th>
<th><blockquote>
<p>DAY:EVENIN*</p>
</blockquote></th>
<th><blockquote>
<p>|-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>MEAL</p>
</blockquote></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>USER MENU (#112.62)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DAY N:MEAL NU:MEAL* ..</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td><blockquote>
<p>116.1 MEAL</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MENU CYCLE (#116.01)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DAY:BREAKFAST MEAL ...</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td><blockquote>
<p>m RECIPE:RECIPE</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>RECIPE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAY:NOON MEAL ........</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td>RECIPE:CATEGORY</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>RECIPE CATEGORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DAY:EVENING MEAL .....</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td>m RECI:POPU:SERV*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE POINT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HOLIDAY MEALS (#116.3)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BREAKFAST MEAL .......</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td>m RECI:RECI:RECI*</td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>RECIPE CATEGORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NOON MEAL ............</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVENING MEAL .........</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DIETS (#111)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRODUCTION DIET ......</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td>116.2 PRODUCTIO*</td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DIET PATTERNS (#111.1)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRODUCTION DIET ......</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td><blockquote>
<p>m SINGUL:SINGUL*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>PRODUCTION DIET</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>USER MENU (#112.62)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAY N:MEAL NU:PRODUCT*</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>L)-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUTRITION PERSON (#115.02)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ADMIS:DIET:PRODUCT* ..</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRODUCTION DIET (#116.211)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SINGULAR PRODUCTION DI*</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>C )-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SERVICE POINT (#119.721)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ADDITIONA:ADD. MEALS *</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>C )-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRODUCTIO:FORECAST % *</p>
</blockquote></td>
<td>(N</td>
<td><blockquote>
<p>C )-&gt;</p>
</blockquote></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td>116.3 HOLIDAY M*</td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td><blockquote>
<p>BREAKFAST MEAL</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>MEAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td><blockquote>
<p>NOON MEAL</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>MEAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td><blockquote>
<p>EVENING MEAL</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>MEAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td>117 MEALS SERVED</td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td><blockquote>
<p>COMM O:COMM O*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>COMMUNICATION O*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td>117.1 STAFFING *</td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td><blockquote>
<p>COMM O:COMM O*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>COMMUNICATION O*</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td>117.3 ANNUAL RE*</td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td><blockquote>
<p>m SPECIA:SPECIA*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETETIC REPORT*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td><blockquote>
<p>m PRIMAR:PRIMAR*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETETIC REPORT*</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>|</td>
<td><blockquote>
<p>m DIETET:DIETET*</p>
</blockquote></td>
<td><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>DIETETIC REPORT*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ANNUAL REPORT (#117.312)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 22%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SPECIALIZED MEDICAL PR* PRIMARY DELIVERY SYSTEM DIETETIC EQUIPMENT ...</p>
</blockquote></th>
<th><p>(N</p>
<p>(N</p>
<p>(N</p></th>
<th><p>C )-&gt;</p>
<p>C )-&gt;</p>
<p>C )-&gt;</p></th>
<th><p>|</p>
<p>|</p>
<p>|</p></th>
<th>117.4 DIETETIC *</th>
<th><blockquote>
<p>|</p>
<p>|</p>
<p>|</p>
</blockquote></th>
<th colspan="2" rowspan="3"></th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NUTRITION PERSON (#115.07) ADMIS:SUPPLEM:10AM FE*</p>
</blockquote></th>
<th>(N</th>
<th>)-&gt;</th>
<th><p>|</p>
<p>|</p></th>
<th>118 SUPPLEMENTA*</th>
<th><blockquote>
<p>|</p>
<p>|</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ADMIS:SUPPLEM:10AM FE* ADMIS:SUPPLEM:10AM FE* ADMIS:SUPPLEM:10AM FE* ADMIS:SUPPLEM:2PM FEE* ADMIS:SUPPLEM:2PM FEE* ADMIS:SUPPLEM:2PM FEE* ADMIS:SUPPLEM:2PM FEE* ADMIS:SUPPLEM:8PM FEE* ADMIS:SUPPLEM:8PM FEE* ADMIS:SUPPLEM:8PM FEE*</p>
<p>ADMIS:SUPPLEM:8PM FEE*</p>
</blockquote></td>
<td><p>(N</p>
<p>(N</p>
<p>(N</p>
<p>(N</p>
<p>(N</p>
<p>(N</p>
<p>(N</p>
<p>(N</p>
<p>(N</p>
<p>(N</p>
<p>(N</p></td>
<td><p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td>CORRESPONDING *</td>
<td><blockquote>
<p>|-&gt;</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>RECIPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>SUPPLEMENTAL FEEDING (#118.1) 10AM FEEDING #1 (N</p>
</blockquote></td>
<td>)-&gt;</td>
<td><p>|</p>
<p>|</p></td>
<td colspan="2"><p>|</p>
<p>|</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>10AM FEEDING #2 (N</p>
<p>10AM FEEDING #3 (N</p>
<p>10AM FEEDING #4 (N</p>
<p>2PM FEEDING #1 (N</p>
<p>2PM FEEDING #2 (N</p>
<p>2PM FEEDING #3 (N</p>
<p>2PM FEEDING #4 (N</p>
<p>8PM FEEDING #1 (N</p>
<p>8PM FEEDING #2 (N</p>
<p>8PM FEEDING #3 (N</p>
<p>8PM FEEDING #4 (N</p>
<p>NUTRITION LOCATION (#119.61) BULK NOURISHMENTS (N</p>
</blockquote></td>
<td><p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p>
<p>)-&gt;</p></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>DIET PATTERNS (#111.1) ASSOCIATED SF MENU ... (N</p>
<p>NUTRITION PERSON (#115.07) ADMIS:SUPPLEM:SF MENU* (N</p>
</blockquote></td>
<td><p>)-&gt;</p>
<p>)-&gt;</p></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><p>|</p>
<blockquote>
<p>118.1 SUPPLEMEN* |</p>
<p>| 10AM FEEDING #1 |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>SUPPLEMENTAL</p>
</blockquote></td>
<td><blockquote>
<p>FE*</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>10AM FEEDING #2 |-&gt;</p>
<p>10AM FEEDING #3 |-&gt;</p>
<p>10AM FEEDING #4 |-&gt;</p>
<p>2PM FEEDING #1 |-&gt;</p>
<p>2PM FEEDING #2 |-&gt;</p>
<p>2PM FEEDING #3 |-&gt;</p>
<p>2PM FEEDING #4 |-&gt;</p>
<p>8PM FEEDING #1 |-&gt;</p>
<p>8PM FEEDING #2 |-&gt;</p>
<p>8PM FEEDING #3 |-&gt;</p>
<p>8PM FEEDING #4 |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL SUPPLEMENTAL</p>
</blockquote></td>
<td><blockquote>
<p>FE* FE* FE* FE* FE* FE* FE* FE* FE* FE* FE*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NUTRITION PERSON (#115.1) ADMIS:TUBEFEE:TF PROD* (N</p>
</blockquote></td>
<td>C )-&gt;</td>
<td><p>|</p>
<p>|</p></td>
<td colspan="2"><p>|</p>
<blockquote>
<p>118.2 TUBEFEEDI* |</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>RECURRING:TUBEFEEDING* (N</p>
</blockquote></td>
<td>C )-&gt;</td>
<td>|</td>
<td colspan="2"><blockquote>
<p>CORRESPONDING * |-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>RECIPE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>DIET PATTERNS (#111.11) ASSOCIATED STANDING OR* (N</p>
</blockquote></td>
<td>)-&gt;</td>
<td><p>|</p>
<p>|</p></td>
<td colspan="2"><p>|</p>
<blockquote>
<p>118.3 STANDING * |</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>ASSOCIATED STANDING OR* (N ASSOCIATED STANDING OR* (N</p>
<p>NUTRITION PERSON (#115.08) ADMIS:STANDIN:ORDER* . (N</p>
</blockquote></td>
<td><p>)-&gt;</p>
<p>)-&gt;</p>
<p>C )-&gt;</p></td>
<td><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Nutrition and Food Service Outpatient Meals Technical Manual and Security Guide 26

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 13%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4" rowspan="2"></th>
<th><p>|</p>
<p>|</p>
<p>|</p>
<p>|</p></th>
<th colspan="2"><blockquote>
<p>119 DIETITIAN T* DIETITIAN ITEM:PATIENT ITEM:ADMISSION</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>|</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>NEW PERSON PATIENT</p>
<p>PATIENT MOVEMENT</p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th colspan="2"></th>
<th colspan="2"></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>INGREDIENT (#113) DIETETIC UNIT OF ISSUE</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>L)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>119.1 UNITS</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NUTRITION PERSON (#115) ISOLATION/PRECAUTION (*</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>C )-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>119.4 ISOLATION*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADMISSION:ISOLATION/P*</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>C )-&gt;</p>
</blockquote></td>
<td>|</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUTRITION PERSON (#115.03) ADMIS:CONSULT:CONSULT*</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>119.5 DIETETIC *</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td>|</td>
<td colspan="2"><blockquote>
<p>USER TO BULLET*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NUTRITION PERSON (#115.01) ADMISSION:LAST LABEL *</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>119.6 NUTRITION*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADMISSION:DIETETIC WARD</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>C )-&gt;</p>
</blockquote></td>
<td>|</td>
<td colspan="2"><blockquote>
<p>CLINICIAN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NEW PERSON</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NUTRITION:DIETETIC WA*</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td colspan="2"><blockquote>
<p>TRAY SERVICE P*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SERVICE POINT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RECURRING:OUTPATIENT *</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td colspan="2"><blockquote>
<p>CAFETERIA SERV*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SERVICE POINT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SPECIAL MEALS:LOCATION</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td colspan="2"><blockquote>
<p>COMMUNICATION *</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>COMMUNICATION O*</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GUEST MEALS:LOCATION . FHZQ DAILY PRINT (#541374) DIET WARD ............</p>
</blockquote></td>
<td><p>(N</p>
<p>(N</p></td>
<td colspan="2"><blockquote>
<p>)-&gt;</p>
<p>S )-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>SUPP. FDG. SITE</p>
<p>DEFAULT ADMISS*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
<p>|</p>
<p>|-&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SUPPLEMENTAL FE*</p>
<p>DIETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>v OUTPATIENT LOC*</p>
<p>m BULK N:BULK N*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WARD LOCATION HOSPITAL LOCATI*</p>
<p>SUPPLEMENTAL FE*</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>m ROOM-B:ROOM-B* m ASSOCI:ASSOCI* m ASSOCI:ASSOCI*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
<p>|-&gt;</p>
<p>|-&gt;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ROOM-BED</p>
<p>WARD LOCATION HOSPITAL LOCATI*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SERVICE POINT (#119.72) PRODUCTION FACILITY ..</p>
</blockquote></td>
<td>(N</td>
<td colspan="2"><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>119.71 PRODUCTI*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>SUPPLEMENTAL FEEDING (#119.74)</p>
</blockquote></td>
<td>|</td>
<td colspan="6">|</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>PRODUCTION FACILITY .. (N )-&gt;</p>
</blockquote></td>
<td>|</td>
<td colspan="6">|</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>FHZQ DAILY PRINT (#541374)</p>
</blockquote></td>
<td>|</td>
<td colspan="6">|</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>PRODUCTION FACILITY .. (N S )-&gt;</p>
</blockquote></td>
<td>|</td>
<td colspan="6">|</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MEAL (#116.112) RECIP:POPULAR:SERVICE*</p>
</blockquote></td>
<td>(N</td>
<td>C</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p></td>
<td><blockquote>
<p>119.72</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE *</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
<p>|</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>NUTRITION LOCATION (#119.6)</p>
</blockquote></td>
<td></td>
<td></td>
<td>|</td>
<td colspan="2"></td>
<td colspan="2"><blockquote>
<p>|</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>TRAY SERVICE POINT ... (N</p>
</blockquote></td>
<td>C</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td>|</td>
<td colspan="2"><blockquote>
<p>PRODUCTION FAC*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>PRODUCTION</p>
</blockquote></td>
<td><blockquote>
<p>FACI*</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>CAFETERIA SERVICE POINT (N FHZQ DAILY PRINT (#541374)</p>
<p>SERVICE POINT (N</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>m ADDITI:ADD. M*</p>
<p>m PRODUC:FORECA*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|-&gt;</p>
<p>|</p>
<p>|-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>PRODUCTION</p>
<p>PRODUCTION</p>
</blockquote></td>
<td><blockquote>
<p>DIET</p>
<p>DIET</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>DIETETIC ENCOUNTERS (#115.7) COMMUNICATIONS OFFICE (N</p>
<p>MEALS SERVED (#117.06)</p>
</blockquote></td>
<td>C</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="2"><blockquote>
<p>119.73 COMMUNIC*</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>|</p>
<p>|</p>
<p>|</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMM OFFICE ..........</p>
<p>STAFFING DATA (#117.11) COMM OFFICE ..........</p>
</blockquote></td>
<td><p>(N</p>
<p>(N</p></td>
<td colspan="2"><blockquote>
<p>)-&gt;</p>
<p>)-&gt;</p>
</blockquote></td>
<td><p>|</p>
<p>|</p>
<p>|</p></td>
<td colspan="6"><p>|</p>
<p>|</p>
<p>|</p></td>
</tr>
</tbody>
</table>

> NUTRITION LOCATION (#119.6) \| \|

<table style="width:100%;">
<colgroup>
<col style="width: 48%" />
<col style="width: 3%" />
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>COMMUNICATION OFFICE . (N</th>
<th>C</th>
<th><blockquote>
<p>)-&gt;</p>
</blockquote></th>
<th><blockquote>
<p>|</p>
</blockquote></th>
<th>|</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FHZQ DAILY PRINT (#541374)</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td>|</td>
</tr>
<tr class="even">
<td>COMMUNICATION OFFICE . (N</td>
<td>S</td>
<td><blockquote>
<p>)-&gt;</p>
</blockquote></td>
<td><blockquote>
<p>|</p>
</blockquote></td>
<td>|</td>
</tr>
</tbody>
</table>

> NUTRITION LOCATION (#119.6) \| \| SUPP. FDG. SITE ...... (N )-\> \| 119.74 SUPPLEME\* \| FHZQ DAILY PRINT (#541374) \| \|

> SUPPLEMENTAL FEEDING S\* (N S )-\> \| PRODUCTION FAC\* \|-\> PRODUCTION FACI\*

> \| 119.8 DIETETIC \* \|

> \| PATIENT \|-\> NUTRITION PERSON

> \| ADMISSION \|-\> PATIENT MOVEMENT

> \| ENTERED CLERK \|-\> NEW PERSON

> \| 119.9 FH SITE P\* \|

> \| OUTPATIENT MEA\* \|-\> DIETS

> \| OUTPATIENT MEA\* \|-\> DIETS

> \| OUTPATIENT MEA\* \|-\> DIETS

> \| OUTPATIENT MEA\* \|-\> DIETS

> \| OUTPATIENT MEA\* \|-\> DIETS

> \| AUTHORIZOR 1 \|-\> NEW PERSON

> \| AUTHORIZOR 2 \|-\> NEW PERSON

> \| AUTHORIZOR 3 \|-\> NEW PERSON

> \| AUTHORIZOR 4 \|-\> NEW PERSON

> \| AUTHORIZOR 5 \|-\> NEW PERSON

> \| m LAB TE:LAB TE\* \|-\> LABORATORY TEST

> \| m LABEL :LABEL \* \|-\> DEVICE

> \| m DRUG C:DRUG C\* \|-\> VA DRUG CLASS

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The menu and options exported by the Outpatient Meals are all located in the FH namespace. Individual options can be viewed by using the Kernel option XUINQUIRE (Inquire). This option is found on the menu XUMAINT (Menu Management), which is a sub-menu of the EVE (Systems Manager Menu) option.

> A diagram of the structure of the Outpatient Meals menu and its options can be produced by using the Kernel option XUUSERACC (Diagram Menus). Choosing XUUSERACC permits you to further select XUUSERACC1 or XUUSERACC2 menu diagrams with entry/exit actions or abbreviated menu diagrams. This option is found on the menu XUMAINT (Menu management), which is a sub-menu of the EVE (Systems Manager Menu) option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Internal Entry Name</p>
</blockquote></th>
<th><blockquote>
<p>Option Name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>[FHMGROM]</p>
</blockquote></td>
<td><blockquote>
<p>OM: Outpatient Meals Main Menu</p>
</blockquote></td>
<td><blockquote>
<p>This menu allows access to all options pertaining to the outpatient meals functionality.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMSMGR]</p>
</blockquote></td>
<td><blockquote>
<p>SM: Special Meals Menu</p>
</blockquote></td>
<td><blockquote>
<p>This menu allows yo access to all special meals options within the outpatient meals menu</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMSR]</p>
</blockquote></td>
<td><blockquote>
<p>RO: Request a Meal</p>
</blockquote></td>
<td><blockquote>
<p>This option allows the request of a special meal.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMSA]</p>
</blockquote></td>
<td><blockquote>
<p>AM: Authorize a Meal</p>
</blockquote></td>
<td><blockquote>
<p>This option allows an authorized user to authorize a special meal request.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMSP]</p>
</blockquote></td>
<td><blockquote>
<p>PM: Print Meal Voucher</p>
</blockquote></td>
<td><blockquote>
<p>This option allows you to print a special meal voucher ticket.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMSC]</p>
</blockquote></td>
<td><blockquote>
<p>CM: Cancel a Meal</p>
</blockquote></td>
<td><blockquote>
<p>This option allows the user to cancel a special meal.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMSS]</p>
</blockquote></td>
<td><blockquote>
<p>MS: Meal Status Report</p>
</blockquote></td>
<td><blockquote>
<p>This option allows to prints a list of existing special meals and their current status</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMRMGR]</p>
</blockquote></td>
<td><blockquote>
<p>RM: Recurring Meals Menu</p>
</blockquote></td>
<td><blockquote>
<p>This menu allows access to all recurring meals options within the outpatient meals or the editing of existing outpatient meals.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMRO]</p>
</blockquote></td>
<td><blockquote>
<p>OD: Order/Edit Outpatient Meals</p>
</blockquote></td>
<td><blockquote>
<p>Option to order recurring outpatient meals or edit existing outpatient meals.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMRE]</p>
</blockquote></td>
<td><blockquote>
<p>EL: Early/Late Tray</p>
</blockquote></td>
<td><blockquote>
<p>This option allows you to enter an early/late tray for an outpatient recurring meal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMRR]</p>
</blockquote></td>
<td><blockquote>
<p>RO: Review Outpatient Meal</p>
</blockquote></td>
<td><blockquote>
<p>Use this option to display/review recurring outpatient meals</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHORD9]</p>
</blockquote></td>
<td><blockquote>
<p>PP: Patient Profile</p>
</blockquote></td>
<td><blockquote>
<p>This option will produce a comprehensive display of most dietetic orders and data associated with a patient's admission. It includes diet orders, active or saved consults, early/late tray requests for the next 72 hours, standing orders, tube feedings, supplemental feedings, etc.</p>
<p>As of Version 5.5, this report will include outpatient data as well, including recurring meals, special meals and guest</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark10" class="anchor"></span>Internal Entry Name</p>
</blockquote></th>
<th><blockquote>
<p>Option Name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>meals.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMRC]</p>
</blockquote></td>
<td><blockquote>
<p>CM: Cancel Outpatient Meal</p>
</blockquote></td>
<td><blockquote>
<p>This option allows the cancellation of existing outpatient recurring meal(s)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMRA]</p>
</blockquote></td>
<td><blockquote>
<p>AO: Additional Orders</p>
</blockquote></td>
<td><blockquote>
<p>This option allows the entry of additional orders for outpatients with recurring meals.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMRT]</p>
</blockquote></td>
<td><blockquote>
<p>TF: Tube feeding</p>
</blockquote></td>
<td><blockquote>
<p>This option allows you to order tube feedings for outpatients with recurring meals.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMRP]</p>
</blockquote></td>
<td><blockquote>
<p>PT: Recurring Meal Plan Expiration List</p>
</blockquote></td>
<td><blockquote>
<p>This option displays a list of meal plans expiring for selected outpatient locations.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMIP]</p>
</blockquote></td>
<td><blockquote>
<p>IP: Outpatient Isolation/Precaution</p>
</blockquote></td>
<td><blockquote>
<p>This option is used for entering Isolations/Precautions for outpatients.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMRAC]</p>
</blockquote></td>
<td><blockquote>
<p>CA: Cancel Additional Order</p>
</blockquote></td>
<td><blockquote>
<p>This option is used to cancel existing additional orders.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMREC]</p>
</blockquote></td>
<td><blockquote>
<p>CE: Cancel Early/Late Tray</p>
</blockquote></td>
<td><blockquote>
<p>This option is used to cancel existing early/late tray orders.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMRTC]</p>
</blockquote></td>
<td><blockquote>
<p>CT: Cancel Tube feeding</p>
</blockquote></td>
<td><blockquote>
<p>This option is used to cancel existing tube feeding orders.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMGMGR]</p>
</blockquote></td>
<td><blockquote>
<p>GM: Guest Meals Menu</p>
</blockquote></td>
<td><blockquote>
<p>This menu allows access to all guest meals options within the outpatient meals menu.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[FHOMGR]</p>
</blockquote></td>
<td><blockquote>
<p>GM: Request a Meal</p>
</blockquote></td>
<td><blockquote>
<p>This option allows the user to order an outpatient guest meal for individuals categorized in one of the five listed classifications and be added to the N&amp;FS meal list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[FHOMGP]</p>
</blockquote></td>
<td><blockquote>
<p>PT: Print Guest Meal List</p>
</blockquote></td>
<td><blockquote>
<p>This option provides a printed list of requested guest meals by Date, Patient Name, Meal, Class, and Location.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> XINDEX is a routine that produces a report called the VA Cross-Reference. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a listing of internal and external routine calls.

> XINDEX is invoked from programmer mode: D ^XINDEX. When selecting routines, select FH\*.

# Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  FH IBDF EDIT HEADER BLOCK Form Header
2.  FH EVSEND OR FH --\> OR event messages
3.  FH ORDERABLE ITEM UPDATE Update Dietetics orderable item
4.  FH RECEIVE FH receives order msg from OE/RR
5.  FH SIGNED REACTION CANCEL FH Signed Reaction Cancel
6.  FH SIGNED REACTION INTERFACE FH Signed Reaction Interface
7.  FHW1 Diet Order
8.  FHW2 Early/Late Tray
9.  FHW3 Isolation/Precautions
10. FHW4 NPO
11. FHW6 Dietetic Consult
12. FHW7 Additional Orders
13. FHW8 Tubefeeding
14. FHWMAS Dietetics MAS Event Processor
15. FHWMENU Dietetic Orders

# Callable Routines/Entry Points/Application Programmer Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following APIs are updated in Outpatient Meals v.5.5:

> The following APIs are new to Outpatient Meals v.5.5:

> All four APIs are used by CPRS/OERR.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> External Interfaces are not used in the Nutrition and Food Service Outpatient Meals V5.5 software.

# Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Nutrition and Food Service Outpatient Meals V. 5.5 subscribes to Database Integration Agreements (DBIAs) with the Health Summary, CPRS, and Nursing. Nutrition and Food Service Outpatient Meals v.

> 5.5 also offers DBIAs for other packages to subscribe to as well.

> DBIA 2287, used by CPRS/OERR, was modified in Nutrition and Food Service Outpatient Meals v. 5.5.

> For detailed information about these DBIAs, log in to FORUM and select the *Integration Agreements Menu* \[DBA IA ISC\] option located under the *DBA* \[DBA\] option (Data Base Administrator). Once in the Integration Agreements Menu Option, select “Inquire” and type FH at the “Select INTEGRATION REFERENCES:” prompt.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Very few of the options in this package would appear to be candidates for standalone use. Therefore, a number of menus have been formally documented as assignable. Other options are not designed for standalone use but may be assigned to locally-developed menus if desired. However, such options may not be utilized in future releases.

> The assignable menus are described in the section Exported Menu Structure.

# Package Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No variables are used package wide.

## Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Under the Special Meals menu, the Request a Meal option will call SETUP^XQALERT to send an alert to the five Authorizers set-up in the site parameters if the person requesting the meal does not hold the FHAUTH key. The Authorize a Meal option will call SETUP^XQALERT to send an alert back to the requestor once the meal has been authorized or denied by an authorizer.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No remote systems are used in the Outpatient Meals V5.5 software

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Archiving capabilities are not currently available for Nutrition and Food Service Outpatient Meals v. 5.5.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites utilizing the Nutrition and Food Service Outpatient Meals v. 5.5 should develop a local contingency plan to be used in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system

> <span id="_bookmark13" class="anchor"></span>outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Officer (RISO).

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No interfacing is used in the Nutrition and Food Service Outpatient Meals V5.5 software.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Under the Special Meals menu, the Authorize a Meal option will call SIG^XUSESIG to prompt the authorizer for their electronic signature when authorizing or denying a special meals voucher.

## Menu Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign the following menus to Nutrition and Food Service Outpatient Meals V. 5.5 users if they have not already been assigned:

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th><blockquote>
<p>User</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FHMGR</p>
</blockquote></td>
<td><blockquote>
<p>Dietetics Management - N&amp;FS application coordinator, Chief, Nutrition and Food Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHWARD</p>
</blockquote></td>
<td><blockquote>
<p>Dietetic Orders - Ward clerks, clinic clerks, nurses, clinical dietitians, dietetic technicians</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Security in this package is controlled almost exclusively by the menu option that is assigned to a person. The use of menus containing MGR give the person read/write access to all files referenced by their options while other menus give only read access to important files.

> Since a substantial amount of file pointering occurs in this package, deletion of entries in many files is prohibited under ordinary conditions. Rather, entries are deactivated and are screened from selection. In order to reactivate these entries, a person with FileMan access of @ or the FHMGR Security Key must select and re-activate any inactive entries.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Allocate the following security keys to appropriate site personnel:

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FHAUTH</p>
</blockquote></td>
<td><blockquote>
<p>This new key allows authorization of Outpatient Meals Special Meals requests.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FHMGR</p>
</blockquote></td>
<td><blockquote>
<p>This key allows deletion of Dietetics file entries as well as the ability to select inactivated entries for re-activation or deletion.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FHWARD</p>
</blockquote></td>
<td><blockquote>
<p>This key is for the set of routines comprising FHWARD, the ward order-entry programs</p>
</blockquote></td>
</tr>
</tbody>
</table>

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Nutrition and Food Service Outpatient Meals v. 5.5 changes and enhancements do not modify any existing file security schemes.

## Official Policy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Nutrition and Food Service Outpatient Meals v. 5.5 software release references no official policy unique to the product regarding the modification of software and distribution of the version.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acronyms and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Acronym</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>API</p>
</blockquote></td>
<td><blockquote>
<p>Application Programmer Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ARTS</p>
</blockquote></td>
<td><blockquote>
<p>Adverse Reaction Tracking</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DFN</p>
</blockquote></td>
<td><blockquote>
<p>File Number—the local/facility patient record number (patient file internal entry number)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DVA</p>
</blockquote></td>
<td><blockquote>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FDA</p>
</blockquote></td>
<td><blockquote>
<p>Food and Drug Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GUI</p>
</blockquote></td>
<td><blockquote>
<p>Graphical User Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7</p>
</blockquote></td>
<td><blockquote>
<p>Health Level 7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HSD&amp;D</p>
</blockquote></td>
<td><blockquote>
<p>Health System Design and Development</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td><blockquote>
<p>Integration Control Number, or national VA patient record number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IMG</p>
</blockquote></td>
<td><blockquote>
<p>Information Management Group</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IRM</p>
</blockquote></td>
<td><blockquote>
<p>Information Resource Management</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KIDS</p>
</blockquote></td>
<td><blockquote>
<p>Kernel Installation and Distribution System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NNAB</p>
</blockquote></td>
<td><blockquote>
<p>National Nutrition Advisory Board</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ODD</p>
</blockquote></td>
<td><blockquote>
<p>Officer of the Day</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OINT</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information National Training and Education Office</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PCE</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Encounter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Information Management Systems</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PMO</p>
</blockquote></td>
<td><blockquote>
<p>Project Management Office</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PTF</p>
</blockquote></td>
<td><blockquote>
<p>Patient Treatment File</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>System Implementation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Department of Veteran Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VERA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Equitable Resource Allocation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VHA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Acronym</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VISN</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Integrated Service Networks</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WOC</p>
</blockquote></td>
<td><blockquote>
<p>Without Compensation</p>
</blockquote></td>
</tr>
</tbody>
</table>
