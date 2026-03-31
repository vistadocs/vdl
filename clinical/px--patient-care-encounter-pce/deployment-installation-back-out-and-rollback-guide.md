---
consolidated_title: "pce standardization deployment, installation, back-out and rollback guide"
app_code: PX
doc_type: DIBR
master_source: "PX*1*211 PCE Standardization Deployment, Installation, Back-Out and Rollback Guide"
master_pub_date: May 2021
consolidated_from: 2 versions
prior_versions:
  - "PX*1*234 PCE Standardization Deployment, Installation, Back-Out and Rollback Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>PCE Standardization 1.0

  Deployment, Installation, Back-Out, and Rollback Guide
---

Patient Care Encounter (PCE), Clinical Reminders (PXRM), and

Health Summary (GMTS)

Patches PX\*1\*211, PXRM\*2\*42, GMTS\*2.7\*122, GMPL\*2\*53, and OR\*3\*501

![](px-1-211-pce-standardization-deployment-installation-back-out-and-rollback-guide/001.png)

May 2021

Office of Information and Technology (OI&T)

Revision History

<table>
<caption><p>Table : Deployment, Installation, Back-Out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 45%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2021</td>
<td>1.4</td>
<td><ul>
<li><p>Add <a href="#post-installation">Post-Installation</a> Section</p></li>
<li><p>Update Download and Back-Out/Rollback instructions and Appendices</p></li>
<li><p>Revise dates on Title page and in Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>May 2019</td>
<td>1.3</td>
<td><p>Updates for T7:</p>
<ul>
<li><p>Removed Site Information Section</p></li>
<li><p>Updated <a href="#RelWebSites">Related Web Sites</a></p></li>
<li><p>Updated <a href="#Section485Example">4.8-5 Example</a></p></li>
<li><p>Updated <a href="#Section487Example">4.8-7 Example</a></p></li>
<li><p>Updated <a href="#appendix-a-installation-example">Appendix A</a></p></li>
<li><p>Updated <a href="#appendix-b-post-install-checksums">Appendix B</a></p></li>
<li><p>Updated <a href="#appendix-c-install-file-print-example">Appendix C</a></p></li>
<li><p>Updated <a href="#appendix-d-build-file-print-example">Appendix D</a></p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td>May 2019</td>
<td>1.2</td>
<td><ul>
<li><p>Minor updates to go to <a href="#T4">t4</a> and add <a href="#or501">OR*3*501</a></p></li>
<li><p><a href="#page5">Updated web links</a></p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td>November 2018</td>
<td>1.2</td>
<td><ul>
<li><p>Reduced Intro Content</p></li>
<li><p>Added sub-section titled “Constraints” (required per VIP DIBOR template)</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td>October 2018</td>
<td></td>
<td>Minor edits</td>
<td></td>
</tr>
<tr class="even">
<td>June 2018</td>
<td>1.1</td>
<td>Update Installation Instructions</td>
<td></td>
</tr>
<tr class="odd">
<td>April 2018</td>
<td>1.0</td>
<td>Initial Draft</td>
<td></td>
</tr>
</tbody>
</table>

Table : Deployment, Installation, Back-Out, and Rollback Roles and Responsibilities

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
  - [Site Readiness Assessment](#site-readiness-assessment)
    - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
    - [Site Preparation](#site-preparation)
  - [Related Documentation](#related-documentation)
  - [Related Web Sites](#related-web-sites)
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
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [Post Installation](#post-installation)
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
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Acronyms](#acronyms)
- [# Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B: Post-Install Checksums](#appendix-b-post-install-checksums)
- [Appendix C: Install File Print Example](#appendix-c-install-file-print-example)
- [Appendix D: Build File Print Example](#appendix-d-build-file-print-example)
This document describes how to install the PCE STANDARDIZATION 1.0 multi-package build (consisting of PX\*1.0\*211, PXRM\*2.0\*42, GMTS\*2.7\*122, GMPL\*2.0\*53, and <span id="or501" class="anchor"></span>OR\*3.0\*501), as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.
The PCE Standardization 1.0 project addresses the lack of standardized data in PCE, which is a barrier to important areas including: interoperability, clinical decision support, and quality reporting. Standardization of immunizations and skin tests was addressed by the VistA Immunization Enhancement (VIMM) project. The goal of this patch is, to the extent possible, to standardize the legacy data in Education Topics, Exams, and Health Factors and to introduce a new V file for capturing standardized codes other than International Classification of Diseases (ICD), Current Procedural Terminology (CPT), and Healthcare Common Procedure Coding System (HCPCS). Systematized Nomenclature of Medicine - Clinical Terms (SNOMED CT) will be the first coding system supported by the new V file. The ability to use a richer set of standardized codes should reduce the need to create new non-standard data types, especially health factors.
The purpose of this guide is to provide a single, common document that describes how to install PCE STANDARDIZATION 1.0, as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources and communications plan. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Required builds:

- LEX\*2.0\*102
- XU\*8.0\*657
- PX\*1.0\*216
- DI\*22.2\*3
- DI\*22.2\*5
- OR\*3.0\*361
- OR\*3.0\*377 
- PXRM\*2.0\*45
- PXRM\*2.0\*46
- GMPL\*2\*50
- GMTS\*2.7\*56
- GMTS\*2.7\*110
- GMPL\*2.0\*49

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No single entity is in charge of decision making for deployment, installation, back out and rollback of the PCE Standardization Build. Rather, the Critical Decision Point representatives (commonly referred to as the three in the box) under the Veterans In Process (VIP) will meet and approve release from a business perspective.

If an issue with the software arises that would require a national rollback, then the same three in the box members under VIP will coordinate with several groups (including Patient Safety, Health Product Support, Information Technology Operations Service (ITOPS), and Site leadership) to decide whether a back out and rollback of the software is necessary. The Facility Area Manager has the final authority to require the patch back out and data rollback and accept the associated risks.

The following table provides PCE Standardization 1.0 project information.

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 30%" />
<col style="width: 16%" />
<col style="width: 28%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
<th><strong>Project Phase (See Schedule)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS</td>
<td>Deployment</td>
<td>Plan and schedule installation</td>
<td>After national release</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the installation</td>
<td>After national release</td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
<td>After national release</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS. The IT support will need to include person(s) to install the KIDS builds for all packages involved. Even though installed in a single install session, the other IT support personnel need to be aware</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
<td>After national release</td>
</tr>
<tr class="odd">
<td></td>
<td>N/A – will work under the VistA ATO and security protocols</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>N/A – no equipment is being added</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel</td>
<td>Installations</td>
<td>Coordinate training</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Facility Area Manager and IT support – which may be local or regional</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
<td>After national release</td>
</tr>
<tr class="odd">
<td></td>
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the Development Team during the compliance period. At the end of the compliance period, support will be transitioned to sustainment</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
<td>After national release</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a Patch Release for patches PX\*1\*211, PXRM\*2\*42, GMTS\*2.7\*122, GMPL\*2\*53, and OR\*3\*501 to local sites.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For project dates, please refer to the PCE STANDARDIZATION 1.0 Project Schedule. The site installation is scheduled to run for 30 days, as depicted in the master deployment schedule, PCE STANDARDIZATION 1.0 Project Schedule.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will install the PCE STANDARDIZATION 1.0 multi-package build.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a Patch Release for patches PX\*1\*211, PXRM\*2\*42, GMTS\*2.7\*122, GMPL\*2\*53, and OR\*3\*501 to local sites.

Health Product Support Patch Release of Products and Patches Guide: [Health Product Support Release of Products and Patches Guide](http://vaww.oed.wss.va.gov/process/Library/health_product_support_release_of_products_and_patches_guide.docx).

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3: Documentation

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>Documentation</th>
<th>Documentation File name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Deployment, Installation, Back-Out, and Rollback Guide</td>
<td><p>px_1_0_211_dibr.docx</p>
<p>px_1_0_211_dibr.pdf</p></td>
</tr>
<tr class="even">
<td>PCE Technical Manual</td>
<td><p>pxtm.docx</p>
<p>pxtm.pdf</p></td>
</tr>
<tr class="odd">
<td>PCE User Manual</td>
<td><p>pxum.docx</p>
<p>pxum.pdf</p></td>
</tr>
<tr class="even">
<td>Clinical Reminders Index Technical Manual</td>
<td><p>pxrm_index_tm.docx</p>
<p>pxrm_index_tm.pdf</p></td>
</tr>
<tr class="odd">
<td>Clinical Reminders Manager’s Manual</td>
<td><p>pxrm_mm.docx</p>
<p>pxrm_mm.pdf</p></td>
</tr>
</tbody>
</table>

> *NOTE: In this document, you will see references to both PX\*1\*211 and PX\*1.0\*211. The difference is that PX\*1\*211 is the name of the patch and PX\*1.0\*211 is the name of the build.*

## Related Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 4: Related Web Sites

| Site                                                                               | URL                       | Description                                                                                                                                                 |
|------------------------------------------------------------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="page5" class="anchor"></span>National Clinical Reminders SharePoint Site |                           | Home of the National Clinical Reminders Workgroup. Contains information about the Workgroup, its activities, and other information about Clinical Reminders |
| VA Software Document Library                                                       | <https://www.va.gov/vdl/> | This is the VistA documentation library; all the Clinical Reminders manuals can be found here                                                               |

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE STANDARDIZATION 1.0 project will not replace or modify the existing VistA Architecture; therefore, it will adhere to existing user interfaces unless otherwise noted in this section.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE STANDARDIZATION 1.0 project will not replace or modify the existing VistA Architecture; therefore, it will adhere to existing user interfaces unless otherwise noted in this section.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Project Manager will communicate with Release Agent, OIT Program Manager, and other stakeholders as needed.

#### Deployment/Installation/Back-Out Checklist

Table 5: Deployment/Installation/Back-Out Checklist

| Activity     | Day |
|------------------|---------|
| Release to Field | TBD     |
| Install By       | TBD     |
| Back-Out         | TBD     |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Other than making sure the required builds are installed there are no pre-installation steps.

- LEX\*2.0\*102
- XU\*8.0\*657
- PX\*1.0\*216
- DI\*22.2\*3
- DI\*22.2\*5
- OR\*3.0\*361
- OR\*3.0\*377 
- PXRM\*2.0\*45
- PXRM\*2.0\*46
- GMPL\*2\*50
- GMTS\*2.7\*56
- GMTS\*2.7\*110
- GMPL\*2.0\*49

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

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

The installation should be performed by a user with programmer access and knowledge of installing host files using Kernel Installation and Distribution System \[XPD MAIN\].

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to install the multi-package build that includes builds PX\*1.0\*211, PXRM\*2.0\*42, GMTS\*2.7\*122, GMPL\*2.0\*53, and OR\*3.0\*501.

This patch can be loaded with users on the system, but it should be done during off-hours. Estimated installation time is less than 5 minutes.

1.  <span id="_Toc483268442" class="anchor"></span>Retrieve the host filecontaining the multi-package build

The software for this patch is being distributed as a host file, the name of the host file is: PCE_STANDARDIZATION_1_0.KID.

The host file is available at the following location:

/srv/vista/patches/SOFTWARE/PCE_STANDARDIZATION_1_0.KID

In Chrome and Edge, right click on PCE_STANDARDIZATION_1_0.KID and use Save link as.

> *NOTE: for test site installations, please refer to the build announcement for the location and name of the file to install.*

2.  <span id="_Toc483268443" class="anchor"></span>Install the patch first in a training or test account

Installing in a non-production environment will give you time to get familiar with new functionality.

3.  <span id="_Toc68097687" class="anchor"></span>Back out preparation

These steps are taken in case the patch needs to be backed out.

- Backup files ^AUTTEDT, ^AUTTEXAM, and ^AUTTHF using your site’s policy for backing up data.
- If the steps are unknown, here is a way it can be done, using ^AUTTEDT as an example:
  - Go to the Cache programmer mode command prompt.
  - At the prompt, enter D GOGEN^%ZSPECIAL.
  - At the device prompt, enter the directory and file name where the global backup is to be stored.
  - At the Parameters? Prompt, press \<enter\>.
  - At the Global prompt, enter ^AUTTEDT(.
  - Verify that the file was created and exists in the directory specified.

Example

DEV5A4:DVFDEV\>D GOGEN^%ZSPECIAL

Device: VA5\$:\[Local Directory\]AUTTEDT_BACKUP.GBL

Parameters? ("WNS") =\>

> **WARNING:** Use a "V" format to avoid problems with control characters.

Global ^AUTTEDT(

Global ^

4.  <span id="_Toc489943249" class="anchor"></span>Load the Distribution

From the Kernel Installation and Distribution System Menu, select the Installation Menu and then the option LOAD a Distribution. Enter the directory name where you placed the host file followed by PCE_STANDARDIZATION_1_0.KID at the Host File prompt.

Example

Select Installation Option: LOAD a DistributionEnter a Host File: /srv/vista/software/AppsTeamShare/PCE_STANDARDIZATION_1_0.KIDKIDS Distribution saved on Mar 11, 2021@09:44:34Comment: PCE Standardization 1.0

From the Installation menu, you may elect to use the following options:

5.  <span id="_Toc492197243" class="anchor"></span>Backup a Transport Global

Use the KIDS Installation option, Backup a Transport Global \[XPD BACKUP\]. This option creates a MailMan message that will back up all current routines on your VistA/M system that will be replaced by the builds in this transport global. (If you need to preserve components that are not routines, you must back them up separately.) At the Select INSTALL NAME: prompt, enter PCE STANDARDIZATION 1.0.

<span id="Section485Example" class="anchor"></span>Example

Select Installation \<TEST ACCOUNT\> Option: Backup a Transport GlobalSelect INSTALL NAME: PCE STANDARDIZATION 1.0 Loaded from Distribution3/24/21@09:25:20=\> PCE STANDARDIZATION ;Created on Mar 11, 2021@09:44:34This Distribution was loaded on Mar 24, 2021@09:25:20 with header ofPCE STANDARDIZATION ;Created onMar 11, 2021@09:44:34It consisted of the following Install(s):PCE STANDARDIZATION 1.0 PX\*1.0\*211 PXRM\*2.0\*42 GMTS\*2.7\*122GMPL\*2.0\*53 OR\*3.0\*501Subject: Backup of PCE STANDARDIZATION 1.0 on Mar 24, 2021ReplaceOnly a Single Package Build can do a Build Backup.PCE STANDARDIZATION 1.0 is of type Multi-PackageYou can only Backup the Routines.Select one of the following:R RoutinesEnter response: RNo routines for PCE STANDARDIZATION 1.0Loading Routines for PX\*1.0\*211......................................................................................................................................Loading Routines for PXRM\*2.0\*42....................................................................Loading Routines for GMTS\*2.7\*122.....Loading Routines for GMPL\*2.0\*53.....Loading Routines for OR\*3.0\*501..Select basket to send to: IN// PATCH BACKUPAnd Send to:

6.  <span id="_Toc492197245" class="anchor"></span>Compare Transport Global to Current System

This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.)

7.  <span id="_Toc492197246" class="anchor"></span>Verify Checksums in Transport Global

This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Try loading the host file again. If the problem still exists, log a ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

<span id="Section487Example" class="anchor"></span>Example

CHOOSE 1-2: 2 Option: 2 Verify Checksums in Transport Global

Select Installation \<TEST ACCOUNT\> Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: PCE STANDARDIZATION 1.0

Loaded from Distribution Mar 24, 2021@09:25:20

=\> PCE STANDARDIZATION 1.0 ;Created on Mar 11, 2021@09:44:34

This Distribution was loaded on Mar 24, 2021@09:25:20 with header of

PCE STANDARDIZATION 1.0 ;Created on Mar 24, 2021@09:25:20

It consisted of the following Install(s):

PCE STANDARDIZATION 1.0 PX\*1.0\*211 PXRM\*2.0\*42 GMTS\*2.7\*122

GMPL\*2.0\*53 OR\*3.0\*501

Want each Routine Listed with Checksums: Yes//

DEVICE: HOME// ;;999 TELNET PORT

8.  <span id="_Toc9233992" class="anchor"></span>Install the Build

From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PCE STANDARDIZATION 1.0 and proceed with the install. If you have problems with the installation, log a ServiceNow ticket and/or call the National Help Desk to report the problem.

Select Installation & Distribution System Option: Installation

Select Installation Option: INSTALL PACKAGE(S)

Select INSTALL NAME: PCE STANDARDIZATION 1.0

Answer the following install questions as follows:

- Although typically the answer is "No," you can answer "Yes," to the question:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install?

*Please remember that rebuilding menu trees will increase patch installation time.*

- Answer "No" to the question:

> Want KIDS to INHIBIT LOGONs during the install?

- Answer "No" to the question:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols?

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This summary of routines should match the transport global listing of routines as there are no Post-install routines or actions required.

## Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a known issue with the Document Storage Systems (DSS) product Compliant Coding Module (CCM), creating V POV entries that have a provider narrative pointer of 0. When the V POV Provider Narrative Repair Utility is run, it replaces the 0 pointer with a pointer to the default provider narrative for the ICD-10 diagnosis.

DSS is working on a fix for this issue, but as of the release of PCE STANDARDIZATON 1.0, DSS does not have a projected release date. Rather than having to manually run the utility periodically, it is suggested that sites create a scheduled option to run the utility once a day during off hours.

The option to schedule is: PXQ V POV PROVIDER NARR REPAIR.

After the DSS fixed is released, the scheduled option can be deleted.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Back-Out is necessary for the PCE feature, the steps are described in this section to return to the last known good operational state of the software.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overall Back-Out strategy is to return the routines to their pre-patch state, as well as backing out any necessary data dictionary changes, and option changes.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out should be considered only if all other avenues are exhausted. The development team will be involved if issues with the patch arise.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Results of User Acceptance Testing will be provided.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out should be considered only if all other avenues are exhausted. The development team will be involved if issues with the patch arise.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out Risks are minimal because with utilization of the back-up created prior to patch installation, the system will revert back to what it was prior to installing the new patch.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an issue with the software arises that would require a rollback, then the same three in the box members under VIP will coordinate with several groups (including Patient Safety, Health Product Support, Information Technology Operations Service (ITOPS), and Site leadership) to decide whether a back out and rollback of the software is necessary. The Facility Area Manager has the final authority to require the patch back out and data rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following process if followed will restore the VistA and CPRS systems to the state prior to the installation of PCE Standardization 1.0.

Step 1: Request a copy of the backout build from the development team.

Step 2: Install the backout build.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback should only be completed if the Back-Out Procedure was implemented.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback should only be considered if all other avenues are exhausted and a Patch cannot fix the issue.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback will take place only if the Back-Out Procedure was implemented.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out live data is a rollback risk.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an issue with the software arises that would require a rollback, then the same three in the box members under VIP will coordinate with several groups (including Patient Safety, Health Product Support, Information Technology Operations Service (ITOPS), and Site leadership) to decide whether a back out and rollback of the software is necessary. The Facility Area Manager has the final authority to require the patch back out and data rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The files listed below will need to be deleted:

- New V file for capturing standardized codes other than ICD, CPT and HCPCS.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To be verified by developer.

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term      | Definition                                                                     |
|-----------|--------------------------------------------------------------------------------|
| CPRS      | Computerized Patient Record System                                             |
| GMPL      | Problem List namespace                                                         |
| GMTS      | Health Summary namespace (also HSUM)                                           |
| GUI       | Graphic User Interface                                                         |
| ICD-10-CM | International Classification of Diseases, 10th Revision, Clinical Modification |
| ICD-9-CM  | International Classification of Diseases, 9th Revision, Clinical Modification  |
| ICR       | Integration Control Registration                                               |
| IOC       | Initial Operating Capabilities                                                 |
| MH        | Mental Health                                                                  |
| OHI       | Office of Health Information                                                   |
| OI        | Office of Information                                                          |
| OIT/OI&T  | Office of Information Technology                                               |
| OMHS      | Office of Mental Health Services                                               |
| ORR       | Operational Readiness Review                                                   |
| PCS       | Patient Care Services                                                          |
| PD        | Product Development                                                            |
| PIMS      | Patient Information Management System                                          |
| PXRM      | Clinical Reminder Package namespace                                            |
| RSD       | Requirements Specification Document                                            |
| SME       | Subject Matter Expert                                                          |
| SNOMED CT | Systematic Nomenclature of Medicine of Clinical Terms                          |
| SQA       | Software Quality Assurance                                                     |
| VA        | Department of Veteran Affairs                                                  |
| VHA       | Veterans Health Administration                                                 |
| VISN      | Veterans Integrated Service Network                                            |
| VistA     | Veterans Health Information System and Technology Architecture                 |

# # Appendix A: Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a capture of a PCE STANDARDIZATION 1.0 installation that provides details of the install.

Example: First-time Install

Install Package(s)

Select INSTALL NAME: PCE STANDARDIZATION 1.0 Loaded from Distribution 3/24/21@11:19:22

=\> PCE STANDARDIZATION 1.0 ;Created on Mar 12, 2021@10:38:19

This Distribution was loaded on Mar 24, 2021@11:19:22 with header of

PCE STANDARDIZATION 1.0 ;Created on Mar 12, 2021@10:38:19

It consisted of the following Install(s):

PCE STANDARDIZATION 1.0 PX\*1.0\*211 PXRM\*2.0\*42 GMTS\*2.7\*122

GMPL\*2.0\*53 OR\*3.0\*501

Checking Install for Package PCE STANDARDIZATION 1.0

Install Questions for PCE STANDARDIZATION 1.0

Checking Install for Package PX\*1.0\*211

Install Questions for PX\*1.0\*211

Incoming Files:

815 PCE PARAMETERS

> **NOTE:** You already have the 'PCE PARAMETERS' File.

839.7 PCE DATA SOURCE

> **NOTE:** You already have the 'PCE DATA SOURCE' File.

9000010 VISIT

> **NOTE:** You already have the 'VISIT' File.

9000010.07V POV

> **NOTE:** You already have the 'V POV' File.

9000010.11V IMMUNIZATION

> **NOTE:** You already have the 'V IMMUNIZATION' File.

9000010.12V SKIN TEST

> **NOTE:** You already have the 'V SKIN TEST' File.

9000010.13V EXAM

> **NOTE:** You already have the 'V EXAM' File.

9000010.16V PATIENT ED

> **NOTE:** You already have the 'V PATIENT ED' File.

9000010.18V CPT

> **NOTE:** You already have the 'V CPT' File.

9000010.23V HEALTH FACTORS

> **NOTE:** You already have the 'V HEALTH FACTORS' File.

9000010.71V STANDARD CODES

> **NOTE:** You already have the 'V STANDARD CODES' File.

9999999.09EDUCATION TOPICS

> **NOTE:** You already have the 'EDUCATION TOPICS' File.

9999999.15EXAM

> **NOTE:** You already have the 'EXAM' File.

9999999.27PROVIDER NARRATIVE

> **NOTE:** You already have the 'PROVIDER NARRATIVE' File.

9999999.64HEALTH FACTORS

> **NOTE:** You already have the 'HEALTH FACTORS' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package PXRM\*2.0\*42

Install Questions for PXRM\*2.0\*42

Incoming Files:

802.4 REMINDER FUNCTION FINDING FUNCTIONS (including data)

> **NOTE:** You already have the 'REMINDER FUNCTION FINDING FUNCTIONS' File.

I will REPLACE your data with mine.

811.4 REMINDER COMPUTED FINDINGS (including data)

> **NOTE:** You already have the 'REMINDER COMPUTED FINDINGS' File.

I will OVERWRITE your data with mine.

811.6 REMINDER SPONSOR

> **NOTE:** You already have the 'REMINDER SPONSOR' File.

811.8 REMINDER EXCHANGE (Partial Definition)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

811.9 REMINDER DEFINITION (Partial Definition)

> **NOTE:** You already have the 'REMINDER DEFINITION' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package GMTS\*2.7\*122

Install Questions for GMTS\*2.7\*122

Incoming Files:

142.1 HEALTH SUMMARY COMPONENT (including data)

> **NOTE:** You already have the 'HEALTH SUMMARY COMPONENT' File.

I will REPLACE your data with mine.

Checking Install for Package GMPL\*2.0\*53

Install Questions for GMPL\*2.0\*53

Checking Install for Package OR\*3.0\*501

Install Questions for OR\*3.0\*501

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;9999 TELNET

-------------------------------------------------------------------------------

Install Started for PCE STANDARDIZATION 1.0 :

Mar 24, 2021@11:19:50

Build Distribution Date: Mar 12, 2021

Installing Routines:

Mar 24, 2021@11:19:50

Install Started for PX\*1.0\*211 :

Mar 24, 2021@11:19:50

Build Distribution Date: Mar 12, 2021

Installing Routines:

Mar 24, 2021@11:19:50

Running Pre-Install Routine: PRE^PXP211I

Checking B indexes.

Checking Education Topics.

Checking Exams.

Checking Health Factors.

Removing old data dictionaries.

Deleting data dictionary for file \# 815

Deleting data dictionary for file \# 839.7

Deleting data dictionary for file \# 9000010

Deleting data dictionary for file \# 9000010.07

Deleting data dictionary for file \# 9000010.11

Deleting data dictionary for file \# 9000010.12

Deleting data dictionary for file \# 9000010.13

Deleting data dictionary for file \# 9000010.16

Deleting data dictionary for file \# 9000010.18

Deleting data dictionary for file \# 9000010.23

Deleting data dictionary for file \# 9000010.71

Deleting data dictionary for file \# 9999999.09

Deleting data dictionary for file \# 9999999.15

Deleting data dictionary for file \# 9999999.27

Deleting data dictionary for file \# 9999999.64

Installing Data Dictionaries:

Mar 24, 2021@11:19:50

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing INPUT TEMPLATE

Installing FORM

Installing DIALOG

Installing PROTOCOL

Installing REMOTE PROCEDURE

Installing LIST TEMPLATE

Installing OPTION

Mar 24, 2021@11:19:50

Running Post-Install Routine: POST^PXP211I

Setting undefined Education Topic Class fields.

Setting the Class of Education Topic: ALCOHOL USE AND MEDICAL PROBLEMS to LOCA.

Setting the Class of Education Topic: MEDICAL PROBLEMS OF ALCOHOL (SCREENING) .

Setting the Class of Education Topic: VA-ADVANCE DIRECTIVES to LOCAL.

Setting the Class of Education Topic: VA-ADVANCE DIRECTIVES SCREENING to LOCAL.

Setting the Class of Education Topic: VA-ALCOHOL ABUSE to LOCAL.

…

Setting the Class of Education Topic: VA-SUBSTANCE ABUSE LIFESTYLE ADAPTATIONS.

Setting the Class of Education Topic: VA-SUBSTANCE ABUSE MEDICATIONS to LOCAL.

Setting the Class of Education Topic: VA-SUNSCREEN to LOCAL.

Setting the Class of Education Topic: VA-TDI EDUCATION to LOCAL.

Setting the Class of Education Topic: VA-TOBACCO USE SCREENING to LOCAL.

Setting all Exam Class fields to LOCAL.

Setting the Class of EXAM: ABDOMEN EXAM to LOCAL.

Setting the Class of EXAM: AUDIOMETRIC SCREENING to LOCAL.

Setting the Class of EXAM: AUDIOMETRIC THRESHOLD to LOCAL.

Setting the Class of EXAM: BREAST EXAM to LOCAL.

Setting the Class of EXAM: CHEST EXAM to LOCAL.

…

Setting the Class of EXAM: SCOLIOSIS SCREENING to LOCAL.

Setting the Class of EXAM: SEX DEVELOPMENT EXAM to LOCAL.

Setting the Class of EXAM: TONOMETRY to LOCAL.

Setting the Class of EXAM: TYMPANOGRAM to LOCAL.

Setting the Class of EXAM: VISION EXAM to LOCAL.

Setting undefined Health Factor Class fields.

Setting the Class of HF: 90 DAY MONITORING ZARIT BURDEN INTERVIEW \[C\] to LOCAL.

Setting the Class of HF: AAA SCREENING AND F/U \[C\] to LOCAL.

Setting the Class of HF: AAA SCREENING CONFIRMED AS COMPLETE to LOCAL.

Setting the Class of HF: ABD AORTIC ANEURYSM 3.0-3.9 CM to LOCAL.

Setting the Class of HF: ABD AORTIC ANEURYSM 4.0-5.4 CM to LOCAL.

…

Setting the Class of HF: WH PAP SMEAR \[C\] to LOCAL.

Setting the Class of HF: WH UNDER CARE OF BREAST CARE SPECIALIST to LOCAL.

Setting the Class of HF: WH UNDER CARE OF GYNECOLOGIST to LOCAL.

Setting the Class of HF: WHEELCHAIR CUSHION to LOCAL.

Setting the Class of HF: WHEN HOB ELEVATED RAISE KNEE to LOCAL.

Generating Print Names for entries that do not have one.

Checking Education Topics.

Checking Exams.

Checking Health Factors.

Making sure all .01s are uppercase.

Checking Education Topics.

Checking Exams.

Checking Health Factors.

Appending \[C\] to the .01 of all category health factors.

Starting a TaskMan job to initialize/rebuild V STANDARD CODES indexes.

The task number is: 1067

Creating full length 'B' index PCE Data Source.

Creating new full length 'B' index for Provider Narrative.

V CPT Provider Narrative and Narrative Category Check/Repair

Task Number 1068 started.

V POV Provider Narrative and Narrative Category Check/Repair

Task Number 1069 started.

Updating Routine file...

Updating KIDS files...

PX\*1.0\*211 Installed.

Mar 24, 2021@11:19:51

Not a production UCI

NO Install Message sent

Install Started for PXRM\*2.0\*42 :

Mar 24, 2021@11:19:51

Build Distribution Date: Mar 12, 2021

Installing Routines:

Mar 24, 2021@11:19:51

Running Pre-Install Routine: PRE^PXRMP42I

DISABLE options.

DISABLE protocols.

Removing old data dictionaries.

Deleting data dictionary for file \# 811.6

Installing Data Dictionaries:

Mar 24, 2021@11:19:51

Installing Data:

Mar 24, 2021@11:19:51

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing FORM

Installing OPTION

Mar 24, 2021@11:19:51

Running Post-Install Routine: POST^PXRMP42I

Rebuilding the 'APDS' index for all taxonomies.

Rebuilding the 'D' index for Reminder Definition Print Names..

Deleting the QUERI extracts.

Deleting QUERI patient lists.

Deleting VA-\*IHD QUERI lists.

Deleted 0 VA-\*IHD QUERI lists.

Deleting VA-\*MH QUERI lists.

Deleted 0 VA-\*MH QUERI lists.

Checking for Sponsor Names that need to be changed to all uppercase.

Rebuilding Sponsor B index.

ENABLE options.

ENABLE protocols.

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*42 Installed.

Mar 24, 2021@11:19:51

Not a production UCI

NO Install Message sent

Install Started for GMTS\*2.7\*122 :

Mar 24, 2021@11:19:51

Build Distribution Date: Mar 12, 2021

Installing Routines:

Mar 24, 2021@11:19:51

Installing Data Dictionaries:

Mar 24, 2021@11:19:51

Installing Data:

Mar 24, 2021@11:19:51

Updating Routine file...

Updating KIDS files...

GMTS\*2.7\*122 Installed.

Mar 24, 2021@11:19:51

Not a production UCI

NO Install Message sent

Install Started for GMPL\*2.0\*53 :

Mar 24, 2021@11:19:51

Build Distribution Date: Mar 12, 2021

Installing Routines:

Mar 24, 2021@11:19:51

Running Post-Install Routine: POST^GMPLY53

Scanning Problem Selection lists for problems with inactive codes...

Updating Routine file...

Updating KIDS files...

GMPL\*2.0\*53 Installed.

Mar 24, 2021@11:19:52

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*501 :

Mar 24, 2021@11:19:52

Build Distribution Date: Mar 12, 2021

Installing Routines:

Mar 24, 2021@11:19:52

Updating Routine file...

Updating KIDS files...

OR\*3.0\*501 Installed.

Mar 24, 2021@11:19:52

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

PCE STANDARDIZATION 1.0 Installed.

Mar 24, 2021@11:19:52

No link to PACKAGE file

Install Completed

# Appendix B: Post-Install Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Checksums: PXRM Routines

VISTA\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: PX\*1.0\*211 PCE PATIENT CARE ENCOUNTER PCE PATIENT CARE ENCOUNTER

PXAI value = 41754252

PXAICPT value = 20598915

PXAICPTV value = 20524406

PXAIERR value = 6216565

PXAIHF value = 9054925

PXAIHFV value = 2220137

PXAIICR value = 6645954

PXAIICRV value = 12849072

PXAIIMM value = 17502496

PXAIIMMV value = 37086535

PXAIMOD value = 1896333

PXAIPED value = 8938808

PXAIPEDV value = 1678279

PXAIPL value = 5173433

PXAIPOV value = 33433863

PXAIPOVV value = 18351189

PXAIPRV value = 34241774

PXAIPRVV value = 15796718

PXAISC value = 11421420

PXAISCV value = 2507125

PXAISK value = 11766988

PXAISKV value = 1477924

PXAIVAL value = 16639730

PXAIVST value = 22448199

PXAIVSTV value = 61946878

PXAIXAM value = 8796529

PXAIXAMV value = 1260682

PXAPI value = 47756429

PXAPIDEL value = 62219131

PXBAPI value = 34284976

PXBAPI1 value = 55175372

PXBGCPT value = 6350410

PXBGPOV value = 11440669

PXBGPRV value = 44705768

PXBGSC value = 475760

PXBPMOD value = 5874980

PXCASC value = 7296482

PXCASOR value = 2775351

PXCEAE value = 32040311

PXCEAE1 value = 27691361

PXCEAPPM value = 6633184

PXCECCLS value = 8826649

PXCECPT value = 70996279

PXCECSTP value = 9302776

PXCEHF value = 15706424

PXCEPED value = 15287972

PXCEPOV value = 14572448

PXCEPOV1 value = 27735487

PXCEPRV value = 36686640

PXCESC value = 27503380

PXCESK value = 36345474

PXCETRT value = 5489505

PXCEVFI1 value = 82681322

PXCEVFI2 value = 40463216

PXCEVFIL value = 41330677

PXCEVIMM value = 111978919

PXCEVIS value = 1789130

PXCEXAM value = 14623291

PXCOPY value = 13230793

PXCPTAPI value = 4429390

PXCSPE value = 1132817

PXDATE value = 6790282

PXEDUINQ value = 22377538

PXEDUMGR value = 45662620

PXEDUSM value = 34287130

PXEXINQ value = 13752981

PXEXMGR value = 43002236

PXEXSM value = 34648427

PXHFINQ value = 16231400

PXHFMGR value = 68401016

PXHFSM value = 38219209

PXINPTR value = 6202218

PXINUSE value = 11309382

PXKCO value = 11165933

PXKENC value = 30511135

PXKFCPT value = 3404775

PXKFCPT1 value = 25403589

PXKFHF value = 2002717

PXKFPED value = 1977716

PXKFSC value = 1969432

PXKFVST value = 11571271

PXKFXAM value = 1932215

PXKIMM value = 37780868

PXKMAIN value = 45493882

PXKMAIN1 value = 58789612

PXKMASC value = 61075789

PXKMCODE value = 56724267

PXKMOD value = 3825073

PXKVST value = 19932548

PXKWSRCH value = 42503838

PXLEX value = 15410021

PXLEXS value = 108898999

PXLOCK value = 5931368

PXMCEVNT value = 5530233

PXMCICHK value = 30352461

PXMCLINK value = 149569356

PXMCODES value = 8945406

PXMSG value = 1213330

PXP211I value = 241805409

PXPNARR value = 83426756

PXPXRM value = 261436336

PXPXRM1 value = 13393609

PXPXRMI1 value = 103637358

PXPXRMI2 value = 138986698

PXQPPUTIL value = 106747229

PXQPPUTILRvalue = 36094475

PXQUTL1 value = 58638007

PXRHS05 value = 11668556

PXRHS07 value = 19973501

PXRHS08 value = 10776728

PXRPC value = 165397212

PXRRFDD value = 22151236

PXRRFDP value = 74542328

PXRRGUT value = 4040472

PXRRLCD value = 6029957

PXRRPAD value = 26210713

PXRRPRD value = 6849309

PXRRPRPL value = 4561688

PXRRPRSC value = 3784002

PXRRWLD value = 16863372

PXSINQ value = 20258214

PXSMAN value = 2327055

PXUTIL value = 20118889

PXUTL1 value = 11511510

PXUTLSCC value = 46401485

PXUTLSTP value = 15136046

PXVSC value = 1025184

PXVSCSM value = 5966575

PXVUTIL value = 21160031

PXVXR value = 25897576

PXXDPT value = 2854137

VSIT value = 27628190

VSIT0 value = 2400031

VSITKIL value = 14972517

done

Select BUILD NAME: PXRM\*2.0\*42 CLINICAL REMINDERS CLINICAL REMINDERS

PXRM value = 44585857

PXRMART value = 5793538

PXRMBMI value = 15273669

PXRMCDEF value = 6688274

PXRMCF value = 64545988

PXRMCVRP value = 175521460

PXRMCVTM value = 19003140

PXRMDATA value = 5905920

PXRMDATE value = 73452738

PXRMDBL value = 78662365

PXRMDEV value = 94601871

PXRMEDU value = 13918373

PXRMERRH value = 57078507

PXRMEUT value = 48579737

PXRMEVFI value = 11414696

PXRMEXAM value = 13736448

PXRMEXDB value = 57975072

PXRMEXLC value = 12932001

PXRMEXLI value = 61412209

PXRMEXLR value = 10670039

PXRMEXMH value = 13805661

PXRMEXPD value = 243933810

PXRMEXU1 value = 52468744

PXRMEXU5 value = 72285914

PXRMFF value = 76357476

PXRMFF0 value = 18180135

PXRMFMTO value = 11567960

PXRMHF value = 53277538

PXRMICHK value = 225635853

PXRMICK1 value = 12234519

PXRMIMM value = 11549713

PXRMIOPT value = 11419394

PXRMISF value = 4874044

PXRMLDR value = 20234429

PXRMLEXL value = 186454787

PXRMLOG value = 67488337

PXRMMSER value = 133664475

PXRMOUTC value = 43713968

PXRMOUTM value = 30066077

PXRMOUTU value = 19206492

PXRMP42I value = 19667470

PXRMPDEM value = 65886599

PXRMPDS value = 39667827

PXRMPINF value = 16604052

PXRMPLST value = 53881985

PXRMPNRP value = 1983529

PXRMPRF value = 15513795

PXRMRCUR value = 13442684

PXRMRULE value = 60162556

PXRMSPED value = 6943031

PXRMSXRM value = 100612241

PXRMTAX value = 65755465

PXRMTAXI value = 2022922

PXRMTERM value = 64733107

PXRMTMED value = 11727267

PXRMTXLS value = 147613164

PXRMTXSM value = 76721210

PXRMUID value = 127583

PXRMUIDE value = 18099598

PXRMUTIL value = 150596029

PXRMVCPT value = 53019296

PXRMVITL value = 16703682

PXRMVSC value = 34098955

PXRMVSIT value = 10884562

PXRMXD value = 90486802

PXRMXEVL value = 1704230

PXRMXSU value = 80002311

PXRMXTA value = 54608368

done

Select BUILD NAME: GMTS\*2.7\*122 HEALTH SUMMARY HEALTH SUMMARY

GMTS2 value = 5607837

GMTSOBJ value = 50800869

GMTSPXEP value = 14426413

GMTSPXFP value = 24736179

GMTSPXXP value = 8513180

done

Select BUILD NAME: GMPL\*2.0\*53 PROBLEM LIST PROBLEM LIST

GMPLBLCK value = 86212397

GMPLMGR value = 28551405

GMPLUTL value = 65708125

GMPLX value = 110662238

GMPLY53 value = 465383

done

Select BUILD NAME: OR\*3.0\*501 ORDER ENTRY/RESULTS REPORTING ORDER ENTR

Y/RESULTS REPORTING

ORUTL5 value = 2538248

ORWPCE1 value = 73367544

done

# Appendix C: Install File Print Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

Select OPTION NAME: XPD PRINT INSTALL FILE Install File Print

Install File Print

Select INSTALL NAME: PX\*1.0\*211

=\> PCE STANDARDIZATION 1.0 ;Created on Mar 12, 2021@10:38:19

DEVICE: HOME// ;;99999 TELNET

PACKAGE: PX\*1.0\*211 Mar 24, 2021 1:44 pm PAGE 1

COMPLETED ELAPSED

-------------------------------------------------------------------------------

STATUS: Install Completed DATE LOADED: MAR 24, 2021@11:19:22

INSTALLED BY: TESTMASTER,USER

NATIONAL PACKAGE: PCE PATIENT CARE ENCOUNTER

INSTALL STARTED: MAR 24, 2021@11:19:50 11:19:51 0:00:01

ROUTINES: 11:19:50

PRE-INIT CHECK POINTS:

XPD PREINSTALL STARTED 11:19:50

XPD PREINSTALL COMPLETED 11:19:50

FILES:

PCE PARAMETERS 11:19:50

PCE DATA SOURCE 11:19:50

VISIT 11:19:50

V POV 11:19:50

V IMMUNIZATION 11:19:50

V SKIN TEST 11:19:50

V EXAM 11:19:50

V PATIENT ED 11:19:50

V CPT 11:19:50

V HEALTH FACTORS 11:19:50

V STANDARD CODES 11:19:50

EDUCATION TOPICS 11:19:50

EXAM 11:19:50

PROVIDER NARRATIVE 11:19:50

HEALTH FACTORS 11:19:50

SECURITY KEY 11:19:50

INPUT TEMPLATE 11:19:50

FORM 11:19:50

DIALOG 11:19:50

PROTOCOL 11:19:50

REMOTE PROCEDURE 11:19:50

LIST TEMPLATE 11:19:50

OPTION 11:19:50

POST-INIT CHECK POINTS:

XPD POSTINSTALL STARTED 11:19:51 0:00:01

XPD POSTINSTALL COMPLETED 11:19:51

INSTALL QUESTION PROMPT ANSWER

XPO1 Want KIDS to Rebuild Menu Trees Upon Completion of Install NO

MESSAGES:

Install Started for PX\*1.0\*211 :

Mar 24, 2021@11:19:50

Build Distribution Date: Mar 12, 2021

Installing Routines:

Mar 24, 2021@11:19:50

Running Pre-Install Routine: PRE^PXP211I

Checking B indexes.

Checking Education Topics.

Checking Exams.

Checking Health Factors.

Removing old data dictionaries.

Deleting data dictionary for file \# 815

Deleting data dictionary for file \# 839.7

Deleting data dictionary for file \# 9000010

Deleting data dictionary for file \# 9000010.07

Deleting data dictionary for file \# 9000010.11

Deleting data dictionary for file \# 9000010.12

Deleting data dictionary for file \# 9000010.13

Deleting data dictionary for file \# 9000010.16

Deleting data dictionary for file \# 9000010.18

Deleting data dictionary for file \# 9000010.23

Deleting data dictionary for file \# 9000010.71

Deleting data dictionary for file \# 9999999.09

Deleting data dictionary for file \# 9999999.15

Deleting data dictionary for file \# 9999999.27

Deleting data dictionary for file \# 9999999.64

Installing Data Dictionaries:

Mar 24, 2021@11:19:50

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing INPUT TEMPLATE

Installing FORM

Installing DIALOG

Installing PROTOCOL

Installing REMOTE PROCEDURE

Installing LIST TEMPLATE

Installing OPTION

Mar 24, 2021@11:19:50

Running Post-Install Routine: POST^PXP211I

Setting undefined Education Topic Class fields.

Setting the Class of Education Topic: ALCOHOL USE AND MEDICAL PROBLEMS to LOCAL.

Setting the Class of Education Topic: MEDICAL PROBLEMS OF ALCOHOL (SCREENING) t

o LOCAL.

Setting the Class of Education Topic: VA-ADVANCE DIRECTIVES to LOCAL.

Setting the Class of Education Topic: VA-ADVANCE DIRECTIVES SCREENING to LOCAL.

Setting the Class of Education Topic: VA-ALCOHOL ABUSE to LOCAL.

…

Setting the Class of Education Topic: VA-SUBSTANCE ABUSE LIFESTYLE ADAPTATIONS

to LOCAL.

Setting the Class of Education Topic: VA-SUBSTANCE ABUSE MEDICATIONS to LOCAL.

Setting the Class of Education Topic: VA-SUNSCREEN to LOCAL.

Setting the Class of Education Topic: VA-TDI EDUCATION to LOCAL.

Setting the Class of Education Topic: VA-TOBACCO USE SCREENING to LOCAL.

Setting all Exam Class fields to LOCAL.

Setting the Class of EXAM: ABDOMEN EXAM to LOCAL.

Setting the Class of EXAM: AUDIOMETRIC SCREENING to LOCAL.

Setting the Class of EXAM: AUDIOMETRIC THRESHOLD to LOCAL.

Setting the Class of EXAM: BREAST EXAM to LOCAL.

Setting the Class of EXAM: CHEST EXAM to LOCAL.

…

Setting the Class of EXAM: SCOLIOSIS SCREENING to LOCAL.

Setting the Class of EXAM: SEX DEVELOPMENT EXAM to LOCAL.

Setting the Class of EXAM: TONOMETRY to LOCAL.

Setting the Class of EXAM: TYMPANOGRAM to LOCAL.

Setting the Class of EXAM: VISION EXAM to LOCAL.

Setting undefined Health Factor Class fields.

Setting the Class of HF: 90 DAY MONITORING ZARIT BURDEN INTERVIEW \[C\] to LOCAL.

Setting the Class of HF: AAA SCREENING AND F/U \[C\] to LOCAL.

Setting the Class of HF: AAA SCREENING CONFIRMED AS COMPLETE to LOCAL.

Setting the Class of HF: ABD AORTIC ANEURYSM 3.0-3.9 CM to LOCAL.

Setting the Class of HF: ABD AORTIC ANEURYSM 4.0-5.4 CM to LOCAL.

…

Setting the Class of HF: WHEN HOB ELEVATED RAISE KNEE to LOCAL.

Setting the Class of HF: ZOSTER IMMUNIZATION \[C\] to LOCAL.

Setting the Class of HF: ZZMH NOSHOW INITIATE WELLNESS CHECK to LOCAL.

Setting the Class of HF: ZZMH NOSHOW SUPPORT CONTACT to LOCAL.

Setting the Class of HF: ZZMH NOSHOW UNABLE TO REACH PT to LOCAL.

Generating Print Names for entries that do not have one.

Checking Education Topics.

Checking Exams.

Checking Health Factors.

Making sure all .01s are uppercase.

Checking Education Topics.

Checking Exams.

Checking Health Factors.

Appending \[C\] to the .01 of all category health factors.

Starting a TaskMan job to initialize/rebuild V STANDARD CODES indexes.

The task number is: 1067

Creating full length 'B' index PCE Data Source.

Creating new full length 'B' index for Provider Narrative.

V CPT Provider Narrative and Narrative Category Check/Repair

Task Number 1068 started.

V POV Provider Narrative and Narrative Category Check/Repair

Task Number 1069 started.

Updating Routine file...

Updating KIDS files...

PX\*1.0\*211 Installed.

Mar 24, 2021@11:19:51

Not a production UCI

NO Install Message sent

# Appendix D: Build File Print Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the KIDS Build File Print option to print out the build components. You can select the multi-package build or any of the individual builds included in the multi-package build.

Select OPTION NAME: XPD PRINT BUILD Build File Print

Build File Print

Select BUILD NAME: PCE STANDARDIZATION 1.0 (Multi-Package)

PX\*1.0\*211

PXRM\*2.0\*42

GMTS\*2.7\*122

GMPL\*2.0\*53

OR\*3.0\*501

DEVICE: HOME// ;;99999 TELNET

PACKAGE: PCE STANDARDIZATION 1.0 Mar 24, 2021 1:54 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: MULTI-PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Mar 12, 2021

DESCRIPTION:

This multi-package builds contains the PCE Standardization build and the

supporting builds from other packages.

For detailed information and installation instructions, please see the PCE

Standardization 1.0 Installation Guide.

SEQUENCE OF BUILDS:

1 PX\*1.0\*211 Required to Continue

2 PXRM\*2.0\*42 Required to Continue

3 GMTS\*2.7\*122 Required to Continue

4 GMPL\*2.0\*53 Required to Continue

5 OR\*3.0\*501 Required to Continue

PACKAGE: PX\*1.0\*211 Mar 24, 2021 1:54 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: PCE PATIENT CARE ENCOUNTER ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Mar 12, 2021

DESCRIPTION:

PCE data standardization, for detailed information and installation

instructions, please see the PCE Standardization 1.0 Installation Guide.

To take full advantage of the PCE standardization work, changes to VistA

applications that use PCE data are required. These applications include

Clinical Reminders, Health Summary, Problem List, and Order Entry/Results

Reporting. To make it easier for sites, the builds for PCE (PX\*1.0\*211),

Clinical Reminders (PXRM\*2.0\*42), Health Summary (GMTS\*2.7\*122), Problem List

(GMPL\*2.0\*53), and Order Entry/Results Reporting (OR\*3.0\*501) are being

distributed in a multi-package build named PCE STANDARDIZATION 1.0.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: PRE^PXP211I DELETE PRE-INIT ROUTINE: No

POST-INIT ROUTINE: POST^PXP211I DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

815 PCE PARAMETERS YES YES NO

839.7 PCE DATA SOURCE YES YES NO

9000010 VISIT YES YES NO

9000010.07 V POV YES YES NO

9000010.11 V IMMUNIZATION YES YES NO

9000010.12 V SKIN TEST YES YES NO

9000010.13 V EXAM YES YES NO

9000010.16 V PATIENT ED YES YES NO

9000010.18 V CPT YES YES NO

9000010.23 V HEALTH FACTORS YES YES NO

9000010.71 V STANDARD CODES YES YES NO

9999999.09 EDUCATION TOPICS YES YES NO

9999999.15 EXAM YES YES NO

9999999.27 PROVIDER NARRATIVE YES YES NO

9999999.64 HEALTH FACTORS YES YES NO

INPUT TEMPLATE: ACTION:

PX SITE PARAMETER EDIT FILE \#815 SEND TO SITE

FORM: ACTION:

PX EDUCATION TOPIC CHANGE LOG FILE \#9999999.09SEND TO SITE

PX EDUCATION TOPIC EDIT FILE \#9999999.09 SEND TO SITE

PX EDUCATION TOPIC EDIT NCM FILE \#9999999.09SEND TO SITE

PX EXAM CHANGE LOG FILE \#9999999.15 SEND TO SITE

PX EXAM EDIT FILE \#9999999.15 SEND TO SITE

PX EXAM EDIT NCM FILE \#9999999.15 SEND TO SITE

PX HEALTH FACTOR CHANGE LOG FILE \#9999999.64SEND TO SITE

PX HEALTH FACTOR EDIT FILE \#9999999.64 SEND TO SITE

PX HEALTH FACTOR EDIT NCM FILE \#9999999.64 SEND TO SITE

PX HF CATEGORY EDIT FILE \#9999999.64 SEND TO SITE

PX VSC EDIT FILE \#9000010.71 SEND TO SITE

DIALOG: ACTION:

8390001.001 SEND TO SITE

8390001.002 SEND TO SITE

8390001.003 SEND TO SITE

ROUTINE: ACTION:

PXAI SEND TO SITE

PXAICPT SEND TO SITE

PXAICPTV SEND TO SITE

PXAIERR SEND TO SITE

PXAIHF SEND TO SITE

PXAIHFV SEND TO SITE

PXAIICR SEND TO SITE

PXAIICRV SEND TO SITE

PXAIIMM SEND TO SITE

PXAIIMMV SEND TO SITE

PXAIMOD SEND TO SITE

PXAIPED SEND TO SITE

PXAIPEDV SEND TO SITE

PXAIPL SEND TO SITE

PXAIPOV SEND TO SITE

PXAIPOVV SEND TO SITE

PXAIPRV SEND TO SITE

PXAIPRVV SEND TO SITE

PXAISC SEND TO SITE

PXAISCV SEND TO SITE

PXAISK SEND TO SITE

PXAISKV SEND TO SITE

PXAIVAL SEND TO SITE

PXAIVST SEND TO SITE

PXAIVSTV SEND TO SITE

PXAIXAM SEND TO SITE

PXAIXAMV SEND TO SITE

PXAPI SEND TO SITE

PXAPIDEL SEND TO SITE

PXBAPI SEND TO SITE

PXBAPI1 SEND TO SITE

PXBGCPT SEND TO SITE

PXBGPOV SEND TO SITE

PXBGPRV SEND TO SITE

PXBGSC SEND TO SITE

PXBPMOD SEND TO SITE

PXCASC SEND TO SITE

PXCASOR SEND TO SITE

PXCEAE SEND TO SITE

PXCEAE1 SEND TO SITE

PXCEAPPM SEND TO SITE

PXCECCLS SEND TO SITE

PXCECPT SEND TO SITE

PXCECSTP SEND TO SITE

PXCEHF SEND TO SITE

PXCEPED SEND TO SITE

PXCEPOV SEND TO SITE

PXCEPOV1 SEND TO SITE

PXCEPRV SEND TO SITE

PXCESC SEND TO SITE

PXCESK SEND TO SITE

PXCETRT SEND TO SITE

PXCEVFI1 SEND TO SITE

PXCEVFI2 SEND TO SITE

PXCEVFIL SEND TO SITE

PXCEVIMM SEND TO SITE

PXCEVIS SEND TO SITE

PXCEXAM SEND TO SITE

PXCOPY SEND TO SITE

PXCPTAPI SEND TO SITE

PXCSPE SEND TO SITE

PXDATE SEND TO SITE

PXEDUINQ SEND TO SITE

PXEDUMGR SEND TO SITE

PXEDUSM SEND TO SITE

PXEXINQ SEND TO SITE

PXEXMGR SEND TO SITE

PXEXSM SEND TO SITE

PXHFINQ SEND TO SITE

PXHFMGR SEND TO SITE

PXHFSM SEND TO SITE

PXINPTR SEND TO SITE

PXINUSE SEND TO SITE

PXKCO SEND TO SITE

PXKENC SEND TO SITE

PXKFCPT SEND TO SITE

PXKFCPT1 SEND TO SITE

PXKFHF SEND TO SITE

PXKFPED SEND TO SITE

PXKFSC SEND TO SITE

PXKFVST SEND TO SITE

PXKFXAM SEND TO SITE

PXKIMM SEND TO SITE

PXKMAIN SEND TO SITE

PXKMAIN1 SEND TO SITE

PXKMASC SEND TO SITE

PXKMCODE SEND TO SITE

PXKMOD SEND TO SITE

PXKVST SEND TO SITE

PXKWSRCH SEND TO SITE

PXLEX SEND TO SITE

PXLEXS SEND TO SITE

PXLOCK SEND TO SITE

PXMCEVNT SEND TO SITE

PXMCICHK SEND TO SITE

PXMCLINK SEND TO SITE

PXMCODES SEND TO SITE

PXMSG SEND TO SITE

PXP211I SEND TO SITE

PXPNARR SEND TO SITE

PXPXRM SEND TO SITE

PXPXRM1 SEND TO SITE

PXPXRMI1 SEND TO SITE

PXPXRMI2 SEND TO SITE

PXQPPUTIL SEND TO SITE

PXQPPUTILR SEND TO SITE

PXQUTL1 SEND TO SITE

PXRHS05 SEND TO SITE

PXRHS07 SEND TO SITE

PXRHS08 SEND TO SITE

PXRPC SEND TO SITE

PXRRFDD SEND TO SITE

PXRRFDP SEND TO SITE

PXRRGUT SEND TO SITE

PXRRLCD SEND TO SITE

PXRRPAD SEND TO SITE

PXRRPRD SEND TO SITE

PXRRPRPL SEND TO SITE

PXRRPRSC SEND TO SITE

PXRRWLD SEND TO SITE

PXSINQ SEND TO SITE

PXSMAN SEND TO SITE

PXUTIL SEND TO SITE

PXUTL1 SEND TO SITE

PXUTLSCC SEND TO SITE

PXUTLSTP SEND TO SITE

PXVSC SEND TO SITE

PXVSCSM SEND TO SITE

PXVUTIL SEND TO SITE

PXVXR SEND TO SITE

PXXDPT SEND TO SITE

VSIT SEND TO SITE

VSIT0 SEND TO SITE

VSITKIL SEND TO SITE

OPTION: ACTION:

PX DELETE ENCOUNTERS W/O VISIT SEND TO SITE

PX IRM MAIN MENU USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PXQ PCE/SD DEBUGGING UTILITIES USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PXQ PRIMARY PROVIDER REPAIR SEND TO SITE

PXQ PROVIDER NARR REPAIR MENU SEND TO SITE

PXQ V CPT PROVIDER NARR REPAIR SEND TO SITE

PXQ V POV PROVIDER NARR REPAIR SEND TO SITE

PXTT ACTIVATE/INACTIVATE MENU DELETE AT SITE

PXTT EDIT EDUCATION TOPICS SEND TO SITE

PXTT EDIT EXAM SEND TO SITE

PXTT EDIT HEALTH FACTORS SEND TO SITE

PXTT EDIT IMMUNIZATION LOT SEND TO SITE

PXTT EDIT IMMUNIZATIONS DELETE AT SITE

PXTT EDIT SKIN TESTS DELETE AT SITE

PXTT EDU TOPICS MANAGEMENT SEND TO SITE

PXTT EXAM MANAGEMENT SEND TO SITE

PXTT HEALTH FACTOR MANAGEMENT SEND TO SITE

PXTT INACTIVE MAPPED CODES RPT SEND TO SITE

PXTT INQUIRE EDUC TOPIC SEND TO SITE

PXTT LIST ACTIVE EDUC TOPICS SEND TO SITE

PXTT LIST ALL EDUC TOPICS SEND TO SITE

PXTT LIST EXAMS SEND TO SITE

PXTT LIST HEALTH FACTORS SEND TO SITE

PXTT LIST IMMUNIZATIONS SEND TO SITE

PXTT LIST SKIN TESTS SEND TO SITE

PXTT PCE INFORMATION ONLY USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PXTT TABLE MAINTENANCE SEND TO SITE

PXTT TEXT/KEYWORD SEARCH SEND TO SITE

PXV EDIT DEFAULT RESPONSES SEND TO SITE

SECURITY KEY: ACTION:

PX CODE MAPPING SEND TO SITE

PROTOCOL: ACTION:

ICD CODE UPDATE EVENT USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

ICPT CODE UPDATE EVENT USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PX CODE SET UPDATE CPT SEND TO SITE

PX CODE SET UPDATE ICD SEND TO SITE

PX EDUCATION TOPICS ADD SEND TO SITE

PX EDUCATION TOPICS CHANGE LOG SEND TO SITE

PX EDUCATION TOPICS COPY SEND TO SITE

PX EDUCATION TOPICS EDIT SEND TO SITE

PX EDUCATION TOPICS INQUIRE SEND TO SITE

PX EDUCATION TOPICS MANAGEMENT MENU SEND TO SITE

PX EDUCATION TOPICS SELECT ENTRY SEND TO SITE

PX EXAM ADD SEND TO SITE

PX EXAM CHANGE LOG SEND TO SITE

PX EXAM COPY SEND TO SITE

PX EXAM EDIT SEND TO SITE

PX EXAM INQUIRE SEND TO SITE

PX EXAM MANAGEMENT MENU SEND TO SITE

PX EXAM SELECT ENTRY SEND TO SITE

PX HEALTH FACTOR ADD SEND TO SITE

PX HEALTH FACTOR CHANGE LOG SEND TO SITE

PX HEALTH FACTOR COPY SEND TO SITE

PX HEALTH FACTOR EDIT SEND TO SITE

PX HEALTH FACTOR INQUIRE SEND TO SITE

PX HEALTH FACTOR MANAGEMENT MENU SEND TO SITE

PX HEALTH FACTOR SELECT ENTRY SEND TO SITE

PXCE ADD/EDIT MENU MERGE MENU ITEMS

PXCE LEXICON REMOVE CODE(S) SEND TO SITE

PXCE LEXICON SELECT CODE(S) SEND TO SITE

PXCE LEXICON SELECT ENTRY SEND TO SITE

PXCE LEXICON SELECT MENU SEND TO SITE

PXCE STANDARD CODES ADD SEND TO SITE

LIST TEMPLATE: ACTION:

PX EDUCATION TOPICS MANAGEMENT SEND TO SITE

PX EXAM MANAGEMENT SEND TO SITE

PX HEALTH FACTOR MANAGEMENT SEND TO SITE

PXCE ADD/EDIT MENU SEND TO SITE

PXCE STANDARD CODES SELECT SEND TO SITE

REMOTE PROCEDURE: ACTION:

PX SAVE DATA SEND TO SITE

REQUIRED BUILDS: ACTION:

LEX\*2.0\*102 Don't install, remove global

XU\*8.0\*657 Don't install, remove global

PX\*1.0\*216 Don't install, remove global

DI\*22.2\*3 Don't install, remove global

DI\*22.2\*5 Don't install, remove global

PACKAGE: PXRM\*2.0\*42 Mar 24, 2021 1:54 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: CLINICAL REMINDERS ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Mar 12, 2021

DESCRIPTION:

This patch supports PCE standardization.

To take full advantage of the PCE standardization work, changes to VistA

applications that use PCE data are required. These applications include

Clinical Reminders, Health Summary, Problem List, and Order Entry/Results

Reporting. To make it easier for sites, the builds for PCE (PX\*1.0\*211),

Clinical Reminders (PXRM\*2.0\*42), Health Summary (GMTS\*2.7\*122), Problem List

(GMPL\*2.0\*53), and Order Entry/Results Reporting (OR\*3.0\*501) are being

distributed in a multi-package build named PCE STANDARDIZATION 1.0.

For detailed information and installation instructions, please see the PCE

Standardization 1.0 Installation Guide.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: PRE^PXRMP42I DELETE PRE-INIT ROUTINE: No

POST-INIT ROUTINE: POST^PXRMP42I DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

802.4 REMINDER FUNCTION FINDING FUNCTIONSNOYES YES REPL NO NO

DATA SCREEN: I (Y=8)!(Y=9)

811.4 REMINDER COMPUTED FINDINGS NO YES YES OVER NO NO

DATA SCREEN: I (Y=35)!(Y=86)!(Y=88)

811.6 REMINDER SPONSOR YES YES NO

811.8 REMINDER EXCHANGE YES YES NO NO

Partial DD: subDD: 811.805

811.9 REMINDER DEFINITION YES YES NO NO

Partial DD: subDD: 811.9 fld: 1.2

PRINT TEMPLATE: ACTION:

PXRM SPONSOR LIST FILE \#811.6 SEND TO SITE

FORM: ACTION:

PXRM DEF PRINT NAME EDIT FILE \#811.9 SEND TO SITE

PXRM TAXONOMY EDIT FILE \#811.2 SEND TO SITE

ROUTINE: ACTION:

PXRM SEND TO SITE

PXRMART SEND TO SITE

PXRMBMI SEND TO SITE

PXRMCDEF SEND TO SITE

PXRMCF SEND TO SITE

PXRMCVRP SEND TO SITE

PXRMCVTM SEND TO SITE

PXRMDATA SEND TO SITE

PXRMDATE SEND TO SITE

PXRMDBL SEND TO SITE

PXRMDEV SEND TO SITE

PXRMEDU SEND TO SITE

PXRMERRH SEND TO SITE

PXRMEUT SEND TO SITE

PXRMEVFI SEND TO SITE

PXRMEXAM SEND TO SITE

PXRMEXDB SEND TO SITE

PXRMEXLC SEND TO SITE

PXRMEXLI SEND TO SITE

PXRMEXLR SEND TO SITE

PXRMEXMH SEND TO SITE

PXRMEXPD SEND TO SITE

PXRMEXU1 SEND TO SITE

PXRMEXU5 SEND TO SITE

PXRMFF SEND TO SITE

PXRMFF0 SEND TO SITE

PXRMFMTO SEND TO SITE

PXRMHF SEND TO SITE

PXRMICHK SEND TO SITE

PXRMICK1 SEND TO SITE

PXRMIMM SEND TO SITE

PXRMIOPT SEND TO SITE

PXRMISF SEND TO SITE

PXRMLDR SEND TO SITE

PXRMLEXL SEND TO SITE

PXRMLOG SEND TO SITE

PXRMMSER SEND TO SITE

PXRMOUTC SEND TO SITE

PXRMOUTM SEND TO SITE

PXRMOUTU SEND TO SITE

PXRMPDEM SEND TO SITE

PXRMPDS SEND TO SITE

PXRMPINF SEND TO SITE

PXRMPLST SEND TO SITE

PXRMPNRP SEND TO SITE

PXRMPRF SEND TO SITE

PXRMRCUR SEND TO SITE

PXRMRULE SEND TO SITE

PXRMSPED SEND TO SITE

PXRMSXRM SEND TO SITE

PXRMTAX SEND TO SITE

PXRMTAXI SEND TO SITE

PXRMTERM SEND TO SITE

PXRMTMED SEND TO SITE

PXRMTXLS SEND TO SITE

PXRMTXSM SEND TO SITE

PXRMUID SEND TO SITE

PXRMUIDE SEND TO SITE

PXRMUTIL SEND TO SITE

PXRMVCPT SEND TO SITE

PXRMVITL SEND TO SITE

PXRMVSC SEND TO SITE

PXRMVSIT SEND TO SITE

PXRMXD SEND TO SITE

PXRMXEVL SEND TO SITE

PXRMXSU SEND TO SITE

PXRMXTA SEND TO SITE

OPTION: ACTION:

PXRM COVER SHEET REMINDER RPT SEND TO SITE

PXRM DEF PRINT NAME EDIT SEND TO SITE

PXRM DEF PRINT NAME REPORT SEND TO SITE

PXRM EXTRACT VA-IHD QUERI DELETE AT SITE

PXRM EXTRACT VA-MH QUERI DELETE AT SITE

PXRM REMINDER MANAGEMENT USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PXRM REMINDER REPORTS USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

INSTALL QUESTIONS:

Default Rebuild Menu Trees Upon Completion of Install: NO

Default INHIBIT LOGONs during the install: NO

Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

REQUIRED BUILDS: ACTION:

PX\*1.0\*211 Don't install, remove global

PXRM\*2.0\*45 Don't install, remove global

PXRM\*2.0\*46 Don't install, remove global

PACKAGE: GMTS\*2.7\*122 Mar 24, 2021 1:54 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: HEALTH SUMMARY ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Mar 12, 2021

DESCRIPTION:

This patch supports PCE standardization.

To take full advantage of the PCE standardization work, changes to VistA

applications that use PCE data are required. These applications include

Clinical Reminders, Health Summary, Problem List, and Order Entry/Results

Reporting. To make it easier for sites, the builds for PCE (PX\*1.0\*211),

Clinical Reminders (PXRM\*2.0\*42), Health Summary (GMTS\*2.7\*122), Problem List

(GMPL\*2.0\*53), and Order Entry/Results Reporting (OR\*3.0\*501) are being

distributed in a multi-package build named PCE STANDARDIZATION 1.0.

For detailed information and installation instructions, please see the PCE

Standardization 1.0 Installation Guide.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

142.1 HEALTH SUMMARY COMPONENT NO YES YES REPL NO NO

DATA SCREEN: I (Y=203)!(Y=230)

ROUTINE: ACTION:

GMTS2 SEND TO SITE

GMTSOBJ SEND TO SITE

GMTSPXEP SEND TO SITE

GMTSPXFP SEND TO SITE

GMTSPXXP SEND TO SITE

INSTALL QUESTIONS:

Default Rebuild Menu Trees Upon Completion of Install: NO

Default INHIBIT LOGONs during the install: NO

Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

REQUIRED BUILDS: ACTION:

GMTS\*2.7\*56 Don't install, remove global

GMTS\*2.7\*110 Don't install, remove global

PX\*1.0\*211 Don't install, remove global

PACKAGE: GMPL\*2.0\*53 Mar 24, 2021 1:54 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: PROBLEM LIST ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Mar 12, 2021

DESCRIPTION:

This patch supports PCE standardization.

To take full advantage of the PCE standardization work, changes to VistA

applications that use PCE data are required. These applications include

Clinical Reminders, Health Summary, Problem List, and Order Entry/Results

Reporting. To make it easier for sites, the builds for PCE (PX\*1.0\*211),

Clinical Reminders (PXRM\*2.0\*42), Health Summary (GMTS\*2.7\*122), Problem List

(GMPL\*2.0\*53), and Order Entry/Results Reporting (OR\*3.0\*501) are being

distributed in a multi-package build named PCE STANDARDIZATION 1.0.

For detailed information and installation instructions, please see the PCE

Standardization 1.0 Installation Guide.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: POST^GMPLY53 DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

ROUTINE: ACTION:

GMPLBLCK SEND TO SITE

GMPLMGR SEND TO SITE

GMPLUTL SEND TO SITE

GMPLX SEND TO SITE

REQUIRED BUILDS: ACTION:

GMPL\*2.0\*49 Don't install, remove global

PX\*1.0\*211 Don't install, remove global

PACKAGE: OR\*3.0\*501 Mar 24, 2021 1:54 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: ORDER ENTRY/RESULTS REPORTING ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Mar 12, 2021

DESCRIPTION:

To take full advantage of the PCE standardization work, changes to VistA

applications that use PCE data are required. These applications include

Clinical Reminders, Health Summary, Problem List, and Order Entry/Results

Reporting. To make it easier for sites, the builds for PCE (PX\*1.0\*211),

Clinical Reminders (PXRM\*2.0\*42), Health Summary (GMTS\*2.7\*122), Problem List

(GMPL\*2.0\*53), and Order Entry/Results Reporting (OR\*3.0\*501) are being

distributed in a multi-package build named PCE STANDARDIZATION 1.0.

For detailed information and installation instructions, please see the PCE

Standardization 1.0 Installation Guide.

In the documentation for DATA2PCE the description of the variable PPEDIT,

which is one of the input parameters to DATA2PCE is:

PPEDIT

(Optional) If an existing encounter already has a Primary Provider and you

want to edit it set this to 1.

Although it was documented, DATA2PCE did not actually enforce this, the

primary provider could be edited even when PPEDIT did not equal 1. DATA2PCE

was changed in PX\*1.0\*211 to work as documented. After that change, internal

testing found that the primary provider could no longer be edited from CPRS.

The cause of this was tracked to the way CPRS was calling DATA2PCE, it was not

properly passing the PPEDIT parameter. The call to DATA2PCE in the routine

ORWPCE1 was corrected.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

ROUTINE: ACTION:

ORUTL5 SEND TO SITE

ORWPCE1 SEND TO SITE

REQUIRED BUILDS: ACTION:

OR\*3.0\*361 Don't install, remove global

OR\*3.0\*531 Don't install, remove global

Build File Print

PCE STANDARDIZATION 1.0 (Multi-Package)

PX\*1.0\*211

PXRM\*2.0\*42

GMTS\*2.7\*122

GMPL\*2.0\*53

OR\*3.0\*501

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PX*1*234 PCE Standardization Deployment, Installation, Back-Out and Rollback Guide

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Choose the PackMan message containing this build. Then select

the INSTALL/CHECK MESSAGE PackMan option to load the build.

2\. From the Kernel Installation and Distribution System Menu,

select the Installation Menu. From this menu,

1.  Select the Verify Checksums in Transport Global

option to confirm the integrity of the routines that

are in the transport global. When prompted for the

INSTALL NAME enter the patch or build name.

PX\*1.0\*234

B. Select the Backup a Transport Global option to create

a backup message. You must use this option and specify

what to backup; the entire Build or just Routines.

The backup message can be used to restore the routines

and components of the build to the pre-patch condition.

i\. At the Installation option menu, select Backup

a Transport Global

ii\. At the Select INSTALL NAME prompt, enter your

build PX\*1.0\*234

iii\. When prompted for the following, enter “R” for

Routines or “B” for Build.

Select one of the following:

B Build

R Routines

Enter response: Build

iv\. When prompted “Do you wish to secure this message? NO//”,

press \<enter\> and take the default response of “NO”.

v\. When prompted with, “Send mail to: Last name, First

Name”, press \<enter\> to take default recipient. Add

any additional recipients.

vi\. When prompted with “Select basket to send to: IN//”,

press \<enter\> and take the default IN mailbox or select

a different mailbox.

C. You may also elect to use the following options:

i\. Print Transport Global – This option will allow

you to view the components of the KIDS build.

ii\. Compare Transport Global to Current System - This

option will allow you to view all changes that will

be made when this patch is installed. It compares

all of the components of this patch, such as

routines, DDs, templates, etc.

D. Select the Install Package(s) option and choose the

patch to install.

i\. If prompted 'Want KIDS to Rebuild Menu Trees Upon

Completion of Install? NO//', answer NO.

ii\. When prompted 'Want KIDS to INHIBIT LOGONs during the

install? NO//', answer NO.

iii\. When prompted 'Want to DISABLE Scheduled Options, Menu

Options, and Protocols? NO//', answer NO.
