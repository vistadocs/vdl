---
consolidated_title: "drm plus installation guide"
app_code: DRM+
doc_type: installation-guide
master_source: "DENT*1.2*91 DRM Plus Installation Guide"
master_pub_date: April 1989
consolidated_from: 4 versions
prior_versions:
  - "DENT*1.2*90 DRM Plus Installation Guide"
  - "DENT*1.2*92 DRM Plus Installation Guide"
  - "DENT*1.2*93 DRM Plus Installation Guide"
---

## Dental Record Manager Plus (DRM Plus) Application

## Installation Guide DENT*1.2*91

<!-- image -->

## Version 1.2 April 1989 (VA Release) (Revised March 2025)

Department of Veterans Affairs Office of Information and Technology (OI&amp;T) Enterprise Program Management Office

## Installation Guide

## DENT*1.2*91 March 2025

## Table of Contents

| Pre-Installation Considerations ..................................................................................................         |   1 |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Installation Procedure ................................................................................................................    |   1 |
| Installation Instructions...............................................................................................................   |   2 |
| Back-out Procedure ...................................................................................................................     |   4 |
| Back-out Strategy ......................................................................................................................   |   4 |
| Back-out Considerations............................................................................................................        |   5 |
| Back-out Criteria ........................................................................................................................ |   5 |
| Back-out Risks...........................................................................................................................  |   6 |
| Authority for Back-out.................................................................................................................    |   6 |
| Back-out Summary ....................................................................................................................      |   6 |

© 2025 Document Storage Systems, Inc.

## Pre-Installation Considerations

This release of DRM Plus consists of both an executable and a KIDS build.

## ****NOTE****

DENT*1.2*91 is to be nationally released to all VAMCs using DRM Plus.

VAMCs using eDRM (Oracle Cerner) should NOT install the updated executable or KIDS build released with this patch.

************

## Installation Procedure

The DENT*1.2*91 patch is being released in a PackMan message and is available on Forum.

The ZIP file may be obtained at:

https://download.vista.med.va.gov/index.html/SOFTWARE/

Documentation describing the details is included in this release. Documentation can be found on the VA Software Documentation Library (VDL) at: https://www.va.gov/vdl/

The documentation includes:

| File Description   | File Name       | FTP Mode   |
|--------------------|-----------------|------------|
| Dental ZIP file    | DENT_1_2_91.zip | BINARY     |

The DENT\_1\_2\_91.zip file contains the following files:

| Title                                                                                                                                                                                                                 | File Name                                                | FTP Mode             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|----------------------|
| ---------------------------------------------------------------------------------------------------------- DRM Plus Release Notes DRM Plus Installation Guide DRM Plus Technical Manual DRM Deployment, Installation, | DENT_1_2P91_RN.pdf DENT_1_2P91_IG.pdf DENT_1_2P91_TM.pdf | Binary Binary Binary |
| Backout & Rollback Guide(DIBORG)                                                                                                                                                                                      | DENT_1_2P91_DIBR.pdf                                     | Binary               |
| DRM Plus (9.1.0.14)                                                                                                                                                                                                   | dentalmrmtx.exe                                          | Binary               |

Users must exit the DRM Plus application; the existing dentalmrmtx.exe and users should not access DRM Plus until all post-installation steps are complete.

All open DRM Plus GUI applications should be closed (no users should be using the application).

It is not necessary to disable any DENTV* options.

## Installation Instructions

GUI Installation Instructions

-----------------------------

Users must exit the DRM Plus application; the existing dentalmrmtx.exe and users should not access DRM Plus until all post-installation steps are complete.

1. Move dentalmrmtx.exe to the root of ...\DOCSTORE (replace existing file)

'...\' indicates your path for where DRM Plus is located

The version of the new exe is 9.1.0.14

*********************************************************************

These are the NEW compatible DRM Plus files for patch 91:

Name                               Version                 Date

------------------------------------------------------------------------

dentalmrmtx.exe                    9.1.0.14 (server)        02/06/2025

KIDS Installation Instructions

------------------------------

*****Do not queue the installation of this patch.*****

The installation time should take less than 5 minutes.

It is not necessary to disable any DENTV options.

1. Choose the PackMan message containing this patch then select the INSTALL/CHECK MESSAGE PackMan option to load the build.

2. From the Kernel Installation and Distribution System Menu, select the Installation Menu.  From this menu, you may elect to use the following option. When prompted for the INSTALL enter the patch DENT*1.2*91:

- a.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates. NOTE: This step is critical in the event it is necessary to back out this patch. You must use this option and specify what to backup; the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.

- i.   At the Installation option menu, select Backup a Transport Global.
- ii.  At the Select INSTALL NAME prompt, enter your build DENT*1.2*91.
- iii. When prompted for the following, enter "B" for Build.

Select one of the following:

B       Build

R       Routines

Enter response: Build

- iv.  When prompted "Do you wish to secure this message? NO//", press &lt;enter&gt; and take the default response of "NO".
- v.   When prompted with, "Send mail to: Last name, First Name", press &lt;enter&gt; to take the default recipient. Add any additional recipients.
- vi.  When prompted with "Select basket to send to: IN//", press &lt;enter&gt; and take the default IN mailbox or select a different mailbox.
- b.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed.  It compares all components of this patch (routines, DDs, templates, etc.).
- c.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
3. Select the Install Package(s) option and choose the patch to install.
- a. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
- b. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO.
- c. When prompted 'Enter the Device you want to print the Install messages. You can queue the install by enter a 'Q' at the device

prompt. Enter a '^' to abort the install.

DEVICE: HOME//     VIRTUAL TELNET   ****DO NOT QUEUE THE INSTALLaccept the default device HOME and the install messages will print to the terminal screen.

## Routine Information

====================

The following is a list of the routine(s) included in this build.

The second line of each routine will look as follows.

;;1.2;DENTAL;&lt;patch list&gt;;APR 11,1989;Build 4

Verify Checksums using CHECK1^XTSUMBLD.

| Routine   | Before Patch   | After Patch   | Patch List                             |
|-----------|----------------|---------------|----------------------------------------|
| DENTVA2   | B44383866      | B49539934     | 38,39,42,43,45,47,50,53,63,66,69,91    |
| DENTVA3   | B26287253      | B31454218     | 43,45,47,59,91                         |
| DENTVA7   | B69580370      | B69790590     | 47,53,55,57,77,91                      |
| DENTVTPA  | B78126672      | B78501596     | 39,42,43,45,47,53,57,59,63,66,69,86,91 |
| DENTVTPD  | B49616067      | B48725325     | 39,47,50,53,86,91                      |
| DENTVUT1  | N/A            | B2215316      | 91                                     |

## Back-out Procedure

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings. Successful back-out requires successful backup prior to installing software. Please read the Dental Record Manager Plus (DRM Plus) Application Deployment, Installation, Backout, and Rollback Guide for detailed instructions.

## Back-out Strategy

The DRM Plus back-out strategy involves communication with stakeholders including site users, OI&amp;T, help desk, developers, quality assurance, and any others such as VA business owners. This communication allows all parties to have an impact on the decision to back-out software, and to act on the plan to restore the environment(s) to a previous, working state. Step by step instructions are followed. Each installation will include specific back-out procedures relevant to the components and to the changes made to the system. Back-out may involve copying a previous version of an executable onto a production server or restoring VistA routines from a transport global.

Successful back-outs require conscientious following of installation steps, especially for any backup procedures. For example, the steps may state that installers copy the previous version of an executable to a safe storage area. If a previous version is not available at the site, DSS, Inc. will provide the necessary version of the software using SFTP or another approved transfer method. After the back-out, tests are performed to ensure the software is working, and then stakeholders are notified. A remediation plan is put into place to correct the issue(s) necessitating a back-out.

VistA KIDs builds cannot be backed out/restored in totality - only routines are part of a backup transport global. Special care is taken during development of VistA code (routines, files, remote procedures, etc.) to make them backward compatible with newer GUI versions to alleviate the issue and avoid typical critical scenario solutions such as emergency patches.

The decision to back-out a specific release needs to be made in a timely manner. Catastrophic failures are usually known early in the testing process - within the first two or three days. Sites are encouraged to perform all test scripts to ensure new code is functioning in their environment, with their data. A back-out should only be considered for critical issues or errors. The normal, or an expedited, issue-focused patch process can correct other bugs.

## Back-out Considerations

Back-outs are not desirable, and the decision to back-out should involve stakeholders from various business units. A back-out should be performed as early after installation as possible to avoid issues with data (see roll-back section). If data corruption has occurred, or will occur, then sometimes it is safer to create an emergency fix to correct the problem, rather than return to a previous state.

## Back-out Criteria

Stakeholders involved in the decision to back-out software should be prepared to answer the following questions:

- Was the installation performed correctly and completely? Installed component versions should be verified.
- What component(s) failed?
- Are failures specific to a user, or to all users? Failures for a specific user may be hardware or parameter setting-based issues (user profile, etc.).
- Is there a work-around for the failure?
- Is data involved in the failure?
- Who will make the decision to revert to a previous version?
- Who will perform the back-out?
- How soon can the back-out be performed?

- Does the staff responsible for the back-out understand the procedures?
- How soon after the decision has been made will the back-out be performed?
- What is the expected time required to perform a reversion?
- What are the communication procedures required in the event of a back-out?
- Has the Back-out Plan been successfully tested?
- What are the success criteria to be used to denote a successful back-out?

## Back-out Risks

DSS, Inc. develops VistA KIDs builds to be backward compatible with previous versions to avoid back-out risks.

When a back-out is necessary, the instructions may include stopping to verify data and/or versions after certain steps. Following instructions carefully will mitigate back-out risks.

## Authority for Back-out

For DENT*1.2*91, the VA Business owner has ultimate responsibility for the product. The business owner or their designee will make the decision to back-out an installation based on feedback from the stakeholders (users, DSS Development, DSS Installation, DSS Support, etc.)

## Back-out Summary

For VA server components, the procedures can be performed in VA test account environments prior to performing them in the production account.

1.  Notify stakeholders using MS Outlook.
2.  Ensure users are not using DRM Plus.
3.  If the development team has determined that the VistA routines should be restored, load the backup transport global (saved in Mailman during the installation process) and install the prior routines.
4.  Enable access to users.
5.  Test the software
6.  Notify stakeholders of the outcome via Outlook.

For  executable components the procedures can be performed in VA test account environments prior to performing them in the production account. The dentalmrmtx executable included with the patch would need to be replaced by the dentalmrmtx executable from the previous release.

## MISCELLANEOUS INFORMATION

=========================

DSS (Document Storage Systems): Help Desk:  REDACTED Hours of Operation: 8:00 AM TO 7:00 PM (ET) After-Hours Support: REDACTED

VA Enterprise Service Desk:  REDACTED

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DENT*1.2*93 DRM Plus Installation Guide

## Dental Record Manager Plus

## (DRM Plus) Application Installation Guide DENT*1.2*93

<!-- image -->

## Department of Veterans Affairs Office of Information and Technology (OI&amp;T) Enterprise Program Management Office

## DENT*1.2*93 February 2026

## EHRM Impact Statement:

----------------------

This patch should have no EHRM impact, and can be installed at all sites, including EHRM converted sites.

****NOTE****

DENT*1.2*93 is an M side only patch and should be installed at all VAMC's.

************

## *****Do not queue the installation of this patch*****

The installation time should take less than 5 minutes.

It is not necessary to disable any DENTV options.

1. Choose the PackMan message containing this patch then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2. From the Kernel Installation and Distribution System Menu, select the Installation Menu.  From this menu, you may elect to use the following options. When prompted for the INSTALL name enter DENT*1.2*93:
- a.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.

> **NOTE:** This step is critical in the event it is necessary to back out this patch.

You must use this option and specify what to backup; the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.

- i. At the Installation option menu, select Backup a Transport Global.
- ii. At the Select INSTALL NAME prompt, enter your build DENT*1.2*93.
- iii. When prompted for the following, enter "B" for Build.

Select one of the following:

B       Build

R       Routines

Enter response: Build

- iv. When prompted "Do you wish to secure this message? NO//", press &lt;enter&gt; and take the default response of

"NO".

- v. When prompted with, "Send mail to: Last name, First Name", press &lt;enter&gt; to take the default recipient. Add any additional recipients.
- vi. When prompted with "Select basket to send to: IN//", press &lt;enter&gt; and take the default IN mailbox or select a different mailbox.
- b.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed.  It compares all components of this patch (routines, DD's, templates, etc.).
- c.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
3. From the Installation Menu, select the Install Package(s) option and choose the patch to install.
- a. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
- b. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO.
- c. When prompted 'Enter the Device you want to print the Install messages. You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

## DEVICE: HOME//     VIRTUAL TELNET ****DO NOT QUEUE THE INSTALL-

accept the default device HOME and the install messages will print to the terminal screen.

## NOTE: Do not delete the DENTV093 install routine as it may be necessary in the event of a back-out event.

## Verify Checksums using CHECK1^XTSUMBLD.

| Routine   | Before Patch   |   After Patch |   Patch List |
|-----------|----------------|---------------|--------------|
| DENTV093  | n/a            |     186616324 |           93 |

## Refer to the DRM Deployment, Installation, Backout, Rollback Guide (DIBORG) for additional information.

Contact the DSS (Document Storage Systems) Help Desk for assistance.

### From: DENT*1.2*92 DRM Plus Installation Guide

## (DRM Plus) Application

## DENT*1.2*92 January 2025

## DEVICE: HOME//     VIRTUAL TELNET ****DO NOT QUEUE THE INSTALLaccept the default device HOME and the install messages will print to the terminal screen.

## NOTE: Do not delete the DENTV092 install routine as it may be necessary in the event of a back-out event.

### From: DENT*1.2*90 DRM Plus Installation Guide

## DENT*1.2*90 June 2024
