---
title: MMRS*1*4 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: MMRS
app_name: Methicillin Resistant Staph Aurerus (MRSA)
section: CLI
app_status: active
pkg_ns: MMRS
patch_ver: 1
patch_id: MMRS*1*4
group_key: "MMRS:MMRS:1"
file_numbers: 
  - 104
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - strong
  - table
  - installation
  - contents
  - class
  - back
  - mmrs
  - rollback
  - install
  - colspan
page_count: 0
word_count: 4143
section_count: 23
table_count: 2
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: January 2017
revision_count: 1
revision_newest: 01/31/2017
revision_oldest: 01/31/2017
docx_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/vle_micro_mmrs_1_0_4__deploy_install_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/vle_micro_mmrs_1_0_4__deploy_install_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=189"
---

VistA Lab Enhancements – Microbiology

Release: MMRS\*1.0\*4

Deployment, Installation, Back-out, and Rollback Guide

![](mmrs-1-4-installation-guide/001.png)

January 2017

Document Version 1.0

Office of Information and Technology (OI&T)

Revision History

| Date       | Document Version | Description         | Author / Team Role                 |
|------------|------------------|---------------------|------------------------------------|
| 01/31/2017 | 1.0              | Document baselined. | <span class="mark">REDACTED</span> |

<span id="_Toc457391409" class="anchor"></span>Table 2: Site Preparation

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the Veterans Affairs (VA) Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

1\. Introduction [1](#introduction)

1.1 Purpose [1](#purpose)

1.2 Dependencies [1](#dependencies)

1.3 Constraints [1](#constraints)

1.4 Orientation [1](#orientation)

1.4.1 Computer Dialogue [2](#computer-dialogue)

1.4.2 Instructions [2](#instructions)

1.4.3 User Response [2](#user-response)

2\. Roles and Responsibilities [2](#roles-and-responsibilities)

3\. Deployment [3](#deployment)

3.1 Site Preparation [3](#site-preparation)

3.2 Software [4](#software)

3.3 Communications [4](#communications)

4\. Pre-Installation and Installation Preparation Instructions [4](#pre-installation-and-installation-preparation-instructions)

4.1 Installation Timing Recommendation [4](#installation-timing-recommendation)

4.1.1 Estimated Timing [5](#estimated-timing)

4.1.2 Kernel Patches [5](#kernel-patches)

4.1.3 Global Growth [5](#global-growth)

4.2 Download and Extract Files [5](#download-and-extract-files)

4.3 Access Requirements and Skills Needed for the Installation [6](#access-requirements-and-skills-needed-for-the-installation)

4.4 Pre-Installation and System Requirements [6](#pre-installation-and-system-requirements)

4.5 Installation Procedure [6](#installation-procedure)

5\. Back-Out Procedure [8](#back-out-procedure)

5.1 Back-Out Strategy [8](#back-out-strategy)

5.2 Back-Out Considerations [8](#back-out-considerations)

5.3 Back-Out Criteria [8](#back-out-criteria)

5.4 Back-Out Risks [9](#back-out-risks)

5.5 Authority for Back-Out [9](#authority-for-back-out)

6\. Rollback Procedure [9](#rollback-procedure)

6.1 Rollback Considerations [9](#rollback-considerations)

6.2 Rollback Criteria [9](#rollback-criteria)

6.3 Rollback Risks [9](#rollback-risks)

6.4 Authority for Rollback [9](#authority-for-rollback)

6.5 Rollback Procedure [9](#rollback-procedure-1)

Appendix A: Example of Captured Installation [10](#appendix-a-example-of-captured-installation)

Appendix B: Example of Installation File Printout [12](#appendix-b-example-of-installation-file-printout)

List of Figures

[Figure 1: Captured Installation [10](#_Toc473615875)](#_Toc473615875)

[Figure 2: Installation File Printout [12](#_Toc473615876)](#_Toc473615876)

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
  - [Orientation](#orientation)
    - [Computer Dialogue](#computer-dialogue)
    - [Instructions](#instructions)
    - [User Response](#user-response)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Site Preparation](#site-preparation)
  - [Software](#software)
  - [Communications](#communications)
- [Pre-Installation and Installation Preparation Instructions](#pre-installation-and-installation-preparation-instructions)
  - [Installation Timing Recommendation](#installation-timing-recommendation)
    - [Estimated Timing](#estimated-timing)
    - [Kernel Patches](#kernel-patches)
    - [Global Growth](#global-growth)
  - [Download and Extract Files](#download-and-extract-files)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Pre-Installation and System Requirements](#pre-installation-and-system-requirements)
  - [Installation Procedure](#installation-procedure)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
- [Appendix A: Example of Captured Installation](#appendix-a-example-of-captured-installation)
- [Appendix B: Example of Installation File Printout](#appendix-b-example-of-installation-file-printout)
The Installation, Back-out, Rollback Guide defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product. It provides installation instructions for the VistA Lab Enhancements (VLE) Microbiology project, release MMRS\*1.0\*4.
The MMRS\*1.0\*4 release shall support the timely identification of multi-drug resistant organisms (MDROs), provide enhanced reporting capabilities for Carbapenem Resistant Enterobacteriaceae (CRE) and Clostridium Difficile Infection (CDI) positive cases, and streamline the MDRO initiative by updating the existing MRSA Program Tools menu options and naming conventions to MDRO where applicable. The features and functionality provided in the patch will provide technicians, MDRO Prevention Coordinators (MPCs) and Infection Prevention (IP) personnel automated tools thereby increasing efficiency and decreasing the amount of labor hours required previously with manual data mining.
In regards to enhanced reporting capabilities, the MMRS\*1.0\*4 release shall provide the following new reporting capabilities:
- CDI reporting functionality to capture positive cases for the wards of a particular facility.
- CRE reporting functionality to capture positive cases within a facility.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the MMRS\*1.0\*4 build will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch MMRS\*1.0\*4 includes the following dependencies:

- MMRS\*1.0\*3
- LR\*5.2\*463

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security controls will be inherited from VistA and therefore will be fully compliant with National Institute of Standards and Technology (NIST) controls and in compliance with Directive 6500. In addition, the MMRS\*1.0\*4 release will be 508 compliant and designed to ensure no performance impacts will be experienced in the production environments.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses package or audience specific notations or directions (e.g., symbols used

to indicate terminal dialogues or user responses) for the installation and post-installation instructions included in this document.

All headings and text in this guide are intentionally formatted flush left, regardless of the heading level, to save space and to make for better readability.

In tables which list mandatory steps (as for installation and post-installation), a column is provided at the right-hand side so that users may check () off the step as it is performed.

### Computer Dialogue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The computer dialogue will appear in Courier New 11-point font.

Example: Courier New font 11 points

### Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions will appear in Arial 11-point font.

Example: Arial font 11 points

### User Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User entry responses will appear in Courier New 11-point font.

Example: Courier New font 11 points

In VistA, every response you type must be followed by pressing the \< Return \> key or the \< Enter \> key.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment, installation, back-out, and roll-back roles and responsibilities are outlined in the table below.

<span id="_Toc457391406" class="anchor"></span>Table 1: Roles and Responsibilities

| ID | Team              | Phase / Role | Tasks                                                                                                                 |
|--------|-----------------------|------------------|---------------------------------------------------------------------------------------------------------------------------|
| 1      | Field Operations (FO) | Deployment       | Plan and schedule deployment.                                                                                             |
| 2      | FO                    | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                                |
| 3      | FO                    | Deployment       | Test for operational readiness.                                                                                           |
| 4      | FO                    | Deployment       | Execute deployment.                                                                                                       |
| 5      | FO                    | Installation     | Plan and schedule installation.                                                                                           |
| 6      | FO                    | Installation     | Ensure authority to operate and that certificate authority security documentation is in place.                            |
| 7      | FO                    | Installation     | Validate through facility point of contact to ensure that IT equipment has been accepted using asset inventory processes. |
| 8      | FO                    | Installations    | Coordinate training.                                                                                                      |
| 9      | FO                    | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).      |
| 10     | FO                    | Post Deployment  | Hardware, Software and System Support.                                                                                    |

<span id="_Toc457391411" class="anchor"></span>Table 3: Software Specifications

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Microbiology (Micro) Initiative is a collaborative solution between the VistA Laboratory Enhancement (VLE) Team and Clinical Laboratory personnel. This solution provides Micro Laboratory Technologists a system that integrates with the existing VistA Microbiology system.

A National Release is planned for February 2017 after testing has been successfully completed at two Test Sites.

Deployment will be performed by Local Facility staff and supported by team members from one or more of the operations organizations: Enterprise Systems Engineering (ESE), Field Operations (FO), Enterprise Operations (EO), and/or others.

## Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each site must prepare for the deployment, installation, and implementation of the Micro capabilities. The extent for which they must prepare will vary based upon the sites current processes.

The following table describes the overall preparation required by the site prior to deployment.

<table>
<caption><p><span id="_Toc471746039" class="anchor"></span>Table 5: M Code Installation Instructions</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site/Other</strong></th>
<th><strong>Problem/Change Needed</strong></th>
<th><strong>Features to Adapt/Modify to New Product</strong></th>
<th><strong>Actions/Steps</strong></th>
<th><strong>Owner</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>Determine changes to current processes.</td>
<td>Existing Micro MDRO procedures.</td>
<td>Evaluate how new processes differ from current processes and adapt training accordingly.</td>
<td><p>Micro Technologists, Laboratory Information Managers (LIMs),</p>
<p>Facility Business Owners</p></td>
</tr>
<tr class="even">
<td>Sites using a VistA Micro currently.</td>
<td>Evaluate configuration changes that will need to be made to adapt to new Micro enhancements.</td>
<td>Existing Order Menus, Order Sets, and Quick Orders.</td>
<td>If using Generic Lab or Consult Order Types, determine if there are ordering menus, sets, and/or quick orders that need to be modified.</td>
<td><p>Micro Technologists, LIMs,</p>
<p>Facility Business Owners</p></td>
</tr>
</tbody>
</table>

<span id="_Toc471746039" class="anchor"></span>Table 5: M Code Installation Instructions

## Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment for the MMRS\*1.0\*4 release.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 17%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Software</strong></th>
<th><strong>Manufacturer</strong></th>
<th><strong>Other</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The following prerequisite release is required for the MMRS*1.0*4 patch:</p>
<ul>
<li><p>MMRS*1.0*3</p></li>
<li><p>LR*5.2*463</p></li>
</ul></td>
<td>Not applicable.</td>
<td>Local OI&amp;T staff will provide the assistance needed to ensure that the users have the latest patches and upgrades required for the build.</td>
</tr>
</tbody>
</table>

## Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Technicians will use email and conference calls for communication during the deployment; email and/or conference calls will be utilized to notify the stakeholders of the successful release of the product.

# Pre-Installation and Installation Preparation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides pre-installation and installation preparation instructions for the MMRS\*1.0\*4 build.

## Installation Timing Recommendation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MMRS\*1.0\*4 patch may be loaded with users on the system; however, it is highly recommended that the patch is installed during non-peak hours to minimize any potential disruption to the users.

### Estimated Timing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation will take less than 5 minutes.

### Kernel Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patches must be current on the target system to avoid problems loading and/or installing this patch.

### Global Growth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no significant change to global growth.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch will be released as a Mailman message to VA Medical Centers (VAMCs) via FORUM.

Sites may retrieve the documentation directly via Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the OI&T Field Offices listed below.

<span class="mark">REDACTED</span>

Documentation will also be distributed via a VLE MMRS MDRO Enhancement.ZIP

file, which contains both .pdf and .docx formatted files.

The latest documentation can also be found on the VA Software Documentation Library

at: <http://www.va.gov/vdl/>

<span id="_Toc471746038" class="anchor"></span>Table 4: Files for Retrieval

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 64%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Contents</strong></th>
<th><strong>Retrieval Format</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MMRS*1.0*4</td>
<td>Mailman message with code attached (PackMan).</td>
<td>Mailman message will be sent to VAMC’s via FORUM distribution. </td>
</tr>
<tr class="even">
<td>VLE MMRS MDRO Enhancement.ZIP</td>
<td><p>VLE Micro_MMRS_1_0_4__Deployment_Installation_Roll Back_Back Out_Guide</p>
<p>VLE Micro_MMRS_1_0_4_Technical_Manual</p>
<p>VLE Micro_MMRS_1_0_4_User_Guide</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is written with the assumption that the reader is experienced or familiar with the following:

- VistA computing environment
- VA FileMan data structures and terminology
- Microsoft Windows

Local or Regional OI&T staff will coordinate the patch installation with the LIM at each site. The Local or Regional OI&T staff have the necessary access and skill set to conduct the installation.

## Pre-Installation and System Requirements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MMRS\*1.0\*4 patch installation must be coordinated with the ADPAC to ensure that all Lab Interface related activities are halted.

## Installation Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the instructions outlined in the table below to install the software.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 66%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step #</strong></th>
<th colspan="2"><strong>Description</strong></th>
<th><strong></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td colspan="2">Select the PackMan message containing the MMRS*1.0*4 patch.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td colspan="2">Select the INSTALL/CHECK MESSAGE PackMan option.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td colspan="2">Access the KIDS menu (XPD MAIN).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td colspan="2">From the KIDS menu, select the Installation menu.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td colspan="2">From the Installation menu, select option #1: Load a Distribution.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td colspan="2">When prompted, ‘INSTALL NAME’, respond ‘MMRS*1.0*4’</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>7</strong></td>
<td colspan="2">When prompted, ‘Want to Continue with Load? YES//’, respond "Yes".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>8</strong></td>
<td colspan="2">From the Installation menu, select option #2, Verify Checksums in Transport Global.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘MMRS*1.0*4’</td>
<td></td>
</tr>
<tr class="even">
<td><strong>10</strong></td>
<td colspan="2">When prompted ‘Want each Routine Listed with Checksums: Yes//’ respond “Yes”</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>a</strong></td>
<td><p>Verify the following routine information:</p>
<p>MMRSCDI Calculated 219284495</p>
<p>MMRSCDI1 Calculated 47343212</p>
<p>MMRSCDI2 Calculated 162714137</p>
<p>MMRSCRE Calculated 90369826</p>
<p>MMRSCRE2 Calculated 12793206</p>
<p>MMRSCRE3 Calculated 160454267</p>
<p>MMRSCRE4 Calculated 34859922</p>
<p>MMRSIPCP Calculated 45727414</p>
<p>MMRSP4 Calculated 634304</p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>11</strong></td>
<td colspan="2">From the Installation menu, select option #3, Print Transport Global</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>12</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘MMRS*1.0*4’</td>
<td></td>
</tr>
<tr class="even">
<td><strong>13</strong></td>
<td colspan="2">When prompted ‘Select one of the following:” respond “1” for Print Summary.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>14</strong></td>
<td colspan="2">When prompted ‘Want each Routine Listed with Checksums: Yes//’ respond “Yes”</td>
<td></td>
</tr>
<tr class="even">
<td><strong>15</strong></td>
<td colspan="2">From the Installation menu, select option #4, Compare Transport Global to Current System.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>16</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘MMRS*1.0*4’</td>
<td></td>
</tr>
<tr class="even">
<td><strong>17</strong></td>
<td colspan="2">When prompted ‘Select one of the following:” respond “2” for Second line of Routines only.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>18</strong></td>
<td colspan="2">From the Installation menu, select option #5: Backup a Global Transport.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>19</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘MMRS*1.0*4’</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>20</strong></td>
<td colspan="2">From the Installation menu, select option #6: Install Package(s).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>21</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘MMRS*1.0*4’</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>22</strong></td>
<td colspan="2">When prompted 'Want KIDS to INHIBIT LOGONs during the install?  NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>23</strong></td>
<td colspan="2">When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>24</strong></td>
<td colspan="2">When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>25</strong></td>
<td colspan="2">When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>26</strong></td>
<td colspan="2"><p>If prompted 'Delay Install (Minutes): (0 - 60): 0//', respond "NO".</p>
<p><strong>Note:</strong> See Appendix A for an example of the installation.</p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>27</strong></td>
<td colspan="2"><p>After receiving the message “Install Completed’, print out the installation for the patch.</p>
<p><strong>Note:</strong> See Appendix B for an example of the installation file printout.</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>28</strong></td>
<td colspan="2">From the KIDS menu, select the Utilities menu.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>29</strong></td>
<td colspan="2">From the Utilities menu, select Install File Print<strong>.</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>30</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘MMRS*1.0*4’</td>
<td></td>
</tr>
<tr class="even">
<td><strong>31</strong></td>
<td colspan="2">Save all printouts.</td>
<td></td>
</tr>
</tbody>
</table>

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The build does not make any changes that would affect the operational state of the software and platform settings. The functionality in the MMRS\*1.0\*4 build will not be available until the installation process has been successfully completed.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, if the option to back up routines was run as directed, ‘Backup a Transport Global’, then routines have the ability to be restored from the “backup” MailMan message that was generated. However, the KIDS installation process does not perform a restore of other VistA components, such as data dictionary, cross-reference, and template changes, etc.

<span class="mark">REDACTED</span>

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM and the Chief of Pathology have the authority to order the back-out.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Criteria for a back-out includes, but are not limited, to the following:

1.  Failed baseline testing.
2.  Non-recoverable software error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No back-out risks have been determined at this time.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM, the Lab Manager, and the Chief of Pathology have the authority to request and approve the back-out and accept the risks.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MMRS\*1.0\*4 build as well as any installed dependent patch changes that follow these releases need to be taken out in reverse of the order in which they were installed; routines and data dictionary modifications and populated data must also be rolled back in reverse order.

<span class="mark">REDACTED</span>

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback considerations have been determined at this time.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only criteria for a rollback that has been determined at this time is that the installation failed baseline testing.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only risk determined at this time is the possibility of downtime which would only effect the users of the Laboratory package.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM, the Lab Manager, and the Chief of Pathology have the authority to require the rollback and accept the risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a rollback is highly unlikely, however if it is required, please contact the Product Support team for assistance. The rollback procedure will require Lab downtime and a reinstall of any previous KIDS versions.

# Appendix A: Example of Captured Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of a captured installation.

<span id="_Toc473615875" class="anchor"></span>Figure 1: Captured Installation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select INSTALL NAME: MMRS*1.0*4 12/28/16@11:58:16</p>
<p>=&gt; MMRS*1*4</p>
<p>This Distribution was loaded on Dec 28, 2016@11:58:16 with header of</p>
<p>MMRS*1*4</p>
<p>It consisted of the following Install(s):</p>
<p>MMRS*1.0*4</p>
<p>Checking Install for Package MMRS*1.0*4</p>
<p>Install Questions for MMRS*1.0*4</p>
<p>Incoming Files:</p>
<p>104 MDRO SITE PARAMETERS (including data)</p>
<p>*BUT YOU ALREADY HAVE 'MRSA SITE PARAMETERS' AS FILE #104!</p>
<p>Shall I write over your MRSA SITE PARAMETERS File? YES//</p>
<p>104.1 MDRO TOOLS LAB SEARCH/EXTRACT</p>
<p>*BUT YOU ALREADY HAVE 'MRSA TOOLS LAB SEARCH/EXTRACT' AS FILE #104.1!</p>
<p>Shall I write over your MRSA TOOLS LAB SEARCH/EXTRACT File? YES//</p>
<p>104.3 MDRO WARD MAPPINGS</p>
<p>*BUT YOU ALREADY HAVE 'MRSA WARD MAPPINGS' AS FILE #104.3!</p>
<p>Shall I write over your MRSA WARD MAPPINGS File? YES//</p>
<p>Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO</p>
<p>Want KIDS to INHIBIT LOGONs during the install? NO// NO</p>
<p>Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//</p>
<p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt.</p>
<p>Enter a '^' to abort the install.</p>
<p>DEVICE: HOME//</p>
<p>MMRS*1.0*4</p>
<p>────────────────────────────────────────────────────────────────────────────────</p>
<p>Installing FORM</p>
<p>Installing OPTION</p>
<p>Dec 29, 2016@10:23:59</p>
<p>Running Post-Install Routine: EN^MMRSP4</p>
<p>Updating Routine file...</p>
<p>Updating KIDS files...</p>
<p>MMRS*1.0*4 Installed.</p>
<p>Dec 29, 2016@10:23:59</p>
<p>Not a production UCI</p>
<p>NO Install Message sent</p>
<p>────────────────────────────────────────────────────────────────────────────────</p>
<p>┌────────────────────────────────────────────────────────────┐</p>
<p>100% │ 25 50 75 │</p>
<p>Complete └────────────────────────────────────────────────────────────┘</p>
<p>Install Completed</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Appendix B: Example of Installation File Printout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of an installation file printout; the printout should be saved for future reference.

<span id="_Toc473615876" class="anchor"></span>Figure 2: Installation File Printout

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PACKAGE: MMRS*1.0*4     Jan 17, 2017 2:49 pm                          PAGE 1</p>
<p>                                             COMPLETED           ELAPSED</p>
<p>-------------------------------------------------------------------------------</p>
<p>STATUS: Install Completed                 DATE LOADED: JAN 17, 2017@14:48:07</p>
<p>INSTALLED BY: LASTNAME,FIRSTNAME</p>
<p>NATIONAL PACKAGE: MDRO INITIATIVE REPORTS</p>
<p>INSTALL STARTED: JAN 17, 2017@14:48:41       14:48:43             0:00:02</p>
<p>ROUTINES:                                    14:48:41           </p>
<p>FILES:</p>
<p>MDRO SITE PARAMETERS                         14:48:41           </p>
<p>MDRO TOOLS LAB SEARCH/EXTRACT                14:48:41           </p>
<p>MDRO TYPES                                   14:48:41           </p>
<p>MDRO WARD MAPPINGS                           14:48:41           </p>
<p>SECURITY KEY                                 14:48:41           </p>
<p>FORM                                         14:48:41           </p>
<p>OPTION                                       14:48:43             0:00:02</p>
<p>POST-INIT CHECK POINTS:</p>
<p>XPD POSTINSTALL STARTED                      14:48:43           </p>
<p>XPD POSTINSTALL COMPLETED                    14:48:43           </p>
<p>INSTALL QUESTION PROMPT                                               ANSWER</p>
<p>XPF104#1   Shall I write over your MRSA SITE PARAMETERS File          YES</p>
<p>XPF104.1#1   Shall I write over your MRSA TOOLS LAB SEARCH/EXTRACT File YES</p>
<p>XPF104.3#1   Shall I write over your MRSA WARD MAPPINGS File          YES</p>
<p>XPO1   Want KIDS to Rebuild Menu Trees Upon Completion of Install     NO</p>
<p>XPI1   Want KIDS to INHIBIT LOGONs during the install                 NO</p>
<p>XPZ1   Want to DISABLE Scheduled Options, Menu Options, and Protocols NO</p>
<p>MESSAGES:</p>
<p> Install Started for MMRS*1.0*4:</p>
<p>               Jan 17, 2017@14:48:41</p>
<p>Build Distribution Date: Dec 20, 2016</p>
<p> Installing Routines:</p>
<p>               Jan 17, 2017@14:48:41</p>
<p> Installing Data Dictionaries:</p>
<p>               Jan 17, 2017@14:48:41</p>
<p> Installing Data:</p>
<p>               Jan 17, 2017@14:48:41</p>
<p> Installing PACKAGE COMPONENTS:</p>
<p> </p>
<p> Installing SECURITY KEY</p>
<p> Installing FORM</p>
<p> Installing OPTION</p>
<p>               Jan 17, 2017@14:48:43</p>
<p> Running Post-Install Routine: EN^MMRSP4</p>
<p> Updating Routine file...</p>
<p> Updating KIDS files...</p>
<p> MMRS*1.0*4 Installed.</p>
<p>               Jan 17, 2017@14:48:43</p>
<p> Install Message sent #34533037</p>
<p>* End of installation process *</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>