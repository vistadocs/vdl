---
title: PXRM*2*30 Epilepsy Center Of Excellence (ECOE) Reminder Dialogs Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Epilepsy Center Of Excellence (ECOE) Reminder Dialogs
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*30
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: The VA-ECOE templates project is a product developed in collaboration with the VA Epilepsy Center of Excellence (ECOE), VHA Informatics Council (VHA IC), National Clinical Reminder Committee (NCRC), National HIMS Office, VistA Maintenance Program (VMP), Nashville Usability Testing staff, and Miami V
audience: 
keywords: 
  - strong
  - ecoe
  - class
  - blockquote
  - even
  - event
  - table
  - contents
  - colspan
  - etiology
page_count: 0
word_count: 4849
section_count: 23
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_30_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_30_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-30-epilepsy-center-of-excellence-ecoe-reminder-dialogs-installation-guide/001.png)

> Epilepsy Center of Excellence

> PXRM\*2.0\*30

> Reminder Dialogs Installation Guide

> September 2013

1.  [<u>Glossary of Terms and Abbreviations</u>](#glossary-of-terms-and-abbreviations)
2.  [<u>Introduction</u>](#introduction)
3.  [<u>Pre-installation Steps</u>](#pre-installation-steps)
    1.  [<u>Consult Orders</u>](#pre-installation-steps)
    2.  [<u>Note Titles</u>](#pre-installation-steps)
    3.  [<u>Labs for AED levels and other orderable items</u>](#labs-for-aed-levels-and-other-orderable-items)
4.  [<u>Installation</u>](#installation)
    1.  [<u>KIDS Build Installation</u>](#installation)
5.  [<u>Component Inventory</u>](#component-inventory)
    1.  [<u>Dialog List</u>](#component-inventory)
    2.  [<u>Branching Terms</u>](#component-inventory)
    3.  [<u>Branching Definitions</u>](#component-inventory)
    4.  [<u>Health Factors</u>](#5.4._Health_Factors)
    5.  [<u>Education Topics</u>](#5.4._Health_Factors)
    6.  [<u>Taxonomies</u>](#taxonomies)
    7.  [<u>Health Summary Objects</u>](#taxonomies)
6.  [<u>Post-installation Steps</u>](#post-installation-steps)
    1.  [<u>Computed Finding Parameter Edits</u>](#post-installation-steps)
    2.  [<u>Mapping Reminder Elements</u>](#6.2._Mapping_Reminder_Elements)
    3.  [<u>Mapping Health Summary Objects</u>](#mapping-health-summary-typesobjects)
    4.  [<u>Enabling and Attaching the Dialogs to Titles</u>](#enabling-and-attaching-the-dialogs-to-titles)
    5.  [<u>Creating the Shared Templates</u>](#creating-the-shared-templates)
7.  [<u>Appendix</u>](#appendix)
    1.  [<u>Appendix (A) – Health Factors</u>](#appendix)
    2.  [<u>Appendix (B) – ICD9 Codes</u>](#7.2_Appendix_(B)_-_ICD9_Codes)
    3.  [<u>Appendix (C) – Adding Dialogs</u>](#7.3_Appendix_(C)_-_Adding_dialogs)
    4.  [<u>Appendix(D)-Editing Health Summaries</u>](#7.3_Appendix_(D)_–_Editing_a_Health_Summ)

# Glossary of Terms and Abbreviations


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Glossary of Terms and Abbreviations](#glossary-of-terms-and-abbreviations)
- [Introduction](#introduction)
- [Pre-installation Steps](#pre-installation-steps)
  - [Consult Orders](#consult-orders)
  - [Note Titles](#note-titles)
  - [Labs for AED levels and other orderable items](#labs-for-aed-levels-and-other-orderable-items)
- [Installation](#installation)
  - [KIDS Build Installation](#kids-build-installation)
- [Component Inventory](#component-inventory)
  - [Dialog List](#dialog-list)
  - [Branching Terms](#branching-terms)
  - [Branching Definitions](#branching-definitions)
  - [Health Factors](#health-factors)
  - [Education Topics](#education-topics)
  - [Taxonomies](#taxonomies)
  - [Health Summary Types/Objects](#health-summary-typesobjects)
- [Post-installation Steps](#post-installation-steps)
  - [Computed Finding Parameter Edits](#computed-finding-parameter-edits)
  - [Before](#before)
  - [After](#after)
  - [Before](#before-1)
  - [After](#after-1)
  - [Before After](#before-after)
  - [Mapping Health Summary Types/Objects](#mapping-health-summary-typesobjects)
  - [Enabling and Attaching the Dialogs to Titles](#enabling-and-attaching-the-dialogs-to-titles)
  - [![](pxrm-2-30-epilepsy-center-of-excellence-ecoe-reminder-dialogs-installation-guide/003.png)Creating the Shared Templates](#pxrm-2-30-epilepsy-center-of-excellence-ecoe-reminder-dialogs-installation-guide003pngcreating-the-shared-templates)
  - [Appendix](#appendix)
  - [Appendix (B) - ICD9 Codes](#appendix-b-icd9-codes)
> AED – Anti Epileptic Drugs
> ECOE – Epilepsy Center of Excellence
> KIDS- Kernel Installation Distribution System
> NCRC – National Clinical Reminder Committee
> SE ECOE- Southeast Epilepsy Center of Excellence
> SLT- Selective Lab Test
> TIU-Text Integrated Utility
> VMP- VistA Maintenance Program
> VNS- Vagus Nerve Stimulation
> Branching Terms- A reminder term used to determine Boolean logic for branching/changing content within a reminder dialog window when it opens specific to the patient’s chart information.
> Branching Definition- A reminder definition that is used within a branching term to evaluate the Boolean logic to determine the content in a reminder window for a dialog element or dialog group.
> Dialog- A window in CPRS that opens in the format of a form to aid the user in creating text in a note and entering information into the record with a point and click interface.
> Education Topics- Informational data markers entered into the record to document topics that the patient was educated on.
> Elements- A component in VistA that is configured to display content for the user when a dialog is opened.
> Health Factor- Informational data marker entered into the record to document patient information that is not readily identifiable with other information data entries in the system.
> Health Summary Types/Objects- A collection of data that displays to the user specific to the patient’s chart they are viewing.
> Mapping- Linking of data markers such as Health Factors or other data entry items to reminder components such as reminder elements.
> National Class- The highest collection of edit permissions which can be assigned to a reminder component
> Taxonomy- Collection of specific codes associated with specific clinical conditions
> Template- Commonly referred to as a dialog. See dialog for definition
> Shared Templates- Templates within the shared templates tree of CPRS, which the users can access and use while documenting in the chart
> Usability Testing- Software usage testing conducted with users for review and acceptance of the software product.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA-ECOE templates project is a product developed in collaboration with the VA Epilepsy Center of Excellence (ECOE), VHA Informatics Council (VHA IC), National Clinical Reminder Committee (NCRC), National HIMS Office, VistA Maintenance Program (VMP), Nashville Usability Testing staff, and Miami VA Healthcare System staff, which provides guidance for the collection of the information of Veterans diagnosed with epilepsy to support uniform care and epilepsy surveillance. Thanks to the Southeast ECoE team led by <u><span class="mark">REDACTED</span></u> SE ECoE Regional Clinical Director and <span class="mark"><u>REDACTED</u></span> the SE ECoE Regional Director, for facilitating the development and implementation of this tool.

> The templates were created for, but not limited to ECOE sites, which are vital for quality control and research data for improvement in specialized epilepsy health care. The templates incorporate all of the American Academy of Neurology Epilepsy Quality Measures and the National Institute of Health recommended Common Data Elements. The database will be maintained by the VA Epilepsy Centers of Excellence Program implemented in 2008 by Public Law 110-387 mandate. Any site other than ECOE sites that would like to use the templates can and should contact <span class="mark"><u>REDACTED</u></span>

> A secondary part of this patch is to update URL’s that are embedded in national Template Fields within CPRS. Currently the URL’s take you to “Page Not Found”. With this release, the links will work correctly. The six Template Fields are listed below. These Template Fields are part of the National Reminders for Alcohol, Depression, PTSD screenings and VANOD reminder dialogs

> VA-URL PCL-C INFO VA-URL PCLC

> VA-URL PHQ9 VA-URL AUDIT-C

> VANOD BRADEN SCALE INFO VANOD URL HANDBOOK

> These six Template Fields will be updated with Reminder Exchange entry VA-URL UPDATE CARRIER ELEMENT and VA-URL UPDATE CARRIER ELEMENT 2. These Reminder Exchange entries contain reminder dialog element VA-URL UPDATE CARRIER ELEMENT and VA-URL UPDATE CARRIER ELEMENT 2. Once the URL’s are updated, both the Reminder Exchange entry and the reminder dialog element will be deleted from your system.

# Pre-installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Consult Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before the patch is installed the Reminder Manager at your site must take note of two mapped consult orders (Quick Order Dialogs). During the patch install the programmer installing the patch will be asked for the name of the local sites mapped orders to make a replacement with. The two dialog elements that contain the quick order are as follows:

> VA-PDIQ POLYTRAUMA CONSULT

> VA-TBI OI CONSULT FOR KNOWN TBI

## Note Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If your site already has consult response titles in place and in use for your Epilepsy service, your site may opt to use those titles instead of the consult response titles below. If your site does not have titles already in use, then the titles listed below are the suggested consult titles that will need to be created and mapped to the National Standard Title “Neurology Consult”. The “EPILEPSY FOLLOW-UP CONSULT RESPONSE” and “EPILEPSY INITIAL CONSULT RESPONSE” titles will also need to be added into the “Consults” document class for responding to consults.

> The “EPILEPSY RESEARCH” note goes into the “Progress Notes” class or designated class at your site for Neurology Notes and mapped to the National Standard Title of

> “Neurology Note”. Further instructions for the dialog setup that links the needed titles to dialogs are covered in the [<u>Post-installation steps</u>](#post-installation-steps).

1.  EPILEPSY FOLLOW-UP CONSULT RESPONSE TITLE Std Title: NEUROLOGY CONSULT
2.  EPILEPSY INITIAL CONSULT RESPONSE TITLE Std Title: NEUROLOGY CONSULT
3.  EPILEPSY RESEARCH TITLE Std Title: NEUROLOGY NOTE

## Labs for AED levels and other orderable items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Work with your local pharmacy to do a lookup for all the Anti-Epileptic Drugs listed in your system. You will need this list of meds post-installation to complete a Health Summary Object.

> The following is a list of elements within the dialogs that will also need to be mapped with order menus, quick orders and order sets that are used at your site:

> VA-ECOE ORDERS LAB AED LEVELS VA-ECOE ORDERS LAB BMP

> VA-ECOE ORDERS LAB CBC VA-ECOE ORDERS LAB LFT VA-ECOE ORDERS LAB VIT D VA-ECOE ORDERS LAB OTHER VA-ECOE ORDERS TEST EEG VA-ECOE ORDERS TEST MRI VA-ECOE ORDERS TEST PET

> VA-ECOE ORDERS TEST ICTAL SPECT

> VA-ECOE ORDERS TEST INTERICTAL SPECT VA-ECOE ORDERS TEST MEG

> VA-ECOE ORDERS TEST VID EEG

> VA-ECOE ORDERS NEUROPSYCHOLOGICAL VA-ECOE OTHER TESTS

> VA-ECOE ORDERS CONSULT MH

> VA-ECOE ORDERS CONSULT OB/GYN VA-ECOE ORDERS CONSULT ENDO VA-ECOE ORDERS CONSULT NEURO VA-ECOE ORDERS CONSULT SWS

> VA-ECOE ORDERS CONSULT OTHER

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## KIDS Build Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA screen capture below is the steps for the KIDS build installation. Note: For easier reading blank lines have been removed in the capture.

> Select Installation \<TEST ACCOUNT\> Option: Install Package(s) Select INSTALL NAME: PXRM\*2.0\*30 8/28/13@12:20:31

> =\> ECOE Dialogs ;Created on Aug 28, 2013@10:47:35

> This Distribution was loaded on Aug 28, 2013@12:20:31 with header of ECOE Dialogs ;Created on Aug 28, 2013@10:47:35

> It consisted of the following Install(s):

> PXRM\*2.0\*30

> Checking Install for Package PXRM\*2.0\*30

> Install Questions for PXRM\*2.0\*30 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

> Install Started for PXRM\*2.0\*30 : Aug 28, 2013@12:21:09

> Build Distribution Date: Aug 28, 2013 Installing Routines:

> Aug 28, 2013@12:21:09

> Running Pre-Install Routine: PRE^PXRMP30I DISABLE options.

> DISABLE protocols. Installing Data Dictionaries:

> Aug 28, 2013@12:21:09

> Installing Data:

> Aug 28, 2013@12:21:10

> Running Post-Install Routine: POST^PXRMP30I ENABLE options.

> ENABLE protocols.

> There are 3 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry ECOE REMINDER DIALOGS

> FINDING entry Q.ECOE TEMP OI FOR POLYTRAUMA CONSULT does not exist.

> Select one of the following: D Delete

> P Replace with an existing entry Q Quit the install

> Enter response: \<You should do a REPLACE with the correct Quick Order here from step 3.1 in this guide\>

> FINDING entry Q.ECOE TEMP OI FOR KNOWN TBI does not exist.

> Select one of the following: D Delete

> P Replace with an existing entry Q Quit the install

> Enter response: \<You should do a REPLACE with the correct Quick Order here from step 3.1 in this guide \>

> FINDING entry Q.ECOE TEMP OI FOR POLYTRAUMA CONSULT does not exist.

> Select one of the following: D Delete

> P Replace with an existing entry Q Quit the install

> Enter response: \<You should do a REPLACE with the correct Quick Order here from step 3.1 in this guide \>

> FINDING entry Q.ECOE TEMP OI FOR KNOWN TBI does not exist.

> Select one of the following: D Delete

> P Replace with an existing entry Q Quit the install

> Enter response: \<You should do a REPLACE with the correct Quick Order here from step 3.1 in this guide \>

2.  Installing Reminder Exchange entry VA-URL UPDATE CARRIER ELEMENT
3.  Installing Reminder Exchange entry VA-URL UPDATE CARRIER ELEMENT 2 Deleting unneeded Dialog entries.

> Deleting VA-URL UPDATE CARRIER ELEMENT Deleting VA-URL UPDATE CARRIER ELEMENT 2

> Deleting unneeded Exchange entries. Deleting VA-URL UPDATE CARRIER ELEMENT

> Deleting VA-URL UPDATE CARRIER ELEMENT 2

> Updating Routine file... Updating KIDS files...

> PXRM\*2.0\*30 Installed.

> Aug 28, 2013@12:25:06

> Not a production UCI

> PXRM\*2.0\*30

> Install Completed

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option You've got PRIORITY mail!

# Component Inventory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Dialog List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="5.4._Health_Factors" class="anchor"></span>There are 4 dialogs that will be installed on your system. The follow-up note and initial note will be tied to note titles. The quality of life and education will be for shared templates. See <u>Post-installation steps</u> section for setting these up.

> VA-ECOE FOLLOW-UP NOTE VA-ECOE INITIAL NOTE

> VA-ECOE QUALITY OF LIFE TPL VA-ECOE EDUCATION TPL

## Branching Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of all the branching terms:

> VA-BL ECOE ALCOHOL USE SCREEN NATIONAL VA-BL ECOE DEPRESSION SCREEN NATIONAL VA-BL ECOE OEF/OIF NATIONAL

> VA-BL ECOE TBI OEF/OIF NATIONAL

## Branching Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is only one branching reminder definition named “VA-BL OEF/OIF COHORT” that is new in this installation. There aren’t any special instructions for this reminder definition.

## Health Factors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are 18 National Class health factors categories containing 272 individual health factors. See [<u>Appendix (A)</u>](#appendix) for listing.

## Education Topics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following National Education topics are included in this install.

| VA-ECOE AED SIDE EFFECTS     |
|------------------------------|
| VA-ECOE BONE HEALTH          |
| VA-ECOE CONTRACEPTION        |
| VA-ECOE DRIVING              |
| VA-ECOE EPILEPSY RESOURCES   |
| VA-ECOE MH                   |
| VA-ECOE OTHER TOPIC          |
| VA-ECOE PREGNANCY            |
| VA-ECOE SAFETY               |
| VA-ECOE SEIZURE PRECAUTIONS  |
| VA-ECOE SUDEP                |
| VA-ECOE SUICIDE IDEATION     |
| VA-ECOE TREATMENT COMPLIANCE |

## Taxonomies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is 1 taxonomy named “VA-ECOE DIAGNOSIS CODES” which is mapped to an element for entering diagnosis codes into the visit encounter. See [<u>Appendix (B)</u>](#7.2_Appendix_(B)_-_ICD9_Codes) for listing.

> Note: This element will not include the diagnosis in any of the text created in the notes.

## Health Summary Types/Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are 8 new Health Summary Types/Objects that will install with this build. Mapping will only be needed for the two Health Summary Types named ECOE AED LEVELS and ECOE VITAMIN D LEVEL.

> ECOE AED LEVELS

> ECOE DEPRESSION CMB ECOE LAST EVENTS NOTED ECOE LAST MED PLAN ECOE OEF/OIF TBI

> ECOE PREVIOUS AEDS

> ECOE PREVIOUS DIAGNOSTICS ECOE VITAMIN D LEVEL ECOE VNS INITIAL

> ECOE VNS LAST

# Post-installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Computed Finding Parameter Edits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are 3 branching reminder terms that each have a VA-REMINDER DEFINITION computed finding. The “Computed Finding Parameter” will need to be edited to remove the imported COMPUTED FINDING PARAMETER entry of “ENTER DEFINITION HERE” and replace it with the names of National definitions.

> 1.

> VA-BL ECOE ALCOHOL USE SCREEN

> Findings:

> Finding Item: VA-REMINDER DEFINITION (FI(1)=CF(35)) Finding Type: REMINDER COMPUTED FINDING

> Condition: I V("STATUS")="DONE"!(V("STATUS")="RESOLVED")

> Computed Finding Parameter: ENTER DEFINITION HERE

> VA-BL ECOE ALCOHOL USE SCREEN

> Findings:

## Before

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Finding Item: VA-REMINDER DEFINITION (FI(1)=CF(35)) Finding Type: REMINDER COMPUTED FINDING

## After

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Condition: I V("STATUS")="DONE"!(V("STATUS")="RESOLVED")

> Computed Finding Parameter: VA-ALCOHOL USE SCREEN (AUDIT-C)

> 2.

> VA-BL ECOE DEPRESSION SCREEN (BEFORE EDIT)

> Findings:

> Finding Item: VA-REMINDER DEFINITION (FI(1)=CF(35)) Finding Type: REMINDER COMPUTED FINDING

> Condition: I V("STATUS")="DONE"!(V("STATUS")="RESOLVED")

> Computed Finding Parameter: ENTER DEFINITION HERE

> VA-BL ECOE DEPRESSION SCREEN

> Findings:

## Before

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Finding Item: VA-REMINDER DEFINITION (FI(1)=CF(35)) Finding Type: REMINDER COMPUTED FINDING

## After

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Condition: I V("STATUS")="DONE"!(V("STATUS")="RESOLVED")

> Computed Finding Parameter: VA-DEPRESSION SCREENING

> Continued on next page…

> 3\.

> <span id="6.2._Mapping_Reminder_Elements" class="anchor"></span>VA-BL ECOE TBI OEF/OIF (BEFORE EDIT)

> Findings:

> Finding Item: VA-REMINDER DEFINITION (FI(1)=CF(35)) Finding Type: REMINDER COMPUTED FINDING

> Condition: I V("STATUS")="DUE NOW"

> Computed Finding Parameter: ENTER DEFINITION HERE

> VA-BL ECOE TBI OEF/OIF (AFTER EDIT)

> Findings:

> Finding Item: VA-REMINDER DEFINITION (FI(1)=CF(35)) Finding Type: REMINDER COMPUTED FINDING

> Condition: I V("STATUS")="DUE NOW"

> Computed Finding Parameter: VA-TBI SCREENING

## Before After

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Mapping Reminder Elements

> The list of Dialog Elements below will need to have the findings mapped to the local orders, order sets or menus. The LAB AED LEVELS should be mapped to a menu that lists the lab orders for the AED list obtained during pre-install. This will need to be created manually at your site if one does not already exist on your system.

> VA-ECOE ORDERS LAB AED LEVELS VA-ECOE ORDERS LAB BMP

> VA-ECOE ORDERS LAB CBC VA-ECOE ORDERS LAB LFT VA-ECOE ORDERS LAB VIT D VA-ECOE ORDERS LAB OTHER VA-ECOE ORDERS TEST EEG VA-ECOE ORDERS TEST MRI VA-ECOE ORDERS TEST PET

> VA-ECOE ORDERS TEST ICTAL SPECT

> VA-ECOE ORDERS TEST INTERICTAL SPECT VA-ECOE ORDERS TEST MEG

> VA-ECOE ORDERS TEST VID EEG

> VA-ECOE ORDERS NEUROPSYCHOLOGICAL VA-ECOE OTHER TESTS

> VA-ECOE ORDERS CONSULT MH

> VA-ECOE ORDERS CONSULT OB/GYN VA-ECOE ORDERS CONSULT ENDO VA-ECOE ORDERS CONSULT NEURO VA-ECOE ORDERS CONSULT SWS

> VA-ECOE ORDERS CONSULT OTHER

## Mapping Health Summary Types/Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Using the AED list in the previous step 5.1, check the Health Summary Types named “ECOE AED LEVELS” and “ECOE VITAMIN D LEVEL”. The selective labs for each medication and for Vitamin D need to be included in the components list in the Health Summary Type, Selective Lab Tests (SLT). Add the addition lab tests as needed for your site. See [<u>Appendix (D)</u>](#7.3_Appendix_(D)_–_Editing_a_Health_Summ) for an example edit.

> HEALTH SUMMARY TYPE INQUIRY Type Name: ECOE AED LEVELS

> Title: AED LEVELS Owner: PROGRAMMER,NAME

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

> Max Hos ICD Pro CPT

> Abb Ord Component Name Occ Time Loc Text Nar Mod Selection

> ------------------------------------------------------------------------------

> SLT 5 AED Levels 1

> CARBAMAZEPINE CLONAZEPAM DIAZEPAM PHENOBARBITAL

## Enabling and Attaching the Dialogs to Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> While using the TIU Editor if at any time the settings do not look correct NEVER click the apply button, but instead click Cancel, then start over.

> Before linking the dialogs to titles or using them in shared templates you must first add each one into the TIU Template Reminder Dialog Parameter list. See [<u>Appendix (C)</u>](#7.3_Appendix_(C)_-_Adding_dialogs) for an example of adding the VA-ECOE INITIAL NOTE dialog to the list.

> Link the dialogs from the TIU editor found in the Options menu in CPRS while on the Notes tab. Create a new template in the Document Titles cabinet in the upper left panel for each title name then associate the title using the dropdown list in the bottom panel.

![](pxrm-2-30-epilepsy-center-of-excellence-ecoe-reminder-dialogs-installation-guide/002.png)

## ![](pxrm-2-30-epilepsy-center-of-excellence-ecoe-reminder-dialogs-installation-guide/003.png)Creating the Shared Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Search for the folder that your Neurology service uses in the Shared Templates cabinet in the upper left panel of the TIU Editor. If one does not exist then you will have to create new one to hold the shared template dialogs. Create 2 new templates in the Neurology folder called “Epilepsy Quality of Life” and “Epilepsy Education”. Link each

> one by selecting the template type of Reminder Dialog and selecting the dialogs named “VA-ECOE Quality of Life TPL” and “VA-ECOE Education TPL” accordingly.

## Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Appendix (A) - Health Factors

> Categories:

> VA-ECOE

> VA-ECOE AED PREVIOUS VA-ECOE AEDS

> VA-ECOE DEVICE OTHER VA-ECOE ETIOLOGY

> VA-ECOE ETIOLOGY PRIMARY VA-ECOE ETIOLOGY SECONDARY VA-ECOE EVENTS

> VA-ECOE EXAM

> VA-ECOE MED PLAN

> VA-ECOE PREV DIAGNOSTIC VA-ECOE QOLIE

> VA-ECOE SOCIAL HX VA-ECOE TBI FACTORS

> VA-ECOE TBI IMG RESULT VA-ECOE TELEMED

> VA-ECOE VNS

> VA-ECOE VNS INITIAL

> Individual Factors list:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VA-ECOE AED 1 DOSAGE</strong></th>
<th><strong>VA-ECOE EVENT 5 MENTAL STATUS</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VA-ECOE AED 1 LEVEL</strong></td>
<td><strong>VA-ECOE EVENT 5 MOTOR ACTIVITY</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 1 NAME</strong></td>
<td><strong>VA-ECOE EVENT 5 OTHER</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 1 PREP</strong></td>
<td><strong>VA-ECOE EVENT 5 POST-ICTAL</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 1 SCHEDULE</strong></td>
<td><strong>VA-ECOE EVENT 5 SENSORY</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 2 DOSAGE</strong></td>
<td><strong>VA-ECOE EVENT 5 START</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 2 LEVEL</strong></td>
<td><strong>VA-ECOE EVENT 5 TIME</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 2 NAME</strong></td>
<td><strong>VA-ECOE EVENT 5 TYPE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 2 PREP</strong></td>
<td><p><strong>VA-ECOE FUNCTIONAL MRI</strong></p>
<p><strong>COMMENTS</strong></p></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 2 SCHEDULE</strong></td>
<td><strong>VA-ECOE FUNCTIONAL MRI DATE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 3 DOSAGE</strong></td>
<td><strong>VA-ECOE FUNCTIONAL MRI LANGUAGE</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 3 LEVEL</strong></td>
<td><strong>VA-ECOE FUNCTIONAL MRI MEMORY</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 3 NAME</strong></td>
<td><strong>VA-ECOE HANDEDNESS BOTH</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 3 PREP</strong></td>
<td><strong>VA-ECOE HANDEDNESS LF</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 3 SCHEDULE</strong></td>
<td><strong>VA-ECOE HANDEDNESS RT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 4 DOSAGE</strong></td>
<td><strong>VA-ECOE HANDEDNESS UNKNOWN</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 4 LEVEL</strong></td>
<td><strong>VA-ECOE HX STATUS EPILEPTICUS</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 4 NAME</strong></td>
<td><strong>VA-ECOE ICTAL SEMIOLOGY</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED 4 PREP</strong></td>
<td><strong>VA-ECOE ICTAL SPECT COMMENT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED 4 SCHEDULE</strong></td>
<td><strong>VA-ECOE ICTAL SPECT DATE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED PREVIOUS COMMENT</strong></td>
<td><strong>VA-ECOE ICTAL SPECT RESULT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AED PREVIOUS DC</strong></td>
<td><strong>VA-ECOE INJURIES</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE AED PREVIOUS DOSE</strong></td>
<td><strong>VA-ECOE INTERICTAL SPECT COMMENT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE AGE AT ONSET</strong></td>
<td><strong>VA-ECOE INTERICTAL SPECT DATE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE CAFFEINE</strong></td>
<td><strong>VA-ECOE INTERICTAL SPECT RESULT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE COMPLETED EDU</strong></td>
<td><strong>VA-ECOE LIVING ARRANGEMENT</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE DEVICE CHANGE PARAMETER</strong></td>
<td><strong>VA-ECOE MED PLAN CHANGE</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE DEVICE COMMENTS</strong></td>
<td><strong>VA-ECOE MED PLAN DISC</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE DEVICE DATE</strong></td>
<td><strong>VA-ECOE MED PLAN NEW</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE DEVICE MFG</strong></td>
<td><strong>VA-ECOE MED PLAN NO CHANGE</strong></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VA-ECOE DEVICE TYPE</strong></th>
<th><strong>VA-ECOE MEG COMMENT</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VA-ECOE DRIVING</strong></td>
<td><strong>VA-ECOE MEG DATE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EEG COMMENT</strong></td>
<td><strong>VA-ECOE MEG RESULT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EEG DATE</strong></td>
<td><strong>VA-ECOE MH HX</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EEG RESULT</strong></td>
<td><strong>VA-ECOE MRI COMMENT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EMPLOYMENT</strong></td>
<td><strong>VA-ECOE MRI DATE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLGY PRIMARY 12</strong></td>
<td><strong>VA-ECOE MRI RESULT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY DEFINITE</strong></td>
<td><strong>VA-ECOE NEURO TEST COMMENT</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY NO</strong></td>
<td><strong>VA-ECOE NEURO TEST DATE</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY POSSIBLE</strong></td>
<td><strong>VA-ECOE NEURO TEST RESULT</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 1</strong></td>
<td><strong>VA-ECOE NO. EVENT TYPES</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 10</strong></td>
<td><strong>VA-ECOE NYSTAGMUS</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 11</strong></td>
<td><strong>VA-ECOE OTHER COMMENT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 12</strong></td>
<td><strong>VA-ECOE OTHER TEST DATE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 13</strong></td>
<td><strong>VA-ECOE OVERALL FREQUENCY</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 14</strong></td>
<td><strong>VA-ECOE PET COMMENT</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 15</strong></td>
<td><strong>VA-ECOE PET DATE</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 16</strong></td>
<td><strong>VA-ECOE PET RESULT</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 2</strong></td>
<td><strong>VA-ECOE PHYSICAL EXAM</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 3</strong></td>
<td><strong>VA-ECOE QOLIE #1</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 4</strong></td>
<td><strong>VA-ECOE QOLIE #10</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 5</strong></td>
<td><strong>VA-ECOE QOLIE #11</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 6</strong></td>
<td><strong>VA-ECOE QOLIE #12A</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 7</strong></td>
<td><strong>VA-ECOE QOLIE #12B</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 8</strong></td>
<td><strong>VA-ECOE QOLIE #12C</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY PRIMARY 9</strong></td>
<td><strong>VA-ECOE QOLIE #12D</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY PRIMARY COMMENT</strong></td>
<td><strong>VA-ECOE QOLIE #12E</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 1</strong></td>
<td><strong>VA-ECOE QOLIE #12F</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 10</strong></td>
<td><strong>VA-ECOE QOLIE #12G</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 11</strong></td>
<td><strong>VA-ECOE QOLIE #2</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 12</strong></td>
<td><strong>VA-ECOE QOLIE #3</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 13</strong></td>
<td><strong>VA-ECOE QOLIE #4</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 14</strong></td>
<td><strong>VA-ECOE QOLIE #5</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 15</strong></td>
<td><strong>VA-ECOE QOLIE #6</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 16</strong></td>
<td><strong>VA-ECOE QOLIE #7</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 2</strong></td>
<td><strong>VA-ECOE QOLIE #8</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 3</strong></td>
<td><strong>VA-ECOE QOLIE #9</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 4</strong></td>
<td><strong>VA-ECOE RECREATIONAL</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 5</strong></td>
<td><strong>VA-ECOE RISK FACTORS</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 6</strong></td>
<td><strong>VA-ECOE SLEEP COMPLAINT</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 7</strong></td>
<td><strong>VA-ECOE SURG COMMENT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 8</strong></td>
<td><strong>VA-ECOE SURG DATE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE ETIOLOGY SECONDARY 9</strong></td>
<td><strong>VA-ECOE SURG RESULT</strong></td>
</tr>
<tr class="odd">
<td><p><strong>VA-ECOE ETIOLOGY SECONDARY</strong></p>
<p><strong>COMMENT</strong></p></td>
<td><strong>VA-ECOE TBI</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 1 AURA</strong></td>
<td><strong>VA-ECOE TBI # DEPLOYMENTS</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 1 AUTONOMIC</strong></td>
<td><strong>VA-ECOE TBI CAUSE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 1 DUR</strong></td>
<td><strong>VA-ECOE TBI COMBAT</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 1 DUR POST-ICTAL</strong></td>
<td><strong>VA-ECOE TBI DATE</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 1 FREQUENCY</strong></td>
<td><strong>VA-ECOE TBI IMG RESULT 1</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 1 LAST</strong></td>
<td><strong>VA-ECOE TBI IMG RESULT 10</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 1 MENTAL STATUS</strong></td>
<td><strong>VA-ECOE TBI IMG RESULT 11</strong></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 1 MOTOR ACTIVITY</strong></td>
<td><strong>VA-ECOE TBI IMG RESULT 12</strong></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 1 OTHER</strong></td>
<td><strong>VA-ECOE TBI IMG RESULT 13</strong></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VA-ECOE EVENT 1 POST-ICTAL</strong></th>
<th><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 14</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VA-ECOE EVENT 1 SENSORY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 15</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 1 START</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 16</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 1 TIME</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 17</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 1 TYPE</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 18</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 2 AURA</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 19</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 2 AUTONOMIC</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 2</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 2 DUR</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 20</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 2 DUR POST-ICTAL</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 21</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 2 FREQUENCY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 22</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 2 LAST</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 3</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 2 MENTAL STATUS</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 4</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 2 MOTOR ACTIVITY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 5</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 2 OTHER</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 6</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 2 POST-ICTAL</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 7</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 2 SENSORY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 8</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 2 START</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT 9</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 2 TIME</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI IMG RESULT COMMENT</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 2 TYPE</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI PATHOLOGY</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 3 AURA</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI SEVERITY</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 3 DUR</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI SURGERY</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 3 DUR POST-ICTAL</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TBI TYPE</strong></p>
<p><strong>VA-ECOE TBI UNKNOWN</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 3 FREQUENCY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TELEMED NO</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 3 LAST</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TELEMED YES</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 3 MENTAL STATUS</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TREMORS</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 3 MOTOR ACTIVITY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE TRIGGERS</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 3 OTHER</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VID EEG COMMENT</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 3 POST-ICTAL</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VID EEG DATE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 3 SENSORY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VID EEG RESULT</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 3 START</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS COMMENT</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 3 TIME</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS FREQUENCY</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 3 TYPE</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL COMMENT</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 4 AURA</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL FREQUENCY</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 4 AUTONOMIC</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL IMPLANT DATE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 4 DUR</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL MAG. CURRENT</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 4 DUR POST-ICTAL</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL MAG. ON TIME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 4 FREQUENCY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL MAG. PULSE</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><span id="7.2_Appendix_(B)_-_ICD9_Codes" class="anchor"></span><strong>VA-ECOE EVENT 4 LAST</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL MODEL</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 4 MENTAL STATUS</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL OFF TIME</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 4 MOTOR ACTIVITY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL ON TIME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 4 OTHER</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL OUTPUT</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 4 POST-ICTAL</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS INITIAL SERIAL</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 4 SENSORY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS MAG. CURRENT</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 4 START</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS MAG. ON TIME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 4 TIME</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS MAG. PULSE</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 4 TYPE</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS OFF TIME</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 5 AURA</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS ON TIME</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 5 AUTONOMIC</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS OUTPUT</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 5 DUR</strong></td>
<td><blockquote>
<p><strong>VA-ECOE VNS PULSE</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 5 DUR POST-ICTAL</strong></td>
<td><blockquote>
<p><strong>VA-ECOE WADA COMMENTS</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VA-ECOE EVENT 5 FREQUENCY</strong></td>
<td><blockquote>
<p><strong>VA-ECOE WADA DATE</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VA-ECOE EVENT 5 LAST</strong></td>
<td><blockquote>
<p><strong>VA-ECOE WADA LANGUAGE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><strong>VA-ECOE WADA MEMORY</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix (B) - ICD9 Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA-ECOE DIAGNOSIS CODES No. 61

> Class: NATIONAL

> Sponsor:

> Review Date:

> Brief Description:

> Edit History:

> Patient Data Source:

> Use Inactive Problems:

> ICD9 Codes:

> Range 345.00-345.01 Adjacent Lower-345.0 Adjacent Higher-345.1

> Code ICD Diagnosis Activation Inactivation Selectable

1.  GEN NONCV EP W/O INTR EP 10/01/1978 X
2.  GEN NONCNV EP W INTR EP 10/01/1978 X Range 345.10-345.10 Adjacent Lower-345.1 Adjacent Higher-345.11

> Code ICD Diagnosis Activation Inactivation Selectable

> 345.10 GEN CNV EPIL W/O INTR EP 10/01/1978 X Range 345.2-345.9 Adjacent Lower-345.11 Adjacent Higher-345.90

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 2%" />
<col style="width: 15%" />
<col style="width: 1%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>ICD Diagnosis</th>
<th></th>
<th>Activation</th>
<th></th>
<th>Inactivation</th>
<th></th>
<th>Selectable</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>345.2</td>
<td>PETIT MAL STATUS</td>
<td></td>
<td>10/01/1978</td>
<td></td>
<td></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>345.3</td>
<td>GRAND MAL STATUS</td>
<td></td>
<td>10/01/1978</td>
<td></td>
<td></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>345.4</td>
<td>PSYCHOMOTOR EPILEPSY</td>
<td></td>
<td>10/01/1978</td>
<td></td>
<td>10/01/1989</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>345.40</td>
<td>PSYMOTR EPIL W/O INT</td>
<td>EPI</td>
<td>10/01/1978</td>
<td></td>
<td></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>345.41</td>
<td colspan="2">PSYMOTR EPIL W INTR EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>345.5</td>
<td colspan="2">PARTIAL EPILEPSY NEC</td>
<td>10/01/1978</td>
<td colspan="2"><blockquote>
<p>10/01/1989</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>345.50</td>
<td colspan="2">PART EPIL W/O INTR EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>345.51</td>
<td colspan="2">PART EPIL W INTR EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>345.6</td>
<td colspan="2">INFANTILE SPASMS</td>
<td>10/01/1978</td>
<td colspan="2"><blockquote>
<p>10/01/1989</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>345.60</td>
<td colspan="2">INF SPASM W/O INTR EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>345.61</td>
<td colspan="2">INF SPASM W INTRACT EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>345.7</td>
<td colspan="2">EPILEPS PARTIAL CONTINUA</td>
<td>10/01/1978</td>
<td colspan="2"><blockquote>
<p>10/01/1989</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>345.70</td>
<td colspan="2">EPIL PAR CONT W/O INT EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>345.71</td>
<td colspan="2">EPIL PAR CONT W INTR EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>345.8</td>
<td colspan="2">EPILEPSY NEC</td>
<td>10/01/1978</td>
<td colspan="2"><blockquote>
<p>10/01/1989</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>345.80</td>
<td colspan="2">EPILEP NEC W/O INTR EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>345.81</td>
<td colspan="2">EPILEPSY NEC W INTR EPIL</td>
<td>10/01/1978</td>
<td colspan="2"></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>345.9</td>
<td colspan="2">EPILEPSY NOS</td>
<td>10/01/1978</td>
<td colspan="2"><blockquote>
<p>10/01/1989</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
</tbody>
</table>

> Range 345.40-345.41 Adjacent Lower-345.4 Adjacent Higher-345.5

> Code ICD Diagnosis Activation Inactivation Selectable

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 33%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>345.40 PSYMOTR EPIL W/O INT EPI</th>
<th><blockquote>
<p>10/01/1978</p>
</blockquote></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>345.41 PSYMOTR EPIL W INTR EPIL</td>
<td><blockquote>
<p>10/01/1978</p>
</blockquote></td>
<td>X</td>
</tr>
</tbody>
</table>

> Range 345.50-345.51 Adjacent Lower-345.5 Adjacent Higher-345.6

> Code ICD Diagnosis Activation Inactivation Selectable

50. PART EPIL W/O INTR EPIL 10/01/1978 X
51. PART EPIL W INTR EPIL 10/01/1978 X Range 345.7-345.7 Adjacent Lower-345.61 Adjacent Higher-345.70

> Code ICD Diagnosis Activation Inactivation Selectable

> 345.7 EPILEPS PARTIAL CONTINUA 10/01/1978 10/01/1989 X Range 345.71-345.71 Adjacent Lower-345.70 Adjacent Higher-345.8

> Code ICD Diagnosis Activation Inactivation Selectable

> 345.71 EPIL PAR CONT W INTR EPIL 10/01/1978 X Range 345.80-345.81 Adjacent Lower-345.8 Adjacent Higher-345.9

> Code ICD Diagnosis Activation Inactivation Selectable

80. EPILEP NEC W/O INTR EPIL 10/01/1978 X
81. EPILEPSY NEC W INTR EPIL 10/01/1978 X Range 345.90-345.91 Adjacent Lower-345.9 Adjacent Higher-346.0

> Code ICD Diagnosis Activation Inactivation Selectable

90. EPILEP NOS W/O INTR EPIL 10/01/1978 X
91. EPILEP NOS W INTR EPIL 10/01/1978 X Range 907.0-907.0 Adjacent Lower-906.9 Adjacent Higher-907.1

> Code ICD Diagnosis Activation Inactivation Selectable

> 907.0 LT EFF INTRACRANIAL INJ 10/01/1978 X Range 649.42-649.44 Adjacent Lower-649.41 Adjacent Higher-649.50

> Code ICD Diagnosis Activation Inactivation Selectable

42. EPILEPSY-DELIVERED W P/P 10/01/2006 X
43. EPILEPSY-ANTEPARTUM 10/01/2006 X
44. EPILEPSY-POSTPARTUM 10/01/2006 X Range 291.81-291.81 Adjacent Lower-291.8 Adjacent Higher-291.82

> Code ICD Diagnosis Activation Inactivation Selectable

> 291.81 ALCOHOL WITHDRAWAL 10/01/1978 X Range 346.0-346.0 Adjacent Lower-345.91 Adjacent Higher-346.00

> Code ICD Diagnosis Activation Inactivation Selectable

> 346.0 CLASSICAL MIGRAINE 10/01/1978 10/01/1992 X Range 346.2-346.2 Adjacent Lower-346.13 Adjacent Higher-346.20

> Code ICD Diagnosis Activation Inactivation Selectable

> 346.2 VARIANTS OF MIGRAINE 10/01/1978 10/01/1992 X Range 346.8-346.8 Adjacent Lower-346.73 Adjacent Higher-346.80

> Code ICD Diagnosis Activation Inactivation Selectable

> 346.8 MIGRAINE NEC 10/01/1978 10/01/1992 X

> Range 780.09-780.09 Adjacent Lower-780.03 Adjacent Higher-780.1

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.09 OTHER ALTERATION CONS. 10/01/1978 X Range 780.31-780.31 Adjacent Lower-780.3 Adjacent Higher-780.32

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.31 FEBRILE CONVULSIONS NOS 10/01/1978 X Range 780.39-780.39 Adjacent Lower-780.33 Adjacent Higher-780.4

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.39 OTHER CONVULSIONS 10/01/1978 X Range 781.0-781.0 Adjacent Lower-780.99 Adjacent Higher-781.1

> Code ICD Diagnosis Activation Inactivation Selectable

> 781.0 ABN INVOLUN MOVEMENT NEC 10/01/1978 X Range 782.0-782.0 Adjacent Lower-781.99 Adjacent Higher-782.1

> Code ICD Diagnosis Activation Inactivation Selectable

> 782.0 SKIN SENSATION DISTURB 10/01/1978 X Range 784.0-784.0 Adjacent Lower-783.9 Adjacent Higher-784.1

> Code ICD Diagnosis Activation Inactivation Selectable

> 784.0 HEADACHE 10/01/1978 X Range 780.50-780.50 Adjacent Lower-780.4 Adjacent Higher-780.51

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.50 SLEEP DISTURBANCE NOS 10/01/1978

> Range 780.01-780.03 Adjacent Lower-780.0 Adjacent Higher-780.09

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.01 COMA 10/01/1978

2.  TRANSIENT ALTERATION 10/01/1978
3.  PERS VEGETAT STATE 10/01/1978

> Range 780.2-780.2 Adjacent Lower-780.1 Adjacent Higher-780.3

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.2 SYNCOPE AND COLLAPSE 10/01/1978

> Range 780.4-780.4 Adjacent Lower-780.39 Adjacent Higher-780.50

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.4 DIZZINESS AND GIDDINESS 10/01/1978

> Range 345.11-345.11 Adjacent Lower-345.10 Adjacent Higher-345.2

> Code ICD Diagnosis Activation Inactivation Selectable

> 345.11 GEN CNV EPIL W INTR EPIL 10/01/1978

> Range 649.41-649.41 Adjacent Lower-649.40 Adjacent Higher-649.42

> Code ICD Diagnosis Activation Inactivation Selectable

> 649.41 EPILEPSY-DELIVERED 10/01/2006

> Range 780.02-780.02 Adjacent Lower-780.01 Adjacent Higher-780.03

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.02 TRANSIENT ALTERATION 10/01/1978

> Range 780.3-780.3 Adjacent Lower-780.2 Adjacent Higher-780.31

> Code ICD Diagnosis Activation Inactivation Selectable

> 780.3 CONVULSIONS 10/01/1978 10/01/1997

> ICD0 Codes:

> CPT Codes:

3.  <span id="7.3_Appendix_(C)_-_Adding_dialogs" class="anchor"></span>Appendix (C) - Adding dialogs to the TIU Template Reminder Dialog Parameter \[starting from the Reminder Manager Menu\]

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: CP CPRS Reminder Configuration

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active PN Progress Note Headers

> RA Reminder GUI Resolution Active

> TIU TIU Template Reminder Dialog Parameter DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

> GEC GEC Status Check Active WH WH Print Now Active

> Select CPRS Reminder Configuration \<TEST ACCOUNT\> Option: TIU TIU Template Reminder Dialog Parameter

> Reminder Dialogs allows as Templates may be set for the following:

> 1 User USR \[choose from NEW PERSON\]

3.  Service SRV \[choose from SERVICE/SECTION\]
4.  Division DIV \[NAME OF YOUR DIVISION\]
5.  System SYS \[YOURSERVER.YOURSITE.MED.VA.GOV\] Enter selection: 5 System NATREM.FO-SLC.MED.VA.GOV

> Setting Reminder Dialogs allows as Templates for System: YOURSERVER.YOURSITE.MED.VA.GOV

> Select Display Sequence: ? Display Sequence Value

> ........

63. VA\*CG INITIAL IN-HOME ASSESSMENT REV
64. VA\*CG CLIN ELIG CHILD NOTE

> Select Display Sequence: 65 \<select a sequence that is not being used in your system\>

> Are you adding 65 as a new Display Sequence? Yes// YES Display Sequence: 65// 65

> Clinical Reminder Dialog: VA-ECOE INITIAL NOTE reminder dialog NATIONAL

> ...OK? Yes// (Yes)

> <span id="7.3_Appendix_(D)_–_Editing_a_Health_Summ" class="anchor"></span>7.3 Appendix (D) – Editing a Health Summary

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: ^create tiu/Health Summary Objects

> --- Manager Document Definition Menu ---

> TIU Health Summary Object Mar 18, 2013@10:15:06 Page: 1 of 4

> TIU Object Name Health Summary Type

1.  ADMISSIONS PAST YR ADMISSIONS PAST YR
2.  AUDIT-C OB AUDC
3.  BDI2 OB-BDI2
4.  BRADEN SCALE 30D VA-BRADEN SCALE 30D
5.  CONSULTS PAST CONSULTS PAST
6.  DEPRESSION REMINDER STATUS DEPR REMINDER STATUS (OBJ)
7.  DIAB RETIN SURV NOTE DIAB RETIN SURV NOTE
8.  ECOE AED LEVELS ECOE AED LEVELS
9.  ECOE AUDC CMB ECOE AUDC CMB
10. ECOE DEPRESSION CMB ECOE DEPRESSION CMB
11. ECOE LAST EVENTS NOTED ECOE LAST EVENTS NOTED
12. ECOE LAST MED PLAN ECOE LAST MED PLAN
13. ECOE OEF/OIF TBI ECOE OEF/OIF TBI
14. ECOE OTHER DEVICE ECOE OTHER DEVICE

> Create New TIU Object Find

> Detailed Display/Edit TIU Object Detailed Display/Edit HS Object Quit

> Select Action: Next Screen// Det

> \+ Enter ?? for more actions

1.  Detailed Display/Edit HS Object
2.  Detailed Display/Edit TIU Object CHOOSE 1-2: 1 Detailed Display/Edit HS Object Select Entry: (1-14) 8

> Next Screen

> Change HS Object Detail Display/Edit HS Object Change Health Summary Type

> Select Item(s): Quit// det Detail Display/Edit HS Object

> HS OBJECT DISPLAY Mar 18, 2013@10:15:56 Page: 1 of 1

> Detailed Display for ECOE AED LEVELS

> HS Object: ECOE AED LEVELS (TIU)

> Health Summary Type: ECOE AED LEVELS Report Period:

> Creator: CARTER,DAVID L

> HS Object

> Print Label: NO Print Report Date and Time: NO Print Blank Line after Label: NO Print Confidentiality Banner: NO Customized Header: YES Print Report Date and Time: NO

> Suppress Components w/o Data: NO Print Component Header: NO Print Deceased Information: NO Print Time-Occurrence Limits: NO National Object: NO Underline Component Header: NO

Blank Line After Header: NO

> Overwrite No Data:

> Enter ?? for more actions Select Action: Quit// edit

1.  Edit HS Object
2.  Edit HS Type CHOOSE 1-2: 2 Edit HS Type

> Editing Health Summary Type 'ECOE AED LEVELS' NAME: ECOE AED LEVELS//

> TITLE: AED LEVELS//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes//

> HEALTH SUMMARY TYPE INQUIRY Type Name: ECOE AED LEVELS

> Title: AED LEVELS Owner: CARTER,DAVID L

| SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN |          |               |
|--------------------------------------------------------------------------------------|----------|---------------|
| Max Hos                                                                              | ICD Pro  | CPT           |
| Abb Ord Component Name Occ Time Loc                                                  | Text Nar | Mod Selection |
| SLT 5 AED Levels 1                                                                   |          |               |

> \* = Disabled Components

> Select COMPONENT: slt LAB TESTS SELECTED SLT

> LAB TESTS SELECTED is already a component of this summary.

> Select one of the following:

> E Edit component parameters

> D Delete component from summary

> Select Action: e Edit component parameters SUMMARY ORDER: 5// 5

> OCCURRENCE LIMIT: 1// TIME LIMIT:

> HEADER NAME: AED Levels// No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select up to 99 items.

> Select SELECTION ITEM: DIAZEPAM

> Searching for a LABORATORY TEST, (pointed-to by SELECTION ITEM)

> Searching for a LABORATORY TEST DIAZEPAM

> ...OK? Yes// (Yes) Select SELECTION ITEM:

> Select COMPONENT:

> Do you wish to review the Summary Type structure before continuing? NO// Please hold on while I resequence the summary order.

> Enter RETURN to continue or '^' to exit: