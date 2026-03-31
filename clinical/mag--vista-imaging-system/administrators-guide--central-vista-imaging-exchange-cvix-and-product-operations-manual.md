---
consolidated_title: "central vista imaging exchange (cvix) administrator's guide and product operations manual"
app_code: MAG
doc_type: AG
master_source: "Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)"
master_pub_date: November 2024
consolidated_from: 5 versions
prior_versions:
  - "MAG*3*269 Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)"
  - "MAG*3*303 Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)"
  - "MAG*3*329 Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)"
  - "MAG*3*348 Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)"
---

---
title: |
  VistA Imaging eXchange (VIX) <span id="PatchTitle" class="anchor"></span>Enhancements and Maintenance

  MAG\*3.0\*<span id="PatchNumber" class="anchor"></span>358

  Central VistA Imaging eXchange (CVIX)  
  Administrator's Guide and Product  
  Operations Manual (POM)
---

> ![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/001.png)

November 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

CVIX Administrator's Guide and Product Operations Manual  
November 2024Property of the US Government

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging Product Development group.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies and are hereby acknowledged.

VistA Imaging Product Development  

Veterans Affairs Internet:  
<http://www.va.gov/imaging>

VA intranet <span class="mark">REDACTED</span>

Revision History

| Date       | Revision | Description                                                                                                            | Author                              |
|------------|----------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| 11/05/2024 | 17.0     | Initial draft for MAG\*3.0\*358.                                                                                       | VA IT VistA Imaging Technical team  |
| 07/01/2023 | 16.0     | Initial draft for MAG\*3.0\*348.                                                                                       | VA IT VistA Imaging Technical team  |
| 05/03/2023 | 15.0     | Initial draft for MAG\*3.0\*329.                                                                                       | VA IT VistA Imaging Technical team  |
| 11/03/2022 | 14.0     | Initial draft for MAG\*3.0\*303.                                                                                       | VA IT VistA Imaging Technical team  |
| 06/01/2022 | 13.6     | Updates for MAG\*3.0\*269 release date.                                                                                | VA IT VistA Imaging Technical team  |
| 05/02/2022 | 13.5     | Updates for P269 T5.                                                                                                   | VA IT VistA Imaging Technical team  |
| 04/20/2022 | 13.4     | Updates for P269 T4.                                                                                                   | VA IT VistA Imaging Technical team  |
| 02/07/2022 | 13.3     | Updates for P269 T3.                                                                                                   | VA IT VistA Imaging Technical team  |
| 12/21/2021 | 13.2     | Updates for P269 T2.                                                                                                   | VA IT VistA Imaging Technical team  |
| 11/30/2021 | 13.1     | Updates for P269 based on feedback from review.                                                                        | VA IT VistA Imaging Technical team  |
| 05/31/2021 | 13.0     | Initial draft for P269.                                                                                                | VA IT VistA Imaging Technical team  |
| 02/28/2021 | 12.1     | Updates for MAG\*3.0\*254 to include DoD images to VA Clinicians section.                                              | VA IT VistA Imaging Technical team  |
| 01/31/2021 | 12.0     | Updates for MAG\*3.0\*254.                                                                                             | VA IT VistA Imaging Technical team  |
| 07/31/2020 | 11.0     | MAG\*3.0\*249 Updates.                                                                                                 | <span class="mark">REDACTED</span>  |
| 03/31/2019 | 10.0     | Additional MAG\*3.0\*205 Updates.                                                                                      | <span class="mark">REDACTED</span>  |
| 02/28/2019 | 9.0      | Additional MAG\*3.0\*205 Updates.                                                                                      | <span class="mark">REDACTED</span>  |
| 08/31/2018 | 8.0      | Additional MAG\*3.0\*205 Updates.                                                                                      | <span class="mark">REDACTED</span>  |
| 07/31/2018 | 7.0      | Additional MAG\*3.0\*205 Updates.                                                                                      | <span class="mark">REDACTED</span>  |
| 05/31/2018 | 6.0      | Additional MAG\*3.0\*205 Updates.                                                                                      | <span class="mark">REDACTED</span>  |
| 04/30/2018 | 5.0      | Revised for MAG\*3.0\*205.                                                                                             | <span class="mark">REDACTED</span>  |
| 09/30/2017 | 4.0      | Revised for MAG\*3.0\*171.                                                                                             | <span class="mark">REDACTED</span>  |
| 08/31/2013 | 3.0      | Revised for MAG\*3.0\*34/116/118, 119, 127, 129. Revised sections Using the Cache Browser and Cache Delete.            | <span class="mark">REDACTED</span>  |
| 07/31/2013 | 2.0      | Revised for MAG\*3.0\*124. Revised sections Using the Cache Browser and Cache Delete.                                  | <span class="mark">REDACTED</span>  |
| 03/31/2013 | 1.0      | Document created for Imaging patch MAG\*3.0\*124. Expanded CVIX Transition Log section with step-by-step instructions. | <span class="mark">REDACTED</span>  |

<span id="_Ref52801618" class="anchor"></span>Table 1: DoD Images Available by Type and Source for VA Viewer
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Terms of Use](#terms-of-use)
  - [Intended Audience](#intended-audience)
  - [Document Conventions](#document-conventions)
  - [Related Information](#related-information)
- [CVIX Overview](#cvix-overview)
  - [CVIX Major Functions](#cvix-major-functions)
    - [Provide DoD Images to VA Clinicians](#provide-dod-images-to-va-clinicians)
    - [Provide VA images to DoD requestors](#provide-va-images-to-dod-requestors)
    - [Provide VA and DoD images to Image Viewer](#provide-va-and-dod-images-to-image-viewer)
    - [Host the VistA Site Service](#host-the-vista-site-service)
  - [CVIX Physical and Logical Description](#cvix-physical-and-logical-description)
  - [CVIX Operational Priority](#cvix-operational-priority)
  - [CVIX Dependencies](#cvix-dependencies)
  - [The CVIX, VIXes, and Multidivisional VA Sites](#the-cvix-vixes-and-multidivisional-va-sites)
  - [CVIX Connection Security](#cvix-connection-security)
- [CVIX General Operations](#cvix-general-operations)
  - [CVIX Monitoring](#cvix-monitoring)
  - [Using the CVIX Transaction Log](#using-the-cvix-transaction-log)
    - [CVIX Transaction Log Fields](#cvix-transaction-log-fields)
    - [CVIX Transaction Log Fields (Export Only)](#cvix-transaction-log-fields-export-only)
    - [Logging on Remote VistA Systems](#logging-on-remote-vista-systems)
  - [User Notifications](#user-notifications)
  - [Cluster-related Activities](#cluster-related-activities)
    - [CVIX cluster: take the node offline](#cvix-cluster-take-the-node-offline)
    - [CVIX cluster: bring the node online](#cvix-cluster-bring-the-node-online)
  - [CVIX Planned Startup and Shutdown](#cvix-planned-startup-and-shutdown)
    - [Planned Full CVIX Shutdown](#planned-full-cvix-shutdown)
    - [Planned Full CVIX Startup](#planned-full-cvix-startup)
  - [CVIX Data Retention and Purges](#cvix-data-retention-and-purges)
  - [CVIX and Backups](#cvix-and-backups)
  - [Critical Metrics](#critical-metrics)
  - [CVIX and User Management](#cvix-and-user-management)
  - [Configurations for DoD images Provided to VA Clinicians](#configurations-for-dod-images-provided-to-va-clinicians)
    - [Additional Configurations for ECIA only for DoD images Provided to VA Clinicians](#additional-configurations-for-ecia-only-for-dod-images-provided-to-va-clinicians)
  - [Configure DICOM Service Class Providers (SCP) Functionality](#configure-dicom-service-class-providers-scp-functionality)
    - [Application Entity (AE) Titles Configuration](#application-entity-ae-titles-configuration)
    - [Laurel Bridge AE Titles Configuration on CVIX](#laurel-bridge-ae-titles-configuration-on-cvix)
    - [AE Titles Configuration on DICOM Service Class User (SCU)](#ae-titles-configuration-on-dicom-service-class-user-scu)
    - [Tomcat DICOM SCP Configuration](#tomcat-dicom-scp-configuration)
    - [Laurel Bridge DICOM SCP Configuration](#laurel-bridge-dicom-scp-configuration)
  - [Configure ID Conversion](#configure-id-conversion)
- [VistA Site Service](#vista-site-service)
  - [VistA Site Service Overview](#vista-site-service-overview)
  - [Checking the Site Service](#checking-the-site-service)
  - [Updating Site Service Data](#updating-site-service-data)
- [CVIX Image Sharing](#cvix-image-sharing)
  - [Remote Metadata Retrieval](#remote-metadata-retrieval)
  - [Remote Image Retrieval](#remote-image-retrieval)
  - [Caching of Metadata and Images](#caching-of-metadata-and-images)
    - [Cache Retention Periods](#cache-retention-periods)
    - [Cache Location and Structure](#cache-location-and-structure)
  - [Image Sharing and CVIX Timeouts](#image-sharing-and-cvix-timeouts)
- [VIX Log Collector Service](#vix-log-collector-service)
  - [VIX Log Collector Overview](#vix-log-collector-overview)
  - [Log Collector Automatic Emails](#log-collector-automatic-emails)
  - [Archived Transaction Log Storage Area](#archived-transaction-log-storage-area)
  - [Excluding a VIX from Log Collection](#excluding-a-vix-from-log-collection)
- [CVIX Troubleshooting](#cvix-troubleshooting)
  - [Routine Errors](#routine-errors)
    - [Connectivity](#connectivity)
    - [Timeouts](#timeouts)
    - [Security](#security)
    - [Station 200 Issues](#station-200-issues)
  - [Significant Errors](#significant-errors)
    - [Error Logs](#error-logs)
  - [Unplanned Shutdowns](#unplanned-shutdowns)
    - [Recovering after unplanned restart of a single CVIX server](#recovering-after-unplanned-restart-of-a-single-cvix-server)
    - [Recovering after unplanned reboot of a single load balancer](#recovering-after-unplanned-reboot-of-a-single-load-balancer)
    - [Recovering after an unscheduled power loss to all components](#recovering-after-an-unscheduled-power-loss-to-all-components)
  - [System Recovery](#system-recovery)
    - [Back-out Procedures](#back-out-procedures)
    - [Rollback Procedures](#rollback-procedures)
  - [CVIX Support](#cvix-support)
- [CVIX Reference/Software Description](#cvix-referencesoftware-description)
  - [CVIX Java Components](#cvix-java-components)
    - [CVIX Servlet Container](#cvix-servlet-container)
    - [CVIX Security Realms](#cvix-security-realms)
    - [CVIX Interfaces](#cvix-interfaces)
    - [CVIX Core](#cvix-core)
    - [CVIX Data Sources](#cvix-data-sources)
  - [Java Installation Locations](#java-installation-locations)
    - [CVIX folders on the System Drive](#cvix-folders-on-the-system-drive)
    - [Java Logs](#java-logs)
  - [VistA/M Information](#vistam-information)
    - [RPCs used by the CVIX](#rpcs-used-by-the-cvix)
    - [Non-MAG RPCs used by the CVIX](#non-mag-rpcs-used-by-the-cvix)
    - [Database Information](#database-information)
    - [Exported Menu Options](#exported-menu-options)
    - [Security Keys](#security-keys)
  - [Other VIX Components](#other-vix-components)
    - [CVIX Security Certificates](#cvix-security-certificates)
    - [.NET](#net)
    - [Java Runtime Environment (JRE)](#java-runtime-environment-jre)
    - [Laurel Bridge DCF Toolkit](#laurel-bridge-dcf-toolkit)
    - [SQLite](#sqlite)
    - [Aware JPEG2000 Toolkit](#aware-jpeg2000-toolkit)
    - [LibreOffice](#libreoffice)
- [Operations and Maintenance Responsibilities/RACI](#operations-and-maintenance-responsibilitiesraci)
- [Appendix A: Image Sharing and DICOM Images](#appendix-a-image-sharing-and-dicom-images)
  - [DoD DICOM Object Filtering](#dod-dicom-object-filtering)
- [Appendix B: CVIX Tools](#appendix-b-cvix-tools)
- [Appendix C: Image Viewer Dashboard](#appendix-c-image-viewer-dashboard)
  - [Image Viewer Dashboard: Homepage](#image-viewer-dashboard-homepage)
  - [Image Viewer Dashboard: Logs](#image-viewer-dashboard-logs)
  - [Image Viewer Dashboard: Search](#image-viewer-dashboard-search)
  - [Image Viewer Dashboard: System Preferences](#image-viewer-dashboard-system-preferences)
    - [Annotation Preferences](#annotation-preferences)
    - [Cine Preferences](#cine-preferences)
    - [Layout Preferences](#layout-preferences)
    - [Copy Attributes](#copy-attributes)
    - [Log Preferences](#log-preferences)
  - [Image Viewer Dashboard: Status](#image-viewer-dashboard-status)
- [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)
This document explains how to maintain and administer the Central VistA Imaging eXchange (CVIX) service.
The CVIX is a special implementation of the VistA Imaging eXchange (VIX) that resides in the VA Amazon Web Services (AWS) cloud. The CVIX facilitates data sharing with the Department of Defense (DoD) across organizational boundaries. The CVIX also supports image data access for VA users not associated with a specific VistA (MyHealtheVet, VBA Claims, Joint Legacy Viewer / Joint Longitudinal Viewer (JLV), etc.).
This document refers to the "Viewer" web application which is also known as the:
- CVIX Viewer
- VIX Viewer
- Enhanced Image Viewer
- Image Viewer
- VistA Imaging Viewer
This document assumes that the CVIX is installed and configured. For information about installation and initial configuration, contact the VistA Imaging development group.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX is a component of VistA Imaging and is regulated as a medical device by the Food and Drug Administration (FDA). Use of the CVIX is subject to the following provisions:

> **CAUTION:** Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.

The FDA classifies VistA Imaging and the CVIX (as a component of VistA Imaging) as a medical device. Unauthorized modifications to VistA Imaging, including the CVIX, such as installing unapproved software, will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820).

Because software distribution/inventory management tools can install inappropriate or unapproved software without a local administrator’s knowledge, sites must exclude the CVIX from such system management tools.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is intended for the VA data center personnel responsible for managing and monitoring the CVIX.

This document presumes a working knowledge of the VistA environment and VistA Imaging components. It presumes intermediate-to-advanced knowledge of Windows server administration and Windows cluster administration.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses the following typographic conventions:

- Controls, options, and button names are shown in Bold.
- A vertical bar is used to separate successive menu choices. For example: “Click File \| Open” means: “Click the File menu; then click the Open option.”
- Keyboard key names are shown in bold and in brackets.
- Sample output is shown in monospace.
- Important or required information is shown in a Note.

## Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to this manual, the following documents contain information about the CVIX:

MAG\*3.0\*358 Patch Description available at <span class="mark">REDACTED</span>

VIX Installation Guide available at <span class="mark">REDACTED</span>

> **NOTE:** This manual serves as both a Product Operations Manual (POM) and a System Administrator’s Guide.

# CVIX Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a high-level summary of what the CVIX does and how it does it. This section covers:

- CVIX Major Functions
- CVIX Physical and Logical Description
- CVIX Operational Priority
- CVIX Dependencies
- The CVIX, VIXes, and Multidivisional VA Sites
- CVIX Connection Security

## CVIX Major Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX’s major functions are:

- Provide the Department of Defense (DoD) images to VA clinicians.
- Provide VA images to DoD clinicians.
- Provide VA/ DoD images to JLV/ Image Viewer users.
- Host the VistA Site Service, the repository of connection information used by various Imaging components.
- Host the VIX log collector.
- Host the VIX functionality to allow consuming applications to obtain metadata and images.

Each of these functions is described in the following sections.

> **NOTE:** The VIX Log Collector Service is installed on the same hardware allocated for the CVIX but is completely independent of the CVIX. For more information about the VIX Log Collector, see *VIX Log Collector Service*.

### Provide DoD Images to VA Clinicians

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX provides a single point of access to the DoD image sources for shared VA/DoD patients (patients with IDs correlated in the VistA Master Veteran Index). At sites that have implemented a VIX, VA clinicians can access these images via the CVIX using the Clinical Display, JLV/ Image Viewer, and VistARad applications.

The flow of DoD images through a CVIX is illustrated in Figure 1. This complexity is not evident to the VA clinicians; they simply use Clinical Display or VistARad to select the desired images.

<span id="_Ref53064225" class="anchor"></span>Figure 1: DoD-to-VA Image Sharing

> ![Table 1 details the types of DoD images that can be retrieved and where they originate from.](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/002.png)

*Table 1 details the types of DoD images that can be retrieved and where they originate from.*

> **NOTE:** There is an ability to switch between HAIMS (Health Artifact and Image Management Solution) and ECIA (Enterprise Clinical Imaging Archive) for DoD images.

<table>
<caption><p><span id="_Ref52871442" class="anchor"></span>Table 2: Anticipated Operational Priority of the CVIX Broken Out by Function</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 37%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>DoD Image category</th>
<th>DoD source</th>
<th>Viewable in VA VistA using</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DoD DICOM (radiology)</td>
<td><p>Available from participating DoD facilities via the ECIA, which is through the CVIX. Note: For a list of DoD participating facilities and information about the types of DICOM objects that can be retrieved, see the <a href="https://www.va.gov/vdl/application.asp?appid=105">VIX Administrator’s Guide</a>.</p>
<p>Metadata for these images is provided by ECIA and the actual images come from ECIA.</p></td>
<td>Clinical Display, JLV/ Image Viewer and VistARad</td>
</tr>
<tr class="even">
<td>DoD artifacts (non-radiology</td>
<td>Available if the Defense Medical Information Exchange (DMIX) Data Exchange Service (DES) servers are online accessible through DAS (Data Access Service) and if DAS servers are capable of communicating with the CVIX.</td>
<td>Clinical Display, JLV/ Image Viewer</td>
</tr>
</tbody>
</table>

<span id="_Ref52871442" class="anchor"></span>Table 2: Anticipated Operational Priority of the CVIX Broken Out by Function

### Provide VA images to DoD requestors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX is also the portal used by all DoD clinicians to access VA images for shared VA/DoD patients. The flow of VA images through a CVIX is illustrated in Figure 2.

<span id="_Ref53651185" class="anchor"></span>Figure 2: VA-to-DOD Image Sharing

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/003.png)

DoD clinicians can access non-DICOM medical images and scanned documents from all VA sites via the CVIX.

> **NOTE:** DoD clinicians cannot access images not stored in VistA Imaging at a VA site or images on a non-integrated 3rd party appliance (i.e., local).

If a VA site implements a local VIX, DoD clinicians also can access locally stored DICOM (radiology) images. For additional details about the types of images that can be accessed, see the [VIX Administrator’s Guide](https://www.va.gov/vdl/application.asp?appid=105).

> **NOTE:** There is an ability to switch between HAIMS and NilRead™ or other query retrieve devices for DoD images.

> **NOTE:** At the VA sites where the image is stored, DoD clinician access requests are logged in the local VistA system. This logging is described in detail in the [VIX Administrator’s](https://www.va.gov/vdl/application.asp?appid=105) Guide.

### Provide VA and DoD images to Image Viewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX hosts all the components needed to provide the image metadata access portal and an embedded Zero footprint image viewer. Data flow between the Image Viewer and a consuming application like JLV is depicted in Figure 3.

<span id="_Ref53560489" class="anchor"></span>Figure 3: Data Flow for Image Viewer Applications

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/004.png)

JLV (clinical and VBA users), not associated with a specific VistA/ VIX, can access any image or report associated with a VA Progress Note or a VA Radiology package report, or DoD images via the CVIX. The CVIX handles all connections with VA sites, insulating the JLV from connection information changes.

> **NOTE:** JLV users cannot access images and other images not stored in VistA Imaging at a VA site.

The Image Viewer itself is described in the [Enhanced Image Viewer User Guide](https://www.va.gov/vdl/application.asp?appid=105)*.*NOTE: The Image Viewer is hosted in a separate application (JLV) that handles user authentication, patient selection, and progress note/report selection. For information about JLV, see [<u>https://www.va.gov/vdl/application.asp?appid=224</u>](https://www.va.gov/vdl/application.asp?appid=224)

The Image Viewer also accommodates VBA access. Authentication information (username and password) for VBA is configurable in the Viewer_config.xml file.

### Host the VistA Site Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Site Service is the repository of connection information used by various imaging components to connect to other VistA systems and VIXes. The CVIX itself also uses it. The VistA Site Service is described in *VistA Site Service*.

## CVIX Physical and Logical Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX cluster is located in the VA Enterprise Cloud (VAEC) AWS environment. The CVIX cluster is made up of:

- Locally load-balanced VMs in AWS Availability Zone 1 (AZ1) and locally load-balanced VMs in AWS Availability Zone 2 (AZ2).
- The enterprise F5 load balancers provide local and global load balancing.
- Each VM is configured with 8 GB RAM per server, 3 Core CPU, each running Windows 2019.

The configuration is virtualized. The hardware was sized to service the estimated user demand based on an estimated number of requests during peak usage.

> **NOTE:** The existing CVIX hardware is actively monitored to ensure that adequate capacity is available. CVIX hardware has completed the migration to the VA VAEC AWS environment to increase capacity and elasticity.

## CVIX Operational Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX is designed for continuous availability. Table 2 summarizes the anticipated operational priority of the CVIX broken out by function (if the CVIX server is offline, all functions are unavailable).

<table>
<caption><p><span id="_Ref52871622" class="anchor"></span>Table 3: CVIX System Requirements</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>CVIX Function</th>
<th>Priority</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Host site service</td>
<td>High</td>
<td><p>If the site service is not available, Clinical Display or VistARad will not work for remote access because they cannot find their local VIX. (They will still work for local image access, and they can still do a remote login into a specific site if they know which site the images are at.)</p>
<p>Some 3<sup>rd</sup> party apps such as TeleReader will not function properly until their access to the site service is restored.</p></td>
</tr>
<tr class="even">
<td>Image Viewer</td>
<td>High</td>
<td>If the Viewer is not running, the CVIX is considered offline and removed from the F5 Load Balancer’s list of nodes to use (The F5 monitors two services on each CVIX node for declaring online status: Apache Tomcat and the VIX Image Viewer). The Viewer depends on the VIX Render service, which depends on a local SQLite VixRender database.</td>
</tr>
<tr class="odd">
<td>VA/DoD</td>
<td>High</td>
<td>The CVIX provides access to remote data that may be relevant or highly valuable for patient care.</td>
</tr>
</tbody>
</table>

<span id="_Ref52871622" class="anchor"></span>Table 3: CVIX System Requirements

> **NOTE:** Datacenter and Capacity redundancy is established – AZ1 and AZ2 are geographically distant. Both are active and ready at any time, with no intervention needed to handle the CVIX load. This configuration ensures Continuity of Operations (COOP) for the CVIX or disaster recovery. AZ1 and AZ2 are each other’s failover sites, and the F5 Traffic Manager is configured to detect failures and automatically redirect traffic between sites and nodes as required.

## CVIX Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 shows the systems that must be present for proper CVIX operation. One or more of these systems being absent will reduce CVIX capabilities, but not eliminate all of them.

| System                    | Function                                                                                                                                                                           | Interface method | CVIX behavior if “System” is not available                                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Local VistA (Station 200) | Provides CVIX with a list of VA facilities that have treated a shared VA/DoD patient. Also provides security tokens that the CVIX uses to access VA sites to fulfill DoD requests. | LAN/RPC          | DoD clinicians, JLV, Blue Button, and VBA users will not be able to access VA or DoD images for VA/DoD shared patients.                                               |
| Site VIXes                | Provide metadata and images to the CVIX.                                                                                                                                           | WAN/HTTP         | DoD clinicians, JLV, Blue Button, and VBA users will not be able to access site-specific radiology images via CVIX, but non-radiology images will still be available. |
| Remote VistA              | Source of remotely stored VA images for DoD clinician access.                                                                                                                      | WAN/RPC          | The CVIX cannot provide images from that site.                                                                                                                        |
| DAS                       | Gateway to DoD DICOM images for VA clinician access.                                                                                                                               | WAN/HTTP         | The CVIX cannot provide DoD DICOM images to the VA.                                                                                                                   |
| ECIA                      | DoD metadata and image repository.                                                                                                                                                 | DICOM SCU        | The CVIX cannot provide DoD DICOM images to the VA.                                                                                                                   |
| DES                       | Source of DoD artifacts and non-DICOM metadata for VA clinician access.                                                                                                            | WAN/HTTP         | The CVIX cannot provide DoD artifacts (scanned documents and non-radiology images) to the VA.                                                                         |

<span id="_Ref52871932" class="anchor"></span>Table 4: Data Path Based on Number of Site VIXes

## The CVIX, VIXes, and Multidivisional VA Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a CVIX requests images and metadata from a VA multidivisional site, the path the data takes depends on how many VIXes are present at that site (Table 4).

<table>
<caption><p><span id="_Ref52873003" class="anchor"></span>Table 5: Descriptions of CVIX Transaction Log Fields</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th># of<br />
VIXes</th>
<th>Data retrieval path</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2 or more</td>
<td>The CVIX gets metadata from the VIX at the primary division. If a subdivision has local image storage and a VIX, the CVIX requests the image from that VIX. If a subdivision has local image storage but does not have a VIX, the CVIX requests the image from the VIX at the primary division.</td>
</tr>
<tr class="even">
<td>1</td>
<td>The CVIX gets all images and metadata from the VIX at the primary division.</td>
</tr>
<tr class="odd">
<td>0</td>
<td><p>The CVIX gets metadata and image locations directly from the VistA System at the primary site and images directly from their storage locations.</p>
<p><strong>Note:</strong> At non-VIX-sites, DICOM (radiology) images cannot be retrieved by the CVIX for DoD requestors.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref52873003" class="anchor"></span>Table 5: Descriptions of CVIX Transaction Log Fields

## CVIX Connection Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The CVIX only responds to requests from authenticated applications. Application-level authentication is invisible to the clinical user who initiated the request.
- When communicating with VistA Remote Procedure Call (RPC) brokers, the CVIX supports Broker Security Exchange (BSE), Identity and Access Management (IAM) STS (Secure Token Service) tokens, and pre-BSE-style remote logins. The CVIX will use BSE remote logins if BSE is enabled on the remote system and BSE authenticated is being utilized.
- CVIX-to-VIX communications require a valid security certificate.

# CVIX General Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section covers:

- CVIX Monitoring
- Using the CVIX Transaction Log
- User Notifications
- Cluster-related Activities
- CVIX Planned Startup and Shutdown
- CVIX Data Retention and Purges
- CVIX and Backups
- CVIX and User Management

## CVIX Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CVIX monitoring/ alert capabilities are fully automated via custom VistA Imaging monitoring utilities and SolarWinds enterprise monitor. In addition, the CVIX admins routinely perform the following manual monitoring and maintenance activities to verify automated tools.

- Once a day, access the transaction log on each CVIX node to verify that the CVIX is running.
- Once a week, check available cache space on each CVIX node.
- Review the CVIX processing load and available capacity by using the Windows Task Manager to determine the CPU cycles being consumed by the Apache Tomcat task.
- On rare occasions, corrupt metadata or image data may be cached and must be manually deleted. One possible indication is the inability to load an image/exam without an error being presented.

If an instance of the CVIX service encounters a fatal error or if a server node in the CVIX cluster reboots unexpectedly, the CVIX service will self-recover.

## Using the CVIX Transaction Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX transaction log records information about every image and metadata transfer handled by the CVIX. Entries in the log are retained for 90 days and then purged. A permanent backup copy of the CVIX transaction log is also stored in the failover cluster described in *VIX Log Collector Service*.

An instance of the CVIX transaction log resides on each active server in the CVIX cluster. The log itself is accessed via a web browser.

To access the CVIX transaction log, go to https://*FQDN*:<span class="mark">REDACTED</span>/Vix/secure/VixLog.jsp (where *FQDN* is the fully qualified domain name of the cluster on which the CVIX is installed).

The main transaction log Web page can be used to display, filter, and export log entries of interest. By default, the page displays the 100 most recent transactions for the current day with the newest entries at the top. For detailed information about each field in the log, see *CVIX Transaction Log Fields*.

> **NOTE:** The CVIX is set up as a load-balanced cluster without server affinity. Check multiple CVIX nodes to see all log entries related to a given transaction (that is, receipt and fulfillment of a specific data request.

To view the CVIX transaction log, complete the following steps:

1.  Navigate to https://*FQDN*:<span class="mark">REDACTED</span>/Vix/secure/VixLog.jsp.
2.  Enter the vixlog username and password in the boxes and click OK.

> **NOTE:** Transaction log credentials are authenticated against the local VistA system. Attempting to use Windows credentials will not work.

3.  The CVIX Transaction Log page will display.
- By default, the page displays the 100 most recent transactions for the current day.
- The transactions are ordered from newest to oldest.
- For detailed information about each field in the log, see CVIX Transaction Log Fields.
4.  To view different parts of the log, use the paging buttons near the top and at the bottom of the log as follows:
- Click ![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/005.png) to show the next page of (older) entries.
- Click ![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/006.png) to show the last page of (oldest) entries.
- Click ![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/007.png) to show the previous page of (newer) entries.
- Click ![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/008.png) to show the first page (newest) entries in the log.

To change the date range and page size in the VIX transaction log, complete the following steps:

1.  To change the date range used to filter log entries, change the values in the From Date/Time and To Date/Time boxes, and then click Show in Browser.
5.  Dates are formatted as YYYY-MM-DD HH-MM.
6.  The most recent log entries are shown first.
7.  To change the number of entries displayed on each page, select a different value from the Transactions per Page box, and then click Show in Browser.

To export part of the transaction log, complete the following steps:

1.  On the Transaction Log page, use the date range boxes near the top of the page to specify the desired date range of export entries.
8.  One thousand exported log entries will result in an approximately 0.5-megabyte file.
9.  The Transactions per Page setting does not apply when log entries are supported.
10. Click Save as CSV for comma-separated values or Save as TSV for tab-separated values.
11. Use the browser Save dialog box to specify where the file will be stored.
12. Use a spreadsheet program or a text editor to open the resulting file.

### CVIX Transaction Log Fields 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the transaction log is displayed in a Web browser, the fields in Table 5 are shown. These fields are also included when the transaction log is exported as a tab-separated values (TSV) or comma-separated values (CSV) file.

Fields that only appear when the transaction log is exported are listed in the next section.

<table>
<caption><p><span id="_Ref52873201" class="anchor"></span>Table 6: Descriptions of CVIX Transaction Log Fields for Export Only</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Date and Time</td>
<td>When the transaction was processed.<br />
Formatted as MM-DD-YYYY, HH:MM: SS, AM/PM.</td>
</tr>
<tr class="even">
<td>Time on VIX</td>
<td>The length of the transaction in milliseconds begins when the CVIX receives a message and ends when the CVIX begins to respond.</td>
</tr>
<tr class="odd">
<td>ICN</td>
<td>The Integration Control Number (ICN) uniquely identifies the patient across the VA and DoD systems. (Note that the ICN is not equivalent to the VA patient ID and is not considered Protected Health Information.)</td>
</tr>
<tr class="even">
<td>Query Type</td>
<td><p>A multi-part field that indicates [handler method receiving site &lt;- sending site].</p>
<p><em>handler</em> identifies the VIX Web application that handled the request, for details, see the <em>CVIX Interfaces</em>.</p>
<p><em>method</em> identifies the specific operation performed.<br />
<br />
<em>receiving site &lt;- sending site</em> indicates the station number and home community ID (where applicable) of the sending and receiving sites.</p></td>
</tr>
<tr class="odd">
<td>Query Filter</td>
<td>Applies to study metadata only. Indicates whether a list of all available studies for a patient was transferred or if a subset based on a date was transferred.</td>
</tr>
<tr class="even">
<td>Asynchronous</td>
<td>Indicates whether the transaction was performed asynchronously (true) or synchronously (false).</td>
</tr>
<tr class="odd">
<td>Items Returned</td>
<td><p>The number of items returned to the requester.</p>
<p>For study metadata, it indicates the number of studies or images in the list being transmitted. For an image, this field will have a value of 1 if the requested image was transmitted or 0 if the requested image was not found.</p>
<p>For other operations, this column is not populated.</p></td>
</tr>
<tr class="even">
<td>Items Received</td>
<td><p>The number of items retrieved from the remote site.</p>
<p>For study metadata, it indicates the number of studies or images in the list being received. For an image, this field will have a value of 1 if the requested image was received or 0 if the requested image was not received.</p>
<p>If the CVIX is operating asynchronously, the values in this field may not match the values in the Items Returned field. In the exported log, this field is labeled “Data Source Items Received.”</p></td>
</tr>
<tr class="odd">
<td>Bytes Returned</td>
<td>If populated, the amount of data returned in the request. In the exported log, this field is labeled “Façade Bytes Returned.”</td>
</tr>
<tr class="even">
<td>Bytes Received</td>
<td><p>If populated, the amount of data received in the request.</p>
<p>In the exported log, this field is labeled “Data Source Bytes</p>
<p>Received.”</p></td>
</tr>
<tr class="odd">
<td>Throughput</td>
<td>The image transfer rate. Both the rate and the units of measurement (KB/sec, MB/sec are indicated). Not populated for metadata. This value is calculated at runtime and is not present in the exported log.</td>
</tr>
<tr class="even">
<td>Quality</td>
<td><p>Populated for images only. It can be one of the following:</p>
<ul>
<li><p>THUMBNAIL</p></li>
<li><p>REFERENCE</p></li>
<li><p>DIAGNOSTIC</p></li>
<li><p>DIAGNOSTIC UNCOMPRESSED</p></li>
</ul>
<p>For more information about these parameters, see <em>Remote Image Retrieval</em>.</p></td>
</tr>
<tr class="odd">
<td>Command Class Name</td>
<td>Internal CVIX command used for debugging and support.</td>
</tr>
<tr class="even">
<td>Originating IP Address</td>
<td>The IP address of the workstation that initiated the image or metadata request. (The same IP address will be reported for all requests originating from the DAS.)</td>
</tr>
<tr class="odd">
<td>User</td>
<td>The name of the End User that initiated the request.</td>
</tr>
<tr class="even">
<td>Item in Cache?</td>
<td><p>TRUE indicates the image is served from the cache. FALSE indicates the image had to be retrieved from its original storage location.</p>
<p>Not populated for other types of transactions.</p></td>
</tr>
<tr class="odd">
<td>Error Message</td>
<td>If a request fails, this field contains an error message describing the failure.</td>
</tr>
<tr class="even">
<td>Modality</td>
<td>If applicable, indicates the modality associated with an image request (standard DICOM modality type codes are used).</td>
</tr>
<tr class="odd">
<td>Purpose of Use</td>
<td>Included for HIPAA tracking purposes.</td>
</tr>
<tr class="even">
<td>Datasource Protocol</td>
<td><p>The source of the data being handled:</p>
<p>vistaimaging – Data from a VistA system</p>
<p>MIX – Radiology data from a source outside of VistA (from the DoD) or from Vista (to the DoD), both through DAS</p>
<p>Vftp – Data from another VIX</p>
<p>DX – Non-radiology data from a source outside of VistA (from the DoD) through DAS/DES</p>
<p>AX – VistA Imaging Documents served by the CVIX (to DoD) through DAS/DES</p></td>
</tr>
<tr class="odd">
<td>Response Code</td>
<td><p>The response code for a request; generally equivalent to HTTP response codes, but in some cases, they are used for statuses specific to the CVIX. Typical values include:</p>
<p>200 – OK (success)</p>
<p>401 – Unauthorized</p>
<p>404 – Not found</p>
<p>409 – Image exists but is not yet available on DoD side and/or Imaging jukebox</p>
<p>412 – BSE token expired</p>
<p>415 – Image conversion exception</p>
<p>500 – Internal server error</p></td>
</tr>
<tr class="even">
<td>Realm Site Number</td>
<td>The STATION NUMBER (field (#99) of the INSTITUTION file (#4) of the site that the requester’s credentials are authenticated against.</td>
</tr>
<tr class="odd">
<td>URN</td>
<td>Only populated for image transactions. Universal Resource Name (URN); the unique name of the image being requested.</td>
</tr>
<tr class="even">
<td>Transaction Number</td>
<td>The Globally Unique Identifier (GUID) for an image or metadata transaction. For transactions that originate from Clinical Display or the DAS, the same identifier will be reflected in the Image Access log at the site where the images are stored. If a transaction crosses the CVIXDAS boundary, the originator’s transaction ID is used on the other side as well (interagency transactions tracking support).</td>
</tr>
<tr class="odd">
<td>VIX Software Version</td>
<td>The software version of the CVIX.</td>
</tr>
<tr class="even">
<td>VistA Login Method</td>
<td>The login method used to access a VistA system. This is only populated when connecting to VistA and only for the transaction that initiates the connection. Possible values are BSE, Claims, or LOCAL.</td>
</tr>
<tr class="odd">
<td>Client Version</td>
<td>If the source of the image or metadata request is VistA Imaging Clinical Display, the version number of the Clinical Display software will be recorded here and not populated for other requestors.</td>
</tr>
<tr class="even">
<td>Data Source Method</td>
<td>Identifies the specific operation performed by the data source.</td>
</tr>
<tr class="odd">
<td>Data Source Version</td>
<td>The version number of the data source.</td>
</tr>
<tr class="even">
<td>Data Source Response Server</td>
<td>The name of the server that responded to the metadata or image request; useful for determining which node in a clustered VIX handled the request. Only populated for requests directed to a VIX.</td>
</tr>
<tr class="odd">
<td>VIX Site Number</td>
<td>The site number of the local VIX (as defined in the local VIX’s VixConfig.xml file). The site number should match the station number (field #99) defined in the INSTITUTION file (#4).</td>
</tr>
<tr class="even">
<td>Requesting VIX Site Number</td>
<td>The site number of the requesting VIX (as defined in the VIX’s VixConfig.xml file), Only populated for Federation (VIX-to-VIX) requests. The site number should match the station number (field #99) defined in the INSTITUTION file (#4).</td>
</tr>
</tbody>
</table>

<span id="_Ref52873201" class="anchor"></span>Table 6: Descriptions of CVIX Transaction Log Fields for Export Only

### CVIX Transaction Log Fields (Export Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the transaction log is exported as a tab- or comma-separated file, the exported file includes all the fields available in the browser view of the log (see the previous section). The exported file also includes additional fields that are described in Table 6.

| Name                               | Description                                                                                                                                                                     |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Façade Bytes Retrieved             | The number of bytes returned to the requestor, where the requestor could be JLV, Clinical Display, VistARad, another VIX, or the CVIX.                                          |
| Data Source Bytes Returned         | The number of bytes returned from the data source, where the data source could be a remote VistA system, a VIX, the CVIX, or a DoD data source such as the DAS or DES, or ECIA. |
| Machine Name                       | Name of the CVIX server that performed the transaction.                                                                                                                         |
| Requesting Site                    | The ID of the site that originated the request; this value is also shown in the Query Type column.                                                                              |
| Exception Class Name               | Internal data used for debugging and support.                                                                                                                                   |
| Time to First Byte                 | Number of milliseconds elapsed from the point where the CVIX opens a connection to a remote site until the remote site begins responding to the request.                        |
| Responding Site                    | The ID of the site that filled the request; this value is also shown in the Query Type column.                                                                                  |
| Command ID                         | Internal ID used for debugging and support.                                                                                                                                     |
| Parent Command ID                  | Internal ID used for debugging and support.                                                                                                                                     |
| Façade Image Format Sent           | The format of the image VIX returns to the requester.                                                                                                                           |
| Façade Image Quality Sent          | The quality of the image VIX returns to the requester; in some cases, this quality will be better than the quality requested (as indicated in the “Quality” column).            |
| Data Source Image Format Received  | The format of the image VIX receives from its source.                                                                                                                           |
| Data Source Image Quality Received | The quality of the image VIX receives from its source.                                                                                                                          |
| Debug Information                  | Internal messaging is used for debugging and support.                                                                                                                           |
| Thread ID                          | The name of the thread that processed the transaction.                                                                                                                          |

<span id="_Ref52885374" class="anchor"></span>Table 7: CVIX Purge Schedule

### Logging on Remote VistA Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the CVIX retrieves images and metadata from a VA site that does not have a VIX, the CVIX will log the image access information in that site’s local IMAGE ACCESS LOG file (#2006.95) the same way a VIX would.

For details about how this information is logged, see the <u>[VIX Administrator’s Guide](https://www.va.gov/vdl/application.asp?appid=105).</u>

## User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Announce a CVIX outage (planned or unplanned) through the Automated Notification Report (ANR) system by contacting the National Help Desk.

For ongoing connectivity issues with DAS, contact the VA IT DAS Technical mail group at <span class="mark">REDACTED</span>.

## Cluster-related Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections cover:

- CVIX cluster: take the node offline.
- CVIX cluster: bring the node online.

### CVIX cluster: take the node offline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action will require a Service Request (SR) or Service Now ticket to the network team to take a fully functional node out of the cluster. To temporarily take a node out of the cluster, stop Apache Tomcat, which will cause the F5 port monitors to declare the node inaccessible.

### CVIX cluster: bring the node online

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action will require a SR to the network team to add a fully functional node to the cluster. To place a temporarily disabled node back in the cluster, start Apache Tomcat, which will cause the F5 port monitors to declare the node accessible.

## CVIX Planned Startup and Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX is designed to be running at all times. For procedures about taking individual servers offline for maintenance, please see the Cluster-related Activities section above. Operations procedures dictate rolling updates to avoid a full shutdown. If necessary, fully shut down and restart all CVIX hardware, using the steps below.

### Planned Full CVIX Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Review *CVIX Dependencies* to ensure that all the implications of a full CVIX shutdown can be planned for.
13. Contact the National Help Desk to file an ANR.
14. Bring down each CVIX VM as the plan requires.

### Planned Full CVIX Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Bring up each VM as started.
15. Verify that Apache Tomcat, Vix Viewer and Vix Render services have started.
16. If there is an open ANR for the CVIX, update the ANR to indicate that the service interruption is over.

## CVIX Data Retention and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX runs a daily purge process for locally stored data, as described in Table 7.

<table>
<caption><p><span id="_Ref98403115" class="anchor"></span>Table 8: Critical Metrics</p></caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Operation</th>
<th>When Performed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Purge Java logs</td>
<td>1 A.M. daily for Java log entries more than 5 days old.</td>
</tr>
<tr class="even">
<td>Purge transaction log<br />
entries</td>
<td>2 A.M. daily for transaction log entries more than 5 days old.</td>
</tr>
<tr class="odd">
<td>Purge CVIX cache</td>
<td><p>3 A.M. daily for images more than 30 days old for DoD images, but more than seven days old for VA images.</p>
<p>Once per minute for old VA metadata, once per hour for old DoD metadata</p></td>
</tr>
<tr class="even">
<td>Purge CVIX Render Cache and DB</td>
<td>12 A.M. (midnight) daily for data older than two days or larger than 1024 MB.</td>
</tr>
</tbody>
</table>

<span id="_Ref98403115" class="anchor"></span>Table 8: Critical Metrics

## CVIX and Backups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 7 represents the data retention values set at the time of release. The location to alter these settings are:

- Tomcat Java logs – adjust days in [C:\VixConfig\JavaLogConfiguration.Config](file:///C:/VixConfig/JavaLogConfiguration.Config), under \<retentionPeriodDays\> and restart Apache Tomcat.
- VIX Transaction logs – adjust days in [C:\VixConfig\TransactionLoggerLocalDataSource-1.0.Config](file:///C:/VixConfig/TransactionLoggerLocalDataSource-1.0.Config), under \<retentionPeriodDays\> and restart Apache Tomcat.
- VixCache – [C:\VixConfig\cache-config\ImagingExchangeCache-cache.xml](file:///C:/VixConfig/cache-config/ImagingExchangeCache-cache.xml) under va-image-region, dod-image-region, and scip-region respectively adjust the ...-lifespan value (make sure the value is defined above in the same file) and restart Apache Tomcat.
- VixRenderCache and VIX SQLite DB – [C:\Program](file:///C:/Program) Files\VistA\Imaging\VIX.Config\Vix.Render.config under the \<Purge\> entry the MaxAgeDays= and MaxCacheSizeMB= values and restart Viewer and Render services.

The CVIX does not need to be explicitly backed up:

- The VIX log collector service automatically backs up CVIX transaction logs.
- CVIX cache is transitory and does not need to be backed up.
- CVIX-specific configuration settings are minimal and can be reestablished by rerunning the CVIX installer. Contact the VIX Development Group by email for details. (<span class="mark">REDACTED</span>)

## Critical Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Critical metrics of the CVIX are shown in Table 8.

| System Accessibility           | 24/7                                |
|--------------------------------|-------------------------------------|
| System Uptime                  | Based on VistA uptime               |
| Online Operational Performance | Aggregate image throughput \>5 Mb/s |
| Production Incidents           | Fewer than 1/month                  |

<span id="_Ref52885819" class="anchor"></span>Table 9: Types and Sources of Metadata requested by Application

## CVIX and User Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CVIX administrators access and maintain the CVIX using NEMA zero token-enabled accounts.

VA clinicians requesting data via the CVIX use local VistA site credentials or authorized VA application credentials (i.e., MHV, JLV, etc.). These are independent of the CVIX.

DoD clinicians requesting data via the CVIX authenticate through DoD EHR authentication (i.e., Armed Forces Health Longitudinal Technology Application (AHLTA), HAIMS, etc.). System-to-system access occurs via a service account (named CVIX, USER) defined for DoD on the Station 200 VistA System.

## Configurations for DoD images Provided to VA Clinicians 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DoD images that can be retrieved from the VA can originate from HAIMS or ECIA. A configuration change to the MIXDataSource-1.0.config file in C:\VixConfig can be made to switch the source of the DoD Images provided to VA clinicians. This configuration is performed as part of the CVIX Installation, see the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105). This section is provided in the event a change needs to be made to this configuration.

The ability to enable the CVIX to collect DoD images from the ECIA requires the following information:

- The connection to AcuoMed, AcuoAccess, and ID lookup software/application.
- The Digital Imaging and Communications in Medicine (DICOM) modality types not to be returned from the DoD.
- Receive the blacklists for three different imaging display applications (VistA Imaging Clinical Display, JLV, VistARad).

Open the MIXDataSource-1.0.config file in C:\VixConfig. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file. Set the value of useEcia to true or false.

- Set useEcia to true if DoD images provided to VA clinicians are to use ECIA.
- Set useEcia to false if DoD images provided to VA clinicians are to use HAIMS.

Update the MIXDataSource-1.0.config file to set useEcia to either true or false (see Figure 4), (if not already set to the correct value) (inside \<useEcia\> \</useEcia\>).

<span id="_Ref56088655" class="anchor"></span>Figure 4: MIXDataSource-1.0.config file - Bottom Portion (Template)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/009.png)

If DoD images provided to VA clinicians are to use HAIMS:

- No, additional configuration is needed. Do not perform the steps in *Additional Configurations for ECIA only for DoD images Provided to VA Clinicians*.

If DoD images provided to VA clinicians are to use ECIA:

- Additional configuration is needed. Perform all the steps in *Additional Configurations for ECIA only for DoD images Provided to VA Clinicians*.

### Additional Configurations for ECIA only for DoD images Provided to VA Clinicians 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This describes additional configuration steps <u>only to be performed</u> when CVIX collection of DoD medical images from <u>ECIA is enabled</u> (i.e., \<useEcia\>true\</useEcia\>).

Perform this step to further configure the CVIX collection of DoD medical images to ECIA via the MIXDataSource-1.0.config file.

> **NOTE:** Before moving forward with the instructions for this step, it is expected that the site administrator is aware of all needed entries in the configuration including \<host\>, \<callingAE\>, and \<calledAE\> for AcuoMed and \<host\>, \<port\>, and \<protocol\>for AcuoAccess.

> **NOTE:** The configuration including \<host\>, \<callingAE\>, and \<calledAE\> for AcuoMed and \<host\> for AcuoAccess are set based on the server type (i.e., test or production) during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise, leave them as they are.

Open the MIXDataSource-1.0.config in C:\VixConfig. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file.

To enable the ECIA configuration, further update the MIXDataSource-1.0.config like Figure 5 and Figure 6:

1.  Set the entry for the host for AcuoMed, (inside \<host\> \</host\>).
17. Set the entry for the port for AcuoMed (inside \<port\> \</port\>).
18. Set the entry for the client identification for AcuoMed (inside \<callingAE\> \</callingAE\>).
19. Set the entry for the server identification for AcuoMed (inside \<calledAE\> \</calledAE\>).
20. Set the entry for the host for AcuoAccess (inside \<host\> \</host\>).
21. Set the port for AcuoAccess (inside \<port\> \</port\>).
22. Set the protocol for AcuoAccess (inside \<protocol\> \</ protocol\>).
23. Verify the \<string\>SR\</string\> line is NOT present inside the \<emptyStudyModalities\> \</emptyStudyModalities\>. (If present, remove this line).
24. Set the DICOM modality types that will not be returned from the DoD (inside \<string\> \</string\> tags).

> **NOTE:** The \<string\> \</string\> tags inside the vistaRadModalityBlacklist are set during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise, leave them as they are.

> **NOTE:** Inside the \<string\> \</string\> tags, insert the DICOM Identifier for the modality. For example, if an “SR” is inserted inside the \<string\> \</string\> tag, then a Structured Report will not be returned from the DoD.

> **NOTE:** If more or less DICOM modality types (referred to as a modality blacklist) are not to be returned from the DoD, add or remove additional \<string\> \</string\> lines (within the opening and closing tags for vistaRadModalityBlacklist). Inside the \<string\> \</string\> tags, insert the DICOM Identifier for the modality.

25. Set the DICOM Service-Object Pair (SOP) Class UIDs (referred to as SOP blacklists) that represent image types and that will be replaced with a static image file for three different image viewer applications (Vista Imaging Clinical Display, JLV, VistaRad). For the blacklist changes, add or remove the DICOM SOP Class UIDs according to the prerequisites. (inside \<string\> \</string\> tags for Vista Imaging Clinical Display; inside \<string\> \</string\> tags for JLV; inside \<string\> \</string\> tags for VistaRad).

> **NOTE:** The \<string\> \</string\> tags inside the SOP blacklists (i.e., sopBlacklistForClinicalDisplay, sopBlacklistForVixViewer, or sopBlacklistForVistaRad) are set during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise, leave them as they are.

> **NOTE:** For example, if a “1.2.840.10008.5.1.4.1.1.88.11” is inserted inside the \<string\> \</string\> tag, then the Basic Text SR that the SOP Class UID represents will be replaced with a static image file for Vista Imaging Clinical Display.

> **NOTE:** For example, if a “1.2.840.10008.5.1.4.1.1.88.11” is inserted inside the \<string\> \</string\> tag, then the Basic Text SR that the SOP Class UID represents will be replaced with a static image file for JLV.

> **NOTE:** For example, if a “1.2.840.10008.5.1.4.1.1.88.11” is inserted inside the \<string\> \</string\> tag, then the Basic Text SR that the SOP Class UID represents will be replaced with a static image file for VistaRad.

> **NOTE:** Inside the \<string\> \</string\> tags, insert the DICOM SOP Class UIDs according to the prerequisites.

> **NOTE:** If more or less DICOM SOP Class UIDs are needed, add or remove additional \<string\> \</string\> lines within the opening and closing tags for the appropriate viewer (i.e., sopBlacklistForClinicalDisplay, sopBlacklistForVixViewer, or sopBlacklistForVistaRad). Inside the \<string\> \</string\> tags, insert the DICOM SOP Class UIDs to blacklist.

Save the MIXDataSource-1.0.config file after updating the entries.

<span id="_Ref48825630" class="anchor"></span>Figure 5: MIXDataSource-1.0.config file - Top Portion (Template)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/010.png)

<span id="_Ref55317764" class="anchor"></span>Figure 6: MIXDataSource-1.0.config file - Middle Portion (Template)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/011.png)

## Configure DICOM Service Class Providers (SCP) Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides details on the DICOM Service Class Provider (SCP) configuration. The DICOM SCP is a service provider on the VIX/CVIX that transfers DICOM files between the VA and DoD. The DICOM SCP is used to allow VA clinicians to use Commercial PACS, or other query retrieve devices, and DoD clinicians to use NilRead™ or other query retrieve devices, to get remote VistA images through the use of DICOM C-FIND and C-MOVE.

Henceforth, this section refers to, Commercial PACS, NilRead™, and query retrieve devices as a DICOM SCP client.

> **NOTE:** NilRead™ is for CVIX, but VIX also can provide data to Commercial PACS to read, as the protocol used is the same; however, other query retrieve devices can also be used.

*Application Entity (*AE) Titles Configuration must be performed manually after CVIX Installation and a Tomcat restart performed after completed. The CVIX install performs some of the configuration for the DICOM SCP automatically with reasonable defaults and predefined entries. Reasonable defaults and predefined entries include the configuration described in *Tomcat DICOM SCP Configuration* and *Laurel Bridge DICOM SCP Configuration* and if specific configuration values are desired instead of the reasonable defaults, then after updating and saving the configuration file, a Tomcat restart must be completed.

> **NOTE:** For additional installations and/or subsequent patch releases, no additional changes to the *Application Entity (*AE) Titles Configuration are necessary unless the settings configured have changed and an update is needed.

> **NOTE:** To update access and verify codes for the account with VistA credentials, plain text versions can be entered directly into the configuration file and are encrypted after restarting the Apache Tomcat service. The access and verify codes can also be updated in the configuration file with a reconfigure installation described see the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105) or use the ImagingUtilities-0.1.jar in C:\VixConfig\Encryption to assist with generating encrypted forms of plain text access and verify codes.

> **NOTE:** If updates are needed to the local drive for the VIX cache, see the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105) and perform a reconfigure installation.

### Application Entity (AE) Titles Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes both the calling and called Application Entity (AE) Titles that must both be configured for DICOM SCP to work. It is necessary to configure both the AE Titles on the CVIX server with those of the DICOM SCP client and also to configure the AE Titles on the DICOM SCP client with those of the CVIX server.

> **NOTE:** The port for the DICOM SCP client where the DICOM SCP is used must be configured as a bi-directional open port in any firewall.

### Laurel Bridge AE Titles Configuration on CVIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The mapping of external AE Titles to TCP/IP addresses and ports is configurable and set at the time of installation by installation/administration personnel on the CVIX server. This mapping is necessary for resolving the IP address and port of C-MOVE Destination AE and must be correctly configured for the Laurel Bridge SCP AE to correctly function as a C-MOVE SCP.

> **NOTE:** The configuration is set for use with NilRead™ based on the server type (i.e., test or production) during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise, leave them as they are.

This section describes how to configure the AE Title file ae_title_mappings located in the folders cfg\dicom within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg\dicom by default).

Open the ae_title_mappings file to perform edits. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file.

For each DICOM SCP client, the AE Title name and its host/port attributes must be set. For each DICOM SCP client, update the following entries for the AE Titles configuration file (refer to Figure 7 for line numbers):

1.  Set the IP address for the host for the DICOM SCP client (after host = - line 7).
26. Set the port for the DICOM SCP ad client where the DICOM SCP is used for the C-STORE operation (after port = - line 8).
27. Set the AE title the DICOM SCP client is using to communicate with the DICOM SCP (calling AE) (inside \[ \] - line 6 and after ae_title = - line 9).

Ensure that each of the updated lines is uncommented (i.e., remove the \# at the front of the line if present). Save the ae_title_mappings file after updating the entries.

<span id="_Ref70085061" class="anchor"></span>Figure 7: AE Titles Configuration File (Template)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/012.png)

A more specific example using NilRead™ with some AE Titles filled in is shown in Figure 8. This example is for illustrative purposes only.

<span id="_Ref118113652" class="anchor"></span>Figure 8: AE Titles Configuration File (Example)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/013.png)

After updating the ae_title_mappings file, as described above, it is necessary to restart the Apache Tomcat service. One way this can be performed is by executing the restart script (Restart_VIX_Services.ps1) as described in the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105).

### AE Titles Configuration on DICOM Service Class User (SCU) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the AE Titles configuration on the AE Titles on the DICOM Service Class User (SCU). Installation/administration personnel on the CVIX server may not be able to perform this configuration and instead must provide the necessary information to the DICOM SCU administration personnel to perform.

The following three pieces of information are needed for the configuration of the DICOM SCU Client: 1) the IP address for the host for the CVIX server, 2) the port of DICOM SCP on the CVIX server, and 3) the AE Title of DICOM SCP (called AE).

Many different DICOM SCU client vendors exist and each of these systems has its own distinct approach to configuration. If additional information regarding specifics of configuring the DICOM SCU client is needed, please reach out to its vendor or consult its documentation.

### Tomcat DICOM SCP Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides details on the ScpConfiguration.Config file located in C:\VixConfig. To update access and verify codes for the account with VistA credentials, plain text versions can be entered directly into the configuration file and are encrypted after restarting the Apache Tomcat service. The access and verify codes can also be updated in the configuration file with a reconfigure installation described see the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105) or use the ImagingUtilities-0.1.jar in C:\VixConfig\Encryption to assist with generating encrypted forms of plain text access and verify codes.

> **NOTE:** Tomcat hosts the DICOM SCP, and the DICOM SCP uses the Laurel Bridge library. Refer to the *Laurel Bridge AE Titles Configuration on CVIX* to configure the ae_title_mappings file which contains the AE Title and port to trust for DICOM SCP.

The CVIX install performs some of the configuration for the DICOM SCP automatically with reasonable defaults and predefined entries. Update two entries in the ScpConfiguration.Config file located in C:\VixConfig to configure the DICOM SCP. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file.

Update the following entries for the DICOM SCP functionality (refer to Figure 9 for line numbers):

1.  Set the DICOM SCU calling AE title, inside opening and closing aeTitle tags (inside \<aeTitle\> \</aeTitle\> - line 22). Change the value from the default setting of ALL.
28. Set the DICOM SCU IP address inside the opening and closing callingAeIp tags (inside \< callingAeIp\> \</callingAeIp\> - line 23). Change the value from the default setting of 0.0.0.0.

<span id="_Ref95990230" class="anchor"></span>Figure 9: DICOM SCP Configuration File (Template)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/014.png)

An example of the ScpConfiguration.Config file with updates for NilRead™ is shown in Figure 10. This example is for illustrative purposes only.

<span id="_Ref95988667" class="anchor"></span>Figure 10: DICOM SCP Configuration File (Example)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/015.png)

Update the following entries for desired DICOM SCP functionality desired beyond the reasonable defaults that are pre-populated (refer to Figure 11 for line numbers):

1.  Set the access code for the account with VistA credentials (inside \<accessCode\> \</accessCode \> - line 3). A plain text version can be entered and will be encrypted after Tomcat restart.
2.  Set the verify code for the account with VistA credentials (inside \<verifyCode\> \</verifyCode \> - line 4). A plain text version can be entered and will be encrypted after Tomcat restart.
29. Set the entry for the maximum thread pool size for simultaneous VIX site fetching (inside \<siteFetchTPoolMax\> \</siteFetchTPoolMax\> - line 5). The default setting is to fetch from at most 20 VIX sites at the same time.
30. Set the entry for the maximum time to wait for fetching from the VIX site. If the thread does not finish within this maximum time the C-FIND will not count the studies from that VIX site in the response (inside \<siteFetchTimeLimit\> \</siteFetchTimeLimit\> - line 6). The fetching thread continues if it is not finished within the time limit. If the fetching is finally successful, the user may re-initiate the C-FIND search and the studies from that site will be counted. The default setting is set to 45 seconds. Depending on the DICOM SCU server settings, this setting may be adjusted to a time the DICOM SCU is willing to wait.
31. Set the entry for the maximum thread pool size for simultaneous image fetching through the local ImageWebApp (inside \<imageFetchTPoolMax\> \</imageFetchTPoolMax\> - line 7). The default setting is to fetch from at most 15 images at the same time.
32. Set the entry for the maximum time to wait for fetching the images. (inside \<imageFetchTimeLimit\> \</imageFetchTimeLimit\> - line 8). The default setting is set to 1,000,000 seconds. Since the default maximum time to wait for fetching the images is longer than one day, there is no effective limit due to the nightly server restart.
33. Set the value to true or false to use the remote image service (true) or the local image service (false) (inside \<useRemoteImageFetch\> \</useRemoteImageFetch\> - line 9). The default setting is set to true.
34. Set the value to true or false to use direct image fetch (inside \<useDirectFetch\> \</useDirectFetch \> - line 10). The default setting is set to true which retrieves the file paths for the images from the remote VistA and retrieves the images directly from the SMB storage. If set to false, direct image fetch is not used.
35. Each time a user makes a query for a patient (C-FIND), the query information (patient ID) and the study metadata is stored in memory cache for future reference by subsequent series queries and image retrieval (C-MOVE). Set the entry for the cache retention period of how long (in hours) this query information and study metadata is stored in memory (inside \<cacheLifespan\> \</cacheLifespan\> - line 11). If 0 is entered, the entries are kept indefinitely in memory or until the next Apache Tomcat service restart.
36. Set the value to true or false for if the C-FIND operation, when querying for studies, also caches the list of studies series metadata in the background (\<preFetchSeries\> \</preFetchSeries\>) - line 12.
37. If desired to set allowed AE Titles for the C-FIND caller called AE that it is calling, inside the opening and closing calledAETitle tags (line 13), insert the AE Title of DICOM SCP (called AE) followed by an underscore (\_) followed by the IP address for the host for the VIX server.
38. Set the entry for the maximum number of images able to be queued to download at once (inside \<imageQueueSize\> \</imageQueueSize\> - line 14). The default setting is to 10,000 images.
39. Set the entry for the number of hours cached metadata is considered valid (metadata older than this time can be overwritten) (inside \<cacheMetaHoursToLive\> \</cacheMetaHoursToLive\> - line 15). The default setting is to 24 hours.
40. If desired to enable fast data transfer set isFdtEnabled to true inside the opening and closing isFdtEnabled tags, otherwise set false (inside \<isFdtEnabled\> \</isFdtEnabled\> - line 16). The default setting is true.
41. If desired to change the port for fast data transfer set the port inside the opening and closing fdtPort tags (inside \<fdtPort\> \</fdtPort\> - line 17). The default port is 2762.

    NOTE: The selected port for fast data transfer must be visible to other VIX across the VA.
42. Set the parameter isGenRptFromImage to reference the first downloaded DICOM image for certain headers (set to true) or the equivalent data in VistA for the report (set to false) (inside \<isGenRptFromImage\> \</isGenRptFromImage\> - line 18). The default is true.
43. If desired to return patch 34 SOP class images from studies set useP34 to true inside the opening and closing useP34 tags, otherwise set false (inside \<useP34\> \</useP34\> - line 19). The default setting is true.
44. If desired to see the VA reports as Secondary Capture images, set buildReport to SC inside the opening and closing buildReport tags (inside \<buildReport\> \</buildReport \> - line 24). To see VA reports as Structured Reports, set buildReport to SR inside the opening and closing buildReport tags (inside \<buildReport\> \</buildReport \> - line 24). To turn off VA report generation, set buildReport to NONE inside the opening and closing buildReport tags (inside \<buildReport\> \</buildReport \> - line 24).
45. If desired to return study query level in C-FIND responses set returnQueryLevel to true inside the opening and closing returnQueryLevel tags, otherwise set false (inside \<returnQueryLevel\> \</ returnQueryLevel\> - line 25).
46. The default setting for studyQueryFilter is radiology inside the opening and closing studyQueryFilter tags (inside \<studyQueryFilter\> \</ studyQueryFilter \> - line 26).

    Radiology includes all DICOM exams with some exceptions. The setting for studyQueryFilter can be changed to all or one of the following specializations which are mapped to VA-specific modalities: cl_cardiology, cl_dermatology, cl_dicom, cl_dental, cl_eyecare, cl_other, and cl_radiology. All includes all exams regardless of their contents, though any exam without an associated Study Instance UID will automatically be excluded from the results. The specialization mappings are defined in DicomCategoryFilterConfiguration.config and can be updated if desired. The specialization mappings include: cl_cardiology filters for any cardiology related study modality, cl_dermatology filters for any dermatology related study modality, cl_dicom filters for any DICOM related study modality, cl_dental filters for any dental related study modality, cl_eyecare filters for any eyecare related study modality, cl_other filters for any other modality not included in other filters available, cl_radiology filters for any radiology related study modality.
47. If desired to not have actively serviced C-MOVE timeouts, set sendKeepAlive to true inside the opening and closing sendKeepAlive tags, otherwise set false (inside \<sendKeepAlive\> \</ sendKeepAlive \> - line 27). The default setting is false.
48. If desired to use concurrent C-STORE, set useMultiAssociations to true inside the opening and closing useMultiAssociations tags, otherwise set false (inside \<useMultiAssociations\> \</useMultiAssociations\> - line 28). The default setting is false.
49. Set the maximum number of concurrent C-STORE connections inside the opening and closing cstoreTPoolMax tags (inside \<cstoreTPoolMax\> \</cstoreTPoolMax\> - line 29).
50. If desired to query patient identifiers unknown to the local VistA set remotePatientResolution to true inside the opening and closing remotePatientResolution tags, otherwise set false (inside \< remotePatientResolution\> \</ remotePatientResolution\> - line 30). The default setting is false. When true the VIX will fall back to querying CVIX with any patient identifiers it receives that cannot be resolved locally.
51. If desired to not fetch certain modality images, set the entries inside the opening and closing modalityBlockList tags for different dataSources.
1.  For each dataSource (DoD or VA), set different modality lists, if necessary, by inserting DoD or VA inside the opening and closing dataSource tags (\<dataSource\> \</dataSource\> - line 33), by default the value is ALL.
2.  The modalities will be filtered at study and series levels. If needed, set at the image level. To do so, set true at the image level when needed by inserting true inside the opening and closing addImageLevelFilter tags, otherwise set false (\<addImageLevelFilter\> \</addImageLevelFilter\> - line 34).
3.  List all the modalities to be blocked for that dataSource separately using string tags inside the opening and closing modalities section (\<modalities\> \</modalities\> - lines 35 and 37). Examples of modalities to potentially include inside the string tags include SR and PR.
52. The installer automatically generates a default blacklist consisting of site codes that configured DICOM SCUs do not receive data from. Your local site code and the site codes of your Veterans Integrated Service Network (VISN) appear in the \<siteCodeBlackList\> section in the file ScpConfiguration.config located in the C:\VixConfig folder. If you want your site’s data to be available to the configured DICOM SCU, ensure your local site code is not in the \<siteCodeBlackList\> section in the ScpConfiguration.config. List all the site codes to be blocked separately using string tags inside the opening and closing siteCodeBlackList section (\<siteCodeBlackList \> \</siteCodeBlackList \> - lines 40 and 46). Examples of site codes to include inside the string tags include the following:
1.  Set a string to 100 to exclude Claims system information.
2.  Set a string tag to 200CLMS to exclude 200 VHA Claims study information.
3.  Set a string tag to 200CORP to exclude the Claims site.
4.  Set a string tag to 741 to exclude Global Disability Examinations.
5.  Set a string tag to LOCAL to signal the DICOM Service to replace it with the local site number and all of the sites in that Veterans Integrated Service Networks (VISN).

    NOTE: If desired to exclude DoD studies information, set a string tag to 200 inside the opening and closing siteCodeBlackList section (\<siteCodeBlackList \> \</siteCodeBlackList\>.
53. List all the SOP class UIDs codes that will not be sent when processing C-MOVEs for studies containing DICOM files of this type to the parent calling AE title using string tags inside the opening and closing sopClassBlackList section (\<sopClassBlackList\> \</sopClassBlackList\> - lines 46 and 48). Examples of SOP class UIDs to include inside the string tags include the following:
1.  Set a string to 1.2.840.10008.5.1.4.1.1.66 to exclude Raw data.

Save the ScpConfiguration.Config file after updating the entries. After updating the DICOM SCP config file, the ScpConfiguration.Config file will look like (Figure 11):

<span id="_Ref69388265" class="anchor"></span>Figure 11: DICOM SCP Configuration File (Example)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/016.png)

For additional DICOM SCU calling AE titles, insert an additional block of code containing the elements from lines 21 to 49 before current line 50 and then repeat steps 1 to 27 inside these additional lines that have been added, see Figure 12.

<span id="_Ref90914075" class="anchor"></span>Figure 12: DICOM SCP Configuration File with Multiple DICOM SCU Calling AE Titles (Example)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/017.png)

After updating the ScpConfiguration.Config file, as described above, it is necessary to restart the Apache Tomcat service. One way this can be performed is by executing the restart script (Restart_VIX_Services.ps1) as described in the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105).

### Laurel Bridge DICOM SCP Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides details on the Laurel Bridge DICOM file located in the cfg folder within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg by default) are desired. This is useful for debugging purposes but the details on how to change this are beyond the scope of this document. For typical CVIX operation, no changes are necessary to the Laurel Bridge DICOM file.

Open the DicomScpConfig file to perform edits. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file. Numerous entries can be updated in the DicomScpConfig configuration file (Figure 13). Save the DicomScpConfig file after updating the entries.

<span id="_Ref72232899" class="anchor"></span>Figure 13: DicomScpConfig Configuration File (Template)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/018.png)

After updating the DicomScpConfig file, as described above, it is necessary to restart the Apache Tomcat service. One way this can be performed is by executing the restart script (Restart_VIX_Services.ps1) as described in the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105).

## Configure ID Conversion 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Id Conversion Configuration calls VA’s Master Veteran Index (MVI) to do the ID Conversion from ICN to Electronic Data Interchange Personal Identifier (EDIPI) or from EDIPI to ICN. On CVIX, ECIA needs this functionality. On CVIX, DICOM SCP also needs this functionality.

Perform this step to further configure the CVIX collection of DoD medical images to ECIA via the IdConversionConfiguration.config file which configures the destination of the ID conversion lookup.

> **NOTE:** Before moving forward with the instructions for this step, it is expected that the site administrator is aware of all needed entries in the configuration, including the \<protocol\>, \</host\>, \<port\>, \<username\>, and \<password\> of the ID lookup.

> **NOTE:** Some of the configuration including \<host\>, \<username\>, and \<password\> may be set based on the server type (i.e., test or production) during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise, leave them as they are.

Open the IdConversionConfiguration.config in C:\VixConfig. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file.

To configure the ID lookup (refer Figure 14 to for line numbers):

1.  Set the protocol for the destination of ID conversion lookup (inside \<protocol\> \</ protocol\> - line 3).
54. Set the entry for the host for the destination of ID conversion lookup (inside \<host\> \</host\> - line 4).
55. Set the port for the destination of ID conversion lookup (inside \<port\> \</ port \> - line 5).
56. Set the urlResource for the destination of ID conversion lookup (inside \<urlResource\> \</ urlResource\> - line 6) (only if a change is needed).
57. Set the username for the destination of ID conversion lookup (inside \<username\> \</username \> - line 7).
58. Set the password for the destination of ID conversion lookup (inside \<password \> \</password \> - line 8).
59. Set the trustStoreFilePath (inside \<trustStoreFilePath\> \</trustStoreFilePath\> - line 9) (only if a change is needed).
60. Set the trustStorePassword (inside \<trustStorePassword\> \</trustStorePassword\> - line 10) (only if a change is needed).

Save the IdConversionConfiguration.config file after updating the entries. The IdConversionConfiguration.config should look like Figure 14.

<span id="_Ref48826512" class="anchor"></span>Figure 14: IdConversionConfiguration.config file (Template)

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/019.png)

# VistA Site Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section covers:

- VistA Site Service Overview
- Checking the Site Service
- Updating Site Service Data

## VistA Site Service Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Site Service is a central repository of connection information. Several Imaging components use the data stored in the site service to connect to Imaging components at other sites, remote VistA systems, and the CVIX.

Because the site service is centralized, Imaging components (such as a VIX or a Clinical Display workstation) at each VA site can use the site service’s connection information without having to locally store and maintain any connection information.

When data is requested from the site service, the request goes to the CVIX’s active load balancer. The load balancer passes the request to a node in the CVIX cluster, and that node retrieves the requested connection information from the site service primary configuration file ([<u>C:\VixConfig\VhaSites.xml</u>](file:///C:/VixConfig/VhaSites.xml)). Then the connection information is passed back to the load balancer and ultimately back to the requestor.

The following sections explain how to check and maintain the site service.

## Checking the Site Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access a listing of what is in the site service, use a browser to go to <span class="mark">REDACTED</span>.

The page that displays list the connection information for all sites registered in the site service. Sites are grouped by VISN (Veterans Integrated Service Network) name.

Additional non-VISN sites are listed at the bottom of the page.

## Updating Site Service Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the connection information in the site service needs to be changed, do the following.

1.  Identify the specific information that needs to be changed. Typically, this will be received in an email directed to the <span class="mark">REDACTED</span> mail group.
61. Use ping or a similar command to verify that the information is correct.
62. Create an offline copy of the VhaSites.xml file. An instance of this file is stored in the [<u>C:\VixConfig</u>](file:///C:/VixConfig) folder on each CVIX node.
63. In the offline copy of VhaSites.xml, locate and update the applicable information.
64. On each CVIX server node, copy the modified VhaSites.xml file to the following folders (the CVIX can remain active during this activity):
- [<u>C:\VixConfig</u>](file:///C:/VixConfig)
- [<u>C:\SiteService</u>](file:///C:/SiteService)
65. For each CVIX node, refresh its cached site service connection information by doing the following:
6.  Use a browser to go to <u>[http://xxx/Vix/secure/SiteService.jsp](http://where),</u> where \<xxx\> is the name of the CVIX node.
4.  In the Site Service Utilities web, click the Refresh Site Service button.
66. Notify the originators of the request that the site service has been updated, and work with them to ensure the new connection information works as expected.

> **NOTE:** A site VIX will not pick up the revised site information until it is restarted or until the VIX automatically updates its cached connection information at 11:00 P.M. daily.

# CVIX Image Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX is a key link in VA-DoD image exchange and is the primary source of information for the JLV. A functional description of the CVIX’s image-sharing capabilities is covered in *CVIX Major Functions*. This section covers:

- Remote Metadata Retrieval
- Remote Image Retrieval
- Caching of Metadata and Images
- Image Sharing and CVIX Timeouts

## Remote Metadata Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an application requests images via a CVIX, the process usually takes two steps: metadata retrieval and then retrieval of the actual image.

> **NOTE:** In the context of the CVIX, metadata is anything that describes an image or image-like object. Metadata includes patient names, IDs of various types, procedure names, the number of images in an exam, and so on.

In some cases, metadata retrieval is the only action needed to fulfill a clinician’s data request. One example of this is the retrieval of an exam report. Also, in some cases (such as a request for a patient ID image by the JLV), an image request may not require a preliminary metadata request.

The CVIX handles metadata retrievals as follows:

1.  An application issues a request for metadata based on a clinician’s activities. The applications in Table 9 can request metadata from the CVIX.

| Requesting Application                                             | Type of metadata requested                        | CVIX interface used by requestor\*\* | Ultimate source of requested metadata                                                     |
|--------------------------------------------------------------------|---------------------------------------------------|--------------------------------------|-------------------------------------------------------------------------------------------|
| VIX (on behalf of JLV, Clinical Display or VistARad, Image Viewer) | DoD metadata for all DoD image/artifact types     | Federation                           | ECIA for DICOM-related metadata or DES via DAS for artifact-related metadata (through DX) |
| DAS                                                                | VA metadata related to DICOM images and artifacts | MIX, AX                              | VIX at VA site if VIX is available. VistA at VA site if VIX is not available              |

<span id="_Ref52886241" class="anchor"></span>Table 10: VIX Image Quality Parameters

> **NOTE:** See *CVIX Interfaces* for more information about CVIX interfaces.

67. If the CVIX is processing a request from the DAS, the CVIX uses the VistA system at Station 200 to determine where in the VA the applicable patient was treated.
68. The CVIX retrieves metadata in the most expeditious manner possible:
- If caching is allowed for the metadata in question, the CVIX checks its local cache for the metadata.
- If caching is not allowed or the metadata is not in the CVIX cache, the CVIX contacts the remote system where the metadata is stored and retrieves the metadata (see the right column in Table 9).

The CVIX passes the data back to the requesting application.

## Remote Image Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a CVIX gets a request for an image, the CVIX uses the following process to deliver the most desirable image in the shortest amount of time. Typically, an image request is preceded by a metadata request, as described in the previous section.

1.  One of the following applications requests a remote image based on a clinician’s activities:
- DAS (from HAIMS) on behalf of a DoD clinician (VA DICOM images).
- DAS (from DES) on behalf of a DoD clinician (VA non-DICOM images).
- Clinical Display, VistARad, or VA JLV on behalf of a VA clinician (DoD images).
- DoD users of JLV, requesting VA artifacts via DES and DAS
- Image Viewer on behalf of a VA clinician (VA images).
69. The CVIX first checks its local cache for the image.
- If the image is in the local CVIX cache and is of the desired quality and is in any of the acceptable formats, the CVIX stops the search and proceeds to step 5.
- If the image is not stored in the local CVIX cache, the CVIX checks the SQLite database if the item is stored in the cluster of CVIX nodes and if an entry is found, the CVIX contacts the node fetches the data, and proceeds with step 5. Otherwise, the CVIX retrieves the image from its source.
70. Depending on the image quality specified by the requestor, the image may be compressed at this point.
- If the image originates from the VA, a VIX may perform the compression if a VIX is present at the originating site. If no VIX is present, the CVIX performs the compression if compression is applicable.
- If the image originates from the DoD, the CVIX does not perform any compression before sending the image to the requestor. (In the case of DICOM images requested by VistARad via a VIX, the images are already compressed and will be decompressed by the VIX).
- Possible image quality parameters are described in Table 10.

| Parameter               | Compression                                                                                                                                                                                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DIAGNOSTIC UNCOMPRESSED | None. Used for objects that will be sent in their native formats such as TIF or PDFs. This parameter will be used by the CVIX when requesting full-fidelity non-radiology images from a VA site with a VIX.                                                          |
| DIAGNOSTIC              | Lossless compression; typically used for DICOM (radiology) images. The highest-resolution available image is located and compressed. The typical compression ratio is about 2.5:1. Any image requestor can use this parameter.                                       |
| REFERENCE               | Lossy compression; typically used for DICOM (radiology) images. The highest-resolution available image is located and compressed. The compression ratio averages about 24:1 for CR images and 10:1 for CT and MR images. Any image requestor can use this parameter. |

<span id="_Ref52886587" class="anchor"></span>Table 11: Image Data Retention Periods

71. The CVIX caches the image in its local cache. If the CVIX compressed the image, the compressed version is cached, not the original version.
72. The CVIX sends the image to the requesting system.

## Caching of Metadata and Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX automatically stores all images and most of the metadata it handles in its local cache. The local CVIX cache is self-managing and is independent of other Imaging storage areas and caches.

The CVIX cache improves the CVIX’s performance by storing data (especially images) retrieved from remote sites and/or processed by the CVIX. If the image is requested again, it can be pulled from the CVIX’s cache or from another CVIX cluster node (when the Cache Cluster option is enabled) without having to retrieve it from the remote site or reprocess it.

> **NOTE:** Metadata and images cached by the CVIX are considered transitory copies and are not a part of the patient record. The site from which the data originates is the official custodian of the data, not the CVIX.

### Cache Retention Periods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX purges data from its cache when the retention period for the data is reached. Images are considered static data that allow longer cache retention while retaining data consistency. Metadata, which is less static, is retained for shorter periods.

Table 11 lists retention periods based on the source and type of data.

| Data type                     | Retained for | Scan to delete old items is run |
|-------------------------------|--------------|---------------------------------|
| VA and DoD images             | 7 / 30 days  | Once per day at 3 AM            |
| VA metadata                   | 1 hour       | Once per minute                 |
| DoD metadata                  | 1 day        | Once per hour                   |
| DICOM SCP images and metadata | 30 days      | Once per minute                 |

<span id="_Ref53561667" class="anchor"></span>Table 12: CVIX Connection Timeout Parameters

### Cache Location and Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX cache is located in [<u>x:\VixCache</u>](file:///x:/VixCache) on each node in the CVIX load-balanced cluster, where x is usually the E drive.

The CVIX cache is divided into regions based on the source and type of data being handled. These regions are reflected in the folder structure of the cache (Figure 15).

<span id="_Ref53560780" class="anchor"></span>Figure 15: CVIX Folder Structure

> ![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/020.png)

Subfolders for each region are further broken down by STATION NUMBER (field (#99) of the INSTITUTION file (#4)) and then by internal ID numbers. Internal ID numbers do not trace back to live data such as SSNs or case IDs.

> **NOTE:** Never manually change the contents of the VixCache folder and subfolders while the CVIX is running.

## Image Sharing and CVIX Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the CVIX retrieves metadata and images from remote sites, the system load at the remote site and Wide Access Network (WAN) network traffic will impact the time needed to complete the retrieval. If a request for data cannot be completed promptly, the CVIX will cancel its request. This prevents excessive delays in client applications that are the ultimate consumers of the metadata and images.

Table 12 summarizes CVIX connection timeout parameters based on the type of remote system and data involved.

<table>
<caption><p><span id="_Ref52955032" class="anchor"></span>Table 13: CVIX Interfaces</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>Remote System Type</th>
<th>CVIX Timeout Behavior</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA data via a remote VIX</td>
<td><p>For metadata, 600 seconds for data transfer to begin (this is to handle very large datasets; usually, the data transfer begins in a few seconds).</p>
<p>For images, wait up to 30 seconds for the initial connection and up to 120 seconds for data transfer to begin.</p></td>
</tr>
<tr class="even">
<td>VA data from a remote non-VIX VA site</td>
<td><p>For metadata, no timeout.</p>
<p>For images, N/A because the local VIX only starts the operation if it can connect to the remote site and can verify that the remote image is present.</p></td>
</tr>
<tr class="odd">
<td>DoD data</td>
<td>For metadata, the CVIX will wait up to 45 seconds to retrieve DoD metadata before sending a timeout message to the VIX that requested the data. For images, the CVIX will wait up to 30 seconds for the initial connection with the DoD image source, and up to 120 seconds for the image transfer to begin. If the CVIX is able to retrieve data from some DoD sources but not all of them, the CVIX will pass a partial response message to the VIX that originally requested the data.</td>
</tr>
</tbody>
</table>

<span id="_Ref52955032" class="anchor"></span>Table 13: CVIX Interfaces

# VIX Log Collector Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section covers:

- VIX Log Collector Overview
- Log Collector Automatic Emails
- Archived Transaction Log Storage Area
- Excluding a VIX from Log Collection

## VIX Log Collector Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Log Collector automatically backs up transaction logs from remote VIXes and from the CVIX. This allows the information in VIX transaction logs to be retained after local logs are purged (the standard local retention period is 90 days).

Once a day, the Log Collector uses the VistA site service to retrieve connection information for all remote VIXes and the CVIX. The Log Collector then collects one full day’s worth of transaction log entries from each VIX (and the CVIX). To ensure that all entries are captured for a given day, the Log Collector pulls entries that are at least 48 hours old. For example: on Monday, the Log Collector service will collect all VIX log entries from the previous Saturday. Logs are collected at 5:30 A.M.

In general, the Log Collection service does not need to be monitored.

- If the Log Collector cannot reach a VIX on a given day, it will queue its backup attempt and attempt to copy any backlogged items during the next backup period.
- If the CVIX failover cluster is rebooted, the Log Collector restarts automatically.

To manually verify that the Log Collector is gathering logs as expected, check the storage area <span class="mark">REDACTED</span> for collected logs for newly backed up files. For specifics, see the *Archived Transaction Log Storage Area*.

## Log Collector Automatic Emails

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Log Collector has any errors over a day, these errors are summarized into an email and sent to specified addressees each day at 7:30 A.M. The email subject line is always “Log Collection Errors.”

Email addresses are initially specified when the Log Collector service is installed. To change the email recipient, use the following steps:

1.  Login as an administrator to the active server.
73. Navigate to C:\Program Files (86)\VistA\Imaging\VixLogCollectorService.
74. Open the file named VixLogCollector.WindowsService.exe.config in a text editor.
75. Locate the “emailAddress” key near the beginning of the file.
76. Edit the value for the emailAddress key as needed. Separate each email address with a comma.
77. Save and close the file.
78. Open the Services window (click Start \| All Programs \| Administrative Tools \| Services).
79. On the right side of the window, locate the VIX Log Collector service.
80. Click the <u>Restart</u> the service link and wait until the service restarts.

## Archived Transaction Log Storage Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The archived transaction log files gathered by the Log Collector are stored under <u>G:\VIXLogs</u> on the failover cluster (Figure 16). The folder structure is set up as follows:

[<u>G:\VIXLogs\\</u>](file:///G:/VIXLogs/)*site*\\*year*\\*month*

...where *site* is the station number of the site where the log came from, and *year* and *month* indicate when the log was collected. In each *month* folder, each day’s worth of transaction log entries for a specific VIX (or CVIX) is stored in a separate tab-separated file.

<span id="_Ref53560872" class="anchor"></span>Figure 16: Transaction Log File Display Example

> ![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/021.png)

> **NOTE:** Only logs more than 48 hours old are archived. A subfolder for the current month will not be created until the third day of the current month.

The month-specific folders in this structure are compressed using standard Windows compression.

## Excluding a VIX from Log Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following steps to disable the automatic collection of transaction logs from a specific VIX or CVIX:

1.  Determine the ID number of the VIX or CVIX for which log collection is to be disabled.
- For a site VIX, this is the STATION NUMBER (field (#99) of the INSTITUTION file (#4) of the site where the VIX resides.
- For the CVIX, this value will be 2001.
81. Login as an administrator to the active server.
82. Navigate to where the archive logs are stored ([<u>E:\VixLogs</u>](file:///E:/VixLogs) is the default location).
83. Open the folder of the VIX (or CVIX) to disable it.
84. Use a text editor to open the VixInfo.xml file.
85. Locate the IsActive element and change the element value from “true” to “false”.
86. Save and close the file.

# CVIX Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section covers:

- Routine Errors
- Significant Errors
- Unplanned Shutdowns
- CVIX Support Routine Errors

## Routine Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system may generate a small set of errors that may be considered routine in the sense that they have minimal impact on the user and do not compromise the operational state of the system. Most of the errors are transient and only require the user to retry an operation. The following subsections describe these errors, their causes, and what, if any, response an operator needs to take.

While the occasional occurrence of these errors may be routine, a large number of errors over a short period is an indication of a more serious problem. In that case, many errors need to be treated as an exceptional condition.

### Connectivity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasional data retrieval failures are expected given the nature of the Wide Area Network (WAN) and the number of systems communicating with the VIX.

### Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX will cancel a data request if it does not get a response from the system in question. For specific timeout information, see *Image Sharing and CVIX Timeouts*.

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the system is a component of a larger system that is responsible for user-level security, it is expected that all errors related to security are handled by the controlling application. All security failures (e.g., inability to access resources or stored objects) are generally caused by the controlling application either incorrectly passing security tokens or failing user authentication. Other security issues are under the jurisdiction of the site VistA Imaging security which has already established protocols and procedures.

If DoD clinicians cannot access any VA images and if Station 200 appears to be available, check the credentials for the CVIX USER service account on Station 200 to ensure that it has not expired. If VA clinicians cannot access DoD artifacts (scanned documents and non-radiology) images, the issue may be the authentication at DAS.

### Station 200 Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there is a temporary Station 200 VistA System outage, the CVIX will automatically refresh any previously cached connections within 30 seconds to 1 minute after Station 200 comes back online. DoD clinicians may have to repeat their most recent image requests, but any issues encountered should be transitory.

If there is an extended Station 200 outage, DoD clinicians will not be able to access VA images for VA/DoD shared patients. VA clinicians/ VBA connecting to CVIX will also be impacted.

If DoD clinicians cannot access any VA images and if Station 200 appears to be available, check the credentials for the CVIX USER service account on Station 200 to ensure that they have not expired.

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors can be defined as errors or conditions that affect the system's stability, availability, performance, or otherwise make the system unavailable to its user base. The following subsections contain information to aid administrators, operators, and other support personnel in resolving significant errors, conditions, or other issues.

### Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX transaction log is the first place to check for errors related to data retrieval. The CVIX transaction logs include unique transaction IDs that can be used to track related actions across other systems (such as other VIXes).

> **NOTE:** Because the CVIX is set up as a load-balanced cluster without server affinity, check multiple CVIX nodes to see all log entries related to a given transaction (that is, receipt and fulfillment of a specific data request).

For detailed information about the transaction log, see *CVIX Transaction Log Fields*.  
For information about the CVIX’s Java logs, see *CVIX Java Components*.

## Unplanned Shutdowns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Recovering after unplanned restart of a single CVIX server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a single server in the CVIX cluster has an unscheduled restart, the request that it was actively processing at the time will fail. However, as soon as the server restarts, the CVIX service will also restart, and processing will continue as normal.

If the CVIX service on a single cluster node encounters a fatal error, the CVIX service will restart itself automatically after 60 seconds and continue restarting itself if it encounters additional errors.

If a specific cluster node needs to be taken offline, use the steps in *CVIX cluster: take the node offline*.

### Recovering after unplanned reboot of a single load balancer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a load balancer shuts down unexpectedly, the second load balancer will automatically begin handling CVIX operations. Let the second load balancer retain the active role if this occurs.

### Recovering after an unscheduled power loss to all components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Startup the CVIX as described in *Planned Full CVIX Startup* and issue an ANR describing the nature of the outage and its resolution time.

Closely monitor CVIX operations until normal operations are verified.

## System Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections define the process and procedures necessary to back-out and rollback the system to a fully operational state after a service interruption. Each of the subsections starts at a specific system state and ends up with a fully operational system.

### Back-out Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the MAG\*3.0\*358 CVIX must be uninstalled, go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*358 CVIX Service Installation Wizard. To backout the CVIX and replace it with the prior version which was included in MAG\*3.0\*367 (which is installed on top of MAG\*3.0\*348), please see the [*MAG\*3.0\*<u>358</u> CVIX Installation Guide*](https://www.va.gov/vdl/application.asp?appid=105) for more detail.

### Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the MAG\*3.0\*358 CVIX must be uninstalled, go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*358 CVIX Service Installation Wizard. To backout the CVIX and replace it with the prior version which was included in MAG\*3.0\*367 (which is installed on top of MAG\*3.0\*348), please see the [*MAG\*3.0\*<u>358</u> CVIX Installation Guide*](https://www.va.gov/vdl/application.asp?appid=105) for more detail.

## CVIX Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problems encountered with the CVIX that are not addressed in this document will require the entry of a Service Now Ticket for VistA Imaging/CVIX Support.

Contact the VA IT DAS Technical mail group at <span class="mark">REDACTED</span> for ongoing connectivity issues with DAS. If there is a CVIX outage, contact the National Help Desk at <span class="mark">REDACTED</span>.

# CVIX Reference/Software Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CVIX Java Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections summarize the CVIX’s primary Java components.

### CVIX Servlet Container

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX uses an Apache Tomcat-based servlet container to provide the environment used to execute the CVIX’s Java code. This servlet container is installed automatically as part of the CVIX installation process.

### CVIX Security Realms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX implements security realms to verify that only properly authenticated applications (the site VIXes, and DoD systems) can use the CVIX Web applications' interfaces. Authentication is handled silently by the application and the CVIX and does not require an explicit login by clinicians requesting images. See *CVIX Connection Security* for more information.

### CVIX Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX uses a dedicated interface for each outside application that requests and receives data from the CVIX.

CVIX interfaces are used both for metadata and image retrieval. In general, each CVIX interface implements a Web service that handles metadata requests and an image servlet that handles image requests. Table 13 summarizes each CVIX interface.

| Interface Name       | Description                                                                                                                                                        |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DICOM SCU            | Handles DICOM metadata and image requests from DoD providers via CVIX. Uses port <span class="mark">REDACTED</span> with the specified application entities (AEs). |
| Federation interface | Handles metadata and image requests from site VIXes; uses port <span class="mark">REDACTED</span>.                                                                 |
| DX                   | Handles non-DICOM metadata and image requests from CVIX to HAIMS and DES via DAS. Uses port REDACTED.                                                              |
| Image Viewer         | Provides Viewing images and retrieving metadata for consuming applications (JLV and C/VIX)                                                                         |

<span id="_Ref52955232" class="anchor"></span>Table 14: CVIX Data Sources

When an interface receives a request, it issues the appropriate command to the CVIX core (described in the next section) for proper disposition. When the CVIX core ultimately responds (the requested data), the same interface responds to the requesting application.

### CVIX Core

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX core provides the central switching intelligence for the CVIX. It:

- Examines commands received from all the CVIX interfaces.
- Determines which CVIX data source is the best to retrieve the data requested and packages the request appropriately before passing the request to the data source.
- Implements and manages the CVIX cache.

### CVIX Data Sources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX has a dedicated data source for each outside entity that it retrieves data from. Data sources receive requests from and return responses to the CVIX core. Table 14 summarizes each CVIX data source. These data sources are identified in the Datasource Protocol field in the CVIX transaction log.

| Data Source Name | Description                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vistaimaging     | Retrieves data from a VistA Imaging System using RPCs.                                                                                                       |
| vista            | Retrieves data from a VistA system without Imaging using RPCs. The CVIX currently uses this data source for communicating with the Station 200 VistA system. |
| vftp             | Retrieves data from other VIXes (or the CVIX) using their Federation interfaces.                                                                             |
| FHIR             | Retrieves non-DICOM metadata from DAS and non-DICOM images from DES via DAS servers.                                                                         |
| ECIA             | Retrieves metadata and DICOM images.                                                                                                                         |

<span id="_Ref52955802" class="anchor"></span>Table 15: MAG (VistA Imaging) RPCs Used by the CVIX

## Java Installation Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the server where the CVIX is installed, CVIX-related files are stored in the locations described below.

### CVIX folders on the System Drive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following CVIX-related folders are on the system drive ([<u>C:\\</u>](file:///C:/)) of each CVIX node. Note that because the CVIX is a collection of services hosted in a servlet container, most CVIX-related files cannot be stored under \Program Files\VistA.

\DCF_RunTime_x64

Laurel Bridge DICOM Connectivity Framework (DCF) toolkit files.

\Program Files\Apache Software Foundation\Tomcat 9.0

Primary application area for the CVIX servlet engine and CVIX program files. Includes:

\bin – servlet engine executables and Aware JPEG2000 toolkit files

\conf – servlet engine configuration files

\lib – shared servlet engine files, CVIX core and data source files, and Aware JPEG2000 toolkit files

\logs – Java and debugging logs

\temp – temporary files

\webapps – CVIX Web applications and associated parameter files

\work – servlet engine system files

\Program Files\Java\jre-1.8-431

The runtime environment files and resources for the CVIX servlet engine and CVIX Java components.

\VixCertStore

Stores CVIX security certificates. For details about security certificates, see the *CVIX Security Certificates.*\VixCache

The primary storage area for images and metadata that the CVIX caches. For details about the CVIX cache, see *Caching of Metadata and Images*.

\VixConfig

Configuration files are used by the CVIX Java components and the CVIX transaction log.

> **NOTE:** Files in the VixConfig folder are generated as part of the CVIX installation process and are regenerated when the CVIX is updated.

### Java Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The active Java logs reside in \Program Files\Apache Software Foundation\Tomcat 9.0\logs on each CVIX server. For active logs, a new instance is generated each day. For older logs, they are retained in the log archive folder named ImagingArchivedLogs with the corresponding drive letter specified during installation.

> **NOTE:** A symbolic link with the name ImagingArchivedLogsLink also resides in \Program Files\Apache Software Foundation\Tomcat 9.0\logs. This symbolic link points to the log archive folder named ImagingArchivedLogs with the corresponding drive letter specified during installation.

Older logs are retained with the date appended to their filenames in a zip format and stored in their respective archive folders. Further, older logs exceeding a pre-defined size (default 250 MB) for each day are rolled over and a new file is generated with a number appended to their filenames after the date.

catalina.log: Tomcat (CVIX servlet container) output.

host-manager.log: Java host manager application output.

ImagingCache.log: CVIX cache output.

ImagingExchangeWebApp.log: CVIX interface/web application output.

jakarta_service.log: Windows jakarta service output.

localhost.log: generated but not populated.

manager.log: generated but not populated.

stderr.log: Tomcat service errors.

VistaRealm.log: CVIX security realm output.

## VistA/M Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 15 describes the RPCs (Remote Procedure calls) that the CVIX uses when it retrieves data from remote VistA systems. The RPCs listed in these sections are only called when getting data from VA sites that do not have a VIX.

### RPCs used by the CVIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref53562091" class="anchor"></span>Table 16: Non-MAG RPCs used by the CVIX</p></caption>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>RPC Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>MAG BROKER SECURITY</strong></p>
<p>Routine: BSE^MAGS2BSE</p></td>
<td>Returns a BSE token from BSE XUS SET VISITOR.</td>
</tr>
<tr class="even">
<td><p><strong>MAG DOD GET STUDIES IEN</strong></p>
<p>Routine: STUDY2^MAGDQR21</p></td>
<td>Returns study information based on the IMAGE file (#2005) Internal Entry Number (IEN) of the image group provided as a parameter.</td>
</tr>
<tr class="odd">
<td><p><strong>MAG DOD GET STUDIES UID</strong></p>
<p>Routine: STUDY1^MAGDQR21</p></td>
<td>Returns study information based on the Study UID that is provided as a parameter.</td>
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
<td><p><strong>MAG4 PAT GET IMAGES</strong></p>
<p>Routine: PGI^MAGSIXG1</p></td>
<td>Returns a list of image groups from the IMAGE file (#2005) based on filters provided.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG CPRS RAD EXAM</strong></p>
<p>Routine: IMAGEC^MAGGTRAI</p></td>
<td>Returns a list of images for the radiology exam.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG GROUP IMAGES</strong></p>
<p>Routine: GROUP^MAGGTIG</p></td>
<td>Returns array of images for a group entry in the IMAGE file (#2005). Included for backward compatibility only.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG INSTALL</strong></p>
<p>Routine: GPACHX^MAGQBUT4</p></td>
<td>Returns a list of all Imaging package installs on the host system.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG LOGOFF</strong></p>
<p>Routine: LOGOFF^MAGGTAU</p></td>
<td>Tracks the time of the Imaging session.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG OFFLINE IMAGE</strong></p>
<p><strong>ACCESSED</strong></p>
<p>Routine: MAIL^MAGGTU3</p></td>
<td>Sends a message when there is an attempt to access image from an offline jukebox platter.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG PAT FIND</strong></p>
<p>Routine: FIND^MAGGTPT1</p></td>
<td>Used for patient lookups.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG PAT INFO</strong></p>
<p>Routine: INFO^MAGGTPT1</p></td>
<td>Returns a string of '^' delimited pieces of patient information.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG PAT PHOTOS</strong></p>
<p>Routine: PHOTOS^MAGGTIG</p></td>
<td>Returns a list of patient photo IDs.</td>
</tr>
<tr class="even">
<td><p><strong>MAGG SYS GLOBAL NODE</strong></p>
<p>Routine: MAG^MAGGTSY2</p></td>
<td>Returns the global node of an IMAGE file (#2005) entry.</td>
</tr>
<tr class="odd">
<td><p><strong>MAGG WRKS UPDATES</strong></p>
<p>Routine: UPD^MAGGTAU</p></td>
<td>Starts a new session for image access logging.</td>
</tr>
<tr class="even">
<td><p><strong>MAGGACTION LOG</strong></p>
<p>Routine: LOGACT^MAGGTU6</p></td>
<td>Call to log an action performed on the image. Actions are logged in the IMAGE ACCESS LOG file (#2006.95).</td>
</tr>
<tr class="odd">
<td><p><strong>MAGGRPT</strong></p>
<p>Routine: BRK^MAGGTRPT</p></td>
<td>Returns associated report for Image IEN.</td>
</tr>
<tr class="even">
<td><p><strong>MAGGUSER2</strong></p>
<p>Routine: USERINF2^MAGGTU3</p></td>
<td>Returns information about a Clinical Display user.</td>
</tr>
</tbody>
</table>

<span id="_Ref53562091" class="anchor"></span>Table 16: Non-MAG RPCs used by the CVIX

### Non-MAG RPCs used by the CVIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 16 shows the RPCs the CVIX uses from other VistA packages. The use of these RPCs is governed by Integration Control Registrations (ICRs) stored in FORUM. For information about viewing specific ICRs*.*

<table>
<caption><p><span id="_Ref53662194" class="anchor"></span>Table 17: Types of Support with Production Environment Location(s) as Appropriate</p></caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>RPC Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DDR FILER</strong></p>
<p>Routine: FILEC^DDR3</p></td>
<td>Generic call to file edits into a FileMan file.</td>
</tr>
<tr class="even">
<td><p><strong>DG SENSITIVE RECORD</strong></p>
<p><strong>ACCESS</strong></p>
<p>Routine: PTSEC^DGSEC4</p></td>
<td>Verifies that a user is not accessing his/her own Patient file record if the RESTRICT PATIENT RECORD ACCESS field (#1201) in the MAS PARAMETERS file (#43) is set to yes and the user does not hold the DG RECORD ACCESS security key. If the parameter is set to yes and the user is not a key holder, a social security number must be defined in the NEW PERSON file (#200) for the user to access any Patient file (#2) record.</td>
</tr>
<tr class="odd">
<td><p><strong>DG SENSITIVE RECORD</strong></p>
<p><strong>BULLETIN</strong></p>
<p>Routine: NOTICE^DGSEC4</p></td>
<td>Adds an entry to the DG Security Log file (#38.1) and generates the sensitive record access bulletin depending on the value in the ACTION input parameter.</td>
</tr>
<tr class="even">
<td><p><strong>VAFCTFU CONVERT ICN TO</strong></p>
<p><strong>DFN</strong></p>
<p>Routine: GETDFN^VAFCTFU1</p></td>
<td>Given a patient ICN, this will return the patient's IEN from the PATIENT file (#2).</td>
</tr>
<tr class="odd">
<td><p><strong>VAFCTFU GET TREATING LIST</strong></p>
<p>Routine: TFL^VAFCTFU1</p></td>
<td>Given a patient DFN, this will return a list of treating facilities.</td>
</tr>
<tr class="even">
<td><p><strong>XUS AV CODE</strong></p>
<p>Routine: VALIDAV^XUSRB</p></td>
<td>Checks to see whether an ACCESS/VERIFY code pair is valid.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS DIVISION GET</strong></p>
<p>Routine: DIVGET^XUSRB2</p></td>
<td>Returns a list of divisions of a user.</td>
</tr>
<tr class="even">
<td><p><strong>XUS DIVISION SET</strong></p>
<p>Routine: DIVSET^XUSRB2</p></td>
<td>Sets the user's selected division in Designated User (DUZ) (2) during sign-on.</td>
</tr>
<tr class="odd">
<td><p><strong>XUS ESSO VALIDATE</strong></p>
<p>Routine: ESSO^XUESSO4</p></td>
<td>Verifies that a provided IAM STS authentication token is valid.</td>
</tr>
<tr class="even">
<td><p><strong>XUS SIGNON SETUP</strong></p>
<p>Routine: SETUP^XUSRB</p></td>
<td>Establishes the environment necessary for DHCP sign-on.</td>
</tr>
<tr class="odd">
<td><p><strong>XWB CREATE CONTEXT</strong></p>
<p>Routine: CRCONTXT^XWBSEC</p></td>
<td>Establishes context on the server that the Broker will check before executing any other remote procedure.</td>
</tr>
<tr class="even">
<td><p><strong>XUS SET VISITOR</strong></p>
<p>Routine: SETVISIT^XUSBSE1</p></td>
<td>Returns a Broker Security Enhancement token to the CVIX.</td>
</tr>
<tr class="odd">
<td><p><strong>XWB GET VARIABLE VALUE</strong></p>
<p>Routine: VARVAL^XWBLIB</p></td>
<td>Accepts the name of a variable that will be evaluated, and its value returned to the server.</td>
</tr>
</tbody>
</table>

<span id="_Ref53662194" class="anchor"></span>Table 17: Types of Support with Production Environment Location(s) as Appropriate

### Database Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX retrieves data from VistA databases using the RPCs described in the previous sections.

The CVIX only writes data directly to remote VistA systems if the VA site does not have a VIX. At such non-VIX sites, the CVIX can make the following updates to the site’s VistA system:

- It can update the IMAGE ACCESS LOG file (#2006.95) to indicate remote image access. See *Logging on Remote VistA Systems* for details.
- It can update a site’s IMAGE file (#2005) with SOP instance UIDs for images that do not have SOP instance UIDs already. The CVIX uses the MAG NEW SOP INSTANCE UID RPC used by other Imaging components for the same purpose.

There are no general CVIX parameters stored on VistA; all parameters are set during installation and are stored in the CVIX’s local configuration files.

### Exported Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no exported VistA menu options associated with the CVIX.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are VistA security keys associated with the CVIX, see Sections 8.3.2, 11, and 12 for further details.

## Other VIX Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX incorporates the following additional components:

- Security certificates
- .NET
- Sun JRE
- Laurel Bridge DCF toolkit
- SQLite
- Aware JPEG2000 toolkit
- LibreOffice

Each component is described in the following sections. All of these components are integral to CVIX operations and cannot be modified without impacting CVIX operations.

### CVIX Security Certificates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a CVIX communicates with another VIX, with a DoD or other system (HAIMS, DES, DAS, ECIA, and so on), they exchange security certificates for authentication purposes. The CVIX’s long-term security certificates are stored in the \VixCertStore directory on each server where the CVIX is installed.

The CVIX security certificates are used in the CVIX installation process and must be available to complete a CVIX installation. VistA Imaging certificates are administered by the VistA Imaging development group. The other certificates needed by the CVIX to communicate with the DAS and HAIMS systems were provided by the teams administering each production system. Please refer to the separate CVIX Certificate_Maintenance.docx document for procedures to replace CVIX or partner system security certificates.

### .NET

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The .NET 4.8 framework is needed to install and update the CVIX software.

Other versions of .NET have no impact on the CVIX installer or update processes and can be installed or not in accordance with local policy.

### Java Runtime Environment (JRE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX’s servlet container and the CVIX itself requires Java Runtime Environment (JRE).

### Laurel Bridge DCF Toolkit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laurel Bridge DCF toolkit, version 3.3.68c, is a third-party toolkit that CVIX uses to convert images to and from DICOM format.

The license for this toolkit is tied to the servers where the CVIX is installed. Shifting to a new server will require an updated license from Laurel Bridge. If a new or updated license is needed, contact the <span class="mark">REDACTED</span> mail group.

### SQLite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX uses SQLite, a public domain database engine, to support the database for the CVIX cache. SQLite is a Structured Query Language (SQL) database that is completely self-managed. There are no site interactions required to maintain this database. The purpose of the database is to manage cached objects. The complete loss of this database is not a failure as it gets repopulated with each caching operation. The amount of data stored in the database and the cache is managed by the application based on available storage. No specific database errors are identified.

### Aware JPEG2000 Toolkit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Aware JPEG2000 toolkit is a third-party software development toolkit that the CVIX uses for image compression and decompression.

Use of this toolkit presumes that a one-time permanent license has been purchased from Aware. This license does not have to be explicitly installed and is transferable from one system to another.

This toolkit is bundled with the CVIX installer and is installed automatically as part of the VIX setup process. Do not install newer versions of the Aware JPEG2000 toolkit not bundled with the CVIX installer unless explicitly directed to do so by the Imaging development team.

### LibreOffice

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX requires the installation of LibreOffice 24.2.5, a third-party open-source office productivity software suite, to support Rich Text Format (RTF) files. The CVIX Installation automatically installs LibreOffice.

# Operations and Maintenance Responsibilities/RACI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The responsibility matrix in Table 17 defines the roles and responsibilities for supporting VistA patches as part of a deployed solution. This is a template of the standard support structure required for VistA patches; therefore, the Project Manager (PM) should note any deviations in responsibility from this standardized Field Operations responsibility matrix in the Operational Acceptance Plan (OAP).

VistA Patching is generally relegated to the sustainment of existing solutions but may also include emergency “hot fix” patches designed to remediate a noted deficiency within the solution. This Responsibility Matrix (Responsible, Accountable, Consulted, Informed, or RACI) is related to VistA patches released and supported at the national level (known as “Class I” patches), which are distributed to the entire Enterprise after testing and release management has been completed. VistA Patches are released via the FORUM, KERNEL, or via Secure File Transfer Protocol (SFTP) directly to the Field.

Entities involved with VistA Patching:

NSD = OI&T National Service Desk

FCIO = Facility Chief Information Officer

SL-ASL = OI&T Service Lines Application Service Line

SL-Core = Core Systems Service Line

PS = OI&T Product Support

VHA = Local Facility medical staff (customer)

FO = Field Operations

PD = OI&T Product Developer

DSO = VHA Decision Support Office

HPS = Health Product Support

| Support                                                        | Production Environments |
|----------------------------------------------------------------|-------------------------|
| Tier 1: NSD                                                    | N/A                     |
| Tier 2: (local OI&T – FCIO/SL-ASL)                             | PD                      |
| Tier 3: HPS                                                    | HPS                     |
| Tier 4: PD/Maintenance FO VistA Patching Responsibility Matrix | PD, FCIO/SL-ASL         |
| Application development                                        | NSD, FCIO, SL, HPS,     |
| Release Management                                             | Vendor                  |
| Rollback Plan                                                  | N/A                     |
| Application installation                                       | N/A                     |
| Application support                                            | N/A                     |
| Client/Server Update (where applicable)                        | SL-Core                 |
| OS Patching (where applicable)                                 | SL-Core                 |
| Change Management                                              | SL-ASL                  |
| Application Administration (Operations and Maintenance)        | SL-ASL                  |
| Local Training for Front Line Staff                            | VHA                     |
| National Training (where applicable)                           | DSO                     |

<span id="_Ref49956493" class="anchor"></span>Table 18: DICOM Modality Types Blocked at the VA if Originating from the DoD

# Appendix A: Image Sharing and DICOM Images

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Images are delivered to VA sites by the CVIX and originate from DAS framework for HAIMS or from ECIA.

## DoD DICOM Object Filtering

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Study information (including reports) for studies associated with all DICOM modality types can be retrieved from the DoD by VA sites.

However, for certain DICOM object types, the associated objects are not images, and Clinical Display and VistARad cannot display them. For these DICOM studies, metadata (including reports) is provided but not the image counts and/or image locations. The following DICOM modality types (Table 18) are blocked if the data originates from the DoD.

<table>
<caption><p><span id="_Ref95375929" class="anchor"></span>Table 19: List of URLs</p></caption>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>DICOM Modality Description</th>
<th>DICOM Identifier</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Audio</td>
<td>AU</td>
</tr>
<tr class="even">
<td><p>Document</p>
<p><em>(Used for DICOM encapsulated secondary captures and scanned documents. Not equivalent to MS Word .doc files )</em></p></td>
<td>DOC</td>
</tr>
<tr class="odd">
<td>Cardiac Electrophysiology (waveforms)</td>
<td>EPS</td>
</tr>
<tr class="even">
<td>Fiducials</td>
<td>FID</td>
</tr>
<tr class="odd">
<td>Hemodynamic Waveform</td>
<td>HD</td>
</tr>
<tr class="even">
<td>Key Object Selection</td>
<td>KO</td>
</tr>
<tr class="odd">
<td>MR Spectroscopy</td>
<td>MS</td>
</tr>
<tr class="even">
<td>Presentation State (all types)</td>
<td>PR</td>
</tr>
<tr class="odd">
<td>Respiratory Waveform</td>
<td>RESP</td>
</tr>
<tr class="even">
<td>Radiotherapy Structure Set</td>
<td>RTSTRUCT</td>
</tr>
<tr class="odd">
<td>RT Treatment Record</td>
<td>RTRECORD</td>
</tr>
<tr class="even">
<td>Radiotherapy Dose</td>
<td>RTDOSE</td>
</tr>
<tr class="odd">
<td>Radiotherapy Plan</td>
<td>RTPLAN</td>
</tr>
</tbody>
</table>

<span id="_Ref95375929" class="anchor"></span>Table 19: List of URLs

VistARad does not support displaying certain DICOM modalities. The data returned from ECIA is already filtered out with all the studies with those modalities. For a list of unsupported modalities, please refer to the *Configurations for DoD images Provided to VA Clinicians*.

JLV, Clinical Display, and VistARad do not support certain SOP classes. Each display has its own unsupported list. For a list of unsupported SOP classes for each display, please refer to the [*Configurations for DoD images Provided to VA Clinicians*](https://www.va.gov/vdl/application.asp?appid=105).

# Appendix B: CVIX Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are numerous tools the system administrator executes to monitor and manage the CVIX server. Table 19 lists the CVIX Tools available.

> **NOTE:** In Table 19, please replace *FQDN* with your server's fully qualified domain name. For example: https://<span class="mark">REDACTED</span>/VixServerHealthWebApp/secure/MyVix.jsp

<table>
<caption><p><span id="_Toc189569307" class="anchor"></span>Table 20: Definitions, Acronyms, and Abbreviations</p></caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>URL</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>https://<em>FQDN</em>:<mark>REDACTED</mark>/Vix/ssl/JavaLogs.jsp</td>
<td><p>Displays information for Java Logs:</p>
<ul>
<li><p>Filename</p></li>
<li><p>File Size</p></li>
<li><p>Date Modified</p></li>
</ul></td>
</tr>
<tr class="even">
<td>https://<mark>REDACTED</mark>/VIXDailyStatus</td>
<td>Shows statistics for all of the VIX sites.</td>
</tr>
<tr class="odd">
<td>https:// <em>FQDN</em>/VixServerHealthWebApp/secure/MyVix.jsp</td>
<td><p>Displays information for the VIX:</p>
<ul>
<li><p>Start Time</p></li>
<li><p>Up Time</p></li>
<li><p>Status</p></li>
<li><p>Realm Configuration</p></li>
<li><p>Tomcat Thread Details</p></li>
<li><p>Transaction Log</p></li>
<li><p>Site Service</p></li>
<li><p>Release of Information (ROI)</p></li>
<li><p>DICOM Services Transmit Failures</p></li>
</ul></td>
</tr>
<tr class="even">
<td>https://<em>FQDN</em>:<mark>REDACTED</mark>/Vix/secure/VixLog.jsp</td>
<td>To access the VIX transaction log while the VIX is running, which contains information about every image and metadata transfer handled by the VIX.</td>
</tr>
<tr class="odd">
<td>https://<em>FQDN</em>:<mark>REDACTED</mark>/vix/viewer/dash</td>
<td>To access a dashboard to access the Image Viewer. The "Dash" is a tool for viewing medical artifacts (similar to the JLV) as well as providing more functionality, such as purging and viewing logs. For more information, see Appendix C: Image Viewer Dashboard.</td>
</tr>
</tbody>
</table>

<span id="_Toc189569307" class="anchor"></span>Table 20: Definitions, Acronyms, and Abbreviations

To access the tools, navigate to <span class="mark">REDACTED</span>/Vix/Viewer/Tools to be prompted to login (Figure 17) at the login page. To login you need a VistA account with the MAG ROI or MAG SYSTEM key. Once logged in, a tools page will appear.

<span id="_Ref163814495" class="anchor"></span>Figure 17: Login Page

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/022.png)

# Appendix C: Image Viewer Dashboard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MAG\*3.0\*177 introduced a dashboard to access the Image Viewer without the need to run a consuming application. To utilize this functionality, the dashboard must be manually enabled through the Image Viewer configuration. To enable the dashboard, modify the Policies section of the C:\Program Files\VistA\Imaging\Vix.Config\VIX.Viewer.config file to include the line below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em>&lt;add name="Viewer.EnableDashboard" value="true" /&gt;</em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The resulting file looks similar to the example below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><em>&lt;?xml version="1.0" encoding="utf-8"?&gt;</em></p>
<p><em>&lt;configuration&gt;</em></p>
<p><em>&lt;configSections&gt;</em></p>
<p><em>&lt;section name="VistA" type="Hydra.VistA.VistAConfigurationSection, Hydra.VistA" /&gt;</em></p>
<p><em>&lt;/configSections&gt;</em></p>
<p><em>&lt;VistA WorkerPoolSize="5" WorkerThreadPoolSize="5"&gt;</em></p>
<p><em>&lt;VixServices&gt;</em></p>
<p><em>&lt;VixService ServiceType="Local" RootUrl="http://localhost:</em><em><mark>REDACTED</mark>"</em></p>
<p><em>&lt;VixService ServiceType="SiteService" RootUrl="http://localhost:</em><em><mark>REDACTED</mark>" /&gt;</em></p>
<p><em>&lt;VixService ServiceType="Viewer" RootUrl="http://+:</em><em><mark>REDACTED</mark>" /&gt;</em></p>
<p><em>&lt;VixService ServiceType="Render" RootUrl="http://localhost:</em><em><mark>REDACTED</mark>" /&gt;</em></p>
<p><em>&lt;/VixServices&gt;</em></p>
<p><em>&lt;Policies&gt;</em></p>
<p><em>&lt;add name="Security.EnablePromiscuousMode" value="true" /&gt;</em></p>
<p><em>&lt;add name="CPRS.ContextId.UseImageIndicator" value="true" /&gt;</em></p>
<p><em>&lt;add name="CPRS.ContextId.ImageIndicatorIndex" value="13" /&gt;</em></p>
<p><em>&lt;add name="Viewer.EnablePresentationState" value="true" /&gt;</em></p>
<p><em>&lt;add name="Viewer.EnableDashboard" value="true" /&gt;</em></p>
<p><em>&lt;add name="Viewer.EnableESignatureVerification" value="true" /&gt;</em></p>
<p><em>&lt;/Policies&gt;</em></p>
<p><em>&lt;/VistA&gt;</em></p>
<p><em>&lt;/configuration&gt;</em></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Restart the VIX Viewer Service.

The default query information resides in the C:\Program Files\VistA\Imaging\Vix.Viewer.Service\TestData\Default.json file. It is not advised to change that file since the installer overwrites it.

To access the Dashboard, in a browser navigate to <span class="mark">REDACTED</span>/vix/viewer/tools to be prompted to login (Figure 17) at the login page. You need a VistA account with the MAG ROI or MAG SYSTEM key. Once logged in, the tools page appears, and click the Image Viewer Dashboard's Open button to display <span class="mark">REDACTED</span>/vix/viewer/dash.

## Image Viewer Dashboard: Homepage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Image Viewer Dashboard homepage (Figure 18) contains the following four options: Logs, Search, System Preferences, and Status.

<span id="_Ref49754550" class="anchor"></span>Figure 18: Image Viewer Dashboard: Homepage

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/023.png)

## Image Viewer Dashboard: Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Image Viewer Dashboard Logs option presents the logs (Figure 19).

<span id="_Ref49950622" class="anchor"></span>Figure 19: Image Viewer Dashboard: Logs

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/024.png)

## Image Viewer Dashboard: Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Image Viewer Dashboard search option (Figure 20) allows the user to edit the fields for both the body and the headers and submit them to query (search) for a patient's study list. The resulting page provides access to each study. The Image Viewer Web Application Programming Interface (API) documentation describes the values for the body and headers. Access the API documentation by entering <span class="mark">REDACTED</span>/vix/viewer/VVSDoc in your browser’s address bar.

<span id="_Ref49950657" class="anchor"></span>Figure 20: Image Viewer Dashboard: Search

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/025.png)

Selecting the View option opens the Image Viewer. The Manage button opens the manage page, and the details show the study level return views. Report opens the text report.

## Image Viewer Dashboard: System Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Image Viewer Dashboard System Preferences option allows for various preferences to be set.

### Annotation Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click Annotation to display annotation preferences (Figure 21).

<span id="_Ref49326086" class="anchor"></span>Figure 21: Annotation Preferences: Annotation

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/026.png)

Click Measurement to display annotation measurement preferences (Figure 22).

<span id="_Ref49326784" class="anchor"></span>Figure 22: Annotation Preferences: Measurement

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/027.png)

Click Ellipse and Rectangle to display annotation ellipse and rectangle preferences (Figure 23).

<span id="_Ref49327037" class="anchor"></span>Figure 23: Annotation Preferences: Eclipse and Rectangle

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/028.png)

Click Label to display label annotation preferences (Figure 24).

<span id="_Ref49957401" class="anchor"></span>Figure 24: Annotation Preferences: Label

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/029.png)

Under the Label preferences, toggle between Annotation, Overlay, Orientation, and Scout & Ruler to set all Label preferences. Click Text to display annotation text preferences (Figure 25).

<span id="_Ref49328237" class="anchor"></span>Figure 25: Annotation Preferences: Text

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/030.png)

Click Mitral and Aortic to display annotation mitral and aortic preferences (Figure 26).

<span id="_Ref52275071" class="anchor"></span>Figure 26: Annotation Preferences: Mitral and Aortic

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/031.png)

### Cine Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view or update Cine preferences, select the Cine Preferences (Figure 27).

<span id="_Ref49328282" class="anchor"></span>Figure 27: Cine Preferences

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/032.png)

### Layout Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view the Layout settings, select the Layout Preference (Figure 28).

<span id="_Ref49328479" class="anchor"></span>Figure 28: Layout Preferences

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/033.png)

Click Add in the bottom right of the window to add a new layout preference.

### Copy Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view the Copy Attributes settings, select the Copy Attributes Preferences (Figure 29).

<span id="_Ref49328550" class="anchor"></span>Figure 29: Copy Attributes Preferences

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/034.png)

### Log Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click Log to view the log preferences (Figure 30).

<span id="_Ref49328615" class="anchor"></span>Figure 30: Log Preferences

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/035.png)

Use the Log Level drop-down to set the log level for both Viewer and Render services. Setting the line limit for the log viewer sets the number of lines in the Line Limit field.

## Image Viewer Dashboard: Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Image Viewer Dashboard Status option shows some configuration keys and values (Figure 31).

<span id="_Ref52274255" class="anchor"></span>Figure 31: Image Viewer Dashboard: Status

![](central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-operations/036.png)

# Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term  | Definition                                              |
|-------|---------------------------------------------------------|
| AE    | Application Entity                                      |
| AHLTA | Armed Forces Health Longitudinal Technology Application |
| ANR   | Automated Notification Report                           |
| API   | Application Programming Interface                       |
| ASL   | Application Service Line                                |
| AWS   | Amazon Web Services                                     |
| BSE   | Broker Security Exchange                                |
| COOP  | Continuity of Operations                                |
| CSV   | Comma-Separated Values                                  |
| CVIX  | Centralized VistA Imaging eXchange                      |
| DAS   | Data Access Service                                     |
| DCF   | DICOM Connectivity Framework                            |
| DES   | Data Exchange Service                                   |
| DICOM | Digital Imaging and Communications in Medicine          |
| DMIX  | Defense Medical Information Exchange                    |
| DoD   | Department of Defense                                   |
| DUZ   | Designated User                                         |
| ECIA  | Enterprise Clinical Imaging Archive                     |
| EDIPI | Electronic Data Interchange Personal Identifier         |
| FDA   | Food and Drug Administration                            |
| GUID  | Globally Unique Identifier                              |
| HAIMS | Health Artifact and Image Management Solution           |
| ICN   | Integration Control Number                              |
| ICR   | Integration Control Registration                        |
| IEN   | Internal Entry Number                                   |
| JLV   | Joint Legacy View / Joint Longitudinal Viewer           |
| JRE   | Java Runtime Environment                                |
| MVI   | Master Veteran Index                                    |
| OAP   | Operational Acceptance Plan                             |
| PM    | Project Manager                                         |
| RACI  | Responsible, Accountable, Consulted, and Informed       |
| ROI   | Release of Information                                  |
| RPC   | Remote Procedure Call                                   |
| RTF   | Rich Text Format                                        |
| SCP   | Service Class Provider                                  |
| SCU   | Service Class User                                      |
| SFTP  | Secure File Transfer Protocol                           |
| SOP   | Service-Object Pair                                     |
| SQL   | Structure Query Language                                |
| TIU   | Text Integration Utility                                |
| TSV   | Tab-Separated Values                                    |
| URN   | Universal Resource Name                                 |
| VAEC  | Veteran Affairs Enterprise Cloud                        |
| VISN  | Veterans Integrated Service Network                     |
| VIX   | VistA Imaging eXchange                                  |
| WAN   | Wide Area Network                                       |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MAG*3*348 Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)

## Using the Cache Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Cache Manager function allows users to browse a CVIX node’s local cache and delete data as required. The Cache Manager is accessed using Chrome or Edge.

To access the CVIX Cache Manager, go to https://*FQDN*:<span class="mark">REDACTED</span>/VixCache (where *FQDN* is the fully qualified domain name of the individual host within the cluster the VIX is installed on).

> **NOTE:** The URL to the CVIX Cache Manager is case-sensitive.

### Cache Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data in the cache is arranged in a hierarchy with one or more of the following levels: data source (VA or DoD) and type (artifact, metadata, or image):

- Repository (VA site or DoD facility)
- Patient identifier (ICN for VA patients)
- Study (group) identifier
- Series and instance identifiers

The source and type of data are the most important factor in determining where an item is cached. When the CVIX Cache Manager is started, the following screen displays (Figure 4):

<span id="_Ref53560629" class="anchor"></span>Figure : VIX Cache Manager Initial Screen Display

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/009.png)

The items immediately under the cache name are called “regions” of the cache. Regions divide the items in the cache by the source of the item (VA versus anywhere else) and the item (image versus anything else). A region defines the conditions under which a cache item is deleted from the cache.

Historically, it has been the case that anything that is not from the VA is from the Department of Defense and anything that is not an image is metadata. Thus, a radiology image from the DoD will be found in the “dod-image-region” while the study text data from a VA site will be found in the “va-metadata-region.

### Technical Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The cache does not understand anything about sites, patients, or studies but operates on the concept of regions, groups, and instances. Regions are collections of similar items with the same lifespan in the cache (i.e., 30 days since last use). Groups are collections of groups and instances. Instances are the cache items proper. Groups are what is called a recursive data structure, a group can contain other groups, which in turn can contain still more groups, *ad infinitum* or at least *ad out-of-memoriam*. The cache limits that hierarchy to specific levels grouped by well-known business concepts (site, patient, etc....). Groups are also the basis that the cache deletes items. If no item in a group has been accessed within the region’s lifespan, then the entire group is deleted from the cache. This is similar to images in a study. If a study has not been accessed for 30 days, then the entire study is deleted from the cache. If none of the studies for a patient have been accessed within 30 days, then the whole patient is deleted from the cache.

Click the “va-image-region” region link, and a list of cache groups will be displayed (Figure 5)

<span id="_Ref53560666" class="anchor"></span>Figure : VIX Cache Manager Region Information Display Example

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/010.png)

The CVIX Cache Manager displays the region's name in the breadcrumb at the top of the page, and a list of the image repositories in this region. To drill down into an image repository, click on the image repository number. To delete an entire image repository, click on the Delete button to the left.

Drill down through the CVIX cache using the links in the CVIX Cache Manager. The levels of the cache–region, repository, patient, study, and image–appear as hyperlinks in the breadcrumb at the top of the page. To delete an item in the cache at any level, click on the Delete button to the left of the item (Figure 6).

<span id="_Ref53560706" class="anchor"></span>Figure : VIX Cache Manager DOD Region Display with Delete Function

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/011.png)

### The DoD Regions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DoD regions are organized by the community operation order identification (OID) number followed by the repository, the patient, and then group identifiers of various sorts. The community OID is an identifier that an enterprise uses to identify itself on the eHealth Exchange. For our purposes, the OIDs are shown in Table 7.

<table>
<caption><p><span id="_Ref52885374" class="anchor"></span>Table 8: CVIX Purge Schedule</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>OID</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.16.840.1.113883.3.42.10012.100001.207</td>
<td>DoD Radiology</td>
</tr>
<tr class="even">
<td>2.16.840.1.113883.3.42.10012.100001.206</td>
<td>DoD Documents</td>
</tr>
<tr class="odd">
<td><p>2.16.840.1.113883.3.166</p>
<p>2.16.840.1.113883.6.233</p></td>
<td>VA Documents</td>
</tr>
<tr class="even">
<td>1.3.6.1.4.1.3768</td>
<td>VA Radiology</td>
</tr>
</tbody>
</table>

<span id="_Ref52885374" class="anchor"></span>Table 8: CVIX Purge Schedule

Below the enterprise OID is a repository (a site in VA parlance). At this time, DoD documents always come from the DES server. Likewise, DoD radiology comes from either HAIMS or ECIA, identified as “200”.

Below the repository identifier is a patient identifier (the patient ICN), and then instances related to that patient.

The DoD metadata region is only used for radiology study text data.

### Cache Item Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clicking a cache item link will retrieve information about the item, such as the last time it was accessed and the size. This information may be useful in locating a specific item.

The size of a cache instance is the size of the file on disk; the size of a cache group is the sum of all the groups and instances contained within it. The checksum, available only for cache instances, results from a mathematical calculation applied to the entire content of the instance. The checksum is used within the VIX to detect data errors. For instance, with the same identifiers, this value should always be the same on all VIX and CVIX.

### Cache Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Usually, the cache is self-managing, determining the cached items that have not been used recently and deleting them. On rare occasions, a corrupt item may be cached. In this case, that corrupt data will be repeatedly served on request. Repeated requests are treated as user access and extend the time that the data stays in the cache. This cache item must be deleted from the cache manually.

Separate and distinct instances of the CVIX cache component reside on each server in the CVIX cluster. A cache item may be cached on one or more servers within the cluster, although the Cache Cluster option eliminates multiple copies of the same item. Without using this option, it is even possible for a cache item to be correct in one server and corrupt in another, leading to difficulty in diagnosing errors. In general, if repeated attempts to access a specific datum through the CVIX fail or present corrupt data, then the item should be in all the cache instances and deleted.

To delete a cache item, collect as much identifying information as possible. At a minimum, this must include whether the source is VA or DoD and, if it is a VA item, whether the image or a study (metadata) is causing problems, and the site the data originated from. In addition, the patient identifier ICN must be known.

Once that information is collected, open the Cache Manager and navigate through the hierarchy to either the corrupt item or to one of its parent groups (patient ID or study) if the item itself cannot be identified. Click on the Delete button and then confirm that the item is to be deleted. The cache does not immediately delete the item since it must synchronize operations from all clients. It may take a few seconds or up to a minute before the item is deleted. Usually, however, it will respond immediately that the item is deleted, and the item will disappear from the Cache Manager.

Finally, it is worth reinforcing that when an item is deleted from the cache, it is not deleted from the original source of the data. If the CVIX is asked for that item again, it will simply notice that it is not in its cache and will retrieve it from the original data source and re-cache it. The effect to the user is a slight delay, nothing more.

The minimal deleterious effect of deleting a cache item, along with difficulty in tracking down an item in one or more cache instances in a cluster, may lead someone to delete “good” cache items to get all the “bad” ones. This is not an issue since the CVIX will simply re-cache the items when requested again.

## Configure DICOM SCP Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides details on the DICOM Service Class Provider (SCP) configuration. The DICOM SCP is a service provider on the VIX/CVIX that transfers DICOM files between the VA and DoD. The DICOM SCP is used to allow VA clinicians to use Commercial PACS, or other query retrieve devices, and DoD clinicians to use NilRead™ or other query retrieve devices, to get remote VistA images through the use of DICOM C-FIND and C-MOVE.

Henceforth, this section refers to, Commercial PACS, NilRead™, and query retrieve devices as a DICOM SCP client.

> **NOTE:** NilRead™ is for CVIX, but VIX also can provide data to Commercial PACS to read, as the protocol used is the same; however, other query retrieve devices can also be used.

*AE Titles Configuration* must be performed manually after CVIX Installation and a Tomcat restart performed after completed. The CVIX install performs some of the configuration for the DICOM SCP automatically with reasonable defaults and predefined entries. Reasonable defaults and predefined entries include the configuration described in *Tomcat DICOM SCP Configuration* and *Laurel Bridge DICOM SCP Configuration* and if specific configuration values are desired instead of the reasonable defaults, then after updating and saving the configuration file, a Tomcat restart must be completed.

> **NOTE:** For additional installations and/or subsequent patch releases, no additional changes to the *AE Titles Configuration* are necessary unless the settings configured have changed and an update is needed.

> **NOTE:** To update access and verify codes for the account with VistA credentials, plain text versions can be entered directly into the configuration file and are encrypted after restarting the Apache Tomcat service. The access and verify codes can also be updated in the configuration file with a reconfigure installation described see the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105) or use the ImagingUtilities-0.1.jar in C:\VixConfig\Encryption to assist with generating encrypted forms of plain text access and verify codes.

> **NOTE:** If updates are needed to the local drive for the VIX cache, see the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105) and perform a reconfigure installation.

### AE Titles Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes both the calling and called Application Entities (AE) Titles that must both be configured for DICOM SCP to work. It is necessary to configure both the AE Titles on the CVIX server with those of the DICOM SCP client and also to configure the AE Titles on the DICOM SCP client with those of the CVIX server.

> **NOTE:** The port for the DICOM SCP client where the DICOM SCP is used must be configured as a bi-directional open port in any firewall.

### Laurel Bridge AE Titles Configuration on CVIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The mapping of external Application Entities (AE) Titles to TCP/IP addresses and ports is configurable and set at the time of installation by installation/administration personnel on the CVIX server. This mapping is necessary for resolving the IP address and port of C-MOVE Destination AE and must be correctly configured for the Laurel Bridge SCP AE to correctly function as a C-MOVE SCP.

> **NOTE:** The configuration is set for use with NilRead™ based on the server type (i.e. test or production) during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise, leave them as they are.

This section describes how to configure the AE Title file ae_title_mappings located in the folders cfg\dicom within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg\dicom by default).

Open the ae_title_mappings file to perform edits. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file.

For each DICOM SCP client, the AE Title name and its host/port attributes must be set. For each DICOM SCP client, update the following entries for the AE Titles configuration file (refer to Figure 10 for line numbers):

1.  Set the IP address for the host for the DICOM SCP client (after host = - line 7).
26. Set the port for the DICOM SCP ad client where the DICOM SCP is used for the C-STORE operation (after port = - line 8).
27. Set the AE title the DICOM SCP client is using to communicate with the DICOM SCP (calling AE) (inside \[ \] - line 6 and after ae_title = - line 9).

Ensure that each of the updated lines is uncommented (i.e. remove the \# at the front of the line if present). Save the ae_title_mappings file after updating the entries.

<span id="_Ref70085061" class="anchor"></span>Figure 10: Sample AE Titles Configuration File

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/015.png)

A more specific example using NilRead™ with some AE Titles filled in is shown in Figure 11. This example is for illustrative purposes only.

<span id="_Ref118113652" class="anchor"></span>Figure : Sample AE Titles Configuration File Filled

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/016.png)

After updating the ae_title_mappings file, as described above, it is necessary to restart the Apache Tomcat service. One way this can be performed is by executing the restart script (Restart_VIX_Services.ps1) as described in the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105).

### AE Titles Configuration on DICOM SCU 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the AE Titles configuration on the AE Titles on the DICOM Service Class User (SCU). Installation/administration personnel on the CVIX server may not be able to perform this configuration and instead must provide the necessary information to the DICOM SCU administration personnel to perform.

The following three pieces of information are needed for the configuration of the DICOM SCU Client: 1) the IP address for the host for the CVIX server, 2) the port of DICOM SCP on the CVIX server, and 3) the AE Title of DICOM SCP (called AE).

Many different DICOM SCU client vendors exist and each of these systems has its own distinct approach to configuration. If additional information regarding specifics of configuring the DICOM SCU client is needed, please reach out to its vendor or consult its documentation.

### Tomcat DICOM SCP Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides details on the ScpConfiguration.Config file located in C:\VixConfig. To update access and verify codes for the account with VistA credentials, plain text versions can be entered directly into the configuration file and are encrypted after restarting the Apache Tomcat service. The access and verify codes can also be updated in the configuration file with a reconfigure installation described see the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105) or use the ImagingUtilities-0.1.jar in C:\VixConfig\Encryption to assist with generating encrypted forms of plain text access and verify codes.

> **NOTE:** Tomcat hosts the DICOM SCP, and the DICOM SCP uses the Laurel Bridge library. Refer to the *Laurel Bridge AE Titles Configuration on CVIX* to configure the ae_title_mappings file which contains the AE Title and port to trust for DICOM SCP.

The CVIX install performs some of the configuration for the DICOM SCP automatically with reasonable defaults and predefined entries. Update two entries in the ScpConfiguration.Config file located in C:\VixConfig to configure the DICOM SCP. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file.

Update the following entries for the DICOM SCP functionality (refer to Figure 12 for line numbers):

1.  Set the DICOM SCU calling AE title, inside opening and closing aeTitle tags (inside \<aeTitle\> \</aeTitle\> - line 21). Change the value from the default setting of ALL.
28. Set the DICOM SCU IP address inside the opening and closing callingAeIp tags (inside \< callingAeIp\> \</callingAeIp\> - line 22). Change the value from the default setting of 0.0.0.0.

<span id="_Ref95990230" class="anchor"></span>Figure : Sample DICOM SCP Configuration File

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/017.png)

An example of the ScpConfiguration.Config file with updates for NilRead™ is shown in Figure 13. This example is for illustrative purposes only.

<span id="_Ref95988667" class="anchor"></span>Figure : Example DICOM SCP Configuration File

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/018.png)

You can update the following entries for the DICOM SCP functionality as desired beyond the reasonable defaults that are pre-populated (refer to Figure 14 for line numbers):

1.  Set the access code for the account with VistA credentials (inside \<accessCode\> \</accessCode \> - line 3). A plain text version can be entered and will be encrypted after Tomcat restart.
2.  Set the verify code for the account with VistA credentials (inside \<verifyCode\> \</verifyCode \> - line 4). A plain text version can be entered and will be encrypted after Tomcat restart.
29. Set the entry for the maximum thread pool size for simultaneous VIX site fetching (inside \<siteFetchTPoolMax\> \</siteFetchTPoolMax\> - line 5). The default setting is to fetch from at most 20 VIX sites at the same time.
30. Set the entry for the maximum time to wait for fetching from the VIX site. If the thread does not finish within this maximum time the C-FIND will not count the studies from that VIX site in the response (inside \<siteFetchTimeLimit\> \</siteFetchTimeLimit\> - line 6). The fetching thread continues if it is not finished within the time limit. If the fetching is finally successful, the user may re-initiate the C-FIND search and the studies from that site will be counted. The default setting is set to 45 seconds. Depending on the DICOM SCU server settings, this setting may be adjusted to a time the DICOM SCU is willing to wait.
31. Set the entry for the maximum thread pool size for simultaneous image fetching through the local ImageWebApp (inside \<imageFetchTPoolMax\> \</imageFetchTPoolMax\> - line 7). The default setting is to fetch from at most 15 images at the same time.
32. Set the entry for the maximum time to wait for fetching the images. (inside \<imageFetchTimeLimit\> \</imageFetchTimeLimit\> - line 8). The default setting is set to 1,000,000 seconds. Since the default maximum time to wait for fetching the images is longer than one day, there is no effective limit due to the nightly server restart.
33. Set the value to true or false to use the remote image service (true) or the local image service (false) (inside \<useRemoteImageFetch\> \</useRemoteImageFetch\> - line 9). The default setting is set to true.
34. Set the value to true or false to use direct image fetch (inside \<useDirectFetch\> \</useDirectFetch \> - line 10). The default setting is set to true which retrieves the file paths for the images from the remote VistA and retrieves the images directly from the SMB storage. If set to false, direct image fetch is not used.
35. Each time a user makes a query for a patient (C-FIND), the query information (patient ID) and the study metadata is stored in memory cache for future reference by subsequent series queries and image retrieval (C-MOVE). Set the entry for the cache retention period of how long (in hours) this query information and study metadata is stored in memory (inside \<cacheLifespan\> \</cacheLifespan\> - line 11). If 0 is entered, the entries are kept indefinitely in memory or until the next Apache Tomcat service restart.
36. Set the value to true or false for if the C-FIND operation, when querying for studies, also caches the list of studies series metadata in the background (\<preFetchSeries\> \</preFetchSeries\>) - line 12.
37. If desired to set allowed AE Titles for the C-FIND caller called AE that it is calling, inside the opening and closing calledAETitle tags (line 13), insert the AE Title of DICOM SCP (called AE) followed by an underscore (\_) followed by the IP address for the host for the VIX server.
38. If desired to query patient identifiers unknown to the local VistA set remotePatientResolution to true inside the opening and closing remotePatientResolution tags, otherwise set false (inside \< remotePatientResolution\> \</ remotePatientResolution\> - line 14). The default setting is false. When true the VIX will fall back to querying CVIX with any patient identifiers it receives that cannot be resolved locally.
39. Set the entry for the maximum number of images able to be queued to download at once (inside \<imageQueueSize\> \</imageQueueSize\> - line 15). The default setting is to 10,000 images.
40. Set the entry for the number of hours cached metadata is considered valid (metadata older than this time can be overwritten) (inside \<cacheMetaHoursToLive\> \</cacheMetaHoursToLive\> - line 16). The default setting is to 24 hours.
41. If desired to enable fast data transfer set isFdtEnabled to true inside the opening and closing isFdtEnabled tags, otherwise set false (inside \<isFdtEnabled\> \</isFdtEnabled\> - line 17). The default setting is true.
42. If desired to change the port for fast data transfer set the port inside the opening and closing fdtPort tags (inside \<fdtPort\> \</fdtPort\> - line 18). The default port is 2762.

    NOTE: The selected port for fast data transfer must be visible to other VIX across the VA.
43. If desired to see the VA reports as Secondary Capture images, set buildReport to SC inside the opening and closing buildReport tags (inside \<buildReport\> \</buildReport \> - line 23). To see VA reports as Structured Reports, set buildReport to SR inside the opening and closing buildReport tags (inside \<buildReport\> \</buildReport \> - line 23). To turn off VA report generation, set buildReport to NONE inside the opening and closing buildReport tags (inside \<buildReport\> \</buildReport \> - line 23).
44. If desired to return study query level in C-FIND responses set returnQueryLevel to true inside the opening and closing returnQueryLevel tags, otherwise set false (inside \<returnQueryLevel\> \</ returnQueryLevel\> - line 24).
45. The default setting for studyQueryFilter is radiology inside the opening and closing studyQueryFilter tags (inside \<studyQueryFilter\> \</ studyQueryFilter \> - line 25).

    Radiology includes all DICOM exams with some exceptions. The setting for studyQueryFilter can be changed to all or one of the following specializations which are mapped to VA-specific modalities: cl_cardiology, cl_dermatology, cl_dicom, cl_dental, cl_eyecare, cl_other, and cl_radiology. All includes all exams regardless of their contents, though any exam without an associated Study Instance UID will automatically be excluded from the results. The specialization mappings are defined in DicomCategoryFilterConfiguration.config and can be updated if desired. The specialization mappings include: cl_cardiology filters for any cardiology related study modality, cl_dermatology filters for any dermatology related study modality, cl_dicom filters for any DICOM related study modality, cl_dental filters for any dental related study modality, cl_eyecare filters for any eyecare related study modality, cl_other filters for any other modality not included in other filters available, cl_radiology filters for any radiology related study modality.
46. If desired to not have actively serviced C-MOVE timeouts, set sendKeepAlive to true inside the opening and closing sendKeepAlive tags, otherwise set false (inside \<sendKeepAlive\> \</ sendKeepAlive \> - line 26). The default setting is false.
47. If desired to not fetch certain modality images, set the entries inside the opening and closing modalityBlockList tags for different dataSources.
1.  For each dataSource (DoD or VA), set different modality lists if necessary, by inserting DoD or VA inside the opening and closing dataSource tags (\<dataSource\> \</dataSource\> - line 29), by default the value is ALL.
2.  The modalities will be filtered at study and series levels. If needed, set at the image level. To do so, set true at the image level when needed by inserting true inside the opening and closing addImageLevelFilter tags, otherwise set false (\<addImageLevelFilter\> \</addImageLevelFilter\> - line 30).
3.  List all the modalities to be blocked for that dataSource separately using string tags inside the opening and closing modalities section (\<modalities\> \</modalities\> - lines 31 and 33). Examples of modalities to potentially include inside the string tags include SR and PR.
48. The installer automatically generates a default blacklist consisting of site codes that configured DICOM SCUs do not receive data from. Your local site code and the site codes of your Veterans Integrated Service Network (VISN) appear in the \<siteCodeBlackList\> section in the file ScpConfiguration.config located in the C:\VixConfig folder. If you want your site’s data to be available to the configured DICOM SCU, ensure your local site code is not in the \<siteCodeBlackList\> section in the ScpConfiguration.config. List all the site codes to be blocked separately using string tags inside the opening and closing siteCodeBlackList section (\<siteCodeBlackList \> \</siteCodeBlackList \> - lines 36 and 42). Examples of site codes to include inside the string tags include the following:
1.  Set a string to 100 to exclude Claims system information.
2.  Set a string tag to 200CLMS to exclude 200 VHA Claims study information.
3.  Set a string tag to 200CORP to exclude the Claims site.
4.  Set a string tag to 741 to exclude Global Disability Examinations.
5.  Set a string tag to LOCAL to signal the DICOM Service to replace it with the local site number and all of the sites in that Veterans Integrated Service Networks (VISN).

    NOTE: If desired to exclude DoD studies information, set a string tag to 200 inside the opening and closing siteCodeBlackList section (\<siteCodeBlackList \> \</siteCodeBlackList\>.

Save the ScpConfiguration.Config file after updating the entries. After updating the DICOM SCP config file, the ScpConfiguration.Config file will look like (Figure 14):

<span id="_Ref69388265" class="anchor"></span>Figure : Sample DICOM SCP Configuration File

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/019.png)

For additional DICOM SCU calling AE titles, insert an additional block of code containing the elements from lines 19 to 43 before current line 44 and then repeat steps 1 to 22 inside these additional lines that have been added, see Figure 15.

<span id="_Ref90914075" class="anchor"></span>Figure : Sample DICOM SCP Configuration File with Multiple DICOM SCU Calling AE Titles

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/020.png)

After updating the ScpConfiguration.Config file, as described above, it is necessary to restart the Apache Tomcat service. One way this can be performed is by executing the restart script (Restart_VIX_Services.ps1) as described in the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105).

### Laurel Bridge DICOM SCP Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides details on the Laurel Bridge DICOM file located in the cfg folder within the Laurel Bridge installation directory (C:\DCF_RunTime_x64\cfg by default) are desired. This is useful for debugging purposes but the details on how to change this are beyond the scope of this document. For typical CVIX operation, no changes are necessary to the Laurel Bridge DICOM file.

Open the DicomScpConfig file to perform edits. Run Notepad, Notepad++, or WordPad as an administrator, and then open the file. Numerous entries can be updated in the DicomScpConfig configuration file (Figure 16). Save the DicomScpConfig file after updating the entries.

<span id="_Ref72232899" class="anchor"></span>Figure : Sample DicomScpConfig Configuration File

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/021.png)

After updating the DicomScpConfig file, as described above, it is necessary to restart the Apache Tomcat service. One way this can be performed is by executing the restart script (Restart_VIX_Services.ps1) as described in the [CVIX Installation Guide](https://www.va.gov/vdl/application.asp?appid=105).

### JRE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX’s servlet container and the CVIX itself requires Java Runtime Environment (JRE) version 8.0_371.

## VIX Viewer Dashboard: Homepage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX Viewer Dashboard homepage (Figure 21) contains the following four options: Logs, Search, System Preferences, and Status.

<span id="_Ref49754550" class="anchor"></span>Figure : VIX Viewer Dashboard: Homepage

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/026.png)

## VIX Viewer Dashboard: Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX Viewer Dashboard Logs option presents the logs (Figure 22).

<span id="_Ref49950622" class="anchor"></span>Figure : VIX Viewer Dashboard: Logs

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/027.png)

## VIX Viewer Dashboard: Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX Viewer Dashboard search option (Figure 23) allows the user to edit the fields for both the body and the headers and submit them to query (search) for a patient's study list. The resulting page provides access to each study. The VIX Viewer Web API documentation describes the values for the body and headers. Access the API documentation by entering <span class="mark">REDACTED</span>/vix/viewer/VVSDoc in your browser’s address bar.

<span id="_Ref49950657" class="anchor"></span>Figure : VIX Viewer Dashboard: Search

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/028.png)

Selecting the View option opens the VIX Viewer. The Manage button opens the manage page, and the details show the study level return views. Report opens the text report.

## VIX Viewer Dashboard: System Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX Viewer Dashboard System Preferences option allows for various preferences to be set.

### Annotation Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click Annotation to display annotation preferences (Figure 24).

<span id="_Ref49326086" class="anchor"></span>Figure : Annotation Preferences: Annotation

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/029.png)

Click Measurement to display annotation measurement preferences (Figure 25).

<span id="_Ref49326784" class="anchor"></span>Figure : Annotation Preferences: Measurement

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/030.png)

Click Ellipse and Rectangle to display annotation ellipse and rectangle preferences (Figure 26).

<span id="_Ref49327037" class="anchor"></span>Figure : Annotation Preferences: Eclipse and Rectangle

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/031.png)

Click Label to display label annotation preferences (Figure 27).

<span id="_Ref49957401" class="anchor"></span>Figure : Annotation Preferences: Label

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/032.png)

Under the Label preferences, toggle between Annotation, Overlay, Orientation, and Scout & Ruler to set all Label preferences. Click Text to display annotation text preferences (Figure 28).

<span id="_Ref49328237" class="anchor"></span>Figure : Annotation Preferences: Text

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/033.png)

Click Mitral and Aortic to display annotation mitral and aortic preferences (Figure 29).

<span id="_Ref52275071" class="anchor"></span>Figure : Annotation Preferences: Mitral and Aortic

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/034.png)

### Cine Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view or update Cine preferences, select the Cine Preferences (Figure 30).

<span id="_Ref49328282" class="anchor"></span>Figure : Cine Preferences

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/035.png)

### Layout Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view the Layout settings, select the Layout Preference (Figure 31).

<span id="_Ref49328479" class="anchor"></span>Figure : Layout Preferences

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/036.png)

Click Add in the bottom right of the window to add a new layout preference.

### Copy Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view the Copy Attributes settings, select the Copy Attributes Preferences (Figure 32).

<span id="_Ref49328550" class="anchor"></span>Figure : Copy Attributes Preferences

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/037.png)

### Log Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click Log to view the log preferences (Figure 33).

<span id="_Ref49328615" class="anchor"></span>Figure : Log Preferences

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/038.png)

Use the Log Level drop-down to set the log level for both Viewer and Render services. Setting the line limit for the log viewer sets the number of lines in the Line Limit field.

## VIX Viewer Dashboard: Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX Viewer Dashboard Status option shows some configuration keys and values (Figure 34).

<span id="_Ref52274255" class="anchor"></span>Figure : VIX Viewer Dashboard: Status

![](mag-3-348-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/039.png)

### From: MAG*3*329 Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)

### Cache Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data in the cache is arranged in a hierarchy with one or more of the following levels: data source (VA or DoD) and type (artifact, metadata, or image):

- Repository (VA site or DoD facility)
- Patient identifier (ICN for VA patients)
- Study (group) identifier
- Series and instance identifiers

The source and type of data are the most important factor in determining where an item is cached. When the CVIX Cache Manager is started, the following screen displays (Figure 4):

<span id="_Ref53560629" class="anchor"></span>Figure : VIX Cache Manager Initial Screen Display

![](mag-3-329-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/005.png)

The items immediately under the cache name are called “regions” of the cache. Regions divide the items in the cache by the source of the item (VA versus anywhere else) and the item (image versus anything else). A region defines the conditions under which a cache item is deleted from the cache.

Historically, it has been the case that anything that is not from the VA is from the Department of Defense and anything that is not an image is metadata. Thus, a radiology image from the DoD will be found in the “dod-image-region” while the study text data from a VA site will be found in the “va-metadata-region.

### Technical Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The cache does not understand anything about sites, patients, or studies but operates on the concept of regions, groups, and instances. Regions are collections of similar items with the same lifespan in the cache (i.e., 30 days since last use). Groups are collections of groups and instances. Instances are the cache items proper. Groups are what is called a recursive data structure, a group can contain other groups, which in turn can contain still more groups, *ad infinitum* or at least *ad out-of-memoriam*. The cache limits that hierarchy to specific levels grouped by well-known business concepts (site, patient, etc....). Groups are also the basis that the cache deletes items. If no item in a group has been accessed within the region’s lifespan, then the entire group is deleted from the cache. This is similar to images in a study. If a study has not been accessed for 30 days, then the entire study is deleted from the cache. If none of the studies for a patient have been accessed within 30 days, then the whole patient is deleted from the cache.

Click the “va-image-region” region link, and a list of cache groups will be displayed (Figure 5)

<span id="_Ref53560666" class="anchor"></span>Figure : VIX Cache Manager Region Information Display Example

![](mag-3-329-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/006.png)

The CVIX Cache Manager displays the region's name in the breadcrumb at the top of the page, and a list of the image repositories in this region. To drill down into an image repository, click on the image repository number. To delete an entire image repository, click on the Delete button to the left.

Drill down through the CVIX cache using the links in the CVIX Cache Manager. The levels of the cache–region, repository, patient, study, and image–appear as hyperlinks in the breadcrumb at the top of the page. To delete an item in the cache at any level, click on the Delete button to the left of the item (Figure 6).

<span id="_Ref53560706" class="anchor"></span>Figure : VIX Cache Manager DOD Region Display with Delete Function

![](mag-3-329-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/007.png)

### The DoD Regions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DoD regions are organized by the community operation order identification (OID) number followed by the repository, the patient, and then group identifiers of various sorts. The community OID is an identifier that an enterprise uses to identify itself on the eHealth Exchange. For our purposes, the OIDs are shown in Table 7.

<table>
<caption><p><span id="_Ref52885374" class="anchor"></span>Table 8: CVIX Purge Schedule</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>OID</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2.16.840.1.113883.3.42.10012.100001.207</td>
<td>DoD Radiology</td>
</tr>
<tr class="even">
<td>2.16.840.1.113883.3.42.10012.100001.206</td>
<td>DoD Documents</td>
</tr>
<tr class="odd">
<td><p>2.16.840.1.113883.3.166</p>
<p>2.16.840.1.113883.6.233</p></td>
<td>VA Documents</td>
</tr>
<tr class="even">
<td>1.3.6.1.4.1.3768</td>
<td>VA Radiology</td>
</tr>
</tbody>
</table>

<span id="_Ref52885374" class="anchor"></span>Table 8: CVIX Purge Schedule

Below the enterprise OID is a repository (a site in VA parlance). At this time, DoD documents always come from the DES server. Likewise, DoD radiology comes from either HAIMS or ECIA, identified as “200”.

Below the repository identifier is a patient identifier (the patient ICN), and then instances related to that patient.

The DoD metadata region is only used for radiology study text data

### Cache Item Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clicking a cache item link will retrieve information about the item, such as the last time it was accessed and the size. This information may be useful in locating a specific item.

The size of a cache instance is the size of the file on disk; the size of a cache group is the sum of all the groups and instances contained within it. The checksum, available only for cache instances, results from a mathematical calculation applied to the entire content of the instance. The checksum is used within the VIX to detect data errors. For instance, with the same identifiers, this value should always be the same on all VIX and CVIX.

### Cache Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Usually, the cache is self-managing, determining the cached items that have not been used recently and deleting them. On rare occasions, a corrupt item may be cached. In this case, that corrupt data will be repeatedly served on request. Repeated requests are treated as user access and extend the time that the data stays in the cache. This cache item must be deleted from the cache manually.

Separate and distinct instances of the CVIX cache component reside on each server in the CVIX cluster. A cache item may be cached on one or more servers within the cluster, although the Cache Cluster option eliminates multiple copies of the same item. Without using this option, it is even possible for a cache item to be correct in one server and corrupt in another, leading to difficulty in diagnosing errors. In general, if repeated attempts to access a specific datum through the CVIX fail or present corrupt data, then the item should be in all the cache instances and deleted.

To delete a cache item, collect as much identifying information as possible. At a minimum, this must include whether the source is VA or DoD and, if it is a VA item, whether the image or a study (metadata) is causing problems, and the site the data originated from. In addition, the patient identifier ICN must be known.

Once that information is collected, open the Cache Manager and navigate through the hierarchy to either the corrupt item or to one of its parent groups (patient ID or study) if the item itself cannot be identified. Click on the Delete button and then confirm that the item is to be deleted. The cache does not immediately delete the item since it must synchronize operations from all clients. It may take a few seconds or up to a minute before the item is deleted. Usually, however, it will respond immediately that the item is deleted, and the item will disappear from the Cache Manager.

Finally, it is worth reinforcing that when an item is deleted from the cache, it is not deleted from the original source of the data. If the CVIX is asked for that item again, it will simply notice that it is not in its cache and will retrieve it from the original data source and re-cache it. The effect to the user is a slight delay, nothing more.

The minimal deleterious effect of deleting a cache item, along with difficulty in tracking down an item in one or more cache instances in a cluster, may lead someone to delete “good” cache items to get all the “bad” ones. This is not an issue since the CVIX will simply re-cache the items when requested again.

### AE Titles Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes both the calling and called Application Entities (AE) Titles that must both be configured for DICOM SCP to work. It is necessary to configure both the AE Titles on the CVIX server with those of the DICOM SCP client and also to configure the AE Titles on the DICOM SCP client with those of the CVIX server.

> **NOTE:** The port for the DICOM SCP client where the DICOM SCP is used must be configured as a bi-directional open port in any firewall.

### AE Titles Configuration on DICOM SCU 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the AE Titles configuration on the AE Titles on the DICOM Service Class User (SCU). Installation/administration personnel on the CVIX server may not be able to perform this configuration and instead must provide the necessary information to the DICOM SCU administration personnel to perform.

The following three pieces of information are needed for the configuration of the DICOM SCU Client: 1) the IP address for the host for the CVIX server, 2) the port of DICOM SCP on the CVIX server, and 3) the AE Title of DICOM SCP (called AE).

Many different DICOM SCU client vendors exist and each of these systems has its own distinct approach to configuration. If additional information regarding specifics of configuring the DICOM SCU client is needed, please reach out to its vendor or consult its documentation.

### From: MAG*3*303 Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)

### Additional for Configurations for ECIA only for DoD images Provided to VA Clinicians 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This describes additional configuration steps <u>only to be performed</u> when CVIX collection of DoD medical images from <u>ECIA is enabled</u> (i.e. \<useEcia\>true\</useEcia\>).

Perform this step to further configure the CVIX collection of DoD medical images to ECIA via the MIXDataSource-1.0.config file.

> **NOTE:** Before moving forward with the instructions for this step, it is expected that the site administrator is aware of all needed entries in the configuration including \<host\>, \<callingAE\>, and \<calledAE\> for AcuoMed and \<host\>, \<port\>, and \<protocol\>for AcuoAccess.

> **NOTE:** The configuration including \<host\>, \<callingAE\>, and \<calledAE\> for AcuoMed and \<host\> for AcuoAccess are set based on the server type (i.e. test or production) during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise leave them as they are.

Open the MIXDataSource-1.0.config in C:\VixConfig. Run Notepad, Notepad++, or WordPad as an administrator and then open the file.

To enable the ECIA configuration, further update the MIXDataSource-1.0.config like Figure 8 and Figure 9:

1.  Set the entry for the host for AcuoMed, (inside \<host\> \</host\> - line 26).
17. Set the entry for the port for AcuoMed (inside \<port\> \</port\> - line 27).
18. Set the entry for the client identification for AcuoMed (inside \<callingAE\> \</callingAE\> - line 29).
19. Set the entry for the server identification for AcuoMed (inside \<calledAE\> \</calledAE\> - line 30).
20. Set the entry for the host for AcuoAccess (inside \<host\> \</host\> - line 43).
21. Set the port for AcuoAccess (inside \<port\> \</port\> - line 44).
22. Set the protocol for AcuoAccess (inside \<protocol\> \</ protocol\> - line 45).
23. Verify the \<string\>SR\</string\> line is NOT present inside the \<emptyStudyModalities\> \</emptyStudyModalities\>. (If present, remove this line).
24. Set the DICOM modality types that will not be returned from the DoD (inside \<string\> \</string\> tags).

> **NOTE:** The \<string\> \</string\> tags inside the vistaRadModalityBlacklist are set during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise leave them as they are.

> **NOTE:** Inside the \<string\> \</string\> tags, insert the DICOM Identifier for the modality. For example, if an “SR” is inserted inside the \<string\> \</string\> tag, then a Structured Report will not be returned from the DoD.

> **NOTE:** If more or less DICOM modality types (referred to as a modality blacklist) are not to be returned from the DoD, add or remove additional \<string\> \</string\> lines (within the opening and closing tags for vistaRadModalityBlacklist). Inside the \<string\> \</string\> tags, insert the DICOM Identifier for the modality.

25. Set the DICOM Service-Object Pair (SOP) Class UIDs (referred to as SOP blacklists) that represent image types and that will be replaced with a static image file for three different image viewer applications (Vista Imaging Clinical Display, JLV, VistaRad). For the blacklist changes, add or remove the DICOM SOP Class UIDs according to the prerequisites. (inside \<string\> \</string\> tags for Vista Imaging Clinical Display; inside \<string\> \</string\> tags for JLV; inside \<string\> \</string\> tags for VistaRad).

> **NOTE:** The \<string\> \</string\> tags inside the SOP blacklists (i.e. sopBlacklistForClinicalDisplay, sopBlacklistForVixViewer, or sopBlacklistForVistaRad) are set during the end of the install via the PowerShell script utility. If these values are not the same as the values you have for these in the installation prerequisites, change them according to the values for these in the prerequisites; otherwise leave them as they are.

> **NOTE:** For example, if a “1.2.840.10008.5.1.4.1.1.88.11” is inserted inside the \<string\> \</string\> tag, then Basic Text SR that the SOP Class UID represents will be replaced with a static image file for Vista Imaging Clinical Display.

> **NOTE:** For example, if a “1.2.840.10008.5.1.4.1.1.88.11” is inserted inside the \<string\> \</string\> tag, then Basic Text SR that the SOP Class UID represents will be replaced with a static image file for JLV.

> **NOTE:** For example, if a “1.2.840.10008.5.1.4.1.1.88.11” is inserted inside the \<string\> \</string\> tag, then Basic Text SR that the SOP Class UID represents will be replaced with a static image file for VistaRad.

> **NOTE:** Inside the \<string\> \</string\> tags, insert the DICOM SOP Class UIDs according to the prerequisites.

> **NOTE:** If more or less DICOM SOP Class UIDs are needed, add or remove additional \<string\> \</string\> lines within the opening and closing tags for the appropriate viewer (i.e. sopBlacklistForClinicalDisplay, sopBlacklistForVixViewer, or sopBlacklistForVistaRad). Inside the \<string\> \</string\> tags, insert the DICOM SOP Class UIDs to blacklist.

Save the MIXDataSource-1.0.config file after updating the entries.

<span id="_Ref48825630" class="anchor"></span>Figure 8: Sample MIXDataSource-1.0.config file - Top Portion

![](mag-3-303-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/009.png)

<span id="_Ref55317764" class="anchor"></span>Figure 9: Sample MIXDataSource-1.0.config file - Middle Portion

![](mag-3-303-central-vista-imaging-exchange-cvix-administrator-s-guide-and-product-/010.png)

### From: MAG*3*269 Central VistA Imaging Exchange (CVIX) Administrator's Guide and Product Operations Manual (POM)

### SQL Express

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CVIX requires the install of SQLEXPRESS_X64-14_0_1000_169.ZIP.
