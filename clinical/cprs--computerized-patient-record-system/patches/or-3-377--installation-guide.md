---
title: OR*3*377 Deployment, Installation, Back Out and Rollback Guide CPRS GUI 31B
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: CPRS GUI 31B
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*377
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 1
description: The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications,
audience: 
keywords: 
  - table
  - cprs
  - installation
  - contents
  - install
  - patch
  - class
  - patches
  - back
  - host
page_count: 0
word_count: 8069
section_count: 26
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_377_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_377_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System Version 31b
---

Deployment, Installation, Back Out and Rollback Guide

CPRS Version 31b Patches

![](or-3-377-deployment-installation-back-out-and-rollback-guide-cprs-gui-31b/001.png)

August 2020

Office of Information & Technology (OI&T)

Enterprise Program Management Office (EPMO)

This page left intentionally blank.

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 56%" />
<col style="width: 17%" />
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
<td>7/14</td>
<td>1.3</td>
<td><p>Added information about patch TIU*1*335:</p>
<ul>
<li><p>Section 7.2.10: Added a section to install PXRM*2*74 after CPRS v31b installation in test.</p></li>
<li><p>Section 12.3.10: Added a section to install PXRM*2*74 after CPRS v31b installation in production.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/14</td>
<td>1.2</td>
<td><p>Added information about patch TIU*1*335:</p>
<ul>
<li><p>Section 4: updated the Test System Checklist to include downloading and installation of TIU*1*335</p></li>
<li><p>Section 5: Added to Software Retrieval list</p></li>
<li><p>Section 7.1: added to Sequence</p></li>
<li><p>Section 7.2.4 was added</p></li>
<li><p>Section 7.2.8: TIU*1*335 installation instructions (for test system)</p></li>
<li><p>Section 10: Added TIU*1*335 to Production System Installation checklist</p></li>
<li><p>Section 2: Added patch to sequence</p></li>
<li><p>Section 2.3.4: Added patch here</p></li>
<li><p>Section 12.3.8: TIU*1*335 installation instructions (for production)</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/20</td>
<td>1.1</td>
<td><p>Section 5: The list of document names was corrected.</p>
<p>Section 7.2.6: For Test account - Added an item about a checksum and a step about rebuilding the Health Summary Ad Hoc report. And an updated Installation section for the PXRM*2.0*45 patch description.</p>
<p>Section 12.3.6: For Production account - Added an item about a checksum and a step about rebuilding the Health Summary Ad Hoc report. And an updated Installation section for the PXRM*2.0*45 patch description.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# # Computerized Patient Record System Graphical User Interface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Computerized Patient Record System Graphical User Interface](#computerized-patient-record-system-graphical-user-interface)
  - [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [Document Conventions](#document-conventions)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
  - [Pre-requisite Patches](#pre-requisite-patches)
  - [Pre-Installation Steps](#pre-installation-steps)
    - [CPRS v31b Preinstallation Check List](#cprs-v31b-preinstallation-check-list)
- [Reporting Issues](#reporting-issues)
- [Test - CPRS v31b Test System Installation Checklist](#test-cprs-v31b-test-system-installation-checklist)
- [Software Retrieval](#software-retrieval)
  - [NOTE: PSO\7\477 contained a list of updated documents included in the release. However, the file names were incorrect. The corrected file names are included in this patch description.](#note-pso7477-contained-a-list-of-updated-documents-included-in-the-release-however-the-file-names-were-incorrect-the-corrected-file-names-are-included-in-this-patch-description)
- [Pre-Installation Steps](#pre-installation-steps-1)
  - [Backup Procedures](#backup-procedures)
    - [Back Up Globals](#back-up-globals)
    - [OR MOB DLL VERSION](#or-mob-dll-version)
- [Installation](#installation)
  - [Sequence](#sequence)
  - [CPRS v31b M patches](#cprs-v31b-m-patches)
    - [XU\8\653](#xu8653)
    - [XT\7.3\142](#xt73142)
    - [CPRS v31b Required Patches](#cprs-v31b-required-patches)
    - [TIU\1\335](#tiu1335)
    - [XU\8\653 – Host file (XU8653.KID)](#xu8653-host-file-xu8653kid)
    - [XT\7.3\142 – Host File (XT73142.KID)](#xt73142-host-file-xt73142kid)
    - [CPRS GUI v31b – Host file (CPRS31BREQUIRED.KID)](#cprs-gui-v31b-host-file-cprs31brequiredkid)
    - [TIU\1\335 – Host file (TIU1335.KID)](#tiu1335-host-file-tiu1335kid)
    - [OR\3\531/PXRM\2\46 (CPRSCOVID20.KID)](#or3531pxrm246-cprscovid20kid)
    - [PXRM\2\74](#pxrm274)
  - [CPRS GUI Executable (OR30377.ZIP)](#cprs-gui-executable-or30377zip)
    - [Methods of installation](#methods-of-installation)
    - [Manual Installation](#manual-installation)
- [TEST - Post-Installation Tasks](#test-post-installation-tasks)
- [TEST – Testing in Test Account](#test-testing-in-test-account)
- [CPRS v31b Production System Installation Checklist](#cprs-v31b-production-system-installation-checklist)
- [Production Pre-Installation Steps](#production-pre-installation-steps)
  - [Backup Procedures](#backup-procedures-1)
    - [Back Up Globals](#back-up-globals-1)
    - [OR MOB DLL VERSION](#or-mob-dll-version-1)
- [Production Installation](#production-installation)
  - [Disable Ordering during Installation](#disable-ordering-during-installation)
  - [Sequence](#sequence-1)
  - [CPRS v31b M patches](#cprs-v31b-m-patches-1)
    - [XU\8\653](#xu8653-1)
    - [XT\7.3\142](#xt73142-1)
    - [CPRS v31b Required Patches](#cprs-v31b-required-patches-1)
    - [TIU\1\335](#tiu1335-1)
    - [XU\8\653 – Host file (XU8653.KID)](#xu8653-host-file-xu8653kid-1)
    - [XT\7.3\142 – Host File (XT73142.KID)](#xt73142-host-file-xt73142kid-1)
    - [CPRS GUI v31b – Host file (CPRS31BREQUIRED.KID)](#cprs-gui-v31b-host-file-cprs31brequiredkid-1)
    - [TIU\1\335 – Host file (TIU1335.KID)](#tiu1335-host-file-tiu1335kid-1)
    - [OR\3\531/PXRM\2\46 (CPRSCOVID20.KID)](#or3531pxrm246-cprscovid20kid-1)
    - [PXRM\2\74](#pxrm274-1)
  - [CPRS GUI Executable (OR30377.ZIP)](#cprs-gui-executable-or30377zip-1)
    - [Methods of installation](#methods-of-installation-1)
    - [Manual Installation](#manual-installation-1)
  - [Enabling Ordering for All Users](#enabling-ordering-for-all-users)
  - [CPRS Documentation](#cprs-documentation)
- [Post-Installation Tasks](#post-installation-tasks)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Resource Management (IRM) staff.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation guide provides instructions for:

- Installing application components that run on M servers at VAMC facilities
- Installing Windows executable programs on workstations or application servers at VAMC facilities
- Performing post-installation tasks—including configuration tasks—that require knowledge of the underlying VistA system

This guide has a section for installing into a site’s test system and then later for installing into a production account. The steps are basically the same, with a few minor exceptions.

- In test, users do not need to be prevented from ordering, but that is a site choice.
- Software need only be downloaded once.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of VistA “Roll and Scroll” interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

> Note: This is an important point and must not be omitted.

Call-outs may be used to draw attention to part of a block of text or a table without disrupting the flow of the block or table. For example:

Sample text, Sample text, Sample text, Sample text

Sample text, Sample text, Sample text, Sample text

Sample text, Sample text, SOMETHING OF NOTE!!

Sample text, Sample text, Sample text,

Sample text, Sample text, Sample text, Sample text, Sample text

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents, in addition to this document, will be available on the VA Software Document Library (VDL) when the patch is released:

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

- *CPRS User Guide: GUI Version*
- *CPRS Technical Manual*
- *CPRS Technical Manual: GUI Version*
- *CPRS v31b Release Notes*
- *CPRS v31b Deployment, Installation, Back Out and Roll Back Guide*
- *CPRS v31b Set Up and Configuration Guide*

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the processes described in this document the tasks outlined in this section must be completed.

## Pre-requisite Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31b expects a fully patched VistA system.

In addition, please check your system for the following:

- Clinical Reminders Update 16 Mammogram Screening Update. [The Install Guide for this update is located on the VA Document Library (VDL).](https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/update_2_0_16_ig.pdf)

  Note: A Clinical Application Coordinator (CAC) should verify that this is installed on the site’s system.
- Clinical Reminders Update 54 Teratogenic Medications Update 4. [The Install Guide for this update is located on the VDL.](https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/update_2_0_54_ig.pdf)

  Note: A Clinical Application Coordinator (CAC) should verify that this is installed on the site’s system.

## Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps need to be taken prior to installing the CPRS v31b items.

### CPRS v31b Preinstallation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This check list will help sites prepare for installation of CPRS v31b. Tasks on the list include communication items, coordination with groups that must take place, and other tasks that must be accomplished for a successful installation.

| CPRS V31B READINESS CHECKLIST                                                                                                                     |                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| TASK                                                                                                                                              | RESPONSIBLE POC                                                                                                                                     | COMMENTS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |
|                                                                                                                                                       |                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
| Confirm that Facility Leadership is aware of CPRS v31b implementation date.                                                                           | Primary Point of Contact (POC), Health Informatics Specialist/Clinical Applications Coordinators (HIS/CAC), Office of Information and Technology (OI&T) | See the *Release v31b Wave Schedule* and *Release v31b Wave Schedule with Sites* on the [CPRS v31b Training Page](https://dvagov.sharepoint.com/sites/OITEPMOHealth/HMPE_PMO_Support_Site/CPRS_Program/CPRS_Training/default.aspx?RootFolder=%2Fsites%2FOITEPMOHealth%2FHMPE%5FPMO%5FSupport%5FSite%2FCPRS%5FProgram%2FCPRS%5FTraining%2FShared%20Documents%2FCPRS%20V31b%20Training&FolderCTID=0x012000DF8A9E562F695F4EACB65F1825C3EFE5&View=%7B0E76B1BB%2D7D11%2D4594%2DA1B0%2DB5F564DED47B%7D) |     |
| Review the *CPRS v31b DIBOR*.                                                                                                                         | OI&T                                                                                                                                                    | Located on the [CPRS v31b Training Page](https://dvagov.sharepoint.com/sites/OITEPMOHealth/HMPE_PMO_Support_Site/CPRS_Program/CPRS_Training/default.aspx?RootFolder=%2Fsites%2FOITEPMOHealth%2FHMPE%5FPMO%5FSupport%5FSite%2FCPRS%5FProgram%2FCPRS%5FTraining%2FShared%20Documents%2FCPRS%20V31b%20Training&FolderCTID=0x012000DF8A9E562F695F4EACB65F1825C3EFE5&View=%7B0E76B1BB%2D7D11%2D4594%2DA1B0%2DB5F564DED47B%7D)                                                                          |     |
| Review the *CPRS v31b Release Notes*                                                                                                                  | HIS/CAC                                                                                                                                                 | Located on the [CPRS v31b Training Page](https://dvagov.sharepoint.com/sites/OITEPMOHealth/HMPE_PMO_Support_Site/CPRS_Program/CPRS_Training/default.aspx?RootFolder=%2Fsites%2FOITEPMOHealth%2FHMPE%5FPMO%5FSupport%5FSite%2FCPRS%5FProgram%2FCPRS%5FTraining%2FShared%20Documents%2FCPRS%20V31b%20Training&FolderCTID=0x012000DF8A9E562F695F4EACB65F1825C3EFE5&View=%7B0E76B1BB%2D7D11%2D4594%2DA1B0%2DB5F564DED47B%7D)                                                                          |     |
| Review the *CPRS v31b Setup and Configuration Guide*                                                                                                  | HIS/CAC and OI&T                                                                                                                                        | Located on the [CPRS v31b Training Page](https://dvagov.sharepoint.com/sites/OITEPMOHealth/HMPE_PMO_Support_Site/CPRS_Program/CPRS_Training/default.aspx?RootFolder=%2Fsites%2FOITEPMOHealth%2FHMPE%5FPMO%5FSupport%5FSite%2FCPRS%5FProgram%2FCPRS%5FTraining%2FShared%20Documents%2FCPRS%20V31b%20Training&FolderCTID=0x012000DF8A9E562F695F4EACB65F1825C3EFE5&View=%7B0E76B1BB%2D7D11%2D4594%2DA1B0%2DB5F564DED47B%7D)                                                                          |     |
| Review the Wave Kickoff Document                                                                                                                      | HIS/CAC, OI&T, Primary POC, HIM, other stakeholders                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
| Confirm CPRS v31a COVID-19 Identifier was installed                                                                                                   | HIS/CAC, OI&T                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
| Confirm the necessary HIS/CAC, POC and OI&T staff are available during the assigned Wave dates at your site (i.e. Wave kick off call)                 | OI&T, HIS/CAC, other Subject Matter Expert (SME), Health Information Management (HIM), Lab Information Manager, etc.                                    | See the *Release v31b Wave Schedule* and *Release v31b Wave Schedule with Sites* on the [CPRS v31b Training Page](https://dvagov.sharepoint.com/sites/OITEPMOHealth/HMPE_PMO_Support_Site/CPRS_Program/CPRS_Training/default.aspx?RootFolder=%2Fsites%2FOITEPMOHealth%2FHMPE%5FPMO%5FSupport%5FSite%2FCPRS%5FProgram%2FCPRS%5FTraining%2FShared%20Documents%2FCPRS%20V31b%20Training&FolderCTID=0x012000DF8A9E562F695F4EACB65F1825C3EFE5&View=%7B0E76B1BB%2D7D11%2D4594%2DA1B0%2DB5F564DED47B%7D) |     |
| Confirm that the necessary change order requests, to have the CPRS v31b patches installed, have been submitted to OI&T (Region, VISN and/or facility) | HIS/CAC, OI&T                                                                                                                                           | in some Regions the OI&T staff have up to 2 weeks to perform the task.                                                                                                                                                                                                                                                                                                                                                                                                                            |     |
| Necessary personnel attend the Wave kick-off call/training for CPRS v31b                                                                              | OI&T, HIS/CAC, other SME (HIM, Lab manager, etc.)                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
| Confirm that local support personnel are prepared and staffed during and after installation into Live account                                         | Primary POC, HIS/CAC, OI&T                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
| Inform all clinical staff of the CPRS v31b production installation date (emails, staff meetings)                                                      | Primary POC, HIS/CAC, OI&T                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
| Confirm that training for clinical staff has taken place.                                                                                             | providers, nursing, Health Information Management (HIM), HIS/CAC                                                                                        | Create/modify training tools, reserve training rooms, send announcement to staff for training, enlist "super users" assistance.                                                                                                                                                                                                                                                                                                                                                                   |     |
| Confirm that OI&T staff have the necessary access to install patches.                                                                                 | OI&T                                                                                                                                                    | Access to servers, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |     |
| Confirm that the patches have been downloaded                                                                                                         | OI&T                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |
| Coordinate with necessary personnel for Citrix updates.                                                                                               | Local site, ITOPS                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |     |

# Reporting Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To report issues with CPRS v31b, please enter a ticket with the National Help Desk.

# Test - CPRS v31b Test System Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

Table 1 Installation Checklist

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 82%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th>Item</th>
<th>Done</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3">Test/Mirror System Installation</td>
</tr>
<tr class="even">
<td><ol type="1">
<li></li>
</ol></td>
<td>Confirm your system is fully patched (see Section 2.1, Pre-requisite Patches, above)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td>Complete sections 2.2 through 2.2.5</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Download and install the XU*8*653 patch (XU_80_653.KID)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Download and install the XT*7.3*142 patch (XT_73_142.KID)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Download and install the CPRS v31b bundle of patches (CPRSV31B_REQUIRED.KID)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Download and install the TIU*1*335 patch (TIU_1_335.KID)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Test/Mirror system has been successful</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="8" type="1">
<li></li>
</ol></td>
<td>Complete Post-Installation tasks</td>
<td></td>
</tr>
</tbody>
</table>

# Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches may be sent as mailman messages or host files. The table below will show in what form the patch will be distributed. The necessary files are:

Table 1 CPRS v31b files

| CPRS Version files to be downloaded | File Contents / Supported Functionality                 |
|-------------------------------------|---------------------------------------------------------|
| XU_8_653.KID                        | Patch XU\*8\*653                                        |
| XT_73_142.KID                       | Patch XT\*7.3\*142                                      |
| CPRSV31B_REQUIRED.KID               | Contains the required patches for the CPRS v31b release |
| TIU_1_335.KID                       | Patch TIU\*1\*335                                       |

> **NOTE:** The login details to access the software will be sent to the site installers in Outlook via an encrypted email message.

## NOTE: PSO\*7\*477 contained a list of updated documents included in the release. However, the file names were incorrect. The corrected file names are included in this patch description.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Corrected file names:

Title File Name Transfer Mode

-------------------------------------------------------------------------------------------------

Outpatient Pharmacy - PSO_7_MAN_UM.DOCX Binary

  Manager's User Manual PSO_7_MAN_UM.PDF Binary

Outpatient Pharmacy - PSO_7_PHAR_UM.DOCX Binary

  Pharmacist's User Manual         PSO_7_PHAR_UM.PDF Binary

Outpatient Pharmacy - PSO_7_SUP_UM.DOC Binary

  Supplemental User Manual PSO_7_SUP_UM.PDF Binary

Outpatient Pharmacy - PSO_7_TECH_UM.DOCX Binary

  Technician's User Manual PSO_7_TECH_UM.PDF Binary

> **NOTE:** OR\*3\*377 contained a list of updated documents as well as source files distributed. Three of those names were changed and the patch description wasn’t updated.

The corrected names are below:

File Name Contents

OR_3_0_377_RN.PDF CPRS GUI v.31 (Patch OR\*3.0\*377) Release Notes

CPRSV31B_REQUIRED.KID CPRS v31B multi-package build

CPRS_31_Help.ZIP This file is not distributed in an individual ZIP file.

The HELP folder is now contained in OR_30_377.ZIP.

# Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before this installation proceeds several steps need to be accomplished. Many of these steps need be done by Clinical Application Coordinators (CAC), Information Technology Operations and Support (ITOPS), and other groups. Once those set up items are completed, installation can proceed.

Instructions for these items are detailed in the *CPRS Set Up and Configuration Guide*.

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps are taken in case the patch needs to be backed out.

### Back Up Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backup each global below:

> **NOTE:** Make sure to backup each global to its own file.

- ^PXD(801.1,
- ^PXD(801,
- ^PXRMD(801.41,
- ^PXD(811.9,
- ^PXRMD(811.5,
- ^PXRMD(811.4,
- ^PXD(811.2,
- ^PXRMD(801.42,
- ^PXRM(810.4,
- ^ORD(101.41,
- ^TIU(8925.1,
- ^WV(790,
- ^WV(790.05,

### OR MOB DLL VERSION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the OR MOB DLL VERSION parameter, find the value of PKG portion of the parameter and make a note of that value by following the steps below:

Select General Parameter Tools \<TEST ACCOUNT\> Option: LV  List Values for a Selected Parameter

Select PARAMETER DEFINITION NAME: OR MOB DLL

     1   OR MOB DLL NAME     CPRS Med Order Button DLL file name

     2   OR MOB DLL VERSION     CPRS Med Order Button DLL version check

CHOOSE 1-2: 2  OR MOB DLL VERSION   CPRS Med Order Button DLL version check

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section gives instructions for installing CPRS v31b. Sites should disable ordering, install the patches, distribute the GUI, re-enable ordering for testers, re-enable ordering for all users.

## Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For CPRS to function correctly, it is necessary that some patches be installed immediately prior to the installation of CPRS Patches. These will be distributed with the CPRS Patches (see

Software Retrieval, above), and they should be installed in the order listed below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>XU*8*653</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol start="2" type="1">
<li><p>XT*7.3*142</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li><p>CPRS V31B REQUIRED PATCHES 1.0</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li><p>TIU*1*335</p></li>
</ol></td>
</tr>
</tbody>
</table>

## CPRS v31b M patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are the actual patches released by this effort.

### XU\*8\*653

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XU\*8\*653 is distributed in a host file separate from the CPRS v31b required bundle. This patch must be installed along with the CPRS v31b required bundle.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>XU*8*653</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### XT\*7.3\*142

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XT\*7.3\*142 is distributed in a host file separate from the CPRS v31b required bundle. This patch must be installed along with the CPRS v31b required bundle.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>XT*7.3*142</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### CPRS v31b Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list of patches are part of the CPRS V31b Required bundle. There is no need to install them individually.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>TIU*1*290</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol start="2" type="1">
<li><p>WV*1*24</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li><p>GMTS*2.7*67</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li><p>DG*5.3*932</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li><p>PXRM*2*45</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li><p>GMRA*4*53</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li><p>GMRC*3.0*88</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="8" type="1">
<li><p>PSO*7*477</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="9" type="1">
<li><p>OR*3*377</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="10" type="1">
<li><p>OR*3.0*531/PXRM*2*46</p></li>
</ol></td>
</tr>
</tbody>
</table>

### TIU\*1\*335

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch TIU\*1\*335 is distributed in a host file separate from the CPRS v31b required bundle. This patch must be installed along with the CPRS v31b required bundle.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>TIU*1*335</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### XU\*8\*653 – Host file (XU_8_653.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*NOTE – do not queue the install.

Users must not be on the system during the installation. This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 10 minutes.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU
    1.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    2.  Note that after loading the distribution you are directed to use the name “XU\*8.0\*653” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu
3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the patch by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt you will need to use the name “XU\*8.0\*653” as noted in 1.b above
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

### XT\*7.3\*142 – Host File (XT_73_142.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*NOTE – do not queue the install.

Users must not be on the system during the installation. This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 10 minutes.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU
    1.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    2.  Note that after loading the distribution you are directed to use the name “XT\*7.3\*142” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu
3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the patch by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt you will need to use the name “XT\*7.3\*142” as noted in 1.b above
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

### CPRS GUI v31b – Host file (CPRS31B_REQUIRED.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the patches listed in section 7.1.3 are part of a single host file for CPRS v31b.

\*\*NOTE – do not queue the install.

Users must not be on the system during the installation. This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 10 minutes.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU.
    1.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    2.  Note that after loading the distribution you are directed to use the name “CPRS V31B REQUIRED PATCHES 1.0” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu.

> NOTE: In the OR\*3\*377 patch description, the after-patch checksum for ORY377 was incorrect. The patch description expected value is 43125694. The actual value should be 43196520.

3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the bundle of patches by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt, you will need to use the name “CPRS V31B REQUIRED PATCHES 1.0” as noted in 1.b above.
5.  When prompted ‘When rebuilding the Health Summary Adhoc Report, do you want to include disabled components?’, answer either YES or NO as appropriate for your site.

> Note: If your site has any components that are temporarily disabled (rather than permanently disabled) and you plan to enable them in the future, you may want to answer YES at this prompt. Keep in mind that you can rebuild the Adhoc Report at any time in the future, at which point you are prompted again whether to include disabled components.

6.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
7.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

Updated Patch Installation Section for PXRM\*2\*45 (a part of the CPRS v31b bundle)

Patch Installation:

-------------------

Pre/Post Installation Overview:

The environment check routine verifies that both Clinical Reminders Update

54 VA-Teratogenic Medications Order Checks (Update \#4) and Update 16

VA-WH Mammogram Screening content update is installed. Installation of

this patch will not proceed if these exchange entries are not installed.

The installation manuals for both updates are available on the VA Software

Documentation Library.

It is important to note that the CPRS v31b Deployment, Installation, Back

Out and Rollback Guide also refers you to a CPRS v31b Configuration and

Setup Guide. This guide provides instructions for both pre and post

install items that must be completed.

Installation Instructions:

Please refer to the "CPRS v31b Deployment, Installation, Back Out and

Rollback Guide" for installation and set-up information. This document is

exported as or_3_0_377_dibr.docx and or_3_0_377_dibr.pdf and is included

in OR_30_377.ZIP and will be emailed to the installation points of contact

by the CPRS Implementation team.

Installation of these host files must be coordinated among the personnel

affected because these host files will be installed in one installation

session.

### TIU\*1\*335 – Host file (TIU_1_335.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*NOTE – do not queue the install.

Users must not be on the system during the installation. This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 10 minutes.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU
    1.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    2.  Note that after loading the distribution you are directed to use the name “TIU\*1.0\*335” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu
3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the patch by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt you will need to use the name “TIU\*1.0\*335” as noted in 1.b above
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

### OR\*3\*531/PXRM\*2\*46 (CPRS_COVID_2_0.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** If the CPRS_COVID_2_0.KID file has previously been installed on your system, it will have to be reinstalled.

Please refer to the *CPRS COVID 2.0 Deployment, Installation, Back-Out and Rollback Guide* for installation and set-up information. This document is exported as CPRS_COVID_2_0_IG.doc and CPRS_COVID_2_0_IG.pdf and will be available on the VDL.

### PXRM\*2\*74 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** Because of shared routines, PXRM\*2\*74 must be installed AFTER PXRM\*2\*45.

Reminders patch PXRM\*2\*74 was released recently. This patch shares at least one routine with PXRM\*2\*45, which is part of the CPRS v31b installation. If CPRS v31b is installed after PXRM\*2\*74 has been installed, then PXRM\*2\*74 must be reinstalled.

The instructions for installing PXRM\*2\*74 are included in the patch description.

## CPRS GUI Executable (OR_30_377.ZIP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the basic CPRS GUI Installation Guide.

Manual Installation Required for CPRS v31b Test Sites

### Methods of installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites have used primarily four methods to distribute the application. Each site will need to decide how they will install. Currently, there is much more participation with ITOPS and coordination with ITOPS will be required.

- Network (shared) installation:

  Where the executable is placed on a network drive, with a shortcut on users’ desktops. The executable is replaced when no users are accessing the GUI program. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Citrix installation:

  Where the executable is run on a remote workstation and the user views the screen remotely. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Gold Path installation:

> where the new executable is placed in a common shared location (called a gold path) and updated when the CPRS GUI is first accessed from the local workstation. This method is handled though desktop enterprise services.

- Manual install:

  which is used primarily for advanced users and at testing locations. This method is somewhat changed from that used previously for Windows XP workstations. For more detail please refer to section 7.3.2, Manual Installation, below.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate the ZIP file for OR\*3\*377 and unzip the file.
2.  Copy the CPRSChart.exe to a test directory, for example, C:\cprstest. You may need to create this new directory.

    Note: You may need to have a user with Administrator rights complete this step.
3.  Create a Shortcut and name it “Test CPRSv31”. This is to give the user another visual cue that this is not the normal CPRS icon.

    ![](or-3-377-deployment-installation-back-out-and-rollback-guide-cprs-gui-31b/002.png)
4.  Copy the borlandmm.dll file into the same directory as cprschart.exe (for example, c:\cprstest). This file should be in the same directory as the CPRSChart.exe for CPRS v31b.
5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  Enter IP and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

![](or-3-377-deployment-installation-back-out-and-rollback-guide-cprs-gui-31b/003.png)

Example of what the shortcut properties dialog might look like.

The server and port number shown above are not real and are for example only.

#### ## CPRS Documentation

The following table shows the documentation released with CPRS v31b. Documentation should be made available to users.

Table 4 CPRS v31b documentation

| *CPRS v31b Release Notes*                                          | Provides an overview of features and changes in CPRS v31b. This document is pertinent to any interested user.         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| *CPRS User Guide: GUI Version*                                     | For end-users, explanation and instructions on using CPRS.                                                            |
| *Online help*                                                      | For end users, explanation of CPRS features.                                                                          |
| *CPRS Technical Manual*                                            | Primarily for users tasked with set up and working on CPRS.                                                           |
| *CPRS Technical Manual: GUI Version*                               | Primarily for users tasked with set up and configuring CPRS.                                                          |
| *CPRS v31b Deployment, Installation, Back Out and Roll Back Guide* | This document. This is for the installers.                                                                            |
| *CPRS v31b Set Up and Configuration Guide*                         | For both installers and CACs to review. Contains items that must be done before and following the patch installation. |

# TEST - Post-Installation Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the *Computerized Patient Record System Version 31b Set Up and Configuration Guide* for the list of post-installation tasks.

# TEST – Testing in Test Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At this point, sites have the chance to test and familiarize themselves with the CPRS v31b in their test account before proceeding to install in their production account.

# CPRS v31b Production System Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

Table 1 Installation Checklist

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 82%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th>Item</th>
<th>Done</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3">Production System Installation</td>
</tr>
<tr class="even">
<td><ol type="1">
<li></li>
</ol></td>
<td>Confirm your system is fully patched (see Section 2.1, Pre-requisite Patches, above)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td>Complete sections 2.2 through 2.2.5</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Download and install the XU*8*653 patch (XU_80_653.KID)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Download and install the XT*7.3*142 patch (XT_73_142.KID)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Download and install the CPRS v31b bundle of patches (CPRSV31B_REQUIRED.KID)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Download and install the TIU*1*335 patch (TIU_1_335.KID)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Test/Mirror system has been successful</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="8" type="1">
<li></li>
</ol></td>
<td>Complete Post-Installation tasks</td>
<td></td>
</tr>
</tbody>
</table>

# Production Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before this installation proceeds several steps need to be accomplished. Many of these steps need be done by Clinical Application Coordinators (CAC), Information Technology Operations and Support (ITOPS), and other groups. Once those set up items are completed, installation can proceed.

Instructions for these items are detailed in the *CPRS Set Up and Configuration Guide*.

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps are taken in case the patch needs to be backed out.

### Back Up Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backup each global below:

> **NOTE:** Make sure to backup each global to its own file.

- ^PXD(801.1,
- ^PXD(801,
- ^PXRMD(801.41,
- ^PXD(811.9,
- ^PXRMD(811.5,
- ^PXRMD(811.4,
- ^PXD(811.2,
- ^PXRMD(801.42,
- ^PXRM(810.4,
- ^ORD(101.41,
- ^TIU(8925.1,
- ^WV(790,
- ^WV(790.05,

### OR MOB DLL VERSION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the OR MOB DLL VERSION parameter, find the value of PKG portion of the parameter and make a note of that value by following the steps below:

Select General Parameter Tools \<TEST ACCOUNT\> Option: LV  List Values for a Selected Parameter

Select PARAMETER DEFINITION NAME: OR MOB DLL

     1   OR MOB DLL NAME     CPRS Med Order Button DLL file name

     2   OR MOB DLL VERSION     CPRS Med Order Button DLL version check

CHOOSE 1-2: 2  OR MOB DLL VERSION   CPRS Med Order Button DLL version check

# Production Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section gives instructions for installing CPRS v31b. Sites should disable ordering, install the patches, distribute the GUI, re-enable ordering for testers, re-enable ordering for all users.

## Disable Ordering during Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is best to ensure that users cannot enter orders while the CPRS software is being updated. To help with this, there is a parameter that disables ordering in CPRS. Disabling ordering should be done before installation begins.

Ordering can then be enabled for testing immediately after installation. The following example shows how to disable ordering for the SYSTEM level.

CHOOSE 1-3: 2  ORWOR DISABLE ORDERING   Disable Ordering in GUI

 

ORWOR DISABLE ORDERING may be set for the following:

 

     2   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV\]

     10  Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\]

 

Enter selection: 5  System   ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV

 

 Setting ORWOR DISABLE ORDERING  for System: ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV

Disable Ordering: YES

 

## Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For CPRS to function correctly, it is necessary that some patches be installed immediately prior to the installation of CPRS Patches. These will be distributed with the CPRS Patches (see Section 0,

Software Retrieval, above), and they should be installed in the order listed below.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>XU*8*653</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol start="2" type="1">
<li><p>XT*7.3*142</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li><p>CPRS V31B REQUIRED PATCHES 1.0</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li><p>TIU*1*335</p></li>
</ol></td>
</tr>
</tbody>
</table>

## CPRS v31b M patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are the actual patches released by this effort.

### XU\*8\*653

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XU\*8\*653 is distributed in a host file separate from the CPRS v31b required bundle. This patch must be installed along with the CPRS v31b required bundle.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>XU*8*653</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### XT\*7.3\*142

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XT\*7.3\*142 is distributed in a host file separate from the CPRS v31b required bundle. This patch must be installed along with the CPRS v31b required bundle.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>XT*7.3*142</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### CPRS v31b Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list of patches are part of the CPRS V31b Required bundle. There is no need to install them individually.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>TIU*1*290</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol start="2" type="1">
<li><p>WV*1*24</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li><p>GMTS*2.7*67</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li><p>DG*5.3*932</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li><p>PXRM*2*45</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li><p>GMRA*4*53</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li><p>GMRC*3.0*88</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="8" type="1">
<li><p>PSO*7*477</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="9" type="1">
<li><p>OR*3*377</p></li>
</ol></td>
</tr>
</tbody>
</table>

### TIU\*1\*335

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch TIU\*1\*335 is distributed in a host file separate from the CPRS v31b required bundle. This patch must be installed along with the CPRS v31b required bundle.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>TIU*1*335</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### XU\*8\*653 – Host file (XU_8_653.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*NOTE – do not queue the install.

Users must not be on the system during the installation. This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 10 minutes.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU
    1.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    2.  Note that after loading the distribution you are directed to use the name “XU\*8.0\*653” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu
3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the patch by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt you will need to use the name “XU\*8.0\*653” as noted in 1.b above
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

### XT\*7.3\*142 – Host File (XT_73_142.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*NOTE – do not queue the install.

Users must not be on the system during the installation. This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 10 minutes.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU
    1.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    2.  Note that after loading the distribution you are directed to use the name “XT\*7.3\*142” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu
3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the patch by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt you will need to use the name “XT\*7.3\*142” as noted in 1.b above
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

### CPRS GUI v31b – Host file (CPRS31B_REQUIRED.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the patches listed in section 7.1.3 are part of a single host file for CPRS v31b.

\*\*NOTE – do not queue the install.

Users must not be on the system during the installation. This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 10 minutes.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU.
    1.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    2.  Note that after loading the distribution you are directed to use the name “CPRS V31B REQUIRED PATCHES 1.0” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu.

> NOTE: In the OR\*3\*377 patch description, the after-patch checksum for ORY377 was incorrect. The patch description expected value is 43125694. The actual value should be 43196520.

3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the bundle of patches by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt, you will need to use the name “CPRS V31B REQUIRED PATCHES 1.0” as noted in 1.b above.
5.  When prompted ‘When rebuilding the Health Summary Adhoc Report, do you want to include disabled components?’, answer either YES or NO as appropriate for your site.

> Note: If your site has any components that are temporarily disabled (rather than permanently disabled) and you plan to enable them in the future, you may want to answer YES at this prompt. Keep in mind that you can rebuild the Adhoc Report at any time in the future, at which point you are prompted again whether to include disabled components.

6.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
7.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

Updated Patch Installation Section for PXRM\*2\*45 (a part of the CPRS v31b bundle)

Patch Installation:

-------------------

Pre/Post Installation Overview:

The environment check routine verifies that both Clinical Reminders Update

54 VA-Teratogenic Medications Order Checks (Update \#4) and Update 16

VA-WH Mammogram Screening content update is installed. Installation of

this patch will not proceed if these exchange entries are not installed.

The installation manuals for both updates are available on the VA Software

Documentation Library.

It is important to note that the CPRS v31b Deployment, Installation, Back

Out and Rollback Guide also refers you to a CPRS v31b Configuration and

Setup Guide. This guide provides instructions for both pre and post

install items that must be completed.

Installation Instructions:

Please refer to the "CPRS v31b Deployment, Installation, Back Out and

Rollback Guide" for installation and set-up information. This document is

exported as or_3_0_377_dibr.docx and or_3_0_377_dibr.pdf and is included

in OR_30_377.ZIP and will be emailed to the installation points of contact

by the CPRS Implementation team.

Installation of these host files must be coordinated among the personnel

affected because these host files will be installed in one installation

session.

### TIU\*1\*335 – Host file (TIU_1_335.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*NOTE – do not queue the install.

Users must not be on the system during the installation. This patch should be loaded during non-peak hours to minimize disruption to users. Installation should take less than 10 minutes.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU
    1.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    2.  Note that after loading the distribution you are directed to use the name “TIU\*1.0\*335” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu
3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the patch by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt you will need to use the name “TIU\*1.0\*335” as noted in 1.b above
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

### OR\*3\*531/PXRM\*2\*46 (CPRS_COVID_2_0.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** If the CPRS_COVID_2_0.KID file has previously been installed on your system, it will have to be reinstalled.

Please refer to the *CPRS COVID 2.0 Deployment, Installation, Back-Out and Rollback Guide* for installation and set-up information. This document is exported as CPRS_COVID_2_0_IG.doc and CPRS_COVID_2_0_IG.pdf and will be available on the VDL.

### PXRM\*2\*74 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** Because of shared routines, PXRM\*2\*74 must be installed AFTER PXRM\*2\*45.

Reminders patch PXRM\*2\*74 was released recently. This patch shares at least one routine with PXRM\*2\*45, which is part of the CPRS v31b installation. If CPRS v31b is installed after PXRM\*2\*74 has been installed, then PXRM\*2\*74 must be reinstalled.

The instructions for installing PXRM\*2\*74 are included in the patch description.

## CPRS GUI Executable (OR_30_377.ZIP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the basic CPRS GUI Installation Guide.

Manual Installation Required for CPRS v31b Test Sites

### Methods of installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites have used primarily four methods to distribute the application. Each site will need to decide how they will install. Currently, there is much more participation with ITOPS and coordination with ITOPS will be required.

- Network (shared) installation:

  Where the executable is placed on a network drive, with a shortcut on users’ desktops. The executable is replaced when no users are accessing the GUI program. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Citrix installation:

  Where the executable is run on a remote workstation and the user views the screen remotely. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Gold Path installation:

> where the new executable is placed in a common shared location (called a gold path) and updated when the CPRS GUI is first accessed from the local workstation. This method is handled though desktop enterprise services.

- Manual install:

  which is used primarily for advanced users and at testing locations. This method is somewhat changed from that used previously for Windows XP workstations. For more detail please refer to section 7.3.2, Manual Installation, above.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate the ZIP file for OR\*3\*377 and unzip the file.
8.  Copy the CPRSChart.exe to a test directory, for example, C:\cprstest. You may need to create this new directory.

    Note: You may need to have a user with Administrator rights complete this step.
9.  Create a Shortcut and name it “Test CPRSv31”. This is to give the user another visual cue that this is not the normal CPRS icon.

    ![](or-3-377-deployment-installation-back-out-and-rollback-guide-cprs-gui-31b/004.png)
10. Copy the borlandmm.dll file into the same directory as cprschart.exe (for example, c:\cprstest). This file should be in the same directory as the CPRSChart.exe for CPRS v31b.
11. Determine the DNS server name or IP address for the appropriate VistA server.
12. Determine the Broker RPC port for the VistA account.
13. Enter IP and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

![](or-3-377-deployment-installation-back-out-and-rollback-guide-cprs-gui-31b/005.png)

Example of what the shortcut properties dialog might look like.

The server and port number shown above are not real and are for example only.

#### ## Enable Ordering for Testers

Once CPRS v31b is installed, sites can enable testing for the specific users that will be testing before all users are allowed on the system.

Below is an example of how to change the parameter at the USER level.

ORWOR DISABLE ORDERING may be set for the following:

 

     2   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV\]

     10  Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\]

 

Enter selection: 2  User   NEW PERSON

Select NEW PERSON NAME: CPRSPROVIDER,TWO CPRSPROVIDER,TWO    TC   PROVIDER

 

---------- Setting ORWOR DISABLE ORDERING  for User: CPRSPROVIDER,TWO ---------

Disable Ordering: NO

Enable all users that will be testing before all users have ordering enabled.

## Enabling Ordering for All Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When testing is complete and the site is comfortable, the site should enable ordering for all users as shown below.

ORWOR DISABLE ORDERING may be set for the following:

 

     2   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV\]

     10  Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\]

 

Enter selection: 5  System   ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV

 

 Setting ORWOR DISABLE ORDERING  for System: ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV

Disable Ordering: YES// @  ...deleted

 

ORWOR DISABLE ORDERING may be set for the following:

 

     2   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV\]

     10  Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\]

## CPRS Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table shows the documentation released with CPRS v31b. Documentation should be made available to users.

Table 4 CPRS v31b documentation

| *CPRS v31b Release Notes*                                          | Provides an overview of features and changes in CPRS v31b. This document is pertinent to any interested user.         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| *CPRS User Guide: GUI Version*                                     | For end-users, explanation and instructions on using CPRS.                                                            |
| *Online help*                                                      | For end users, explanation of CPRS features.                                                                          |
| *CPRS Technical Manual*                                            | Primarily for users tasked with set up and working on CPRS.                                                           |
| *CPRS Technical Manual: GUI Version*                               | Primarily for users tasked with set up and configuring CPRS.                                                          |
| *CPRS v31b Deployment, Installation, Back Out and Roll Back Guide* | This document. This is for the installers.                                                                            |
| *CPRS v31b Set Up and Configuration Guide*                         | For both installers and CACs to review. Contains items that must be done before and following the patch installation. |

# Post-Installation Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the *Computerized Patient Record System Version 31b Set Up and Configuration Guide* for the list of post-installation tasks.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a major issue with the patch, the Facility CIO may make the decision to back-out the patch. However, this decision should include both Health Product Support and the CPRS development team

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out the changes associated with CPRS v31b, personnel would install patch OR\*3.0\*412 that should back out all the patches installed with CPRS v31b.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches should be backed out only if they cause a catastrophic failure of the system.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the patches involved with CPRS v31b would affect many different parts of CPRS. For more information about all the changes in CPRS v31b, please reference the *CPRS v31b Release Notes*, which can be obtained from the [VA Software Document Library](https://www.va.gov/vdl/). However, installing the OR\*3.0\*412 patch should return CPRS to the state it was in prior to the install of CPRS v31b.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility Chief Information Officer (FCIO) has the ultimate responsibility for the decision to back out the two patches and revert to a previous version. The FCIO should consult with the CPRS Development team and Health Product Support Clinical personnel before backing out the patches.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out the features with CPRS v31b, a back out patch was created which should uninstall all the patches installed with CPRS v31b and return the system to a previous state. To back out CPRS v31b, follow these steps:

1.  Install the OR\*3.0\*412 patch.
2.  Reinstall the files that were backed up in Step 6.
3.  Remove the CPRS v31b executable (cprschart.exe) and redistribute the CPRS v31a executable.
4.  Check the desktop icons to see if any adjustments need to be made.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the rollback has been successful, check that the option is back at 31.116. Use VA FileMan to check that MENU TEXT field of the OR CPRS GUI CHART option in the OPTION file (#19) has been reset to 1.0.31.116.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback is required for this installation.