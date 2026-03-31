---
title: VistA Imaging System Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: plain
doc_subject: VistA Imaging System
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
description: The VistA Imaging System captures, stores, displays, and distributes medical images. These medical images are part of a patient’s medical record and are protected by the Federal Privacy Act and by HIPAA (the Health Insurance Portability and Accountability Act). Images are stored on magnetic servers
audience: 
keywords: 
  - class
  - colspan
  - dicom
  - table
  - contents
  - security
  - imaging
  - vista
  - even
  - image
page_count: 0
word_count: 11928
section_count: 35
table_count: 6
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: July 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGSECGD.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGSECGD.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

![](vista-imaging-system-security-guide/001.png)

VistA Imaging System

Security Guide

July 2019 – Revision 25

MAG\*3.0\*204

  
VistA Imaging System Security Guide  
MAG\*3.0\*34, MAG\*3.0\*116, MAG\*3.0\*118, MAG\*3.0\*119, MAG\*3.0\*127, MAG\*3.0\*129, MAG\*3.0\*204  
July 2019Property of the US Government

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging Product Development group.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

VistA Imaging Product Development  

[<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

Revision History

16 July 2019 Updates for MAG\*3.0\*204

[<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

--Updated section 1.3 to include new Windows versions, title page, footers, revision history, and TOC.

2 August 2013 Updates for MAG\*3.0\*34, MAG\*3.0\*116, MAG\*3.0\*118, MAG\*3.0\*119, MAG\*3.0\*127, MAG\*3.0\*129  
[<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) (rev 24).  
--Added new sections 2.85 *Security Keys for DICOM Importer II* and 2.14 *HDIG Security 2.14* (and all its sub-sections) Updated sections 1.1, 1.3, 1.3.2.5, 2.9, 2.11.1, 2.11.2, 2.12, 2.13, 2.13.2, 2.15.

15 Mar 2013 Updates for MAG\*3.0\*124 (Rev. 23). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

--Updated sections 2.2.5; added section 2.2.5.1 AWIV Web Application (new); 2.2.5.2 Security Keys for AWIV)

26 Nov 2012 Updates for MAG\*3.0\*122. [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .  
--Updated sections 2.2.1, 2.8.1, 2.9, 2.12.

09 Nov 2011 Updates for MAG\*3.0\*104 (rev 21). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .  
--Updated Appendix A and A.11; removed obsolete subsections under A.11.

01 Sep 2011 Updates for MAG\*3.0\*117 (rev 20). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .  
--Updated sections 2.8.2 and 2.9; added Glossary entries

31 May 2011 Updates for MAG\*3.0\*39 (rev 19). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)  
--Updated sections 2.3, 2.7, 2.9; added new section 2.14  
--Made global text corrections listed on p.1 of the Change Pages document

04 May 2011 Updates for MAG\*3.0\*106 (rev 18). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)  
--Updated sections 2.8.3 and 2.9

21 Mar 2011 Update For MAG\*3.0\*115 (rev 17). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

01 Feb 2011 Updates for MAG\*3.0\*105 and 98 (rev 16). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)  
--Added new section 2.2.4 for Patch 105.  
--Updated section 2.8.1 for Patch 98.  
--non-patch update. Section 2.11, IPRM replaces OCIS.

1 Dec 2010 Updates for MAG\*3.0\*53 and MAG\*3.0\*66 (rev 15). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)  
--Updated section 2.9 for Patch 53.  
--Updated sections 1.1, 1.2, 2.2.3 and 2.1.2 for Patch 66.

21 Sep 2010 Updates for MAG\*3.0\*111, MAG\*3.0\*90, and MAG\*3.0\*94 (rev 14). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) y.  
--Updated sections 2.2.1, 2.6, and 2.8.2 for Patches 111 and 94.  
--Updated section 2.8.4 for Patch 90.

09 Jul 2010 Updates for MAG\*3.0\*83 (rev 13). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .  
--Updated sections 1.2, 2.2.1, and 2.8.1; correct typos in section 2.8.4; added new appendix for VIX.

10 Feb 2010 Updates for Patch 93 and Patch 101 (rev 12) [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)  
-- Updated sections 1.1, 2.6, 2.8.2, 2.9 for Patch 93  
-- Updated sections 2.2.3, 2.8.4, 2.9 for Patch 101

20 Oct 2009 Updates for Patch 72 and applied change pages for Patch 54 (rev 11), [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

> For Patch 72: updates to section 2.8.1.

> General cleanup and corrections for sections: 1.1, 2.2.2 2.13.3  
> 29 Feb 2008 Patch 59 revisions (rev 10): Updates to section 2.8.3. [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .

14 Jan 2008 Patch 76 revisions (rev 9): Updates to sections 1.3, 2.8.4, and 2.11.2. [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

04 May 2007 Patch 46 and 65 revisions (rev 8): Updates to section 2.9. [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .

20 July 2006 Patch 50 revisions (rev 7): Updated section 2.9. [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

30 June 2006 Patch 18 revisions (rev 6): Updated sections 1.2, 2.8, 2.9, and 2.11.2. Removed obsolete sections 2.11.2.1 and 2.11.2.2. [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

05 Dec 2005 Patch 57 revisions (rev 5): Added 2 keys released with patch 30 to section 2.8. Removed obsolete information from sections 2.10 and 2.11. Incorporated p45 changes to sections 2.2 and 2.12. [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

8 Feb 2005 Updated information for Patch 48 (rev 4). [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main)

27 April 2004 Changed “Revision 1” references” to “Revision 2”

23 April 2004 Updated information for Patch 8 (rev 3)

16 April 2004 Updated information for Patch 11

5 Nov 2003 Updated Security Features section

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Security Management](#security-management)
  - [Introduction](#introduction)
  - [Software Application and User Interface](#software-application-and-user-interface)
  - [Security Measures](#security-measures)
- [Security Features](#security-features)
  - [Mail Group and Alerts](#mail-group-and-alerts)
  - [Remote Systems](#remote-systems)
    - [Remote Image Views](#remote-image-views)
    - [Routing to DICOM Storage SCPs (Service Class Providers)](#routing-to-dicom-storage-scps-service-class-providers)
    - [Query/Retrieve](#queryretrieve)
    - [Images Posted to MIRC](#images-posted-to-mirc)
    - [AWIV with CVIX](#awiv-with-cvix)
  - [Note: NCAT reports are available if NCAT is available and online.](#note-ncat-reports-are-available-if-ncat-is-available-and-online)
  - [Archiving/Purging](#archivingpurging)
  - [Contingency Planning](#contingency-planning)
    - [Magnetic Share](#magnetic-share)
    - [Optical Disk Jukebox](#optical-disk-jukebox)
    - [Network](#network)
    - [Workstations Used During Medical Care Procedures](#workstations-used-during-medical-care-procedures)
  - [Interfacing](#interfacing)
  - [Electronic Signature](#electronic-signature)
  - [Menus](#menus)
  - [Security Keys](#security-keys)
    - [General Security Keys](#general-security-keys)
    - [Security Keys for Clinical Display](#security-keys-for-clinical-display)
    - [Security Keys for Clinical Capture](#security-keys-for-clinical-capture)
    - [Security Keys for VistARad](#security-keys-for-vistarad)
    - [Security Keys for the DICOM Importer II](#security-keys-for-the-dicom-importer-ii)
  - [File Security](#file-security)
  - [Windows Security](#windows-security)
  - [Workstation Security](#workstation-security)
    - [SMS Software, DICOM Gateways and Background Processors](#sms-software-dicom-gateways-and-background-processors)
    - [SMS Software and VistARad](#sms-software-and-vistarad)
  - [Audit Trails](#audit-trails)
  - [VistA DICOM Gateway](#vista-dicom-gateway)
    - [Modality Worklist](#modality-worklist)
    - [DICOM Gateway Service Account](#dicom-gateway-service-account)
    - [Kernel RPC Broker Routines](#kernel-rpc-broker-routines)
  - [HDIG Security](#hdig-security)
    - [HDIG Service Account](#hdig-service-account)
    - [Apache Tomcat Administrator Account](#apache-tomcat-administrator-account)
    - [DICOM AE Security Matrix](#dicom-ae-security-matrix)
    - [Security Keys Required for Deleting a Study by Accession Number](#security-keys-required-for-deleting-a-study-by-accession-number)
    - [Security Mechanisms for the Logs in that Record HDIG Activities](#security-mechanisms-for-the-logs-in-that-record-hdig-activities)
    - [Patient Security Logging for Sensitive Patients](#patient-security-logging-for-sensitive-patients)
  - [Background Processor Servers](#background-processor-servers)
  - [References](#references)
- [Appendix A VIX Security Information](#appendix-a-vix-security-information)
  - [The VIX and CVIX are described in detail in the VIX Administrator’s Guide.](#the-vix-and-cvix-are-described-in-detail-in-the-vix-administrators-guide)
  - [A.1 Mail Groups, Alerts, and Bulletins](#a1-mail-groups-alerts-and-bulletins)
  - [A.2 Remote Systems](#a2-remote-systems)
  - [A.3 Archiving](#a3-archiving)
  - [A.4 Contingency Planning](#a4-contingency-planning)
  - [A.5 Interfacing](#a5-interfacing)
  - [A.6 Electronic Signatures](#a6-electronic-signatures)
  - [A.7 Menus](#a7-menus)
  - [A.8 Security Keys](#a8-security-keys)
  - [A.9 File Security](#a9-file-security)
  - [A.10 Software Pushes and the VIX](#a10-software-pushes-and-the-vix)
  - [A.11 VistA Account for BHIE Framework Access](#a11-vista-account-for-bhie-framework-access)
  - [A.12 References](#a12-references)
  - [A.13 Official Policies](#a13-official-policies)
- [Glossary](#glossary)
This manual is provided to control the release of sensitive information related to VistA Imaging V. 3.0 software (Note: The Security Guide will not be included in any Freedom of Information Act (FOIA) request releases.) This document shall not be distributed outside the VA Intranet.
Since certain keys and authorization must be delegated for proper management of the VistA Imaging System, information about these items also may be found in the technical and user manuals.

# Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging System captures, stores, displays, and distributes medical images. These medical images are part of a patient’s medical record and are protected by the Federal Privacy Act and by HIPAA (the Health Insurance Portability and Accountability Act). Images are stored on magnetic servers that are backed up on optical disk jukebox servers. The hardware configurations should include a high-capacity tape backup unit. Additionally, backups (copies) of the optical platters can be created. Those backups should be taken off site. Security keys are required for use of the package and special features such as image deletion. An electronic signature is required for copying and printing images. The Joint Commission on Accreditation of Health Organizations (JCAHO) has been very interested in image storage during their visits to the VistA Imaging sites and has recommended guidelines in these areas.

## Software Application and User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging System is a suite of Windows applications with user interfaces written predominately in Delphi. Certain components are written in C++ (VistARad), Java (the VIX) and M (the DICOM Gateway), and Java (the Query/Retrieve application).

Client components in the Imaging System make calls to the Veterans Health Information Systems and Technology Architecture (VistA) hospital information system using the Remote Procedure Call (RPC) Broker.

*The Food and Drug Administration classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes.*

## Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging servers and workstations are protected by several security measures. Security protection is built into the software for Windows XP, Windows 7, Windows 2008 Server, Windows 2010 Server, and Windows 2012 Server. The use of other versions of Windows is not permitted. If a site has a requirement to use an unpermitted operating system version, then the site’s administrator should contact the VistA Imaging National Project Office (NPO). The Food and Drug Administration (FDA) Quality System Regulation (QSR) permits the use of the VistA Imaging software only on approved hardware and operating systems. Only the NPO can determine compliance with QSR (not Customer Support or any other party), elect to test a new platform, or authorize any changes.

This page intentionally left blank.

# Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Mail Group and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MAG SERVER mail group is created during the VistA Imaging KIDS software installation. This mail group is used for messages related to system configuration and usage based on information collected by the software. The VistA Imaging KIDS installer and the remote imaging development mail group are added as initial members.

There are no alerts that are created, required, or used by this application.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Remote Image Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the remote image viewing functionality is used without a VistA Image Exchange (VIX) service, the VistA Imaging system logs image access information at remote sites. User accounts are also created on the remote system when the user logs into their local system and accesses remote images. Images from remote sites are transmitted to the local site for viewing with the Clinical Display client or VistARad client on an as-requested basis. No encryption is used for the images or the data. Verification of the image integrity is done visually by the user.

For information about VIX-supported remote image views, see *Appendix A VIX Security Information*.

Patch 111 provides the availability of the Broker Security Enhancement (BSE) for VistA Imaging clients. BSE is a token based authentication method that provides enhanced security over the previously used CAPRI login method.

Patch 94 modifies remote image view functionality in Display and TeleReader to make use of BSE. The client will first use BSE when attempting to connect to remote sites. If BSE fails, the client will use the CAPRI remote site login. When CAPRI is used, the system will generate a log entry to track the usage of the CAPRI authentication method. Using the BSE or CAPRI remote login method does not affect the usability of the applications, and it is transparent to the user.

The Kernel Team will release a patch to disable the CAPRI authentication method after Patch 94 is released. When the Kernel Team disables the CAPRI authentication method, only clients 94 and later will be able to connect to sites for remote image viewing.

Users with the annotation permission at the remote site can make annotations to remote VA images. Remote annotating is intended to assist in remote interpretation of images.

Notes:

1.  Users cannot annotate images from the Department of Defense (DoD).
2.  Users cannot save permanent annotations to VistARad-annotated radiology images.
3.  Radiology image annotations can only be saved in the VistARad application.

### Routing to DICOM Storage SCPs (Service Class Providers)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Studies and associated header data may be pushed to DICOM Storage SCPs on an ad hoc basis. Site-configurable rules-based routing may also be used to push newly acquired studies and associated header data to DICOM Storage SCPs without human intervention.

Confirmation and acknowledgement is provided via the methods inherent in a DICOM data exchange.

Transmitted data is not encrypted; US Federal regulations and VA internal policy prohibit unencrypted transmission of patient information outside the VA's intranet.

### Query/Retrieve 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Studies and associated header data may be retrieved by validated DICOM Query/Retrieve SCUs (Service Class Users) on an ad hoc basis. To receive the data, DICOM Query/Retrieve SCUs must provide valid patient and study attributes.

Confirmation and acknowledgement is provided via the methods inherent in a DICOM data exchange.

Transmitted data is not encrypted; US Federal regulations and VA internal policy prohibit unencrypted transmission of patient information outside the VA’s intranet.

### Images Posted to MIRC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistARad can be used to post images, series, or exams of broader interest (a.k.a. “teaching files”) to local or offsite Medical Imaging Resource Center (MIRC) servers. It is imperative that images posted to such servers contain no personally identifiable information (PII). Ensuring that images contain no PII is the user’s responsibility. VistARad will have already removed any PII from text data. However, burned-in pixel data cannot be removed. Therefore, the user must ensure that there is no PII in the burned-in pixel data of any image, series, or exam uploaded to the MIRC.

### AWIV with CVIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging Advanced Web Image Viewer (AWIV) retrieves all image information from the Centralized VistA Imaging Exchange (CVIX) service. Access to the AWIV is available only from within VistAWeb and requires the user to authenticate against a VistA system. User credentials from VistAWeb are passed to the AWIV using 256-bit AES encryption and are used to connect to remote VA systems through the CVIX. Access to VA data through the CVIX shares the same functionality as VIX-supported remote image views, described in Appendix A.

#### AWIV Web Application 

The AWIV Web Application, hosted on the CVIX, is independent of VistAWeb and VistA Imaging Clinical Display, and enables use of the AWIV via Microsoft Edge/Google Chrome.

The AWIV Web Application is hosted on the CVIX because it is not feasible to acquire secure socket layer (SSL) certificates for each VA VIX service. SSL certificates are used to encrypt the communication of data between web browsers and the CVIX.

#### Security Keys for AWIV 

Users of the AWIV Web Application are required to be authenticated to the claims system or have security keys that allow them access to view images. During the log-in process users will select what site they wish to authenticate against. The user must have a valid account at that site to view log-in. Patient lookup is then done against this selected site. Only patients seen at this site can be viewed.

Users authenticated against VHA facilities (non-claims users) will have access to images based on the security keys the user has at that facility. Enforcement of security keys is handled by the AWIV Web Application, with the exception of the MAG REVIEW NCAT key. The AWIV Web Application passes a parameter to the AWIV component which indicates if the user has the MAG REVIEW NCAT key. The enforcement of the MAG REVIEW NCAT key is handled by the AWIV component.

Security Keys Supported by AWIV Web Application

| Security Key   | Function                                                                             |
|--------------------|------------------------------------------------------------------------------------------|
| MAGDISP ADMIN      | Enables the holder to display administrative images/documents.                           |
| MAGDISP CLIN       | Enables the holder to display clinical images/documents.                                 |
| MAG PAT PHOTO ONLY | Enables a user to view the patient photo only and gives the user no other functionality. |
| MAG REVIEW NCAT    | User can view NCAT Report.                                                               |
| MAG ROI            | Users with this key need not enter an electronic signature when printing images.         |

## Note: NCAT reports are available if NCAT is available and online.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving/Purging 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All images acquired using the VistA Imaging System are archived immediately to the optical disk jukebox. This provides two copies of the image on site for an initial period of time. In addition, the magnetic server should be backed up regularly as specified by site system administrator. The tapes and/or optical media copies should be moved to an offsite location.

> **NOTE:** See the Installation Guide for details on backup types and frequency.

Images are periodically purged from the magnetic server to free up disk space. A purge can be started manually by the VistA Imaging coordinator. Typically, the process is either triggered automatically when the available free space is less than a site-specified threshold or scheduled to manage space and backup activities. Images on the jukebox are never deleted. The coordinator specifies the date criteria for the purge: the Date Accessed, the Date Created, or the Date Modified, which are attributes of an image on the RAID. Keep Days are specified by the type of image.

The Purge operation checks for pointers to network locations on the jukebox, and then verifies that the database references to the images are correct and that the files referenced are on the jukebox before it purges them.

After the magnetic copy of an image is purged, the only copy of the image will be the one on the jukebox. This is why it is critical to create backups of optical disk platters.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging System relies on a number of devices for its operation, including magnetic file servers, one or more optical disk jukebox servers, network components and workstations.

Sites should have procedures defined for use in case of a system outage.

### Magnetic Share

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Image management software within the VistA Imaging package allows a site with a magnetic share that is down, to indicate that it is “offline”. When a share is set to “offline”, all images will be retrieved directly from the jukebox.

In many cases, sites have chosen to purchase “clustered” Microsoft Windows™ file servers. This adds an extra layer of redundancy that allows the image shares to be accessible even if a server is down.

Read/write access to image shares is limited to restricted accounts.

### Optical Disk Jukebox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The jukebox is used for long-term storage. Most of the time images that are requested will reside on the magnetic server. Access to jukebox shares is also restricted.

### Network 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging System is dependent on a properly operating network. Network problems will cause users to be unable to view images or to access data within VistA. Some DICOM image capture capability is available even under conditions where VistA, the servers, or the hospital network is not operational. However, the network should be repaired as quickly as possible, as there is no workstation access to images. Sites should maintain equipment for detecting problems in their network and spare switches and devices for rapid maintenance and repair. It is very important that sites have proper documentation of their networks. These documents should be available for review by your Regional Information Security Officer (RISO).

### Workstations Used During Medical Care Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a workstation malfunctions, it is necessary that the workstation be repaired or replaced immediately. In many cases the patient is in the operating room or having a procedure performed at the time of the failure. It is recommended that medical centers keep “hot spare” workstations available so that when a trouble call is placed, the new workstation can immediately replace the problem workstation. Subsequently, the failed workstation can be repaired as time permits.

## Interfacing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Imaging interfaces to a number of image capture devices and to other systems. The following is a list of devices and systems that have been used by the application:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 23%" />
<col style="width: 28%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><br />
Product</strong></th>
<th><strong>Connection type</strong></th>
<th><strong>Used in (Medical Center) Service/Section</strong></th>
<th><strong>Restriction</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Electron Microscope with JVC video camera mounted with an adapter</td>
<td>Video output</td>
<td>Pathology Lab</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="even">
<td>Multi-headed microscope with JVC video camera mounted with an adapter</td>
<td>RGB analog output</td>
<td>Hematology (can also be used for live conferencing)</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="odd">
<td>Document Scanners - HP Desktop - Microtek – Fujitsu</td>
<td>TWAIN/ SCSI inter- face</td>
<td>Tumor Registry, Medical Libraries, Scanned Advance Directives, Consent Forms</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="even">
<td>Siemens Cardiac Catheterization system</td>
<td>RGB (may require a composite to RGB converter)</td>
<td>Cath Lab</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="odd">
<td>Echocardiograph Ultra Sound unit</td>
<td>RGB analog output</td>
<td>Echo Lab</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="even">
<td>Video Endoscopy Unit via probe (Fuji &amp; Olympus)</td>
<td>RGB analog output</td>
<td>GI Lab</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="odd">
<td>Pulmonary Endoscope</td>
<td>RGB analog output</td>
<td>Bronc Lab</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="even">
<td>Endoscopic retrograde cholangiopancreato-graphy (ERCP) procedure to C-ARM</td>
<td>Import to floppy disk</td>
<td>Radiology equipment used during endoscopic procedure</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="odd">
<td>Regular VCR viewer with calibration</td>
<td>Video output</td>
<td>Neurology for sleep studies</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="even">
<td>Arthroscope</td>
<td>Video output</td>
<td>Orthopedics</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="odd">
<td>Laparoscope</td>
<td>Video output</td>
<td>Vascular, Surgery</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="even">
<td>SLIT Lamp</td>
<td>Video output</td>
<td>Ophthalmology</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="odd">
<td>Cystoscope</td>
<td>RGB analog output</td>
<td>Urology</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="even">
<td>Digitized scanners: Lumisys 75, Lumisys 100, 150</td>
<td>SCSI port or TWAIN interface</td>
<td>Radiology</td>
<td>Imaging procedure keys</td>
</tr>
<tr class="odd">
<td>Portable hand held cameras: Olympus, Polaroid, Kodak</td>
<td>Via import function from USB 2.0 or higher, FireWire, or Thunderbolt</td>
<td>Dermatology, Plastic Surgery, operating rooms, Orthopedics, emergency rooms, wards, clinics (Example of types of images: lesions, bedsores, skin pigmentation, etc.)</td>
<td>Imaging procedure keys</td>
</tr>
</tbody>
</table>

Please note the security of the equipment will depend on the Medical Center’s policies and/or the medical area supervision.

All equipment purchased for interfacing with the VistA Imaging System must first be tested by the VistA Imaging development team.

## Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging System requires an electronic signature when an image is copied or printed from the image database. The signature is required of the person obtaining the image to indicate that privacy and security will be properly protected for that image and that the image is being copied or printed for an authorized purpose.

Only one electronic signature is required when attaching image groups to a signed TIU note. Prior to Patch 94, users were required to electronically sign each image in a group, individually.

## Menus 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the workstations, there is a menu option that allows users with the MAG DELETE key to delete images that have been collected in error. A record is kept of all deleted images.

## Security Keys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of security keys associated with the VistA Imaging system. The following tables summarize security keys and their function.

### General Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Please be cautious when assigning the following keys; the keys are intended for Imaging Support personnel. Review the descriptions before assigning these keys.

| General Security Keys |                                                                                                                                                                                                                                                                                                                               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAG ANNOTATE MGR          | User can add, edit, and delete annotations. Permissions provided by this key apply only to images at the site where the user has the key. This key also allows users to create annotations regardless of the settings of the user’s account in the PARAMETER DEFINITION (MAG IMAGE ALLOW ANNOTATE) specified at a given site. |
| MAGDFIX ALL               | Allows the holder to perform DICOM CORRECT functions on any entry in the DICOM FAILED IMAGES file (#2006.575). Users who do not hold this key will only be able to correct entries that were captured on their own site's gateway.                                                                                            |
| MAG DELETE                | This key allows the holder to delete images from the IMAGE file (#2005). Pointers in parent packages such as Medicine, Surgery, Lab, Radiology, and TIU will also be deleted.                                                                                                                                                 |
| MAG DOD FIX               | This key gives the holder permission to run the MagKat utility.                                                                                                                                                                                                                                                               |
| MAG PREFETCH              | This key allows a user to 'PreFetch' or Queue all images for a patient. This means that all images for a patient that are on the jukebox will be copied from the jukebox to the magnetic server cache.                                                                                                                        |
| MAG SYSTEM                | Given to person(s) managing VistA Imaging Systems. Required to modify site parameters via the Background Processor or to modify workstation parameters via the MAGSYS application. Also enables the display of DICOM header data for radiology images on Clinical Display workstations.                                       |
| MAG VIX ADMIN             | This key grants access to the VIX transaction log and HDIG administration parameters (HDIG server accounts access/verify code and email addresses). This key should be assigned to VIX and HDIG administrators. For more information, see the *VIX Administrator’s Guide*.                                                    |

### Security Keys for Clinical Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following keys are used for display of images and should be limited to appropriate personnel.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Display-related Security Keys</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAG RAD SETTINGS</td>
<td colspan="2">User can edit the CT Presets in the Clinical Imaging Display Radiology Viewer window.</td>
</tr>
<tr class="even">
<td>MAG ROI</td>
<td colspan="2">User can print (single or multiple) images or copy images without having to enter an electronic signature. This key should only be assigned to the HIMS Release of Information Officer.</td>
</tr>
<tr class="odd">
<td>MAGDISP ADMIN</td>
<td colspan="2">User can display administrative images/documents.</td>
</tr>
<tr class="even">
<td>MAGDISP CLIN</td>
<td colspan="2">User can display clinical images/documents.</td>
</tr>
<tr class="odd">
<td>MAG EDIT</td>
<td colspan="2">The MAG EDIT key is used to correct an image field when an index field is incorrect or incomplete, such as correction of a wrongly selected specialty. Only users assigned the MAG EDIT key can edit an image. The MAG EDIT key is also required to access the QA Review Utility when performing quality assurance reviews of the scanned images. Only the Chief, HIM or authorized designated personnel (e.g., VistA Imaging Coordinator, Scanning Supervisor) should be assigned this key.</td>
</tr>
<tr class="even">
<td>MAG PAT PHOTO ONLY</td>
<td colspan="2">User can view only the patient photo.</td>
</tr>
<tr class="odd">
<td>MAG QA REVIEW</td>
<td colspan="2">User can access QA Review and QA Review Report from Clinical Display Utilities Menu.</td>
</tr>
<tr class="even">
<td>MAG REVIEW NCAT</td>
<td colspan="2">User can view NCAT reports.</td>
</tr>
<tr class="odd">
<td>MAG VIEW DOD IMAGES</td>
<td colspan="2"><p>In Patch 72 and 93 versions of Clinical Display, users must have this key to display DoD images.</p>
<p>In newer versions of Clinical Display, this key is not checked.</p></td>
</tr>
</tbody>
</table>

### Security Keys for Clinical Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** If the ‘CAPTURE KEYS’ site parameter has been initialized, the following keys will need to be assigned appropriately.

| Capture-related Security Keys |                                                                                                                      |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------|
| MAG CAPTURE                       | Allow capture of images without an associated specialty (e.g., 'NONE' on the Imaging Capture configuration window).  |
| MAG NOTE EFILE                    | User can electronically file notes without an electronic signature from the Imaging Capture workstation.             |
| MAGCAP ADMIN                      | Allow capture of images associated with the ‘Admin Document’ specialty.                                              |
| MAGCAP CP                         | Allow capture of Clinical Procedure images.                                                                          |
| MAGCAP LAB                        | User can capture Laboratory images from the Imaging Capture workstation.                                             |
| MAGCAP MED C                      | User can capture Cardiology images from the Imaging Capture workstation.                                             |
| MAGCAP MED G                      | User can capture GI images from the Imaging Capture workstation.                                                     |
| MAGCAP MED GEN                    | User can capture Generic Medicine images from the Imaging Capture workstation.                                       |
| MAGCAP MED H                      | User can capture Hematology images from the Imaging Capture workstation.                                             |
| MAGCAP MED HI                     | User can capture Internal Medicine / Hematology images from the Imaging Capture workstation.                         |
| MAGCAP MED I                      | User can capture Internal Medicine images from the Imaging Capture workstation.                                      |
| MAGCAP MED N                      | User can capture Neurology images from the Imaging Capture workstation.                                              |
| MAGCAP MED P                      | User can capture Pulmonary / Endoscopy images from the Imaging Capture workstation.                                  |
| MAGCAP MED PF                     | User can capture Pulmonary Function Test images from the Imaging Capture workstation.                                |
| MAGCAP MED R                      | User can capture Rheumatology images from the Imaging Capture workstation.                                           |
| MAGCAP MED Z                      | User can capture Consult images from the Imaging Capture workstation.                                                |
| MAGCAP PHOTOID                    | User can capture Photo ID images from the Imaging Capture workstation.                                               |
| MAGCAP RAD                        | User can capture Radiology images from the Imaging Capture workstation.                                              |
| MAGCAP SUR                        | User can capture Surgery images from the Imaging Capture workstation.                                                |
| MAGCAP TIU                        | User can capture TIU images from the Imaging Capture workstation.                                                    |
| MAGCAP TRC                        | A user with this key can capture images associated with a "TeleReader Consult" from the Imaging Capture workstation. |

### Security Keys for VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following keys are related to VistARad and should be limited to appropriate personnel.

| VistARad-related Security Keys |                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAGJ DEMAND ROUTE                  |                                                                                                                                                                                                                                                                                                                                                 | User can access VistARad’s on-demand routing capability. On-demand routing can be used to manually send exams to remote sites. For more information, refer to the VistARad or Routing User Guides.                                                                                                                                                                                        |
| MAGJ DEMAND ROUTE DICOM            | Allows the user to use the on-demand routing function to queue exam images to be routed to selected remote DICOM destinations. This function only works for sites that have been configured for routing of images. An updated Routing agreement needs to be submitted and approved by the VistA Imaging Group before this function can be used. |                                                                                                                                                                                                                                                                                                                                                                                           |
| MAGJ OVERRIDE ANNOTATIONS          |                                                                                                                                                                                                                                                                                                                                                 | Grants to a radiologist user of VistARad access to the menu option Override Annotations when viewing an exam whose status is “Complete.” This functionality is detailed in the VistARad User Guide and Vista Imaging Technical Manual.                                                                                                                                                    |
| MAGJ REMOTE ACCESS CONTROL         |                                                                                                                                                                                                                                                                                                                                                 | Allows a VistARad user to access the Monitored Sites configuration subset of the VIX Configuration settings tab, and to view exam list data in the Monitored Sites tab of the Manager.                                                                                                                                                                                                    |
| MAGJ SEE BAD IMAGES                |                                                                                                                                                                                                                                                                                                                                                 | User can view images in VistARad that are associated with an exam that has failed the “Patient Safety” database checks.                                                                                                                                                                                                                                                                   |
| MAGJ STORE IMAGES                  |                                                                                                                                                                                                                                                                                                                                                 | Allows VistARad users to save Voxar images as secondary captures to VistA.                                                                                                                                                                                                                                                                                                                |
| MAGJ SYSTEM MANAGER                |                                                                                                                                                                                                                                                                                                                                                 | Allows access to Voxar-related settings in the VistARad Settings dialog. Grants access to additional data in the Imaging Internal Data display window. This functionality is detailed in the *VistARad User Guide* and *VistA Imaging Technical Manual*. Assigned only to VistARad administrators. Grants access to the Local Site VIX configuration subset of the VIX Configuration tab. |
| MAGJ SYSTEM USER                   |                                                                                                                                                                                                                                                                                                                                                 | Allows a user to create and delete site-level hanging protocols, templates, and image presets associated with the VistARad ‘sysAdmin’ user.                                                                                                                                                                                                                                               |
| MAGJ VOXAR COPYIMAGE               |                                                                                                                                                                                                                                                                                                                                                 | Allows VistARad users to copy images using Voxar (Enables the Copy to Clipboard button in the Voxar Reading manager window; refer to Voxar documentation for more information.)                                                                                                                                                                                                       |
| MAGJ VOXAR EXPORTCAPTURE           |                                                                                                                                                                                                                                                                                                                                                 | Allows VistARad users to export images using Voxar (Enables the three Export-related buttons in the Voxar Reading manager window; refer to Voxar documentation for more information.)                                                                                                                                                                                                 |
| MAGJ VOXAR PRINTCOMPOSER           |                                                                                                                                                                                                                                                                                                                                                 | Allows VistARad users to print images using Voxar (Enables the Print Composer button in the Voxar Reading manager window; refer to Voxar documentation for more information.)                                                                                                                                                                                                         |

### Security Keys for the DICOM Importer II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DICOM Importer II is a role-based application. The tasks that users can perform are linked to the role of the user. This allows Imaging System Managers and Imaging System Administrators to define different types of user accounts and thus limit access to the functions that the DICOM Importer II provides.

For more information about the roles, see the *DICOM Importer II User Manual*.

All users of the DICOM Importer II client application must have the MAG DICOM VISA menu assigned as a secondary menu option. In addition to this, each user must have one of the following security keys, depending on their role.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 0%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><strong>Security Keys for the DICOM Importer II</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">MAGV IMPORT MEDIA STAGER</td>
<td>Allows DICOM Importer II users to stage (copy) from media to staging persistent storage, where it waits for reconciliation processing.</td>
</tr>
<tr class="even">
<td>MAGV IMPORT STAGE MEDIA ADV</td>
<td colspan="2"><p>Allows DICOM Importer II users to:</p>
<ul>
<li><p>Stage (copy) studies from media to staging persistent storage and</p></li>
<li><p>View images on the media.</p></li>
</ul>
<p>This key extends security key MAGV IMPORT MEDIA STAGER.</p></td>
</tr>
<tr class="odd">
<td colspan="2">MAGV IMPORT RECON CONTRACT</td>
<td><p>Allows DICOM Importer II users to:</p>
<ul>
<li><p>Stage media at the study level</p></li>
<li><p>View images on the media</p></li>
<li><p>Associate study DICOM objects with an existing Radiology or Consult order for reconciliation.</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2">MAGV IMPORT RECON ARTIFACT</td>
<td><p>Allows DICOM Importer II users to:</p>
<ul>
<li><p>Stage media at the study level</p></li>
<li><p>View images on the media</p></li>
<li><p>Associate study DICOM objects with an existing Radiology or Consult order for reconciliation.</p></li>
<li><p>Place new Radiology orders using the Importer II user interface.</p></li>
<li><p>Use DICOM Correct to fix errors in studies in the DICOM Correct queue.</p></li>
<li><p>Manage the DICOM Importer II queue</p></li>
<li><p>Run, view, print and save DICOM Importer II reports</p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">MAGV IMPORT REPORTS</td>
<td>Allows DICOM Importer II users to view, print, and save reports to a text file.</td>
</tr>
</tbody>
</table>

## File Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists all files associated with the VistA Imaging application and the default VA FileMan security for each.

<table style="width:100%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="9"><strong>File Security</strong></th>
</tr>
<tr class="odd">
<th><p><strong>File</strong></p>
<p><strong>Number</strong></p></th>
<th><strong>File Name</strong></th>
<th><p><strong>DD</strong></p>
<p><strong>Access</strong></p></th>
<th colspan="2"><p><strong>RD</strong></p>
<p><strong>Access</strong></p></th>
<th><p><strong>WR</strong></p>
<p><strong>Access</strong></p></th>
<th><p><strong>DEL</strong></p>
<p><strong>Access</strong></p></th>
<th><p><strong>LAYGO</strong></p>
<p><strong>Access</strong></p></th>
<th><p><strong>Audit</strong></p>
<p><strong>Access</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2005</td>
<td>IMAGE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2005.001</td>
<td>IMAGING STUDY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.002</td>
<td>IMAGING ANNOTATION FILE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2005.02</td>
<td>OBJECT TYPE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2005.021</td>
<td>IMAGE FILE TYPES</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.03</td>
<td>PARENT DATA FILE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2005.1</td>
<td>IMAGE AUDIT</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2005.2</td>
<td>NETWORK LOCATION</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2005.4</td>
<td>IMAGE HISTOLOGICAL STAIN</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2005.41</td>
<td>MICROSCOPIC OBJECTIVE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2005.6</td>
<td>IMAGING PATIENT REFERENCE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.61</td>
<td>IMAGING PROCEDURE REFERENCE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.62</td>
<td>IMAGE STUDY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.63</td>
<td>IMAGE SERIES</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.64</td>
<td>IMAGE SOP INSTANCE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.65</td>
<td>IMAGE INSTANCE FILE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.66</td>
<td>IMAGING DUPLICATE UID LOG</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.71</td>
<td>IMAGING DICOM FIELDS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.8</td>
<td>IMAGING SERVICE INSTITUTION</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2005.81</td>
<td>MAG DESCRIPTIVE CATEGORIES</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2005.82</td>
<td>IMAGE INDEX FOR CLASS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.83</td>
<td>IMAGE INDEX FOR TYPES</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.84</td>
<td>IMAGE INDEX FOR SPECIALTY/SUBSPECIALTY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.85</td>
<td>IMAGE INDEX FOR PROCEDURE/EVENT</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.86</td>
<td>IMAGE ACTIONS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.87</td>
<td>IMAGE LIST FILTERS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.872</td>
<td>DICOM INDEX MAPPING</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2005.88</td>
<td>MAG REASON FILE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.99</td>
<td>IMAGE INDEX FOR BODY PART</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.03</td>
<td>IMAGE BACKGROUND QUEUE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.031</td>
<td>IMAGE BACKGROUND QUEUE POINTER</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.033</td>
<td>OFFLINE IMAGES</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.034</td>
<td>IMPORT QUEUE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.035</td>
<td>SEND QUEUE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.036</td>
<td>ROUTING STATISTICS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.04</td>
<td>ACQUISITION DEVICE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.041</td>
<td>ACQUISITION SESSION FILE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.1</td>
<td>IMAGING SITE PARAMETERS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.15</td>
<td>DICOM UID ROOT</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.17</td>
<td>MUSE VERSIONS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.18</td>
<td>IMAGING USER PREFERENCE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.19</td>
<td>IMAGING USERS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.5</td>
<td>PACS MESSAGE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.51</td>
<td>DICOM DATA ELEMENT DICTIONARY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.511</td>
<td>DIAGNOSTIC INFO FIELD</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.52</td>
<td>DICOM MESSAGE TEMPLATE DICTIONARY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.53</td>
<td>DICOM UID DICTIONARY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.531</td>
<td>EXTENDED SOP NEGOTIATION</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.532</td>
<td>DICOM SOP CLASS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.539</td>
<td>DICOM UID SPECIFIC ACTION</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.54</td>
<td>PDU TYPE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.55</td>
<td>DICOM WORKLIST PATIENT</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.56</td>
<td>DICOM WORKLIST STUDY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.563</td>
<td>DICOM GATEWAY PARAMETER</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.564</td>
<td>DICOM QUEUE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5641</td>
<td>DICOM GATEWAY MACHINE ID</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2005.565</td>
<td>EXPORT DICOM RUN FILE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.57</td>
<td>DICOM HL7 SEGMENT</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.571</td>
<td>DICOM RAW IMAGE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5711</td>
<td>DICOM M2MB RPC QUEUE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5712</td>
<td>DICOM FIXED QUEUE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5713</td>
<td>DICOM UNKNOWN MODALITY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5714</td>
<td>DICOM INCOMPLETE OBJECT</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5715</td>
<td>CURRENT IMAGE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5719</td>
<td>DICOM ERROR LOG</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.572</td>
<td>EXAMINATION COMPLETE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.573</td>
<td>GE PACS QUERY/RETRIEVE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5732</td>
<td>DICOM QUERY RETRIEVE RESULT</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5733</td>
<td>QUERY/RETRIEVE STATISTICS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.574</td>
<td>DICOM IMAGE OUTPUT</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.575</td>
<td>DICOM FAILED IMAGES</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5751</td>
<td>DICOM OBJECTS TO BE IMPORTED</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5752</td>
<td>IMPORTABLE DICOM OBJECTS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5757</td>
<td>DICOM RADIOLOGY PROCEDURE MODIFIIERS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5758</td>
<td>DICOM RADIOLOGY PROCEDURES</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5759</td>
<td>OUTSIDE IMAGING LOCATION</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5761</td>
<td>DICOM MESSAGE STATISTISTICS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5762</td>
<td>DICOM INSTRUMENT STATISTICS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5763</td>
<td>DICOM PACS STATISTICS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5764</td>
<td>DICOM LOCAL INSTRUMENT STATISTICS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.577</td>
<td>DICOM FIFO QUEUE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.58</td>
<td>DICOM LOG</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.581</td>
<td>INSTRUMENT DICTIONARY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.582</td>
<td>MODALITY TYPE DICTIONARY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5821</td>
<td>CT CONVERSION PARAMETERS</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.583</td>
<td>MODALITY WORKLIST DICTIONARY</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5831</td>
<td>DICOM HEALTHCARE PROVIDER SERVICE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5839</td>
<td>DICOM GMRC TEMP LIST</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.584</td>
<td>TCP/IP PROVIDER PORT LIST</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5841</td>
<td>TELEREADER ACQUISITION SERVICE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5842</td>
<td>TELEREADER ACQUISITION SITE</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.5843</td>
<td>TELEREADER READER</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5849</td>
<td>TELEREADER READ/UNREAD LIST</td>
<td>@</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.585</td>
<td>USER APPLICATION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.586</td>
<td>PROVIDER APPLICATION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.587</td>
<td>DICOM TRANSMIT DESTINATION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.588</td>
<td>APPLICATION ENTITY TITLE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.59</td>
<td>ROUTING RULE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.5906</td>
<td>ROUTE LOAD BALANCE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.596</td>
<td>ACTION QUEUE STATUS</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.598</td>
<td>DICOM ERROR MESSAGE QUEUE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.599</td>
<td>DICOM Error Log</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.61</td>
<td>MAG RAD EXAM STATUS CATEGORIES</td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>2006.621</td>
<td>MAG CT PARAMETER</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.623</td>
<td>MAG CR PARAMETER</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.63</td>
<td>MAG RAD LIST DATA ELEMENTS</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.631</td>
<td>MAG RAD LISTS DEFINITION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.634</td>
<td>MAGJ ZLIST SEARCH</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.65</td>
<td>MAG RAD PRIOR EXAMS LOGIC</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.67</td>
<td>MAG RAD CPT MATCHING</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.671</td>
<td>MAG RAD BODY PART</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.672</td>
<td>MAG RAD BODY REGION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.68</td>
<td>MAGJ USER DATA</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.69</td>
<td>MAG VISTARAD SITE PARAMETERS</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.8</td>
<td>BP WORKSTATIONS</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.81</td>
<td>IMAGING WINDOWS WORKSTATIONS</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.82</td>
<td>IMAGING WINDOWS SESSIONS</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.83</td>
<td>DICOM WORKSTATION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.87</td>
<td>DICOM GATEWAY INFORMATION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.911</td>
<td>DICOM GATEWAY INSTRUMENT DICTIONARY</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.912</td>
<td>DICOM GATEWAY MODALITY DICTIONARY</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.913</td>
<td>ARTIFACT KEYLIST</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.914</td>
<td>RETENTION POLICY</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.915</td>
<td>ARTIFACT DESCRIPTOR</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.916</td>
<td>ARTIFACT</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.917</td>
<td>STORAGE PROVIDER</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.918</td>
<td>ARTIFACT INSTANCE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.9191</td>
<td>MAGV GATEWAY CONFIGURATION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.9192</td>
<td>DICOM AE SECURITY MATRIX</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.9193</td>
<td>IMAGING APPLICATION SERVICE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.921</td>
<td>ARTIFACT RETENTION POLICY</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.922</td>
<td>RETENTION POLICY FULFILLMENT</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.923</td>
<td>RETENTION POLICY STORAGE PROVIDER MAP</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.924</td>
<td>STORAGE PROVIDER AVAILABILITY</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.925</td>
<td>TRANSFER STATISTICS</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.926</td>
<td>STORAGE TRANSACTION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.927</td>
<td>QUEUE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.928</td>
<td>QUEUE MESSAGE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.93</td>
<td>IMAGING EVENT AUDIT LOG</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.931</td>
<td>IMAGING EVENT AUDITABLE ACTION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.941</td>
<td>MAG WORK ITEM</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.9411</td>
<td>MAG WORK ITEM HISTORY</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.9412</td>
<td>WORKLIST</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.9413</td>
<td>MAG WORK ITEM STATUS</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.9414</td>
<td>MAG WORK ITEM SUBTYPE</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.9421</td>
<td>MAGV IMPORT STUDY LOG</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="odd">
<td>2006.9422</td>
<td>MAGV IMPORT MEDIA LOG</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td></td>
</tr>
<tr class="even">
<td>2006.95</td>
<td>IMAGE ACCESS LOG</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="odd">
<td>2006.96</td>
<td>IMAGE INDEX CONVERSION</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
<tr class="even">
<td>2006.961</td>
<td>MULTI IMAGE PRINT</td>
<td colspan="2">@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
</tr>
</tbody>
</table>

## Windows Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Windows provides security through the use of user profiles, policies/rights, directory/share permissions and domain configuration. VistA Imaging file servers should be configured as a member servers of the VISN domain. The *VistA Imaging Installation Guide* also defines recommended user profiles, groups and policies to be administered.

## Workstation Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security of an Imaging workstation is the same as any other personal computer located within the Medical Center and should be covered by the Medical Center’s Equipment Security Guidelines and/or policies.

Restricting access to the VistA Imaging workstation by placing the workstation in a secure area (such as a locked office) would be optimal. However, the use of the workstation would be limited to only those assigned to the office. Placing the workstation in an open area accessible by all clinical staff would be beneficial to all but can present a problem of theft or tampering. Physical security of the PC to prevent theft or altering of internal electronic boards is recommended; a cable lock can prevent the opening of the case of the PC box unit.

Security software is required, such as virus detection software and desktop configuration restriction software. Virus protection software must be installed on the servers to protect imaging file servers against viruses. The VA has validated McAfee VirusScan for use on Imaging File Servers and other Imaging components. For guidance in locating security software information, contact the Information Protection and Risk Management (IPRM) office at their web site at [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) . For additional assistance, contact the VA Help Desk. Commercial products are available for controlling access to system setup and files. Policies and profiles can be used to restrict access in a Microsoft Windows workstation environment. The BIOS of all VistA Imaging workstations should be password protected.

### SMS Software, DICOM Gateways and Background Processors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA Security Policy requires that, on many computers, specific software is installed to ensure that the machines are running the most up-to-date virus protection software.

DICOM Gateway Systems and Background Processors must be able to operate continually, without unplanned interruption. While it is acknowledged that any computer that is connected to the network must have adequate virus protection, the provision of this protection cannot interrupt the processing of essential medical data.

VA's SMS and EPO software distribution mechanism can trigger a safety problem because it causes the system to reboot while it might be processing essential data. As a result, the VA’s SMS and EPO software cannot be installed on any VistA DICOM Gateway or Background Processor.

Each site must appoint a person who is responsible for applying Microsoft updates to the DICOM Gateways when Microsoft makes mandatory patches (also known as “Critical Updates and Service Packs”) available. The responsible person should check at least once per week whether any critical updates are available, and make certain that they are installed while the medical software is not active.

The virus protection software should be configured such that it automatically downloads and applies new updates for the virus definition files on a daily basis.

### SMS Software and VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because software distribution/inventory management tools can be used to install inappropriate or unapproved software without an administrator’s knowledge, VistARad workstations must be excluded from Microsoft’s Systems Management Server (SMS) server or similar systems.

> **NOTE:** The installation of unapproved components onto a VistARad diagnostic workstation will result in an adulterated medical device. The use of adulterated medical devices violates US Federal Law (21CFR820).

Information about exclusion and removal of SMS can be found at: [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .

If there are any questions about the contents of these documents, refer to the EIE (VA Enterprise Infrastructure Engineering) portal at: [[<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) /](http://vaww.cis.va.gov/).

## Audit Trails 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging software has several files that can be used to audit usage of VistA Imaging workstations and access to image files.

- The IMAGING WINDOWS WORKSTATIONS file (#2006.81) can be used to review the date and time the Display, Capture, or VistARAD application was installed, the last access date/time the workstation was used, and who last signed onto the workstation. This information is vital for the Imaging system manager to audit workstation usage.
- The IMAGE AUDIT file (#2005.1) records data from deleted image records of the IMAGE file (#2005) and serves as an audit trail for deleted images. When image deletion takes place, the image is deleted off of the magnetic server (if it exists), and the associated specialty package pointer to the image file is deleted. The data from the IMAGE file (#2005) is copied over to the IMAGE AUDIT file (#2005.1) using the same internal entry number. The image residing on the optical jukebox is not deleted, so it can be retrieved (if necessary) by the system manager.
- The IMAGE ACCESS LOG file (#2006.95) tracks users’ access to images and patient records, as well as the copying and deleting of image files. Entries are added to the local IMAGE ACCESS LOG file (#2006.95) by remote users when accessing remote images. Actions of remote users are logged in the same manner as local image access.
- The QUERY/RETRIEVE STATISTICS file (#2006.5733) records requests for and delivery of data to Query/Retrieve SCU
- IMAGING ANNOTATION FILE (#2005.002). This file can be used to view annotation (audit) history for an image. When users with Annotations permission add and save annotations during a session, the log file tracks each annotation added and stores the following user information: name, date and time, and the user’s service. The log file also tracks changes (such as modifications and deletions) that a user with the MAG ANNOTATE MGR key makes to annotations.

## VistA DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VistA DICOM Gateway connects to a VistA system using the M2M RPC Broker. Access to the physical equipment of the DICOM Gateway itself is protected using the features of the Windows™ operating system, and access from the DICOM Gateway to the VistA Hospital Information System is protected using the standard VA Kernel security features.

There are two special cases (see following sections) where automated processes will use these standard security features in a specific fashion.

### Modality Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modality Worklist queries are processed by DICOM Gateways. Such requests are issued by Imaging equipment (“modalities”) when they need patient scheduling information. Under normal circumstances, a DICOM Gateway is able to respond to a Modality Worklist query using only information that is stored locally on the DICOM Gateway. In some special cases, the DICOM Gateway needs to query its VistA Hospital Information System for details that the DICOM Gateway does not store locally. Since “modalities” are lab-equipment that connects to a DICOM Gateway directly through TCP/IP, using the standard DICOM protocol, a DICOM Gateway has no concept of a “VistA user context” for these Modality Worklist queries. In the exception that a DICOM Gateway needs to query its VistA system for old Radiology case information, it will use a special access and verify code that is configured on that DICOM Gateway (stored in encrypted form).

### DICOM Gateway Service Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some processes on a DICOM Gateway are executed in typical “user oriented” sessions: the user logs in, performs a task, and logs out. However, the tasks that embody the main purpose of the DICOM Gateway run for a long time, typically weeks or months on end, and are intended to keep functioning in an automated fashion, that is: without any human interaction.

Since these tasks need to be started at some point in time, a (fully privileged) user will login, and request the menu option that starts the long-running task. From that point on, the task will run and will continue to run until stopped by a system manager.

When the network connection between the DICOM Gateway and the VistA Hospital Information System is interrupted, the DICOM Gateway will recover from this situation, and will periodically attempt to reconnect (at 5 minute intervals). Once the connection is re-established, the DICOM Gateway will continue processing where it left off when the connection was interrupted.

The situation may arise that:

1.  A user logs in with valid credentials.
2.  Start a long-running task on a DICOM Gateway.
3.  Several weeks later change his/her access or verify code on VistA.
4.  Sometime after that, the DICOM Gateway loses its connection with VistA and starts making attempts to reconnect.

At this point in time, the credentials that the user provided to the DICOM Gateway (and that the DICOM Gateway will continue to use when attempting to reconnect to the VistA system) will no longer be valid, and attempts to reconnect will fail.

Since it is essential that the DICOM Gateway should be capable of continuing to perform its function, without human interaction, a site can establish a special “service account” for which the access and verify codes will not expire. When a DICOM Gateway cannot re-establish a network connection as a result of the scenario described above, the DICOM Gateway will:

1.  Send an e-mail message to a local mail group warning site management that valid credentials need to be re-established
2.  Use the “service account” to continue processing, until a human is available to re-establish valid credentials on the DICOM Gateway.

> The DICOM Gateway service account must have the following:

- MAG VIX ADMIN security key assigned to it
- MAG DICOM VISA assigned to it as a secondary menu option
- OR CPRS GUI CHART assigned to it as a secondary menu option

### Kernel RPC Broker Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two RPC Broker routines are incorporated into the DICOM Gateway software:

> Routine Used For  
> XLFDT Date and time formatting  
> XUSRB1 Encrypt/decrypt access and verify codes

## HDIG Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hybrid Image DICOM Gateway (HDIG) uses a set of security mechanisms to protect the integrity of the VistA system and the data that it stores:

- HDIG Service account
- Apache Tomcat administrator account
- AE Security Matrix

### HDIG Service Account 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hybrid Image DICOM Gateway (HDIG) uses the DICOM Gateway service account to connect to VistA and to run the services that it provides. This account is also used by the (legacy) DICOM Gateway and is described in section *2.13.2 DICOM Gateway* Service Account.

The service account that the HDIG uses to connect to VistA is configured when the HDIG is installed for the first time. Users set the account credentials when they run the HDIG Service Installation Wizard as illustrated in the following screenshot.

![](vista-imaging-system-security-guide/002.png)

For more information about the HDIG Service Installation Wizard and the requirements for the accounts whose credentials are set when the HDIG is installed for the first time, see the *VistA Imaging DICOM Gateway Installation Guide*.

The credentials for the DICOM Gateway service account are stored in an XML configuration file. The passwords for the HDIG service account are encrypted. When the DICOM Gateway service account credentials expire or when they are changed and the HDIG can no longer connect to VistA, it sends a notification that the credentials of the DICOM Gateway service account are invalid. The email addresses to which the HDIG sends notifications for invalid service account credentials are also specified when the HDIG is installed for the first time.

After initial installation, authorized users can change the password for the HDIG service account and the email addresses to which the HDIG sends notifications when it detects invalid service account credentials through the HDIG statistics page.

To change the password of the DICOM Gateway service account and the email address (or addresses) for notifications of invalid DICOM Gateway service account credentials and error in the processing flow, users must have:

- MAG VIX ADMIN security key
- MAG DICOM VISA secondary menu option
- OR CPRS GUI CHART secondary menu option

For more information about accessing the HDIG statistics page and changing the password or the email addresses for notification for invalid credentials, see the *VistA Imaging DICOM Gateway User Guide*.

### Apache Tomcat Administrator Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Apache Tomcat administrator account is used to run the HDIG service in the Tomcat environment on the local system. This account and its credentials are also configured when the HDIG is installed for the first time.

The following image shows the prompts to specify the credentials of the Apache Tomcat administrator account that appears when users install the HDIG for the first time.

![](vista-imaging-system-security-guide/003.png)

For more information about the Apache Tomcat administrator account, see the *VistA Imaging DICOM Gateway Installation Guide.*

### DICOM AE Security Matrix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authorized users can control access to the VistA system and the services the HDIG supports through the DICOM AE Security Matrix. The DICOM AE Security Matrix is the file DICOM AE SECURITY MATRIX (#2006.9192). It includes the configuration settings of all remote device that use the DICOM services the HDIG provides to connect to the VistA system. Only devices listed in the file can access the VistA system. Each device can only use the service or services specified for the device in the DICOM AE SECURITY MATRIX.

To configure the DICOM AE SECURITY MATRIX, users must have:

- MAG SYSTEM security key
- Access to the Imaging System Manager menu \[MAG SYS MENU\]

For more information about the DICOM AE Security Matrix, see the *VistA Imaging DICOM Gateway Installation Guide*.

### Security Keys Required for Deleting a Study by Accession Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authorized users can delete studies stored in VistA by accession number.

To delete a study by accession number users must have:

- MAG SYSTEM security key
- MAG DELETE security key
- Access to the Imaging System Manager menu \[MAG SYS MENU\]

For more information about deleting studies by accession number, see the *VistA Imaging Technical Manual*.

### Security Mechanisms for the Logs in that Record HDIG Activities 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HDIG logs its activities in several logs.

- Application log

> The Application log is encrypted because it may contain protected health information. Access to the Application log is restricted to authorized users. Users need the following to access the Application log:

- MAG VIX ADMIN security key
- MAG DICOM VISA VistA menu

> Users must be authenticated to access the application log. For information about accessing the Application log, see the *VistA Imaging DICOM Gateway User Guide.*

- HDIG Summary log

> The HDIG Summary log is one of the logs of the Hybrid DICOM Image Gateway (HDIG). It is useful for detecting and correcting errors in the operation of the HDIG, because it contains troubleshooting information in plain language – a format that is simple and easy to read and understand. In addition to this, the log is not encrypted and it can be accessed by authorized support and administrative personnel. For information about accessing the Application log, see the *VistA Imaging DICOM Gateway User Guide.*

- Audit log

> The Audit log records system level events, such as HDIG startup and shutdown. It does not contain protected health information (PHI) or any other type of patient information.

> Access to the Audit log is restricted to authorized VA personnel (typically the VistA administrator and the Security Officer).

> All events written to the Audit log are also written to the Application log. This enables VistA Imaging coordinators and administrators to access information when troubleshooting the HDIG or trying to identify causes of problems in its operation.

### Patient Security Logging for Sensitive Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Security log records all attempts to access and retrieve the records of sensitive patients based on the user account credentials (DUZ).

For more information about the Security log, see the *PIMS V5.3 ADT Module User Manual Security Officer Menu*.

## Background Processor Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Background Processor (BP) applications manage the storage and distribution of Clinical images both within the local area network (LAN) and remote storage within the VA wide area network (WAN). It is a requirement of the VistA Imaging system that the applications operate 24/7. The BP Queue Processor is responsible not only for file transmissions, but also network grooming by way of purges to ensure that adequate space is available for newly acquired images.

Since these tasks need to be started at some point in time, a (fully privileged) user will log in and start the Queue Processor. From that point on, the task will run and will continue to run until stopped by a system manager.

When the network connection between the BP Server(s) and the VistA Hospital Information System is interrupted, the BP Server(s) will recover from this situation, and will periodically attempt to reconnect (at 3 minute intervals). This reconnection will be attempted, without human interaction. A site can establish a special “service account” for which the access and verify codes will not expire.

Once the connection is re-established, the BP Server(s) will continue processing where it left off when the connection was interrupted.

## References 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following references for the VistA Imaging System are available through the VistA Imaging website [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .
- Installation manuals, technical manual, user manuals, release notes, planning document, and DICOM conformance statements.
- References for Windows can be obtained from the Microsoft Corporation.
This page intentionally left blank.

# Appendix A VIX Security Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix contains security information specific to the VistA Imaging Exchange (VIX) service. Information in this appendix applies only to VA sites that have implemented a VIX.

The VIX is an optional VistA Imaging component used to exchange images between VA sites and the Department of Defense (DoD). In the case of VIX-supported VA-VA image sharing, a VIX can be at the requesting site only, the responding site only, or at both sites. In the case of VA-DoD image sharing, a VIX must be at the applicable VA site and must also be able to communicate with the CVIX (the centralized VistA Imaging Exchange service).

After a VA site implements a VIX, the VIX handles all local requests for remotely stored images (including Clinical Display remote image views). The VIX also serves copies of locally stored images to remote requestors (other VA sites and DoD clinicians via the CVIX).

## The VIX and CVIX are described in detail in the *VIX Administrator’s Guide*.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A.1 Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX will automatically notify the VistA Imaging development group when it starts or restarts.

## A.2 Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the VIX processes data requests from a remote system, the VIX uses web services for metadata and HTTP ‘get’ commands for images and image-like artifacts.

Transmission frequency is dependent on the requesting party.

Data transfers can be synchronous or asynchronous depending on the nature of the request; the VIX uses HTTP response codes to acknowledge requests.

## A.3 Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX does not archive data. The VIX temporarily caches data and does not replace the existing Imaging archive.

## A.4 Contingency Planning 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As defined for VistA Imaging in general (see section 2.4).

## A.5 Interfacing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX incorporates the Laurel Bridge DCF DICOM Toolkit and the Aware JPEG2000 Toolkit. For details about these toolkits, refer to the *VIX Administrator’s Guide*.

## A.6 Electronic Signatures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX does not implement any new electronic signatures.

## A.7 Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX does not have any security-related menu options on VistA.

## A.8 Security Keys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MAG VIX ADMIN key gives the holder access to the web-based VIX transactions log. For more information, see the *VIX Administrator’s Guide*.

## A.9 File Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As defined for VistA Imaging in general (see section 2.9).

## A.10 Software Pushes and the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX server is an Imaging component, and Imaging components are FDA-regulated medical devices that cannot be modified by unauthorized parties in a production environment. Because software distribution/inventory management tools can install inappropriate or unapproved software without a local administrator’s knowledge, sites must exclude the VIX server from automated update systems.

## A.11 VistA Account for BHIE Framework Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of the MAG\*3.0\*104 VIX, the VistA account needed to support DoD image accesses is no longer needed. Credentialing is now handled using Station 200 data and the CVIX (Centralized VistA Imaging Exchange) service.

Sites that have previously established a VistA account to support DoD image access may disable the account after updating their VIX to MAG\*3.0\*104.

## A.12 References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIX documentation is available at [<u>REDACTED</u>](https://vaww.edis2.med.va.gov/main) .

## A.13 Official Policies 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As defined for VistA Imaging in general (see section 2.16).

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                  |                                                                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Architecture     | The design of the components of a computer, network, or software system.                                                                                                                          |
| Archive          | The long-term storage of data or images.                                                                                                                                                          |
| Audit trail      | Record of activity on a particular file or computer.                                                                                                                                              |
| BHIE             | Bidirectional Health Information Exchange                                                                                                                                                         |
| DoD              | Department of Defense                                                                                                                                                                             |
| DICOM            | Digital Imaging and Communications in Medicine. A medical imaging standard, DICOM is standard for Radiology equipment and is being adopted by the other members of the medical imaging community. |
| File             | All the data that describes a document or image.                                                                                                                                                  |
| File protection  | Techniques for preventing files from being erased.                                                                                                                                                |
| File server      | A machine where shared software and data files are stored.                                                                                                                                        |
| Frame grabber    | A device that translates a frame from a video image into a still digitized image.                                                                                                                 |
| High resolution  | An image or a display that has more pixels per inch than a conventional display.                                                                                                                  |
| HDIG             | Hybrid DICOM Image Gateway: An image gateway that combines the legacy DICOM Gateway and the new VISA Gateway. It implements DICOM services.                                                       |
| Image            | The computerized representation of a picture, or graphic.                                                                                                                                         |
| Image abstract   | A “thumbnail” version of an image, which requires less computer processing resources to display than the actual image.                                                                            |
| Image group      | A group of images associated with a medical examination.                                                                                                                                          |
| Image processing | The translation of an image into a digital computer language so that it may be manipulated in size, color, clarity, or to enhance portions of it.                                                 |
| Image resolution | The fineness or coarseness of an image.                                                                                                                                                           |
| Imaging system   | Collection of units that work together to capture and recreate images.                                                                                                                            |
| JCAHO            | Joint Commission on Accreditation of Health Organizations                                                                                                                                         |
| Jukebox          | A device that holds multiple optical discs and can swap them in and out of the drive as needed.                                                                                                   |
| Login (Logon)    | Procedure for gaining access to the system or program.                                                                                                                                            |
| Multimedia       | Combining more than one medium for the dissemination of information (e.g., text, graphics, full video motion, audio).                                                                             |
| MUMPS            | Massachusetts General Hospital Utility Multi-Programming System                                                                                                                                   |
| NCAT             | Neurocognitive Assessment Tool                                                                                                                                                                    |
| Off-line         | Something that is not available for access on the system.                                                                                                                                         |
| On-line          | Something that is available for access on the system.                                                                                                                                             |
| Resolution       | Measure of output quality (dpidots per inch) or halftone quality (lpilines per inch).                                                                                                           |
| Retrieval        | The ability to search for, select, and display an image or other data from storage.                                                                                                               |
| RGB              | Red, Green, Blue. The colors used in varying combinations and intensities on monitors, TV screens, and other color displays.                                                                      |
| RPC              | Remote Procedure Call                                                                                                                                                                             |
| Server           | A computer that is dedicated to a task (generally data storage).                                                                                                                                  |
| Storage media    | The physical device onto which data is recorded.                                                                                                                                                  |
| User preferences | The preferences that each user sets in the User Preferences window that control the circumstances and ways in which the Imaging package displays images.                                          |
| VistA            | <u>V</u>eterans Health <u>I</u>nformation <u>S</u>ystem <u>T</u>echnology <u>A</u>rchitecture. VistA replaces DHCP.                                                                               |
