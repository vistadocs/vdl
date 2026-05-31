---
title: DATUP DIBR - PRED*3*6
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: null
app_code: PRED
app_name: 'Pharmacy: Pharmacy Data Update (DATUP)'
section: GUI
app_status: active
pkg_ns: PRED
patch_ver: 3.2
patch_id: PRED*3.2
group_key: PRED:PRED:3.2
file_numbers: []
security_keys: []
menu_options: 0
description: Deployment, Installation, Back-Out, and Rollback Guide
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 1003
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: January 2024
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/PRED_3_2_01_P6_dibr.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/PRED_3_2_01_P6_dibr.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=203
audit_applied: '2026-05-31'
master_source: DATUP DIBR - PRED*3*6
master_pub_date: January 2024
consolidated_from: 3 versions
prior_versions:
- DATUP DIBR - PRED*3*3
- DATUP DIBR - PRED*3*7
consolidated_title: datup dibr
---

Data Update (DATUP) 3.2.01

Deployment, Installation, Back-Out, and Rollback Guide (DIBR)

![](datup-dibr-pred-3-6/001.png)

January 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 49%" />
<col style="width: 20%" />
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
<td>01/23/2024</td>
<td>4.0</td>
<td><p>PRED*3*6:</p>
<p>upgrade Log4j version from 2.19.0 to</p>
<p>2.20.0, upgraded to ESAPI version from 2.4.0 to 2.5.2.0 and upgraded to Apache Commons Collections from 3.2.1 to 4.4</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>02/13/2023</td>
<td>3.0</td>
<td><p>PRED*3*5:</p>
<p>Upgraded Log4j2 verion 2.19.0</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>03/18/2022</td>
<td>2.0</td>
<td><p>PRED*3*4:</p>
<ul>
<li><p>Updated DATUP version to 3.1.02</p></li>
<li><p>Upgraded Log4j2 verion 2.17.1</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>03/15/2021</td>
<td>1.0</td>
<td><p>PRED*3*3:</p>
<ul>
<li><p>Updated DATUP version to 3.1.01</p></li>
<li><p>Updated Log4j version to Log4j2</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
</tbody>
</table>

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Guide for new patches going into the VA Enterprise. The guide includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Guide is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
- [Deployment](#deployment)
  - [Deployment Steps:](#deployment-steps)
- [Installation](#installation)
- [Back-Out Procedure](#back-out-procedure)
  - [Backout Process:](#backout-process)
    - [Prerequisites:](#prerequisites)
    - [Backout Steps:](#backout-steps)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback](#rollback)
This document describes how to deploy and install the patch PRED\*3\*6 for the Pharmacy Reengineering (PRE) DATUP application, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial off-the-shelf (COTS) product is being installed, the vendor provided User and Installation guide may be used, but the back-out recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the DATUP application patch, PRED\*3\*6, will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for deployment, back-out, and rollback are included in this document.

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP will only be installed on national pharmacy re-engineering servers and will be done by AITC/PITC support staff. No site installation is necessary.

- Prerequisite: Download the datup-national-3.2.01.0001zip. If needed, contact the HPSCLIN team at Liberty IT Solutions for file location or installation assistance.
- Zip file includes following files for EAR file deployment:
  - datup-national-3.2.01.0001.ear
- Backup Classpath and Arguments at current Server Startup in Weblogic console

## Deployment Steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  (SA) unzip datup-national-3.2.01.0001.zip.
2.  Follow the steps in section 3.4, Deployment.

> Or

1.  Shutdown WebLogic servers

> <u>EAR File Deployment:</u>

2.  Backup 3.1.03.0001.ear from WebLogic
3.  Backup log4j-api-2.19.0.jar and log4j-core-2.19.0.jar
4.  Backup esapi-2.1.0.jar
5.  Replace log4j-api-2.20.0.jar and log4j-core-2.20.0.jar
6.  Replace esapi-2.5.2.0.jar
7.  Deploy datup-national-3.2.01.0001.ear
8.  Restart the servers
9.  Smoke Test Weblogic.
10. Validate deployment successful.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation is not applicable for PRED\*3\*6, because this is a patch-specific deployment.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backout plan will be executed if deployment fails functional testing and cannot be remediated immediately.

## Backout Process:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Prerequisites: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Previous datup-national-3.1.03.0001 still exists in installation directory along with log4j-1.2-api-2.19.0.jar at /lib/ folder where WebLogic is installed
- For Example, - /u01/app/oracle/user_projects/domains/pecs_production/lib.
- Replace Classpath and Arguments at server start in weblogic from backup.

### Backout Steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Uninstall previous release as per section 4.1, Uninstall Previous Release of the, PRED_3_1_03_P3_IGN.DOCX.

1.  Delete datup-national-3.2.03.0001.ear
2.  Delete log4j-api-2.20.0.jar and log4j-core-2.20.0.jar
3.  Delete esapi-2.5.2.0.jar
4.  Replace log4j-api-2.19.0.jar and log4j-core-2.19.0.jar
5.  Replace esapi-2.1.0.jar
6.  Deploy datup-national-3.1.03.0001.ear
7.  Smoke Test WebLogic.
8.  Validate backout successful

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the national DATUP installation is up and running, navigate a web-browser to the logs directory on your server. example: /u01/app/OracleHome/user_projects/domains/ppsn/DATUPLOGS

Verify that the server.log file has an entry indicating the next scheduled run time of the DATUP application.

Example:

DEBUG \[<span class="mark">REDACTED</span>pharmacy.peps.updater.common.utility.DifUpdateScheduler:scheduleNextTimer\] Next scheduled DIF update time: Fri, 12/29/2023, 09:30:00 PM, CDT

This line indicates that the system is running.

# Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable because there is no data update for PRED\*3\*6.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DATUP DIBR - PRED*3*3

### Backout Steps for LOG4J:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Shutdown WebLogic servers
2.  Restore the old log4j jar file log4j-1.2.17.jar
3.  Replace the existing log4j2.xml with the old log4j.properties
4.  Update the Arguments and Class Path for old log4j.xml file and logs
5.  Restart the servers
