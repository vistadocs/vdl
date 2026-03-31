---
title: Veteran's Crisis Line Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 1
patch_id: YS*1
group_key: "YS:YS:1"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - span
  - application
  - installation
  - version
  - table
  - class
  - contents
  - server
  - crisis
  - line
page_count: 0
word_count: 6635
section_count: 22
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 9
revision_newest: 12/01/2014
revision_oldest: 6/3/2013
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/vcl_installation_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/vcl_installation_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

|     |     |     |
|-----|-----|-----|

Veterans Crisis Line (VCL)

Installation Guide

![](veteran-s-crisis-line-version-1-installation-guide/001.png)

Version 0.6December 2014

Revision History

|            |         |                                                                                                                                              |                                    |
|------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Date       | Version | Description                                                                                                                                  | Author                             |
| 12/01/2014 | 0.6     | Technical edit. Added figure captions and two new screens to section 6.                                                                      | <span class="mark">REDACTED</span> |
| 6/25/14    | 0.5     | Updated content and formatting                                                                                                               | <span class="mark">REDACTED</span> |
| 6/12/14    | 0.4     | Updated with current installation instructions                                                                                               | <span class="mark">REDACTED</span> |
| 05/08/2014 | 0.3     | Removed Other Considerations section, which included 2008 server references. Added pre-prod links to Section 3.1, General Installation Flow. | <span class="mark">REDACTED</span> |
| 05/06/2014 | 0.2     | Modified web installation content to meet AITC standards.                                                                                    | <span class="mark">REDACTED</span> |
| 3/25/2014  | 0.2     | Added Raj’s SSRS content. Added AITC content to pre-installation section. Reviewed and incorporated comments from SQA.                       | <span class="mark">REDACTED</span> |
| 02/18/2014 | 0.2     | Add MDWS installation instructions                                                                                                           | <span class="mark">REDACTED</span> |
| 02/06/14   | 0.2     | Added instructions on how to obtain VCL code base.                                                                                           | <span class="mark">REDACTED</span> |
| 6/3/2013   | 0.1     | Created template                                                                                                                             | <span class="mark">REDACTED</span> |

Table of Contents

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Audience](#audience)
  - [Scope](#scope)
  - [Veterans Crisis Line](#veterans-crisis-line)
  - [Using This Manual](#using-this-manual)
  - [How Much Do I Need to Install?](#how-much-do-i-need-to-install)
  - [Related Documentation](#related-documentation)
- [Preinstallation](#preinstallation)
  - [Preinstallation Steps](#preinstallation-steps)
  - [System Backup](#system-backup)
  - [Retrieving Files from Staging Areas](#retrieving-files-from-staging-areas)
    - [Database Staging Area](#database-staging-area)
    - [Application Staging Area](#application-staging-area)
- [Installation Prerequisites](#installation-prerequisites)
  - [SSL Setup](#ssl-setup)
  - [General VCL Installation Flow](#general-vcl-installation-flow)
  - [MDWS installation](#mdws-installation)
  - [System Requirements](#system-requirements)
- [Backout Plan](#backout-plan)
- [Post Installation Instructions](#post-installation-instructions)
- [Installing and Configuring the SQL Server Reports Server (SSRS) Component](#installing-and-configuring-the-sql-server-reports-server-ssrs-component)
  - [Audience](#audience-1)
  - [Pre-Requisites](#pre-requisites)
  - [Configuring the Reports Server (Includes SSL)](#configuring-the-reports-server-includes-ssl)
  - [Defining the Reporting Web Project](#defining-the-reporting-web-project)
    - [Customizing the Site name:](#customizing-the-site-name)
  - [Reporting Services SSL Configuration](#reporting-services-ssl-configuration)
  - [Uploading Previously Developed “Sample Reports” to the Server](#uploading-previously-developed-sample-reports-to-the-server)
- [Patching the Production Environment with Updated Code](#patching-the-production-environment-with-updated-code)
- [Troubleshooting](#troubleshooting)
  - [Rollback Instructions](#rollback-instructions)
- [FAQ](#faq)
This Veterans Crisis Line (VCL) Installation Guide provides information for Information Resource Management (IRM) personnel to install and configure the components of the VCL application.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Office of Mental Health Services (OMHS) is currently managing a web-based application (herein referred to as VCL) utilized by their confidential, free 24-hours hotline staff to make referrals to the appropriate field-based Suicide Prevention Coordinators (SPCs).

OMHS is requesting OIT to assist OMHS to enhance, deploy and support the existing Veterans Crisis Line application and hardware platform utilizing Information Technology (IT) best practices and procedures rather than maintaining the existing ad-hoc environment.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document has been prepared for system administrators and database administrators who need to set up development, pre-production and/or production environments at the Austin Information Technology Center (AITC). It is presumed that readers of this document understand basic concepts of the VCL environments as well as any system specialties that might pertain to the installation of the VCL software.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Installation Guide includes steps for installing the Pre-Prod environment. Assumptions for installation include the following:

- Pre-installation steps have been completed.
- 9957’s have been submitted 30 days prior to need date for each environment
- All backups have been performed
- All files have been placed into the appropriate staging area
- Application server certificates have been installed.

## Veterans Crisis Line

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual guides the reader through a very specific order for installing and configuring the various components of VCL.

## How Much Do I Need to Install?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on your purposes for installing VCL components, you may not need to install all of the components described in this Installation Guide. Please follow these guidelines for determining which components you should install:

This Guide also covers the install from a total “ground-up” perspective. This involves the following additional steps:

- Restoring the VCL database from a backup file.
- Obtaining and installing the VCL code.
- Installing the appropriate version of SQL Server Reporting Services.
- Installing the correct version and configuration of IIS.
- Installing the correct version of MDWS web service.

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the following documentation for additional information about VCL.

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the [VA Software Documentation Library](http://www4.va.gov/vdl/).

| File Name                                  | Description                                                                                                          |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| VCL Production Operations Manual (POM).PDF | Includes system and operational description for VCL, information about routine operations, and contingency planning. |
| VCL_Release Notes.PDF                      | Release notes on new features and functionality                                                                      |
| VCL_User Guide.PDF                         | VCL User Guide                                                                                                       |
| VCL_Installation Guide.PDF                 | Installation Guide for installation in various environments                                                          |

*This page intentionally left blank for double-sided printing.*

# Preinstallation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections include steps required to setup the development environment.

## Preinstallation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following preinstallation steps need to be completed for the development environment:

Group Account Creation

1.  Verify/Create Security Groups for Report Viewer and Manager (9957 or ePAS).

<u>This function is now complete for all environments</u>

1.  Create the Groups used for User Management Access based on the specific environment and functions.
2.  Groups Created
    1.  Dev
        1.  VCLREPORTMANAGER_DEV
        2.  VCLREPORTVIEWER_DEV
    2.  Preproduction
        1.  VCLREPORTMANAGER_PPD
        2.  VCLREPORTVIEWER_PPD
    3.  Production
        1.  VCLREPORTMANAGER
        2.  VCLREPORTVIEWER

![](veteran-s-crisis-line-version-1-installation-guide/002.png)

2.  Submit request to grant permissions to the Security Groups created:

<u>This function is now complete for Development</u>

1.  Granting permissions to these groups allow individuals to be added to the Security Groups rather than making multiple changes on the servers. Permissions and titles are specific to the environment, including the actual names of the database. These must be completed after the databases have been created.
2.  Permissions Created so far:
    1.  Development
        1.  VCLREPORTMANAGER_DEV
            1.  On the database server VAAUSSQL1a: Read permission on DB: "NationalSuicideHotline_Test1" R\W on DB's:VCLReportServer and VCLReportServerTempDB
            2.  On the VAAUCVCLAPP80 in SQL Server Reporting Service Grant the following roles: Browser, Report Builder
        2.  VCLREPORTVIEWER_DEV
            1.  On the database server VAAUSSQL1a: Read permissions on DB's: VCLReportServerTempDB, VCLReportServer and "NationalSuicideHotline_Test1"
            2.  On the VAAUCVCLAPP80 in SQL Server Reporting Service Grant the following roles: Browser

![](veteran-s-crisis-line-version-1-installation-guide/003.png)

3.  Submit request to add users to appropriate security groups (9957 or ePAS):

<u>This function is now complete for Development.</u>*Note: Developers have requested and been individually granted elevated privileges in the development environment. Elevated privileges are restricted to EO AITC Administrators in other environments.*

<span class="mark">REDACTED</span>

![](veteran-s-crisis-line-version-1-installation-guide/004.png)

Service Account Creation

1.  Verify/Create Application Service Accounts (9957 or ePAS) – <u>This function is now complete for all environments</u>
    1.  Create the accounts used for the application to connect to the database based on the specific environment and functions.
    2.  Service Accounts Created
        1.  Dev
            1.  VaAacVclAppDev - Development Application Service Account
            2.  VaAacVclRptRODev - Development Reporting Service Account
        2.  Preproduction
            1.  VaAacVclAppPpd - PreProduction Application Service Account
            2.  VaAacVclRptROPpd - PreProduction Reporting Service Account
        3.  Production
            1.  VaAacVclAppPrd - Production Application Service Account
            2.  VaAacVclRptROPrd - Production Reporting Service Account

![](veteran-s-crisis-line-version-1-installation-guide/005.png)

2.  Submit request to grant permissions to the Security Groups created: <u>This function is complete for Development</u>
    1.  Granting permissions to these groups allow the application to connect to the database. Permissions and titles are specific to the environment, including the actual names of the database. These must be completed after the databases have been created.
    2.  Permissions Created so far:
        1.  Dev
            1.  VaAacVclAppDev
                1.  Grant read/write access to DB NationalSuicideHotline_Test on VAAUSSQL1A
                2.  Grant read/write access to DB NationalSuicideHotline_Test1 on VAAUSSQL1A
            2.  VaAacVclRptRODev
                1.  Grant read only access to DB NationalSuicideHotline_Test on VAAUSSQL1A
                2.  Grant read only access to DB NationalSuicideHotline_Test1 on VAAUSSQL1A

![](veteran-s-crisis-line-version-1-installation-guide/006.png)

## System Backup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Austin Information Technology Center (AITC) system backup procedures include the following:

- Backing up the system
- VMWARE Consolidated BACKUP
- Request snapshot of entire server image. Snapshots are only completed upon request and are deleted after eight hours.
- Backup of the database

*Note: Full backups are performed on the system every Friday. Differential backups are performed daily.*

## Retrieving Files from Staging Areas

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Database Staging Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VCL Development team drops files for the Dev and PPD instance here: vaausvclapp80\vcl. Production Data Transfer will be handled according to protocols defined in a separate “Data Transfer Agreement.”

### Application Staging Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VCL Development team drops files for the application server here: vaausvclapp80\vcl.

# Installation Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following preinstallation requirements apply for users who are installing VCL:

- Windows server needs to be installed on to the target environment.
- The environment will vary based on utilization (PPD).
- Technical Manager / Configuration Manager has submitted all the firewall rules.
- Sufficient disk space is available on the application server as specified by AITC
- Database Administrator has approved 9957’s to create application accounts and roles
- Microsoft Web Service Extension 3.5
- Microsoft .Net Framework 4.0, which can be downloaded from <http://www.microsoft.com/en-us/download/details.aspx?id=17718>.
- IIS 7
  - MDWS can be installed in a new virtual directory.
- MDWS installation reference, located at <http://vaww.oed.portal.va.gov/projects/vet_crisis_line_enhancements/Library/User%20Documentation%20and%20National%20Release/mwvs2_0ig.doc>.
- Windows Server 2008 with IIS 7.0.
  - Install Microsoft .NET 3.5.1
  - Install Static Content
- A shared SQL Server Database is to be utilized. Here are the desired version specifics:
  - Database Version 10.0.1600.22 (Note, this is the SQL Server 2008 Non-R2 version)
- The SQL Server Management Studio is will be installed on the PPD Servers. Here are the version specifics:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Microsoft SQL Server Management Studio 10.0.1600.22 ((SQL_PreRelease).080709-1414 )</p></li>
<li><p>Microsoft Data Access Components (MDAC) 6.1.7601.17514 (win7sp1_rtm.101119-1850)</p></li>
<li><p>Microsoft MSXML 2.6 3.0 4.0 5.0 6.0</p></li>
<li><p>Microsoft Internet Explorer 9.10.9200.16750</p></li>
<li><p>Microsoft .NET Framework 2.0.50727.5472</p></li>
<li><p>Operating System 6.1.7601</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- SQL Server Reporting Services (SSRS) is to be installed on an application server. In the PPD instances, this will be installed on the only Application Server. In PRD, this should be installed on a server selected based on load balancing needs. The SSRS version as well as the Business Intelligence Development Studio version details are listed below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Microsoft Visual Studio 2008 Version 9.0.30729.1 SP</p></li>
<li><p>Microsoft .NET Framework Version 3.5 SP1</p></li>
<li><p>Installed Edition: IDE Standard</p></li>
<li><p>Hotfix for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB945282)</p></li>
<li><p>Hotfix for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB946040)</p></li>
<li><p>Hotfix for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB946308)</p></li>
<li><p>Hotfix for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB946344)</p></li>
<li><p>Hotfix for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB946581)</p></li>
<li><p>Hotfix for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB947173)</p></li>
<li><p>Hotfix for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB947540)</p></li>
<li><p>Hotfix for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB947789)</p></li>
<li><p>Security Update for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB2251487)</p></li>
<li><p>Security Update for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB2669970)</p></li>
<li><p>Security Update for Microsoft Visual Studio 2008 Shell (integrated mode) - ENU (KB972222)</p></li>
<li><p>SQL Server Analysis Services</p></li>
<li><p>Microsoft SQL Server Analysis Services Designer</p></li>
<li><p>Version 10.50.4260.0</p></li>
<li><p>SQL Server Integration Services</p></li>
<li><p>Microsoft SQL Server Integration Services Designer</p></li>
<li><p>Version 10.0.1600.22 ((SQL_PreRelease).080709-1414 )</p></li>
<li><p>SQL Server Reporting Services</p></li>
<li><p>Microsoft SQL Server Reporting Services Designers</p></li>
<li><p>Version 10.0.1600.22</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## SSL Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VCL will provide PII information. To be complaint with government, VCL will encrypt all communication between client browser and server.

VCL has a total of three web sites. One requires a signed certificate. The SSL web site will have three sub-sites, which will be the three VCL web applications. 

AITC will take responsibility for the SSL setup.

> Dev

<span class="mark">REDACTED</span>

> Pre-Prod

> <span class="mark">REDACTED</span>

> Prod

> <span class="mark">REDACTED</span>

## General VCL Installation Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following flow diagram illustrates an overview of the basic information flow of the application. This installation does not include the VistA servers, only verifying the MDWS-VistA connection.

![](veteran-s-crisis-line-version-1-installation-guide/007.png)

<span id="_Toc405203751" class="anchor"></span>Figure 1: VCL Application Flow

IIS Installation Settings

1.  Verify IIS is installed with default settings with the following exceptions:
    1.  Install Microsoft .NET 3.5.1
    2.  Install Static Content
    3.  Install Web Services Enhancements 3.0
    4.  Verify the ASP.NET Session State Service is set to a startup type of Automatic, and is running.

> ![](veteran-s-crisis-line-version-1-installation-guide/008.png)

![](veteran-s-crisis-line-version-1-installation-guide/009.png)

<span id="_Toc405203752" class="anchor"></span>Figure 2: VCL Installed Components

IIS Installed Components

![](veteran-s-crisis-line-version-1-installation-guide/010.png)

<span id="_Toc405203753" class="anchor"></span>Figure 3: VCL Add Features Wizard

IIS Additional Components

![](veteran-s-crisis-line-version-1-installation-guide/011.png)

<span id="_Toc405203754" class="anchor"></span>Figure 4: VCL Installing Web Services Enhancements 3.0 – select Runtime option

![](veteran-s-crisis-line-version-1-installation-guide/012.png)

> <span id="_Toc405203755" class="anchor"></span>Figure 5: Installing Web Services Enhancements 3.0 – Click Finish to complete installation

Locate VCL Code

2.  The VCL code will be uploaded onto the dev server in the location vaausvclapp80\vcl\vcl-####.zip. It will be in an archive, with a naming convention that identifies the version, and when unpacked will have a directory structure similar to the following:

![](veteran-s-crisis-line-version-1-installation-guide/013.png)

<span id="_Toc405203756" class="anchor"></span>Figure 6: Unpack VCL Code Archive

Unpack the VCL code archive to E:\VCL. The folder structure should look similar to the following:

Create and set up VCL web sites

3.  Open IIS Manager.

![](veteran-s-crisis-line-version-1-installation-guide/014.png)

<span id="_Toc405203757" class="anchor"></span>Figure 7: IIS Manager

4.  In IIS Manager, go to IIS -\> Authentication
5.  Select "Anonymous Authentication" then select "Edit"
6.  Under the "Edit Anonymous Authentication Credentials" window, make sure "Application Pool Identity" is selected.
7.  Rename default site to server website name.
8.  There are three applications to be created under the server website name. Right-click the server website name, and select “Add Application”

> Please note that the creation of the web sites will also create the application pools, which is detailed in step b under the creation of each web application (steps 5, 6, and 7).

9.  Fill in the following information for the CrisisCenter web application:
    1.  Site name: CrisisCenter
    2.  Application pool: CrisisCenter
    3.  Physical path: E:\VCL\CrisisCenter
10. Fill in the following information for the Response web application:
    1.  Site name: Response
    2.  Application pool: Response
    3.  Physical path: E:\VCL\CrisisCenterResponse
11. Fill in the following information for the Admin web application:
    1.  Site name: Admin
    2.  Application pool: Admin
    3.  Physical path: E:\VCL\CrisisCenterAdmin
12. IIS Manager should look similar to the following when you are done:

![](veteran-s-crisis-line-version-1-installation-guide/015.png)

<span id="_Toc405203758" class="anchor"></span>Figure 8: VCL Site Breakout

te

<span id="_Toc405203759" class="anchor"></span>Figure 9: VCL Site Breakout Expanded

Require SSL

13. Add the HTTPS bindings to the website certificate using whatever process you have in place to accomplish this.
14. Select the newly created website, then double-click SSL Settings. Select Require SSL, and click Apply.

![](veteran-s-crisis-line-version-1-installation-guide/016.png)

<span id="_Toc405203760" class="anchor"></span>Figure 10: SSL Settings

Modify application pools

15. In IIS Manager, click Application Pools

![](veteran-s-crisis-line-version-1-installation-guide/017.png)

<span id="_Toc405203761" class="anchor"></span>Figure 11: Application Pools

16. Double-click the CrisisCenter application pool, and change the Managed Pipeline Mode from Integrated to Classic. Click “OK” when done
17. Double-click the Response application pool, and change the Managed Pipeline Mode from Integrated to Classic. Click “OK” when done
18. Double-click the Admin application pool, and change the Managed Pipeline Mode from Integrated to Classic. Click “OK” when done

![](veteran-s-crisis-line-version-1-installation-guide/018.png)

<span id="_Toc405203762" class="anchor"></span>Figure 12: Edit Application Pool settings

CrisisCenter application pool permissions to the appropriate file system folder

19. Give the CrisisCenter application pool file system permissions to access the CrisisCenter code. Open Windows Explorer, navigate to E:\VCL\\ right-click the CrisisCenter folder, select Properties, and select the Security tab.

![](veteran-s-crisis-line-version-1-installation-guide/019.png)

<span id="_Toc405203763" class="anchor"></span>Figure 13: CrisisCenter Properties

20. Click the Edit button, then click Add.

![](veteran-s-crisis-line-version-1-installation-guide/020.png)

<span id="_Toc405203764" class="anchor"></span>Figure 14: Permissions for CrisisCenter

21. Click Locations, and select the IIS server hosting the VCL code.

![](veteran-s-crisis-line-version-1-installation-guide/021.png)

<span id="_Toc405203765" class="anchor"></span>Figure 15: Locations

22. Click OK. Under “Enter the object names to select”, type “IIS APPPOOL\CrisisCenter” for the CrisisCenter website.

![](veteran-s-crisis-line-version-1-installation-guide/022.png)

<span id="_Toc405203766" class="anchor"></span>Figure 16: Enter the Object Names to Select

23. Click Check Names to verify your entry was correct. If so the text you entered will change to the name of the appropriate application pool.

![](veteran-s-crisis-line-version-1-installation-guide/023.png)

<span id="_Toc405203767" class="anchor"></span>Figure 17: Check Names

24. Click OK. Leave the default permissions granted to the application pool account.

![](veteran-s-crisis-line-version-1-installation-guide/024.png)

<span id="_Toc405203768" class="anchor"></span>Figure 18: Default Permissions

25. Click OK until all folder property windows are closed.

Admin application pool permissions

26. Give the Admin application pool file system permissions to access the Admin code. Open Windows Explorer, navigate to E:\VCL\\ right-click the CrisisCenterAdmin folder, select Properties, and select the Security tab.
27. Click the Edit button, then click Add.
28. Click Locations, and select the IIS server hosting the VCL code.
29. Click OK. Under “Enter the object names to select”, type “IIS APPPOOL\Admin” for the Admin website.
30. Click Check Names to verify your entry was correct. If so the text you entered will change to the name of the appropriate application pool.
31. Click OK. Leave the default permissions granted to the application pool account.
32. Click OK until all folder property windows are closed.

Response application pool permissions

33. Give the Response application pool file system permissions to access the Response code. Open Windows Explorer, navigate to E:\VCL\\ right-click the CrisisCenterResponse folder, select Properties, and select the Security tab.
34. Click the Edit button, then click Add.
35. Click Locations, and select the IIS server hosting the VCL code.
36. Click OK. Under “Enter the object names to select”, type “IIS APPPOOL\Response” for the Response website.
37. Click Check Names to verify your entry was correct. If so the text you entered will change to the name of the appropriate application pool.
38. Click OK. Leave the default permissions granted to the application pool account.
39. Click OK until all folder property windows are closed.

Web site IIS authentication pass-through settings.

40. In IIS Manager, select the CrisisCenter virtual directory. Under IIS in the center of the IIS Manager, select Authentication. Under Actions on the right hand side of the IIS Manager, select Basic Settings.

![](veteran-s-crisis-line-version-1-installation-guide/025.png)

<span id="_Toc405203769" class="anchor"></span>Figure 19: IIS Manager, CrisisCenter Virtual directory

41. Click Connect As.

![](veteran-s-crisis-line-version-1-installation-guide/026.png)

<span id="_Toc405203770" class="anchor"></span>Figure 20: Edit Application

42. Select “Application user (pass-through authentication).

![](veteran-s-crisis-line-version-1-installation-guide/027.png)

<span id="_Toc405203771" class="anchor"></span>Figure 21: Connect As dialogue

43. Click OK on the “Connect As” window and the “Edit Application”, which will return you to IIS Manager.
44. In IIS Manager, select the Admin virtual directory. Under IIS in the center of the IIS Manager, select Authentication. Under Actions on the right hand side of the IIS Manager, select Basic Settings.
45. Click Connect As.
46. Select “Application user (pass-through authentication).
47. Click OK on the “Connect As” window and the “Edit Application”, which will return you to IIS Manager.
48. In IIS Manager, select the Response virtual directory. Under IIS in the center of the IIS Manager, select Authentication. Under Actions on the right hand side of the IIS Manager, select Basic Settings.
49. Click Connect As.
50. Select “Application user (pass-through authentication).
51. Click OK on the “Connect As” window and the “Edit Application”, which will return you to IIS Manager.

> Session state server set-up

52. 

Web site set up verification*Note: The following are links for pre-production and production environments:*

Dev  
<span class="mark">REDACTED</span>

PreProd/Test

<span class="mark">REDACTED</span>

Prod

<span class="mark">REDACTED</span>

There are sub-sites in each environment:

For example, vcl.aac.va.gov/admin, vcl.aac.va.gov/crisiscenter, vcl.aac.va.gov/MDWS, and vcl.aac.va.gov/response.

53. Test each site out to see if they work properly. You will get screens like the following if the sites are working:

![](veteran-s-crisis-line-version-1-installation-guide/028.png)

<span id="_Toc405203772" class="anchor"></span>Figure 22: Crisis Center Hotline Login

![](veteran-s-crisis-line-version-1-installation-guide/029.png)

<span id="_Toc405203773" class="anchor"></span>Figure 23: CrisisCenter Response

![](veteran-s-crisis-line-version-1-installation-guide/030.png)

<span id="_Toc405203774" class="anchor"></span>Figure 24: CrisisCenter Administrator

## MDWS installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MDWS is the web service application that bridge the gap between VCL applications and VistA sites. Current version used 3.0.3.5. The installation file is provided.

Installation Steps:

1.  Verify the .NET Framework 4.0 is installed on the server. If not then install it.
2.  Obtain the MDWS files from <span class="mark">REDACTED</span>.
3.  Extract archive to E:\VCL\MDWS.
4.  Open IIS Manager and select Application Pools.
5.  Create an application pool with the following parameters:

![](veteran-s-crisis-line-version-1-installation-guide/031.png)

6.  Under Sites, right click the server website name and select Add Application.
7.  Fill in the following information for the MDWS web application:
    1.  Site name: MDWS
    2.  Application pool: MDWS
    3.  Physical path: E:\VCL\MDWS
8.  Set up the session state server for MDWS by going to the server website/MDWS Home -\> ASP.NET, then double-click Session State.
9.  Under Session State, select In Process, and then click Apply
10. Give the MDWS application pool file system permissions to access the MDWS code. Open Windows Explorer, navigate to E:\VCL\\ right-click the MDWS folder, select Properties, and select the Security tab.
11. Click the Edit button, then click Add.
12. Click Locations, and select the IIS server hosting the MDWS code.
13. Click OK. Under “Enter the object names to select”, type “IIS APPPOOL\MDWS” for the MDWS website.
14. Click Check Names to verify your entry was correct. If so the text you entered will change to the name of the appropriate application pool.
15. Click OK. Leave the default permissions granted to the application pool account.
16. Click OK until all folder property windows are closed.
17. Once completed, test it going to https://localhost/MDWS/CallService.asmx in a browser on the server.

![](veteran-s-crisis-line-version-1-installation-guide/032.png)

Obtaining the VCL Installation Files

- The VCL application code will be provided in a ZIP archive. This archive is to be unpacked in the directory that will host the three websites needed for VCL: Hotline, Response, and Admin. The lead developer of the VCL team will have the location of the archive of the code files. These files will be uploaded into vaausvclapp80\vcl into a file name that includes software version information
- The VCL database installation is performed by restoring from a SQL Server backup file. The details regarding file name and location should be available with the Database Administrator. (Dev and PPD data exports will be uploaded into vaausvclapp80\vcl. PRD data transfer will be accomplished according to the separate Data Transfer Agreement.)

> Perform a restore for the VCL database, using the appropriate backup file. A sample restore statement is provided below:

> RESTORE DATABASE \[NationalSuicideHotline_PreProd\] FROM

> DISK = N'C:\0_VCL\TEMPDB-Backup'

> WITH FILE = 1,

> MOVE N'NationalSuicideHotline' TO N'C:\0_VCL\PreProd\NationalSuicideHotline_PreProd_dat.mdf',

> MOVE N'NationalSuicideHotline_log' TO N'C:\0_VCL\PreProd\NationalSuicideHotline_PreProd_log.ldf',

> NOUNLOAD,

> STATS = 10

> GO

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Storage requirements for installation:

| Type of Data | Size |
|------------------|----------|
| Applications     | \< 5MB   |
| Help Files       | \< 1MB   |

Sites should reserve 1KB of storage space per observation for data that will accumulate. The vast majority of growth will occur in the OBS file (#704.117).

The following describes the installation environment for on the VistA client workstation:

- Workstations must be running under Windows. Refer to <http://vaww.vairm.vaco.va.gov/vadesktop> for additional information on VA standard desktop configurations.
- Remote Procedure Call (RPC) Broker Workstation must be installed.
- The workstation must be connected to the local area network.
- Administrator privileges are needed on any machine on which CP Gateway Service is installed.

# Backout Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the back out procedures for VCL.

During installation of a new VCL baseline, if there are any issues with new baseline, the new baseline will be backed out and the system will be restored to the previous baseline.

In the event that a backout of the VCL installed code is needed, code should be rolled back to the last known working version. AITC will retrieve the tape backup of the last known good production version to reinstall. The database admin and system admin will determine the correct last working version to rollback to.

The following are the steps to back out VCL to its previous version:

1.  Notify the Remedy Help Desk <span class="mark">REDACTED</span> and VCL application users about backout plan initiation.
2.  When VCL is first deployed to AITC, a copy of the existing VCL install files will be placed at vaausvclapp80\vcl.
3.  Disable user access to the VCL system while the back out procedures are in process.
4.  Delete all of the VCL code from the following location where it was uploaded onto the dev server:

vaausvclapp80\vcl\vcl-2.0 build 21.zip (Build information is provided as an example.) The VCL code will be in an archive, with a naming convention that identifies the version, and when unpacked will have a directory structure similar to the following:

![](veteran-s-crisis-line-version-1-installation-guide/033.png)

<span id="_Toc405203775" class="anchor"></span>Figure 25: Unpack VCL Code Archive

5.  Rename the backup copied folders. Backup the VCL database on the dev server (vaaussql1a.) 
6.  Perform a full database backup of database "NationalSuicideHotline_Test" on vaaussql1a. 
7.  Create an additional backup VCL folder at an additional location on vaaussql1a in case the VCL application needs to be backed out again.
8.  Conduct system health checks of the VCL application.
9.  Enable VCL application user access.
10. Notify the Remedy Help Desk (1-888-596-4357) and VCL users of successful backout.

# Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AITC Build Manager will submit the needed access request forms (if not already submitted) for the environment. Where possible, a primary POC for each group of permissions being granted will be designated. The System and Database Administrators will complete the SDM tasks needed to grant access as required. The primary POC for each group should be contacted to verify access.

*Note: This Install Guide Addresses the basic "vanilla" product.*

After completing the instructions contained in this Guide, please apply the Patch in order to upgrade the product to the latest version. We need to include the all the Increment 3 upgrades.

Instructions for the Patch, along with the step-by-step database scripts, have been detailed in change order CO217347FY14.

# Installing and Configuring the SQL Server Reports Server (SSRS) Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is intended to provide a complete step-by-step walkthrough for installing and configuring the SQL Server Reports Server component, for the Veterans Crisis Line application.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience is the System and Database Administrators, and the VCL Manager at AITC.

## Pre-Requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following pre-requisites must be in place before all the steps outlined in this document can be completed:

1.  Two security groups will need to be setup in the VA Active Directory:
    - VCL REPORTVIEWER and VCL REPORTMANAGER.

The Group creation process is as follows:

- First create the Group in the VA active directory
- Next create a *database login* for the Group, in the NationalSuicideHotline database
- Then create a *user* corresponding to the *login*, in the ReportServerDatabase.
- Finally, add the authorized individuals, as members of the group.
- Notes:
1.  The suffixes \_DEV and \_PPD must be added to these groups, in order to set them up for the Development and Preproduction environments respectively.
2.  Group membership is controlled through the AITC user creation process. A “VA 9957” security form must be processed for each member who is added to the group.
2.  A “service account” will need to be setup for each environment:

> (For the DEV, Pre-Prod and Prod databases, respectively)

1.  Dev
    1.  VaAacVclAppDev - Development Application Service Account
    2.  VaAacVclRptRODev - Development Reporting Service Account
2.  Preproduction
    1.  VaAacVclAppPpd - PreProduction Application Service Account
    2.  VaAacVclRptROPpd - PreProduction Reporting Service Account
3.  Production
    1.  VaAacVclAppPrd - Production Application Service Account

> VaAacVclRptROPrd - Production Reporting Service Account

The service account creation process is as follows:

- First create the account in the VA active directory
- Next create a *database login* in the NationalSuicideHotline database
- Then create a *user* corresponding to the login, in the ReportServerDatabase.
- Note: This account must have read-only access to all the tables in the VCL Database, EXCEPT for: HotlineCalls, HotlineCalls_H, HotlineCallsDetails, HotlineCallsDetails_H.

## Configuring the Reports Server (Includes SSL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Start Menu, select “run as Administrator” for the Reporting Services Configuration Manager.

![](veteran-s-crisis-line-version-1-installation-guide/034.png)

<span id="_Toc405203776" class="anchor"></span>Figure 26: Reporting Services Configuration Connection

Here are the steps to configure SSL on SSRS:

Log on to VCL APP server go to Reporting services configuration Manager, see below:

![](veteran-s-crisis-line-version-1-installation-guide/035.png)

<span id="_Toc405203777" class="anchor"></span>Figure 27: Reporting Services Configuration Manager

Click window popup as below:

![](veteran-s-crisis-line-version-1-installation-guide/036.png)

<span id="_Toc405203778" class="anchor"></span>Figure 28: Specify a Server Name

Click Connect see the above figure.

![](veteran-s-crisis-line-version-1-installation-guide/037.png)

<span id="_Toc405203779" class="anchor"></span>Figure 29: Report Server Status

Select Web services URL from the left-hand pane. Add the SSL certificate and SSL port (see drop-down highlighted in yellow.)

![](veteran-s-crisis-line-version-1-installation-guide/038.png)

<span id="_Toc405203780" class="anchor"></span>Figure 30: SSL Certificate and SSL Port

Click Advanced and add the following SSL Certificate information (highlighted in yellow below:)

![](veteran-s-crisis-line-version-1-installation-guide/039.png)

<span id="_Toc405203781" class="anchor"></span>Figure 31: SSL Certification Information

Select the Report Manager URL

![](veteran-s-crisis-line-version-1-installation-guide/040.png)

<span id="_Toc405203782" class="anchor"></span>Figure 32: Add Report Manager URL

Click Advanced and add as shown below:

![](veteran-s-crisis-line-version-1-installation-guide/041.png)

<span id="_Toc405203783" class="anchor"></span>Figure 33: UpdatingSSL Certificates

Click OK.

This will complete the SSL section of SSRS.

## Defining the Reporting Web Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Application server machine (APP80 in case of Dev) open Internet Explorer and go to the reporting services URL.

1\. From the Reports Manager home page, create a *Datasource* named VCLDatasource.

![](veteran-s-crisis-line-version-1-installation-guide/042.png)

<span id="_Toc405203784" class="anchor"></span>Figure 34: Create a Datasource

2.  Select “Credentials stored securely in Reports Server”.

Also check “Use as Windows Credentials when connecting…”

> **NOTE:** AITC will need to type in the username and password for the service account in this section.

![](veteran-s-crisis-line-version-1-installation-guide/043.png)

<span id="_Toc405203785" class="anchor"></span>Figure 35: VCL Datasource

3.  After the Datasource has been created, select it by clicking on it.
4.  Click on Generate Model

![](veteran-s-crisis-line-version-1-installation-guide/044.png)

<span id="_Toc405203786" class="anchor"></span>Figure 36: Generate Model

5.  Create a new *Model* named VCLModel.

![](veteran-s-crisis-line-version-1-installation-guide/045.png)

<span id="_Toc405203787" class="anchor"></span>Figure 37: VCL Model

You must define the security, by adding role assignments and giving permissions.

6.  To define the security, click on Site Settings.
7.  Click New Role Assignment.
8.  Add VCLREPORTMANAGER, as “System User” (allows Manager to see Report Builder link).

![](veteran-s-crisis-line-version-1-installation-guide/046.png)

<span id="_Toc405203788" class="anchor"></span>Figure 38: System User

Next, define the security for all the items that will be created.

9.  Click the Home link, then Properties tab.
10. Click on *New Role Assignment*, add VCLReportManager and VCLReportViewer.

Manager gets Browser, Publisher and ReportsBuilder permissions. The Viewer group gets only Browser and Builder permissions.

![](veteran-s-crisis-line-version-1-installation-guide/047.png)

<span id="_Toc405203789" class="anchor"></span>Figure 39: New Role Assignment

Next, ensure that the Datasource cannot be modified by anyone.

11. Click on the Datasource, and select the Security tab.
12. Ensure that even the MANAGER role can only see (but not alter) this particular object.

This is called Item-level security.

![](veteran-s-crisis-line-version-1-installation-guide/048.png)

<span id="_Toc405203790" class="anchor"></span>Figure 40: Edit Role Assignment

Similarly, you will want to override the inherited security for this item and set Item-level security for the Model as well:

13. Click on the Model, and select the Security tab.
14. Ensure that even the MANAGER role can only see (but not alter).

![](veteran-s-crisis-line-version-1-installation-guide/049.png)

<span id="_Toc405203791" class="anchor"></span>Figure 41: Security

15. Also, check the “Hide in List View” flag for the model. This will prevent its accidental deletion by the end user.

![](veteran-s-crisis-line-version-1-installation-guide/050.png)

<span id="_Toc405203792" class="anchor"></span>Figure 42: Properties

### Customizing the Site name:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click on Site Settings, then General. Enter the following text: Veterans Crisis Line – Custom Reports.

> **NOTE:** Append (DEV) or (TEST) for those environments respectively.

![](veteran-s-crisis-line-version-1-installation-guide/051.png)

<span id="_Toc405203793" class="anchor"></span>Figure 43: Veterans Crisis Line – Custom Reports

|     |     |
|-----|-----|

<span id="_Toc404156191" class="anchor"></span>

## Reporting Services SSL Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This has been covered in section 6.3

## Uploading Previously Developed “Sample Reports” to the Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>On the Application server machine (APP80 in case of Dev) open Internet Explorer and go to the reporting services URL.</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1.</td>
<td><p>The pre-defined reports are located in the following folder on VaAusVclApp80 (the Dev Application Server):</p>
<blockquote>
<p>E:\VCL\Scripts\Report_scripts</p>
</blockquote>
<p>At the Reports Manager home page, select <em><strong>Upload File</strong></em> and upload the .rdl report files one by one.</p>
<p>![](veteran-s-crisis-line-version-1-installation-guide/052.png)</p></td>
</tr>
</tbody>
</table>

<span id="_Toc405203794" class="anchor"></span>Figure 44: Upload File

# Patching the Production Environment with Updated Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event that a patch needs to be installed in the AITC production environment, the following steps should be followed.

1.  Copy the patch files <span class="mark">REDACTED</span>
2.  Write documentation that details how to install the patch. Use the following steps as a guideline. You may need to revise to meet your local environment specifications.
- Open IIS Manager, expand Sites, and select the vaww.vcl.aac.va.gov website.
- Under Manage Web Site, click Stop.
- Copy code base archive <span class="mark">REDACTED</span> to production environment, and unzip.
  - Copy all files and folders from CrisisCenter to E:\VCL\CrisisCenter, overwriting existing files and folders.
  - Copy all files and folders from CrisisCenterAdmin to E:\VCL\CrisisCenterAdmin, overwriting existing files and folders.
  - Copy all files and folders from CrisisCenterResponse to E:\VCL\CrisisCenterResponse, overwriting existing files and folders.
- Return to IIS Manager and click Application Pools.
- Select the CrisisCenter application pool.
- Under Application Pool Tasks, click Recycle.
- Select the CrisisCenterAdmin application pool.
- Under Application Pool Tasks, click Recycle.
- Select the CrisisCenterResponse application pool.
- Under Application Pool Tasks, click Recycle.
- Under Sites, select vaww.vcl.aac.va.gov website.
- Under Manage Web Site, click Start.
3.  Send an email to the AITC team requesting a Change Order (CO) be opened for a patch be installed, and attach the installation instructions to the email. <span class="mark">REDACTED</span> For example:

![](veteran-s-crisis-line-version-1-installation-guide/053.png)

<span id="_Toc405203795" class="anchor"></span>Figure 45: Change Order Request Email

4.  Wait for the AITC team to respond back saying they have installed the patch.
5.  Verify your patch was installed successfully. If required, have a VCL user log in and verify it for you.

# Troubleshooting 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VCL development team participated with AITC resources during a dry run of the install process and any problems encountered were remediated and incorporated into this guide. VCL developers are available during the installation for assistance.

## Rollback Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For initial release, if there are any issues with the first migration, the rollback plan is to revert back to the Orlando environment.

After initial release, if there are any issues with the VCL application, the necessary action is to roll back to the last clean working version. The database admin and system admin should determine the correct last working version to rollback to.

The following are the steps to return the VCL database to its last working version:

1.  Restore database "NationalSuicideHotline_Test" from the backup version from step 7 of the above Backout Procedures.

The database restore will clean the database and restore it to the clean state created in step 7 of Section 3.5.3 Backout Procedures.

2.  Confirm that the backup and new working application folders are renamed.
3.  Test the VCL application and confirm that the restored version is working correctly.

Refer to section 6.6 of the [ISCP](http://vaww.oed.portal.va.gov/projects/vet_crisis_line_enhancements/Library/Forms/AllItems.aspx?RootFolder=%2fprojects%2fvet%5fcrisis%5fline%5fenhancements%2fLibrary%2fUser%20Documentation%20and%20National%20Release&FolderCTID=0x012000836A27F944BCDA4390DB2BFA889E1A7E&View=%7bC98F591B%2d0DD2%2d41E1%2d9CA2%2d2807E05B1B74%7d) for key contacts in the event that a rollback for the VCL software is needed.

# FAQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Question</strong></th>
<th><strong>What do I do if I have installation issues?</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Response</strong></td>
<td><ol type="1">
<li><p>If assistance is needed during installation, please create a Remedy Ticket or contact the <mark>REDACTED</mark></p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>Question</strong></td>
<td><strong>How can I check my connection to the broker server?</strong></td>
</tr>
<tr class="odd">
<td><strong>Response</strong></td>
<td><ol type="1">
<li><p>Check the windows registry (HKLM/software/vista/broker/servers) key and ensure that the key is set to the correct IP and port.</p></li>
</ol>
<ol type="1">
<li><p>Check that the broker is running on the correct instance of VistA and on the correct port.</p></li>
</ol>
<ul>
<li><p>Type D ^%SS to show the list</p></li>
<li><p>Find the instance and find the line XWBTCPL</p></li>
<li><p>Verify that the TCP|port number is correct</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Question</strong></td>
<td><strong>How can I check the Windows application Event Notifier?</strong></td>
</tr>
<tr class="odd">
<td><strong>Response</strong></td>
<td><ol type="1">
<li><p>Right-click <strong>My Computer</strong>.</p></li>
</ol>
<ol start="2" type="1">
<li><p>Select <strong>Manage</strong>.</p></li>
<li><p>Expand <strong>Event Viewer</strong>.</p></li>
<li><p>Select <strong>Application</strong>.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>Question</strong></td>
<td><strong>How do I stop the CP Gateway Service?</strong></td>
</tr>
<tr class="odd">
<td><strong>Response</strong></td>
<td><ol type="1">
<li><p>In Windows, click <strong>Start</strong> | <strong>Control Panel</strong> | <strong>Administrative Tools</strong> | <strong>Services</strong>. The Services window displays.</p></li>
</ol>
<ol start="5" type="1">
<li><p>Click the Clinical Procedures Gateway row. A link, <u>Stop</u> the service, displays.</p></li>
<li><p>Click <strong>Stop</strong>. A progress window displays as the service stops.</p></li>
<li><p>When the progress window closes, the Services window redisplays. The status column in the Clinical Procedures Gateway row displays <strong>Stopped</strong>.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>Question</strong></td>
<td><strong>How can I change the time interval for CP Console and CP Flowsheets at which they time out?</strong></td>
</tr>
<tr class="odd">
<td><strong>Answer</strong></td>
<td>The time interval is set using the TIMED READ value in the NEW PERSON file (#200).</td>
</tr>
<tr class="even">
<td><strong>Question</strong></td>
<td><strong>What are the post-deployment requirements for testing the successful install?</strong></td>
</tr>
<tr class="odd">
<td><strong>Answer</strong></td>
<td><ul>
<li><p>Verify the code deployment</p></li>
<li><p>Validate connections with other systems</p></li>
</ul></td>
</tr>
</tbody>
</table>