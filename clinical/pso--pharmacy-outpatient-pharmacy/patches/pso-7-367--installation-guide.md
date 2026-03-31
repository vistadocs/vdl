---
title: PSO*7*367 VistA FDA Medication Guides Project Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: VistA FDA Medication Guides Project
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*367
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: > The purpose of this Installation Guide is to provide an explanation of the installation and implementation process for the Food and Drug Administration (FDA) Medication Guides Increment 3 project.
audience: 
keywords: 
  - table
  - contents
  - blockquote
  - class
  - transport
  - global
  - printer
  - install
  - installation
  - updates
page_count: 0
word_count: 1928
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/phar_fda_med_guide_rel3_ig_vista.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/phar_fda_med_guide_rel3_ig_vista.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

> ![](pso-7-367-vista-fda-medication-guides-project-installation-guide/001.png)

FDA Medication Guides Project

> VistA Component

> INSTALLATION GUIDE

> XU\*8\*566 PSN\*4\*264 PSO\*7\*367 PSX\*2\*70

> March 2012

> Department of Veterans Affairs Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Purpose](#purpose)
- [Scope](#scope)
- [Before You Begin](#before-you-begin)
- [Section 1: Pre-Installation](#section-1-pre-installation)
    - [Documentation](#documentation)
    - [System Requirements](#system-requirements)
    - [User Interfaces](#user-interfaces)
    - [Hardware Interfaces](#hardware-interfaces)
    - [Software Interfaces](#software-interfaces)
    - [User Characteristics](#user-characteristics)
    - [Acronyms](#acronyms)
    - [Dependencies and Constraints](#dependencies-and-constraints)
    - [Data Dictionary Updates](#data-dictionary-updates)
  - [Consolidated Mail Outpatient Pharmacy (CMOP)](#consolidated-mail-outpatient-pharmacy-cmop)
  - [National Drug File (NDF)](#national-drug-file-ndf)
  - [Kernel](#kernel)
- [Section 2: Installation of Patches](#section-2-installation-of-patches)
    - [Installing XU\8\566](#installing-xu8566)
    - [Installing PSN\4\264](#installing-psn4264)
    - [Installing PSO\7\367](#installing-pso7367)
    - [Installing PSX\2\70](#installing-psx270)
- [Section 3: Configuration](#section-3-configuration)
    - [Automatically Printing FDA Medication Guides is Optional](#automatically-printing-fda-medication-guides-is-optional)
    - [Updating the WINDOWS NETWORK PRINTER NAME field (#75) in the DEVICE file (#3.5)](#updating-the-windows-network-printer-name-field-75-in-the-device-file-35)
    - [Updating the FDA MED GUIDE PRINT SERVER URL field (#134) in the OUTPATIENT SITE file (#59)](#updating-the-fda-med-guide-print-server-url-field-134-in-the-outpatient-site-file-59)
    - [Updating the FDA MED GUIDE PRINTER Multiple (#135) in the OUTPATIENT SITE file (#59)](#updating-the-fda-med-guide-printer-multiple-135-in-the-outpatient-site-file-59)
| Date | Revision | Description  | Author                         |
|----------|--------------|------------------|------------------------------------|
| O3/12    | 1.0          | Original Version | <span class="mark">REDACTED</span> |
> *(This page included for two-sided copying.)*

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this Installation Guide is to provide an explanation of the installation and implementation process for the Food and Drug Administration (FDA) Medication Guides Increment 3 project.

> The intended audience for this document is the Information Resources Management Service (IRMS) staff responsible for installing patches and Outpatient Pharmacy staff responsible for maintaining the pharmacy files.

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Outpatient Pharmacy application was modified to allow for automatic printing of FDA Medication Guides when available along with prescription labels on the designated FDA Medication Guide printers. Outpatient Pharmacy was also modified to provide the ability to reprint an FDA Medication Guide when reprinting a prescription label, to create and maintain a list of FDA Medication Guide printers for a specific pharmacy division, and to change the printer at any point of the dispensing process. FDA Medication Guides may be reprinted for any given prescription fill. Changes were made to the Consolidated Mail Outpatient Pharmacy (CMOP) activity log to show which specific FDA Medication Guide was available when the prescription fill was transmitted to CMOP. A PC based Java software

> ![](pso-7-367-vista-fda-medication-guides-project-installation-guide/002.png)component was introduced to enable the automatic printing of the FDA Medication Guide from within VistA. The ability to update the Windows network printer name for a specific device is available through the Kernel application.

# Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document is organized into three major sections: “Pre-Installation”, “Installation of Patches”, and Configuration. You must install the Java Component first. A

> separate Installation Guide is provided for the installation of the Java Component. See PHAR_FDA_MED_GUIDE_REL3_IG_JAVA.doc.

> It is expected that most sites will install the software and not immediately implement the new interface. This approach is recommended.

> Having the proper setup of parameters and settings is critical to the success of the implementation.

# Section 1: Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides information that helps you determine patch and system requirements before installing the patches that are included in this project. It also helps you understand the updates that the installation process makes. Additionally, descriptions are provided regarding the specific parameters that you must set up to implement the interface.

### Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Documentation distributed with the FDA Medication Guide project includes the following and may be retrieved from the VISTA Documentation Library (VDL) on the Internet at the following address: [<u>http://www.va.gov/vdl</u>](http://www.va.gov/vdl).

> <u>File Names</u> <u>Description</u>

> PSO_7_PHAR_UM_R0312.pdf Outpatient Pharmacy User Manual PSO_7_P367_PHAR_UM_CP.pdf Outpatient Pharmacy User Manual Change Pages PSO_7_TM_R0312.pdf Outpatient Pharmacy Technical Manual

> PSO_7_P367_TM_CP.pdf Outpatient Pharmacy Technical Manual Change Pages PHAR_FDA_MED_GUIDE_REL3_RN.pdf FDA Medication Guides Project Release Notes PHAR_FDA_MED_GUIDE_REL3_VISTA\_

> IG.pdf FDA Medication Guides Project VistA Installation Guide PHAR_FDA_MED_GUIDE_REL3_JAVA\_

> IG.pdf FDA Medication Guides Project Java Installation Guide

### System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The FDA Medication Guide project operates on standard hardware platforms used by the Veterans Health Administration (VHA) facilities and requires the following Department of Veterans Affairs (VA) software packages to support the enhancements in this project.

> New functionality is being added to the Outpatient Pharmacy V.7.0, CMOP V.2.0, and Kernel V.8.0 applications to allow users to automatically print the associated FDA Medication Guide for a specific prescription as well as reprint FDA Medication Guides.

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package</strong></th>
<th><strong>Minimum Version Needed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA FileMan</td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Health Level 7</td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Order Entry/Results Reporting</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CMOP</td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>NDF</td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Outpatient</td>
<td><blockquote>
<p>7.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Pharmacy Data Management</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Controlled Substances</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Toolkit</td>
<td><blockquote>
<p>7.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Drug Accountability</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

### User Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This software product will conform to the existing VistA conventions found in the Outpatient Pharmacy package. The reports, option and screen formats will conform to the existing VistA conventions. Report formats and option process steps, such as “roll & scroll” will be field tested for usability by test site personnel to ensure that all new functionality meets the needs of the VHA user.

### Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The product will run on standard hardware platforms that Department of Veterans Affairs Healthcare (VHA) facilities use. These systems consist of standard or upgraded Alpha AXP clusters that operate on Virtual Memory System (VMS)/Linux running the Intersystems Cache Product.

> These enhancements are compatible with existing hardware. No hardware issues are involved with these enhancements.

### Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An interface between Outpatient Pharmacy V.7.0 and NDF V.4.0 is required to manage the FDA Medication Guide output for this enhancement. Existing interfaces with other applications to support prescription processing will be maintained for this enhancement.

### User Characteristics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The intended users of the FDA Medication Guide Project will include pharmacists, pharmacy technicians, and veteran patients and their families.

### Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>API</td>
<td><blockquote>
<p>Application Programming Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CFR</td>
<td><blockquote>
<p>Code of Federal Regulations</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CMOP</td>
<td><blockquote>
<p>Consolidated Mail Outpatient Pharmacy</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FDA</td>
<td><blockquote>
<p>Food and Drug Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>NDC</td>
<td><blockquote>
<p>National Drug Code</p>
</blockquote></td>
</tr>
<tr class="even">
<td>NDF</td>
<td><blockquote>
<p>National Drug File</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OPAI</td>
<td><blockquote>
<p>Outpatient Pharmacy Automation Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PDF</td>
<td><blockquote>
<p>Portable Document Format</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PMI</td>
<td><blockquote>
<p>Patient Medication Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RSD</td>
<td><blockquote>
<p>Requirements Specification Document</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SQA</td>
<td><blockquote>
<p>Software Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td>URL</td>
<td><blockquote>
<p>Uniform Resource Locator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VAMCs</td>
<td><blockquote>
<p>Veterans Affairs Medical Centers</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VHA</td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VistA</td>
<td><blockquote>
<p>Veterans Health Information Systems and Technology Architecture</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Dependencies and Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pharmacy Benefits Management (PBM) policies and FDA regulations exist that define which medications contain FDA Medication Guides. These should not be modified without guidance from PBM.

### Data Dictionary Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark14" class="anchor"></span>Outpatient Pharmacy

#### File Updates

> The following new sub-file was added to the OUTPATIENT SITE file (#59) to store the list of printers available for printing FDA Medication Guides for the division.

- FDA MED GUIDE PRINTER (#135)

#### Field Updates

> The following new field was added to the DEVICE file (#3.5) to store the Windows network name of the FDA Medication Guide printers:

- WINDOWS NETWORK PRINTER NAME (#75)

> The following new fields were added to the new sub-file FDA MED GUIDE PRINTER (#135)

- FDA MED GUIDE PRINTER (#.01)
- DEFAULT PRINTER (#.02)

> The following new field was added to the OUPATIENT SITE file (#59)

- FDA MED GUIDE PRINT SERVER URL (#134)

> The following new field was added to the PRESCRIPTION file (#52), LABEL DATE/TIME sub-file (#52.032)

- FDA MED GUIDE FILENAME (#35)

> The following new field was added to the PRESCRIPTION file (#52), CMOP EVENT sub-file (#52.01)

- FDA MED GUIDE FILENAME (#35)

#### Input Template Updates

> The following template was modified to allow users to update FDA Medication Guide Printers and the address for the server where Java is installed via the *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\] option.

- PSO SITE

#### Protocol Updates

> The following protocol was modified

- PSO LM HIDDEN OTHER \#2

> The following new protocol was added

- PSO LM REPRINT FDA MED GUIDE

#### Menu Option Updates

> The following option was modified to include the editing of the new field, WINDOWS NETWORK PRINTER NAME.

- Edit All Device Fields option \[XUDEVEDITALL\]

#### Routine Updates

> The following new routine was added:

- PSOFDAUT

> The following routines were modified:

- PSOB
- PSOBMST
- PSOEXRST
- PSOFDAMG
- PSOLBL
- PSOLBL1
- PSOLBL2
- PSOLBLN
- PSOLBLN1
- PSOLLL1
- PSOLLL4
- PSOLLL8
- PSOLLLI
- PSOLSET
- PSOORAL1
- PSORXL
- PSORXRP1
- PSORXRP2
- PSORXRPT
- PSORXVW1
- PSORXVW2
- PSOSULB1
- PSOSURST

## Consolidated Mail Outpatient Pharmacy (CMOP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Routine Updates

> The following routines were modified:

- PSXRPPL
- PSXRSUS
- PSXRXU

## National Drug File (NDF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Field Updates

> The following field in the VA PRODUCT file (#50.68) was updated to add a period after the help prompt, and the technical description was updated to indicate the location of the repository for FDA Medication Guides.

- FDA MED GUIDE (#100)

#### Routine Updates

> The following routine was modified:

- PSNFDAMG

## Kernel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### File Updates

> The following file was modified:

- DEVICE (#3.5)

#### Field Updates

> The following new field was added

- WINDOWS NETWORK PRINTER NAME (#75)

#### Routine Updates

> The following routine was modified:

- XTHC10

# Section 2: Installation of Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This installation is comprised of PSO\*7\*367, PSN\*4\*264, PSX\*2\*70 and XU\*8\*566. Please read the following installation instructions carefully before beginning the installation.

> Patches should be installed in the following order:

> XU\*8\*566 PSN\*4\*264 PSO\*7\*367 PSX\*2\*70

### Installing XU\*8\*566

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch may be installed with VISTA users online. However, it is recommended that it be Queued for a time of generally least activity.

> TaskMan does not need to be STOPPED or placed in a WAIT state, and installation should take less than a minute.

#### To install XU\*8\*566:

1.  Use the *'INSTALL/CHECK MESSAGE'* option on the *PackMan* menu.
2.  The patch has now been loaded into a transport global on your system. You now need to use KIDS to install the transport global.
3.  On the KIDS menu, under the 'Installation' *menu, use the following* options:
    1.  *Print Transport Global*
    2.  *Compare Transport Global to Current System*
    3.  *Verify Checksums in Transport Global*
    4.  *Backup a Transport Global*
4.  On the KIDS menu, under the 'Installation' menu, use the following option: Select Installation Option: Install Package(s)

> Select INSTALL NAME: XU\*8.0\*566

> ==========

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Example of XU\*8\*566 Installation

> Select Installation Option: INSTall Package(s)

> Select INSTALL NAME: XU\*8.0\*566 9/27/11@12:18:03

> =\> XU\*8\*566 - 09/27/2011 - \#1

> This Distribution was loaded on Sep 27, 2011@12:18:03 with header of XU\*8\*566 - 09/27/2011 - \#1

> It consisted of the following Install(s): XU\*8.0\*566

> Checking Install for Package XU\*8.0\*566

> Install Questions for XU\*8.0\*566

> Incoming Files:

> 3.5 DEVICE (Partial Definition) Note: You already have the 'DEVICE' File.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// GENERIC INCOMING TELNET

> XU\*8.0\*566

> ────────────────────────────────────────────────────────────────────────────────

> Build Distribution Date: Sep 27, 2011

> Installing Routines:

> Sep 27, 2011@12:23:46

> Installing Data Dictionaries:

> Sep 27, 2011@12:23:46

> Updating Routine file...

> Updating KIDS files...

> XU\*8.0\*566 Installed.

> Sep 27, 2011@12:23:46

> Not a production UCI

> NO Install Message sent

> ──────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

> Install Completed

### Installing PSN\*4\*264

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation takes less than five minutes. This patch should be installed during non-peak requirement hours. No options need to be placed out of order and no users need to be off the system during the installation of this patch.

> To install PSN\*4\*264

1.  Use the *INSTALL/CHECK MESSAGES* option on the *PackMan* menu.
2.  From the *Kernel Installation & Distribution System* (KIDS) menu, select the Installation menu.
3.  From this *menu, you may select to use the following* options (when prompted for INSTALL NAME, enter PSN\*4.0\*264).
    1.  *Backup a Transport Global* - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.
    2.  *Compare Transport Global to Current System* - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  *Verify Checksums in Transport Global* - This option will ensure the integrity of the routines that are in the transport global.
    4.  *Print Transport Global* - This option will allow you to view the components of the KIDS build.
4.  *Use the Install Package(s)* option and select PSN\*4.0\*264.
5.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond NO.
6.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.

> Example of PSN\*4\*264 Installation

> Select Installation Option: INStall Package(s)

> Select INSTALL NAME: PSN\*4.0\*264 9/27/11@12:17:58

> =\> PSN\*4\*264 - 09/27/2011 - \#1

> This Distribution was loaded on Sep 27, 2011@12:17:58 with header of PSN\*4\*264 - 09/27/2011 - \#1

> It consisted of the following Install(s): PSN\*4.0\*264

> Checking Install for Package PSN\*4.0\*264 Install Questions for PSN\*4.0\*264

> Incoming Files:

> 50.68 VA PRODUCT (Partial Definition) Note: You already have the 'VA PRODUCT' File.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// GENERIC INCOMING TELNET

> PSN\*4.0\*264

> ────────────────────────────────────────────────────────────────────────────────

> 

> Build Distribution Date: Sep 27, 2011

> Installing Routines:

> Sep 27, 2011@12:21:16

> Installing Data Dictionaries:

> Sep 27, 2011@12:21:16

> Updating Routine file... Updating KIDS files...

> PSN\*4.0\*264 Installed.

> Sep 27, 2011@12:21:16

> Not a production UCI

> NO Install Message sent

> ──────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

> Install Completed

### Installing PSO\*7\*367

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch installation will take less than 2 minutes. It is recommended that installation be queued for off peak hours.

> To install PSO\*7\*367

1.  Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu.
2.  From the *Kernel Installation & Distribution System* (KIDS) menu, select the Installation menu.
3.  From this *menu, you may select to use the foll*owing options (when *prompted for* INSTALL NAME, enter PSO\*7.0\*367).
    1.  *Backup a Transport Global -* This option will create a backup *message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.*
    2.  *Compare Transport Global to Current System* - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  *Verify Checksums in Transport Global* - This option will ensure the integrity of the routines that are in the transport global.
    4.  *Print Transport Global* - This option will allow you to view the components of the KIDS build.
4.  *Use the Install Package(s)* option and select the package PSO\*7.0\*367.
5.  When prompted "Want *KIDS* to INHIBIT LOGONs during the install? NO//" respond NO.
6.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.

> Example of PSO\*7\*367 Installation

> Select Installation Option: INSTall Package(s)

> Select INSTALL NAME: PSO\*7.0\*367 9/27/11@12:17:24

> =\> PSO\*7\*367 - 09/27/2011 - \#1

> This Distribution was loaded on Sep 27, 2011@12:17:24 with header of PSO\*7\*367 - 09/27/2011 - \#1

> It consisted of the following Install(s): PSO\*7.0\*367

> Checking Install for Package PSO\*7.0\*367

> Install Questions for PSO\*7.0\*367

> Incoming Files:

> 52 PRESCRIPTION (Partial Definition) Note: You already have the 'PRESCRIPTION' File.

> 59 OUTPATIENT SITE (Partial Definition) Note: You already have the 'OUTPATIENT SITE' File.

> Want KIDS to INHIBIT LOGONs during the install? NO// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// GENERIC INCOMING TELNET

> PSO\*7.0\*367

> ──────────────────────────────────────────────────────────────────────────────

> PSOXZA16 PSOXZA2 PSOXZA3 PSOXZA4 PSOXZA5 PSOXZA6 PSOXZA7 PSOXZA8 PSOXZA9

> Updating KIDS files...

> PSO\*7.0\*367 Installed.

> Sep 27, 2011@12:18:42

> Not a production UCI

> NO Install Message sent

> ──────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

> Install Completed

### Installing PSX\*2\*70

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch installation will take less than 2 minutes. It is recommended that installation be queued for off peak hours.

> Do not install or schedule patch PSX\*2\*70 to install when prescriptions are being transmitted to CMOP. Wait for the CMOP transmission to finish or complete the installation before the transmission starts.

#### To install PSX\*2\*70:

1.  Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu.
3.  From this *menu, you may select to use the following* options (when *prompted* for INSTALL NAME, enter PSX\*2.0\*70).
    1.  *Backup a Transport Global* - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.
    2.  *Compare Transport Global to Current System* - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  *Verify Checksums in Transport Global* - This option will ensure the integrity of the routines that are in the transport global.
    4.  *Print Transport Global* - This option will allow you to view the components of the KIDS build.
4.  Use the Install Package(s) option and select the package PSX\*2.0\*70.
5.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond NO.
6.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.

> Example of PSX\*2\*70 Installation

> Select Installation Option: INStall Package(s)

> Select INSTALL NAME: PSX\*2.0\*70 9/27/11@12:17:52

> =\> PSX\*2\*70 - 09/27/2011 - \#1

> This Distribution was loaded on Sep 27, 2011@12:17:52 with header of PSX\*2\*70 - 09/27/2011 - \#1

> It consisted of the following Install(s): PSX\*2.0\*70

> Checking Install for Package PSX\*2.0\*70 Install Questions for PSX\*2.0\*70

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// GENERIC INCOMING TELNET

> PSX\*2.0\*70

> ────────────────────────────────────────────────────────────────────────────────

> Install Started for PSX\*2.0\*70 :

> Sep 27, 2011@12:22:32

> Build Distribution Date: Sep 27, 2011

> Installing Routines:

> Sep 27, 2011@12:22:32

> Updating Routine file... Updating KIDS files...

> PSX\*2.0\*70 Installed.

> Sep 27, 2011@12:22:32

> Not a production UCI

> NO Install Message sent

> ──────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

> Install Completed

# Section 3: Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Automatically Printing FDA Medication Guides is Optional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The FDA Medication Guide automatic printing functionality is an optional functionality. Each pharmacy division may choose to turn this functionality ON or OFF. Reasons a pharmacy division might choose to turn the FDA Medication Guide automatic printing functionality OFF are:

- FDA Medication Guides print on a different printer than the prescription labels. High-volume window prescription dispensing sites may not have the necessary resources for collating FDA Medication Guides with their corresponding prescription labels.
- Automated-dispensing systems such as Optfill also perform the prescription label printing, which usually happens at a later time than when the labels are printed in VistA. Since FDA Medication Guides automatically print at the same time labels print from VistA, medication guides may print too early in the dispensing process, causing confusion.

> To turn the FDA Medication Guide automatic printing functionality OFF or to not turn it ON for a specific pharmacy division, make sure the FDA MED GUIDE PRINT SERVER URL field has no value. This field can be edited via the Site Parameter Enter/Edit \[PSO SITE PARAMETERS\] option, as shown below.

> Note: Whether the functionality is being turned ON or OFF, the prescription label printed from VistA will still include the note “Read FDA Med Guide” when one is associated with the medication being dispensed.

> Example of Updating the FDA Med Guide Print Server URL Field

### Updating the WINDOWS NETWORK PRINTER NAME field (#75) in the DEVICE file (#3.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After installing all the patches from this project you must identify all the physical printers that will be used for printing FDA Medication Guide at your site. Once you have identified the printers that will be used at your site, please follow these steps to configure each printer in VistA for printing FDA Medication Guides:

1.  Identify the Windows Network Printer name for each printer that will be used for printing FDA Medication Guides (e.g., ‘-IXX- hp 4250 bld 2 room 350’). If you are having difficulty identifying the printer name, consult with your Windows system administrator.

> Note: Any printer used to print med guides must be defined as a local printer on the Windows server hosting the software. That is, the printer spooler must be hosted on the same server where the FDA Med Guides Printer Tool software is running.

> If you need to access a remote printer, you must still define it as a local printer spooler, but you can point to the remote printer by associating the port property to the remote printer’s UNC (Universal Naming Convention) path. For instance, port=\\serverName\printerName.

2.  Update the VistA DEVICE file (#3.5) with the printer Windows Network Name.
    1.  Select Device Management Application when you logon to VistA as shown below.

> Example of Selecting Device Management Application

2.  Select Device Edit Option.

> Example of Selecting Device Edit Option

3.  Select Edit All Device Fields Option.

> Example of Selecting Edit All Device Fields Option

4.  Select the Corresponding VistA Device ID for the Printer You’re Setting Up.

> If you are unable to find the printer on the current list of VistA devices, you must create a new entry for it. If the printer will not be used by VistA for anything else other than for printing FDA Medication Guides, all the non-required fields can be left blank.

> Example of Selecting Corresponding VistA Device ID

5.  Update the WINDOWS NETWORK PRINTER NAME field.

> Step through all the fields until you get to the WINDOWS NETWORK PRINTER NAME field for the device. You may also use the shortcut “^WINDOWS NETWORK PRINTER NAME” at any field in order to go straight to field you need to update.

> Example of Updating the Windows Network Printer Name Field

> Select DEVICE NAME:

### Updating the FDA MED GUIDE PRINT SERVER URL field (#134) in the OUTPATIENT SITE file (#59)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The next step is to configure the server address and port number for each site where the Java Application responsible for printing the FDA Medication Guides was installed, as shown below. You may also use the shortcut “^FDA MED GUIDE PRINT SERVER URL” to go straight to the field you need to update.

> Example of Updating the FDA Med Guide Print Server URL Field

### Updating the FDA MED GUIDE PRINTER Multiple (#135) in the OUTPATIENT SITE file (#59)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This step is optional. Sites can maintain a list of printers used for printing FDA Medication Guide for each Pharmacy Division. Also, one printer can be marked as ‘default’, which will be automatically selected when the user logs on to the division in the Outpatient Pharmacy application. The first screen capture shows how to update the list of printers while the second screen shows how the list of printers displays for the users when they log on to a Pharmacy Division.

> Example of Setting up FDA Medication Guide Printers for a Specific Pharmacy Division

> PLANO5\$PRT

> You may enter a new FDA MED GUIDE PRINTER, if you wish Enter the FDA Medication Guide printer for the division.

> Only devices with a Windows Network Printer Name are allowed.

> Answer with DEVICE NAME, or LOCAL SYNONYM, or \$I, or VOLUME SET(CPU), or SIGN-ON/SYSTEM DEVICE, or FORM CURRENTLY MOUNTED

> Do you want the entire DEVICE List? N

> Select FDA MED GUIDE PRINTER: FDA MED GUIDE PRINTER 1 ROOM 273 \_LTA9058:

> Are you adding 'FDA MED GUIDE PRINTER 1' as a new FDA MED GUIDE PRINTER (the 1ST for this OUTPATIENT SITE)? No// Y

> (Yes)

> DEFAULT PRINTER: ?

> Indicate whether the printer is the default FDA Medication Guide Printer for the division.

> Choose from:

> 1 YES

> DEFAULT PRINTER: Y YES

> Select FDA MED GUIDE PRINTER: FDA MED GUIDE PRINTER 2 OUTP PHARMACY Are you adding ' FDA MED GUIDE PRINTER 2' as a new FDA MED GUIDE PRINTER

> (the 2ND for this OUTPATIENT SITE)? No// Y (Yes)

> DEFAULT PRINTER:

> Select FDA MED GUIDE PRINTER:

> Example of How the List of Pr inters Configured Above Benefits the Outpatient Pharmacy User s Logging into a Specific Pharmacy Division.

> *(This page included for two-sided copying.)*