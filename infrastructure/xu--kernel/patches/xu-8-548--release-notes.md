---
title: XU*8*548 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*548
group_key: "XU:XU:8"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - extract
  - installation
  - table
  - contents
  - crosswalk
  - patch
  - vista
  - changes
  - transport
  - global
page_count: 0
word_count: 1400
section_count: 3
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2011
revision_count: 2
revision_newest: 01/13/2011
revision_oldest: 08/23/2010
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu_80_p548_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu_80_p548_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

HIPAA 5010 – Enhancement 12

NPI Crosswalk Extract

Patch XU\*8.0\*548

Release Notes and Installation Guide

![](xu-8-548-release-notes/001.png)

January 2011

Revision History

| Date       | Version | Description               | Author   |
|------------|---------|---------------------------|----------|
| 08/23/2010 | 1.0     | Initial                   | REDACTED |
| 01/13/2011 | 2.0     | Patch Description changes | REDACTED |

Table of Contents

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
- [SUPPORT INFORMATION](#support-information)
Changes to the Veterans Health Integrated Systems Technology Architecture (VistA) National Provider Identifier (NPI) Crosswalk Extract application software are being requested by the Veterans Health Administration (VHA) Chief Business Office (CBO) Business Development Department to comply with Health Insurance Portability and Accountability Act (HIPAA) standards and meet payer requirements in support of VHA revenue collection initiatives.
The U.S. Department of Health and Human Services (HHS) adopted the NPI as the standard health identifier for health care providers. VHA implemented VistA software system changes to facilitate compliance with HIPAA NPI regulations in May 2007. Since then, CBO Business Development Department through the Office of Enterprise Development (OED) has released a number of software patches to the original VistA NPI design to meet business needs. The VistA system utilizes the NPI in the Integrated Billing (IB), e-Claims Management Engine (ECME), and Fee Basis software applications as the primary identifier for providers and facilities for billing via the Electronic Data Interchange (EDI) process.
One of the software released was the NPI Crosswalk Extract. The NPI Crosswalk Extract software application is designed to extract both organizational and individual practitioner NPI data from the VistA National Institution File (File 4) and the VistA New Person File (File 200), respectively in addition to a few other files. Note that the NPI Crosswalk Extract application currently pulls data on both VHA and non-VHA organizations and practitioners. This patch includes the CBO requested changes to the VHA component of the NPI Crosswalk Extract application.

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

Patch XU\*8\*528 must be installed before installing XU\*8\*548

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that this patch be installed outside of normal working hours, however, if installed during the normal workday, other VistA users will not be affected. Users are allowed to be on the system during the installation except for those options listed below. It is recommended that the patch be installed during non-peak time. It will take less than five minutes to install the patch, but the installation may be queued.

You do not need to stop TaskMan or the background filers.

1.  Load Transport Global

> Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.

> Enter message action (in IN basket): Ignore// x Xtract KIDS

> Select PackMan function: INSTALL/CHECK MESSAGE

2.  Start up KIDS

> Start up the Kernel Installation and Distribution System Menu

> \[XPD MAIN\]

> Edits and Distribution ...

> Utilities ...

> Installation ...

Select Kernel Installation & Distribution System Option: INStallation

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

3.  Select Installation Option

> NOTE: The following are OPTIONAL - (When prompted for the INSTALL NAME, enter XU\*8.0\*548):

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  Select Installation Option: Install Package(s)

> This is the step to start the installation of this KIDS patch:

1.  Choose the Install Package(s) option to start the patch install.
2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO/',answer NO

### Post-Installation Consideration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these instructions is to make sure that your system is configured properly for this NPI Crosswalk Extract so that it will run every time the CBO requests it via the NPI Administration web site.

The Chief Business Office schedules an NPI Crosswalk Extract report periodically (typically once a month) from all Veteran's Administration provider sites. The scheduling of this report is done via the VA NPI Crosswalk Extract Administration web site using HL7 messages. The NPI Crosswalk Extract process is automated and runs in the background at each site.

Once the NPI Crosswalk Extract has been requested by the VA NPI Crosswalk Extract Administration web site, each site responds with an acknowledgement that it has received the request. When the extract is actually scheduled in TaskMan, a second acknowledgement message is sent to the web site stating that the report has actually been scheduled. This same process occurs when the VA NPI Crosswalk Extract Administration web site cancels the extract.

Finally, once the NPI Crosswalk has been run, three final messages are sent. The first message is an acknowledgement to the web site that the extract was indeed run. The second message, which is sent via MailMan, is a summary message about the extract. The final message, also sent via MailMan, is the actual NPI Crosswalk Extract.

For this process to work correctly several requirements must be met:

1.  The NPI EXTRACT VERIFICATION mail group must be defined and correctly configured. The most common problem is that the REMOTE MEMBER address is not present or is incorrectly typed. The correct configuration is:

NPI EXTRACT VERIFICATION

TYPE: public ALLOW SELF ENROLLMENT: NO

REFERENCE COUNT: 65 LAST REFERENCED: JUN 01, 2010

RESTRICTIONS: UNRESTRICTED

MEMBER: XXXXX,XXXXXX

DESCRIPTION: Members of this mail group will automatically receive an

email verification entry for each NPI Extract file that has been generated

at the sites.

ORGANIZER: POSTMASTER

REMOTE MEMBER: REDACTED

> The remote member MUST be entered exactly as shown above.

> Common mistake: The remote member is NOT entered into the system correctly. It usually misspelled or not defined.

2.  The REDACTED domain must exist and defined as:

Select DOMAIN NAME: REDACTED

NUMBER: 579 NAME: REDACTED

FLAGS: S RELAY DOMAIN: REDACTED

DHCP ROUTING INDICATOR: NPS DISABLE TURN COMMAND: YES

LEVEL 1 NAME (c): GOV LEVEL 2 NAME (c): VA.GOV

LEVEL 3 NAME (c): REDACTED LEVEL 4 NAME (cREDACTED

3.  The logical link NPI OUT must exist and be configured as follows:

Select HL LOGICAL LINK NODE: NPI OUT

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// Y (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// BOTH Computed Fields and Record

Number

(IEN)

LLP TYPE: TCP AUTOSTART: Enabled

QUEUE SIZE: 10 RE-TRANSMISSION ATTEMPTS: 3

READ TIMEOUT: 27 ACK TIMEOUT: 270

TCP/IP ADDRESS: 00.00.00.00 TCP/IP PORT: 8090

TCP/IP SERVICE TYPE: CLIENT (SENDER) PERSISTENT: NO

RETENTION: 50 SAY HELO: NO

> **NOTE:** the IP address MUST be populated and the AUTOSTART field MUST be enabled. The IP address shown is NOT a valid IP address for your site. It should point to your local VIE. If you’re not sure of your sites VIE IP address please contact the VIE NATIONAL ADMIN Exchange mail group.

Common mistake: This HL LOGIGAL LINK must have AUTOSTART set to "Enabled”.

# Release Changes and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch contains enhancements and modifications relating to the XUS NPI EXTRACT REPORT \[XUS NPI EXTRACT\] option which is already loaded at the sites. The changes contained in this patch address the following:

1.  Create logic to pull the Organization Name and Pay-To Address that appear in the Pay-To Provider loop on X12 claims as viewed from the local facility VistA option "MCCR Site Parameter Display/Edit".
2.  Create a field in NPI individual extract data to house the primary taxonomy code. The primary taxonomy code should no longer appear in the current taxonomy code field. The taxonomy code field should carry the practitioner's other taxonomy codes, if they have any.
3.  Create a field in the NPI individual extract data to house the practitioner's current status and a second field for the date on which that status began.

# SUPPORT INFORMATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing, these patches will be supported by the Office of Enterprise Development, the development team. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any issues that arrive related to these patches. At the end of this 30 day period, assistance with issues related to these patches will be addressed through the Help Desk and the submittal of Remedy tickets if needed.

An existing ICR 4964 was modified as part of this patch. For further information please refer to FORUM