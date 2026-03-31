---
title: VistA Imaging DICOM Gateway Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: VistA Imaging DICOM Gateway
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - dicom
  - gateway
  - table
  - contents
  - vista
  - imaging
  - image
  - installation
  - application
  - class
page_count: 0
word_count: 30951
section_count: 50
table_count: 30
figure_count: 0
appendix_count: 9
has_toc: False
is_stub: False
pub_date: July 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_DICOMig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_DICOMig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

VistA Imaging DICOM GatewayInstallation Guide

![](vista-imaging-dicom-gateway-installation-guide/001.png)

July 2023 – Revision 35

Office of Information and Technology (OIT)

DICOM Gateway Installation GuideProperty of the US Government

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging Product Development group.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies and are hereby acknowledged.

VistA Imaging Product Development  

<u>Caution</u>: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Revision History</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>14 July 2023</td>
<td><p>Applied changes to IRISHealth Installation instructions<br />
Updated Installation section for MAG*3.0*319, and replaced Cache`2014 with IRIS</p>
<p>Relocated 4.8.1-4.8.3 from 4.7 to 4.8<br />
Added note to 4.8.2 regarding new IRIS installation</p>
<p>Removed SSH/Reflection</p>
<p>Document formatting</p></td>
</tr>
<tr class="even">
<td>24 Jan 2019</td>
<td><p>Applied changes for:</p>
<p>MAG*3.0*218</p>
<p>2.1 Hardware and Software Requirements</p>
<p>3.2 Setting Up the Operating Environment</p>
<p>3.4 Installing the Software</p>
<p>3.4 Installing the Software</p>
<p>3.4 Installing the Software</p>
<p>3.4 Installing the Software</p>
<p>3.4.2 Verifying Cache Installation</p>
<p>3.4.3 Setting Up Cache Service Network Account and Password</p>
<p>3.4.3 Setting Up Cache Service Network Account and Password</p>
<p>3.4.3 Setting Up Cache Service Network Account and Password</p>
<p>3.4.3 Setting Up Cache Service Network Account and Password</p>
<p>3.4.3 Setting Up Cache Service Network Account and Password</p>
<p>3.4.3 Setting Up Cache Service Network Account and Password</p>
<p>3.4.4 Verify the DICOM Gateway Installation</p>
<p>3.5 Obtaining a Cache License</p>
<p>3.6.1.2 More Privileges</p>
<p>3.8 SSH Setup</p>
<p>3.8.1 Prerequisites</p>
<p>3.8.4 DICOM_SSH_Setup.bat</p>
<p>3.8.5 Open and Close Reflection for Secure IT Server Console</p>
<p>3.9 Starting Application Routines</p>
<p>3.9 Starting Application Routines</p>
<p>3.9 Starting Application Routines</p>
<p>3.9 Starting Application Routines</p>
<p>4.1 Site-Specific Parameters</p>
<p>4.3 Configure the DICOM Gateway and Load the DICOM Dictionaries</p>
<p>4.3.1/4.3.2 Name of System/Location of DICOM Gateway</p>
<p>4.3.5 DICOM Dictionary Directory</p>
<p>4.3.6 Communication Channels</p>
<p>4.3.10 Auto-Routing Active</p>
<p>4.3.15/4.3.16 Kind of PACS/C-Move Destination</p>
<p>4.3.19/4.3.22 Dashes in SSN sent to PACS/Mail Group</p>
<p>4.3.24/4.3.25 Access Code for Background Tasks/Verify Code for Background Tasks</p>
<p>4.3.27/4.3.28 E-Mail Post Office/E-Mail Post Office Port Number</p>
<p>4.3.30 DICOM Message Logs</p>
<p>4.4.13 Provider Application Dictionary</p>
<p>4.5 Automatically Generating Instrument Shortcut Icons</p>
<p>4.6 Adding DICOM Application Entries to the HOSTS file</p>
<p>4.7 Security</p>
<p>4.7.2 Securing the Cache Cube</p>
<p>4.8.3</p>
<p>4.7.3 Disable Telnet on the DICOM Gateway</p>
<p>4.8 Personal Preferences</p>
<p>4.8 Personal Preferences</p>
<p>5.1 VistA - PACS Radiology Interface Setup Instructions</p>
<p>5.3 Change Subscribers</p>
<p>5.3 Change Subscribers</p>
<p>5.5 Service Account</p>
<p>6.1 Pre-Installation</p>
<p>6.1/6.2 Pre-Installation/Upgrading the DICOM Gateway</p>
<p>6.2 Upgrading the DICOM Gateway</p>
<p>6.2 Upgrading the DICOM Gateway</p>
<p>6.2 Upgrading the DICOM Gateway</p>
<p>6.2 Upgrading the DICOM Gateway</p>
<p>6.2 Upgrading the DICOM Gateway</p>
<p>6.3 Installing Cache 2014.1</p>
<p>6.3 Installing Cache 2014.2</p>
<p>6.4 Verifying Cache Installation</p>
<p>6.5 Setting Up Cache Service Network Account and Password</p>
<p>6.6 Verifying the DICOM Gateway Installation</p>
<p>6.6 Verifying the DICOM Gateway Installation</p>
<p>A.3 Shortcuts for the VistA Imaging DICOM Gateway</p>
<p>A.3 Shortcuts for the VistA Imaging DICOM Gateway</p>
<p>B.2/B.2.1 Master Files/Master File Menu Options</p>
<p>B.2.2 General Formatting Issues</p>
<p>B.3.1 ELEMENT.DIC</p>
<p>B.3.4 SCP_LIST.DIC</p>
<p>B.3.5 TEMPLATE.DIC</p>
<p>B.4 Site-Specific Master Files</p>
<p>B.4.2 INSTRUMENT.DIC</p>
<p>B.4.2/B.4.2.1 INSTRUMENT.DIC/Icons for Instruments</p>
<p>B.2.4.1 Icons for Instruments</p>
<p>B.4.3.1 Image Processing Overview</p>
<p>B.4.3.2 Assigning Field Values for the Modality Dictionary</p>
<p>B.4.3.2.1 Image Processing Rules</p>
<p>B.4.3.4/B.4.5 Setting Up the MODALITY.INC File/SCU_LIST.DIC</p>
<p>B.4.5 SCU_LIST.DIC</p>
<p>B.4.5 SCU_LIST.DIC</p>
<p>B.4.6 WORKLIST.DIC</p>
<p>B.4.7.2.1 Adding the Consult to the file</p>
<p>B.4.7.2.1 Adding the Consult to the file</p>
<p>C.1 Overview</p>
<p>C.2 IP Addresses and Subnet Masks</p>
<p>C.2.4 Example 4 - Use Multiple Subnets</p>
<p>D.2 IPCONFIG</p>
<p>D.3 PING</p>
<p>D.5/D.6 NETSTAT/DICOM_Echo</p>
<p>D.7 Send_Image</p>
<p>G Setting Up the MUMPS-to-MUMPS Broker</p>
<p>H.2 TCP/IP Settings</p>
<p>I Change Cached Password for Secure Shell</p></td>
</tr>
<tr class="odd">
<td>30 July 2018</td>
<td>Updated for MAG*3.0.218 upgrade of Caché from 2010.2 to 2014.1</td>
</tr>
<tr class="even">
<td>25 Jan 2017</td>
<td>Added Section 6.8 instructions on turning journaling off in support of MAG3.0*166 S. Marner (Rev 30)</td>
</tr>
<tr class="odd">
<td>29 Mar 2017</td>
<td>Updated for Patch 176 Secure Shell Replacement of Telnet (SSH replaced occurrences of Telnet; added of Section 3.9; and added edits to A.3, A.4, C.1 and C.4)</td>
</tr>
<tr class="even">
<td>9 May 2016</td>
<td>Updated for MAG*3.0*162 and added Caché cube security steps. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> (Rev 29)</td>
</tr>
<tr class="odd">
<td>13 Sep 2013</td>
<td>Changed this guide to cover only the legacy DICOM Gateway. Installation procedures for the Hybrid DICOM Image Gateway (HDIG) are in the document <em>VistA Imaging Hybrid DICOM Image Gateway (HDIG) Installation Guide</em>. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> (Rev 19)</td>
</tr>
<tr class="even">
<td>22 July 2013</td>
<td><p>Applied change pages for MAG*3.0*162 (Updates: Changed name of file 2006.5831 from DICOM</p>
<p>for Healthcare Providers to Clinical Specialty DICOM &amp; HL7, removed 4.4.6 Imaging Service Dictionary since it doesn’t exist, added the LAB imaging service in various places, added B.4.2.2 on MAG_CSTORE with port number, updated B.4.6 WORKLIST.DIC, rewrote B.4.7 Editing the Clinical Specialty DICOM &amp; HL7 file). <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> k (Rev. 18)</p></td>
</tr>
<tr class="odd">
<td>17 Dec 2012</td>
<td>Applied change pages for MAG*3.0*123 (Updates: Chapter 3. New sections 3.6 and 4.3.29). <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 17)</td>
</tr>
<tr class="even">
<td>1 Sept 2011</td>
<td><p>Applied change pages for:<br />
MAG*3.0*49 (sections 4.1, 4.3.27, 4.3.28, 4.4.15, 4.4.16, 5.1, 5.1.1-5.1.7, 5.3, 5.4, B.4.5, B.4.8).</p>
<p>MAG*3.0*99 (sections 3.4, 3.5, 3.8, 4, B.4.2, B.4.3, B.4.3.1, B.4.3.2, B.4.3.2.1, B.4.3.2.1.1, B.4.3.3, B.4.3.4, B.4.6). <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 16)</p></td>
</tr>
<tr class="odd">
<td>1 Dec 2010</td>
<td><p>Applied change pages for:<br />
MAG*3.0*53 (sections 1.2, 2.8.1, 3.5, 3.6.2, 4.3, 4.4, 4.5, Appendix B, B.2.1, B.4, B.4.1, B.4.2, B.4.3, B.4.4, B.4.5, B.4.6, Appendix F, Appendix I).</p>
<p>MAG*3.0*66 (sections 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 3.8, 3.8.1, B.4.4, Appendix E, Appendix F, Appendix I).</p>
<p>General corrections (removed duplicate spaces in the beginning of sentences). <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 15)</p></td>
</tr>
<tr class="even">
<td>20 Oct 2009</td>
<td>Applied change pages for Patch 54. General corrections in section B.4.4, added revision number, fixed typos and document conventions throughout document, updated organizational name to OED. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 14)</td>
</tr>
<tr class="odd">
<td>15 Aug 2007</td>
<td>Updated section 4.3 for Patch 69. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 13)</td>
</tr>
<tr class="even">
<td>20 Mar 2007</td>
<td>Updates for Patch 69. Updated content in sections 1.2, 2.1, 2.4, 2.7, 2.8.1-2, 3.2, 3.4-11, 4.3.1, 4.3.12-13, 4.3.20, 4.3.26-27, 4.5, 4.5.7-9, 5.2.1-3, A.1-4, B.3.4, and B.4. Additional cosmetic updates reflecting shift to Caché made throughout manual. Remove obsolete section B.3.7. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 12)</td>
</tr>
<tr class="odd">
<td>20 Jul 2006</td>
<td>Patch 50 changes: Added Appendix H. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 11)</td>
</tr>
<tr class="even">
<td>30 Jun 2006</td>
<td>Patch 51 changes: Updated sections B.4.2.2.1, B.4.4, G.1. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 10)</td>
</tr>
<tr class="odd">
<td>12 Dec 2005</td>
<td>Patch 57 changes: Updated obsolete information in sections 3.2, 3.5.2, 3.5.3, 4.5, and A.4. Verified removal of sensitive data and references to NT. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> . (Rev 9)</td>
</tr>
<tr class="even">
<td>23 Nov 2004</td>
<td>Updated Section 4.7 to reflect default partition size of 500 (Rev 8)</td>
</tr>
<tr class="odd">
<td>20 Apr 2004</td>
<td>Removed “draft” wording</td>
</tr>
<tr class="even">
<td>6 Mar 2004</td>
<td>Patch 11 - Incorporated revisions from developer feedback. (Rev 7)</td>
</tr>
<tr class="odd">
<td>14 Jan 2004</td>
<td>Patch 11 - Incorporated revisions from developer feedback. (Rev 6)</td>
</tr>
<tr class="even">
<td>22 Dec 2003</td>
<td>Formatting updates (Rev 5)</td>
</tr>
<tr class="odd">
<td>3 Nov 2003</td>
<td>Patch 10 – updated footer dates (Rev 4)</td>
</tr>
<tr class="even">
<td>31 Oct 2002</td>
<td>Changes for Patch 10 – replaced references to Clinical Specialties with Healthcare Providers (Rev 3)</td>
</tr>
<tr class="odd">
<td>30 Aug 2002</td>
<td>Added information about interface to Healthcare Provider (Rev 2)</td>
</tr>
<tr class="even">
<td>21 Sep 2000</td>
<td>Incorporated final review comments from <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> (Rev 1) –<a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></td>
</tr>
<tr class="odd">
<td>20 Sep 2000</td>
<td>Incorporated final review comments from <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a> – <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></td>
</tr>
<tr class="even">
<td>8 Sep 2000</td>
<td>Update names of accounts and groups to latest convention. <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></td>
</tr>
<tr class="odd">
<td>9 Mar 2000</td>
<td>Original version checked in – <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></td>
</tr>
<tr class="even">
<td>30 Aug 2000</td>
<td>Added reviewer comments from Amy Padgett –<a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></td>
</tr>
<tr class="odd">
<td>16 Aug 2000</td>
<td>Editing revisions – <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></td>
</tr>
<tr class="even">
<td>1 Aug 2000</td>
<td>Many editing revisions – <a href="https://vaww.edis2.med.va.gov/main">REDACTED</a></td>
</tr>
</tbody>
</table>
# # Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Preface](#preface)
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Typical configuration](#typical-configuration)
  - [Documentation Conventions](#documentation-conventions)
- [Pre-Initialization Instructions](#pre-initialization-instructions)
  - [Hardware and Software Requirements](#hardware-and-software-requirements)
  - [VA Security Policy](#va-security-policy)
  - [Sequence of Activities](#sequence-of-activities)
  - [Master Files and Software Required to Run the DICOM Gateway](#master-files-and-software-required-to-run-the-dicom-gateway)
  - [System Configuration and Global Placement](#system-configuration-and-global-placement)
  - [Resources (unique or unusual) Required for Software Product](#resources-unique-or-unusual-required-for-software-product)
  - [Sizing Considerations](#sizing-considerations)
  - [Recommendations for Software Installation and Testing](#recommendations-for-software-installation-and-testing)
    - [For an “initial” installation](#for-an-initial-installation)
    - [Software to be installed in the main VistA System](#software-to-be-installed-in-the-main-vista-system)
- [Installing the VistA Imaging DICOM Gateway](#installing-the-vista-imaging-dicom-gateway)
  - [Prerequisites for Getting Started](#prerequisites-for-getting-started)
  - [Setting Up the Operating Environment](#setting-up-the-operating-environment)
  - [Map a Network Drive for Dictionary Files](#map-a-network-drive-for-dictionary-files)
  - [Installing the Software](#installing-the-software)
    - [Installing the DICOM Gateway](#installing-the-dicom-gateway)
    - [Installing IRIS for Health](#installing-iris-for-health)
    - [Verifying IRIS Installation](#verifying-iris-installation)
    - [Setting up IRIS Service Network Account and Password](#setting-up-iris-service-network-account-and-password)
    - [Verifying IRIS Service Account Installation](#verifying-iris-service-account-installation)
- [# Securing the Gateway and IRIS](#securing-the-gateway-and-iris)
  - [Security updates in IRIS Management Portal](#security-updates-in-iris-management-portal)
    - [Login to the IRIS Management Portal](#login-to-the-iris-management-portal)
    - [Disable Telnet](#disable-telnet)
    - [Set the username and password for Management Portal Users](#set-the-username-and-password-for-management-portal-users)
    - [Configure Management Portal to Require Credentials for Login](#configure-management-portal-to-require-credentials-for-login)
    - [Turning off Journaling](#turning-off-journaling)
  - [Verifying Full Control of the ImageIn Folder](#verifying-full-control-of-the-imagein-folder)
  - [Remove Authenticated Users from httpd.exe](#remove-authenticated-users-from-httpdexe)
- [Starting and configuring the Legacy DICOM Gateway](#starting-and-configuring-the-legacy-dicom-gateway)
  - [Configure the DICOM Gateway and Load the DICOM Dictionaries](#configure-the-dicom-gateway-and-load-the-dicom-dictionaries)
    - [Name of System](#name-of-system)
    - [Location of DICOM Gateway](#location-of-dicom-gateway)
    - [DICOM Data Directories](#dicom-data-directories)
    - [Percentage of Free Disk Space](#percentage-of-free-disk-space)
    - [DICOM Dictionary Directory](#dicom-dictionary-directory)
    - [Communication Channels](#communication-channels)
    - [DICOM Image Gateway](#dicom-image-gateway)
    - [DICOM Text Gateway](#dicom-text-gateway)
    - [DICOM Routing Processor](#dicom-routing-processor)
    - [Auto-Routing Active](#auto-routing-active)
    - [Radiology](#radiology)
    - [Consults and Anatomic Pathology](#consults-and-anatomic-pathology)
    - [Send Text to commercial PACS](#send-text-to-commercial-pacs)
    - [Receive EXAM COMPLETE Message from commercial PACS](#receive-exam-complete-message-from-commercial-pacs)
    - [Kind of PACS](#kind-of-pacs)
    - [C-Move destination](#c-move-destination)
    - [Modality Worklist Provider](#modality-worklist-provider)
    - [Send CPT Modifiers](#send-cpt-modifiers)
    - [Dashes in SSN sent to PACS](#dashes-in-ssn-sent-to-pacs)
    - [TCP/IP Address for VistA](#tcpip-address-for-vista)
    - [TCP/IP Port for MUMPS-to-MUMPS Broker](#tcpip-port-for-mumps-to-mumps-broker)
    - [Mail Group](#mail-group)
    - [Display Patient Name](#display-patient-name)
    - [Access Code for Background Tasks](#access-code-for-background-tasks)
    - [Verify Code for Background Tasks](#verify-code-for-background-tasks)
    - [Modality Worklist Port Numbers](#modality-worklist-port-numbers)
    - [E-Mail Post Office](#e-mail-post-office)
    - [E-Mail Post Office Port Number](#e-mail-post-office-port-number)
    - [Specifying the Agency](#specifying-the-agency)
    - [DICOM Message Logs](#dicom-message-logs)
    - [Image with Long Values](#image-with-long-values)
  - [Loading the DICOM Dictionaries](#loading-the-dicom-dictionaries)
    - [DICOM Data Element Dictionary](#dicom-data-element-dictionary)
    - [DICOM Message Template Dictionary](#dicom-message-template-dictionary)
    - [DICOM Unique Identifier Dictionary](#dicom-unique-identifier-dictionary)
    - [Extended SOP Negotiation Table](#extended-sop-negotiation-table)
    - [DICOM PDU Types](#dicom-pdu-types)
    - [DICOM HL7 Segment and Field Dictionary](#dicom-hl7-segment-and-field-dictionary)
    - [Instruments](#instruments)
    - [Modalities](#modalities)
    - [CT Conversion History](#ct-conversion-history)
    - [Modality Worklist](#modality-worklist)
    - [Port Numbers for Text Gateway sending messages to PACS](#port-numbers-for-text-gateway-sending-messages-to-pacs)
    - [User Application Parameters](#user-application-parameters)
    - [Provider Application Dictionary](#provider-application-dictionary)
    - [Application Entity Title Dictionary](#application-entity-title-dictionary)
    - [Data Transfer](#data-transfer)
    - [Terminal Title](#terminal-title)
  - [Verify the DICOM Gateway Installation](#verify-the-dicom-gateway-installation)
  - [Logging into the DICOM Gateway](#logging-into-the-dicom-gateway)
  - [Recommended Icons – DGW Terminal sessions](#recommended-icons-dgw-terminal-sessions)
  - [Gateway Tasks Related to Gateway Types](#gateway-tasks-related-to-gateway-types)
- [Appendix A Creating Automatic Startup of IRIS Terminal Sessions](#appendix-a-creating-automatic-startup-of-iris-terminal-sessions)
  - [A.1 Introduction](#a1-introduction)
  - [A.2 Customize DICOM Gateway Startup.bat](#a2-customize-dicom-gateway-startupbat)
  - [A.3 TERMINALTITLE.DIC](#a3-terminaltitledic)
  - [A.4 Update TERMINALTITLE.DIC Menu](#a4-update-terminaltitledic-menu)
- [Appendix B Master Files](#appendix-b-master-files)
  - [B.1 Overview](#b1-overview)
  - [B.2 Master Files](#b2-master-files)
    - [B.2.1 Master File Menu Options](#b21-master-file-menu-options)
    - [B.2.2 General Formatting Issues](#b22-general-formatting-issues)
  - [B.3 Static Master Files](#b3-static-master-files)
    - [B.3.1 ELEMENT.DIC](#b31-elementdic)
    - [B.3.2 HL7.DIC](#b32-hl7dic)
    - [B.3.3 CTPARAM.DIC](#b33-ctparamdic)
    - [B.3.4 SCPLIST.DIC](#b34-scplistdic)
    - [B.3.5 TEMPLATE.DIC](#b35-templatedic)
    - [B.3.6 UID.DIC](#b36-uiddic)
    - [B.3.7 Additional Data](#b37-additional-data)
  - [B.4 Site-Specific Master Files](#b4-site-specific-master-files)
    - [B.4.1 AETITLE.DIC](#b41-aetitledic)
    - [B.4.2 INSTRUMENT.DIC](#b42-instrumentdic)
    - [B.4.3 MODALITY.DIC](#b43-modalitydic)
    - [B.4.4 PORTLIST.DIC](#b44-portlistdic)
    - [B.4.5 SCULIST.DIC](#b45-sculistdic)
    - [B.4.6 WORKLIST.DIC](#b46-worklistdic)
    - [B.4.7 Editing the Clinical Specialty DICOM & HL7 file](#b47-editing-the-clinical-specialty-dicom-hl7-file)
- [Appendix C Networking Fundamentals](#appendix-c-networking-fundamentals)
  - [C.1 Overview](#c1-overview)
  - [C.2 IP Addresses and Subnet Masks](#c2-ip-addresses-and-subnet-masks)
    - [C.2.1 Example 1 – Original Configuration – Seven-bit Subnet Mask](#c21-example-1-original-configuration-seven-bit-subnet-mask)
    - [C.2.2 Example 2 – Change to Eight-bit Subnet Mask](#c22-example-2-change-to-eight-bit-subnet-mask)
    - [C.2.3 Example 3 – Keep Seven-Bit Subnet Mask and Add Secondary IP Address to Servers](#c23-example-3-keep-seven-bit-subnet-mask-and-add-secondary-ip-address-to-servers)
    - [C.2.4 Example 4 – Use Multiple Subnets](#c24-example-4-use-multiple-subnets)
  - [C.3 Default Gateways](#c3-default-gateways)
  - [C.4 HOSTS File](#c4-hosts-file)
- [Appendix D Diagnostic Networking Tools](#appendix-d-diagnostic-networking-tools)
  - [D.1 HOSTDIR.BAT](#d1-hostdirbat)
  - [D.2 IPCONFIG](#d2-ipconfig)
  - [D.3 PING](#d3-ping)
  - [D.4 TRACERT](#d4-tracert)
  - [D.5 NETSTAT](#d5-netstat)
  - [D.6 DICOMEcho](#d6-dicomecho)
  - [D.7 SendImage](#d7-sendimage)
- [Appendix E Port Numbers for VistA Imaging DICOM Gateway Applications](#appendix-e-port-numbers-for-vista-imaging-dicom-gateway-applications)
- [Appendix F VistA Imaging DICOM Gateway Application Entity (AE) Titles](#appendix-f-vista-imaging-dicom-gateway-application-entity-ae-titles)
- [Appendix G Setting Up the MUMPS-to-MUMPS Broker](#appendix-g-setting-up-the-mumps-to-mumps-broker)
- [Appendix H Change IRIS Password](#appendix-h-change-iris-password)
- [Appendix I KIDS Package to Install in the VistA System](#appendix-i-kids-package-to-install-in-the-vista-system)
  - [I.1 VistA -PACS Radiology Interface Setup Instructions](#i1-vista-pacs-radiology-interface-setup-instructions)
  - [I.2 VistA -PACS ADT Interface Setup Instructions](#i2-vista-pacs-adt-interface-setup-instructions)
  - [I.3 Change Subscribers](#i3-change-subscribers)
  - [I.4 Radiology HL7 Protocols and Imaging Subscribers](#i4-radiology-hl7-protocols-and-imaging-subscribers)
  - [I.5 Entering Facility Names for Sending/Receiving Applications for PACS Messaging](#i5-entering-facility-names-for-sendingreceiving-applications-for-pacs-messaging)
  - [I.6 Service Account](#i6-service-account)
This guide is written to assist in the installation of the VistA Imaging DICOM Gateway. The recommended background of those installing this software includes knowledge of Windows and network component installation.
This guide also provides configuration specifications needed by the commercial DICOM vendors to properly interface their equipment to VistA.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DICOM is an acronym for Digital Imaging and Communications in Medicine standard. DICOM brings open systems technology to the medical imaging marketplace and enables VistA to communicate directly with commercial medical imaging equipment.

DICOM is a set of networked client/server applications that are implemented on top of TCP/IP. DICOM is part of the VistA networked application suite, along with CPRS, JLV, Kernel Broker, MS Exchange, and Windows file servers. Similar networking techniques are used for installing and maintaining these applications.

The VistA Imaging DICOM Gateway is a suite of VA-developed software that facilitates the transmission of DICOM images between the image acquisition modalities and the equipment on which these images are permanently stored. The images and information about them are stored in the VistA database as a part of the patient record. Once images have been stored in the system, they are available for viewing from any VistA clinical or diagnostic workstation.

The software in the VistA Imaging DICOM Gateway is intended to run on one or more servers (per site) that are loosely coupled with the VistA Hospital Information System (HIS).

The gateway has two functional areas that process imaging service requests: the Legacy DICOM Gateway (LDGW) service and the HDIG service.

The LDGW services are written in MUMPS and runs as a set of tasks within a InterSystems IRIS for Health™ system (IRIS). The interface uses the TCP/IP protocol to communicate with commercial DICOM devices and Windows file servers, and the VistA hospital information system (HIS). To operate the system, the IRIS Server needs to be running first. The various subtasks of the VistA Imaging Legacy DICOM Gateway then run invisibly in the background. The LDGW should be installed on all DICOM Gateways. Depending on the purpose of the gateway, several different configuration options can be used: Text Gateway, an Image Gateway, a Routing Processor, or any combination thereof.

The Hybrid DICOM Image Gateway (HDIG) is the newest component of the DICOM Gateway and enables the storage of the newly supported Service Object Pair (SOP) classes.

## Typical configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The diagram below shows the most common configuration of a system in which the VistA Imaging DICOM Gateway is deployed.

![Figure 1 VISA and the DICOM Gateway](vista-imaging-dicom-gateway-installation-guide/002.png)

*Figure 1 VISA and the DICOM Gateway*

(This image is out of date and will be updated with the next patch)

In the previous diagram, each computer has a dedicated function. It is possible to assign any combination of functions to any of these computers.

In theory, one computer could perform all tasks. In practice, however, it is much more efficient to assign specific tasks to specific computers. The typical configuration is one text gateway and one or more image gateways.

No more than one multi-image device (such as a CT or MRI) should be placed on a gateway since every image must go through the IRIS terminal session for processing images on the gateway. In addition to this, other single-image modalities like CR or US can be placed on the same DICOM Gateway.

> **NOTE:** This document describes the LDGW. All subsequent references to the Image Gateway refer to the Legacy DICOM Gateway and not the Hybrid DICOM Image Gateway (HDIG). For information on the HDIG see the *VistA Imaging Hybrid DICOM Image Gateway (HDIG) Installation Guide* and the *VistA Imaging DICOM Gateway User Manual*. These documents can be found on the VA Software Document Library (VDL) <https://www.va.gov/vdl/application.asp?appid=105>.

## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following conventions are used in this manual.

| Convention    | Description                                                                                                                                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bold type     | User keyboard entry.                                                                                                                                                                                              |
| \<Enter\>     | Return key or Enter key.                                                                                                                                                                                          |
| \<Control+x\> | A keystroke that involves pressing the control-key, keeping it depressed, and then pressing another key.                                                                                                          |
| \<SHIFT\>     | Shift key.                                                                                                                                                                                                        |
| \<ESC\>       | Escape key.                                                                                                                                                                                                       |
| \<Num Lock\>  | Top left key on the numeric keypad (above the 7), may also be labeled Numeric Lock; this makes any keypad key activate the number shown on its surface; it is the equivalent of a SHIFT LOCK for alphabetic keys. |

# Pre-Initialization Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Hardware and Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A site may have one or more servers running the VistA Imaging DICOM Gateway software.

It is assumed that a network will be present with sufficient capacity to transport image files in a reasonable amount of time. See [*Appendix C*](#appendix-c-networking-fundamentals) for details about network set-up, which needs to be completed *before* any VistA Imaging DICOM Gateway computer can be installed.

The hardware requirements for each processor are the same.

- The Servers should have enough memory (16+ G RAM) to run the operating system. A 17-inch (or larger) color monitor configured to 1280 x 1024 resolution, and a minimum of 4 virtual processors should be used.
- The DICOM Gateway software from patch MAG\*3.0\*319 forward is approved to run on Windows Server 2019 based on VA Policies and Procedures at this time.
- Any disks that are permanently mounted on the system must be formatted using the NTFS format (the FAT format is no longer permitted at the VA).
- IRISHealth version 2022.1.0.209.0.21702 or newer
- VA-Mandated, up-to-date, virus protection software. (i.e.: McAfee)
- The installer needs local administrator privileges on any machine for the duration of the installation procedure.

It will usually take less than one hour to complete the entire installation process for one server. Configuration and interfacing with DICOM devices will take additional time.

> **CAUTION:** When performing an installation as an upgrade of the VistA Imaging Legacy DICOM Gateway, review [Appendix B.4](#b.4-site-specific-master-files) for details about master files that may need to be upgraded manually, i.e.: option 4-2-9 Reinitialize All the DICOM Master Files, as a dictionary change might come with the new LDGW patch.

Instructions are provided in [Appendix C](#appendix-c-networking-fundamentals) for setting up the network between the various DICOM related processors and the VistA system.

Instructions for adding a “modality” are described in the .[*VistA Imaging* DICOM User Manual](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_dicomug.pdf)

Instructions are provided in [Appendix A](#appendix-a-creating-automatic-startup-of-iris-terminal-sessions) for creating Terminal sessions to start components of the Gateway software.

## VA Security Policy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA Security Policy requires that on many computers, specific software be installed to ensure that the machines are running the most up-to-date virus protection software.

While it is acknowledged that any computer that is connected to the network must have adequate virus protection, software must not be installed on a medical device that causes it to reboot while it might be processing essential data. As a result, some software cannot be permitted on any VistA DICOM Gateway. Follow Regional Business Critical Systems policy for obtaining/managing software including McAfee updates and exclusions.

> **NOTE:** Steps to secure the DICOM Gateway database are outlined in [Securing the Gateway and IRIS.](#securing-the-gateway-and-iris)

## Sequence of Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The correct sequence of activities for most patches is as follows:

1.  Perform KIDS install for any Kernel components (e.g., MUMPS-to-MUMPS Broker).
2.  Stop all C-Store processes; leave image processing running.
3.  If applicable stop HDIG Tomcat Service.
4.  Perform KIDS install for Imaging patch on VistA.
5.  Perform any updates to user accounts on VistA.
6.  Stop all gateway processes.
7.  Load Imaging patch on gateways.
8.  Configure gateways.
9.  Connect to VistA (using MUMPS-to-MUMPS Broker).
10. Test user accounts.
11. Start regular gateway processing.
12. Monitor VistA error trap.

## Master Files and Software Required to Run the DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software for the VistA Imaging DICOM Gateway is distributed as a single executable file (named MAG3_0Pnnn_DICOM_SETUP.EXE). This file performs an installation using the tool-set from InstallShield. This file may be downloaded from the VA Software Download server:  
  
[https://download.vista.med.va.gov/index.html/SOFTWARE/](https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdownload.vista.med.va.gov%2Findex.html%2FSOFTWARE%2F&data=05%7C01%7C%7Caf73e63395604c44a5b108db2a164ab5%7Ce95f1b23abaf45ee821db7ab251ab3bf%7C0%7C0%7C638150047446985621%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=udMmhjG5RnyD1qCajoUTIrmSu6KiYvZ3l0e3kyJxYz0%3D&reserved=0)

When the installation process is completed, all software for the VistA Imaging DICOM Gateway will be installed. When a patch contains components that reside on a DICOM Gateway as well as components that reside inside the VistA Hospital Information System, the distribution will include a VA-Kernel KIDS file, as well as an InstallShield set-up executable.

> **NOTE:** It is recommended that users copy the install file to a local hard drive on the machine before starting. (For example: MAG3_0P319_DICOM_SETUP.EXE)

## System Configuration and Global Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some global variables are local to the DICOM Gateway, while others are maintained on the VistA system. The global variables that reside on the VistA system are:

|           |                         |                                         |
|-----------|-------------------------|-----------------------------------------|
| Name  | Initial Size \[MB\] | Growth                              |
| ^MAGD     | 0.1                     | Does not grow beyond 0.5 MB             |
| ^MAGDAUDT | 0                       | 1 MB per 250,000 studies                |
| ^MAGDHL7  | 0[^1]                   | Should be purged when size exceeds 5 MB |
| ^MAGDOUTP | 0                       | Does not grow beyond 0.5 MB             |

^MAGD is for the “DICOM Correct” application and error handling procedures. It contains information about every image file that fails a patient and study lookup on the main system. When manual corrections are made, the entries are deleted from ^MAGD, so it does not continually grow.

^MAGDAUDT counts the number of different types of messages per day, as well as the number of images acquired from each instrument.

^MAGDHL7 contains all the HL7 messages passed from the HIS/RIS to the DICOM Gateway. The data in it can be periodically deleted, so that it will plateau to some maximum size and then be trimmed back.

^MAGDOUTP contains the requests for DICOM Image transmission from VistA to a remote Application Entity. Since the requests are deleted after being satisfied, the global remains very small.

> **NOTE:** The global variables ^MAGDHL7 and ^MAGDWLST will be created as the system is being used, ^MAGDHL7 on the main VistA System, and ^MAGDWLST on the VistA DICOM Text Gateway System.

## Resources (unique or unusual) Required for Software Product

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging DICOM Gateway will require a high-speed network capability. Storage of acquired images will require a multi-terabyte storage capability. Refer to [Appendix C](#appendix-c-networking-fundamentals) for more information.

## Sizing Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A typical installation uses about <u>4GB</u> of disk space in the C drive for the IRIS system, and the various supporting files. As images are acquired, disk space will be used temporarily, until the images have been processed by the DICOM Gateway application and moved to their permanent storage. When a site acquires a new modality and images cannot be processed until parameters are set up properly to support that modality, the temporary image storage may grow to several gigabytes.

## Recommendations for Software Installation and Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation procedure described in the following chapters involves the following steps.

### For an “initial” installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the VistA Imaging DICOM Gateway on a new server, perform the following steps:

1.  Create a number of files and directories on the target system. (e.g.: C:\DICOM, C:\\ C:\InterSystems …etc.)
2.  Create a number of processing icons on the target system.
3.  Create IRIS environment.
4.  Establish master files containing site-specific information on common network share(lists of modalities, instruments, port numbers, and so forth).
5.  Load master file information into IRIS database.
6.  Create the shortcuts for the various instruments.
7.  Establish IRIS logon security.

Most of these steps can be executed in an automated fashion using the scripts from [Chapter 3](#installing-the-vista-imaging-dicom-gateway).

### Software to be installed in the main VistA System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to software to be installed on the DICOM Gateway server(s), there is also <u>a KIDs file</u> to be installed in the main VistA system. See [Appendix I](#appendix-i-kids-package-to-install-in-the-vista-system).

# Installing the VistA Imaging DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter provides instructions for installing the VistA Imaging Legacy DICOM Gateway (LDGW).

## Prerequisites for Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Fully patched Windows operating system is installed on the target server.
2.  Suitable up-to-date virus protection software has been installed and exclusions configured.
3.  The VistA Imaging KIDS package must be installed. See the [*VistA Imaging Installation Guide*](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGinstallgd.pdf) for details.
4.  The DICOM Gateway installation MAG3_0Pnnn_DICOM_SETUP.EXE file has been downloaded from the VA SOFTWARE download site  
    >   
    > <https://download.vista.med.va.gov/index.html/SOFTWARE/>  
    >   
    > and is placed on the local drive of the target server LDGW.
5.  Local administrator rights to the target computer (not domain admin user rights).
6.  If either the image directory or the master files directory will reside on network drives, these drives should be mapped consistently on the target computer (with the same drive letters). Any existing DICOM\DICT master files should be backed up and saved before the new installation.

## Setting Up the Operating Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following steps will generally make the use of the system easier.

1.  Complete the installation of Microsoft Windows as the local administrator and not the VHAxxxIA account.
2.  Apply the latest approved Service Packs for Microsoft Windows operating system.
3.  The system/server should be part of the va.gov domain.
4.  When VistA Imaging is first installed, ensure a user account has been added to the master domain (the VISN’s domain) named VHAvv\VHAxxxIA, where xxx are the three letters that identify the site and vv is the identification of the VISN (usually two digits). If this user is not yet set up, see the [VistA Imaging Installation Guide](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGinstallgd.pdf) for details on creating this user.
5.  On each gateway/server add the VHAvv\VHAxxxIA user to the local Administrators group.
6.  Configure the Network Interface for TCP/IP. Do not use Microsoft’s DHCP to assign any addresses. For each system, use a static IP address, a default gateway address, and a subnet mask.
7.  Make sure that the DNS information is defined according to the VA’s national mandates. Contact your local LAN Administrator with any questions about the settings.
8.  If a local Domain Name Server (DNS) system is being used, make sure this local DNS is the first DNS server in the list.
9.  From this point forward, login as VHAvv\VHAxxxIA to perform the rest of the installation.
10. If any new disk-drives are installed, they must be formatted using the NTFS format.

## Map a Network Drive for Dictionary Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When only a single computer is to be installed at a site and this computer will perform all DICOM Gateway tasks, this step may be skipped. However, in a networked configuration with multiple DICOM Gateways, it is usually beneficial to use a shared drive to store the dictionary files and master files, so that all processors on the network can share the same resources. This will also make future maintenance a lot easier. In the examples throughout this manual, the assumption is made that the “dictionary drive” is mapped as drive “F:”.

## Installing the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you install the DICOM Gateway:

- Check to ensure the logon user (with local admin right) has a …\\Administrator\]\Local Settings\Temp folder. If the Temp folder does not exist, create it, and then ensure that the logon user has all the privileges to access that folder.
- Review the Patch Description for patch-specific instructions.

### Installing the DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The screenshots are provided as a representation and the actual screenshots may show different patch numbers, path locations and other details.

1.  If you have not already done so, login as VHAvv\VHAxxxIA.
2.  Right click MAG3_0P319_DICOM_setup.exe to run as administrator to start the InstallShield wizard and wait until the installation procedure is extracted. This may take a few minutes.

![](vista-imaging-dicom-gateway-installation-guide/003.png)

> **NOTE:** Some newer systems may take several minutes and then be presented with this screen:

![](vista-imaging-dicom-gateway-installation-guide/004.png)

3.  When the User Account Control window appears, click Yes.

![](vista-imaging-dicom-gateway-installation-guide/005.png)

4.  A Preparing to Install window will appear. No user action required.

![](vista-imaging-dicom-gateway-installation-guide/006.png)

5.  When the Text Data Directories dialog box displays, verify that the correct number of Text Data Directories is indicated. Then click Next. On systems that are already function as Text Gateways, the proper number of data directories will be detected automatically.

> ![](vista-imaging-dicom-gateway-installation-guide/007.png)

> For most other systems, you can use the default number – 2 (Two). (Only one data directory is needed.)

6.  The InstallShield Wizard Dialog will open, click Next.

> ![](vista-imaging-dicom-gateway-installation-guide/008.png)

7.  In the License Agreement dialog box displays, review the terms of the license agreement, click I accept the terms of this license agreement, and then click Next.

> ![](vista-imaging-dicom-gateway-installation-guide/009.png)

8.  Specify the environment which you are installing the DICOM Gateway when prompted by selecting the appropriate agency option: VA (Department of Veterans Affairs) or IHS (Indian Health Services) Click Next,

> ![](vista-imaging-dicom-gateway-installation-guide/010.png)

9.  When InstallShield prompts you to specify the destination folder (the folder in which the Legacy DICOM Gateway software is installed), make sure that the installation program is pointing to the C:\\ drive (local system drive). The installation will likely fail if you choose an alternate path Click Next.

> ![](vista-imaging-dicom-gateway-installation-guide/011.png)

10. Choose either Custom or Complete setup, depending on your needs. If dictionary files already exist on a shared drive, chose Custom. Then, click Next.

![](vista-imaging-dicom-gateway-installation-guide/012.png)

1.  The Custom setup allows you to change the default location of the folders for the images (Image_Data) and the dictionary files (DICOM_Dictionaries). This is convenient if you want the images to be stored on a different drive (not the default, which is C). You must use the Custom option if you want the dictionary files to be installed on a network drive. If you choose Custom, continue with step c.
2.  If you choose the Complete setup, you will not be able to change the default location (C:\DICOM\\ for the folders for the images and the dictionary files. If you choose Complete, continue with step 13.

> If you selected the Custom setup type, the Custom Setup dialog box displays.

3.  In the Custom Setup dialog box, click the item (not the icon, but the actual item name) in the list and verify that the Install To area shows the correct folder for the installation.

> For the Image_Data and DCF Runtime items, the location of these directories should NOT be changed.

> ![](vista-imaging-dicom-gateway-installation-guide/013.png)

4.  For the DICOM_Dictionaries (the master file directory), if you need to change the location of this directory, click Change and then use the dialog box that displays to select the appropriate location.

> ![](vista-imaging-dicom-gateway-installation-guide/014.png)

> ![](vista-imaging-dicom-gateway-installation-guide/015.png)

> **NOTE:** The DICOM dictionary directory is usually on a shared network system and is used to hold DICOM master files. F:\DICOM is typically the DICOM dictionary directory. You may select any other device letter or Fully Qualified Domain Name (FDQN) with shared network drive (i.e.: \\VHAxxxclu10a...\GW_dic_files), however.

5.  In a typical installation, DICOM_Dictionaries are installed in the \DICOM\Dict directory on a network drive and Image_Data and DCF Runtime is installed on the C: drive. The installation process does not overwrite site-configurable master files.
6.  For site configurable master files, like AE_TITLE.DIC, the installation first copies the matching sample file (AE_TITLE.SAMPLE in this example) to the master files directory. If the master file does not already exist, the installation renames the sample file and makes it a master file. In the example, it will rename AE_TITLE.SAMPLE to AE_TITLE.DIC. If the master file exists, the installation keeps the sample file in the master files directory for reference.
7.  Site-configurable master files include AE_Title, Instrument, Modality, Portlist, Route, SCU_List, and Worklist.
11. Click the names of all components to verify that they are set to be installed onto the correct disk drive.
12. After verifying that all components are set to be installed in their appropriate destinations, click Next in the Custom Setup dialog box.
13. If you want to change any of the installation settings or if you are not sure about the value of a parameter, you can click Back to go back to the window where that setting may be modified. Otherwise, click Install to begin the installation process.

> ![](vista-imaging-dicom-gateway-installation-guide/016.png)

> While the installation is proceeding, the status of the installer will be displayed in a progress window. Do not click any buttons while this window is visible (the only button available is Cancel and clicking it will discontinue the installation).

> As the installation proceeds, a progress bar will be displayed. Several message boxes will pop up and disappear throughout the install process. When the reminder window “Don’t forget to run ‘Install IRIS’ located on your desktop.” appears, click OK.

> ![](vista-imaging-dicom-gateway-installation-guide/017.png)

14. When the installation is complete, the last window displays. Click Finish to complete the 1<sup>st</sup> part of installation of the new DICOM Legacy Gateway software.

> ![](vista-imaging-dicom-gateway-installation-guide/018.png)

> In some cases, there may be additional tasks that you must perform. In this scenario, a message box will be displayed that indicates the remaining installation steps.

### Installing IRIS for Health

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you install the DICOM Gateway you will see a DICOM Install\_IRIS icon (short cut) on your desktop. ![](vista-imaging-dicom-gateway-installation-guide/019.png)

To install IRIS:

1.  Right-click the Install_IRIS icon on your desktop and then select “Run as Administrator”. (This icon was created when you installed the DICOM Gateway in the preceding steps.)

![](vista-imaging-dicom-gateway-installation-guide/020.png)

If prompted “Do you want to allow this app to make changes to your device” click YES.

![](vista-imaging-dicom-gateway-installation-guide/021.png)

2.  The installation program opens a command prompt window on the Task Bar. Click on the command prompt window on the Task Bar to see the full command prompt window.

    ![](vista-imaging-dicom-gateway-installation-guide/022.png)
3.  During the installation of IRIS, a Setup message box will appear and disappear.

    ![](vista-imaging-dicom-gateway-installation-guide/023.png)

    ![](vista-imaging-dicom-gateway-installation-guide/024.png)

    This box indicates the progress of the installation; you do not need to do anything while this message box is visible.
2.  Once install has finished click on the command prompt. Wait until you see the ‘Install Complete’ message on the command prompt window. Then, press any key or click in the window to close it.

    ![](vista-imaging-dicom-gateway-installation-guide/025.png)

### Verifying IRIS Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing IRIS, verify that it is properly installed. There is an IRIS launcher icon in the system tray (usually located on the lower right side of the display) that gives access to the various management functions for IRIS. This document will refer to the IRIS launcher as the “IRIS ICON.”

When IRIS for Health is inactive, this icon is grey:

![](vista-imaging-dicom-gateway-installation-guide/026.png)

When IRIS for Health is active, this icon has color blue/white:

![](vista-imaging-dicom-gateway-installation-guide/027.png)

To verify that IRIS is installed:

1.  Right-click the IRIS icon located in the system tray.

    ![](vista-imaging-dicom-gateway-installation-guide/028.png)
2.  Click About. If IRIS is installed, the following About screen displays. The most current IRIS version is displayed.

![](vista-imaging-dicom-gateway-installation-guide/029.png)

> **NOTE:** Once IRIS has been installed using the automated procedure shown in the previous sections, it will automatically start each time the computer is re-booted. Under normal circumstances, the end user will not have to act to start or stop the IRIS system. Additional processes, such as listener and IRIS terminal sessions, must be started to make the gateway fully operational.

The various options related to configuration of the IRIS system are described in the documentation that comes with the IRIS system and are provided through the menu that is shown above. Some configuration options are accessed through the menu option labeled Management Portal.

### Setting up IRIS Service Network Account and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To finally complete the IRIS installation, set up the IRIS Service with Imaging Administrator (IA) Network Account and Password. The username and password for IRIS must be set using the IRISinstall.exe from the Command Prompt for the LDGW to function properly.

1)  Run Administrator Command Prompt

> Note: To open the Administrator: Command Prompt by Run with ‘CMD’- then select ‘Run as Administrator’ on Windows server 2019.

> ![](vista-imaging-dicom-gateway-installation-guide/030.png)

2)  A User Access Control window will appear, click Yes

![](vista-imaging-dicom-gateway-installation-guide/031.png)

3)  Enter the following one-line command:

> C:\InterSystems\IRISHealth\bin\\IRISinstall.exe setserviceusername IRIS "{*IA network service account username(*“vhann\vhaxxxia”*)}*" "{*IA network service account password}*"

> Note: there is a space between IRIS, “username” and “password”. Example C:\InterSystems\IRISHealth\bin\IRISinstall.exe setserviceusername IRIS "vhann\vhaxxxia" "password"

> Then press \<Enter\>

> ![](vista-imaging-dicom-gateway-installation-guide/032.png)

> After seeing ‘service Username and Password Set’, Reboot the DICOM Gateway server for the IA network service account come into effect.

### Verifying IRIS Service Account Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When IRIS is restarted after the server reboot. Check the Windows Services to make the IA service account is set in InterSystems IRIS Controller service.

1.  From the Windows Start Menu, click Start \| Administrative Tools \| Services, or Server Manager \| Tools \| Services.
2.  Right-click InterSystems IRIS Controller for IRIS.
3.  Select Properties.

![](vista-imaging-dicom-gateway-installation-guide/033.png)

4.  On the logon tab, verify that IA Account is being used.

> ![](vista-imaging-dicom-gateway-installation-guide/034.png)

# # Securing the Gateway and IRIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section highlights some general issues that are relevant during the installation of the VistA Imaging DICOM Gateway software. Detailed information about security issues related to the VistA Imaging DICOM Gateway is documented in the VistA Imaging Security Manual.

## Security updates in IRIS Management Portal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you install MAG3_0Pnnn_DICOM_setup.exe on the Gateway with IRIS, perform the following steps to secure the gateway database. All the Legacy DICOM Gateway (LDGW) short-cut/Menu tree options will still depend on VistA user authentication (access/verify code).

### Login to the IRIS Management Portal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Windows Task Bar, click on the up arrow, click on the IRIS icon and then select Management Portal. The IRIS login screen is displayed.

> Note: If your machine does not have a web browser installed, access the Management Portal on your local machine. Below is a sample URL syntax.

> [*http://servername:52773/csp/sys/UtilHome.csp*](http://servername:52773/csp/sys/UtilHome.csp)

2.  Enter the IRIS username and password.

> Note: If this is a fresh LDGW server installation, at the first time you login to the Management Portal , use the default user name '\_system' and password 'SYS' to login Management Portal. Then change the Telnet configuration/Security setting accordingly.

### Disable Telnet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To disable Telnet service on the DICOM Gateway follow the steps below:

1.  Click on System Administration, then click on Security, then click on Services.

> ![](vista-imaging-dicom-gateway-installation-guide/035.png)

2.  Select the %Service_Telnet link.

![](vista-imaging-dicom-gateway-installation-guide/036.png)

3.  Uncheck Service Enabled, select the Save button.

![](vista-imaging-dicom-gateway-installation-guide/037.png)

### Set the username and password for Management Portal Users 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This process configures the Management Portal and Studio to require password authentication (also known as the “IRIS login”) and not to allow unauthenticated access. DO NOT check the Remember Password box for the security policy.

1.  Click on System Administration, then click on Security, then click on Users.

> ![](vista-imaging-dicom-gateway-installation-guide/038.png)

3.  The System – Security Management – Users page is displayed.

> ![](vista-imaging-dicom-gateway-installation-guide/039.png)

4.  On the Users page click on the Admin user to modify/reset password. This displays the \[General\] tab of the Edit User page for configuring users.

![](vista-imaging-dicom-gateway-installation-guide/040.png)

5.  On the Edit Definition for user Admin page, click on “Enter new password” radio button

![](vista-imaging-dicom-gateway-installation-guide/041.png)

6.  Set values for only the following user properties:

> •Password (required) — Enter new password value.

| NOTE: The Veterans Administration recommends no fewer than 16 characters to include 1 uppercase, 1 lowercase, 1 number and 1 special character. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|

> •Confirm Password (required) — Enter new password value to confirm.

> *Make note of the new password*.

7.  Click the Save button to save the password.

| NOTE: If the two passwords do not match, an error message will pop up prompting the user to reenter the passwords. |
|------------------------------------------------------------------------------------------------------------------------|

8.  Click on Users in the breadcrumb trail to go back to the System – Security Management – Users page.

> ![](vista-imaging-dicom-gateway-installation-guide/042.png)

9.  Repeat steps 1 through 7 to create a password for the following users:
- \_SYSTEM
- CSPSystem
- SuperUser

### Configure Management Portal to Require Credentials for Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This process configures Management Portal services to require password authentication and not to allow unauthenticated access. Once you finish modifying the %Service items and CSP Applications, the user will be required to enter their username and password to access the Management Portal and CSP relative features.

#### %Service

1.  Click on System Administration, then click on Security, then click on Services.

![](vista-imaging-dicom-gateway-installation-guide/043.png)

2.  The System - Security Management – Services page is displayed.

![](vista-imaging-dicom-gateway-installation-guide/044.png)

3.  On the Services page, select %Service_Console from the Name column to edit. This displays the Edit Definition for service %Service_Console to configure the authentication method. In the Definition window, verify that both the Service Enabled and Unauthenticated check boxes are checked.

![](vista-imaging-dicom-gateway-installation-guide/045.png)

4.  Click Save.

#### CSP Applications

1.  From the Management Portal home page, select System Administration, then select Security, then select Applications, then select Web Applications.

![](vista-imaging-dicom-gateway-installation-guide/046.png)

2.  Select /csp/sys/exp. The Edit Web Applications /csp/sys/exp page is displayed.

![](vista-imaging-dicom-gateway-installation-guide/047.png)

3.  Check the Unauthenticated box and then uncheck the Password box. Click Save.

> ![](vista-imaging-dicom-gateway-installation-guide/048.png)

4.  When the changes to the application have been saved, the message “Application saved” will be displayed. Click on the Web Applications breadcrumb trail to return to the list of Web Applications. Repeat steps 1 through 3 for the following Web Applications:
- /csp/sys/mgr
- /csp/sys/op
- /csp/sys/sec
5.  When finished, the Web Applications table should look like the figure below.

![](vista-imaging-dicom-gateway-installation-guide/049.png)

### Turning off Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Setting the DICOM database item, Global Journal State, option to “No” corrects the excessive disk space usage and an added benefit is that the image processing speed increased significantly. If sites are experiencing this problem, it is recommended that they turn the journaling off.

1.  Click on System Administration, then click on Configuration, then click on System Configuration, then click on Local Databases.

> ![](vista-imaging-dicom-gateway-installation-guide/050.png)

2.  The Local Databases screen appears:

> ![](vista-imaging-dicom-gateway-installation-guide/051.png)

3.  Click on DICOM to display the Database Properties screen:

> ![](vista-imaging-dicom-gateway-installation-guide/052.png)

4.  Uncheck the ‘Global Journal State’ checkbox and then click the ‘Save’ button and close Management Portal.

    ![](vista-imaging-dicom-gateway-installation-guide/053.png)![](vista-imaging-dicom-gateway-installation-guide/054.png)

## Verifying Full Control of the Image_In Folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing the Legacy DICOM Gateway, verify that the System Domain Admin Service Account (IA account) has full control of the C:\DICOM\Image_In folder.

1.  In Explorer, right click the c:\DICOM\Image_In and select Properties.
2.  Select the Security tab. The following Image_In Properties screen is displayed

![](vista-imaging-dicom-gateway-installation-guide/055.png)

## Remove Authenticated Users from httpd.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authenticated Users must be removed from the httpd.exe file once Iris is installed to avoid creating a security violation:

1.  Navigate to the C:\InterSystems\IRISHealth\httpd\bin folder in Windows Explorer.

![](vista-imaging-dicom-gateway-installation-guide/056.png)

2.  Right-click on HTTPD.EXE and then click on Properties to display the Properties screen.

![](vista-imaging-dicom-gateway-installation-guide/057.png)

3.  Click on the Security tab and then click on the Advanced button to display the Advanced Security Settings window.

![](vista-imaging-dicom-gateway-installation-guide/058.png)

4.  Select Authenticated Users.

![](vista-imaging-dicom-gateway-installation-guide/059.png)

5.  Click on the Remove button to delete the Authenticated Users.

![](vista-imaging-dicom-gateway-installation-guide/060.png)

6.  Click on the OK button to close the window and finalize the process.

![](vista-imaging-dicom-gateway-installation-guide/061.png)

# Starting and configuring the Legacy DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start configuring the DICOM Gateway

1.  Double Click on the short_cut ‘Initial Startup.bat’ ![](vista-imaging-dicom-gateway-installation-guide/062.png) on Windows desktop press return for Y

    ![](vista-imaging-dicom-gateway-installation-guide/063.png)
2.  Enter your VistA Full Qualified Domain Name (FQDN) or IP address, and the port \# for M-M broker listener. (Only required 1<sup>st</sup> time LDGW configuration)

    ![](vista-imaging-dicom-gateway-installation-guide/064.png)
3.  Enter your LDGW VistA account Access/Verify code to login.

## Configure the DICOM Gateway and Load the DICOM Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the process of completely configuring a VistA Imaging DICOM Gateway, including loading all the dictionaries.

> **NOTE:** Individual portions of the VistA Imaging DICOM Gateway can be selectively updated as well. This operation is described in the [*VistA Imaging DICOM Gateway User Manual*](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_dicomug.pdf).

1.  To configure the DICOM Gateway select menu option 4-2-2:

> 4 System Maintenance

> → 2 Gateway Configuration and DICOM Master Files

> → 2 Update Gateway Configuration Parameters

### Name of System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system title is a short character string that appears on the top of the main DICOM application menu. Examples:

“Washington DICOM Image Server System \#3”

“New Orleans DICOM Text Gateway”

> Please enter the system title: IMAGUSER's Gateway \<Enter\>

### Location of DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The configuration program will query the VistA system in order to obtain a list of the locations that are operational for the site. When a DICOM Gateway is part of a site that has only one location, the software will merely display the name of that location, and not ask the end-user for any input, e.g.:

> This computer is currently located at SALT LAKE CITY (660)

Otherwise, the end-user will be asked to identify the name of the location for which the DICOM Gateway in question will be operating.

### DICOM Data Directories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DICOM data directories are located on the local system and are used to hold both the DICOM text and image files. C:\DICOM is typically the DICOM data directory. However, you may select another device letter (C:-Z:).

> Please enter the device letter for

> the DICOM text directory: c:// \<Type Response\> \<Enter\>

> Please enter the device letter for

> the DICOM image directories: c:// \<Type Response\> \<Enter\>

### Percentage of Free Disk Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software will cease storing image files when the amount of free disk space drops below a certain threshold. The usual value for this threshold is 15%.

> Please enter the percentage of free disk space

> required to allow storage of image files: 15%// \<Type Response\> \<Enter\>

### DICOM Dictionary Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DICOM dictionary directory is usually on a shared network system and is used to hold DICOM master files. F:\DICOM is typically the DICOM dictionary directory. You may select any other device letter or Fully Qualified Domain Name (FDQN) with shared network drive (i.e.: \\VHAxxxclu10a...\GW_dic_files), however.

> Enter the device letter for

> the DICOM dictionary directory: c:// \<Type Response\> \<Enter\>

### Communication Channels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Communication channels are used to broadcast VistA event data. A separate channel is needed for each different destination. For instance, event data may be sent to both a commercial PACS and to one or more Modality Worklist service class providers (for example a Mitra Broker or a DeJarnette MediShare). Each destination must have its own event channel *n* and a dedicated c:\dicom\data*n* subdirectory. This is not used much anymore as the Mitra boxes have been phased out.

The number of communication channels must be between 1 and 9.

> Please enter the number of communication channels 2// \<Type Response\> \<Enter\>

### DICOM Image Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this system is to be configured as a VistA DICOM Image Gateway, the answer to this question must be Yes. If this system is to be configured otherwise, answer No.

> **NOTE:** A VistA DICOM Gateway may be configured as a Text Gateway, an Image Gateway, a Routing Processor, or any combination thereof.

> Will this system be a DICOM Image Gateway? No// \<Type Response\> \<Enter\>

### DICOM Text Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this system is to be configured as a VistA DICOM Text Gateway, to support the Modality Worklist and/or send event messages to a commercial Picture Archiving and Communication System (PACS), the answer to this question must be Yes. If this system is to be configured otherwise, answer No.

> **NOTE:** A VistA DICOM Gateway may be configured as a Text Gateway, an Image Gateway, a Routing Processor, or any combination thereof.

> Will this system be a DICOM Text Gateway? YES// \<Type Response\> \<Enter\>

### DICOM Routing Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this DICOM Gateway is to be configured as a VistA DICOM Routing Processor, the answer to this question must be Yes. If this system is to be configured otherwise, answer No.

> **NOTE:** A VistA DICOM Gateway may be configured as a Text Gateway, an Image Gateway, a Routing Processor, or any combination thereof.

> Will this system be a DICOM Routing Processor? YES// \<Type Response\> \<Enter\>

### Auto-Routing Active

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If one of the DICOM Gateways at this site is being used as a Routing Processor, the answer to this question must be Yes. If no automated routing is to occur at this site, the answer to this question must be No.

> Will this computer be part of a system where 'autorouting' is active? NO// \<Type Response\> \<Enter\>Note: When the answer to this question is set to Yes, queue-entries will be created for automated routing. If no Routing Processor is active at the site, these queue entries will accumulate and never be processed or purged.

For detailed information about setting up a DICOM Gateway to perform automated routing, see the [*VistA Imaging DICOM Routing Setup and User Guide*](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_routing_user_guide.pdf).

### Radiology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this DICOM Gateway is to be configured as a computer that processes Radiology exams, the answer to this question must be Yes. If this system is to be configured otherwise, answer No.

> Will this Text Gateway be used for Radiology? YES// \<Type Response\> \<Enter\>Note: A VistA DICOM Gateway may be configured as one that processes Radiology exams, one that handles Consults, or one that supports both.

### Consults and Anatomic Pathology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this DICOM Gateway is to be configured as a computer that processes Consults and Anatomic Pathology, the answer to this question must be Yes. If this system is to be configured otherwise, answer No.

> Will this Text Gateway be used for Consults and Anatomic Pathology? YES// \<Type Response\> \<Enter\>Note: A VistA DICOM Gateway may be configured as one that processes Radiology exams, one that handles Consults, or one that supports both.

### Send Text to commercial PACS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this VistA DICOM Text Gateway is to be configured to send messages to either a commercial PACS or a Modality Worklist provider (for example, a Mitra Broker or a DeJarnette MediShare), the following question should be answered with Yes. Otherwise, answer No.

> Send text to a commercial PACS, Mitra Broker, et cetera? n// \<Type Response\> \<Enter\>

### Receive EXAM COMPLETE Message from commercial PACS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EXAM COMPLETE message is sent by some commercial PACS to signal that all the images for a study have been acquired and are ready to be sent to VistA. The EXAM COMPLETE message then serves as a trigger for VistA to pull the images from the commercial PACS. Other commercial PACS do not use the EXAM COMPLETE message, but autoroute their images to VistA.

If a commercial PACS is going to transmit EXAM COMPLETE messages to VistA that indicate all the images in a study are ready to be sent, answer Yes to this question. Otherwise, answer “No.”

> Is a PACS going to send Exam Complete messages to VistA? NO// \<Type Response\> \<Enter\>

### Kind of PACS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the previous question is answered with “Yes,” an additional question will be asked:

> Select the kind of commercial PACS at this site

> -----------------------------------------------

> 1 - GE Medical Systems PACS with Mitra PACS Broker

> 2 - GE Medical Systems PACS with ACR-NEMA Text Gateway

> 3 - eMed Technology Corporation PACS

> 4 - Other commercial PACS

> What kind of a PACS? \<Type Response\> \<Enter\>

This question will only be asked on a system that is slated to either be sending text messages to a PACS, or to be receiving Exam Complete messages from a PACS. Enter the sequence number for the kind of PACS that is present at the site.

### C-Move destination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This question will only be asked on a system that is slated to be receiving Exam Complete messages from a PACS.

- Some PACSs find the VistA system using its Application Entity Title, so that they can move images from PACS to VistA.
- An AE-title can have up to 16 characters.
- While the DICOM standard allows spaces in AE-titles, these names are often also used as "hostnames" in TCP/IP addresses. Hence, it is strongly recommended to refrain from using names with spaces in them.

Enter the PACS-to-VistA C-Move destination AE Title: VISTA_STORAGE// \<Type Response\> \<Enter\>

### Modality Worklist Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this Text Gateway is to be configured to provide the “Modality Worklist” capability, answer Yes to this question. Otherwise, answer No.

> Will this system be a Modality Worklist Provider? y// \<Enter\> yes

### Send CPT Modifiers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifier codes are included when CPT codes are transmitted. These modifier codes\` may be sent to PACSs and modalities via DICOM as a two-character suffix to a procedure code (*nnnn-xx*). The usual configuration is to include the modifier suffix.

If the modifier suffices are to be included in messages, answer Yes to this question. If these suffixes are to be omitted, answer No.

If the site is going to use VistARad, enter Yes. If it is going to use a commercial PACS, check with the vendor to see if it can support CPT-Modifiers.

> Send CPT Modifiers? Yes // \<Type Response\> \<Enter\>

### Dashes in SSN sent to PACS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This question will be asked only on a system that is slated to send text messages to a PACS.

The DICOM Text Gateway can be configured to include or not include dashes in Social Security Numbers sent to a PACS. If the PACS can handle dashes in Social Security Numbers, enter Yes. If it cannot handle them, enter No.

Include DASHES in Social Security Numbers sent to PACS? YES// \<Type Response\> \<Enter\>Note: Dashes can also be suppressed in Modality Worklist. See Section [B.4.6 WORKLIST.DIC](#b.4.6-worklist.dic).

### TCP/IP Address for VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to connect to the VistA system using the MUMPS-to-MUMPS Kernel Broker, the DICOM Gateway must know the TCP/IP address of the VistA system. Enter the site-specific address.

> Enter the network address for the main VistA HIS: ecp.\<VistaSiteName\>.med.va.gov// \<Type Response\> \<Enter\>

The address may be entered as the numeric address (in those cases that the connection must be with a specific processor) or to the “human-readable” name that is set up in the domain name server(DNS).

> **NOTE:** The TCP/IP Address was entered when initially starting the LDGW and should not need to be updated again.

### TCP/IP Port for MUMPS-to-MUMPS Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To connect to the VistA system using the MUMPS-to-MUMPS Kernel Broker, the DICOM Gateway must know the TCP/IP port number on which the Broker is listening on the VistA system. Enter the site-specific port-number.

> Enter the network port number for the main VistA HIS: 148##// \<Type Response\> \<Enter\>

> **NOTE:** The TCP/IP Port was entered when initially starting the LDGW and should not need to be updated again.

### Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When significant operational issues arise, the DICOM Gateway will send e-mail messages to a site-specific mail-group. Enter the e-mail address for the site-specific mail-group.

Note 1: A DICOM Gateway sends e-mail using the standard SMTP protocol, *not* through MailMan. If a mail-group within MailMan needs to receive these e-mail messages, the name of this mail-group cannot include any space characters.

Note 2: A site may or may not decide to include addresses in this mail-group that cause a pager/cell phone to be activated.

> Send emergency e-mail notices to: DICOM@site// \<Type Response\> \<Enter\>

### Display Patient Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A DICOM Image Gateway presents an activity log while it is processing images. This activity log includes information that contains patient identifiers. When this display is visible from a public area, it is necessary to suppress the privacy-sensitive details.

When these details are to be suppressed (i.e., displayed as a series of asterisks), the answer to this question must be No. If these details are allowed to be visible, the answer to this question can be Yes.

> Display Patient Name/ID in Image Processing? NO// \<Type Response\> \<Enter\>

### Access Code for Background Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an external entity sends a Modality Worklist request to a DICOM Gateway, the DICOM Gateway is usually able to respond to the request using information that is stored on the Gateway itself. In some cases, the DICOM Gateway will need to query the VistA system for details to report back to the requester. When the DICOM Gateway makes such a request to the VistA system, it will use the access code that is specified as the answer to this question.

> **NOTE:** The response to this question is treated as a password; i.e., it is not displayed on the monitor of the end-user. Also, you will be prompted to enter access code again for verification.

> Access Code for Background Tasks // \<Type Response\> \<Enter\>

### Verify Code for Background Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an external entity sends a Modality Worklist request to a DICOM Gateway, the DICOM Gateway is usually able to respond to the request using information that is stored on the Gateway itself. In some cases, the DICOM Gateway will need to query the VistA system for details to report back to the requester. When the DICOM Gateway makes such a request to the VistA system, it will use the verify code that is specified as the answer to this question.

> **NOTE:** The response to this question is treated as a password (i.e., it is not displayed on the monitor of the end-user). Also, you will be prompted to enter verify code again for verification.

> Verify Code for Background Tasks // \<Type Response\> \<Enter\>

### Modality Worklist Port Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Normally, modality worklist requests are processed through TCP/IP port number 60010. Some sites have equipment that uses a different port number, and which cannot be configured to use any other port number. In order to support such equipment, it is possible to define additional port numbers for modality worklist processors.

> Currently, there is a Modality WorkList processor for

> the following port:

> 60010

> Change? \[A/D/N\] N// ? \<Enter\>

> Enter one of the following:

> No if no (additional) change is to be made

> Add \<number\> to add a listener for a port

> Delete \<number\> to remove a listener for a port

> Note that valid port numbers are integers between 1 and 65535.

> Note that the listener for port 60010 may not be removed.

> Currently, there is a Modality WorkList processor for

> the following port:

> 60010

> Change? \[A/D/N\] N// a 104 \<Enter\>

> Currently, there are Modality WorkList processors for

> the following ports:

> 104

> 60010

> Change? \[A/D/N\] N// d 104 \<Enter\>

> Currently, there is a Modality WorkList processor for

> the following port:

> 60010

> Change? \[A/D/N\] N//

### E-Mail Post Office

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Department of Veterans Affairs has three virus-checking post offices set up for nationwide e-mail. The post office that should be selected for this setting should be the one to which the site has the best network-connection. There are six possible responses for this question:

> 0: the local VistA system at R03CLEAPP10.r03.med.va.gov

> 1: smtp.va.gov - this is the default post office for the VA

> 2: smtpre.ihs.gov - this is the default for the Indian Health Service

> 3: forum.va.gov - this is the VA Forum post office(or enter the TCP/IP address of the system to be used).

> Which post office will this computer use? smtp.va.gov// \<Type Response\> \<Enter\>Note: VA policy on the usage of e-mail post offices has changed several times while this documentation was being prepared. At the time this documentation is being written, the only value that is allowed to be entered for this parameter is “smtp.va.gov”.

Consult with your ISO for the VA’s current policy on this issue.

### E-Mail Post Office Port Number 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Define the port number for the E-Mail Post Office when prompted:

> Which port number will this computer use for e-mail? 25// \<Type Response\> \<Enter\>

Email is transmitted using SMTP protocol. Normally, this protocol uses port number 25. In some cases, a different port number may have been set up at the site.

> **NOTE:** The port number should be between 1 and 65,535:  
1 \<= port number \<= 65,535.

For more information about E-Mail Post Office, see the section [5.1.27](#e-mail-post-office) .

### Specifying the Agency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are setting up a new DICOM Gateway, when you run option 4-2-2, you are prompted to specify whether the DICOM Gateway is installed at a Department of Veterans Affairs (VA) site or an Indian Health Services (IHS) site.

> Is this gateway installed in VA (V)or IHS (I)? V// \<Type Response\> \<Enter\>

If you get this prompt, do one of the following:

- For VA sites, press Enter to accept the default, V.
- For IHS sites, type I and press Enter.

### DICOM Message Logs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Define the number of DICOM Message logs you want to retain when prompted:

> How many DICOM Message Logs do you want to keep? 20// \<Type Response\> \<Enter\>

### Image with Long Values 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Define if Imaging Processing should reject DICOM objects that have excessively long data elements. Enter “Yes” to reject DICOM objects and “No” to accept.

> Should Image Processing reject objects with excessively long values? NO// \<Type Response\> \<Enter\>

## Loading the DICOM Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DICOM Dictionaries are constructed by populating a number of FileMan globals with data from the master files. [Appendix B](#_Appendix_B_Master) contains a detailed description of each master file. The format and contents of the resulting subtrees in global variable ^MAGDICOM(2006.5xx) are described in the (online) FileMan Data Dictionaries.

Sites should make changes to the master files only for the site-specific DICOM Dictionaries. The information in the global variable themselves should not be manually modified, as it will be overwritten the next time the master file is loaded.

In order to start loading the dictionaries, select menu option 4-2-9:

> 4 System Maintenance

> → 2 Gateway Configuration and DICOM Master Files

> → → 9 Reinitialize All the DICOM Master Files

> Ready to build all of the DICOM Master Files? y// \<Enter\> yes

> **NOTE:** If the DICOM dictionaries are stored in a network path, that will be shown: *\\server\share\DICOM\Dict\\*DICOMDICNAME*.DIC*

> Example:

> From: f:\DICOM\Dict\ELEMENT.DIC

> To : \\server\share\DICOM\Dict\ELEMENT.DIC

### DICOM Data Element Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file ELEMENT.DIC are loaded into global variable ^MAGDICOM(2006.51,…).

The contents of the master file ELEMENT.DIC may not be modified by the site.

Building the DICOM Element Dictionary -- ^MAGDICOM(2006.51)

Ready to read dictionary file "f:\DICOM\Dict\ELEMENT.DIC"? y// y \<Enter\>

### DICOM Message Template Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file TEMPLATE.DIC are loaded into global variable ^MAGDICOM(2006.52,…).

The contents of the master file TEMPLATE.DIC may not be modified by the site.

Building the DICOM Message Template Dictionary -- ^MAGDICOM(2006.52)

Ready to read dictionary file "f:\DICOM\Dict\TEMPLATE.DIC"? y// \<Enter\> yes

\*\*\* PASS 1 STARTED \*\*\*

\*\*\* PASS 2 STARTED \*\*\*

\- DONE -

### DICOM Unique Identifier Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file UID.DIC are into global variable ^MAGDICOM(2006.53,…).

The contents of the master file UID.DIC may not be modified by the site.

Building the DICOM UID Dictionary -- ^MAGDICOM(2006.53)

Ready to read dictionary file "f:\DICOM\Dict\UID.DIC"? y// y \<Enter\>

### Extended SOP Negotiation Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the Extended SOP (Service Object Pair) Negotiation Table is loaded into global variable ^MAGDICOM(2006.531,…).

Updating the extended SOP negotiation table... done!

### DICOM PDU Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the PDU (Protocol Data Unit) table is loaded into global variable ^MAGDICOM(2006.54,…).

Updating the PDU TYPE table... done!

### DICOM HL7 Segment and Field Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file HL7.DIC are loaded into global variable ^MAGDICOM(2006.57,…).

The site may not modify the contents of the master file HL7.DIC.

Building the DICOM HL7 dictionary in ^MAGDICOM(2006.57)

Ready to read dictionary file "f:\DICOM\Dict\HL7.DIC"? y// y \<Enter\>

done!

### Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file INSTRUMENT.DIC are loaded into global variable ^MAGDICOM(2006.581,…).

The contents of the master file INSTRUMENT.DIC must be customized for the site.

Building the Instrument Dictionary -- ^MAGDICOM(2006.581)

Ready to read dictionary file "f:\DICOM\Dict\INSTRUMENT.DIC"? y// y \<Enter\>

### Modalities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file MODALITY.DIC are loaded into global variable ^MAGDICOM(2006.582,…).

The contents of the master file MODALITY.DIC must be customized for the site.

Building the Modality Type Dictionary -- ^MAGDICOM(2006.582)

Ready to read dictionary file "f:\DICOM\Dict\MODALITY.DIC"? y// y \<Enter\>

### CT Conversion History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file CT_PARAM.DIC are loaded into global variable ^MAGDICOM(2006.5821,…).

The contents of the master file CT_PARAM.DIC may not be customized for the site.

Building the CT Conversion History Dictionary -- ^MAGDICOM(2006.5821)

Ready to read dictionary file "f:\DICOM\Dict\CT_PARAM.DIC"? y// y \<Enter\>

### Modality Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file WORKLIST.DIC are loaded into global variable

^MAGDICOM(2006.583,…).

The contents of the master file WORKLIST.DIC must be customized for the site.

Building the Modality Worklist Dictionary -- ^MAGDICOM(2006.583)

Ready to read dictionary file "f:\DICOM\Dict\WORKLIST.DIC"? y// y \<Enter\>

### Port Numbers for Text Gateway sending messages to PACS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file PORTLIST.DIC are loaded into global variable ^MAGDICOM(2006.584,…).

The contents of the master file PORTLIST.DIC, if used, must be customized for your site.

Building the TCP/IP Provider Port Dictionary -- ^MAGDICOM(2006.584)

Ready to read dictionary file "f:\DICOM\Dict\PORTLIST.DIC"? y// y \<Enter\>

### User Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file SCU_LIST.DIC are loaded into global variable ^MAGDICOM(2006.585,…).

The contents of the master file SCU_LIST.DIC must be customized for the site.

Building the User Application Dictionary -- ^MAGDICOM(2006.585)

Ready to read dictionary file "f:\DICOM\Dict\SCU_LIST.DIC"? y// y \<Enter\>

### Provider Application Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file SCP_LIST.DIC are loaded into global variable ^MAGDICOM(2006.586,…).

The contents of the master file SCP_LIST.DIC may not be modified by the site.

Building the Provider Application Dictionary -- ^MAGDICOM(2006.586)

Ready to read dictionary file "f:\DICOM\Dict\SCP_LIST.DIC"? y// y \<Enter\>

### Application Entity Title Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During this step, the contents of the file AE_TITLE.DIC are loaded into global variable ^MAGDICOM(2006.588,…).

The contents of the master file AE_TITLE.DIC may be customized for the site.

Building the Application Entity Title Dictionary -- ^MAGDICOM(2006.588)

Ready to read dictionary file "f:\DICOM\DICT\AE_TITLE.dic"? y// yes\<Enter\>

### Data Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The master file named DATAMISC.DIC references several other dictionary files that contain lists of additional data elements to be displayed on a diagnostic workstation. These “data transfer” dictionaries are loaded during this step.

Ready to read dictionary file "f:\DICOM\DICT\DATAMISC.DIC"? y//

### Terminal Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The master file named TERMINAL_TITLE.DIC is loaded (see [Appendix A](#appendix-a-creating-automatic-startup-of-iris-terminal-sessions)).

Ready to read dictionary file "f:\DICOM\DICT\TERMINAL_TITLE.dic"? y// yes \<Enter\>

-- DICOM Master File Build completed successfully –

## Verify the DICOM Gateway Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  On the DICOM Gateway, run option 4-1-4 to verify the patch version.

4 - System Maintenance

à 1 - System Operation

àà 4 - Display the Version of the Software

2.  On the DICOM Gateway, run option 4-2-1 to verify the LDGW configuration.

4 - System Maintenance

à 2 - Gateway Configuration and DICOM Master Files

àà 1 - Display Gateway Configuration Parameters

3.  Run option 4-2-11 to confirm the Access and Verify codes.

> 4 – System Maintenance

> à 2 – Gateway Configuration and Master Files

> àà 11 – Validate Access/Verify Codes for Modality Worklist

4.  Run option 4-2-12 to take DICOM Gateway parameters and store them on VistA.

> 4 System Maintenance

> → 2 Gateway Configuration and Master Files

> → → 12 Display Versions and/or Time Stamps of Components

## Logging into the DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With patch MAG\*3.0\*319 new Auto-Login/Start up of LDGW Terminal Sessions, the various DICOM Gateway programs that are part of the VistA Imaging DICOM Gateway, e.g.: 1-1,2-3,2-8-2…etc., can be started from one short_cut on Windows desktop:

Double click the shortcut icon “DICOM Gateway Startup” on the desktop (or C:\Users\Public\Desktop), then click/select on the most left window with the title “1-1 Start Processing Text…” from the listing group on Windows task bar to login with the LDGW VistA access/verify code.

![](vista-imaging-dicom-gateway-installation-guide/065.png)

![](vista-imaging-dicom-gateway-installation-guide/066.png)

![](vista-imaging-dicom-gateway-installation-guide/067.png)

The default “DICOM Gateway Startup” opens all windows. You can specify for each gateway the terminal windows that open. You must modify the DICOM Gateway Startup.bat. See [Appendix A](#appendix-a-creating-automatic-startup-of-iris-terminal-sessions).

## Recommended Icons – DGW Terminal sessions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation process creates a shortcut icon of 9 IRIS terminal sessions for the benefit of the end-user. A typical site will use only a subset of these 9. It is recommended that a site customize the windows that are described below. Usage of the various session will depend on the tasks that are run from the system. The table below shows which gateway tasks relate to which type of gateway. See [Appendix A](#a.1-introduction).

## Gateway Tasks Related to Gateway Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Menu Option                                      | Text G/W | Image G/W | Routing G/W | Study Tracker G/W |
|--------------------------------------------------|----------|-----------|-------------|-------------------|
| 1-1\|Start Processing Text Messages              | X        |           |             |                   |
| 1-4\|Display Modality Worklist Statistics        | X        |           |             |                   |
| 2-3\|Process DICOM Images                        |          | X         |             |                   |
| 2-5\|Display Real-Time Storage Server Statistics |          | X         |             |                   |
| 2-8-2\|Export DICOM Objects                      |          |           | X           |                   |
| 2-8-12\|Real-Time Batch Export Queue Monitor     |          |           | X           |                   |
| 2-14-1\|VistA Client Query/Retrieve Surrogate    |          |           |             | X                 |
| 2-14-2\|Q/R Surrogate to Retrieve Images         |          |           |             | X                 |
| 3-1\|Start Routing Transmission Processor        |          |           | X           |                   |
| 3-3\|Start Routing Evaluation Processor          |          |           | X           |                   |

# Appendix A Creating Automatic Startup of IRIS Terminal Sessions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default IRIS installation will be enable the Automatic Startup of IRIS Terminal Session w/ one login (access/verify code)

## A.1 Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the DICOM Gateways were first released (1996), Telnet terminal sessions were used with Micronetics Standard MUMPS. The use of Telnet terminal sessions was continued with the InterSystems Caché implementations. Telnet was a non-secure protocol, however.

Five years ago, when MAG\*3.0\*166 was released and SSH was installed on the Cache DICOM Gateways to replace Telnet, Micro Focus Reflection Workspace was added to provide a secure connection. Reflection server and client was installed on the DICOM Gateways. Reflection clients were used to access Reflection servers on the same DICOM Gateway. It was soon realized that Reflection provided no value to the DICOM Gateway because Caché and IRIS Terminal communicated directly with the MUMPS servers on the local DICOM Gateway bypassing Telnet. With the upgrade to IRIS, we will discontinue the use of Reflection and SSH and instead use IRIS Terminal with an automatic start up process. (The Telnet service will continue to be disabled.)

The automatic startup procedure for IRIS Terminal sessions has the following capabilities:

- Display name of the application in the Title Bar of the IRIS Terminal window
- Automatically navigate the menu tree and start the appropriate application
- Require a single login for all of IRIS Terminal windows started in a batch
- Position the IRIS Terminal window on the screen
- Adjust the size of the IRIS Terminal window (rows and columns)

## A.2 Customize DICOM Gateway Startup.bat

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit the DICOM Gateway Startup.bat Shortcut on the desktop by right clicking the shortcut and selecting Edit.

> ![](vista-imaging-dicom-gateway-installation-guide/068.png)

The DICOM Gateway Startup.bat can be modified to specify which windows automatically display, the position of each window on the screen and size of the window. These are controlled by the Call LDGW_Startup lines in the file. To remove a window comment it out with “rem” in the front. Lines can also be added to start additional windows.

Example

rem LDGD_StartUp Option X-Pos Y-Pos Rows Columns

call LDGW_StartUp 1-1 0 0 20 70

rem call LDGW_StartUp 2-3 625 0

rem call LDGW_StartUp 3-1 1250 0

call LDGW_StartUp 2-8-2 0 400

call LDGW_StartUp 2-8-12 625 400 25 90

call LDGW_StartUp 3-3 1250 400

call LDGW_StartUp 2-14-1 0 800

call LDGW_StartUp 2-14-2 625 800

call LDGW_StartUp - 1250 800

The current window options that can be included in the DICOM Gateway Startup.bat are listed below. A window can be added more than once.

> 1-1\|Start Processing Text Messages

> 1-4\|Display Modality Worklist Statistics

> 2-3\|Process DICOM Images

> 2-5\|Display Real-Time Storage Server Statistics

> 2-8-2\|Export DICOM Objects

> 2-8-12\|Real-Time Batch Export Queue Monitor

> 2-14-1\|VistA Client Query/Retrieve Surrogate

> 2-14-2\|Q/R Surrogate to Retrieve Images

> 3-1\|Start Routing Transmission Processor

> 3-3\|Start Routing Evaluation Processor

> 4-1-3\|Issue a DICOM Echo Request

> -\|VistA DICOM Gateway Menu

The screens shot below shows how the menu trees in all nine windows were automatically navigated to the appropriate application. Login was required for just the first most upper left (reduced 20x70 size) window and then propagated to the other eight windows

![](vista-imaging-dicom-gateway-installation-guide/069.png)

## A.3 TERMINAL_TITLE.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new TERMINAL_TITLE.DIC contains the list of windows that are available to be customized in DICOM Gateway Startup.bat. This information can be modified to allow additional windows to be available.

The format of each entry is {option number string} \| {option title}

- {option number string} are the are the option's menu numbers separated by dashes
- {option title} is displayed in the Title Bar of the DICOM Gateway terminal window

If an entry does not exist for an option, the default InterSystems title will be used.

1-1\|Start Processing Text Messages

1-4\|Display Modality Worklist Statistics

2-3\|Process DICOM Images

2-5\|Display Real-Time Storage Server Statistics

2-8-2\|Export DICOM Objects

2-8-12\|Real-Time Batch Export Queue Monitor

2-14-1\|VistA Client Query/Retrieve Surrogate

2-14-2\|Q/R Surrogate to Retrieve Images

3-1\|Start Routing Transmission Processor

3-3\|Start Routing Evaluation Processor

-\|VistA DICOM Gateway Menu

## A.4 Update TERMINAL_TITLE.DIC Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the TERMINAL_TITLE.DIC is modified the menu option 4-2-13 Update TERMINAL_TITLE.DIC needs to be run.

Answer Yes to the “Ready to read dictionary file” question.

![](vista-imaging-dicom-gateway-installation-guide/070.png)

The TERMINAL_TITLE.DIC will then be updated

![](vista-imaging-dicom-gateway-installation-guide/071.png)

# Appendix B Master Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## B.1 Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging DICOM Gateway uses a number of tables to drive certain parameterized procedures within the VistA Imaging DICOM Gateway software. These tables are populated from the data in a set of ASCII text files. In the context of the VistA Imaging DICOM Gateway, these text files are called “master files.”

Common usage within the Department of Veterans Affairs is to use the term “file” for a subtree of a global variable in MUMPS. The master files that are described in this chapter, however, are files in the more traditional sense: entities that live in directories within an operating system. To minimize confusion about the meaning of the term “file,” this chapter will reserve the term “file” for entities outside of MUMPS, and the term “table” for databases within a MUMPS environment.

## B.2 Master Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging DICOM Gateway uses a number of FileMan tables to drive the VistA Imaging DICOM Gateway software. These FileMan tables are populated from ASCII text data stored in master files located in a directory named F:\DICOM\Dict, (in this document, the drive-letter F: is used; see sections [3.3](#map-a-network-drive-for-dictionary-files) and [3.4](#installing-the-software)). The actual name for this directory is stored by the VistA Imaging DICOM Gateway software as data in ^MAGDICOM(2006.563,1,“DICT PATH”).

### B.2.1 Master File Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu of the VistA Imaging DICOM Gateway has number of options that each import one, some or all of the master files. These menu options are:

4 System Maintenance

à 2 Gateway Configuration and DICOM Master Files

à à 1 Display Gateway Configuration Parameters

à à 2 Update Gateway Configuration

à à 3 Update AETITLE.DIC

à à 4 Update INSTRUMENT.DIC

à à 5 Update MODALITY.DIC

à à 6 Update PORTLIST.DIC

à à 7 Update SCU_LIST.DIC

à à 8 Update WORKLIST.DIC

à à 9 Reinitialize All the DICOM Master Files

à à 10 Create Shortcuts for Instruments

à à 11 Validate Access/Verify Codes for Modality Worklist

à à 12 Display Versions and/or Time Stamps of Components

13 Update TERMINAL_TITLE.DIC

There are two groups of master files: static ones that are the same for all sites, and site-configurable ones that must be edited at each site.

### B.2.2 General Formatting Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In all master files, lines that start with a pound sign (“#”) are comment lines.
- Text lines that do not start with a number sign contain dictionary data.
- While updating master files, blank lines and comment lines will be ignored.

> **NOTE:** The final line in any master file must be followed by an “end-of-line” control sequence (carriage return and line feed). If the final “end-of-line” control sequence is missing, the line will be invisible to the software that updates the master files. To prevent this problem, all distributed versions of the master files end with the following comment line:

\# End of File\<CR\>\<LF\>

## B.3 Static Master Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the format and contents of the static master files, which are part of the release distribution of the VistA Imaging.

Static master files in this category contain data that is the same for all sites. These files may not be modified by the sites (reference VA directive and FDA warning).

The following files are included in the release:

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>FileMan Table</strong></th>
<th><strong>MUMPS Routine</strong></th>
<th><strong>Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CT_PARAM.DIC</td>
<td>2006.5821</td>
<td>^MAGDMFB7</td>
<td>Contains list of image processing rules for historical CT images.</td>
</tr>
<tr class="even">
<td>DATAGECT.DIC</td>
<td><p>2006.511</p>
<p>sub 2006.5112</p></td>
<td>^MAGDIR4</td>
<td>Contains list of data-items to be shown on diagnostic workstation displays.</td>
</tr>
<tr class="odd">
<td>DATA_CR.DIC</td>
<td><p>2006.511</p>
<p>sub 2006.5112</p></td>
<td>^MAGDIR4</td>
<td>Contains list of data-items to be shown on diagnostic workstation displays.</td>
</tr>
<tr class="even">
<td>DATAMISC.DIC</td>
<td><p>2006.511</p>
<p>sub 2006.5112</p></td>
<td>^MAGDIR4</td>
<td>Contains list of data-items to be shown on diagnostic workstation displays.</td>
</tr>
<tr class="odd">
<td>DATA_MRI.DIC</td>
<td><p>2006.511</p>
<p>sub 2006.5112</p></td>
<td>^MAGDIR4</td>
<td>Contains list of data-items to be shown on diagnostic workstation displays.</td>
</tr>
<tr class="even">
<td>ELEMENT.DIC</td>
<td>2006.51</td>
<td>^MAGDMFB2</td>
<td>Contains DICOM Standard data elements.</td>
</tr>
<tr class="odd">
<td>HL7.DIC</td>
<td>2006.57</td>
<td>^MAGDMFB7</td>
<td>Contains list of HL7 message templates.</td>
</tr>
<tr class="even">
<td>SCP_LIST.DIC</td>
<td>2006.586</td>
<td>^MAGDMFB9</td>
<td>Contains lists of parameters for Provider Applications</td>
</tr>
<tr class="odd">
<td>TEMPLATE.DIC</td>
<td>2006.52</td>
<td><p>^MAGDMFB3</p>
<p>^MAGDMFB4</p></td>
<td>Contains templates for DICOM messages.</td>
</tr>
<tr class="even">
<td>UID.DIC</td>
<td>2006.53</td>
<td>^MAGDMFB5</td>
<td>Contains list of unique DICOM identifiers.</td>
</tr>
</tbody>
</table>

### B.3.1 ELEMENT.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file ELEMENT.DIC contains the DICOM data dictionary. As part of the installation process, this file is read by routine ^MAGDMB2 and is used to construct the FileMan table DICOM Data Element Dictionary (File 2006.51, stored in ^MAGDICOM(2006.51,…)).

In a DICOM data stream, every data element is identified by a four-byte binary “tag” consisting of a two-byte group field and a two-byte element field. The tag value is usually represented by two groups of four hexadecimal digits, separated by a comma (group, element, e.g., 0010,21B0 for Additional Patient History). Odd-numbered groups denote private elements and are accompanied by an explicit owner identification code.

The file ELEMENT.DIC contains three kinds of records:

The first is the “group” record, which for odd-numbered groups defines the owner identification code for private elements. Following the group record are one or more “element” records that define each element and its set of attributes. Some of the element records are followed by optional “value” records, which define the legal set of enumerated values or defined terms for the element.

The values of an element are “enumerated values” when the value of that element may be one of an explicitly specified set of standard values, which shall not be extended by implementers.

The values of an element are “defined terms” when the value of that element may be one of an explicitly specified set of standard values, which may be extended by implementers.

The formats for the different record types are as follows:

|                                         |                                                                                                                                       |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| • Group Record:                         | \<group\> \| \<group owner\> \| \<group title\>                                                                                       |
| • Element Record:                       | \<tag\> \| \<element name\> \| \<value representation\> \| \<multiplicity\> \| \<value flag\> \| \<retired flag\>                     |
| • Value Record:                         | \<tag\> \| \<permitted value\>                                                                                                        |
| The different fields are defined below: |                                                                                                                                       |
| \<group\>                               | The group identifier, expressed in four hexadecimal digits.                                                                           |
| \<group owner\>                         | Blank for groups that are defined in the DICOM standard, and otherwise contains the name of or a mnemonic for the owner of the group. |
| \<group title\>                         | A name for the group for documentation purposes.                                                                                      |
| \<tag\>                                 | Identifies the group and element(s), the value may contain hexadecimal digits and several wildcard characters.                        |
| \<element name\>                        | The name of the element (case-sensitive).                                                                                             |
| \<value representation\>                | The 2-letter data type mnemonic.                                                                                                      |
| \<multiplicity\>                        | Identifies the (maximum) number of values that may be passed at a time.                                                               |
| \<retired flag\>                        | An identifier that denotes that the element is no longer current.                                                                     |
| \<permitted value\>                     | The enumerated value or defined term, along with its meaning.                                                                         |

Example:

0010\|\|Patient Information

0010,0000\|Group Length\|UL\|1\|\|

0010,0010\|Patient's Name\|PN\|1\|\|

0010,0020\|Patient ID\|LO\|1\|\|

0010,0021\|Issuer of Patient ID\|LO\|1\|\|

0010,0030\|Patient's Birth Date\|DA\|1\|\|

0010,0032\|Patient's Birth Time\|TM\|1\|\|

0010,0040\|Patient's Sex\|CS\|1\|E\|

0010,0040\|M=male

0010,0040\|F=female

0010,0040\|O=other

0039\|VA DHCP\|Admission, Discharge, and Transfer Information Shadow

0039,0000\|Group Length\|UL\|1\|\|

0039,0010:1:00FF\|Owner of Group\|LO\|1\|\|

0039,xx10\|Current Patient Location Sequence\|SQ\|1\|\|

0039,xx20\|Patient's Institutional Residence Sequence\|SQ\|1\|\|

When a \<tag\> contains an “xx,” this means that it is a private element, and the same definition applies to all tags that have any hexadecimal digit in the position of that “xx.”

When a tag contains a value of the format \<start\>:\<step\>:\<end\>, this means that the same definition applies to all values covered by that range definition.

The information in ELEMENT.DIC is extracted directly from the DICOM standard (element definitions are specified in Part 6: Data Dictionary (PS 3.6); lists of permitted values are specified in Part 3: Information Object Definitions (PS 3.3)). The full DICOM standard can be found at <https://www.dicomstandard.org>/

The data from this file is stored in MUMPS in the following structure:

^MAGDICOM(2006.51,d0,0) = group , element \[ , owner \] ^ name ^ VR ^ mult ^ flag

^MAGDICOM(2006.51,d0,1,d1,0) = value ^ meaning

^MAGDICOM(2006.51,“B”, group element \[owner\], d0) = “”

^MAGDICOM(2006.51,d0,1,“B”,value,d1) = “”

### B.3.2 HL7.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file HL7.DIC contains the definitions of the recognized HL7 messages. As part of the installation process, this file is read by routine ^MAGDMB7 and is used to construct the FileMan table DICOM HL7 SEGMENT (File 2006.57, stored in ^MAGDICOM(HL7,…)).

The routine ^MAGDHRP uses the values in this table to produce a formatted HL7 message listing.

Each record consists of two pieces. The first piece is either the HL7 segment identifier (if it is alphanumeric), or it contains the HL7 segment field number (if it is numeric). The second piece is text that defines either the name of the segment or the name of the field.

Example of an HL7 segment with its fields:

PID\|Patient Identification Segment

1\|Set ID - Patient ID

2\|Patient ID (External ID)

3\|Patient ID (Internal ID)

4\|Alternate Patient ID

5\|Patient Name

6\|Mother's Maiden Name

7\|Date of Birth

8\|Sex

9\|Patient Alias

10\|Race

11\|Patient Address

12\|Country Code

13\|Phone Number - Home

14\|Phone Number - Business

15\|Language - Patient

16\|Marital Status

17\|Religion

18\|Patient Account Number

19\|SSN Number - Patient

20\|Driver's Lic Num - Patient

21\|Mother's Identifier

22\|Ethnic Group

The data from this file is stored in MUMPS in the following structure:

^MAGDICOM(“HL7”,d0,0) = segment ^ name of segment

^MAGDICOM(“HL7”,d0,1,d1,0) = name of element

^MAGDICOM(“HL7”,“B”,segment,d0) = “”

### B.3.3 CT_PARAM.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file CT_PARAM.DIC contains the definitions of historical CT parameters used by VA sites that are supported by the VistA Imaging DICOM Gateway. The primary purpose of this file is for CT images processed before installation of Imaging Patch 30. (In images processed after the installation of Patch 30, image processing rules are saved into the image’s .txt file, and the CT_PARAM.DIC file is not used.)

There is one type of record in CT_PARAM.DIC.

|                                                        |                                                                                                 |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| • Application Record:                                  | \<Site Code\> \| \<Manufacturer\>\|\<Model\>\|\<Latest Date Saved\>\|\<Image Processing Rules\> |
| The different fields in this record are defined below: |                                                                                                 |
| \<Site Code\>                                          | Also known as the Institution Code.                                                             |
| \<Manufacturer\>                                       | The manufacturer of the equipment producing the images; element (0008,0070).                    |
| \<Model\>                                              | The manufacturer’s model name for the equipment; element (0008,1090).                           |
| \<Latest Date Saved\>                                  | The last date this specific image processing rule was set or changed in MODALITY.DIC.           |
| \<Image Processing Rules\>                             | Control the conversion of the image from DICOM to Targa file format.                            |

Example of entries in CT_PARAM.DIC:

442\|TOSHIBA\|AQUILION\|9-Jun-2006\|b12 a2048 f0 c4095

442\|TOSHIBA\|ASTEION\|25-Feb-2005\|b12

442\|PHILIPS\|BRILLIANCE16\|14-Jul-2006\|

442\|GE MEDICAL SYSTEMS\|HISPEED\|4-May-2004\|b12 a1000 f0 c4095

442\|GE MEDICAL SYSTEMS\|HISPEED CT/I\|9-Jun-2006\|b12 f0

442\|GE MEDICAL SYSTEMS\|LIGHTSPEED16\|9-Jun-2006\|b12 f0 c4095

442\|PHILIPS\|MX8000\|9-Jun-2006\|b12

442\|PHILIPS\|MX8000 IDT 16\|9-Jun-2006\|b12 f0 c4095

442\|PICKER INTERNATIONAL, INC.\|PQ5000\|9-Jun-2006\|b12 a1000 f0 c4095

### B.3.4 SCP_LIST.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file SCP_LIST.DIC contains the definitions of the applications that are supported by the VistA Imaging DICOM Gateway operating in the role of a Service Class Provider (SCP). As part of the installation process, this file is read by routine ^MAGDMB9 and is used to construct the FileMan table Provider Application List (File 2006.586, stored in ^MAGDICOM(2006.586,…)).

There are three kinds of records in the file SCP_LIST.DIC. The first is the “application” record, which identifies the name of the VistA service class provider. Following the application record are one or more “service” records defining the services that may be utilized. Following a “service” record, there is at least one “transfer syntax” record, defining how information may be exchanged.

|                                         |                                                                  |
|-----------------------------------------|------------------------------------------------------------------|
| • Application Record:                   | \<called AE title\> \| \<application name\>                      |
| • Service Record:                       | \| \<SOP Class\>                                                 |
| • Transfer Syntax Record:               | \| \| \<syntax\>                                                 |
| The different fields are defined below: |                                                                  |
| \<called AE title\>                     | The title of the called VistA provider (SCP) application entity. |
| \<application name\>                    | The name that VistA uses to refer to the DICOM application.      |
| \<SOP Class\>                           | The name of the DICOM service object pair (SOP).                 |
| \<syntax\>                              | is the name of a supported transfer syntax                       |

Example of entries in SCP_LIST.DIC:

\# VistA Service Class Providers

\# \<VistA Application Entity Title\> \| \<application name\>

\# \| \<supported SOP class\>

\#

VISTA_WORKLIST\|VistA Modality Worklist

\|Verification SOP Class

\|\|Implicit VR Little Endian

\|Modality Worklist Information Model – FIND

\|\|Implicit VR Little Endian

\#

VISTA_STORAGE\|VistA Storage

\|Verification SOP Class

\|\|Explicit VR Little Endian

\|\|Implicit VR Little Endian

\|Computed Radiography Image Storage

\|\|Explicit VR Little Endian

\|\|Implicit VR Little Endian

\|CT Image Storage

\|\|Explicit VR Little Endian

\|\|Implicit VR Little Endian

\|Ultrasound Multi-frame Image Storage (retired)

\|\|Explicit VR Little Endian

\|\|Implicit VR Little Endian

The data from this file is stored in MUMPS in the following structure:

^MAGDICOM(2006.586,d0,0) = AE Title ^ Application name

^MAGDICOM(2006.586,d0,1,d1,0) = SOP Class UID ^ SOP Class Name

^MAGDICOM(2006.586,d0,1,d1,1,d2,0)

= Transfer Syntax UID ^ Transfer Syntax Name

^MAGDICOM(2006.586,“B”,AE Title,d0) = “”

^MAGDICOM(2006.586,d0,1,“B”,SOP Class UID,d1) = “”

^MAGDICOM(2006.586,d0,1,d1,1,“B”,Transfer Syntax UID,d2) = “”

### B.3.5 TEMPLATE.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file TEMPLATE.DIC contains model definitions of the messages that are supported by the VistA Imaging DICOM Gateway. As part of the installation process, this file is read by routines ^MAGDMB3 and ^MAGDMFB4 and is used to construct the file F:\DICOM\\ Dict\Template.TMP and the FileMan table DICOM Message Template Dictionary (File 2006.52, stored in ^MAGDICOM(2006.52,…)).

DICOM data elements are the attributes of the Service Classes and the Information Object Definitions. The service classes and information object definitions are joined together to form the Service-Object Pair (SOP) classes. The SOP classes are the high-level communications message protocol units of DICOM.

The file TEMPLATE.DIC defines the way that the DICOM data elements are combined to make up the SOP Classes. The file TEMPLATE.DIC contains attributes of the service classes, the information object definition modules, and the SOP classes. Because the same set of attributes is often repeated in several different SOP classes, the gateway master file update software uses a macro facility so that the attributes can be defined once and used multiple times. The file TEMPLATE.DIC is expanded by the macro facility (routine ^MAGDMFM4) to create the file Template.TMP, which contains the model of each DICOM message. The routine ^MAGDMFB3 routine invokes ^MAGDMFM4 to expand the macros, and then reads the resulting file F:\DICOM\\ Dict\Template.TMP to populate the FileMan table in global variable ^MAGDICOM(2006.52).

The format for the macro definitions is as follows:

> {\$define \<name of macro\>}

> \<body of macro\>

> {\$end \<name of macro\>}

The macro facility performs simple text replacement. When a macro is invoked, the invocation is replaced by the macro text. The format for a macro invocation is {\<name of macro\>}. The macro invocation is replaced with \<body of macro\> in the expanded text. Macros may be nested.

The \<body of macro\> (i.e., the macro text) consists of a sequence of DICOM Element Records and (optional) Macro Invocation Records. The formats for these two types of records are as follows:

|                                         |                                                                                        |
|-----------------------------------------|----------------------------------------------------------------------------------------|
| • Element Record:                       | \<element name\> \| \<tag\> \| \<group owner\> \| \<SCP/SCU Type\> \|\<default value\> |
| • Macro Invocation:                     | {\<name of macro\>}                                                                    |
| The different fields are defined below: |                                                                                        |
| \<element name\>                        | The case-sensitive name of the element.                                                |
| \<tag\>                                 | The group and element numbers, in (gggg,eeee) hexadecimal format.                      |
| \<group owner\>                         | The name/mnemonic for the owner of the group.                                          |
| \<SCP/SCU Type\>                        | The SCP and SCU DICOM Type (1, 1C, 2, 3, etc.).                                        |
| \<default value\>                       | The default value of the element in the message.                                       |

Example of a macro definition:

{\$define N-EVENT-REPORT-RQ}

Affected SOP Class UID\|(0000,0002)\|\|1/1\|

Command Field\|(0000,0100)\|\|1/1\|0100H

Message ID\|(0000,0110)\|\|1/1\|

Priority\|(0000,0700)\|\|1/1\|

Data Set Type\|(0000,0800)\|\|1/1\|0003H

Affected SOP Instance UID\|(0000,1000)\|\|1/1\|

Event Type ID\|(0000,1002)\|\|1/1\|

{\$end N-EVENT-REPORT-RQ}

Macros are used for building model message templates.

A message template consists of four different types of records. The “template” record identifies the beginning of the message template. The “SOP” record defines the SOP class for the template. The “element” and “macro invocation” records define the element attributes of the template. The different fields for the “template” and “sop” records are defined below:

|                                                                              |                                                                                         |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| • Template Record:                                                           | \$TEMPLATE \| \<message name\> \| \<DIMSE\> \| \<typename\> \| \<typeid\>               |
| • SOP Record:                                                                | \$SOP \| \<SOP class name\>                                                             |
| • Element Record:                                                            | \<element name\> \| \<tag\> \| \<group owner\> \| \<SCP/SCU Type\> \| \<default value\> |
| • Macro Invocation:                                                          | {\<name of macro\>}                                                                     |
| The different fields for the “template” and “sop” records are defined below: |                                                                                         |
| \<message name\>                                                             | The name of the template.                                                               |
| \<DIMSE\>                                                                    | The DICOM Message Service Element.                                                      |
| \<typename\>                                                                 | The DICOM Event Type Name.                                                              |
| \<typeid\>                                                                   | The DICOM Event Type Id.                                                                |
| \<SOP class name\>                                                           | The case-sensitive name of the SOP class defined in the UID.DIC file.                   |

> **NOTE:** Refer to the [DICOM standard, Part 4 Service Class Specifications (PS 3.4)](https://dicom.nema.org/medical/dicom/current/output/html/part04.html) for the definition of the DICOM terms.

Example of a template definition:

\$TEMPLATE\|PATIENT DEMOGRAPHIC CHANGE\|N-EVENT-REPORT\|Patient Updated\|3\|

\$SOP\|VA Detached Patient Management SOP Class

{N-EVENT-REPORT-RQ}

Instance Creation Date\|(0008,0012)\|\|-/2\|

Instance Creation Time\|(0008,0013)\|\|-/2\|

Instance Creator UID\|(0008,0014)\|\|-/2\|

{Patient Data}

{Message Handle}

The element information in the file TEMPLATE.DIC is extracted directly from the DICOM standard, [Part 6: Data Dictionary (PS 3.6)](https://dicom.nema.org/medical/dicom/current/output/html/part06.html) and [Part 7:Message Exchange (PS 3.7).](https://dicom.nema.org/medical/dicom/current/output/html/part07.html) The list of attributes comes from [Part 3: Information Object Definitions (PS 3.3)](https://dicom.nema.org/medical/dicom/current/output/html/part03.html) and [Part 7:Message Exchange (PS 3.7).](https://dicom.nema.org/medical/dicom/current/output/html/part07.html)

See [https://www.dicomstandard.org/](https://www.dicomstandard.org/%20) for more information about the DICOM standard.

The data from this file is stored in MUMPS in the following structure:

^MAGDICOM(2006.52,d0,0) = Title ^ DIMSE ^ SOP Class ^ Type Name ^ Type ID

^MAGDICOM(2006.52,d0,1,d2,0) = tag ^ name ^ SCP type / SCU type ^ Value ^ Pointer

^MAGDICOM(2006.52,“B”,Title,d0) = “”

### B.3.6 UID.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file UID.DIC contains the definitions of the unique identifiers for SOP classes, transfer syntax’s and class instances for the DICOM standard. As part of the installation process, this file is read by routine ^MAGDMB5 and is used to construct the FileMan table DICOM UID Dictionary (File 2006.53, stored in ^MAGDICOM(2006.53,…)).

DICOM uses a unique object identification scheme based upon ISO-9834-3. This standard uses numeric fields separated by periods that are assigned in a left-to-right hierarchical fashion in order to allow uniqueness. All DICOM standard UIDs have the root 1.2.840.10008, and UIDs generated by the VA have the root 1.2.840.113754.

The file UID.DIC contains all the pre-defined UID values that are used by the VistA DICOM applications.

The file UID.DIC contains two types of records:

|                                                                                                                                                                                                                                              |                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| • UID Record:                                                                                                                                                                                                                                | \<UID Value\> \| \<UID Name\> \| \<UID Type\> \| \<Reference\> \| \<Function\>     |
| • Meta Record                                                                                                                                                                                                                                | \| \<UID Value\> \| \<UID Name\>                                                   |
| When a UID identifies a Meta SOP Class, the record for the Meta SOP Class will be followed by one or more Meta records. In such a case, each Meta record defines one UID that identifies a SOP class that is a member of the Meta SOP class. |                                                                                    |
| The different fields are defined below:                                                                                                                                                                                                      |                                                                                    |
| \<UID Value\>                                                                                                                                                                                                                                | The unique period delimited numeric string that represents the value of the UID    |
| \<UID Name\>                                                                                                                                                                                                                                 | The text name for the UID; 1:1 mapping between \<UID Value\> and \<UID NAME\>.     |
| \<UID Type\>                                                                                                                                                                                                                                 | Indicates the usage for the UID.                                                   |
| \<Reference\>                                                                                                                                                                                                                                | Documents where the UID is officially defined.                                     |
| \<Function\>                                                                                                                                                                                                                                 | Identifies which UIDs are supported by VistA Storage (for example, S for Storage). |

Example of some UID definitions:

1.2.840.10008.1.1\|Verification SOP Class\|SOP Class\|Part 4\|\*

1.2.840.10008.3.1.2.1.4\|Detached Patient Management Meta SOP Class

\|Meta SOP Class\|Part 4\|

\|1.2.840.10008.3.1.2.1.1\|Detached Patient Management SOP Class

\|1.2.840.10008.3.1.2.2.1\|Detached Visit Management SOP Class

1.2.840.113754.3.1.2.1.4\|VA Detached Patient Management Meta SOP Class

\|Meta SOP Class\|Part 4\|S

\|1.2.840.113754.3.1.2.1.1\|VA Detached Patient Management SOP Class

\|1.2.840.113754.3.1.2.2.1\|VA Detached Visit Management SOP Class

The UID information in the file UID.DIC is extracted directly from the [DICOM Standard, Part 6: Data Dictionary (PS 3.6)](https://dicom.nema.org/medical/dicom/current/output/html/part06.html) and material supplied by the Imaging Project.

The data from this file is stored in MUMPS in the following structure:

^MAGDICOM(2006.53,d0,0) = Name ^ UID Code ^ Type ^ Reference

^MAGDICOM(2006.53,d0,1,d1,0) = Name ^ UID Code

^MAGDICOM(2006.53,“B”,Name,d0)= “”

^MAGDICOM(2006.53,“C”,UID Code,d0) = “”

^MAGDICOM(2006.53,d0,1,“B”,Name,d1) = “”

^MAGDICOM(2006.53,d0,1,“C”,UID Code,d1) = “”

### B.3.7 Additional Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain DICOM elements are extracted from the DICOM image header and copied into the “about image” text file when an image is processed. These data items are then displayed on the diagnostic workstation with the image.

Different items may be selected and displayed for different modalities. Currently, the following files with lists of additional data-items are available:

- DATAGECT.DIC (specific for CT equipment from General Electric and others)
- DATA_CR.DIC (specific for CR equipment)
- DATAMISC.DIC (general for any other equipment)
- DATA_MRI.DIC (specific for MRI equipment)

In these files, each line that defines a data-item consists of two parts: the first part identifies an attribute tag, and the second part specifies an attribute name, e.g.:

> 0008,0070\|Manufacturer

The data from these files is stored in MUMPS in the following structure:

^MAGDICOM(2006.511,d0,0) = filename

^MAGDICOM(2006.511,d0,1,d1,0)=tag ^ name

^MAGDICOM(2006.511,“B”,filename,d0) = “”

#### B.3.7.1 DATAMISC.DIC

The file DATAMISC.DIC contains a list of general-purpose elements to be displayed. These data-items are:

> 0008,0008\|Image Type

> 0008,0023\|Image Date

> 0008,0033\|Image Time

> 0008,0060\|Modality

> 0008,0070\|Manufacturer

> 0008,0080\|Institution Name

> 0008,1010\|Station Name

> 0008,1090\|Manufacturer's Model Name

> 0018,0010\|Contrast/Bolus Agent

> 0018,0015\|Body Part Examined

> 0018,5100\|Patient Position

> 0020,0010\|Study ID

> 0020,0011\|Series Number

> 0020,0012\|Acquisition Number

> 0020,0013\|Image Number

> 0020,0032\|Image Position (Patient)

> 0028,0004\|Photometric Interpretation

> 0028,0010\|Rows

> 0028,0011\|Columns

> 0028,0030\|Pixel Spacing

> 0028,0101\|Bits Stored

> 0028,0102\|High Bit

> 0028,0103\|Pixel Representation

> 0028,1052\|Rescale Intercept

0028,1053\|Rescale Slope

> **NOTE:** In the following lists, the highlighted lines are additional fields.

#### B.3.7.2 DATAGECT.DIC

The data-items for CTs from General Electric (and other manufacturers) are:

> 0008,0008\|Image Type

> 0008,0023\|Image Date

> 0008,0033\|Image Time

> 0008,0060\|Modality

> 0008,0070\|Manufacturer

> 0008,0080\|Institution Name

> 0008,1010\|Station Name

> 0008,1090\|Manufacturer's Model Name

> 0018,0010\|Contrast/Bolus Agent

> 0018,0015\|Body Part Examined

> 0018,0050\|Slice Thickness

> 0018,0060\|KVP

> 0018,1100\|Reconstruction Diameter

> 0018,1120\|Gantry/Detector Tilt

> 0018,1150\|Exposure Time

> 0018,1151\|X-ray Tube Current

> 0018,1190\|Focal Spot(s)

> 0018,1210\|Convolution Kernel

> 0018,5100\|Patient Position

> 0020,0010\|Study ID

> 0020,0011\|Series Number

> 0020,0012\|Acquisition Number

> 0020,0013\|Image Number

> 0020,0032\|Image Position (Patient)

> 0020,0060\|Laterality

> 0020,1040\|Position Reference Indicator

> 0020,1041\|Slice Location

> 0028,0004\|Photometric Interpretation

> 0028,0010\|Rows

> 0028,0011\|Columns

> 0028,0030\|Pixel Spacing

> 0028,0101\|Bits Stored

> 0028,0102\|High Bit

> 0028,0103\|Pixel Representation

> 0028,1052\|Rescale Intercept

> 0028,1053\|Rescale Slope

#### B.3.7.3 DATA_CR.DIC

The data-items for CRs are:

> 0008,0008\|Image Type

> 0008,0023\|Image Date

> 0008,0033\|Image Time

> 0008,0060\|Modality

> 0008,0070\|Manufacturer

> 0008,0080\|Institution Name

> 0008,1010\|Station Name

> 0008,1090\|Manufacturer's Model Name

> 0018,0010\|Contrast/Bolus Agent

> 0018,0015\|Body Part Examined

> 0018,1004\|Plate ID

> 0018,1400\|Acquisition Device Processing Description

> 0018,1405\|Relative X-ray Exposure

> 0018,5100\|Patient Position

> 0018,6000\|Sensitivity

> 0020,0010\|Study ID

> 0020,0011\|Series Number

> 0020,0012\|Acquisition Number

> 0020,0013\|Image Number

> 0020,0032\|Image Position (Patient)

> 0028,0004\|Photometric Interpretation

> 0028,0010\|Rows

> 0028,0011\|Columns

> 0028,0030\|Pixel Spacing

> 0028,0101\|Bits Stored

> 0028,0102\|High Bit

> 0028,0103\|Pixel Representation

> 0028,1052\|Rescale Intercept

> 0028,1053\|Rescale Slope

#### B.3.7.4 DATA_MRI.DIC

The data items for MRIs are:

> 0008,0008\|Image Type

> 0008,0023\|Image Date

> 0008,0033\|Image Time

> 0008,0060\|Modality

> 0008,0070\|Manufacturer

> 0008,0080\|Institution Name

> 0008,1010\|Station Name

> 0008,1090\|Manufacturer's Model Name

> 0018,0010\|Contrast/Bolus Agent

> 0018,0015\|Body Part Examined

> 0018,0020\|Scanning Sequence

> 0018,0080\|Repetition Time

> 0018,0081\|Echo Time

> 0018,0083\|Number of Averages

> 0018,0091\|Echo Train Length

> 0018,1310\|Acquisition Matrix

> 0018,5100\|Patient Position

> 0020,0010\|Study ID

> 0020,0011\|Series Number

> 0020,0012\|Acquisition Number

> 0020,0013\|Image Number

> 0020,0032\|Image Position (Patient)

> 0028,0004\|Photometric Interpretation

> 0028,0010\|Rows

> 0028,0011\|Columns

> 0028,0030\|Pixel Spacing

> 0028,0101\|Bits Stored

> 0028,0102\|High Bit

> 0028,0103\|Pixel Representation

> 0028,1052\|Rescale Intercept

> 0028,1053\|Rescale Slope

## B.4 Site-Specific Master Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the format and contents of the site-specific master files.

Currently, the following files exist:

| File Name                  | FileMan Table | Comment                                                                                                                                                                       |
|--------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AETITLE.DIC                    | 2006.588          | Contains list of aliases’ that point to entries in the SCP_LIST.DIC                                                                                                               |
| INSTRUMENT.DIC                 | 2006.581          | Contains list of operational instruments and their associated listening ports.                                                                                                    |
| MODALITY.DIC                   | 2006.582          | Contains list of parameters for handling modalities.                                                                                                                              |
| PORTLIST.DIC                   | 2006.584          | Contains list of port numbers for handling instruments. Contains the port numbers of commercial PACS (typically Mitra Brokers) that receive messages from the DICOM Text Gateway. |
| SCU_List.DIC                   | 2006.585          | Contains lists of parameters for User Applications.                                                                                                                               |
| WORKLIST.DIC                   | 2006.583          | Contains list of parameters for Modality Worklist handling.                                                                                                                       |
| Clinical Specialty DICOM & HL7 | 2006.5831         | Contains mapping of Request Services (^GMR(123.5)) to Image Index for Specialty/Subspecialty (^MAG(2005.84))                                                                      |
| TERMINAL_TITLE.DIC         | N/A               | [See Appendix A, Section A.3](#a.3-terminal_title.dic)                                                                                                                            |

The contents of the files in this section need to be customized to reflect the actual attributes used at the site.

> **NOTE:** These changes should be made to the text file dictionaries in DICOM\Dict only. The software will load this information from these dictionary files into the global variables, overwriting any previously saved information.

> **NOTE:** in the .dic files, leading and trailing spaces are ignored when the data is imported into the database. This makes it possible to align information for easier reading:

\#

RADIOLOGY \|\|RAD\| RAD \|LONG\|Local Vista Modality Worklist provider

DENTAL \|\|CON\| DENT \|LONG\|Local dental worklist provider

OPHTHALMOLOGY \|\|CON\| OPHTH \|LONG\|Local eye care worklist provider

OPTOMETRY \|\|CON\| OPTOM \|LONG\|Local optometry worklist provider

CARDIOLOGY \|\|CON\| CARDIO \|LONG\|Local cardiology worklist provider

PATH \|\|LAB\| CY,SP \|LONG\|Local cardiology worklist provider

\#

### B.4.1 AETITLE.DIC 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file APPLICATION ENTITY TITLE (#2006.588) on the DICOM Gateway provides aliases for APPLICATION ENTITY TITLES stored in the global ^MAGDICOM (2006.588) and AE_TITLE.DIC file.

DICOM negotiation requests now require <u>known</u> Called Application Entity Titles so that acceptable presentation contexts in SCP_LIST.DIC can be properly identified.

AE_TITLE.DIC is an Application Entity Title dictionary. The AE_TITLE.DIC is used to map the Called Application Entity Title of a DICOM negotiation request to the alias that identifies the VistA Application Entity Title name for the SCP. This is used for looking up acceptable presentation contexts in SCP_LIST.DIC. The Called Application Entity Title for a DICOM request must either be the VistA Application Entity Title name for the SCP defined in SCP_LIST.DIC (for example, “VISTA_STORAGE”) or else one defined in AE_TITLE.DIC as an alias for the VistA one. Otherwise, the DICOM negotiation request will be rejected.

The default Mallinckrodt SEND_IMAGE.EXE Called Application Entity Title “DICOM_STORAGE” is mapped to “VISTA_STORAGE” in the distributed version of AE_TILE.DIC as shown below. (The mapping is not case-sensitive.)

The AE_TITLE.DIC is also used to record names associated with Application Entity Titles. (For example, “Walter Reed AMC” is the site name for the Application Entity Title “OS1WRAMC”.)

Add any entries to AE_TITLE.DIC (none may be needed) and run Menu Option 4-2-3.

\# Last edited 30 July 2008, 11:43 am

\#

\# Application Entity Title

\# \<Application Entity Title\> \| \<VistA Application Title Alias\> \| \<Site Name\>

\#

\# This entry is for Mallinckrodt Send_Image

DICOM_STORAGE\|VistA_Storage\|VistA Imaging Testing

\#

\# Put your entries here

\#

\#

\# end of file

### B.4.2 INSTRUMENT.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file INSTRUMENT.DIC contains the definitions of the various image acquisition devices that the site uses. Menu Option 4.2.4, Update INSTRUMENT.DIC, reads this file to populate the Instrument Dictionary file (#2006.581). This is done as part of the installation process, and whenever operational information has changed at the site.

Use the VistA Imaging DICOM Gateway menu to update this master file as follows:

4\. System Maintenance

à 2. Gateway Configuration and DICOM Master Files

à à 4. Update INSTRUMENT.DIC

Each image producing instrument must send its images to a VistA storage provider. In the VistA DICOM Image Gateway, there is a separate storage provider process running on a dedicated network port for each instrument that produces images. The file INSTRUMENT.DIC lists each image producing instrument and its dedicated communications port, along with its corresponding imaging service.

An entry in the file INSTRUMENT.DIC is formatted as follows:

\<mnemonic\> \| \<description\> \| \<institution name\> \| \<imaging service\> \| \<port\> \[ \| \<machine \]

The different fields are defined below:

\<mnemonic\> A short code for the instrument created by the site (it must be unique). Typically, abbreviations like CR1, CT2, NM, GI-FLUORO, and so forth.

\<description\> Free text describing the instrument and its location.

\<institution name\> The name of the institution (as defined in Piece(^DIC(4,ien,0),”^”,1)). It also may be the site ID or may be left null (default is the site of the DICOM Gateway).

\<imaging service\> Indicates where the orders and reports are placed on the hospital information system (“RAD”, “CON”, or “LAB” – see below)

\<port\> The network communications port number (this must be unique, see Appendix E)

\<machine\> Identifies the Image Gateway computer that will receive image files from this instrument (optional parameter, free text)

Example of a portion of the INSTRUMENT.DIC file:

> \# Computed Radiography

> CR1\|Fuji AC3 CR, Room 2156\|Wilmington, DE\|RAD\|60050\|ISWIMGDIG1

> CR2\|Fuji AC3 CR, Room 2160 (Chest)\|Wilmington, DE\|RAD\|60051\|ISWIMGDIG3

> CR3\|Fuji AC3 CR, Cubby, 2145 Hallway\|Wilmington, DE\|RAD\|60052\|ISWIMDIG2

> \#

> \# Computed Tomography

> CT1\|GE High Speed Advantage, Room 2142\|Wilmington, DE\|RAD\|60060\|ISWIMGDIG1

> \#

> \# Clinical Specialties

> \# EYE-2\|Eye Examination Station\|\|CON\|60302\|ISWIMGDIG1

In the previous example, please observe that there are five different instruments and three different modalities.

The site must create an entry in the file INSTRUMENT.DIC for each piece of equipment that is going to produce images and send them to VistA. Otherwise, the DICOM Gateway cannot acquire the images from the equipment.

Please note that the port numbers must be unique for every instrument. Use a unique port even where several different VistA DICOM Image Gateways are used. Making the port numbers unique, makes it possible to redirect the output of any image producing instrument to a different VistA DICOM Image Gateway by adding a second IP address to the gateway. The recommended port number scheme is included in [Appendix E](#appendix-e-port-numbers-for-vista-imaging-dicom-gateway-applications).

Names of institutions must be spelled exactly, as in the Institution File (File number 4, stored in ^DIC(4,...)) or use the IEN from the Institution File. These names are processed in a case-insensitive fashion. Only the part of the name before the first comma needs to match the value in the institution file. Any other punctuation characters that occur in that part of the official name must appear in the value that is entered here.

If no name is specified for the name of an institution, the default value from the gateway site will be used.

Names of imaging services must be either “RAD,” for Radiology, or “CON,” for consults and procedures, or “LAB” for Anatomic Pathology.

> **NOTE:** The names must be spelled in all upper-case characters.

The sixth parameter identifies the Image Gateway to which the instrument will transmit its image files. DICOM Gateways are identified by the host-name of their computer. Host-names are typically assigned by OIT and site management, and usually follow VA-wide naming conventions.

A sample file INSTRUMENT.SAMPLE is supplied with the VistA Imaging DICOM Gateway distribution and may be edited by adding and/or deleting the pound sign (“#”). During an initial installation, this sample file is renamed to INSTRUMENT.DIC. When performing an upgrade, the existing copy of this file will remain unaffected. Information from the sample file may be manually transferred to the operational master file at the discretion of the site.

#### B.4.2.1 Legacy Icons for Instruments

The generation of icons is now a manual procedure for all instruments when the program ^MAGDMFIC is run. The Site Manager can then adjust the icons in the window to show only those storage providers that are actually being used on the current Server.

When set-up parameters need to be modified for one of these icons, it is important to know the values that should be entered. The typical values for each of these icons are shown below.

![](vista-imaging-dicom-gateway-installation-guide/072.png)

In the example above, the complete value for “target” would be:

"C:\Program Files(x86)\VistA\Imaging\DICOM\MAG_CSTORE.exe" localhost 60000 CR1Note: The quotes around the path-name for the C-Store program are required.

The entry for “Target” should link the icon to the “C-Store” program, and specify the parameters:

- IP-address is always “localhost” (never modify this value).
- Port number is always 60000 (never modify this value).
- Instrument name is the abbreviation for the instrument, e.g., “CR1” (only modify this value to reflect changes made in the master file INSTRUMENT.DIC).

The icon can be changed to be more descriptive for the type of instrument. For CRs, the distributed system provides two sample icons:

![](vista-imaging-dicom-gateway-installation-guide/073.png)

The end-user may select any other icon that would be more descriptive of the instrument.

#### B.4.4.2 Invoking MAG_CSTORE.EXE without an INSTRUMENT.DIC entry

For modality testing, MAG_CSTORE.EXE may be invoked using a port number instead of the instrument name. The port number must not be one that is already used in INSTRUMENT.DIC or used for anything else. This bypasses the HDIG and is useful for acquiring DICOM objects in the traditional manner and storing them in the C:\DICOM\IMAGE_IN folder.

The complete format of the command is shown below.

#### B.4.4.2.1 Traditional way using an instrument mnemonic defined in INSTRUMENT.DIC

MAG_CSTORE localhost 60000 \<instrument mnemonic\>

> Example: MAG_CSTORE.exe" localhost 60000 CR1

#### B.4.4.2.2 Specifying a port number (one not used in INSTRUMENT.DIC)

MAG_CSTORE localhost 60000 \<port number\>

> Example: MAG_CSTORE.exe" localhost 60000 50100

#### B.4.4.2.3 Specifying a port number and designating an Imaging Service

MAG_CSTORE localhost 60000 “\<port number\> \<imaging service\>”

> Example: MAG_CSTORE.exe" localhost 60000 “50100 RAD”

#### B.4.4.2.4 Specifying a port number and designating an Imaging Service and Location

MAG_CSTORE localhost 60000 “\<port number\> \<imaging service\> \<location\>”

> Example: MAG_CSTORE.exe" localhost 60000 “50100 RAD BOSTON, MA”

MAG_CSTORE.EXE may be invoked either from the CMD shell or via a shortcut. The following two figures illustrate this.

![](vista-imaging-dicom-gateway-installation-guide/074.png)

![](vista-imaging-dicom-gateway-installation-guide/075.png)

### B.4.3 MODALITY.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file MODALITY.DIC contains the definitions of the parameters that the DICOM Gateway needs to process image files, store them on the file server, and associate them with the patient record. Menu Option 4.2.5, Update MODALITY.DIC, reads this file to populate the Modality Type Dictionary File (#2006.582). This is done as part of the installation process and whenever operational information has changed at the site.

Use the VistA Imaging DICOM Gateway menu to update this master file as follows:

4\. System Maintenance

à 2. Gateway Configuration and DICOM Master Files

à à 5. Update MODALITY.DIC

#### B.4.3.1 Image Processing Overview

After the gateway acquires images, it has to process them and incorporate them into the patient medical record. The rules for processing the images produced by each different kind of modality are stored in the file MODALITY.DIC.

> **NOTE:** The information in the following sections is for reference purposes only. All images can come in through one default entry using the \<DICOM\> rule as shown below.DEFAULT\|DEFAULT\|DEFAULT\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC

Each time the gateway processes an image, it does the following:

1.  Extracts the patient and study information from the image header.
2.  Looks up the study on VistA using the patient and study information from the image header.
3.  Creates the image abstract (also known as thumbnail or icon).
4.  Processes the image according to the image format and parameters specified in the field \<image processing rules\> in the file MODALITY.DIC. Images can be stored in their original DICOM format or converted in TARGA (\*.TGA) format. DICOM format is the preferred. Only in rare instances for VistARad sites and specific modalities that are having display issues, should Targa be used. For more information, see section
5.  *B.4.3.2.1 Image Processing*Rules.
6.  Saves image attributes from the header in a text (\*.TXT) file.

#### B.4.3.2 Assigning Field Values for the Modality Dictionary

The file MODALITY.DIC determines how the DICOM Gateway stores images. The structure of each record is:

Modality Record: \<mfgr\> \| \<model\> \| \<modality\> \| \<image processing rules\> \| \<accession number code\> \| \<text data code\>\| \<text data file\> \| \<imaging service\>

The different fields are:

\<mfgr\> The manufacturer of the equipment producing the images; element (0008,0070).

\<model\> The manufacturer’s model name for the equipment; element (0008,1090).

\<modality\> The official DICOM defined term for the modality; element (0008,0060).

\<image processing rules\> The rules that control the format in which the image is stored. For more information about the syntax of the image processing rules, see section [B.4.3.2.1 Image Processing Rules](\l)

Please use \<DICOM\>.

\<accession number code\> The name of the M routine used to extract the accession number from image header. The typical value is CORRECT^MAGDIR3.

\<text data code\> The M routine for outputting text data (\*.TXT) for diagnostic workstation. This is how Hounsfield units are calculated for CT images when converting to DICOM.

\<text data file\> A text file that lists DICOM attributes to output as text (\*.TXT) for diagnostic workstation (see [*B.3.7 Additional Data*](#b.3.7-additional-data) for a description of the format of a text data file).

\<imaging service\> A parameter that indicates where the orders and reports are placed on the hospital information system. The value is either “RAD” for Radiology, “CON” for CPRS consults and procedures, or “LAB” for Anatomic Pathology. It is used to select imaging service-specific processing.

The file MODALITY.DIC includes defaults as well as entries for different modalities. If there is no definition for the specific device, the DICOM Gateway uses the default definitions.

> **NOTE:** There can be multiple entries for an instrument, if the instrument produces more than one type of image.

There are several types of default definitions:

- The general default modality definition must always be present in the file MODALITY.DIC and should never be modified.

> DEFAULT\| DEFAULT\|DEFAULT\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|RAD

- You can also set up modality-specific defaults for each modality type, as noted below and illustrated in the example. Including these definitions, while optional, is strongly recommended so that individual modalities can be converted to DICOM storage one at a time. Additional examples can be found in the MODALITY.SAMPLE file provided during installation.

> DEFAULT\| DEFAULT\|CR\|R8/\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|RAD

- In addition to the default definitions, you can set up or continue using modality-specific definitions by manufacturer, model, and modality as illustrated in the following example.

> ACME, Inc.\|Coyotes Rule\|CT\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAGECT.DIC\|RAD

The DICOM Gateway applies the modality definitions in the following order of specificity:

1.  Manufacturer, model, and modality
2.  General by modality type
3.  General

If there is a specific modality definition for a modality, manufacturer, and model, these settings will apply to that modality. If such a definition is missing, the default setting for the modality type for the modality will apply. If this setting is also missing, the general default definition will apply.

We recommend using the defaults for all modalities. Use device-specific definitions only for devices if the images from these devices do not display properly when stored in DICOM format. For more information, see [B.4.3.2.1 Image Processing Rules](\l)

The MODALITY.DIC entry for the image acquisition device should specify “\<DICOM\>” in the \<image processing rules\> field when the image should be stored in DICOM format. Typically, the entry should specify “CORRECT^MAGDIR3” in the \<accession number code\> field. The “RoadRunner” example illustrates this:

\# Examples:

\#

\# ACME CT Company\|BETA\|CT\|b12 f0\|GECT^MAGDIR3\|GECTHISA^MAGDIR4A\|DATAGECT.DIC\|RAD

\#

\# RoadRunner, INC\|Beep-Beep\|OT\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|CON

\#

\# end of file

The next example shows a configuration to handle a CT study containing both standard and Secondary Capture images. The normal CT SOP Class-based images will process into a Targa images. The accompanying Secondary Capture SOP Class-based image will process but stay as a DICOM image. The trigger to accomplish this is the \<SC\> pseudo modality type.

\# Examples:

\#

Roadrunner, Inc.\|Beep-Beep\|CT\|b12 a1000 f0 c4095\|LONGCASE^MAGDIR3\|\|DATAGECT.DIC\|RAD

Roadrunner, Inc.\|Beep-Beep\|\<SC\>\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|RAD

\#

\# end of file

The \<SC\> pseudo-modality code can only be used for scanners that support the SOP classes listed below. (Note: These objects can only be saved as DICOM, not as TGA.):

- 1.2.840.10008.5.1.4.1.1.7 (Secondary Capture Image Storage)
- 1.2.840.10008.5.1.4.1.1.7.2 (Multi-frame Grayscale Byte Secondary Capture Image Storage)
- 1.2.840.10008.5.1.4.1.1.7.3 (Multi-frame Grayscale Word Secondary Capture Image Storage)
- 1.2.840.10008.5.1.4.1.1.7.4 (Multi-frame True Color Secondary Capture Image Storage

#### B.4.3.2.1 Image Processing Rules

Images are converted from the DICOM format to the Targa format by the program MAG_DCMTOTGA.EXE. The image processing rules are parameters of MAG_DCMTOTGA.EXE and control the conversion process. The rules are specified in the master file MODALITY.DIC. They are not case-sensitive.

Two sets of rules, separated by a slash (/), can be placed in the \<image processing rules\> field of the modality record. When two sets of rules are present in the same record, the first set of rules defines the reduced size image. The second set defines the full-size image that the diagnostic workstation uses.

The value \<DICOM\> in a rule indicates that the DICOM Gateway should store the full-size images in DICOM format (with a .DCM extension). When the value \<DICOM\> is not present in the rule, the DICOM Gateway stores the full-size image with a .BIG extension.

In addition to the full-size image, the DICOM Gateway can produce a reduced Targa image (with a .TGA extension). The framing and reduction factors in the modality record define the Targa image.

The following table explains the framing and reduction parameters and their values:

> A*nnn* Add *nnn* to each pixel (before the minimum/maximum check is performed).

> B*nnn*\* Specifies the number of bits in the original pixel.

> C*nnn* Ceiling (maximum) pixel value; any value \> *nnn* is replaced by *nnn.*

> F*nnn* Floor (minimum) pixel value; any value \< *nnn* is replaced by *nnn.*

> I Invert each pixel.

> O*nnn*\* Byte offset in the DICOM file to the image.

> R1 Reduce the size of the image file by outputting the low-order byte of a two-byte pixel.

> R2 Reduce the size of the image file by two by shifting two-byte pixels into one-byte pixels.

> R4 Reduce the size of the image by four by combining four pixels into one two-byte pixel.

> R8 Reduce the size of the image by eight by combining four pixels into one one-byte pixel.

> R16 Reduce the size of the image by sixteen by combining sixteen pixels into one two-byte pixel.

> R32 Reduce the size of the image by thirty-two by combining sixteen pixels into one one-byte pixel.

> S*nnn* Subtract *nnn* from each pixel (unsigned arithmetic, executed before add is performed).

> X*nnn*\* X-dimension of the image (horizontal width or the number of columns).

> Y*nnn*\* Y-dimension of the image (vertical height or the number of rows).

When it processes an image, the DICOM Gateway validates the image processing rules. This is necessary to ensure that the original copy of the image is not altered during storage and is essential for compliance with DICOM Level 2 archive standards. Images, like CR and DX, can only have \<DICOM\> or no parameter in MODALITY.DIC for the full-size image. The image processing rules for such images cannot have reduction and framing parameters. In addition to this, the reduced image associated with these types of images, must have a valid reduction factor (Rnn), where nn represents a reduction value with one to two digits. The reduced image may also have framing parameters defined.

The following examples are valid and will be accepted.  
(Please note that these are partial entries shortened for simplicity.)

> ACME, Inc.\|Coyotes Rule\|CR\|

> ACME, Inc.\|Coyotes Rule\|CR\|\<DICOM\>

> ACME, Inc.\|Coyotes Rule\|CR\| R8/

> ACME, Inc.\|Coyotes Rule\|CR\| R8/\<DICOM\>

> ACME, Inc.\|Coyotes Rule\|CR\|b10 f0 c1023 R8/

> ACME, Inc.\|Coyotes Rule\|CR\|b10 f0 c1023 R8/\<DICOM\>

The following rules define syntax of in the MODALITY.DIC file:

- The slash can be followed *only by* \<DICOM\>. That is, the backslash cannot be followed by a reduction factor, a framing factor, or a space.
  - When the backslash is followed by \<DICOM\>, the image will be processed in DICOM format. Its full-size image will be stored with a .DCM extension and its reduced size image will have a TGA extension.
  - When the slash is *not* followed by \<DICOM\>, the image will be processed in Targa format. Its full-size image will be stored with a .BIG extension and its reduced size image, if defined, will have a TGA extension.
- The framing and reduction parameters should *precede* the backslash.
- When there is a slash, the reduction factor should be specified. That is, a slash should *always* be preceded by a reduction factor. The slash should not be used when a reduction factor is not specified.

> The following examples are *not* valid and will be rejected.

> ACME, Inc.\|Coyotes Rule\|CR\| /\<DICOM\>

> ACME, Inc.\|Coyotes Rule\|CR\| R8/R8

> ACME, Inc.\|Coyotes Rule\|CR\| R8/R8\<DICOM\>

> ACME, Inc.\|Coyotes Rule\|CR\|b10 f0 c1023 R8/\|b10 f0

> ACME, Inc.\|Coyotes Rule\|CR\|b10 f0 c1023 R8/ b10 f0 \<DICOM\>

> ACME, Inc.\|Coyotes Rule\|CR\| R8/\<DICOM\>\<DICOM\>

#### B.4.3.2.2.1 Typical Values for Image Conversion Parameters, for reference only

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parameter Value</strong></th>
<th><strong>Equipment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;DICOM&gt;</td>
<td>Images stored in VistA in DICOM format, exactly as they were received from the instrument.</td>
</tr>
<tr class="even">
<td>b8</td>
<td>Acuson, Sequoia, US</td>
</tr>
<tr class="odd">
<td>b12 f0 c4095</td>
<td>ADAC, *, NM</td>
</tr>
<tr class="even">
<td>b12 f0 c4095</td>
<td>ADAC, Solus, NM</td>
</tr>
<tr class="odd">
<td>b12 f0 c4095</td>
<td>ADAC, Vertex, NM</td>
</tr>
<tr class="even">
<td><p>b12 f0 c4095 R8/ or</p>
<p>b12 f0 c4095 R8/&lt;DICOM&gt;</p></td>
<td>AGFA, ADC 5145, CR</td>
</tr>
<tr class="odd">
<td>b8</td>
<td>Aspect Electronics, Inc., Access Acquisition Module, US and OT</td>
</tr>
<tr class="even">
<td>b8 f0</td>
<td>ATL, 8500-0030-01 (HDI 3000, Pegasus Level 8), US</td>
</tr>
<tr class="odd">
<td><p>b10 f0 c1023 R8/ or</p>
<p>b10 f0 c1023 R8/&lt;DICOM&gt;</p></td>
<td>DeJarnette Research Systems, ImageShare CR, CR</td>
</tr>
<tr class="even">
<td><p>b10 f0 c1023 R8/ or</p>
<p>b10 f0 c1023 R8/&lt;DICOM&gt;</p></td>
<td>DeJarnette Research Systems, Imageshare Fuji CR Acquisition Station, CR</td>
</tr>
<tr class="odd">
<td>b8</td>
<td>Diasonics, *, US</td>
</tr>
<tr class="even">
<td>b10</td>
<td>GE Medical Systems, DLX, XA</td>
</tr>
<tr class="odd">
<td>b8</td>
<td>GE Medical Systems, DRS, RF</td>
</tr>
<tr class="even">
<td>b12 f0</td>
<td>GE Medical Systems, Genesis CT9800 QHL, CT</td>
</tr>
<tr class="odd">
<td>b12 f0</td>
<td>GE Medical Systems, Genesis HiSpeed RP, CT</td>
</tr>
<tr class="even">
<td>b12 f0</td>
<td>GE Medical Systems, Genesis Jupiter, CT</td>
</tr>
<tr class="odd">
<td>b12 f0</td>
<td>GE Medical Systems, Genesis Signa, MR</td>
</tr>
<tr class="even">
<td>b12 f0</td>
<td>GE Medical Systems, HiSpeed CT/i, CT</td>
</tr>
<tr class="odd">
<td>b12 f0</td>
<td>GE Medical Systems, HiSpeed RP, CT</td>
</tr>
<tr class="even">
<td>a1000 b12 f0 c4095</td>
<td>GE Medical Systems, ProSpeed, CT</td>
</tr>
<tr class="odd">
<td>b12 f0</td>
<td>GE Medical Systems, Rhapsode, CT</td>
</tr>
<tr class="even">
<td>b12 f0 c4095 R8</td>
<td>Lumisys, *, CR, CT, NM, OT, RAD, SC and US</td>
</tr>
<tr class="odd">
<td>b12 f0 c4095 R8</td>
<td>Lumisys, LS75, CR, CT, MR, MRI, NM, OT, RAD, SC and US</td>
</tr>
<tr class="even">
<td>b12 f0 c4095</td>
<td>Picker International, Inc., AX000, MR</td>
</tr>
<tr class="odd">
<td>b12 f0 c4095</td>
<td>Picker International, Inc., Edge 1.5T, MR</td>
</tr>
<tr class="even">
<td>b16 a1000 f0 c4095</td>
<td>Picker International, Inc., Polaris, CT</td>
</tr>
<tr class="odd">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., PQ2000, CT</td>
</tr>
<tr class="even">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., PQ2000, SC</td>
</tr>
<tr class="odd">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., PQ5000, CT</td>
</tr>
<tr class="even">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., PQ5000, SC</td>
</tr>
<tr class="odd">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., PQ6000, CT</td>
</tr>
<tr class="even">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., PQS, CT</td>
</tr>
<tr class="odd">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., PQS, SC</td>
</tr>
<tr class="even">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., VOXEL, CT</td>
</tr>
<tr class="odd">
<td>b12 a1000 f0 c4095</td>
<td>Picker International, Inc., VOXELQ, CT</td>
</tr>
<tr class="even">
<td>b8</td>
<td>VAMC Image Acquisition Corporation, VA Image Camera, OT</td>
</tr>
</tbody>
</table>

The parameter value for the AGFA CR and the Fuji CR (labeled above as “DeJarnette Research Systems Imageshare”) consists of two parts. The first part is used to create the clinician’s down-sampled image file and the second is used to create the full diagnostic resolution image file, which could either be a file in DICOM format or a file with a .BIG extension.

#### B.4.3.2.2 Accession Number Extraction Subroutines

The names of the MUMPS routines for extracting the accession number from the image header, and for outputting formatted text for display on the diagnostic workstation, are defined by the VistA Imaging Project.

Possible names of subroutines that extract Accession Numbers are:

| Line Tag^Routine | Description                                         |
|----------------------|---------------------------------------------------------|
| CORRECT^MAGDIR3      | DICOM for Consults and Procedures (native DICOM format) |
| IGNORE^MAGDIR3       | Ignore Image                                            |
| STUDYUID^MAGDIR3     | Get from a VistA-generated Study Instance UID           |
| GEMSPACS^MAGDIR3     | GE Medical Systems PACS                                 |
| PQ2000^MAGDIR3       | Picker PQ 2000 CT                                       |
| GECTHISA^MAGDIR3     | GE High Speed Advantage CT                              |
| GEDRS^MAGDIR3        | GE Digital Radiography System                           |
| LONGCASE^MAGDIR3     | Long Case Number                                        |
| PIDCASE^MAGDIR3      | PID after SSN                                           |
| PIDCASE2^MAGDIR3     | PID after //                                            |
| STUDYID^MAGDIR3      | Study ID with Long Case Number                          |
| ADACNM^MAGDIR3       | ADAC Nuclear Medicine                                   |
| SERDESC^MAGDIR3      | ADAC Nuclear Medicine, Solus                            |
| PNAME^MAGDIR3        | After Patient Name                                      |
| MEDCASE^MAGDIR3      | Medicine Capture                                        |

#### B.4.3.2.2.1 Typical Values for Accession Number Subroutine

| Parameter Value | Equipment                                                           |
|---------------------|-------------------------------------------------------------------------|
| PNAME^MAGDIR3       | Acuson, Sequoia, US                                                     |
| LONGCASE^MAGDIR3    | ADAC, \*, NM                                                            |
| LONGCASE^MAGDIR3    | ADAC, Solus, NM                                                         |
| LONGCASE^MAGDIR3    | ADAC, Vertex, NM                                                        |
| LONGCASE^MAGDIR3    | AGFA, ADC 5145, CR                                                      |
| PIDCASE^MAGDIR3     | Aspect Electronics, Inc., Access Acquisition Module, US and OT          |
| LONGCASE^MAGDIR3    | ATL, 8500-0030-01 (HDI 3000, Pegasus Level 8), US                       |
| LONGCASE^MAGDIR3    | DeJarnette Research Systems, ImageShare CR, CR                          |
| LONGCASE^MAGDIR3    | DeJarnette Research Systems, Imageshare Fuji CR Acquisition Station, CR |
| PNAME^MAGDIR3       | Diasonics, \*, US                                                       |
| STUDYID^MAGDIR3     | GE Medical Systems, DLX, XA                                             |
| GEDRS^MAGDIR3       | GE Medical Systems, DRS, RF                                             |
| LONGCASE^MAGDIR3    | GE Medical Systems, Genesis CT9800 QHL, CT                              |
| GECTHISA^MAGDIR3    | GE Medical Systems, Genesis HiSpeed RP, CT                              |
| GECT^MAGDIR3        | GE Medical Systems, Genesis Jupiter, CT                                 |
| LONGCASE^MAGDIR3    | GE Medical Systems, Genesis Signa, MR                                   |
| LONGCASE^MAGDIR3    | GE Medical Systems, HiSpeed CT/i, CT                                    |
| GECTHISA^MAGDIR3    | GE Medical Systems, HiSpeed RP, CT                                      |
| LONGCASE^MAGDIR3    | GE Medical Systems, ProSpeed, CT                                        |
| LONGCASE^MAGDIR3    | GE Medical Systems, Rhapsode, CT                                        |
| LONGCASE^MAGDIR3    | Lumisys, \*, CR, CT, NM, OT, RAD, SC and US                             |
| LONGCASE^MAGDIR3    | Lumisys, LS75, CR, CT, MR, MRI, NM, OT, RAD, SC and US                  |
| PQ2000^MAGDIR3      | Picker International, Inc., AX000, MR                                   |
| PQ2000^MAGDIR3      | Picker International, Inc., Edge 1.5T, MR                               |
| PQ2000^MAGDIR3      | Picker International, Inc., Polaris, CT                                 |
| PQ2000^MAGDIR3      | Picker International, Inc., PQ2000, CT                                  |
| PQ2000^MAGDIR3      | Picker International, Inc., PQ2000, SC                                  |
| LONGCASE^MAGDIR3    | Picker International, Inc., PQ5000, CT                                  |
| PQ2000^MAGDIR3      | Picker International, Inc., PQ5000, CT                                  |
| LONGCASE^MAGDIR3    | Picker International, Inc., PQ5000, SC                                  |
| PQ2000^MAGDIR3      | Picker International, Inc., PQ5000, SC                                  |
| PQ2000^MAGDIR3      | Picker International, Inc., PQ6000, CT                                  |
| PQ2000^MAGDIR3      | Picker International, Inc., PQS, CT                                     |
| PQ2000^MAGDIR3      | Picker International, Inc., PQS, SC                                     |
| PQ2000^MAGDIR3      | Picker International, Inc., VOXEL, CT                                   |
| PQ2000^MAGDIR3      | Picker International, Inc., VOXELQ, CT                                  |
| IGNORE^MADGIR3      | (skip this image)                                                       |

> **NOTE:** There are multiple possibilities for the same modality, depending on whether the image was sent directly or via a commercial PACS.

#### B.4.3.2.3 Text Data Subroutines - Setup

Possible names of subroutines that generate extra text data are:

| Line Tag^Name | Description          |
|-------------------|--------------------------|
| GECT^MAGDIR4A     | General Electric CTs     |
| PICKERCT^MAGDIR4A | Picker CTs               |
| PHILIPCT^MAGDIR4A | Philips CTs              |
| GELCA^MAGDIR4A    | General Electric LCA DLX |

#### B.4.3.2.3.1 Typical Values for Data Extraction Subroutine

| Parameter Value | Equipment                                                           |
|---------------------|-------------------------------------------------------------------------|
| (none)              | Accuson, Sequoia, US                                                    |
| (none)              | ADAC, \*, NM                                                            |
| (none)              | ADAC, Solus, NM                                                         |
| (none)              | ADAC, Vertex, NM                                                        |
| (none)              | AGFA, ADC 5145, CR                                                      |
| (none)              | Aspect Electronics, Inc., Access Acquisition Module, US and OT          |
| (none)              | ATL, 8500-0030-01 (HDI 3000, Pegasus Level 8), US                       |
| (none)              | DeJarnette Research Systems, ImageShare CR, CR                          |
| (none)              | DeJarnette Research Systems, Imageshare Fuji CR Acquisition Station, CR |
| (none)              | Diasonics, \*, US                                                       |
| GELCA^MAGDIR4A      | GE Medical Systems, DLX, XA and RF                                      |
| GECT^MAGDIR4A       | GE Medical Systems, Genesis CT9800 QHL, CT                              |
| GECT^MAGDIR4A       | GE Medical Systems, Genesis HiSpeed RP, CT                              |
| GECT^MAGDIR4A       | GE Medical Systems, Genesis Jupiter, CT                                 |
| GECT^MAGDIR4A       | GE Medical Systems, Genesis Signa, MR                                   |
| GECT^MAGDIR4A       | GE Medical Systems, HiSpeed CT/i, CT                                    |
| GECT^MAGDIR4A       | GE Medical Systems, HiSpeed RP, CT                                      |
| GECT1000^MAGDIR4A   | GE Medical Systems, ProSpeed, CT                                        |
| GECT^MAGDIR4A       | GE Medical Systems, Rhapsode, CT                                        |
| (none)              | Lumisys, \*, CR, CT, NM, OT, RAD, SC and US                             |
| (none)              | Lumisys, LS75, CR, CT, MR, MRI, NM, OT, RAD, SC and US                  |
| (none)              | Picker International, Inc., AX000, MR                                   |
| (none)              | Picker International, Inc., Edge 1.5T, MR                               |
| PickerCT^MAGDIR4A   | Picker International, Inc., Polaris, CT                                 |
| PickerCT^MAGDIR4A   | Picker International, Inc., PQ2000, CT                                  |
| PickerCT^MAGDIR4A   | Picker International, Inc., PQ2000, SC                                  |
| PickerCT^MAGDIR4A   | Picker International, Inc., PQ5000, CT                                  |
| PickerCT^MAGDIR4A   | Picker International, Inc., PQ5000, SC                                  |
| PickerCT^MAGDIR4A   | Picker International, Inc., PQ6000, CT                                  |
| PickerCT^MAGDIR4A   | Picker International, Inc., PQS, CT                                     |
| PickerCT^MAGDIR4A   | Picker International, Inc., PQS, SC                                     |
| PickerCT^MAGDIR4A   | Picker International, Inc., VOXEL, CT                                   |
| PickerCT^MAGDIR4A   | Picker International, Inc., VOXELQ, CT                                  |

#### B.4.3.2.4 Text Data File – Setup

Possible names of files with DICOM elements to be output as text data are:

|              |                      |
|--------------|----------------------|
| Name     | Description      |
| DATAGECT.DIC | General Electric CTs |
| DATA_CR.DIC  | CR Units             |
| DATAMISC.DIC | Miscellaneous        |
| DATA_MRI.DIC | MRI Units            |

#### B.4.3.2.4.1 Typical Values for Text Data Extraction Element List

| Parameter Value | Equipment                                                           |
|---------------------|-------------------------------------------------------------------------|
| DATAMISC.DIC        | Accuson, Sequoia, US                                                    |
| DATAMISC.DIC        | ADAC, \*, NM                                                            |
| DATAMISC.DIC        | ADAC, Solus, NM                                                         |
| DATAMISC.DIC        | ADAC, Vertex, NM                                                        |
| DATAMISC.DIC        | AGFA, ADC 5145, CR                                                      |
| DATAMISC.DIC        | Aspect Electronics, Inc., Access Acquisition Module, US and OT          |
| DATAMISC.DIC        | ATL, 8500-0030-01 (HDI 3000, Pegasus Level 8), US                       |
| DATAMISC.DIC        | DeJarnette Research Systems, ImageShare CR, CR                          |
| DATAMISC.DIC        | DeJarnette Research Systems, Imageshare Fuji CR Acquisition Station, CR |
| DATAMISC.DIC        | Diasonics, \*, US                                                       |
| DATAMISC.DIC        | GE Medical Systems, DLX, XA and RF                                      |
| DATAGECT.DIC        | GE Medical Systems, Genesis CT9800 QHL, CT                              |
| DATAGECT.DIC        | GE Medical Systems, Genesis HiSpeed RP, CT                              |
| DATAGECT.DIC        | GE Medical Systems, Genesis Jupiter, CT                                 |
| DATAGECT.DIC        | GE Medical Systems, Genesis Signa, MR                                   |
| DATAGECT.DIC        | GE Medical Systems, HiSpeed CT/i, CT                                    |
| DATAGECT.DIC        | GE Medical Systems, HiSpeed RP, CT                                      |
| DATAGECT.DIC        | GE Medical Systems, ProSpeed, CT                                        |
| DATAGECT.DIC        | GE Medical Systems, Rhapsode, CT                                        |
| DATAMISC.DIC        | Lumisys, \*, CR, CT, NM, OT, RAD, SC and US                             |
| DATAMISC.DIC        | Lumisys, LS75, CR, CT, MR, MRI. NM, OT, RAD, SC and US                  |
| DATAMISC.DIC        | Picker International, Inc., AX000, MR                                   |
| DATAMISC.DIC        | Picker International, Inc., Edge 1.5T, MR                               |
| DATAGECT.DIC        | Picker International, Inc., Polaris, CT                                 |
| DATAGECT.DIC        | Picker International, Inc., PQ2000, CT                                  |
| DATAGECT.DIC        | Picker International, Inc., PQ2000, SC                                  |
| DATAGECT.DIC        | Picker International, Inc., PQ5000, CT                                  |
| DATAGECT.DIC        | Picker International, Inc., PQ5000, SC                                  |
| DATAGECT.DIC        | Picker International, Inc., PQ6000, CT                                  |
| DATAGECT.DIC        | Picker International, Inc., PQS, CT                                     |
| DATAGECT.DIC        | Picker International, Inc., PQS, SC                                     |
| DATAGECT.DIC        | Picker International, Inc., VOXEL, CT                                   |
| DATAGECT.DIC        | Picker International, Inc., VOXELQ, CT                                  |

#### B.4.3.4 Setting Up the MODALITY.DIC File

The defaults in the modality master file, MODALITY.DIC, are set so the DICOM Gateway will store images in DICOM format. We recommend using defaults for all modalities and devices except when the images do not display correctly. In such cases, you should add an entry for the specific device to store the images in Targa format.

The file MODALITY.SAMPLE, which is included with the DICOM Gateway, contains the general default definition and default definitions for some modalities. The sample file can be edited by adding or deleting the pound sign (“#”), which indicates comments. When the DICOM Gateway is first installed, the sample file is renamed to MODALITY.DIC. When performing an upgrade, the existing copy of MODALITY.DIC remains unaffected.

You should then set up defaults for all modalities to store images in DICOM. You can use the default modality definitions in the sample file to guide you. The following are examples of default definitions.

DEFAULT\| DEFAULT \|CT\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|RAD

DEFAULT\| DEFAULT \|CR\|R8/\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|RAD

DEFAULT\| DEFAULT \|DX\|R16/\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|RAD

DEFAULT\| DEFAULT \|OT\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|RAD

DEFAULT\| DEFAULT \|US\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAMISC.DIC\|RAD

The defaults in MODALITY.SAMPLE are set to store images in their original DICOM format. Some image viewers may have trouble displaying images in DICOM format from certain devices. Such devices should be configured to store images in Targa format.. When the modality master file contains a device-specific definition, the device-specific definition overrides the defaults. You must comment out the device-specific definition for the defaults to be used.

To comment out a definition add the pound sign “#” before the record.

\#ACME, Inc.\|Coyotes Rule\|CT\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAGECT.DIC\|RAD

To activate a definition, remove the pound sign.

ACME, Inc.\|Coyotes Rule\|CT\|\<DICOM\>\|CORRECT^MAGDIR3\|\|DATAGECT.DIC\|RAD

### B.4.4 PORTLIST.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Portlist.dic dictionary is not used anymore. This section is retained for historical reference.

The file PORTLIST.DIC contains the port numbers of commercial PACS (typically Mitra Brokers) that receive messages from the DICOM Text Gateway. This file is read by routine ^MAGDMB8 to (re)construct the FileMan table Radiology TCP/IP Provider Port (File 2006.584, stored in ^MAGDICOM(2006.584,…)). This should be done manually as part of the installation process, and whenever operational information has changed at the site.

Use the VistA Imaging DICOM Gateway menu to update this master file as follows:

4\. System Maintenance

à 2. Gateway Configuration and DICOM Master Files

à à 6. Update PORTLIST.DIC

The VistA DICOM Text Gateway has the ability to send (push) data to multiple destinations. These destinations may be commercial PACSs or commercial providers of the DICOM Modality Worklist service. The file PORTLIST.DIC is used to specify the communication ports for each of the different applications receiving VistA text transactions.

Portlist Record: \<menu option\> \| \<AE title\> \| \<port number\> \| \<file mode\> \| \<channel\>

The various fields are defined below:

\<menu option\> The text for the communications menu of the VistA DICOM Text Gateway.

\<AE title\> The application entity title of the service.

\<port number\> The network communications port number.

\<file mode\> Specifies that the service will use fifo queue file buffering.

\<channel\> Is 1:n, for the DICOM\DATA1 to DICOM\DATAn directory.

An example of the file PORTLIST.DIC is shown below:

\#Menu-option\|AE Title\|Port\|File Mode (FIFO QUEUE or DIRECT)\|CHANNEL

PACS Interface\|VistA PACS I/F\|60041\|FIFO QUEUE\|1

\#MITRA Broker Interface\|VistA PACS I/F\|60042\|FIFO QUEUE\|2

\#DeJarnette Medishare Interface\|VistA PACS I/F\|60043\|FIFO QUEUE\|2

A sample file PORTLIST.SAMPLE is supplied with the VistA Imaging DICOM Gateway distribution and may be edited by adding and/or deleting the pound sign (“#”). During an initial installation, this sample file is renamed to PORTLIST.DIC. When performing an upgrade, the existing copy of this file will remain unaffected. Information from the sample file may be transferred to the operational master file at the discretion of the site.

The port number for this dictionary should be on the range 60040:60049 – see [Appendix E](#appendix-e-port-numbers-for-vista-imaging-dicom-gateway-applications).

The data from this file is stored in MUMPS in the following structure:

^MAGDICOM(2006.584,d0,0) = Destination ^ Name ^ Port ^ Mode ^ Channel

^MAGDICOM(2006.584,“B”,Destination,d0) = “”

### B.4.5 SCU_LIST.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SCU_LIST.DIC contains entries for various types of non-VistA DICOM applications and is stored in the f:\DICOM\Dict folder on the drive specified for storing master files. Initially developed to send images to Print SCPs (Service Class Providers), the use of this file has been expanded.

- One of the purposes of including entries in this file is so that images can be transmitted to DICOM Storage destinations. For the details of using entries as Routing Destinations, see the [VistA Imaging DICOM Gateway Routing Setup and User Guide](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_routing_user_guide.pdf).
- This file also contains entries for the VistA Query/Retrieve application and the devices that use this application to retrieve studies from VistA. For details, see *Section 4.5.18* in the [*VistA Imaging* DICOM User Manual](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_dicomug.pdf) .

Despite its name, SCU_LIST.DIC contains entries for SCPs as well as SCUs. All information needed to initiate an association is stored in this file. This file is read by routine ^MAGDMB9 to (re)construct the FileMan table User Application (File 2006.585, stored in ^MAGDICOM (2006.585,…)). This should be done as part of the installation process, and whenever operational information has changed at the site.

Use the VistA Imaging DICOM Gateway menu to update this master file as follows:

4\. System Maintenance

à 2. Gateway Configuration and DICOM Master Files

à à 7. Update SCU_LIST.DIC

There are four kinds of records in SCU_LIST.DIC. The first is the “provider” record, which identifies a DICOM application. Following the provider record are one or more “service” records defining the services to be utilized. “Service” records may be followed by optional “transfer syntax” records. The last record is a “Role” record used only for query/retrieve. The Role record, unlike the other records, must be preceded by a tilde (~), if it is present, and will have one line for each role supported by the query/retrieve device.

· Provider Record: \<application name\> \| \<called AE title\> \| \<calling AE title\> \| \<destination IP address\> \| \<destination port number\>  
\[ \| \<PACS-type\> \]\[\| \<priority\> \|\] \<store\>

• Service Record: \<presentation context name\> \| \<transfer syntax name\>

• Transfer Syntax Record: \| \| \<transfer syntax name\>

• Role Record: ~\<service type\>\|\<user Y/N \>\|\<provider Y/N\>

The different fields are defined below:

\<application name\> The name that VistA uses to refer to the DICOM application.

\<called AE title\> The title of the called provider (SCP) application entity.

\<calling AE title\> The name of the VistA user (SCU) application entity.

\<destination IP address\> The network IP address of the provider (SCP) application entity.

\<destination port number\> The network port number for the provider (SCP application entity.

\<PACS-type\> Optional field that indicates the type of PACS system. Valid values are Null, “GE” or “KODAK”

\<priority\> Optional field that sets the priority. Any integer is valid. Defaults to 500 if no value is provided.

\<store\> Indicates if the device is a storage device. Valid values are “STORE” or Null.\<presentation context name\> The name of the DICOM service object pair (SOP).

\<transfer syntax name\> The name of the DICOM transfer syntax

~\<service type\> Query/retrieve only. The services supported by the query/retrieve device. Valid values are “C-Find”, “C-Move”, or “S-Store”

\<user Yes/No\> Query/retrieve only. Indicates if the device is a user of the named \<service type\>.

\<provider Yes/No\> Query/retrieve only. Indicates if the device is a provider of the named \<service type\>.

The following is an example of entries in SCU_LIST.DIC:

\# User Application List

\# Format:

\# line 1:App Name\|Called AE\|Calling AE\|Destination IP Address\|Socket\|Type\|priority\|store

\# line 2:\|Presentation Context Name\|Transfer Syntax Name

\# line 3:\|\|Transfer Syntax Name (if there are more than one)

\#

Local Modality Worklist\|VistA_Worklist\|VistA Testing\|LOCALHOST\|60010\|\|\|WORKLIST

\|Verification SOP Class\|Implicit VR Little Endian

\|Study Root Query/Retrieve Information Model - MOVE\|Implicit VR Little Endian

\#

A sample version of this file, named SCU_LIST.SAMPLE, is supplied with the VistA Imaging DICOM Gateway distribution, and may be edited by adding and/or deleting the pound sign (“#”). During an initial installation, this sample file is renamed to SCU_LIST.DIC.

When performing an update, the existing copy of this file will remain unaffected. Information from the sample file may be transferred to the operational master file at the discretion of the site.

The data from this file is stored in MUMPS in the following structure:

^MAG(2006.587,D0,0)= SERVICE NAME  
^MAG(2006.587,D0,1,0)=SERVICE TYPE  
^MAG(2006.587,D0,1,D1,0)= ""

After editing the contents of this file, it must be loaded onto the DICOM Gateway and into the VistA database using the VistA Imaging DICOM Gateway menu Update SCU_LIST.DIC as described earlier in this section.

> **NOTE:** In the \*.DIC files, leading and trailing spaces are ignored when the data is imported into the database. This makes it possible to align information for easier reading.

### B.4.6 WORKLIST.DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file WORKLIST.DIC contains the definitions of the various parameters that are needed for Modality Worklist processing by the instruments that are being used at the site. Menu Option 4.2.8, Update WORKLIST.DIC, reads this file to populate the Modality Worklist Dictionary file (#2006.583). This is done manually as part of the installation process, and whenever operational information has changed at the site.

After editing, use the VistA Imaging DICOM Gateway menu option to update this master file as follows:

4\. System Maintenance

à 2. Gateway Configuration and DICOM Master Files

à à 8. Update WORKLIST.DIC

The file WORKLIST.DIC is used in conjunction with the VistA Modality Worklist Service Class Provider. It maps the modality issuing the request to the corresponding site of image acquisition, image service, and image type. The record defining the modality is defined below:

\<calling AE Title\> \| \<institution name\> \| \<imaging service\> \| \<imaging type\> \| \<format options\> \| \<description\>

The different fields are defined below:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<tbody>
<tr class="odd">
<td>&lt;calling AE Title&gt;</td>
<td>The AE title of the modality; different units should use different AE titles.</td>
</tr>
<tr class="even">
<td>&lt;institution name&gt;</td>
<td>The name of the institution (as defined in 0.1 field of the INSTITUTION (#4) file. These names are processed in a case-insensitive fashion. Only the part of the name before the first comma needs to match the value in the institution file. Any other punctuation characters that occur in that part of the official name must appear in the value that is entered here. It also may be the site id or left null (the default is the site of the gateway).</td>
</tr>
<tr class="odd">
<td>&lt;imaging service&gt;</td>
<td><p>The name of the imaging service:</p>
<p>“<strong>RAD</strong>” for Radiology</p>
<p>“<strong>CON</strong>” for CPRS Consult/Procedure Request Tracking</p>
<p>“<strong>LAB</strong>” for Anatomic Pathology</p></td>
</tr>
<tr class="even">
<td>&lt;imaging type&gt;</td>
<td><p>The imaging type may have any of the following six formats:</p>
<ol type="1">
<li><p>For radiology, the abbreviation of the imaging type of the procedure, from the IMAGING TYPE file (#79.2)</p></li>
</ol>
<blockquote>
<p>(that is, RAD, NM, US, MRI, CT, ANI, CARD, VAS, or MAM)</p>
</blockquote>
<ol start="2" type="1">
<li><p>For consults or procedures, the abbreviation from IMAGE INDEX FOR SPECIALTY/SUBSPECIALTY file (#2005.84)</p></li>
<li><p>For consults or procedures, the abbreviation from IMAGE INDEX FOR SPECIALTY/SUBSPECIALTY file (#2005.84) followed by "/" and the abbreviation from IMAGE INDEX FOR PROCEDURE/EVENT file (#2005.85)</p></li>
<li><p>For consults or procedures, the abbreviation from IMAGE INDEX FOR SPECIALTY/SUBSPECIALTY file (#2005.84) followed by "/*" – this includes all of the worklists for the specialty</p></li>
<li><p>Anatomic pathology utilizes the abbreviation to get the internal ID, and then the subscript value. from the ACCESSION file (#68).</p></li>
<li><p>A comma delimited list of any of the above – this allows a modality to be used by differ services (for example an angiography suite that is shared between radiology and cardiology)</p></li>
</ol>
<p>Note: a prefix of "RAD:", "CON:", or "LAB:" can be used to specify an imaging type for a different imaging service.</p></td>
</tr>
<tr class="odd">
<td>&lt;format options&gt;</td>
<td><p>Format Options: Accession Number / SSN / Weight / Allergies / Reason</p>
<ul>
<li><p>Accession Number: Long or Short (case number) - Default = LONG</p></li>
<li><p>SSN: Dash or NoDash - Default DASH</p></li>
<li><p>Weight: Weight or NoWeight - Default WEIGHT</p></li>
<li><p>Allergies: Output in Allergies (0010,2110) or Medical Alerts</p></li>
</ul>
<blockquote>
<p>(0010,2000) - default both</p>
</blockquote>
<ul>
<li><p>Reason: Output reason for request in Requested Procedure Comments</p></li>
</ul>
<blockquote>
<p>(0040,1400) or Additional Patient History (0010,21B0) (send both is the default)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>&lt;description&gt;</td>
<td>A description that describes the equipment, and typically, also its location.</td>
</tr>
</tbody>
</table>

Examples of the WORKLIST.DIC file are shown below:

\# Examples:

\#

\# Radiology

\#PCU_QWL_SCU\|\<Your Institution goes here\>\|RAD\|RAD\|LONG\|Building E, Rm 225

CT_SCAN_1\|688\|RAD\|CT\|LONG\|Philips CT, Radiology East, Rm B-129

\#

\# Consults

IRIS-1\|\|CON\|OPHTH\|LONG\|Canon Retinal Camera, Eye Clinic, Rm, E-170

DENIX-2\|\|CON\|DENTAL\|LONG\|Intra-Oral Xray Unit, Rm, D-153

GI_LAB_SCU\|\<Your Institution goes here\>\|CON\|GI\|LONG\|North Clinic

\#

\# Anatomic Pathology

PATH\|\|LAB\|SP,CY\|L\|AP Surgical Path and Cytopath, but not Electron Microscopy

\#

\# Different Image Types

C1\|\|CON\|CARDIO\|L\|CARDIO alone

C2\|\|CON\|CARDIO/ECHO\|L\|CARDIO ECHO alone

C3\|\|CON\|CARDIO/CATH\|L\|CARDIO CATH alone

C4\|\|CON\|CARDIO/EKG\|L\|CARDIO EKG alone

C5\|\|CON\|CARDIO,CARDIO/CATH,CARDIO/ECHO\|L\|all CARDIO, but not EKG

C6\|\|CON\|CARDIO/\*\|L\|all CARDIO together including EKG

RC\|\|RAD\|RAD,CON:CARDIO,CON:OPHTH\|L\|RAD, CARDIO, and OPHTH

CR\|\|CON\|RAD:RAD,CARDIO/\*,OPHTH\|L\|RAD, CARDIO/\*, and OPHTH

\#

\# Allergy and Weight preferences

A1\|\|RAD\|RAD\|L////\|RAD with defaults for allergies, reason, and weight

A2\|\|RAD\|RAD\|L///a/\|RAD with allergies returned in Allergies (0010,2110)

A3\|\|RAD\|RAD\|L///M/\|RAD with allergies returned in Medical Alerts (0010,2000)

R1\|\|RAD\|RAD\|L////c\|RAD with reason in Requested Procedure Comment (0040,1400)

R2\|\|RAD\|RAD\|L////h\|RAD with reason in Additional Patient History (0010,21B0)

W1\|\|RAD\|RAD\|L//W//\|RAD with weight returned

W2\|\|RAD\|RAD\|L//N//\|RAD with weight set to null (NoWeight)

The file WORKLIST.DIC has to be edited for every new instrument using the VistA modality worklist service.

### B.4.7 Editing the Clinical Specialty DICOM & HL7 file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CLINICAL SPECIALTY DICOM & HL7 file is used for mapping CPRS Consult Request Tracking Consults and Procedures to DICOM Modality Worklist and to HL7 that is sent to clinical specialty PACS.

#### B.4.7.1 Displaying the CLINICAL SPECIALTY DICOM & HL7 file

The following example shows how to display the entries in the file. (The file used in these examples contains fictional data.)

Select OPTION NAME: MAGD DICOM MENU DICOM Menu Options

ECTP Edit CT PARAMETER File

ICTP Display MAGD CT PARAMETER entries

ECRP Edit CR PARAMETER File

ICRP Display MAGD CR PARAMETER entries

ECS Edit CLINICAL SPECIALTY DICOM & HL7 file

EXP Display DICOM OBJECT EXPORT file entries

CLN Correct Clinical Specialties DICOM File Entries

RAD Correct RAD-DICOM File Entries

Clean Up DICOM Gateway (Failed Images)

Clean Up Gateway (DICOM Destinations)

List Unread Studies

Print DICOM Failed Image File Entries

Rename DICOM Gateway (DICOM Destinations)

Rename DICOM Gateway (Failed Images)

Validate DICOM Correct Information

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select DICOM Menu Options \<TEST ACCOUNT\> Option: ecs Edit CLINICAL SPECIALTY DI

COM & HL7 file

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 3 Display the existing dictionary

DEVICE: HOME// HERE

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) -- 7/19/13@12:07 \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-- Consult --

Request Service: CARDIOLOGY

Worklist: CARDIO (CARDIOLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): CARDIOLOGY

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: GASTROENTEROLOGY

Worklist: GI (GASTROENTEROLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): GI CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: OPHTHALMOLOGY

Worklist: OPHTH (OPHTHALMOLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): OPHTHALMOLOGY OPHTHALMOLOGY-EYEPHOTOGRAPHY

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: DENTAL-OPT

Worklist: DENT (DENTISTRY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): DENTAL CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: DENTAL-INPT

Worklist: DENT (DENTISTRY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): DENTAL CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- End of File --

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option:

#### B.4.7.2 Adding a Consult to the CLINICAL SPECIALTY DICOM & HL7 file

In the following example, a general Pulmonary Consult is added to the file. This is a two-step process. First, the entry is added to this file. Second, the Stop Code is added using the *CONSULT ASSOCIATED STOP CODE* menu option. This associates the consult request with the clinic(s) where the patient is seen. This information is used when the appointment is made to provide DICOM Modality Worklist with scheduling information for the consult request.

#### B.4.7.2.1 Adding the Consult to the file

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 1 Consult

Enter the Request Service: PULMONARY

Enter the Imaging Specialty Index: PULMONARY

Enter the Imaging Procedure Index:

Enter the Acquisition Institution: 660

1 660 SALT LAKE CITY UT 660

2 660AA SALT LAKE DOM UT VAMC 660AA

CHOOSE 1-2: 1 SALT LAKE CITY UT 660

Enter the CPT Code:

Enter the HL7 (Optimized) Subscription List: MAG

1 MAGD ADT

2 MAGD DEFAULT

CHOOSE 1-2: 2 MAGD DEFAULT

Enter the Clinic \#1: PU

1 PULMONARY

2 PULMONARY CLINIC

CHOOSE 1-2: 2 PULMONARY CLINIC

Enter the Clinic \#2:

Request Service = PULMONARY

Procedure =

Specialty Index = PULMONARY -- PULM

Procedure Index =

Worklist = PULM (PULMONARY)

Acquired at = 660 -- SALT LAKE CITY

CPT Code =

HL7 Subscriber List = MAGD DEFAULT

Clinic = PULMONARY CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

Create this entry? n// YES -- entry created

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 4 Quit

Note that the Pulmonary Consult will appear on the Modality Worklist with the name PULM.

#### B.4.7.2.2 Add the Stop Codes(s)

Now use the *CONSULT ASSOCIATED STOP CODE* menu option to define a Stop Code(s) associated with the consult request.

Select OPTION NAME: CONSULTASSOCIATED STOP CODE SD ASSOCIATED STOP CODE CONSULT ASSOCIATED STOP CODE

CONSULT ASSOCIATED STOP CODE

Select REQUEST SERVICES SERVICE NAME: PULMONARY

Select ASSOCIATED STOP CODE: PU

1 PUBLIC HEALTH NURSING 122 10-01-2007

2 PULMONARY FUNCTION 104

3 PULMONARY/CHEST 312

CHOOSE 1-3: 2 PULMONARY FUNCTION 104

Are you adding 'PULMONARY FUNCTION' as

a new ASSOCIATED STOP CODE (the 1ST for this REQUEST SERVICES)? No// Y (Yes)

Select ASSOCIATED STOP CODE: PULMONARY FUNCTION 104

...OK? Yes// N (No)

PU

1 PUBLIC HEALTH NURSING 122 10-01-2007

2 PULMONARY/CHEST 312

CHOOSE 1-2: 2 PULMONARY/CHEST 312

Are you adding 'PULMONARY/CHEST' as

a new ASSOCIATED STOP CODE (the 2ND for this REQUEST SERVICES)? No// Y (Yes)

Select ASSOCIATED STOP CODE:

Select REQUEST SERVICES

#### B.4.7.2.3 Display the Consult with the Stop Code(s)

Now when the CLINICAL SPECIALTY DICOM & HL7 file is display, the Stop codes are shown.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 3 Display the existing dictionary

DEVICE: HOME// HERE

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) -- 7/19/13@12:44 \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-- Consult --

Request Service: CARDIOLOGY

Worklist: CARDIO (CARDIOLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): CARDIOLOGY

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: GASTROENTEROLOGY

Worklist: GI (GASTROENTEROLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): GI CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: OPHTHALMOLOGY

Worklist: OPHTH (OPHTHALMOLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): OPHTHALMOLOGY OPHTHALMOLOGY-EYEPHOTOGRAPHY

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: DENTAL-OPT

Worklist: DENT (DENTISTRY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): DENTAL CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: DENTAL-INPT

Worklist: DENT (DENTISTRY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): DENTAL CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: PULMONARY

Worklist: PULM (PULMONARY)

Acquired at: 660 -- SALT LAKE CITY

HL7 Subscriber List: MAGD DEFAULT

Clinic(s): PULMONARY CLINIC

Associated Stop Code: PULMONARY FUNCTION

Associated Stop Code: PULMONARY/CHEST

-- End of File --

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 4 Quit

#### B.4.7.3 Adding a Procedure to the CLINICAL SPECIALTY DICOM & HL7 file

In the following example, a Cardiology Electrocardiogram is added to the file. This is the same two-step process as adding a consult. First, the entry is added to this file. Second, the Stop Code is added using the *CONSULT ASSOCIATED STOP CODE* menu option.

#### B.4.7.3.1 Adding the Procedure to the file

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 2 Procedure

Enter the Procedure: ELECTRO

1 ELECTROCARDIOGRAM

2 ELECTROPHYSIOLOGY

CHOOSE 1-2: 1 ELECTROCARDIOGRAM

Request Service: CARDIOLOGY

Enter the Imaging Specialty Index: CARD

1 CARDIAC SURGERY

2 CARDIOLOGY

CHOOSE 1-2: 2 CARDIOLOGY

Enter the Imaging Procedure Index: EKG

Enter the Acquisition Institution: 660

1 660 SALT LAKE CITY UT 660

2 660AA SALT LAKE DOM UT VAMC 660AA

CHOOSE 1-2: 1 SALT LAKE CITY UT 660

CPT Code: 93005 -- ELECTROCARDIOGRAM TRACING

Change this value? n// NO

Enter the HL7 (Optimized) Subscription List: MAG

1 MAGD ADT

2 MAGD DEFAULT

CHOOSE 1-2: 2 MAGD DEFAULT

Enter the Clinic \#1: CARDIOLOGY IMAGPROVIDERFIVEEIGHT,FIVEEIGHT

Enter the Clinic \#2:

Request Service = CARDIOLOGY

Procedure = ELECTROCARDIOGRAM

Specialty Index = CARDIOLOGY -- CARDIO

Procedure Index = EKG -- EKG

Worklist = CARDIO/EKG (CARDIOLOGY/EKG)

Acquired at = 660 -- SALT LAKE CITY

CPT Code = 93005 -- ELECTROCARDIOGRAM TRACING

HL7 Subscriber List = MAGD DEFAULT

Clinic = CARDIOLOGY

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

Create this entry? n// YES -- entry created

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 4 Quit

Note that the Electrocardiogram procedure will appear on the Modality Worklist with the name CARD/EKG.

#### B.4.7.3.2 Add the Stop Codes(s)

Now use the *CONSULT ASSOCIATED STOP CODE* menu option to define a Stop Code(s) associated with the procedure request.

Select OPTION NAME: CONSULT ASSOCIATED STOP CODE SD ASSOCIATED STOP CODE CO

NSULT ASSOCIATED STOP CODE

CONSULT ASSOCIATED STOP CODE

Select REQUEST SERVICES SERVICE NAME: CARD

1 CARDIOLOGY

2 CARDIOLOGY CLINIC

CHOOSE 1-2: 1 CARDIOLOGY

Select ASSOCIATED STOP CODE: EKG 107

Are you adding 'EKG' as a new ASSOCIATED STOP CODE (the 1ST for this REQUEST S

ERVICES)? No// Y (Yes)

Select ASSOCIATED STOP CODE:

Select REQUEST SERVICES SERVICE NAME:

#### B.4.7.3.3 Display the Consult with the Stop Code(s)

Now when the CLINICAL SPECIALTY DICOM & HL7 file is display, the Stop codes are shown.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 3 Display the existing dictionary

DEVICE: HOME// HERE

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) -- 7/19/13@13:09 \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

-- Consult --

Request Service: CARDIOLOGY

Worklist: CARDIO (CARDIOLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): CARDIOLOGY

Associated Stop Code: EKG

-- Consult --

Request Service: GASTROENTEROLOGY

Worklist: GI (GASTROENTEROLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): GI CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: OPHTHALMOLOGY

Worklist: OPHTH (OPHTHALMOLOGY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): OPHTHALMOLOGY OPHTHALMOLOGY-EYEPHOTOGRAPHY

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: DENTAL-OPT

Worklist: DENT (DENTISTRY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): DENTAL CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: DENTAL-INPT

Worklist: DENT (DENTISTRY)

Acquired at: 660 -- SALT LAKE CITY

Clinic(s): DENTAL CLINIC

> **WARNING:** No Associated Stop Codes are defined for this Request Service.

Use CONSULT ASSOCIATED STOP CODE menu option to define them.

-- Consult --

Request Service: PULMONARY

Worklist: PULM (PULMONARY)

Acquired at: 660 -- SALT LAKE CITY

HL7 Subscriber List: MAGD DEFAULT

Clinic(s): PULMONARY CLINIC

Associated Stop Code: PULMONARY FUNCTION

Associated Stop Code: PULMONARY/CHEST

-- Procedure --

Request Service: CARDIOLOGY

Procedure: ELECTROCARDIOGRAM

Worklist: CARDIO/EKG (CARDIOLOGY/EKG)

Acquired at: 660 -- SALT LAKE CITY

CPT Code: 93005 -- ELECTROCARDIOGRAM TRACING

HL7 Subscriber List: MAGD DEFAULT

Clinic(s): CARDIOLOGY

Associated Stop Code: EKG

-- End of File --

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 4 Quit

#### B.4.7.4 Changing an entry in the CLINICAL SPECIALTY DICOM & HL7 file

In the following example, a procedure index (SCREENING AND SURVEILLANCE) is added to the Pulmonary Consult. This will change the name of the consult on the Modality Worklist from PULM to PULM/SCRNSURV.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 1 Consult

Enter the Request Service: PULMONARY

An entry for the PULMONARY consult

is already on file.

Request Service = PULMONARY

Procedure =

Specialty Index = PULMONARY -- PULM

Procedure Index =

Worklist = PULM (PULMONARY)

Acquired at = SALT LAKE CITY -- 660

CPT Code =

HL7 Subscriber List = MAGD DEFAULT

Clinic = PULMONARY CLINIC

Associated Stop Code = PULMONARY FUNCTION

Associated Stop Code = PULMONARY/CHEST

Change this entry? n// y YES

Delete the entire entry? n// NO -- entry not deleted

Imaging Specialty Index: PULMONARY -- PULM

Change this value? n// NO

Imaging Procedure Index:

Change this value? n// y YES

Enter the Imaging Procedure Index: scr

1 SCREENING

2 SCREENING (ACTIVE)

3 SCREENING AND SURVEILLANCE

CHOOSE 1-3: 3 SCREENING AND SURVEILLANCE

Acquisition Institution: SALT LAKE CITY -- 660

Change this value? n// NO

CPT Code:

Change this value? n// NO

HL7 (Optimized) Subscription List: MAGD DEFAULT

Change this value? n// NO

Clinic: PULMONARY CLINIC --------------- Remove this clinic? n// NO

Enter the Clinic \#2:

Request Service = PULMONARY

Procedure =

Specialty Index = PULMONARY -- PULM

Procedure Index = SCREENING AND SURVEILLANCE -- SCRNSURV

Worklist = PULM/SCRNSURV (PULMONARY/SCREENING AND SURVEILLANCE)

Acquired at = SALT LAKE CITY -- 660

CPT Code =

HL7 Subscriber List = MAGD DEFAULT

Clinic = PULMONARY CLINIC

Associated Stop Code = PULMONARY FUNCTION

Associated Stop Code = PULMONARY/CHEST

Update this entry? n// y YES

Entry Updated

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* \*\*\*

\*\*\* CLINICAL SPECIALTY DICOM & HL7 file (#2006.5831) Editor \*\*\*

\*\*\* \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Add/Edit a Consult or a Procedure?

Select one of the following:

1 Consult

2 Procedure

3 Display the existing dictionary

4 Quit

Enter an option: 4 Quit

Now the Pulmonary Consult will appear on the Modality Worklist with the name PULM/SCRNSURV.

> **NOTE:** If this change were to be made on a live system, those modalities that were previously mapped to PULM would need to be re-mapped to PULM/SCRNSURV. It might be necessary to map them to both PULM and PULM/SCRNSURV to be backward compatible with existing studies in the worklist and forward compatible with the new studies.

This is easily done by including both in the WORKLIST.DIC file as shown below:

\<AE Title\> \|\|PULM,PULM/SCRNSURV\|L\|mapped to both PULM and PULM/SCRNSURV

# Appendix C Networking Fundamentals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## C.1 Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TCP/IP inter-process (i.e., computer-to-computer) communications are performed between operating system endpoints called sockets. A socket is assigned a unique numeric port value (1-65535) when it is placed into use. Server applications allocate sockets and assign well-known port numbers when they start up. Client applications allocate sockets and access the server applications via the well-known port numbers.

Internet convention reserves port numbers 1-1023 for the system. The Secure Shell server application, for example, uses port number 22. Port numbers 1024-5000 are automatically assigned by the system, as needed, for things like handling client sessions. Port numbers above 5000 are available for user-developed services[^2] (e.g., VA Kernel Broker uses 9200).

DICOM applications require well-known port numbers. The port numbers for the VistA Imaging DICOM Gateway are assigned in a consistent dedicated fashion so that each application always uses the same port number, and different applications are always assigned different port numbers.

This allows applications to be moved between machines for redundancy and load balancing, without requiring the port numbers to be reconfigured. The VistA Imaging DICOM Gateway applications use port numbers in the range of 60000-61000 (see [Appendix E](#appendix-e-port-numbers-for-vista-imaging-dicom-gateway-applications)).

## C.2 IP Addresses and Subnet Masks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Internet Protocol (IP) addresses are defined for network interfaces. More than one address may be defined for an individual network interface, and a machine may have more than one network interface. If a machine has more than one network interface, the IP address for each of the interfaces must be assigned in different subnets.

IP addresses are 32 bits long and are represented in the format *aaa.bbb.ccc.ddd*, where *aaa*, *bbb*, *ccc*, and *ddd* are the first, second, third, and fourth octets (bytes) respectively.

Large organizations sub-divide their network namespace into logically independent *<u>subnets</u>*.

With the TCP/IP protocol suite, two machines can directly communicate with one another *<u>only if they have IP addresses that are in the same subnet</u>*. Otherwise, routers must be used to provide inter-subnet store and forward communications.

The *<u>subnet mask</u>* is used to partition the network namespace IP addresses into the different subnets.

The subnet mask is also 32 bits long and has the same *aaa.bbb.ccc.ddd* format as the IP address. By definition, the subnet mask consists of a string of high-order ONE bits followed by a string of low-order ZERO bits. The bits in the *aaa* octet of the subnet mask are usually set to ONE. The *bbb, ccc,* and *ddd* octets have a specific number of high-order ONE bits and low-order ZERO bits. The sequence of the ONE bits in the subnet mask define the subnet of the IP address. In a very frequently used combination in the VA, the *ccc* and *ddd* octets may have a string of nine high-order ONE bits followed by seven low-order ZERO bits. The resulting decimal sequence 255.255.255.128 (i.e., 11111111.11111111.11111111.10000000 in binary) is commonly referred to as a seven-bit subnet mask.

The selection of the subnet mask is a crucial configuration factor governing performance in the imaging network.

Two IP addresses are in the same subnet if two conditions are met:

- They have the same subnet mask.
- The logical AND of the subnet mask and each IP address are the same.

Routing imposes a network bottleneck for high-volume LAN applications like imaging. It is highly desirable, for performance reasons, to avoid routing imaging traffic, whenever possible. One way to accomplish this is to use a switched network topology and place all of the components (workstations, servers, etc.) in the same subnet. Another way is to have separate subnets, but to assign multiple IP addresses to the servers, one for each subnet.

### C.2.1 Example 1 – Original Configuration – Seven-bit Subnet Mask

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assume that machines A, B, C, and D are all on the same switched network. Machines A and B are file servers containing images, and machines C and D are imaging workstations.

Subnet Mask 255.255.255.128 (seven-bit subnet mask)

IP Address A 111.222.34.30

IP Address B 111.222.34.31

IP Address C 111.222.34.130

IP Address D 111.222.34.131

> **NOTE:** In all the examples in this document, dummy IP addresses starting with 111.222 are used (Please ignore the fact that 111.xxx.yyy.zzz is a Class A network address, while 152.xxx.yyy.zzz is a Class B one).

The subnet mask specifies that the upper three octets and the high order bit of the low order octet must be the same. The seven low order bits may be different.

There are 128 (2<sup>7</sup>) different IP address combinations in this subnet, of which 126 may be used (The lowest and highest addresses in the range are reserved).

In Example 1, there are two different subnets: 111.222.34.0 to 111.222.34.127 and 111.222.34.128 to 111.222.34.255. IP Addresses A and B are in one subnet (see Table C.1), while IP addresses C and D are in another subnet (see Table C.2).

IP Address “A” Logically ANDed with Subnet Mask

|                | Decimal Notation | Binary Notation                 |
|----------------|----------------------|-------------------------------------|
| IP Address “A” | 111.222.34.30        | 01101111.11011110.00100010.00011110 |
| Subnet Mask    | 255.255.255.128      | 11111111.11111111.11111111.10000000 |
| Logical AND    | 111.222.34.0         | 01101111.11011110.00100010.00000000 |

Table C.1IP Address “C” Logically ANDed with Subnet Mask

|                | Decimal Notation | Binary Notation                 |
|----------------|----------------------|-------------------------------------|
| IP Address “C” | 111.222.34.130       | 01101111.11011110.00100010.10000010 |
| Subnet Mask    | 255.255.255.128      | 11111111.11111111.11111111.10000000 |
| Logical AND    | 111.222.34.128       | 01101111.11011110.00100010.10000000 |

Table C.2

Machines A and B can communicate directly with each other, as can machines C and D, but machines A and B cannot directly communicate with machines C and D. A router is required in order for machines A & B to communicate with machines C & D.

Rather poor image retrieval performance is obtained in the Example 1 configuration because every byte of data transferred from the file servers (A & B) to the workstations (C & D) must pass through the router. As Example 2 will show, merely by changing the subnet mask by one bit can dramatically improve image transfer times.

### C.2.2 Example 2 – Change to Eight-bit Subnet Mask

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assume that machines A, B, C, and D are all on the same switched network. Machines A and B are file servers containing images, and machines C and D are imaging workstations.

Subnet Mask 255.255.255.0 (eight-bit subnet mask)

IP Address A 111.222.34.30

IP Address B 111.222.34.31

IP Address C 111.222.34.130

IP Address D 111.222.34.131

In Example 2, there is only one subnet: 111.222.34.0 to 111.222.34.255 with 254 usable IP addresses. Machines A, B, C, and D can directly communicate with each other without requiring a router.

There is a significant gain in performance for the imaging application between the first and the second configuration. The second configuration is much faster than the first because the images can be retrieved from the file servers directly, without having to be passed through a router.

### C.2.3 Example 3 – Keep Seven-Bit Subnet Mask and Add Secondary IP Address to Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another option is to keep the original nine-bit subnet masks and add secondary IP addresses to the servers.

Assume that machines A, B, C, and D are all on the same switched network. Machines A and B are file servers containing images, and machines C and D are imaging workstations.

Subnet Mask 255.255.255.128 (seven-bit subnet mask)

IP Address A 111.222.34.30, 111.222.34.250

IP Address B 111.222.34.31, 111.222.34.251

IP Address C 111.222.34.130

IP Address D 111.222.34.131

In Example 3, there are the two original subnets: 111.222.34.0 to 111.222.34.127 and 111.222.34.128 to 111.222.34.255. IP Addresses C and D are in one subnet, but IP addresses A and B are in both subnets. Machines A, B, C, and D can directly communicate with each other without requiring a router. Like Example 2, there is a similar significant gain in performance for the imaging application with this configuration.

For several years, the seven-bit subnet mask 255.255.255.128 was the recommended for the VA when the network topology consisted of several subnets connected by routers. With the new switched network topology consisting (ideally) of a <u>single subnet</u> containing several segments connected together by switches, other subnet mask values will be used.

The Telecommunications Support Office recommends using Variable Length Subnet Masks with a switched network topology in order to minimize the router load and maximize throughput. This means using different-sized subnet masks for different parts of the network IP address space.

To achieve optimal performance in a switched network topology, partition the IP address space and assign subnet masks to provide the largest possible subnets and minimize routing.

### C.2.4 Example 4 – Use Multiple Subnets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VAMC has been assigned the 111.222.29.1 to 111.222.32.126 range of IP addresses. All addresses outside this range are assigned to other facilities. The entire VAMC is wired with a 100 Base TX switched network infrastructure. What subnet masks should be used to provide the largest possible subnets?

The best solution is to use three subnets as follows:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 31%" />
<col style="width: 28%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>IP Address Range</strong></th>
<th><strong>Subnet Mask</strong></th>
<th><strong>Number of Addresses</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Subnet A</td>
<td>111.222.29.1 - 111.222.29.254</td>
<td><p>255.255.255.0</p>
<p>eight-bit subnet mask</p></td>
<td>254</td>
</tr>
<tr class="even">
<td>Subnet B</td>
<td>111.222.30.1 - 111.222.31.254</td>
<td><p>255.255.254.0</p>
<p>nine-bit subnet mask</p></td>
<td>510</td>
</tr>
<tr class="odd">
<td>Subnet C</td>
<td>111.222.32.1 - 111.222.32.126</td>
<td><p>255.255.255.128</p>
<p>seven-bit subnet mask</p></td>
<td>126</td>
</tr>
</tbody>
</table>

Note how the values of the IP addresses affect the way that the subnets can be constructed. The high-order bits of the IP address ANDed with the subnet mask must be the same for the entire subnet. IP addresses 111.222.30.\* and 111.222.31.\* can be placed into the same subnet using the nine-bit mask because the value of the ANDs are both 111.222.30.0. Note, however, that IP addresses 111.222.29.\* and 111.222.30.\* cannot be placed into the same subnet using the nine-bit mask, because the value for the ANDs are different, 111.222.28.0 and 111.222.30.0 respectively.

Subnet A can accommodate the imaging application with up to 250 workstations with no need for routing. An application with more workstations (like office automation) might be placed in Subnet B. Miscellaneous applications can be placed in Subnet C.

If the seven-bit subnet mask were used instead of the variable length subnet mask scheme, there would be seven subnets with 126 addresses in each. The image file servers could then have multiple IP addresses, one in each subnet to avoid much of the routing. Otherwise, considerably more routing would be required.

Another site has used subnet mask 255.255.128.0 (allowing 32,766 addresses) so that all the devices in the facility are on the same subnet. It is also possible to use a VISN-wide Class A private network address scheme with a subnet mask 255.0.0.0 and IP addresses like 10.130.xxx.yyy.

> **NOTE:** The site then may need to provide an IP address conversion capability so that ~~Silver Spring can access~~ the gateway can be accessed remotely.

<u>Warning</u>: Changes to the subnets need to be reflected in the routers and the other systems on the network.

For further information, contact your CIO Network Group and the network vendor specialists.

## C.3 Default Gateways

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Default Gateway is typically a port on a router that is used to transfer traffic between subnets. The default gateway port IP address must be in the same subnet as the IP address of the network interface. Typically, the bottom or top address in a subnet is used as the IP address for the default gateway. In this example, the default gateway IP address might be 111.222.34.1 or 111.222.34.126 for IP addresses A and B, and 111.222.34.129 or 111.222.34.254 for IP addresses C and D.

It is possible to set the default gateway IP address incorrectly and still get routing to occur. Some routers have an automatic address resolution option, which, if enabled, will automatically resolve IP addresses and perform routing, in spite of the possibility that the default gateway IP address is incorrect. This feature may tend to hide IP address problems and may promote bad networking practices.

The IP addresses on a Windows workstation are set by mouse clicking on Start, picking Settings, and selecting Control Panel. Clicking on the Network icon on the Control Panel window brings up the Network window. Selecting the Protocols tab brings up a list of the installed network protocols. Selecting the TCP/IP Protocol and the Properties button brings up the Microsoft TCP/IP Properties window. Select the adapter and enter the IP address, subnet mask, and default gateway. The system may have to be rebooted afterwards.

The Advanced button brings up the Advanced IP Addressing window that allows the entry of the additional IP addresses. The IP addresses can be in either the same subnet or in different subnets. This is very useful for connecting servers to multiple subnets. It is also useful in the event of a system failure for redirecting communications to an operational VistA DICOM machine.

For imaging workstations, the IP address, subnet mask, default gateway, and other parameters, such as DNS addresses, can be left blank and be assigned at run time using the Dynamic Host Configuration Protocol (DHCP). This should not be used for VistA Imaging DICOM Gateways, however, as permanent (i.e., hard-coded) IP addresses are usually required for communications by the commercial DICOM equipment.

## C.4 HOSTS File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HOSTS file maps IP addresses to aliases. Aliases are mnemonics, memory aids that can serve multiple purposes. It is very useful to place entries for all the commercial DICOM equipment into the HOSTS file of the VistA Imaging DICOM Gateway.

Using aliases makes it much easier to access the other systems. The aliases can be used in commands in place of the numeric IP addresses. If it is necessary to change the IP address of the commercial DICOM equipment, it can be changed in the HOSTS file while keeping the same familiar alias.

Service providers can use the information in the HOSTS file in a reverse fashion, to lookup incoming client IP addresses and display the corresponding alias.

<u>Example of HOSTS file:</u>

\# VAMC DICOM Image Producing Modalities

111.222.35.30 CT1 \# Picker CT PQ-2000 \#1

111.222.35.31 CT2 \# Picker CT PQ-2000 \#2

111.222.35.32 CT3 \# GEMS High Speed Advantax CT

The HOSTS file is not limited to IP addresses of other systems, however. Aliases can also point to the current system (using the IP address 127.0.0.1) and form a local loopback.

A new IRIS TERMINAL session needs to be created for each alias in order for it to be displayed in the title bar while it is running.

> **NOTE:** The alias can also contain the menu prompt numbers, making it easier to start the process).

<u>Example of HOSTS file:</u>

\# local host telnet connections for the VistA DICOM PACS Interface

\# VistA DICOM Text Gateway

127.0.0.1 TEXT_INTERFACE_1_1 \# HIS to DICOM Test Interface

127.0.0.1 EMED_PACS_1_2_1 \# EMED PACS Communications

127.0.0.1 MITRA_BROKER_1_2_2 \# MITRA / FUJI Communications

# Appendix D Diagnostic Networking Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## D.1 HOSTDIR.BAT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The full path to the HOSTS file is several directories deep and is system dependent (e.g., c:\Windows\system32\drivers\etc\hosts). Rather than trying to remember which path to use for which system and typing in the whole thing every time, use the following script:

cd %SystemRoot%\system32\drivers\etc

This takes you to the directory containing the HOSTS file. The script is stored in the file c:\Program Files(x86)\VistA\Imaging\DICOM\hostdir.bat. The installation procedure ensures that this directory will be included in the path, so that this command file can be started by simply typing “hostdir”.

## D.2 IPCONFIG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current system’s IP address, subnet masks, and default gateways can be conveniently displayed with the IPCONFIG command, as shown below:

c:\\ipconfig

Windows IP Configuration

Ethernet adapter DC21X42:

IP Address. . . . . . . . . : 222.111.36.162

Subnet Mask . . . . . . . . : 255.255.255.192

Default Gateway . . . . . . : 222.111.36.190

Ethernet adapter DC21X41:

IP Address. . . . . . . . . : 111.222.36.39

Subnet Mask . . . . . . . . : 255.255.255.128

IP Address. . . . . . . . . : 111.222.36.40

Subnet Mask . . . . . . . . : 255.255.255.128

Default Gateway . . . . . . : 111.222.36.122

Note that the second network interface has two different IP addresses assigned to it. This illustrates how one VistA Imaging DICOM Gateway can be configured to subsume the tasks of another, in the event of a system failure. In this example, the system with IP address 111.222.36.40 was taken out of service and all of its tasks were given to the system with IP address 111.222.36.39. The DICOM applications that had run on the old system now run on the new system without any changes to the commercial DICOM system’s configuration files.

Multiple IP addresses can also be used in a switched network to span multiple subnets. These additional IP address can be defined by selecting the Advanced button of the Microsoft TCP/IP Properties window (see Section [C.2.3](#c.2.3-example-3-keep-seven-bit-subnet-mask-and-add-secondary-ip-address-to-servers) above).

## D.3 PING

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Probably the most useful command for network troubleshooting is PING which, like the navy destroyers of old, listens for an echo response from its target destination. The pinging of FORUM, the VA email system, is shown below:

c:\\ping forum

Pinging FORUM \[nnn.nnn.nn.nn\] with 32 bytes of data:

Reply from nnn.nnn.nn.nn: bytes=32 time\<10ms TTL=254

Reply from nnn.nnn.nn.nn: bytes=32 time\<10ms TTL=254

Reply from nnn.nnn.nn.nn: bytes=32 time\<10ms TTL=254

Reply from nnn.nnn.nn.nn: bytes=32 time\<10ms TTL=254

or

Request timed out.

Request timed out.

Request timed out.

Request timed out.

The above example shows the results of one successful and one unsuccessful PING. The PING protocol uses “impc” request and response packets. Four “impc requests” were issued by PING and four (or zero) “impc responses” were received.

A system should <u>always</u> be able to ping its default gateway. A good initial test for physical network integrity is to try to ping the system’s default gateway.

> **NOTE:** While most DICOM devices support PING in both directions, at least one commercial DICOM image acquisition device (the GE Digital Radiofluoro DRS 3.1) simulates a phony PING function by attempting to establish an FTP session with the destination system. This does not work with the VistA DICOM system, since Windows Professional workstation does not normally provide an FTP server.

## D.4 TRACERT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to PING, Windows Professional supports TRACERT (trace route) to explicitly display the full route that is used to communicate with the target system. This tool presents many more diagnostic details. The route to Forum is shown below:

c:\\tracert forum

Tracing route to FORUM \[nnn.nnn.nn.nn\]

over a maximum of 30 hops:

1 \<10 ms \<10 ms \<10 ms 111.222.38.122

2 \<10 ms \<10 ms \<10 ms FORUM \[nnn.nnn.nn.nn\]

Trace complete.

In the above example, the host system nnn.nnn.nn.nn used its default gateway nnn.nnn.nn.nn to hop first to the gateway nnn.nnn.nn.nn and then to FORUM nnn.nnn.nn.nn.

## D.5 NETSTAT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NETSTAT displays protocol statistics and current TCP/IP network connections. The telnet, NetBIOS, and DICOM sessions are displayed by NETSTAT, as shown in the following example:

C:\\netstat

Active Connections

Proto Local Address Foreign Address State

TCP isw-xxx:60000 localhost:1091 ESTABLISHED

TCP isw-xxx:60120 localhost:1096 ESTABLISHED

TCP isw-xxx:1091 localhost:60000 ESTABLISHED

TCP isw-xxx:1096 localhost:60120 ESTABLISHED

TCP isw-xxx:1070 VHAISWXX2:nbsession ESTABLISHED

TCP isw-xxx:1073 VHAISWXX1:nbsession ESTABLISHED

TCP isw-xxx:22 localhost:60743 ESTABLISHED

In this example, ports 1070 and 1073 are used for NetBIOS sessions, and the other ports were used for DICOM. Port 60000 and 60120 were used for the VistA DICOM application, while ports 1091 and 1096 were assigned by the system for DICOM clients.

## D.6 DICOM_Echo

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The DICOM_Echo utility is part of our normal distribution and is located in the c:\Program Files(x86)\VistA\Imaging\DICOM directory.

C-ECHO is a DICOM service that is used to verify communications to a remote DICOM application entity (AE). A Verification SOP Class user can send a C-ECHO request to another DICOM AE. If the remote AE is a Verification SOP Class provider, it will return a C-ECHO response back to the original requesting AE. This function is analogous to a DICOM application-level PING.

DICOM_Echo is a public domain utility written by the Mallinckrodt Institute of Radiology that sends a C-ECHO request to a remote DICOM AE, and then waits for a response.

<u>To View HELP:</u>

C:\User\>dicom_echo

dicom_echo \[-a title\] \[-d\] \[-c title\] \[-m mode\] \[-n num\] \[-p\] \[-r repeat\] \[-s sleeptime\] \[-v\] \[-x\] node port

a Application title of this application

c Called AP title to use during Association setup

d Drop Association after echo requests

m Mode for SCU/SCP negotiation (SCU, SCP, SCUSCP)

n Number of network connections

p Dump service parameters after Association Request

r Number of times to repeat echo request

s Time to sleep after each echo request

v Verbose mode for DUL/SRV facilities

x Do not release Associations when finished with echo

node Node name of server

port Port number of server

<u>Actual Usage:</u>

C:\User\>dicom_echo 111.222.36.38 60120

Echo context: Context

Verification Response

Message ID Responded to: 1

Verification Status: 0000

Echo Response

Message ID Responded To: 1

Data Set Type: 0101

Status: 0000 Status Information:-

Successful operation

Class UID: 1.2.840.10008.1.1

## D.7 Send_Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Send_Image utility is part of our normal distribution and is located in the c:\Program Files\VistA\Imaging\DICOM directory.

C-STORE is the DICOM service that is used to transfer an image (i.e., a composite object) to a remote DICOM application entity. A Storage SOP Class user can send a C-STORE request to another DICOM destination. If the remote DICOM destination is a corresponding Storage SOP Class provider, it will accept the association and await image transfer. The Storage SOP Class user can then transfer one or more images to the Storage SOP Class provider. After the images are sent, it closes the association.

Send_Image is a public domain utility written by the Mallinckrodt Institute of Radiology to issue a C-STORE request and send one or more images to a remote DICOM Storage SOP Class provider.

<u>To View HELP:</u>

C:\User\>send_image

send_image \[-a application\] \[-c called\] \[-m maxPDU\] \[-p\] \[-q\] \[-r\]  
\[-s SOPName\]\[-t\] \[-x FAC\] \[-X xfer\] \[-v\] \[-w flag\] \[-Z\] node port image \[image...\]

-a Set application title of this (calling) application

-c Set called AE title to title in Association RQ

-m Set maximum PDU in Association RQ to maxPDU

-p Alter image by sending minimal pixel data

-q Quiet mode. Suppresses some messages to stdout

-r Make program sensitive to response status. If not success, stop

-s Force an initial Association using one SOP Class based on SOPName

(CR, CT, MR, NM, SC, US)

-t Time the image transfer. Print elapsed time and transfer rate.

-v Place DUL and SRV facilities in verbose mode

-x Place one facility(DCM, DUL, SRV) in verbose mode

-X Specify a transfer syntax to be proposed; may repeat this switch

-w Set open options; flag can be REPEAT

-Z Allow VR mismatch in input files

node Node name for network connection

port TCP / IP port number of server application

image A list of one or more images to send

<u>Actual Usage:</u>

C:\User\>send_image -q cemax30 104 a0000001.dcm a0000002.dcm a0000003.dcm

Store Response

Message ID Resp:1

Data Set Type: 0101

Status: 0000 Status Information:-

Successful operation

Class UID: 1.2.840.10008.5.1.4.1.1.2

Instance UID: 1.2.840.113619.2.1.11101.786458237.2.11.858271581

Store Response

Message ID Resp:2

Data Set Type: 0101

Status: 0000 Status Information:-

Successful operation

Class UID: 1.2.840.10008.5.1.4.1.1.2

Instance UID: 1.2.840.113619.2.1.11101.786458237.2.11.858271582

Store Response

Message ID Resp:3

Data Set Type: 0101

Status: 0000 Status Information:-

Successful operation

Class UID: 1.2.840.10008.5.1.4.1.1.2

# Appendix E Port Numbers for VistA Imaging DICOM Gateway Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Attention</u>: For inter-process communications, DICOM applications require well-known port numbers[^3].

The VistA Imaging DICOM Gateway uses port numbers in the 60000-61000 range, in order to avoid conflicting with those used by other applications.

> **NOTE:** 104 is commonly used as the default port number for DICOM.

The following table contains suggested port numbers for the VistA DICOM Applications.

| VistAImaging DICOM Gateway Application | Port Number |
|-------------------------------------------------|-----------------|
| Commercial Modality Worklist SCP \#1            | 60041           |
| Commercial Modality Worklist SCP \#2            | 60042           |
| Commercial PACS Text Interface                  | 60040           |
| CR Modality – Image Storage                     | 60100 – 60109   |
| CT Modality – Image Storage                     | 60120 – 60129   |
| Default – Image Storage                         | 104             |
| Dental – Image Storage                          | 60200 – 60299   |
| Digital Angiography – Image Storage             | 60150 – 60159   |
| Digital Radio Fluoro – Image Storage            | 60140 – 60149   |
| Digital Radiography – Image Storage             | 60110 – 60119   |
| Film Digitizer – Image Storage                  | 60190 – 60199   |
| Image acquisition MUMPS storage controller      | 60000           |
| Modality Worklist SCP                           | 60010           |
| MR Modality – Image Storage                     | 60130 – 60139   |
| Nuclear Medicine – Image Storage                | 60170 – 60179   |
| Ophthalmology – Image Storage                   | 60300 – 60399   |
| Performed Procedure Step SCP                    | 60020           |
| Query/Retrieve SCP                              | 60090           |
| Storage Commitment SCP                          | 60030           |
| Ultrasound – Image Storage                      | 60160 – 60169   |
| Visible Light – Image Storage                   | 60180 – 60189   |

# Appendix F VistA Imaging DICOM Gateway Application Entity (AE) Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DICOM requires the calling application entity to supply both its AE title and the called AE title when the association request is made. The AE titles for the VistA Gateway processes are listed in the following table (These values are defined in the master file named SCP_LIST.DIC).

| VistAImaging DICOM Gateway Process | Application Entity Title |
|---------------------------------------------|------------------------------|
| PACS Text Interface                         | VISTA_PACS_IF                |
| Query/Retrieve Provider                     | VISTA_QR_SCP                 |
| Query/Retrieve User                         | VistA_QR_SCU                 |
| Modality Worklist                           | VistA_Worklist               |
| Image Storage                               | VistA_Storage                |
| Image Import                                | VISTA_SEND_IMAGE             |

# Appendix G Setting Up the MUMPS-to-MUMPS Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the [M-to-M Broker Kernel Documentation](https://www.va.gov/vdl/documents/Infrastructure/M_to_M_Broker/xwb1_1p34sp.pdf).

# Appendix H Change IRIS Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the password for the IA account is changed, the details that are saved also needs to be updated on IRIS service.

1.  Open the ‘InterSystems IRIS Controller for IRIS’ from Windows - Services

> ![](vista-imaging-dicom-gateway-installation-guide/076.png)

2.  Right click – Properties, select the ‘Log On’ tab. The update the password and Apply/OK.

> Make sure to Stop and restart the IRIS service to ensure the new password is valid.

> ![](vista-imaging-dicom-gateway-installation-guide/077.png)

# Appendix I KIDS Package to Install in the VistA System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the installation of the “KIDS” package that is to be installed into a VistA system to support the VistA Imaging DICOM Gateway that will be running on satellite SERVERs. The complete KIDS installation is detailed in the VistA Imaging Installation Guide or Patch Description. Specific details pertinent to the DICOM Gateway are covered here.

The name of the KIDS package will be in the VistA Imaging namespace (“MAG”). Review the [VistA Imaging Installation Guide](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGinstallgd.pdf) or an example of the KIDS installation.

Installation of the KIDS package “VistA Imaging” is required to establish the files needed for DICOM image acquisition and for DICOM Text Gateway. It establishes the global variable (^MAGDHL7) used for providing information to an outside PACS vendor and for providing a modality worklist to a radiology instrument. Data dictionaries and menu options are also created to assist in manual correction of images that failed to be processed during the initial image download for the Radiology and Consult modalities.

The following sections describe those parts of the KIDS installation on the VistA system that pertain to the operation of the DICOM Gateway.

## I.1 VistA -PACS Radiology Interface Setup Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps are required to establish the global variable (^MAGDHL7) used for providing radiology order information to an outside PACS vendor and for providing a modality worklist to radiology devices. These steps are performed on the VistA system using FileMan utility. Apply one-step at a time to allow testing changes and tracking errors before applying all changes. It is imperative that you follow the instructions precisely -- especially if you are not installing in a test account.

1.  Use FileMan Enter/Edit to edit file 771 (HL7 APPLICATION PARAMETER) and update the FACILITY NAME field for the following entries RA-CLIENT-IMG, RA-SERVER-IMG and MAGD-CLIENT. Also, ensure that the ACTIVE\INACTIVE field is set to active for entries RA-SERVER-IMG, MAGD-CLIENT, MAG COMRCL PACS and MAG VISTA IMGNG.
2.  Follow the instructions in sections [Change Subscribers](#_Change_Subscribers) and [Entering Facility Names for Sending/Receiving Applications for PACS Messaging](#_Entering_Facility_Names) to subscribe to the appropriate HL7 Radiology event drivers (either V2.1 or V2.4) and associate the appropriate facility name with Imaging’s PACS protocols.
3.  Activate the triggering of HL7 messages during Radiology exam registration by entering RA-SERVER-IMG into the SENDING APPLICATION field of the RA REG 2.4 protocol entry.

Select OPTION: EN \<Enter\>TER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: ACCESSION// 101 \<Enter\> PROTOCOL (1710 entries)

EDIT WHICH FIELD: ALL// SENDING APPLICATION \<Enter\>

THEN EDIT FIELD:

Select PROTOCOL NAME: RA REG 2.4 \<Enter\> Rad/Nuc Med exam registered

SENDING APPLICATION: RA-SERVER-IMG \<Enter\>

Once this step is complete, entries should start populating file 772 and file 2006.5 (global variable ^MAGDHL7). You can test by using the Radiology options to register an exam. For each exam case registered, an entry will be set in file 2006.5.

4.  Select the EXAMINATION STATUS for each Imaging type that should trigger the “examined” HL7 message. The HL7 will only be triggered once for an exam – when the exam has been upgraded to the status with the GENERATE EXAMINED HL7 MESSAGE field set to Yes. (Examination Status file \#72).

Example:

\>D P^DII \<Enter\>

VA FileMan 22.0

Select OPTION: ENT \<Enter\>ER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PROTOCOL// 72 \<Enter\> EXAMINATION STATUS

(55 entries)

EDIT WHICH FIELD: ALL// 8 \<Enter\> GENERATE EXAMINED HL7 MESSAGE

THEN EDIT FIELD: \<Enter\>

Select EXAMINATION STATUS: EXAMINED \<Enter\>

1 EXAMINED GENERAL RADIOLOGY

2 EXAMINED ULTRASOUND

3 EXAMINED MAGNETIC RESONANCE IMAGING

4 EXAMINED NUCLEAR MEDICINE

5 EXAMINED CARDIOLOGY STUDIES (NUC MED)

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 \<Enter\> EXAMINED GENERAL RADIOLOGY

GENERATE EXAMINED HL7 MESSAGE: YES// \<Enter\>

5.  Follow step 3 and apply to protocol RA EXAMINED 2.4 instead of RA REG 2.4.

Select OPTION: EN \<Enter\>TER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 101 \<Enter\> PROTOCOL

EDIT WHICH FIELD: SENDING APPLICATION \<Enter\>

Select PROTOCOL NAME: RA EXAMINED 2.4 \<Enter\>

SENDING APPLICATION: RA-SERVER-IMG \<Enter\>

Once this step is complete, entries should start populating file 772 and file 2006.5 (^MAGDHL7 global). You can test by using the Radiology options to edit an exam. For each exam case edited that is upgraded to the status with the GENERATE EXAMINED HL7 MESSAGE field set to yes, an entry will be set in file 2006.5 (Usually this is done for all cases that have been upgraded to examined).

6.  Apply the step outlined for steps3 for the RA CANCEL 2.4 protocol.

INPUT TO WHAT FILE: 101 \<Enter\> PROTOCOL

EDIT WHICH FIELD: SENDING APPLICATION \<Enter\>

Select PROTOCOL NAME: RA CANCEL 2.4 \<Enter\>

SENDING APPLICATION: RA-SERVER-IMG \<Enter\>

Use the Radiology option to cancel a radiology case. An entry for each canceled case should be entered into files 772 & 2006.5.

7.  Apply step 3 for the RA RPT 2.4 protocol.

INPUT TO WHAT FILE: 101 \<Enter\> PROTOCOL

EDIT WHICH FIELD: SENDING APPLICATION \<Enter\>

Select PROTOCOL NAME: RA RPT 2.4 \<Enter\>

SENDING APPLICATION: RA-SERVER-IMG \<Enter\>

Use the Radiology option to produce a verified report. Only verified reports will create entries in files 772 and 2006.5.

> **REMINDER:** If any errors occur, the DHCP-PACS Radiology interface can be stopped by taking the following steps:

- Removing the SENDING APPLICATION and SUBSCRIBERS entries from the protocol causing the error.
- Log a support ticket or contact the VA support group. Include a copy of the error trap with the ticket.

## I.2 VistA -PACS ADT Interface Setup Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This section is relevant for sites interfacing to a Commercial PACS system.

The following are the instructions for establishing the interface to provide a mechanism for notifying the PACS system regarding changes in ADT events.

1.  Use FileMan to set the field PACS INTERFACE SWITCH to ON in the IMAGING SITE PARAMETERS file (#2006.1).

\> Do P^DII \<Enter\>

VA FileMan 22.0

Select OPTION: EN \<Enter\> TER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: IMAGING SITE PARAMETERS// 2006.1 \<Enter\>

IMAGING SITE PARAMETER (1 entry)

EDIT WHICH FIELD: ALL// PACS INTERFACE SWITCH \<Enter\>

THEN EDIT FIELD: \<Enter\>

Select IMAGING SITE PARAMETERS NAME: yoursite name \<Enter\>

PACS INTERFACE SWITCH: 1 \<Enter\> ON PACS INTERFACE

Select IMAGING SITE PARAMETERS NAME: \<Enter\>

Select OPTION: \<Enter\>

\>

2.  Routine ^MAGDHLE invokes INIT^HLTRANS which checks for the existence of “PACS GATEWAY” entry in the NON-DHCP APPLICATION PARAMETER file (#770).

First, the following entry needs to be established in the HL7 APPLICATION PARAMETER file (#771):

> NAME: PACGATEWAY

> ACTIVE/INACTIVE: ACTIVE

Then the following entry must be created in the NON-DHCP APPLICATION PARAMETER file (#770):

> NAME: PACSGATEWAY

> NON-DHCP FACILITY NAME: *your facility name*

> DHCP STATION NUMBER: *your facility number*

> DHCP APPLICATION: PAC GATEWAY \<\<Pointer to file 771.

Then the entry for PAC GATEWAY entry in file 771 can be renamed to PACS GATEWAY.

Use FileMan to perform this set-up:

\> Do P^DII\<Enter\>

VA FileMan 22.0

Select OPTION: en \<Enter\> TER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 771 \<Enter\> HL7 APPLICATION PARAMETER (139 entries)

EDIT WHICH FIELD: ALL// \<Enter\>

Select HL7 APPLICATION PARAMETER NAME: PAC GATEWAY \<Enter\>

Are you adding 'PAC GATEWAY' as

a new HL7 APPLICATION PARAMETER (the 140TH)? No// Y \<Enter\> (Yes)

ACTIVE/INACTIVE: AC \<Enter\> ACTIVE

FACILITY NAME: ^ \<Enter\>

Select HL7 APPLICATION PARAMETER NAME: \<Enter\>

Select OPTION: en \<Enter\> TER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: HL7 APPLICATION PARAMETER// 770 \<Enter\>

HL7 NON-DHCP APPLICATION PARAMETER (2 entries)

EDIT WHICH FIELD: ALL// \<Enter\>

Select HL7 NON-DHCP APPLICATION PARAMETER NAME: PACS GATEWAY \<Enter\>

Are you adding 'PACS GATEWAY' as

a new HL7 NON-DHCP APPLICATION PARAMETER (the 3RD)? No// Y \<Enter\> (Yes)

HL7 NON-DHCP APPLICATION PARAMETER DHCP STATION NUMBER: \<*your station number*\> \<Enter\>

HL7 NON-DHCP APPLICATION PARAMETER NON-DHCP FACILITY NAME: \<*your facility name*\> \<Enter\>

HL7 NON-DHCP APPLICATION PARAMETER DHCP APPLICATION: PAC GATEWAY \<Enter\> ACTIVE

DHCP STATION NUMBER: \<*your facility number*\> // \<Enter\>

NON-DHCP FACILITY NAME: \<*your facility name*\> // \<Enter\>

MAXIMUM BLOCK SIZE: ^ \<Enter\>

Select HL7 NON-DHCP APPLICATION PARAMETER NAME: \<Enter\>

Select OPTION: en \<Enter\> TER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: HL7 NON-DHCP APPLICATION PARAMETER// 771 \<Enter\>

HL7 APPLICATION PARAMETER (140 entries)

EDIT WHICH FIELD: ALL// .01 \<Enter\> NAME

THEN EDIT FIELD: \<Enter\>

Select HL7 APPLICATION PARAMETER NAME: PAC GATEWAY \<Enter\> ACTIVE

NAME: PAC GATEWAY// PACS GATEWAY \<Enter\>

Select HL7 APPLICATION PARAMETER NAME: \<Enter\>

Select OPTION: \<Enter\>

3.  The ADT changes are trigged by a protocol running off the MAS Event driver. You must add the MAGD DHCP-PACS ADT EVENTS protocol to the DGPM Movements Events protocol.

\> Do P^DII \<Enter\>

VA Fileman 22.0

Select OPTION: en \<Enter\> TER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: IMAGING WORKSTATIONS// 101 \<Enter\> PROTOCOL

EDIT WHICH FIELD: ALL// ITEM \<Enter\>

1 ITEM (multiple)

2 ITEM TEXT

CHOOSE 1-2: 1 \<Enter\>

EDIT WHICH ITEM SUB-FIELD: ALL// \<Enter\>

THEN EDIT FIELD: \<Enter\>

Select PROTOCOL NAME: DGPM MOVEMENT EVENTS \<Enter\>

Select ITEM: IB CATEGORY C BILLING// MAGD DHCP-PACS ADT EVENTS \<Enter\>

NOTIFICATION DHCP-PACS ADT EVENT

MNEMONIC: ^ \<Enter\>

Select PROTOCOL NAME: \<Enter\>

Select OPTION: \<Enter\>

This completes the creation of the items necessary for the PACS ADT interface. Use the PIMMS option to Admit, Transfer and Discharge a patient to test the cross-reference setting. During the update processing, on any of these three transactions, the system will spawn off a background task that will execute the cross-reference routine and display the following on the screen:

\*\*\* HL7 TASK FOR PACS \*\*\*

If successful, the HL7 messages for the events will be recorded in the PACS MESSAGES file (#2006.5).

## I.3 Change Subscribers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As referenced from Section 5.1, use the instructions in this section to update subscribe the HL7 Radiology Imaging Subscriber Protocols to the Radiology version 2.4 event driver protocols. (As explained in the NOTE in the screen dialog box, these instructions could also be used to subscribe to the Radiology version 2.1 event driver protocols if for some reason it were deemed necessary not to use HL7 2.4.)

1.  Use the Imaging System Manager (MAG SYS MENU) setup options. Type the bolded responses.

DVA\>D ^XUP

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT320 48 LINE

Select OPTION NAME: MAG SYS MENU Imaging System Manager Menu

HL7 Imaging HL7 Messaging Maintenance ...

IX Image Index Conversion Menu ...

LS Edit Network Location STATUS

TR Telereader Menu ...

Ad hoc Enterprise Site Report

Delete Image Group

Enter/edit Reason

Imaging Database Integrity Checker Menu ...

Imaging Site Reports ...

Select Imaging System Manager Menu Option: HL7 Imaging HL7 Messaging Maintenance

RHL7 Maintain Subscriptions to Radiology HL7 Drivers

IHE Configure IHE-Based HL7 Interface to PACS

Select Imaging HL7 Messaging Maintenance Option: RHL7 Maintain Subscriptions to

Radiology HL7 Drivers

MAGD SEND ORM protocol found...

MAGD SEND ORU protocol found...

RA CANCEL protocol found...

RA EXAMINED protocol found...

RA REG protocol found...

RA RPT protocol found...

RA CANCEL 2.4 protocol found...

RA EXAMINED 2.4 protocol found...

RA REG 2.4 protocol found...

RA RPT 2.4 protocol found...

Enter the desired version of HL7: 2.4 HL7 Version 2.4

*\[NOTE: Enter 2.1 instead of 2.4 above if you wish to subscribe to the Version 2.1 protocols.\]*

Subscribing to HL7 version 2.4 protocols...

Protocol RA CANCEL has been unsubscribed from...

Protocol RA EXAMINED has been unsubscribed from...

Protocol RA REG has been unsubscribed from...

Protocol RA RPT has been unsubscribed from...

Protocol RA CANCEL 2.4 has been subscribed to...

Protocol RA EXAMINED 2.4 has been subscribed to...

Protocol RA REG 2.4 has been subscribed to...

Protocol RA RPT 2.4 has been subscribed to...

2.  Select option IHE to enter name and address information for the HL7 PACS interface (if you are using a commercial PACS), and to turn on HL7 version 2.4 messaging to the VistA DICOM Gateway.
    1.  You are presented with the sending application name and receiving application name. These are the names that will be sent in the MSH Segment of the HL7 messages that are transmitted to PACS (if used) and to the VistA DICOM Gateway. (See also the PACs Configuration Notes on the following pages.)
- Ordinarily, you will not wish to change either of these names and will enter NO when prompted to change them.
- If you wish to change either of these names, enter YES when prompted.
  1.  You are then asked to enter the TCP/IP address and port number for the logical link. This information defines where VistA HL7 will send the ADT messages. If you are not using a commercial PACS, leave the TCP/IP address and port number blank. If you need help finding the correct values to enter at these prompts, please consult your site’s PACS Administrator or HL7 Specialist.
  2.  Finally, you will be asked whether you want to turn on the IHE-based interface. You must answer YES if you wish HL7 version 2.4 messages to be sent from VistA to PACS (if used) and to the DICOM Gateway. If you do not wish HL7 version 2.4 messages to be sent from VistA to PACS (if used) and to the DICOM Gateway, enter NO.

> The following is a sample of the prompts you will see when you select option IHE. The bolded text is what you need to type. Note that the IP address and port number are examples and you should enter the ones that apply to your PACS. If you are not using a commercial PACS, leave the IP address and port number blank.

  RHL7 Maintain Subscriptions to Radiology HL7 Drivers

IHE Configure IHE-Based HL7 Interface to PACS

Select Imaging HL7 Messaging Maintenance Option: IHE Configure IHE-Based HL7 Interface to PACS

HL7 PACS Interface Configuration

Sending application name: MAG VISTA IMGNG

Receiving application name: MAG COMRCL PACS

Do you wish to change either of these names? NO

Please enter the TCP/IP address and port number for the logical link.

TCP/IP ADDRESS: www.xxx.yyy.zzz \<enter the address that applies to your PACS\>

TCP/IP PORT: nnnnn \<enter the port number that applies to your PACS\>

Enter Y or YES below to turn the IHE-based HL7 PACS interface ON;

enter N or NO to turn the interface OFF.

IHE PACS HL7 INTERFACE ACTIVE: Y YES

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PACS CONFIGURATION NOTES</strong></th>
<th><p>PACS must be configured to accept in field <em>MSH-3-Sending Application</em> the value of “Sending application name:” shown in the preceding sample, and to return this value in field <em>MSH-5-Receiving Application</em> when sending replies.</p>
<p>PACS must be configured to accept in field <em>MSH-5-Receiving Application</em> the value of “Receiving application name:” shown in the preceding sample, and to return this value in field <em>MSH-3-Sending Application</em> when sending replies.</p>
<blockquote>
<p>For both these values, follow your PACS manufacturer’s configuration instructions.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## I.4 Radiology HL7 Protocols and Imaging Subscribers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If HL7 Version 2.4 is in use, Imaging subscribers will be attached to Radiology event drivers for HL7 V2.4 messaging as shown below.

NAME: RA REG 2.4

ITEM TEXT: Rad/Nuc Med exam registered (v2.4 HL7)

TYPE: event driver CREATOR: HENDERSON,MIKE

PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is registered. It executes code that creates an HL7 ORM message

consisting of PID, PV1, ORC, OBR, OBX and ZDS segments. The message contains

all relevant information about the exam, including procedure, time of

registration, procedure modifiers, CPT modifiers, patient allergies, and

clinical history.

This protocol is used to trigger v2.4 compliant HL7 messages.

TIMESTAMP: 61846,30525 SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: D MAIN^RAHLACK

SUBSCRIBERS: MAGJ PREFETCH/SEND ORM

SUBSCRIBERS: MAGD SEND ORM

NAME: RA EXAMINED 2.4

ITEM TEXT: Rad/Nuc Med examined case (v2.4 HL7)

TYPE: event driver CREATOR: HENDERSON,MIKE

PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam has been edited by the user. It executes code that creates an

HL7 ORM message consisting of PID, PV1, ORC, OBR, OBX and ZDS segments. This

message contains all relevant information about the exam, including procedure,

time of registration, procedure modifiers, CPT modifiers, patient allergies,

and clinical history.

This protocol is used to trigger v2.4 compliant HL7 messages.

TIMESTAMP: 61846,30525 SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: D MAIN^RAHLACK

SUBSCRIBERS: MAGD SEND ORM

NAME: RA CANCEL 2.4

ITEM TEXT: Rad/Nuc Med exam cancellation (v2.4 HL7)

TYPE: event driver CREATOR: HENDERSON,MIKE

PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is cancelled. It executes code that creates an HL7 ORM message

consisting of PID, PV1, ORC, OBR, OBX and ZDS segments. The message contains

all relevant information about the exam, including procedure, time of

cancellation, procedure modifiers, CPT modifiers, patient allergies and

clinical history.

This protocol is used to trigger v2.4 compliant HL7 messages.

TIMESTAMP: 61846,30525 SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: D MAIN^RAHLACK

SUBSCRIBERS: MAGD SEND ORM

NAME: RA RPT 2.4

ITEM TEXT: Rad/Nuc Med report released/verified (v2.4 HL7)

TYPE: event driver CREATOR: HENDERSON,MIKE

PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine report enters into a status of Verified or Released/Not Verified. It

executes code that creates an HL7 ORU message consisting of PID, OBR and OBX

segments. The message contains relevant information about the report,

including procedure, procedure modifiers, diagnostic code, interpreting

physician, impression text and report text.

This protocol is used to trigger v2.4 compliant HL7 messages.

TIMESTAMP: 61846,30525 SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: D MAIN^RAHLACK

SUBSCRIBERS: MAGD SEND ORU

## I.5 Entering Facility Names for Sending/Receiving Applications for PACS Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the VistA HL7 package, the correct facility names need to be associated with the MAG VISTA IMGNG sending application and with the MAG COMRCL PACS receiving application. This section provides instructions on how to do this.

You associate the facility names with the sending and receiving applications using the HL7 menu system. You must have access to the HL7 menus to set the facility names for the sending and receiving applications.

1.  Assign the correct facility name to the MAG VISTA IMGNG sending application as follows:
    1.  From the main menu, select option HL7 MAIN MENU and enter the underlined values illustrated in the following sample.

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

HLO HL7 (Optimized) MAIN MENU ...

Select HL7 Main Menu Option: <u>IN</u>terface Developer Options

EA Application Edit

EP Protocol Edit

EL Link Edit

VI Validate Interfaces

Reports ...

Select Interface Developer Options Option: <u>EA</u> Application Edit

Select HL7 APPLICATION PARAMETER NAME: <u>MAG VISTA IMGNG</u> ACTIVE

> An entry screen like this one will appear:

HL7 APPLICATION EDIT

--------------------------------------------------------------------

NAME: MAG VISTA IMGNG ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: VA-WOIFO COUNTRY CODE: USA

HL7 FIELD SEPARATOR: HL7 ENCODING CHARACTERS:

MAIL GROUP:

1.  Change the value of the FACILITY NAME field to indicate the facility in which VistA is installed. The value you specify will be transmitted to PACS in the field *MSH-4-Sending Facility*.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PACS CONFIGURATION NOTES</strong></th>
<th><p>PACS must be configured to accept the value specified for the FACILITY NAME field in field <em>MSH-4-Sending Facility</em> when receiving messages, and to return this value in field <em>MSH-6-Receiving Facility</em> when sending replies.</p>
<p>Follow your PACS manufacturer’s configuration instructions to configure your PACS in this manner.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  After changing the FACILITY NAME field, save your changes and exit the form.
2.  Assign the correct facility name to the MAG COMRCL PACS receiving application as follows:
    1.  From the HL7 APPLICATION PARAMETER NAME menu option, select MAG COMRCL PACS.

Select HL7 APPLICATION PARAMETER NAME: MAG COMRCL PACS ACTIVE

> An entry screen like this one will appear.

HL7 APPLICATION EDIT

--------------------------------------------------------------------

NAME: MAG COMRCL PACS ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: CPACS FACILITY COUNTRY CODE: USA

HL7 FIELD SEPARATOR: HL7 ENCODING CHARACTERS:

MAIL GROUP:

1.  Change the value of the FACILITY NAME field to indicate the facility in which PACS is installed. This value will be transmitted to PACS in field *MSH-6-Receiving Facility*.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PACS CONFIGURATION NOTES</strong></th>
<th><p>PACS will need to be configured to accept this value in field <em>MSH-6-Receiving Facility</em> when receiving messages, and to return this value in field <em>MSH-4-Sending Facility</em> when sending replies.</p>
<p>Follow your PACS manufacturer’s configuration instructions to configure your PACS in this manner.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  After changing the FACILITY NAME field, save your changes and exit the form.

## I.6 Service Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some processes on a DICOM Gateway are executed in typical “user oriented” sessions: the user logs in, performs a task, and logs out. However, the tasks that embody the main purpose of the DICOM Gateway run for a long time, typically weeks or months on end, and are intended to keep functioning without any human interaction.

Since these tasks need to be started at some point in time, a (fully privileged) user will log in, and request the menu option that starts the long-running task. From that point on, the task will run and will continue to run until stopped by a system manager.

When the network connection between the DICOM Gateway and the VistA Hospital Information System is interrupted, the DICOM Gateway will recover from this situation, and will periodically attempt to reconnect (at 5-minute intervals). Once the connection is re-established, the DICOM Gateway will continue processing where it left off when the connection was interrupted.

To establish a service account, use the Kernel Tools to establish the account, then conduct a dialog like the following:

VISTA\>d P^DII \<Enter\>

VA FileMan 22.0

Select OPTION: en \<Enter\> TER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: // 2006.1 \<Enter\> IMAGING SITE PARAMETERS

(2 entries)

EDIT WHICH FIELD: ALL// DICO \<Enter\>

1 DICOM GATEWAY ACCESS CODE

2 DICOM GATEWAY VERIFY CODE

CHOOSE 1-2: 1 \<Enter\> DICOM GATEWAY ACCESS CODE

THEN EDIT FIELD: DICO \<Enter\>

1 DICOM GATEWAY ACCESS CODE

2 DICOM GATEWAY VERIFY CODE

CHOOSE 1-2: 2 \<Enter\> DICOM GATEWAY VERIFY CODE

THEN EDIT FIELD: \<Enter\>

Select IMAGING SITE PARAMETERS INSTITUTION NAME: \`1 \<Enter\> \<your site name\>

DICOM GATEWAY ACCESS CODE: \<hidden\>// xxaccxx_123 \<Enter\>

DICOM GATEWAY VERIFY CODE: \<hidden\>// xxverxx_456 \<Enter\>

Select IMAGING SITE PARAMETERS INSTITUTION NAME: \<Enter\>

Select OPTION: \<Enter\>

VISTA\>

[^1]: For VistA installations, the data for ^MAGDHL7 accrues as events happen in the system.

[^2]: UNIX<sup></sup> Network Programming, W. Richard Stephens, Prentice Hall, 1990, page 304.

[^3]: DICOM applications require “hard coded” IP addresses and cannot use those assigned by the Dynamic Host Configuration Protocol (DHCP).