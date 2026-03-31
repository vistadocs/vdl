---
title: MOCHA Server Version 1.1.01 Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Install Guide
app_code: PREM
app_name: "Pharmacy: Medication Order Check Healthcare Application (MOCHA)"
section: GUI
app_status: active
pkg_ns: PREM
patch_ver: 1.1.01
patch_id: PREM*1.1.01
group_key: "PREM:PREM:1.1.01"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Purpose](#purpose) - [Un-Deploy Old MOCHA Server Build](#un-deploy-old-mocha-server-build) - [Deploy New MOCHA Server Build](#deploy-new-mocha-server-build) - [Backout Plan](#backout-plan) The purpose of this Install guide is to provide instructions for the deployment of the PRE MOCHA Server ap
audience: 
keywords: 
  - mocha
  - server
  - figure
  - install
  - deployment
  - weblogic
  - console
  - panel
  - application
  - guide
page_count: 0
word_count: 1535
section_count: 1
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2013
revision_count: 5
revision_newest: 09/12/2013
revision_oldest: 03/01/2012
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Medication_Order_Check_HC_Applic/prem_1_1_p1_mocha_server_v1-1-01_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Medication_Order_Check_HC_Applic/prem_1_1_p1_mocha_server_v1-1-01_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=201"
---

Pharmacy Reengineering

Medication Order Check Healthcare Application  
(MOCHA) Server

Version 1.1.01

Installation Guide

![](mocha-server-version-1-1-01-install-guide/001.png)

September 2013

Revision History

| Date       | Version Number | Description of Revision                                                                                                                                             | Author                             |
|------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 09/12/2013 | 1.1            | Added version number to the Title page, changed MOCHA Server version number in the footer from 1.1 to 1.1.01, changed the EAR filename and made formatting changes. | <span class="mark">REDACTED</span> |
| 10/26/2012 | 1.0            | Updated Title Page                                                                                                                                                  | <span class="mark">REDACTED</span> |
| 08/27/2012 | 1.0            | Removed FOD comments                                                                                                                                                | <span class="mark">REDACTED</span> |
| 08/21/2012 | 1.0            | Updated formatting, minor text edits, internal cross-references.                                                                                                    | <span class="mark">REDACTED</span> |
| 03/01/2012 | 1.0            | Initial draft of the Pharmacy Reengineering (PRE) Installation Plan for MOCHA SERVER build deployment on WebLogic Application Server.                               | <span class="mark">REDACTED</span> |

Table of Contents

# # Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Purpose](#purpose)
- [Un-Deploy Old MOCHA Server Build](#un-deploy-old-mocha-server-build)
- [Deploy New MOCHA Server Build](#deploy-new-mocha-server-build)
- [Backout Plan](#backout-plan)
The purpose of this Install guide is to provide instructions for the deployment of the PRE MOCHA Server application build on a WebLogic (application) Server.
The following instructions detail the steps required to perform an installation of a release for the MOCHA software when an existing release is already deployed. These steps assume a fresh installation has been completed, and there is an existing MOCHA Server Application up and running which will be replaced by the WebLogic Build.
This is a two-step process: first, remove the old release (build), and then deploy the new PRE MOCHA Server application build.

# Un-Deploy Old MOCHA Server Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail how to un-deploy the MOCHA Server build:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 2‑1.

![](mocha-server-version-1-1-01-install-guide/002.png)

Figure ‑: Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 2‑2.

![](mocha-server-version-1-1-01-install-guide/003.png)

Figure ‑: Change Center

4.  WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 2‑3.

![](mocha-server-version-1-1-01-install-guide/004.png)

Figure ‑: Summary of Deployments – Stopping MOCHA

5.  Select the previously deployed MOCHA (Server) deployment, click Stop, and then select Force Stop Now from the drop-down list box.
6.  WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 2‑4.

![](mocha-server-version-1-1-01-install-guide/005.png)

Figure ‑: Force Stop Application Assistant

7.  Click Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
8.  WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 2‑5.

![](mocha-server-version-1-1-01-install-guide/006.png)

Figure ‑: Summary of Deployments – MOCHA Deployment Prepared

9.  Verify that the State of the MOCHA deployment is Prepared.
10. Select the previously deployed MOCHA deployment, and then click Delete.
11. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 2‑6.

![](mocha-server-version-1-1-01-install-guide/007.png)

Figure ‑: Delete Application Assistant

12. Click Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
13. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 2‑7.

![](mocha-server-version-1-1-01-install-guide/008.png)

Figure ‑: Summary of Deployments – MOCHA Deployment Deleted

14. Verify that the MOCHA deployment is deleted and no longer present.
15. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 2‑8.

![](mocha-server-version-1-1-01-install-guide/009.png)

Figure ‑: Activate Changes

# Deploy New MOCHA Server Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the deployment of the MOCHA Server application Build on WebLogic application Server.

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 3‑1.

![](mocha-server-version-1-1-01-install-guide/010.png)

Figure ‑: Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑2.

![](mocha-server-version-1-1-01-install-guide/011.png)

Figure ‑: Change Center

4.  Click Install found in the Deployments panel in the right column of the WebLogic console. For reference, see Figure 3‑3.

![](mocha-server-version-1-1-01-install-guide/012.png)

Figure ‑: Deployments

5.  WebLogic will now display the panel Install Application Assistant in the right column of the console, where the location of the MOCHA Server deployment will be found. For reference, see Figure 3‑4.

![](mocha-server-version-1-1-01-install-guide/013.png)

Figure ‑: Install Application Assistant

6.  Select the MOCHA deployment; select the MOCHA Server-\> mocha-server-1.1.01.1420.ear file.
    1.  If the MOCHA Server build for deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the Location panel within the Install Application Assistant in the right column of the console. For reference, see Figure 3‑5.

![](mocha-server-version-1-1-01-install-guide/014.png)

Figure ‑: Locate Deployment to Install and Prepare for Deployment

2.  If the MOCHA Server build for deployment has not been transferred to the Deployment Machine:
    1.  Click on the upload your file(s) link in the Install Application Assistant panel in the right section of the console. For reference, see Figure 3‑5.
    2.  Click the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
    3.  Click Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the Locate deployment to install and prepare for deployment panel within the Install Application Assistant. For reference, see Figure 3‑6.

![](mocha-server-version-1-1-01-install-guide/015.png)

Figure ‑: Upload a Deployment to the Admin Server

7.  Once the MOCHA Server build for deployment is located and selected, click Next.
8.  WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, Install this deployment as an application, and click Next. For reference, see Figure 3‑7 .

![](mocha-server-version-1-1-01-install-guide/016.png)

Figure ‑: Choose Targeting Style

9.  Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step. For reference, see Figure 3‑8.

![](mocha-server-version-1-1-01-install-guide/017.png)

Figure ‑: Select Deployment Targets

> NOTE: Select part of cluster and select mocha1, 2, 3,

10. For the Target, select the Deployment Server. For example, LocalPharmacyServer.
11. Click Next.
12. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen. For reference, see Figure 3‑9 .

![](mocha-server-version-1-1-01-install-guide/018.png)

Figure ‑: Optional Settings

13. Enter the Name for the deployment. For example, MOCHA.
14. Verify that the following default option for Security is selected:

DD Only: Use only roles and policies that are defined in the deployment descriptors.

15. Verify that the following default option for Source accessibility is selected:

Use the defaults defined by the deployment's targets.

16. Click Next.
17. Within the Install Application Assistant in the right column of the console WebLogic will now display the panel Review your choices and click Finish, which summarizes the steps completed above. For reference, see Figure 3‑10.

![](mocha-server-version-1-1-01-install-guide/019.png)

Figure ‑: Review Your Choices and Click Finish

18. Verify that the values match those entered in Steps 6 through 17 and click Finish.
19. WebLogic will now display the panel Settings for MOCHA, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order. For reference, see Figure 3‑11.

![](mocha-server-version-1-1-01-install-guide/020.png)

Figure ‑: Settings for MOCHA

20. Leave all the values as defaulted by WebLogic and click Save.
21. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑12.

![](mocha-server-version-1-1-01-install-guide/021.png)

Figure ‑: Activate Changes

22. Within the Domain Structure panel in the left column of the WebLogic console, click the PRE \> Deployments node. For reference, see Figure 3‑13.

![](mocha-server-version-1-1-01-install-guide/022.png)

Figure ‑: Domain Structure

23. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 3‑14.

![](mocha-server-version-1-1-01-install-guide/023.png)

Figure ‑: Summary of Deployments

24. Select the previously deployed MOCHA deployment, click Start, and then select Servicing all requests from the drop-down list box.
25. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 3‑15

![](mocha-server-version-1-1-01-install-guide/024.png)

Figure ‑: Start Application Assistant

26. Click Yes in the Start Application Assistant panel in the right column of the WebLogic console.
27. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 3‑16.

![](mocha-server-version-1-1-01-install-guide/025.png)

Figure ‑: Summary of Deployments – MOCHA Deployment Active

28. Verify that the State of the MOCHA deployment is Active.

# Backout Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the Backout plan of the MOCHA Server application on WebLogic application Server.

1.  Un-deploy MOCHA Server 1.1.01 build (mocha-server-1.1.01.1420.ear file) as detailed in [Section 2](#un-deploy-old-mocha-server-build).
2.  Deploy MOCHA Server 1.1 build (mocha-server-1.1.00.001.ear file) as detailed in [Section 3](#deploy-new-mocha-server-build).