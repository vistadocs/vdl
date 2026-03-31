---
title: IB*2*436 HIPAA 5010 Release Notes/Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: HIPAA 5010 Release Notes/
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*436
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - provider
  - claims
  - patch
  - changes
  - vista
  - billing
  - legal
page_count: 0
word_count: 1488
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_20_p436_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_20_p436_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

HIPAA 5010 Enhancements:

AR for Medicare Policy Types,

Dual Provider Status & Entity Type,

and

Legal Claims & the NPI

Patch IB\*2\*436

Release Notes and Installation Guide

![](ib-2-436-hipaa-5010-release-notes-installation-guide/001.png)

December 2010

*(This page included for two-sided copying.)*

Revision History

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 38%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
<tr class="odd">
<th>12/29/2010</th>
<th>1.0</th>
<th>Initial</th>
<th><p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*(This page included for two-sided copying.)*

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Hardware Compatibility](#hardware-compatibility)
  - [System Specifications](#system-specifications)
- [Installation and Configuration](#installation-and-configuration)
    - [Pre-Installation Considerations](#pre-installation-considerations)
    - [Installation Procedure](#installation-procedure)
    - [Post-Installation Consideration](#post-installation-consideration)
- [Release Changes and Enhancements](#release-changes-and-enhancements)
  - [## AR for Medicare Policy Types](#ar-for-medicare-policy-types)
  - [Provider Status and Entity Type](#provider-status-and-entity-type)
  - [Legal Claims and the NPI](#legal-claims-and-the-npi)
- [Support Information](#support-information)
The U.S. Department of Health and Human Services (HHS) adopted the National Provider Identifier (NPI) as the standard health identifier for health care providers. Veterans Health Administration (VHA) implemented Veterans Health Integrated Systems Technology Architecture (VistA) software system changes to facilitate compliance with Health Insurance Portability and Accountability Act (HIPAA) NPI regulations in May 2007. Since then, Chief Business Office (CBO) Business Development Department through the Office of Enterprise Development (OED) has released a number of software patches to the original VistA NPI design to meet business needs. The VistA system utilizes the NPI in the Integrated Billing (IB), e-Claims Management Engine (ECME), and Fee Basis software applications as the primary identifier for providers and facilities for billing via the Electronic Data Interchange (EDI) process.
Changes to VistA were requested by the VHA CBO Business Development Department to comply with HIPAA standards and meet payer requirements in support of VHA revenue collection initiatives. Some of these changes were requested in an effort to improve the integrity of data stored in VistA files and remove HIPAA rules built into VistA that are negatively impacting non-HIPAA covered transactions.
Additionally, changes to VistA Integrated Billing (IB) and Accounts Receivable (AR) applications were requested by the Veterans Health Administration (VHA) Chief Business Office (CBO) Business Development Department to improve financial integrity and relieve the excessive staff burden inadvertently created by the implementation of electronic Medicare Remittance Advice (MRA) in 2005.

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special hardware considerations.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special system considerations.

# Installation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches IB\*2\*323, IB\*2\*349, and IB\*2\*400 must be installed before installing IB\*2\*436

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that this patch be installed outside of normal working hours; however, if installed during the normal workday, other VistA users will not be affected. Users are allowed to be on the system during the installation except for those options listed below. It is recommended that the patch be installed during non-peak time.

You do not need to stop TaskMan or the background filers.

The following options need to be disabled for this patch:

> ENTER/EDIT BILLING INFORMATION \[IB EDIT BILLING INFO\]

> PROVIDER ID MAINTENANCE \[IBCE PROVIDER MAINT\]

1.  Load Transport Global

> Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.

> Enter message action (in IN basket): Ignore// x Xtract KIDS

> Select PackMan function: INSTALL/CHECK MESSAGE

2.  Start Up KIDS

> Start up the Kernel Installation and Distribution System Menu

> \[XPD MAIN\]

> Edits and Distribution ...

> Utilities ...

> Installation ...

3.  Select Kernel Installation & Distribution System Option: INStallation

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

4.  Select Installation Option

> NOTE: The following are OPTIONAL - (When prompted for the INSTALL NAME, enter IB\*2.0\*436):

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
5.  Select Installation Option: Install Package(s)

> This is the step to start the installation of this KIDS patch:

1.  Choose the Install Package(s) option to start the patch install.
2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//' answer NO
3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO
4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//',answer YES (unless otherwise indicated)
5.  When prompted 'Enter options you wish to mark as 'Out Of Order':' Enter the following options: ENTER/EDIT BILLING INFORMATION \[IB EDIT BILLING INFO\]

> PROVIDER ID MAINTENANCE \[IBCE PROVIDER MAINT\]

### Post-Installation Consideration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After this patch has been installed, those with the "IB PROVIDER EDIT" security key (these individuals would have access to the PROVIDER ID MAINTENANCE option) must review their MailMan messages for the report that is generated as a result of this installation.  The subject line of this email is: "\*\*CLEAN-UP REPORT\*\* - \#200 to \#355.93".

# Release Changes and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch contains enhancements and modifications relating HIPAA 5010 AR for Medicare Policy Types, Dual Provider Status and Entity Type and Legal Claims and the NPI. The changes contained in this patch address the following:

## ## AR for Medicare Policy Types 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Create a new plan type in VistA to accommodate MediGap plan (F&G).

#### All MRA secondary insurance claims will be billed the patient responsibility amount unless the claim is an outpatient claim or an inpatient Professional claim and, in both cases, the MRA secondary insurance is not “MEDIGAP (SUPPLEMENTAL)”.  For outpatient claims and inpatient Professional claims, where the MRA secondary insurance is not “MEDIGAP (SUPPLEMENTAL)”, the new calculation is patient responsibility PLUS Medigap unpaid amount. Therefore, for those MRA secondary insurance’s whose plan type is the new one for MEDIGAP PLAN F & MEDIGAP PLAN G – only outpatient claims and inpatient Professional claims will fall in the new calculation of patient responsibility plus Medigap unpaid amount.  All inpatient Institutional claims with this new plan type (PLAN F and PLAN G) will use the original calculation of patient responsibility.

## Provider Status and Entity Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Allow for entry and storage of a given provider's name (Last, First Middle) to exist in identical content and format in the New Person File (#200) and the IB/Non-VA Other Billing Provider File (#355.93).
2.  To allow the use of a comma in Non-VA Facility names.
3.  Clean-up the IB/Non-VA Other Billing Provider File (#355.93) during the patch installation process:
1.  Synchronize values between the New Person File (#200) and the IB/Non-VA Other Billing Provider File. This utility is run one time during the installation process to compare the Provider Name values using the NPI as the common field. When differences are identified, the provider name in the New Person File will be copied to the provider name field of the IB/Non-VA Other Billing Provider File.
2.  Create a one-time report of all the changes resulting from the aforementioned installation utility.
3.  Email the above report to those users with the "IB PROVIDER EDIT" security key.
4.  Allow Duplicate names between the New Person File (#200) and the IB/Non-VA Other Billing Provider File (#355.93).

## Legal Claims and the NPI 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the purpose of these enhancements, legal claims will be defined as a Billing Rate Type of "NO FAULT INS.", "WORKERS' COMP.", and "TORT FEASOR".

1.  Ability to authorize specified legal claims lacking an NPI.
2.  Ability to locally print legal claims lacking an NPI.
3.  Ability to locally print legal claims with any NPI, if any NPI is available.
4.  Ability to ensure that if the "NO FAULT INS.", "WORKERS' COMP." or "TORT FEASOR" claim is ultimately deemed billable to third-party insurance that the requirement for the NPI remains.

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing, these patches will be supported by the Office of Enterprise Development, the development team. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any issues that arrive related to these patches. At the end of this 30 day period, assistance with issues related to these patches will be addressed through the Help Desk and the submittal of Remedy tickets if needed.