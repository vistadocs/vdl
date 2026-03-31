---
consolidated_title: "datup local installation guide"
app_code: PRED
doc_type: IG
master_source: "DATUP Version 2 Local Installation Guide"
master_pub_date: July 2014
consolidated_from: 3 versions
prior_versions:
  - "DATUP Version 3.0.01 Local Installation Guide"
  - "DATUP Version 3 Local Installation Guide"
---

Local Data Update (DATUP) Installation Guide

Pharmacy Reengineering

![](datup-version-2-local-installation-guide/001.png)

July 2014

Office of Information and Technology (OIT)

Product Development (PD)

REVISION HISTORY

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. No Change Pages document is created for this manual. Replace any previous copy with this updated version.

<table>
<caption><p><span id="_Ref213809714" class="anchor"></span>Table 3‑. Optional Site Configuration Properties</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>July 18, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Changed date (month) to reflect real release date</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>June 3, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Fixed pagination</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 30, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Added footnote describing relationship between FDB MedKnowledge Framework and FDB-DIF, updated text appropriately. Updated TOC.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>May 28, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated images for 508 compliance; changed FDB MedKnowledge Framework back to FDB-DIF. Updated TOC</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 27, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated Revision History format; did a partial search and replace on FDB-DIF (and other similar iterations) to FDB MedKnowledge Framework, though not in the instructions as the tool may not be updated yet. Removed extraneous definitions of FDB.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>May 21, 2014</td>
<td>i</td>
<td>N/A (First Release)</td>
<td><p>Updated Revision History</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 21, 2014</td>
<td>i, 3, B-1</td>
<td>N/A (First Release)</td>
<td><p>Updated Title Page, Corrected Version number in Overview section, minor text edit, added B-1 to Table of Figures.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>May 19, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>DBA Corrected Information, minor formatting updates</p>
<p><mark>REDACTED</mark>, <mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 13, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Edits to headings, TOC, references, and footers</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>February 7, 2013</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Technical Writer Edits</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>February 5, 2013</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updates to various section for DATUP 2.0</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>February 1, 2013</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Incorporated database configuration updates for DATUP 2.0, FDB installation instructions moved to FDB install guide.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>August 27, 2012</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Changed formatting and performed edits</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>August 14,2012</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updates to various section to address minor configuration changes</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 29,2012</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated the document to address change request #CR5172 (Image Processing for PPS)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>December 3, 2010</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>No changes since last delivery. Updated the version number to reflect the latest release of DATUP.</p>
<p>SwRI</p></td>
</tr>
<tr class="odd">
<td>November 12, 2010</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated the document to address change request #CR2942.</p>
<p>SwRI</p></td>
</tr>
<tr class="even">
<td>October 8, 2010</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Renamed all instances of “PEDTUP” to “DATUP.”</p>
<p>SwRI</p></td>
</tr>
<tr class="odd">
<td>September 3, 2010</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Local PEDTUP Installation Guide: Initial version.</p>
<p>SwRI</p></td>
</tr>
</tbody>
</table>

<span id="_Ref213809714" class="anchor"></span>Table 3‑. Optional Site Configuration Properties

ProPath Template used v1.6, June 2012

TABLE OF CONTENTS

LIST OF FIGURES

Figure 3‑1. WebLogic Console [5](#_Ref191089515)

Figure 3‑2. Domain Structure [8](#_Ref256581857)

Figure 3‑3. Change Center [9](#_Ref256581858)

Figure 3‑4. Summary of Servers [9](#_Ref256581859)

Figure 3‑5. Settings for Deployment Server [10](#_Ref256581860)

Figure 3‑6. Server Start Tab [11](#_Ref256581861)

Figure 3‑7. Activate Changes [12](#_Ref256581862)

Figure 3‑8. Domain Structure [13](#_Ref184087883)

Figure 3‑9. Change Center [13](#_Ref184087925)

Figure 3‑10. Summary of JDBC Data Sources [14](#_Ref181416612)

Figure 3‑11. JDBC Data Source Properties [15](#_Ref191102359)

Figure 3‑12. Transaction Options [16](#_Ref191089711)

Figure 3‑13. Connection Properties [17](#_Ref191089804)

Figure 3‑14. Test Database Connection [18](#_Ref191089849)

Figure 3‑15. Select Targets [19](#_Ref191089523)

Figure 3‑16. Summary of JDBC Data Sources [19](#_Ref181418183)

Figure 3‑17. Statement Cache Size Parameter [20](#_Ref258586453)

Figure 3‑18. Activate Changes [20](#_Ref193865244)

Figure 3‑19. Lock & Edit [23](#_Ref195512216)

Figure 3‑20. JMS Modules [23](#_Ref195512217)

Figure 3‑21. JMS Modules [24](#_Ref195512223)

Figure 3‑22. JMS System Module Properties [24](#_Ref195512238)

Figure 3‑23. JMS System Module Targets [25](#_Ref195512256)

Figure 3‑24. Add Resources to JMS System Module [25](#_Ref195512273)

Figure 3‑25. Activate Changes [26](#_Ref195512291)

Figure 3‑26. Lock & Edit [26](#_Ref193978393)

Figure 3‑27. JMS Modules [27](#_Ref193978412)

Figure 3‑28. JMS Modules [27](#_Ref193978431)

Figure 3‑29. Summary of Resources [28](#_Ref193978452)

Figure 3‑30. Choose Type of Resource to Create [29](#_Ref193981712)

Figure 3‑31. Foreign Server Properties [29](#_Ref193977655)

Figure 3‑32. Foreign JMS Server Target [30](#_Ref193981734)

Figure 3‑33. Summary of Resources [31](#_Ref193981761)

Figure 3‑34. Foreign JMS Server General Configuration [32](#_Ref193981790)

Figure 3‑35. Activate Changes [33](#_Ref193978131)

Figure 3‑36. Lock & Edit [33](#_Ref271266366)

Figure 3‑37. JMS Modules [34](#_Ref271266392)

Figure 3‑38. JMS Modules [34](#_Ref271266409)

Figure 3‑39. Summary of Resources [35](#_Ref271266425)

Figure 3‑40. Foreign JMS Server General Configuration [36](#_Toc389565184)

Figure 3‑41. Destinations [37](#_Ref271266475)

Figure 3‑42. Foreign Connection Factory Properties [37](#_Ref271266551)

Figure 3‑43. Activate Changes [38](#_Ref271266563)

Figure 3‑44. Lock & Edit [38](#_Ref193981831)

Figure 3‑45. JMS Modules [39](#_Ref193981847)

Figure 3‑46. JMS Modules [39](#_Ref193981888)

Figure 3‑47. Summary of Resources [40](#_Ref193981910)

Figure 3‑48. Foreign JMS Server General Configuration [41](#_Ref193978585)

Figure 3‑49. Foreign JMS Server Connection Factories [42](#_Ref193979224)

Figure 3‑50. Foreign Connection Factory Properties [42](#_Ref193979563)

Figure 3‑51. Activate Changes [43](#_Ref193979715)

Figure 3‑52. Domain Structure [44](#_Ref178735721)

Figure 3‑53. Change Center [45](#_Ref181421187)

Figure 3‑54. Deployments [45](#_Ref178732223)

Figure 3‑55. Install Application Assistant [46](#_Ref178732382)

Figure 3‑56. Locate Deployment to Install and Prepare for Deployment [47](#_Ref184090181)

Figure 3‑57. Upload a Deployment to the Admin Server [48](#_Ref184090012)

Figure 3‑58. Choose Targeting Style [49](#_Ref176676787)

Figure 3‑59. Select Deployment Targets [49](#_Ref191090118)

Figure 3‑60. Optional Settings [50](#_Ref191090176)

Figure 3‑61. Review Your Choices and Click Finish [51](#_Ref191090260)

Figure 3‑62. Settings for DATUP [52](#_Ref191090327)

Figure 3‑63. Activate Changes [53](#_Ref178733999)

Figure 3‑64. Domain Structure [53](#_Ref181421306)

Figure 3‑65. Summary of Deployments [54](#_Ref191090401)

Figure 3‑66. Start Application Assistant [54](#_Ref191090464)

Figure 3‑67. Summary of Deployments – DATUP Deployment Active [55](#_Ref191090529)

Figure 4‑1. Domain Structure [57](#_Ref246231865)

Figure 4‑2. Change Center [58](#_Ref246231871)

Figure 4‑3. Summary of Deployments – Stopping DATUP [58](#_Ref246231328)

Figure 4‑4. Force Stop Application Assistant [59](#_Ref246231887)

Figure 4‑5. Summary of Deployments – DATUP Deployment Prepared [59](#_Ref246231898)

Figure 4‑6. Delete Application Assistant [60](#_Ref246231908)

Figure 4‑7. Summary of Deployments – DATUP Deployment Deleted [60](#_Ref246231916)

Figure 4‑8. Activate Changes [61](#_Ref246231924)

Figure B‑1: Combined DATUP/PECS Architecture Diagram [2](#_Toc389565220)

LIST OF TABLES

Table 3‑1. Terminology [6](#_Ref176675115)

Table 3‑2. Optional Site Configuration Properties [43](#_Ref213809714)

*(This page included for two-sided copying.)*

# Project Scope


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Project Scope](#project-scope)
  - [Project Description](#project-description)
  - [PRE Project Goals and Objectives](#pre-project-goals-and-objectives)
  - [DATUP Background](#datup-background)
  - [Related Documents](#related-documents)
- [Document Overview](#document-overview)
  - [Document Background](#document-background)
  - [Overview](#overview)
- [Installation Instructions](#installation-instructions)
  - [Terminology](#terminology)
  - [Assumptions](#assumptions)
  - [Database Installation and Configuration](#database-installation-and-configuration)
  - [WebLogic Installation Instructions](#weblogic-installation-instructions)
    - [Class Path](#class-path)
    - [WebLogic Server Startup Configuration](#weblogic-server-startup-configuration)
    - [Local JDBC Data Source Configuration](#local-jdbc-data-source-configuration)
    - [Log4j](#log4j)
    - [Local JMS Configuration](#local-jms-configuration)
    - [Site Configuration Properties](#site-configuration-properties)
    - [DATUP Configuration Properties](#datup-configuration-properties)
    - [DATUP Cleanup Script](#datup-cleanup-script)
    - [Deployment](#deployment)
- [Upgrade Installation Instructions](#upgrade-installation-instructions)
  - [Uninstall Previous Release](#uninstall-previous-release)
  - [Deploy New Release](#deploy-new-release)
- [System Verification](#system-verification)
  - [Verification](#verification)

## Project Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goal of the VHA Pharmacy Reengineering (PRE) project is to design and develop a re-engineered pharmacy system, incorporating changes that have been made to the Enterprise Architecture and changes in pharmacy business processes. The intent of the PRE program is to ensure that no current system functionality is lost, but that it is either replicated in the new system or replaced by improved process and functionality. While the overall plan is still based on designing and implementing a complete pharmacy system, the scope of the effort has been defined to address a focused subset of the PRE functionality confined to the Data Update (DATUP) process.

## PRE Project Goals and Objectives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The objective of the PRE project is to facilitate the improvement of pharmacy operations, customer service, and patient safety for the VHA. The PRE project will help address the identified goals and vision for the VHA Pharmacy System.

The goal for the PRE project is a seamless and integrated nationally-supported system that is an integral part of the Health*<u>e</u>*Vet-Veterans Health Information Systems & Technology Architecture (VistA) environment. To meet this goal, the PRE project will enhance pharmacy data exchange, as well as clinical documentation capabilities, in a truly integrated fashion to improve operating efficiency and patient safety. Additionally, it will provide a flexible technical environment to adjust to future business conditions and to meet patient needs in the clinical environment. Achieving this goal will enable resolution of current pharmacy issues, improve patient safety, and facilitate long-term process stability.

## DATUP Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP supports the Medication Order Check Healthcare Application (MOCHA) by performing data source updates. MOCHA conducts order checks using First Databank (FDB) MedKnowledge Framework[^1] within the existing VistA pharmacy application. FDB MedKnowledge Framework is a data product that provides the latest identification and safety information on medications. Additionally, FDB provides the latest algorithms used to perform order checks. DATUP processes the data updates associated with FDB MedKnowledge Framework. The order checks performed by MOCHA include:

- Drug-Drug Order Check – Check interactions between two or more drugs, including interaction monographs.
- Duplicate Therapy Order Check – Check for duplicated drug classifications between two or more drugs.
- Drug-Dose Order Check – Check minimum and maximum single doses, verify the dosing schedule, and provide the normal dosing range.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A complete list of documents relating to the PRE project and the DATUP development effort can be found in the Glossary and Acronym List (Version 5.0, dated September 26, 2008).

# Document Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information contained in this Local Data Update (DATUP) Installation Guide is specific to DATUP development, which supports the MOCHA component. This section defines the layout of this document and provides an outline of the document structure.

## Document Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document details the steps required to install the DATUP software at a local site, the terminology used for the configuration and deployment of the software, and the assumptions for installing the software. Additionally, this document details how to install and configure the database environment. This document accompanies the delivery of the DATUP.v2.0.00.001CM software release. The DATUP Version Description Document (Version 2.0.00.001CM) is delivered as a companion document to this Installation Guide. Refer to the Version Description Document for more information on the software inventory and versions used in the DATUP.v2.0.00.001CM software release.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list provides a brief description of the sections included in this document:

Section 1: Provides introductory material delineating the purpose of the PRE project and the scope of the MOCHA effort

Section 2: Presents an overview of the layout of the document

Section 3: Presents the installation instructions for the DATUP v2.0.00.001CM software release

Section 4: Presents verification steps to verify that the installation was successful

Text in a Courier New font indicates WebLogic Console panels or text, commands, and settings that must be typed, executed, or configured to complete the installation.

*(This page included for two-sided copying.)*

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions detail the steps required to perform a *fresh* installation of the DATUP software at a local site. For *upgrade* installation instructions see Section 4. Section 3.1 details the terminology used for the configuration and deployment of the DATUP software. Section 3.2 outlines the assumptions for installing the DATUP software. While the system may be configured to run outside the given assumptions, doing so requires modifications that are not detailed in this document. Section 3.3 describes how to install and configure the DATUP software properly. Finally, Section 3.3 provides an overview of the Database Server component.

In order to understand the installation and verification process, the reader should be familiar with the WebLogic console shown in Figure 3‑1. The WebLogic console is a Web page viewable from any Internet browser; however, Internet Explorer, Version 7, is recommended. The WebLogic console is generally divided into two sections. The left section contains the Change Center, Domain Structure, and other informational panels. The right section displays panels containing additional options or configuration details. Note: With the exception of the Change Center and Domain Structure references, further references to WebLogic console panels refer to panels in the right section of the WebLogic console.

![](datup-version-2-local-installation-guide/002.png)

<span id="_Ref191089515" class="anchor"></span>Figure ‑. WebLogic Console

## Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In an effort to make these installation instructions as general as possible for installation at any site, a few terms are used throughout the instructions with the intent that they be replaced with site-specific values.

Table 3‑1 contains a list of those terms used only within this document as well as sample site-specific values for each term. Additionally, references to the DATUP-L-1 server may be replaced with the site-specific name of the destination server at the installation site. <span id="_Ref176675115" class="anchor"></span>

Table ‑. Terminology

| Term                                                               | Definition                                                                                                                                                                             | Sample                                 |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Database Server                                                    | Machine on which Caché is installed and runs                                                                                                                                           | DATUP-L-1-DB                           |
| Deployment Machine                                                 | Site-specific machine on which WebLogic is installed and runs                                                                                                                          | DATUP-L-1                              |
| Deployment Server                                                  | WebLogic managed server where DATUP is deployed                                                                                                                                        | LocalPharmacyServer                    |
| Deployment Server Port                                             | Port on which the Deployment Server is listening                                                                                                                                       | 8010                                   |
| Deployment Server’s class path directory                           | Folder location on the Deployment Server where libraries on the class path are located (see WebLogic documentation for instructions on setting a WebLogic managed server’s class path) | /opt/bea/domains/PRE/lib               |
| Java Database Connectivity (JDBC) Universal Resource Locator (URL) | URL to connect to Caché database                                                                                                                                                       | jdbc:Cache://DATUP-l-1-db:1972/FDB_DIF |

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation instructions found within this guide are intended to be performed on a clean installation of WebLogic 10.3, with a separate managed server to act as the Deployment Server. For details on completing the installation of the following items, please refer to each item’s installation and configuration documentation supplied by Oracle.

For successful deployment of the DATUP software at a site, the following assumptions must be met:

- The Deployment Server is configured and running.
- WebLogic is configured to run with the Java™ Standard Edition Development Kit, Version 1.6+.
- Access to the WebLogic console is by means of any valid administrative user name and password.
- The proper Caché database driver libraries for the chosen deployment environment are present on the class path for the respective Deployment Servers.
- Red Hat Enterprise Linux 5.2 operating system is properly installed.
- Domain Name Server (DNS) resolution is configured for the DATUP server.
- The installation instructions are followed in the order that the sections are presented within this Installation Guide.
- FDB-DIF v3.3 database is installed on the Database Server. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project’s Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.

## Database Installation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDB MedKnowledge Framework database used by DATUP requires Caché to be successfully installed. The Caché database has specific installation procedures and files for each operating system. Red Hat Linux must be successfully installed prior to installing the Caché database. A successful installation of a Caché database instance is one in which the installation guide procedures are followed, resulting in an error-free installation.

The installation of the Caché database is described in the Caché Installation Guide, Version 2008.2, Section 4, Installing Caché on UNIX and Linux. The standard installation should be used to install the Caché database server software.

For successful deployment of the DATUP 2.0 software at a site, the FDB-DIF v3.3 database must be installed. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project’s Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.

## WebLogic Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections detail the steps required to configure and deploy DATUP onto WebLogic at a local site.

### Class Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for the Caché JDBC data source to be added to the WebLogic configuration, the Caché JDBC driver must first be added to the Deployment Server’s class path. Use the JDBC driver provided within the Caché distribution and the WebLogic documentation to add the driver to the class path.

The local DATUP Enterprise Application Archive (EAR) file contains all the required libraries for the proper functioning of the application. If any other applications have been deployed to the Deployment Server, there may be conflicting third-party libraries in the Deployment Server's class path that will cause DATUP to operate differently than expected. If versions on the Deployment Server’s class path differ from those defined in the DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010), the preferred solution is to remove the library from the Deployment Server's class path. If that is not possible, replace the libraries with the DATUP versions.

### WebLogic Server Startup Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP requires additional arguments added to the WebLogic Server’s Server Start properties. This section details the steps to add the arguments to the server

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑2.

    ![](datup-version-2-local-installation-guide/003.png)

<span id="_Ref256581857" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑3.

    ![](datup-version-2-local-installation-guide/004.png)

<span id="_Ref256581858" class="anchor"></span>Figure ‑. Change Center

4.  Click on the server name corresponding to the deployment server in the Summary of Servers panel found in the right column of the WebLogic console. For reference, see Figure 3‑4.

    ![](datup-version-2-local-installation-guide/005.png)

<span id="_Ref256581859" class="anchor"></span>Figure ‑. Summary of Servers

5.  WebLogic will now display the panel Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server are set. For reference, see Figure 3‑5.

    ![](datup-version-2-local-installation-guide/006.png)

<span id="_Ref256581860" class="anchor"></span>Figure ‑. Settings for Deployment Server

6.  Click on the Server Start tab.
7.  WebLogic will now display the panel Server Start tab in the Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server are set. For reference, see Figure 3‑6.

    ![](datup-version-2-local-installation-guide/007.png)

<span id="_Ref256581861" class="anchor"></span>Figure ‑. Server Start Tab

8.  Insert the following text in the Arguments box:

    -Xms1024m

    -Xmx1024m

    -XX:PermSize=1024m

    -XX:MaxPermSize=1024m

    -Dweblogic.JobScheduler=true

> Also add a arguments for Log4j file and other Log files. (see for reference below, modify path per your server configuration) :-

> -Dlog4j.configuration=file:/u01/user_proj/domains/PECS/log4j.xml-Dlog4j.logs.dir=servers/NationalPharmacyServer/logs-Dpeps.datup.configuration=/opt/fdb_datup_configuration.properties

9.  Click the Save Button
10. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑7.

    ![](datup-version-2-local-installation-guide/008.png)

<span id="_Ref256581862" class="anchor"></span>Figure ‑. Activate Changes

### Local JDBC Data Source Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses a database connection by means of a data source to DIF in order to perform order checks. Complete the following steps to create a new connection pool and data source for DIF.

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑8.

    ![](datup-version-2-local-installation-guide/009.png)

<span id="_Ref184087883" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑9.

    ![](datup-version-2-local-installation-guide/010.png)

<span id="_Ref184087925" class="anchor"></span>Figure ‑. Change Center

4.  Click New found in the Summary of JDBC Data Sources panel found in the right column of the WebLogic console. For reference, see Figure 3‑10.

    ![](datup-version-2-local-installation-guide/011.png)

<span id="_Ref181416612" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

5.  WebLogic will now display the panel Create a New JDBC Data Source in the right column of the console, where details of the new data source are set. For reference, see Figure 3‑11.

    ![](datup-version-2-local-installation-guide/012.png)

<span id="_Ref191102359" class="anchor"></span>Figure ‑. JDBC Data Source Properties

6.  For the Name, type FDB-DIF.
7.  For the JNDI Name, type datasource/FDB-DIF.
8.  For the Database Type, select Cache.
9.  For the Database Driver, verify that Intersystems’s Cache Driver (Type 4) Versions: Any is selected.
10. Click Next.
11. WebLogic will now display the panel Transaction Options in the right column of the console, where the transaction attributes for this data source are set. For reference, see Figure 3‑12.

    ![](datup-version-2-local-installation-guide/013.png)

<span id="_Ref191089711" class="anchor"></span>Figure ‑. Transaction Options

12. Select the Emulate Two-Phase Commit radio button.
13. Click Next.
14. WebLogic will now display the panel Connection Properties in the right column of the console, where the connection pool attributes are set. For reference, see Figure 3‑13.

    ![](datup-version-2-local-installation-guide/014.png)

<span id="_Ref191089804" class="anchor"></span>Figure ‑. Connection Properties

15. For Database Name, type the name of the Caché database to which DATUP will connect. For example, FDB_DIF.
16. For Host Name, type the name of the machine on which Caché is running. For example, DATUP-L-1-DB.
17. For Port, type the port on which Caché is listening. For example, 1972.
18. For Database User Name, type the user’s name to connect to the FDB database. For example, developer. The user entered should be the same as configured during the FDB database setup using the FDB-DIF Installation/Migration guide. Verify username and password with the DBA.
19. For Password and Confirm Password, type the password for the user given previously. For example, pharmacy.
20. Click Next.
21. WebLogic will now display the panel Test Database Connection in the right column of the console, where the new data source can be tested. For reference, see Figure 3‑14.

    ![](datup-version-2-local-installation-guide/015.png)

<span id="_Ref191089849" class="anchor"></span>Figure ‑. Test Database Connection

22. Leave all values as set by default, with the exception of Test Table Name. For this attribute, type fdb_version.
23. Click Next.
24. WebLogic will now display the panel Select Targets in the right column of the console, where the target server is selected for the new data source. For reference, see Figure 3‑15.

    ![](datup-version-2-local-installation-guide/016.png)

<span id="_Ref191089523" class="anchor"></span>Figure ‑. Select Targets

25. Select the Deployment Server as the target. For example, LocalPharmacyServer.
26. Click Finish.
27. WebLogic will now display the panel Summary of JDBC Data Sources in the right column of the console, where the newly created data source is displayed. For reference, see Figure 3‑16.

    ![](datup-version-2-local-installation-guide/017.png)

<span id="_Ref181418183" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

28. Prepared statement caching will need to be turned off to work around a defect in Cache. To do so, select the newly created data source, FDB-DIF, and navigate to the Connection Pool tab. Change the Statement Cache Size parameter to 0 then click save. For reference, see Figure 3‑17.

![](datup-version-2-local-installation-guide/018.png)

<span id="_Ref258586453" class="anchor"></span>Figure ‑. Statement Cache Size Parameter

29. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑18.

    ![](datup-version-2-local-installation-guide/019.png)

<span id="_Ref193865244" class="anchor"></span>Figure ‑. Activate Changes

### Log4j

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses Log4j to provide debug and error logs. Although the application will function without Log4j installed, using it can be helpful to troubleshoot potential issues. Because DATUP can operate without Log4j configured, all instructions within this section are only required if debugging deployed code.

If the installation of Log4j is desired, the Java Archive (JAR) can be found within the local DATUP EAR, or it can be downloaded from the Internet. Please refer to the DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010) for the version required.

To install Log4j, the Log4j JAR must be placed on the Deployment Server’s class path and the log4j.xml must be edited to include the DATUP appenders and loggers. Complete the following instructions to place the Log4j library on the Deployment Server’s class path. If Log4j is already installed on the Deployment Server, these steps do not need to be completed.

1.  Locate the Deployment Server’s Class Path Directory.
2.  Copy the log4j-1.2.15.jar file into a folder within the class path.
3.  Configure WebLogic to include the Log4j library in the Deployment Server’s class path. Please refer to the WebLogic documentation provided by BEA for completing this step.
4.  Restart the Deployment Server to load Log4j.

With Log4j installed on the Deployment Server, the log4j.xml file must be modified to include the DATUP configuration. Note that the appenders place the logs under a log folder. This folder must be created at the same directory level at which the Deployment Server is running. For example, /opt/bea/domains/PRE/log. Without this folder, Log4j will not be able to create the log files specified in the DATUP configuration. Alternatively, the file locations could be altered to be placed in a different location. Follow the steps below to complete this process:

1.  If Log4j has already been installed, locate the log4j.xml file used for the Deployment Server. Otherwise, create a new log4j.xml file that is either located in a folder on the Deployment Server class path, or use the log4j.configuration Java system property to set the location of the file. Please refer to the WebLogic provided by BEA and Log4j documentation provided by Apache to complete any of these operations.
2.  Add the following configuration to the log4j.xml file:

    \<appender name="PepsAppender" class="org.apache.log4j.RollingFileAppender"\>

    \<param name="File" value="log/peps.log"/\>

    \<param name="Append" value="false"/\>

    \<param name="MaxBackupIndex" value="10"/\>

    \<layout class="org.apache.log4j.PatternLayout"\>

    \<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

    \</layout\>

    \</appender\>

    \<appender name="SpringAppender" class="org.apache.log4j.RollingFileAppender"\>

    \<param name="File" value="log/spring.log"/\>

    \<param name="Append" value="false"/\>

    \<param name="MaxBackupIndex" value="10"/\>

    \<layout class="org.apache.log4j.PatternLayout"\>

    \<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

    \</layout\>

    \</appender\>

    \<logger name="org.springframework" additivity="false"\>

    \<level value="error" /\>

    \<appender-ref ref="SpringAppender"/\>

    \</logger\>

    \<logger name="<span class="mark">REDACTED.pharmacy.peps</span>" additivity="false"\>

    \<level value="error" /\>

    \<appender-ref ref="PepsAppender"/\>

    \</logger\>
3.  If profiling is turned on and should be recorded, add the following configuration to the log4j.xml file:

    \<appender name="ProfileAppender" class="org.apache.log4j.RollingFileAppender"\>

    \<param name="File" value="log/profile.log" /\>

    \<param name="Append" value="false" /\>

    \<param name="MaxBackupIndex" value="10" /\>

    \<layout class="org.apache.log4j.PatternLayout"\>

    \<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c%M\] %m%n" /\>

    \</layout\>

    \</appender\>

    \<logger name="<span class="mark">REDACTED.pharmacy.peps</span>.common.utility.profile" additivity=”false”\>

    \<level value="info" /\>

    \<appender-ref ref="ProfileAppender" /\>

    \</logger\>
4.  Restart the Deployment Server to load the Log4j configuration.

The given Log4j configuration assumes that an existing log4j.xml file is being modified, as the configurations above are only a fragment of a complete Log4j configuration. In particular, the given configuration will only log messages for classes in the org.springframework and <span class="mark">REDACTED.pharmacy.peps</span> packages and sub-packages. No other classes are covered. If additional logging is desired, other logger elements or the root element must be configured. In addition, the given Log4j configuration only logs error-level messages and optionally the info-level profiling messages. For further information, reference http://wiki.apache.org/logging-log4j/Log4jXmlFormat.

*Note: Due to policy constraints, this document cannot support live links. Copy and paste the above link into your browser.*

### Local JMS Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A DATUP local instance is comprised of a JMS module, including the remote JMS server to the DATUP national instance with destinations pointing to the local receive topic, the national receive queue, as well as, a connection factory. Complete the following instructions, in order by section, for each element of the local JMS configuration. These installation instructions must be repeated for each DATUP local site installation.

#### JMS Module

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑19.

    ![](datup-version-2-local-installation-guide/020.png)

<span id="_Ref195512216" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑20.

    ![](datup-version-2-local-installation-guide/021.png)

<span id="_Ref195512217" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑21.

    ![](datup-version-2-local-installation-guide/022.png)

<span id="_Ref195512223" class="anchor"></span>Figure ‑. JMS Modules

5.  Click New.
6.  WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is The following properties will be used to identify your new module, where the new JMS module will be configured. For reference, see Figure 3‑22.

    ![](datup-version-2-local-installation-guide/023.png)

<span id="_Ref195512238" class="anchor"></span>Figure ‑. JMS System Module Properties

7.  For Name, enter a unique name for the new JMS system module. For example, LocalPharmacyJmsModule.
8.  Leave Descriptor File Name and Location In Domain blank.
9.  Click Next.
10. WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is Targets, where the new JMS module will be configured. For reference, see Figure 3‑23.

    ![](datup-version-2-local-installation-guide/024.png)

<span id="_Ref195512256" class="anchor"></span>Figure ‑. JMS System Module Targets

11. For Targets, select the Deployment Server for the DATUP local instance. For example, LocalPharmacyServer-1.
12. Click Next.
13. WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is Add resources to this JMS system module, where the new JMS module will be configured. For reference, see Figure 3‑24.

    ![](datup-version-2-local-installation-guide/025.png)

<span id="_Ref195512273" class="anchor"></span>Figure ‑. Add Resources to JMS System Module

14. Leave the Would you like to add resources to this JMS system module? check box unchecked.
15. Click Finish.
16. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑25.

    ![](datup-version-2-local-installation-guide/026.png)

<span id="_Ref195512291" class="anchor"></span>Figure ‑. Activate Changes

#### Foreign JMS Server

1.  Open and log on to the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑26.

    ![](datup-version-2-local-installation-guide/027.png)

<span id="_Ref193978393" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑27.

    ![](datup-version-2-local-installation-guide/028.png)

<span id="_Ref193978412" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑28.

    ![](datup-version-2-local-installation-guide/029.png)

<span id="_Ref193978431" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in the JMS Module section. For example, LocalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for LocalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑29.

    ![](datup-version-2-local-installation-guide/030.png)

<span id="_Ref193978452" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click New.
8.  WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Choose the type of resource you want to create, where the JMS module will be further configured. For reference, see Figure 3‑30.

    ![](datup-version-2-local-installation-guide/031.png)

<span id="_Ref193981712" class="anchor"></span>Figure ‑. Choose Type of Resource to Create

9.  Select Foreign Server.
10. Click Next.
11. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Foreign Server Properties, where the JMS module will be further configured. For reference, see Figure 3‑31.

    ![](datup-version-2-local-installation-guide/032.png)

<span id="_Ref193977655" class="anchor"></span>Figure ‑. Foreign Server Properties

12. For Name, enter a unique name for the foreign server. For example, RemoteNationalPharmacyJmsServer.
13. Click Next.
14. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Foreign Server Properties, where the JMS module will be further configured. For reference, see Figure 3‑32.

    ![](datup-version-2-local-installation-guide/033.png)

<span id="_Ref193981734" class="anchor"></span>Figure ‑. Foreign JMS Server Target

15. For Targets, verify that the target chosen is the WebLogic server for this DATUP installation.
16. Click Finish.
17. WebLogic will now display the panel Settings for LocalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑33.

    ![](datup-version-2-local-installation-guide/034.png)

<span id="_Ref193981761" class="anchor"></span>Figure ‑. Summary of Resources

18. Click on the link for the foreign JMS server just created. For example, RemoteNationalPharmacyJmsServer.
19. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Configuration - General, where the JMS module will be further configured. For reference, see Figure 3‑34.

    ![](datup-version-2-local-installation-guide/035.png)

<span id="_Ref193981790" class="anchor"></span>Figure ‑. Foreign JMS Server General Configuration

20. For JNDI Connection URL, enter the URL to the National Deployment Server. For example, t3://test-datup-n:8021.
21. Leave the default values for the remaining settings JNDI Properties Credential, Confirm JNDI Properties Credential, JNDI Properties, and Default Targeting Enabled.
22. Click Save.
23. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑35.

    ![](datup-version-2-local-installation-guide/036.png)

> <span id="_Ref193978131" class="anchor"></span>Figure ‑. Activate Changes

#### Destination

1.  Open and log on to the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑36.

    ![](datup-version-2-local-installation-guide/037.png)

<span id="_Ref271266366" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑37.

    ![](datup-version-2-local-installation-guide/038.png)

<span id="_Ref271266392" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑38.

    ![](datup-version-2-local-installation-guide/039.png)

<span id="_Ref271266409" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in the JMS Module section. For example, LocalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for LocalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑39.

    ![](datup-version-2-local-installation-guide/040.png)

<span id="_Ref271266425" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click on the link for the foreign JMS server created in the Foreign JMS Server section. For example, RemoteNationalPharmacyJmsServer.
8.  WebLogic will now display the panel Settings for RemoteNationalPharmacyJms  
    Server in the right column of the console. Within the panel is Configuration - General, where the JMS module will be further configured. For reference, see Figure 3‑40.

    ![](datup-version-2-local-installation-guide/041.png)

<span id="_Toc389565184" class="anchor"></span>Figure ‑. Foreign JMS Server General Configuration

9.  Select the Destinations tab.
10. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Foreign Destinations Configuration, where the JMS module will be further configured. For reference, see Figure 3‑41.

    ![](datup-version-2-local-installation-guide/042.png)

<span id="_Ref271266475" class="anchor"></span>Figure ‑. Destinations

11. Click New.
12. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Foreign Connection Factory Properties, where the JMS module will be further configured. For reference, see Figure 3‑42.

    ![](datup-version-2-local-installation-guide/043.png)

<span id="_Ref271266551" class="anchor"></span>Figure ‑. Foreign Connection Factory Properties

13. For Name, enter a unique name for the foreign JMS Destination. For example, DatupDestination
14. For Local JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/queue/national/  
    datup/receive.
15. For Remote JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/queue/national/  
    datup/receive.
16. Click OK.
17. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑43.

    ![](datup-version-2-local-installation-guide/044.png)

<span id="_Ref271266563" class="anchor"></span>Figure ‑. Activate Changes

#### Connection Factory

1.  Open and log on to the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑44.

    ![](datup-version-2-local-installation-guide/045.png)

<span id="_Ref193981831" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑45.

    ![](datup-version-2-local-installation-guide/046.png)

<span id="_Ref193981847" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑46.

    ![](datup-version-2-local-installation-guide/047.png)

<span id="_Ref193981888" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in the JMS Module section. For example, LocalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for LocalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑47.

    ![](datup-version-2-local-installation-guide/048.png)

<span id="_Ref193981910" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click on the link for the foreign JMS server created in the Foreign JMS Server section. For example, RemoteNationalPharmacyJmsServer.
8.  WebLogic will now display the panel Settings for RemoteNationalPharmacyJms  
    Server in the right column of the console. Within the panel is Configuration - General, where the JMS module will be further configured. For reference, see Figure 3‑48.

    ![](datup-version-2-local-installation-guide/049.png)

<span id="_Ref193978585" class="anchor"></span>Figure ‑. Foreign JMS Server General Configuration

9.  Select the Connection Factories tab.
10. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Connection Factories Configuration, where the JMS module will be further configured. For reference, see Figure 3‑49.

    ![](datup-version-2-local-installation-guide/050.png)

<span id="_Ref193979224" class="anchor"></span>Figure ‑. Foreign JMS Server Connection Factories

11. Click New.
12. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Foreign Connection Factory Properties, where the JMS module will be further configured. For reference, see Figure 3‑50.

    ![](datup-version-2-local-installation-guide/051.png)

<span id="_Ref193979563" class="anchor"></span>Figure ‑. Foreign Connection Factory Properties

13. For Name, enter a unique name for the foreign connection factory. For example, DatupConnectionFactory.
14. For Local JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/factory.
15. For Remote JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/factory.
16. Click OK.
17. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑51.

    ![](datup-version-2-local-installation-guide/052.png)

<span id="_Ref193979715" class="anchor"></span>Figure ‑. Activate Changes

### Site Configuration Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to filter FDB drug-drug interactions replaced by custom VA drug-drug interactions, the fdb_custom_ddimstrings FDB-DIF table must be populated with a mapping between the FDB-DIF interaction to be replaced and the custom VA drug-drug interaction. One attribute of this mapping is a configurable category code, with a default of FDB_ID. A file, <span class="mark">REDACTED.pharmacy.peps</span>.siteConfig.properties, can be placed within a folder on the Deployment Server’s class path in order to override this default. Follow the BEA WebLogic documentation for adding folders to a server’s class path. Each property is set via a key/value pair. For example, fdb.id.category=FDB_ID, where fdb.id.category is the key and FDB_ID is the value. Table 3‑2 defines the optional property.

| Key             | Definition                                                                                                                                          | Sample |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| fdb.id.category | Category code used within the fdb_custom_ddimstrings table for mapping FDB-DIF drug-drug interactions replaced by custom VA drug-drug interactions. | FDB_ID |

### DATUP Configuration Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use the DATUP component, a configuration file must be configured for each WebLogic deployment. The location of this file was configured in Section 3.4.2 and is by default fdb_datup_configuration.properties. This file is self documenting and contains the list of configurable properties for DATUP. See Appendix A for a sample version.

### DATUP Cleanup Script

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP creates temporary zip files during the update process. A script has been provided in the /scripts/datupcleanup.sh file. This file provides a template to remove any files that DATUP creates during the update process. If the bash interpreter is not located at /bin/bash or the system’s default temporary directory is not located at /tmp, the script file must be updated, comments in the example file show which lines to change.

To automate this process using the CRON scheduler, copy the file to the /etc/cron.weekly/ directory for weekly execution. If you wish this script to run more often, it can be copied to the /etc/cron.daily/ directory for daily execution. The script must be given execution permissions, so the command chmod 755 datupcleanup.sh must also be run on the command line.

### Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the deployment of the DATUP application at a local site. Prior to completing these steps, the WebLogic class path, the WebLogic database configurations, and the Deployment Server must be restarted to load the changed configuration. Please refer to Sections 3.4.1 and 0 for instructions concerning these configuration items. Complete the following steps to deploy DATUP:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 3‑52.

    ![](datup-version-2-local-installation-guide/053.png)

<span id="_Ref178735721" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑53.

    ![](datup-version-2-local-installation-guide/054.png)

<span id="_Ref181421187" class="anchor"></span>Figure ‑. Change Center

4.  Click Install found in the Deployments panel in the right column of the WebLogic console. For reference, see Figure 3‑54.

    ![](datup-version-2-local-installation-guide/055.png)

<span id="_Ref178732223" class="anchor"></span>Figure ‑. Deployments

5.  WebLogic will now display the panel Install Application Assistant in the right column of the console, where the location of the DATUP deployment will be found. For reference, see Figure 3‑55.

    ![](datup-version-2-local-installation-guide/056.png)

<span id="_Ref178732382" class="anchor"></span>Figure ‑. Install Application Assistant

6.  Select the DATUP deployment, select the DATUP.local.2.0.00.001CM.ear file. Replace the release number for the current release.
    1.  If the DATUP deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the Location panel within the Install Application Assistant in the right column of the console. For reference, see Figure 3‑56.

        ![](datup-version-2-local-installation-guide/057.png)

<span id="_Ref184090181" class="anchor"></span>Figure ‑. Locate Deployment to Install and Prepare for Deployment

2.  If the DATUP deployment has not been transferred to the Deployment Machine:
    1.  Click on the upload your file(s) link in the Install Application Assistant panel in the right section of the console. For reference, see Figure 3‑56.
    2.  Click the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
    3.  Click Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the Locate deployment to install and prepare for deployment panel within the Install Application Assistant. For reference, see Figure 3‑57.

        ![](datup-version-2-local-installation-guide/058.png)

<span id="_Ref184090012" class="anchor"></span>Figure ‑. Upload a Deployment to the Admin Server

7.  Once the DATUP deployment is located and selected, click Next.
8.  WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, Install this deployment as an application, and click Next. For reference, see Figure 3‑58.

    ![](datup-version-2-local-installation-guide/059.png)

<span id="_Ref176676787" class="anchor"></span>Figure ‑. Choose Targeting Style

9.  Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step. For reference, see Figure 3‑59.

    ![](datup-version-2-local-installation-guide/060.png)

<span id="_Ref191090118" class="anchor"></span>Figure ‑. Select Deployment Targets

10. For the Target, select the Deployment Server. For example, LocalPharmacyServer.
11. Click Next.
12. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen. For reference, see Figure 3‑60.

    ![](datup-version-2-local-installation-guide/061.png)

<span id="_Ref191090176" class="anchor"></span>Figure ‑. Optional Settings

13. Enter the Name for the deployment. For example, Local DATUP.
14. Verify that the following default option for Security is selected:

    DD Only: Use only roles and policies that are defined in the deployment descriptors.
15. Verify that the following default option for Source accessibility is selected:

    Use the defaults defined by the deployment's targets.
16. Click Next.
17. Within the Install Application Assistant in the right column of the console WebLogic will now display the panel Review your choices and click Finish, which summarizes the steps completed above. For reference, see Figure 3‑61.

    ![](datup-version-2-local-installation-guide/062.png)

<span id="_Ref191090260" class="anchor"></span>Figure ‑. Review Your Choices and Click Finish

18. Verify that the values match those entered in Steps 1 through 17 and click Finish.
19. WebLogic will now display the panel Settings for Local DATUP, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order. For reference, see Figure 3‑62.

    ![](datup-version-2-local-installation-guide/063.png)

<span id="_Ref191090327" class="anchor"></span>Figure ‑. Settings for DATUP

20. Leave all the values as defaulted by WebLogic and click Save.
21. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑63.

    ![](datup-version-2-local-installation-guide/064.png)

<span id="_Ref178733999" class="anchor"></span>Figure ‑. Activate Changes

22. Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 3‑64.

    ![](datup-version-2-local-installation-guide/065.png)

<span id="_Ref181421306" class="anchor"></span>Figure ‑. Domain Structure

23. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 3‑65.

    ![](datup-version-2-local-installation-guide/066.png)

<span id="_Ref191090401" class="anchor"></span>Figure ‑. Summary of Deployments

24. Select the previously deployed DATUP deployment, click Start, and then select Servicing all requests from the drop-down list box.
25. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 3‑66.

    ![](datup-version-2-local-installation-guide/067.png)

<span id="_Ref191090464" class="anchor"></span>Figure ‑. Start Application Assistant

26. Click Yes in the Start Application Assistant panel in the right column of the WebLogic console.
27. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 3‑67.

    ![](datup-version-2-local-installation-guide/068.png)

<span id="_Ref191090529" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Active

28. Verify that the State of the DATUP deployment is Active.

    *(This page included for two-sided copying.)*

# Upgrade Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions detail the steps required to perform an installation of a release for the DATUP software, when an existing release is already deployed at a local site. These steps assume a fresh installation has been completed, following the steps in Section 3.

## Uninstall Previous Release 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the un-installation of the DATUP application. Prior to completing these steps, the DATUP application must have been deployed following the steps in Section 3. Complete the following steps to un-deploy DATUP at a local site:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 4‑1.

    ![](datup-version-2-local-installation-guide/069.png)

<span id="_Ref246231865" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 4‑2.

    ![](datup-version-2-local-installation-guide/070.png)

<span id="_Ref246231871" class="anchor"></span>Figure ‑. Change Center

4.  WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 4‑3.

    ![](datup-version-2-local-installation-guide/071.png)

<span id="_Ref246231328" class="anchor"></span>Figure ‑. Summary of Deployments – Stopping DATUP

5.  Select the previously deployed DATUP deployment, click Stop, and then select Force Stop Now from the drop-down list box.
6.  WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 4‑4.

    ![](datup-version-2-local-installation-guide/072.png)

<span id="_Ref246231887" class="anchor"></span>Figure ‑. Force Stop Application Assistant

7.  Click Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
8.  WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 4‑5.

    ![](datup-version-2-local-installation-guide/073.png)

<span id="_Ref246231898" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Prepared

9.  Verify that the State of the DATUP deployment is Prepared.
10. Select the previously deployed DATUP deployment, and then click Delete.
11. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 4‑6.

    ![](datup-version-2-local-installation-guide/074.png)

<span id="_Ref246231908" class="anchor"></span>Figure ‑. Delete Application Assistant

12. Click Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
13. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 4‑7.

    ![](datup-version-2-local-installation-guide/075.png)

<span id="_Ref246231916" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Deleted

14. Verify that the DATUP deployment is deleted and no longer present.
15. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 4‑8.

    ![](datup-version-2-local-installation-guide/076.png)

<span id="_Ref246231924" class="anchor"></span>Figure ‑. Activate Changes

## Deploy New Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy the new release, follow the same deployment steps found in Section 3.4.9.

*(This page included for two-sided copying.)*

# System Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section will verify that the DATUP system is up and running at a local site.

## Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that a DATUP installation is up and running at a local site, navigate a web-browser to the logs directory on the server, for example, http://datup-l-1/logs/LocalDatupServer/logs.

Verify that the server.log file has an entry indicating the next scheduled run time for the DATUP application. The server.log entry looks like:

DEBUG \[<span class="mark">REDACTED.pharmacy.peps</span>.updater.common.utility.DifUpdateScheduler:scheduleNextTimer\] Next scheduled DIF update time: Thu, 08/26/2010, 02:45:00 PM, CDT

This line indicates that the system is running.

*(This page included for two-sided copying.)*

<span id="_Toc389565141" class="anchor"></span>Appendix A

<span id="_Toc389565142" class="anchor"></span>Local DATUP Configuration

This appendix provides a configuration file example for a local site based on the baseline fdb_datup_configuration.properties file located on the delivery CD in the /configuration directory.

Example DATUP Configuration Properties for a Local Site

\###################################################

\#------------------- Scheduler -------------------

\###################################################

\###################################################

\# Scheduled nightly update time (military time).

\#

\# For example, "0230" schedules the nightly update

\# for 2:30 am.

\#

\# \*This parameter applies to National and Local.

\###################################################

scheduled.time=1405

\###################################################

\#------------------- FTP Server -------------------

\###################################################

\###################################################

\# FTP server hostname

\#

\# Specify the anonymous FTP server hostname.

\#

\# \*This parameter applies to National and Local.

\###################################################

ftp.hostname=<span class="mark">REDACTED</span>

\###################################################

\# FTP server port number

\#

\# Specify the anonymous FTP server port number.

\#

\# \*This parameter applies to National and Local.

\###################################################

ftp.port=21

\###################################################

\# FTP server username/password.

\#

\# Specify the anonymous account username/password.

\#

\# \*These parameters apply to National and Local.

\###################################################

ftp.username=PECS

ftp.password=

\###################################################

\# FTP server working directory

\#

\# Specify the FTP working directory, relative to

\# the FTP root directory.

\#

\# \*This parameter applies to National and Local.

\###################################################

ftp.directory.working=pharmacy_uft

\###################################################

\# Pending FDB-DIF update storage directory.

\#

\# Specify the pending directory, relative to the

\# working directory, to the location where FDB-DIF

\# full, incremental, and custom ZIP files will be

\# placed for processing.

\#

\# \*This parameter applies to National.

\###################################################

ftp.directory.pending=fdb_dif

\###################################################

\#------------------- FDB DIF ---------------------

\###################################################

\###################################################

\# Number of random FDB-DIF verification tests

\#

\# Specify the number of random FDB-DIF verification

\# tests to run. 10 is a reasonable number. However,

\# do not specify a large number as it will cause an

\# unacceptable delay for processing new VistA order

\# checks during that time.

\#

\# \*This parameter applies to National and Local.

\###################################################

fdb.verification.test.count=5

\###################################################

\#------------------- Email Server -----------------

\###################################################

\###################################################

\# Email server hostname

\#

\# \*This parameter applies to National and Local.

\###################################################

email.hostname=SMTP.VA.GOV

\###################################################

\# Email sender name

\#

\# For example, "noreply@va.gov".

\#

\# \*This parameter applies to National and Local.

\###################################################

email.sender=noreply_national_DATUP1.1_sqa@<span class="mark">REDACTED</span>

\###################################################

\# Email username/password

\#

\# May be necessary to relay email.

\#

\# \*These parameters apply to National and Local.

\###################################################

email.username=

email.password=

\###################################################

\# Email list for success notifications

\#

\# Include individuals that should be notified about

\# successful FDB/FDB-Custom updates.

\#

\# \*This parameter applies to National and Local.

\###################################################

email.list.success=SDDPREArch@<span class="mark">REDACTED</span>

\###################################################

\# Email list for failure notifications

\#

\# Include individuals that should be notified about

\# failed FDB/FDB-Custom updates.

\#

\# \*This parameter applies to National and Local.

\###################################################

\#email.list.failure=<span class="mark">REDACTED</span>

email.list.failure=SDDPREArch@<span class="mark">REDACTED</span>

\###################################################

\# Email list for available update notifications

\#

\# Include individuals that should be notified about

\# available FDB/FDB-Custom updates once they are

\# applied and tested and National. This list should

\# include the local site managers.

\#

\# \*This parameter applies to National.

\###################################################

email.list.update.available=SDDPREArch@<span class="mark">REDACTED</span>

\###################################################

\#------------------- Locality -----------------

\###################################################

\###################################################

\# Regional Data Center (RDC) name

\#

\# Specify the name of the RDC or leave blank if

\# this installation is not part of a RDC.

\#

\# \*This parameter applies to Local.

\###################################################

locality.rdc.name=

\###################################################

\# Site number(s)

\#

\# Specify the site number(s) for this installation.

\# If more than one site is associated with this

\# installation, separate the site numbers with a

\# comma (e.g., 423,512,211).

\#

\# \*This parameter applies to Local.

\###################################################

locality.site.number=

\###################################################

\# Number of retained FDB-DIF incremental archives

\#

\# Due to potential site outages, it is necessary

\# to retain a certain number of FDB-DIF archives.

\#

\# \*This parameter applies to National.

\###################################################

fdb.retention=20

\###################################################

\# Number of statements to batch before commit

\#

\# Specify the number of statements to batch before

\# a commit to the database. This value is database

\# vendor and JDBC driver dependent. A reasonable

\# batch size is 500. However, tests show that Cache

\# may throw system errors with a batch size greater

\# than 200.

\#

\# Specify a batch size of 0 to disable batching. A

\# single commit will be issued at the end of the

\# incremental update.

\#

\# \*This parameter applies to National and Local.

\###################################################

fdb.batch.commit.size=0

\###################################################

\#------------------- IMAGE PROCESSING--------------

\#This parameter specifies if Images will be processed

\#or not.

\#The Parameter is “TRUE” for National and “FALSE” for

\#LOCAL by default.

\###################################################

image.processing.national=TRUE

image.processing.local=FALSE

\###################################################

\# The location where the image files will be stored

\#

\#

\# \*This parameter applies to National only

\###################################################

image.directory.national=/tmp/imaging/

\###################################################

\# The location where the image files will be stored

\#

\#

\# \*This parameter applies to local only

\###################################################

image.directory.local=/tmp/imaging/

\###################################################

\# The email to send to names or group for Image

\#Procesing.

\#This parameter can be blank

\#

\# \*This parameter applies to National only

\###################################################

image.email.sendto.national=

\#image.email.sendto.national=SDDPREArch@<span class="mark">REDACTED</span>

\#image.email.sendto.national=<span class="mark">REDACTED</span>

\###################################################

\# The email to send to names or group for Image

\#Processing

\#This parameter can be blank

\#This parameter applies to local only

\###################################################

image.email.sendto.local=SDDPREArch@<span class="mark">REDACTED</span>

<span id="_Toc389565143" class="anchor"></span>Appendix B

<span id="_Toc389565144" class="anchor"></span>Combined DATUP / PECS Architecture

This appendix provides the combined DATUP / PECS architecture diagram for reference. The combined logical system components are:

1.  DATUP – Implements the FDB-DIF update business logic.
2.  Scheduler – Background process for scheduling DATUP.
3.  WebLogic – Application server environment.
4.  Configuration File – Defines the DATUP configuration settings.
5.  Email Templates – Templated emails for notifications sent to National/Local Managers.
6.  Anonymous FTP Server – FTP Server that hosts the FDB-DIF update archives.
7.  Email Server – Email relay server.
8.  PECS – Implements the FDB-Custom drug business logic.
9.  CT Staging Database – Stores PECS FDB-Custom modifications.
10. DATUP Database – Stores DATUP site update history.
11. FDB-DIF Database – Stores the FDB-DIF drug database.
12. Legacy VistA – Existing VistA server.

Figure B−1 illustrates the logical system components for the National and Local environments. The National components are responsible for verifying and publishing FDB-DIF and FDB-Custom updates to the Anonymous FTP Server. The Local components then consume and apply the verified updates in an automated manner.

![](datup-version-2-local-installation-guide/077.png)

<span id="_Toc389565220" class="anchor"></span>Figure B‑: Combined DATUP/PECS Architecture Diagram

[^1]: At the time of development, this product was known as FDB Drug Information Framework (commonly abbreviated as FDB-DIF). The references to FDB-DIF in this manual are necessary due to previously completed code and instructions that could not be changed to match the new product name.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DATUP Version 3.0.01 Local Installation Guide

## Backout Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out the current DATUP build, follow the steps in Section 4.1 to uninstall the build. Then, follow the steps in Section 3.4.7 to deploy the previous build.

*(This page included for two-sided copying.)*
