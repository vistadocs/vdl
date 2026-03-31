---
title: PSO*7*367 VistA FDA Medication Guides Project Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: VistA FDA Medication Guides Project
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*367
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - guide
  - medication
  - pharmacy
  - outpatient
  - table
  - contents
  - updates
  - cmop
  - printer
  - prescription
page_count: 0
word_count: 962
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/phar_fda_med_guide_rel3_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/phar_fda_med_guide_rel3_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

![](pso-7-367-vista-fda-medication-guides-project-release-notes/001.png)

FDA Medication Guides Project

Release Notes

XU\*8\*566

PSN\*4\*264

PSO\*7\*367

PSX\*2\*70

March 2012

Product Development
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Project Enhancements](#project-enhancements)
  - [# Outpatient Pharmacy, Consolidated Mail Outpatient Pharmacy (CMOP), National Drug File (NDF) and Kernel Updates](#outpatient-pharmacy-consolidated-mail-outpatient-pharmacy-cmop-national-drug-file-ndf-and-kernel-updates)
  - [Outpatient Pharmacy](#outpatient-pharmacy)
  - [Consolidated Mail Outpatient Pharmacy (CMOP)](#consolidated-mail-outpatient-pharmacy-cmop)
  - [National Drug File (NDF)](#national-drug-file-ndf)
  - [Kernel](#kernel)
The National Drug File (NDF) module provides standardized drug information for all Department of Veterans Affairs Medical Centers (VAMCs). The Outpatient Pharmacy package provides a way to manage the medication regimen of veterans seen in outpatient clinics and to monitor and manage the workload and costs in the Outpatient Pharmacy. The Consolidated Mail Outpatient Pharmacy (CMOP) package provides a regional system resource to expedite the distribution of mail-out prescriptions to veteran patients
The Outpatient Pharmacy application was modified to allow for automatic printing of FDA Medication Guides on a separate, designated printer along with the prescription label and PMI sheet, if one is available for the medication being dispensed. Outpatient Pharmacy was also modified to provide the option to reprint an FDA Medication Guide when reprinting a prescription label, to create and maintain a list of FDA Medication Guide printers for a specific pharmacy division and to change the FDA Medication Guide printer at any point of the dispensing process.
Changes were made to the Consolidated Mail Outpatient Pharmacy activity log to show which specific FDA Medication Guide was available when the prescription fill was transmitted to CMOP.

## Project Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software provides the following enhancements:

- Automatic printing of the FDA Medication Guide along with prescription labels on designated FDA Medication Guide printers without any direct user interaction.
- Ability to enable or disable the automatic printing of the FDA Medication Guide by pharmacy division.
- Ability to reprint the FDA Medication Guide when reprinting a prescription label.
- Ability to reprint the FDA Medication Guide for any given prescription fill or the latest FDA Medication Guide available for the medication on the prescription.
- Display on the prescription label that an FDA Medication Guide is available, and if printed, needs to accompany the documentation before being given to the patient.
- Ability to change the FDA Medication Guide printer at any point of the dispensing process, similar to changing the label printer.
- Ability to create and maintain a list of FDA Medication Guide printers for a specific pharmacy division.
- Changes to the prescription label activity logs showing which specific FDA Medication Guide document was active at the time the Rx was printed either locally or CMOP. The recording of the FDA Medication guide in the activity log does not prove that the document was printed along with the label.

*(This page included for two-sided copying.)*

## # Outpatient Pharmacy, Consolidated Mail Outpatient Pharmacy (CMOP), National Drug File (NDF) and Kernel Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the changes made to the Outpatient Pharmacy, Consolidated Mail Outpatient Pharmacy (CMOP), NDF and Kernel packages for the automatic printing of the Food and Drug Administration (FDA) Medication Guide for the Veterans Health Information Systems and Technology Architecture (VistA).

## Outpatient Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

############################### File Updates

The following new sub-file was added to the OUTPATIENT SITE file (#59) to store the list of printers available for printing FDA Medication Guide for the division.

- FDA MED GUIDE PRINTER (#135)

############################### Field Updates

The following new field was added to the DEVICE file (#3.5) to store the Windows network name of the FDA Medication Guide printers:

- WINDOWS NETWORK PRINTER NAME (#75)

The following new fields were added to the new sub-file FDA MED GUIDE PRINTER (#135)

- FDA MED GUIDE PRINTER (#.01)
- DEFAULT PRINTER (#.02)

The following new field was added to the OUPATIENT SITE file (#59)

- FDA MED GUIDE PRINT SERVER URL (#134)

The following new field was added to the PRESCRIPTION file (#52), LABEL DATE/TIME sub-file (#52.032)

- FDA MED GUIDE FILENAME (#35)

The following new field was added to the PRESCRIPTION file (#52), CMOP EVENT sub-file (#52.01)

- FDA MED GUIDE FILENAME (#35)

###############################  Input Template Updates

The following template was modified to allow users to update FDA Medication Guide Printers and the address for the server where java is installed via the *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\] option.

- PSO SITE

############################### Protocol Updates

The following protocol was modified

- PSO LM HIDDEN OTHER \#2

The following new protocol was added

- PSO LM REPRINT FDA MED GUIDE

############################### Menu Option Updates

The following option was modified to include the editing of the new field, WINDOWS NETWORK PRINTER NAME.

- Edit All Device Fields option \[XUDEVEDITALL\]

############################### Routine Updates

The following new routine was added:

- PSOFDAUT

The following routines were modified:

- PSOB
- PSOBMST
- PSOEXRST
- PSOFDAMG
- PSOLBL
- PSOLBL1
- PSOLBL2
- PSOLBLN
- PSOLBLN1
- PSOLLL1
- PSOLLL4
- PSOLLL8
- PSOLLLI
- PSOLSET
- PSOORAL1
- PSORXL
- PSORXRP1
- PSORXRP2
- PSORXRPT
- PSORXVW1
- PSORXVW2
- PSOSULB1
- PSOSURST

## Consolidated Mail Outpatient Pharmacy (CMOP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

############################### Routine Updates

The following routines were modified:

- PSXRPPL
- PSXRSUS
- PSXRXU

## National Drug File (NDF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

############################### Field Updates

The following field in the VA PRODUCT file (#50.68) was updated to add a period after the help prompt, and the technical description was updated to indicate the location of the repository for FDA Medication Guides.

- FDA MED GUIDE (#100)

############################### Routine Updates

The following routine was modified:

- PSNFDAMG

## Kernel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

############################### File Updates

The following file was modified:

- DEVICE (#3.5)

############################### Field Updates

The following new field was added:

- WINDOWS NETWORK PRINTER NAME (#75)

############################### Routine Updates

The following routine was modified:

- XTHC10

*(This page included for two-sided copying.)*