---
title: PSB*3*47/PSS*1*141 BCMA Version 3 Immunizations Documentation
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*47
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - bcma
  - orderable
  - task
  - immunizations
  - table
  - contents
  - immunization
  - application
  - installation
  - install
page_count: 0
word_count: 2930
section_count: 8
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p47_pss_1_p141_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p47_pss_1_p141_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

---
date: "![](psb-3-47-pss-1-141-bcma-version-3-immunizations-documentation/001.png)"
---

IMMUNIZATIONS DOCUMENTATION BY BAR CODE MEDICATION ADMINISTRATION (BCMA)

INSTALLATIONGUIDE

PSB\*3\*47 and PSS\*1\*141

October 2009

Table of Contents

*(This page left blank for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pre-Installation Considerations](#pre-installation-considerations)
  - [External Relationships](#external-relationships)
  - [BCMA2PCE Pre-Installation Considerations](#bcma2pce-pre-installation-considerations)
    - [Unschedule AJEY PSB PX BCMA2PCE TASK](#unschedule-ajey-psb-px-bcma2pce-task)
    - [Identify Existing Relationships in BCMA2PCE Application](#identify-existing-relationships-in-bcma2pce-application)
- [Installation Procedure](#installation-procedure)
  - [Install Patch PSS\1\141](#install-patch-pss1141)
  - [Install Patch PSB\3\47](#install-patch-psb347)
  - [Mapping Relationships Between the PHARMACY ORDERABLE ITEMS File (#50.7) and the IMMUNIZATION File (#9999999.14)](#mapping-relationships-between-the-pharmacy-orderable-items-file-507-and-the-immunization-file-999999914)
- [Post Installation Considerations](#post-installation-considerations)
  - [Validate the Immunizations Documentation by BCMA Nightly Task \[PSB PX BCMA2PCE TASK\] Option](#validate-the-immunizations-documentation-by-bcma-nightly-task-psb-px-bcma2pce-task-option)
  - [Queuing the Nightly Background Option](#queuing-the-nightly-background-option)
This installation guide will describe the setup steps necessary to begin use of the Immunizations Documentation by Bar Code Medication Administration (BCMA) application introduced with patches PSB\*3\*47 and PSS\*1\*141. Patch PSB\*3\*47 adds *Immunizations Documentation by BCMA Nightly Task* \[PSB PX BCMA2PCE TASK\] option to the *Bar Code Medication Administration Manager* \[PSB MGR\] menu. You can use this option to run a task which will create a record within Patient Care Encounter (PCE) for medications marked as given in BCMA that have been identified as immunizations.  The primary intended use of this option is to queue it as a nightly background task, which will process the previous day’s BCMA administrations of immunizations. Patch PSS\*1\*141 adds the ASSOCIATED IMMUNIZATION field (#9) to the PHARMACY ORDERABLE ITEM file (#50.7). A mapping relationship is created between the PHARMACY ORDERABLE ITEM file (#50.7) and the pointed-to immunization so that a record can be created in the V IMMUNIZATION file (#9000010.11) corresponding to the BCMA administration of an immunization.
For sites running the BCMA2PCE Class III application, please see the Pre-Installation Considerations section for important steps that need to be completed prior to installing the Immunizations Documentation by BCMA Class I application.
*(This page left blank for two-sided copying.)*

# Pre-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this section is to provide considerations prior to installing the Immunizations Documentation by BCMA Class I application.

- All sites should install these patches, even if they are currently using the BCMA2PCE Class III application.
- It is recommended that sites install the software in test accounts prior to installing the application in a production account, but all sites are expected to install the patches to their production VistA system.
- Implementation of the new features, which includes mapping relationships between the PHARMACY ORDERABLE ITEM file (#50.7) and IMMUNIZATION file (#9999999.14) may be performed at the discretion of the local facility.
- For sites running the BCMA2PCE Class III application, you will need to identify existing mapped relationships prior to installing the Immunizations Documentation by BCMA Class I application*.* For sites not running the BCMA2PCE Class III application, it is not necessary to produce any reports from the system prior to installing the Immunizations Documentation by BCMA Class I application.
- Patch PSS\*1\*141 should be installed first, as it is required by patch PSB\*3\*47.
- Both patches can be installed with users on the system.
- Each patch takes less than one minute to install.
- In order to manually validate the *Immunizations Documentation by BCMA Nightly Task* \[PSB PX BCMA2PCE TASK\] option after installation, the user will need access to the PSB MANAGER security key.

## External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA V. 3.0 can only be run in an environment that already has several existing features, such as a standard MUMPS operating system. It also requires the following Department of Veterans Affairs (VA) software packages (versions listed or higher) — and all current patches. Otherwise, BCMA V. 3.0 will *not* be fully functional for your users.

- Inpatient Medications 5.0
- Kernel 8.0
- MailMan 8.0
- Nursing 4.0
- Order Entry/Results 3.0  
  Reporting
- Patient Care Encounter 1.0
- Pharmacy Data 1.0  
  Management
- RPC Broker (32-bit) 1.1
- Toolkit 7.3
- VA FileMan 22.0
- Vitals/Measurements 5.0

  Pharmacy Data Management V.1.0 can only be run in an environment that already has several existing features. It also requires the following Department of Veterans Affairs (VA) software packages (versions listed or higher) — and all current patches. Otherwise, Pharmacy Data Management V. 1.0 will *not* be fully functional for your users.
- National Drug File 4.0
- Outpatient Pharmacy 7.0
- Inpatient Medications 5.0
- Kernel 8.0
- VA FileMan 22.0

## BCMA2PCE Pre-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information is presented as pre-installation considerations for sites currently running the BCMA2PCE Class III application.

### Unschedule AJEY PSB PX BCMA2PCE TASK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For sites running the BCMA2PCE Class III application, your system will need the *BCMA Immunizations to PCE Nightly Task* \[AJEY PSB PX BCMA2PCE TASK\] option unscheduled before installing the Class I application Immunizations Documentation by BCMA. Below is the process for a programmer to unschedule that task.

Select Taskman Management Options: SCHedule/Unschedule Options

Select OPTION to schedule or reschedule: AJEY PSB PX BCMA2PCE TASK

BCMA Immunizations to PCE Nightly Task

...OK? Yes// \<Enter\> (Yes)

Edit Option Schedule

<u>Option Name</u>: AJEY PSB PX BCMA2PCE TASK

Menu Text: BCMA Immunizations to PCE Nightl TASK ID: 1730560

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: NOV 29,2008@01:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **WARNING:** DELETIONS ARE DONE IMMEDIATELY!

(EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)

Are you sure you want to delete this entire record (Y/N)? Y

Select OPTION to schedule or reschedule: \<Enter\>

### Identify Existing Relationships in BCMA2PCE Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For sites running the BCMA2PCE Class III application, it is strongly recommended that you identify existing relationships between the PHARMACY ORDERABLE ITEM file (#50.7) and the IMMUNIZATION file (#9999999.14). The purpose of identifying existing relationships is so you can recreate those same relationships after you install the Class I application Immunizations Documentation by BCMA.

Below is a sample VA FileMan print report that shows one method to identify existing mapped relationships. In the BCMA2PCE Class III application, mapped relationships were stored in the IMMUNIZATION file (#9999999.14). In the Immunizations Documentation by BCMA Class I application, mapped relationships are stored in the PHARMACY ORDERABLE ITEM file (#50.7). You may find that you will map the same immunization to several pharmacy orderable items. 

Select OPTION: PRINT FILE ENTRIES

OUTPUT FROM WHAT FILE: IMMUNIZATION// \<Enter\>

SORT BY: NAME// RELATED RX ORDERABLE ITEM

RELATED RX ORDERABLE ITEM SUB-FIELD: .01 RELATED RX ORDERABLE ITEM

START WITH RELATED RX ORDERABLE ITEM: FIRST// \<Enter\>

WITHIN RELATED RX ORDERABLE ITEM, SORT BY: \<Enter\>

FIRST PRINT FIELD: .01 NAME

THEN PRINT FIELD: RELATED RX ORDERABLE ITEM (multiple)

THEN PRINT RELATED RX ORDERABLE ITEM SUB-FIELD: .01 RELATED RX ORDERABLE ITEM

THEN PRINT RELATED RX ORDERABLE ITEM SUB-FIELD: \<Enter\>

THEN PRINT FIELD: \<Enter\>

Heading (S/C): IMMUNIZATION LIST// \<Enter\>

STORE PRINT LOGIC IN TEMPLATE: \<Enter\>

DEVICE: ;;999 VIRTUAL TERMINAL FOR TELNET

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

IMMUNIZATION LIST DEC 15,2008 16:26 PAGE 1

NAME

RELATED RX ORDERABLE ITEM

--------------------------------------------------------------------------------

TETANUS DIPTHERIA (TD-ADULT)

DIPHTHERIA TOXOID/TETANUS TOXOID

TETANUS TOXOID

TETANUS TOXOID ABSORBED

HEPATITIS B

HEPATITIS B

HEPATITIS B

INFLUENZA

INFLUENZA

INFLUENZA

PNEUMOCOCCAL

PNEUMOCOCCAL VACCINE

HEPATITIS A

HEPATITIS A

HEPA/HEPB ADULT

HEPATITIS A/HEPATITIS B

ZOSTER

ZOSTER VACCINE LIVE (OKA/MERCK)

HUMAN PAPILLOMAVIRUS (HPV)

PAPILLOMAVIRUS HUMAN

TETANUS DIPHTHERIA PERTUSSIS (Tdap)

DIPHTH,PERTUSS(ACELL),TET

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is the step-by-step procedure for installing patches PSS\*1\*141 and PSB\*3\*47. Patch PSS\*1\*141 should be installed first, as it is required by patch PSB\*3\*47.

## Install Patch PSS\*1\*141

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be installed with users on the system. Installation will take less than 1 minute.

 

Suggested time to install: non-peak requirement hours.

1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu.
2.  From the Kernel Installation & Distribution System menu, select the Installation menu.

 

3\. From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter PSS\*1.0\*141):

- Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
- Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
- Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4.  Use the Install Package(s) option and select the package PSS\*1.0\*141.
5.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//”, respond NO.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", respond NO.
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//", respond NO.

## Install Patch PSB\*3\*47

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be loaded with users on the system. Installation will take less than 1 minute.

 

Suggested time to install: non-peak requirement hours.

 

1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu.
2.  From the Kernel Installation & Distribution System menu, select the Installation menu option.
3.  From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter PSB\*3.0\*47) 
- Backup a Transport Global - this option will create a backup message of any routines exported with the patch.  It will NOT backup any other changes such as DDs or templates.
- Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed.  It compares all components of the patch (routines, DDs, templates, etc.).
- Verify Checksums in Transport Global - this option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - this option will allow you to view the components of the KIDS build.
4.  Use the Install Package(s) option and select PSB\*3.0\*47.
5.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//", respond NO.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", respond NO.
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//", respond NO.

## Mapping Relationships Between the PHARMACY ORDERABLE ITEMS File (#50.7) and the IMMUNIZATION File (#9999999.14)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the modified *Edit Orderable Items* \[PSS EDIT ORDERABLE ITEMS\] option that is installed with patch PSS\*1\*141, you can create relationships between a given orderable item (e.g., INFLUENZA INJ) and an immunization (e.g., INFLUENZA). These relationships will also be seen in the *Dispense Drug/Orderable Item Maintenance* \[PSS MAINTAIN ORDERABLE ITEMS\] option. Both options appear on the *Orderable Item Management* \[PSS ORDERABLE ITEM MANAGEMENT\] menu.

Select Orderable Item Management Option: EDIT Orderable Items

This option enables you to edit Orderable Item names, Formulary status,

drug text, Inactive Dates, and Synonyms.

Select PHARMACY ORDERABLE ITEM NAME: INFLUENZA INFLUENZA INJ

Orderable Item -\> INFLUENZA

Dosage Form -\> INJ

List all Drugs/Additives/Solutions tied to this Orderable Item? YES// \<Enter\>

Orderable Item -\> INFLUENZA

Dosage Form -\> INJ

Dispense Drugs:

---------------

INFLUENZA VACCINE

Are you sure you want to edit this Orderable Item? NO// YES

Now editing Orderable Item:

INFLUENZA INJ

Orderable Item Name: INFLUENZA//\<Enter\>

This Orderable Item is Formulary.

This Orderable Item is marked as a Non-VA Med.

Select OI-DRUG TEXT ENTRY: \<Enter\>

INACTIVE DATE: \<Enter\>

DAY (nD) or DOSE (nL) LIMIT: \<Enter\>

MED ROUTE: \<Enter\>

SCHEDULE TYPE: \<Enter\>

SCHEDULE: \<Enter\>

PATIENT INSTRUCTIONS: \<Enter\>

ASSOCIATED IMMUNIZATION: INFLUENZA FLU,3 YRS INFLUENZA

Select SYNONYM: \<Enter\>

*(This page left blank for two-sided copying.)*

# Post Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this section is to provide information for consideration after patches PSS\*1\*141 and PSB\*3\*47 have been installed.

## Validate the Immunizations Documentation by BCMA Nightly Task \[PSB PX BCMA2PCE TASK\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the patch is installed and the mapped relationships between pharmacy orderable items and immunizations are established, run the *Immunizations Documentation by BCMA Nightly Task* \[PSB PX BCMA2PCE TASK\] option, once interactively. This may be done by selecting the option from the *Bar Code Medication AdministrationManager* \[PSB MGR\] menu. Access to this menu requires that the user be a holder of the PSB MANAGER security key.

Validation

“Select START DATE” is the only prompt presented to the user and represents when the application will begin evaluating recorded medication administrations. Valid responses for the Start Date field will be any past date, up to and including yesterday. The option will default to yesterday’s date (T-1). For the purposes of validating the Class I option, this default is acceptable, as long as at least one immunization was recorded via BCMA on the day prior to running the option. If there are no immunizations found by the report for that particular date, nothing will display, and selection of a previous start date (e.g., T-2 or T-3) is appropriate. The option can also be used to backlog entries in the V IMMUNIZATION file (#9000010.11). Sites that have an existing manual process using Clinical Reminder Dialogs or the Computerized Patient Record System (CPRS) Encounter button to record this data may find duplicative data filed by this application, as a new record will be created any time there is a unique combination of patient name, entry date, and immunization name. The potential for unintended duplicates can be reduced by appropriate selection of IMMUNIZATION file (#9999999.14) entries during mapping, especially when there are multiple choices for a given vaccine (e.g., Pneumococcal vs. Pneumo-Vax) and selecting the same immunization entry that is used by local Clinical Reminder dialogs. As shown in the screen capture below, each immunization found will display two lines of data to the screen.

Example: Data Displayed to Screen

Select OPTION NAME: PSB PX BCMA2PCE TASK

Immunizations Documentation by BCMA Nightly Task

Immunizations Documentation by BCMA

Select START DATE: Dec 18, 2008//12-1 (DEC 01, 2008)

BCMAPATIENT, ONE FLU,3 YRS (12/1/08) BCMANURSE, ONE

Result code: 1

BCMAPATIENT, ONE PNEUMOVAX (12/1/08) BCMANURSE, ONE

Result: Immunization already on file.

For each orderable item that is found in which there is an associated immunization, the application will display the patient name, entry date, immunization name, and the person who recorded the BCMA administration. Nothing will display on the screen when there are no BCMA immunizations found for a particular date.

  
Results

Once an immunization is found, the next line will display a result code.

- Result code 1 indicates a successful transmission of data to PCE.
- Result codes -1, -2 and -3 indicate a problem filing the data to PCE.
  - -1 is returned if there were errors in PCE but the data was filed as completely as possible. For example, error code -1 can occur if the nurse who recorded the administration in BCMA does not have a valid and current entry in the PERSON CLASS field (#8932.1).
  - -2 is returned if PCE could not find or create an entry in the VISIT file (#9000010).
  - -3 is returned if PCE was called incorrectly, which is indicative of a problem with this BCMA application.

If the task generates an error code, file a Remedy ticket. If you don’t have access to Remedy please call the VA Service Desk at 1-888-596-4357 and they will file a ticket on your behalf.

A message will be displayed if there is already a record on file for the combination of patient name, entry date, and immunization name. Duplicate data will not be filed.

Example: Result Codes and Existing Records

Select OPTION NAME: PSB PX BCMA2PCE TASK

Immunizations Documentation by BCMA Nightly Task

Immunizations Documentation by BCMA

Select START DATE: Dec 18, 2008//12-1 (DEC 01, 2008)

BCMAPATIENT, ONE FLU,3 YRS (12/1/08) BCMANURSE, ONE

Result code: 1

BCMAPATIENT, ONE PNEUMOVAX (12/1/08) BCMANURSE, ONE

Result: Immunization already on file.

## Queuing the Nightly Background Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the option is confirmed as working correctly, the final step in installation is to queue the option via TaskMan so that it will run nightly. The start time should be after 12:00 midnight, and early enough to avoid interfering with daytime workload. The example shown below uses 1:00 a.m. as a suggestion.

After the task has been queued, there is no specific use of the manual (interactive) option as shown above other than to backlog data, or to correct missing data if the task rescheduling failed. Each time the task runs, it will process the previous day’s administrations from BCMA. Therefore, if it runs successfully on a daily basis, there will be no need to manually run the option.

Select Taskman Management Option: SCHedule/Unschedule Options

Select OPTION to schedule or reschedule: PSB PX BCMA2PCE TASK Immunizations

Documentation by BCMA Nightly Task

Are you adding 'PSB PX BCMA2PCE TASK' as

a new OPTION SCHEDULING (the 116TH)? No// Y (Yes)

Edit Option Schedule

Option Name: PSB PX BCMA2PCE TASK \<Enter\>

Menu Text: Immunizations Documentation by B TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: DEC 20,2008@01:00

DEVICE FOR QUEUED JOB OUTPUT: \<Enter\>

QUEUED TO RUN ON VOLUME SET: \<Enter\>

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS: \<Enter\>

SPECIAL QUEUEING: \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit     Save     Next Page     Refresh

 

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Save                                    Press \<PF1\>H for help    Insert

                   

*(This page left blank for two-sided copying.)*