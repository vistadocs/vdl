---
title: CMOP Version 2 Installation Guide for Controlled Substance Prescriptions
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: for Controlled Substance Prescriptions
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this document is to provide installation instructions for the four patches that comprise the Consolidated Mail Outpatient Pharmacy (CMOP) Controlled Substance Rxs project. These patches include Controlled Substances (PSD\3\21), Outpatient Pharmacy (PSO\7\33), Consolidated Mail Outpati
audience: 
keywords: 
  - install
  - cmop
  - controlled
  - installation
  - substance
  - outpatient
  - pharmacy
  - distribution
  - table
  - contents
page_count: 0
word_count: 3782
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/cmop_cs_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/cmop_cs_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

![](cmop-version-2-installation-guide-for-controlled-substance-prescriptions/001.png)

CMOP CONTROLLED SUBSTANCE RXSINSTALLATION GUIDE

(Revised)

May 2000

V*IST*A Technical Services

Table of Contents

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide installation instructions for the four patches that comprise the Consolidated Mail Outpatient Pharmacy (CMOP) Controlled Substance Rxs project. These patches include Controlled Substances (PSD\*3\*21), Outpatient Pharmacy (PSO\*7\*33), Consolidated Mail Outpatient Pharmacy (PSX\*2\*23), and Pharmacy Data Management (PSS\*1\*28).

> **NOTE:** If you are not using Consolidated Mail Outpatient Pharmacy V. 2.0, or will not be sending Controlled Substance prescriptions to the CMOP facility for processing, the patches to Outpatient Pharmacy, Controlled Substances, and Pharmacy Data Management must still be installed. The Installation of CMOP Controlled Substance Rxs Patches section of this manual will provide additional instructions for this situation.

The intended audience for this document is the Medical Center staff responsible for installation of the patches and set up of the site parameter used for suspense as described in the Post- Installation instructions section of this document.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The CMOP software establishes an interface for the electronic transfer of prescription data between the Department of Veterans Affair’s (VA’s) remote facilities (Medical Centers and outpatient clinics) and the Consolidated Mail Outpatient Pharmacy (CMOP) Host system. This is an integrated and highly automated outpatient prescription dispensing system. The CMOP Controlled Substance Rxs enhancements provide the ability to allow the electronic transmission of controlled substance prescriptions to CMOPs, provide tracking reports at remote facilities, and ensure that controlled substance inventories at remote facilities are not affected if prescriptions are filled at the CMOP. Modifications to the CMOP software will allow prescriptions written for schedule III-V controlled substances to be electronically transmitted via a separate batch transmission from the remote facility to the CMOP Host facility. Tracking reports will be modified to differentiate controlled from non-controlled prescriptions.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Drug Enforcement Agency (DEA) has granted the Veterans Health Administration (VHA) a waiver to conduct an approved trial of the dispensing of controlled substances (Schedule III – V) by VA CMOPs. A controlled substance is defined as a drug or other substance, or immediate precursor, included in Schedules I-V, that requires special handling due to dispensing restrictions. Schedule designation is based on the drug or substance’s potential for abuse, accepted medical use in treatment in the United States, and the extent of psychological or physical dependence of the drug if abused. More restrictive and abuse-potential drugs carry a lower schedule. Currently all controlled substance prescriptions are filled locally at each Department of Veterans Affairs Medical Center (VAMC) or outpatient clinic.

# # Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Purpose](#purpose)
  - [Scope](#scope)
  - [The CMOP software establishes an interface for the electronic transfer of prescription data between the Department of Veterans Affair’s (VA’s) remote facilities (Medical Centers and outpatient clinics) and the Consolidated Mail Outpatient Pharmacy (CMOP) Host system. This is an integrated and highly automated outpatient prescription dispensing system. The CMOP Controlled Substance Rxs enhancements provide the ability to allow the electronic transmission of controlled substance prescriptions to CMOPs, provide tracking reports at remote facilities, and ensure that controlled substance inventories at remote facilities are not affected if prescriptions are filled at the CMOP. Modifications to the CMOP software will allow prescriptions written for schedule III-V controlled substances to be electronically transmitted via a separate batch transmission from the remote facility to the CMOP Host facility. Tracking reports will be modified to differentiate controlled from non-controlled prescriptions.](#the-cmop-software-establishes-an-interface-for-the-electronic-transfer-of-prescription-data-between-the-department-of-veterans-affairs-vas-remote-facilities-medical-centers-and-outpatient-clinics-and-the-consolidated-mail-outpatient-pharmacy-cmop-host-system-this-is-an-integrated-and-highly-automated-outpatient-prescription-dispensing-system-the-cmop-controlled-substance-rxs-enhancements-provide-the-ability-to-allow-the-electronic-transmission-of-controlled-substance-prescriptions-to-cmops-provide-tracking-reports-at-remote-facilities-and-ensure-that-controlled-substance-inventories-at-remote-facilities-are-not-affected-if-prescriptions-are-filled-at-the-cmop-modifications-to-the-cmop-software-will-allow-prescriptions-written-for-schedule-iii-v-controlled-substances-to-be-electronically-transmitted-via-a-separate-batch-transmission-from-the-remote-facility-to-the-cmop-host-facility-tracking-reports-will-be-modified-to-differentiate-controlled-from-non-controlled-prescriptions)
- [# Release Notes](#release-notes)
- [Consolidated Mail Outpatient Pharmacy V. 2.0](#consolidated-mail-outpatient-pharmacy-v-20)
- [Controlled Substances V. 3.0](#controlled-substances-v-30)
- [Outpatient Pharmacy V. 7.0](#outpatient-pharmacy-v-70)
  - [## ## Pharmacy Data Management V. 1.0](#pharmacy-data-management-v-10)
- [Pre-Installation](#pre-installation)
- [Installation of CMOP Controlled Substance Rxs Patches](#installation-of-cmop-controlled-substance-rxs-patches)
- [# After installing the CMOP Controlled Substance Rxs patches, you will need to coordinate the marking of drugs with your CMOP Host facility.](#after-installing-the-cmop-controlled-substance-rxs-patches-you-will-need-to-coordinate-the-marking-of-drugs-with-your-cmop-host-facility)
- [# The CMOP Controlled Substance Rxs enhancements require the installation of four patches. All patches can be installed while users are on the system. Installation of each patch will take less than one minute. Please read each patch installation section thoroughly before beginning the installation.](#the-cmop-controlled-substance-rxs-enhancements-require-the-installation-of-four-patches-all-patches-can-be-installed-while-users-are-on-the-system-installation-of-each-patch-will-take-less-than-one-minute-please-read-each-patch-installation-section-thoroughly-before-beginning-the-installation)
  - [Step 1: Installation of Controlled Substance Patch PSD\3\21](#step-1-installation-of-controlled-substance-patch-psd321)
The CMOP Controlled Substance Rxs release contains enhancements to several products. Each enhancement is briefly described in this section.

# Consolidated Mail Outpatient Pharmacy V. 2.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The *CMOP Mark/Unmark (Single drug)* option and the routine PSXMARK is deleted. The same functionality exists in Pharmacy Data Management software.
- Several CMOP report options are modified so as not to screen out drugs identified as schedule III-V controlled substances.
- The *Report of Unreleased Rxs* option has been modified to sort by controlled substance prescriptions, non-controlled substance prescriptions, or both. The drug name and the order number will also be added to the report.
- A separate transmission has been created for controlled substance prescriptions sent to the CMOP Host facility for filling.
- A separate auto transmission for controlled substance prescriptions has been created.
- The *Rx Inquiry* option was modified to display the CARRIER (#17), PACKAGE ID (#18) and CONTROLLED SUBS FLAG (#19) fields in the CMOP MASTER DATABASE file (#552.4).

# Controlled Substances V. 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The *Outpatient Rx’s* option is modified to prevent the posting and releasing of a controlled substance if the CMOP status is transmitted, dispensed or retransmitted. Controlled substance prescriptions with the status of “Not dispensed” shall be releasable.

# Outpatient Pharmacy V. 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A new report, *Controlled Substance Rx Dispensing Report*, has been created. This report prints out a log of Schedule III-V controlled substance prescriptions that have been filled at a Host CMOP facility. It can be sorted by division, and then by release date or drug. The report displays patient information as well as prescription information such as number, drug name, quantity, release date, fill/refill number, CMOP facility dispensed from, and CMOP status of the fill/refill.
- The *Released/Unreleased Report* option is modified to sort by controlled substance prescriptions, non-controlled substance prescriptions, or both.
- The *View Prescription* option was modified to display the CARRIER (#10) and PACKAGE ID (#11) fields in the CMOP EVENT multiple of the PRESCRIPTION file (#52).
- An additional parameter was created for the controlled substance data transmissions in the OUTPATIENT PHARMACY SITE file (#59). This field shall designate the number of days before the fill date that a controlled substance prescription can be pulled from the RX SUSPENSE file (#52.5).

## ## ## Pharmacy Data Management V. 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The *CMOP Mark/Unmark (Single drug)* option has been modified to remove the screen that disallows a drug identified as a Schedule III-V controlled substance to be marked for CMOP transmission.
- The *Drug Enter/Edit* option is modified to remove the screen that disallows a drug identified as a Schedule III-V controlled substance to be marked for CMOP transmission.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Patch Requirements 

The CMOP - Controlled Substance Rxs enhancement is made up of four patches. They are PSD\*3\*21, PSO\*7\*33, PSX\*2\*23, and PSS\*1\*28. The patches should be installed in the order presented in this manual. Prior to installation of the four patches listed above, the following patches must be installed to Controlled Substances, CMOP, Outpatient Pharmacy, and Pharmacy Data Management:

- PSD\*3\*15
- PSO\*7\*9
- PSO\*7\*32 \*
- PSS\*1\*20
- PSS\*1\*22
- PSX\*2\*24

\* Because the CMOP Host facilities do not use the Outpatient Pharmacy software, this patch is required only when installing at a medical center. The Kernel Installation & Distribution System (KIDS) will display a warning message that PSO\*7\*32 is required when the CMOP Patch PSX\*2\*23 is installed at a Host facility. This message can be ignored.

> NOTE: If you are not running CMOP V. 2.0, patch PSX\*2\*24 does not need to be installed.

<u>  
</u>

# Installation of CMOP Controlled Substance Rxs Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # After installing the CMOP Controlled Substance Rxs patches, you will need to coordinate the marking of drugs with your CMOP Host facility.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # The CMOP Controlled Substance Rxs enhancements require the installation of four patches. All patches can be installed while users are on the system. Installation of each patch will take less than one minute. Please read each patch installation section thoroughly before beginning the installation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patches should be installed in the following order:

1.  Controlled Substances (PSD\*3\*21)
2.  Outpatient Pharmacy (PSO\*7\*33)
3.  Consolidated Mail Outpatient Pharmacy (PSX\*2\*23)
4.  Pharmacy Data Management (PSS\*1\*28)

> **NOTE:** If you are not running CMOP V. 2.0, you should skip the installation of the patch PSX\*2\*23 and install the patches for the three other software products.

<u>  
</u>

## Step 1: Installation of Controlled Substance Patch PSD\*3\*21

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc472127766" class="anchor"></span>1. Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.

2\. Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu to install each patch.

3\. From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.

4\. From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter PSD\*3.0\*21):

> a\. *Backup a Transport Global* - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes, such as DDs or templates.

b\. *Compare Transport Global to Current System* - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. *Verify Checksums in Transport Global* - this option will ensure the integrity of the routines that are in the transport global.

5.  Use the *Install Package(s)* option and select the package PSD\*3.0\*21.
6.  When prompted, “Want KIDS to INHIBIT LOGONs during the install? YES//” respond <u>NO</u>.
7.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” respond <u>NO</u>.
8.  After installing all patches, any routines that were unmapped as part of step 2 should be returned to the mapped set once the last installation has run to completion.

<u>Example of Install</u>

Select Kernel Installation & Distribution System Option: <u>Inst</u>allation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: <u>INSTALL</u> Package(s)

Select INSTALL NAME: <u>PSD\*3.0\*21</u> Loaded from Distribution 2/29/00@14:18:11

=\> PSD\*3\*21

This Distribution was loaded on Feb 29, 2000@14:18:11 with header of

PSD\*3\*21

It consisted of the following Install(s):

PSD\*3.0\*21

Checking Install for Package PSD\*3.0\*21

Install Questions for PSD\*3.0\*21

Want KIDS to INHIBIT LOGONs during the install? YES// <u>NO</u>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>NO</u>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// <u>\<RET\></u>

PSD\*3.0\*21

────────────────────────────────────────────────────────────────────────────────

Install Started for PSD\*3.0\*21 :

Feb 29, 2000@14:22:06

Build Distribution Date: Sep 04, 1999

Installing Routines:

Feb 29, 2000@14:22:06

Updating Routine file...

Updating KIDS files...

PSD\*3.0\*21 Installed.

Feb 29, 2000@14:22:06

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

Step 2: Installation of Outpatient Pharmacy Patch PSO\*7\*33<span id="_Toc472127767" class="anchor"></span>

1\. Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.

2.  Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu to install each patch.

3\. From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.

4\. From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter PSO\*7.0\*33):

> a\. *Backup a Transport Global* - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.

> b\. *Compare Transport Global to Current System* - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. *Verify Checksums in Transport Global* - this option will ensure the integrity of the routines that are in the transport global.

5.  Use the *Install Package(s)* option and select the package PSO\*7.0\*33.
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//” respond <u>NO</u>.
7.  When prompted, “Want KIDS to INHIBIT LOGONs during the install? YES//” respond <u>NO</u>.
8.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” respond <u>NO</u>.
9.  After installing all patches, any routines that were unmapped as part of step 2 should be returned to the mapped set once the last installation has run to completion.

Example of Install

Select Kernel Installation & Distribution System Option: <u>Inst</u>allation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: <u>INSTALL</u> Package(s)

Select INSTALL NAME: <u>PSO\*7.0\*33</u> Loaded from Distribution 12/15/99@14:04:0

9

=\> PSO\*7\*33

This Distribution was loaded on Dec 15, 1999@14:04:09 with header of

PSO\*7\*33

It consisted of the following Install(s):

PSO\*7.0\*33

Checking Install for Package PSO\*7.0\*33

Install Questions for PSO\*7.0\*33

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// <u>NO</u>

Want KIDS to INHIBIT LOGONs during the install? YES// <u>NO</u>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>NO</u>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// <u>\<RET\></u>

Install Started for PSO\*7.0\*33 :

Dec 15, 1999@14:06:13

Build Distribution Date: Dec 08, 1999

Installing Routines:

Dec 15, 1999@14:06:13

Installing PACKAGE COMPONENTS:

Installing OPTION

Dec 15, 1999@14:06:14

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*33 Installed.

Dec 15, 1999@14:06:15

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

Step 3: Installation of CMOP Patch PSX\*2\*23<span id="_Toc472127768" class="anchor"></span>

> **NOTE:** If you are not running CMOP V. 2.0, you should skip the installation of the patch PSX\*2\*23 and proceed to step 4, “Installation of Pharmacy Data Management Patch PSS\*1\*28”.

When installing PSX\*2\*23, a Data Dictionary warning will be displayed at the Medical Centers and CMOP Host Facilities. At the Medical Center the warning will read “\*\*ERROR IN DATA DICTIONARY FOR FILE \#552.4\*\*. At the CMOP Host Facility, the warning will read “\*\*ERROR IN DATA DICTIONARY FOR FILE \#550\*\*”. Both warnings can be ignored. They are an anomaly due to having one patch for both the Medical Center and CMOP Host Facility installations.

PSX\*2\*23 was designed to install differently at the Consolidated Mail Outpatient Pharmacy host facilities than at the VA Medical Centers. When running ^XINDEX on the build, PSX\*2.0\*23, a warning "File \# 552.41 is missing !" will be displayed at the VA Medical Centers. Similarly, the CMOP host facilities will see the warning that "File \# 550.09 is missing !" File \#552.4 only resides at the Consolidated Mail Outpatient Pharmacy host facilities and file \#550 only resides at the VA Medical Centers. The warnings are appropriate and can be ignored.

The Post-Installation routine PSXPOST1 is deleted upon completion of the Installation.

1\. Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.

2\. Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu to install this patch.

3\. Before installing this patch, use the TaskMan option *List Tasks* \[XUTM INQ\] to list currently running tasks. DO NOT install this patch if any PSX namespaced tasks are running.

4\. From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.

5\. Use the *Load a Distribution* option and load the PSX\*2.0\*23 software distribution file.

6\. From this menu, you may select to use the following options:

> a\. *Backup a Transport Global* - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.

> b\. *Compare Transport Global to Current System* - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

3.  *Verify Checksums in Transport Global* - this option will ensure the integrity of the routines that are in the transport global.
    7.  Use the *Install Package(s)* option and select the package PSX\*2.0\*23.
    8.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//” respond <u>NO</u>.
    9.  When prompted “Want KIDS to INHIBIT LOGONs during the install? YES//” respond <u>NO.</u>
    10. When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” respond <u>NO</u>.
    11. After installing all patches, any routines that were unmapped as part of step 2 should be returned to the mapped set once the last installation has run to completion.

Example of Install

Select Kernel Installation & Distribution System Option: <u>Inst</u>allation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: <u>INSTALL</u> Package(s)

Select INSTALL NAME: <u>PSX\*2.0\*23</u> Loaded from Distribution 4/11/00@09:23:44

=\> PSX\*2\*23

This Distribution was loaded on Apr 11, 2000@09:23:44 with header of

PSX\*2\*23

It consisted of the following Install(s):

PSX\*2.0\*23

Checking Install for Package PSX\*2.0\*23

Install Questions for PSX\*2.0\*23

Incoming Files:

550 CMOP SYSTEM (Partial Definition)

> **NOTE:** You already have the 'CMOP SYSTEM' File. <u>MEDICAL CENTER INSTALL</u>

552.4 CMOP MASTER DATABASE (Partial Definition) <u>HOST CMOP INSTALL</u>

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//<u>\<RET\></u>

Want KIDS to INHIBIT LOGONs during the install? YES// <u>NO</u>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>NO</u>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//<u>\<RET\></u>

Install Started for PSX\*2.0\*23 :

Apr 11, 2000@09:25:10

Build Distribution Date: Apr 10, 2000

Installing Routines:

Apr 11, 2000@09:25:10

Installing Data Dictionaries:

\*\* ERROR IN DATA DICTIONARY FOR FILE \# 552.4 \*\*

Data Dictionary not installed; Partial DD/File does not exist. <u>MEDICAL CENTER INSTALL</u>

Apr 11, 2000@09:25:11

\*\* ERROR IN DATA DICTIONARY FOR FILE \# 550 \*\*

Data Dictionary not installed; Partial DD/File does not exist. <u>HOST CMOP INSTALL</u>

Apr 11, 2000@09:25:11

Installing PACKAGE COMPONENTS:

Installing OPTION

Apr 11, 2000@09:25:11

Running Post-Install Routine: ^PSXPOST1

PSX\*2.0\*23

--------------------------------------------------------------------------------

> **NOTE:** This routine will be deleted from your system after running to completion.

The Medical Center installation is now REMOVING host options and files.

Remember to configure the DAYS TO PULL SUSPENDED CS CMOP parameter.

Remember to run the Setup CS Auto-transmission option \[PSXR AUTO TRANSMIT CS\].

Both procedures are described in the Post-Installation section of the CMOP CS

Installation Guide.

Done.

Updating Routine file...

Updating KIDS files...

PSX\*2.0\*23 Installed.

Apr 11, 2000@09:25:12

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

Step 4: Installation of Pharmacy Data Management Patch PSS\*1\*28<span id="_Toc472127769" class="anchor"></span>

> **NOTE:** If you are running CMOP V 2.0, you must have CMOP patch PSX\*2\*23 installed before you can install this patch.

1\. Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.

2\. Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu to install each patch.

3\. From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.

4\. From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter PSS\*1.0\*28):

> a\. *Backup a Transport Global* - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.

> b\. *Compare Transport Global to Current System* - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. *Verify Checksums in Transport Global* - this option will ensure the integrity of the routines that are in the transport global.

5.  Use the *Install Package(s)* option and select the package PSS\*1.0\*28.
6.  When prompted “Want KIDS to INHIBIT LOGONs during the install? YES//” respond <u>NO</u>.
7.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” respond <u>NO</u>.
8.  After installing all patches, any routines that were unmapped as part of step 2 should be returned to the mapped set once the last installation has run to completion.

Example of Install

Select Kernel Installation & Distribution System Option: <u>Inst</u>allation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: <u>INSTALL</u> Package(s)

Select INSTALL NAME: <u>PSS\*1.0\*28</u> Loaded from Distribution 12/14/99@17:24:

43

=\> PSS\*1\*28

This Distribution was loaded on Dec 14, 1999@17:24:43 with header of

PSS\*1\*28

It consisted of the following Install(s):

PSS\*1.0\*28

Checking Install for Package PSS\*1.0\*28

Will first run the Environment Check Routine, PSSCMOPE

Install Questions for PSS\*1.0\*28

Want KIDS to INHIBIT LOGONs during the install? YES// <u>NO</u>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>NO</u>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// <u>\<RET\></u>

PSS\*1.0\*28

────────────────────────────────────────────────────────────────────────────────

Install Started for PSS\*1.0\*28 :

Dec 14, 1999@17:25:17

Build Distribution Date: Sep 30, 1997

Installing Routines:

Dec 14, 1999@17:25:18

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*28 Installed.

Dec 14, 1999@17:25:18

Install Message sent \#152212

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

Post-Installation<span id="_Toc472127770" class="anchor"></span>

After installing the CMOP Controlled Substance Rxs patches, you will need to coordinate the marking of drugs with your CMOP Host facility.

A new parameter, DAYS TO PULL SUSPENDED CS CMOP, has been added to control the days to pull ahead for the controlled substances transmissions. This parameter works exactly like the parameter, DAYS TO PULL FROM SUSPENSE, already contained in Outpatient Pharmacy V. 7.0. The default value for this parameter is zero. The new parameter is accessed through the *Site Parameter Enter/Edit* option found within the *Outpatient Pharmacy Supervisor Functions* menu.

EXAMPLE:

Select Outpatient Pharmacy Manager Option: <u>SUP</u>ervisor Functions

Select Supervisor Functions Option: <u>SITE</u> Parameter Enter/Edit

Select SITE NAME: <u>BIRMINGHAM</u>

Would you like to see all site parameters for this division? Y// <u>NO</u>

NAME: BIRMINGHAM//<u>^DAYS TO PULL SUSPENDED CS CMOP</u>

DAYS TO PULL SUSPENDED CS CMOP: 0// <u>7</u>

A new option, Setup CS Auto-transmission \[PSXR AUTO TRANSMIT CS\] has been added to the Transmission Menu (PSXR TRANSMIT MENU). This option is used to schedule automatic CS transmissions. The option works exactly like the Setup Auto-transmission \[PSXR AUTO TRANSMIT\] that is currently used to transmit non-CS Rxs to the CMOP host facility.

EXAMPLE:

Select OPTION NAME: <u>PSXR TRANSMIT MENU</u> Transmission Menu

Select Transmission Menu Option: <u>PSXR AUTO TRANSMIT CS</u>

Enter the date to start automatic controlled subs processing: NOW// <u>RTN</u> (MAR 25,

2000@12:46)

Number of days to transmit thru: (0-10): 0// <u>7</u>

Enter rescheduling frequency (hours) transmission: (1-96): <u>24</u>

Begin CS Automatic Transmissions : MAR 27, 2000@12:46

Rescheduling Frequency : 24 hours

Number of days to transmit through : 7

Is this correct? NO// <u>YES</u>

To initialize the automatic transmissions for controlled substances to the CMOP Host facility, access the *SETUP CS AUTO Transmission* option described in the following example. This option works exactly like the standard *SETUP AUTO Transmission* option that is already in place. Enter the desired date to start the transmissions, how many days of data each transmission should span and how often the transmissions are to take place.

EXAMPLE:

Select OPTION NAME: <u>PSXR TRANSMIT MENU</u> Transmission Menu

Select Transmission Menu Option: <u>SETUP CS AUTO-transmission</u>

Enter the date to start automatic controlled subs processing: NOW//<u>(MAY 1, 2000@12:42)</u>

Number of days to transmit thru: (0-10): 0// <u>7</u>

Enter rescheduling frequency (hours) transmission: (1-96): <u>24</u>

Begin CS Automatic Transmissions : MAY 1, 2000@12:42

Rescheduling Frequency : 24 hours

Number of days to transmit through : 7

Is this correct? NO// <u>YES</u>

Select Transmission Menu Option: