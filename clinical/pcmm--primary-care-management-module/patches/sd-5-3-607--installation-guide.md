---
title: SD*5.3*607 Installation Guide Patch
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Patch
app_code: PCMM
app_name: Primary Care Management Module
section: CLI
app_status: active
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*607
group_key: "PCMM:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: This guide provides details on the preparation for and installation of Patch SD\5.3\607 to the PCMM software. It includes instructions on the installation of the Client software (PCMM GUI).
audience: 
keywords: 
  - pcmm
  - installation
  - table
  - contents
  - shortcut
  - patch
  - parameters
  - windows
  - files
  - directory
page_count: 0
word_count: 533
section_count: 3
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_607ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_607ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=95"
---

![](sd-5-3-607-installation-guide-patch/001.png)

Scheduling V. 5.3

Primary Care Management Module

(PCMM)

Installation Guide

Patch SD\*5.3\*607

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [Introduction](#introduction)
- [Pre Installation](#pre-installation)
- [Installation Activities](#installation-activities)
  - [Manual Installation Steps](#manual-installation-steps)
  - [Configure Run-Time Parameters](#configure-run-time-parameters)
| Date   | Version | Description                   | Author                             |
|--------|---------|-------------------------------|------------------------------------|
| 1/2014 | 1.00    | Baseline first published copy | <span class="mark">REDACTED</span> |
|        |         |                               |                                    |
|        |         |                               |                                    |
|        |         |                               |                                    |

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides details on the preparation for and installation of Patch SD\*5.3\*607 to the PCMM software. It includes instructions on the installation of the Client software (PCMM GUI).

This patch provides updates to the PCMM GUI only. There are no changes to any V*IST*A applications.

# Pre Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The workstation must have one of the following operating systems.

- MS Windows XP
- MS Windows 7

Each workstation should be networked into your V*IST*A Server through a local area network. The RPC Broker’s RPC Broker Test should have successfully run on each client workstation.

Windows 7 workstation must have the following Windows Update installed:

- Windows Update KB917607

Minimum screen resolution for optimal use is 1280 x 800. Resolutions below this will cause some parts of PCMM to not be visible.

# Installation Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Manual Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  EXTRACT THE FILES: Once you receive the PCMM_GUI_1_3_0_28.zip file, save it to your hard drive in a directory of your choice (for example C:\Users\XXXXXXXX\Documents\PCMM_607). Then double click on the PCMM_GUI_1_3_0_28.zip file and extract the files to the directory you would like the PCMM GUI to be run from.
2.  VALIDATE FILES: Check to make sure you have the following files in the directory/folder listed above: PCMM.exe, PCMM.hlp, SD_53_607IG.doc, SD_53_607IG.pdf, and PCMM.GID. PCMM.exe, PCMM.GID, and PCMM.hlp must be located in the same directory in order for the PCMM Help File to load properly.
3.  CREATE A SHORTCUT: Once the files are unzipped (extracted), go to that directory and right click the mouse on the executable (PCMM.exe) file, and click Create Shortcut. Drag that shortcut to your desktop.

## Configure Run-Time Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  ENTER THE RUN-TIME PARAMETERS IN THE SHORTCUT: Right-click on the PCMM shortcut, and click Properties. In the “Target” box it will have the location of the PCMM.exe (for example C:\Users\XXXXXX\Documents \PCMM_607\PCMM.exe). Click the mouse in the empty space after C:\Users\XXXXXX\Documents \PCMM_607\PCMM.exe and press the space bar to add a space after the C:\Users\XXXXXX\Documents \PCMM-607\PCMM.exe and then enter s= then the IP address, a space and then p= followed by the port you are connecting to. For example, the Target area of the shortcut should look like the following:

C:\Users\XXXXXX\Documents\PCMM_607\PCMM.exe s=10.4.229.50 p=9573

![](sd-5-3-607-installation-guide-patch/002.png)

4.  SAVE THE SHORTCUT PARAMETERS: Click OK to save the shortcut settings.
5.  RUN PCMM GUI USING THE SHORTCUT: Double click the shortcut to run the PCMM GUI and verify connection to server.