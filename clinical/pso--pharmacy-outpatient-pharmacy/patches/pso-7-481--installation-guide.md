---
title: PSO*7*481 Non-VA Provider Updates Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Non-VA Provider Updates
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*481
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - provider
  - patch
  - installation
  - back
  - import
  - providers
  - deployment
  - rollback
page_count: 0
word_count: 5632
section_count: 33
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_ig_p481.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_ig_p481.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Non-VA Provider Updates (PSO\*7.0\*481)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](pso-7-481-non-va-provider-updates-installation-guide/001.png)

February 2019

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date    | Description     | Author                             |
|---------|-----------------|------------------------------------|
| 02/2019 | Initial Release | <span class="mark">REDACTED</span> |

<span id="_Toc859037" class="anchor"></span>Table : OI Field Offices

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and the roles and responsibilities involved in all these activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software. It should be structured appropriately to reflect these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan are required to be completed prior to Critical Decision Point \#2 (CD \#2). The expectation is that they will be updated throughout the lifecycle of the project for each build, as needed.

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
  - [Access Requirements and Skills Needed for the Installation and Importing](#access-requirements-and-skills-needed-for-the-installation-and-importing)
  - [Installation Procedure](#installation-procedure)
    - [PSO\7.0\481 VistA Installation](#pso70481-vista-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [Importing Non-VA Providers](#importing-non-va-providers)
  - [SERVICE/SECTION (#29) field](#servicesection-29-field)
    - [TITLE (#3.1) field](#title-31-field)
    - [PSDMGR key](#psdmgr-key)
    - [Non-VA Provider Import \[PSO NON-VA PROVIDER IMPORT\]](#non-va-provider-import-pso-non-va-provider-import)
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
    - [Inactivate Imported Non-VA Providers](#inactivate-imported-non-va-providers)
    - [Option Deletion](#option-deletion)
    - [Routine Deletion](#routine-deletion)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the Non-VA Provider Updates patch, PSO\*7.0\*481, and how to back-out the product.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single common document that describes how, when, where, and to whom the Non-VA Provider Updates patch PSO\*7.0\*481 will be deployed and installed, as well as how it is to be backed out, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Released patch XU\*8.0\*630 is a required patch for the Non-VA Provider Updates patch PSO\*7.0\*481 and must be installed in the same account with PSO\*7.0\*481.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-VA Provider Updates patch PSO\*7.0\*481 is expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. Non-VA Provider Updates patch PSO\*7.0\*481 utilizes existing nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity oversees decision making for deployment, installation, back out and rollback of Non-VA Provider Updates patch PSO\*7.0\*481. The release agent and application coordinators under the VIP will approve deployment and install from an Office of Information and Technology (OIT) perspective. If an issue with the software arises, then the area managers and other site leadership will meet. A back out and rollback decision of the software will be made with the input from Patient Safety, Health Product Support, IT Operations, and Services personnel. The following table provides information for Non-VA Provider Updates patch PSO\*7.0\*481.

<span id="_Toc859036" class="anchor"></span>Table 1: Roles and Responsibilities

<table>
<caption><p><span id="_Toc859038" class="anchor"></span>Table : Manuals to be Downloaded</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 16%" />
<col style="width: 39%" />
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
<td>IT Operations and Services personnel</td>
<td>Deployment</td>
<td>Plan and schedule deployment</td>
</tr>
<tr class="even">
<td>IT Operations and Services personnel</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
</tr>
<tr class="odd">
<td>Site personnel</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="even">
<td><p>IT Operations and Services personnel.</p>
<p>The IT support will need to include person(s) to install the Kernel Installation &amp; Distribution System (KIDS) build</p></td>
<td>Installation</td>
<td>Plan and schedule installation</td>
</tr>
<tr class="odd">
<td>N/A – will work under the VistA ATO and security protocols.</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
</tr>
<tr class="even">
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
</tr>
<tr class="odd">
<td>IT Operations and Services personnel</td>
<td>Implementation</td>
<td>Retrieve and place site specific .csv file for importing</td>
</tr>
<tr class="even">
<td>IT Operations and Services personnel</td>
<td>Implementation</td>
<td>Coordinate with pharmacy staff and import the non-VA provider data</td>
</tr>
<tr class="odd">
<td>Facility CIO, IT Operations, and Services personnel</td>
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

<span id="_Toc859038" class="anchor"></span>Table : Manuals to be Downloaded

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release, then patch PSO\*7.0\*481 will be released from the National Patch Module. After it’s released it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing, and deployment to production will be at the site’s discretion. It is anticipated there will be a 30-day compliance period. \*\*Please note that this patch must be installed in the site’s mirror/test account to test the installation of the patch. The import functionality, however, will not work in the mirror/test accounts.

After patch PSO\*7\*481 is installed, sites will have the option to import data for non-VA providers into the NEW PERSON (#200) file. Sites that elect not to import the non-VA provider data are not required to do so.

> **NOTE:** upcoming patches to the NEW PERSON (#200) file will render this process non-functional and that the data cannot be imported later. All updates should be completed prior to the install of patch XU\*8\*688.

IT staff responsible for installing the patch and retrieving the csv file from the anonymous directory to the site’s directory will work in close coordination with the Pharmacy staff. They will be responsible for performing the import function of Non-VA providers at the respective sites. Holders of the PSDMGR key among the Pharmacy staff will get the emails for the providers that were imported successfully and unsuccessfully. These emails will help the pharmacy staff to take further action, if needed.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. This is considered a maintenance release, and installation, within the constraints of the compliance period for the release, will be at the site’s discretion.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Non-VA Provider Updates patch PSO\*7.0\*481 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-VA Provider Updates patch PSO\*7.0\*481 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, Non-VA Provider Updates patch PSO\*7.0\*481 will be deployed to all VistA systems.

The Production IOC testing sites are:

- Birmingham VAMC
- San Diego HCS

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for Non-VA Provider Updates patch PSO\*7.0\*481. A fully patched VistA system is the only requirement.

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

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an action item and National Change Order prior to the release of Non-VA Provider Updates patch PSO\*7.0\*481 advising them of the upcoming release.

Non-VA Provider Updates patch PSO\*7.0\*481 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch PSO\*7.0\*481 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-VA Provider Updates patch PSO\*7.0\*481 assumes a fully-patched VistA system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be loaded with users on the system. You may wish to install it during non-peak hours. This patch should take less than 5 minutes to install. Kernel patches must be current on the target system to avoid problems loading and/or installing this patch.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-VA Provider Updates patch PSO\*7.0\*481 is being released as a PackMan Message distributed through the National Patch Module. However, there are manual updates as well as data files containing the Non-VA Provider data for each Veterans Integrated Service Network (VISN) and State that can be downloaded.

The preferred method is to retrieve files from <span class="mark">REDACTED</span>.

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the documentation directly using Secure File Transfer Protocol (SFTP) from the <span class="mark">REDACTED</span> directory at the following

| Location                           | Site                               |
|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

<span id="_Toc859039" class="anchor"></span>Table : Non-VA Provider Data Files to be Downloaded

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl/

| File Name                                                                                     | File Contents         | Download Format |
|-----------------------------------------------------------------------------------------------|-----------------------|-----------------|
| Outpatient Pharmacy (PSO) Manager User's Manual                                               | pso_7_man_um_p481.pdf | Binary          |
| Outpatient Pharmacy (PSO) Technical Manual/Security Guide                                     | pso_7_tm_p481.pdf     | Binary          |
| Non-VA Provider Updates (PSO\*7.0\*481) Deployment, Installation, Backout and Roll-Back Guide | pso_7_ig_p481.pdf     | Binary          |

<span id="_Toc859040" class="anchor"></span>Table : HPS Clinical Sustainment Contacts

Software support personnel may retrieve the Non-VA Provider data files for their individual VISN and State(s) in Comma Separated Value (CSV) format directly using SFTP from the ANONYMOUS directory in the sub folder “PSO_481”. Sub-folders for each VISN will be contained within the folder PSO_481.

| File Name           | File Contents                                                                                              | Download Format |
|---------------------|------------------------------------------------------------------------------------------------------------|-----------------|
| PSO_481_VISN_ST.csv | VISN is the VISN number and ST is the state abbreviation for the files containing the Non-VA Provider data | Binary          |

Provides a list of the files, it’s content, and the download format that will be needed for this patch.

Retrieve the files applicable for your VISN and state and transfer them to a directory accessible from your VistA production environment. The VistA import option will not allow data to be imported from another VISN.

If your site's providers are in multiple states, then importing multiple files (one from each state) can be done. Provider information is separated out by VISN and state into Excel files. For example, a California site in VISN 21 might import a file for VISN 21/California and VISN 21/Nevada. A file for VISN 22/California cannot be imported because only files for VISN 21 may be imported.

Filename format = PSO_481_VISN_ST.csv (Example: PSO_481_21_CA.csv includes all non-VA providers for VISN 21 in California.)

After this patch is installed, the site’s IT support personnel can coordinate with pharmacy staff and invoke the Non-VA Provider Import \[NON-VA PROVIDER IMPORT\] option which is located within the Outpatient Pharmacy Manager \[PSO MANAGER\] menu under the Maintenance (Outpatient Pharmacy) \[PSO MAINTENANCE\] menu to import the Non-VA Providers contained in the Excel files for your VISN. See section 4.10 in this manual for additional information.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation and Importing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of Non-VA Provider Updates patch PSO\*7.0\*481 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Ability to File Transfer Protocol (FTP) a file to the local VistA instance.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PSO\*7.0\*481 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch will not be functionally testable in a mirror/test/non-production account. The functionality from this patch can only be exercised in a production environment. Install it into mirror/test accounts to test the VistA Patch installation prior to installing into production.

VistA installation procedure:

1.  Use the “INSTALL/CHECK MESSAGE” option of the PackMan menu. This option will load the KIDS patch onto the system.
2.  The patch has now been loaded into a Transport global on the system. Use KIDS to install the transport global.
3.  On the menu for KIDS select the “Installation” menu.
4.  Use the “Verify Checksum in Transport Global” option and verify that all routines have the correct checksums.

On the KIDS menu, under the “Installation” menu, use the following options:

1.  Print Transport Global
2.  Compare Transport Global to Current System
3.  Backup a Transport Global

The routines in this patch are new, so there is no need to back up the transport global.

5.  Use the “Install Package(s)” option under the “Installation” menu and select the package “PSO\*7.0\*481”.
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//”, choose “NO”.
7.  When prompted “Want KIDS to INHIBIT LOGONs during the install? NO//”, choose “NO”.
8.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//”, choose “NO”.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the checksum of the routines are equal to the checksum listed on the patch description.

## Importing Non-VA Providers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site’s IT support personal responsible for installation of the Vista Patch will perform this action with coordination from local pharmacy staff. Local pharmacy staff do not have sufficient system privileges to be able to import the non-VA provider data.

## SERVICE/SECTION (#29) field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pharmacy staff at each site determines whether an existing entry in the SERVICE/SECTION (#49) file should be used to populate the SERVICE/SECTION (#29) field in the NEW PERSON (#200) file for Non-VA providers which are imported. Sites may decide to define a new entry such as "NON-VA COMMUNITY CARE" into the SERVICE/SECTION (#49) file.

Sites may also decide not to populate the SERVICE/SECTION (#29) field. In that case, the following prompt is answered by pressing "enter":

Which SERVICE/SECTION (#29) field entry should be used?

At this prompt enter the Service/Section or if there is none press “enter”

### TITLE (#3.1) field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that the site pre-defines the titles "HN NON-VA PROVIDER" and "TW NON-VA PROVIDER" in the TITLE (#3.1) file before starting the import process.

The provider information will file with one of these titles.

If the titles are not defined in the TITLE (#3.1) file, the Non-VA provider titles will not display in CPRS.

### PSDMGR key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan messages are sent to the holders of the PSDMGR key containing information about:

1.  Providers which were filed successfully
2.  Providers which were not filed due to duplication of NPI's, etc.

### Non-VA Provider Import \[PSO NON-VA PROVIDER IMPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new option is added to the Outpatient Pharmacy Manager \[PSO MANAGER\] menu, Non-VA Provider Import \[PSO NON-VA PROVIDER IMPORT\].

The file import does not file non-VA provider information into the IB NON/OTHER VA BILLING PROVIDER (#355.93) file.

The expectation is that sites will perform the import once but multiple imports can be done up until XU\*8\*688 is released. Once XU\*8\*688 is released and once installed then the import option will no longer function. There may be monthly updates to the posted .csv files until XU\*8\*688 is released. Subsequent copies of spreadsheets might contain updated information for providers such as DEA Expiration Date, address, etc. The file import does not update existing entries in the NEW PERSON (#200) file.

If provider information on the spreadsheet does not include a DEA number, the AUTHORIZED TO WRITE MED ORDERS (#53.1) field of the NEW PERSON (#200) file will not be populated. Sites may perform a FileMan search for any of these entries and then define the AUTHORIZED TO WRITE MED ORDERS (#53.1) field if desired. (This scenario was discovered during field testing.)

Example of importing using the Non-VA Provider Import \[PSO NON-VA PROVIDER IMPORT\] option:

Select Outpatient Pharmacy Manager \<TEST ACCOUNT\> Option: Maintenance (Outpatient Pharmacy)

Site Parameter Enter/Edit

Edit Provider

Add New Providers

Queue Background Jobs

Autocancel Rx's on Admission

Bingo Board Manager ...

Edit Data for a Patient in the Clozapine Program

Enter/Edit Clinic Sort Groups

Initialize Rx Cost Statistics

Edit Pharmacy Intervention

Delete Intervention

Auto-delete from Suspense

Automate Internet Refill

Delete a Prescription

Enter/Edit Automated Dispensing Devices

Expire Prescriptions

Manual Auto Expire Rxs

Non-VA Provider Import

Prescription Cost Update

Purge Drug Cost Data

Recompile AMIS Data

Select Maintenance (Outpatient Pharmacy) \<TEST ACCOUNT\> Option: NON-VA Provider Import

Considerations before invoking this option:

TITLE (#3.1) file:

Have the titles "HN NON-VA PROVIDER" and "TW NON-VA PROVIDER"

been defined in the TITLE (#3.1) file in this system?

It is optional to have the titles defined.

However, the providers loaded by this patch will have no titles

listed in CPRS if these titles are not pre-defined prior to importing

the non-VA provider information included in this update.

SERVICE/SECTION (#49) file:

Determine whether an entry for the SERVICE/SECTION (#29) field

should be populated during the import.

It is optional to populate the SERVICE/SECTION (#29) field.

Your site may wish to define a new SERVICE/SECTION (#49) file entry

such as "NON-VA COMMUNITY CARE".

Do you wish to proceed? NO// YES

Your site VISN is: 1. *\<this will be whatever your VISN is\>*

Only providers for your VISN may be imported.

Directory name // *\<insert directory path\>*

File Name // *\<insert file name PSO_481_VISN_ST.csv where VISN is your VISN number and ST is your state abbreviation\>*

Press ENTER if the SERVICE/SECTION (#29) field should not be populated.

Which SERVICE/SECTION (#29) field entry should be used? \<*enter a valid entry from the SERVICE/SECTION (#49) file or press “enter” if the field should not be populated\>*

Requested Start Time: NOW// (MAY 16, 2018@16:49:21)

PSO NON-VA PROVIDER IMPORT TASKED:1238567

After completion, MailMan message(s) will be sent to holders of the PSDMGR key.

MailMan Message ExamplesFor successful import:

Subj: VACAA: Filing Success \[#2750644\] 05/16/18@16:49 7 lines

From: Non-VA Provider Updates In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

This message lists new Non-VA Providers successfully uploaded into the VistA

NEW PERSON file (#200) for VACAA.

IEN Provider

------------ -----------------------------------

1111111111 PROVIDER1,NM

1111111111 PROVIDER2,NM

For Duplicate NPI(s) in file:

Subj: VACAA: NPI(s) Listed Multiple Times in Spreadsheet \[#2750645\]

05/16/18@16:49 7 lines

From: Non-VA Provider Updates In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

This message lists Non-VA Provider data that failed to load into the VistA

NEW PERSON file (#200) because the NPI was listed in the spreadsheet multiple

times - possibly under multiple addresses.

NPI Provider Street Address

---------- -------------------- -------------------

1111111111 PROVIDER1,NM 65 MESQUITE ST

1111111111 PROVIDER1,NM 61 BARK ST

Enter message action (in IN basket): Ignore//

For No New Entries:

This MailMan message is sent if no providers were filed. It is unlikely that no new providers will be filed, but it might happen at sites which do not have very many non-VA providers. This message will let the users know that there are no new entries in case they double check new entries after the option finishes.

Subj: VACAA: Filing Success \[#2750660\] 05/16/18@17:13 8 lines

From: Non-VA Provider Updates In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

This message lists new Non-VA Providers successfully uploaded into the VistA

NEW PERSON file (#200) for VACAA.

\*\*\*\* NO NEW PROVIDERS SUCCESSFULLY UPLOADED \*\*\*\*

\*\*\*\* SEE SEPARATE MESSAGES CONCERNING FILING PROBLEMS \*\*\*\*

\*\*\*\* AND INFORMATION ON PROVIDERS WHICH ARE ALREADY ON FILE \*\*\*\*

Enter message action (in IN basket): Ignore//

For NPI already on file before patch install:

This message lists providers listed in the spreadsheet, but the NPI is already on file at the site.

Subj: VACAA: NPI(s) Already On File \[#2750661\] 05/16/18@17:13 6 lines

From: Non-VA Provider Updates In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

This message lists Non-VA Provider(s) that failed to load into the VistA

NEW PERSON file (#200) because the NPI was already on file.

NPI Provider

---------- --------------------

2222222222 PROVIDER3,NM

Enter message action (in IN basket): Ignore//

For Name already on file (with no NPI):

This message is generated if there is a name match in the NEW PERSON (#200) file but that entry does not contain an NPI. These entries need to be manually checked to see if the name matches in the NEW PERSON (#200) file are the same person. The site then decides whether to define the entries from the spreadsheet.

Subj: VACAA: Name(s) already on file in the New Person (#200) file \[#2750662\]

05/16/18@17:13 6 lines

From: Non-VA Provider Updates In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

This message lists Non-VA Provider data that failed to load into the VistA

NEW PERSON file (#200) because the name is already on file

NPI Provider Street Address

---------- -------------------- -------------------

3333333333 PROVIDER4,NM 123 SUNSET DR.

Enter message action (in IN basket): Ignore//

Example FileMan Search to view imported Non-VA Providers:

VA FileMan 22.2

Select OPTION: 3 SEARCH FILE ENTRIES

Output from what File: NEW PERSON// (1815 entries)

-A- SEARCH FOR NEW PERSON FIELD: DATE ENTERED

-A- CONDITION: EQUALS

-A- EQUALS DATE: T (JAN 17, 2019) *\<date of import\>*

-B- SEARCH FOR NEW PERSON FIELD: AUTHORIZED TO WRITE MED ORDERS

-B- CONDITION: NULL

-C- SEARCH FOR NEW PERSON FIELD: NON-VA PRESCRIBER

-C- CONDITION: EQUALS

-C- EQUALS: YES

-D- SEARCH FOR NEW PERSON FIELD:

IF: A&B&C DATE ENTERED EQUALS any time during JAN 17,2019 (1/17/2019)

and AUTHORIZED TO WRITE MED ORDERS NULL

and NON-VA PRESCRIBER EQUALS "1" (YES)

OR:

STORE RESULTS OF SEARCH IN TEMPLATE:

Sort by: NAME//

Start with NAME: FIRST//

First Print FIELD: NUMBER

Then Print FIELD: NAME

1 NAME

2 NAME COMPONENTS

CHOOSE 1-2: 1 NAME

Then Print FIELD:

Heading (S/C): NEW PERSON Search//

Example of Non-VA provider filed by this patch:

NAME: xxxx,xxxx TITLE: HN NON-VA PROVIDER

STREET ADDRESS 1: 123 STREET STREET ADDRESS 2: SUITE 100

CITY: ANYTOWN STATE: ANYSTATE

ZIP CODE: 12345 SEX: MALE

DATE ENTERED: JUL 31, 2018 CREATOR: TASKMAN,PROXY USER

NAME COMPONENTS: 200 DEGREE: MD

SERVICE/SECTION: OPTIONAL

SIGNATURE BLOCK PRINTED NAME: xxxx xxxx

KEY: XUORES GIVEN BY: TASKMAN,PROXY USER

DATE GIVEN: JUL 31, 2018

SUBJECT ORGANIZATION: Veteran Care In The Community

SUBJECT ORGANIZATION ID: n/a UNIQUE USER ID: 1111111111

NPI: 1111111111 NPI ENTRY STATUS: DONE

AUTHORIZE RELEASE OF NPI: Yes

EFFECTIVE DATE/TIME: JUL 31, 2018@17:09:08

STATUS: ACTIVE NPI: 1111111111

AUTHORIZED TO WRITE MED ORDERS: YES DEA#: AX111111111

PROVIDER CLASS: PHYSICIAN PROVIDER TYPE: FEE BASIS

REMARKS: HN NON-VA PROVIDER SCHEDULE II NARCOTIC: Yes

SCHEDULE II NON-NARCOTIC: Yes SCHEDULE III NARCOTIC: Yes

SCHEDULE III NON-NARCOTIC: Yes SCHEDULE IV: Yes

SCHEDULE V: Yes DEA EXPIRATION DATE: OCT 31, 2020

NON-VA PRESCRIBER: YES TAX ID: 11-1111111

PSIM UPDATE USER: TASKMAN,PROXY USER PSIM UPDATE DT: JUL 31, 2018@17:09

If Non-VA Providers that have been imported need to be inactivated, see section 5.61 for information on the Non-VA Provider Inactivate \[PSO NON-VA PROVIDER INACTIVATE\] option.

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

Since this patch is made up of new routines, there was no need to create a backup. Instructions for removing the routines and options coming in with this patch are below.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the two test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of PSO\*7.0\*481. The sites either passed or failed any item based on testing. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for patch PSO\*7.0\*481 is in the event of a catastrophic failure.

Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with Non-VA Provider Import PSO\*7.0\*481 patch. Use the following contacts:

| Name & Title                       | Title                              | Email                              | Telephone Number                   |
|------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Lists the individuals who should be contacted if this patch needs to be backed-out. It provides their email and phone contact information.

### Inactivate Imported Non-VA Providers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new option, Non-VA Provider Inactivate \[PSO NON-VA PROVIDER INACTIVATE\], will allow for the inactivation of providers which were previously imported by this patch if it is decided later that the providers should not remain active due to workflow or other issues. The Non-VA Provider Inactivate \[PSO NON-VA PROVIDER INACTIVATE\] option is only accessible by users with programmer level access and is not attached to a menu.

This option will populate the DISUSER (#7) field with "YES". The INACTIVE DATE (#53.4) and TERMINATION DATE (#9.2) fields will be populated with the previous day's date so that the providers will be immediately inactive. The REMARKS (#53.9) field will contain a comment that the entry was inactivated by this option.

The security key "XUPROG" is required before a user can run this option.

Example of Non-VA Provider Inactivate \[PSO NON-VA PROVIDER INACTIVATE\]:

Select OPTION NAME: PSO NON-VA PROVIDER INACTIVATE Non-VA Provider

Inactivate Non-VA Provider Inactivate

The following information displays to the user:

This option is to be used ONLY to inactivate non-VA providers

which were loaded by the Non-VA Provider Import option.

If you proceed, NEW PERSON (#200) file entries which meet

the following criteria:

NON-VA PRESCRIBER (#53.91) field = YES

REMARKS (#53.9) field contains "NON-VA PROVIDER"

DATE ENTERED (#30) field = the date specified in the "DATE ENTERED" prompt

will have:

DISUSER (#7) field set to "YES"

TERMINATION DATE (#9.2) and INACTIVE DATE (#53.4) fields populated with

yesterday's date. (Yesterday's date must be used in order to immediately

inactivate the providers.)

REMARKS (#53.9) field will have a comment added: "INACTIVATED BY NON-VA

INACTIVATE OPTION".

Do you wish to proceed? NO// YES

What DATE ENTERED for the entries which should be inactivated? T (JUL

31, 2018) *\<enter date you want entries inactivated\>*

NEW PERSON (#200) file entries for non-VA providers which were entered on

JUL 31, 2018 will be inactivated.

Do you wish to proceed? NO// YES

Starting -- Please wait ..................

Finished.

Check ^XTMP("PSONONVA_INACTIVATE \#####" for IEN's which have been

inactivated. *\<##### will be a unique number\>*

Press Return to continue:

IT staff can view the XTMP global after running this option to see a list of IENs for entries that were inactivated. No other notification is provided to the user from inactivating non-VA providers using the Non-VA Provider Inactivate \[PSO NON-VA PROVIDER INACTIVATE\] option. Using the example above, enter the following to see the list of entries inactivated by this action:

VISTA\>D ^%G

Device:

Right margin: 80 =\>

Screen size for paging (0=nopaging)? 24 =\>

For help on global specifications DO HELP^%G

Global ^XTMP("PSONONVA_INACTIVATE \#####" -- NOTE: translation in effect

^XTMP("PSONONVA_INACTIVATE \#####",0)="3190315^3190114^Non-VA Provider Update"

^XTMP("PSONONVA_INACTIVATE \#####",3190114,IEN1)=""

IEN2)=""

IEN3)=""

IEN4)=""

IEN5)=""

The information that is displayed can then be captured and forwarded to the pharmacy staff that requested the inactivation.

Example of NEW PERSON (#200) file entry which is inactivated by this option:

NAME: xxxx,xxxx DISUSER: YES

TITLE: HN NON-VA PROVIDER TERMINATION DATE: JUL 30, 2018

STREET ADDRESS 1: 1234 STREET

STREET ADDRESS 2: SUITE 100 CITY: ANYTOWN

STATE: ANYSTATE ZIP CODE: 12345

SEX: MALE DATE ENTERED: JUL 31, 2018

CREATOR: TASKMAN,PROXY USER Entry Last Edit Date: JUL 31, 2018

NAME COMPONENTS: 200 DEGREE: MD

SERVICE/SECTION: OPTIONAL

SIGNATURE BLOCK PRINTED NAME: xxxx xxxx

KEY: XUORES GIVEN BY: TASKMAN,PROXY USER

DATE GIVEN: JUL 31, 2018

SUBJECT ORGANIZATION: Veteran Care In The Community

SUBJECT ORGANIZATION ID: n/a UNIQUE USER ID: 1111111111

NPI: 1111111111 NPI ENTRY STATUS: DONE

AUTHORIZE RELEASE OF NPI: Yes

EFFECTIVE DATE/TIME: JUL 31, 2018@17:09:08

STATUS: ACTIVE NPI: 1111111111

AUTHORIZED TO WRITE MED ORDERS: YES DEA#: AX1111111

INACTIVE DATE: JUL 30, 2018 PROVIDER CLASS: PHYSICIAN

PROVIDER TYPE: FEE BASIS

REMARKS: HN NON-VA PROVIDER; INACTIVATED BY NON-VA INACTIVATE OPTION

SCHEDULE II NARCOTIC: Yes SCHEDULE II NON-NARCOTIC: Yes

SCHEDULE III NARCOTIC: Yes SCHEDULE III NON-NARCOTIC: Yes

SCHEDULE IV: Yes SCHEDULE V: Yes

DEA EXPIRATION DATE: DEC 31, 2018 NON-VA PRESCRIBER: YES

TAX ID: 11-1111111 PSIM UPDATE USER: xxxx,xxxx

### Option Deletion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Non-VA Provider Inactivate \[PSO NON-VA PROVIDER INACTIVATE\] option and the Non-VA Provider Import \[PSO NON-VA PROVIDER IMPORT\] option can be removed from the Maintenance (Outpatient Pharmacy) \[PSO MAINTENANCE\] menu through FileMan.

1.  Delete the option as an item under the Maintenance (Outpatient Pharmacy) \[PSO MAINTENANCE\] menu:

> VA FileMan 22.2

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

> Input to what File: OPTION// (13653 entries)

> EDIT WHICH FIELD: ALL// MENU

> 1 MENU (multiple)

> 2 MENU TEXT

> CHOOSE 1-2: 1 MENU (multiple)

> EDIT WHICH MENU SUB-FIELD: ALL// ITEM

> THEN EDIT MENU SUB-FIELD:

> THEN EDIT FIELD:

> Select OPTION NAME: PSO MAINTENANCE

> Select ITEM: PSO NON-VA PROVIDER IMPORT// @

> SURE YOU WANT TO DELETE THE ENTIRE ITEM? Y (Yes)

> Select ITEM: PSO AUTO DISPENSING DEVICE// ^ \<-- shift 6 to exit

3.  Delete the two options from the Option (#19) file:

> VA FileMan 22.2

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

> Input to what File: OPTION// (13653 entries)

> EDIT WHICH FIELD: ALL//

> Select OPTION NAME: Select OPTION NAME: PSO NON-VA PROVIDER

> 1 PSO NON-VA PROVIDER IMPORT Non-VA Provider Import

> 2 PSO NON-VA PROVIDER INACTIVATE Non-VA Provider

> Inactivate

> CHOOSE 1-2: 1 PSO NON-VA PROVIDER IMPORT Non-VA Provider

> Import

> NAME: PSO NON-VA PROVIDER IMPORT Replace @

> SURE YOU WANT TO DELETE THE ENTIRE 'PSO NON-VA PROVIDER IMPORT'

> OPTION? Y (Yes)

> SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

> BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

> DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A

> WHILE)? No// (No)

4.  Repeat the above for the option "PSO NON-VA PROVIDER INACTIVATE"

### Routine Deletion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines in this patch are new there are no previous versions to restore.

The routines PSONVAP2, PSONVAP3, and PSONVAP4 may be deleted using the Delete Routines option under the Programmer Options menu:

Select Routine Tools \<TEST ACCOUNT\> Option: DELETE Routines

ROUTINE DELETE

All Routines? No =\> No

Routine: PSONVAP2

Routine: PSONVAP3

Routine: PSONVAP4

Routine:

3 routines

3 routines to DELETE, OK: NO// YES

To prevent accidental deletion of a needed routine due to a typo when specifying the routine, use this option cautiously. It does not cause harm to keep the routines on the system since the options have been deleted.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Confirm Routines PSONVAP2, PSONVAP3 and PSONVAP4 have been removed from the environment.
5.  Confirm options Non-VA Provider Import \[PSO NON-VA PROVIDER IMPORT\] and Non-VA Provider Inactivate \[PSO NON-VA PROVIDER INACTIVATE\] have been removed from the Options (#19) file.

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

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A