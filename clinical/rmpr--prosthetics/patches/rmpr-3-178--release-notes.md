---
title: RMPR*3*178 Use of GIP in Prosthetics Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Use of GIP in Prosthetics
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*178
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - inventory
  - table
  - contents
  - rmpr
  - prosthetics
  - stock
  - release
  - patch
  - generic
  - dynamed
page_count: 0
word_count: 1300
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_178_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_178_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

Prosthetics

RMPR\*3\*178

Release Notes

![](rmpr-3-178-use-of-gip-in-prosthetics-release-notes/001.png)

October 2016

Office of Information and Technology (OI&T)

.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [New Features and Functions Added](#new-features-and-functions-added)
    - [New Option](#new-option)
    - [New Routine](#new-routine)
  - [Enhancements and Modifications to Existing Software](#enhancements-and-modifications-to-existing-software)
    - [Modified Routines](#modified-routines)
  - [Known Issues](#known-issues)
    - [New Service Requests Resolved](#new-service-requests-resolved)
- [Product Documentation](#product-documentation)
- [Installation Instructions](#installation-instructions)
- [Post Installation Instructions](#post-installation-instructions)
The Use of GIP in Prosthetics enhancement facilitates use of the Generic Inventory Package (GIP) functionality in VistA to track prosthetic inventory.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to communicate changes to the VistA system resulting from implementation of Prosthetics RMPR\*3.0\*178 and to provide instructions for installing the patch.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the Use of GIP in Prosthetics and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for the RMPR\*3\*178 release.

This enhancement is provided as a patch to VistA to configure the VistA system so that the Prosthetics Department can use the Generic Inventory Package (GIP) instead of the Prosthetic Inventory Package (PIP) to track prosthetics inventory.

VA sites that make the transition to GIP prosthetics tracking have the ability to suppress the posting of a prosthetic issuance in GIP, depending on whether the site is using a Point-Of-Use (POU) or other system outside of VistA to update the inventory.

Exception: Sites using DynaMed are required to continue to use Prosthetics Inventory Package and not transition prosthetics inventory to GIP until a solution is implemented that supports GIP and DynaMed.

> **NOTE:** This patch does NOT provide instructions to sites for transitioning inventory from PIP to GIP.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new features and functions added to the RMPR\*3\*178 release.

### New Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new option--Generic Inventory (GIP) Stock Issues--\[RMPR GIP STOCK\], provides the capability to issue prosthetics stock that is maintained by the IFCAP Generic Inventory Package (GIP). This option automatically updates inventory in IFCAP GIP. However, when the items issued are from an INVENTORY POINT that is linked to a Point of Use (POU) supply cabinet then this option does not update the inventory, since these are special cabinets that automatically update GIP inventory balances, via HL7 messaging, when stock is removed. This option also checks the DynaMed System Parameter flag to determine if the site is running DynaMed, and if so this option will abort. Sites using DynaMed should continue to use PIP until a solution is implemented for DynaMed and GIP.

The new RMPR GIP STOCK option is exported as a Menu Option on the Purchasing menu \[RMPR PURCHASING MENU\] which is descendent from both the RMPR CLERK menu and the RMPR OFFICIAL menu.

RMPR CLERK Prosthetic Clerk's Menu

Purchasing ... \[RMPR PURCHASING MENU\]

Generic Inventory (GIP) Stock Issues \[RMPR GIP STOCK\]

RMPR OFFICIAL Prosthetic Official's Menu

Purchasing ... \[RMPR PURCHASING MENU\]

Generic Inventory (GIP) Stock Issues \[RMPR GIP STOCK\]

### New Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new routine was created:

- RMPR178P

This post install routine checks for the existence of a PRGIP Site Parameter and removes it if it exists. Some sites may have been incorrectly instructed to add this parameter in order to support handling prosthetics inventory with the Generic Inventory Package.

## Enhancements and Modifications to Existing Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications in the Prosthetics RMPR\*3\*178 release.

### Modified Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines were modified:

- RMPRSTL

A new function was added to this routine that determines whether an inventory point is linked to an automated supply station (Point of Use Cabinet). This function is supported by DBIA with IFCAP (DBIA 6374 to read IFCAP GIP files). Additionally, logic is added to call existing DBIA to update GIP inventory when inventory point is not POU. When inventory point is POU inventory is not updated since this is done through HL7 messaging from the POU inventory functionality, when stock is removed.

- RMPRSTK

  Two new checks (DynaMed check and GIP Flag Check) were added to ensure appropriateness of using GIP for inventory. This routine is also the entry point for the new Generic Inventory (GIP) Stock Issues \[RMPR GIP STOCK\] option.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites using DynaMed can not use GIP for Prosthetics inventory at this time. The new Generic Inventory (GIP) Stock Issues \[RMPR GIP STOCK\] option checks to see if DynaMed is in use and, if so, aborts the option.

This patch does not provide instructions or processes to support the actual transition of inventory from the Prosthetics package to the Generic Inventory package (GIP)*.*

### New Service Requests Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following New Service Request was resolved with this patch:

- NSR20140206 – Use of GIP in Prosthetics

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- Prosthetics Basic User Manual, prostheticsbasicusermanual.pdf
- Release Notes, rmpr_3_178_rn.pdf

User documentation for Inpatient Medications V.5.0 provides detailed information on the functionality and can be found on the VistA Document Library (VDL).

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter RMPR\*3.0\*178.
1.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
2.  Print Transport Global - This option will allow you to view the components of the KIDS build.
3.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
4.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.

4\. From the Installation Menu, select the Install Package(s) option and choose the patch to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// Press \<Enter\>

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO// Press \<Enter\>

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// Press \<Enter\>

8\. When prompted "Enter options you wish to mark as 'Out of Order':", enter the following options:

> Prosthetic Clerk's Menu \[RMPR CLERK\]

> Prosthetic Official's Menu \[RMPR OFFICIAL\]

> Purchasing \[RMPR PURCHASING MENU\]

> Stock Issues \[RMPR STOCK ISS\]

9\. When prompted "Enter protocols you wish to mark as 'Out of Order':", press \<return\>.

10\. If prompted "Delay Install (Minutes): (0 - 60): 0//, respond 0.

# Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites currently running PIP for prosthetics inventory must coordinate the conversion to GIP for prosthetics inventory.

Sites using DynaMed cannot use GIP for Prosthetics inventory at this time.