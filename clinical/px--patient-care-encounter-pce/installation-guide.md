---
title: PX*1*215 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: null
app_code: PX
app_name: Patient Care Encounter (PCE)
section: CLI
app_status: active
pkg_ns: PX
patch_ver: 1
patch_id: PX*1*215
group_key: PX:PX:1
file_numbers:
- '3'
- '50.67'
- '800'
- '811.1'
- '920'
- '920.05'
- '920.051'
- '920.1'
- '920.2'
- '920.3'
- '920.4'
- '920.5'
- '920.6'
- '920.61'
- '1201'
- '1204'
- '1220'
- '1302'
- '1303'
- '1312'
- '1313'
- '1601'
- '80101'
- '80102'
- '81101'
- '81201'
- '81202'
- '81203'
- '900001'
- '999999'
security_keys:
- PROVIDER
menu_options: 0
description: VistA Immunization Enhancements Increment 3.0VIMM Patch PX\1.0\215Installation Guide
audience: System administrators performing installation
keywords: []
page_count: 0
word_count: 2502
section_count: 8
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: null
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/px_1_p215_installation_guide.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/px_1_p215_installation_guide.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=82
audit_applied: '2026-05-31'
master_source: PX*1*215 Installation Guide
master_pub_date: 'null'
consolidated_from: 2 versions
prior_versions:
- PX*1*216 Installation Guide
consolidated_title: installation guide
---

VistA Immunization Enhancements Increment 3.0VIMM Patch PX\*1.0\*215Installation Guide

![](px-1-215-installation-guide/001.png)

October 2016Version 1.2Revision History

<table>
<caption>Version History</caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Version</td>
<td>Description</td>
<td>Author</td>
</tr>
<tr class="even">
<td>10/20/2016</td>
<td>1.2</td>
<td><p>Revised version</p>
<p>Updated coversheet (month: from September to October), (version: from 1.1 to 1.2).</p>
<p>Updated footer from VIMM Patch PX*1.1*215 to VIMM Patch PX*1.0*215 and the month to October.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/2016</td>
<td>1.1</td>
<td>Revised version</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/2016</td>
<td>1.0</td>
<td>Initial version</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Version History

<u>Table of Contents</u>

# Description of Program


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Description of Program](#description-of-program)
- [Goal of VIMM 2.0](#goal-of-vimm-20)
- [New Features in Patch PX\1.0\215](#new-features-in-patch-px10215)
- [Test Sites](#test-sites)
- [Documentation Retrieval Instructions (VIMM Patch PX\1.0\215)](#documentation-retrieval-instructions-vimm-patch-px10215)
- [Patch Installation (VIMM Patch PX\1.0\215)](#patch-installation-vimm-patch-px10215)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Pre-Installation Instructions](#pre-installation-instructions)
  - [Post-Installation Instructions](#post-installation-instructions)
  - [Rollback Instructions](#rollback-instructions)
- [Installation Instructions for Dependent/Associated Patch](#installation-instructions-for-dependentassociated-patch)
  - [Installation Instructions for Patch PSN\4.0\448](#installation-instructions-for-patch-psn40448)
- [Installation Instructions for PX\1.0\215](#installation-instructions-for-px10215)
- [Step-by-Step Instructions for PX\1.0\215](#step-by-step-instructions-for-px10215)
- [Post-Installation Instructions / Routine Information for PX\1.0\215](#post-installation-instructions-routine-information-for-px10215)
  - [Post-Installation Instructions](#post-installation-instructions-1)
  - [Routine Information](#routine-information)
The Veterans Health Information Systems and Technology Architecture (VistA) Immunizations Enhancements (VIMM) 2.0 project modifies existing Immunization and Skin Test files and adds additional files to enable VA to quickly and reliably document and exchange standardized skin test and immunization information on beneficiaries across services and departments.
Additionally, modifications support VistA Evolution requirements.
This provides a Veteran patient-centric immunization record exchangeable with the external community. Clinicians will have access to a more complete medical history in the VistA electronic medical record resulting in improved health status as well as public health monitoring.

# Goal of VIMM 2.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Information Systems and Technology Architecture (VistA) Immunizations Enhancements (VIMM) 2.0 project, Increment 3, builds upon the file structures and standardized data introduced in Increments 1 and 2 by adding functional enhancements to the existing VistA Patient Care Encounter (PCE) package.

# New Features in Patch PX\*1.0\*215

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch provides the following new features:

1.  Creates Remote Procedure Calls (RPCs) for use by the Enterprise Health Management Platform (eHMP) project, the Computerized Patient Record System (CPRS) software, Data Access Service (DAS), and others. These RPCs retrieve immunization information from the following files:

> VACCINE INFORMATION STATEMENT (#920)

> IMMUNIZATION INFO SOURCE (#920.1)

> IMM ADMINISTRATION ROUTE (#920.2)

> IMM ADMINISTRATION SITE (BODY) (#920.3)

> IMM CONTRAINDICATION REASONS (#920.4)

> IMM REFUSAL REASONS (#920.5)

> V IMM CONTRA/REFUSAL EVENTS (#9000010.707)

> IMM MANUFACTURER (#9999999.04)

> IMMUNIZATION (#9999999.14)

> IMMUNIZATION LOT (#9999999.41)

> IMM DEFAULT RESPONSES (#920.05)

2.  Introduces functionality for capturing the reason(s) an immunization was not given by documenting immunization contraindications and/or refusal events. This functionality includes the following:
1.  Creation of the V IMM CONTRA/REFUSAL EVENTS file (#9000010.707).
2.  A WARNING UNTIL DATE may be stored for temporary contraindications/refusals. The contraindication/refusal is valid until this date.
3.  When an immunization for a patient is associated with valid contraindications/refusals, (WARNING UNTIL DATE is not a past date), the software will display a warning and the user will be required to acknowledge the warning and enter a justification reason before continuing with administration.
    1.  Inactivates the functionality of the PCE CODE MAPPING file (#811.1). The file will still exist, but the mappings in the file will no longer be used to determine which related entries in the V IMMUNIZATION (#9000010.11), V SKIN TEST (#9000010.12), and V CPT (#9000010.18) files need to automatically be recorded. From now on, the mappings in the CODING SYSTEM multiple of the IMMUNIZATION (#9999999.14) and SKIN TEST (#9999999.28) files will be used for this purpose. There are a few differences with this new approach:
1.  The PCE CODE MAPPING file was managed locally, while the CODING SYSTEM multiple of the IMMUNIZATION and SKIN TEST files are standardized and managed nationally.
2.  We will now support mappings to ICD-10 codes. If an immunization or skin test is mapped to an ICD-10 code, when that immunization or skin test is documented, we will automatically file the mapped ICD-10 code to the V POV file (#9000010.07).
3.  We will stop the practice of automatically recording an immunization or skin test when a corresponding CPT code is filed. The mappings will only be used to automatically file the corresponding codes (CPT and ICD-10) when an immunization or skin test is documented. However, in the reverse scenario, when a CPT code is documented, we will not automatically record the corresponding immunization or skin test.
4.  Codes will only automatically be filed when a VA-administered (non-historical) immunization or skin test is documented.
    1.  Includes functionality to enable a documenting provider to view some immunization prompts with default values to accept and to edit the responses if need be. This functionality includes:
1.  Creation of the IMM DEFAULT RESPONSES file (#920.05) to store facility specific default values by immunization type for ROUTE OF ADMINISTRATION, SITE OF ADMINISTRATION, DOSE, DOSE UNITS, and COMMENTS.
2.  Creation of the Immunization Default Responses Enter/Edit menu option \[PXV EDIT DEFAULT RESPONSES\] to allow authorized users to enter or update information in the IMM DEFAULT RESPONSES file (#920.05).
    1.  Updates the NDC CODE (VA) field (#.18) in the IMMUNIZATION LOT file (#9999999.41) so that access to information in the NDC/UPN file (#50.67) is controlled by application programmer interfaces (APIs).

APIs Associated:<u>API New/Modified/Deleted</u>

DATA2PCE^PXAPI (ICR \#1889) Modified

GETENC^PXAPI (ICR \#1894) Modified

ENCEVENT^PXKENC (ICR \#1894) Modified

VICR^PXPXRM (ICR \#4250) New

VICR^PXPXRMI1 (ICR \#4519) New

DQSAVE^PXRPC (ICR \#6386) New

IMMSTAT^PXAPIIM (ICR \#6387) New

Files & Fields Associated:<u>File Name (Number)</u>

> <u>Field Name (Number) New/Modified/Deleted</u>

IMM DEFAULT RESPON (#920.05)

> FACILITY (#.01) New

> IMMUNIZATION (multiple field \#1, sub-file \#920.051) New

> IMMUNIZATION (#.01) of the IMMUNIZATION

> sub-file (#920.051) New

> ROUTE OF ADMINISTRATION (#1302) of the

> IMMUNIZATION sub-file (#920.051) New

> SITE OF ADMINISTRATION (#1303) of the

> IMMUNIZATION sub-file (#920.051) New

> DOSE (#1312) of the IMMUNIZATION

> sub-file (#920.051) New

> DOSE UNITS (#1313) of the IMMUNIZATION

> sub-file (#920.051) New

> COMMENTS (#81101) of the IMMUNIZATION

> sub-file (#920.051) New

IMM CONTRAINDICATION REASONS (#920.4)

> CONCEPT CODING SYSTEM (#.05) Modified

IMM ROUTES TO SITES (#920.6)

> ROUTE (#.01) New

> SITES (multiple field \#1, sub-file \#920.61) New

> SITES (#.01) of the SITES sub-file (#920.61) New

V IMMUNIZATION (#9000010.11)

> WARNING ACKNOWLEDGED (#1220) New

> WARNING OVERRIDE REASON (#1601) New

V SKIN TEST (#9000010.12)

> CODING SYSTEM (multiple field \#3, sub-file

> \#9000010.123) Deleted

> CODING SYSTEM (#.01) of the CODING SYSTEM

> sub-file (#9000010.123) Deleted

> CODE (multiple field \#.02, sub-file \#9000010.1231

> of the CODING SYSTEM sub-file (#9000010.123) Deleted

> CODE (#.01) of the CODE sub-file (#9000010.1231) Deleted

V IMM CONTRA/REFUSAL EVENTS (#9000010.707)

> CONTRAINDICATION/REFUSAL (#.01) New

> PATIENT NAME (#.02) New

> VISIT (#.03) New

> IMMUNIZATION (#.04) New

> WARN UNTIL DATE (#.05) New

> DATE/TIME RECORDED (#.06) New

> EVENT DATE AND TIME (#1201) New

> ENCOUNTER PROVIDER (#1204) New

> EDITED FLAG (#80101) New

> AUDIT TRAIL (#80102) New

> COMMENTS (#81101) New

> VERIFIED (#81201) New

> PACKAGE (#81202) New

> DATA SOURCE (#81203) New

IMMUNIZATION LOT (#9999999.41)

> NDC CODE (VA) (#.18) Modified

PCE CODE MAPPING (#811.1) Modified

<u>Options Associated:</u><u>Option Name Type New/Modified/Deleted</u>

PXV EDIT DEFAULT RESPONSES Run Routine New

PX PCE CODE MAPPING LIST Print Modified

<u>Protocols Associated:</u><u>Protocol Name New/Modified/Deleted</u>

PXCE ADD/EDIT MENU Modified

PXCE ICR ADD New

<u>RPCs Associated:</u><u>RPC New/Modified/Deleted</u>

PX SAVE DATA Modified

PXVIMM ADMIN CODES New

PXVIMM ADMIN ROUTE New

PXVIMM ADMIN SITE New

PXVIMM ICR LIST New

PXVIMM IMM DETAILED New

PXVIMM IMM FORMAT New

PXVIMM IMM LOT New

PXVIMM IMM MAN New

PXVIMM IMM SHORT LIST New

PXVIMM IMMDATA New

PXVIMM INFO SOURCE New

PXVIMM VICR EVENTS New

PXVIMM VIS New

<u>Patient Safety Issues (PSIs):</u>

PSPO \#2995

PSPO \#3069

<u>Defect Tracking System Ticket(s) & Overview:</u>

1\. INC000001294271

R4956462FY15

R6300645FY16

<u>Related Patient Safety Issues:</u>

PSPO \#2995

PSPO \#3069

<u>Problem:</u>

> PCE CODE MAPPING issues are causing duplicate or incorrect entries to be documented to the V IMMUNIZATION file.

<u>Resolution:</u>

> The PCE CODE MAPPING file will be deprecated. Instead, we will use the CODING SYSTEM multiple of the IMMUNIZATION and SKIN TEST files.

# Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Cleveland, OH
- St. Louis, MO
- San Antonio, TX

# Documentation Retrieval Instructions (VIMM Patch PX\*1.0\*215)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software documentation is being released as a host file and/or documentation describing the new functionality introduced by this patch is available.

The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at: http://www4.va.gov/vdl/

| Title                                               | File Name         | FTP Mode |
|-----------------------------------------------------|-------------------|----------|
| Patient Care Encounter (PCE) V. 1.0 User Manual     | PX_1_UM_R0816.PDF | (binary) |
| Patient Care Encounter (PCE) V.1.0 Technical Manual | PX_1_TM_R0816.PDF | (binary) |
| Clinical Reminders (PXRM) Index Technical Manual    | PXRM_INDEX_TM.PDF | (binary) |

List of user documentation for patch PX\*1\*215

# Patch Installation (VIMM Patch PX\*1.0\*215)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Associated patches:

> Patch PX\*1.0\*186 must be installed BEFORE PX\*1.0\*215

> Patch PX\*1.0\*195 must be installed BEFORE PX\*1.0\*215

> Patch PX\*1.0\*210 must be installed BEFORE PX\*1.0\*215

> Patch PSN\*4.0\*448 must be installed BEFORE PX\*1.0\*215

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-installation process will generate a report from the PCE CODE MAPPING file (#811.1) for review. The report will contain all active mappings where either a) an inactive immunization was mapped to a CPT code; or b) a CPT code was mapped to an immunization or skin test. The report will be emailed to the user who installed the patch and to the mail group specified in the REMINDER MANAGEMENT MAILGROUP field (#3) of the CLINICAL REMINDER PARAMETERS file (#800). The report will also be sent to the VHA National Center for Health Promotion and Disease Prevention (NCP) for review. If it is determined that patient charts may have been affected with erroneous data prior to the inactivating of the PCE CODE MAPPING file with this patch, the site will be contacted and instructed to submit a help desk ticket for resolution.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSN\*4.0\*448 must be installed before installing patch PX\*1.0\*215.

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event a rollback is needed, the site should log a CA SDM (Service Desk Manager) ticket. The site must work closely with the development team to back out the patch, as it requires restoring data dictionaries (DDs).

Refer to the VIMM 2.0 Increment 3 Recovery Procedures document for more information.

Located at this link: <span class="mark">REDACTED</span>

Rollback procedures for PSN\*4.0\*448 are included in the document mentioned above.

# Installation Instructions for Dependent/Associated Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **WARNING:** Associated patch must be installed in the proper order

The following patches must be installed in this order

1.  Patch PSN\*4.0\*448 Additional NDC/UPN APIS
2.  Patch PX\*1.0\*215 VIMM 2.0 patch

The following installation instructions for the dependent patch has been included in the following section.

## Installation Instructions for Patch PSN\*4.0\*448

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Associated patch:

> PSN\*4.0\*296 must be installed BEFORE PSN\*4.0\*448

Description of Patch PSN\*4.0\*448

> This patch adds three components to the routine PSNAPIS, supported by Integration Control Registration (ICR) \#2531, to provide additional access to the NDC/UPN file (#50.67).

1.  INTRAN - This entry point provides input transform lookup functionality for fields that store NDC codes.
2.  DRGCLS - This entry point returns class and parent class for a National Drug Code (NDC).
3.  QLIST - This entry point provides executable help ("?" or "??") for fields that store NDC codes.

> APIs Associated:

> <u>API New/Modified/Deleted</u>

> INTRAN^PSNAPIS New

> DRGCLS^PSNAPIS New

> QLIST^PSNAPIS New

Additional Information:Test Sites:

- Cleveland, OH
- Heartland-East HCS
- San Antonio, TX

Software and Documentation Retrieval Instructionsfor Patch PSN\*4.0\*448:

> The software documentation is being released as a host file and/or documentation describing the new functionality introduced by this patch is available.

> The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

> Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

> <span class="mark">REDACTED</span>

> Documentation can also be found on the VA Software Documentation Library at: http://www4.va.gov/vdl/.

| Title                                    | File Name            | FTP Mode |
|------------------------------------------|----------------------|----------|
| Pharmacy Re-Engineering (PRE) API Manual | PHAR_1_API_R0316.PDF | (binary) |

List of user documentation for patch PSN\*4\*448

INSTALLATION INSTRUCTIONS for Patch PSN\*4.0\*448

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter the patch \# (PSN\*4.0\*448):
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install. Enter PSN\*4.0\*448.
5.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'

> Answer NO.

6.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//'

> Answer NO.

Routine Information:

> The second line of each of these routines now looks like:

> ;;4.0;NATIONAL DRUG FILE; \*\*\[Patch List\]\*\*; 30 Oct 98;Build 2

> The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

> Routine Name: PSNAPIS

> Before: B50538431 After: B59524567 \*\*2,3,47,70,169,108,262,296,448\*\*

# Installation Instructions for PX\*1.0\*215

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **WARNING:** Associated patch must be installed in the proper order

The following patches must be installed in this order:

1.  Patch PSN\*4.0\*448 Additional NDC/UPN APIS
2.  Patch PX\*1.0\*215 VIMM 2.0 patch

This patch should be installed during a period of minimal system activity, preferably with users off the system. Installation time is expected to be approximately 10 minutes.

# Step-by-Step Instructions for PX\*1.0\*215

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be installed during a period of minimal system activity, preferably with users off the system. Installation time is expected to be approximately 10 minutes.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch \# (PX\*1.0\*215):
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
    4.  Print Transport Global - This option will allow you to view the components of the KIDS build.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install. Enter PX\*1.0\*215.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//'

> Answer YES.

6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'

> Answer NO.

7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Answer NO.

# Post-Installation Instructions / Routine Information for PX\*1.0\*215

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Routine Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second line of each of these routines now looks like:

> ;;1.0;PCE PATIENT CARE ENCOUNTER ;\*\*\[Patch List\]\*\*;Aug 12, 1996;Build 10

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

Routine Name: PXAI

> Before: B40979532 After: B42819168 \*\*15,74,69,102,111,112,130,164,168,215\*\*

Routine Name: PXAIICR

Before: n/a After: B5253575 \*\*215\*\*

Routine Name: PXAIICRV

Before: n/a After: B12775865 \*\*215\*\*

Routine Name: PXAIIMM

Before: B14255138 After: B16045767 \*\*45,124,209,210,215\*\*

Routine Name: PXAPIIM

Before: B2741056 After: B80558091 \*\*210,215\*\*

Routine Name: PXCEAE

Before: B32867509 After: B33109650 \*\*37,67,99,147,156,172,195,215\*\*

Routine Name: PXCEAE1

Before: B29168014 After: B29262597 \*\*22,73,199,201,210,215\*\*

Routine Name: PXCEICR

Before: n/a After: B18593217 \*\*215\*\*

Routine Name: PXCEVFI1

> Before: B23924796 After: B33198888 \*\*23,73,112,136,143,124,184,185,210,215\*\*

Routine Name: PXCEVFI2

Before: B34344095 After: B37818294 \*\*22,73,95,96,124,158,184,215\*\*

Routine Name: PXCEVFIL

> Before: B43615497 After: B44185519 \*\*9,30,22,73,88,89,104,147,124,169,210,215\*\*

Routine Name: PXCEVIMM

Before: B83423957 After: B86101677 \*\*27,124,199,201,210,215\*\*

Routine Name: PXKENC

Before: B29230371 After: B29334197 \*\*15,22,73,108,143,183,210,215\*\*

Routine Name: PXKFCPT1

Before: B23838795 After: B24656697 \*\*11,73,124,194,209,215\*\*

Routine Name: PXKFICR

Before: n/a After: B1725753 \*\*215\*\*

Routine Name: PXKFIMM

Before: B4427968 After: B5142444 \*\*22,124,201,209,210,215\*\*

Routine Name: PXKFPOV1

Before: n/a After: B9458058 \*\*215\*\*

Routine Name: PXKMAIN

> Before: B55417967 After: B55424847 \*\*22,59,73,88,69,117,130,124,174,164,210,215\*\*

Routine Name: PXKMAIN2

Before: B10938982 After: B25829818 \*\*69,186,215\*\*

Routine Name: PXPXRM

Before: B88904295 After: B125590932 \*\*119,199,210,215\*\*

Routine Name: PXPXRMI1

Before: B55159505 After: B104225670 \*\*119,194,210,215\*\*

Routine Name: PXRPC

Before: B109684381 After: B156917264 \*\*200,209,210,215\*\*

Routine Name: PXVNDC

Before: n/a After: B1736379 \*\*215\*\*

Routine Name: PXVP215

Before: n/a After: B34039279 \*\*215\*\*

Routine Name: PXVRESP

Before: n/a After: B3810590 \*\*215\*\*

Routine Name: PXVRPC1

Before: n/a After: B70359613 \*\*215\*\*

Routine Name: PXVRPC2

Before: n/a After: B29476719 \*\*215\*\*

Routine Name: PXVRPC3

Before: n/a After: B28618741 \*\*215\*\*

Routine Name: PXVRPC4

Before: n/a After: B131321819 \*\*215\*\*

Routine Name: PXVRPC5

Before: n/a After: B35105697 \*\*215\*\*

Routine Name: PXVRPC6

Before: n/a After: B16158307 \*\*215\*\*

Routine Name: PXVUTIL

Before: B10006565 After: B13284181 \*\*201,210,215\*\*

Routine Name: PXVZRT

Before: B71159926 After: B82546869 \*\*206,215\*\*

Routine list of preceding patches: 168, 186, 195, 206, 210