---
title: Community Care Referral and Authorization (CCRA) Technical Manual (Updated with patches GMRC*3*99, 106, 123)
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: Community Care Referral and Authorization (CCRA)  (Updated with patches GMRC*3*99, 106, 123)
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
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
  - patch
  - link
  - table
  - contents
  - ccra
  - message
  - vista
  - install
  - exhibit
  - community
page_count: 0
word_count: 7343
section_count: 13
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/ccra_gmrc_patch_technical_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/ccra_gmrc_patch_technical_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

Community Care Referral and Authorization (CCRA) Software as a Service (SaaS) and Integration Development

GMRC 99, GMRC 106, and GMRC 123

Patch Technical Manual

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/001.png)

June 2019Version 6.0

Office of Information and Technology (OIT)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table>
<caption>Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.</caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 23%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th>Version</th>
<th>Date</th>
<th>Author</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0.1</td>
<td>04/02/2018</td>
<td><mark>REDACTED</mark></td>
<td>Initial draft</td>
</tr>
<tr class="even">
<td>0.2</td>
<td>04/12/2018</td>
<td><mark>REDACTED</mark></td>
<td>Review with comments</td>
</tr>
<tr class="odd">
<td>0.3</td>
<td>04/12/2018</td>
<td><mark>REDACTED</mark></td>
<td>Review with comments</td>
</tr>
<tr class="even">
<td>0.4</td>
<td>04/16/2018</td>
<td><mark>REDACTED</mark></td>
<td><p>QC Review</p>
<ul>
<li><blockquote>
<p>Title page: Added version number</p>
</blockquote></li>
<li><blockquote>
<p>Throughout doc:</p>
</blockquote></li>
</ul>
<ul>
<li><p>Made minor changes to language and grammar</p></li>
<li><p>Applied consistent text styles</p></li>
<li><p>Replaced “the VA” with “VA” where appropriate</p></li>
<li><p>Added alt text to all exhibits</p></li>
</ul>
<ul>
<li><blockquote>
<p>Exhibits 1–3, 6, and 8–25: Replaced non-508-compliant figures with 508-compliant images</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Section 1: Updated intro text</p>
</blockquote></li>
<li><blockquote>
<p>Appendix A: Replaced table of acronyms</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>1.0</td>
<td>04/18/2018</td>
<td><mark>REDACTED</mark></td>
<td>DPM Review</td>
</tr>
<tr class="even">
<td>2.0</td>
<td>04/26/2018</td>
<td><mark>REDACTED</mark></td>
<td><ul>
<li><p>Update required associated patch numbers in document to match Patch Description document</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>2.1</td>
<td>07/18/2018</td>
<td><mark>REDACTED</mark></td>
<td><p>Updates to include GMRC Patch 106</p>
<ul>
<li><blockquote>
<p>Section 2.1.6: Added this section with details about Patch 106</p>
</blockquote></li>
<li><blockquote>
<p>Exhibit 4: Added this image</p>
</blockquote></li>
<li><blockquote>
<p>Section 4: Added a new routine to the list</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>2.2</td>
<td>07/18/2018</td>
<td><mark>REDACTED</mark></td>
<td><p>QC Review</p>
<ul>
<li><blockquote>
<p>Title page: Updated title, month, and version number</p>
</blockquote></li>
<li><blockquote>
<p>Footer: Updated title and month</p>
</blockquote></li>
<li><blockquote>
<p>Throughout doc:</p>
</blockquote></li>
</ul>
<ul>
<li><p>Made minor changes to language and grammar</p></li>
<li><p>Updated exhibit numbering</p></li>
</ul>
<ul>
<li><blockquote>
<p>Exhibits 5–9: Added linked references within the text</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>3.0</td>
<td>07/23/2018</td>
<td><mark>REDACTED</mark></td>
<td>DPM Review</td>
</tr>
<tr class="even">
<td>3.1</td>
<td>08/21/2018</td>
<td><mark>REDACTED</mark></td>
<td><ul>
<li><p>Updated Section 1 – Included overview of both patches</p></li>
<li><p>Updated Section 2 – Removed patch specific information, as the section applies to both patches</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3.2</td>
<td>08/21/2018</td>
<td><mark>REDACTED</mark></td>
<td><p>Updates</p>
<ul>
<li><p>Section 2.1.3.1: Updated the installation instructions for Patch 99</p></li>
<li><p>Section 2.1.3.1: Updated the installation instructions for Patch 99</p></li>
<li><p>Section 4: Added text to specify which routine applies to which patch</p></li>
</ul></td>
</tr>
<tr class="even">
<td>4.0</td>
<td>08/21/2018</td>
<td><mark>REDACTED</mark></td>
<td>DPM Review</td>
</tr>
<tr class="odd">
<td>4.1</td>
<td>09/25/2018</td>
<td><mark>REDACTED</mark></td>
<td>Section 2.1.3: Updated the installation instructions for patch 99</td>
</tr>
<tr class="even">
<td>4.2</td>
<td>09/25/2018</td>
<td><mark>REDACTED</mark></td>
<td>QC review of updated installation instructions</td>
</tr>
<tr class="odd">
<td>5.0</td>
<td>09/25/2018</td>
<td><mark>REDACTED</mark></td>
<td>DPM Review</td>
</tr>
<tr class="even">
<td>5.1</td>
<td>06/06/2019</td>
<td><mark>REDACTED</mark></td>
<td><p>Updated for patch 123</p>
<ul>
<li><p>Updated Section 1 for introduction of patch</p></li>
<li><p>Updated Section 2.1.3 software requirements</p></li>
<li><p>Created Section 2.1.7, with new exhibit for installation of patch</p></li>
<li><p>Updated Section 4 with new routine information</p></li>
<li><p>Updated Section 7.1 with new HL7 parameters</p></li>
<li><p>Updated Section 9 with security information</p></li>
<li><p>Updated Section 12, 12.4, 12.5 and 12.6, troubleshooting</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>6.0</td>
<td>06/17/2019</td>
<td><mark>REDACTED</mark></td>
<td>Program Manager Review</td>
</tr>
</tbody>
</table>

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.

Table of Contents

Table of Exhibits

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Document Orientation](#document-orientation)
    - [Disclaimers](#disclaimers)
    - [References](#references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [System Requirements](#system-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Software Requirements](#software-requirements)
    - [Installation of Patch 99](#installation-of-patch-99)
    - [Enable the Interface Link](#enable-the-interface-link)
    - [Verify that the Interface Link Is Running](#verify-that-the-interface-link-is-running)
    - [Installation of Patch 106](#installation-of-patch-106)
    - [Installation of Patch 123](#installation-of-patch-123)
- [Files](#files)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [HL7 Messaging](#hl7-messaging)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
- [Security](#security)
- [Archiving](#archiving)
- [Non-Standard Cross-References](#non-standard-cross-references)
- [Troubleshooting](#troubleshooting)
  - [Check the System Link Monitor](#check-the-system-link-monitor)
  - [Stop/Start the Interface Link](#stopstart-the-interface-link)
  - [Edit the Logical Link Parameters](#edit-the-logical-link-parameters)
  - [Edit the Application Parameters](#edit-the-application-parameters)
  - [Edit the Protocols](#edit-the-protocols)
  - [View HL7 Message Transmission Log](#view-hl7-message-transmission-log)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
- [Appendix A: Acronyms and Abbreviations](#appendix-a-acronyms-and-abbreviations)
HealthShare Referral Manager (HSRM) is an enterprise-wide system in support of community care used by facility community care staff to generate referrals and authorizations for Veterans receiving care in the community. Clinical and Department of Veterans Affairs (VA) community care staff located at VA medical centers, outpatient clinics, community-based outpatient clinics, and Veterans Integrated Service Network offices use this solution to enhance Veteran access to care. HSRM is an integral component of the community care information technology (IT) architecture that allows Veterans to receive care from community providers.
HSRM allows VA to transition from what is currently a largely manual process to a more streamlined process that generates standardized referrals and authorizations according to clinical and business rules. HSRM supports clinical and administrative processes expected to:
- Seamlessly provide eligible Veterans with prompt referrals to a community provider of their choice
- Provide community providers with referrals and authorizations consistent with industry standards
- Decrease the administrative burden on VA clinical and facility community care staff members by establishing clinical and business pathways that reflect best practices, consistent outcomes, and reduced turnaround times, along with a solution that automates those pathways
- Facilitate communication between facility community care staff and community providers via a unified platform that enables the secure exchange of medical information
This document contains the instructions to install patch GMRC\*3.0\*99 into the Veterans Health Information Systems and Technology Architecture (VistA) system. This patch will load the routines and protocols necessary for a Health Level 7 (HL7) interface messaging process for the Community Care Referral and Authorization (CCRA) project. It also contains the instructions to install patch GMRC\*3.0\*106 This patch contains changes to the code that generates the HL7 consult messages introduced by patch GRMC\*3.0\*99. The CCRA Project required the addition of the following information to the existing HL7 message to support additional functionality in HealthShare Referral Manager:
- The addition to IN1 segments to support other health insurance (OHI)
- The addition of the Reimbursable flag to the interface to communicate to HSRM that the VA may not be the primary insurance plan for the requested service
- The addition of the division or site ID that is separate from the station ID of the site hosting the VistA instance. This is necessary for VistA instances supporting multiple division sites so that HSRM has the division identifier
This document also contains instructions to install patch GMRC\*3.0\*123 into the VistA system. This patch builds on the functionality of patches 99 and 106 and contains additional OHI information being sent from VistA to HSRM. The additional OHI includes:
- Plan ID, Coordination of Benefits and Last Verified Date
- A Precert Flag, if it exists in VistA, is added to a new IN3 segment in the HL7 message. If the Precert data is blank in VistA the IN3 segment is not included
- Referring and/or Primary Care Provider NPI value(s)
Patch 123 also allows for HSRM to respond back to VistA with consult updates. This includes:
- Update to the consult status
- Updates to notes within the consult related to the following HSRM values: Consult Status, Referral Date, Referral Expiration Date and Program Authority
Note that in order for HSRM to update the VistA system, the user in HSRM must exist in VistA. This patch checks the user’s email address within the New Person file (#200). If the person exists in this file, then the data can be filed in VistA. If not, an application NACK message is sent back to HSRM to denote that the message was rejected, and the data not filed. This patch includes a new HL7 logical link used for this application NACK.
Note also that the HL7 process to receive data from HSRM into VistA uses whatever listener port the specific site uses. It is assumed there will be a listener port. The name of said port is not known to this process nor is needed in order to install the patch and run the associated software. Each site should already have a listener port set up.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to detail how to install this patch on the VistA system. It is intended for personnel who navigate and maintain the HL7 message processing system for community care users.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinicians using the Computerized Patient Record System (CPRS) sometimes need to create a consult for services outside of the VA facility. This patch updates the protocols necessary to allow CPRS to send those community care consult requests from VistA to HSRM using VistA’s existing HL7 message processing technology. HSRM is a commercial off-the-shelf product used to track these non-VA consult services.

> **NOTE:** The term “non-VA consult services” stems from the fact that VistA is generating consult requests that are to be delivered outside VA facilities. The request is sent via HL7 message to HSRM, where the consult is tracked further. However, the consult itself is delivered in a non-VA environment, which is what pushes the consult into community care.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience for this technical manual is local IT support, management, development personnel, and those responsible for maintaining the VistA HL7 architecture at the VA site.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at VA by employees of the federal government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code, this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties and makes no guarantees, express or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by VA of these websites or the information, products, or services contained therein. VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of VA.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA Software Document Library (VDL) – HL7 (VistA messaging) section, including:
- Technical Manual
- Site Manager Developer Manual v 1.6\*161
- Community Care Referral and Authorization Patch 99 Technical Manual
- Consult/Request Tracking Technical Manual

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is implemented using the VistA Kernel and Installation Distribution System (KIDS). During the installation process the user will be asked to identify the Internet protocol (IP) address and port for the HSRM server that is provided to facilities during initial implementation of HSRM.

After implementation, any maintenance required should be handled through the standard VistA HL7 message processing options.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is a release for GMRC.

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. This patch does not require any changes to the hardware currently in use at the site.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Patches GMRC\*3.0\*75, GMRC\*3.0\*85, GMRC\*3.0\*96 must already be installed in order to install this patch. GMRC\*3.0\*99 needs to be installed before GMRC\*3.0\*106, and both must be installed before GMRC\*3.0\*123.

> **NOTE:** GMRC\*3.0\*112 was created as a required emergency patch in April 2019 to resolve an issue where control characters within consults were causing looping problems within the VistA HL7 software. This patch must be installed before GMRC\*3.0\*123. Its installation follows standard VistA methodology within the KIDS menu options.

This patch is designed to make use of existing HL7 hardware and software. No updates to these existing systems, user setup, or configuration is necessary beyond the information required within the installation instructions themselves. The setup of the HSRM system is outside the scope of this patch.

### Installation of Patch 99

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes the steps followed to load the patch into VistA. These steps can be completed with users on the system. This should take less than 15 minutes to configure.

> **NOTE:** Patches GMRC\*3.0\*75, GMRC\*3.0\*85, GMRC\*3.0\*96 must already be installed in order to install this patch. This patch should take less than 15 minutes to install.

The IP address and port for the HealthShare Server will be provided when HealthShare Referral Manager is connected to the site. If you have not been provided this information by the implementation manager, you are instructed to enter the following:

> IP address: 0.0.0.0

> Port Number: 0000

Please note that the installation of this patch is not complete until all the steps are followed. At a high level, these steps are:

1.  Load the patch.
2.  Install the patch (shown here).
3.  Enable the logical link (see Section 2.1.4).
4.  Confirm that the link is operational by sending a message.

Once the installation is complete, creation of a consult using a community care service should generate an HL7 message to HSRM.

#### Setup/Configure Instructions

1.  Choose the PackMan message containing this patch.
5.  Choose the INSTALL/CHECK MESSAGE PackMan option.
6.  From the KIDS menu, select the Installation menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter GMRC\*3.0\*99.
    1.  Back up a Transport Global – This option creates a backup message of any routines exported with this patch. It does not back up any other changes (e.g., data dictionaries, templates).
    2.  Compare Transport Global to Current System – This option allows you to view all changes that will be made when this patch is installed. It compares all components of this patch (e.g., routines, data dictionaries, templates).
    3.  Verify Checksums in Transport Global – This option allows you to ensure the integrity of the routines that are in the transport global.
7.  From the Installation menu, select the Install Package(s) option; when prompted for the INSTALL NAME, enter GMRC\*3.0\*99.
8.  At the prompt, "Enter the Coordinator for Mail Group 'GMRCCCRA NOTIFICATIONS:", enter the name of person responsible for populating this mail group with users. This VistA Mail Group will receive notifications when problems occur with transmitting consults.
9.  At the prompt, “Enter the IP address for the HealthShare server,” enter the IP address for the HealthShare server you will send the NON-VA Consults to. (The IP address for the HealthShare server will be provided when HealthShare Referral Manager is connected to the site. If you have not been provided this information by the implementation manager, you are instructed to enter the following IP address: 0.0.0.0.)
10. At the prompt, “Enter the Port for the HealthShare server,” enter the port the HealthShare server is listening on. (The port for the HealthShare server will be provided when HealthShare Referral Manager is connected to the site. If you have not been provided this information by the implementation manager, you are instructed to enter the following port number: 0000.)
11. If prompted, “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//,” respond NO.
12. When prompted, “Want KIDS to INHIBIT LOGONs during the install? NO//,” respond NO.
13. If prompted, “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//,” respond NO.
14. If prompted, “Delay Install (Minutes): (0 - 60): 0//,” respond 0.

An example of KIDS install dialogue for this patch is provided in Exhibit 1.

<span id="_Ref511381860" class="anchor"></span>Exhibit 1: Sample Patch 99 Install Dialogue

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/002.png)

> **NOTE:** In this example, the highlighted x’s are used instead of numbers to denote user responses and an IP address and relevant information are not identified in a public document. The sites will have to determine the correct values for these fields before they will be able to install the patch. If the user gets to this point and does not have the required information, he or she will have to exit and uninstall the patch, then come back with the correct information to complete the installation.

Once installation is completed, the system will run the post-install routine, using the user-entered responses for IP address and port to update the HL7 application protocols and logical link values needed for the CCRA project. This avoids the necessity for the user to update these protocols and links manually within VistA.

> **NOTE:** If the IP address or port later need to be changed for any reason, instructions can be found in Section 12.

### Enable the Interface Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enable the HL7 interface link created by this patch, go into the VistA HL main menu and select the Filer and Link Management Options. From there, select the SL Stop/Start Links option, as shown in Exhibit 2.

<span id="_Ref511382626" class="anchor"></span>Exhibit 2: Screenshot: Start the Logical Link GMRCCCRA

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/003.png)

Once this logical link is thus enabled, messages can proceed through the interface.

### Verify that the Interface Link Is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA allows the user to ping a link to verify that it is running properly and that the connections are in place. In the Filer and Link Management options, select the PI Ping (TCP Only) option, as shown in Exhibit 3. If an acknowledgement is not received as shown here, then there is a problem with the connection. Verify the logical link, application parameters, and protocols. If the problem persists, call the Enterprise Service Desk to check on the HSRM side of the connection, and refer to the Site Manager Developer Manual in the VDL as needed.

<span id="_Ref511383285" class="anchor"></span>Exhibit 3: Screenshot: Ping TCP/IP Port

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/004.png)

Note that once the patch is installed and the link is working, an HL7 message is created within VistA when a community care or Department of Defense treatment consult service is entered and signed. This triggers the message creation to HSRM.

### Installation of Patch 106

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please note that the installation of this patch is not complete until all the steps are followed. At a high level, these steps are:

1.  Load the patch.
15. Install the patch (shown here).

#### Setup/Configure Instructions

16. Choose the PackMan message containing this patch.
17. Choose the INSTALL/CHECK MESSAGE PackMan option.
18. From the KIDS menu, select the Installation menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter GMRC\*3.0\*106.
1.  Back up a Transport Global – This option creates a backup message of any routines exported with this patch. It does not back up any other changes (e.g., data dictionaries, templates). In order to back out this patch, this option must be used.
2.  Compare Transport Global to Current System – This option allows you to view all changes that will be made when this patch is installed. It compares all components of this patch (e.g., routines, data dictionaries, templates).
3.  Verify Checksums in Transport Global – This option allows you to ensure the integrity of the routines that are in the transport global.
19. From the Installation menu, select the Install Package(s) option; when prompted for the INSTALL NAME, enter GMRC\*3.0\*106.
20. If prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//,” respond NO.
21. When prompted, “Want KIDS to INHIBIT LOGONs during the install? NO//,” respond NO.
22. If prompted, “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//,” respond NO.
23. If prompted, “Delay Install (Minutes): (0 - 60): 0//,” respond 0.

An example of KIDS install dialogue for this patch is provided in Exhibit 4.

<span id="_Ref519677430" class="anchor"></span>Exhibit 4: Sample Patch 106 Install Dialogue

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/005.png)

> **NOTE:** Patch 106 includes enhancements to Patch 99, adding data to the HL7 messages without changing any processes.

### Installation of Patch 123

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please note that the installation of this patch is not complete until all the steps are followed. At a high level, these steps are:

1.  Load the patch
24. Install the patch (shown here)

    Installing the patch may require setting up a new logical link, CCRA-NAK. The patch includes a pre-install routine which will check the VistA system to see if this link has been created. If not, it will ask the installer for the Heath Connect Server IP Address and Port values, and it will create the link. A sample of the creation of this link is included in the example below.

#### Setup/Configure Instructions

1.  Choose the PackMan message containing this patch.
25. Choose the INSTALL/CHECK MESSAGE PackMan option.
26. From the KIDS menu, select the Installation menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter GMRC\*3.0\*123.
1.  Back up a Transport Global – This option creates a backup message of any routines exported with this patch. It does not back up any other changes (e.g., data dictionaries, templates). In order to back out this patch, this option must be used
2.  Compare Transport Global to Current System – This option allows you to view all changes that will be made when this patch is installed. It compares all components of this patch (e.g., routines, data dictionaries, templates)
3.  Verify Checksums in Transport Global – This option allows you to ensure the integrity of the routines that are in the transport global
27. From the Installation menu, select the Install Package(s) option; when prompted for the INSTALL NAME, enter GMRC\*3.0\*123
28. If prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//,” respond NO
29. When prompted, “Want KIDS to INHIBIT LOGONs during the install? NO//,” respond NO
30. If prompted, “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//,” respond NO.
31. If prompted, “Delay Install (Minutes): (0 - 60): 0//,” respond 0

    An example of KIDS install dialogue for this patch is provided in Exhibit 5.

> <span id="_Toc11708772" class="anchor"></span>Exhibit 5: Sample Patch 123 Install Dialogue

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select INSTALL NAME: GMRC*3.0*123 4/24/19@11:55:48</p>
<p>=&gt; GMRC*3.0*123 ;Created on Apr 24, 2019@11:50:10</p>
<p>This Distribution was loaded on Apr 24, 2019@11:55:48 with header of</p>
<p>GMRC*3.0*123 ;Created on Apr 24, 2019@11:50:10</p>
<p>It consisted of the following Install(s):</p>
<p>GMRC*3.0*123</p>
<p>Checking Install for Package GMRC*3.0*123</p>
<p>Install Questions for GMRC*3.0*123</p>
<p>Incoming Mail Groups:</p>
<p>Enter the Coordinator for Mail Group 'GMRCCCRA NOTIFICATIONS':</p>
<p>TESTUSER,ONE//</p>
<p>OT</p>
<p>Want KIDS to INHIBIT LOGONs during the install? NO//</p>
<p>Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//</p>
<p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt.</p>
<p>Enter a '^' to abort the install.</p>
<p>DEVICE: HOME// HOME (CRT)</p>
<p>GMRC*3.0*123</p>
<p>--------------------------------------------------------------------------</p>
<p>Apr 24, 2019@11:56:06</p>
<p>Build Distribution Date: Apr 24, 2019</p>
<p>Installing Routines:</p>
<p>Apr 24, 2019@11:56:06</p>
<p>Running Pre-Install Routine: LINK^GMRC123P</p>
<p>Checking VistA system for CCRA-NAK logical link setup...</p>
<p>*NOTE: The following section is from the GMRC123P pre-install</p>
<p>routine. It is used to set up the CCRA-NAK logical link for HL7</p>
<p>processing. If the CCRA-NAK link already exists this portion of</p>
<p>the install will be skipped.</p>
<p>CCRA-NAK logical link being set up now. We'll need some information from</p>
<p>you.</p>
<p>Please have the HealthConnect server IP address and Port number ready.</p>
<p>PLEASE ENTER THE HEALTHCONNECT SERVER IP ADDRESS: <mark>xxx.xxx.xxx.xxx</mark></p>
<p>PLEASE ENTER THE HEALTHCONNECT SERVER PORT NUMBER: <mark>xxxx</mark></p>
<p>*NOTE: End of pre-install process.</p>
<p>Installing MAIL GROUP</p>
<p>Installing HL7 APPLICATION PARAMETER</p>
<p>Installing PROTOCOL</p>
<p>Apr 24, 2019@11:58:10</p>
<p>Updating Routine file...</p>
<p>Updating KIDS files...</p>
<p>GMRC*3.0*123 Installed.</p>
<p>Apr 24, 2019@11:58:10</p>
<p>No link to PACKAGE file</p>
<p>NO Install Message sent</p>
<p>--------------------------------------------------------------------------</p>
<p>------</p>
<p>+------------------------------------------------------------+</p>
<p>100% | 25 50 75 |</p>
<p>Complete +------------------------------------------------------------+</p>
<p>Install Completed</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** Patch 123 includes enhancements to Patches 99 and 106, adding data to the HL7 messages. A new process allows valid HSRM users to update consult information in VistA. No other processes are changed.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No VistA file structures are affected by this patch. Data is updated within the existing protocol file related to the new HL7 message processing for community care.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch includes the following routines:

GMRCCCRA: This new routine is used by the VistA system to generate the appropriate HL7 messages when a community care consult is entered into the system. (Patches 99, 106, and 123)

POST^GMRCP99: This new routine uses the information entered by the user during the installation process to set up the appropriate HL7 application protocols and logical links. (Patch 99)

GMRCGUIB: This existing routine is modified at the line tag CMT. A line of code was added to verify that a consult was created for community care; if so, it will trigger a new HL7 message to HSRM that includes the comment. (Patch 99)

GMRCACMT: This existing routine is modified at the line tag COMMENT. A line of code was added to verify that a consult was created for community care; if so, it will trigger a new HL7 message to HSRM that will include the comment. (Patch 99)

GMRCCCR1: This is a subroutine from GMRCCCRA created in Patch 106 and updated for patch 123. It also contains subroutines used by the GMRCCCRI routine.

GMRCCCRI: This routine is used by VistA to parse and process the consult update received from HSRM. This routine is new in patch 123.

LINK^GMRC123P: This is a pre-install routine used by patch 123. It checks to see if the CCRA-NAK logical link exists in the system. If not, it asks for the Health Connect Server IP Address and Port number, then creates the logical link in the VistA system. This link is required to receive consult updates from HSRM to VistA. This link is also used by the SD\*5.3\*707 scheduling patch, which may or may not be installed previously.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. There are no VistA options to be exported as part of this patch.

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail groups can be created to respond to any system failures related to HL7 message processing. This will be managed at the individual sites.

Included in the patch is a new mail group; created specifically for the HSRM interface process, this mail group is populated automatically as part of the link setup. This new mail group is called GMRCCCRA NOTIFICATIONS, and it includes the <span class="mark">REDACTED</span> exchange email as a member. The mail group is added to the GMRC CCRA SEND HL7 application parameter.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch refers to the community care message processing with the HSRM system. It updates HL7 protocols and links to allow message processing to take place between VistA and HSRM.

## HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols are created and/or updated:

- GMRC CCRA REF-I12 CLIENT
- GMRC CCRA REF-I13 CLIENT
- GMRC CCRA REF-I14 CLIENT
- GMRC CCRA-HSRM REF-I12 SERVER
- GMRC CCRA-HSRM REF-I13 SERVER
- GMRC CCRA-HSRM REF-I14 SERVER
- CONSULTS TO CCRA

  The following protocols are created and/or updated for patch 123:
- GMRC HSRM-CCRA REF-I13 CLI
- GMRC HSRM-CCRA REF-I13 SERVER
- GMRC HSRM-CCRA REF-I14 CLIENT
- GMRC HSRM-CCRA REF-I14 SERVER

There are two new HL7 application parameters:

- GMRC CCRA RECEIVE
- GMRC CCRA SEND

  Patch 123 creates and uses two new HL7 application parameters:
- GMRC HSRM-CCRA RECEIVE
- GMRC HSRM-CCRA SEND

There is a new HL7 logical link: GMRCCCRA.

Patch 123 creates another new logical link: CCRA-NAK.

These are used to transmit data to and from HSRM via HL7 message processing. The data being moved is information regarding clinical consults that will be fulfilled via community care.

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. No exemptions to VA or VistA standards are required for this patch.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security of the software is handled through existing measures within VistA, and those measures do not need to be updated for this patch. We are running this on the VA network along with its other applications. Data is transmitted and stored only over the VA’s trusted Internet connection network and on VA servers.

As noted in the introduction, in order to send data from HSRM into VistA for patch 123, the HSRM user must be registered and valid within the VistA system. The software identifies the user email address within the HL7 message and verifies the user within VistA. If the user does not exist, then the message is rejected, and no data is filed.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Archiving of data related to this patch and the HL7 messages created for community care follow the same processes as existing HL7 constructs. These do not need to be updated.

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. There are no changes made by this patch to cross-references, standard or non-standard.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General troubleshooting guidelines:

- Troubleshooting the interface and its links on the VistA side of the interface should be performed by IT personnel responsible for the HL7 system within VistA.
- If messages are not transmitting from VistA, check the System Link Monitor to confirm that all messages are sent. If messages are stopped or if the link is in an OpenFail status, then shut down and restart the link.
- If the message queue in the System Link Monitor shows that all messages are sent, and the count increases when a new message is sent, then the problem is with the HSRM connection. In this case, the Enterprise Service Desk must be contacted.
- If an OpenFail status remains after stopping and restarting the logical link, refer to the Site Manager Developer Manual V 1.6\*161 in the HL7 portion of the VDL for more tips and guidelines, or call the Enterprise Service Desk for assistance.

  Please note that all troubleshooting guidelines that refer to the logical link GMRCCCRA created with patch 99 are also true for the CCRA-NAK logical link created with patch 123.

## Check the System Link Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If messages are not being received in HSRM, the first thing to do is to check the link monitor and verify that messages are being created in VistA and sent out via the interface.

1.  Navigate to the HL7 Menu, shown in Exhibit 6.

> <span id="_Ref519678184" class="anchor"></span>Exhibit 6: Screenshot: System Management Menu

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/006.png)

32. Select Systems Link Monitor, highlighted in Exhibit 7.

> <span id="_Ref519678204" class="anchor"></span>Exhibit 7: Screenshot: Select Systems Link Monitor

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/007.png)

33. Check to see if the GMRCCCRA link is listed as Shutdown or Inactive, highlighted in Exhibit 8.

> <span id="_Ref519678223" class="anchor"></span>Exhibit 8: Screenshot: Shutdown or Inactive Link

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/008.png)

34. If the link is Inactive, this usually means a message hasn’t been sent for a certain amount of time and probably does not indicate a problem. If the status is Shutdown, use the Filer and Link Management Options menu item under the HL7 menu (highlighted in Exhibit 9) to restart the link.

> <span id="_Ref519678310" class="anchor"></span>Exhibit 9: Screenshot: Select Filer and Link Management Option

> ![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/009.png)

35. If the link is in an OpenFail state, this indicates a problem with the connection. Stop/restart the link to see if this fixes the problem. If it doesn’t, review the logical link, application parameters, and protocols for accuracy. If the problem persists, call the Enterprise Service Desk for assistance. You may also refer to the Site Manager Developer Manual in the VDL.

    Note: Troubleshooting of HL7 issues should be done by an HL7 support person who has knowledge of VistA HL7 and how it works. If support is unable to find the issue, it should be escalated to the next troubleshooting tier.
36. Restart the link using Menu item SL Start/Stop Links. Type “GMRCCCRA” when given the prompt “Select HL LOGICAL LINK NODE,” highlighted in Exhibit 10.

> <span id="_Ref511394351" class="anchor"></span>Exhibit 10: Screenshot: Select Logical Link Node to Restart

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/010.png)

Note that in this screen example the logical link is already active. If it were not, this option would start the link immediately once it is identified as shown. (An example of this is found in Exhibit 2.)

## Stop/Start the Interface Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 2.1.4 provides instructions on starting/stopping the logical link. Note that if the logical link needs to be edited for any reason, the link must first be stopped. Stopping the GMRCCCRA HL7 logical link will stop sending messages to the GMRC CCRA HealthShare server. After editing the link, it must be restarted using the same menu option as shown. This will allow messages to be sent once again. The HL7 system will immediately send any messages that may have accrued in a backlog while the link was shut down.

## Edit the Logical Link Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the information entered during the install is incorrect or needs to be modified at a later date, this can be done by editing the logical link GMRCCCRA.

1.  Go to the VistA HL main menu, as shown in Exhibit 11.

> <span id="_Ref511390983" class="anchor"></span>Exhibit 11: Screenshot: HL Main Menu in VistA

> ![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/011.png)

2.  Select the Interface Developer Options from the menu, as shown in Exhibit 12.

> <span id="_Ref511391031" class="anchor"></span>Exhibit 12: Screenshot: Interface Developer Options Menu

> ![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/012.png)

3.  Next, select the EL Link Edit option to make changes to the logical link. This will bring up a single-line prompt, asking you to identify the logical link to be modified, as shown in Exhibit 13.

> <span id="_Ref511391177" class="anchor"></span>Exhibit 13: Screenshot: Select Logical Link GMRCCCRA

> ![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/013.png)

4.  Once you have identified the logical link to edit, the edit screen appears, as shown in Exhibit 14.

> <span id="_Ref511391488" class="anchor"></span>Exhibit 14: Screenshot: HL7 Logical Link Edit Screen

> ![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/014.png)

> For privacy purposes, the Institution value and DNS Domain have been removed in this example. The DNS Domain is not part of this patch, but it is determined at the site if used.

This is the option used to edit the logical link. To edit the IP address and port, go to the LLP Type prompt, which shows a value of TCP/IP, and hit \<Enter\>. This will bring up a new pop-up window, as shown in Exhibit 15.

<span id="_Ref511391550" class="anchor"></span>Exhibit 15: Screenshot: Edit TCP/IP Parameters

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/015.png)

For privacy purposes, the IP address and port number have been removed in this example.

Here, the IP address and the port number used for this logical link can be updated. Other fields in this screen are dependent upon the policies of the individual site. Enter the values you want for these fields, move to the end of the screen, and close it to return to the Logical Link Edit screen. When you have completed all modifications, save what you have done in the Logical Link Edit screen, and exit the menu option.

The value provided in the Re-Transmission Attempts field indicates how many retries will occur if the message fails. If no value is provided for this field, the default is set to five retries.

In this example, the Exceed Re-Transmit Action is set to Restart, which means that the link/process will shut down and restart the link. When the link is restarted, it will attempt to send the messages in the queue. This loop continues until the messages are sent and acknowledged by the receiving station. Our link has been set up to send a notification email to the default notification VistA email group for that VistA system. If the link fails and it restarts, an email is sent to the members of this VistA email group. Upon receiving the email, the site’s HL7 support team should investigate to see why the link is failing and fix the issue.

Note that the Retention field should be left alone without strict guidelines from the site. The ACK and READ Timeout values can be increased if the network is slow. Note also that if messages are not sent, they are not automatically purged from the system; they remain in queue until the connection is reestablished, then sent in the order they were created.

## Edit the Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two application parameters associated with this patch: GMRC CCRA SEND and GMRC CCRA RECEIVE. To modify either of these, from within the Interface Developer Options menu select EA Application Edit. This will bring up a one-prompt window, asking you to identify the Application Parameter Name, as shown in Exhibit 16.

> **NOTE:** These instructions are the same for the Application Parameters created as part of patch 123, GMRC HSRM-CCRA RECEIVE and GMRC HSRM-CCRA SEND. Simply change the name of the application you are editing as you follow these steps.

<span id="_Ref511393239" class="anchor"></span>Exhibit 16: Screenshot: List of GMRC CCRA Application Parameters

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/016.png)

Identify the GMRC CCRA application you wish to edit and hit \<Enter\>. This will bring up the Application Edit screen, shown in Exhibit 17.

<span id="_Ref511393282" class="anchor"></span>Exhibit 17: Screenshot: HL7 Application Edit

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/017.png)

For privacy purposes, the facility name has been blanked out in this example. The two HL7 fields contain standard values and should not be altered.

This is where a mail group associated with the application can be created or updated. A mail group is populated automatically as part of this patch. This mail group, using the VistA MailMan functionality, receives alerts that may occur in relation to the application. Individual mail groups are edited in the VistA MailMan functions.

## Edit the Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses how to update or modify the client and server protocols created by this patch. From the Interface Developer Options menu, select the EP Protocol Edit option. You will immediately be asked which protocol you wish to edit. A list of the GMRC CCRA protocols created by this patch is presented in Exhibit 18.

<span id="_Ref511393574" class="anchor"></span>Exhibit 18: Screenshot: List of GMRC CCRA Protocols

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/018.png)

Select the protocol you wish to edit. For this example, we will take the first one. Selecting it brings up the HL7 Interface Setup screen, as shown in Exhibit 19.

> **NOTE:** These instructions are the same for editing the Protocols created by patch 123.

<span id="_Ref511393690" class="anchor"></span>Exhibit 19: Screenshot: HL7 Interface Setup

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/019.png)

This screen has hooks into the other interface edit screens (note that text at the top right says, “page 1 of 2”). The Name field is the protocol you selected. If you hit \<Enter\> at the Name prompt, screen 2 will appear, as shown in Exhibit 20.

<span id="_Ref511394279" class="anchor"></span>Exhibit 20: Screenshot: Update Subscriber from within Edit Protocol Option

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/020.png)

Screen 2, shown here, is the subscriber edit screen. Note that the Receiving Application field contains the application value we saw earlier. If you hit \<Enter\> at this field, you will be able to edit the application parameters, as shown previously. The Logical Link field performs in the same manner. If you hit \<Enter\> at that field, a new pop-up window will allow you to edit the logical link and all its parameters.

## View HL7 Message Transmission Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA HL7 message processing system includes an option to view messages in the transmission log. The data within the message can help determine any potential errors with the data collected for a consult. At the HL Main screen shown in Exhibit 10, select Message Management Options. This brings up a new screen, shown in Exhibit 21.

<span id="_Ref511394371" class="anchor"></span>Exhibit 21: Screenshot: Message Management Options

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/021.png)

From within this screen, select the View Transmission Log option. This option will present questions to determine what group of messages to include. You will be asked what type of search to conduct, as shown in Exhibit 22.

<span id="_Ref511394424" class="anchor"></span>Exhibit 22: Screenshot: Search Transmission Log Selection

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/022.png)

If you want to check on a message that went out today, for example, select “M.”

The next screen asks for a start date and ending date/time for your search, as shown in Exhibit23.

<span id="_Ref511394891" class="anchor"></span>Exhibit 23: Screenshot: Start/Stop Time Selection for Viewing Transmission Log

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/023.png)

Next, you will be asked questions to identify the type of message to search for and which link these messages were associated with (GMRCCRA or CCRA-NAK). You can select by specific status code, as shown in Exhibit 24.

<span id="_Ref511394932" class="anchor"></span>Exhibit 24: Screenshot: Message Search Criteria – Status Codes

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/024.png)

You will also be asked to select other options, including the link and the message type. For this example, we will use our GMRCCRA link and the message type REF for Patient Referral, as shown in Exhibit 25.

> **NOTE:** These instructions are the same for troubleshooting messages sent via the CCRA-NAK logical link created with patch 123.

<span id="_Ref511394999" class="anchor"></span>Exhibit 25: Screenshot: Message Search Selection Criteria

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/025.png)

After the last prompt has been entered, a screen shows all the messages that meet the selection criteria. As shown in Exhibit 26.

<span id="_Ref511395043" class="anchor"></span>Exhibit 26: Screenshot: List of Messages that Match the Criteria

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/026.png)

The list can be shortened by selecting one of the specific event types, such as I12 or I13, instead of choosing “ALL.”

The up and down arrows can be used to move through the list. On the first screen the up-arrow key is not available (the list assumes you start at the bottom of the screen you are on), but the user can use the Q key on the keyboard to move the cursor farther up from the bottom of the page. The message number underlined is the one that will be selected when the user hits \<Enter\>.

From within Message Contents screen, shown in Exhibit 27, different portions of the message can be seen by scrolling up and down. You can also use the “N” key to open a text search window, which will take you to the associated text within the message. To exit the message, type \<CTRL-E\>.

<span id="_Ref511395241" class="anchor"></span>Exhibit 27: Screenshot: Message Contents

![](community-care-referral-and-authorization-ccra-technical-manual-updated-with-pat/027.png)

This set of instructions enables the search for specific message. VistA does not allow users to search for a specific patient name without knowing the message ID. This requires intervention from someone with FileMan access, who would need to perform an Inquire to File Entries search within the HL7 message text file.

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error correction will occur as normal within the confines of HL7 message processing. As stated above, the troubleshooting of HL7 issues should be done by an HL7 support person who has knowledge of VistA HL7 and how it works. If support is unable find the issue, it should be escalated to the next troubleshooting tier.

# Appendix A: Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc11708795" class="anchor"></span>Exhibit 28: Acronyms and Abbreviations

| Acronym or Abbreviation | Definition                                                  |
|-----------------------------|-----------------------------------------------------------------|
| CCRA                        | Community Care Referral and Authorization                       |
| CPRS                        | Computerized Patient Record System                              |
| DNS                         | Domain Name System                                              |
| HL7                         | Health Level 7                                                  |
| HSRM                        | HealthShare Referral Manager                                    |
| IP                          | Internet Protocol                                               |
| IT                          | Information Technology                                          |
| KIDS                        | Kernel Installation and Distribution System                     |
| OIT                         | Office of Information and Technology                            |
| VA                          | U.S. Department of Veterans Affairs                             |
| VDL                         | VA Software Document Library                                    |
| VistA                       | Veterans Health Information Systems and Technology Architecture |

Acronyms and AbbreviationsThis table lists definitions for the acronyms and abbreviations used in this document.