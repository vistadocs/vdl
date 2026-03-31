---
title: EN Version 7 RTLS Enhancement Interfaces Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: RTLS Enhancement Interfaces Manual
app_code: EN
app_name: Engineering (AEMS / MERS)
section: FIN
app_status: active
pkg_ns: EN
patch_ver: 7
patch_id: EN*7
group_key: "EN:EN:7"
file_numbers: []
security_keys: []
menu_options: 0
description: > The Department of Veterans Affairs (VA) is implementing an enterprise-wide solution for a Real Time Location System (RTLS) for the VA. RTLS will be used for the purpose of tracking objects such as equipment, supplies, and instruments. RTLS has the ability to locate patients and staff as well. In a
audience: 
keywords: 
  - table
  - contents
  - rtls
  - interface
  - wavemark
  - vista
  - aems
  - mers
  - strong
  - class
page_count: 0
word_count: 5047
section_count: 24
table_count: 11
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: March 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/rtls_ese_interfaces_technical_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/rtls_ese_interfaces_technical_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=37"
---

# Department of Veterans Affairs


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Department of Veterans Affairs](#department-of-veterans-affairs)
    - [Real Time Location System (RTLS) ESE](#real-time-location-system-rtls-ese)
    - [March 2017](#march-2017)
    - [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [References](#references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Manage AEMS-MERS Interface Application Jobs](#manage-aems-mers-interface-application-jobs)
  - [Modify the Timeframe for the Queue in AEMS-MERS](#modify-the-timeframe-for-the-queue-in-aems-mers)
  - [Modify the Timing/Frequency of the GIP-WaveMark Interface](#modify-the-timingfrequency-of-the-gip-wavemark-interface)
- [Files](#files)
  - [PENDING RTLS EVENTS (#6930)](#pending-rtls-events-6930)
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [RTLS Interface Menu \[VIAA01 RTLS RPC MENU\]](#rtls-interface-menu-viaa01-rtls-rpc-menu)
  - [VIAA MAKE WEB CALL TO MULE Option](#viaa-make-web-call-to-mule-option)
- [Archiving](#archiving)
- [Callable Routines/Entry Points/Application Program Interfaces](#callable-routinesentry-pointsapplication-program-interfaces)
- [External Relationships](#external-relationships)
  - [Minimum Software Requirements](#minimum-software-requirements)
  - [VistA and Other Software Interactions](#vista-and-other-software-interactions)
    - [AEMS-MERS Interface to Intelligent InSites RTLS](#aems-mers-interface-to-intelligent-insites-rtls)
    - [GIP Interface to WaveMark RTLS](#gip-interface-to-wavemark-rtls)
    - [PATIENT File Interface to WaveMark](#patient-file-interface-to-wavemark)
    - [EMPLOYEE Interface to WaveMark](#employee-interface-to-wavemark)
    - [CART-CL Interface to WaveMark](#cart-cl-interface-to-wavemark)
  - [Integration Agreements (IA)](#integration-agreements-ia)
- [Internal Relationships](#internal-relationships)
- [Global Variables](#global-variables)
- [Glossary](#glossary)
- [Additional Useful Information](#additional-useful-information)
  - [External Interfaces](#external-interfaces)
  - [Cross-References](#cross-references)
  - [Software Security](#software-security)
- [Appendix A: RTLS-VistA Interface Configuration Tool](#appendix-a-rtls-vista-interface-configuration-tool)
  - [Getting Started](#getting-started)
    - [Understanding the AEMS-MERS RTLS Jobs](#understanding-the-aems-mers-rtls-jobs)
    - [Understanding the Job Scheduling Mechanism](#understanding-the-job-scheduling-mechanism)
    - [Accessing the Snap-In within Intelligent InSites](#accessing-the-snap-in-within-intelligent-insites)
  - [Initial Set Up](#initial-set-up)
    - [Adding a VISN](#adding-a-visn)
    - [Adding a VA Facility definition](#adding-a-va-facility-definition)
    - [Adding a Job](#adding-a-job)
  - [Managing Existing Jobs](#managing-existing-jobs)
    - [Modifying a Job Schedule](#modifying-a-job-schedule)
    - [Running a Job on Demand](#running-a-job-on-demand)
    - [Suspending a Job](#suspending-a-job)
    - [Deleting a Job](#deleting-a-job)
  - [Managing an Existing VA Facility Definition](#managing-an-existing-va-facility-definition)
    - [Modifying a VA Facility Definition](#modifying-a-va-facility-definition)
    - [Deleting a VA Facility Definition](#deleting-a-va-facility-definition)
- [Appendix B: Troubleshooting](#appendix-b-troubleshooting)
  - [RTLS Interface Application](#rtls-interface-application)
    - [Understanding the Log Files](#understanding-the-log-files)
    - [Troubleshooting](#troubleshooting)
  - [CART-CL/WaveMark Interface](#cart-clwavemark-interface)
    - [Understanding the High Level Operations](#understanding-the-high-level-operations)
    - [Troubleshooting](#troubleshooting-1)
  - [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)

### Real Time Location System (RTLS) ESE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Interfaces Technical Manual
![](en-version-7-rtls-enhancement-interfaces-manual/001.png)

### March 2017

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 3.2
> *This page intentionally left blank*

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 49%" />
<col style="width: 21%" />
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
<td>6/16/2014</td>
<td>1.0</td>
<td>Initial Submission to VA</td>
<td>HP</td>
</tr>
<tr class="even">
<td>7/9/2014</td>
<td>1.1</td>
<td>Update to section 2.2 to include more detail. Updated ICR list in section 8.3</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/10/2014</td>
<td>1.2</td>
<td><p>Updated:</p>
<p>1.3 scope to list interfaces Reference to Appendix A Added table header to section 4</p>
<p>8.2.3 to add more info</p>
<p>14.2.2. updated</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/11/2014</td>
<td>1.3</td>
<td>Updates to Table 1</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>7/14/2014</td>
<td>2.0</td>
<td>Subsequent submission to VA</td>
<td>HP</td>
</tr>
<tr class="even">
<td>8/15/2014</td>
<td>3.0</td>
<td>Subsequent submission to VA</td>
<td>HP</td>
</tr>
<tr class="odd">
<td>2/12/2016</td>
<td>3.1</td>
<td>Updated section 13.1.1 for the date processing changes for inventory updates to AEMS-MERS.</td>
<td>HP</td>
</tr>
<tr class="even">
<td>3/7/2017</td>
<td>3.2</td>
<td><p>Updated per HPS review:</p>
<ul>
<li><p>Section 8.3 to add file numbers</p></li>
<li><p>Section 8.2.3 to remove reference to the year 2013</p></li>
</ul></td>
<td>HPES</td>
</tr>
</tbody>
</table>
> *This page intentionally left blank*
1.  [Introduction 1](#introduction)
    1.  [Overview 1](#overview)
    2.  [Purpose 3](#purpose)
    3.  [Scope 3](#scope)
    4.  [References 3](#references)
2.  [Implementation and Maintenance 3](#implementation-and-maintenance)
    1.  [Manage AEMS-MERS Interface Application Jobs 4](#manage-aems-mers-interface-application-jobs)
    2.  [Modify the Timeframe for the Queue in AEMS-MERS 4](#modify-the-timeframe-for-the-queue-in-aems-mers)
    3.  [Modify the Timing/Frequency of the GIP-WaveMark Interface 5](#modify-the-timingfrequency-of-the-gip-wavemark-interface)
3.  [Files 5](#files)
    1.  [PENDING RTLS EVENTS (#6930) 5](#pending-rtls-events-6930)
4.  [Routines 6](#routines)
5.  [Exported Options 8](#exported-options)
    1.  [RTLS Interface Menu \[VIAA01 RTLS RPC MENU\] 8](#rtls-interface-menu-viaa01-rtls-rpc-menu)
    2.  [VIAA MAKE WEB CALL TO MULE Option 8](#viaa-make-web-call-to-mule-option)
6.  [Archiving 9](#archiving)
7.  [Callable Routines/Entry Points/Application Program Interfaces 9](#callable-routinesentry-pointsapplication-program-interfaces)
8.  [External Relationships 9](#external-relationships)
    1.  [Minimum Software Requirements 9](#minimum-software-requirements)
    2.  [VistA and Other Software Interactions 10](#vista-and-other-software-interactions)
        1.  [AEMS-MERS Interface to Intelligent InSites RTLS 10](#aems-mers-interface-to-intelligent-insites-rtls)
        2.  [GIP Interface to WaveMark RTLS 10](#gip-interface-to-wavemark-rtls)
        3.  [PATIENT File Interface to WaveMark 11](#patient-file-interface-to-wavemark)
        4.  [EMPLOYEE Interface to WaveMark 12](#employee-interface-to-wavemark)
        5.  [CART-CL Interface to WaveMark 13](#cart-cl-interface-to-wavemark)
    3.  [Integration Agreements (IA) 13](#integration-agreements-ia)
9.  [Internal Relationships 15](#internal-relationships)
10. [Global Variables 15](#global-variables)
11. [Glossary 15](#glossary)
12. [Additional Useful Information 16](#additional-useful-information)
    1.  [External Interfaces 16](#external-interfaces)
    2.  [Cross-References 16](#cross-references)
    3.  [Software Security 16](#software-security)
13. [Appendix A: RTLS-VistA Interface Configuration Tool 16](#appendix-a-rtls-vista-interface-configuration-tool)
    1.  [Getting Started 17](#getting-started)
        1.  [Understanding the AEMS-MERS RTLS Jobs 17](#understanding-the-aems-mers-rtls-jobs)
        2.  [Understanding the Job Scheduling Mechanism 18](#understanding-the-job-scheduling-mechanism)
        3.  [Accessing the Snap-In within Intelligent InSites 19](#accessing-the-snap-in-within-intelligent-insites)
    2.  [Initial Set Up 21](#initial-set-up)
        1.  [Adding a VISN 21](#adding-a-visn)
        2.  [Adding a VA Facility definition 22](#adding-a-va-facility-definition)
        3.  [Adding a Job 24](#adding-a-job)
    3.  [Managing Existing Jobs 26](#managing-existing-jobs)
        1.  [Modifying a Job Schedule 26](#modifying-a-job-schedule)
        2.  [Running a Job on Demand 27](#running-a-job-on-demand)
        3.  [Suspending a Job 28](#suspending-a-job)
        4.  [Deleting a Job 29](#deleting-a-job)
    4.  [Managing an Existing VA Facility Definition 30](#managing-an-existing-va-facility-definition)
        1.  [Modifying a VA Facility Definition 30](#modifying-a-va-facility-definition)
        2.  [Deleting a VA Facility Definition 32](#deleting-a-va-facility-definition)
14. [Appendix B: Troubleshooting 33](#appendix-b-troubleshooting)
    1.  [RTLS Interface Application 33](#rtls-interface-application)
        1.  [Understanding the Log Files 33](#understanding-the-log-files)
        2.  [Troubleshooting 33](#troubleshooting)
    2.  [CART-CL/WaveMark Interface 36](#cart-clwavemark-interface)
        1.  [Understanding the High Level Operations 36](#understanding-the-high-level-operations)
        2.  [Troubleshooting 37](#troubleshooting-1)
    3.  [Frequently Asked Questions (FAQ) 37](#frequently-asked-questions-faq)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Department of Veterans Affairs (VA) is implementing an enterprise-wide solution for a Real Time Location System (RTLS) for the VA. RTLS will be used for the purpose of tracking objects such as equipment, supplies, and instruments. RTLS has the ability to locate patients and staff as well. In addition, environmental monitoring (i.e. humidity and temperature) of equipment and rooms is included in the solution. Multiple RFID tags and technologies are being deployed (using existing wireless infrastructure, or wired infrastructure) to meet specifications and specialized needs.

> The Veterans Health Administration (VHA) has a requirement to implement RTLS in all its facilities over the next several years. Each VHA Veterans Integrated Service Network (VISN) will have its own RTLS database(s) that will be accessible via a single, standard user interface. The RTLS at each VISN must also be capable of exchanging data with VA information systems (e.g. VistA) and with a single national information system, (the National Data Repository \[NDR\]), that will serve to aggregate and display RTLS data from the VISN-level RTLS databases. The NDR, at a minimum, will be an information based solution with open, flexible architecture that will house sophisticated business intelligence, predictive analytics, and reporting capabilities used for process improvement, business and financial analytics, workflow analysis and research analysis.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS solution consists of the tags (active, passive, and 2D barcodes), the databases associated with the collection of the data from the tags, and a Graphical User Interface (GUI) software application(s) that allow users to interact with the RTLS data. [Figure 1](#figure-1-rtls-overview) depicts the system overview and a breakdown of the major components of RTLS.

> ![](en-version-7-rtls-enhancement-interfaces-manual/002.png)

#### Figure 1 RTLS Overview

> The RTLS ESE Interface Applications have been developed to connect the VA legacy systems to RTLS. The RTLS Interface Applications orchestrate specific Mule Enterprise Service Bus (ESB) process flows to support the following functional areas:

- AEMS-MERS equipment synchronization with RTLS
- GIP Inventory supply synchronization with WaveMark
- Search of VistA employee data from within the WaveMark system
- Search of VistA patient data from within the WaveMark system

> Also included in the VA RTLS solution is an interface that provides CART-CL with supply usage information related to a patient captured by the WaveMark system.

> The environment needed to run the RTLS Interface Applications is multi-server and includes the following distinct deployment components:

- RTLS VistA Patch (KIDS build)
- WebLogic VistaService Web Services
- RTLS ESB application component
- RTLS-VistA Interface Configuration Tool

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this manual is to provide the necessary technical information about the structure and function of the logical components of the RTLS Interface Applications to aid technical support staff with the configuration, maintenance and troubleshooting of the individual interface components that comprise the software solution.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The manual describes how to configure and maintain the RTLS Interface Applications. The interfaces covered in the RTLS Interface Applications are:

- Automated Engineering Management System/Medical Equipment Reporting System (AEMS- MERS) Intelligent InSites Interface
- Cardiovascular Assessment Reporting and Tracking system for Catheterization Labs (CART-CL) WaveMark Interface
- Employee (VistA NEW PERSON File) WaveMark Interface
- Patient (VistA PATIENT File) WaveMark Interface
- Generic Inventory Package (GIP) WaveMark Interface

> Installation of the RTLS Interface Applications is covered in the RTLS ESE Installation Guide. Information on how end users interact with the interface components is covered in the RTLS ESE Interfaces User Guide.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- \[RTLS ESE Installation Guide\] Real Time Location Systems (RTLS) ESE Installation Guide
- \[RTLS ESE Security Plan\] Real Time Location Systems (RTLS) ESE Security Plan
- \[RTLS ESE Interfaces User Guide\] Real Time Location Systems (RTLS) ESE Interfaces User Guide
- VA WaveMark User Guide

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VA RTLS Program is an incremental program. The RTLS Interface Application along with RTLS hardware and software will be progressively deployed to locations within the VA VISNs and CMOP. Deployment and installation is planned as an incremental rollout to each VISN and CMOP until all VISNs/CMOP are deployed.

> The post-installation tasks needed to configure the RTLS Interface Application are covered in the RTLS ESE Installation Guide. Beyond the initial installation and configuration, there is minimal maintenance to be performed. The following sections provide more information about maintenance tasks.

## Manage AEMS-MERS Interface Application Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The AEMS-MERS/RTLS interface is comprised of several interface jobs that synchronize equipment tracking data between VistA and RTLS. These jobs are scheduled through the RTLS-VistA Interface Configuration Tool described in Section [13 Appendix A: RTLS-VistA Interface Configuration Tool.](#appendix-a-rtls-vista-interface-configuration-tool)

## Modify the Timeframe for the Queue in AEMS-MERS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS VistA Patch contains an option, ‘Make Web Call to Mule’ \[VIAA MAKE WEB CALL TO MULE\], to send Engineering file changes (via MUMPS Style Cross Reference events) to the RTLS database via a Mule server. The option is a queue process that can check on user-specified intervals, to see if there are any record changes from files EQUIPMENT INV (#6914) and ENG SPACE (#6928) that need to be transmitted to RTLS. To modify the timeframe for the record transmission, use the following steps:

> Note: Recommended timeframe for the queue is between 1 and 5 minutes.

1.  From the System Manager Menu, select Taskman Management.
2.  From the Taskman Management Menu, select Schedule/Unschedule Options.
3.  At the “Select OPTION to schedule or reschedule” prompt, type VIAA MAKE WEB CALL TO MULE
4.  At the “QUEUED TO RUN AT WHAT TIME” prompt, type the time of day expressed in military time for the job to begin preceded by the characters “T@”. For example, T@13:00 would represent the job beginning at 1:00 PM each day.
5.  At the “RESCHEDULING FREQUENCY” prompt, type the number of seconds between job runs followed by the letter “S”. For example, 180S would represent a 3 minute interval.

> See Figure 2 for an example of the Schedule Make Web Call to Mule Option steps and results.

> Figure 2 Example of Scheduling the new option

## Modify the Timing/Frequency of the GIP-WaveMark Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The GIP-WaveMark interface has two scheduled jobs that work in unison to keep current WaveMark inventory supply counts updated in GIP. These scheduled jobs are managed by end users (i.e. VA Inventory Managers). Instructions on how to run the interfaces is described in the VA WaveMark User Guide.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS Interface Application contains one new VistA file called PENDING RTLS EVENT (#6930).

## PENDING RTLS EVENTS (#6930)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As part of the synchronization of equipment details between AEMS-MERS and RTLS, a unidirectional Mule ESB flow detects changes in equipment inventory files in AEMS-MERS and pushes the specified fields to the RTLS system. This is a triggered process. The MUMPS Style Cross References on the EQUIPMENT INV (#6914) file queue the triggered events in the PENDING RTLS EVENTS (#6930) file. A VistA TaskMan job processes the pending entries on a configured polling interval (e.g. 1-5 minutes) and issues an HTTP request to the Mule flow via the HWSC (Health-e-Vet Web Service Client). A MUMPS Style Cross Reference identifies an action that should take place when the value of fields defined in that cross-reference is changed. This provides timely updates of RTLS with data maintained in AEMS-MERS. When changes occur in the ENG SPACE file (#6928), a similar triggered process is completed.

> The PENDING RTLS EVENTS file introduces a resiliency feature by saving record changes that could not be sent to RTLS when the Mule server is offline for any reason. Record changes are sent when communication is re-established.

> For more information about the fields within the PENDING RTLS EVENTS file, complete the following steps:

1.  Login to VistA with your access and verify codes.
2.  From the Systems Manager Menu, select VA FileMan.
3.  Select Data Dictionary Utilities.
4.  Select List File Attributes.

> The PENDING RTLS EVENTS file does not have any special templates.

> The PENDING RTLS EVENTS file is also described in the AEMS-MERS/Intelligent InSites SDD.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For a brief description of the routines created to support the RTLS Interface Application, use the First Line Routine Print \[XU FIRST LINE PRINT\] menu option by completing the following steps:

1.  Login to VistA with your access and verify codes.
2.  From the Systems Manager Menu, select Programmer Options.
3.  Select Routine Tools.
4.  From the Routine Tools Menu, select First Line Routine Print
5.  At the “All Routines?” prompt, press enter.
6.  At the “Routine:” prompt, type VIAA\*
7.  At the second “Routine:” prompt, press enter.

> The number of routines included in the VIAA patch is displayed.

8.  At the “(A)lpha, (D)ate ,(P)atched…” prompt, press enter.
9.  At the “Include line (2)…” prompt, press enter.
10. At the “DEVICE: HOME//” prompt, press enter. The list of routine names and a brief description of each is displayed.

> See Vista for an example of the steps.

#### Figure 3 Displaying routines in VistA

> FM VA FileMan ...

> Menu Management ... Programmer Options ... Operations Management ... Spool Management ...

> Information Security Officer Menu ... Taskman Management ...

> HL7 Main Menu ... User Management ...

> Application Utilities ... Capacity Planning ...

> Manage Mailman ...

> Select Systems Manager Menu \<TEST ACCOUNT\> Option: PROgrammer Options

> KIDS Kernel Installation & Distribution System ... NTEG Build an 'NTEG' routine for a package

> PG Programmer mode

> Calculate and Show Checksum Values Delete Unreferenced Options

> Error Processing ... Global Block Count List Global

> Map Pointer Relations Number base changer Routine Tools ...

> Test an option not in your menu Verifier Tools Menu ...

> Select Programmer Options \<TEST ACCOUNT\> Option: ROUTINE Tools

> %Index of Routines

> Check Routines on Other CPUs

> Compare local/national checksums report Compare routines on tape to disk Compare two routines

> Delete Routines

> First Line Routine Print Flow Chart Entire Routine Flow Chart from Entry Point Group Routine Edit

> Input routines List Routines

> Load/refresh checksum values into ROUTINE file Output routines

> Routine Edit

> Routines by Patch Number Variable changer

> Version Number Update

> Select Routine Tools \<TEST ACCOUNT\> Option: FIRST Line Routine Print

> PRINTS FIRST LINES

> The following table provides a quick reference to the functional areas of VistA the routines are related to.

> Table 1 Vista Packages and Associated Routines

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Package or File</strong></th>
<th><strong>Routine Names</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AEMS-MERS</td>
<td><p>VIAAEAD VIAAEUT</p>
<p>VIAAMB1</p></td>
</tr>
<tr class="even">
<td>GIP</td>
<td><p>VIAAIMUP VIAAIPDE VIAAPAR</p>
<p>VIAASQH</p></td>
</tr>
<tr class="odd">
<td>NEW PERSON #200</td>
<td>VIAANPR</td>
</tr>
<tr class="even">
<td>PATIENT #2</td>
<td>VIAAPTR</td>
</tr>
<tr class="odd">
<td>General utility for RTLS project</td>
<td>VIAAQUE VIAATRI</td>
</tr>
</tbody>
</table>

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections provide information about exported VistA options.

## RTLS Interface Menu \[VIAA01 RTLS RPC MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS Interface Menu is included with the RTLS Interface Application. This menu contains the RPC options used to refresh RTLS.

> RTLS Interface Menu \[VIAA01 RTLS RPC MENU\]

> This is the RTLS interface menu which includes Remote Procedure Calls for multiple packages in VistA.

> This menu option is used by the RTLS Interface Application only. No special access is needed for the menu.

## VIAA MAKE WEB CALL TO MULE Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIAA MAKE WEB CALL TO MULE option is included with the RTLS Interface Application. This option sends engineering file changes to the RTLS database via a Mule server. This option is a queue process that checks every number of minutes, configured by the site, to see if there are any record changes from files \#6914 and \#6928 that need to be transmitted to RTLS.

> At installation, the job should be scheduled to run every 1 to 5 minutes for effective record transmission. The time interval is user-specified. To adjust this time interval, see section [2.2.](#modify-the-timeframe-for-the-queue-in-aems-mers)

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS Interface Application does not require archiving.

# Callable Routines/Entry Points/Application Program Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS VistA patch (under namespace VIAA) has one routine that is called from multiple fields in the data dictionaries for files \#6914 and \#6928. The entry tag is WC and the routine is VIAATRI. VIAATRI is designed to be used for the RTLS Interface Application only.

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections provide information about relationships between VistA and the external software components that comprise the RTLS solution.

## Minimum Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following tables list the software and minimum versions required for the RTLS Interface Application.

#### Table 2 Prerequisite VistA software

| Software Application or Patch                                                         | Namespace | Version |
|-------------------------------------------------------------------------------------------|---------------|-------------|
| AEMS-MERS (Automated Engineering Management System-Medical Equipment Reporting System)    | EN            | 7.0         |
| IFCAP (Integrated Funds Distribution, Control Point Activity, Accounting and Procurement) | PRC           | 5.1         |
| Kernel                                                                                    | XU            | 8.0         |
| VA FileMan                                                                                | DI            | 22.0        |

> Table 3 Non-VistA Required Software

| Software Application           | Version                         |
|------------------------------------|-------------------------------------|
| Intelligent InSites RTLS           | 4.6                                 |
| Mule Enterprise Edition            | 3.3.2                               |
| Oracle JRockit                     | R28.2.5-4.1.0 64 bit (for WebLogic) |
| Oracle WebLogic Enterprise Edition | 10.3.6 64 bit                       |
| Red Hat Enterprise Linux (RHEL)    | 6.5                                 |
| Sun/Oracle JDK                     | 1.6 update 45 (for Mule ESB)        |
| WaveMark EncounterLink             | 2.5                                 |
| WaveMark Engine                    | 5.27                                |

| Software Application | Version      |
|--------------------------|------------------|
| WaveMark InterfaceEngine | 1.3              |
| MMC Console              | 3.4.1            |
| Microsoft SQL Server     | 2008 R2 or later |

> Note: Your versions to install may differ based on later agreement between RTLS and local VA infrastructure.

## VistA and Other Software Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The overall RTLS system is used for the purpose of tracking objects such as equipment, supplies, and instruments. RTLS has the ability to locate staff and patients as well. The RTLS Interface Application has been developed to connect the VA legacy systems to RTLS and serves various different functional areas. The external relationships between the VA legacy systems (i.e. VistA and CART-CL) and other software, including Commercial off the Shelf (COTS) products, are described in the following sections.

### AEMS-MERS Interface to Intelligent InSites RTLS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AEMS-MERS, also known as the Engineering Package within VistA, is in use today at all VHA facilities and some other VA entities. Equipment is currently tagged with 2D barcodes, and details about the equipment are entered into AEMS-MERS.

> Intelligent InSites RTLS is a COTS real time location system designed for the healthcare industry. RTLS gathers data from real time location, condition sensing, and other systems, then delivers meaningful real time actionable information for reporting and analytical purposes.

> The bi-directional interface between AEMS-MERS and RTLS provides RTLS with details about tagged AEMS-MERS equipment and provides AEMS-MERS with updated equipment location information.

> Through the RTLS Interface Application, AEMS-MERS sends equipment details from the EQUIPMENT INV file (#6914) to the RTLS InSites database. The RTLS system captures current equipment location information through active and passive RTLS tags and sends updated location information to the EQUIPMENT INV (#6914) file.

### GIP Interface to WaveMark RTLS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Generic Inventory Package (GIP) is a module of VistA Integrated Funds Control, Accounting and Procurement (IFCAP) that resides locally and manages the receipt, distribution, and maintenance of stock items received for the supply warehouse from outside vendors and distributed to primary inventory points. GIP is the system of record for expendable/consumable supplies, such as those typically stored in cabinets and storage rooms and used for patient care.

> WaveMark is a COTS product. WaveMark uses RFID enabled cabinets and Point of Use Stations (XPOS) to maintain an accurate inventory of passively tagged GIP expendable/consumable supplies stored in WaveMark cabinets. The WaveMark cabinets come in many form factors as shown in Figure 4. Figure 5 illustrates how an item is scanned into the WaveMark system using an XPOS.

> The RTLS Interface Application includes code to implement a bi-directional flow of information between GIP and WaveMark for VA Cath Lab supplies. GIP sends a list of approved expendable/consumable supplies (i.e. ITEM MASTER NUMBERs and associated reference data) to WaveMark. GIP receives from WaveMark periodic inventory updates of all items stored in the WaveMark Smart Cabinets.

> ![](en-version-7-rtls-enhancement-interfaces-manual/003.png)

#### Figure 4 WaveMark Smart Cabinets

![](en-version-7-rtls-enhancement-interfaces-manual/004.png)

> Figure 5 WaveMark Pont of use Station

> Through the GIP-WaveMark interaction, a list of approved expendable/consumable GIP supplies is sent to WaveMark from the ITEM MASTER file (#441). The WaveMark passive tagging of expendable/consumable supplies provides GIP with an accurate inventory of supplies. The WaveMark system updates inventory levels as well as par values for the supplies that are synchronized between the two systems in the GENERIC INVENTORY file (#445).

### PATIENT File Interface to WaveMark

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PATIENT file/WaveMark interface performs a real time search for patient information to help positively identify a patient before a procedure.

> VHA Directive 2010-023 states “It is VHA policy that any VHA health care provider performing a surgery or invasive procedure must complete specific steps to ensure that the procedure is performed on the correct patient, at the correct site, and with the correct implant, if applicable.”

> Improving the accuracy of patient identification is one of the National Patient Safety Goals (NPSGs). The Patient Safety Advisory Group advises The Joint Commission on the development and updating of NPSGs.

> As part of the RTLS interface applications, the WaveMark system helps Cath Lab nurses and technicians verify a patient’s identity by using a scanner attached to the WaveMark XPOS to scan the patient’s wristband. The WaveMark XPOS uses the unique identifier located on the wristband to send a request for information from the VistA PATIENT (#2) file. After data retrieval from VistA, the patient name, gender, and date of birth are displayed on the WaveMark XPOS. These data elements are not stored in the WaveMark system.The Patient ICN is the only data element stored. Figure 6 shows what the WaveMark XPOS will display to the nurses and technicians responsible for verifying the patient’s identity.

> ![](en-version-7-rtls-enhancement-interfaces-manual/005.png)

> Figure 6 WaveMark XPOS Patient Confirmation Window

### EMPLOYEE Interface to WaveMark

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Employee Interface (NEW PERSON (#200) file to WaveMark helps identify staff to ensure that the correct staff is associated with patient procedures and facilitates data accuracy and normalization.

> As part of the goal of improving employee identity verification for VA healthcare, the Joint Commission recommends positively identifying the employee. The accurate identification of employee is improved by using a unique identifier IEN (Internal Entry Number). The real-time lookup of the employee information that is relevant to the process is retrieved and displayed for the clinician to confirm through WaveMark Point of Use Station (XPOS).

> The WaveMark Engine exposes a Web-based UI that allows administrators to manage the employee lists in the WaveMark system. Using the Manage Lists tool users are able to add and remove doctors and staff from the WaveMark system. To add employees, the administrator enters the last name of the employee and clicks a button that will invoke the interface and perform the lookup. The returned matches from the VistA NEW PERSON (#200) file will be displayed. This display includes additional identifying data such as the full first and last name, title, and service/section to allow the administrator to select the correct employee if more than one possible match is returned.

> The WaveMark XPOS systems are installed at the point of care either in the procedure room or the control room of the procedure room. The XPOS system has a graphical user interface (GUI) that is navigated and controlled by the end users using a touch screen. Figure 7 shows what the WaveMark system will display on the XPOS for the staff list.

![](en-version-7-rtls-enhancement-interfaces-manual/006.png)

#### Figure 7 Staff List displayed on the WaveMark XPOS

> The interface exposes Internal Entry Number (IEN), name, and position (e.g., doctor, nurse, or technician) information from the Vista NEW PERSON file (#200) for staff identification.

### CART-CL Interface to WaveMark

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA currently employs inventory tools, such as GIP, to assign codes to individual consumable models as they are deployed at VAMCs. Data about the usage of the consumables is recorded by a system called CART-CL that aggregates all usage data in Cath Labs from all VAMCs. CART-CL is currently used to record consumables used in Cath Labs, such as stents and balloons. CART-CL also tracks patient information and associates it with the used consumables.

> This is a software interface that allows the WaveMark system to directly pass specific information to a pair of SQL Server staging tables created in CART-CL exclusively for this purpose. CART-CL does not pass any information to the WaveMark system.

> The scheduler in the WaveMark Interface Engine is responsible for dispatching the interface. The Interface Engine includes intelligence to not dispatch more than one instance of this interface at any given time.

## Integration Agreements (IA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ICR \# | Name                                           | Description                                                                                                                                                                                                                                                                                                                                  |
|------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5913       | READ/WRITE ACCESS TO FILE \#6914 (EQUIPMENT INV)   | Request permission for READ access via FileMan calls to file \#6914 in order to complete RPC queries from Intelligent Insites, and to update the file in VistA when requested. This is part of the RTLS National project to facilitate tracking equipment updates in Engineering, while keeping Intelligent Insites with up to date information. |
| 5914       | READ ACCESS TO FILE \#6911 (EQUIPMENT CATEGORY)    | Request permission for READ access via FileMan calls to file \#6911 in order to complete RPC queries from Intelligent Insites. This is part of the RTLS National project to facilitate tracking equipment updates in Engineering, while keeping Intelligent Insites with up to date information.                                                 |
| 5915       | READ ACCESS TO FILE \#6928 (ENG SPACE)             | Request permission for READ access via FileMan calls to file \#6928 in order to complete RPC queries from Intelligent Insites. This is part of the RTLS National project to facilitate tracking equipment updates in Engineering, while keeping Intelligent Insites with up to date information.                                                 |
| 5916       | READ ACCESS TO FILE \#6917 (CATEGORY STOCK NUMBER) | Request permission for READ access via FileMan calls to file \#6917 in order to complete RPC queries from Intelligent Insites. This is part of the RTLS National project to facilitate tracking equipment updates in Engineering, while keeping Intelligent Insites with up to date information.                                                 |

| ICR \# | Name                                            | Description                                                                                                                                                                                                                                                                                    |
|------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5917       | READ ACCESS TO FILE \#6914.1 (CMR)                  | Request permission for READ access via FileMan calls to file \#6914.1 in order to complete RPC queries from Intelligent Insites. This is part of the RTLS National project to facilitate tracking equipment updates in Engineering, while keeping Intelligent Insites with up to date information. |
| 5918       | READ ACCESS TO FILE \#6912 (MANUFACTURER LIST FILE) | Request permission for READ access via FileMan calls to file \#6912 in order to complete RPC queries from Intelligent Insites. This is part of the RTLS National project to facilitate tracking equipment updates in Engineering, while keeping Intelligent Insites with up to date information.   |
| 5920       | READ ACCESS TO FILE \#6910 (ENG INIT PARAMETERS)    | Request permission for READ access via FileMan calls to file \#6910 in order to complete RPC queries from Intelligent Insites. This is part of the RTLS National project to facilitate tracking equipment updates in Engineering, while keeping Intelligent Insites with up to date information.   |
| 5921       | READ ACCESS TO FILE \#441 (ITEM MASTER)             | Request permission for READ access via FileMan calls to file \#441 in order to complete RPC queries from WaveMark. This is part of the RTLS National project to facilitate tracking clinical supplies in the Cathlab inventory point for GIP.                                                      |
| 5922       | READ ACCESS TO FILE \#440 (VENDOR)                  | Request permission for READ access via FileMan calls to file \#440 in order to complete RPC queries from WaveMark. This is part of the RTLS National project to facilitate tracking clinical supplies in the Cathlab inventory point for GIP.                                                      |
| 5923       | READ ACCESS TO FILE \#445 (GENERIC INVENTORY)       | Request permission for READ and WRITE access via FileMan calls to file \#445 in order to complete RPC queries from WaveMark. This is part of the RTLS National project to facilitate tracking clinical supplies in the Cath Lab inventory point for GIP.                                           |
| 5993       | RTLS POINTING TO FILE 1                             | The Real Time Location System (RTLS) is requesting approval to point to the file of files (#1). This is to be used for building calls to File Manager API'S dynamically.                                                                                                                           |
| 6067       | READ ACCESS TO FILE \#445.6 (GROUP CATEGORY)        | Request permission for READ access via FileMan calls to file \#445.6 in order to complete RPC queries from WaveMark.                                                                                                                                                                               |
| 6068       | READ ACCESS TO FILE \#420.5 (UNIT OF ISSUE)         | Request permission for READ access via FileMan calls to file \#420.5 in order to complete RPC queries from WaveMark.                                                                                                                                                                               |
| 6069       | ENGINEERING CALL TO RTLS AFTER DATA CHANGE          | The RTLS project has requested the Engineering files \#6914 and \#6928 to have a number of fields modified with MUMPS cross references to report data changes.                                                                                                                                     |

| ICR \# | Name              | Description                                                                                                                                                                            |
|------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10035      | PATIENT FILE \#2      | Any nationally released cross-reference on the supported fields in this Integration Agreement are “open/supported” for direct global references (as well as reference through VA FileMan). |
| 10060      | NEW PERSON FILE \#200 | All fields supported for Read w/FileMan only for “new” code.                                                                                                                               |

# Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS Interface Applications contain no options that rely on entry or exit logic from other options.

> Updates to files EQUIPMENT INV (#6914) and ENG SPACE (#6928), both through FileMan and the Engineering package options are captured and sent to RTLS.

# Global Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS Interface Applications contain a global variable called ^VIAA. There are no SACC exemptions required in the RTLS Interface Applications.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term  | Definition                                                                     |
|-----------|------------------------------------------------------------------------------------|
| AEMS-MERS | Automated Engineering Management System /Medical Equipment Reporting System        |
| API       | Application Programming Interface                                                  |
| CART-CL   | Clinical Assessment, Reporting, and Tracking Catheterization Lab                   |
| CMOP      | Consolidated Mail Order Pharmacy                                                   |
| COTS      | Commercial Off the Shelf                                                           |
| CRON      | CRON Table                                                                         |
| ESB       | Enterprise Service Bus                                                             |
| ESE       | Enterprise Systems Engineering                                                     |
| GIP       | Generic Inventory Package                                                          |
| GUI       | Graphical User Interface                                                           |
| IA        | Integration Agreement                                                              |
| ICR       | Integration Control Registration                                                   |
| IEN       | Internal Entry Number                                                              |
| IFCAP     | Integrated Funds Distribution, Control Point Activity, Accounting, and Procurement |
| JDK       | Java Development Kit                                                               |
| KIDS      | Kernel Installation & Distribution System                                          |
| MMC       | Microsoft Management Console                                                       |
| MUMPS     | Massachusetts General Hospital Utility Multi-Programming System                    |
| Term | Definition                      |
|----------|-------------------------------------|
| NDR      | National Data Repository            |
| RFID     | Radio Frequency Identification      |
| RHEL     | Red Hat Enterprise Linux            |
| RPC      | Remote Procedure Call               |
| RTLS     | Real Time Location System           |
| SACC     | Standards and Conventions Committee |
| SDD      | Software Design Document            |
| SQA      | Software Quality Assurance          |
| SQL      | Structured Query Language           |
| UI       | User Interface                      |
| VA       | Veterans Affairs                    |
| VHA      | Veterans Health Administration      |
| VISN     | Veterans Integrated Service Network |
| XPOS     | Point of Service Station            |

# Additional Useful Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The primary purpose of the RPCs developed for the RTLS Interface Applications is to support the RTLS solution. The RPCs are not designed to be called by other software.

## Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Software Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Security is addressed in the RTLS ESE Security Plan.

# Appendix A: RTLS-VistA Interface Configuration Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS-VistA Interface Configuration Tool is a software utility for managing jobs between VistA and RTLS. The tool is designed for administrative users of RTLS to have a single location to view and manage network connections and associated jobs within the VISN. The tool is a web application hosted on the interface WebLogic server and is displayed as a Snap-in screen on the Intelligent InSites user interface. The tab in the Intelligent InSites user interface is labeled *Interface Apps*.

> At this time, the tool manages jobs for the AEMS/MERS-RTLS interface, but is designed to be extended if other VistA interfaces are developed requiring scheduled job management. The tool is also designed to be extended to an enterprise level so a single deployment could control all VISNs and associated jobs.

> Note: The screen captures used throughout this appendix are from the ES Labs SQA instance and are for illustrative purposes only.

## Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS-VistA Interface Configuration Tool provides the VA with a mechanism to control the timing and frequency of the jobs that encompass the interface between AEMS-MERS and Intelligent InSites.

> The tool is installed as a snap-in on the Intelligent InSites user interface and represents all of the VA facilities and jobs associated with a VISN. The tool is organized in a hierarchical manner: all jobs are associated with a VA facility and all VA facilities are associated with the VISN.

### Understanding the AEMS-MERS RTLS Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The AEMS-MERS/RTLS interface suite is comprised of several interface jobs that synchronize the equipment tracking data between VistA and RTLS. These jobs are scheduled through the RTLS-VistA Interface Configuration Tool and described below:

- Populate New Asset Details – a job to update newly added AEMS-MERS equipment items in RTLS with additional data elements from the EQUIPMENT INV file (#6914). AEMS-MERS equipment items are initially created in RTLS with a subset of data elements. This job populates RTLS with the additional data elements for all equipment items added since the last job was run.
- Bulk Update – a job to loop through all assets in RTLS for a given station and update the RTLS asset details from AEMS-MERS. The purpose of this process is to periodically re-synchronize all assets between both systems.
- Moved Equipment Inventory - Passive and Active tags - a job to update equipment item locations in AEMS-MERS. When the Moved Equipment Inventory job is run, the location of all AEMS-MERS equipment items tracked in RTLS that have a new location since the last job was run and a inventory date in RTLS that is more recent than AEMS-MERS are updated in AEMS- MERS with the new location and a timestamp.
- Static Active Tagged Equipment Inventory- a job to supplement the information provided by the Moved Equipment Inventory job. This job queries RTLS for active tagged equipment items that have not changed locations and uses the last time the equipment item was “sensed by RTLS” to compare with the last inventory date in AEMS-MERS. AEMS-MERS is updated with a new timestampif the “sensed by RTLS” date is newer than the inventory date in AEMS-MERS.
- Static Passive Tagged Equipment Inventory - a job to supplement the information provided by the Moved Equipment Inventory job. This job queries RTLS for passive tagged equipment items that have not changed locations and uses the last time the equipment item was sensed by RTLS to compare against the inventory date in AEMS-MERS. If the “sensed by RTLS” date is newer than the inventory date in AEMS-MERS, AEMS-MERS is updated with a new timestamp. The last time the item was sensed by RTLS is determined by checking an InSites custom attribute that gets updated by the RTLS passive tag scanner.
- Unmapped Location Report - a job detecting Intelligent InSites locations that do not have RTLS External References tying them back to a VistA space file entry, usually because one does not exist. The job generates a simple report, showing the name of the location from Intelligent InSites and the number of asset movement actions that are tied to that location. The report can be used to research which asset locations may need a corresponding VistA Engineering Space file entry based on the frequency at which they occur.
- Invalid Location Report – a job that detects location ‘space’ external-references that point to invalid Engineering Space file entries. This report lists the RTLS Location Name and the current ‘space’ external-reference value for all locations within a station that point to invalid spaces.

> Note: The reports are delivered to designated RTLS system users via the Intelligent InSites user interface.

> For more information about the data elements exchanged and the detailed process flow, see the AEMS- MERS ICD.

### Understanding the Job Scheduling Mechanism

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS-VistA Interface Configuration Tool connects to a Linux job scheduling software utility called cron. Cron schedules jobs to run periodically at fixed times, dates, or intervals. Cron schedules are expressed in a pattern listing seconds, minutes, hour, day of month, month, and day of week, respectively. Cron schedules are stored in a file called a Crontab (CRON TABle), thus the RTLS-VistA Interface Configuration tool field is called Crontab. The format of the Crontab field in the tool is as follows:

> Each of the sections in the crontab field is separated by a space, with the final section allowing one or more spaces. No spaces are allowed within sections 1-5, only between them. The example below represents a job that runs at 3AM every day. For example:

![](en-version-7-rtls-enhancement-interfaces-manual/007.png)

#### Crontab Field Syntax

> The following table provides a definition of each Crontab section.

| Section  | Definition                     |
|--------------|------------------------------------|
| Seconds      | 0 – 59                             |
| Minutes      | 0 - 59                             |
| Hour         | 0 – 23 where 0 represents midnight |
| Day of Month | 1 - 31                             |
| Month        | 1 - 12                             |
| Day of Week  | 0-6 where 0 represents Sunday      |

> The following table defines special characters allowed in the Crontab pattern.

| Special Characters | Description                                                                                                                                                                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Asterisk (\*)          | The asterisk (\*) represents every instance (i.e. every hour, every weekday, every month) of a time period.                                                                                                                                                       |
| Comma (,)              | Comma-separated values can be used to run more than one instance of a particular command within a time period. For example, Day of Month expressed as 2,5,22 represents a job that runs on the 2<sup>nd</sup>, 5<sup>th</sup>, and 22<sup>nd</sup> of each month. |
| Question Mark (?)      | Question mark is an alternative to ‘\*’. It is used instead of '\*' for leaving either day-of-month or day-of-week blank.                                                                                                                                         |
| Slash (/)              | The forward slash (/) represents increments of ranges. For example, "\*/3" in the hour field is equivalent to "0,3,6,9,12,15,18,21" because "\*" specifies 'every hour' but the "/3" means every 3 hours.                                                         |

#### Crontab Examples

> The following table provides examples to illustrate the flexibility of the Crontab scheduling pattern.

| Seconds | Minutes | Hour | Day of Month | Month | Day of Week | Execution Time                                                                   |
|-------------|-------------|----------|------------------|-----------|-----------------|--------------------------------------------------------------------------------------|
| 0           | 0/30        | \*       | \*               | \*        | ?               | Every 30 minutes every day                                                           |
| 0           | 0           | 0        | 1,10,15          | \*        | ?               | Midnight on the 1<sup>st</sup>, 10<sup>th</sup>, and 15<sup>th</sup> of every month. |
| 0           | 0           | 16       | \*               | \*        | 0               | Every Sunday at 4:00 PM                                                              |

#### Scheduling Considerations

> The following is a list of things to consider before you schedule a new job or modify an existing one:

- An understanding of the crontab functionality is crucial before adding or changing the frequency of jobs.
- An understanding of the payload for a job is crucial before changing the frequency.
- The Static Active Tagged Equipment Inventory and Static Passive Tagged Equipment Inventory jobs should not be scheduled for intervals of less than five minutes due to the amount of processing overhead and network traffic generated.
- Logging activity occurs each time the jobs are run. Logging levels (e.g. warnings vs. informational messages) are controlled by an RTLS administrator. The current logging levels of the system should be taken into consideration when scheduling the frequency of the jobs.

### Accessing the Snap-In within Intelligent InSites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS-VistA Interface Configuration Tool is a Snap-In on the Intelligent InSites user interface. In order to access the Snap-In, you’ll need a password and userid to access Intelligent InSites and a password and userid to access the WebLogic server. To access the snap-in, use the following steps:

1.  Login to Intelligent InSites. The Welcome page displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/008.png)

#### Figure 8: Function Role Selection

2.  Select the InSites Administrator check box and click Continue. The Intelligent InSites home page displays.

![](en-version-7-rtls-enhancement-interfaces-manual/009.png)

#### Figure 9: Intelligent InSites Home Page

3.  Click the Interface Apps tab.
4.  Enter the userid and password for the WebLogic server provided by the system administrator. The RTLS-VistA Interface Configuration Tool main page displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/010.png)

> Figure 10: RTLS-VistA Interface Configuration Tool

## Initial Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following tasks are part of the ESE RTLS installation and deployment. These tasks are only performed once as part of the initial deployment of a facility.

### Adding a VISN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Adding a VISN (i.e. Network) is only necessary when the facility you are deploying is the first facility within a VISN to be deployed. If your facility is not the first and the VISN is defined, go to section [13.2.2](#adding-a-va-facility-definition) [Adding a VA Facility definition.](#adding-a-va-facility-definition) To add a VISN, use the following steps:

5.  From the RTLS-VistA Interface Configuration Tool main page, click Add Network.

> The Add VISN screen displays. The InSites Scheme and InSites Port fields are pre-populated.

> ![](en-version-7-rtls-enhancement-interfaces-manual/011.png)

#### Figure 11: Add VISN

6.  Enter the VISN Name provided by the VA.
7.  Enter the 3-digit VISN Number provided by the VA.
8.  Enter the InSites Host URL provided by Intelligent InSites.
9.  Enter the InSites User name provided by Intelligent InSites.
10. Enter the password associated with the InSites user name.
11. Click Save.

### Adding a VA Facility definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add or associate a VA Facility (i.e. Network) with a VISN, use the following steps:

1.  From the RTLS-VistA Interface Configuration Tool main page, click Edit within the Actions area of the VISN.

> The Display Network screen displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/012.png)

#### Figure 12: Display Network

2.  From the Display Network screen, click Add Site. The Add Site screen displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/013.png)

#### Figure 13: Add Site

> The VISN field is pre-populated.

3.  Enter the Campus Name provided by the VA (e.g. Omaha, NE).
4.  Enter the Station number.
5.  Enter the VistA Instance number.
6.  Next to Active, click True to activate the facility.
7.  Click Save.

### Adding a Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are multiple jobs that comprise the feature set of the AEMS-MERS Intelligent-InSites interface. The RTLS-VistA Interface Configuration Tool connects to a Linux job scheduling software utility called cron to schedule jobs. Before adding a new job, it’s important to have a strong understanding of the crontab function. For more information, see [13.1.2](#understanding-the-job-scheduling-mechanism) Understanding the job scheduling mechanism. All jobs can be added using the following steps:

1.  From the RTLS-VistA Interface Configuration Tool main page, click View within the Actions area of the VISN.

> The Display Site screen displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/014.png)

#### Figure 14: Display Site

2.  Click Add Job

> The Add Job screen displays.

![](en-version-7-rtls-enhancement-interfaces-manual/015.png)

#### Figure 15: Add Job

> The Station number is pre-populated.

3.  Select the Job type.
4.  Enter a description in the Description field.
5.  Enter the VistA instance number in the VistA Instance field. The VistA instance number is the first three-digits of the Station number.
6.  Enter the Cron schedule in the CronTab field.
7.  Next to Active, click True to activate the job.
8.  Click Save.

## Managing Existing Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections represent tasks necessary for maintaining the AEMS-MERS/RTLS interface jobs.

### Modifying a Job Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A job may need to have a schedule adjustment. The RTLS-VistA Interface Configuration Tool connects to a Linux job scheduling software utility called cron to schedule jobs. Before making a schedule adjustment, it’s important to have a strong understanding of the crontab function. For more information, see [13.1.2](#understanding-the-job-scheduling-mechanism) Understanding the job scheduling mechanism.

> To change an existing job, use the following steps:

1.  From the RTLS-VistA Interface Configuration Tool main page, click View within the Actions area of the VISN.

> The Display Site screen displays.

![](en-version-7-rtls-enhancement-interfaces-manual/016.png)

#### Figure 16: Display Site

2.  In the Jobs area, click Edit next to the job. The Edit Job screen displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/017.png)

#### Figure 17: Edit Job

3.  Modify the field(s).
4.  Click Save.

### Running a Job on Demand

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On very rare occasions, a job may need to be run on demand. Before running a job on demand, make sure you understand the network implications and associated payload, see Section [13.1.2.3 Scheduling](#scheduling-considerations) [Considerations](#scheduling-considerations) for more information. To run a job on demand, use the following steps:

1.  From the RTLS-VistA Interface Configuration Tool main page, click View within the Actions area of the VISN.

> The Display Site screen displays.

2.  In the Jobs area, click View next to the job. The Display Job screen displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/018.png)

#### Figure 18: Display Job

3.  Ensure the Active field is set to true.
4.  Click Run Now.

> A confirmation message is displayed.

### Suspending a Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There may be occasions when a job needs to be temporarily suspended (e.g. due to system maintenance). To suspend an active job, use the following steps:

1.  From the RTLS-VistA Interface Configuration Tool main page, click View within the Actions area of the VISN.

> The Display Site screen displays.

2.  In the Jobs area, click Edit next to the job. The Edit Job screen displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/019.png)

#### Figure 19: Edit Job

3.  Next to the Active field, click False.
4.  Click Save.

### Deleting a Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Deleting a job is done immediately and the job definition cannot be recovered. Exercise this option with caution. Use the following steps to delete a job:

1.  From the RTLS-VistA Interface Configuration Tool main page, click View within the Actions area of the VISN.

> The Display Site screen displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/020.png)

#### Figure 20: Display Site

2.  In the Jobs area, click Delete next to the job. The job is deleted.

## Managing an Existing VA Facility Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections represent tasks necessary for modifying or deleting a VA Facility definition from the RTLS-VistA Interface Configuration Tool.

### Modifying a VA Facility Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A parameter related to the VA Facility definition may need to be changed. To change an existing facility definition, use the following steps:

1.  From the RTLS-VistA Interface Configuration Tool main page, click View in the Actions area. The Display Network screen displays.

> ![](en-version-7-rtls-enhancement-interfaces-manual/021.png)

#### Figure 21: Display Network

2.  In the Sites area, click Edit next to the site. The Edit Site screen displays.

![](en-version-7-rtls-enhancement-interfaces-manual/022.png)

#### Figure 22: Edit Site

3.  Change the field(s).
4.  Click Save.

### Deleting a VA Facility Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Deleting a VA Facility definition (i.e. Site) from the tool is done immediately and the jobs associated with the facility are also deleted. The VA Facility definition cannot be recovered. Exercise this option with caution. Use the following steps to delete a site:

1.  From the RTLS-VistA Interface Configuration Tool main page, click View within the Actions area of the VISN.

> The Display Network screen displays.

![](en-version-7-rtls-enhancement-interfaces-manual/023.png)

#### Figure 23: Display Network

2.  In the Sites area, click Delete next to the site. The site is deleted.

# Appendix B: Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections provide information on potential operational issues within the RTLS system. The content is divided into two main sections based on the underlying technologies employed. The RTLS Interface Applications cover the four interfaces related to VistA, WebLogic, and the Mule ESB flows.

> The CART-CL/WaveMark Interface section covers the CART-CL/WaveMark interface.

## RTLS Interface Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS Interface Applications orchestrate specific Mule ESB process flows to support the following functional areas:

- AEMS-MERS Equipment synchronization with RTLS
- GIP Inventory Supply synchronization with WaveMark
- Search of VistA employee data for use within the WaveMark system
- Search of VistA patient demographic data for use within the WaveMark system

### Understanding the Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS Interface Applications use a Java logging framework called log4j. The log files are defined in the log4j.properties file and also included below for convenience. The log4j.properties file can be used to configure different logging levels for each RTLS interface component and also to enable and disable logging as needed. The log files capture information about exceptions that arise while running the application.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Log File</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/data/rtls/vistasvcs/{env}/log/rtls.log</td>
<td>WebLogic log file.</td>
</tr>
<tr class="even">
<td>/data/mule/{env}/logs/mule_ee.log</td>
<td>Mule ESB log file.</td>
</tr>
<tr class="odd">
<td>/data/mule/{env}/logs/{flowname}.log</td>
<td><p>The following interfaces have log files:</p>
<ul>
<li><p>AEMS-MERS/Intelligent InSites</p></li>
<li><blockquote>
<p>Employee/WaveMark</p>
</blockquote></li>
<li><blockquote>
<p>Patient/WaveMark</p>
</blockquote></li>
<li><blockquote>
<p>GIP/WaveMark</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

> Note: In the log file names above, {env} represents an environmental variable set during installation.

> {flowname} represents the interface job flow name.

### Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The interfaces employ Mule ESB and the WebLogic-based Vista Service RESTful Web Services. Mule ESB and VistaService capture details of runtime errors in the log4j files. The following table is provided as a reference to possible RTLS Interface Application exceptions.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 29%" />
<col style="width: 23%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Interface</strong></th>
<th><strong>Issue</strong></th>
<th><strong>Possible Cause</strong></th>
<th><strong>Solution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>AEMS-</p>
<p>MERS/Intelligent Sites</p></td>
<td>A scheduled job failed.</td>
<td>Network connectivity issues.</td>
<td>Check the AEMS- MERS and Mule ESB log files. Scheduled jobs automatically retry using the same parameters during the next scheduled interval if the scheduler in unable to reach the Mule ESB. The jobs can also be run on demand, but this option should be exercised with extreme caution. See Section <a href="#appendix-a-rtls-vista-interface-configuration-tool">13</a> <a href="#appendix-a-rtls-vista-interface-configuration-tool">Appendix A: RTLS-</a> <a href="#appendix-a-rtls-vista-interface-configuration-tool">VistA Interface</a> <a href="#appendix-a-rtls-vista-interface-configuration-tool">Configuration Tool</a> for more information.</td>
</tr>
<tr class="even">
<td><p>AEMS-</p>
<p>MERS/Intelligent InSites</p></td>
<td>The Intelligent InSites user interface does not contain expected AEMS-MERS data.</td>
<td>Information is not available from AEMS- MERS or VistaServices encountered an unexpected condition that prevented it from fulfilling the request.</td>
<td>Check the AEMS- MERS log file. The input validation response codes are 404 for resource not found and 500 for all other failures.</td>
</tr>
<tr class="odd">
<td><p>AEMS-</p>
<p>MERS/Intelligent InSites</p></td>
<td>Update of a field in AEMS- MERS that contains a trigger for our interface does not get updated in Intelligent InSites.</td>
<td>Communication issue with Mule ESB.</td>
<td><p>Check the PENDING RTLS EVENTS</p>
<p>(#6930) file to see if the missing update exists within the file. The PENDING RTLS</p>
<p>EVENTS file introduces a redundancy to save record changes that could not be sent to RTLS when the Mule server is offline for any reason. If the missing update exists in the file, then the MAKE WEB CALL TO MULE</p>
<p>TaskMan option is possibly not running, and needs to be restarted. Restart the</p>
<p>TaskMan option. If the</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 29%" />
<col style="width: 23%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Interface</strong></th>
<th><strong>Issue</strong></th>
<th><strong>Possible Cause</strong></th>
<th><strong>Solution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>option fails again, contact the VistA Administrator.</td>
</tr>
<tr class="even">
<td>Employee/WaveMark</td>
<td>Employee not found message is displayed through the WaveMark User Interface.</td>
<td>Employee name is not found in NEW PERSON file.</td>
<td>Check the spelling of the last name. If the spelling is correct and the employee name is still not found, add the employee manually to the list. For information on how to add employees to the WaveMark interface, see the VA WaveMark User’s Manual.</td>
</tr>
<tr class="odd">
<td>Employee/WaveMark</td>
<td>Employee search failure other than Employee not found.</td>
<td>Possible erroneous http request, an internal http server error, or a network connectivity error.</td>
<td>Check the Employee log file. Response code 400 represents a bad request being passed through the interface and 500 represents an internal service error. Check for network connectivity.</td>
</tr>
<tr class="even">
<td>Patient/WaveMark</td>
<td>Patient not found message is displayed through the WaveMark User Interface.</td>
<td>PATIENT file record is not available in VistA</td>
<td>Check the Patient log file. Response code 404 represents not patient not found in the VistA file. CathLab procedure cannot continue without the patient’s identity being verified through the WaveMark user interface.</td>
</tr>
<tr class="odd">
<td>Patient/WaveMark</td>
<td>Patient search failure other than Patient not found.</td>
<td>Possible erroneous http request, an internal http server error, or a network connectivity issue.</td>
<td><p>Check the Employee log file and the Mule ESB log file. Response code 400 represents a bad request being passed through the interface and 500 represents an internal service error.</p>
<p>Check for network connectivity.</p></td>
</tr>
<tr class="even">
<td>GIP/WaveMark</td>
<td>ItemMasterUpdate process failure.</td>
<td>ItemMasterUpdate process failure.</td>
<td>Check the Muleitemmaster.log</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 29%" />
<col style="width: 23%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Interface</strong></th>
<th><strong>Issue</strong></th>
<th><strong>Possible Cause</strong></th>
<th><strong>Solution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>file and the Mule mule_ee.log log file. Response code 500 represents a failure of the ItemMasterUpdate process. The Vista Service rtls.log can provide additional details.</td>
</tr>
<tr class="even">
<td>GIP/WaveMark</td>
<td>Failure of the OnHandLink processes (i.e. Usage Feed and True Up Feed)</td>
<td>Failure of the OnHandLink processes (i.e. Usage Feed and True Up Feed)</td>
<td>Check the Muleonhandlink.log file and the Mule mule_ee.log file. Any response other than 202 is a failure. Response code 202 represents a successful upload. The Vista Service rtls.log can provide additional details</td>
</tr>
<tr class="odd">
<td>GIP/WaveMark</td>
<td>Failure of the OnHandLink processes (i.e. Usage Feed and True Up Feed)</td>
<td><p>Record in GENERIC INVENTORY (445)</p>
<p>file is locked by another user in GIP.</p></td>
<td><p>Check to make sure the record is no longer locked and re-run the feed. Consider re- scheduling the feeds to run beyond normal working hours to reduce the chance of another record locking event.</p>
<p>The Vista Service rtls.log can provide additional details on a locked GIP record.</p></td>
</tr>
</tbody>
</table>

## CART-CL/WaveMark Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CART-CL/WaveMark interface allows the WaveMark system to directly pass specific information related to the WaveMark encounter to a pair of SQL Server staging tables created in CART-CL exclusively for this purpose.

### Understanding the High Level Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The scheduler in the WaveMark Interface Engine is responsible for dispatching the CART-CL/WaveMark interface. Once an instance of EncounterLink has been dispatched, it will go through the following high level operations:

1.  Query the WaveMark Engine for all encounters that have not been sent to CART-CL.
2.  Translate the data into a series of SQL inserts.
3.  Establish a JDBC connection to the CART-CL CART_RTLS database.
4.  Send the data to CART-CL in the form of SQL inserts. WaveMark’s EncounterLink (i.e. ELCART0001) is aware of the status of all interface operations. In the event that data fails to be sent from WaveMark to CART-CL, EncounterLink will ensure that the dropped/failed encounter is resent.
5.  Commit the data.

### Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The connection between CART-CL and WaveMark is initiated by the WaveMark system. Errors are logged in the WaveMark Interface Engine user interface (UI). The WaveMark Interface Engine UI provides information about the interface that generated the error, a description of the error, a timestamp for when the error occurred, and a severity.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Issue</strong></th>
<th><strong>Possible Cause</strong></th>
<th><strong>Solution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Connection between WaveMark components is unavailable due to loss of power or connectivity.</td>
<td>Failure to query the WaveMark engine.</td>
<td>A retry mechanism is implemented and controlled using a backend settings file. The query to the WaveMark Engine will be attempted three times. If all three attempts fail, an error is logged. Escalate the issue as appropriate.</td>
</tr>
<tr class="even">
<td>Connection between WaveMark and CART-CL is unavailable.</td>
<td>Failure to establish a JDBC connection to CART-CL.</td>
<td>Check the WaveMark Interface Engine user interface for a listing of the error, a description of the error, and the date and time the error occurred. Escalate the issue as appropriate.</td>
</tr>
<tr class="odd">
<td>Connection between WaveMark and CART-CL is unavailable due to loss of power or connectivity.</td>
<td>Failure to send the data to CART-CL.</td>
<td><blockquote>
<p>All sent encounters during this session are rolled back, and an error is logged. Check the WaveMark Interface Engine user interface for a listing of the error, a description of the error, and the date and time the error occurred. Escalate the issue as appropriate.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Frequently Asked Questions (FAQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For a list of Frequently Asked Questions, see the RTLS ESE Installation Guide.