---
title: MOCHA Server Version 3.1 DIBR (Updated with PREM*3*2)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: DIBR (Updated with PREM*3*2)
app_code: PREM
app_name: "Pharmacy: Medication Order Check Healthcare Application (MOCHA)"
section: GUI
app_status: active
pkg_ns: PREM
patch_ver: 3.1
patch_id: PREM*3.1
group_key: "PREM:PREM:3.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - deployment
  - weblogic
  - table
  - console
  - panel
  - mocha
  - contents
  - column
  - back
  - right
page_count: 0
word_count: 1977
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Medication_Order_Check_HC_Applic/prem_3_p2_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Medication_Order_Check_HC_Applic/prem_3_p2_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=201"
---

---
title: |
  <span id="_top" class="anchor"></span>Medication Order Check Healthcare Application Server 3.1 (MOCHA Server 3.1)

  Deployment, Installation, Back-Out, and Rollback Guide (DIBR)
---

![](mocha-server-version-3-1-dibr-updated-with-prem-3-2/001.png)

October 2020

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 49%" />
<col style="width: 24%" />
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
<td>10/22/2020</td>
<td>1.0</td>
<td><p>PREM*3*2:</p>
<ul>
<li><p>Deployment, Installation, Back-out, and Rollback Guide for MOCHA patch</p></li>
</ul>
<p><strong>(VA Security and Code Quality Standards and Technical Reference Model Compliance)</strong></p></td>
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
    - [Backout Steps for EAR file:](#backout-steps-for-ear-file)
    - [Backout Steps for LOG4J:](#backout-steps-for-log4j)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback](#rollback)
This document describes how to deploy and install the various components of the patch PREM\*3\*2 for the Medication Order Check Healthcare Application (MOCHA) Server, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial Off-the-Shelf (COTS) product is being installed, the vendor provided User and Installation guide may be used, but the back-out recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the MOCHA server patch, PREM\*3\*2, will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. This guide also identifies resources, communications plan, and rollout schedule. Specific instructions for deployment, back-out, and rollback are included in this document.

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prerequisites:

Provide mocha 3.1.00.0000.zip file to AITC team. The zip file includes following files for ear file deployment and log4j2 upgrade:

- mocha-server-3.1.00.0000.ear
- log4j2.xml
- log4j-api-2.10.0.jar
- log4j-core-2.10.0.jar

## Deployment Steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Shutdown WebLogic servers.
2.  Deploy ear files:
    1.  Delete mocha-server-3.0.00.0028.ear from WebLogic
    2.  Deploy mocha-server-3.1.00.0000.ear
3.  Migrate to log4j2.
    1.  Backup the old log4j jar files:
        1.  log4j-1.2.15.jar
    2.  Replace the old log4j jar file with the new version of jar files:
        1.  log4j-api-2.10.0.jar
        2.  log4j-core-2.10.0.jar
4.  Backup the log4j.properties.
5.  Replace the existing log4j.properties with the new log4j2.xml.
6.  Update the Arguments and Class Path with the latest log4j2.xml file and log4j2 library version.
7.  Remove the argument:

> \-Dlog4j.logs.dir=/u01/app/oracle/user_projects/domains/moc-prod/logs

8.  Restart the servers.
9.  Smoke test Weblogic.
10. Validate deployment successful.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation is not applicable for PREM\*3\*2, because this is a patch-specific deployment.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backout plan will be executed if deployment fails functional testing and cannot be remediated immediately.

## Backout Process:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Prerequisites: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous mocha-server-3.0.00.0028.ear and old log4j files still exist in installation directory.

### Backout Steps for EAR file:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Delete mocha-server-3.1.00.0000.ear *(refer to section 4.1.2.1 for detailed steps for removing the new ear files)*.
2.  Deploy 3.0.00.0028*.*ear *(refer section 4.1.2.2 for detailed steps for deploying old ear files)*.
3.  Smoke Test WebLogic.
4.  Validate backout was successful.

#### Remove New Release:

1.  Open and log into the WebLogic console.Use WebLogic username and password.
2.  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3.  Within the *Change Center* panel in the left column of the WebLogic console, select Lock & Edit.
4.  WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
5.  Select the previously deployed MOCHA deployment, select Stop, and then select Force Stop Now from the drop-down list.
6.  WebLogic will now display the panel *Force Stop Application Assistant* in the right column of the console for confirmation to start servicing requests.
7.  Select Yes in the *Force Stop Application Assistant* panel in the right column of the WebLogic console.
8.  WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
9.  Verify that the State of the MOCHA deployment is Prepared.
10. Select the previously deployed MOCHA deployment, and then select Delete.
11. WebLogic will now display the panel *Delete Application Assistant* in the right column of the console for confirmation to start servicing requests.
12. Select Yes in the *Delete Application Assistant* panel in the right column of the WebLogic console.
13. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
14. Verify that the MOCHA deployment is deleted and no longer present.

#### Deploy Rolled-Back Release:

The following steps detail the deployment of the rolled-back MOCHA application.

1.  Use the WebLogic console that was started at the beginning of the roll-back process.
2.  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3.  Verify that the application is in Lock & Edit mode. Lock & Edit mode is indicated by the greyed-out Lock & Edit selection button.
4.  Select the Install button in the *Deployments* panel in the right column of the WebLogic console.
5.  WebLogic will now display the panel *Install Application Assistant* in the right column of the console, where the location of the MOCHA deployment will be found.
    1.  If the rolled-back MOCHA deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the *Location* panel, which is within the *Install Application Assistant* panel in the right column of the console. Choose the ear file associated with the rolled-back release.
    2.  If the rolled-back MOCHA deployment has not been transferred to the Deployment Machine:
        1.  Select on the upload your file(s) link in the *Install Application Assistant* panel in the right section of the console.
        2.  Select the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
        3.  Select Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the *Locate deployment to install and prepare for deployment* panel within the *Install Application Assistant*.
6.  Once the rolled-back MOCHA deployment is located and selected, select Next.
7.  WebLogic will now display the panel *Choose targeting style* within the *Install Application Assistant* in the right column of the console. Leave the default value selected, install this deployment as an application, and select Next.
8.  Within the *Install Application Assistant* in the right column of the console, WebLogic will now display the panel *Select deployment targets*, where the Deployment Server will be selected as the target in the next step.
9.  For the Target, select the Deployment Server.
10. Select Next.
11. Within the *Install Application Assistant*, WebLogic will now display the panel *Optional Settings* in the right column of the console, where the name of the deployment and the copy behavior are chosen.
12. Enter the Name for the deployment. Use: mocha-server-3.0.00.0028.ear
13. Verify that the following default option for Security is selected:
14. DD Only: Use only roles and policies that are defined in the deployment descriptors.
15. Verify that the following default option for Source accessibility is selected:
16. Use the defaults defined by the deployment's targets.
17. Select Next.
18. Within the *Install Application Assistant*, in the right column of the console WebLogic, the panel *Review your choices and click Finish* will now be displayed, which summarizes the steps completed above.
19. Verify that the values match those entered in Steps 6 through 17 and select Finish.
20. WebLogic will now display the panel *Settings for MOCHA*, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
21. Leave all the values as defaulted by WebLogic and select Save.
22. Within the *Change Center* panel in the left column of the WebLogic console, select Activate Changes.
23. Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
24. WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
25. Select the previously deployed mocha-server-3.0.00.0028 deployment, select Start, and then select Servicing all requests from the drop-down list.
26. WebLogic will now display the panel *Start Application Assistant* in the right column of the console for confirmation to start servicing requests.
27. Select Yes in the *Start Application Assistant* panel in the right column of the WebLogic console.
28. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
29. Verify that the State of the mocha-server-3.0.00.0028 deployment is Active.

### Backout Steps for LOG4J:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Shutdown the WebLogic servers.
2.  Restore the old log4j jar file:

> log4j-1.2.15.jar

3.  Replace the existing log4j2.xml with the old log4j.properties.
4.  Update the Arguments and Class Path wtih the old log4j.xml file and log4j library version.
5.  Add the argument:

> \-Dlog4j.logs.dir=/u01/app/oracle/user_projects/domains/moc-prod/logs

6.  Restart the servers.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the MOCHA Server ear file has been deployed and log4j is restored to the old version successfully, it can be verified by accessing an xml page from a web browser.

Open a web browser, such as Internet Explorer, and enter the URL in the following format:

http://*mochaserverhostname*:*port*/MOCHA/ordercheck, where the *mochaserverhostname* is the fully-qualified domain name of the Linux server running MOCHA Server, and *port* is the port number where the ear file was deployed in WebLogic. Here is a sample URL for reference: http://exampleserver.abc.va.gov:8001/MOCHA/ordercheck

If the MOCHA Server app is up, the browser should return xml that looks similar to this:

\<?xml version="1.0" encoding="UTF-8"?\>

\<exception xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="gov/va/med/pharmacy/peps/external/common/preencapsulation/vo/exception" xsi:schemaLocation="gov/va/med/pharmacy/peps/external/common/preencapsulation/vo/exception exception.xsd"\>\<code\>PRE\</code\>\<message\>No XML request was sent. The xmlRequest parameter must be set with the XML containing the request to process.\</message\>\<detailedMessage\>\<\![CDATA\[

Further details for this error have been logged. Contact the system administrator to obtain the log file.

\]\]\>\</detailedMessage\>\</exception\>

\<?xml version="1.0" encoding="UTF-8"?\>

# Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable because there is no data update for PREM\*3\*2.