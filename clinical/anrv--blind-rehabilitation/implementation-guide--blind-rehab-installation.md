---
consolidated_title: "blind rehab installation/ implementation guide"
app_code: ANRV
doc_type: IG-IMP
master_source: "Blind Rehab Version 5 Installation/ Implementation Guide"
master_pub_date: May 2006
consolidated_from: 2 versions
prior_versions:
  - "Blind Rehab Version 5.1 Installation/ Implementation Guide"
---

![](blind-rehab-version-5-installation-implementation-guide/001.png)

BLIND REHABILITATION VistA

INSTALLATION/IMPLEMENTATION GUIDE

![](blind-rehab-version-5-installation-implementation-guide/002.png)

Version 5.0.26.8

May 2006

VistA Health System Design & Development

Revision History

| *Date* | *Description*                                                                       | *Author*                       |
|------------|-----------------------------------------------------------------------------------------|------------------------------------|
| 07/07/2005 | Initial documentation                                                                   | <span class="mark">REDACTED</span> |
| 08/05/2005 | Updated document 5.01                                                                   | <span class="mark">REDACTED</span> |
| 08/25/2005 | Updated document 5.02                                                                   | <span class="mark">REDACTED</span> |
| 09/08/2005 | Updated document 5.03                                                                   | <span class="mark">REDACTED</span> |
| 09/22/2005 | Revised document to include the Checklist created by <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 09/30/2005 | Updated document 5.04 to include guidance from feedback.                                | <span class="mark">REDACTED</span> |

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Benefits](#benefits)
  - [Enhanced Technology](#enhanced-technology)
- [Orientation](#orientation)
  - [Recommended Users](#recommended-users)
  - [Related Manuals](#related-manuals)
  - [Screen Displays and Text Notes](#screen-displays-and-text-notes)
  - [Documentation Retrieval](#documentation-retrieval)
  - [VistA Intranet](#vista-intranet)
- [Pre-Installation Information](#pre-installation-information)
  - [Target Audience](#target-audience)
  - [Test Sites](#test-sites)
  - [Hardware and Operating Systems Requirements](#hardware-and-operating-systems-requirements)
  - [M Server Requirements](#m-server-requirements)
  - [Client Workstation](#client-workstation)
  - [Network communications software](#network-communications-software)
  - [Software Installation Time](#software-installation-time)
  - [Name Space](#name-space)
  - [New Globals](#new-globals)
  - [VistA Software Requirements](#vista-software-requirements)
  - [Routine List](#routine-list)
  - [Options](#options)
  - [Security Keys](#security-keys)
  - [Parameter Definitions](#parameter-definitions)
  - [Remote Procedures](#remote-procedures)
  - [Skills Required to Perform the Installation](#skills-required-to-perform-the-installation)
  - [Pre-Installation Data Cleanup](#pre-installation-data-cleanup)
- [Installation Instructions](#installation-instructions)
  - [Connector Proxy and Application Proxy accounts](#connector-proxy-and-application-proxy-accounts)
  - [Load, Install, or Verify Dependencies are installed](#load-install-or-verify-dependencies-are-installed)
  - [Data Migration](#data-migration)
  - [Load and Install Blind Rehabilitation 5.0 KIDS Build on the M Server](#load-and-install-blind-rehabilitation-50-kids-build-on-the-m-server)
    - [Build Installation](#build-installation)
- [Implementation](#implementation)
  - [User Setup](#user-setup)
- [Addendum A – Installation Checklist](#addendum-a-installation-checklist)
  - [Introduction](#introduction-1)
  - [Pre Installation Activities](#pre-installation-activities)
  - [Installation Order](#installation-order)
    - [VistALink 1.5](#vistalink-15)
    - [KAAJEE](#kaajee)
    - [Person Service Lookup (PSL)](#person-service-lookup-psl)
    - [Patient Service Construct (PSC)](#patient-service-construct-psc)
    - [Blind Rehabilitation 5.0](#blind-rehabilitation-50)
    - [Post Installation Activities](#post-installation-activities)
- [Glossary/Acronym List](#glossaryacronym-list)
The Blind Rehabilitation (BR) V5.0 application provides enhanced tracking, and reporting, of the blind rehabilitation services provided to veterans by:
- Visual Impairment Service Teams (VIST)Coordinators
- Blind Rehabilitation Centers (BRCs)
- Blind Rehabilitation Outpatient Specialists (BROS)
- Visual Impairment Services Outpatient Rehabilitation (VISOR) Programs
- Visual Impairment Center to Optimize Remaining Sight (VICTORS)
Currently, there is no VistA software that meets the needs of the Blind Rehabilitation Centers or BROS and the VIST 4.0 package only monitors, tracks, and reports on a limited amount of data for the VIST.
The site-based VIST 4.0 package will be replaced with the re-hosted Blind Rehabilitation (BR) 5.0 application supporting the Health*<u>e</u>*Vet-VistA enterprise architecture. In addition to providing the base functionality of the VIST 4.0 system, BR 5.0 will provide a web-enabled GUI through which users can access enhanced capabilities intended for VIST Coordinators, new functionality for BROS, BRC personnel and waiting times and waiting list.
The Blind Rehabilitation 5.0 application will provide entirely new functionality that will encompass and integrate all five segments of the Blind Rehabilitation Services including waiting times and waiting list.

## Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Complies with Health*<u>e</u>*Vet-VistA Architecture
- Complies with 508 regulations, using W3C standards
- Accessible web based application, via a web browser
- Supports the OI Single Sign-on initiative
- User authentication via role based permissions
- User friendly
- Seamless continuum of care
- Minimum user disruption
- Simplified data entry
- Better identification and treatment of veterans
- Consolidates data
- Enables system driven waiting times and waiting list tracking and reporting capabilities
- Enables users to receive comprehensive views of a patient’s BR Services across institutions
- Facilitates data tracking and auditing capabilities
- Improves accountability
- Enhanced reporting features
- Provides Data Standardization which improves and provides consolidated data reporting
- Improved blind services tracking
- Enables Research and Provides Outcomes tracking and reporting capabilities
- Improves VHA organizational communication
- Transmits to the Health Data Repository

## Enhanced Technology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A single consolidated database and application will replace the current site-specific VIST 4.0 package
- Fulfills the congressional mandate on waiting times and waiting list calculations
- Electronic referral process to track patient applications for service
- Notifications feature to alert users of pending referrals
- Nationwide centralization of Blind Rehabilitation services data to allow nationwide reporting
- Ad-hoc reporting capabilities
- Secure Web Access (128 Bit SSL) from any authorized VA workstation
- Improved technology using web browser access and improved data security, via the VHA intranet
- Uses modern system architecture which allows for faster system enhancements
- Enhancements will be rolled out to all users at the same time ensuring consistent data
- Allows ability to track BR patient care access across institutions
- Patients can be referred to other institutions if they move without having to recreate patient data
- Patient lookup using the Health*<u>e</u>*Vet-VistA
- Patient lookup using Health*<u>e</u>*Vet-VistA Person Lookup Service (PSL) and Patient Service Construct (PSC)
- Standardized lookup tables using the Health*<u>e</u>*Vet-VistA Standard Data Service (SDS)
- Improved data integrity
- Minimize the maintenance and support required by IT support staff

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following staff is required for installing and supporting Blind Rehabilitation:

Information Resource Management System personnel (IRMS), Local Coordinators, and Enterprise VistA Support (EVS)

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation V. 5.0 Technical Manual/Security Guide

Blind Rehabilitation V. 5.0 Release Notes

Blind Rehabilitation V. 5.0 User Manual

Online Help is available from within the application

Pre-installation Information section provides information needed beforehand to install Blind Rehabilitation 5.0 KIDS build.

Installation Instructions section contains instructions and examples of Blind Rehabilitation 5.0 installation process.

Implementation Instructions provides directions for implementing Blind Rehabilitation software.

## Screen Displays and Text Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user’s response in this manual is in bold type, but does not appear on the screen as bold. The bold part of the entry is the letter or letters that you must type so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy. Every response you type must be followed by pressing the return key (or enter key for some keyboards). Whenever the return or enter key should be pressed, you will see the symbol \<Ret\>. This symbol is not shown but is implied if there is bold input.

Within the examples representing actual terminal dialogues, the author may offer information about the dialogue. You can find this information enclosed in brackets, for example, \[type your name here\], and will not appear on the screen.

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can find the documentation files for Blind Rehabilitation on the OI Field Office \[ANONYMOUS.SOFTWARE\] directories.

|                 |                   |                                                                              |                        |     |
|-----------------|-------------------|------------------------------------------------------------------------------|------------------------|-----|
| *File Name* | *Description* |                                                                              | *Retrieval Format* |     |
| ANRV5_0CIG.PDF  |                   | \* Blind Rehabilitation Centralized Server Installation/Implementation Guide | Binary                 |     |
| ANRV5_0VIG.PDF  |                   | \*\* Blind Rehabilitation VistA Installation/Implementation Guide            | Binary                 |     |
| ANRV5_0RN.PDF   |                   | Blind Rehabilitation Release Notes                                           | Binary                 |     |
| ANRV5_0TM.PDF   |                   | Blind Rehabilitation Technical Manual/Security Guide                         | Binary                 |     |
| ANRV5_0UM.PDF   |                   | Blind Rehabilitation User Manual                                             | Binary                 |     |

> \* This Installation Guide is only for Centralized Servers, not to be used at the field VistA site.

> \*\* This Installation/Implementation Guide is for field VistA sites.

## VistA Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product is available on the intranet at the following address:

<http://www.va.gov/vdl/>

This address takes you to the VistA Documentation Library (VDL), which has a listing of all the clinical software manuals. Click on the Visual Impairment Service Team (VIST) link and it will take you to the Blind Rehabilitation documentation.

The link below allows access to the Blind Rehabilitation home page:

<span class="mark">REDACTED</span>.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information contains recommendations and requirements for the pre-installation of the Blind Rehabilitation software.

The Blind Rehabilitation Application is run from a Centralized Application Server along with an Oracle database that also interfaces with the VistA servers running within the VA Intranet. The system uses both VistA and Oracle to store and retrieve data. The local sites will only need to setup the VistA portion of the software the centralized system is managed by a separate support team. Users access the system through a web based interface such as Internet Explorer using a provided link.

The Blind Rehabilitation KIDS build contains VistA software comprising of the following:

- M routines
- Options
- Keys
- RPC Broker Calls

## Target Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers of the Blind Rehabilitation Software must have a basic working knowledge of the systems to which they are administering and deploying applications. For M installations, the installer should have working knowledge of administering an M system.

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Blind Rehabilitation 5.0 software was tested at the Bay Pines Test Lab and at the following VistA test sites:

|                                                 |                    |                               |
|-------------------------------------------------|--------------------|-------------------------------|
| *Test Sites*                                | *Beta Cycle I* | *Beta Cycle II (Go Live)* |
| Augusta                                         | X                  | X                             |
| VA Puget Sound Health Care System               |                    | X                             |
| Southern Arizona VA Health Care System (Tucson) | X                  | X                             |
| Hines VA Medical Center Chicago                 | X                  | X                             |

## Hardware and Operating Systems Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before performing the installation of the Blind Rehabilitation Software, certain environmental requirements for both the M server and the client workstation must be satisfied. These requirements are described below.

## M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools are required on your M server in order to install and use Blind Rehabilitation 5.0:

One of the following operating systems:

- Cache’/NT: Cache’ (version 3.2.31.1 or greater)
- Cache’/VMS: Cache’ (version 4.1 or greater)

Network communications software:

- TCP/IP
- VistALink Listener Port

## Client Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use the Blind Rehabilitation System, the following minimum hardware and software tools are required on your client workstation:

- 80x86-based client workstation. For additional workstation requirements refer to the VA workstation hardware requirements.

Software Requirements:

- Windows XP 32-bit operating system
- Web Browser: Microsoft Internet Explorer version 5.0 or higher with High Encryption (128 bit) and JavaScript enabled.
- Adobe Acrobat version 5.1 or higher with browser plug-in enabled.

## Network communications software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Blind Rehabilitation System requires networked client workstations running TCP/IP.

## Software Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of this software will not affect users on the system. Therefore, there is no need for log on to be disabled. The estimated installation time is 10 minutes during off peak hours.

## Name Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Blind Rehabilitation software name space is ANRV.

## New Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new Globals are created on the VistA system.

## VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the installation of Blind Rehabilitation 5.0, the following packages must be installed and fully patched. The Installation Checklist provided in Addendum A of this document is organized in a step-wise manner to assist in loading any missing or new package/patch in the correct order.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 29%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>Software</strong></em></th>
<th><em><strong>Version</strong></em></th>
<th><em><strong>Required Patches</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel</td>
<td>V. 8</td>
<td><p>XU*8*238</p>
<p>XU*8*265</p>
<p>XU*8*284</p>
<p>XU*8*309</p>
<p>XU*8*337</p>
<p>XU*8*361</p>
<p>XU*8*325</p>
<p>XU*8*343</p>
<p>XU*8*329 (Kernel Authentication &amp; Authorization for J2EE Weblogic)</p></td>
</tr>
<tr class="even">
<td>Kernel Toolkit</td>
<td>V. 7.3</td>
<td><p>XT*7.3*89</p>
<p>XT*7.3*67</p></td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td>V. 22</td>
<td></td>
</tr>
<tr class="even">
<td>VistALink</td>
<td>V. 1.5 (XOBU 1.5)</td>
<td></td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td>V. 1.1</td>
<td></td>
</tr>
<tr class="even">
<td>TIU</td>
<td>V. 1.0</td>
<td></td>
</tr>
<tr class="odd">
<td>OERR</td>
<td>V. 3.0</td>
<td></td>
</tr>
<tr class="even">
<td>Registration</td>
<td>V. 5.3</td>
<td><p>DG*5.3*538 (Person Service Lookup)</p>
<p>DG*5.3*615 (Person Service Lookup)</p>
<p>DG*5.3*620 (Person Service Lookup)</p>
<p>DG*5.3*557 (Patient Services)</p></td>
</tr>
</tbody>
</table>

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">The following list contains the routines included in Blind Rehabilitation 5.0. Since they are new routines, they are Post-install values.</span>

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<tbody>
<tr class="odd">
<td><em><strong>Routine</strong></em></td>
<td><em><strong>Checksum Values</strong></em></td>
</tr>
<tr class="even">
<td><mark>ANRVJ1</mark></td>
<td><p><mark>CHECK1^XTSUMBLD value = 5515859</mark></p>
<p><mark>CHECK^XTSUMBLD value = 1321780</mark></p></td>
</tr>
<tr class="odd">
<td><mark>ANRVJP</mark></td>
<td><p><mark>CHECK1^XTSUMBLD value = 873634</mark></p>
<p><mark>CHECK^XTSUMBLD value = 602697</mark></p></td>
</tr>
</tbody>
</table>

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These options are either being sent to be added to the option file so that users may access the Blind Rehabilitation V5 software (ANRVJ_BLINDREHAB), or they are being deleted at the site to prevent users from editing VIST 4.0 files that have been migrated to the new system. Options that allow read only access to the VIST 4.0 systems data will remain intact but should only be used for reviewing legacy data.

| *Name*                     | *Status*   |
|--------------------------------|----------------|
| ANRVJ_BLINDREHAB               | SEND TO SITE   |
| ANRV DELETE REFERRAL           | DELETE AT SITE |
| ANRV DELETE ROSTER             | DELETE AT SITE |
| ANRV EDIT VIST OPTIONS         | DELETE AT SITE |
| ANRV ENTER/EDIT CHECKLIST      | DELETE AT SITE |
| ANRV ENTER/EDIT INACTIVE VIST  | DELETE AT SITE |
| ANRV ENTER/EDIT REFERRAL       | DELETE AT SITE |
| ANRV ENTER/EDIT VARO CLAIMS    | DELETE AT SITE |
| ANRV ENTER/EDIT VIST LETTER    | DELETE AT SITE |
| ANRV ENTER/EDIT VIST PARAMETER | DELETE AT SITE |
| ANRV ENTER/EDIT VIST PATIENT   | DELETE AT SITE |
| ANRV EYE DIAG NARRATIVE        | DELETE AT SITE |
| ANRV PATIENT REVIEW            | DELETE AT SITE |

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following security keys are being sent to the site and are used by the KAAJEE software to add enhanced ‘Strong’ security to the Blind Rehabilitation system for users.

| *Name*                                                                         | *Status* |
|------------------------------------------------------------------------------------|--------------|
| ANRVADMINROLE (this should only be given to users requiring Administration rights) | SEND TO SITE |
| ANRVUSERROLE (all users of the Blind Rehabilitation system will require this key)  | SEND TO SITE |

## Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following definitions are being sent to the site to maintain server and client version integrity.

| *Name*                                                   | *Status* |
|--------------------------------------------------------------|--------------|
| ANRV GUI VERSION (maintains current version loaded in VistA) | SEND TO SITE |

## Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Remote Procedures

| *Name*            | *Function*                                                                                       | *Status* |
|-----------------------|------------------------------------------------------------------------------------------------------|--------------|
| ANRV CREATE ENCOUNTER | Used to set globals prior to calling the DATA2PCE API                                                | SEND TO SITE |
| ANRV PROBLEM LIST     | Displays Active, Inactive or All patient problems                                                    | SEND TO SITE |
| ANRVJ1_RPC_MAIN       | This is the main RPC entry point and is used to execute a variety of tags within the ANRVJ1 routine. | SEND TO SITE |

## Skills Required to Perform the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions for performing the needed functions are provided in the vendor-supplied operating system manuals as well as VistA publications.

You need to know how to do the following:

1.  Copy files using commands of the host file system.
2.  Load routines from: diskettes, tapes, and/or host files.

## Pre-Installation Data Cleanup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to data migration, the data migration team will test the data from the VIST 4.0 system. If missing or inconsistent data exists, the site will need to correct the data prior to installation of Blind Rehabilitation 5.0. If VIST 4.0 is not loaded at your site, you can skip this portion of the installation.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the Blind Rehabilitation System is a three-part process involving your client workstation, VistA, and connection via the application server to the VistA databases. Each part of the installation consists of a few basic steps that are described below.

## Connector Proxy and Application Proxy accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Connector Proxy: The Connector Proxy user account is a non-interactive user account that has no menus. An established Connector Proxy user account is necessary to maintain a connection between the J2EE Application Server using a connection pool and the VistALink server port. When users connect to the Blind Rehabilitation system they are given a connection from the connection pool but must authenticate with their access and verify code using KAAJEE to interact with the VistA system. For more information regarding Connector Proxy setup, please refer to the VistALink 1.5 Installation Guide.

Application Proxy: This is an application specific user account that allows the Blind Rehabilitation software to perform background tasks required by the centralized application. Tasks such as updating patient demographic information between the MPI and the VistA server are performed without necessitating user intervention. These tasks are limited to specific remote procedure calls and are used only for reading data. The application proxy user account is created during the installation of the Blind Rehabilitation KIDS build.

## Load, Install, or Verify Dependencies are installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Blind Rehabilitation System requires that several dependencies be in place prior to the installation of the Blind Rehabilitation VistA package (ANRV_5_0.KIDS). Refer to the Installation Checklist provided in Addendum A of this document for load order. For detailed information on any patch or package, please refer to the documentation for the specific package and or patch. This information is not a replacement for the package or patch documentation. The packages and patches required are listed below:

> VistALink XOBU 1.5

> KAAJEE V1 (Kernel Authentication & Authorization for J2EE)

> PSL V4 (Person Service Lookup)

> PSC V2 (Patient Service Construct)

## Data Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Implementation team will work with your site to help cleanup any data migration issues found during preliminary extracts of VIST 4.0 data at your site. They will also coordinate the activities of shutting down the VIST 4.0 options to Enter/Edit data. The installation of the Blind Rehabilitation KIDS build (ANRV_5_0.KID) will delete the Enter/Edit options from VIST 4.0. At that time, users should not enter/edit data in the VIST 4.0 software and they should await notification to begin using Blind Rehabilitation 5.0. If a site has locally created VIST 4.0 options that allow the Enter/Edit of data in VIST 4.0 then these will need to be put out of order. The sites will still have the ability to generate reports from VIST 4.0 at this point however, the data left in VIST 4.0 is considered legacy data. The HDR team will do a final extract of VIST 40 data after the Blind Rehabilitation 5.0 KIDS build ANRV_5_0.KID is installed at the site. No further extracts will be done at the site after this occurs. Once the data extract is complete, the data is loaded in the new system during data migration and the user will then enter/edit data in the new Blind Rehabilitation 5.0 system. Below are the options that are deleted by the ANRV_5_0.KIDS build:

- ANRV DELETE REFERRAL                           
- ANRV DELETE ROSTER                           
- ANRV EDIT VIST OPTIONS                        
- ANRV ENTER/EDIT CHECKLIST                
- ANRV ENTER/EDIT INACTIVE VIST           
- ANRV ENTER/EDIT REFERRAL                
- ANRV ENTER/EDIT VARO CLAIMS           
- ANRV ENTER/EDIT VIST LETTER            
- ANRV ENTER/EDIT VIST PARAMETER     
- ANRV ENTER/EDIT VIST PATIENT            
- ANRV EYE DIAG NARRATIVE                  
- ANRV LETTER MENU                              
- ANRV PATIENT REVIEW                          

## Load and Install Blind Rehabilitation 5.0 KIDS Build on the M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the steps in this section to install the Blind Rehabilitation ANRV_5_0.KIDS build. The globals for this build will not be loaded until the dependant packages and patches listed above have been installed.

<u>NOTE</u>: Do not install the ANRV_5_0.KIDS build until instructed to do so by the implementation manager. An implementation manager will contact the site and provide instructions for downloading the ANRV_5_0.KIDS package and installation documentation. This is a controlled distribution since after install of the package users will not have Enter/Edit capability in the VIST 4.0 software. Once the ANRV_5_0.KIDS build is installed, the legacy VIST 4.0 system will be unusable. To prevent extended downtime for VIST 4.0 users please wait until the implementation manager has given your site a date to install.

### Build Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use the KIDS Installation option; Load A Distribution \[XPD LOAD DISTRIBUTION\]. Enter ‘ANRV_5_0.KID’ as the name of the Host File. This will load the transport globals contained in the distribution: BLIND REHABILITATION 5.0, which contains the Routines, Remote Procedures, and Options necessary to run Blind Rehabilitation 5.0.
2.  You can run the KIDS Installation option, Verify Checksums in Transport Global \[XPD PRINT CHECKSUM\]. This option will ensure the transport global was not corrupted in transit. Use ‘Blind Rehabilitation V5.0’ as the response to the Select INSTALL NAME prompt.
3.  Follow the example below:

Step 1 Load the distribution

Select Installation Option: 1 Load a Distribution

Enter a Host File: \<Location of file\>ANRV_5_0_KID

KIDS Distribution saved on Jun 27, 2005@11:43:49

Comment: BLIND REHABILITATION V5.0

This Distribution contains Transport Globals for the following Package(s):

BLIND REHABILITATION 5.0

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

BLIND REHABILITATION 5.0

Use INSTALL NAME: BLIND REHABILITATION 5.0 to install this Distribution.

Step 2 Verify Checksums

Select Installation Option: VERIFY Checksums in Transport Global

Select INSTALL NAME: BLIND REHABILITATION 5.0 Loaded from Distribution

Loaded from Distribution 7/20/05@15:46:19

=\> BLIND REHABILITATION V5.0 ;Created on Jun 27, 2005@11:43:49

This Distribution was loaded on Jul 20, 2005@15:46:19 with header of

BLIND REHABILITATION V5.0 ;Created on Jun 27, 2005@11:43:49

It consisted of the following Install(s):

BLIND REHABILITATION 5.0

2 Routine checked, 0 failed.

  
Step 3 Install the KIDS build

Install using XPD install option

Select INSTALL NAME: BLIND REHABILITATION 5.0 Loaded from Distribution

Loaded from Distribution 7/1/05@11:23:36

=\> BLIND REHABILITATION V5.0 ;Created on Jun 27, 2005@11:43:49

This Distribution was loaded on Jul 01, 2005@11:23:36 with header of

BLIND REHABILITATION V5.0 ;Created on Jun 27, 2005@11:43:49

It consisted of the following Install(s):

BLIND REHABILITATION 5.0

Checking Install for Package BLIND REHABILITATION 5.0

Install Questions for BLIND REHABILITATION 5.0

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// CONSOLE

BLIND REHABILITATION 5.0

Installing SECURITY KEY

Installing REMOTE PROCEDURE

Installing OPTION

Jul 01, 2005@11:28:49

Running Post-Install Routine: ^ANRVJP

Added new Application Proxy User 'ANRVAPPLICATION,PROXY USER'.

Updating Routine file

Updating KIDS files

BLIND REHABILITATION 5.0 Installed.

Jul 01, 2005@11:28:49

Install Message sent \#29

100%

Complete

Install Completed

# Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## User Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Connector Proxy M Account</u>

If your site has not created a Connector Proxy then use the Kernel Tool to create the Connector Proxy M Account for J2EE applications to use. Instructions for setup of this M account are provided in the VistALink Installation Guide 1.5.

The VistA/M system manager is the only one who can grant access to incoming VistALink connections from a J2EE system. Using the Foundations Management menu, create a Connector Proxy user account using the Enter/Edit Connector Proxy option. The system manager must have the XUMGR security key and the Foundations Management option.

1.  Below is a sample of an existing connector proxy for blind rehab.

> From the Foundations Management menu, select the option CP Enter/Edit Connector Proxy User:

> SP Site Parameters SL Start Listener

> CFG Manage Configurations STP Stop Listener

> CP Enter/Edit Connector Proxy User SB Start Box

> RE Refresh CU Clean Up Log

> SS System Status

> Select Action: Quit// CP Enter/Edit Connector Proxy User

> Enter NPF CONNECTOR PROXY name: CONNECTOR,HINES EMC

> Want to edit ACCESS CODE (Y/N): Y

> Enter a new ACCESS CODE \<Hidden\>: \*\*\*\*\*\*\*

> Please re-type the new code to show that I have it right: \*\*\*\*\*\*\*\*\*

> Want to edit VERIFY CODE (Y/N):

> Please re-type the new code to show that I have it right: \*\*\*\*\*\*\*\*\*

> PRIMARY MENU OPTION: \<NONE\>

2.  You must provide the Access and Verify codes to the EMC using PKI. Information on securely sending this information will be sent to the site ISO.
3.  This account requires no Primary Menu Options since the account will only be used for the application server to maintain a connection to the server to provide users of Blind Rehabilitation a connection from the connection pool. The Verify Code for this account is set to not expire.

<u>  
Edit Blind Rehabilitation Users (VistA)</u>

Users and System Administrators will need the following Secondary Menu option and the appropriate Security Key to use the Blind Rehabilitation 5.0 software.

> Secondary Menu

- ANRVJ_BLINDREHAB (Blind Rehabilitation)
- DGRR GUI PATIENT LOOKUP (GUI Patient Lookup RPC access)
- DGRR PATIENT SERVICE QUERY (Patient Service Query)
- XUS KAAJEE WEB LOGON (KAJEE BROKER CONTEXT)

Security Key

- ANRVUSERROLE (This needs to be given to all users of Blind Rehab)
- ANRVADMINROLE (This should be given only to users who will be administrators)

The implementation managers will setup the users within the Blind Rehabilitation System during installation. After the initial installation, user-administrators will take over adding new staff to the system. The Blind Rehabilitation Central Office and the site must communicate with the implementation manager and construct a complete list of users (with their Roles and Institutions) who require access to the Blind Rehabilitation application.

The deployment team will provide further setup information and the link to the Blind Rehabilitation application.

<u>At this point, the VistA installation of Blind Rehabilitation is complete</u><u>This portion applies to system administrators and the deployment team</u><u>Refer to the Blind Rehabilitation User Manual 5.0 under the Administration Menu section for instructions to Enter New Users in the Blind Rehabilitation system</u>

# Addendum A – Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation depends on new Health*<u>e</u>*Vet-VistA services and API’s from packages and patches that must be available prior to the installation of Blind Rehabilitation. The dependant applications that must be installed are KAAJEE (Kernel Authentication & Authorization for J2EE), VistALink 1.5, PSL (Person Service Lookup), PSC (Patient Service Construct) and finally Blind Rehabilitation 5.0. The checklists below contain installation information and summary checklists to assist in loading all VistA software required to use Blind Rehabilitation. The system being updated may require additional patches not listed in this document.

<u>NOTE:</u> This checklist is a supplement or a quick guide and doesn’t replace the more detailed guidance offered by the main Installation Guides for KAAJEE, VistALink 1.5, PSL, PSC and Blind Rehabilitation 5.0.

## Pre Installation Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To ensure a successfully configured Blind Rehabilitation 5.0 system, complete the items below prior to the install of the VistA KIDS builds.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 48%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>Complete Y/N</strong></em></th>
<th><em><strong>Activity</strong></em></th>
<th><em><strong>Assigned to</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Prior to data migration, the data from VIST 4.0 will be tested by the data migration team and any inconsistencies must be corrected to ensure a clean data migration from VIST 4.0 to Blind Rehabilitation 5.0. If you do not have VIST 4.0 data to be migrated then this step can be skipped.</td>
<td><p>Data Migration Contact:</p>
<p>________________________</p></td>
</tr>
<tr class="even">
<td></td>
<td>Inform any users of VIST 4.0 that the data from VIST 4.0 is to be migrated on the date that the install for Blind Rehabilitation 5.0 is performed. Let users of the VIST 4.0 system know that once the data migration occurs and Blind Rehabilitation 5.0 is installed that there will be no further ability to enter or edit VIST patients in the legacy system.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Review this checklist prior to installation and if you have any questions then please refer to the associated package documentation or contact the implementation team. This checklist is provided as a condensed installation guide to assist sites in the installation of Blind Rehabilitation 5.0 and the dependant applications required to run this application and future Health<em><u>e</u></em>Vet-VistA software.</td>
<td></td>
</tr>
</tbody>
</table>

## Installation Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is presented in the sequence that each dependant application has to be installed. Each dependant application may have additional patch requirements. The sections and load order are as follows:

1.  VistALink 1.5
2.  KAAJEE
3.  Person Service Lookup
4.  Patient Service Construct
5.  Blind Rehabilitation 5.0

This checklist is a supplement or a quick guide and doesn’t replace the more detailed guidance offered by the main Installation Guides for VistALink 1.5, KAAJEE, PSL, PSC and Blind Rehabilitation 5.0. Refer to those documents for further information.

### VistALink 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System Requirements:

| *Installed Y/N* | *Package*      | *Patch*  |
|---------------------|--------------------|--------------|
|                     | Kernel 8.0         | XU\*8.0\*265 |
|                     |                    | XU\*8.0\*337 |
|                     |                    | XU\*8.0\*361 |
|                     | Kernel Toolkit 7.3 | XT\*7.3\*89  |

Installation Instructions:

1.  Install Kernel and Kernel Toolkit patches
2.  Remove any VistALink users (e.g., Care Management clients) from the system. Check the System Status for any XOBVSKT routines. If you find any of these jobs running on the system, notify the users to logoff or FORCEX the jobs. Active users may receive NOSOURCE or CLOBBER errors.
3.  Disable the VLINK TCPIP service in VMS
4.  Install VistALink 1.5 (XOBU 1.5, Distributed as XOB_1_5.KID)
5.  Enable the VLINK TCPIP service in VMS
6.  Ensure you have:
- Created one Connector Proxy User on your VistA/M system for use by the J2EE application servers at the Hines EMC data center. These servers host the Health*<u>e</u>*Vet-VistA Blind Rehabilitation 5.0 application and require the Connector Proxy User account to execute RPC’s on your VistA/M system; and
- Securely communicated the credentials (Access/Verify codes) assigned to this Connector Proxy User account to the appropriate personnel at the Hines EMC.
- To create the Connector Proxy user you must have the XUMGR key:
- Use the Foundations Management menu and enter CP for the Enter/Edit Connector Proxy User.
- Enter the user name for the connector proxy user the name CONNECTOR, HINES EMC is recommended for this user.
- Enter an Access Code for this user account.
- Enter a Verify Code for this user account.
- DO NOT GIVE THIS USER ACCOUNT ANY MENUS. This user account is only for the Connection pool located on the J2EE application server.

### KAAJEE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System Requirements:

Required patches for this software are included in previous installs and not listed here.

| Installed Y/N | Package        | Patch                                                                           |
|---------------|----------------|---------------------------------------------------------------------------------|
|               | Kernel XU\*8.0 | XU\*8.0\*329 (KAAJEE - Kernel Authentication & Authorization for J2EE WebLogic) |

### Person Service Lookup (PSL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System Requirements:

| Installed Y/N | Package              | Patch                                |
|---------------|----------------------|--------------------------------------|
|               | Kernel XU\*8.0       | XU\*8.0\*325                         |
|               | Registration DG\*5.3 | DG\*5.3\*538 (Person Service Lookup) |

### Patient Service Construct (PSC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System Requirements:

| Installed Y/N | Package         | Patch                          |
|---------------|-----------------|--------------------------------|
|               | Registration DG | DG\*5.3\*557(Patient Services) |

### Blind Rehabilitation 5.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>NOTE</u>: Sites should not continue with this step until they are notified by the implementation team since it will shutdown VIST 4.0.

System Requirements:

Below is the summary of the package implementation for Blind Rehabilitation 5.0 distributed as ANRV_5_0.KID. See the previous sections for dependant/required patch and packages.

| Installed Y/N | Package                                               | Distribution | Patch/Package                                                                                                                             |
|---------------|-------------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------|
|               | Blind Rehabilitation 5.0                              | ANRV_5_0.KID | ANRV\*5.0 This is the build required to run Blind Rehabilitation 5.0                                                                      |
|               | Data Migration/Conversion to Blind Rehabilitation 5.0 |              | Data Migration activities will occur at this point. This step can be skipped for sites that don’t contain data for the VIST 4.0 software. |

### Post Installation Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Setup:

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Complete Y/N</th>
<th>Step</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Provide Connector Proxy information from VistALink installation above to the Blind Rehabilitation deployment team at Hines EMC.</td>
</tr>
<tr class="even">
<td></td>
<td><ol type="1">
<li><p>Add secondary menu to Blind Rehabilitation 5.0 VistA User Accounts:</p>
<ol type="a">
<li><p>Blind Rehab/VIST 5.0 [ANRVJ_BLINDREHAB]</p></li>
</ol></li>
</ol></td>
</tr>
<tr class="odd">
<td></td>
<td><ol start="2" type="1">
<li><p>Add Security Keys to Blind Rehabilitation 5.0 VistA User Accounts:</p>
<ol type="a">
<li><p>ANRVUSERROLE is necessary for all Users of the system.</p></li>
<li><p>ANRVADMINROLE is necessary for all Administrators of the system.</p></li>
</ol></li>
</ol></td>
</tr>
<tr class="even">
<td></td>
<td><ol start="3" type="1">
<li><p>Add users to the Blind Rehabilitation application. This can only be done by users who have been designated as Blind Rehabilitation System Administrators. If you are not authorized to do this then a list of users must be sent to the System Administrator to have new users added to the system.</p></li>
</ol></td>
</tr>
</tbody>
</table>

  
Workstation Software Requirements:

- Web Browser: Microsoft Internet Explorer version 5.0 or higher with High Encryption (128 bit) JavaScript and Accept Cookies must be enabled.
- Adobe Acrobat Reader version 5.1 or higher with browser plug-in enabled.Workstation Hardware Requirements and Guidelines:
- Refer to VA workstation hardware requirements.Provide Link to Blind Rehabilitation:

At this point users may access the system. Users can access the system by entering the URL Web Address in their browser <span class="mark">REDACTED</span>. It is recommended that sites provide a desktop link containing the URL and add a link to the users Favorite Links in Internet Explorer or the link can be set as the default link within the Internet Browser. Sites may also provide a link to the application using the GUI Tools menu in CPRS, for information on adding these links to the GUI Tools Menu, please refer to CPRS documentation.

# Glossary/Acronym List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| *Term/Acronym*                                | *Description*                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AAA                                               | (Veteran Health Administration) Authentication, Authorization and Accountability Standards                                                                                                                                                                                                                                                                                                                                                                                  |
| AAIP                                              | Authentication and Authorization Infrastructure Program                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ADPAC                                             | Automated Data Processing Application Coordinator                                                                                                                                                                                                                                                                                                                                                                                                                           |
| AMIS                                              | Automated Management Information System                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| API                                               | Application Program Interface                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Audit Trail                                       | A history of the changes made to a record including old data, new data, and the name of the user who made the change. Record of access and modifications                                                                                                                                                                                                                                                                                                                    |
| BCMA                                              | Bar Code Medication Administration. A VistA software application that validates medications against active orders before the medication is given to the patient.                                                                                                                                                                                                                                                                                                            |
| BR                                                | Blind Rehabilitation Project                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Blind Rehabilitation Center (BRC)                 | A residential inpatient program that provides comprehensive adjustment to blindness training and serves as a resource to a catchments area usually comprised of multiple Veterans Integrated Service Networks (VISN).                                                                                                                                                                                                                                                       |
| BRC Application Letter                            | This is a cover letter for a Blind Rehabilitation Center (BRC) Application packet. This letter requires editing and is used to print for individual veterans.                                                                                                                                                                                                                                                                                                               |
| BRC Follow-up Letter                              | This is a questionnaire sent to the veteran following blind rehabilitation training. It is used to assist the center or clinic in following-up on the veteran.                                                                                                                                                                                                                                                                                                              |
| Blind Rehabilitation Outpatient Specialist (BROS) | Blind Rehabilitation instructors possessing advanced technical knowledge and competencies in at least two Blind Rehabilitation disciplines at the journeyman level.\[2\]                                                                                                                                                                                                                                                                                                    |
| CAT                                               | Computer Access Training                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| CARF                                              | Commission on the Accreditation of Rehabilitative Facilities                                                                                                                                                                                                                                                                                                                                                                                                                |
| CCOW                                              | Clinical Context Object Work Group                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| CCOW Term Telnet                                  | An application (written in Delphi) which is Remote Procedure Call (RPC) Broker aware and capable of CCOW with CCOW, which can be used to access the Roll and Scroll environment, such as List Manager, in VistA.                                                                                                                                                                                                                                                            |
| CCOW Timing Program                               | A program, written in Delphi that tests the amount of time for Remote Procedure Calls to be processed by the server.                                                                                                                                                                                                                                                                                                                                                        |
| CHISS                                             | Common Health Information Security Services                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C&P                                               | Compensation & Pension                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Claim Letter                                      | This is a cover letter to a Veterans Administration Regional Office (VARO) when filing a claim on behalf of a VIST veteran. This letter is used to print for individual veterans.                                                                                                                                                                                                                                                                                           |
| Common Procedure Terminology (CPT)                | A method for coding procedures performed on a patient, for billing purposes.                                                                                                                                                                                                                                                                                                                                                                                                |
| CPRS                                              | A VistA software application that provides an integrated patient record system for use by clinicians, managers, quality assurance staff, and researchers                                                                                                                                                                                                                                                                                                                    |
| CPRS/CCR                                          | Computerized Patient Record System/Computerized Clinical Reminder Module                                                                                                                                                                                                                                                                                                                                                                                                    |
| CPRS/VSM                                          | Computerized Patient Record System/Vital Signs Module                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Computerized Patient Record System (CPRS)         | A clinical record system, which integrates many VistA packages to provide a common entry and data retrieval point for clinicians and other hospital personnel. (CPRS). CPRS is a Veterans Health Information Systems and Technology Architecture (VistA) software application that enables clinicians, nurses, clerks, and others to enter, review, and continuously update all information connected with patients.                                                        |
| Context Vault                                     | Data store that houses user sign-on credentials in a CCOW user context.                                                                                                                                                                                                                                                                                                                                                                                                     |
| DaIS                                              | Development and Infrastructure Support                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DBIA                                              | Data Base Integration Agreement                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DELPHI                                            | A Rapid Application Development (RAD) system/application developed by Borland International, Inc. Delphi is similar to Visual Basic from Microsoft, but whereas Visual Basic is based on the BASIC programming language, Delphi is based on Pascal.                                                                                                                                                                                                                         |
| Division                                          | The subunit under institute has 5-6 digits/letter division ID and less than a 35 character name                                                                                                                                                                                                                                                                                                                                                                             |
| EJB                                               | Enterprise Java Bean                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Encounter                                         | A contact between a patient and a provider who has the primary responsibility of assessing and treating the patient. A patient may have multiple encounters per visit. Outpatient encounters include scheduled appointments and walk-in unscheduled visits. A clinician’s telephone communications with a patient may be represented by a separate visit entry. If the patient is seen in an outpatient clinic while an inpatient, this is treated as a separate encounter. |
| Episode of Care                                   | An interval of care by a health care facility or provider for a specific medical problem or condition. It may be continuous or it may consist of a series of intervals marked by one or more brief separations from care, and can also identify the sequence of care (e.g., emergency, inpatient, outpatient), thus serving as one measure of health care provided.                                                                                                         |
| FSOD                                              | Functional Status Outcomes Database                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Graphical User Interface (GUI)                    | A type of display format that enables users to choose commands, initiate programs, and other options by selecting pictorial representations (icons) via a mouse or a keyboard.                                                                                                                                                                                                                                                                                              |
| HCFA                                              | Health Care Financing Administration                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| HCPCS                                             | HCFA Common Procedure Coding System                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| HFS                                               | Host File Server is a system (WinNT/Dec Alpha) file access mechanism that enables the M software (server software) to access the system-level files.                                                                                                                                                                                                                                                                                                                        |
| Health*<u>e</u>*Vet-Vist*A*                       | The Health*<u>e</u>*Vet-VistA architecture will be a services-based architecture. Applications will be constructed in tiers with distinct user interface, middle and data tiers. Two types of services will exist, core services (infrastructure and data) and application services (a single logical authoritative source of data).                                                                                                                                        |
| HIPAA                                             | Health Insurance Portability and Accountability Act of 1996. Also referred to as, HIPAA.                                                                                                                                                                                                                                                                                                                                                                                    |
| HL7                                               | Health Level Seven                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| HSD&D                                             | Health Systems Design & Development                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| HSM                                               | Hospital-Supplied Self Medication                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| HTTP                                              | Hyper Text Transfer Protocol                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| HTTPS                                             | Secured HTTP Protocol                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ICD9                                              | International Classification of Diseases 9<sup>th</sup> Edition                                                                                                                                                                                                                                                                                                                                                                                                             |
| ICN                                               | Identification Control Number                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| IDL                                               | Iterative Development Lifecycle                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| IE                                                | Internet Explorer                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| IEN                                               | Internal Entry Number                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Independent Verification and Validation (IV&V)    | The IV&V team supports the HSD&D mission by promoting standardization, improving software release quality and effectiveness of healthcare delivery through planned and controlled evaluation, testing, and integration of healthcare information systems. Visit the http://vista.med.va.gov/ivv/ site for additional information.                                                                                                                                           |
| Inpatient Visit                                   | The admission of a patient to a VAMC and any clinically significant change related to treatment of that patient. For example, a treating specialty change is clinically significant, whereas a bed switch is not. The clinically significant visits created throughout the inpatient stay would be related to the inpatient admission visit. If the patient is seen in an outpatient clinic while an inpatient, this is treated as a separate encounter.                    |
| Institution                                       | A major hospital with subdivisions, usually has a name \< 30 letters and a three-digit division ID                                                                                                                                                                                                                                                                                                                                                                          |
| Invitation for VIST Review                        | This is an invitation to blinded veterans from VIST, offering a health evaluation. Veterans may accept or deny the invitation. This letter satisfies the requirements of M-2, Part XXIII and is meant to be printed as a mass mailing.                                                                                                                                                                                                                                      |
| IP                                                | Meds Inpatient Medications                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IRM                                               | Information Resources Management                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| IRS Exemption Letter                              | This letter advises the Internal Revenue Service of legally blind status of veterans. This letter requires editing and is to be printed for individual veterans.                                                                                                                                                                                                                                                                                                            |
| ISO                                               | Information Security Officer                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ISSRA                                             | Interim Security Services for Rehosted Applications                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Iterative Development                             | The technique used to deliver the functionality of a system in a successive series of releases of increasing completeness. Each iteration is focused on defining, analyzing, designing, building, and testing a set of requirements.                                                                                                                                                                                                                                        |
| IV                                                | Intravenous                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| J2EE                                              | The Java 2 Platform, Enterprise Edition (J2EE) is an environment for developing and deploying enterprise applications. The J2EE platform consists of a set of services, APIs, and protocols that provide the functionality for developing multi-tiered, Web-based applications.                                                                                                                                                                                             |
| JAAS                                              | [Java Authentication and Authorization Service. For more information refer to the JAAS Web site at the following address: http://java.sun.com/products/jaas/index-14.html](http://java.sun.com/products/jaas/index-14.html)                                                                                                                                                                                                                                                 |
| JAVA                                              | Java is a programming language. It can be used to complete applications that may run on a single computer or be distributed among servers and clients in a network.                                                                                                                                                                                                                                                                                                         |
| JCAHO                                             | Joint Commission on the Accreditation of Health Care Organizations                                                                                                                                                                                                                                                                                                                                                                                                          |
| JDBC                                              | Java Database Connection                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| JSP                                               | Java Server Page                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Kernel                                            | Set of VistA software routines that function as an intermediary between the host operating system/application and the VistA application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying M implementation.                                                                                                                                    |
| Kiosk                                             | Public workstations shared by multiple users.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| List Manager                                      | A VistA software product that creates a framework for user actions. List Manager is part of the VistA software infrastructure.                                                                                                                                                                                                                                                                                                                                              |
| LOINC                                             | Logical Observation Identifier Names and Codes                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MAH                                               | Medication Administration History                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MAS                                               | Medical Administration Service                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MH Assistant                                      | Mental Health Assistant                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MST                                               | Military Sexual Trauma                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| MTAS                                              | Middle Tier WebLogic Application Server                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MVC                                               | Model View Controller                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| New Person (#200) File                            | A VistA file that contains data on employees, users, practitioners, etc. of the VA.                                                                                                                                                                                                                                                                                                                                                                                         |
| NOIS                                              | National Online Information System                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| NVS                                               | National VistA Support                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| O-R                                               | Object-Relational                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OCS                                               | VA Office of Cyber Security                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| OID                                               | Oracle Internet Directory                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ORACLE                                            | Oracle is a relational database that supports the Structured Query Language (SQL), now an industry standard.                                                                                                                                                                                                                                                                                                                                                                |
| ORACLE 9iAS                                       | Oracle 9i Application Server                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PATS                                              | Patient Advocate Tracking System/application. When completed, the Patient Advocate Tracking System/application will replace the current, site-based Patient Representative package with a national level application.                                                                                                                                                                                                                                                       |
| PCE                                               | Patient Care Encounter                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PIMS                                              | Patient Information Management System                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PIR                                               | Patient Incident Review File                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PLU                                               | Patient Lookup                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PRN                                               | Pro Re Nata, Latin meaning ‘as needed’                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Prototype                                         | An initial working model as proof of concept of a product or new version of an existing product.                                                                                                                                                                                                                                                                                                                                                                            |
| Provider                                          | The entity that furnishes health care to consumers. An individual or defined group of individuals who provide a defined unit of health care services (defined = codable) to one or more individuals at a single session.                                                                                                                                                                                                                                                    |
| PTF                                               | Patient Treatment File (PTF) at AAC                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RDBMS                                             | Relational Database Management System                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Registration                                      | Registration File                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| RN                                                | Registered Nurse                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ROES                                              | Remote Order Entry System                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SAS                                               | SAS is a company that provides data analysis, data mining, and data storage                                                                                                                                                                                                                                                                                                                                                                                                 |
| ScreenMan                                         | VA FileMan utility that provides a screen-oriented interface for editing and displaying data                                                                                                                                                                                                                                                                                                                                                                                |
| SDD                                               | Software Design Document                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SQA                                               | Software Quality Assurance                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SRS                                               | Software Requirements Specifications                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SSL                                               | Secure Socket Layer                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SSO                                               | Single Sign On                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TCP/IP                                            | Transmission Control Protocol/Internet Protocol                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Thin-client                                       | A simple client program, which relies on most of the function of the system being in the server, usually the Web browser in a Web domain                                                                                                                                                                                                                                                                                                                                    |
| TIU                                               | Text Integration Utility                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| User                                              | An Administrator, a Clinician, or a Researcher                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VA                                                | Veterans Affairs                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VA FileMan                                        | VistA database management system.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VAMC                                              | Veterans Affairs Medical Centers                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VARO                                              | Veterans Administration Regional Office                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VHA                                               | Veterans Health Administration                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VISN                                              | Veterans Integrated Service Network                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VIST                                              | Visual Impairment Service Team                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VistA                                             | Veterans Health Information Systems and Technology Architecture                                                                                                                                                                                                                                                                                                                                                                                                             |
| VistA MailMan                                     | VistA electronic mail system                                                                                                                                                                                                                                                                                                                                                                                                                                                |