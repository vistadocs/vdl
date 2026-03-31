---
title: VIX Admin Guide
doc_type: AG
doc_label: Administrator's Guide
doc_layer: plain
doc_subject: 
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: archive
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 2006
security_keys: []
menu_options: 2
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - strong
  - class
  - table
  - image
  - contents
  - blockquote
  - even
  - remote
  - style
  - width
page_count: 0
word_count: 17645
section_count: 39
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/vix_admin_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/vix_admin_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=413"
---

---
title: VistA Imaging Exchange Administrator’s Guide
---

![](vix-admin-guide/001.png)

> Department of Veterans Affairs

> Office of Information and Technology (OI&T)

> VistA Imaging Exchange (VIX) Administrator's Guide February 2018

> Property of the US Government

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging Product Development group.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Product Development Department of Veterans Affairs Internet: <span class="mark">REDACTED</span>

> VA intranet: <span class="mark">REDACTED</span>

> Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 7%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Rev</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>02 February</p>
<p>2018</p></td>
<td>10</td>
<td>Additional updates for MAG*3.0*185. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>14 November</p>
<p>2017</p></td>
<td>9</td>
<td>Updated for MAG*3.0*185 and incorporated comments from reviewers. <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>05 October</p>
<p>2017</p></td>
<td>8</td>
<td>Updated for P170 and 177, including VIX image viewer. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>9 September</p>
<p>2013</p></td>
<td>7</td>
<td>Added section ROI VIX Operation, Configuration and Statistics; <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01 August 2013</td>
<td>6</td>
<td>Renamed for joint rollup of MAG*3.0*34/116/118, MAG*3.0*119, MAG*3.0*127, MAG*3.0*129. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>15 July 2013</td>
<td>5</td>
<td><p>Updated for Imaging patch MAG*3.0*119. Updated sections on Related Information; The VIX Transaction Log; Caching of Metadata and Images.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td><p>14 September</p>
<p>2012</p></td>
<td>4</td>
<td>Updated for Imaging patch MAG*3.0*118. Minor grammar and wording corrections. Added DICOM Importer Application Services, updated VIX Transaction log location, Added new VIX Interfaces, Added new RPCs related to VIX/Importer II, <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>14 Oct 2011</td>
<td>3</td>
<td><p>Updated for Imaging patch MAG*3.0*104 to reflect expanded image sharing and involvement of CVIX. Reorganized to support future revisions.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>20 Jan 2011</td>
<td>2</td>
<td>Updated for Imaging patch MAG*3.0*115. Clarified “site number” references to properly indicate station #. Added new VistARad-related information in descriptions of the 100 node in file #2006.95. Minor wording corrections. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>22 Apr 2010</td>
<td>1</td>
<td>Document created for Imaging patch MAG*3.0*83. <mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> Contents

1.  [Introduction 1](#introduction)
    1.  [Intended Audience 1](#intended-audience)
    2.  [Terms of Use 1](#terms-of-use)
    3.  [Document Conventions 2](#document-conventions)
    4.  [Section Summary 2](#section-summary)
    5.  [Related Information 3](#related-information)
    6.  [VIX Support 3](#vix-support)
2.  [VIX Overview 4](#_bookmark7)
    1.  [The VIX and Image Sharing 4](#the-vix-and-image-sharing)
        1.  [VA-VA Image Sharing 5](#va-va-image-sharing)
        2.  [DoD-to-VA Image Sharing 6](#dod-to-va-image-sharing)
        3.  [VA-to-DoD Image Sharing 7](#va-to-dod-image-sharing)
        4.  [What is the CVIX? 7](#what-is-the-cvix)
    2.  [DICOM Importer III Application Services 9](#dicom-importer-iii-application-services)
    3.  [VIX Image Viewer 9](#vix-image-viewer)
        1.  [New Services Introduced by MAG\*3.0\*170, 177 and 185 10](#new-services-introduced-by-mag3.0170-177-and-185)
        2.  [Troubleshooting 11](#troubleshooting)
        3.  [Windows Services 11](#windows-services)
        4.  [Windows Processes 12](#windows-processes)
        5.  [Service Logging 12](#service-logging)
        6.  [Viewer Image Caching 12](#viewer-image-caching)
        7.  [VIX Viewer Test Page 13](#vix-viewer-test-page)
        8.  [Supported SOP Classes 17](#_bookmark22)
    4.  [VIX Implementation and Configuration 17](#vix-implementation-and-configuration)
    5.  [VIX Dependencies 17](#vix-dependencies)
    6.  [VIX Operational Priority 18](#vix-operational-priority)
        1.  [Standalone Server 18](#standalone-server)
    7.  [Security, Data Integrity, and Data Sensitivity Considerations 19](#security-data-integrity-and-data-sensitivity-considerations)
3.  [VIX General Operations 20](#vix-general-operations)
    1.  [VIX General Operations Overview 20](#vix-general-operations-overview)
    2.  [The VIX and the VistA Site Service 20](#the-vix-and-the-vista-site-service)
    3.  [Using the VIX Transaction Log 21](#using-the-vix-transaction-log)
        1.  [VIX Transaction Log Fields 22](#vix-transaction-log-fields)
        2.  [VIX Transaction Log Fields (Export Only) 26](#vix-transaction-log-fields-export-only)
        3.  [Log Collector Service 27](#log-collector-service)
    4.  [VIX Data Retention and Purges 27](#vix-data-retention-and-purges)
    5.  [VIX Startup and Shutdown 28](#vix-startup-and-shutdown)
    6.  [Monitoring/Maintaining the VIX 28](#monitoringmaintaining-the-vix)
        1.  [Checking the VIX Service: 2012 R2 Standalone Server 29](#checking-the-vix-service-2012-r2-standalone-server)
    7.  [Monitoring/Maintaining the VIX Viewer 30](#monitoringmaintaining-the-vix-viewer)
        1.  [Troubleshooting the VIX Viewer 30](#troubleshooting-the-vix-viewer)
    8.  [The VIX and Backups 32](#the-vix-and-backups)
4.  [VIX Image Sharing 33](#vix-image-sharing)
    1.  [Remote Metadata Retrieval 33](#remote-metadata-retrieval)
        1.  [Metadata Requests from Clinical Display 34](#metadata-requests-from-clinical-display)
        2.  [Metadata Requests from VistARad 34](#metadata-requests-from-vistarad)
    2.  [Metadata Requests from the New Image Viewer 36](#metadata-requests-from-the-new-image-viewer)
    3.  [Remote Image Retrieval 36](#remote-image-retrieval)
        1.  [Image Quality and VIX Compression 37](#image-quality-and-vix-compression)
        2.  [Image Types vs. Image Formats 38](#image-types-vs.-image-formats)
    4.  [Caching of Metadata and Images 39](#caching-of-metadata-and-images)
        1.  [Cache Retention Periods 40](#cache-retention-periods)
        2.  [Cache Location 40](#cache-location)
    5.  [Using the VIX Cache Manager 40](#using-the-vix-cache-manager)
        1.  [Cache Organization 40](#cache-organization)
    6.  [Image Sharing-related Logging 46](#image-sharing-related-logging)
        1.  [Logging on VistA 46](#logging-on-vista)
        2.  [Additional Client Logging 48](#additional-client-logging)
    7.  [Image Sharing and VIX Timeouts 48](#image-sharing-and-vix-timeouts)
    8.  [Troubleshooting 50](#troubleshooting-1)
5.  [ROI VIX Operation, Configuration and Statistics 53](#roi-vix-operation-configuration-and-statistics)
    1.  [How the VIX Processes ROI Requests 53](#how-the-vix-processes-roi-requests)
        1.  [Processing ROI Disclosure Requests Immediately 53](#processing-roi-disclosure-requests-immediately)
        2.  [Periodic Processing of ROI Disclosure Requests 53](#periodic-processing-of-roi-disclosure-requests)
        3.  [Purging Completed Disclosures 54](#purging-completed-disclosures)
        4.  [Processing Disclosure Wait Time 54](#processing-disclosure-wait-time)
        5.  [ROI Periodic Processing Credentials 54](#roi-periodic-processing-credentials)
        6.  [Alerts About Problems in the ROI Configuration 54](#alerts-about-problems-in-the-roi-configuration)
    2.  [Getting Information About ROI Processing 56](#getting-information-about-roi-processing)
        1.  [Information the ROI Processing Status Page Provides 56](#information-the-roi-processing-status-page-provides)
    3.  [Modifying the ROI Processing Parameters of the VIX 59](#modifying-the-roi-processing-parameters-of-the-vix)
    4.  [Changing User List for Get Invalid ROI Credentials Email Notifications 60](#changing-user-list-for-get-invalid-roi-credentials-email-notifications)
6.  [VIX Reference/Software Description 62](#vix-referencesoftware-description)
    1.  [VIX Java Components 62](#vix-java-components)
        1.  [VIX Servlet Container 62](#vix-servlet-container)
        2.  [VIX Security Realms 62](#vix-security-realms)
        3.  [VIX Interfaces 62](#vix-interfaces)
        4.  [VIX Core 63](#vix-core)
        5.  [VIX Data Sources 63](#vix-data-sources)
        6.  [Java Installation Locations 64](#java-installation-locations)
        7.  [Java Logs 65](#java-logs)
    2.  [VistA/M Information 65](#vistam-information)
        1.  [RPCs Used by the VIX 65](#rpcs-used-by-the-vix)
        2.  [Database Information 71](#database-information)
        3.  [Exported Menu Options 71](#exported-menu-options)
        4.  [Security Keys 71](#security-keys)
        5.  [User Accounts 71](#user-accounts)
    3.  [Other VIX Components 72](#other-vix-components)
        1.  [VIX Security Certificate 72](#vix-security-certificate)

[6.3.2. .NET 72](#net)

3.  [Sun JRE 72](#sun-jre)
4.  [Laurel Bridge DCF Toolkit 72](#laurel-bridge-dcf-toolkit)
5.  [Aware JPEG2000 Toolkit License 73](#aware-jpeg2000-toolkit-license)
7.  [Appendix: Image Sharing and DICOM Images 74](#appendix-image-sharing-and-dicom-images)
    1.  [DoD DICOM Object Filtering 74](#dod-dicom-object-filtering)
    2.  [VA DICOM Images Provided to DoD 75](#va-dicom-images-provided-to-dod)
8.  [Index 77](#index)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Intended Audience](#intended-audience)
  - [Terms of Use](#terms-of-use)
  - [Document Conventions](#document-conventions)
  - [Section Summary](#section-summary)
  - [Related Information](#related-information)
  - [VIX Support](#vix-support)
- [VIX Overview](#vix-overview)
  - [The VIX and Image Sharing](#the-vix-and-image-sharing)
    - [VA-VA Image Sharing](#va-va-image-sharing)
    - [DoD-to-VA Image Sharing](#dod-to-va-image-sharing)
    - [VA-to-DoD Image Sharing](#va-to-dod-image-sharing)
    - [What is the CVIX?](#what-is-the-cvix)
  - [DICOM Importer III Application Services](#dicom-importer-iii-application-services)
  - [VIX Image Viewer](#vix-image-viewer)
    - [New Services Introduced by MAG\3.0\170, 177 and 185:](#new-services-introduced-by-mag30170-177-and-185)
    - [Troubleshooting](#troubleshooting)
    - [Windows Services](#windows-services)
    - [Windows Processes](#windows-processes)
    - [Service Logging](#service-logging)
    - [Viewer Image Caching](#viewer-image-caching)
    - [VIX Viewer Test Page](#vix-viewer-test-page)
  - [VIX Implementation and Configuration](#vix-implementation-and-configuration)
  - [VIX Dependencies](#vix-dependencies)
  - [VIX Operational Priority](#vix-operational-priority)
    - [Standalone Server](#standalone-server)
  - [Security, Data Integrity, and Data Sensitivity Considerations](#security-data-integrity-and-data-sensitivity-considerations)
- [VIX General Operations](#vix-general-operations)
  - [VIX General Operations Overview](#vix-general-operations-overview)
  - [The VIX and the VistA Site Service](#the-vix-and-the-vista-site-service)
  - [Using the VIX Transaction Log](#using-the-vix-transaction-log)
    - [VIX Transaction Log Fields](#vix-transaction-log-fields)
    - [VIX Transaction Log Fields (Export Only)](#vix-transaction-log-fields-export-only)
    - [Log Collector Service](#log-collector-service)
  - [VIX Data Retention and Purges](#vix-data-retention-and-purges)
  - [VIX Startup and Shutdown](#vix-startup-and-shutdown)
  - [Monitoring/Maintaining the VIX](#monitoringmaintaining-the-vix)
    - [Checking the VIX Service: 2012 R2 Standalone Server](#checking-the-vix-service-2012-r2-standalone-server)
  - [Monitoring/Maintaining the VIX Viewer](#monitoringmaintaining-the-vix-viewer)
    - [Troubleshooting the VIX Viewer](#troubleshooting-the-vix-viewer)
  - [The VIX and Backups](#the-vix-and-backups)
- [VIX Image Sharing](#vix-image-sharing)
  - [Remote Metadata Retrieval](#remote-metadata-retrieval)
    - [Metadata Requests from Clinical Display](#metadata-requests-from-clinical-display)
    - [Metadata Requests from VistARad](#metadata-requests-from-vistarad)
  - [Metadata Requests from the New Image Viewer](#metadata-requests-from-the-new-image-viewer)
  - [Remote Image Retrieval](#remote-image-retrieval)
    - [Image Quality and VIX Compression](#image-quality-and-vix-compression)
    - [Image Types vs. Image Formats](#image-types-vs-image-formats)
  - [Caching of Metadata and Images](#caching-of-metadata-and-images)
    - [Cache Retention Periods](#cache-retention-periods)
    - [Cache Location](#cache-location)
  - [Using the VIX Cache Manager](#using-the-vix-cache-manager)
    - [Cache Organization](#cache-organization)
  - [Image Sharing-related Logging](#image-sharing-related-logging)
    - [Logging on VistA](#logging-on-vista)
    - [Additional Client Logging](#additional-client-logging)
  - [Image Sharing and VIX Timeouts](#image-sharing-and-vix-timeouts)
  - [Troubleshooting](#troubleshooting-1)
- [ROI VIX Operation, Configuration and Statistics](#roi-vix-operation-configuration-and-statistics)
  - [How the VIX Processes ROI Requests](#how-the-vix-processes-roi-requests)
    - [Processing ROI Disclosure Requests Immediately](#processing-roi-disclosure-requests-immediately)
    - [Periodic Processing of ROI Disclosure Requests](#periodic-processing-of-roi-disclosure-requests)
    - [Purging Completed Disclosures](#purging-completed-disclosures)
    - [Processing Disclosure Wait Time](#processing-disclosure-wait-time)
    - [ROI Periodic Processing Credentials](#roi-periodic-processing-credentials)
    - [Alerts About Problems in the ROI Configuration](#alerts-about-problems-in-the-roi-configuration)
  - [Getting Information About ROI Processing](#getting-information-about-roi-processing)
    - [Information the ROI Processing Status Page Provides](#information-the-roi-processing-status-page-provides)
  - [Modifying the ROI Processing Parameters of the VIX](#modifying-the-roi-processing-parameters-of-the-vix)
  - [Changing User List for Get Invalid ROI Credentials Email Notifications](#changing-user-list-for-get-invalid-roi-credentials-email-notifications)
- [VIX Reference/Software Description](#vix-referencesoftware-description)
  - [VIX Java Components](#vix-java-components)
    - [VIX Servlet Container](#vix-servlet-container)
    - [VIX Security Realms](#vix-security-realms)
    - [VIX Interfaces](#vix-interfaces)
    - [VIX Core](#vix-core)
    - [VIX Data Sources](#vix-data-sources)
    - [Java Installation Locations](#java-installation-locations)
    - [Java Logs](#java-logs)
  - [VistA/M Information](#vistam-information)
    - [RPCs Used by the VIX](#rpcs-used-by-the-vix)
    - [Database Information](#database-information)
    - [Exported Menu Options](#exported-menu-options)
    - [Security Keys](#security-keys)
    - [User Accounts](#user-accounts)
  - [Other VIX Components](#other-vix-components)
    - [VIX Security Certificate](#vix-security-certificate)
    - [.NET](#net)
    - [Sun JRE](#sun-jre)
    - [Laurel Bridge DCF Toolkit](#laurel-bridge-dcf-toolkit)
    - [Aware JPEG2000 Toolkit License](#aware-jpeg2000-toolkit-license)
- [Appendix: Image Sharing and DICOM Images](#appendix-image-sharing-and-dicom-images)
  - [DoD DICOM Object Filtering](#dod-dicom-object-filtering)
  - [VA DICOM Images Provided to DoD](#va-dicom-images-provided-to-dod)
- [Index](#index)
> This document explains how to maintain and administer the VistA Imaging Exchange
> (VIX) service.
> The VIX is used to facilitate data sharing and exchange across organizational and functional boundaries. Currently the VIX’s primary purpose is to support image sharing between VA (Department of Veterans Affairs) medical facilities as well as between VA and the Department of Defense (DoD) medical facilities. It is anticipated that the VIX’s role will be expanded to support data sharing and exchange within a facility as well as between facilities.
> Beginning with MAG\*3.0\*170, the VIX hosts a zero footprint viewer providing services to consuming application chiefly eHMP and JLV. These services are expected to be utilized by future applications. With these changes, the VIX becomes a more critical component as it is providing access not only to remote but local images as well.
> Maintenance of this component becomes more critical to the clinical operation at the site level. The operation of a site VIX also affects access to the portion of the patient record stored at the site.
> This document assumes that the VIX is installed and configured. For information about VIX system requirements, installation, and configuration see the *[<u>VIX Installation Guide</u>](https://www.va.gov/vdl/application.asp?appid=105).*

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document is intended for VA staff responsible for managing a local VIX.

> One part of this document[*<u>, Image Sharing Related Logging</u>*](#image-sharing-related-logging) , may also be of interest to VA Imaging Coordinators at non-VIX sites. This section describes how remote VIXes log access to locally stored images.

> This document presumes a working knowledge of the VistA environment, VistA Imaging components and workflow, Windows server administration, and Windows cluster administration.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX is a component of VistA Imaging and is regulated as a medical device by the Food and Drug Administration (FDA). Use of the VIX is subject to the following provisions:

- Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.
- The FDA classifies VistA Imaging, and the VIX (as a component of VistA Imaging) as a medical device. Unauthorized modifications to VistA Imaging, including the VIX, such as the installation of unapproved software, will adulterate

> the medical device. The use of an adulterated medical device violates US federal law (21CFR820).

- Because software distribution/inventory management tools can install inappropriate or unapproved software without a local administrator’s knowledge, sites must exclude the VIX server from such systems.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document uses the following typographic conventions.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Symbol/Typeface</strong></th>
<th><strong>Meaning/Use</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Bold</strong></td>
<td>User input, selection, GUI element (menu item, button, field)</td>
<td><p>Click <strong>Finish</strong>.</p>
<p>Choose <strong>Open</strong> from the <strong>File</strong> menu. Type the user account name in the</p>
<p><strong>Name</strong> field.</p></td>
</tr>
<tr class="even">
<td><p>Monospaced font (typically in a box)</p>
<p>(Bold indicates user input or selection).</p></td>
<td>Command-line sample or output (such as character- based screen captures and computer source code), menus, file names</td>
<td><p>Navigate to the</p>
<p>\Docs\Imaging_Docs_Latest folder.</p></td>
</tr>
<tr class="odd">
<td><em>Italics</em></td>
<td>Emphasis, reference to section in the document or another document, or a variable</td>
<td>For more information, see the <em><a href="https://www.va.gov/vdl/application.asp?appid=105"><u>VistA</u></a> <a href="https://www.va.gov/vdl/application.asp?appid=105"><u>Imaging DICOM Gateway</u></a> <a href="https://www.va.gov/vdl/application.asp?appid=105"><u>Installation Guide</u></a>.</em></td>
</tr>
<tr class="even">
<td>Square brackets, monospace or italics</td>
<td>Variable, placeholder, VistA menu</td>
<td><p>Access the Kernel Installation and Distribution System Menu [XPD MAIN].</p>
<p>;;3.0;IMAGING;[Patch</p>
<p>List];Mar 19, 2002;Build</p>
<p>1989;Feb 21, 2011</p>
<p>MAG*3.0*&lt;<em>PatchNumber</em>&gt;.KID</p></td>
</tr>
</tbody>
</table>

## Section Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- [VIX Overview](#_bookmark7) – A high-level overview of VIX capabilities and key concepts.
- [VIX General Operations](#vix-general-operations) – A description of day-to-day activities that relate to all VIX capabilities.
- [VIX Image Sharing](#vix-image-sharing) – A description of VIX operations specific to image sharing.
- VIX Image Viewer – A description of VIX operations specific to image viewing hosted by the VIX
- ROI VIX Operation, Configuration and Statistics – A description of how the VIX processes ROI requests.
- VIX Reference/Software Description – VIX technical information.

## Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Additional documents containing information about the VIX can be found on the VistA Imaging SharePoint site here:

> [<u>https://www.va.gov/vdl/application.asp?appid=105</u>](https://www.va.gov/vdl/application.asp?appid=105)

## VIX Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span class="mark">REDACTED</span>

# VIX Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter provides a high-level summary of what the VIX does and how it does it. This chapter covers:

- [<u>The VIX and Image Sharing</u>](#the-vix-and-image-sharing)
- [<u>DICOM Importer III Application Services</u>](#dicom-importer-iii-application-services)
- [<u>VIX Image Viewer</u>](#vix-image-viewer)
- [<u>VIX Implementation and Configuration</u>](#vix-implementation-and-configuration)
- [<u>VIX Dependencies</u>](#vix-dependencies)
- [<u>VIX Operational Priority</u>](#vix-operational-priority)
- [<u>Security, Data Integrity, and Data Sensitivity Considerations</u>](#security-data-integrity-and-data-sensitivity-considerations)

## The VIX and Image Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX implements image sharing between the Department of Veterans Affairs (VA) and participating Department of Defense (DoD) medical facilities. The VIX also supports and extends VA-to-VA remote image sharing for Clinical Display and VistARad.

> The VIX delivers these capabilities in such a way that:

- Clinicians can locate and review images from all VA and participating DoD facilities without having to manually log into the remote site.
- Wide Area Network (WAN) traffic is minimized whenever possible using the VIX’s compression and caching strategies.
- The VIX handles the burden of connection management and data retrieval rather than client applications such as Clinical Display and VistARad.

> At sites where a VIX is implemented, the VIX’s involvement in data retrieval begins when a clinician selects a patient who has been seen at the local hospital as well as at one or more remote hospitals. The clinician’s client software (Clinical Display or VistARad) pulls information about locally stored images from the local VistA system, while information about remote images is pulled from remote sites via VIX. The clinician uses this information to decide what images to display. Local images are retrieved directly from the local hospital, while remote images are retrieved via the VIX. From the clinician’s perspective, accessing an image works the same way, regardless if the image is from local storage, a remote VA site, or from the DoD.

> The following sections outline how a VIX fits in when accessing remote images.

### VA-VA Image Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following diagram shows how remote VA images and related metadata flow through a VIX.

![](vix-admin-guide/002.png)

> When the VIX is used for VA-to-VA image sharing, the VIX can handle anything stored in VistA Imaging. This includes radiology images, clinical images of all types, scanned documents, video, and audio.

> Note: MUSE EKG waveforms, commercial PACS images, and other images not stored in VistA Imaging cannot be retrieved using the VIX.

> Note: If a local VIX is not implemented, VA-VA image sharing is still available (at reduced performance) to local Clinical Display and zero-footprint Image Viewer users, but not to VistARad users.

### DoD-to-VA Image Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a local VIX is used to retrieve DoD images for shared VA/DoD patients, the local VIX sends clinicians’ requests to the Centralized VistA Image Exchange (CVIX). The CVIX in turn handles the communication with the various sources of DoD images.

![](vix-admin-guide/003.png)

> VA clinicians can access the following types of DoD images for shared patients if a local VIX is implemented and if the appropriate DoD image sources are online.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Image Category</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DoD DICOM</p>
<p>images</p></td>
<td><p>Available from participating DoD facilities via the CVIX and originating from the DAS Image Adapter.</p>
<p><strong>Note:</strong> There are a limited number of non-image DICOM objects that are not provided. For more information, see <a href="#dod-dicom-object-filtering"><em><u>DoD DICOM Object Filtering</u></em>.</a></p></td>
</tr>
<tr class="even">
<td><p>DoD artifacts</p>
<p>(non-radiology medical images, scanned documents, etc.)</p></td>
<td>Available if HAIMS (Health Artifact and Image Management Solution) servers are online and if HAIMS servers are capable of communicating with the CVIX.</td>
</tr>
</tbody>
</table>

### VA-to-DoD Image Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a VA site implements a VIX, that VIX also allows DoD clinicians to access locally stored DICOM images for VA/DoD shared patients. For additional details about the types of images involved, see [*<u>VA DICOM Images Provided to DoD</u>*.](#va-dicom-images-provided-to-dod)

![](vix-admin-guide/004.png)

> Note: DoD clinician image access requests are logged in the local VistA system.

> Note: DoD clinicians can access locally stored non-DICOM medical images and scanned documents using the CVIX alone as long as the patient in question is a shared VA/DoD patient. A local VIX is not required.

> Note: MUSE EKG waveforms, commercial PACS images, and other images not stored in VistA Imaging cannot be accessed by DoD clinicians.

### What is the CVIX?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Centralized VistA Image Exchange (CVIX) service functions as a VIX for the entire DoD. It:

- Provides a single point for VA access to DoD images. Among other things, this means that local site VIXes do not have to be modified if there is a change in how DoD image sources request or provide data; only the CVIX is impacted.
- Provides the portal used by all DoD clinicians to request all VA images. In this role, the CVIX uses the VistA system at Station 200 to provide VA treating facility information for shared patients and temporary VA credentials for DoD clinicians.

> The CVIX server also:

- Hosts the VistA Site Service
- Hosts the VIX Log Collector
- Supports the Advanced Image Web Viewer (AWIV). For more information about the AWIV, see the *[<u>VistA Imaging AWIV User Guide</u>](https://www.va.gov/vdl/application.asp?appid=105).*

#### VIXes and Image Sharing at Multidivisional Sites

> VIX implementation at a multidivisional site can be handled in two ways:

- A multidivisional site can implement a single VIX at a primary division to serve all divisions.
- A multidivisional site can implement a VIX at the primary division as well as at one or more subdivisions.

> When a local clinician at a VIX-equipped multidivisional site requests remote metadata and images, the “closest” VIX is used. For example:

- If the division where the clinician is logged into has a VIX, that VIX is used in preference to any other VIXes that may be present.
- If the division where the clinician logged into does not have a VIX, the VIX at the primary division is used.

> When clinicians outside of the multidivisional site request local metadata and images from a VIX-equipped multidivisional site:

- Metadata requests are always handled by the VIX at the primary division, because that VIX is local to the applicable VistA database.
- If a subdivision has local image storage and a VIX, the VIX at that subdivision provides the image to the remote requestor.
- If a subdivision has local image storage but does not have a VIX, the VIX at the primary division provides the image to the remote requestor.

> Performance considerations aside, these distinctions will not be apparent to clinicians after VIXes are fully implemented, and clinicians do not have to determine “which VIX to use.”

> Note: Images from different subdivisions within a multidivisional site are considered local images by client software (such as Clinical Display and VistARad). Because of this, the clients request these images directly and not via the VIX.

#### Optional Direct Connection to a DoD PACS Integrator

> If a participating DoD facility shares a direct network connection with a VA site that has a VIX, the DoD facility’s PACS integrator and the VA’s VIX can be configured to communicate directly for DICOM image transfers. This allows the images to be accessed at LAN speeds rather than WAN speeds.

> Note: This capability is used for DICOM images only.

> For more information about this option, contact the VistA Imaging development group at [<span class="mark">REDACTED</span>.](mailto:VHAVIVIXSETUP@va.gov)

## DICOM Importer III Application Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Importer III is a distributed application for allowing users to import outside studies from CD, DVD, or network sources, and process and reconcile studies that have entered the DICOM correct workflow. It is composed of a client application that uses the VIX as an application server, and a server component running on the site’s HDIGs that picks up reconciled studies and work items for asynchronous processing.

> In its role as the Importer III’s application server, the VIX provides the following broad categories of functionality:

- User services including login, user key retrieval, and related functions
- Patient services including search, patient sensitivity logging, and related functions
- Storage services including retrieving the current read and write locations for the image shares
- DICOM Importer application services, including
  - Validation of application version compatibility
  - Importer work item creation, updating, retrieval, and deletion
  - Decoding of DICOMDIR files
  - Inspecting images from studies to determine whether or not they already exist in VistA
  - Order retrieval for a specified patient
  - Metadata retrieval for Ordering Providers, Ordering Locations, Procedures, and Procedure Modifiers
  - Searching for and generating reports

## VIX Image Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MAG\*3.0\*177 introduced new VIX services to support a zero-footprint web based image viewer. The zero-footprint image viewer is not a standalone application. It is a service

> for external applications to integrate with their apps for viewing images stored in VistA Imaging or images in other enterprises accessible through VistA Imaging (i.e. DoD). It also introduces a specialized VIX called the rVIX to handle image and viewer requests from external applications such as eHMP and JLV. These external applications connect to the rVIX servers (currently located at the Austin Information Technology Center (AITC) and Philadelphia Information Technology Center (PITC)) for image and image related metadata queries.

> The rVIX serves out images (through the zero-footprint viewer) if the site that the user logged in to has not upgraded their VIX to MAG\*3.0\*170 or later. Otherwise, the viewing of images to the zero-footprint viewer will be redirected and served out through the user’s local VIX if the site has already installed MAG\*3.0\*170 or later. This arrangement keeps image traffic local to the facility as much as possible (for better performance) while continuing to provide access to images for users whose site VIX has not yet been upgraded. All image access using the zero-footprint image viewer, whether local or remote, goes through the VIX (and/or rVIX) and utilizes these new services.

![](vix-admin-guide/005.png)

> Image Viewer Data and Control flow Using eHMP as an Example Application

### New Services Introduced by MAG\*3.0\*170, 177 and 185:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VIX Viewer Service: The viewer service is the only public interface used by consuming applications such as eHMP and JLV. It is used to fetch image related metadata to view images in a web browser. The zero-footprint image viewer is hosted and served out by the Viewer service.
2.  VIX Render Service: The Render service is not a public interface, it is an internal service to pre-process images so they can be displayed efficiently in a web image viewing application. The Render service is used by the Viewer

> service. The Render cache is a cache of pre-processed images which allows subsequent image accesses through the viewer to be much quicker because there is no need to pre-process these images.

3.  Listener service: The listener service is a generic TCPIP listener that was introduced to speed up the VIX connections to VistA.
4.  SQLEXPRESS: SQLEXPRESS is a local database and associated services used to manage images in the cache.
5.  Supported SOP Classes Newly supported SOP Classes are being made available with MAG\*3.0\*185. [<u>(see the MAG\*3.0\*185 patch description for a detailed</u> <u>listing)</u>](http://vaww.oed.portal.va.gov/applications/VistAImaging/VistA%20Enterprise%20Documents/Forms/AllItems.aspx?RootFolder=%25)

### Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is important to ensure the viewer and render Windows services are up and running as they are critical for viewing images while using the zero-footprint image viewer. The listener service is a non-critical service as it is only used to help with performance of the VIX RPC calls.

> All VIX services prior to patch MAG\*3.0\*170 run under the Apache Tomcat Windows service. The new services run under their own separate Windows services. See details below to verify the all VIX Windows services and processes are operational.

> It is also important to verify that the VIX is sized appropriately and the usage of resources such as disk drive, CPU and memory are not exceeded.

### Windows Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ensure that Apache Tomcat, VIX Render Service, VIX Viewer Service, Listener Tool, and SQL Server (SQLEXPRESS) services are up and operational. See below for service details.

> Note: The Apache Tomcat version may vary depending on which patch level is installed.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vix-admin-guide/006.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vix-admin-guide/007.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vix-admin-guide/008.png)</p>
</blockquote></td>
<td>![](vix-admin-guide/009.png)</td>
</tr>
</tbody>
</table>

### Windows Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Verify that the VIX Viewer and Render processes are running in the Windows Task Manager.

6.  Launch the Windows Task Manager
7.  Look for the following processes:
    1.  VIX.Viewer.Service
    2.  VIX.Render.Service
    3.  Hydra.IX.Processer (x10) – the number of worker processes configurable on the VIX; the actual amount may be more or less
    4.  Hydra.VistA.Worker (x10) - the number of worker processes configurable on the VIX; the actual amount may be more or less
8.  If any of these processes are not running, restart the Viewer and Render services.

> Note: it can take up to a minute for all Hydra.IX.Processor processes to start

### Service Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If all related VIX Windows services and processes are running, the service logs can be reviewed to check for errors. By default, the logging level for the services is set to “Warn”. This means that warnings and errors will appear in the log files. If a more granular level of logging is needed for troubleshooting, it can be changed from “Warn" to “Trace” in the rules section at the end of each config file listed below:

1.  VIX Viewer Service
    1.  C:\Program Files\VistA\Imaging\Vix.Viewer.Service\NLog.config
    2.  C:\Program Files\VistA\Imaging\Vix.Viewer.Service\Worker.NLog.config
2.  VIX Render Service
    1.  C:\Program Files\VistA\Imaging\Vix.Render.Service\NLog.config
    2.  C:\Program Files\VistA\Imaging\Vix.Render.Service\Processor.NLog.config

> Note: Once you are done troubleshooting be sure to set the logging level back to “Warn” or the log files will become very large and can potentially fill up the hard drive

### Viewer Image Caching

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The zero-footprint image viewer uses pre-processed images and metadata that are stored in the VIX Render cache. The VIX render cache is a temporary cache of files that is built automatically when images are requested for viewing. When images are requested for viewing, the Viewer service fetches the images from the local VIX cache and calls the Render service to create optimized versions of those images for rendering in a web browser. The following describes how to manually re-initialize the Render cache on any given VIX server if needed:

1.  Stop the VIX Viewer and VIX Render services
2.  Delete all folders in the top level Render cache folder located in*:*

> *\<Cache Drive\> :\VIXRenderCache*

3.  Re-Install and configure SQL Express
    1.  Copy the SQL Express installation (SQLExpress_x64-12_0_2000_8.zip) to a local folder on the server
    2.  Extract all the files
    3.  In the command prompt window, navigate to the directory used for extracted files
    4.  Run the following command: Setup.exe

> ![](vix-admin-guide/010.png)/ConfigurationFile=ConfigurationFileInstall.ini

4.  Review the console window and ensure no errors were reported
5.  Restart the VIX Viewer and Render Services
6.  Verify Viewer operations by opening a few studies by launching via zero- footprint Image Viewer in JLV.

### VIX Viewer Test Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MAG\*3.0\*177 introduced a test page to access image viewer functionality without the need of running a consuming application. To utilize this functionality, the test page has to be manually enabled through the VIX Viewer configuration. To enable the test page, modify the Policies section of the C:\Program Files\VistA\|imaging\Vix.Config\Vix.Viewer.Config file to include the line below:

> The resulting file will look similar to the example below:

> Warning: The Test page provides no security so it cannot be left open. Once the test event is complete, the configuration file must be altered to comment out the test page enable.

> Restart the VIX Viewer Service.

> The default test information can be added by modifying the c:\Program Files\VistA\Imaging\Vix.Viewer.Service\test.json file.

> The file contains sections for making requests to the VIX Viewer. Below is an example of the file:

> *{*

> The Header section of the file contains the user and login information while the Items section contain individual query parameters for items to be sent to the viewer service.

> To access the Test page, enter the test page URL on the browser address bar: http(s)://\<Vix Host\>:\<viewer port\>/vix/viewer/test

![](vix-admin-guide/011.png)

> The user can edit the fields on the screen for both the body and the headings and submit them as different queries. When a query is submitted, the resulting page contains access to each study.

![](vix-admin-guide/012.png)

> Selecting the View option will open the VIX Viewer. The Manage button will open the manage page and the details show the study level return views.

1.  <span id="_bookmark22" class="anchor"></span>Currently Supported SOP Classes

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SOP Classes Newly Supported in MAG*3.0*185</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SOP Class Name</td>
<td>SOP Class UID</td>
</tr>
<tr class="even">
<td>Breast Tomosynthesis Image Storage</td>
<td>1.2.840.10008.5.4.1.1.13.1.3</td>
</tr>
<tr class="odd">
<td>Enhanced CT Image Storage</td>
<td>1.2.840.10008.5.4.1.1.2.1</td>
</tr>
<tr class="even">
<td>Enhanced MR Image Storage</td>
<td>1.2.840.10008.5.4.1.1.4.1</td>
</tr>
<tr class="odd">
<td>12-lead ECG Waveform Storage</td>
<td>1.2.840.10008.5.4.1.1.9.1.1</td>
</tr>
<tr class="even">
<td>General ECG Waveform Storage</td>
<td>1.2.840.10008.5.4.1.1.9.1.2</td>
</tr>
</tbody>
</table>

> Table 1: SOP Classes

## VIX Implementation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX is hosted on a dedicated VM. Careful considerations should be given when sizing the VIX. With the introduction of the VIX Viewer the VIX uses a lot more resources as it has to process the images for rendering, and it also can cache a large number of images.

> VIX configuration is largely automated and is handled as part of the VIX installation process.

> Installation details, including licensing, supported operating systems, and hardware requirements, are covered in the *VIX Installation Guide*.

> Note: Radiology exams acquired before the release of MAG\*3.0\*50 do not have the information needed by DoD display applications to properly split exams into series.

> VA sites that implement a VIX and that plan on sharing historic/related exams with DoD sites should execute the MagKat utility distributed with MAG\*3.0\*98. Doing so will populate DICOM series information for radiology exams acquired before the release of MAG\*3.0\*50. See the [*<u>VistA Imaging Storage Utilities Manual</u>*](https://www.va.gov/vdl/application.asp?appid=105) *f*or details.

## VIX Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following systems must be present for proper VIX operation.

> Except for the local VistA database, the VIX can function for a period of time at reduced efficiency if any of these systems are temporarily unavailable.

| Name/Location | Function                                                                                                                                          | Interface Method |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Local VistA       | Provides metadata and image locations to requesting VIXes, control access to local VIX transaction log; VistA logging of VIX-mediated image accesses. | LAN/RPC              |
| VIX cache         | Provides cached images for improved speed.                                                                                                            | LAN                  |

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 55%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name/Location</strong></th>
<th><strong>Function</strong></th>
<th><strong>Interface Method</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Remote VistA</td>
<td>Source of remotely stored VA images for local clinician access. (The VIX will continue to operate if a specific remote VistA system is unavailable; it just cannot provide images from that remote system)</td>
<td>WAN/http</td>
</tr>
<tr class="even">
<td><p>CVIX</p>
<p>(at VA data center)</p></td>
<td><p>Source of remotely stored DoD images for local clinician access. (The VIX will continue to operate if CVIX is unavailable; it just cannot provide DoD images.)</p>
<p>Also hosts the VistA site service, which provides connection data to the VIX. A VIX will use locally cached connection data if the VistA Site Service is not available.</p></td>
<td>WAN/http</td>
</tr>
<tr class="odd">
<td>RVIX</td>
<td>Metadata source for the consuming applications. The consuming application (eHMP, JLV or others) query the RVIX and the RVIX uses the federation to retrieve site specific information. The RVIX also has the ability to provide viewing for applications not authenticated against a specific site VIX.</td>
<td>WAN/http</td>
</tr>
</tbody>
</table>

## VIX Operational Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The operational priority of the VIX depends on the nature of the server where the VIX is installed and what the VIX is being used for at a given site.

### Standalone Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the VIX is installed on a standalone server, the VIX’s operational priority depends on the role of clinicians using the VIX for remote image access. If the standalone server where the VIX is installed is shut down:

- Clinicians using Clinical Display will still be able to retrieve remote images (at reduced performance) using Remote Image Views, so in this scenario, the operational priority of a VIX on a standalone server is low.
- Radiologists performing remote reading using the VistARad VIX-assisted operations will not be able to view local and remote images together unless the images are routed to VistARad using the DICOM Gateway’s routing function. Because of the variations involved, each site must make its own operational priority assessment in this case.
- Clinicians viewing images in eHMP and JLV retrieve images using the RVIX and the site VIX. Loss of either resource will block image viewing. The RVIX is already running on a load balanced cluster.
- IMPORTER: DICOM Importer II/III users will be unable to login and import images

> For detailed information about how the VIX responds if the hosting server is rebooted, see *[<u>VIX Startup and Shutdown</u>](#vix-startup-and-shutdown).*

## Security, Data Integrity, and Data Sensitivity Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX uses the following security, data integrity, and sensitive data handling methods.

- The VIX only responds to requests from authenticated applications. Application- level authentication is invisible to the user who initiated the request.
- Requests for VA data include user credentials that are authenticated and logged by the VistA system where the data resides. The VIX supports both Broker Security Enhancement (BSE) and pre-BSE-style remote logins.
- Access to the VIX transaction log requires authentication with the local VistA system (relative to the VIX in question) and is limited to VistA users that hold the MAG VIX ADMIN security key.
- VIX installation and VIX-to-VIX communications cannot proceed without a security certificate.
- The VIX delegates the sensitivity (data integrity checking implemented by the application that is requesting data from the VIX. \[When Clinical Display requests data, Clinical Display specific logic is used. When VistARad requests data, VistARad specific logic is used.\]).

# VIX General Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter covers:

- [<u>VIX General Operations Overview</u>](#vix-general-operations-overview)
- [<u>The VIX and the VistA Service</u>](#the-vix-and-the-vista-site-service)
- [<u>Using the VIX Transaction Log</u>](#using-the-vix-transaction-log)
- [<u>VIX Data Retention and Purges</u>](#vix-data-retention-and-purges)
- [<u>VIX Startup and Shutdown</u>](#vix-startup-and-shutdown)
- [<u>Monitoring/Maintaining the VIX</u>](#monitoringmaintaining-the-vix)
- [<u>Monitoring/Maintaining the VIX Viewer</u>](#monitoringmaintaining-the-vix-viewer)
- [<u>The VIX and Backups</u>](#the-vix-and-backups)

## VIX General Operations Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VIX operations fall into two categories.

- General operations, which are described in this chapter
- Function-specific operations (such as image sharing), which are covered later in this manual

> General operations are the activities that always occur as long as the VIX is running. These include retrieving data from the VistA Site Service, general logging, purging old data, and VIX startup/shutdown.

> While most VIX operations are automated, the VIX does require some basic monitoring. For more information, see [*Monitoring/Maintaining the VIX*.](#monitoringmaintaining-the-vix)

## The VIX and the VistA Site Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Site Service is a CVIX-hosted central repository of connection information. A VIX (along with other VistA Imaging components) uses the VistA Site Service to get connection information for other VistA sites, other VIXes, and the CVIX itself.

> The VIX automatically downloads and caches connection information from the site service each day at 11:00 PM and any time the VIX is restarted. The VIX uses this cached information rather than access the site service for every transaction.

> If your local connection information for VistA or the VIX changes, you must do the following:

1.  Contact the [<span class="mark">REDACTED</span>](mailto:VHAVISITESERVICE@va.gov) mail group to update your site’s information in the VistA Site Service.
2.  After step 1 is complete, re-run the VIX installation wizard to update your VIX configuration information. For details, see the [*<u>VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

## Using the VIX Transaction Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX transaction log records information about every image and metadata transfer handled by the VIX. Entries in the log are retained for 30 days, and then purged. A permanent backup copy of the VIX transaction log is also stored remotely.

> The VIX transaction log can be accessed using Internet Explorer 7 (or later) and

> Firefox 3 (or later). The main transaction log Web page can be used to display, filter, and export log entries of interest.

> To access the transaction log you will need the following:

- A VistA account that has the MAG VIX ADMIN security key assigned to it (while the log is a Web page, the VIX uses a VistA account to secure the log).
- Access to https://\<FQDN\>/Vix/ssl/VixLog.jsp

> (where \<FQDN\> is the server the VIX is installed on.)

> Note: For security reasons, completely close out of your browser at the end of your session.

> You can only access the VIX transaction log while the VIX is running.

#### To view the VIX transaction log, complete the following steps.

1.  Navigate to https://\<FQDN\>/Vix/ssl/VixLog.jsp.
2.  Enter your VistA access and verify codes in the User Name and Password boxes and click OK.

> Note: Transaction log credentials are authenticated against the local VistA system. Attempting to use Windows credentials will not work.

3.  The VIX Transaction Log page will display.
    - By default, the page displays the 100 most recent transactions for the current day.
    - The transactions are ordered from newest to oldest.
4.  For detailed information about each field in the log, see [*<u>VIX Transaction Log Fields</u>*](#vix-transaction-log-fields).
5.  To view different parts of the log, use the paging buttons near the top and at the bottom of the log as follows:
    - Click ![](vix-admin-guide/013.png) to show the next page of (older) entries.
    - Click ![](vix-admin-guide/014.png) to show the previous page of (newer) entries.
    - Click ![](vix-admin-guide/015.png) to show the first page (newest) entries in the log.

#### To change the date range and page size in the VIX transaction log, complete the following steps.

1.  To change the date range used to filter log entries, change the values in the Start Date and End Date boxes, and then click Show in Browser.
    - Dates are formatted as MM/DD/YYYY.
    - The most recent log entries are shown first.
2.  To change the number of entries displayed on each page, select a different value from the Transactions per Page box, and then click Show in Browser.

#### To export part of the transaction log, complete the following steps.

1.  On the Transaction Log page, use the date range boxes near the top of the page to specify the desired date range of entries to export.
    - 1,000 exported log entries will result in an approximately 0.5 megabyte file.
    - The Transactions per Page setting does not apply when log entries are supported.
2.  Click Save as CSV for comma-separated values or Save as TSV for tab-separated values.
3.  Use the browser Save dialog box to specify where the file will be stored.
4.  Use a spreadsheet program or a text editor to open the resulting file.

### VIX Transaction Log Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the transaction log is displayed in a Web browser, the following fields are shown. These fields are also included when the transaction log is exported as a tab-separated (.TSV) or comma-separated (.CSV) file.

> Fields that only appear when the transaction log is exported are listed in the next section.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>VIX Transaction Log Fields</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Date and Time</td>
<td>When the transaction was processed by the VIX. Formatted as MM-DD-YYYY, HH:MM:SS, AM/PM.</td>
</tr>
<tr class="odd">
<td>Time on VIX</td>
<td>The length of the transaction in milliseconds, beginning when the VIX receives a message and ending when the VIX begins to send the response.</td>
</tr>
<tr class="even">
<td>ICN</td>
<td><p>The Integration Control Number used to uniquely identify the patient across the VA and DoD systems.</p>
<p>(Note that the ICN is not equivalent to the VA patient ID, and is not considered Protected Health Information.)</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>VIX Transaction Log Fields</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Query Type</td>
<td><p>A multi-part field that indicates [<em>handler method receiving site &lt;- sending site</em>].</p>
<p><em>handler</em> identifies the VIX Web application that handled the request. For details see <a href="#vix-interfaces"><em><u>VIX Interfaces</u></em>.</a></p>
<p><em>method</em> identifies the specific operation performed: image transfer – Used to transfer an image.</p>
<blockquote>
<p>getStudyList – Provides the DoD with study metadata from a VA VistA system via the CVIX.</p>
<p>Other methods relate to metadata and are described in</p>
<p><a href="#remote-metadata-retrieval"><em><u>Remote Metadata</u></em>.</a></p>
</blockquote>
<p><em>receiving site &lt;- sending site</em> indicates:</p>
<blockquote>
<p>The station number and home community ID (where applicable) of the sending and receiving sites.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Query Filter</td>
<td>Applies to study metadata only. Indicates whether a list of all available studies for a patient was transferred or if a subset based on date was transferred.</td>
</tr>
<tr class="even">
<td>Asynchronous</td>
<td>Indicates whether the transaction was performed asynchronously (true) or synchronously (false).</td>
</tr>
<tr class="odd">
<td>Items Returned</td>
<td><p>The number of items returned to the requester.</p>
<p>For study metadata, indicates the number of studies or images in the list being transmitted. For an image, this field will have a value of 1 if the requested image was transmitted or 0 if the requested image was not found.</p>
<p>For other operations, this column is not populated.</p></td>
</tr>
<tr class="even">
<td>Items Received</td>
<td><p>The number of items retrieved from the remote site.</p>
<p>For study metadata, indicates the number of studies or images in the list being received. For an image, this field will have a value of 1 if the requested image was received or 0 if the requested image was not received.</p>
<p>If the VIX is operating asynchronously, the values in this field may not match the values in the Items Returned field.</p>
<p><em>In the exported log, this field is labeled “Data Source Items Received.”</em></p></td>
</tr>
<tr class="odd">
<td>Bytes Returned</td>
<td><p>If populated, the amount of data returned in the request.</p>
<p><em>In the exported log, this field is labeled “Façade Bytes Returned.”</em></p></td>
</tr>
<tr class="even">
<td>Bytes Received</td>
<td><p>If populated, the amount of data received in the request.</p>
<p><em>In the exported log, this field is labeled “Data Source Bytes Received.”</em></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>VIX Transaction Log Fields</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Throughput</td>
<td>The image transfer rate. Both the rate and the units of measurement (KB/sec, MB/sec are indicated). Not populated for metadata. This value is calculated at runtime and is not present in the exported log.</td>
</tr>
<tr class="odd">
<td>Quality</td>
<td><p>Populated for images only. Can be one of the following: THUMBNAIL</p>
<blockquote>
<p>REFERENCE DIAGNOSTIC</p>
<p>DIAGNOSTIC UNCOMPRESSED</p>
</blockquote>
<p>For more information about these parameters, see <em><a href="#image-quality-and-vix-compression">Image</a></em> <a href="#image-quality-and-vix-compression"><em>Quality and VIX Compression</em>.</a></p></td>
</tr>
<tr class="even">
<td>Command Class Name</td>
<td>Internal VIX command used for debugging and support.</td>
</tr>
<tr class="odd">
<td>Originating IP Address</td>
<td>The IP address of the workstation that initiated the image or metadata request.</td>
</tr>
<tr class="even">
<td>User</td>
<td>The name of the clinician that initiated the request.</td>
</tr>
<tr class="odd">
<td>Item in Cache?</td>
<td><p>TRUE indicates the image is served from the cache.</p>
<p>FALSE indicates the image had to be retrieved from its original storage location.</p>
<p>Not populated for other types of transactions.</p></td>
</tr>
<tr class="even">
<td>Error Message</td>
<td>If a request fails, this field contains an error message describing the failure.</td>
</tr>
<tr class="odd">
<td>Modality</td>
<td>If applicable, indicates the modality associated with an image request (standard DICOM modality type codes are used).</td>
</tr>
<tr class="even">
<td>Purpose of Use</td>
<td>Included for HIPAA tracking purposes.</td>
</tr>
<tr class="odd">
<td>Data Source Protocol</td>
<td><p>The source of the data being handled: vistaimaging – Data from a VistA system</p>
<blockquote>
<p>mix,dx – DICOM data from a source outside of VistA (typically the DoD)</p>
<p>vftp – Data from another VIX</p>
<p>mix,ax – Non-DICOM (artifact) data from a source outside of VistA (typically the DoD)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>VIX Transaction Log Fields</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>Response Code</td>
<td><p>The response code for a request; generally equivalent to HTTP response codes but in some cases they are used for statuses specific to the VIX. Typical values include:</p>
<blockquote>
<p>200 – OK (success) 401 – Unauthorized 404 – Not found</p>
<p>409 – Image exists but is not yet available on DoD PACS integrator and/or Imaging jukebox</p>
<p>412 – BSE token expired</p>
<p>415 – Image conversion exception 500 – Internal server error</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Realm Site Number</td>
<td>The STATION NUMBER (field (#99)) of the INSTITUTION file (#4) of the site that the requester’s credentials are authenticated against.</td>
</tr>
<tr class="even">
<td>URN</td>
<td>Only populated for image transactions. Universal Resource Name; the unique name of the image being requested.</td>
</tr>
<tr class="odd">
<td>Transaction Number</td>
<td>The Globally Unique Identifier (GUID) for an image or metadata transaction. For transactions that originate from Clinical Display or the DoD, the same identifier will be reflected in the Image Access log at the site where the images are stored.</td>
</tr>
<tr class="even">
<td>VIX Software Version</td>
<td>The software version used by the local VIX.</td>
</tr>
<tr class="odd">
<td>VistA Login Method</td>
<td>The method used to access a VistA system. This is only populated when connecting to VistA and only for the transaction that initiates the connection. Possible values are BSE, CAPRI, or LOCAL.</td>
</tr>
<tr class="even">
<td>Client Version</td>
<td>The version number of the Clinical Display software. This field is populated only for Clinical Display requests.</td>
</tr>
<tr class="odd">
<td>Data Source Method</td>
<td>Identifies the specific operation performed by the data source.</td>
</tr>
<tr class="even">
<td>Data Source Version</td>
<td>The version number of the data source.</td>
</tr>
<tr class="odd">
<td>DataSourceResponse Server</td>
<td><p>The name of the server that responded to the metadata or image request.</p>
<p>Only populated for requests directed to a VIX or CVIX.</p>
<p><strong>Note:</strong> This field cannot be populated if the requesting or responding server is a MAG*3.0*83 VIX.</p></td>
</tr>
<tr class="even">
<td>VIX Site Number</td>
<td>The site number of the local VIX (as defined in the local VIX’s VixConfig.xml file). The site number should match the station number (field #99) defined in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td>Requesting VIX Site Number</td>
<td>The site number of the requesting VIX (as defined in the remote VIX’s VixConfig.xml file), Only populated for Federation (VIX-to- VIX) requests. The site number should match the station number (field #99) defined in the INSTITUTION file (#4).</td>
</tr>
</tbody>
</table>

### VIX Transaction Log Fields (Export Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the transaction log is exported as a tab- or comma-separated file, the exported file includes all of the fields available in the browser view of the log (see previous section). The exported file also includes additional fields that are described in the following table.

| VIX Transaction Log Fields (export only) |                                                                                                                                                                                    |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                                     | Description                                                                                                                                                                    |
| Façade Bytes Retrieved                       | The number of bytes returned to the requestor, where the requestor could be Clinical Display, VistARad, another VIX, or the CVIX.                                                  |
| Data Source Bytes Returned                   | The number of bytes returned from the data source, where the data source could be a remote VistA system, a VIX, the CVIX, or a DoD data source such as the DAS interface or HAIMS. |
| Machine Name                                 | Name of the VIX server that performed the transaction.                                                                                                                             |
| Requesting Site                              | The ID of the site that originated the request; this value is also shown in the Query Type column.                                                                                 |
| Exception Class Name                         | Internal data used for debugging and support.                                                                                                                                      |
| Time to First Byte                           | Number of milliseconds elapsed from the point where the VIX opens a connection to a remote site until the remote site begins responding to the request.                            |
| Responding Site                              | The ID of the site that filled the request; this value is also shown in the Query Type column.                                                                                     |
| Command ID                                   | Internal ID used for debugging and support.                                                                                                                                        |
| Parent Command ID                            | Internal ID used for debugging and support.                                                                                                                                        |
| Façade Image Format Sent                     | The format of the image VIX returns to the requester.                                                                                                                              |
| Façade Image Quality Sent                    | The quality of the image VIX returns to the requester; in some cases this quality will be better than the quality requested (as indicated in the “Quality” column).                |
| Data Source Image Format Received            | The format of the image VIX receives from its source.                                                                                                                              |
| Data Source Image Quality Received           | The quality of the image VIX receives from its source.                                                                                                                             |
| Debug Information                            | Internal messaging used for debugging and support.                                                                                                                                 |
| Thread ID                                    | The name of the thread that processed the transaction.                                                                                                                             |

### Log Collector Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX Log Collector service automatically backs up VIX transaction logs and stores the backup copies on a centralized data center server. This allows the information in VIX transaction logs to be retained after the logs are purged locally (the local retention period is 30 days). The Log Collector service is hosted on the same data center servers where the CVIX resides.

> Once a day, the log collector service copies each VIX’s local transaction logs to a data server storage area for permanent storage. The time that the backup is performed is configured centrally, and is set to be during low-usage hours.

> When the Log Collector performs its daily backup, it collects only one full day’s worth of VIX transaction log entries to limit network impact. For example: on Monday, the Log Collector service will collect all VIX log entries from the previous Saturday.

> If the Log Collector cannot reach a VIX on a given day, it queues its backup attempt and attempts to copy any backlogged items during the next backup period. Multiple failed attempts to back up a specific transaction log will generate an email warning to data center administrator’s (email address entered during the VIX installation), who then would contact the local VIX administrator if local corrective action were needed.

> The VIX Log Collector service does not require any site-level or local VIX configuration.

## VIX Data Retention and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX writes only a limited amount of data to VistA; this is described in *[<u>Database</u>](#database-information) [<u>Information</u>](#database-information)*. The VIX transaction log is stored on the server where the VIX is installed (see page [21](#using-the-vix-transaction-log) for details); images and associated metadata are stored in the VIX cache.

> The VIX runs a daily purge process for locally stored data as described in the following table:

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th><strong>When Performed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Purge Java logs</td>
<td>1 A.M. daily for Java log entries more than 30 days old.</td>
</tr>
<tr class="even">
<td>Purge transaction log entries</td>
<td>2 A.M. daily for transaction log entries more than 30 days old.</td>
</tr>
<tr class="odd">
<td>Purge VIX cache</td>
<td><p>3 A.M. daily for images more than 30 days old.</p>
<p>Once per minute for old VA metadata, once per hour for old DoD metadata</p></td>
</tr>
</tbody>
</table>

## VIX Startup and Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX service is designed to be running at all times; when the VIX is implemented on the same cluster used for Imaging resources, the VIX is a part of the same resource group that is used to manage image storage, and is not intended to be shut down or restarted independently from the rest of the resource group.

> In general, the only time the VIX service needs to be shut down independently from the hosting server is when the VIX software is being updated. For details, including user impact, refer to the *VIX Installation Guide*.

> The following table summarizes how the VIX service responds if there is a restart of the server on which the VIX is installed or if there is an interruption of the VIX’s connection to the local VistA System.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Scenario</strong></th>
<th><strong>VIX Service Behavior</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Unplanned server shutdown (or failover)</td>
<td>If the VIX is installed on a standalone server, the VIX service restarts itself after the server is restarted.</td>
</tr>
<tr class="even">
<td>Planned server shutdown (maintenance, Microsoft software updates, etc.)</td>
<td>The VIX service does not need to be stopped; the VIX service will restart automatically once the server is restarted.</td>
</tr>
<tr class="odd">
<td>VIX service fatal error (server unaffected)</td>
<td>On a standalone server, the VIX service will restart itself automatically after 60 seconds, and continue restarting itself if it encounters additional errors.</td>
</tr>
<tr class="even">
<td>Local VistA system restart and/or restore</td>
<td><p>In the event of a local VistA system restart, the VIX will automatically refresh any previously cached connections within 30 seconds to 1 minute.</p>
<p>VIX operations are unaffected in a VistA system database restore; the VIX stores no configuration information on VistA.</p></td>
</tr>
</tbody>
</table>

## Monitoring/Maintaining the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In typical usage scenarios, the VIX service will need only minimal monitoring and maintenance.

- Once a day, access the transaction log to verify that the VIX is running and that the VIX communication ports (8080 and 8443) are not blocked. If necessary, you can also verify the state of the VIX service directly as described below.
- Once a week, check available space on the drive used for the VIX cache. In a newly implemented VIX, the VIX cache size will increase rapidly for the first 30 days, and then should level off as the VIX begins to purge older images.
- Optionally, you can get a sense of the VIX processing load by using the Windows Task Manager to determine the CPU cycles being consumed by the Apache Tomcat task.

> As described in the previous section, the VIX service will restart automatically if the hosting server is restarted.

### Checking the VIX Service: 2012 R2 Standalone Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  On the server where the VIX is installed, log in as a local administrator.
2.  Open the Services window (click Start \| All Programs \| Administrative Tools \| Services).
3.  On the right side of the window, locate the Apache Tomcat service and verify that its status is Started.

![](vix-admin-guide/016.png)

## Monitoring/Maintaining the VIX Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX Viewer hosts two independent services. These services show up as the VIX Viewer Service and the VIX Render Service.

![](vix-admin-guide/017.png)

> The Viewer and Render services must be operational for the site VIX to be able to provide viewing. To verify operation, one has to log into the consuming applications, select a patient with images, and display the images. If the operation fails, proceed to the trouble shooting section.

### Troubleshooting the VIX Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Operation of the VIX Viewer depends on the presence and correct operation of a number of resources.

- The Apache Tomcat service must be operational and the VIX services must be operational
- The Microsoft SQL Express instance must up and operational
- There should be sufficient disk space available for the VIX and Render caches
- The VIX Viewer and Render Services must be running and operational

> To verify that the VIX is operational proceed to the normal trouble shooting of VIX services.

> To verify that that Microsoft SQL Express instance is operational, review the Render Service logs located in:

> *\<System Drive\>\Program Files\VistA\Imaging\VIX.Render.Service\log*

> Look for any errors related to access to SQL server. In case the SQL server is failing, follow the steps outlined in Fixing the VIX Viewer Cache Errors.

#### Fixing the VIX Viewer Cache Errors

1.  Stop the VIX Viewer and VIX Render Services
2.  Delete all the files in the Viewer cache located in

> *\<Cache Drive\> :\VIXRenderCache*

3.  Install and configure SQL Express
    1.  Copy the SQL Express installation (SQLExpress_x64-12_0_2000_8.zip) to a local folder on the server
    2.  Extract all the files
    3.  Launch a command prompt window as a local Administrator
    4.  In the command prompt window, navigate to the directory used for extracted files
    5.  ![](vix-admin-guide/018.png)Run the following command: Setup/ConfigurationFile=ConfigurationFileInstall.ini
4.  Review the console window and ensure no errors were reported
5.  Restart the VIX Viewer and Render Services
6.  Verify viewer operations by opening a few studies

#### Analyzing VIX Viewer Logs

> The VIX Viewer keeps logs in *\<System Drive\>:\Program Files\VistA\Imaging\VIX.Viewer.Service\log and \<System Drive\>:\Program Files\VistA\Imaging\VIX.Render.Service\log.* Review the log for errors.

> The logging level is controlled by the setting in the NLog.config file located in the directory above the logs.

> \<rules\>

> \<logger name="\*" minlevel="Warn" writeTo="logfile" /\>

> \</rules\>

> \</nlog\>

> To get more details, the minlevel property can be set to “Trace”. The Trace level will generate a lot of logging, so it is advised to set it back to “Warn” for normal operation.

## The VIX and Backups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX itself does not need to be explicitly backed up.

- The VIX transaction logs are automatically backed up offsite.
- The VIX cache is transitory and does not need to be backed up.
- VIX-specific configuration settings can be recovered by reinstalling the VIX software.

> Note: The Laurel Bridge DCF toolkit that the VIX uses has a unique product serial number that should be stored in a safe place in case the VIX needs to be reinstalled. For details about where and how this serial number is used, see the [*<u>VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105) If you need to recover this serial number and there is no local record of it, you can contact the <span class="mark">REDACTED</span> mail group.

# VIX Image Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes the VIX operations that are specific to image sharing. Specifically, this chapter covers:

- [<u>Remote Metadata Retrieval</u>](#remote-metadata-retrieval)
- [<u>Remote Image Retrieval</u>](#metadata-requests-from-the-new-image-viewer)
- [<u>Caching of Metadata and Images</u>](#caching-of-metadata-and-images)
- [<u>Image Sharing-related Logging</u>](#image-sharing-related-logging)
- [<u>Image Sharing and VIX Timeouts</u>](#image-sharing-and-vix-timeouts)
- [<u>Troubleshooting</u>](#troubleshooting-1)

## Remote Metadata Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a VIX is used to retrieve remote images, the image retrieval is always preceded by the retrieval of applicable metadata<sup>\*</sup>. Also, in some cases such as the retrieval of an exam report, metadata retrieval is the only action needed to fulfill a clinician’s data request.

> Many Clinical Display or VistARad operations will silently trigger requests to the VIX to retrieve metadata from remote sites. In general, the VIX handles metadata retrievals as follows:

1.  The application (Clinical Display or VistARad) issues a request for metadata based on a clinician’s activities.
2.  The local VIX determines whether caching is allowed for the specific request. For details about which requests are cached, see the tables in the next two sections.
3.  If caching is not allowed, the VIX skips all cache checks, retrieves the metadata directly from the remote site, and proceeds to step 5.
4.  If caching is allowed, the VIX first attempts to retrieve the desired metadata from its own local cache. If the metadata cannot be found locally, it is retrieved from the remote site.

| Remote site type | How remote metadata is retrieved                                                                                  |
|----------------------|-----------------------------------------------------------------------------------------------------------------------|
| VA site with VIX     | The remote VIX retrieves the metadata, either from the remote VIX’s own cache or from the remote site’s VistA system. |

- In the context of the VIX, metadata is anything that describes an image or image-like object. Metadata includes patient names, IDs of various types, procedure names, index field values, number of images in an exam, radiology reports, and so on.

| Remote site type | How remote metadata is retrieved                                                         |
|----------------------|----------------------------------------------------------------------------------------------|
| VA site; no VIX      | The local VIX retrieves the metadata directly from the remote VistA Imaging system.          |
| DoD (via CVIX)       | The CVIX retrieves the metadata either from its own cache or from the applicable DoD system. |

5.  The local VIX passes the data back to the requesting application.

### Metadata Requests from Clinical Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table summarizes the metadata requests that Clinical Display can issue to a

> VIX. The request names used in the table are reflected in the Query Type field of the VIX transaction log.

<table style="width:100%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 61%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Clinical Display Metadata Request</strong></th>
<th><strong>Data Returned</strong></th>
<th><p><strong>VIX</strong></p>
<p><strong>caching allowed?</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>getImageDev Fields</td>
<td>Populates data in the Image Information Advanced window when <strong>Field Values</strong> is used to look up IMAGE file (#2005) values for a remote image.</td>
<td>No</td>
</tr>
<tr class="even">
<td>getImage Information</td>
<td>Populates data in the Image Information window.</td>
<td>No</td>
</tr>
<tr class="odd">
<td>getImageSystem GlobalNode</td>
<td>Populates data in the Image Information Advanced window when <strong>^MAG(2005</strong> is used to display the global for a remote image.</td>
<td>No</td>
</tr>
<tr class="even">
<td>getPatientShallow StudyList</td>
<td><p>Provides the study metadata used in remote site buttons, the Image List, and Abstracts windows.</p>
<p><strong>Note:</strong> For this request, the local VIX always gets fresh data from remote VistA system and always locally caches the data it retrieves. This is done so the data is readily available for getStudyImageList requests that use the same data.</p></td>
<td>Yes, see note</td>
</tr>
<tr class="odd">
<td>getStudyImageList</td>
<td>Provides the study metadata needed to populate the Group Abstracts window.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>getStudyReport</td>
<td>Retrieves a report for a remote exam.</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>pingServerEvent</td>
<td>Indicates whether a remote site is available.</td>
<td>n/a</td>
</tr>
<tr class="even">
<td>postImageAccess Event</td>
<td>Sends a message to a VA site IMAGE ACCESS LOG file (#2006.95) when a VA image is viewed, copied, or printed.</td>
<td>n/a</td>
</tr>
</tbody>
</table>

### Metadata Requests from VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table summarizes the metadata requests that VistARad can issue to a VIX. The request names used in the table are reflected in the Query Type field of the VIX transaction log.

<table style="width:100%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 61%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistARad Metadata Request</strong></th>
<th><strong>Data Returned</strong></th>
<th><p><strong>VIX</strong></p>
<p><strong>caching allowed?</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>getActiveWorklist</td>
<td>Populates remote worklists accessed using the VistARad Monitored Sites exam list tab.</td>
<td>No</td>
</tr>
<tr class="even">
<td>getExamDetails</td>
<td><p>Retrieves additional exam metadata when a local VistARad user opens a remote exam.</p>
<p><strong>Note:</strong> In some cases this request can be partially filled using data previously cached to fill a recent getSiteExamList request. If this is the case, the VIX will use whatever cached data is available and pull the rest of the data from the remote site.</p></td>
<td>Yes, see note</td>
</tr>
<tr class="odd">
<td>getExamSiteMeta dataCachedStatus</td>
<td>Checks to see if a list of exams for a remote patient is already on the local VIX cache.</td>
<td>n/a</td>
</tr>
<tr class="even">
<td>getReport</td>
<td>Retrieves a report for a remote exam.</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>getRequisition</td>
<td>Retrieves a requisition for a remote exam.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>getSiteExamList</td>
<td><p>Retrieves a list of exams for a specific patient from a remote site.</p>
<p><strong>Note:</strong> Whenever this request is made, the VIX automatically issues an asynchronous getExamDetails request as well.</p></td>
<td>Yes, see note</td>
</tr>
<tr class="odd">
<td>pingServer</td>
<td>Indicates if a remote site is available.</td>
<td>n/a</td>
</tr>
<tr class="even">
<td>postImageAccess</td>
<td>Sends a message to a VA site IMAGE ACCESS LOG file (#2006.95) when a VA image is viewed, copied, or printed.</td>
<td>n/a</td>
</tr>
</tbody>
</table>

## Metadata Requests from the New Image Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 61%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>New Image Viewer Metadata Request</strong></th>
<th><strong>Data Returned</strong></th>
<th><p><strong>VIX</strong></p>
<p><strong>caching allowed?</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/vix/viewer/studyqu ery</td>
<td>The basic metadata of the studies.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>detailsUrl</td>
<td>Detailed metadata about the study.</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>thumbnailUrl</td>
<td>Thumbnail image that could be used to represent the study.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>manageUrl</td>
<td>A web page that displays image thumbnails, imaging data etc. You can delete images or manage controlled images using this web page.</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>viewerUrl</td>
<td>A web page containing the image viewer.</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>/vix/viewer/ping</td>
<td>Check if the service is running.</td>
<td>Yes</td>
</tr>
</tbody>
</table>

## Remote Image Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a clinician selects a remote VA or DoD image for display, the VIX uses complex processing to deliver the most desirable image in the shortest amount of time.

> The following steps summarize this process.

1.  The clinician initiates the display of a remote VA or DoD image.
2.  The application (Clinical Display or VistARad) issues a request for the image to the local VIX. The contents of this request (which was provided by the VIX in an earlier metadata retrieval) includes the following:
    - The image identifier
    - The desired image quality (see [*<u>Image Quality and VIX Compression</u>*](#image-quality-and-vix-compression))
    - A list of acceptable image formats (see [*Image Types vs. Image Formats*](#image-types-vs.-image-formats))
3.  The local VIX first checks its own local cache for the image. If the VIX finds the image in its cache and if the image of the desired quality and is in any of the acceptable formats, the local VIX stops the search and proceeds to step 6.
4.  If the image is not stored on the local VIX’s cache, the VIX queries the remote site for the image.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Remote Site Type</strong></th>
<th><strong>How Remote Image is Retrieved</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA site with VIX</td>
<td><p>The remote VIX retrieves the image, either from the remote VIX’s own cache or from the remote site’s VistA system.</p>
<p>The remote VIX may convert or compress the image (based on the quality specified in the request) to increase the speed of WAN transfers.</p></td>
</tr>
<tr class="even">
<td>VA site; no VIX</td>
<td>The local VIX retrieves the image directly from the remote VistA Imaging system.</td>
</tr>
<tr class="odd">
<td>DoD (via CVIX)</td>
<td><p>The CVIX retrieves the image, either from its own cache or from the applicable DoD system.</p>
<p>The CVIX may convert or compress the image (based on the quality specified in the request) to reduce retrieval times.</p></td>
</tr>
</tbody>
</table>

5.  If needed, the local VIX decompresses or converts the image into one of acceptable image formats.
6.  The local VIX passes the image to the requesting application.

### Image Quality and VIX Compression

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The combination of the requested image quality and whether or not there is a remote VIX involved can affect how a VIX fills a request for a remote image.

> The following table summarizes these processing differences. For simplicity’s sake, this table presumes that the request originates locally, that the requester is a VA clinician, and that an image of the requested quality is *not* already in either the local or remote VIX cache (in which case some or all of the processing would be skipped).

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Requested by</strong></th>
<th><strong>VIX Compression Logic<sup>*</sup></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIAGNOSTIC</td>
<td>Clinical Display Radiology Viewer and VistARad, VIX Viewer</td>
<td><p>If a remote VIX is present, the remote VIX locates the highest-resolution image available and automatically converts the image into a lossless compressed format before sending the image across the WAN to the local</p>
<p>VIX. For radiology images, lossless DICOM encapsulated JPEG 2000 is the most frequently used format with a compression ratio of about of 2.5:1.</p>
<p>If there is no remote VIX, the local VIX locates the highest- resolution image available at the remote site and pulls the image across the WAN in the image’s native (uncompressed) format.</p></td>
</tr>
</tbody>
</table>

- If the requested image originates from the DoD, the CVIX performs the same operations that a remote VIX would perform.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Requested by</strong></th>
<th><strong>VIX Compression Logic<sup>*</sup></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DIAGNOSTIC</p>
<p>UNCOMPRESSED</p></td>
<td>Clinical Display Full Resolution Viewer, VIX Viewer</td>
<td><p>If a remote VIX is present, it will automatically package the images as a ZIP file before transferring them across the WAN.</p>
<p>If there is no remote VIX, the local VIX locates the highest- resolution image available at the remote site and pulls the image across the WAN in the image’s native (uncompressed) format.</p></td>
</tr>
<tr class="even">
<td>REFERENCE</td>
<td>Clinical Display Radiology Viewer only, VIX Viewer</td>
<td><p>If a remote VIX is present, it generates a new reference quality copy of the image using the highest resolution source image available. Then the remote VIX sends the reference quality image across the WAN to the local VIX.</p>
<ul>
<li><p>The new image will be as good as, if not better than, any pre-existing reference quality image(s) stored on the remote VistA system.</p></li>
<li><p>The compression ratio achieved averages about 24:1 for CR images and 10:1 for CT and MR images.</p></li>
</ul>
<p>If there is no remote VIX, the local VIX checks the remote VistA system for a downsampled image.</p>
<ul>
<li><p>If a downsampled image is present (as is usually the case for CR or DR images), that image is retrieved across the WAN.</p></li>
<li><p>If a downsampled image is not present (as may be the case for CT and MR images), the local VIX pulls the full resolution image from the remote site across the WAN. The local VIX then converts the image to one of the formats specified in the image request.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>THUMBNAIL</td>
<td>Clinical Display, VIX Viewer</td>
<td>The presence or absence of a remote VIX does not impact how thumbnail images are handled.</td>
</tr>
</tbody>
</table>

### Image Types vs. Image Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a local VA clinician requests a remote image from the VIX, an earlier metadata retrieval has already established the formats that the desired image can be delivered in.

> The following table lists possible formats that the VIX can return based on image type. When multiple formats are listed, the VIX will check each potential storage location (VIX local cache, VIX remote cache \[if present\], remote VistA system) for an instance of the image in any of the possible formats before proceeding to the next “more remote” storage location. If the image has to ultimately be retrieved from the remote site, and if it is not in one of the possible formats, the image will be converted to one of the possible formats before returning it to the requesting application.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 54%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Image Type (from</strong></p>
<p><strong>#2005.021</strong></p></th>
<th><strong>Image Description (from #2005.021)</strong></th>
<th><strong>Possible formats returned by VIX</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| 1       | JPEG                                                        | JPEG, TIFF, bitmap        |
|---------|-------------------------------------------------------------|---------------------------|
| 3\*     | XRAY (TGA) (intended for Clinical Display Radiology Viewer) | DICOMJ2K, J2K, DICOM, TGA |
| 3\*\*   | XRAY (TGA) (intended for VistARad)                          | DICOM, TGA                |
| 9       | Black and White image                                       | JPEG, TIFF, bitmap        |
| 17      | Color Scan                                                  | JPEG, TIFF, bitmap        |
| 18      | Patient Photo                                               | JPEG, TIFF, bitmap        |
| 19      | XRAY_JPEG                                                   | JPEG, TIFF, bitmap        |
| 15      | TIFF                                                        | JPEG, TIFF, bitmap        |
| 21      | Motion Video (AVI, MPG)                                     | AVI                       |
| 100\*   | DICOM (intended for Clinical Display Radiology Viewer)      | DICOMJ2K, J2K, DICOM, TGA |
| 100\*\* | DICOM (intended for VistARad)                               | DICOM, TGA                |
| 101     | HTML                                                        | HTML                      |
| 102     | Word                                                        | DOC                       |
| 103     | ASCII Text                                                  | TEXT_PLAIN                |
| 104     | PDF                                                         | PDF                       |
| 105     | RTF                                                         | RTF                       |
| 103     | Audio (WAV, MP3)                                            | WAV, MP3                  |

| \* The local VIX will always attempt to convert the requested image to DICOM J2K if the header data is available. |
|-------------------------------------------------------------------------------------------------------------------|
| \*\* The local VIX will always attempt to convert the requested image to DICOM if the header data is available.   |

## Caching of Metadata and Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX automatically stores all images and most of the metadata it handles as a part of image sharing in its own local cache. The VIX cache is self-managing and is independent from other Imaging storage areas and caches.

> The VIX cache improves the VIX performance by storing data (especially images) retrieved from remote sites and/or processed by the VIX. If the image is requested again, it can be pulled from the local cache of the VIX without having to retrieve it from the remote site or reprocess it.

> At multidivisional sites where there can be more than one VIX, the VIX that handles the data is the only VIX that will cache the data (if applicable).

> Note: Metadata and images cached by the VIX are considered transitory copies and are not a part of the patient record. The site from which the data originates is the official custodian of the data, not the VIX.

### Cache Retention Periods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX purges data from its cache when the retention period for the data is reached. The images are considered static data, allowing relatively long cache retention while retaining data consistency. Metadata, which is less static, is retained for shorter periods.

> The following table lists retention periods based on the source and type of the data.

| Data type     | Retained for | Scan to delete old items is run |
|-------------------|------------------|-------------------------------------|
| VA and DoD images | 30 days          | Once per day at 3AM                 |
| VA metadata       | 1 hour           | Once per minute                     |
| DoD metadata      | 1 day            | Once per hour                       |

### Cache Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The cache is located in the /VixCache folder on a local drive (when the VIX is installed on a dedicated standalone server).

> Note: Never manually change the contents of the Vix Cache folder and subfolders using Windows Explorer while the VIX is running.

> Note: If you need to change the location of the VIX cache, you will need to re-run the VIX installation wizard to update your VIX’s configuration information. For details, see the [*<u>VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

## Using the VIX Cache Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A VIX ache Manager function allows users to browse the VIX cache, identify corrupt data, and delete data as required. The cache browser is accessed using Internet Explorer 7 or later and Firefox 3 or later.

> To access the VIX Cache Manager, go to http://\<FQDN\>:8080/CacheWeb (where

> \<FQDN\> is the fully qualified domain name of the individual host.

> Note: The URL to the VIX Cache Manager is case sensitive.

### Cache Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The data in the cache is arranged in a hierarchy with one or more of the following levels;

- data source (VA or DoD) and type (artifact, metadata, or image)
- repository (VA site or DoD facility)
- patient identifier (ICN for VA patients)
- study (group) identifier
- series and instance identifiers.

> The source and type of the data are the most important factor in determining where an item is cached. When the VIX Cache Manager is opened in a browser the following screen displays:

![](vix-admin-guide/019.png)

> The items immediately under the cache name are called “regions” of the cache. Regions divide the items in the cache by the source of the item (VA versus anywhere else) and the type of the item (image versus anything else). A region defines the conditions under which a cache item is deleted from the cache.

> Historically, it has been the case that anything that is not from the VA is from the DoD and anything that is not an image is metadata. Thus, a radiology image from the DoD will be found in the “dod-image-region” while the study text data from a VA site will be found in the “va-metadata-region”.

#### Technical Specifics

> The cache does not understand anything about sites, patients, or studies but operates on the concept of regions, groups, and instances. Regions are collections of similar items that have the same lifespan in the cache (i.e., 30 days since last use). Groups are collections of groups and instances. Instances are the cache items proper. Groups are

> what is called a recursive data structure, a group can contain other groups, which in turn can contain still more groups. The cache limits that hierarchy to specific levels grouped by well-known business concepts (site, patient, etc.). Groups are also the basis that the cache deletes items. If no item in a group has been accessed within the region’s lifespan then the entire group is deleted from the cache. If you think of the images in a study, then this makes more sense, if a study has not been accessed for 30 days, then the entire study is deleted from the cache. If none of the studies for a patient have been accessed within 30 days, then the whole patient is deleted from the cache.

> Click the “va-image-region” region link and a list of cache groups will be displayed. You should see something like the next illustration, except that the cache contents will be different.

![](vix-admin-guide/020.png)

> The VIX Cache Manager displays the name of the region in the breadcrumb at the top of the page, and a list of the image repositories in this region. To drill down into an image repository, click on the image repository number. To delete an entire image repository, click on the Delete button to the left.

> You can drill down through the VIX cache using the links in the VIX Cache Manager. The levels of the cache–region, repository, patient, study, and image—appear as

> hyperlinks in the breadcrumb at the top of the page. To delete an item in the cache at any level, click on the Delete button to the left.

![](vix-admin-guide/021.png)

#### The DoD Regions

> DoD regions are organized by the community operation order identification (OID) number followed by the repository, the patient and then group identifiers of various sorts. The community OID is an identifier that an enterprise uses to identify itself on the Nationwide Health Information Network (NwHIN). For our purposes, the OIDs that you need are shown in the table below:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>OID</strong></th>
<th><blockquote>
<p><strong>Enterprise</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>2.16.840.1.113883.3.42.10012.100001.207</strong></td>
<td><blockquote>
<p><strong>DoD Radiology</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>2.16.840.1.113883.3.42.10012.100001.206</strong></td>
<td><blockquote>
<p><strong>DoD Documents</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><strong>2.16.840.1.113883.3.166</strong></p>
<p><strong>2.16.840.1.113883.6.233</strong></p></td>
<td><blockquote>
<p><strong>VA Documents</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>1.3.6.1.4.1.3768</strong></td>
<td><blockquote>
<p><strong>VA Radiology</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Below the enterprise OID is a repository (a site in VA parlance). At this time, DoD documents always come from the Central HAIMS server and are identified as “central”. Likewise, DoD radiology always comes from the DAS interface, identified as “200”.

> The DoD metadata region is only used for radiology study text data.

#### Cache Item Information

> Clicking a cache item link will retrieve information about the item, such as the last time it was accessed and the size. This information may be useful in locating a specific item.

> The size of a cache instance is the size of the file on disk (including its descendants); the size of a cache group is the sum of all of the groups and instances contained within it. The checksum, available only for cache instances, is the result of a mathematical calculation applied to the entire content of the instance. The checksum is used within the VIX to detect data errors. For an instance with the same identifiers, this value should always be the same on all VIX and on CVIX.

> ![](vix-admin-guide/022.png)

#### Cache Delete

> Usually the cache is self-managing, determining the cached items that have not been used recently and deleting them. On rare occasions, a corrupt item may be cached. In this case, that corrupt data will be repeatedly served on request. Repeated requests are treated as user access and extend the time that the data stays in the cache. This cache item must be deleted from the cache manually.

> To delete a cache item, collect as much identification information as you can. At a minimum, this must include whether the source is the VA or the DoD and, if it is a VA item, whether the image or a study (metadata) is causing problems and the site the data originated from. In addition the patient identifier must be known.

> Once that information is collected, open the VIX Cache Manager and navigate through the hierarchy to either the corrupt item or to one of its parent groups (patient ID or study) if the item itself cannot be identified. Click on the Delete button to the left of the item and then confirm that you want the item deleted. The cache does not immediately delete

> the item since it has to synchronize operations from all clients. It may take a few seconds or up to a minute before the item is actually deleted. Usually though, it will respond immediately that the item is deleted and the item will disappear from the VIX Cache Manager.

> Finally, it is worth reinforcing that when an item is deleted from the cache it is not deleted from the original source of the data. If the VIX is asked for that item again it will simply notice that it is not in its cache and will retrieve it from the original data source and re-cache it. The effect to the user is a slight delay, nothing more.

> The minimal deleterious effect of deleting a cache item may lead someone to delete “good” cache items to get all of the “bad” ones. This is not an issue, since the VIX will simply re-cache the items when they are requested again.

## Image Sharing-related Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In addition to the VIX transaction log, VIX-supported image sharing is logged on VistA and temporarily logged by Clinical Display.

### Logging on VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IMAGE ACCESS LOG file (#2006.95) uses specific values in the ACCESS TYPE field (#1) and the ADDITIONAL DATA field (#100) to indicate when a VIX was involved in an image access.

#### VIX-related Access Type Values

> If the ACCESS TYPE field (#1) in an IMAGE ACCESS LOG file (#2006.95) entry contains one of the values listed below, the VIX accessed the image on behalf of a remote requester.

> Note that only the values unique to the VIX are described. For information about other entries in the IMAGE ACCESS LOG file (#2006.95), refer to the file’s data dictionary.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Access Type Value</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RVVAVA</td>
<td><p>A locally stored image that a remote VA Clinical Display or AWIV user accesses via a VIX.</p>
<p><strong>Note:</strong> This value can be present even if there is no local VIX (i.e., the image was accessed via a remote VIX).</p></td>
</tr>
<tr class="even">
<td>VR-RVVAVA</td>
<td><p>A locally stored image that a remote VA VistARad user accesses via a VIX.</p>
<p><strong>Note:</strong> This value can be present even if there is no local VIX (i.e., the image was accessed via a remote VIX).</p>
<p><strong>Note:</strong> A similar value, VR-RVVAVA/REM, indicates a remote VistARad access <em>without</em> a VIX.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Access Type Value</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RVVADOD</td>
<td><p>A locally stored image that a DoD clinician requests via the VIX (or CVIX if a local VIX is not present).</p>
<p><strong>Note:</strong> In this scenario, the VIX (or CVIX) reports all <em>requests</em>. Because the requested image is ultimately passed to DoD systems, the VIX (or CVIX) cannot report if the requested image was actually accessed or not.</p></td>
</tr>
<tr class="even">
<td>RVDODVA</td>
<td><p>A remotely stored DoD image that a local VA Clinical Display user accesses via the VIX.</p>
<p><strong>Note:</strong> The VIX logs this activity at the requesting site rather than at the site where the image is stored because the DoD storage site is unknown to the VIX.</p>
<p><strong>Note:</strong> Access to remotely stored DoD images is not logged in #2006.95 if the access is made using VistARad. However, these accesses are recorded in the VIX transaction log.</p></td>
</tr>
</tbody>
</table>

#### VIX-Related Additional Data Values

> The VIX will also populate the Additional Data field (#100) based on data provided by the requesting application.

> Because the VIX adds a lot of information to this single free-text field, the VIX uses “\|” characters to organize the Additional Data field into four “parts”. Note that these parts exist for organizational purposes only, and are not considered discreet pieces in the FileMan sense.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"><strong>If Access Type is...</strong></th>
<th colspan="4"><blockquote>
<p><strong>Then Additional Data contains...</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><strong>Part 1</strong></p>
</blockquote></th>
<th><strong>Part 2</strong></th>
<th><strong>Part 3</strong></th>
<th><strong>Part 4</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RVVAVA</td>
<td><blockquote>
<p>empty</p>
</blockquote></td>
<td><blockquote>
<p>VIX transaction ID</p>
</blockquote></td>
<td>Requesting VA site ID</td>
<td>empty</td>
</tr>
<tr class="even">
<td>RVVADOD</td>
<td><blockquote>
<p>empty</p>
</blockquote></td>
<td><blockquote>
<p>VIX transaction ID</p>
</blockquote></td>
<td>Requesting DoD site ID</td>
<td>Username of the requesting DoD clinician</td>
</tr>
<tr class="odd">
<td>RVDODVA</td>
<td><blockquote>
<p>DoD image ID</p>
</blockquote></td>
<td><blockquote>
<p>VIX transaction ID</p>
</blockquote></td>
<td>local VA site ID</td>
<td>empty</td>
</tr>
<tr class="even">
<td>VR-RVVAVA</td>
<td colspan="4"><blockquote>
<p><em>VIX transaction ID</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Example – RVVAVA Access Type

> ^MAG(2006.95,16401,0)=16401^<u>RVVAVA</u>^126^51^DOD^ROU^3090216.081305^1023^1^4892

> ^688

> ^MAG(2006.95,16401,100)=\|<u>246a2052-70b1-4ed7-af55-bea35b1</u>\|<u>688</u>\|

1.  

#### Example – RVVADOD Access Type

> ^MAG(2006.95,610535,0)=610535^<u>RVVADOD</u>^1376^8820^<u>DOD</u>^XXX^3100302.094747^ 1023^1^6557^660

> ^MAG(2006.95,610535,100)=\|<u>5aafabc4-2361-4a34-b843-5aad4163620c</u> <u>XX.XXX.MIL/HP0000-PZ01</u>\|<u>DoDUsername</u>

#### Example – RVDODVA Access Type

> ^MAG(2006.95,610566,0)=610566^<u>RVDODVA</u>^126^^Wrks^ROU^3100302.134155^1023^1^6561^ 660

> ^MAG(2006.95,610566,100)=<u>urn:bhieimage:rp02_0108_rp01-e403e3c3-bdc2-4494-b816-</u> <u>3757b435ec0b</u>\|<u>{EEEF890A-4C66-4F8C-8121-2CD1FE8F9B80}</u>\|<u>660</u>\|

#### Example – VR-RVVAVA Access Type

> ^MAG(2006.95,720029,0)=720029^<u>VR-RVVAVA</u>^126^506^VRAD:3.0.90.6^ROU^ 3100405.161144^1011^1^8478^660

> ^MAG(2006.95,720029,100)={71247e80-f250-42c3-b8ea-9156b6d03a28}

### Additional Client Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Clinical Display Message History Log

> The Message History log on a Clinical Display workstation can also be used to check/troubleshoot VIX activities.

- To access this log, click ![](vix-admin-guide/023.png) located in the lower left corner of the main Clinical Display window.
- The “transid” in the Message History log can be traced to specific transactions in the VIX transaction log. See [*VIX Transaction Log Fields*](#vix-transaction-log-fields) for details.
- Certain details (such as IENs and image paths) are shown only if the active user holds the MAG SYSTEM key.
- The Message History Log is session-specific and is cleared when Clinical Display is exited.

#### VistARad Logging of VIX Operations

> Refer to VistARad documentation for details.

## Image Sharing and VIX Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a local VIX retrieves metadata and images from remote sites, the system load at the remote site and WAN network traffic will impact the time needed to complete the

> retrieval. If a request for data cannot be completed in a timely manner, the local VIX will cancel its request. This prevents excessive delays in client applications (Clinical Display and VistARad) that use the VIX.

> The following table summarizes VIX connection timeout parameters based on the type of remote system and data involved.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Remote System Type</strong></th>
<th><strong>Local VIX Timeout if No Response</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA data via a remote VIX</td>
<td><p>For metadata, 600 seconds for data transfer to begin (this is to handle very large datasets; usually data transfer begins in a few seconds).</p>
<p>For images, wait up to 30 seconds for initial connection and up to 120 seconds for data transfer to begin.</p></td>
</tr>
<tr class="even">
<td>VA data from a remote non-VIX VA site</td>
<td><p>For metadata, no timeout.</p>
<p>For images, N/A because the local VIX only starts the operation if it can connect to the remote site and can verify that the remote image is present.</p></td>
</tr>
<tr class="odd">
<td>DoD data via the CVIX</td>
<td><p>For metadata, the CVIX will wait up to 45 seconds to retrieve DoD metadata before sending a timeout message to the local VIX.</p>
<p>For images, the CVIX will wait up to 30 seconds for the initial connection with the DoD image source, and up to 120 seconds for the image transfer to begin.</p>
<p>If the CVIX is able to retrieve data from some DoD sources but not all of them, the CVIX will pass a “partial” response message to the local VIX.</p>
<p><strong>Note:</strong> For some patients, especially polytrauma cases, the source of DoD DICOM data needs more than 45 seconds to process the request. If this happens at the CVIX, the local VIX will send a “Try Again” message to the local requesting application (such as Clinical Display or VistARad) In most cases, the requested data will be available within a minute or so and a subsequent request will be successful.</p>
<p><strong>Note:</strong> Because the CVIX can retrieve DoD data from multiple sources, there may be cases where one DoD data source responds but another does not. If this happens at the CVIX, the local VIX will send a “partial” message to the local requesting application.</p></td>
</tr>
</tbody>
</table>

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following information may help diagnose potential VIX-related image sharing problems.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Symptom</strong></th>
<th><strong>Check</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VIX transaction log not accessible</td>
<td><p>On the server where the VIX is installed, make sure that the VIX is running and that ports 8080 and 8443 are not blocked by antivirus firewalls or by an ACL (access control list) update.</p>
<p>Also, make sure the VIX service is running as described in</p>
<p><a href="#monitoringmaintaining-the-vix"><em>Monitoring/Maintaining the</em> VIX.</a></p></td>
</tr>
<tr class="even">
<td>Clinical Display cannot connect to any remote sites</td>
<td><p>Make sure the local VIX is running and that required ports are open as described above (if you can access the VIX transaction log, the VIX is running).</p>
<p>Determine if the issue is specific to one Clinical Display workstation or if it affects all workstations.</p>
<p>On an affected Clinical Display workstation, disconnect from and reconnect to all remote sites. If that does not work, restart the Clinical Display software.</p>
<p>(If the VIX is the source of the issue, restarting Clinical Display will make Clinical Display use pre-VIX remote image views, which is not dependent on a VIX. However, pre-VIX remote image views cannot be used to access DoD images, and in some cases they will have poorer performance than VIX- supported remote image views.)</p></td>
</tr>
<tr class="odd">
<td>VistARad cannot connect to any remote sites</td>
<td><p>Make sure the local VIX is running and that required ports are open as described above (if you can access the VIX transaction log, the VIX is running).</p>
<p>Determine if the issue is specific to one VistARad workstation or if it affects all workstations.</p>
<p>On an affected VistARad workstation, go to <strong>View | Settings | VIX Configuration</strong> and verify that the settings on the tab are correct. See the VistARad documentation for details.</p></td>
</tr>
<tr class="even">
<td>Retrieval times increase significantly relative to previous retrievals</td>
<td><p>If the problem is specific to one remote site, there may be an issue with the remote site’s VIX. Image retrievals will continue at reduced performance until the remote VIX is up and running.</p>
<p>If the problem is specific to Clinical Display, check to see if Clinical Display is using pre-VIX remote image views. If this is the case, restart Clinical Display to verify that it will use the VIX for subsequent image retrievals.</p>
<p>If the problem is specific to VistARad, refer to VistARad documentation for details.</p>
<p>In rare cases, the local VIX cache may become full. (If the VIX cache is full, the VIX will continue to retrieve images but will bypass its cache.) If the VIX cache is full, contact customer support.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Symptom</strong></th>
<th><strong>Check</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>If the problem affects all remote sites and the potential issues above have been eliminated, WAN congestion may be the issue.</td>
</tr>
<tr class="even">
<td>A specific VA remote site is disconnected (but other remote sites are available)</td>
<td><p>Determine if the problem affects multiple patients or if it occurs only for a specific patient.</p>
<p>If the problem is specific to a single patient, the most likely cause is a problem with the metadata being retrieved from the remote site.</p>
<p>If the problem affects all patients, the issue is most likely connectivity with the remote site.</p>
<p>In both cases, contact the remote site (if possible) or customer support.</p></td>
</tr>
<tr class="odd">
<td>Some, but not all remote images from VA sites are inaccessible</td>
<td><p>Try to determine if the problem is specific to certain sites, patients, or image types; then contact customer support.</p>
<p>If the problem is specific to remote radiology images, try to view those images using both VistARad and the Clinical Display Radiology Viewer; then report the results to customer support.</p></td>
</tr>
<tr class="even">
<td>ID mismatch icon or Questionable Integrity warning for remote images</td>
<td>If the metadata of a remote image does not correlate with local identifiers, the VIX will still retrieve the image and store it in the VIX cache, but Clinical Display or VistARad may block the display of an image. If possible, contact the remote site’s Imaging Coordinator, or contact customer support.</td>
</tr>
<tr class="odd">
<td>DoD remote site button in Clinical Display shows “Try Again” label</td>
<td><p>This can occur if the source of DoD DICOM images cannot respond to a metadata request via the CVIX within 30 seconds. This is especially likely to happen if the patient in question is a polytrauma patient with a large number of studies.</p>
<p>In most cases, the originating system can finish processing the request in a minute or so. Clicking the DoD button again will renew the request and the data will be retrieved by the VIX if it is available.</p></td>
</tr>
<tr class="even">
<td>DoD remote site button in Clinical Display shows “Partial” label</td>
<td><p>This can occur if one or more DoD data sources cannot respond to a request for metadata in a timely manner. If this occurs, the CVIX will send all available metadata back to local VIX, and will also use the “partial” flag to indicate that the data is potentially incomplete.</p>
<p>If this issue persists, especially for multiple patients, contact customer support.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Symptom</strong></th>
<th><strong>Check</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DoD remote site is unavailable</p>
<p>(no “Try Again” label in button)</p></td>
<td><p>If the DoD is available on VistARad workstations but not on Clinical Display workstations, verify that the Clinical Display workstations are using the VIX to retrieve images. To do this, check the Image ID of the remote image in the Clinical Display Image List. If the Image ID is prefixed with the string “urn”, the VIX is being used. If a standard ID is shown, the VIX is not being used, and you should restart the workstations in question and then try to reconnect to the DoD.</p>
<p>If this occurs for Patch 93 Clinical Display only, verify that the MAG VIEW DOD IMAGES security key is assigned to the user. (This key is not checked for Patch 94 or later.)</p>
<p>If the connection remains unavailable for more than an hour, contact customer support.</p></td>
</tr>
<tr class="even">
<td>DoD connection is available but images are inaccessible</td>
<td><p>If an “Image not Available” icon is shown in Clinical Display, there was a delay in processing the images. Wait 30 seconds and try to display the image again.</p>
<p>If an “Image not Found” icon is shown in Clinical Display, the issue cannot be resolved on the VA side. If the image is deemed necessary for medical care, contact customer support.</p></td>
</tr>
<tr class="odd">
<td>One or more images appear to be corrupted</td>
<td><p>Display the image on a different Clinical Display or VistARad workstation to verify that the problem is with the actual image (rather than a transitory display error).</p>
<p>If the problem persists, contact customer support immediately.</p></td>
</tr>
</tbody>
</table>

# ROI VIX Operation, Configuration and Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter explains how the VIX processes ROI (Release of Information) requests, describes the ROI-related statistics and configuration parameters, and explains how to configure the other ROI-related parameters of the VIX.

## How the VIX Processes ROI Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are two ways in which the VIX can process ROI disclosure requests:

- Immediately when it gets the disclosure request and/or
- Periodically, in the background

> How the VIX processes ROI disclosures is determined by two parameters its configuration. By default both parameters are enabled and the VIX uses both ways to process ROI disclosure requests at the same time.

> Users with the MAG VIX ADMIN security key can modify these parameters.

> Note: At least one of the two ROI processing parameters must be enabled for the VIX to process ROI requests. If both parameters are disabled, the VIX will not process ROI requests. It will display a message alerting VIX administrators to the fact that ROI requests cannot be processed until at least one of the parameters is enabled.

> Note: Reinstalling the VIX service resets these parameters to their default enabled values. If these values have been changed manually the change will need to be reapplied after the VIX service is installed.

### Processing ROI Disclosure Requests Immediately

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the parameter Process Disclosure Requests Immediately is enabled, the VIX processes ROI disclosure requests when it receives them. This option does not require ROI processing credentials. The VIX uses the credentials of the user who submits the ROI request to process the disclosure. By default this option is enabled. However, if the VIX gets too busy, users with the MAG VIX ADMIN security key can disable this option and configure the VIX to only process ROI disclosures periodically.

> Note: If the VIX is interrupted while it is processing an ROI request because of a network disconnection or a VIX restart, the ROI disclosure will be completed only if periodic processing is enabled. If periodic processing is not enabled, the request will not be completed.

### Periodic Processing of ROI Disclosure Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When periodic processing is enabled, the VIX processes ROI disclosure requests periodically, in the background. Enabling periodic processing is useful because it allows an ROI disclosure to be completed even if the VIX operation is interrupted because the VIX was restarted or because it ran into an issue.

> Periodic processing requires a valid VistA account with ROI processing credentials. If the credentials provided to the VIX are invalid, periodic processing will not work.

> For information about setting ROI Processing credentials, see *[ROI Periodic Processing](#roi-periodic-processing-credentials)* [*Credentials*.](#roi-periodic-processing-credentials)

### Purging Completed Disclosures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the parameter Completed Disclosures Purge Processing is enabled, the VIX purges old ROI disclosures after the number of days specified in the parameter Completed Disclosures Purge Days.

> The purge removes the metadata associated with an ROI disclosure from the VistA database. The actual ROI disclosure result is removed when the VIX cache purges data, which is typically after 30 days.

> Completed disclosures purge processing requires a valid VistA account with ROI periodic processing credentials. If the credentials provided to the VIX are invalid, completed disclosures purge processing will not work.

### Processing Disclosure Wait Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The parameter Processing Disclosure Wait Time indicates the number of minutes the VIX waits for an ROI disclosure to be in a processing state before resetting the disclosure request. ROI disclosures are processed in several either active or waiting states. If a request stays in an active state beyond the number of minutes specified in this parameter, it is reset to a waiting state to be processed. By default the wait time to process a work item is 120 minutes. The value should be set to a period that is long enough for a work item to complete but not too long to orphan the ROI disclosure request.

> For information about setting ROI Processing credentials, see *[ROI Periodic Processing](#roi-periodic-processing-credentials) [Credentials](#roi-periodic-processing-credentials)*.

### ROI Periodic Processing Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ROI periodic processing credentials are the credentials the VIX uses to do periodic processing for ROI. These credentials must be valid VistA credentials with the MAG DICOM and OR CPRS GUI CHART secondary menu options. The credentials can be the credentials of the same service account that the DICOM Gateway and the HDIG use.

> For more information about setting the access and verify codes of the account, see the

> [*<u>VistA Imaging VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

> Users with the MAG VIX ADMIN security key can reset the access and verify code of the account through the ROI Processing Status page. For more information about the procedure, see [*Modifying the ROI Processing Parameters of the VIX*.](#modifying-the-roi-processing-parameters-of-the-vix)

### Alerts About Problems in the ROI Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the VIX encounters a problem with the ROI processing configuration, for example, if both periodic processing and Process Disclosure Requests Immediately are disabled, it

> displays an alert at the top of the ROI Processing Status page and the Release of Information (ROI) Configuration page. When there is a message, this means that there is a problem with the current configuration and you should take actions to resolve the issue or issues. For information about the procedure for modifying the ROI processing parameters of the VIX, see [*Modifying the ROI Processing Parameters of the VIX*](#modifying-the-roi-processing-parameters-of-the-vix).

## Getting Information About ROI Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can see the status of an ROI request and get information about ROI statistics on the ROI Processing Status page.

#### To display the ROI Processing Status page:

> In your browser, open the URL for the ROI Processing Status page:

> http://\<*VIXHostName*\>:8080/ROIWebApp

> where \<*VIXHostName*\> is the name of the fully qualified domain name (FQDN) of the server on which the VIX is installed

> The following image shows the ROI Processing Status page.

> ![](vix-admin-guide/024.png)

### Information the ROI Processing Status Page Provides

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ROI Processing Status page provides statistics about the ROI processing jobs since the last VIX restart. The counters for each field are reset every time the VIX is restarted.

> The following table explains the information that the VIX provides for ROI processing.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Group</p>
</blockquote></th>
<th><blockquote>
<p>Field</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ROI Statistics</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Disclosure Requests</p>
</blockquote></td>
<td><blockquote>
<p>The number of requests made to the VIX for ROI disclosures.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Disclosures Completed Successfully</p>
</blockquote></td>
<td><blockquote>
<p>The number of successfully completed ROI disclosures.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Studies Sent to Export Queue</p>
</blockquote></td>
<td><blockquote>
<p>The number of studies sent to the export queue to be processed. A disclosure may contain several studies that are sent to the export queue (among others that may be processed by the VIX).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Disclosures Failed Processing</p>
</blockquote></td>
<td><blockquote>
<p>The number of ROI disclosures that did not complete successfully.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Disclosures Cancelled</p>
</blockquote></td>
<td><blockquote>
<p>The number of ROI disclosures that were cancelled before completion.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Periodic Processing</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>When periodic processing is enabled, the VIX processes ROI disclosures in the periodically in the background.</p>
<p>Periodic processing requires an account with ROI processing credentials, which is configured when the VIX is installed.</p>
<p>For more information about periodic processing, see <a href="#periodic-processing-of-roi-disclosure-requests">Periodic Processing of ROI Disclosure Requests.</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Configuration Enabled</p>
</blockquote></td>
<td><blockquote>
<p>When this parameter is set to true, periodic processing is enabled and the VIX processes ROI requests periodically in the background.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Current Status</p>
</blockquote></td>
<td><blockquote>
<p>Indicates the current status of periodic processing. The values are:</p>
<p>Disabled – Indicates that periodic processing is disabled.</p>
<p>Enabled – Indicates that periodic processing is enabled and that there is an account with valid ROI processing credentials.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Completed Disclosures Purge Processing</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>When completed disclosures purge processing is enabled, the VIX purges old ROI disclosures after the number of days specified in its configuration. Completed disclosures purge processing requires an account with ROI processing credentials. For more information, see <a href="#purging-completed-disclosures">Purging Completed Disclosures.</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Configuration Enabled</p>
</blockquote></td>
<td><blockquote>
<p>Indicates if completed disclosures purge processing is enabled. When this parameter is set to true, completed disclosures purge processing is enabled.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Group</p>
</blockquote></th>
<th><blockquote>
<p>Field</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Current Status</p>
</blockquote></td>
<td><blockquote>
<p>Indicates the current status of completed disclosures purge processing. The values are:</p>
<p>Disabled – Indicates that completed disclosures purge processing is disabled.</p>
<p>Enabled – Indicates that completed disclosures purge processing is enabled and that there is an account with valid ROI processing credentials.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Other ROI Options</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Process Disclosure Requests Immediately</p>
</blockquote></td>
<td><blockquote>
<p>When enabled, the VIX processes ROI disclosures immediately when it gets the request. This option does not require ROI processing credentials. The VIX uses the credentials of the user who submits the ROI request to process the disclosure. For more information, see <a href="#processing-roi-disclosure-requests-immediately"><em>Processing ROI Disclosure Requests Immediately</em>.</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>In Process Work Item Wait Time</p>
</blockquote></td>
<td><blockquote>
<p>Indicates the number of minutes the VIX waits for an ROI disclosure to be in a processing state before resetting the disclosure request. ROI disclosures are processed in several either active or waiting states.</p>
<p>For more information, see <em><a href="#processing-disclosure-wait-time">Processing Disclosure Wait</a> <a href="#processing-disclosure-wait-time">Time.</a></em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Configure ROI Options</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>To change any of the VIX ROI configuration settings click on the Configure ROI Options link. Accessing this configuration page requires VistA credentials for a user with the MAG VIX ADMIN security key.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Invalid Credentials Email Notification</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>To change any of these settings click on the Configure ROI Options link. This configuration page requires VistA credentials for a user with the MAG VIX ADMIN security key.</p>
<p>When the VIX is configured to do periodic processing for ROI or completed disclosures purge processing, it authenticates the ROI processing credentials. If the account credentials are invalid or expired, the VIX sends an email notification of the invalid credentials.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Invalid Credentials Email Notification Addresses</p>
</blockquote></td>
<td><blockquote>
<p>The email address or addresses to which the VIX sends an email notification about invalid ROI processing credentials. The value can include multiple email addresses (separated by a comma) and/or an email group. The email will come from the <a href="mailto:vix@va.gov">vix@va.gov</a> email account. The values are specified when the VIX is installed. Users with the MAG VIX ADMIN key can modify these values.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Group</p>
</blockquote></th>
<th><blockquote>
<p>Field</p>
</blockquote></th>
<th><blockquote>
<p>Description</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Update the Invalid Credentials Email Notification Addresses</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>To change the email addresses to send notifications to click on the Update the Invalid Credentials Email Notification Addresses link. Accessing this page requires VistA credentials for a user with the MAG VIX ADMIN security key.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Alert Messages</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>If there is a problem with the VIX ROI processing configuration, the VIX displays a message at the top of the page indicating that you need to change the configuration to resolve the issue. For more information about the alerts, see <a href="#alerts-about-problems-in-the-roi-configuration"><em>Alerts</em>.</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Modifying the ROI Processing Parameters of the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users with the MAG VIX ADMIN security key can change the ROI configuration parameters of the VIX and re-set the access and verify codes of the service account with the ROI periodic processing credentials.

#### To change the ROI processing parameters of the VIX:

1.  In your browser, open the URL for the ROI Statistics page:

> http://\<*VIXHostName*\>:8080/ROIWebApp

> where \<*VIXHostName*\> is the name of the fully qualified domain name (FQDN) of the computer on which the VIX is installed

2.  In the ROI Processing Status page, click the link Configure ROI Options.
3.  In the dialog box that displays, enter the access and verify code of the user with the MAG VIX ADMIN security key. Then, click OK.

![](vix-admin-guide/025.png)

4.  ![](vix-admin-guide/026.png)In the Configure Release of Information (ROI) page, modify the configuration parameters as desired. For information about the parameters, see [*Information theROI Processing Status Page Provides*.](#information-the-roi-processing-status-page-provides)
5.  Click the Save Configuration button to save the changes. The page will be refreshed with a status message indicating if the changes were saved or if there was an error.
6.  To return to the ROI Processing Status page, click on the ROI Status link on the left side of the page.

## Changing User List for Get Invalid ROI Credentials Email Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the VIX encounters a problem with the service account credentials (invalid credentials or expired verify code), it sends an email notification to the address or addresses specified in its configuration. The parameter Invalid Credentials Email Notification Addresses specifies the email address or addresses to which the VIX sends an email notification about invalid ROI processing credentials. The value can include multiple email addresses (separated by a comma) and/or an email group.

> The email notification for invalid credentials will come from the <vix@va.gov> email account. The values of the Invalid Credentials Email Notification Addresses are specified when the VIX is installed. Users with the MAG VIX ADMIN key can modify these values.

> To change the list of email addresses to which the VIX sends notifications about invalid ROI processing credentials:

1.  In your browser, open the URL for the ROI Statistics page:

> http://\<*VIXHostName*\>:8080/ROIWebApp

> where \<*VIXHostName*\> is the name of the fully qualified domain name (FQDN) of the computer on which the VIX is installed

2.  In the ROI Processing Status page, click the link Update the Invalid Credentials Email Notification Addresses.
3.  ![](vix-admin-guide/027.png)In the dialog box that displays, enter the access and verify code of the user with the MAG VIX ADMIN security key. Then, click OK.
4.  In the Configure Invalid Credentials Email Notification Addresses page, modify the list of addresses as desired. The list can contain multiple addresses separated by commas and/or an email group.

> ![](vix-admin-guide/028.png)

5.  Click the Save Configuration button to save the changes. The page will be refreshed with a status message indicating if the changes were saved or if there was an error.
6.  To return to the ROI Processing Status page, click on the ROI Status link on the left side of the page.

# VIX Reference/Software Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VIX Java Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections summarize the primary Java components of the VIX.

### VIX Servlet Container

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX uses an Apache Tomcat-based servlet container to provide the environment used to execute the Java code on the VIX. This servlet container is installed automatically as part of the VIX installation process.

### VIX Security Realms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX implements security realms to verify that only properly authenticated applications (Clinical Display, VistARad, and other VIXes) can use the interfaces provided by the VIX Web applications. Authentication is handled silently by the application and the VIX, and does not require an explicit login by clinicians requesting images.

### VIX Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX uses a dedicated interface for each outside application that requests and receives data from the VIX.

> VIX interfaces are used for both metadata and image retrieval. In general, each VIX interface implements a Web service that handles metadata requests and an image servlet that handles image requests. The following table summarizes each VIX interface.

| Interface Name         | Description                                                               |
|----------------------------|-------------------------------------------------------------------------------|
| VistARad interface         | Handles metadata and image requests from local VistARad workstations.         |
| Clinical Display interface | Handles metadata and image requests from local Clinical Display workstations. |
| Federation interface       | Handles metadata and image requests from other remote VIXes or the CVIX.      |

| Interface Name                | Description                                                                                                                                                                                  |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MIX,DX Interface                  | Handles DICOM metadata and image requests from DoD providers.                                                                                                                                    |
| User services interface           | Handles user-related functionality such as authentication and security key retrieval.                                                                                                            |
| Patient services interface        | Handles patient-related functionality, including patient search and sensitive patient access logging.                                                                                            |
| Storage services interface        | Handles requests related to read and write locations and metadata.                                                                                                                               |
| DICOM Importer services interface | Handles application-specific requests for the importer, including study and order metadata, performing CRUD operations on work items, dealing with Importer reports, and other related features. |

> When an interface receives a request, it issues the appropriate command to the VIX core for proper disposition. When the VIX core ultimately provides a response (the requested data), the same interface responds to the requesting application.

### VIX Core

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX core provides the central switching intelligence for the VIX. It performs the following:

- Examines commands received from all the VIX interfaces.
- Determines which VIX data source is the best one to retrieve the data requested and packages the request appropriately before passing the request to the data source.
- Implements and manages the VIX cache.

### VIX Data Sources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX has a dedicated data source for each outside entity from which it retrieves data. Data sources receive requests from and return responses to the VIX core. The following table summarizes each VIX data source. These data sources are identified in the Data Source Protocol field in the VIX transaction log.

| Data Source Name | Description                                                                      |
|----------------------|--------------------------------------------------------------------------------------|
| vistaimaging         | Retrieves data from a VistA System using RPCs                                        |
| mix,dx               | Retrieves DICOM data from the DoD via the DAS framework’s mix,dx interface.          |
| vftp                 | Retrieves data from other VIXes (or the CVIX/RVIX) using their Federation interfaces |

### Java Installation Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On the server where the VIX is installed, VIX-related files are stored in the locations described below.

> For installation procedures, see the [*<u>VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

#### VIX folders on the System Drive

> The following VIX-related folders are on the system drive (usually C:\\. Note that because the VIX is a collection of services hosted in a servlet container, most VIX related-files cannot be stored under \Program Files\VistA.

#### \DCF_Runtime

> Laurel Bridge DICOM Connectivity Framework (DCF) toolkit files

#### \Program Files\Apache Software Foundation\Tomcat 8.1.45

> Primary application area for the VIX servlet engine and VIX program files. Includes:

> \bin – servlet engine executables and Aware JPEG2000 toolkit files

> \conf – servlet engine configuration files

> \lib – shared servlet engine files, VIX core and data source files, and Aware JPEG2000 toolkit files

> \logs – Java and debugging logs

> \temp – temporary files

> \webapps – VIX Web applications and associated parameter files

> \work – servlet engine system files

#### \Program Files\Java\jre1.8.0_121

> The runtime environment files and resources for the VIX servlet engine and for VIX Java components.

#### \Program Files\Vista\Imaging\VixInstaller

> VIX installation files and resources.

#### \VixCertStore

> Stores VIX security certificates. For details about security certificates, see the *[VIX](#vix-security-certificate)* [*Security Certificate*](#vix-security-certificate) section.

#### VIX Folders on the System Drive or a Shared Drive

> When the VIX is installed on a standalone server, the following folders can be on either the system drive or on a shared drive at the site’s discretion.

#### \VixCache

> This is the primary storage area for images and metadata that the VIX caches. For details about the VIX cache, see [*Caching of Metadata and Images*.](#caching-of-metadata-and-images)

#### \VixConfig

> Configuration files used by the VIX Java components and the VIX transaction log.

> Note: Files in the VixConfig folder are generated as part of the VIX installation process and are regenerated when the VIX is updated.

### Java Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following Java logs reside in \Program Files\Apache Software Foundation\Tomcat 6.0\Logs. For active logs, a new instance is generated each day and the older instances are retained with the date appended to their filenames.

> catalina.log: Tomcat (VIX servlet container) output. host-manager.log: Java host manager application output. ImagingCache.log: VIX cache output.

> ImagingExchangeWebApp.log: VIX interface/web application output.

> jakarta_service.log: Windows jakarta service output. localhost.log: generated but not populated. manager.log: generated but not populated. stderr.log: Tomcat service errors.

> VistaRealm.log: VIX security realm output.

## VistA/M Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections describe how a VIX interacts with local and remote VistA systems.

### RPCs Used by the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX uses numerous remote procedure calls (RPCs). Most of these RPCs are part of the VistA Imaging (MAG) package and are listed below. RPCs from other packages are listed in the next section.

#### MAG RPCs Used by the VIX

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>MAG RPCs used by the VIX</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPC Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><p><strong>MAG BROKER SECURITY</strong></p>
<p>Routine: BSE^MAGS2BSE</p></td>
<td>Returns a BSE token from BSE (Broker Security Enhancement) XUS SET VISITOR.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>MAG RPCs used by the VIX</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPC Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><p><strong>MAG DICOM GET HOSP LOCATION</strong></p>
<p>Routine: GETLOC^MAGDRPCB</p></td>
<td>Returns a list of matching hospital locations.</td>
</tr>
<tr class="odd">
<td><p><strong>MAG DICOM RADIOLOGY MODIFIERS</strong></p>
<p>Routine: MOD^MAGDRPCA</p></td>
<td>Returns a list of entries from the PROCEDURES MODIFIER file (#71.2) sorted by Radiology Imaging Type.</td>
</tr>
<tr class="even">
<td><p><strong>MAG DICOM RADIOLOGY PROCEDURES</strong></p>
<p>Routine: PROC^MAGDRPCA</p></td>
<td>This RPC returns a list of Radiology Procedures for ‘no-credit’ Imaging locations within a given division. If the division does not have any ‘no-credit’ Imaging locations defined, the results will return an error message indicating the problem. Modified by MAG*3.0*118 to – optionally – filter out procedure types <strong>B</strong>road and <strong>P</strong>arent.</td>
</tr>
<tr class="odd">
<td><p><strong>MAG DOD GET STUDIES IEN</strong></p>
<p>Routine: STUDY2^MAGDQR21</p></td>
<td>Returns study information based on the IMAGE file (#2005) Internal Entry Number (IEN) of the image group that is provided as a parameter.</td>
</tr>
<tr class="even">
<td><p><strong>MAG DOD GET STUDIES UID</strong></p>
<p>Routine: STUDY1^MAGDQR21</p></td>
<td>Returns study information based on the Study UID that is provided as a parameter.</td>
</tr>
<tr class="odd">
<td><p><strong>MAG EVENT AUDIT</strong></p>
<p>Routine: EVENT^MAGUAUD</p></td>
<td>The RPC is used to populate the data dictionaries (tables) introduced in this patch.</td>
</tr>
<tr class="even">
<td><p><strong>MAG GET NETLOC</strong></p>
<p>Routine: SHARE^MAGGTU6</p></td>
<td>Returns a list of all entries in the NETWORK LOCATION file (#2005.2).</td>
</tr>
<tr class="odd">
<td><p><strong>MAG IMAGE CURRENT INFO</strong></p>
<p>Routine: INFO^MAGDQR04</p></td>
<td>Returns current values for the various DICOM tags that are to be included in the header of an image.</td>
</tr>
<tr class="even">
<td><p><strong>MAG NEW SOP INSTANCE UID</strong></p>
<p>Routine: NEWUID^MAGDRPC9</p></td>
<td>Generates a new SOP Instance UID for an image and stores the value in the IMAGE file (#2005) if a SOP instance UID is not already present.</td>
</tr>
<tr class="odd">
<td><p><strong>MAG3 CPRS TIU NOTE</strong></p>
<p>Routine: IMAGES^MAGGNTI</p></td>
<td>Returns a list of all images for a Text Integration Utility (TIU) document.</td>
</tr>
<tr class="even">
<td><p><strong>MAG4 GET IMAGE INFO</strong></p>
<p>Routine: GETINFO^MAGGTU3</p></td>
<td>Returns specific fields of an image entry for display in the Clinical Display Image Information window.</td>
</tr>
<tr class="odd">
<td><p><strong>MAG4 INDEX GET ORIGIN</strong></p>
<p>Routine: IGO^MAGSIXGT</p></td>
<td>This call will return an array of INDEX ORIGIN.</td>
</tr>
<tr class="even">
<td><p><strong>MAG4 PAT GET IMAGES</strong></p>
<p>Routine: PGI^MAGSIXG1</p></td>
<td>Returns a list of image groups from the IMAGE file (#2005) based on filters provided.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG CPRS RAD EXAM</strong></p>
<p>Routine: IMAGEC^MAGGTRAI</p></td>
<td>Returns a list of images for the radiology exam.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG DEV FIELD VALUES</strong></p>
<p>Routine: GETS^MAGGTSYS</p></td>
<td>Returns a list of field values for an IEN in the IMAGE file (#2005).</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>MAG RPCs used by the VIX</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPC Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><p><strong>MAGG GROUP IMAGES</strong></p>
<p>Routine: GROUP^MAGGTIG</p></td>
<td>Returns array of images for a group entry in the IMAGE file (#2005). Included for backward compatibility only.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG INSTALL</strong></p>
<p>Routine: GPACHX^MAGQBUT4</p></td>
<td>Returns a list of all Imaging package installs on the host system.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG LOGOFF</strong></p>
<p>Routine: LOGOFF^MAGGTAU</p></td>
<td>Tracks the time of the Imaging session.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG OFFLINE IMAGE ACCESSED</strong></p>
<p>Routine: MAIL^MAGGTU3</p></td>
<td>Sends a message when there is an attempt to access image from an offline jukebox platter.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG PAT FIND</strong></p>
<p>Routine: FIND^MAGGTPT1</p></td>
<td>Used for patient lookups.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG PAT INFO</strong></p>
<p>Routine: INFO^MAGGTPT1</p></td>
<td>Returns a string of '^' delimited pieces of patient information.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG PAT PHOTOS</strong></p>
<p>Routine: PHOTOS^MAGGTIG</p></td>
<td>Returns a list of patient photo IDs.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG SYS GLOBAL NODE</strong></p>
<p>Routine: MAG^MAGGTSY2</p></td>
<td>Returns the global node of an IMAGE file (#2005) entry.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG WRKS UPDATES</strong></p>
<p>Routine: UPD^MAGGTAU</p></td>
<td>Starts a new session for image access logging.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGGACTION LOG</strong></p>
<p>Routine: LOGACT^MAGGTU6</p></td>
<td>Call to log an action performed on the image. Actions are logged the IMAGE ACCESS LOG file (#2006.95).</td>
</tr>
<tr class="even">
<td><p><strong>MAGGRPT</strong></p>
<p>Routine: BRK^MAGGTRPT</p></td>
<td>Returns associated report for Image IEN.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGGUSER2</strong></p>
<p>Routine: USERINF2^MAGGTU3</p></td>
<td>Returns information about a Clinical Display user.</td>
</tr>
<tr class="even">
<td><p><strong>MAGJ CACHELOCATION</strong></p>
<p>Routine: CACHEQ^MAGJUTL3</p></td>
<td>Obtains the locations for images that have been routed to remote sites/workstations.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGJ CPTMATCH</strong></p>
<p>Routine: CPTGRP^MAGJUTL4</p></td>
<td>Finds related radiology procedures based on the matching tables in the MAG RAD CPT MATCHING file (#2006.67).</td>
</tr>
<tr class="even">
<td><p><strong>MAGJ EXAM REPORT</strong></p>
<p>Routine: RADRPT^MAGJRPT</p></td>
<td>Retrieves a radiology report.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGJ PT ALL EXAMS</strong></p>
<p>Routine: PTLSTALL^MAGJLST1</p></td>
<td>Retrieves a list of all radiology exams for a selected patient.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>MAG RPCs used by the VIX</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPC Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><p><strong>MAGJ RADACTIVEEXAMS</strong></p>
<p>Routine: ACTIVE^MAGJLS2</p></td>
<td>Retrieves lists of “unread,” “recent,” or “all active” radiology exams for VistARad.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGJ RADCASEIMAGES</strong></p>
<p>Routine: OPENCASE^MAGJEX1</p></td>
<td>Fetches IMAGE file (#2005) information for all the images for a selected case. If the case's images are on the archive (jukebox), then this RPC initiates a fetch of the image files from the archive.</td>
</tr>
<tr class="even">
<td><p><strong>MAGJ RADORDERDISP</strong></p>
<p>Routine: ORD^MAGJRPT</p></td>
<td>Returns the Detailed Request Display (order) for the radiology exam.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGJ STUDY DATA</strong></p>
<p>Routine RPCIN^MAGJEX3</p></td>
<td>Obtains various study and/or image data stored in XML format.</td>
</tr>
<tr class="even">
<td><p><strong>MAGJ USER2</strong></p>
<p>Routine: USERINF2^MAGJUTL3</p></td>
<td>Returns information about a VistARad user.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGJ VIX LOG REMOTE IMG ACCESS</strong></p>
<p>Routine: LOGRIA^MAGJVAPI</p></td>
<td>Logs remote image accesses.</td>
</tr>
<tr class="even">
<td><p><strong>MAGN CPRS IMAGE LIST</strong></p>
<p><strong>Routine:</strong> IMAGEL^MAGNTRAI</p></td>
<td>Lists images for Rad Exams or TIU Notes by CPRS context.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV ADD WORK ITEM TAGS</strong></p>
<p>Routine: ADDTAG^MAGVIM01</p></td>
<td>Allows tags to be added to work items in the WORK ITEM (#2006.941) file. Tags consist of a tag name and a tag value. Tags and values can be used to look up entries in the WORK ITEM (#2006.941) file.</td>
</tr>
<tr class="even">
<td><p><strong>MAGV CONFIRM RAD ORDER</strong></p>
<p>Routine: CONFIRM^MAGVIM06</p></td>
<td>Returns a RAD/NUC MED ORDERS file (#75.1) IEN for a set of DICOM Unique Identifiers.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV CREATE WORK ITEM</strong></p>
<p>Routine:CRTITEM^MAGVIM01</p></td>
<td>Creates work item entries in the WORK ITEM file (#2006.94) and the WORK ITEM HISTORY file (#2006.941).</td>
</tr>
<tr class="even">
<td><p><strong>MAGV DELETE WORK ITEM</strong></p>
<p>Routine:DELWITEM^MAGVIM01</p></td>
<td>Deletes a single entry in the WORK ITEM file (#2006.941).</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV FIND WORK ITEM</strong></p>
<p>Routine:</p></td>
<td>Returns an array of work items with values that match the parameters provided.</td>
</tr>
<tr class="even">
<td><p><strong>MAGV GET NEXT WORK ITEM</strong></p>
<p>Routine:FIND^MAGVIM01</p></td>
<td>Returns the work item with the oldest LAST UPDATED date/time with the specified expected status and work item type.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV GET PAT ORDERS</strong></p>
<p>Routine:GETORD^MAGVIM02</p></td>
<td>Returns an array of consult or radiology orders for and input patient enterprise identifier.</td>
</tr>
<tr class="even">
<td><p><strong>MAGV GET WORK ITEM</strong></p>
<p>Routine: GETITEM^MAGVIM01</p></td>
<td>Returns all of the data elements for a single entry in the WORK ITEM file (#2006.941).</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV GET WORKLISTS</strong></p>
<p>Routine: GETLIST^MAGVIM01</p></td>
<td>Returns a list of all worklist entries in the WORKLIST file (#2006.942). The worklists name and active status are returned in an array.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>MAG RPCs used by the VIX</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPC Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><p><strong>MAGV IMPORT MEDIA LOG STORE</strong></p>
<p>Routine: IMPMEDIA^MAGVIM03</p></td>
<td>Files data from an Importer III media import event to the MAGV IMPORT MEDIA LOG file (#2006.9422).</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV IMPORT STATUS</strong></p>
<p>Routine: IMSTATUS^MAGVIM01</p></td>
<td>Given a set of UIDS, a patient identifier, and an accession number, this remote procedure returns the import status of a matching item.</td>
</tr>
<tr class="even">
<td><p><strong>MAGV IMPORT STUDY LOG REPORT</strong></p>
<p>Routine: IMPLOGEX^MAGVIM03</p></td>
<td>Exports data from the MAGV IMPORT STUDY LOG file (#2006.9421) as formatted reports.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV IMPORT STUDY LOG STORE</strong></p>
<p>Routine: IMPLOGIN^MAGVIM03</p></td>
<td>Collects study-level data for objects imported by the DICOM Importer III.</td>
</tr>
<tr class="even">
<td><p><strong>MAGV RAD EXAM ORDER</strong></p>
<p>Routine: XMORDER^MAGVIM05</p></td>
<td>Wraps a call to the RAMAG EXAM ORDER remote procedure, and re-formats the output for the DICOM Importer III application. Returns the IEN of the new order in the RAD/NUC MED ORDERS file (#75.1), or an array of error messages.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV RAD EXAM REGISTER</strong></p>
<p>Routine: XMREGSTR^MAGVIM05</p></td>
<td>Wraps a call to the RAMAG EXAM REGISTER remote procedure, and re-formats the output for the DICOM Importer III application. Returns the IEN of the new case in the RAD/NUC MED PATIENT file (#70), or an array of error messages.</td>
</tr>
<tr class="even">
<td><p><strong>MAGV RAD STAT COMPLETE</strong></p>
<p>Routine: XMCOMPLT^MAGVIM05</p></td>
<td>Wraps call to code underlying the remote procedure RAMAG EXAM COMPLETE.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGV RAD STAT EXAMINED</strong></p>
<p>Routine: XMEXAMIN^MAGVIM05</p></td>
<td>Wraps calls to the remote procedure RAMAG EXAMINED and re-formats the output.</td>
</tr>
<tr class="even">
<td><p><strong>MAGV UPDATE WORK ITEM</strong></p>
<p>Routine: UPDITEM^MAGVIM01</p></td>
<td>Updates a work item in the WORK ITEM file (#2006.94). It also creates an entry in the WORK ITEM HISTORY file (#2006.941).</td>
</tr>
</tbody>
</table>

#### Non-MAG RPCs used by the VIX

> The VIX uses the following RPCs from other VistA packages. The use of these RPCs is governed by Integration Control Registrations (ICRs) stored in FORUM. For information about viewing specific ICRs, see Chapter 12 in the *VistA Imaging Technical Manual*

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Non-MAG RPCs used by the VIX</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RPC Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><p><strong>DDR FILER</strong></p>
<p>Routine: FILEC^DDR3</p></td>
<td>Generic call to file edits into a FileMan file.</td>
</tr>
<tr class="odd">
<td><p><strong>DG SENSITIVE RECORD ACCESS</strong></p>
<p>Routine: PTSEC^DGSEC4</p></td>
<td>Verifies that a user is not accessing his/her own Patient file record if the RESTRICT PATIENT RECORD ACCESS field (#1201) in the MAS PARAMETERS file (#43) is set to yes and the user does not hold the DG RECORD ACCESS security key. If parameter set to yes and user is not a key holder, a social security number must be defined in the NEW PERSON file (#200) for the user to access any Patient file (#2) record.</td>
</tr>
<tr class="even">
<td><p><strong>DG SENSITIVE RECORD BULLETIN</strong></p>
<p>Routine: NOTICE^DGSEC4</p></td>
<td>Adds an entry to the DG Security Log file (#38.1) and generates the sensitive record access bulletin depending on the value in ACTION input parameter.</td>
</tr>
<tr class="odd">
<td><p><strong>PSB GETPROVIDER</strong></p>
<p>Routine: PROVLST^PSBRPCMO</p></td>
<td>Used to get a list of active providers.</td>
</tr>
<tr class="even">
<td><p><strong>VAFCTFU CONVERT ICN TO DFN</strong></p>
<p>Routine: GETDFN^VAFCTFU1</p></td>
<td>Given a patient Integration Control Number (ICN), this will return the patient Internal Entry Number (IEN) from the PATIENT file (#2).</td>
</tr>
<tr class="odd">
<td><p><strong>VAFCTFU GET TREATING LIST</strong></p>
<p>Routine: TFL^VAFCTFU1</p></td>
<td>Given a patient DFN, this will return a list of treating facilities.</td>
</tr>
<tr class="even">
<td><p><strong>XUS AV CODE</strong></p>
<p>Routine: VALIDAV^XUSRB</p></td>
<td>Checks to see whether a ACCESS/VERIFY code pair is valid.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS DIVISION GET</strong></p>
<p>Routine: DIVGET^XUSRB2</p></td>
<td>Returns a list of divisions of a user.</td>
</tr>
<tr class="even">
<td><p><strong>XUS DIVISION SET</strong></p>
<p>Routine: DIVSET^XUSRB2</p></td>
<td>Sets the user's selected division in DUZ(2) during sign-on.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS SIGNON SETUP</strong></p>
<p>Routine: SETUP^XUSRB</p></td>
<td>Establishes environment necessary for DHCP sign-on.</td>
</tr>
<tr class="even">
<td><p><strong>XWB CREATE CONTEXT</strong></p>
<p>Routine: CRCONTXT^XWBSEC</p></td>
<td>Establishes context on the server that the Broker will check before executing any other remote procedure.</td>
</tr>
<tr class="odd">
<td><p><strong>XWB GET VARIABLE VALUE</strong></p>
<p>Routine: VARVAL^XWBLIB</p></td>
<td>Accepts the name of a variable that will be evaluated and its value returned to the caller.</td>
</tr>
</tbody>
</table>

### Database Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX retrieves data from both local and remote VistA databases using the RPCs described in the previous sections.

> The VIX writes data to VistA if it needs to update the following:

- IMAGE ACCESS LOG file (#2006.95). See [*Logging on VistA*](#logging-on-vista).
- IMAGE file (#2005) with SOP instance UIDs for images that do not have SOP instance UIDs already. The VIX does this using the MAG NEW SOP INSTANCE UID RPC used by other Imaging components for the same purpose.

> There are no general VIX parameters stored on VistA. Any site-specific VIX parameters are set during installation and are stored in the local configuration files of the VIX.

### Exported Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no exported VistA menu options associated with the VIX.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX uses the MAG VIX ADMIN security key to determine who can access the VIX transaction log. See [*Using the VIX Transaction* Log](#using-the-vix-transaction-log) for more information.

> When a Clinical Display, VIX Image Viewer or VistARad user uses the VIX to access remote VA images, their locally assigned security keys are honored on the remote VistA system. VistARad and Clinical Display security keys are described in the *VistA Imaging Technical Manual*.

### User Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a VA clinician retrieves metadata or images from a remote VA site via a VIX, their VistA account information is used to automatically log into the remote VA site. Users do not need to explicitly enter access or verify codes.

> When a DoD clinician retrieves metadata or images from a VA site, the credentialing is handled by the Station 200 VistA system that is co-located with the CVIX. If a local service account was established for the initial VIX implementation (MAG\*3.0\*83), that account is no longer needed after updating to the most recent VIX.

> A DoD clinician’s requests for local images are logged at the site where the images reside. See [*Image Sharing-related Logging*](#image-sharing-related-logging) for details.

## Other VIX Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX incorporates the following additional components.

- [<u>Security certificate</u>](#vix-security-certificate)
- [<u>.NET</u>](#net)
- [<u>Sun JRE</u>](#sun-jre)
- [<u>Laurel Bridge DCF toolkit</u>](#laurel-bridge-dcf-toolkit)
- [<u>Aware JPEG2000 toolkit</u>](#aware-jpeg2000-toolkit-license)

> Each component is described in the following sections. All of these components are integral to VIX operations and cannot be modified without impacting VIX operations.

### VIX Security Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a VIX communicates with another VIX, they exchange security certificates for authentication purposes. This long-term security certificate is stored in the \VixCertStore directory on the server where the VIX is installed.

> The VIX security certificate is provided as a part of the VIX installation process and must be available to complete a VIX installation.

### .NET

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The .NET 4.X framework is needed to install and update the VIX software.

> Patches for .NET 4.X, if any, should be installed as soon as reasonably possible after they are released in accordance with local site maintenance policies and the Windows update guidelines documented in the [*<u>VistA Imaging Technical Manual.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

> Other versions of .NET have no impact on the VIX installer or update processes and can be installed or not in accordance with local policy.

### Sun JRE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX’s servlet container and the VIX itself require the Sun Java Runtime Environment (JRE). The Sun JRE is installed automatically as a part of the VIX installation process.

> Do not install later versions of the Sun JRE. The correct JRE for the VIX is bundled with the VIX installation software.

### Laurel Bridge DCF Toolkit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Laurel Bridge DICOM Connectivity Framework (DCF) toolkit, version 3.3.X, is a third-party toolkit that VIX uses to convert images to and from DICOM format.

> The license for this toolkit is tied to the server where the VIX is installed. Shifting to a new server will require an updated license from Laurel Bridge. If a new or updated license is needed, contact the [<span class="mark">REDACTED</span>](mailto:VHAVILBLicenses@va.gov) mail group.

> Version 3.3.X of this toolkit is bundled with the VIX installer and is installed automatically as part of the VIX setup process. Do not install this toolkit manually.

> This toolkit requires the presence of a compatible *Microsoft Visual C++ 2005 Redistributable Package (x86)*. If it is not present, C++ will be installed automatically as a part of the VIX setup process.

### Aware JPEG2000 Toolkit License

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For information regarding the Aware Toolkit License, see the *[<u>VistA Imaging Exchange</u>](https://www.va.gov/vdl/application.asp?appid=105) [<u>(VIX) Service Installation Guide.</u>](https://www.va.gov/vdl/application.asp?appid=105)*

# Appendix: Image Sharing and DICOM Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Images are delivered to VA sites by the CVIX and originate from the Data Access Service (DAS) framework.

## DoD DICOM Object Filtering

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Study information (including reports) for studies associated with all DICOM modality types can be retrieved from the DoD by VA sites with a local VIX.

> However, for certain DICOM object types, the associated objects are not actually images and Clinical Display and VistARad cannot display them. For these types of DICOM studies, the VIX will provide the metadata (including reports), but will not provide the image counts and/or image locations. The VIX blocks the following DICOM modality types, and only if the data originates from the DoD.

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>DoD objects not displayable at the VA (metadata and reports remain accessible)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DICOM Modality Description</strong></td>
<td><strong>DICOM Identifier</strong></td>
</tr>
<tr class="even">
<td>Audio</td>
<td>AU</td>
</tr>
<tr class="odd">
<td><p>Document</p>
<p><em>(Used for DICOM encapsulated secondary captures and scanned documents. Not equivalent to MS Word .doc files )</em></p></td>
<td>DOC</td>
</tr>
<tr class="even">
<td>Cardiac Electrophysiology (waveforms)</td>
<td>EPS</td>
</tr>
<tr class="odd">
<td>Fiducials</td>
<td>FID</td>
</tr>
<tr class="even">
<td>Hemodynamic Waveform</td>
<td>HD</td>
</tr>
<tr class="odd">
<td>Key Object Selection</td>
<td>KO</td>
</tr>
<tr class="even">
<td>MR Spectroscopy</td>
<td>MS</td>
</tr>
<tr class="odd">
<td>Presentation State (all types)</td>
<td>PR</td>
</tr>
<tr class="even">
<td>Respiratory Waveform</td>
<td>RESP</td>
</tr>
<tr class="odd">
<td>Radiotherapy Structure Set</td>
<td>RTSTRUCT</td>
</tr>
<tr class="even">
<td>RT Treatment Record</td>
<td>RTRECORD</td>
</tr>
<tr class="odd">
<td>Radiotherapy Dose</td>
<td>RTDOSE</td>
</tr>
<tr class="even">
<td>Radiotherapy Plan</td>
<td>RTPLAN</td>
</tr>
<tr class="odd">
<td>Structured Report (all types)</td>
<td>SR</td>
</tr>
</tbody>
</table>

## VA DICOM Images Provided to DoD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DoD clinicians can request the following types of exams from the VA via the CVIX:

<table>
<colgroup>
<col style="width: 71%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>VA DICOM Objects Provided to DoD</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DICOM Modality Description</strong></td>
<td><strong>DoD Identifiers</strong></td>
</tr>
<tr class="even">
<td>Angioscopy (retired)</td>
<td>AS, RAD AS</td>
</tr>
<tr class="odd">
<td>Biomagnetic Imaging</td>
<td>BI, RAD BI</td>
</tr>
<tr class="even">
<td>Color flow Doppler (retired)</td>
<td>CD, RAD CD</td>
</tr>
<tr class="odd">
<td>Cinefluorography (retired)</td>
<td>CF, RAD CF</td>
</tr>
<tr class="even">
<td>Culposcopy (retired)</td>
<td>CP, RAD CP</td>
</tr>
<tr class="odd">
<td>Computed Radiography</td>
<td>CR, RAD CR</td>
</tr>
<tr class="even">
<td>Cystoscopy (retired)</td>
<td>CS, RAD CS</td>
</tr>
<tr class="odd">
<td>Computed Tomography</td>
<td>CT, RAD CT</td>
</tr>
<tr class="even">
<td>Duplex Doppler (retired)</td>
<td>DD, RAD DD</td>
</tr>
<tr class="odd">
<td>Diaphanography</td>
<td>DG, RAD DG</td>
</tr>
<tr class="even">
<td>Digital Microscopy (retired)</td>
<td>DM, RAD DM</td>
</tr>
<tr class="odd">
<td>Digital Radiography</td>
<td>DR, RAD DR, DX, RAD DX</td>
</tr>
<tr class="even">
<td>Digital Subtraction Angiography</td>
<td>DS, RAD DS</td>
</tr>
<tr class="odd">
<td>Echocardiography (retired)</td>
<td>EC, RAD EC</td>
</tr>
<tr class="even">
<td>Endoscopy</td>
<td>ES, RAD ES</td>
</tr>
<tr class="odd">
<td>Fluorescein Angiography (retired)</td>
<td>FA, RAD FA</td>
</tr>
<tr class="even">
<td>Fundoscopy</td>
<td>FS, RAD FS</td>
</tr>
<tr class="odd">
<td>General Microscopy</td>
<td>GM, RAD GM</td>
</tr>
<tr class="even">
<td>Intra-oral Radiography</td>
<td>IO, RAD IO</td>
</tr>
<tr class="odd">
<td>Laparoscopy (retired)</td>
<td>LP, RAD LP</td>
</tr>
<tr class="even">
<td>Laser Surface Scan</td>
<td>LS, RAD LS</td>
</tr>
<tr class="odd">
<td>Magnetic Resonance Angiography (retired)</td>
<td>MA, RAD MA</td>
</tr>
<tr class="even">
<td>Mammography</td>
<td>MG, RAD MG</td>
</tr>
<tr class="odd">
<td>Magnetic Resonance</td>
<td>MR, RAD MR</td>
</tr>
<tr class="even">
<td>Nuclear Medicine</td>
<td>NM, RAD NM</td>
</tr>
<tr class="odd">
<td>Positron Emission Tomography</td>
<td>PT, RAD PT</td>
</tr>
<tr class="even">
<td>Radio Fluoroscopy</td>
<td>RF, RAD RF</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 71%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>VA DICOM Objects Provided to DoD</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DICOM Modality Description</strong></td>
<td><strong>DoD Identifiers</strong></td>
</tr>
<tr class="even">
<td>Radiographic Imaging</td>
<td>RG, RAD RG</td>
</tr>
<tr class="odd">
<td>Single-Photon Emission Computed Tomography (retired)</td>
<td>ST, RAD ST</td>
</tr>
<tr class="even">
<td>Thermography</td>
<td>TG, RAD TG</td>
</tr>
<tr class="odd">
<td>Ultrasound</td>
<td>US, RAD US</td>
</tr>
<tr class="even">
<td>X-ray Angiography</td>
<td>XA, RAD XA</td>
</tr>
<tr class="odd">
<td>External-Camera Photography</td>
<td>XC, RAD XC</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \#2005 file, 72
> \#2006.95 file, 47
> .NET 4.X framework, 73 ‘listener, 11
> abstract (thumbnail) quality, 39 Access Type (#1) field, 47
> accounts, user, 20, 72
> Additional Data (#100) field, 48
> AWIV, 8
> backups, VIX, 33
> cache. *See* VIX cache Clinical Display
> Message History log, 49
> metadata requests generated by, 35 troubleshooting, VIX-related, 51
> compression, image, 38
> connection timeouts, 50
> CSV file, exporting transaction log as, 23 customer support, 3
> CVIX
> described, 8
> Log Collector service and, 28
> data sources, VIX, 64 data, sensitive, 20 dependent systems
> summary of, 18
> VIX shutdown and, 29 DIAGNOSTIC parameter, 38
> DICOM toolkit, 73 DoD hospitals
> PACS integrator, 9
> façades (interfaces), VIX, 63 FDA guidelines, 1
> format, image, 39
> get... methods (metadata requests), 35, 36
> help, getting, 3 hostnames, changes to, 21
> Image Access Log (#2006.95) file, 47
> Image File (#2005), 72 image sharing
> DoD to VA, 7 VA to DoD, 6 VA to VA, 5
> images
> quality and compression, 38 retention periods for, 41 retrieval delays, 51 retrieving via VIX, 37 supported, 5, 7
> types vs. formats, 39 interfaces, VIX, 63
> Java Runtime Environment, 73 keys, security, 72
> Laurel Bridge DCF toolkit, 73 Log Collector service, 28
> logs
> Image Access Log (#2006.95) file, 47
> Java, 66
> Message History, 49
> VIX transaction log, 22, 29
> MAG VIX ADMIN key, 72
> maintenance and monitoring, 29 Message History Log, 49 metadata
> caching of, 40
> described, 34
> retention periods for, 41 retrieving via VIX, 34
> multidivisional sites VIX behavior at, 8
> VIX cache behavior at, 40
> PACS integrator, DoD, 9 patients, polytrauma, 50
> pingServer, 36
> pingServerEvent, 35
> port numbers, changes to, 21 ports, VIX, 29
> postImageAccess, 36
> postImageAccessEvent, 35
> purging, VIX, 28
> quality, image, 38
> REFERENCE parameter, 39 remote image views, 51 render service, 11, 31
> retrieval times, 51
> ROI disclosures, 54
> RPCs used by VIX, 66, 70
> security, 20
> security certificate for VIX, 73 security keys, 72
> security realms, VIX, 63 sensitive data, 20
> server names, changes to, 21 service, listener, 11
> service, render, 11, 31
> service, viewer, 11, 31 servlet container, VIX, 63 shutdown, VIX, 29
> site service, 21
> sqlexpress, 11
> startup VIX, 29
> Sun JRE, 73
> support, customer, 3
> THUMBNAIL parameter, 39
> timeouts, connection, 50 transaction log
> accessing, 22
> exporting, 23
> fields in, 23, 27
> MAG VIX ADMIN key, 72
> monitoring, 29
> troubleshooting, 51 Try Again message, 52
> TSV file, exporting transaction log as, 23 user accounts, 20, 72
> viewer service, 11, 31 VistA Site Service, 21
> VistA, changes made by VIX, 72 VistARad
> metadata requests generated by, 36 troubleshooting, VIX-related, 51
> Visual J# runtime environment, 73 VIX
> backups and, 33
> connection timeouts, 50
> dependencies, 18
> described, 1, 4
> image handling, 37, 38
> installation locations, 65
> Java logs, 66
> licensed subcomponents of, 73 metadata handling, 34
> monitoring, 29 multidivisional sites and, 8 operational priority of, 19 ports used by, 29
> purge operations, 28
> remote image views and, 51 RPCs used by, 66, 70
> security, 20
> security certificate, 73
> security keys, 72 shutdown and startup, 29 terms of use, 1 transaction log, 22
> troubleshooting, 51
> VistA changes made by, 72 VistA logging and, 47
> sites, multidivisional, 8 VIX cache
> checking for images, 37 checking for metadata, 34 described, 40
> monitoring, 29
> VIX Log Collector service, 28 Web services, VIX, 63
