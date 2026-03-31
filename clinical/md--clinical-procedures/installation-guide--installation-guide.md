---
consolidated_title: "installation guide"
app_code: MD
doc_type: IG
master_source: "MD*1*26 Installation Guide (CP Flowsheets)"
master_pub_date: August 2011
consolidated_from: 6 versions
prior_versions:
  - "MD*1*66 Installation Guide (Hemodialysis)"
  - "MD*1*70 Installation Guide (Hemodialysis)"
  - "MD*1*71 Installation Guide (User)"
  - "MD*1*75 Installation Guide (Hemodialysis)"
  - "MD*1*76 Installation Guide (CP Flowsheets)"
---

> ![](md-1-26-installation-guide-cp-flowsheets/001.png)

> CLINICAL PROCEDURES (CP) V1.0 FLOWSHEETS MODULE INSTALLATION GUIDE

> MD\*1.0\*26

> August 2011

> Department of Veterans Affairs Office of Information & Technology (OI&T)

> Product Development (PD)

> Revision History

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 20%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Patch MD*1.0*16 released.</p>
</blockquote></td>
<td><blockquote>
<p>May 2011</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Corrected filename in section 3 "Installing</p>
<p>the KIDS Build” and searched entire document for same error.</p>
</blockquote></td>
<td><blockquote>
<p>July 2011</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Changed all references of MD1_0P16_Gateway_Installer.exe to MD1_0P16CPGatewayServiceSetup.exe.</p>
</blockquote></td>
<td><blockquote>
<p>July 2011</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Section 4.3 – moved step 4 above figure 4-2</p>
<p>for more logical ordering. Section 4.6 – moved note to the top of step 1.</p>
</blockquote></td>
<td><blockquote>
<p>July 2011</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Removed note about password protected file from section 5.2 “ CP Flowsheets”, and</p>
<p>revised text in first paragraph.</p>
</blockquote></td>
<td><blockquote>
<p>July 2011</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> *This page intentionally left blank for double-sided printing.*

1.  [Introduction 1](#introduction)
    1.  [Overview 1](#overview)
        1.  [CP Gateway Service 1](#cp-gateway-service)
        2.  [The CP Gateway Service ADT System 2](#the-cp-gateway-service-adt-system)
        3.  [CliO Database 2](#clio-database)
        4.  [Terminology Mapping 2](#terminology-mapping)
    2.  [CP Flowsheets 3](#cp-flowsheets)
    3.  [CP Console 3](#_bookmark7)
    4.  [Using This Manual 3](#_bookmark8)
    5.  [How Much Do I Need to Install? 4](#_bookmark9)
2.  [Preinstallation 5](#_bookmark10)
    1.  [Installation Prerequisites 5](#_bookmark11)
    2.  [General MD\*1.0\*16 Installation Flow 5](#_bookmark12)
    3.  [Obtaining the Clinical Flowsheets Installation Files 6](#_bookmark13)
    4.  [System Requirements 7](#_bookmark14)
    5.  [Setting up the Global Placement 9](#_bookmark15)
    6.  [Other Considerations 9](#_bookmark16)
3.  [Installing the KIDS Build 11](#_bookmark17)
4.  [Post-KIDS Configuration 19](#post-kids-configuration)
    1.  [Creating a Service Account for CP Gateway Service 19](#creating-a-service-account-for-cp-gateway-service)
    2.  [Configuring User Roles By Assigning Menu Options and Keys 21](#configuring-user-roles-by-assigning-menu-options-and-keys)
    3.  [Configuring the Inbound HL7 Feed 22](#configuring-the-inbound-hl7-feed)
    4.  [Configuring the PROTOCOL File for ADT Feed 24](#configuring-the-protocol-file-for-adt-feed)
    5.  [Step 4: Configuring the VDEF for ADT Feed 25](#step-4-configuring-the-vdef-for-adt-feed)
    6.  [Step 5: Configuring the outbound ADT Feed 27](#step-5-configuring-the-outbound-adt-feed)
5.  [Installing the CP Flowsheets and CP Console Clients 33](#installing-the-cp-flowsheets-and-cp-console-clients)
    1.  [CP Console 33](#cp-console)
    2.  [CP Flowsheets 34](#cp-flowsheets-1)
    3.  [Backout Plan 34](#backout-plan)
6.  [Installing the CP Gateway Service 37](#installing-the-cp-gateway-service)
    1.  [Running the Gateway Installer 38](#running-the-gateway-installer)
    2.  [Verifying the CP Gateway Service 42](#verifying-the-cp-gateway-service)
    3.  [Manually Registering the CP Gateway Service 44](#manually-registering-the-cp-gateway-service)
    4.  [Configuring the CP Gateway Service 44](#configuring-the-cp-gateway-service)
    5.  [Configuring ADT Feed Subscriptions 47](#configuring-adt-feed-subscriptions)
    6.  [Starting the CP Gateway Service 50](#starting-the-cp-gateway-service)
7.  [Post Installation 53](#post-installation)
    1.  [Adding Command Line Switches 53](#adding-command-line-switches)
    2.  [Add CP Flowsheets to the CPRS Tools Menu (ORWT TOOLS MENU) 54](#add-cp-flowsheets-to-the-cprs-tools-menu-orwt-tools-menu)
8.  [FAQ 57](#faq)
9.  [Glossary 59](#glossary)

> *This page intentionally left blank for double-sided printing.*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
    - [CP Gateway Service](#cp-gateway-service)
    - [The CP Gateway Service ADT System](#the-cp-gateway-service-adt-system)
    - [CliO Database](#clio-database)
    - [Terminology Mapping](#terminology-mapping)
  - [CP Flowsheets](#cp-flowsheets)
- [Post-KIDS Configuration](#post-kids-configuration)
  - [Creating a Service Account for CP Gateway Service](#creating-a-service-account-for-cp-gateway-service)
  - [Configuring User Roles By Assigning Menu Options and Keys](#configuring-user-roles-by-assigning-menu-options-and-keys)
  - [Configuring the Inbound HL7 Feed](#configuring-the-inbound-hl7-feed)
  - [Configuring the PROTOCOL File for ADT Feed](#configuring-the-protocol-file-for-adt-feed)
  - [Step 4: Configuring the VDEF for ADT Feed](#step-4-configuring-the-vdef-for-adt-feed)
  - [Step 5: Configuring the outbound ADT Feed](#step-5-configuring-the-outbound-adt-feed)
- [Installing the CP Flowsheets and CP Console Clients](#installing-the-cp-flowsheets-and-cp-console-clients)
  - [CP Console](#cp-console)
  - [CP Flowsheets](#cp-flowsheets-1)
  - [Backout Plan](#backout-plan)
- [Installing the CP Gateway Service](#installing-the-cp-gateway-service)
  - [Running the Gateway Installer](#running-the-gateway-installer)
  - [Verifying the CP Gateway Service](#verifying-the-cp-gateway-service)
  - [Manually Registering the CP Gateway Service](#manually-registering-the-cp-gateway-service)
  - [Configuring the CP Gateway Service](#configuring-the-cp-gateway-service)
  - [Configuring ADT Feed Subscriptions](#configuring-adt-feed-subscriptions)
  - [Starting the CP Gateway Service](#starting-the-cp-gateway-service)
- [Post Installation](#post-installation)
  - [Adding Command Line Switches](#adding-command-line-switches)
  - [Add CP Flowsheets to the CPRS Tools Menu (ORWT TOOLS MENU)](#add-cp-flowsheets-to-the-cprs-tools-menu-orwt-tools-menu)
- [FAQ](#faq)
- [Glossary](#glossary)
> This *Clinical Procedures (CP) V1.0 Flowsheets Module Installation Guide* provides information for Information Resource Management (IRM) personnel to install and configure the components of Clinical Flowsheets (MD\*1.0\*16).

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Clinical Flowsheets patch of the CP package provides an electronic representation of the traditional paper flowsheet maintained during each inpatient stay. Vitals, Intake/Output, Wound Documentation, etc., are examples of data types that can be recorded via Clinical Flowsheets into the Veterans Health Information System and Technology Architecture (VistA) system. Clinical Flowsheets provides a departure from its predecessor applications by storing collected information as discrete data. Some date elements, such as vital signs, are available to the Vitals Package and Computerized Patient Record System (CPRS). Various reports built on the other data elements are available for CPRS in the form of Text Integration Utilities (TIU) Notes.

> There are two ways to enter data into Clinical Flowsheets: manually and via Health Level 7 (HL7) messaging. Any instrument or external system capable of sending HL7 messages is considered a source of data for Clinical Flowsheets (provided that the HL7 messages conform to Clinical Flowsheets requirements).

> Clinical Flowsheets uses VistA Data Extraction Framework (VDEF) support, HL7 messaging, and the CP Gateway service to notify the medical device of the patient’s admission, discharge, and transfer.

> The Clinical Flowsheets patch consists of the following three Graphical User Interface (GUI) components and one (1) Kernel Installation & Distribution System (KIDS) build:

> ![](md-1-26-installation-guide-cp-flowsheets/002.png) CP Console

> ![](md-1-26-installation-guide-cp-flowsheets/003.png) CP Flowsheets

> ![](md-1-26-installation-guide-cp-flowsheets/004.png) CP Gateway Service ![](md-1-26-installation-guide-cp-flowsheets/005.png) MD_1_P16.kid

> The CP Console component provides the tools to create the CP Flowsheets. Sites can begin this process following the installation.

> The CP Flowsheets application is available by request from the implementation team.

### CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CP Gateway Service is the component that processes HL7 messages.

> Unlike the Legacy CP Gateway, the new CP Gateway Service is a Windows service that will, by default, restart automatically when the system is restarted.

> The CP Gateway Service is composed of two subsystems, one existing solely within VistA, and the other existing as a Windows service that interacts with VistA by way of the Remote Procedure Call (RPC) Broker. Other systems send observations to VistA inside an HL7 (ORU^R01) inbound message. The message is received by the VistA HL7 system, the patient and device are validated after which the message is forwarded to the CP Gateway Service.

> The VistA CP Gateway subsystem parses and validates the patient-identifying information and the device identifier. If the patient information and device identifiers are valid, the Windows service is notified that there is a message waiting to be processed in VistA. The Windows service calls into VistA via the RPC Broker to retrieve the HL7 message. The Windows service then parses and validates the observation data and saves the validated information in the CliO data store.

### The CP Gateway Service ADT System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CP Gateway Service Admissions, Discharges, Transfers (ADT) system distributed within patch MD\*1.0\*16 allows Clinical Procedures to notify other systems when an admission, discharge or transfer occurs. This notification occurs via HL7, and allows these other systems to prepopulate their patient databases with patient demographic information as stored in VistA. This allows these other systems to guarantee the correctness of their patient information when they send clinical observations to CP.

> As part of patch MD\*1.0\*16, CP is distributing a subscriber protocol (MD DGPM PATIENT MOVEMENT). This protocol is registered as a subscriber to the Patient Information Management System (PIMS) event publisher protocol DGPM MOVEMENT EVENTS. When notified of a patient movement, MD DGPM PATIENT MOVEMENT stores information relevant to the patient movement in the CP_MOVEMENT_AUDIT file (#704.005).

> After this information is stored in the CP_MOVEMENT_AUDIT file, the VDEF processing task retrieves it and uses it to generate an appropriate ADT message. This message is then submitted to the HL7 system, which uses dynamic routing to determine to which logical link(s) the ADT message should be sent.

> The following three items require configuration for the ADT feed (event handling system) to work.

> ![](md-1-26-installation-guide-cp-flowsheets/006.png) PROTOCOL file (#101) ![](md-1-26-installation-guide-cp-flowsheets/007.png) VDEF

> ![](md-1-26-installation-guide-cp-flowsheets/008.png) HL7

### CliO Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CliO database provides a standardized terminology data store for all clinical observations throughout the Department of Veterans Affairs (VA).

### Terminology Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are 115 different Legacy interfaces for medical devices which are supported by the Office of Information & Technology (OI&T). These devices do not always use the same terms to describe the data they transmit. For example, one device may use the term “heart rate,” while another may transmit the same information as “pulse.” The CP Gateway provides extensive terminology mapping which translates such proprietary labels so the information is understood to represent the same thing and, thus, be stored appropriately. This is more efficient than trying to compel each medical device vendor to conform to using standard terminology.

> Similarly, CP Flowsheets can display the data to the user using the terminology that is preferred at a given unit or medical center. A flowsheet used by an Medical Intensive Care Unit (MICU) at one hospital can be customized to display “Heart Rate,” while a flowsheet used by a step-down unit may display “HR” or “Pulse.”

## CP Flowsheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Introduction

> CP Flowsheets provides an electronic representation of the traditional paper flowsheet. This user- friendly, customizable Graphical User Interface (GUI) provides functionality for data entry, validation and editing, as well as patient management.

> ![](md-1-26-installation-guide-cp-flowsheets/009.png) Based on the paper flowsheets used in Critical Care Units, Flowsheets provides electronic flowsheets that can be custom designed for any clinical area of a Medical Center.

> ![](md-1-26-installation-guide-cp-flowsheets/010.png) Flowsheets is a tool that allows clinicians to standardize assessment templates nationwide.

> ![](md-1-26-installation-guide-cp-flowsheets/011.png) Flowsheets provides the ability to report discreet observations data combined with progress notes. ![](md-1-26-installation-guide-cp-flowsheets/012.png) Flowsheets creates a complete audit trail of patient documentation.

1.  <span id="_bookmark7" class="anchor"></span>CP Console

> CP Console provides the tools to build the flowsheet views and layouts that are used in inpatient settings for patient care, for recording vital statistics as necessary. It also provides a means for configuring the CP Gateway, assigning permissions to CP Flowsheets users, and system administration.

> For more information about CP Console, refer to the *CP V1.0 Flowsheets Module Implementation Guide*.

2.  <span id="_bookmark8" class="anchor"></span>Using This Manual

> This manual guides the reader through a very specific order for installing and configuring the various components of Clinical Flowsheets. This section of the manual will explain the reasoning for that order.

> It is recommended that you follow this order because steps described in the later chapters are dependent upon certain previous steps.

> Chapter 2. Preinstallation: This chapter lists installation prerequisites. Please install the specified patches and/or packages before attempting to install Clinical Flowsheets.

> Chapter 2 also describes where you can download the files needed to install Clinical Flowsheets.

> Chapter 3. Installing the KIDS Build: This chapter provides a screen capture of the KIDS build installation process.

> Chapter 4. Post-KIDS Configuration: This chapter contains instructions for system and user configuration that occurs in VistA.

> Chapter 5. Installing the CP Gateway Service: This chapter walks the reader through the workflow to install the CP Gateway Service application. This involves running the MD1_0P16CPGatewayServiceSetup.exe file mentioned in Chapter 2..

> Chapter 6. Installing the CP Flowsheets and CP Console Clients: The chapter describes how to install the CP Flowsheets client application and the CP Console application.

> Chapter 7. Post Installation: This chapter introduces executable command line switches and how to add CP Flowsheets to the CPRS Tools menu.

> Chapter 8. FAQ: This chapter contains answers to frequently asked questions.

#### Chapter 9. Glossary

3.  <span id="_bookmark9" class="anchor"></span>How Much Do I Need to Install?

> Depending on your purposes for installing MD\*1.0\*16, you may not need to install all of the components described in this Installation Guide. Please follow these guidelines for determining which components you should install:

> ![](md-1-26-installation-guide-cp-flowsheets/013.png) If the site is not currently running Clinical Procedures, only the KIDS build needs to be installed.

> All other installation instructions and post-installs can be ignored.

> ![](md-1-26-installation-guide-cp-flowsheets/014.png) If the site is running Clinical Procedures and does not plan on implementing Clinical Flowsheets at this time, only the KIDS and CP Console (replacement for the current CP Manager) needs to be installed.

> ![](md-1-26-installation-guide-cp-flowsheets/015.png) If the site is running Clinical Procedures and wishes to begin the implementation of Clinical Flowsheets, then all four components need to be installed: KIDS, CP Console, CP Flowsheets and the new CP Gateway Service.

> ![](md-1-26-installation-guide-cp-flowsheets/016.png) Note: the CP Manager application is no longer supported after the installation of MD\*1.0\*16.

> Use CP Console to perform the functions previously provided by CP Manager.

1.  <span id="_bookmark10" class="anchor"></span>Preinstallation
    1.  <span id="_bookmark11" class="anchor"></span>Installation Prerequisites

> ![](md-1-26-installation-guide-cp-flowsheets/017.png) Clinical Flowsheets cannot be installed as a stand-alone application without CP. If this is a first-time installation, you must first install the CP package and released CP patches. For more information on installing CP, refer to the *CP V1.0 Flowsheets Module Installation Guide*.

> ![](md-1-26-installation-guide-cp-flowsheets/018.png) Although packaged separately, Clinical Flowsheets is part of the Clinical Procedures patch, MD\*1.0\*16. Thus, Clinical Flowsheet functionality cannot be installed without the Clinical Procedures application. If you do not have the Clinical Procedures (CP) package and all released CP patches prior to MD\*1.0\*16 are not installed, you must install them.

> ![](md-1-26-installation-guide-cp-flowsheets/019.png) Vitals Patch GMRV\*5.0\*22 and patches GMRV\*5.0\*23, MD\*1.0\*20, and MD\*1.0\*21 must be installed prior to the installation of patch MD\*1.0\*16.

> ![](md-1-26-installation-guide-cp-flowsheets/020.png) Coordinate the installation with the Nursing Automated Data Processing Application Coordinator (ADPAC), Medicine ADPAC, Information Resource Management Service (IRMS) and if applicable at your site, the Clinical Application Coordinator (CAC).

2.  <span id="_bookmark12" class="anchor"></span>General MD\*1.0\*16 Installation Flow

> The following flow diagram illustrates an overview of the basic flow of the MD\*1.0\*16 Installation.

![](md-1-26-installation-guide-cp-flowsheets/021.png)

> Figure 2-1, Installation Flow

3.  <span id="_bookmark13" class="anchor"></span>Obtaining the Clinical Flowsheets Installation Files

> There are three distribution files that are used to install the three Clinical Flowsheets components (CP Gateway Service, CP Console, and CP Flowsheets). There is also a configuration file containing the sample views. The distribution files are available for download from the Anonymous directories.

> File Transfer Protocol (FTP) Instructions:

> The file listed below may be obtained via FTP. The preferred method is to FTP the files from: <span class="mark">REDACTED</span>

> This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

> CIO FIELD OFFICE FTP ADDRESS DIRECTORY

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 40%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Albany</p>
</blockquote></th>
<th><blockquote>
<p><a href="ftp://ftp.fo-albany.med.va.gov/"><mark>Redacted</mark></a></p>
</blockquote></th>
<th>[anonymous.software]</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><blockquote>
<p><a href="ftp://ftp.fo-hines.med.va.gov/"><mark>Redacted</mark></a></p>
</blockquote></td>
<td>[anonymous.software]</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><blockquote>
<p><a href="ftp://ftp.fo-slc.med.va.gov/"><mark>Redacted</mark></a></p>
</blockquote></td>
<td>[anonymous.software]</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 36%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>File Name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Contents</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Retrieval Format</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>MD_1_P16.kid</strong></p>
</blockquote></td>
<td><blockquote>
<p>MD*1.0*16 KIDS Build</p>
</blockquote></td>
<td><blockquote>
<p>ASCII</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MD1_0P16_Sample_Views.xml</strong></p>
</blockquote></td>
<td><blockquote>
<p>Sample Views</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
</tbody>
</table>

> MD1_0P16CPGatewayServiceSetup.exe MD\*1.0\*16 CP Gateway Service setup file BINARY

> MD1_0P16_EXES_AND_DOC.zip 12 files indented below BINARY

> -CliO_Terminology.doc MD\*1.0\*16 Clinical Flowsheets Terminology file

> -CPConsole.cnt MD\*1.0\*16 CP Console online Help contents file

> -CPConsole.exe MD\*1.0\*16 CP Console Executable

> -CPConsole.hlp MD\*1.0\*16 CP Console online Help file

> -CPGatewayService.exe MD\*1.0\*16 CP Gateway Service Executable

> -MD_1_P16.KID MD\*1.0\*16 KIDS Build

> -MD_1_P16_IG.pdf MD\*1.0\*16 Clinical Procedures (CP) V1.0 Flowsheets Module

> Installation Guide

> -MD_1_P16_IMPG.pdf MD\*1.0\*16 Clinical Procedures (CP) V1.0 Flowsheets Module

> Implementation Guide

> -MD_1_P16_RN.pdf MD\*1.0\*16 Clinical Procedures (CP) V1.0 Flowsheets Module

> Release Notes

> -MD_1_P16_TM.pdf MD\*1.0\*16 Clinical Procedures (CP) Technical Manual and Package Security Guide

> -MD_1_P16_UM.pdf MD\*1.0\*16 Clinical Procedures (CP) V1.0 Flowsheets Module

> User Manual

> -RoboEx32.dll .DLL file required to access Help files MD1_0P16_Flowsheets.zip 4 files indented below BINARY Note: This file is available upon request from the implementation team.

> -CPFlowsheets.exe MD\*1.0\*16 CP Flowsheets Executable

> -CPFlowsheets.hlp MD\*1.0\*16 CP Flowsheets online Help file

> -CPFlowsheets.cnt MD\*1.0\*16 CP Flowsheets online Help contents file

> -RoboEx32.dll .DLL file required to access Help files

#### The CP Flowsheets.exe is not included within MD\*1\*16 as this executable is an optional and controlled roll out, managed by the Implementation Manager. A readiness checklist will be provided by the Implementation Manager when the site requests the CP Flowsheets.exe.

> To request the CP Flowsheets.exe, contact [<u>VA OIT OED ClinProc Implementation Support</u>](mailto:VAOITOEDClinProcImplementationSupport@va.gov).

4.  <span id="_bookmark14" class="anchor"></span>System Requirements

> Storage requirements for Clinical Flowsheets client installation:

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Type of Data</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Size</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Applications</p>
</blockquote></td>
<td><blockquote>
<p>&lt; 5MB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Help Files</p>
</blockquote></td>
<td><blockquote>
<p>&lt; 1MB</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Sites should reserve 1KB of storage space per observation for data that will accumulate. The vast majority of growth will occur in the OBS file (#704.117).

> The following describes the installation environment for Clinical Flowsheets on the VistA client workstation:

> ![](md-1-26-installation-guide-cp-flowsheets/022.png) Workstations must be running under Windows XP Professional. Refer to [<u>http://vaww.vairm.vaco.va.gov/vadesktop</u>](http://vaww.vairm.vaco.va.gov/vadesktop) for additional information on VA standard desktop configurations.

> ![](md-1-26-installation-guide-cp-flowsheets/023.png) Remote Procedure Call (RPC) Broker Workstation must be installed.

> ![](md-1-26-installation-guide-cp-flowsheets/024.png) The Clinical Context Object Workgroup (CCOW) runtime from Sentillion must be installed if CCOW functionality is desired. Please see your Information Resource Management (IRM) representative for the installation of CCOW.

> ![](md-1-26-installation-guide-cp-flowsheets/025.png) The workstation must be connected to the local area network.

> ![](md-1-26-installation-guide-cp-flowsheets/026.png) Administrator privileges are needed on any machine on which CP Gateway Service is installed.

> ![](md-1-26-installation-guide-cp-flowsheets/027.png)VistA Data Extraction Framework (VDEF) should be installed prior to MD\*1.0\*16

5.  <span id="_bookmark15" class="anchor"></span>Setting up the Global Placement

#### IMPORTANT

> A new global ^MDC will be built during the installation of the KIDS build. To avoid it being built in a perhaps incorrect default location it is necessary to have the system administrators create and place the ^MDC global on the proper volume set before the installation.

6.  <span id="_bookmark16" class="anchor"></span>Other Considerations

> ![](md-1-26-installation-guide-cp-flowsheets/028.png) Sites are recommended to install the software in test accounts prior to installing it in production accounts.

> ![](md-1-26-installation-guide-cp-flowsheets/029.png) Refer to the MD\*1.0\*16 Patch Description for information on verifying the KIDS build checksum before installing Clinical Flowsheets.

> ![](md-1-26-installation-guide-cp-flowsheets/030.png) MD\*1.0\*16 is released under a regular mandate. Once Patch MD\*1.0\*16 is released, sites have 30 days to install it; however, there is no mandatory date to implement it.

> ![](md-1-26-installation-guide-cp-flowsheets/031.png) This patch can be loaded with users on the system. Installing MD\*1.0\*16 will not affect any users on the system, including those using the pre-patch 16 Clinical Procedures system.

> ![](md-1-26-installation-guide-cp-flowsheets/032.png) Installation time is less than five minutes.

> Note: the time required to complete the post-install and to receive the MailMan message will vary depending on your system load.

> ![](md-1-26-installation-guide-cp-flowsheets/033.png) Installation of this patch should NOT BE QUEUED. ![](md-1-26-installation-guide-cp-flowsheets/034.png) Suggested time to install: non-peak requirement hours.

> ![](md-1-26-installation-guide-cp-flowsheets/035.png) The CP Console and CP Flowsheets components may be installed locally on individual workstations or remotely on a server that is operating 24/7.

> ![](md-1-26-installation-guide-cp-flowsheets/036.png) The CP Manager application is no longer supported after the installation of MD\*1.0\*16. Use CP Console to perform the functions previously provided by CP Manager.

> *This page intentionally left blank for double-sided printing.*

2.  <span id="_bookmark17" class="anchor"></span>Installing the KIDS Build
1.  To install the KIDS build, download MD1_0P16_EXES_AND_DOC.zip as instructed in step 2.3 above. Once the download is complete, unzip the file to C:\MD_INSTALL (or another location) and note that location. Copy the MD_1_P16.kid from this location and add it to the installation directory on the VistA server.

> Note: ASCII transfer format must be used for uploading the MD_1_P16.kid file from the local desktop to the installation directory on the VistA server.

2.  Programmer variables can be initialized by executing the command D ^XUP. Validate that DUZ(0)=”@”
3.  Use the KIDS installation menu option \[XPD MAIN\] and select Installation and then Load a Distribution to load the MD_1_P16.kid file onto your M system.
4.  Use the KIDS installation menu option \[XPD MAIN\] and select Installation and then Install Package(s) to install the distribution into your M system.
5.  Install or update the CP Gateway Service.

> Note: ASCII format must be used for downloading the MD_1_P16.kid file.

> The patch installation may pause, in some cases for several minutes, at the “installing new terminology” line of the patch installation. This is normal and the patch installation will continue after the terminology is installed.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 30%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>704.005</p>
</blockquote></th>
<th><blockquote>
<p>CP_MOVEMENT_AUDIT</p>
</blockquote></th>
<th rowspan="5"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>704.006</p>
</blockquote></th>
<th><blockquote>
<p>CP_PROTOCOL_LOCATION</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>704.007</p>
</blockquote></th>
<th><blockquote>
<p>CP_SHIFT</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>704.008</p>
</blockquote></th>
<th><blockquote>
<p>CP_SCHEDULE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>704.101</p>
</blockquote></th>
<th><blockquote>
<p>TERM</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>704.102</p>
</blockquote></td>
<td><blockquote>
<p>TERM_TYPE (including</p>
</blockquote></td>
<td><blockquote>
<p>data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.103</p>
</blockquote></td>
<td><blockquote>
<p>TERM_QUALIFIER_PAIR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.104</p>
</blockquote></td>
<td><blockquote>
<p>TERM_UNIT_CONVERSION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.105</p>
</blockquote></td>
<td><blockquote>
<p>TERM_UNIT_PAIR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.106</p>
</blockquote></td>
<td><blockquote>
<p>TERM_CHILD_PAIR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.107</p>
</blockquote></td>
<td><blockquote>
<p>TERM_RANGE_CHECK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.108</p>
</blockquote></td>
<td><blockquote>
<p>TERM_MAPPING_TABLE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.109</p>
</blockquote></td>
<td><blockquote>
<p>TERM_MAPPING_PAIR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.111</p>
</blockquote></td>
<td><blockquote>
<p>OBS_VIEW</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.1111</p>
</blockquote></td>
<td><blockquote>
<p>OBS_VIEW_TERMINOLOGY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.1112</p>
</blockquote></td>
<td><blockquote>
<p>OBS_VIEW_FILTER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.112</p>
</blockquote></td>
<td><blockquote>
<p>OBS_FLOWSHEET</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.1121</p>
</blockquote></td>
<td><blockquote>
<p>OBS_FLOWSHEET_PAGE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.1122</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_FLOWSHEET_SUPP_PAGE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.1123</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_FLOWSHEET_TOTAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.113</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_TOTAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.1131</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_TOTAL_TERMINOLOGY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.115</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_ALARM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.116</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_SET</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.1161</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_SET_OBS_PAIR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.117</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.118</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_QUALIFIER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.119</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OBS_AUDIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>704.121</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP_KARDEX_ACTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>704.1211</p>
<p>704.1212</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CP_KARDEX_EVENTS</p>
<p>CP_KARDEX_AUDIT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// ;;9999 TELNET TERMINAL

> Install Started for MD\*1.0\*16 : Mar 01, 2010@10:59:06

> Build Distribution Date: Feb 24, 2010

> Installing Routines:

> Mar 01, 2010@10:59:06

> Running Pre-Install Routine: ^MDPRE16 Removing existing Clinical Data Model files. MD\*1.0\*16 Pre-Init Tasks Done.

> Installing Data Dictionaries:

> Mar 01, 2010@10:59:15

> Installing Data:

> Mar 01, 2010@10:59:15

> Installing PACKAGE COMPONENTS:

> Installing SECURITY KEY

> Installing DIALOG

> Installing MAIL GROUP

> Installing HL LOGICAL LINK

> Installing HL7 APPLICATION PARAMETER

> Installing PROTOCOL

#### Note: If your site does not plan to implement Clinical Flowsheets and is installing MD\*1.0\*16 only because it is mandated to do so, you are not required to do anything beyond installing the KIDS build.

> *This page intentionally left blank for double-sided printing.*

# Post-KIDS Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before you begin using Clinical Flowsheets:

1.  Create a Service Account for the CP Gateway Service.
2.  Configure the user roles by assigning menu options and keys.

> Note: Items 3 – 7 are required only for sites using the CP Gateway Service for interfacing. Sites that will use the Clinical Flowsheets package only for manual entry should only be concerned with items 1 and 2.

3.  Configure the inbound HL7 feed.

> Note: If you are not going to be implementing Flowsheets, ignore step 4. If you have implemented CP Legacy and you are not implementing Flowsheets, continue with steps 5-7.

4.  Configure the PROTOCOLs.
5.  Configure the VistA Data Extraction Framework (VDEF).
6.  Configure the outbound Admission Discharge and Transfer (ADT) link and PROTOCOLs.
7.  Configure the outbound ADT subscriptions.

## Creating a Service Account for CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will need to create a generic account for the CP Gateway Service to use for connections to VistA.

> The CP Gateway Service uses the RPC Broker to communicate with the VistA server and therefore, requires an access code/verify code pair to connect.

1.  Assign this new service account RPC Broker Context for CP Gateway \[MDCP Gateway Context\] option as a secondary menu option ONLY and do not assign any primary menu so that interactive access will not be allowed for this account.
2.  Create a service account in the NEW PERSON file (#200) with access and verify codes. The first name should be USER and the last name CPGATEWAY. Ensure that the VERIFY CODE NEVER EXPIRES flag is SET for this user.

> ![](md-1-26-installation-guide-cp-flowsheets/037.png)

> Figure 4-1, Add User

> Note: Use FileMan or the ADD a New User option.

> ![](md-1-26-installation-guide-cp-flowsheets/038.png) NAME: CPGATEWAY, USER

> ![](md-1-26-installation-guide-cp-flowsheets/039.png) INITIAL: UC

> ![](md-1-26-installation-guide-cp-flowsheets/040.png) ACCESS CODE: *Determined locally by IRM* ![](md-1-26-installation-guide-cp-flowsheets/041.png) VERIFY CODE: *Determined locally by IRM* ![](md-1-26-installation-guide-cp-flowsheets/042.png) XUS Active User: YES

> ![](md-1-26-installation-guide-cp-flowsheets/043.png) SERVICE/SECTION: *Determined locally by IRM.*

> ![](md-1-26-installation-guide-cp-flowsheets/044.png) SECONDARY MENU OPTIONS: MDCP GATEWAY CONTEXT and MD CLIO

> The following screen capture demonstrates how the data you enter will appear:

> Important: After creating the CP Gateway user, you should attempt to log on to VistA with the access and verify codes you created in step 2. VistA should not allow you to complete the logon, but many VistA systems require a verify code change at the first logon. If your system has this requirement, it will prevent the CP Gateway service from starting until the verify code on the CP Gateway service account is changed.

## Configuring User Roles By Assigning Menu Options and Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In VistA, assign each Clinical Flowsheets user (including the service account CP Gateway user) the CliO Service Options \[MD CLIO\] option as a secondary menu option. See section 6.4, step 1 for details about configuring the CP Gateway.
2.  In VistA, give Clinical Flowsheets managers the MD MANAGER and MD ADMINISTRATOR

> keys.

> MD ADMINISTRATOR: This key gives the user complete access to all functions in CP Console and CP Flowsheets. Without this key, the user relies on permissions assigned to in CP Console. This user is typically an IRM or a Super CAC.

> MD MANAGER: This key gives the user rights to edit, audit, and rescind observations entered by other users. This key also gives rights to import views into CP Console. This user is typically a Nurse Manager or CAC.

> MD HL7 MANAGER: CP Flowsheets requires the VistA MD HL7 MANAGER role or the MD ADMINISTRATOR role to access the HL7 Monitor. Assign this role to a user who will assist with the HL7 messaging component of CP Flowsheets.

> MD READ-ONLY: Assign this role to a user to prevent them from entering data in Flowsheets. DO NOT assign MD READ-ONLY to a user concurrently with any role other than MD HL7 MANAGER. Doing so will lead to unpredictable results. A user with the MD READ-ONLY key may NOT log on to CP Console and will have limited functionality in CP Flowsheets.

> MD TRAINEE: Data entered into CP Flowsheets by a user with the MD TRAINEE key does not display on the flowsheet until it has been verified (on the Log Files tab) by any user who was not assigned the MD TRAINEE key.

> Note: If your site is going to use ONLY CP Flowsheets and not the CP Gateway Service, you can stop after section 4.1. Section 4.2 is not required.

## Configuring the Inbound HL7 Feed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ICU devices forward observation data to VistA inside HL7 (ORU^R01) inbound messages.

1.  Review the settings for the MDHL IN logical link for correctness and compatibility with the local environment.
2.  Edit the MDHL logical link.

<table>
<colgroup>
<col style="width: 84%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select OPTION NAME: HL MAIN MENU HL7 Main Menu</p>
<p>Event monitoring menu ...</p>
</blockquote></th>
<th rowspan="9"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Systems Link Monitor</p>
<p>Filer and Link Management Options ... Message Management Options ...</p>
<p>Interface Developer Options ...</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Site Parameter Edit</p>
<p>HLO HL7 (Optimized) MAIN MENU ...</p>
<p>Select HL7 Main Menu Option: INterface Developer Options</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>EA Application Edit</p>
<p>EP Protocol Edit</p>
<p>EL Link Edit</p>
<p>VI Validate Interfaces</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Reports ...</p>
<p>Select Interface Developer Options Option: EL Link Edit Select HL LOGICAL LINK NODE: MDHL IN</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>HL7 LOGICAL LINK</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>NODE: MDHL IN</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>INSTITUTION:</p>
<p>MAILMAN DOMAIN:</p>
<p>AUTOSTART: Enabled</p>
<p>QUEUE SIZE: 100</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>LLP TYPE: TCP DNS DOMAIN:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Scroll down to the Lower Level Protocol (LLP) TYPE settings and press \<Enter\>. The TCP settings for this logical link display ([Figure 4-2](#_bookmark22)).
4.  1Set the Transmission Control Protocol/Internet Protocol (TCP/IP) SERVICE TYPE to SINGLE LISTENER.

![](md-1-26-installation-guide-cp-flowsheets/045.png)

> <span id="_bookmark22" class="anchor"></span>Figure 4-2, TCP/IP Service Type

5.  Set the TCP/IP PORT to the port number of the HL7 target used by the 3<sup>rd</sup> party devices.
6.  Set the TaskMan STARTUP NODE according to local requirements.
7.  Start the logical link (in the background).

> 1 Patch MD\*1.0\*26 August 2011 Moved step 4 above figure 4-2.

## Configuring the PROTOCOL File for ADT Feed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: You only need to continue with the following steps if you are using ADT Outbound Messaging.

> Patch MD\*1.0\*16 exports a subscriber protocol, MD DGPM PATIENT MOVEMENT, that must be added to the ITEM multiple of the DGPM MOVEMENT EVENTS entry in the PROTOCOL file (#101). This allows the CP ADT feed to receive notification that a patient was admitted, discharged, or transferred.

> Note: Ensure that the logical links are started in the background, or it could take a long time to complete.

> The following capture shows how to add MD DGPM PATIENT MOVEMENT to the ITEM multiple:

> Note: When transporting the KIDS build, the MDC CPAN VS event driver protocol processing ID may initially be set to "debug". This may prevent ADT^A01 messages from going out.

> Important: As part of the installation process, it is recommended to edit the protocol and delete the processing ID.

> ![](md-1-26-installation-guide-cp-flowsheets/046.png)The following screen illustrates this step:

> Figure 4-3, Editing the Protocol

## Step 4: Configuring the VDEF for ADT Feed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: You will need to reactivate the VDEF APIs after installing ALL subsequent MD\*1.0\*16 builds.

1.  Select the VDEF Configuration and Status \[VDEF CONFIGURATION MENU\] option.
2.  Activate CP in the VDEF Custodial Package Activate/Inactivate \[VDEF Custodial Package\] option.
3.  Activate the CP APIs in the VDEF system. There are seven APIs that require activation. ![](md-1-26-installation-guide-cp-flowsheets/047.png) ADT-A01-CPAN

> ![](md-1-26-installation-guide-cp-flowsheets/048.png) ADT-A02-CPTP

> ![](md-1-26-installation-guide-cp-flowsheets/049.png) ADT-A03-CPDE![](md-1-26-installation-guide-cp-flowsheets/050.png) ADT-A08-CPUPI![](md-1-26-installation-guide-cp-flowsheets/051.png) ADT-A11-CPCAN![](md-1-26-installation-guide-cp-flowsheets/052.png) ADT-A12-CPCT![](md-1-26-installation-guide-cp-flowsheets/053.png) ADT-A13-CPCDE

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>VistA HL7 PROTOCOL</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Custodial Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>API Event Active Flag</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Extraction Program</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Event Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MDC CPAN VS</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL PROCEDURES</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>MDCA01</p>
</blockquote></td>
<td><blockquote>
<p>CLIO Admit/Visit Notification (A01)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MDC CPTP VS</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL PROCEDURES</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>MDCA02</p>
</blockquote></td>
<td><blockquote>
<p>CLIO Transfer a Patient (A02)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MDC CPDE VS</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL PROCEDURES</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>MDCA03</p>
</blockquote></td>
<td><blockquote>
<p>CLIO Discharge/End Visit (A03)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MDC CPUPI VS</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL PROCEDURES</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>MDCA08</p>
</blockquote></td>
<td><blockquote>
<p>CLIO Update Patient Info (A08)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MDC CPCAN VS</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL PROCEDURES</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>MDCA11</p>
</blockquote></td>
<td><blockquote>
<p>CLIO Cancel Admit Notice (A11)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MDC CPCT VS</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL PROCEDURES</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>MDCA12</p>
</blockquote></td>
<td><blockquote>
<p>CLIO Cancel Transfer (A12)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MDC CPCDE VS</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL PROCEDURES</p>
</blockquote></td>
<td><blockquote>
<p>ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p>MDCA13</p>
</blockquote></td>
<td><blockquote>
<p>CLIO Cancel Discharge (A13)</p>
</blockquote></td>
</tr>
</tbody>
</table>

4.  Activate each CP API.
5.  Repeat step 4 for each of the seven APIs.

> Confirm that the VDEF Maintenance request queue is running.

## Step 5: Configuring the outbound ADT Feed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HL7 system delivers ADT messages to vendor devices. Therefore, you need to generate a subscriber PROTOCOL and logical link for each device to which Clinical Flowsheets sends an ADT message. The subscriber PROTOCOL uses MDC ADT OUTBND as the application and uses the IP address and port number of the vendor server in the logical link.

1.  Add a logical link.

> 1Note: The TCP/IP address and port shown below should be replaced with those of *your site’s*

> medical device or the aggregating server of the medical device.

<table>
<colgroup>
<col style="width: 84%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Select OPTION NAME: HL MAIN MENU HL7 Main Menu</p>
<p>Event monitoring menu ... Systems Link Monitor</p>
<p>Filer and Link Management Options ... Message Management Options ...</p>
<p>Interface Developer Options ... Site Parameter Edit</p>
<p>HLO HL7 (Optimized) MAIN MENU ...</p>
<p>Select HL7 Main Menu Option: Interface Developer Options EA Application Edit</p>
<p>EP Protocol Edit</p>
<p>EL Link Edit</p>
<p>VI Validate Interfaces Reports ...</p>
<p>Select Interface Developer Options Option: EL Link Edit</p>
<p>Select HL LOGICAL LINK NODE: MDSPL001 (<strong>Note:</strong> This is an example based on a Spacelabs device. The actual link node name may differ based on the site’s device type.)</p>
<p>Are you adding 'MDSPL001' as a new HL LOGICAL LINK (the 85TH)? No// Y (Yes)</p>
<p>HL7 LOGICAL LINK</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NODE: MDSPL001 INSTITUTION:</p>
<p>MAILMAN DOMAIN:</p>
<p>AUTOSTART:</p>
<p>QUEUE SIZE: 10</p>
<p>LLP TYPE: TCP DNS DOMAIN:</p>
</blockquote></td>
<td rowspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7 LOGICAL LINK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table>

> 1 Patch MD\*1.0\*26 August 2011 Moved note to the top of step 1.

> The following figure shows additional suggested values for the logical link:

![](md-1-26-installation-guide-cp-flowsheets/054.png)

> Figure 4-4, Logical Link Values

2.  Add a subscriber PROTOCOL using the HL EDIT INTERFACE Option Name.

> Each subscriber PROTOCOL requires a unique name. In order to ensure this uniqueness, rules are used when generating a new PROTOCOL name. As new vendors are added, likewise PROTOCOL vendor abbreviations will be added.

> ![](md-1-26-installation-guide-cp-flowsheets/055.png)The first two letters of the name of the PROTOCOL are MD.

> ![](md-1-26-installation-guide-cp-flowsheets/056.png) Two or three characters of the name are based on the vendor name.

> ![](md-1-26-installation-guide-cp-flowsheets/057.png)The last three characters are a serial number starting with 001.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Vendor Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PROTOCOL Vendor Abbreviation</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>General Electric.</p>
</blockquote></td>
<td><blockquote>
<p>GE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Spacelabs</p>
</blockquote></td>
<td><blockquote>
<p>SPL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Philips</p>
</blockquote></td>
<td><blockquote>
<p>PHL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Picis</p>
</blockquote></td>
<td><blockquote>
<p>PIC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Clinicomp</p>
</blockquote></td>
<td><blockquote>
<p>CLI</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note: The above vendor abbreviations are specified for outbound ADT messages only - not inbound observation messages from third-party vendors. Not all vendors listed are necessarily interfaced with Clinical Flowsheets.

#### Example

> The PROTOCOL used with a Spacelabs device at a specific hospital is MDSPL001.

<table>
<colgroup>
<col style="width: 84%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select OPTION NAME: HL MAIN MENU HL7 Main Menu</p>
</blockquote></th>
<th rowspan="11"><blockquote>
<p>Insert</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Event monitoring menu ... Systems Link Monitor</p>
<p>Filer and Link Management Options ...</p>
<p>Message Management Options ...</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Interface Developer Options ... Site Parameter Edit</p>
<p>HLO HL7 (Optimized) MAIN MENU ...</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select HL7 Main Menu Option: Interface Developer Options EA Application Edit</p>
<p>EP Protocol Edit</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>EL Link Edit</p>
<p>VI Validate Interfaces Reports ...</p>
<p>Select Interface Developer Options Option: EP Protocol Edit</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select PROTOCOL NAME: MDSPL001</p>
<p>Located in the MD (CLINICAL PROCEDURES) namespace.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Are you adding 'MDSPL001' as a new PROTOCOL? No// Y (Yes) PROTOCOL ITEM TEXT: SPACELABS SERVER 1</p>
<p>PROTOCOL IDENTIFIER:</p>
<p>HL7 INTERFACE SETUP PAGE 1 OF 2</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>NAME: MDSPL001</p>
<p>DESCRIPTION (wp): (empty)</p>
</blockquote></th>
</tr>
<tr class="header">
<th><p>ENTRY ACTION:</p>
<p>EXIT ACTION:</p>
<blockquote>
<p>TYPE: subscriber</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Enter a code from the list. Choose from:</p>
<p>E event driver</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>S subscriber &lt;Edit the TYPE to be SUBSCRIBER</p>
<p>Press &lt;PF1&gt;H for help</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Press \<Enter\>. Control is sent to the HL7 Subscriber edit screen.

> Note: Once you enter the RECEIVING APPLICATION information (MDC ADT OUTBOUND xxx), you will see the full list of vendors noted in Step 2 . The xxx in the above field indicates the vendor type, which could be for example, PHL for Phillips.

4.  Activate the logical link.

> Note: Both Link Manager and Task Manager must be running.

> *This page intentionally left blank for double-sided printing.*

# Installing the CP Flowsheets and CP Console Clients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CP Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CP Console client application is released as part of Patch MD\*1.0\*16. The distribution file is available for download from the Anonymous directories. The patch distribution file name is MD1_0P16_EXES_AND_DOC.zip.

> Note: To configure the CP Gateway Service, you must install CP Console on the same server, before running CP Console to configure the CP Gateway Service.

> However, if you are not using the CP Gateway Service to receive data from a third party device, you do not have to install or configure it.

> To install the CP Console client, complete the following steps:

1.  Extract the compressed ZIP file MD1_0P16_EXES_AND_DOC.zip. It includes the following files:

> ![](md-1-26-installation-guide-cp-flowsheets/058.png) CPConsole.exe

> ![](md-1-26-installation-guide-cp-flowsheets/059.png) CliO_Terminology.doc![](md-1-26-installation-guide-cp-flowsheets/060.png) MD_1_P16_UM.doc![](md-1-26-installation-guide-cp-flowsheets/061.png) MD_1_P16_IG.doc

> ![](md-1-26-installation-guide-cp-flowsheets/062.png) MD_1_P16_IMPG.pdf

> ![](md-1-26-installation-guide-cp-flowsheets/063.png) MD_1_P16_RN.pdf![](md-1-26-installation-guide-cp-flowsheets/064.png) MD_1_P16_TM.pdf![](md-1-26-installation-guide-cp-flowsheets/065.png) CPConsole.hlp

> ![](md-1-26-installation-guide-cp-flowsheets/066.png)![](md-1-26-installation-guide-cp-flowsheets/067.png) CPConsole.cnt RoboEx32.dll

2.  Distribute the CPConsole.exe file. If you are installing the application onto individual workstations, usually the CPConsole executable file is placed in the following directory: C:\Program Files\VistA\Clinical Procedures.

> If a remote installation is chosen (by storing the application executables on a network rather than locally), you must create a link that reflects the target path. This link can then be distributed (copied) to workstations.

3.  The online Help files (files ending in .HLP and .CNT) and the .DLL file should go in a subdirectory of the folder where the executables are placed. Name this directory Help, for example C:\Program Files\VistA\Clinical Procedures\Help.

> Installing the CP Flowsheets and CP Console Clients

4.  The CliO_Terminology.doc should go in a subdirectory of the folder where the executables are placed. Name this directory Documents, for example C:\Program Files\VistA\Clinical Procedures\Documents.

## CP Flowsheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1The CP Flowsheets client application is released as part of Patch MD\*1.0\*16 but is available as a separate file. The distribution file name is MD1_0P16_Flowsheets.zip.

> To install the CP Flowsheets client, complete the following steps:

1.  Obtain and extract the compressed ZIP file MD1_0P16_Flowsheets.zip. It includes the following files:

> ![](md-1-26-installation-guide-cp-flowsheets/068.png) CPFlowsheets.exe![](md-1-26-installation-guide-cp-flowsheets/069.png) CPFlowsheets.hlp![](md-1-26-installation-guide-cp-flowsheets/070.png) CPFlowsheets.cnt![](md-1-26-installation-guide-cp-flowsheets/071.png) RoboEx32.dll

2.  Extract the CPFlowsheets.exe file. If you are installing the application onto individual workstations, usually the CPFlowsheets executable file is placed in the following directory: C:\Program Files\VistA\Clinical Procedures.

> If a remote installation is chosen (by storing the application executables on a network rather than locally), you must create a link that reflect the target path. This link can then be distributed (copied) to workstations.

3.  The online Help files (files ending in .HLP and .CNT) and the .DLL file should go in a subdirectory of the folder where the executables are placed. Name this directory Help, for example C:\Program Files\VistA\Clinical Procedures\Help.

## Backout Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Due to the complexity of the task step-by-step procedures for backing out the MD\*1.0\*16 patch are not provided here. The procedure is documented in the Production Operations Manual MD_1_P16_POM.doc.

> 1 Patch MD\*1.0\*26 August 2011 Removed note about password protected file from section 5.2 “ CP Flowsheets”, and revised text in first paragraph.

> To backout the installation, please create a Remedy Ticket or contact the Remedy Help Desk at <span class="mark">REDACTED</span>

> *This page intentionally left blank for double-sided printing.*

# Installing the CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CP Gateway Service is released as part of Patch MD\*1.0\*16. The patch distribution file is available for download from the Anonymous directories. The patch distribution includes the setup file

> 4MD1_0P16CPGatewayServiceSetup.exe.

#### Notes:

> ![](md-1-26-installation-guide-cp-flowsheets/072.png) A copy of the CP Console application MUST be installed on the same server as the CP Gateway Service in order to administer the CP Gateway Service. This is because the CP Gateway Service depends on information that is stored in the local system registry by the CP Console application.

> ![](md-1-26-installation-guide-cp-flowsheets/073.png) The CP Gateway Service does not replace or overwrite the previous CP Gateway, both Gateways can continue to be run and can run on the same system if desired. Any machine capable of running Windows Server 2003 will be sufficient to run the CP Gateway Service..

> ![](md-1-26-installation-guide-cp-flowsheets/074.png) You can only have one copy of the CP Gateway Service installed on a server because the server manages the connection properties in the system registry. If you want to run a CP Gateway Service in TEST and PRODUCTION, you will need two servers.

> To install the CP Gateway Service, complete the following steps:

1.  Run the “MD1_0P16CPGatewayServiceSetup.exe.” This will install CPGatewayService.exe. The installer will also stop, uninstall, and remove any prior installations of the CP Gateway Service. The installer will then attempt to start the updated CP Gateway service. (See “

> 4 Patch MD\*1.0\*26 August 2011 Changed all references of MD1_0P16_Gateway_Installer.exe to MD1_0P16CPGatewayServiceSetup.exe.

> Running the Gateway Installer” in this document.)

2.  Start the CP Gateway Service if this is a first-time installation or the service could not be started automatically.

## Running the Gateway Installer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section demonstrates the various screens of the MD1_0P16CPGatewayServiceSetup.exe file. This workflow assumes that you have already downloaded and extracted the MD1_0P16CPGatewayServiceSetup.exe file, as mentioned above. It also assumes that you have Administrator privileges on the system upon which you will be installing the CP Gateway. Administrator privileges are required to install the CP Gateway.

> To install The CP Gateway Service, do the following:

1.  Double-click the MD1_0P16CPGatewayServiceSetup.exe file. Please wait while the installer program extracts files and prepares your system. If you watch carefully, you will see three progress indicators display in turn. Once the extraction is complete, the first screen of the InstallShield Wizard displays (Figure 6-1).

![](md-1-26-installation-guide-cp-flowsheets/075.png)

> Figure 6-1, CP Gateway InstallShield Wizard

2.  Click Next. The ReadMe Information screen displays some notes about the current release (Figure 6-2).

> ![](md-1-26-installation-guide-cp-flowsheets/076.png)

> <span id="_bookmark32" class="anchor"></span>Figure 6-2, Readme Information

> Note: [Figure 6-2](#_bookmark32) is included as an example only. The Readme information details will change with each build.

3.  Optionally review the release notes, then click Next. The Destination Folder screen displays (Figure 6-3).

![](md-1-26-installation-guide-cp-flowsheets/077.png)

> <span id="_bookmark33" class="anchor"></span>Figure 6-3, Destination Folder

4.  The recommended location for the Clinical Flowsheets application files is C:\Program Files\VistA\Clinical Procedures. To choose a different location, click the Change button ([Figure 6-3](#_bookmark33)) and navigate to the desired folder (Figure 6-4), then click OK to close the Change Current Destination Folder window.

> ![](md-1-26-installation-guide-cp-flowsheets/078.png)

> Figure 6-4, Change Current Destination Folder

5.  Click Next to accept the folder name and continue. The Ready to Install the Program window displays (Figure 6-5).

![](md-1-26-installation-guide-cp-flowsheets/079.png)

> Figure 6-5, Installation Settings

6.  The installation settings display. Click Back to make changes, click Cancel to exit the wizard, or click Install to begin the installation. A window displays progress bars while you wait for the applications to be installed (Figure 6-6).

> ![](md-1-26-installation-guide-cp-flowsheets/080.png)

> Figure 6-6, Installation Status

7.  An Information popup displays a message that the Service was installed successfully. (Figure 6- 7). Click OK to close the information popup.

![](md-1-26-installation-guide-cp-flowsheets/081.png)

> Figure 6-7, Information Popup

8.  When installation is complete, the InstallShield Wizard Completed window displays (Figure 6-8). Click Finish to close the InstallShield Wizard.

> ![](md-1-26-installation-guide-cp-flowsheets/082.png)

> Figure 6-8, InstallShield Wizard Completed

## Verifying the CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Verify that the Gateway Installer (MD1_0P16CPGatewayServiceSetup.exe) registered the CP Gateway Service.

> In Windows, open the Services applet:

9.  Click Start.
10. Click Run. The Run dialog displays (Figure 6-9).
11. Type services.msc in the Open field.

![](md-1-26-installation-guide-cp-flowsheets/083.png)

> Figure 6-9, Run Dialogue

12. Click OK. The Services window opens (Figure 6-10).

> ![](md-1-26-installation-guide-cp-flowsheets/084.png)

> Figure 6-10, Services Window

13. Verify that “CP Gateway Service” is in the list ([Figure 6-11](#_bookmark35)). If it is not in the list, you must manually register it, as described in the next section “

> ![](md-1-26-installation-guide-cp-flowsheets/085.png)Manually Registering the CP Gateway Service.”

> <span id="_bookmark35" class="anchor"></span>Figure 6-11, CP Gateway Service

> Note: The very first time, it will not be started. Before it can be started, you must enter the CP Gateway Server settings in CP Console, as described in the section “Configuring the CP Gateway Service,” later in this chapter.

## Manually Registering the CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the CP Gateway Service was not successfully registered, you will need to register the service manually: In Windows, open a DOS window.

1.  Click Start.
2.  Click Run.
3.  In the Open text box, type cmd.
4.  Click OK. DOS window opens.
1.  Go to the directory where you installed CP Gateway. The default file location is c:\program files\VistA\Clinical Procedures\Gateway\\
2.  At the DOS prompt, type: CPGatewayService.exe /install

> An Information popup displays ([Figure 6-12](#_bookmark37)).

![](md-1-26-installation-guide-cp-flowsheets/086.png)

3.  <span id="_bookmark37" class="anchor"></span>Click OK.

> Figure 6-12, Information Popup

4.  To close the DOS window, type “exit” and press \<Enter\>.

> Note: If the installer hasn’t been configured yet, you need to configure before installing.

## Configuring the CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once you have verified that the CP Gateway Service was registered, you must configure it. You will only need to configure the CP Gateway Service once. Subsequent installations (even following uninstalls) will be able to use prior settings to achieve the connection.

> The CP Gateway Service must be installed and registered with Windows before you can configure it in CP Console.

1.  Login to CP Console using your access code/verify code pair.. The CP Gateway Configuration detail displays. ([Figure 6-13](#_bookmark39)).

> ![](md-1-26-installation-guide-cp-flowsheets/087.png)

> <span id="_bookmark39" class="anchor"></span>Figure 6-13, CP Gateway Configuration Details

2.  The VistA Server Settings field entries are stored on the workstation in the system registry. This allows the CP Gateway Service to connect at startup to the appropriate VistA system with which you are communicating. Type in the field entries.
    1.  Access Code of the site’s VistA service user account with the RPC Broker Context for CP Gateway \[MDCP Gateway Context\] option as a secondary menu
    2.  Verify Code of the site’s VistA service user account with the RPC Broker Context for CP Gateway \[MDCP Gateway Context\] option as a secondary menu
    3.  RPC Broker Port for the CP Gateway Service on the VistA server to which you are connecting the broker
    4.  IP Address of the VistA server
3.  Obtain the IP address for the Gateway Server Settings used by the VistA server to connect to your local service. You can get it from a few places, such as from a network administrator, from Network Control Panel settings, or from a Windows command screen, as described below.

> Note: It is required that you use a static IP address in the following format:

> *xxx.xxx.xxx.xxx*. [Figure 6-14](#_bookmark40) shows an example of an IP address: 10.3.31.72.

> *Optional* – One way to obtain the IP address on a Windows system is as follows:

1.  Click Start \| Run.
2.  Type cmd.
3.  Type ipconfig. A list displays that contains the IP address ([Figure 6-14](#_bookmark40)).

![](md-1-26-installation-guide-cp-flowsheets/088.png)

> <span id="_bookmark40" class="anchor"></span>Figure 6-14, IP Address

4.  The lower half of the CP Gateway Configuration screen ([Figure 6-13](#_bookmark39)) provides fields for you to enter the CP Gateway Server Settings. [Figure 6-15](#_bookmark41) provides a close up view of this screen area, along with sample entries.

![](md-1-26-installation-guide-cp-flowsheets/089.png)

> <span id="_bookmark41" class="anchor"></span>Figure 6-15, Gateway Server Settings

> The following list provides more detailed explanations of the various Gateway Server Settings.

1.  IP Address: Enter the workstation IP address on which the CP Gateway Service is installed
2.  Notify Port: This is the listening port of the local machine that opens when a message is sent to the workstation. The default is 8888.
3.  Log Level: Specify the amount of detail to log in the Windows Event Viewer for the CP Gateway Service.

> ![](md-1-26-installation-guide-cp-flowsheets/090.png) Critical – only severe errors

> ![](md-1-26-installation-guide-cp-flowsheets/091.png) Error – critical + errors that cause instability in the operation of the CP Gateway Service ![](md-1-26-installation-guide-cp-flowsheets/092.png) Warning – Critical + error + any items captured but that allow the CP Gateway Service to

> continue running

> ![](md-1-26-installation-guide-cp-flowsheets/093.png) Detail – critical + error + warning + detailed execution trail of everything that the CP Gateway Service does as it processes HL7 messages

4.  Log Directory: The directory in which the logs for the CP Gateway Service are stored. The default is C:\temp\\ and .\\ dumps them in the CP Gateway Service directory.
5.  Days To Retain Data: The number of days to retain successfully processed HL7 data before purging messages in the “In Processed” state.
6.  CP/Imaging Xfer Directory: This field is reserved for future use.
7.  Data Retrieval Mechanism: The source for data retrieval. The recommended setting is VistA Notification.
8.  Polling Interval: A field used only in Legacy polling applications.
5.  Click Save to store the settings. Next, you must start the CP Gateway Service.

## Configuring ADT Feed Subscriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The dynamic routing system (ADT feed) must be configured, so that HL7 knows to which system to deliver the ADT messages.

1.  Log in to CP Console, using your access code/verify code pair.
2.  Expand the CP Console tree view and click Parameters.
3.  Select CP ADT Feed Configuration. The CP ADT Feed Configuration detail displays with a list of current ADT targets.

> ![](md-1-26-installation-guide-cp-flowsheets/094.png)

> Figure 6-16, CP ADT Feed Configuration

4.  To add a new ADT target, click New. The Add ADT Target window displays.

![](md-1-26-installation-guide-cp-flowsheets/095.png)

> Figure 6-17, Add ATD Target

5.  From the PROTOCOL list, select a subscriber PROTOCOL name (such as MDGE001 or MDSPL001)

> Note: Do not select any PROTOCOL names that start with MDC_ADT.

6.  From the Division list, select either an entire division or a ward within a division. (This allows Clinical Flowsheets to filter outbound messages by patient location.)

> Note: Selecting an entire division will not enable all outbound ADT messaging for the entire division.

7.  In the PROTOCOL Link Name box, enter a name. We suggest following a naming convention that includes the PROTOCOL, the division, and the ADT event type (for example MDGE_SICU_A01)
8.  From the HL7 Event Type drop-down, select an ADT outbound message type.
9.  Click OK.

> Repeat steps 4-9 for each HL7 event type you need to link. Contact [<u>VA</u>](mailto:VAOITOEDClinProcImplementationSupport@va.gov) <u>OIT OED ClinProc</u> <u>Implementation Support</u> if you need a list of which ADT events can be accepted.

> ![](md-1-26-installation-guide-cp-flowsheets/096.png) A01 Admit/visit notification ![](md-1-26-installation-guide-cp-flowsheets/097.png) A02 Patient transfer

> ![](md-1-26-installation-guide-cp-flowsheets/098.png)![](md-1-26-installation-guide-cp-flowsheets/099.png) A03 Discharge/end visit ![](md-1-26-installation-guide-cp-flowsheets/100.png) A08 Update patient info ![](md-1-26-installation-guide-cp-flowsheets/101.png) A11 Cancel admission ![](md-1-26-installation-guide-cp-flowsheets/102.png) A12 Cancel transfer

> A13 Cancel discharge/end visit

## Starting the CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: Following the first installation, manually start the CP Gateway Service.

> Subsequent installations will generally be able to use previous settings and both register and start the service automatically as part of the install (MD1_0P16CPGatewayServiceSetup.exe).

> To manually start the service, do the following:

1.  In Windows, open the Services applet:
    1.  Click Start.
    2.  Click Run.
    3.  In the Open text box, type services.msc
    4.  Click OK. The Services window opens.
2.  Find “Clinical Procedures Gateway Service” in the list (Figure 6-18).

![](md-1-26-installation-guide-cp-flowsheets/103.png)

> Figure 6-18, Clinical Procedures Gateway Service

3.  Right-click “Clinical Procedures Gateway Service” and select Start. A progress window displays as the service starts (Figure 6-19).

> ![](md-1-26-installation-guide-cp-flowsheets/104.png)

> Figure 6-19, Clinical Procedures Gateway Progress

4.  When the progress window closes, the Services window redisplays. The status column in the Clinical Procedures Gateway row displays Started.

> *This page intentionally left blank for double-sided printing.*

# Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Adding Command Line Switches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets and CP Console both support command line switches to save users time when logging on. There is also a command line switch to suppress the use of CCOW, should you not wish to use it.

> Command line switches can be applied to Desktop icons, Start Menu items, or the command assigned to an item on the CPRS tools menu.

> The following command line switches are supported by these two applications: \[/server=*servername*\] \[/port=*listenerport*\] \[/noccow\]

> In the following example, the CP Flowsheets application will run without first requiring the user to select a server and port from the Connect To window (Figure 7-1):

> "C:\Program Files\VistA\Clinical Procedures\CPFlowsheets.exe" /server=Hines /port=9100

![](md-1-26-installation-guide-cp-flowsheets/105.png)

> Figure 7-1, Connect To window

> CP Flowsheets will bypass the Connect To window and directly display the VistA Sign-on window. Once the user enters Access and Verify Codes, CP Flowsheets will connect to the specified server and port. (The Open Patient window will display.)

> In the following example, the CP Flowsheets application will run without CCOW functionality: "C:\Program Files\VistA\Clinical Procedures\CPFlowsheets.exe" /noccow

> Once the user has logged onto VistA and the CP Flowsheets main screen displays, the status line displays the No CCOW icon and notification (Figure 7-2).

![](md-1-26-installation-guide-cp-flowsheets/106.png)

> Figure 7-2, No CCOW Status

> Switches:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 50%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Name</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
<th><blockquote>
<p>Abbreviation</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>/server</p>
</blockquote></td>
<td><blockquote>
<p>Specifies a VistA server to which you are connected.</p>
</blockquote></td>
<td><blockquote>
<p>/s</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>/port</p>
</blockquote></td>
<td><blockquote>
<p>Specifies an alternate listener port on the selected server.</p>
</blockquote></td>
<td><blockquote>
<p>/p</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/noccow</p>
</blockquote></td>
<td><blockquote>
<p>Prevents CCOW from running</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## Add CP Flowsheets to the CPRS Tools Menu (ORWT TOOLS MENU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can use the ORWT TOOLS MENU to set up access to CP Flowsheets from the CPRS Tools menu. You can set up the options for the site and then override them as appropriate at the division, service, and user levels. Here are some guidelines:

> ![](md-1-26-installation-guide-cp-flowsheets/107.png) Enter each item in the format, NAME=COMMAND.

> NAME is the name that displays on the menu, such as CP Flowsheets. If you want to provide keyboard access, you can also enter *&* in front of a letter, such as CP & Flowsheets.

> COMMAND is the directory path followed by the executable name.

#### Notes:

> ![](md-1-26-installation-guide-cp-flowsheets/108.png)

![](md-1-26-installation-guide-cp-flowsheets/109.png)

> You must surround a path that contains space characters, such as C:\Program Files\\.. with quotation marks. You can also include switches in the path. Here’s an example:

> CP Flowsheets=”C:\Program Files\Clinical Procedures\CPFlowsheets.exe”

> /cprs / s=%SRV /p=%PORT

> You can pass context-sensitive parameters, which are entered as placeholders, and then converted to the appropriate values at runtime. The placeholder parameter used with Clinical Procedures is:

> %DFN Indicates the DFN of the currently selected patient in CPRS. This parameter passes the current patient to Clinical Procedures. You can also use %DFN as a placeholder in other CP applications.

> %SRV Indicates the name of the server that CPRS is currently connected to. This parameter passes the current server name to Clinical Procedures. You can also use %SRV as a placeholder in other CP applications.

Post Installation

> %PORT Indicates the listener port that CPRS is currently communicating through. This parameter passes the current listener port to Clinical Procedures. You can also use

> %PORT as a placeholder in other CP applications.

> ![](md-1-26-installation-guide-cp-flowsheets/110.png) Command line switches, such as nonsharedbroker, can be used. Refer to the *CP Flowsheets Module Implementation Guide* “<u>Appendix A - CP Application Startup Options and Command</u> <u>Line Switches</u>,” for more information.

> Example: Create a tools menu option that contains CP Flowsheets. From the system prompt, do the following:

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 8%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>User</p>
</blockquote></th>
<th>USR</th>
<th>[choose</th>
<th><blockquote>
<p>from</p>
</blockquote></th>
<th><blockquote>
<p>NEW PERSON]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Location</p>
</blockquote></td>
<td>LOC</td>
<td>[choose</td>
<td><blockquote>
<p>from</p>
</blockquote></td>
<td><blockquote>
<p>HOSPITAL LOCATION]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.5</p>
</blockquote></td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td>[choose</td>
<td><blockquote>
<p>from</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE/SECTION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td>[REGION</td>
<td><blockquote>
<p>5]</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> When you select “CP Flowsheets” from the CPRS Tools menu, CP Flowsheets is displayed and the actual server, port, and global reference are substituted for the command line switches.

> *This page intentionally left blank for double-sided printing.*

# FAQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Question</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>What do I do if I have installation issues?</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Response</strong></p>
</blockquote></td>
<td><blockquote>
<p>1. If assistance is needed during installation please create a Remedy Ticket or contact the</p>
<p><strong>Remedy Help Desk</strong> <mark>REDACTED</mark>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Question</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>How can I check my connection to the broker server?</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Response</strong></p>
</blockquote></td>
<td><ol type="1">
<li><p>Check the windows registry (HKLM/software/vista/broker/servers) key and ensure that the key is set to the correct IP and port.</p></li>
<li><p>Check that the broker is running on the correct instance of VistA and on the correct port.</p></li>
</ol>
<blockquote>
<p>![](md-1-26-installation-guide-cp-flowsheets/111.png) Type D ^%SS to show the list</p>
<p>![](md-1-26-installation-guide-cp-flowsheets/112.png) Find the instance and find the line XWBTCPL ![](md-1-26-installation-guide-cp-flowsheets/113.png) Verify that the TCP|port number is correct</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Question</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>How can I check the Windows application Event Notifier?</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Response</strong></p>
</blockquote></td>
<td><ol type="1">
<li><p>Right-click <strong>My Computer</strong>.</p></li>
<li><p>Select <strong>Manage</strong>.</p></li>
<li><p>Expand <strong>Event Viewer</strong>.</p></li>
<li><p>Select <strong>Application</strong>.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Question</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>How do I stop the CP Gateway Service?</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Response</strong></p>
</blockquote></td>
<td><ol type="1">
<li><p>In Windows, click <strong>Start</strong> | <strong>Control Panel</strong> | <strong>Administrative Tools</strong> | <strong>Services</strong>. The Services window displays.</p></li>
<li><p>Click the Clinical Procedures Gateway row. A link, <u>Stop</u> the service, displays.</p></li>
<li><p>Click <strong>Stop</strong>. A progress window displays as the service stops.</p></li>
<li><p>When the progress window closes, the Services window redisplays. The status column in the Clinical Procedures Gateway row displays <strong>Stopped</strong>.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Question</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>How can I change the time interval for CP Console and CP Flowsheets at which they time</strong></p>
<p><strong>out?</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Answer</strong></p>
</blockquote></td>
<td><blockquote>
<p>The time interval is set using the TIMED READ value in the NEW PERSON file (#200).</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>

> *This page intentionally left blank for double-sided printing.*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This glossary is used for the Clinical Flowsheets project and may include terms and definitions not used in this specific document.
<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>&lt;RET&gt;</strong></td>
<td>Carriage return.</td>
</tr>
<tr class="even">
<td><strong>Access Code</strong></td>
<td>A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.</td>
</tr>
<tr class="odd">
<td><strong>Action</strong></td>
<td>A functional process that a clinician or clerk uses in the TIU computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.</td>
</tr>
<tr class="even">
<td><strong>ADP</strong></td>
<td>Automated Data Processing</td>
</tr>
<tr class="odd">
<td><strong>ADP Coordinator/- ADPAC/Application Coordinator</strong></td>
<td>Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as clinical procedures, PIMS, etc.</td>
</tr>
<tr class="even">
<td><strong>ADT</strong></td>
<td>Advanced Data Type (InterSystems Cache). Also Admissions, Discharges, Transfers.</td>
</tr>
<tr class="odd">
<td><strong>AP</strong></td>
<td>Arterial pressure</td>
</tr>
<tr class="even">
<td><strong>API</strong></td>
<td>Application Programming Interface. An interface that a computer system, library, or application provides in order to accept requests for services from other programs, and/or to allow data to be exchanged between them.</td>
</tr>
<tr class="odd">
<td><strong>Application</strong></td>
<td>A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.</td>
</tr>
<tr class="even">
<td><strong>Archive</strong></td>
<td>The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.</td>
</tr>
<tr class="odd">
<td><strong>Assessment</strong></td>
<td><p>Assessment is the documentation of a clinician ‟s observations and interpretation of a patient’s clinical state based on a particular set of observations. The documentation is in the form of name-value pairs with values selected from a predetermined set, of name-value pairs in which the value is a number or set of numbers, or of free text.</p>
<p>Examples of assessments from paper ICU flowsheets are coma scale, patient opens eyes, pupil size, reaction to light, and so on.</p></td>
</tr>
<tr class="even">
<td><strong>ASU</strong></td>
<td>Authorization/Subscription Utility. An application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderable. ASU is distributed with TIU in this version; eventually it will probably become independent, to be used by many VistA packages.</td>
</tr>
<tr class="odd">
<td><strong>Attachments</strong></td>
<td><p>Attachments are files or images stored on a network share that can be linked to the CP study. CP is able to accept data/final result report files from automated instruments.</p>
<p>The file types that can be used as attachments are the following:</p>
<p>.txt - Text files</p>
<p>.rtf - Rich text files</p>
<p>.jpg - JPEG Images</p>
<p>.jpeg - JPEG Images</p>
<p>.bmp - Bitmap Images</p>
<p>.tiff - TIFF Graphics (group 3 and group 4 compressed and uncompressed types)</p>
<p>.pdf - Portable Document Format</p>
<p>.html - Hypertext Markup Language</p>
<p>.DOC (Microsoft Word) files are not supported. Be sure to convert .doc files to .rtf or to .pdf format.</p></td>
</tr>
</tbody>
</table>
| Term                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Background Processing | Simultaneous running of a "job" on a computer while working on another job. Examples would be printing of a document while working on another, or the software might do automatic saves while you are working on something else.                                                                                                                                                                                                                                                 |
| Background Task       | A job running on a computer while simultaneously working on a second job.                                                                                                                                                                                                                                                                                                                                                                                                        |
| Backup Procedures     | The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.                                                                                                                                                                                                                                                                                                               |
| Boilerplate Text      | A pre-defined TIU template that can be filled in for Titles, Speeding up the entry process. TIU exports several Titles with boilerplate text which can be modified to meet specific needs; sites can also create their own.                                                                                                                                                                                                                                                      |
| BP                    | Blood Pressure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Broker                | Software which mediates between two objects, such as a client and a server or a repository and a requestor.                                                                                                                                                                                                                                                                                                                                                                      |
| Browse                | Lookup the file folder for a file that you would like to select and attach to the study. (e.g., clicking the “...” button to start a lookup).                                                                                                                                                                                                                                                                                                                                    |
| Bulletin              | A canned message that is automatically sent by MailMan to a user when something happens to the database.                                                                                                                                                                                                                                                                                                                                                                         |
| Business Rule         | Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned CP note may be edited by a provider who is also the expected signer of the note).                                                                                                                                                                                                                                    |
| CAC                   | Clinical Application Coordinator.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Care Action           | Care action is an intervention scheduled on a patient that may or may not be ordered.                                                                                                                                                                                                                                                                                                                                                                                            |
| CCB                   | Change Control Board.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| CCDSS                 | Clinical Care Delivery Support System.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CCOW                  | Clinical Context Object Workgroup. An HL7 standard protocol through which applications can synchronize in real-time, enabling Single Sign On and Context Management.                                                                                                                                                                                                                                                                                                             |
| CDR                   | Clinical Data Repository.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CIS                   | Clinical Information System. An ICU Clinical Information System is any hardware/software system that works in concert to collect, store, display, and/or enable manipulation of potential, clinically relevant information. A CIS also acts as an HL7 Gateway. Vendors of monitors and other instruments used in an ICU provide the CIS. The primary distinguishing feature of this CIS is its ability to manually select a subset of all available data and send it to the EMR. |
| Class                 | Part of Document Definitions, Classes group documents. For example, “CLINICAL PROCEDURES” is a class with many kinds of Clinical Procedures notes under it. Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.                                                                                                                                            |
| Clinical Flowsheets   | A module of the Clinical Procedures package that allows the collection of discrete data from medical devices or a Clinical Information System. It is a complete HL7 standardized instrument interface developed and owned by the Department of Veterans Affairs. This module is comprised of three components: the CP Flowsheets application, the CP Console application, and the CliO Generic Interface.                                                                        |
| Clinical Reminders    | A system which allows caregivers to track and improve preventive healthcare and disease treatment for patients and to ensure timely clinical interventions.                                                                                                                                                                                                                                                                                                                      |
| CliO                  | Clinical Observations database.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CM                    | Configuration Management.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Term                | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Consult             | Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.                                                                                                                             |
| Contingency Plan    | A plan that assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.                                                                                                                                                                                                    |
| CP                  | Clinical Procedures.                                                                                                                                                                                                                                                                                                                                                                                               |
| CP Console          | An application used by Administrators to configure the CP Flowsheets application and its interface settings.                                                                                                                                                                                                                                                                                                       |
| CP Definition       | CP Definitions are procedures within Clinical Procedures.                                                                                                                                                                                                                                                                                                                                                          |
| CP Flowsheets       | A GUI component of the Clinical Flowsheets package. Its primary functions are to provide a means to display data collected from a medical device and to allow manual entry of data. Additional functionality is provided to display and print reports, verify incoming observational data, add comments, correct erroneous information, and submit TIU Notes to CPRS.                                              |
| CP Gateway          | The service application that prepares the data contents of HL7 messages for use in CP Hemodialysis. It requires no direct user interaction.                                                                                                                                                                                                                                                                        |
| CP Manager          | The CP Manager application is no longer supported after the installation of MD\*1.0\*16; it has been superseded by. CP Console.                                                                                                                                                                                                                                                                                    |
| CP Study            | A CP study is a process created to link the procedure result from the medical device or/and to link the attachments browsed from a network share to the procedure order.                                                                                                                                                                                                                                           |
| CPRS                | Computerized Patient Record System. A comprehensive VistA program, which allows clinicians and others to enter and view orders, Progress Notes and Discharge Summaries (through a link with TIU), Problem List, view results, reports (including health summaries), etc.                                                                                                                                           |
| Data Dictionary     | A description of file structure and data elements within a file.                                                                                                                                                                                                                                                                                                                                                   |
| DBIA                | Database Integration Agreement.                                                                                                                                                                                                                                                                                                                                                                                    |
| Delphi              | A programming language, also known as Object Pascal.                                                                                                                                                                                                                                                                                                                                                               |
| Device              | A hardware input/output component of a computer system (e.g., CRT, printer).                                                                                                                                                                                                                                                                                                                                       |
| Display Interval    | The amount of time that displays in each column of a flowsheet view. Display interval is configurable from 1 minute to 24 hours. Shorter interval settings can improve readability when a large amount of data is received over a short period of time. Longer interval settings allow you to view longer periods of time while reducing the amount of horizontal scrolling necessary to view all columns.         |
| DLL                 | Dynamically Linked Library. These files provide the benefit of shared libraries.                                                                                                                                                                                                                                                                                                                                   |
| DOB                 | Date of Birth.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Document Class      | Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Cardiology notes might be a Document Class, with Echo notes, ECG notes, etc. as Titles under it. Or maybe the Document Class would be Endoscopy Notes, with Colonoscopy notes, etc. under that Document Class.                                                                                   |
| Document Definition | Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects. |
| DUZ                 | Designated user. This is the internal FileMan number for a particular user.                                                                                                                                                                                                                                                                                                                                        |
| Edit                | Used to change/modify data typically stored in a file.                                                                                                                                                                                                                                                                                                                                                             |
| Term                    | Description                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EMR                     | Electronic Medical Record. Health*e*Vet, is the permanent medical record for a patient in VistA                                                                                                                                                                                                                                                                                |
| Field                   | A data element in a file.                                                                                                                                                                                                                                                                                                                                                      |
| File                    | The M construct in which data is stored for retrieval later. A computer record of related information.                                                                                                                                                                                                                                                                         |
| File Manager or FileMan | Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file, a database.                                                                                                                                                                                        |
| File Server             | A machine where shared software is stored.                                                                                                                                                                                                                                                                                                                                     |
| Flowsheet               | A flowsheet is a table, chart, spreadsheet, or other method of displaying data on two axes. One axis represents time intervals and the other axis represents the readings from an ICU monitor documented at the various time intervals.                                                                                                                                        |
| Flowsheet view          | A customizable subsection (or page) of a flowsheet. Flowsheet views are created by adding and arranging terms and choosing their default qualifiers. Flowsheet views can be set up to display observations, provide a way to manually enter observations, and display reports.                                                                                                 |
| Fluid off               | Cumulative volume of fluid removed from patient.                                                                                                                                                                                                                                                                                                                               |
| Gateway                 | The software that performs background processing for Clinical Procedures.                                                                                                                                                                                                                                                                                                      |
| Global                  | An M term used when referring to a file stored on a storage medium, usually a magnetic disk.                                                                                                                                                                                                                                                                                   |
| GUI                     | Graphical User Interface. A Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), etc.                                                                                      |
| HDR                     | Health Data Repository.                                                                                                                                                                                                                                                                                                                                                        |
| HEP (CUM)               | Cumulative heparin infusion                                                                                                                                                                                                                                                                                                                                                    |
| HFS                     | Host File System.                                                                                                                                                                                                                                                                                                                                                              |
| HIPAA                   | Health Insurance Portability and Accountability Act.                                                                                                                                                                                                                                                                                                                           |
| HL7                     | Health Level 7. A language which various healthcare systems use to interface with one another.                                                                                                                                                                                                                                                                                 |
| HL7 Gateway             | Hardware or software provided by a vendor that is able to receive information in a vendor ‟s proprietary format from one or more ICU monitors and other instruments, to translate the data into standardized HL7 message format, and to pass the messages to other systems.                                                                                                    |
| HR                      | Heart Rate.                                                                                                                                                                                                                                                                                                                                                                    |
| HSD&D                   | Office of Information (OI), Health Systems Design & Development.                                                                                                                                                                                                                                                                                                               |
| HSITES                  | Health Systems Implementation, Training, Education, and Support.                                                                                                                                                                                                                                                                                                               |
| ICU                     | Intensive Care Unit.                                                                                                                                                                                                                                                                                                                                                           |
| IEN                     | Internal Entry Number.                                                                                                                                                                                                                                                                                                                                                         |
| IJ                      | Internal Jugular.                                                                                                                                                                                                                                                                                                                                                              |
| Instrument              | An instrument is a device used to perform a medical function on a patient. In Clinical Flowsheets instrument refers to ICU monitors, which are electronic devices that collect and/or display information concerning the physical state of a patient. Usually, the monitor attaches to a patient and takes readings over time without requiring intervention for each reading. |
<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Interpreter</strong></td>
<td><p>Interpreter is a user role exported with USR*1*19 to support the Clinical Procedures Class. The role of the Interpreter is to interpret the results of a clinical procedure.</p>
<p>Users who are authorized to interpret the results of a clinical procedure are sent a notification when an instrument report and/or images for a CP request are available for interpretation. Business rules are used to determine what actions an interpreter can perform on a document of a specified class, but the interpreter themselves are defined by the Consults application. These individuals are „clinical update users‟ for a given consult service.</p></td>
</tr>
<tr class="even">
<td><strong>IRM</strong></td>
<td>Information Resource Management.</td>
</tr>
<tr class="odd">
<td><strong>IRMS</strong></td>
<td>Information Resource Management Service.</td>
</tr>
<tr class="even">
<td><strong>JCAHO</strong></td>
<td>Joint Commission on Accreditation of Healthcare Organizations.</td>
</tr>
<tr class="odd">
<td><strong>Kernel</strong></td>
<td>A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.</td>
</tr>
<tr class="even">
<td><strong>Key</strong></td>
<td>A level of access assigned to a Flowsheets user that determines which Flowsheets functions the user may perform. Refer to “User Role” in this Glossary.</td>
</tr>
<tr class="odd">
<td><strong>LAYGO</strong></td>
<td>An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.</td>
</tr>
<tr class="even">
<td><strong>LPES/CPS</strong></td>
<td>Legacy Product Enterprise Support/Clinical Product Support. Enterprise Product Support (formerly Enterprise VistA Support).</td>
</tr>
<tr class="odd">
<td><strong>log</strong></td>
<td>A list that provides the time and description of events as they occur.</td>
</tr>
<tr class="even">
<td><strong>M</strong></td>
<td>Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi- Programming System. This is the programming language used to write all VistA applications.</td>
</tr>
<tr class="odd">
<td><strong>MailMan</strong></td>
<td>An electronic mail, teleconferencing, and networking system.</td>
</tr>
<tr class="even">
<td><strong>MAP</strong></td>
<td>Mean Arterial Pressure.</td>
</tr>
<tr class="odd">
<td><strong>Menu</strong></td>
<td>A set of options or functions available to users for editing, formatting, generating reports, etc.</td>
</tr>
<tr class="even">
<td><strong>Module</strong></td>
<td>A component of a software application that covers a single topic or a small section of a broad topic.</td>
</tr>
<tr class="odd">
<td><strong>MUMPS</strong></td>
<td>Massachusetts General Hospital Utility Multi-Programming System. Obsolete; now known as "M" programming language.</td>
</tr>
<tr class="even">
<td><strong>Namespace</strong></td>
<td>A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application.</td>
</tr>
<tr class="odd">
<td><strong>Network Server Share</strong></td>
<td>A machine that is located on the network where shared files are stored.</td>
</tr>
<tr class="even">
<td><strong>Notebook</strong></td>
<td>This term refers to a GUI screen containing several tabs or pages.</td>
</tr>
<tr class="odd">
<td><strong>NTE</strong></td>
<td>Not To Exceed.</td>
</tr>
<tr class="even">
<td><strong>OI</strong></td>
<td>Office of Information. Formerly known as Chief Information Office Field Office, Information Resource Management Field Office, and Information Systems Center.</td>
</tr>
<tr class="odd">
<td><strong>option</strong></td>
<td>A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions.</td>
</tr>
<tr class="even">
<td><strong>optional page</strong></td>
<td>One of two special types of flowsheet views which provides a way to track a specific condition (e.g., a pacemaker) on its own flowsheet view. An Optional Page can display only once in a given flowsheet. If an optional page is closed and then redisplayed, any data previously entered still displays.</td>
</tr>
</tbody>
</table>
| Term                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Package               | Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA.                                                                                                                                                                                                                                                                                                    |
| page                  | This term refers to a tab on a GUI screen or notebook.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Password              | A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).                                                                                                                                                                                                                                                                                                    |
| PCE                   | Patient Care Encounter.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Permission            | Setting that can be used to allow access to particular views, flowsheets, etc. to one or more specific users and to control the type of access each user has.                                                                                                                                                                                                                                                                                              |
| PIMS                  | Patient Information Management System.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Pivot                 | Swap the axes of a table or chart. This causes the values that were displayed along the vertical axis to be displayed along the horizontal axis and the values that were displayed along the horizontal axis to be displayed along the vertical axis.                                                                                                                                                                                                      |
| PM                    | Project Manager.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pointer               | A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.                                                                                                                                                                                                                                                                                              |
| PRN                   | As needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Procedure Request     | Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without first requiring formal consultation.                                                                                                                                                                                                                                                                                                                    |
| Program               | A set of M commands and arguments, created, stored, and retrieved as a single unit in M.                                                                                                                                                                                                                                                                                                                                                                   |
| Protocol              | A set of rules governing communication within and between computing endpoints.                                                                                                                                                                                                                                                                                                                                                                             |
| PS                    | Provider Systems.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PV                    | Pulmonary Vascular.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| QG                    | Quality Gate.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Qualifiers            | A word or phrase that provides specific information about an observation. For example, an observation could have qualifiers such as Unit (f=degrees Fahrenheit, c=degrees Celsius, bpm=beats per minute, rpm=respirations per minute, etc.), Method (Cu=cuff BP, Dop=Doppler BP, etc.), Position (Ly=lying, Si=sitting, St=standing, etc.), Location (La=left arm, LL=left leg, RA=right arm, RL=right leg, etc.), Quality (A=accurate, E=Estimated), etc. |
| Queuing               | The scheduling of a process/task to occur later. Queuing is normally done if a task is a heavy user of computer resources.                                                                                                                                                                                                                                                                                                                                 |
| RAID                  | Redundant Array of Inexpensive Disks. A data storage scheme using multiple hard drives to share or replicate data among the drives.                                                                                                                                                                                                                                                                                                                        |
| Result                | A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.                                                                                                                                                                                                                                                                 |
| Routine               | A set of M commands and arguments, created, stored, and retrieved as a single unit in M.                                                                                                                                                                                                                                                                                                                                                                   |
| RPC                   | Remote Procedure Call. A protocol that allows a computer program running on one host to cause code to be executed on another host.                                                                                                                                                                                                                                                                                                                         |
| Rx                    | Prescription.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SAC                   | Standards And Conventions.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Security Key          | A function which unlocks specific options and makes them accessible to an authorized user.                                                                                                                                                                                                                                                                                                                                                                 |
| Sensitive Information | Any information which requires a degree of protection and which should be made available only to authorized users.                                                                                                                                                                                                                                                                                                                                         |
| Term                    | Description                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service                 | A long-running executable designed to perform specific functions without user intervention. Windows services can be configured to restart automatically when the operating system is rebooted.                                                                                                                                                                                    |
| SGML                    | Standard Generalized Markup Language.                                                                                                                                                                                                                                                                                                                                             |
| Shift                   | A period of time that can be defined in CP Flowsheets. This often corresponds to the time an individual an individual works.                                                                                                                                                                                                                                                      |
| Site Configurable       | A term used to refer to features in the system that can be modified to meet the needs of each site                                                                                                                                                                                                                                                                                |
| Software                | A generic term for a related set of computer programs, such as an operating system that enables user programs to run.                                                                                                                                                                                                                                                             |
| SQA                     | Software Quality Assurance.                                                                                                                                                                                                                                                                                                                                                       |
| SRS                     | Software Requirements Specification.                                                                                                                                                                                                                                                                                                                                              |
| SSN                     | Social Security Number.                                                                                                                                                                                                                                                                                                                                                           |
| Status Symbols          | Codes used in order entry and Consults displays to designate the status of the order.                                                                                                                                                                                                                                                                                             |
| STS                     | Standards and Terminology Services. An initiative to create and maintain standardized terminology throughout the VA by assigning a code to every term.                                                                                                                                                                                                                            |
| Supplemental page       | One of two special types of flowsheet views which provides a way to track a specific condition (e.g., a pressure wound) on its own flowsheet view. Multiple supplemental pages can be added to a single flowsheet in order to track numerous specific conditions. If a supplemental page is closed and then a new supplemental page is added, the new supplemental page is blank. |
| Tab                     | One of the five primary GUI screens of the CP Flowsheets application: Flowsheet, Alarms, Reports, Log Files, and HL7 Monitor.                                                                                                                                                                                                                                                     |
| Task Manager or TaskMan | A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.                                                                                                                                                                                                                                                    |
| Term                    | As used in Flowsheets, a term is any piece of relevant data. A term, like “Blood Pressure” will typically have one or more associated measures, modifiers, or qualifiers.                                                                                                                                                                                                         |
| Terminology             | Standardization of words and terms used in Flowsheets.                                                                                                                                                                                                                                                                                                                            |
| Title                   | Titles are definitions for documents. They store the behavior of the documents which use them.                                                                                                                                                                                                                                                                                    |
| TIU                     | Text Integration Utilities.                                                                                                                                                                                                                                                                                                                                                       |
| TMP                     | Trans Membrane Pressure.                                                                                                                                                                                                                                                                                                                                                          |
| UFR                     | Ultrafiltration Rate.                                                                                                                                                                                                                                                                                                                                                             |
| UI                      | User Interface.                                                                                                                                                                                                                                                                                                                                                                   |
| UNC                     | Universal Naming Convention.                                                                                                                                                                                                                                                                                                                                                      |
| Untrusted device        | A medical instrument which has not been mapped for use with the Clinical Flowsheets package. Data sent from an untrusted device will not display in a flowsheet view until someone reviews it (on the CP Flowsheets Log Files tab) and marks it as verified.                                                                                                                      |
| URL                     | Uniform Resource Locator. A means of finding a resource (such as a web page or a device) on the Internet.                                                                                                                                                                                                                                                                         |
| URR                     | Urea Reduction Ratio. The reduction in urea as a result of dialysis.                                                                                                                                                                                                                                                                                                              |
| User                    | A person who enters and/or retrieves data in a system, usually utilizing a CRT.                                                                                                                                                                                                                                                                                                   |
| User Class              | User Classes are the basic components of the User Class hierarchy of ASU (Authorization/Subscription Utility) which allows sites to designate who is authorized to do what to documents or other clinical entities.                                                                                                                                                               |
<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>User Role</strong></td>
<td>User Role (in a documentation context). The role of the user with respect to the document in question (e.g., Author/Dictator, Expected Signer, Expected Cosigner, Attending Physician, etc.).</td>
</tr>
<tr class="even">
<td><strong>User Role</strong></td>
<td><p>User Role (in a Flowsheets setup context). The role of a Flowsheets user with respect to which Flowsheets functions the user will have permission to perform. Flowsheets User Role include the following.</p>
<ul>
<li><p>MD ADMINISTRATOR</p></li>
<li><p>MD MANAGER</p></li>
<li><blockquote>
<p>MD HL7 MANAGER</p>
</blockquote></li>
<li><p>MD READ-ONLY</p></li>
<li><p>MD TRAINEE</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Utility</strong></td>
<td>An M program that assists in the development and/or maintenance of a computer system.</td>
</tr>
<tr class="even">
<td><strong>UUEncoded format</strong></td>
<td>A form of binary to text encoding whose name derives from "Unix-to-Unix encoding”.</td>
</tr>
<tr class="odd">
<td><strong>VA</strong></td>
<td>Department of Veterans Affairs. Formerly the Veterans Administration.</td>
</tr>
<tr class="even">
<td><strong>VAMC</strong></td>
<td>Department of Veterans Affairs Medical Center.</td>
</tr>
<tr class="odd">
<td><strong>VDEF</strong></td>
<td>VistA Data Extraction Framework.</td>
</tr>
<tr class="even">
<td><strong>Verify Code</strong></td>
<td>A unique security code which serves as a second level of security access. Use of this code is site specific. This term is sometimes used interchangeably the term password.</td>
</tr>
<tr class="odd">
<td><strong>VHA</strong></td>
<td>Veteran Health Administration.</td>
</tr>
<tr class="even">
<td><strong>VistA</strong></td>
<td>Veterans Health Information Systems and Technology Architecture.</td>
</tr>
<tr class="odd">
<td><strong>VP</strong></td>
<td>Venous Pressure.</td>
</tr>
<tr class="even">
<td><strong>VUID</strong></td>
<td>Veterans Health Administration (VHA) Unique Identifier. A unique identifier that specifies individual data elements or observations. In Clinical Flowsheets, each term is assigned a VUID.</td>
</tr>
<tr class="odd">
<td><strong>Workstation</strong></td>
<td>A personal computer running the Windows 9x or NT operating system.</td>
</tr>
<tr class="even">
<td><strong>XML</strong></td>
<td>Extensible Markup Language. A simplified subset of Standard Generalized Markup Language (SGML). Its primary purpose is to facilitate the sharing of data across different information systems.</td>
</tr>
<tr class="odd">
<td><strong>XMS</strong></td>
<td>Extended Memory Specification. The specification describing the use of extended memory in real mode for storing data.</td>
</tr>
</tbody>
</table>


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MD*1*76 Installation Guide (CP Flowsheets)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CP Flowsheets v1.0.76.2 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Flowsheets v1.0.76.2 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Flowsheets v1.0.76.2 and the associated M patch (if applicable) are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. CP Flowsheets v1.0.76.2 utilizes existing, nationally released security controls to control access.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Flowsheets v1.0.76.2 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to IOC sites for verification of functionality. Once that testing is completed and approval is given for national release, CP Flowsheets v1.0.76.2 (MD\*1\*76) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

- Tomah VA Medical Center (Tomah, WI)
- VA Southern Nevada Healthcare System (Las Vegas, NV)

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for CP Flowsheets v1.0.76.2. A fully patched VistA system is the only requirement.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GUI source code for this patch is available in ZIP file MD_1_76_SRC.ZIP which can be obtained at location: <span class="mark">REDACTED</span>

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action Item and National Change Order prior to the release of CP Flowsheets v1.0.76.2 advising them of the upcoming release.

CP Flowsheets v1.0.76.2 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch MD\*1\*76 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Flowsheets v1.0.76.2 assumes a fully-patched VistA system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

\[GUI\] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.).

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Flowsheets v1.0.76.2 is being released as a PackMan Message distributed through the National Patch Module combined with a .ZIP file containing the GUI file(s).

The ZIP file can be obtained at location: <span class="mark">REDACTED</span>

Documentation can be found on the VA Software Documentation Library at: <https://www.va.gov/vdl/>

<span id="_Toc525291728" class="anchor"></span>Table 2: File to be Downloaded

| File Name   | File Contents                          | Download Format |
|-------------|----------------------------------------|-----------------|
| MD_1_76.ZIP | CP Flowsheets executable and help file | Binary          |

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of CP Flowsheets v1.0.76.2 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MD\*1\*76 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name: MD\*1.0\*76
2.  Select the Backup a Transport Global option to create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
3.  You may also elect to use the following options:
1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
1.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
2.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

### CP Flowsheets v1.0.76.2 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file (MD_1_76.ZIP) contains the CP Flowsheets GUI executable and associated files. Download the ZIP file and extract all the files.

#### CP Flowsheets GUI Methods of Installation

The following methods of installation of CP Flowsheets are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

<u>Network (Shared) Installation:</u>

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPFlowsheets.exe) across the LAN.

The GUI executable (CPFlowsheets.exe) and help file (CPFlowsheets.chm) are copied to a network shared location. Users are provided with a desktop shortcut to run CPFlowsheets.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties

At the time of a CP Flowsheets version update, the copy of CPFlowsheets.exe and the help file are replaced, on the network share, with the new version.

Any users requiring access to another site's CP Flowsheets system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of CP Flowsheets (e.g. for testing purposes) a different version of CPFlowsheets.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

<u>Citrix Installation:</u>

The GUI executable (CPFlowsheets.exe) and associated files are installed and ran from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

> **NOTE:** For issues with CAG, please contact the local or national help desk.

<u>Local Workstation Installation:</u>

This is the “standard” method of installation where the GUI executable (CPFlowsheets.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. This is outside the scope of the Sustainment team. A National package (Clinical Procedures Flowsheets v1.0.76.2) has been prepared and made available to Regional COR Client Technologies leadership.

<u>Manual Install:</u>

This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or users who need to have access to a pre-production (mirror) VistA instance.

1.  Locate the MD_1_76.ZIP and unzip the file.
3.  Copy the contents of the zip archive to a directory appropriate for programs. For example: C:\Program Files (x86)\Vista\CP Flowsheets. A new directory may need to be created.

    Note: Administrator rights are required to complete these steps.
4.  Create a Shortcut and name it “CP Flowsheets”. This can be done by using Windows Explorer to navigate to the file location of CP Flowsheets.exe, right Clicking on the file and choosing \[Send to\] \> \[Desktop (Create Shortcut)\]

> <span id="_Toc525291723" class="anchor"></span>Figure 1: How to Create Shortcut

> ![](md-1-76-installation-guide-cp-flowsheets/002.png)

5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  Right click on the newly created Shortcut and select Properties. Enter “s=” IP (or DNS name) and “p=” RPC port in the Target field (or use ServerList.exe).

> <span id="_Toc525291724" class="anchor"></span>Figure 2: CP Flowsheets Shortcut Properties

> ![](md-1-76-installation-guide-cp-flowsheets/003.png)

> **NOTE:** The server and port number shown above are for example only.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VISTA\] After installing the VistA side patch, attempt the GUI verification. If the VistA side installed properly there will be no version error upon trying to open the application.

\[GUI\] Launch the CP Flowsheets GUI and verify the splash screen announces running version 1.0.76.2

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] This patch has one pre-install routine MDPOST76 which should have been deleted after install, and one routine MDTERM that needs to be restored to its previous version using the backup PackMan message created during the install. To back out the change made by MDPOST76 requires manually reverting the version check parameter to the previous GUI version “1.0.63.2”.

\[GUI\] To revert to the CP Flowsheets GUI, the 1.0.63.2 GUI would have to be redistributed.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on CP Flowsheets v1.0.76.2. This was a maintenance release to correct defects discovered in CP Flowsheets v1.0.63.2. There is no additional functionality included.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of MD\*1\*76. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. Any issues were reported back to the development team and were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out CP Flowsheets v1.0.76.2 would result in the re-instatement of the issues addressed in CP Flowsheets v1.0.76.2.

The back-out process, would significantly impact patient care due to the interruption. Therefore, the back-out process should only be performed in an emergency situation.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for CP Flowsheets v1.0.76.2 is in the event of a catastrophic failure.

Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with CP Flowsheets v1.0.76.2. Use the following contacts:

<span id="_Toc525291729" class="anchor"></span>Table 3: HPS CLIN Contacts

| Name                               | Title           | Email                              | Telephone                          |
|------------------------------------|-----------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | Project Manager | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

If the decision is made to proceed with back-out and rollback, the HPS Clinical Sustainment team be available to assist sites.

1.  \[VistA\] In section 4.8.1 (step 2B), the individual installing the patch used option \[Backup a Transport Global\] to create a PackMan message that will revert the MDTERM routine to its previous state. If for any reason that PackMan Message cannot be located, contact HPS Sustainment: Clinical Contacts (see section 5.6).
2.  Navigate in VistA to the XPAR EDIT PARAMETER option .
8.  At the Select PARAMETER DEFINITION NAME: prompt, enter MD PARAMETERS.
9.  At the Select Enter selection: prompt, enter SYSTEM.
10. At the Select Parameter Name: prompt, enter VERSION_CPFLOWSHEETS.
11. At the Parameter Name: prompt, hit the enter key to accept the default.
12. At the Parameter Value: prompt, enter 1.0.63.2.
13. \[GUI\] Coordinate with the appropriate IT support, local and regional, to schedule the time to push out and install the previous GUI executable.
14. Once CP Flowsheets v1.0.63.2 GUI has been installed, verify operations before making available to all staff.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure the v1.0.63.2 executable launches properly.
15. Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

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

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will automatically rollback version.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### From: MD*1*71 Installation Guide (User)

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP User Documentation v1.0.71.3 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the CAG.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, CP User v1.0.71.3 (MD\*1.0\*71) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

- TBD
- TBD

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for CP User v1.0.71.3. A fully patched VistA system is the only requirement.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action item and National Change Order prior to the release of CP User v1.0.71.3 advising them of the upcoming release.

CP User v1.0.71.3 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch MD\*1.0\*71 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

### MD\*1.0\*71 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and select the INSTALL/CHECK MESSAGE PackMan option to load the KIDS patch into a Transport Global on your system.
2.  From the Kernel Installation & Distribution System Menu (KIDS), select the Installation menu:

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, you must use the Backup a Transport Global option to create a back out message. When prompted for the INSTALL NAME enter the package name: MD\*1.0\*71
4.  Also from this menu, you may elect to use the following options:
    - Verify Checksums in Transport Global
    - Print Transport Global
    - Compare Transport Global to Current System
5.  Select the Install Package(s) option and enter the package name: MD\*1.0\*71
6.  When prompted, Want KIDS to INHIBIT LOGONs during the install? NO//, respond NO.
7.  When prompted, Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, respond NO.

### CP User v1.0.71.3 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the CP User GUI executable and help file. Download the ZIP file and extract all the files.

#### CP User documentation GUI Methods of Installation

The following methods of installation of CP User are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/Veterans Integrated Services Network (VISN) policies, Local Area Network (LAN) performance, or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

- Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPUser.exe) across the LAN.

> The GUI executable (CPUser.exe), help file (CPUSER.chm) files are copied to a network shared location. Users are provided with a desktop shortcut to run CPUser.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the Target field of the shortcut properties.

> At the time of a CP User version update the copy of CPUser.exe and the help file are replaced, on the network share, with the new version.

> Any users requiring access to another site's CP User system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of CP User (e.g. for testing purposes) a different version of CPUser.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

- Citrix installation:

> The GUI executable (CPUser.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary CAG infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

- Local workstation installation:

  This is the “standard” method of installation where the GUI executable (CPUser.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via System Center Configuration Manager (SCCM). This is outside the scope of the Sustainment team. A National package (CP User v1.0.71.3) has been prepared and made available to Regional Contracting Officer’s Representative (COR) Client Technologies leadership.
- Manual install:

  This method is available for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.
1.  Locate the MD_1_71.ZIP and unzip the file.
2.  Copy the contents of the zip archive to a test directory, for example, C:\CPUser. You may need to create this new directory.

    Note: You need to have a user with Administrator rights to the personal computer (PC) to complete these steps.
3.  Create a Shortcut and name it, Test CP User v1_71. This is to give the user another visual cue that this is not the normal CP User icon.

> <span id="_Toc20906452" class="anchor"></span>Figure 1: Shortcut Icon for Test CPUser v71

![](md-1-71-installation-guide-user/002.png)

4.  Determine the Domain Name System (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties or use ServerList.exe (which launches a selection screen for various servers and ports defined).

> <span id="_Toc20906453" class="anchor"></span>Figure 2: Test CPUser v71 Properties

> ![](md-1-71-installation-guide-user/003.png)

> **NOTE:** The server and port number shown above are for example only.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the test sites listed in Section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the MD\*1.0\*71 build. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

### From: MD*1*70 Installation Guide (Hemodialysis)

### MD\*1.0\*70 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, the \[Backup a Transport Global\] option must be used to create a back out Patch.
4.  From this menu, use one of the following options:
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
5.  Use the Install Package(s) options and select the package MD\*1.0\*70.
6.  When prompted, Want KIDS to INHIBIT LOGONs during the install? NO//, respond NO.
7.  When prompted, Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, respond NO.

### CP Hemodialysis v1.0.70.1 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the CP Hemodialysis v1.0.70.1 GUI executable. Download the ZIP file and extract all the files.

#### CP Hemodialysis GUI Methods of Installation

The following methods of installing CP Hemodialysis are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant use of more than one option below.

- Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (Hemodialysis.exe) across the LAN.

> The GUI executable and related files for each application are copied to a network shared location. Users are provided with a desktop shortcut to run the executable directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the Target field of the shortcut properties.

> At the time of a CP Hemodialysis version update, the copy of the files in the folders are replaced, on the network share, with the new versions from the zip file.

> Any users requiring access to another site's CP Hemodialysis system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of CP Hemodialysis (e.g. for testing purposes) a different version of CP Hemodialysis executable files can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

- Citrix installation:

> The GUI executable (Hemodialysis.exe) and help file (Hemodialysis.hlp) are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

- Local workstation installation:

> This is the “standard” method of installation where the GUI executable (Hemodialysis.exe) and help file (Hemodialysis.hlp) are installed on and run from the user's local workstation.

> Download the MD_1_70.zip file and extract all the files. 

> Hemodialysis.exe and the Hemodialysis.chm (help) file will need to be installed in the same directory on workstations. 

> Note: There is a national SCCM package to help sites or Information Technology Operations (ITOPS) distribute the Hemodialysis GUI.

- Manual install:

  This method is used primarily for advanced users and at testing locations. This method has somewhat changed from what has been used previously for Windows XP workstations.
1.  Locate the MD_1_70.ZIP and unzip the file.
2.  Copy the Hemodialysis.exe to a test directory, for example, C:\CPHemodialysisTest. You may need to create this new directory.

> Note: You may need to have a user with Administrator rights complete this step.

3.  Create a Shortcut and name it Test CPHemodialysis v70. This is to give the user another visual cue that this is not the normal CP Hemodialysis icon.

> Figure 1: Test CPHemodialysis v70 Shortcut Icon

![](md-1-70-installation-guide-hemodialysis/002.png)

4.  Copy the Hemodialysis.chm file into the same directory as Hemodialysis.exe (for example, c:\\ CPHemodialysisTest).
5.  Determine the Domain Name Server (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

> Figure 2: Test CPHemodialysis v70 Properties

> ![](md-1-70-installation-guide-hemodialysis/003.png)

> The server and port number shown above are not real and are for example only.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on CP Hemodialysis v1.0.70.1. This was a maintenance release to correct defects discovered in CP Hemodialysis v1.0.66.2, no additional functionality was included.

### From: MD*1*66 Installation Guide (Hemodialysis)

### MD\*1.0\*66 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, must use the \[Backup a Transport Global\] option to create a back out Patch
4.  From this menu, you may elect to use the following options:

Compare Transport Global to Current System

Verify Checksums in Transport Global

5.  Use the Install Package(s) options and select the package MD\*1.0\*66
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
7.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.

### From: MD*1*75 Installation Guide (Hemodialysis)

### MD\*1.0\*75 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, must use the \[Backup a Transport Global\] option to create a back out Patch
4.  From this menu, you may elect to use the following options:

Compare Transport Global to Current System

Verify Checksums in Transport Global

5.  Use the Install Package(s) options and select the package MD\*1.0\*75
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
7.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.
