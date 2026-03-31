---
consolidated_title: "deployment, installation, back-out, rollback guide"
app_code: TIU
doc_type: DIBR
master_source: "TIU*1*374 Deployment, Installation, Back-Out, Rollback Guide"
master_pub_date: December 2025
consolidated_from: 2 versions
prior_versions:
  - "TIU*1*297 Deployment, Installation, Back-Out, Rollback Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Mobile Electronic Documentation (TIU\*1.0\*374)

  Deployment, Installation, Back-out, and Rollback Guide
---

![](tiu-1-374-deployment-installation-back-out-rollback-guide/001.png)

December 2025

Office of Information and Technology (OIT)

Table of Contents

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
  - [Site Readiness Assessment](#site-readiness-assessment)
    - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
    - [Site Information (Locations, Deployment Recipients)](#site-information-locations-deployment-recipients)
    - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Facility Specifics](#facility-specifics)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [TIU\1.0\374 VistA Installation](#tiu10374-vista-installation)
    - [Mobile Electronic Documentation v2.3.374.4 GUI Installation](#mobile-electronic-documentation-v233744-gui-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Troubleshooting](#troubleshooting)
  - [Not Current Patch in VistA Error](#not-current-patch-in-vista-error)
  - [MED Missing Remote Procedure Calls (RPCs) in VistA Error](#med-missing-remote-procedure-calls-rpcs-in-vista-error)
  - [Invalid Pointer Operation Error](#invalid-pointer-operation-error)
  - [Application Context Error](#application-context-error)
  - [Write Access Error](#write-access-error)
  - [CPRS CHART – Library Not Registered Error](#cprs-chart-library-not-registered-error)
  - [MED Database Open Error](#med-database-open-error)
  - [MED Database Compact Messages](#med-database-compact-messages)
  - [Network Connection Error](#network-connection-error)
  - [RPC Broker Error](#rpc-broker-error)
  - [CPRS Error](#cprs-error)
  - [Invalid Date Error](#invalid-date-error)
  - [Missing Required Data Fields Error](#missing-required-data-fields-error)
This document describes how to deploy and install the Mobile Electronic Documentation v2.3.374.4, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial Off The Shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Mobile Electronic Documentation v2.3.374.4 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mobile Electronic Documentation v2.3.374.4 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation v2.3.374.4 and the associated M patch are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. Mobile Electronic Documentation v2.3.374.4 utilizes existing, nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity oversees decision making for deployment, installation, back out and rollback of Mobile Electronic Documentation v2.3.374.4. Rather, the Release Agent and Release Coordinators under the Veterans In Process will meet and approve deployment and install from an OIT perspective. If an issue with the software arises, then the facility CIO and other site leadership will meet along with input from Patient Safety and Health Product Support to initiate a back out and rollback decision of the software along with Region and Site leadership. The following table provides Mobile Electronic Documentation v2.3.374.4 project information.

<table>
<caption><p><span id="_Toc206068916" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 15%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>Team</th>
<th>Phase / Role</th>
<th>Tasks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Site personnel in conjunction with IT support – which may be local or regional.</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
</tr>
<tr class="even">
<td>Site personnel in conjunction with IT support – which may be local or regional.</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
</tr>
<tr class="odd">
<td>Site personnel.</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="even">
<td>Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="odd">
<td>Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
</tr>
<tr class="even">
<td>N/A – will work under the VistA ATO and security protocols.</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
</tr>
<tr class="odd">
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
</tr>
<tr class="even">
<td>N/A – no new functionality is being introduced.</td>
<td>Installations</td>
<td>Coordinate training</td>
</tr>
<tr class="odd">
<td>Facility CIO and IT support – which may be local or regional.</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
</tr>
<tr class="even">
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the HPS Clinical Sustainment team.</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
</tr>
</tbody>
</table>

<span id="_Toc206068916" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release, the patch TIU\*1.0\*374 will be released from the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site’s discretion. It is anticipated there will be a 45-day compliance period.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Mobile Electronic Documentation v2.3.374.4 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation v2.3.374.4 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to IOC sites for verification of functionality. Once that testing is completed and approval is given for national release, Mobile Electronic Documentation v2.3.374.4 (TIU\*1.0\*374) will be deployed to all VistA systems.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for Mobile Electronic Documentation v2.3.374.4. A fully patched VistA system is the only requirement.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action item and National Change Order prior to the release of Mobile Electronic Documentation v2.3.374.4 advising them of the upcoming release.

Mobile Electronic Documentation v2.3.374.4 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch TIU\*1.0\*374 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment / Installation 

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation v2.3.374.4 assumes a fully-patched VistA system.

> **NOTE:** The user must have the TIU MED GUI RPC V2 option assigned as a Secondary Menu item. Contact the Information Resource Management (IRM) or Clinical Applications Coordinator (CAC) to gain access to the Mobile Electronic Documentation Secondary option \[TIU MED GUI RPC V2\].

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

\[GUI\] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.)

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation v2.3.374.4 is being released as a PackMan Message distributed through Forum combined with a .ZIP file containing the GUI file(s).

The preferred method is to retrieve files from download.vista.med.va.gov.

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following

| Location       | Site                |
|----------------|---------------------|
| Hines          | fo-hines.med.va.gov |
| Salt Lake City | fo-slc.med.va.gov   |

<span id="_Toc206068917" class="anchor"></span>Table 2: OI Field Offices

Documentation can also be found on the VA Software Documentation Library at:

<http://www4.va.gov/vdl/>

| File Name     | File Contents                                                 | Download Format |
|---------------|---------------------------------------------------------------|-----------------|
| TIU_1_374.ZIP | Mobile Electronic Documentation executable and fresh database | Binary          |

<span id="_Toc206068918" class="anchor"></span>Table 3: Mobile Electronic Documentation v2.3.374.4 Files to be Downloaded

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of Mobile Electronic Documentation v2.3.374.4 requires the following:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TIU\*1.0\*374 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, must use the \[Backup a Transport Global\] option to create a back out Patch.
4.  Also from this menu, you may elect to use the following options:
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
5.  Use the Install Package(s) options and select the package TIU\*1.0\*374.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
7.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.

### Mobile Electronic Documentation v2.3.374.4 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP files contain the Mobile Electronic Documentation GUI executable and associated files. Download the ZIP file and extract all the files.

#### Pre-Requisite

If your site is currently using the TIU MED software:

- Make sure that your Home Based Health Care providers have imported all pending notes.
- Make note of the current TIU templates Update Path by opening MED and selecting a patient.
  - Select the ‘Tools’ menu, click Settings and simply make note of the Template Update Path name \>\>\>

    ![](tiu-1-374-deployment-installation-back-out-rollback-guide/002.png)

    Note: Write down this pathname and then close MED.

#### Install MED

Obtain and extract the TIU_1_374.ZIP file to C:\Program File(x86)\Mobile Electronic Documentation.

> **NOTE:** You will need admin rights in order to perform this action

If this is a fresh install, create a Shortcut on the desktop to the MED.EXE and name it “Launch MED”.

#### Configure and launch MED

1.  On the desktop, Right Click the “Launch MED” icon and choose properties.
2.  Enter the appropriate s=servername and p=rpcbrokerport in the Target field as displayed in the example below.

    ![](tiu-1-374-deployment-installation-back-out-rollback-guide/003.png)

#### Configure the TIU Template Update folder on every TIU MED Laptop.

1.  Before deploying the HBPC laptop/client workstation to the user, the IRM or CAC must retrieve and select a patient in MED on each laptop/client workstation and add the network Templates path so the templates will be available for use in MED.

> **NOTE:** While connected to the VA network/VistA, if you do not supply the appropriate signon credentials (i.e., PIV PIN/VA Access and Verify codes) you can access MED but cannot retrieve patients and summaries. You must sign into MED using the appropriate signon credentials before you can retrieve patient information from VistA.

2.  Launch MED
3.  Click Retrieve Patient(s).
4.  Click Select a Patient.
5.  Sign onto VistA: Enter your Access/Verify code.

> **NOTE:** The person entering the Access and Verify codes will need the Secondary Menu: TIU MED GUI RPC V2.

6.  Select a patient to retrieve from the list.
7.  Click Retrieve.
8.  Once the patient is retrieved, click Close. The MED Patient Select window is displayed.
9.  Select the patient’s name again and click OK.
10. Select the Tools menu and then select the Settings option, as shown below:

> TIU MED—Settings menu option

![](tiu-1-374-deployment-installation-back-out-rollback-guide/004.png)

11. In the Users & Settings dialogue, if not already selected, click on the Data & Files tab.
12. Next to "Template Update Path:" enter the network pathname where the TIU Templates are contained AND make sure ‘Retrieve Health Summaries’ is checked.

> ![](tiu-1-374-deployment-installation-back-out-rollback-guide/005.png)

> **NOTE:** If needed, your CPRS Clinical Coordinator should be able to assist you with this pathname.

13. Close MED. Then re-open MED to the Notes tab for a patient to ensure that the templates are present.

#### Set Permissions for the Mobile Electronic Documentation folder.

On the HBPC laptop/client workstation, do the following:

1.  Navigate to the C:\Program Files (x86)\Mobile Electronic Documentation\Templates.
2.  Right click on the Mobile Electronic Documentation folder.
3.  Select Properties, and then select the group or user name in the upper portion of the Properties dialogue.
4.  Check the Write checkbox under the Allow column in the lower portion of the Properties dialogue.
5.  Press OK.

> **NOTE:** In order for user to write the appropriate information while using the MED software, they must have Full Control access permission to the Mobile Electronic Documentation folder. If they do not, they will get access violation errors when launching MED.

#### CPRS Registration and Windows

> **NOTE:** This is not required if this prior version has already been registered on this PC you do not need to perform the following steps.

CPRS must be properly registered in the Windows registry for COM objects to properly launch in CPRS, otherwise your end users may see this message when trying to import MED notes into CPRS.

![](tiu-1-374-deployment-installation-back-out-rollback-guide/006.png)

> **NOTE:** This is not a CPRS software bug.

#### CPRS

1.  CPRS will register itself in the registry automatically in Windows if CPRS is launched once as ‘Run as Administrator’.
2.  Sign on to the laptop as an administrator.
3.  Right Click the CPRS Icon and select ‘Run as Administrator.’
4.  Sign in is not required, launching CPRS once as ‘run as administrator’ properly registers CPRS in the Windows registry.

#### Mobile Electronic Documentation 

- In addition to the steps outlined above, the MED Import DLL COM objects need to be registered on each workstation. To register a COM object, execute the following command on each machine, after the file has been copied to the hard disk:  
  regsvr32 C:\Program Files (x86)\Mobile Electronic Documentation\MEDImport.dll
- The regsvr32 program is a windows utility that registers and un-registers COM objects. For a list of additional flags that can be passed, run regsvr32 without a filename.

> **NOTE:** If the COM object is not present or has not been registered, CPRS will raise an error, alerting the user that the COM Object is not registered on the workstation. Following the error, CPRS will continue on as if the COM object did not exist. Additional attempts to run the COM object will be automatically aborted without an error until CPRS is restarted.

> **NOTE:** For further information about using MED, see the Mobile Electronic Documentation Help (i.e., MED.chm help file) in the Mobile Electronic Documentation folder on the laptop/client workstation and Mobile Electronic Documentation (MED) User Manual located on the [VDL](https://www.va.gov/vdl/application.asp?appid=190).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VISTA\] Verify the checksum of routine TIU374P is equal to the checksum listed on the patch description.

\[GUI\] Launch the Mobile Electronic Documentation GUI and verify the splash screen now announces that you are running version 2.3.374.4.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] In section 8.4.1 (step 3) the individual installing the patch used option \[Backup a Transport Global\] to create a packman message that will revert the Mobile Electronic Documentation components to their pre- v2.3.374.4 state. This includes everything transported in the TIU\*1.0\*315 (Mobile Electronic Documentation v2.3.315.1) build. If for any reason that PackMan Message cannot be located, Contact HPS Sustainment: Clinical (see section 5.6)

\[GUI\] To revert to the Mobile Electronic Documentation GUI, the 2.3.315.1 GUI would have to be redistributed

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on Mobile Electronic Documentation v2.3.374.4. This was a maintenance release to correct defects discovered in Mobile Electronic Documentation 2.3.315.1. There was no additional functionality included.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the three test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of TIU\*1.0\*374. The sites either passed or failed any item based on testing. The tests were performed by Clinical Application Coordinators at each site who are familiar using the application. The test cases were then delivered with concurrence by the sites to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out Mobile Electronic Documentation v2.3.374.4 would result in the re-instatement of the issues addressed in Mobile Electronic Documentation v2.3.315.1.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks*.*

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for Mobile Electronic Documentation v2.3.374.4 is in the event of a catastrophic failure.

> **NOTE:** The Vista Changes and GUI changes are independent of each other. In the case of a catastrophic failure of the GUI, the VistA Patch can remain in the system; consequently, if the catastrophic failure is in the VistA side, the site can back out the VistA patch and continue to use the updated GUI

1.  Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with Mobile Electronic Documentation v2.3.374.4. Use the following contacts:

Figure 1: HPS Clinical Sustainment Contacts

| Name & Title             | Email                                                          | Telephone Number |
|------------------------------|--------------------------------------------------------------------|----------------------|
| Joe Niksich, Project Manager | <joe.niksich@va.gov>                                               | 708-769-0559         |
| Chris Bell, Technical Leader | [<u>Christopher.Bell2@va.gov</u>](mailto:Christopher.Bell2@va.gov) | 941-592-5820         |

8.  If the decision is made to proceed with back-out and rollback, the HPS Sustainment Clinical team be available to assist sites that have misplaced their backup PackMan message, as well as give you the instructions on downloading the executable.
9.  \[VistA\] (if needed)
    1.  Open the Backup MailMan Message
    2.  At the “Enter message action (in IN basket): Ignore//” prompt Enter “X” for \[Xtract PackMan\]
    3.  At the “Select PackMan function:” prompt select \[INSTALL/CHECK MESSAGE\]. The old routine is now restored
    4.  \[GUI\] (if needed) Coordinate with the appropriate IT support, local and regional, to schedule the time to install TIU\*1.0\*315 and to push out / install the previous GUI executable.
10. Once TIU\*1.0\*315 and Mobile Electronic Documentation 2.3.315.1 have been installed, verify operations before making available to all staff.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure the 2.3.315.1 executable launches properly.
2.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the various errors and messages you may encounter while using the Mobile Electronic Documentation (MED) application.

> **NOTE:** Refer to the *Mobile Electronic Documentation (MED) User Manual* for additional information.

## Not Current Patch in VistA Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following error may be displayed when an older version of MED is installed or is the wrong KIDS version in VistA:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/007.png)

Description: MED is not installed or an older version is installed on VistA.

Resolution: Install/Reinstall the latest patch.

## MED Missing Remote Procedure Calls (RPCs) in VistA Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following error may display when an older version of MED is installed in VistA:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/008.png)

Description: MED is not installed or an older version is installed on VistA and is missing remote procedure calls (RPCs).

Resolution: Install/Reinstall the latest version.

## Invalid Pointer Operation Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following error may be displayed if the MED VistA KIDS install is not correct:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/009.png)

Description: The MED application is missing all the remote procedure calls (RPCs).

Resolution: Install/Reinstall the latest version.

## Application Context Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following error may be displayed for MED application context errors:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/010.png)

Description: Application context is a menu requirement for using all Remote Procedure Call (RPC) Broker calls. Each application has its own application context. The MED application context is TIU MED GUI RPC V2.

Resolution: The TIU MED GUI RPC V2 menu option needs to be assigned to all MED users, either on a common menu or one of the user's secondary menus.

## Write Access Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following access error may be displayed for MED application users who do not have the appropriate access permissions to the MED directory:

> Exception EFCreateError in module MED.exe at 0002363E

> Cannot create file "C:\Program Files\Mobile Electronic Documentation\med.err". Access is denied.

Description: The user does not have the appropriate access permissions to the MED executable directory on the client workstation/laptop. In order for users to write the appropriate information while using the MED software, all users must be given Full Control access permission to the following MED application directory:

C:\Program Files\Mobile Electronic Documentation

Resolution: Give all users Full Control access permission to the following MED application directory on the client workstation/laptop:

C:\Program Files\Mobile Electronic Documentation

## CPRS CHART – Library Not Registered Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following access error may be displayed when trying to import a MED note into CPRS for those MED application users who do not have the appropriate access permissions to the MED directory:

> CPRS CHART – Library Not Registered

Description: The user does not have the appropriate access permissions to the MED executable directory on the client workstation/laptop. In order for users to write the appropriate information while using the MED software, all users must be given Full Control access permission to the following MED application directory:

C:\Program Files\Mobile Electronic Documentation

Resolution: Give all Home Based Primary Care (HBPC) users Full Control access permission to the following MED application directory on the client workstation/laptop:

C:\Program Files\Mobile Electronic Documentation

## MED Database Open Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following error may be displayed if there is a problem with opening the MED database:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/011.png)

Description: The MED.mdb database should be in the following db subdirectory:

C:\Program Files\Mobile Electronic Documentation\db\MED.mdb

Resolution: Install/Reinstall the latest patch.

## MED Database Compact Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Warning Message: The following warning message will be displayed when compacting the MED Microsoft® Access database:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/012.png)

After clicking YES, you should see the following message:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/013.png)

After pressing OK, MED closes.

Description: When the MED database meets or exceeds this size in the Suggest Compact After (MB) field (default value is 1024 MB), MED automatically prompts the user to compact the database. Currently, it is suggested the user answer No to compact the database when prompted. If users choose to compact the database they will see a series of warning and action messages (see above).

The MED.mdb database should be in the following db subdirectory:

C:\Program Files\Mobile Electronic Documentation \db\MED.mdb

Resolution: Close and save all open notes *before* compacting the MED Microsoft® Access database.

## Network Connection Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following blank dialogues may be displayed if the MED RPC Broker fails to make a VistA connection:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/014.png)

Or:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/015.png)

Description: There may be a very long pause after selecting Retrieve Patients, and then the Retrieve Patients dialogue is blank. MED is running but not connected to VistA.

Resolution: Check the desktop shortcut. Verify that the IP server address and port number is correct. Also, check for a network connection error.

## RPC Broker Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: You may see the following Remote Procedure Call (RPC) Broker error dialogue when starting MED:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/016.png)

Description: This means that the user has not been assigned the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC V2\].

Resolution: Contact the Information Resource Management (IRM) or Clinical Applications Coordinator (CAC) to gain access to the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC V2\].

## CPRS Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: You may see the following dialogue when trying to import notes into CPRS:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/017.png)

Description: You may be trying to import MED notes on a computer that does not have MED installed. For example, MED is installed on the laptop/client workstation, but you are trying to import MED notes on another client workstation.

Resolution: If MED is loaded on the laptop/client workstation, contact IRM for assistance to "re-register" the MEDImport.dll file and then restart CPRS.

## Invalid Date Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following error may be displayed during the patient import process:

![](tiu-1-374-deployment-installation-back-out-rollback-guide/018.png)

Description: The Date of Birth (DOB) is in the wrong format in the MED database (MED.mdb). Click the OK button to retrieve more details.

Resolution: Verify that the correct MED GUI Version 2.3.311.6 is running on the laptop/client workstation. If it is the correct GUI, then the current patient information is from a prior version. To fix this, use the current MED GUI to retrieve the patient data and it will properly update the DOB in the MED database.

## Missing Required Data Fields Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Message: The following types of error messages may be displayed for missing data fields (highlighted):

![](tiu-1-374-deployment-installation-back-out-rollback-guide/019.png)

Description: Required fields in templates that are missing data will display a warning message, and the missing fields will be highlighted in blue. Just as in CPRS, the template cannot be completed and saved unless the required fields are completed. Unlike CPRS regular dialog templates, the missing fields will be obviously marked.

> Note: Prior versions of MED highlighted required missing data fields in yellow. To make MED Section 508 compliant, the color of the fields is now set to Active Caption Color.

Resolution: Enter the missing required data fields. Users can reset he highlight colors by changing the Microsoft® Windows theme.