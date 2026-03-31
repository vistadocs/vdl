---
title: PXRM*2*26 ICD-10 Update Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: ICD-10 Update
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*26
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - taxonomy
  - dialog
  - codes
  - routine
  - filed
  - palli
  - cons
  - dgptxx
  - updating
  - record
page_count: 0
word_count: 24148
section_count: 32
table_count: 7
figure_count: 2
appendix_count: 6
has_toc: False
is_stub: False
pub_date: August 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_26_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_26_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-26-icd-10-update-installation-guide/001.png)

Clinical Reminders

ICD-10 UPDATE

Installation Guide

DG\*5.3\*862

GMPL\*2\*44

PXRM\*2.0\*26

August 2014

Office of Information and Technology (OIT)

Product Development

Table of Contents

Introduction [1](#introduction)

Background [1](#background)

Clinical Reminders ICD-10 Update Project [1](#clinical-reminders-icd-10-update-project)

Patches in this project build [2](#patches-in-this-project-build)

Taxonomy Management Changes [3](#taxonomy-management-changes)

Taxonomy Management Dialog Changes [4](#taxonomy-management-dialog-changes)

Related Documentation [5](#related-documentation)

Related Web Sites [6](#related-web-sites)

Pre-Installation [7](#pre-installation)

1\. Check All Reminder Dialogs for Invalid Items. [7](#check-all-reminder-dialogs-for-invalid-items.)

2\. Run Finding Usage Reports on ICD-9 Diagnosis and CPT-4 Procedures, with “All” selected. [8](#run-finding-usage-reports-on-icd-9-diagnosis-and-cpt-4-procedures-with-all-selected.)

3\. Check Dialogs and Taxonomies for Reused Codes [9](#check-dialogs-and-taxonomies-for-reused-codes)

4\. Review Procedure (CPT) and Diagnosis (POV) Finding Type Parameter [10](#review-procedure-cpt-and-diagnosis-pov-finding-type-parameter)

5\. Reminder Taxonomy Selectable Diagnosis and Selectable Procedure [11](#reminder-taxonomy-selectable-diagnosis-and-selectable-procedure)

6\. Check for Taxonomies With Nonsensically Large Code Ranges [12](#check-for-taxonomies-with-nonsensically-large-code-ranges)

7\. Verify Mail Group Membership [12](#verify-mail-group-membership)

8\. Required Software [13](#required-software)

Installation [13](#installation)

1\. Retrieve the host file containing the multi-package build. [13](#retrieve-the-host-file-containing-the-multi-package-build.)

2\. Install the patch first in a training or test account. [13](#_Toc483268443)

3\. Back up the Reminder Dialog data (801.41); this is necessary if the data must be restored. [14](#back-up-the-reminder-dialog-data-801.41-this-is-necessary-if-the-data-must-be-restored.)

4\. Prevent Extracts and Reports From Running [14](#prevent-extracts-and-reports-from-running)

• Check Pending Extracts [14](#check-pending-extracts)

• Check for PXRM Running/Scheduled Tasks [14](#check-for-pxrm-runningscheduled-tasks)

5\. Load the distribution. [15](#load-the-distribution.)

6\. Backup a Transport Global [15](#backup-a-transport-global)

7\. Compare Transport Global to Current System [16](#compare-transport-global-to-current-system)

8\. Verify Checksums in Transport Global [16](#verify-checksums-in-transport-global)

9\. Install the build [16](#install-the-build)

Post-Install Instructions [17](#post-install-instructions)

Pre and Post-installation Routines [17](#pre-and-post-installation-routines)

1\. Steps for IRM Managers [18](#steps-for-irm-managers)

2\. Steps for Reminder Managers [18](#steps-for-reminder-managers)

3\. Check a dialog using taxonomies in CPRS [20](#check-a-dialog-using-taxonomies-in-cprs)

4\. Modify Reflections terminal emulator set-up (optional) [20](#modify-reflections-terminal-emulator-set-up-optional)

Acronyms [23](#acronyms)

Appendix A: Installation Example [25](#appendix-a-installation-example)

Appendix B: Post-Install Checksums [101](#appendix-b-post-install-checksums)

Appendix C: Finding Usage Report Examples [106](#appendixC)

Appendix D: Check All Active Reminder Dialogs for Invalid Items Example [109](#appendix-d-check-all-active-reminder-dialogs-for-invalid-items-example)

Appendix E: Install File Print Example [110](#appendix-e-install-file-print-example)

Appendix F: Build File Print Example [112](#appendix-f-build-file-print-example)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Background](#background)
  - [Clinical Reminders ICD-10 Update Project](#clinical-reminders-icd-10-update-project)
  - [Patches in this project build](#patches-in-this-project-build)
  - [Taxonomy Management Changes](#taxonomy-management-changes)
  - [## Taxonomy Management Dialog Changes](#taxonomy-management-dialog-changes)
  - [## Related Documentation](#related-documentation)
  - [Related Web Sites](#related-web-sites)
- [Pre-Installation](#pre-installation)
  - [Check All Reminder Dialogs for Invalid Items.](#check-all-reminder-dialogs-for-invalid-items)
  - [Run Finding Usage Reports on ICD-9 Diagnosis and CPT-4 Procedures, with “All” selected.](#run-finding-usage-reports-on-icd-9-diagnosis-and-cpt-4-procedures-with-all-selected)
  - [Check Dialogs and Taxonomies for Reused Codes](#check-dialogs-and-taxonomies-for-reused-codes)
  - [Review Procedure (CPT) and Diagnosis (POV) Finding Type Parameter](#review-procedure-cpt-and-diagnosis-pov-finding-type-parameter)
  - [Reminder Taxonomy Selectable Diagnosis and Selectable Procedure](#reminder-taxonomy-selectable-diagnosis-and-selectable-procedure)
  - [Check for Taxonomies With Nonsensically Large Code Ranges](#check-for-taxonomies-with-nonsensically-large-code-ranges)
  - [Verify Mail Group Membership](#verify-mail-group-membership)
  - [Required Software](#required-software)
- [Installation](#installation)
  - [Retrieve the host file containing the multi-package build.](#retrieve-the-host-file-containing-the-multi-package-build)
  - [Back up the Reminder Dialog data (801.41); this is necessary if the data must be restored.](#back-up-the-reminder-dialog-data-80141-this-is-necessary-if-the-data-must-be-restored)
  - [Prevent Extracts and Reports From Running](#prevent-extracts-and-reports-from-running)
  - [Check Pending Extracts](#check-pending-extracts)
  - [Check for PXRM Running/Scheduled Tasks](#check-for-pxrm-runningscheduled-tasks)
  - [Load the distribution.](#load-the-distribution)
  - [Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [## Install the build](#install-the-build)
  - [# Post-Install Instructions](#post-install-instructions)
  - [Pre and Post-installation Routines](#pre-and-post-installation-routines)
  - [## Steps for IRM Managers](#steps-for-irm-managers)
  - [Steps for Reminder Managers](#steps-for-reminder-managers)
  - [Check a dialog using taxonomies in CPRS](#check-a-dialog-using-taxonomies-in-cprs)
  - [## Modify Reflections terminal emulator set-up (optional)](#modify-reflections-terminal-emulator-set-up-optional)
- [Acronyms](#acronyms)
- [# Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B: Post-Install Checksums](#appendix-b-post-install-checksums)
- [Appendix D: Check All Active Reminder Dialogs for Invalid Items Example](#appendix-d-check-all-active-reminder-dialogs-for-invalid-items-example)
- [Appendix E: Install File Print Example](#appendix-e-install-file-print-example)
- [Appendix F: Build File Print Example](#appendix-f-build-file-print-example)

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The International Classification of Diseases (ICD) is a clinical coding system developed, monitored, and copyrighted by the World Health Organization (WHO). In the United States (US), the National Center for Health Statistics (NCHS), part of the Centers for Medicare and Medicaid Services (CMS), is the agency responsible for overseeing of the clinical modification to the ICD code set.

> On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old ICD-9-CM code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service, or date of discharge for inpatients, that occur on or after the industry activation date. The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven

> alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision-making and outcomes research.

> VA’s Transition to ICD-10: Implementation of ICD-10-CM and PCS is an immense undertaking, requiring system and business changes throughout all HIPAA-covered entities of the health care industry, including the U.S. Department of Veterans Affairs (VA). All inpatient discharges and outpatient encounter dates on or after the compliance date will require ICD-10 codes as the standard code set for recording and reporting diagnosis and inpatient procedures. This transition will impact Information Technology (IT) systems, secondary data stores, forms and business processes and stakeholders at all levels of the organization.

## Clinical Reminders ICD-10 Update Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Clinical Reminders ICD-10 Update project is updating the Clinical Reminders application to allow the use of ICD-10 codes. A very general approach has been taken, wherein Clinical Reminders taxonomies are being restructured to be Lexicon-based instead of pointer-based. This allows the use of any coding system supported by the Lexicon package. In addition to adding ICD-10 codes, SNOMED CT codes are being added. With the release of CPRS 29, SNOMED CT codes can be collected by Problem List and Clinical Reminders will be able to search for them.

## Patches in this project build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PXRM\*2.0\*26

> This build changes Clinical Reminders taxonomies from being pointer-based to being Lexicon-based. A number of things are done to accomplish this. The Reminder Taxonomy data dictionary (file \#811.2) is restructured, a new taxonomy management system is introduced, and taxonomy evaluation is changed to accommodate the new structure. For Reminder Dialogs, users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog, but will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog.

> See the User Manual and the Taxonomy Management and Dialog Management sections of the Clinical Reminders Manager’s Manual for details of changes made by PXRM\*2.0\*26.

> Under the Lexicon-based structure, codes are no longer entered as a range, eliminating the need for taxonomy expansion. The post-install routine in PXRM\*2.0\*26 will convert all existing taxonomies and reminder dialogs to the new structure.

DG\*5.3\*862 - PTF ICD-10 CHANGES FOR CLINICAL REMINDERS

> This build updates the Clinical Reminders Index cross-references in the PTF file (#45) to accommodate ICD-10 diagnosis and procedure codes. It restructures the PTF portion of the Clinical Reminders Index to a generic format that can support all ICD coding systems. This format is:

> ^PXRMINDX (45, CODING SYSTEM,"INP", CODE, NODE, DFN, DATE, DAS)

> ^PXRMINDX (45, CODING SYSTEM,"PNI", DFN, NODE, CODE, DATE, DAS)

> Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. For details, see the Clinical Reminders Index Technical Guide/Programmer’s Manual (PXRM_INDEX_TM).

> The post-install routine will start a background job to rebuild the file \#45 index in the new format.

GMPL\*2.0\*44 - PROBLEM LIST ICD-10 CHANGES FOR CLINICAL REMINDERS

> This build updates the Clinical Reminders Index cross-references in the Problem file (#9000011) to accommodate ICD-10 CM diagnosis codes and SNOMED CT codes. It restructures the Problem List portion of the Clinical Reminders Index to a generic format that can support ICD and SNOMED CT coding systems. This format is:

> ^PXRMINDX (9000011, CODING SYSTEM,”ISPP”, CODE, STATUS, PRIORITY, DFN, DLM, DAS)

> ^PXRMINDX (9000011, CODING SYSTEM,”PSPI”, DFN, STATUS, PRIORITY, CODE, DLM, DAS)

> Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. For details, see the Clinical Reminders Index Technical Manual (PXRM_INDEX_TM).

> The post-install routine will start a background job to rebuild the file \#9000011 index in the new format.

## Taxonomy Management Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reminder taxonomies, stored in file \#811.2, provide a convenient way to create a set of coded values and give the set a name. For example, the VA-DIABETES taxonomy contains a list of ICD diagnosis codes that signify the patient has a diagnosis of diabetes.

> *In the past*, taxonomies were based on pointers to the ICD diagnosis file (#80), the ICD Operation/ Procedure file (#80.1), and the CPT file (#81). Multiple ranges of codes (low code to high code) could be defined for each of these coding systems. When editing was finished, each range of codes was expanded to include all the codes from the low code to the high code. Some coding systems such as SNOMED CT do not assign any meaning to the codes, so they cannot be grouped by code and the concept of a range of codes is meaningless. In some cases, for coding systems that do support the concept of a range, code set updates have inserted an unrelated code into a range.

> *New Approach:* For the above reasons, patch PXRM\*2\*26 changes taxonomies so that they are Lexicon-based. This is a general approach that allows Clinical Reminders taxonomies to support any coding system defined in Lexicon’s Coding Systems file (#757.03), provided Lexicon maintains the coding system and patient data using the coding system is stored in VistA.

> For each coding system it includes, the Coding Systems file defines a three-character abbreviation, nomenclature, source title, and source (e.g., ICD, ICD-9-CM, International Classification of Diseases, Diagnosis, 9th Edition, and US Department of Health and Human Services). The three-character abbreviation provides a convenient way to refer to coding systems and is used by Clinical Reminders Taxonomies. The following coding systems are supported by Clinical Reminders:

| Abbreviation | Nomenclature |
|------------------|------------------|
| 10D              | ICD-10-CM        |
| 10P              | ICD-10-Procedure |
| CPT              | CPT-4            |
| CPC              | HCPCS            |
| ICD              | ICD-9-CM         |
| ICP              | ICD-9-Procedure  |
| SCT              | SNOMED CT        |

> NOTE: PXRM\*2\*26 doesn’t add ICD-10 diagnosis codes to the taxonomies.

## ## Taxonomy Management Dialog Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *In the past*, users created Reminder Dialogs containing ICD-9-CM and/or CPT-4 codes. When using codes as Finding Items or Additional Finding Items in CPRS, the end user didn’t select codes; codes were automatically filed to VistA when the element/group was selected in the Reminder Dialog.

> A Taxonomy could only be used as a Finding Item; it created a pick list of codes for the user to pick from in CPRS. The display in CPRS was controlled by the set-up in the Reminder Finding Parameter File (#801.45) and the Reminder Taxonomy File (#811.2). These controls determined if the Taxonomy should assign codes to the current encounter or an historical encounter. The controls also determined what prompts were assigned to the Reminder Dialog in CPRS.

> *New approach*: Users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog. Users will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog. To maintain similar end user functionality in CPRS, a new prompt called Taxonomy Pick List Display has been added to the dialog editor. This controls how Taxonomies should display in CPRS.

> New Fields

> *Taxonomy Pick List:* This field controls if and what pick lists should appear in CPRS. The possible values are based on the setup of the Taxonomy in the Finding Item Field. If a pick list is set to not display, the active codes marked to be used in a dialog will automatically be filed to PCE for the encounter date for that element when the finish button is clicked. Possible values for this field:

- All = A pick list will display for each code type (ICD/10D and CPT) in taxonomy.
- DX Only = A pick list will display only for ICD/10D codes
- CPT Only = A pick list will display only for CPT codes
- NONE = No pick list for either ICD or CPT. All codes in taxonomy are entered into PCE

> *Diagnosis Header*: This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All. The default value is from the Reminder Finding Type Parameter.

> *Procedure Header*: This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All. The default value is from the Reminder Finding Type Parameter.

> Also, after PXRM\*2.0\*26 is installed, users will no longer be able to set one Taxonomy Element to prompt for both Current and Historical Encounter Data. Users will need to create an element for each encounter type, Current and Historical. If the element Resolution Type is set to Done Elsewhere, then the editor will prompt the user to accept the default prompts for the taxonomy which includes prompts for historical data. Any other resolution type or no resolution type will prompt data for the current encounter date.

> For the ICD-10 implementation, Reminder Dialogs will display ICD-9-CM or ICD-10-CM codes in a pick list based on the code set versioning rules. Reminder Dialogs determine what codes to display using the following rules:

- Current encounters= active codes for that encounter date; Addendums will use the parent note Encounter date.
- Historical encounters= active codes for system date

> Also note that previously dialogs were set to both current and historical encounters. Dialogs are now set to current encounters only. Please review dialogs before using in CPRS. 

> Dialog conversions

- Taxonomies are automatically generated for all dialogs that use ICD-9 diagnosis codes or CPT codes as a finding or additional finding.
- Dialogs with preexisting taxonomies will have the settings from file 801.45 move to the element/group level.
- Dialogs with codes only will generate new taxonomies and the codes will be replaced with taxonomies.
- Dialog elements/groups that are updated will have the edit history updated with the changes due to the data conversion.
- Three MailMan messages will be generated due to the data conversion:
  - A pre-conversion message lists dialogs, elements, and groups to be updated with pre- patched structure.
  - A post-conversion message lists dialogs, elements, and groups with the new structure.
  - A message listing error messages during dialog conversion.

## ## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                  |                         |
|----------------------------------|-------------------------|
| Documentation                    | Documentation File name |
| Release Notes                    | PXRM_2_0_26_RN.PDF      |
| User Manual                      | PXRM_2_0_26_UM.PDF      |
| Manager’s Manual                 | PXRM_2_0_MM.PDF         |
| Technical Manual                 | PXRM_2_0_TM.PDF         |
| Reminders Index Technical Manual | PXRM_INDEX_TM.PDF       |

> **NOTE:** In this document you will see references to both PXRM\*2\*26 and PXRM\*2.0\*26. The difference is that PXRM\*2\*26 is the name of the patch and PXRM\*2.0\*26 is the name of the build.

## Related Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                           |                                                           |                                                                                                  |
|-----------------------------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Site                                                      | URL                                                       | Description                                                                                      |
| National Clinical Reminders site                          | <http://vista.med.va.gov/reminders>                       | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders       |
| National Clinical Reminders Committee                     | <http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx> | This committee directs the development of new and revised national reminders                     |
| VistA Document Library                                    | <http://www.va.gov/vdl/>                                  | Contains manuals for Clinical Reminders and related applications.                                |
| Health Information Management (HIM) ICD-10 Implementation | <http://vaww.vhahim.va.gov/>                              | Contains general information, training resources, and other tools for VA’s transition to ICD-10. |

# Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch includes pre-install steps to be *<u>completed a day before the actual install</u>* of PXRM\*2.0\*26 by the IRM staff and a Reminder Manager. These pre-install steps are highly recommended due to the data conversion for both taxonomies and dialogs. Please coordinate between the IRM staff and your Reminder Manager to complete.

- Run the “Check All Reminder Dialogs for Invalid Items” report. This identifies any dialogs that require clean-up before the data conversion, as they may cause errors during the install.
- Run the Finding Usage Report, to be used for troubleshooting purposes after the data has been converted.
- Review the Finding Type Parameter List and verify that there is a meaningful description defined for the Prefix/Suffix for each Enabled Resolution Status for CPT and POV parameters.
- Verify that at least one Reminder Manager is assigned to the Clinical Reminders mail group.

## Check All Reminder Dialogs for Invalid Items. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This will list issues with the set-up of any of the Reminder Dialog. You can use this report to do any clean-up before installing PXRM \*2.0\*26. Also, it can be used to troubleshoot any error messages that are auto-generated from the post conversion message. See example in [Appendix D](#appendix-d-check-all-active-reminder-dialogs-for-invalid-items-example).

- Access the Dialog Management menu and select the Reminder Dialog Reports.
- Select “All” to run the Check All Active Reminder Dialog for Invalid Items.
- Review report output with the table below and clean up, as needed.

> Select Reminder Dialog Management \<TEST ACCOUNT\> Option: DR Dialog Reports

> OR Reminder Dialog Elements Orphan Report

> ER Empty Reminder Dialog Report

> ALL Check all active reminder dialog for invalid items

> CH Check Reminder Dialog for invalid items

> Select Dialog Reports Option: ALL Check all active reminder dialog for invalid items

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 16%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Clean-up Needed</p>
</blockquote></th>
<th><blockquote>
<p>Clean-up Not Needed</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Disabled dialog items in the dialog</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Incomplete sequences in the dialog</p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>All sub-items in the dialog are pointing to a valid entry on the system</p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>All finding items, additional finding items, and orderable items are pointing to a valid entry on the system</p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Result groups are pointing to a valid MH Test and a MH scale has been defined for the result group</p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>An odd number of “|” characters in a dialog text field. If this is the case, it would not be possible to determine which part is a TIU Object</p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Progress Note Text and the Alternate Progress Note text fields have valid TIU Objects and TIU Template Field</p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## Run Finding Usage Reports on ICD-9 Diagnosis and CPT-4 Procedures, with “All” selected. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See example in [Appendix C](#appendixC).

- Access the Reminder Reports menu on the Reminder Manager’s Menu.
- Enter “FUR” from the Select Reminder Reports Option.
- Select Taxonomy, ICD9 Diagnosis and Procedure reminder findings and “All.”
- Review and retain these reports, as these can be used for troubleshooting after PXRM\*2.0\*26 has been installed.
  - Identify which dialogs use codes as finding items or additional finding.
    - For Taxonomy “types” of finding….
      - Identify which dialogs use taxonomies as finding items.
      - Used to update taxonomies with ICD-10 codes.

> Select Reminder Managers Menu Option: RP Reminder Reports

> RD Reminders Due Report

> RDU Reminders Due Report (User)

> RDT User Report Templates

> EPT Extract EPI Totals

> EPF Extract EPI List by Finding and SSN

> EQT Extract QUERI Totals

> GEC GEC Referral Report

> REV Review Date Report

> FUR Finding Usage Report

> Select Reminder Reports Option: FUR

> Clinical Reminders Finding Usage Report

> Select from the following reminder findings (\* signifies standardized):

## Check Dialogs and Taxonomies for Reused Codes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A reused code is a code that the standards development organization has inactivated and then sometime later reactivated with a different meaning. An example is the CPT code 90714.

Code Activation Inactivation UID Description

--------- ---------- ------------ --- -----------

90714 06/01/1994 04/01/1999 Active Immunization of Typhoid

Vaccine

07/01/2005 Tetanus and Diphtheria Toxoids

(TD) Adsorbed, Preservative Free,

when Administered to Individuals 7

Years or Older, for Intramuscular

use

> When a reused code is included in a taxonomy and marked as “Use in Dialog”, a defect in CPRS GUI version 29 always causes the description from the first activation period, regardless of the encounter date, to populate the Provider Narrative in PCE. CPRS GUI version 30.A, which is expected to be released in August 2014, corrects this defect.

> This defect more heavily impacts reminder taxonomies containing CPT codes for immunizations but is not limited to a specific code set. Reused codes can be found in the ICD-9, CPT, and HPCS code sets. You can run the Finding Usage report in step two and see if any reused codes on the list below are in the results. Also, use the Finding Usage report to find any taxonomies that are being used in a dialog. If any such taxonomies are found, use taxonomy inquiry to determine if the taxonomy contains any reused codes; if it does, use one of the workarounds described below.

> Before CPRS GUI version 30.A is released, you can prevent incorrect provider narrative text being stored for a reused CPT or HCPCS code using the workarounds below. Note that prior to the installation of PXRM\*2\*26, HCPCS codes are treated as CPT codes in Clinical Reminders.

> Workaround 1: For immunizations and skin tests, setup the reminder dialog to use the immunization or skin test instead of the CPT code via a taxonomy. The PCE Code Mapping File capability can be used to automatically store the CPT code. You will need to make sure that the CPT code is properly mapped in the code mapping file. If you need assistance with this, please enter a Remedy ticket.

> Workaround 2: In all other cases, instead of using a dialog to file the code, use the CPRS Encounter Form.

> The Standards and Terminology Service Team has provided the following list of reused codes:

> <u>9 ICD-9 diagnosis codes</u>

> 282.40 282.43 282.44 282.45 282.46 282.47 284.01 284.09

> 284.89

> <u>6 ICD-9 procedure codes</u>

> 02.21 32.41 39.81 81.18 89.49 99.78

> <u>150 CPT/HCPCS codes</u>

> 0001F 0005F 1127F 1128F 21011 22010 22206 22207

> 22552 27415 27416 31620 31626 31627 31651 33782

> 33783 35637 35638 43845 46930 49440 75956 77425

> 78582 82656 83631 83700 83861 86305 86335 86357

> 86386 90460 90650 90653 90654 90714 90951 90952

> 90953 90954 90955 90956 90957 90958 90966 90967

> 90968 90969 93280 93890 95017 95018 99150 99174

> A4252 A4349 A4360 A4363 A4520 A4555 A4600 A4648

> A4650 A7020 A9180 A9520 B4157 B4159 B4161 D2970

> D6710 E0170 E0670 E1036 E1352 E1354 E1356 E1392

> G0159 G0160 G0161 G0163 G0164 G0428 G0429 J0151

> J0180 J0220 J0400 J0480 J0490 J0840 J0890 J1050

> J1290 J1300 J1430 J1561 J1562 J1640 J1740 J1741

> J1930 J2170 J2850 J3060 J3110 J3300 J3355 J7180

> J7196 J7315 J7316 J7508 J7610 J7615 J7620 J7627

> J7640 J7645 J7650 J7660 J7665 J7670 J9330 L3916

> L3918 L3924 L3930 L5703 L6715 L6880 L8605 L8615

> L8616 L8617 L8618 L8621 L8622 L8623 L8624 L8627

> L8628 L8629 L8680 L8690 Q0161 T2049

## Review Procedure (CPT) and Diagnosis (POV) Finding Type Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Access Reminder Dialog Management, Dialog Parameters, General Finding Type Parameter option.

- Select the Item Finding Type Parameter and review the Prefix/Suffix values for Procedure (CPT) and Diagnosis (POV) finding types. These are pre-populated by the software but can be edited at the element. The intent of this step is to verify that the values display a meaningful description in CPRS.

> ![](pxrm-2-26-icd-10-update-installation-guide/002.png)

- Example in CPRS where the prefix and suffix has been edited during the element set-up. ‘Dx recorded at encounter.’ and ‘Px done at encounter.’

> ![](pxrm-2-26-icd-10-update-installation-guide/003.png)

- Review the Resolution Status type Enabled/Disable values for both CPT and POV entries.

> ![](pxrm-2-26-icd-10-update-installation-guide/004.png)

- If both Done at Encounter and Done Elsewhere are enabled, any dialog using a taxonomy that contains codes for the finding parameter will no longer work the same in CPRS.
- With PXRM\*2.0\*26, the dialog will only support one resolution status per element. The conversion process will set the existing element to Done At Encounter. If the dialog should support both a Done At Encounter and a Done Elsewhere, the site should do the following after the patch has been installed:
  - Create a new element for the Done Elsewhere Status.
  - Create a group that contains both the Done At Encounter and the Done Elsewhere Elements.
  - Replace the current element in the dialog with the new group.

## Reminder Taxonomy Selectable Diagnosis and Selectable Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reminder taxonomies contain two multiples named SELECTABLE DIAGNOSIS and SELECTABLE PROCEDURE. During the post-init when taxonomies are converted to the new data structure, any codes in these multiples that are not already in the Selected Codes multiple will be moved there with a TERM/CODE of “Copy from selectable diagnosis” and “Copy from selectable procedure”; these codes will be marked as Use In Dialog. After these codes have been moved, you can edit the taxonomy and delete any of the codes you don’t want. It should be noted that if the build is installed again, the Selectable Diagnosis and Selectable Procedure codes will be moved again and you will have to delete them again. If your site is a test site, or if you will be installing the build more than once for some other reason, there is an alternative to having to edit the taxonomy after each install. You can use FileMan Search File Entries to find all your taxonomies that contain Selectable Diagnosis or Selectable Procedure codes. For each of these taxonomies, you can use FileMan Enter or Edit File entries to delete any codes that you do not want moved to the Selected Codes multiple.

## Check for Taxonomies With Nonsensically Large Code Ranges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Extremely large code ranges do not make sense clinically and can cause a store error during the taxonomy conversion process. The store error will prevent the PXRM\*2.0\*26 installation from completing, so it is a good idea to make sure you do not have any taxonomies with nonsensically large code ranges. The easiest way to do this is to use FileMan’s Search File Entries on file \#811.3 (Expanded Taxonomies) and check for large values of the fields NICD0, NICD9, and NICPT; these fields are the total number of codes of each type. A large value would be something over 1500. Here is an example for NICD9:

> VA FileMan 22.0

> Select OPTION: SEARCH FILE ENTRIES

> OUTPUT FROM WHAT FILE: EXPANDED TAXONOMIES//

> -A- SEARCH FOR EXPANDED TAXONOMIES FIELD: NICD9

> -A- CONDITION: \> GREATER THAN

> -A- GREATER THAN: 1500

> -B- SEARCH FOR EXPANDED TAXONOMIES FIELD:

> IF: A// NICD9 GREATER THAN "1500"

> STORE RESULTS OF SEARCH IN TEMPLATE:

> SORT BY: NUMBER//

> START WITH NUMBER: FIRST//

> FIRST PRINT FIELD: .01 EXPANDED TAXONOMY

> THEN PRINT FIELD: NICD9

> THEN PRINT FIELD:

> Heading (S/C): EXPANDED TAXONOMIES SEARCH Replace

> DEVICE:

> Since these fields are the total number of codes of each type, it may be that there are just a large number of ranges defined and not a single large range. To check for a single large range, do an inquiry on any taxonomy that was found by the FileMan searches and examine each range that is defined. Correct any that are too large to be clinically relevant.

## Verify Mail Group Membership

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Verify that there is at least one Reminder Manager assigned to the Clinical Reminder mail group. Inquire to file \#800 CLINCIAL REMINDER PARAMETERS SITE PARAMETERS.  There is a field: REMINDER MANAGEMENT MAILGROUP: that will list your local mailgroup to check for members.

## Required Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *PXRM\*2.0\*26*

| Package/Patch      | Namespace | Version | Comments      |
|--------------------|-----------|---------|---------------|
| Clinical Reminders | PXRM      | 2       | Fully patched |
| DRG Grouper        | ICD       | 18.0    | ICD\*18.0\*57 |
| Lexicon Utility    | LEX       | 2       | LEX\*2.0\*80  |
| Kernel             | XU        | 8.0     | Fully patched |
| VA FileMan         | DI        | 22      | Fully patched |

> *DG\*5.3\*862 *

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Package/Patch</td>
<td>Namespace</td>
<td>Version</td>
<td>Comments</td>
</tr>
<tr class="even">
<td><p>Registration</p>
<p>DG*5.3*478</p></td>
<td>DG</td>
<td>5.3</td>
<td></td>
</tr>
</tbody>
</table>

> *GMPL\*2.0\*44 *

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Package/Patch</td>
<td>Namespace</td>
<td>Version</td>
<td>Comments</td>
</tr>
<tr class="even">
<td><p>Problem List</p>
<p>GMPL*2.0*43</p></td>
<td>GMPL</td>
<td>2.0</td>
<td></td>
</tr>
</tbody>
</table>

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to install the multi-package build that includes patches DG\*5.3\*862, GMPL\*2.0\*44, and PXRM\*2.0\*26.

> IMPORTANT: Install this build in your production accounts during non-peak/off-hours. The PXRMINDEX Global will be rebuilt for files 45 and 9000011,and reminder evaluation will be disabled while these indexes are rebuilding.

> Estimated installation time is 10- 15 minutes; re-indexing time is 10 minutes to 3 hours.

> *The installation needs to be done by a person with DUZ(0) set to "@."*

## Retrieve the host file containing the multi-package build. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use ftp to access the build (the name of the host file is CR_ICD-10_UPDATE .KID) from one of the following locations (with the ASCII file type):

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span id="_Toc483268443" class="anchor"></span><span class="mark">REDACTED</span> \\

> Install the patch first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality.

## Back up the Reminder Dialog data (801.41); this is necessary if the data must be restored.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Back up data using your site’s policy for backing up data.
- If the steps are unknown. here is a way it can be done:
  - Go to a command prompt.
  - At the prompt, enter D GOGEN^%ZSPECIAL.
  - At the device prompt, enter the name of the local directory where the file is to be stored with the name of the file. (FILE_801_41_DATA_BACKUP.GBL)
  - At the Parameters? Prompt, press \<enter\>.
  - At the Global prompt, enter ^PXRMD(801.41.
  - Verify that the file was created and exists in the directory specified.

Example

> DEV5A4:DVFDEV\>D GOGEN^%ZSPECIAL

> Device: VA5\$:\[Local Directory\]FILE_801_41_DATA_BACKUP.GBL

> Parameters? ("WNS") =\>

> Warning: Use a "V" format to avoid problems with control characters.

> Global ^PXRMD(801.41,

> Global ^

> .

## Prevent Extracts and Reports From Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Check Pending Extracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Contact your Reminders Manager to assist with this step
- Access the Reminder Extract Menu and select Reminder Extract Management.
- For each Extract listed, check the View/Schedule Extract to see if any are scheduled to run around the time of installation. If so, these will have to be re-scheduled. This can be done by using the Taskman Schedule/ Unscheduled Options

## Check for PXRM Running/Scheduled Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- From TaskMan Management search for any Clinical Reminders or PXRM tasks.
- Look to see if there are any scheduled tasks to start or run around the installation time or during the re-indexing of the globals. (Re-indexing may take up to 3 hours after the installation is finished. During the re-indexing clinical reminder evaluation will be disabled.)
- If any tasks are identified, these must be rescheduled after the re-indexing.
- When reminder evaluation is disabled a MailMan message will be sent to the Clinical Reminders mail group notifying the members that evaluation has been disabled.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In programmer mode, type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD INSTALLATION MENU), , and then the option LOAD a Distribution. Enter the directory name where you placed the host file followed by CR_ICD-10_UPDATE.KID at the Host File prompt.

> Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: VA5\$:\[DOWNLOADS\]CR_ICD-10_UPDATE.KID

> KIDS Distribution saved on NOV 27: CR_ICD-10_UPDATE.KID

> From the Installation menu, you may elect to use the following options:

## Backup a Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Installation option, Backup a Transport Global \[XPD BACKUP\]. This option creates a MailMan message that will back up all current routines on your VistA/M system that will be replaced by the packages in this transport global. (If you need to preserve components that are not routines, you must back them up separately.)  

> At the Select INSTALL NAME: prompt, enter Clinical Reminders ICD-10 Update 1.0

> Example:

> Select Installation  \<TEST ACCOUNT\> Option: 5  Backup a Transport Global

> Select INSTALL NAME:   <span class="mark">CLINICAL REMINDERS ICD-10 UPDATE 1.0</span>      6/27/13@13:07:40

>      =\> Clinical Reminders ICD-10 Update; Created on Jun 19, 2013@08:20:53

> This Distribution was loaded on Jun 27, 2013@13:07:40 with header of

>    Clinical Reminders ICD-10 Update; Created on Jun 19, 2013@08:20:53

>    It consisted of the following Install(s):

> CLINICAL REMINDERS ICD-10 UPDATE 1.0     DG\*5.3\*862    GMPL\*2.0\*44

>     PXRM\*2.0\*26

> Subject: Backup of CLINICAL REMINDERS ICD-10 UPDATE 1.0 install on Jun 2

>   Replace

> No routines for CLINICAL REMINDERS ICD-10 UPDATE 1.0

> Loading Routines for DG\*5.3\*862

> Routine DG53862I is not on the disk...

> Loading Routines for GMPL\*2.0\*44

> Routine GMPLP44I is not on the disk...

> Loading Routines for PXRM\*2.0\*26.....

> Routine PXRMCPLS is not on the disk...............

> Routine PXRMDTAX is not on the disk..

> Routine PXRMDUTL is not on the disk...................................

> Routine PXRMLEXL is not on the disk......

> Routine PXRMP26D is not on the disk..

> Routine PXRMP26E is not on the disk..

> Routine PXRMP26I is not on the disk..

> Routine PXRMP26X is not on the disk.........

> Routine PXRMSCR is not on the disk...

> Routine PXRMSINQ is not on the disk.......

> Routine PXRMTAXL is not on the disk....

> Routine PXRMTXCE is not on the disk..

> Routine PXRMTXCR is not on the disk..

> Routine PXRMTXCS is not on the disk..

> Routine PXRMTXIM is not on the disk..

> Routine PXRMTXIN is not on the disk..

> Routine PXRMTXSM is not on the disk..

> Routine PXRMUIDR is not on the disk..........

> Send mail to: PXRMPROGRAMMER, ONE

> Select basket to send to: IN// PATCH BACKUP 

> And Send to:

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## Verify Checksums in Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

> Example

> CHOOSE 1-2: 2 Verify Package Integrity

> Select BUILD NAME: PXRM\*2.0\*26 CLINICAL REMINDERS

> Want each Routine Listed with Checksums: Yes// YES

> DEVICE: HOME// ;;999 TELNET PORT

## ## Install the build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build CLINICAL REMINDERS ICD-10 UPDATE 1.0 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: CLINICAL REMINDERS ICD-10 UPDATE 1.0

> Answer the following install questions as follows:

- Although typically the answer is "No," you can answer "Yes," to the question:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install?

> *Please remember that rebuilding menu trees will increase patch installation time.*

- Answer "No" to the question:

> Want KIDS to INHIBIT LOGONs during the install?

- Answer "No" to the question:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols?

The post-inits for DG\*5.3\*862 and GMPL\*2.0\*44 will start a TaskMan job to rebuild their portions of the Clinical Reminders Index. While these indexes are rebuilding, reminder evaluation will be disabled.

When these indexes are finished rebuilding, reminder evaluation will be enabled and Clinical Reminders should now be available in CPRS. A MailMan message will be sent to the Clinical Reminders mail group notifying the members that evaluation has been enabled.

## # Post-Install Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre and Post-installation Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pre-install: PXRM\*2.0\*26 renames the option PXRM TAXONOMY MANAGEMENT to PXRM TAXONOMY MANAGEMENT (OLD) and makes it unavailable to users.

> Post-install: During the post-install, a number of conversions are performed, as described earlier in this manual.

> After a successful installation, the init routines PXRMP26D, PXRMP26E, PXRMP26I, PXRMP26T, and PXRMP26X can be deleted.

Mail Messages

- In the post-install, DG\*5.3\*862 starts a background job that will rebuild ^PXRMINDX (45) in the new format. This job will generate one or two messages to the Clinical Reminders mail group. One message will give the status of the rebuild, and tell if any errors or problems were encountered. If there were problems, another message will be sent with the details of the errors or problems. If bad data is encountered in PTF and you need assistance dealing with it, you can submit a support ticket. After a successful installation, the init routine DG53862I can be deleted.
- In the post-install, GMPL\*2.0\*44 starts a background job that will rebuild ^PXRMINDX (9000011) in the new format. This job will generate one or two messages to the Clinical Reminders mail group. One message will give the status of the rebuild and tell if any errors or problems were encountered. If there were problems, another message will be sent with the details of the errors or problems. During testing, many sites have found that they have some corrupted entries in the Problem List file. Some typical examples seen in the MailMan message are:

> Subject: CLINICAL REMINDER INDEX BUILD ERROR(S) FOR GLOBAL ^AUPNPROB(

> GLOBAL: ^AUPNPROB( ENTRY: 1102 missing date last modified

> GLOBAL: ^AUPNPROB( ENTRY: 214464 has the invalid code -1^Invalid IEN for File

> GLOBAL: ^AUPNPROB( ENTRY: 214385 has the invalid code -1^Invalid IEN for File

> GLOBAL: ^AUPNPROB( ENTRY: 183670 missing DFN

> GLOBAL: ^AUPNPROB( ENTRY: 183669 missing DFN

> It is suggested that a facility representative who has the authority to review content evaluate the  status of a problem entry and make updates, including changes to the status of the problem. CACs and/or HIM representatives could be used for this task. Some suggested steps to resolve the corrupted data problems are:

- Use FileMan inquire for each entry with the IEN by entering \`NNNN to obtain details of the specific Problem List record. 
- Using CPRS and the Problems tab, view the problem to determine the current status.
- If it is active, review the entry to determine if there is any appearance of corrupt or invalid data. It should be noted that the issues found may likely be old and may not have been user-added. Take appropriate corrective action, such as inactivation and/or change of status to remove the invalid data, with annotation in the comments that the entry was reviewed and appears to be invalid, as identified with the GMPL\*2.0\*44 build install. The use of annotation via comments will ensure that proper documentation in the record is retained for any action taken. 
- If not active, verify that the problem cannot be currently used, and add notation that the entry appears to be invalid via comments, with no further action. The use of annotation via comments will ensure that proper documentation in the record is retained for any action taken.
- If you require additional assistance you can submit a support ticket. 

> After a successful installation, the init routine GMPLP44I can be deleted.

- As part of a post-install routine, a MailMan message listing the dialog and the elements of the dialogs that were affected by the conversion will be sent.

## ## Steps for IRM Managers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Review PXRM\*2.0\*26 Install file entry for any error messages; if found, then contact the Reminder Manager at your site.
- Distribute a copy of the Install File Entry to the Reminder Manager.

## Steps for Reminder Managers 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Three MailMan messages are generated as a result of the dialog conversion and sent to the Clinical Reminders mail group. Please review the messages for errors and validate the dialog conversion, using the pre- and post-conversion messages to do a manual side-by-side comparison.

1)  Review for failed dialog conversions listed as an error MailMan message.

![](pxrm-2-26-icd-10-update-installation-guide/005.png)

2)  Pre-conversion Mailman message:

PB-FLU VACC GIVEN

 =======================================================

          Resolution Type:

             Finding Item: ICD9.V04.81

  

 Additional Finding Items:

     Items: CPT.90471

     Items: CPT.90658

  

     Components:

     Sequence: 10 Prompt PXRM PRIMARY DIAGNOSIS Exclude From PN Text:Yes
3)  Post-conversion Mailman message:

> When taxonomies are created during conversion, the name of the dialog element/group they are contained in is the name of the new taxonomy.

![](pxrm-2-26-icd-10-update-installation-guide/006.png)

## Check a dialog using taxonomies in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Check a dialog that contains one of the taxonomies that you compared in the reports, to ensure that the dialog functions as expected. If you spot any problems or have questions, log a Remedy ticket.

## ## Modify Reflections terminal emulator set-up (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to improve the appearance of the new taxonomy management system, it is recommended that users check their Reflections terminal emulator setup, and make sure that the background is changed from the default color white.

> The foreground can be whatever color the user prefers to use with the chosen background.

> ![](pxrm-2-26-icd-10-update-installation-guide/007.png)

> Figure 1: Terminal Setup

Missing text when printing tip

You may notice when printing large amounts of text to the screen, parts of it are missing. To fix this, the Reflections setup must have Save from Scrolling Regions checked. The sequence is: Setup =\> Display =\> Screen =\> Display Memory Advanced.

![](pxrm-2-26-icd-10-update-installation-guide/008.png)

Figure 2: Display Setup

![](pxrm-2-26-icd-10-update-installation-guide/009.png)

Figure 3: Save from scrolling regions

\*NOTE – KNOWN ANOMALY:

In List Manager displays, for any action that works with a list, you can select the list and then the action or select the action and then the list. In the first case, the system uses List Manager’s list selection, which displays the list as a string of items. If the list has too many items, it generates an error. To prevent this, select the action first.

For example, on the code selection screen, if you do an ICD-10 Lexicon search for diabetes, you will see a list of around 250 codes. If you enter 1-250 at the Select Action prompt, you’ll get a range error. However, if you select Add, then you can enter 1-250 and not get an error.

<u>Lexicon Selection Nov 14, 2013@11:16:15 Page: 57 of 57</u>

Term/Code: diabetes

253 ICD-10-CM codes were found.

<u>+No. Code Active Inactive Description</u>

Gestational Diabetes

250 P70.2 10/1/2014 Neonatal diabetes mellitus

251 Z13.1 10/1/2014 Encounter for Screening for Diabetes

Mellitus

252 Z83.3 10/1/2014 Family History of Diabetes Mellitus

253 Z86.32 10/1/2014 Personal History of Gestational Diabetes

+ Next Screen - Prev Screen ?? More Actions

ADD Add to taxonomy UID Use in dialog

RFT Remove from taxonomy SAVE Save

RFD Remove from dialog

Select Action: Quit// 1-250

<span class="mark">\>\>\> Range too large: 1-250.</span>

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OIT Master Glossary is available at <http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm>
> National Acronym Directory:
> <http://vaww1.va.gov/Acronyms/>
| Term       | Definition                                                                      |
|------------|---------------------------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                                              |
| Clin4      | National Customer Support team that supports Clinical Reminders                 |
| CPRS       | Computerized Patient Record System                                              |
| DBA        | Database Administration                                                         |
| DG         | Registration and Enrollment Package namespace                                   |
| ESM        | Enterprise Systems Management (ESM)                                             |
| FIM        | Functional Independence Measure                                                 |
| GMPL       | Problem List namespace                                                          |
| GMTS       | Health Summary namespace (also HSUM)                                            |
| GUI        | Graphic User Interface                                                          |
| HRMH/HRMHP | High Risk Mental Health Patient                                                 |
| IAB        | Initial Assessment & Briefing                                                   |
| ICD-10-CM  | International Classification of Diseases, 10th Revision Clinical Modification   |
| ICD-9-CM   | International Classification of Diseases, Ninth Revision, Clinical Modification |
| ICR        | Internal Control Number                                                         |
| IOC        | Initial Operating Capabilities                                                  |
| LSSD       | Last Service Separation Date                                                    |
| MH         | Mental Health                                                                   |
| OHI        | Office of Health Information                                                    |
| OI         | Office of Information                                                           |
| OIT/OI&T   | Office of Information Technology                                                |
| OMHS       | Office of Mental Health Services                                                |
| ORR        | Operational Readiness Review                                                    |
| PCS        | Patient Care Services                                                           |
| PD         | Product Development                                                             |
| PIMS       | Patient Information Management System                                           |
| PMAS       | Program Management Accountability System                                        |
| PTM        | Patch Tracker Message                                                           |
| PXRM       | Clinical Reminder Package namespace                                             |
| RSD        | Requirements Specification Document                                             |
| SD         | Scheduling Package Namespace                                                    |
| SG         | Scheduling, Registration, Admission/Discharge/Transfer namespace                |
| SME        | Subject Matter Expert                                                           |
| SNOMED CT  | Systematic Nomenclature of Medicine of Clinical Terms                           |
| SQA        | Software Quality Assurance                                                      |
| VA         | Department of Veteran Affairs                                                   |
| VHA        | Veterans Health Administration                                                  |
| VISN       | Veterans Integrated Service Network                                             |
| VistA      | Veterans Health Information System and Technology Architecture                  |

# # Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a capture of a Clinical Reminders ICD-10 Update installation that provides details of the install. This copy should be forwarded to the CAC who maintains Clinical Reminders to help them understand what data is being converted

Example: First-time Install

Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

Select INSTALL NAME: CLINICAL REMINDERS ICD-10 UPDATE 1.0 5/9/14@09:59:23

=\> Clinical Reminders ICD-10 Update ;Created on May 08, 2014@12:35:09

This Distribution was loaded on May 09, 2014@09:59:23 with header of

Clinical Reminders ICD-10 Update ;Created on May 08, 2014@12:35:09

It consisted of the following Install(s):

CLINICAL REMINDERS ICD-10 UPDATE 1.0 DG\*5.3\*862 GMPL\*2.0\*44

PXRM\*2.0\*26

Checking Install for Package CLINICAL REMINDERS ICD-10 UPDATE 1.0

Install Questions for CLINICAL REMINDERS ICD-10 UPDATE 1.0

Checking Install for Package DG\*5.3\*862

Install Questions for DG\*5.3\*862

Checking Install for Package GMPL\*2.0\*44

Install Questions for GMPL\*2.0\*44

Checking Install for Package PXRM\*2.0\*26

Install Questions for PXRM\*2.0\*26

Incoming Files:

801.41 REMINDER DIALOG

> **NOTE:** You already have the 'REMINDER DIALOG' File.

801.45 REMINDER FINDING TYPE PARAMETER (including data)

> **NOTE:** You already have the 'REMINDER FINDING TYPE PARAMETER' File.

I will OVERWRITE your data with mine.

802.4 REMINDER FUNCTION FINDING FUNCTIONS (including data)

> **NOTE:** You already have the 'REMINDER FUNCTION FINDING FUNCTIONS' File.

I will OVERWRITE your data with mine.

811.2 REMINDER TAXONOMY

> **NOTE:** You already have the 'REMINDER TAXONOMY' File.

811.4 REMINDER COMPUTED FINDINGS (including data)

> **NOTE:** You already have the 'REMINDER COMPUTED FINDINGS' File.

I will OVERWRITE your data with mine.

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

--------------------------------------------------------------------------------

Install Started for CLINICAL REMINDERS ICD-10 UPDATE 1.0 :

May 09, 2014@10:00:16

Build Distribution Date: May 08, 2014

Installing Routines:

May 09, 2014@10:00:16

Install Started for DG\*5.3\*862 :

May 09, 2014@10:00:16

Build Distribution Date: May 08, 2014

Installing Routines:

May 09, 2014@10:00:16

Running Post-Install Routine: POST^DG53862I

Creating Clinical Reminders Index cross-references.

Creating PTF ICD diagnosis cross-references.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, HOLD ON...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...SORRY, HOLD ON...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, JUST A MOMENT PLEASE...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...SORRY, THIS MAY TAKE A FEW MOMENTS...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, HOLD ON...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...HMMM, HOLD ON...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...SORRY, HOLD ON...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...HMMM, I'M WORKING AS FAST AS I CAN...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling DG701 Input Template of File 45.........

'DGPTX7' ROUTINE FILED.............

'DGPTX71' ROUTINE FILED.

'DGPTX72' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG PTF CREATE PTF ENTRY Input Template of File 45......

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...HMMM, THIS MAY TAKE A FEW MOMENTS...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating PTF ICD procedure cross-references.

Creating index definition ...

Compiling DG401 Input Template of File 45..

'DGPTX4' ROUTINE FILED.............

'DGPTX41' ROUTINE FILED.

'DGPTX42' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...HMMM, I'M WORKING AS FAST AS I CAN...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG401 Input Template of File 45..

'DGPTX4' ROUTINE FILED.............

'DGPTX41' ROUTINE FILED.

'DGPTX42' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG401 Input Template of File 45..

'DGPTX4' ROUTINE FILED.............

'DGPTX41' ROUTINE FILED.

'DGPTX42' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...SORRY, JUST A MOMENT PLEASE...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG401 Input Template of File 45..

'DGPTX4' ROUTINE FILED.............

'DGPTX41' ROUTINE FILED.

'DGPTX42' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, HOLD ON...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling DG401 Input Template of File 45..

'DGPTX4' ROUTINE FILED.............

'DGPTX41' ROUTINE FILED.

'DGPTX42' ROUTINE FILED.

Compiling Cross-Reference(s) 45 of File 45.

...SORRY, JUST A MOMENT PLEASE...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, HOLD ON...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling Cross-Reference(s) 45 of File 45.

...HMMM, THIS MAY TAKE A FEW MOMENTS...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling Cross-Reference(s) 45 of File 45.

...EXCUSE ME, JUST A MOMENT PLEASE...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

Creating index definition ...

Compiling Cross-Reference(s) 45 of File 45.

...SORRY, THIS MAY TAKE A FEW MOMENTS...

'DGPTXX1' ROUTINE FILED.

'DGPTXX2' ROUTINE FILED.

'DGPTXX3' ROUTINE FILED.

'DGPTXX4' ROUTINE FILED.

'DGPTXX5' ROUTINE FILED.

'DGPTXX6' ROUTINE FILED.

'DGPTXX7' ROUTINE FILED.

'DGPTXX8' ROUTINE FILED.

'DGPTXX9' ROUTINE FILED.

'DGPTXX10' ROUTINE FILED.

'DGPTXX11' ROUTINE FILED.

'DGPTXX12' ROUTINE FILED.

'DGPTXX' ROUTINE FILED.

PTF Clinical Reminders Index rebuild queued.

The task number is 299178.

Updating Routine file...

Updating KIDS files...

DG\*5.3\*862 Installed.

May 09, 2014@10:00:21

Not a production UCI

NO Install Message sent

Install Started for GMPL\*2.0\*44 :

May 09, 2014@10:00:21

Build Distribution Date: May 08, 2014

Installing Routines:

May 09, 2014@10:00:21

Running Post-Install Routine: POST^GMPLP44I

Creating Clinical Reminders Index cross-references.

Creating Problem List .01 diagnosis cross-reference.

Creating Problem List SNOMED CT cross-reference.

Creating Problem List Mapping Targets cross-reference.

Problem List Clinical Reminders Index rebuild queued.

The task number is 299179.

Updating Routine file...

Updating KIDS files...

GMPL\*2.0\*44 Installed.

May 09, 2014@10:00:21

Not a production UCI

NO Install Message sent

Install Started for PXRM\*2.0\*26 :

May 09, 2014@10:00:21

Build Distribution Date: May 08, 2014

Installing Routines:

May 09, 2014@10:00:22

Running Pre-Install Routine: PRE^PXRMP26I

DISABLE options.

DISABLE protocols.

Disabling reminder evaluation.

Setting up taxonomy management option.

Building lists of dialogs to update

Removing old data dictionaries.

Deleting data dictionary for file \# 811.2

Deleting data dictionary for file \# 801.41

Installing Data Dictionaries:

May 09, 2014@10:00:23

Installing Data:

May 09, 2014@10:00:23

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing INPUT TEMPLATE

Installing FORM

Installing PROTOCOL

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Installing LIST TEMPLATE

Installing OPTION

May 09, 2014@10:00:51

Running Post-Install Routine: POST^PXRMP26I

Copying all taxonomy Brief Descriptions to Description.

Working on taxonomy 691 PALLI CONS CANCER/HEMA COND

Brief description: Cancer and Hematologic Conditions

Working on taxonomy 691 PALLI CONS CARDIO COND OTHER THAN CA

Brief description: Cardiopulmonary Conditions Other than Cancer

Working on taxonomy 691 PALLI CONS CNS COND OTHER THAN CA

Brief description: CNS Conditions Other Than Cancer

Working on taxonomy 691 PALLI CONS DERM CONDITION DX

Brief description: Dermatologic Conditions

Working on taxonomy 691 PALLI CONS GI OTHER THAN CA

Brief description: Gastrointestinal Conditions Other than Cancer

Working on taxonomy 691 PALLI CONS INFECTIOUS COND

Brief description: Infectious Conditions and SIRS

Working on taxonomy 691 PALLI CONS RENAL OTHER THAN CA

Brief description: Renal Conditions Other than Cancer

Working on taxonomy 691 PALLI CONS RHEUM/VASC/THROMB

Brief description: Rheumatologic, Vasculitic, and Thromboembolic Conditions

Working on taxonomy ACUTE MI

Brief description: Prior DX of MI

Working on taxonomy Advance Directives

Brief description does not exist.

Working on taxonomy BILATERIAL MASTECTOMY

Brief description: Mastectomy codes

Working on taxonomy CA pneumonia

Brief description: CAP

Working on taxonomy CA-ESOPH LIVER PANCREAS

Brief description: Ca with life exp \<6M

Working on taxonomy CHEY-BIL AMPUTEE

Brief description: LE amputation codes

Working on taxonomy CHEY-CERVICAL CANCER SCREEN

Brief description: Cervical cancer screen codes

Working on taxonomy CHEY-COPD

Brief description: COPD codes

Working on taxonomy CHEY-CVA

Brief description: CVA codes

Working on taxonomy CHEY-EMP

Brief description: EMPLOYEE LIST

Working on taxonomy CHEY-HEALTHY LIFESTYLE

Brief description: Healthy lifestyle codes

Working on taxonomy CHEY-HEP A VACCINE

Brief description: Hep A vaccine codes

Working on taxonomy CHEY-HEP B VACCINE

Brief description: Hep b vaccine codes

Working on taxonomy CHEY-HGB A1C

Brief description: Hgb A1C codes

Working on taxonomy CHEY-HYSTERECTOMY

Brief description: Hysterectomy codes

Working on taxonomy CHEY-MAMMOGRAM SCREENS

Brief description: FOR RADIOLOGY RESOLUTION OF REMINDER

Working on taxonomy CHEY-PARAPLEGIC

Brief description: Paraplegic codes

Working on taxonomy CHEY-SPIROMETRY/PFT

Brief description: Spirometry/PFT codes

Working on taxonomy CHEY-TB HIGH RISK

Brief description: TB risk codes

Working on taxonomy CHEY-TOTAL BLINDNESS

Brief description: Total blindness codes

Working on taxonomy CHRONIC OBSTRUCTIVE ASTHMA

Brief description does not exist.

Working on taxonomy CHRONIC OBSTRUCTIVE BRONCHITIS

Brief description does not exist.

Working on taxonomy CHY AAA DIAGNOSIS

Brief description: For AAA diagnosis

Working on taxonomy CHY-HYPOTHYROIDISM

Brief description: FOR DR. HOLLAND

Working on taxonomy COLITIS/ILEITIS(GJ)

Brief description: Codes for ileitis, colitis

Working on taxonomy COLON POLYPS

Brief description: Colon

Working on taxonomy COLON REMOVAL

Brief description: Codes for partial colectomy

Working on taxonomy COLON REMOVAL-TOTAL

Brief description: CPT FOR TOTAL COLECTOMY

Working on taxonomy COLONOSCOPY

Brief description: Codes for colonoscopy

Working on taxonomy COLORECTAL CANCER

Brief description: Colorectal cancer codes

Working on taxonomy CONGESTIVE HEALTH FAILURE

Brief description does not exist.

Working on taxonomy COPD

Brief description does not exist.

Working on taxonomy COR PULMONALE

Brief description does not exist.

Working on taxonomy DEMENTIA CODES - SHERIDAN

Brief description: Dementia codes to screen driving and firearms

Working on taxonomy DEPRESSION CODES

Brief description: for depression assessment

Working on taxonomy DEPRESSION SCREEN

Brief description: Depression screen code

Working on taxonomy DIABETES

Brief description: DIABETES

Working on taxonomy DIABETIC EYE EXAM

Brief description: Diabetic Eye Exams

Working on taxonomy DIABETIC/RENAL DISEASE

Brief description: ICD-9 codes for diab renal dis

Working on taxonomy EMPHYSEMA

Brief description does not exist.

Working on taxonomy ESOPHAGUS CANCER

Brief description does not exist.

Working on taxonomy FAMILY HX of Colon CA

Brief description: Family hx of GI cancer

Working on taxonomy FEMALE ENDOMETRIUM/OVARIAN(GJ)

Brief description: endometrium/ovarians ca dx

Working on taxonomy FOBT COMPLETE

Brief description: Fecal occult blood test codes

Working on taxonomy HEART FAILURE

Brief description does not exist.

Working on taxonomy HEP C INFECTION

Brief description does not exist.

Working on taxonomy HIGH RISK COLON POLPS

Brief description: MALIGNANT POLPYS

Working on taxonomy HIGH RISK COLONOSCOPY

Brief description: Lesion/Polpy removed

Working on taxonomy HIGH RISK FLU/PNEUMONIA

Brief description: Flu/pneumonia risk codes

Working on taxonomy HISTORY OF COLON POLYPS

Brief description: Reporting PERSONAL HISTORY of colon polyps.

Working on taxonomy HIV TX

Brief description: HIV DIAGNOSIS

Working on taxonomy HPV VACCINE CPT CODE

Brief description: CPT CODE HPV

Working on taxonomy HYPOXIA

Brief description does not exist.

Working on taxonomy IHD PROCEDURES

Brief description does not exist.

Working on taxonomy INTERSTITIAL DISEASE

Brief description does not exist.

Working on taxonomy IRRITABLE BOWEL SYNDROME

Brief description: Dx. of

Working on taxonomy LESION REMOVAL/COLONOSCOPY

Brief description does not exist.

Working on taxonomy LIVER CANCER

Brief description does not exist.

Working on taxonomy LV NON-VESTED PATIENTS

Brief description: CODES THAT VEST

Working on taxonomy MIGRAIN HEADACHES

Brief description does not exist.

Working on taxonomy NEW EMPLOYEE CODES

Brief description does not exist.

Working on taxonomy OBESITY 278.00

Brief description does not exist.

Working on taxonomy OSTEOPOROSIS

Brief description does not exist.

Working on taxonomy OVERWEIGHT

Brief description does not exist.

Working on taxonomy PALLIATIVE CONSULT ENCOUNTER DX

Brief description: Encounter Diagnosis: O NOT OPEN HISTORICAL OPTION)

Working on taxonomy PANCREAS CANCER

Brief description does not exist.

Working on taxonomy POSITIVE PPD

Brief description does not exist.

Working on taxonomy POST-OP WOUND INFECTION

Brief description does not exist.

Working on taxonomy REGIONAL ENTERITIS

Brief description: Crohn's Disease

Working on taxonomy SATP ENROLLMENT

Brief description does not exist.

Working on taxonomy SCHIZOPHRENIA

Brief description does not exist.

Working on taxonomy SECONDARY POLYCYTHEMIA

Brief description does not exist.

Working on taxonomy SIGMOIDOSCOPY

Brief description: CODES FOR FLEX/RIGID SIG

Working on taxonomy SLC-MOVE CO-MORBIDITIES

Brief description: MOVE EXCLUSION CRITERIA

Working on taxonomy SLEEP APNEA

Brief description does not exist.

Working on taxonomy TETANUS DIPHTHERIA CHY

Brief description: Tetanus and diphtheria codes

Working on taxonomy TOBACCO USE

Brief description: Tobacco use codes

Working on taxonomy TOBACCO USE ACTIVE PROBLEM LIST

Brief description does not exist.

Working on taxonomy TOBACCO USE DX

Brief description: TOBACCO USE BY DX

Working on taxonomy ULCERATIVE COLITIS

Brief description: Ulcerative Colitis codes

Working on taxonomy URINARY INCONTINENCE

Brief description: ACOVE/INCONTINENCE OF URINE CODES

Working on taxonomy V20-DIABETES

Brief description: Diabetic diagnosis codes

Working on taxonomy V23 TDAP CPT CODES

Brief description: CPT CODES FOR TDAP

Working on taxonomy V23 TETANUS DIPHTHERIA

Brief description: Tetanus and diphtheria codes

Working on taxonomy VA-ABD AORTIC ANEURYSM

Brief description: ICD codes and CPT codes indicating AAA

Working on taxonomy VA-ALCOHOL ABUSE

Brief description: Alcohol abuse codes

Working on taxonomy VA-ALCOHOLISM SCREENING

Brief description: Alcoholism screening codes

Working on taxonomy VA-BREAST TUMOR

Brief description: Breast tumor, mass, infection, pain

Working on taxonomy VA-CERVICAL CA/ABNORMAL PAP

Brief description: Cervical ca/abnormal pap codes

Working on taxonomy VA-CERVICAL CANCER SCREEN

Brief description: Cervical cancer screen codes

Working on taxonomy VA-CHOLESTEROL

Brief description: Cholesterol codes

Working on taxonomy VA-COLORECTAL CA

Brief description: Colorectal cancer codes

Working on taxonomy VA-COLORECTAL CANCER SCREEN

Brief description: Rectal cancer screen codes

Working on taxonomy VA-DEPRESSION DIAGNOSIS

Brief description: Codes for depression, including MDD

Working on taxonomy VA-DEPRESSION DX OUTPT VISIT

Brief description: Codes for depression, including MDD

Working on taxonomy VA-DIABETES

Brief description: Diabetic diagnosis codes

Working on taxonomy VA-DIABETES HEDIS

Brief description: Diabetic diagnosis codes

Working on taxonomy VA-DIABETES HEDIS PROB LIST

Brief description: Diabetic diagnosis codes

Working on taxonomy VA-ECOE DIAGNOSIS CODES

Brief description does not exist.

Working on taxonomy VA-EXERCISE COUNSELING

Brief description: Exercise counseling codes

Working on taxonomy VA-FLEXISIGMOIDOSCOPY

Brief description: Flexisigmoidoscopy codes

Working on taxonomy VA-FOBT

Brief description: Fecal occult blood test codes

Working on taxonomy VA-HEPATITIS C INFECTION

Brief description: HEP C CODES

Working on taxonomy VA-HIGH RISK FOR FLU/PNEUMONIA

Brief description: Flu/pneumonia risk codes

Working on taxonomy VA-HIGH RISK FOR INFLUENZA

Brief description: High Risk for Flu develop by NCP and ID 2-09

Working on taxonomy VA-HIGH RISK FOR TB

Brief description: TB risk codes

Working on taxonomy VA-HYPERTENSION

Brief description: Hypertension codes

Working on taxonomy VA-HYPERTENSION CODES

Brief description: Hypertension codes

Working on taxonomy VA-HYPERTENSION SCREEN

Brief description: Hypertension screen codes

Working on taxonomy VA-HYSTERECTOMY

Brief description does not exist.

Working on taxonomy VA-IHD AND ASVD

Brief description: IHD and other atherosclerosis

Working on taxonomy VA-IMAGING FOR AAA (NON-SPECIFIC)

Brief description: CODES THAT MAY OR MAY NOT REPRESENT ADEQUATE SCREENING

Working on taxonomy VA-INFLUENZA IMMUNIZATION

Brief description: Influenza immunization codes

Working on taxonomy VA-ISCHEMIC HEART 412 DISEASE

Brief description: Ischemic Heart 412 Disease Diagnoses

Working on taxonomy VA-ISCHEMIC HEART DISEASE

Brief description: Ischemic Heart Disease Diagnoses

Working on taxonomy VA-MAMMOGRAM/SCREEN

Brief description: Mammogram/screening CPT codes

Working on taxonomy VA-MASTECTOMY

Brief description: Mastectomy codes

Working on taxonomy VA-MHV BILATERAL AMPUTEE

Brief description: ICD codes for bilateral amputee

Working on taxonomy VA-MHV COLONOSCOPY

Brief description: Codes for colonoscopy

Working on taxonomy VA-MHV DIABETIC RETINAL DISEASE

Brief description does not exist.

Working on taxonomy VA-MHV IHD AND ATHERSCLEROSIS

Brief description: Atherosclerotic disease

Working on taxonomy VA-MHV RETINAL EXAMINATION

Brief description: retinal exam codes

Working on taxonomy VA-MHV SIGMOIDOSCOPY

Brief description: Codes for Flexible sigmoidoscopy

Working on taxonomy VA-NUTRITION

Brief description: Nutrition codes

Working on taxonomy VA-OBESITY

Brief description: Obesity codes

Working on taxonomy VA-PALLI CONS CANCER/HEMA COND

Brief description: Cancer and Hematologic Conditions

Working on taxonomy VA-PALLI CONS CARDIO COND OTHER THAN CA

Brief description: Cardiopulmonary Conditions Other than Cancer

Working on taxonomy VA-PALLI CONS CNS COND OTHER THAN CA

Brief description: CNS Conditions Other Than Cancer

Working on taxonomy VA-PALLI CONS DERM CONDITION DX

Brief description: Dermatologic Conditions

Working on taxonomy VA-PALLI CONS GI OTHER THAN CA

Brief description: Gastrointestinal Conditions Other than Cancer

Working on taxonomy VA-PALLI CONS INFECTIOUS COND

Brief description: Infectious Conditions and SIRS

Working on taxonomy VA-PALLI CONS RENAL OTHER THAN CA

Brief description: Renal Conditions Other than Cancer

Working on taxonomy VA-PALLI CONS RHEUM/VASC/THROMB

Brief description: Rheumatologic, Vasculitic, and Thromboembolic Conditions

Working on taxonomy VA-PNEUMOC DZ RISK - CHEMOTHERAPY

Brief description: encounters for chemotherapy

Working on taxonomy VA-PNEUMOC DZ RISK - HIGH

Brief description: High Risk for Pneumococcal Disease

Working on taxonomy VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP

Brief description: Highest risk but not immunocompromised

Working on taxonomy VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED

Brief description: Highest Risk - immunocompromised

Working on taxonomy VA-PNEUMOCOCCAL VACCINE

Brief description: Pneumococcal vaccine codes

Working on taxonomy VA-POLYTRAUMA AMPUTATION

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA AUDITORY

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA BRAIN INJURY

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA BURN

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA INPT REHAB

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA ORTHO

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA PTSD

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA SCI

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA VISION

Brief description does not exist.

Working on taxonomy VA-POLYTRAUMA WAR INJURY

Brief description does not exist.

Working on taxonomy VA-PROSTATE CA

Brief description: Prostate cancer codes

Working on taxonomy VA-PSA

Brief description: PSA codes

Working on taxonomy VA-PSYCHOTHERAPY CPT CODES

Brief description: PSYCHOTHERAPY CODES FOR DEPRESSION

Working on taxonomy VA-PTSD DIAGNOSIS

Brief description: PTSD CODES

Working on taxonomy VA-PTSD DX OUTPT PRIMARY

Brief description: PTSD CODES, OUTPT, PRIMARY ONLY

Working on taxonomy VA-PTSD DX OUTPT VISIT

Brief description: PTSD CODES

Working on taxonomy VA-SAFETY COUNSELING

Brief description: Safety counseling codes

Working on taxonomy VA-SCHIZOPHRENIA

Brief description: SCHIZOPHRENIA CODES

Working on taxonomy VA-TB/POSITIVE PPD

Brief description: Positive PPD codes

Working on taxonomy VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCL (TAXONOMIES)

Brief description: Teratogenic Meds Order Check Exclusions

Working on taxonomy VA-TERMINAL CANCER PATIENTS

Brief description: Terminal cancer codes

Working on taxonomy VA-TETANUS DIPHTHERIA

Brief description: Tetanus and diphtheria codes

Working on taxonomy VA-TOBACCO USE

Brief description: Tobacco use codes

Working on taxonomy VA-WEIGHT AND NUTRITION SCREEN

Brief description: Weight/nutr. screen codes

Working on taxonomy VA-WH BILATERAL MASTECTOMY

Brief description: Codes for bilateral mastectomy

Working on taxonomy VA-WH HYSTERECTOMY W/CERVIX REMOVED

Brief description: Hysterectomy with cervix removed

Working on taxonomy VA-WH IUD INSERTION (TAXONOMY)

Brief description: Insert Intrauterine Device

Working on taxonomy VA-WH IUD REMOVAL (TAXONOMY)

Brief description: Remove Intrauterine Device

Working on taxonomy VA-WH PAP SMEAR OBTAINED

Brief description: Obtain PAP smear codes

Working on taxonomy VA-WH PAP SMEAR SCREEN CODES

Brief description: PAP Smear screen codes w/o obtained codes

Working on taxonomy VA-WH TUBAL LIGATION CODES (TAXONOMY)

Brief description: Tubal Ligation

Working on taxonomy VA-WH TUBAL REANASTOMOSIS (TAXONOMY)

Brief description: Tubal Reanastomosis

Copying ranges of codes for all taxonomies.

Copy codes for taxonomy 691 PALLI CONS CANCER/HEMA COND (IEN=107)

Copy codes for taxonomy 691 PALLI CONS CARDIO COND OTHER THAN CA (IEN=105)

Copy codes for taxonomy 691 PALLI CONS CNS COND OTHER THAN CA (IEN=106)

Copy codes for taxonomy 691 PALLI CONS DERM CONDITION DX (IEN=102)

Copy codes for taxonomy 691 PALLI CONS GI OTHER THAN CA (IEN=104)

Copy codes for taxonomy 691 PALLI CONS INFECTIOUS COND (IEN=100)

Copy codes for taxonomy 691 PALLI CONS RENAL OTHER THAN CA (IEN=103)

Copy codes for taxonomy 691 PALLI CONS RHEUM/VASC/THROMB (IEN=101)

Copy codes for taxonomy ACUTE MI (IEN=442036)

Copy codes for taxonomy Advance Directives (IEN=43)

Copy codes for taxonomy BILATERIAL MASTECTOMY (IEN=442014)

Copy codes for taxonomy CA pneumonia (IEN=53)

Copy codes for taxonomy CA-ESOPH LIVER PANCREAS (IEN=75)

Copy codes for taxonomy CHEY-BIL AMPUTEE (IEN=442020)

Copy codes for taxonomy CHEY-CERVICAL CANCER SCREEN (IEN=442013)

Copy codes for taxonomy CHEY-COPD (IEN=442002)

Copy codes for taxonomy CHEY-CVA (IEN=442015)

Copy codes for taxonomy CHEY-EMP (IEN=442011)

Copy codes for taxonomy CHEY-HEALTHY LIFESTYLE (IEN=442005)

Copy codes for taxonomy CHEY-HEP A VACCINE (IEN=442012)

Copy codes for taxonomy CHEY-HEP B VACCINE (IEN=442008)

Copy codes for taxonomy CHEY-HGB A1C (IEN=442016)

Copy codes for taxonomy CHEY-HYSTERECTOMY (IEN=442010)

Copy codes for taxonomy CHEY-MAMMOGRAM SCREENS (IEN=71)

Copy codes for taxonomy CHEY-PARAPLEGIC (IEN=442017)

Copy codes for taxonomy CHEY-SPIROMETRY/PFT (IEN=442003)

Copy codes for taxonomy CHEY-TB HIGH RISK (IEN=442009)

Copy codes for taxonomy CHEY-TOTAL BLINDNESS (IEN=442019)

Copy codes for taxonomy CHRONIC OBSTRUCTIVE ASTHMA (IEN=39)

Copy codes for taxonomy CHRONIC OBSTRUCTIVE BRONCHITIS (IEN=38)

Copy codes for taxonomy CHY AAA DIAGNOSIS (IEN=69)

Copy codes for taxonomy CHY-HYPOTHYROIDISM (IEN=68)

Copy codes for taxonomy COLITIS/ILEITIS(GJ) (IEN=442030)

Copy codes for taxonomy COLON POLYPS (IEN=442028)

Copy codes for taxonomy COLON REMOVAL (IEN=442001)

Copy codes for taxonomy COLON REMOVAL-TOTAL (IEN=442023)

Copy codes for taxonomy COLONOSCOPY (IEN=442022)

Copy codes for taxonomy COLORECTAL CANCER (IEN=442024)

Copy codes for taxonomy CONGESTIVE HEALTH FAILURE (IEN=40)

Copy codes for taxonomy COPD (IEN=7)

Copy codes for taxonomy COR PULMONALE (IEN=12)

Copy codes for taxonomy DEMENTIA CODES - SHERIDAN (IEN=67)

Warning - selectable code Invalid Code (not found in the ICD-9-CM system) is n.

Copy codes for taxonomy DEPRESSION CODES (IEN=46)

Copy codes for taxonomy DEPRESSION SCREEN (IEN=567007)

Copy codes for taxonomy DIABETES (IEN=674022)

Copy codes for taxonomy DIABETIC EYE EXAM (IEN=442021)

Copy codes for taxonomy DIABETIC/RENAL DISEASE (IEN=526016)

Copy codes for taxonomy EMPHYSEMA (IEN=3)

Copy codes for taxonomy ESOPHAGUS CANCER (IEN=54)

Copy codes for taxonomy FAMILY HX of Colon CA (IEN=442025)

Copy codes for taxonomy FEMALE ENDOMETRIUM/OVARIAN(GJ) (IEN=442029)

Copy codes for taxonomy FOBT COMPLETE (IEN=58)

Copy codes for taxonomy HEART FAILURE (IEN=57)

Copy codes for taxonomy HEP C INFECTION (IEN=442007)

Copy codes for taxonomy HIGH RISK COLON POLPS (IEN=51)

Copy codes for taxonomy HIGH RISK COLONOSCOPY (IEN=48)

Copy codes for taxonomy HIGH RISK FLU/PNEUMONIA (IEN=442004)

Copy codes for taxonomy HISTORY OF COLON POLYPS (IEN=442035)

Copy codes for taxonomy HIV TX (IEN=83)

Copy codes for taxonomy HPV VACCINE CPT CODE (IEN=76)

Copy codes for taxonomy HYPOXIA (IEN=37)

Copy codes for taxonomy IHD PROCEDURES (IEN=108)

Copy codes for taxonomy INTERSTITIAL DISEASE (IEN=13)

Copy codes for taxonomy IRRITABLE BOWEL SYNDROME (IEN=442037)

Copy codes for taxonomy LESION REMOVAL/COLONOSCOPY (IEN=442034)

Copy codes for taxonomy LIVER CANCER (IEN=55)

Copy codes for taxonomy LV NON-VESTED PATIENTS (IEN=109)

Copy codes for taxonomy MIGRAIN HEADACHES (IEN=14)

Copy codes for taxonomy NEW EMPLOYEE CODES (IEN=442018)

Copy codes for taxonomy OBESITY 278.00 (IEN=73)

Copy codes for taxonomy OSTEOPOROSIS (IEN=138)

Copy codes for taxonomy OVERWEIGHT (IEN=72)

Copy codes for taxonomy PALLIATIVE CONSULT ENCOUNTER DX (IEN=82)

Copy codes for taxonomy PANCREAS CANCER (IEN=56)

Copy codes for taxonomy POSITIVE PPD (IEN=442033)

Copy codes for taxonomy POST-OP WOUND INFECTION (IEN=59)

Copy codes for taxonomy REGIONAL ENTERITIS (IEN=442026)

Copy codes for taxonomy SATP ENROLLMENT (IEN=47)

Copy codes for taxonomy SCHIZOPHRENIA (IEN=442032)

Copy codes for taxonomy SECONDARY POLYCYTHEMIA (IEN=41)

Copy codes for taxonomy SIGMOIDOSCOPY (IEN=442031)

Copy codes for taxonomy SLC-MOVE CO-MORBIDITIES (IEN=74)

Copy codes for taxonomy SLEEP APNEA (IEN=42)

Copy codes for taxonomy TETANUS DIPHTHERIA CHY (IEN=80)

Copy codes for taxonomy TOBACCO USE (IEN=436024)

Warning - ICD code 305.10 is not valid.

Warning - selectable code Invalid Code (not found in the ICD-9-CM system) is n.

Copy codes for taxonomy TOBACCO USE ACTIVE PROBLEM LIST (IEN=110)

Copy codes for taxonomy TOBACCO USE DX (IEN=111)

Copy codes for taxonomy ULCERATIVE COLITIS (IEN=442027)

Copy codes for taxonomy URINARY INCONTINENCE (IEN=99)

Copy codes for taxonomy V20-DIABETES (IEN=81)

Copy codes for taxonomy V23 TDAP CPT CODES (IEN=79)

Copy codes for taxonomy V23 TETANUS DIPHTHERIA (IEN=78)

Copy codes for taxonomy VA-ABD AORTIC ANEURYSM (IEN=215)

Copy codes for taxonomy VA-ALCOHOL ABUSE (IEN=17)

Warning - selectable code Invalid Code (not found in the ICD-9-CM system) is n.

Copy codes for taxonomy VA-ALCOHOLISM SCREENING (IEN=34)

Copy codes for taxonomy VA-BREAST TUMOR (IEN=18)

Copy codes for taxonomy VA-CERVICAL CA/ABNORMAL PAP (IEN=5)

Copy codes for taxonomy VA-CERVICAL CANCER SCREEN (IEN=30)

Copy codes for taxonomy VA-CHOLESTEROL (IEN=24)

Copy codes for taxonomy VA-COLORECTAL CA (IEN=4)

Copy codes for taxonomy VA-COLORECTAL CANCER SCREEN (IEN=31)

Copy codes for taxonomy VA-DEPRESSION DIAGNOSIS (IEN=49)

Copy codes for taxonomy VA-DEPRESSION DX OUTPT VISIT (IEN=160)

Copy codes for taxonomy VA-DIABETES (IEN=28)

Copy codes for taxonomy VA-DIABETES HEDIS (IEN=317)

Copy codes for taxonomy VA-DIABETES HEDIS PROB LIST (IEN=316)

Copy codes for taxonomy VA-ECOE DIAGNOSIS CODES (IEN=115)

Copy codes for taxonomy VA-EXERCISE COUNSELING (IEN=32)

Copy codes for taxonomy VA-FLEXISIGMOIDOSCOPY (IEN=15)

Copy codes for taxonomy VA-FOBT (IEN=27)

Copy codes for taxonomy VA-HEPATITIS C INFECTION (IEN=2)

Copy codes for taxonomy VA-HIGH RISK FOR FLU/PNEUMONIA (IEN=9)

Copy codes for taxonomy VA-HIGH RISK FOR INFLUENZA (IEN=220)

Copy codes for taxonomy VA-HIGH RISK FOR TB (IEN=11)

Copy codes for taxonomy VA-HYPERTENSION (IEN=1)

Copy codes for taxonomy VA-HYPERTENSION CODES (IEN=44)

Copy codes for taxonomy VA-HYPERTENSION SCREEN (IEN=23)

Copy codes for taxonomy VA-HYSTERECTOMY (IEN=6)

Copy codes for taxonomy VA-IHD AND ASVD (IEN=315)

Copy codes for taxonomy VA-IMAGING FOR AAA (NON-SPECIFIC) (IEN=214)

Copy codes for taxonomy VA-INFLUENZA IMMUNIZATION (IEN=33)

Copy codes for taxonomy VA-ISCHEMIC HEART 412 DISEASE (IEN=60)

Copy codes for taxonomy VA-ISCHEMIC HEART DISEASE (IEN=45)

Copy codes for taxonomy VA-MAMMOGRAM/SCREEN (IEN=16)

Copy codes for taxonomy VA-MASTECTOMY (IEN=19)

Copy codes for taxonomy VA-MHV BILATERAL AMPUTEE (IEN=87)

Copy codes for taxonomy VA-MHV COLONOSCOPY (IEN=85)

Copy codes for taxonomy VA-MHV DIABETIC RETINAL DISEASE (IEN=88)

Copy codes for taxonomy VA-MHV IHD AND ATHERSCLEROSIS (IEN=66)

Copy codes for taxonomy VA-MHV RETINAL EXAMINATION (IEN=89)

Copy codes for taxonomy VA-MHV SIGMOIDOSCOPY (IEN=86)

Copy codes for taxonomy VA-NUTRITION (IEN=21)

Copy codes for taxonomy VA-OBESITY (IEN=20)

Copy codes for taxonomy VA-PALLI CONS CANCER/HEMA COND (IEN=127)

Copy codes for taxonomy VA-PALLI CONS CARDIO COND OTHER THAN CA (IEN=125)

Copy codes for taxonomy VA-PALLI CONS CNS COND OTHER THAN CA (IEN=126)

Copy codes for taxonomy VA-PALLI CONS DERM CONDITION DX (IEN=122)

Copy codes for taxonomy VA-PALLI CONS GI OTHER THAN CA (IEN=124)

Copy codes for taxonomy VA-PALLI CONS INFECTIOUS COND (IEN=120)

Copy codes for taxonomy VA-PALLI CONS RENAL OTHER THAN CA (IEN=123)

Copy codes for taxonomy VA-PALLI CONS RHEUM/VASC/THROMB (IEN=121)

Copy codes for taxonomy VA-PNEUMOC DZ RISK - CHEMOTHERAPY (IEN=118)

Copy codes for taxonomy VA-PNEUMOC DZ RISK - HIGH (IEN=77)

Copy codes for taxonomy VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP (IEN=344)

Copy codes for taxonomy VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED (IEN=119)

Copy codes for taxonomy VA-PNEUMOCOCCAL VACCINE (IEN=25)

Copy codes for taxonomy VA-POLYTRAUMA AMPUTATION (IEN=98)

Copy codes for taxonomy VA-POLYTRAUMA AUDITORY (IEN=97)

Copy codes for taxonomy VA-POLYTRAUMA BRAIN INJURY (IEN=96)

Copy codes for taxonomy VA-POLYTRAUMA BURN (IEN=95)

Copy codes for taxonomy VA-POLYTRAUMA INPT REHAB (IEN=94)

Copy codes for taxonomy VA-POLYTRAUMA ORTHO (IEN=93)

Copy codes for taxonomy VA-POLYTRAUMA PTSD (IEN=92)

Copy codes for taxonomy VA-POLYTRAUMA SCI (IEN=91)

Copy codes for taxonomy VA-POLYTRAUMA VISION (IEN=90)

Copy codes for taxonomy VA-POLYTRAUMA WAR INJURY (IEN=84)

Copy codes for taxonomy VA-PROSTATE CA (IEN=8)

Copy codes for taxonomy VA-PSA (IEN=26)

Copy codes for taxonomy VA-PSYCHOTHERAPY CPT CODES (IEN=50)

Copy codes for taxonomy VA-PTSD DIAGNOSIS (IEN=70)

Copy codes for taxonomy VA-PTSD DX OUTPT PRIMARY (IEN=224)

Copy codes for taxonomy VA-PTSD DX OUTPT VISIT (IEN=176)

Copy codes for taxonomy VA-SAFETY COUNSELING (IEN=35)

Copy codes for taxonomy VA-SCHIZOPHRENIA (IEN=52)

Copy codes for taxonomy VA-TB/POSITIVE PPD (IEN=10)

Copy codes for taxonomy VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCL (TAXONOMIES)

Copy codes for taxonomy VA-TERMINAL CANCER PATIENTS (IEN=61)

Copy codes for taxonomy VA-TETANUS DIPHTHERIA (IEN=29)

Copy codes for taxonomy VA-TOBACCO USE (IEN=22)

Warning - ICD code 305.10 is not valid.

Warning - selectable code Invalid Code (not found in the ICD-9-CM system) is n.

Copy codes for taxonomy VA-WEIGHT AND NUTRITION SCREEN (IEN=36)

Copy codes for taxonomy VA-WH BILATERAL MASTECTOMY (IEN=62)

Copy codes for taxonomy VA-WH HYSTERECTOMY W/CERVIX REMOVED (IEN=64)

Copy codes for taxonomy VA-WH IUD INSERTION (TAXONOMY) (IEN=113)

Copy codes for taxonomy VA-WH IUD REMOVAL (TAXONOMY) (IEN=112)

Copy codes for taxonomy VA-WH PAP SMEAR OBTAINED (IEN=63)

Copy codes for taxonomy VA-WH PAP SMEAR SCREEN CODES (IEN=65)

Copy codes for taxonomy VA-WH TUBAL LIGATION CODES (TAXONOMY) (IEN=117)

Copy codes for taxonomy VA-WH TUBAL REANASTOMOSIS (TAXONOMY) (IEN=116)

Dialogs updates

Dialog HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE Pre-conversion codes

Diagnosis Code: V06.5

Procedure Code: 90718

Taxonomy HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE added to dialog.

Taxonomy HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE post-conversion codes list:

Diagnosis Code: V06.5

Procedure Code: 90718

Dialog IM HEP B DONE ELSEWHERE Pre-conversion codes

Procedure Code: 90632

Taxonomy IM HEP B DONE ELSEWHERE added to dialog.

Taxonomy IM HEP B DONE ELSEWHERE post-conversion codes list:

Procedure Code: 90632

Dialog V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM Pre-conversion codes

Diagnosis Code: V80.2

Procedure Code: 99211

Taxonomy V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM added to dialog.

Taxonomy V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM post-conversion codes list:

Diagnosis Code: V80.2

Procedure Code: 99211

Dialog V\*-HF DIAB TELERET DISPO TELERETINAL EXAM Pre-conversion codes

Diagnosis Code: V80.2

Procedure Code: 99211

Taxonomy V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM added to dialog.

Taxonomy V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM post-conversion codes list:

Diagnosis Code: V80.2

Procedure Code: 99211

Dialog 691 PALL INPT 99255 Pre-conversion codes

Procedure Code: 99255

Taxonomy 691 PALL INPT 99255 added to dialog.

Taxonomy 691 PALL INPT 99255 post-conversion codes list:

Procedure Code: 99255

Dialog 691 PALL INPT 99254 Pre-conversion codes

Procedure Code: 99254

Taxonomy 691 PALL INPT 99254 added to dialog.

Taxonomy 691 PALL INPT 99254 post-conversion codes list:

Procedure Code: 99254

Dialog 691 PALL INPT 99253 Pre-conversion codes

Procedure Code: 99253

Taxonomy 691 PALL INPT 99253 added to dialog.

Taxonomy 691 PALL INPT 99253 post-conversion codes list:

Procedure Code: 99253

Dialog 691 PALL INPT 99252 Pre-conversion codes

Procedure Code: 99252

Taxonomy 691 PALL INPT 99252 added to dialog.

Taxonomy 691 PALL INPT 99252 post-conversion codes list:

Procedure Code: 99252

Dialog 691 PALL INPT 99251 Pre-conversion codes

Procedure Code: 99251

Taxonomy 691 PALL INPT 99251 added to dialog.

Taxonomy 691 PALL INPT 99251 post-conversion codes list:

Procedure Code: 99251

Dialog 691 PALL INPT ENCOUNTER Pre-conversion codes

Diagnosis Code: V66.7

Taxonomy 691 PALL INPT ENCOUNTER added to dialog.

Taxonomy 691 PALL INPT ENCOUNTER post-conversion codes list:

Diagnosis Code: V66.7

Dialog 691 PALL OUTPT 99245 Pre-conversion codes

Procedure Code: 99245

Taxonomy 691 PALL OUTPT 99245 added to dialog.

Taxonomy 691 PALL OUTPT 99245 post-conversion codes list:

Procedure Code: 99245

Dialog 691 PALL OUTPT 99244 Pre-conversion codes

Procedure Code: 99244

Taxonomy 691 PALL OUTPT 99244 added to dialog.

Taxonomy 691 PALL OUTPT 99244 post-conversion codes list:

Procedure Code: 99244

Dialog 691 PALL OUTPT 99243 Pre-conversion codes

Procedure Code: 99243

Taxonomy 691 PALL OUTPT 99243 added to dialog.

Taxonomy 691 PALL OUTPT 99243 post-conversion codes list:

Procedure Code: 99243

Dialog 691 PALL OUTPT 99242 Pre-conversion codes

Procedure Code: 99242

Taxonomy 691 PALL OUTPT 99242 added to dialog.

Taxonomy 691 PALL OUTPT 99242 post-conversion codes list:

Procedure Code: 99242

Dialog 691 PALL OUTPT 99241 Pre-conversion codes

Procedure Code: 99241

Taxonomy 691 PALL OUTPT 99241 added to dialog.

Taxonomy 691 PALL OUTPT 99241 post-conversion codes list:

Procedure Code: 99241

Dialog 691 PALL OUTPT ENCOUNTER Pre-conversion codes

Diagnosis Code: V66.7

Taxonomy 691 PALL INPT ENCOUNTER added to dialog.

Taxonomy 691 PALL INPT ENCOUNTER post-conversion codes list:

Diagnosis Code: V66.7

Dialog GP TOB CURRENT USER OPTIONAL ACTIONS FY07 Pre-conversion codes

Diagnosis Code: 305.1

Taxonomy GP TOB CURRENT USER OPTIONAL ACTIONS FY07 added to dialog.

Taxonomy GP TOB CURRENT USER OPTIONAL ACTIONS FY07 post-conversion codes list:

Diagnosis Code: 305.1

Dialog GP TOB ED COUNSELING (CURRENT USER) FY07 Pre-conversion codes

Diagnosis Code: 305.1

Taxonomy GP TOB CURRENT USER OPTIONAL ACTIONS FY07 added to dialog.

Taxonomy GP TOB CURRENT USER OPTIONAL ACTIONS FY07 post-conversion codes list:

Diagnosis Code: 305.1

Dialog CCHT DISEASE INDICATIONS SUBST ABUSE Pre-conversion codes

Diagnosis Code: 305.90

Taxonomy CCHT DISEASE INDICATIONS SUBST ABUSE added to dialog.

Taxonomy CCHT DISEASE INDICATIONS SUBST ABUSE post-conversion codes list:

Diagnosis Code: 305.90

Dialog CCHT DISEASE INDICATIONS PTSD (ICD9) Pre-conversion codes

Diagnosis Code: 309.81

Taxonomy CCHT DISEASE INDICATIONS PTSD (ICD9) added to dialog.

Taxonomy CCHT DISEASE INDICATIONS PTSD (ICD9) post-conversion codes list:

Diagnosis Code: 309.81

Dialog CCHT DISEASE INDICATIONS DEPRESSION (ICD9) Pre-conversion codes

Diagnosis Code: 311.

Taxonomy CCHT DISEASE INDICATIONS DEPRESSION (ICD9) added to dialog.

Taxonomy CCHT DISEASE INDICATIONS DEPRESSION (ICD9) post-conversion codes list:

Diagnosis Code: 311.

Dialog CCHT DISEASE INDICATIONS DIABETES (ICD9) Pre-conversion codes

Diagnosis Code: 250.00

Taxonomy CCHT DISEASE INDICATIONS DIABETES (ICD9) added to dialog.

Taxonomy CCHT DISEASE INDICATIONS DIABETES (ICD9) post-conversion codes list:

Diagnosis Code: 250.00

Dialog CCHT DISEASE INDICATIONS HTN (ICD9) Pre-conversion codes

Diagnosis Code: 401.9

Taxonomy CCHT DISEASE INDICATIONS HTN (ICD9) added to dialog.

Taxonomy CCHT DISEASE INDICATIONS HTN (ICD9) post-conversion codes list:

Diagnosis Code: 401.9

Dialog CCHT DISEASE INDICATIONS COPD (ICD9) Pre-conversion codes

Diagnosis Code: 496.

Taxonomy CCHT DISEASE INDICATIONS COPD (ICD9) added to dialog.

Taxonomy CCHT DISEASE INDICATIONS COPD (ICD9) post-conversion codes list:

Diagnosis Code: 496.

Dialog CCHT DISEASE INDICATIONS CHF (ICD9) Pre-conversion codes

Diagnosis Code: 428.0

Taxonomy CCHT DISEASE INDICATIONS CHF (ICD9) added to dialog.

Taxonomy CCHT DISEASE INDICATIONS CHF (ICD9) post-conversion codes list:

Diagnosis Code: 428.0

Dialog EYE LEGAL BLINDNESS ICD9 369.4 Pre-conversion codes

Diagnosis Code: 369.4

Taxonomy EYE LEGAL BLINDNESS ICD9 369.4 added to dialog.

Taxonomy EYE LEGAL BLINDNESS ICD9 369.4 post-conversion codes list:

Diagnosis Code: 369.4

Dialog EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23 Pre-conversion codes

Diagnosis Code: 369.23

Taxonomy EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23 added to dialog.

Taxonomy EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23 post-conversion codes list:

Diagnosis Code: 369.23

Dialog EYE NEAR NORMAL ICD9 369.9 Pre-conversion codes

Diagnosis Code: 369.9

Taxonomy EYE NEAR NORMAL ICD9 369.9 added to dialog.

Taxonomy EYE NEAR NORMAL ICD9 369.9 post-conversion codes list:

Diagnosis Code: 369.9

Dialog EYE NORMAL VISION ICD9 367.9 Pre-conversion codes

Diagnosis Code: 367.9

Taxonomy EYE NORMAL VISION ICD9 367.9 added to dialog.

Taxonomy EYE NORMAL VISION ICD9 367.9 post-conversion codes list:

Diagnosis Code: 367.9

Dialog ICD9 250.50 Pre-conversion codes

Diagnosis Code: 250.50

Taxonomy ICD9 250.50 added to dialog.

Taxonomy ICD9 250.50 post-conversion codes list:

Diagnosis Code: 250.50

Dialog ICD9 250.51 Pre-conversion codes

Diagnosis Code: 250.51

Taxonomy ICD9 250.51 added to dialog.

Taxonomy ICD9 250.51 post-conversion codes list:

Diagnosis Code: 250.51

Dialog ICD9 250.52 Pre-conversion codes

Diagnosis Code: 250.52

Taxonomy ICD9 250.52 added to dialog.

Taxonomy ICD9 250.52 post-conversion codes list:

Diagnosis Code: 250.52

Dialog ICD9 250.53 Pre-conversion codes

Diagnosis Code: 250.53

Taxonomy ICD9 250.53 added to dialog.

Taxonomy ICD9 250.53 post-conversion codes list:

Diagnosis Code: 250.53

Dialog ICD9 362.01 Pre-conversion codes

Diagnosis Code: 362.01

Taxonomy ICD9 362.01 added to dialog.

Taxonomy ICD9 362.01 post-conversion codes list:

Diagnosis Code: 362.01

Dialog ICD9 362.02 Pre-conversion codes

Diagnosis Code: 362.02

Taxonomy ICD9 362.02 added to dialog.

Taxonomy ICD9 362.02 post-conversion codes list:

Diagnosis Code: 362.02

Dialog ICD9 250.02 Pre-conversion codes

Diagnosis Code: 250.02

Taxonomy ICD9 250.02 added to dialog.

Taxonomy ICD9 250.02 post-conversion codes list:

Diagnosis Code: 250.02

Dialog ICD9 250.01 Pre-conversion codes

Diagnosis Code: 250.01

Taxonomy ICD9 250.01 added to dialog.

Taxonomy ICD9 250.01 post-conversion codes list:

Diagnosis Code: 250.01

Dialog ICD9 250.00 Pre-conversion codes

Diagnosis Code: 250.00

Taxonomy CCHT DISEASE INDICATIONS DIABETES (ICD9) added to dialog.

Taxonomy CCHT DISEASE INDICATIONS DIABETES (ICD9) post-conversion codes list:

Diagnosis Code: 250.00

Dialog V\*-DG DIAB EYE CODES Pre-conversion codes

Diagnosis Code: V80.2

Taxonomy V\*-DG DIAB EYE CODES added to dialog.

Taxonomy V\*-DG DIAB EYE CODES post-conversion codes list:

Diagnosis Code: V80.2

Dialog ICD9 362.13 Pre-conversion codes

Diagnosis Code: 362.13

Taxonomy ICD9 362.13 added to dialog.

Taxonomy ICD9 362.13 post-conversion codes list:

Diagnosis Code: 362.13

Dialog ICD9 250.03 Pre-conversion codes

Diagnosis Code: 250.03

Taxonomy ICD9 250.03 added to dialog.

Taxonomy ICD9 250.03 post-conversion codes list:

Diagnosis Code: 250.03

Dialog ICD9 362.03 Pre-conversion codes

Diagnosis Code: 362.03

Taxonomy ICD9 362.03 added to dialog.

Taxonomy ICD9 362.03 post-conversion codes list:

Diagnosis Code: 362.03

Dialog ICD9 362.04 Pre-conversion codes

Diagnosis Code: 362.04

Taxonomy ICD9 362.04 added to dialog.

Taxonomy ICD9 362.04 post-conversion codes list:

Diagnosis Code: 362.04

Dialog ICD9 362.05 Pre-conversion codes

Diagnosis Code: 362.05

Taxonomy ICD9 362.05 added to dialog.

Taxonomy ICD9 362.05 post-conversion codes list:

Diagnosis Code: 362.05

Dialog ICD9 362.06 Pre-conversion codes

Diagnosis Code: 362.06

Taxonomy ICD9 362.06 added to dialog.

Taxonomy ICD9 362.06 post-conversion codes list:

Diagnosis Code: 362.06

Dialog ICD9 362.10 Pre-conversion codes

Diagnosis Code: 362.10

Taxonomy ICD9 362.10 added to dialog.

Taxonomy ICD9 362.10 post-conversion codes list:

Diagnosis Code: 362.10

Dialog ICD9 362.07 Pre-conversion codes

Diagnosis Code: 362.07

Taxonomy ICD9 362.07 added to dialog.

Taxonomy ICD9 362.07 post-conversion codes list:

Diagnosis Code: 362.07

Dialog 691 PALLI CONS OUTPT ENCOUNTER GP Pre-conversion codes

Diagnosis Code: V66.7

Taxonomy 691 PALL INPT ENCOUNTER added to dialog.

Taxonomy 691 PALL INPT ENCOUNTER post-conversion codes list:

Diagnosis Code: V66.7

Dialog 691 PALLI CONS INPT ENCOUNTER GP Pre-conversion codes

Diagnosis Code: V66.7

Taxonomy 691 PALL INPT ENCOUNTER added to dialog.

Taxonomy 691 PALL INPT ENCOUNTER post-conversion codes list:

Diagnosis Code: V66.7

Dialog CANCER OF THE PANCREAS ICD9 157.9 Pre-conversion codes

Diagnosis Code: 157.9

Taxonomy CANCER OF THE PANCREAS ICD9 157.9 added to dialog.

Taxonomy CANCER OF THE PANCREAS ICD9 157.9 post-conversion codes list:

Diagnosis Code: 157.9

Dialog CANCER OF THE LIVER ICD9 155.2 Pre-conversion codes

Diagnosis Code: 155.2

Taxonomy CANCER OF THE LIVER ICD9 155.2 added to dialog.

Taxonomy CANCER OF THE LIVER ICD9 155.2 post-conversion codes list:

Diagnosis Code: 155.2

Dialog CANCER OF THE ESOPHAGUS ICD9 150.9 Pre-conversion codes

Diagnosis Code: 150.9

Taxonomy CANCER OF THE ESOPHAGUS ICD9 150.9 added to dialog.

Taxonomy CANCER OF THE ESOPHAGUS ICD9 150.9 post-conversion codes list:

Diagnosis Code: 150.9

Dialog ECH TOBACCO ADD HX TO PL Pre-conversion codes

Diagnosis Code: V15.82

Taxonomy ECH TOBACCO ADD HX TO PL added to dialog.

Taxonomy ECH TOBACCO ADD HX TO PL post-conversion codes list:

Diagnosis Code: V15.82

Dialog ICD9 NURSE ED REFER PWA Pre-conversion codes

Diagnosis Code: V82.6

Procedure Code: 99211

Taxonomy ICD9 NURSE ED REFER PWA added to dialog.

Taxonomy ICD9 NURSE ED REFER PWA post-conversion codes list:

Diagnosis Code: V82.6

Procedure Code: 99211

Dialog HF LIPID LDL \>190 Pre-conversion codes

Procedure Code: 3050F

Taxonomy HF LIPID LDL \>190 added to dialog.

Taxonomy HF LIPID LDL \>190 post-conversion codes list:

Procedure Code: 3050F

Dialog HF LIPID LDL 160-190 Pre-conversion codes

Procedure Code: 3050F

Taxonomy HF LIPID LDL \>190 added to dialog.

Taxonomy HF LIPID LDL \>190 post-conversion codes list:

Procedure Code: 3050F

Dialog HF LIPID LDL 130-159 Pre-conversion codes

Procedure Code: 3050F

Taxonomy HF LIPID LDL \>190 added to dialog.

Taxonomy HF LIPID LDL \>190 post-conversion codes list:

Procedure Code: 3050F

Dialog HF LIPID LDL 71-99 Pre-conversion codes

Procedure Code: 3048F

Taxonomy HF LIPID LDL 71-99 added to dialog.

Taxonomy HF LIPID LDL 71-99 post-conversion codes list:

Procedure Code: 3048F

Dialog HF LIPID LDL \<=70 Pre-conversion codes

Procedure Code: 3048F

Taxonomy HF LIPID LDL 71-99 added to dialog.

Taxonomy HF LIPID LDL 71-99 post-conversion codes list:

Procedure Code: 3048F

Dialog VA-GP IM PNEUMOC PPSV23 PNEUMOVAX Pre-conversion codes

Procedure Code: 90471

Procedure Code: 90732

Taxonomy GP IM PNEUMOC PPSV23 PNEUMOVAX added to dialog.

Taxonomy GP IM PNEUMOC PPSV23 PNEUMOVAX post-conversion codes list:

Procedure Code: 90471

Procedure Code: 90732

Dialog VA-PALLI CONS OUTPT 99245 (E) Pre-conversion codes

Procedure Code: 99245

Taxonomy 691 PALL OUTPT 99245 added to dialog.

Taxonomy 691 PALL OUTPT 99245 post-conversion codes list:

Procedure Code: 99245

Dialog VA-PALLI CONS OUTPT 99244 (E) Pre-conversion codes

Procedure Code: 99244

Taxonomy 691 PALL OUTPT 99244 added to dialog.

Taxonomy 691 PALL OUTPT 99244 post-conversion codes list:

Procedure Code: 99244

Dialog VA-PALLI CONS OUTPT 99243 (E) Pre-conversion codes

Procedure Code: 99243

Taxonomy 691 PALL OUTPT 99243 added to dialog.

Taxonomy 691 PALL OUTPT 99243 post-conversion codes list:

Procedure Code: 99243

Dialog VA-PALLI CONS OUTPT 99242 (E) Pre-conversion codes

Procedure Code: 99242

Taxonomy 691 PALL OUTPT 99242 added to dialog.

Taxonomy 691 PALL OUTPT 99242 post-conversion codes list:

Procedure Code: 99242

Dialog VA-PALLI CONS OUTPT 99241 (E) Pre-conversion codes

Procedure Code: 99241

Taxonomy 691 PALL OUTPT 99241 added to dialog.

Taxonomy 691 PALL OUTPT 99241 post-conversion codes list:

Procedure Code: 99241

Dialog VA-PALLI CONS OUTPT ENCOUNTER GP Pre-conversion codes

Diagnosis Code: V66.7

Taxonomy 691 PALL INPT ENCOUNTER added to dialog.

Taxonomy 691 PALL INPT ENCOUNTER post-conversion codes list:

Diagnosis Code: V66.7

Dialog VA-PALLI CONS INPT 99255 (E) Pre-conversion codes

Procedure Code: 99255

Taxonomy 691 PALL INPT 99255 added to dialog.

Taxonomy 691 PALL INPT 99255 post-conversion codes list:

Procedure Code: 99255

Dialog VA-PALLI CONS INPT 99254 (E) Pre-conversion codes

Procedure Code: 99254

Taxonomy 691 PALL INPT 99254 added to dialog.

Taxonomy 691 PALL INPT 99254 post-conversion codes list:

Procedure Code: 99254

Dialog VA-PALLI CONS INPT 99253 (E) Pre-conversion codes

Procedure Code: 99253

Taxonomy 691 PALL INPT 99253 added to dialog.

Taxonomy 691 PALL INPT 99253 post-conversion codes list:

Procedure Code: 99253

Dialog VA-PALLI CONS INPT 99252 (E) Pre-conversion codes

Procedure Code: 99252

Taxonomy 691 PALL INPT 99252 added to dialog.

Taxonomy 691 PALL INPT 99252 post-conversion codes list:

Procedure Code: 99252

Dialog VA-PALLI CONS INPT 99251 (E) Pre-conversion codes

Procedure Code: 99251

Taxonomy 691 PALL INPT 99251 added to dialog.

Taxonomy 691 PALL INPT 99251 post-conversion codes list:

Procedure Code: 99251

Dialog VA-PALLI CONS INPT ENCOUNTER GP Pre-conversion codes

Diagnosis Code: V66.7

Taxonomy 691 PALL INPT ENCOUNTER added to dialog.

Taxonomy 691 PALL INPT ENCOUNTER post-conversion codes list:

Diagnosis Code: V66.7

Dialog VA-GP IM PNEUMOC PCV13 PREVNAR Pre-conversion codes

Procedure Code: 90471

Procedure Code: 90670

Taxonomy GP IM PNEUMOC PCV13 PREVNAR added to dialog.

Taxonomy GP IM PNEUMOC PCV13 PREVNAR post-conversion codes list:

Procedure Code: 90471

Procedure Code: 90670

Dialog VA-PALLI CONS PT PREFER DOC NO (E) Pre-conversion codes

Procedure Code: G8260

Taxonomy PALLI CONS PT PREFER DOC NO (E) added to dialog.

Taxonomy PALLI CONS PT PREFER DOC NO (E) post-conversion codes list:

Procedure Code: G8260

Dialog VA-PALLI CONS PT PREFER DOC YES (E) Pre-conversion codes

Procedure Code: 1123F

Taxonomy PALLI CONS PT PREFER DOC YES (E) added to dialog.

Taxonomy PALLI CONS PT PREFER DOC YES (E) post-conversion codes list:

Procedure Code: 1123F

Dialog VA-PALLI CONS SURROGATE INFO DOC NO (E) Pre-conversion codes

Procedure Code: G8260

Taxonomy PALLI CONS PT PREFER DOC NO (E) added to dialog.

Taxonomy PALLI CONS PT PREFER DOC NO (E) post-conversion codes list:

Procedure Code: G8260

Dialog VA-PALLI CONS SURROGATE INFO DOC YES (E) Pre-conversion codes

Procedure Code: 1123F

Taxonomy PALLI CONS PT PREFER DOC YES (E) added to dialog.

Taxonomy PALLI CONS PT PREFER DOC YES (E) post-conversion codes list:

Procedure Code: 1123F

Dialog VA-PALLI CONS DYSPNEA SEVERE (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA MODERATE (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA MILD (E) Pre-conversion codes

Procedure Code: 3450F

Taxonomy PALLI CONS DYSPNEA MILD (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA MILD (E) post-conversion codes list:

Procedure Code: 3450F

Dialog VA-PALLI CONS DYSPNEA NONE (E) Pre-conversion codes

Procedure Code: 3450F

Taxonomy PALLI CONS DYSPNEA MILD (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA MILD (E) post-conversion codes list:

Procedure Code: 3450F

Dialog VA-PALLI CONS DYSPNEA 10 (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA 9 (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA 8 (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA 7 (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA 6 (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA 5 (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA 4 (E) Pre-conversion codes

Procedure Code: 3451F

Taxonomy PALLI CONS DYSPNEA SEVERE (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA SEVERE (E) post-conversion codes list:

Procedure Code: 3451F

Dialog VA-PALLI CONS DYSPNEA 3 (E) Pre-conversion codes

Procedure Code: 3450F

Taxonomy PALLI CONS DYSPNEA MILD (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA MILD (E) post-conversion codes list:

Procedure Code: 3450F

Dialog VA-PALLI CONS DYSPNEA 2 (E) Pre-conversion codes

Procedure Code: 3450F

Taxonomy PALLI CONS DYSPNEA MILD (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA MILD (E) post-conversion codes list:

Procedure Code: 3450F

Dialog VA-PALLI CONS DYSPNEA 1 (E) Pre-conversion codes

Procedure Code: 3450F

Taxonomy PALLI CONS DYSPNEA MILD (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA MILD (E) post-conversion codes list:

Procedure Code: 3450F

Dialog VA-PALLI CONS DYSPNEA 0 (E) Pre-conversion codes

Procedure Code: 3450F

Taxonomy PALLI CONS DYSPNEA MILD (E) added to dialog.

Taxonomy PALLI CONS DYSPNEA MILD (E) post-conversion codes list:

Procedure Code: 3450F

Dialog VA-PALLI CONS PAIN SEVERE (E) Pre-conversion codes

Procedure Code: 1125F

Taxonomy PALLI CONS PAIN SEVERE (E) added to dialog.

Taxonomy PALLI CONS PAIN SEVERE (E) post-conversion codes list:

Procedure Code: 1125F

Dialog VA-PALLI CONS PAIN MODERATE (E) Pre-conversion codes

Procedure Code: 1125F

Taxonomy PALLI CONS PAIN SEVERE (E) added to dialog.

Taxonomy PALLI CONS PAIN SEVERE (E) post-conversion codes list:

Procedure Code: 1125F

Dialog VA-PALLI CONS PAIN MILD (E) Pre-conversion codes

Procedure Code: 1125F

Taxonomy PALLI CONS PAIN SEVERE (E) added to dialog.

Taxonomy PALLI CONS PAIN SEVERE (E) post-conversion codes list:

Procedure Code: 1125F

Dialog VA-PALLI CONS PAIN NONE (E) Pre-conversion codes

Procedure Code: 1126F

Taxonomy PALLI CONS PAIN NONE (E) added to dialog.

Taxonomy PALLI CONS PAIN NONE (E) post-conversion codes list:

Procedure Code: 1126F

Dialog HF LIPID LDL 120-129 Pre-conversion codes

Procedure Code: 3049F

Taxonomy HF LIPID LDL 120-129 added to dialog.

Taxonomy HF LIPID LDL 120-129 post-conversion codes list:

Procedure Code: 3049F

Dialog HF LIPID LDL 100-119 Pre-conversion codes

Procedure Code: 3049F

Taxonomy HF LIPID LDL 120-129 added to dialog.

Taxonomy HF LIPID LDL 120-129 post-conversion codes list:

Procedure Code: 3049F

Dialog FLU RECIEVED ELSEWHERE Pre-conversion codes

Diagnosis Code: V04.81

Procedure Code: 90658

Taxonomy FLU RECIEVED ELSEWHERE added to dialog.

Taxonomy FLU RECIEVED ELSEWHERE post-conversion codes list:

Diagnosis Code: V04.81

Procedure Code: 90658

Dialog IM PNEUMO-VAC DONE ELSEWHERE Pre-conversion codes

Diagnosis Code: V03.82

Procedure Code: 90732

Taxonomy IM PNEUMO-VAC DONE ELSEWHERE added to dialog.

Taxonomy IM PNEUMO-VAC DONE ELSEWHERE post-conversion codes list:

Diagnosis Code: V03.82

Procedure Code: 90732

Dialog IM TD-ADULT DONE ELSEWHERE Pre-conversion codes

Diagnosis Code: V06.5

Procedure Code: 90718

Taxonomy HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE added to dialog.

Taxonomy HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE post-conversion codes list:

Diagnosis Code: V06.5

Procedure Code: 90718

Dialog COLON CANCER Pre-conversion codes

Procedure Code: 44160

Taxonomy COLON CANCER added to dialog.

Taxonomy COLON CANCER post-conversion codes list:

Procedure Code: 44160

Dialog COLONOSCOPY POLYPS Pre-conversion codes

Diagnosis Code: 211.3

Taxonomy COLONOSCOPY POLYPS added to dialog.

Taxonomy COLONOSCOPY POLYPS post-conversion codes list:

Diagnosis Code: 211.3

Dialog HEP A ELSEWHERE Pre-conversion codes

Procedure Code: 90632

Taxonomy IM HEP B DONE ELSEWHERE added to dialog.

Taxonomy IM HEP B DONE ELSEWHERE post-conversion codes list:

Procedure Code: 90632

Dialog HEP B ELSEWHERE Pre-conversion codes

Procedure Code: 90636

Taxonomy HEP B ELSEWHERE added to dialog.

Taxonomy HEP B ELSEWHERE post-conversion codes list:

Procedure Code: 90636

Updating record for dialog EMPHYSEMA IEN: 196

Updating record for dialog COPD IEN: 197

Updating record for dialog COR PULMONALE IEN: 198

Updating record for dialog INTERSTITIAL DISEASE IEN: 199

Updating record for dialog MIGRAINE HEADACHES IEN: 209

Updating record for dialog CHRONIC OBSTR. BRONCHITIS IEN: 211

Updating record for dialog CHRONIC OBSTRUCTIVE ASTHMA IEN: 212

Updating record for dialog CONGESTIVE HEART FAILURE IEN: 213

Updating record for dialog SECONDARY POLYCYTHEMIA IEN: 214

Updating record for dialog SLEEP APNEA IEN: 216

Updating record for dialog TX TETANUS AND DIPHTHERIA CODES IEN: 424

Adding default Header Text for POV.

Adding default Header Text for CPT.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX TETANUS AND DIPHTHERIA CODES IEN: 424

Updating record for dialog HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE IEN: 426

Adding Taxonomy HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE as an Additional Find.

Updating edit history of the dialog.

Completed record updates for dialog HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE I6

Updating record for dialog TX HYSTERECTOMY CODES IEN: 433

Adding default Header Text for CPT.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX HYSTERECTOMY CODES IEN: 433

Updating record for dialog TX MAMMOGRAM/SCREENING CPT CODES IEN: 440

Adding default Header Text for POV.

Adding default Header Text for CPT.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX MAMMOGRAM/SCREENING CPT CODES IEN: 440

Updating record for dialog TX MASTECTOMY CODES IEN: 441

Updating record for dialog TX ISCHEMIC HEART DISEASE DIAGNOSES IEN: 558

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX ISCHEMIC HEART DISEASE DIAGNOSES IEN: 558

Updating record for dialog IM HEP B DONE ELSEWHERE IEN: 631

Adding Taxonomy IM HEP B DONE ELSEWHERE as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog IM HEP B DONE ELSEWHERE IEN: 631

Updating record for dialog TX POSITIVE PPD CODES IEN: 850

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX POSITIVE PPD CODES IEN: 850

Updating record for dialog SHE TX DEMENTIA CODES TO SCREEN DRIVING AND IEN: 124

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog SHE TX DEMENTIA CODES TO SCREEN DRIVING AND4

Updating record for dialog TX PROSTATE CANCER CODES IEN: 1230

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX PROSTATE CANCER CODES IEN: 1230

Updating record for dialog TX HEP C INFECTION IEN: 1273

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX HEP C INFECTION IEN: 1273

Updating record for dialog V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM IEN: 1294

Adding Taxonomy V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM4

Updating record for dialog V\*-HF DIAB TELERET DISPO TELERETINAL EXAM IEN: 1295

Adding Taxonomy V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog V\*-HF DIAB TELERET DISPO TELERETINAL EXAM I5

Updating record for dialog BMI CONSIDER ADDING OVERWEIGHT TO PROBLEM LIST IEN: 8

Updating record for dialog BMI CONSIDER ADDING OBESITY TO PROBLEM LIST IEN: 1343

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog BMI CONSIDER ADDING OBESITY TO PROBLEM LIST3

Updating record for dialog 691 PALL CONSULT ENCOUNTER DX IEN: 1969

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL CONSULT ENCOUNTER DX IEN: 1969

Updating record for dialog 691 PALL INPT 99255 IEN: 2015

Adding Taxonomy 691 PALL INPT 99255 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL INPT 99255 IEN: 2015

Updating record for dialog 691 PALL INPT 99254 IEN: 2018

Adding Taxonomy 691 PALL INPT 99254 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL INPT 99254 IEN: 2018

Updating record for dialog 691 PALL INPT 99253 IEN: 2019

Adding Taxonomy 691 PALL INPT 99253 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL INPT 99253 IEN: 2019

Updating record for dialog 691 PALL INPT 99252 IEN: 2020

Adding Taxonomy 691 PALL INPT 99252 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL INPT 99252 IEN: 2020

Updating record for dialog 691 PALL INPT 99251 IEN: 2021

Adding Taxonomy 691 PALL INPT 99251 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL INPT 99251 IEN: 2021

Updating record for dialog 691 PALL INPT ENCOUNTER IEN: 2022

Adding Taxonomy 691 PALL INPT ENCOUNTER as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL INPT ENCOUNTER IEN: 2022

Updating record for dialog 691 PALL OUTPT 99245 IEN: 2023

Adding Taxonomy 691 PALL OUTPT 99245 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL OUTPT 99245 IEN: 2023

Updating record for dialog 691 PALL OUTPT 99244 IEN: 2024

Adding Taxonomy 691 PALL OUTPT 99244 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL OUTPT 99244 IEN: 2024

Updating record for dialog 691 PALL OUTPT 99243 IEN: 2025

Adding Taxonomy 691 PALL OUTPT 99243 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL OUTPT 99243 IEN: 2025

Updating record for dialog 691 PALL OUTPT 99242 IEN: 2026

Adding Taxonomy 691 PALL OUTPT 99242 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL OUTPT 99242 IEN: 2026

Updating record for dialog 691 PALL OUTPT 99241 IEN: 2027

Adding Taxonomy 691 PALL OUTPT 99241 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL OUTPT 99241 IEN: 2027

Updating record for dialog 691 PALL OUTPT ENCOUNTER IEN: 2028

Adding Taxonomy 691 PALL INPT ENCOUNTER as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALL OUTPT ENCOUNTER IEN: 2028

Updating record for dialog GP TOB CURRENT USER OPTIONAL ACTIONS FY07 IEN: 2060

Adding Taxonomy GP TOB CURRENT USER OPTIONAL ACTIONS FY07 as an Additional Find.

Updating edit history of the dialog.

Completed record updates for dialog GP TOB CURRENT USER OPTIONAL ACTIONS FY07 I0

Updating record for dialog GP TOB ED COUNSELING (CURRENT USER) FY07 IEN: 2063

Adding Taxonomy GP TOB CURRENT USER OPTIONAL ACTIONS FY07 as an Additional Find.

Updating edit history of the dialog.

Completed record updates for dialog GP TOB ED COUNSELING (CURRENT USER) FY07 IE3

Updating record for dialog CCHT DISEASE INDICATIONS SUBST ABUSE IEN: 2183

Adding Taxonomy CCHT DISEASE INDICATIONS SUBST ABUSE as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CCHT DISEASE INDICATIONS SUBST ABUSE IEN: 23

Updating record for dialog CCHT DISEASE INDICATIONS PTSD (ICD9) IEN: 2184

Adding Taxonomy CCHT DISEASE INDICATIONS PTSD (ICD9) as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CCHT DISEASE INDICATIONS PTSD (ICD9) IEN: 24

Updating record for dialog CCHT DISEASE INDICATIONS DEPRESSION (ICD9) IEN: 2185

Adding Taxonomy CCHT DISEASE INDICATIONS DEPRESSION (ICD9) as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CCHT DISEASE INDICATIONS DEPRESSION (ICD9) 5

Updating record for dialog CCHT DISEASE INDICATIONS DIABETES (ICD9) IEN: 2186

Adding Taxonomy CCHT DISEASE INDICATIONS DIABETES (ICD9) as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CCHT DISEASE INDICATIONS DIABETES (ICD9) IE6

Updating record for dialog CCHT DISEASE INDICATIONS HTN (ICD9) IEN: 2187

Adding Taxonomy CCHT DISEASE INDICATIONS HTN (ICD9) as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CCHT DISEASE INDICATIONS HTN (ICD9) IEN: 217

Updating record for dialog CCHT DISEASE INDICATIONS COPD (ICD9) IEN: 2188

Adding Taxonomy CCHT DISEASE INDICATIONS COPD (ICD9) as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CCHT DISEASE INDICATIONS COPD (ICD9) IEN: 28

Updating record for dialog CCHT DISEASE INDICATIONS CHF (ICD9) IEN: 2189

Adding Taxonomy CCHT DISEASE INDICATIONS CHF (ICD9) as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CCHT DISEASE INDICATIONS CHF (ICD9) IEN: 219

Updating record for dialog EYE LEGAL BLINDNESS ICD9 369.4 IEN: 3557

Adding Taxonomy EYE LEGAL BLINDNESS ICD9 369.4 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog EYE LEGAL BLINDNESS ICD9 369.4 IEN: 3557

Updating record for dialog EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23 IEN: 3558

Adding Taxonomy EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23 8

Updating record for dialog EYE NEAR NORMAL ICD9 369.9 IEN: 3559

Adding Taxonomy EYE NEAR NORMAL ICD9 369.9 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog EYE NEAR NORMAL ICD9 369.9 IEN: 3559

Updating record for dialog EYE NORMAL VISION ICD9 367.9 IEN: 3560

Adding Taxonomy EYE NORMAL VISION ICD9 367.9 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog EYE NORMAL VISION ICD9 367.9 IEN: 3560

Updating record for dialog ICD9 250.50 IEN: 5341

Adding Taxonomy ICD9 250.50 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 250.50 IEN: 5341

Updating record for dialog ICD9 250.51 IEN: 5342

Adding Taxonomy ICD9 250.51 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 250.51 IEN: 5342

Updating record for dialog ICD9 250.52 IEN: 5343

Adding Taxonomy ICD9 250.52 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 250.52 IEN: 5343

Updating record for dialog ICD9 250.53 IEN: 5344

Adding Taxonomy ICD9 250.53 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 250.53 IEN: 5344

Updating record for dialog ICD9 362.01 IEN: 5345

Adding Taxonomy ICD9 362.01 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.01 IEN: 5345

Updating record for dialog ICD9 362.02 IEN: 5346

Adding Taxonomy ICD9 362.02 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.02 IEN: 5346

Updating record for dialog ICD9 250.02 IEN: 5349

Adding Taxonomy ICD9 250.02 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 250.02 IEN: 5349

Updating record for dialog ICD9 250.01 IEN: 5350

Adding Taxonomy ICD9 250.01 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 250.01 IEN: 5350

Updating record for dialog ICD9 250.00 IEN: 5352

Adding Taxonomy CCHT DISEASE INDICATIONS DIABETES (ICD9) as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 250.00 IEN: 5352

Updating record for dialog V\*-DG DIAB EYE CODES IEN: 5355

Adding Taxonomy V\*-DG DIAB EYE CODES as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog V\*-DG DIAB EYE CODES IEN: 5355

Updating record for dialog ICD9 362.13 IEN: 5364

Adding Taxonomy ICD9 362.13 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.13 IEN: 5364

Updating record for dialog ICD9 250.03 IEN: 5413

Adding Taxonomy ICD9 250.03 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 250.03 IEN: 5413

Updating record for dialog ICD9 362.03 IEN: 6113

Adding Taxonomy ICD9 362.03 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.03 IEN: 6113

Updating record for dialog ICD9 362.04 IEN: 6114

Adding Taxonomy ICD9 362.04 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.04 IEN: 6114

Updating record for dialog ICD9 362.05 IEN: 6115

Adding Taxonomy ICD9 362.05 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.05 IEN: 6115

Updating record for dialog ICD9 362.06 IEN: 6116

Adding Taxonomy ICD9 362.06 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.06 IEN: 6116

Updating record for dialog ICD9 362.10 IEN: 6117

Adding Taxonomy ICD9 362.10 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.10 IEN: 6117

Updating record for dialog ICD9 362.07 IEN: 6118

Adding Taxonomy ICD9 362.07 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 362.07 IEN: 6118

Updating record for dialog 691 PALLI CONS OUTPT ENCOUNTER GP IEN: 6914

Adding Taxonomy 691 PALL INPT ENCOUNTER as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS OUTPT ENCOUNTER GP IEN: 6914

Updating record for dialog 691 PALLI CONS INPT ENCOUNTER GP IEN: 6915

Adding Taxonomy 691 PALL INPT ENCOUNTER as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS INPT ENCOUNTER GP IEN: 6915

Updating record for dialog 691 PALLI CONS INFECTIOUS COND TAX GP IEN: 6917

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS INFECTIOUS COND TAX GP IEN: 7

Updating record for dialog 691 PALLI CONS RHEUM/VAS/THROM COND TAX GP IEN: 6918

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS RHEUM/VAS/THROM COND TAX GP 8

Updating record for dialog 691 PALLI CONS DERMATOLOGIC DX IEN: 6919

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS DERMATOLOGIC DX IEN: 6919

Updating record for dialog 691 PALLI CONS RENAL COND TAX GP IEN: 6920

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS RENAL COND TAX GP IEN: 6920

Updating record for dialog 691 PALLI CONS GI COND TAX GP IEN: 6921

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS GI COND TAX GP IEN: 6921

Updating record for dialog 691 PALLI CONS CARDIO COND TAX GP IEN: 6922

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS CARDIO COND TAX GP IEN: 6922

Updating record for dialog 691 PALLI CONS CNS COND TAX GP IEN: 6923

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS CNS COND TAX GP IEN: 6923

Updating record for dialog 691 PALLI CONS CANCER/HEMA COND TAX GP IEN: 6924

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog 691 PALLI CONS CANCER/HEMA COND TAX GP IEN:4

Updating record for dialog CANCER OF THE PANCREAS ICD9 157.9 IEN: 6970

Adding Taxonomy CANCER OF THE PANCREAS ICD9 157.9 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CANCER OF THE PANCREAS ICD9 157.9 IEN: 6970

Updating record for dialog CANCER OF THE LIVER ICD9 155.2 IEN: 6971

Adding Taxonomy CANCER OF THE LIVER ICD9 155.2 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CANCER OF THE LIVER ICD9 155.2 IEN: 6971

Updating record for dialog CANCER OF THE ESOPHAGUS ICD9 150.9 IEN: 6972

Adding Taxonomy CANCER OF THE ESOPHAGUS ICD9 150.9 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog CANCER OF THE ESOPHAGUS ICD9 150.9 IEN: 6972

Updating record for dialog ECH TOBACCO ADD HX TO PL IEN: 7011

Adding Taxonomy ECH TOBACCO ADD HX TO PL as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ECH TOBACCO ADD HX TO PL IEN: 7011

Updating record for dialog TX TERMINAL CANCER CODES IEN: 7056

Updating record for dialog ICD9 NURSE ED REFER PWA IEN: 7319

Adding Taxonomy ICD9 NURSE ED REFER PWA as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog ICD9 NURSE ED REFER PWA IEN: 7319

Updating record for dialog HF LIPID LDL \>190 IEN: 7539

Adding Taxonomy HF LIPID LDL \>190 as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HF LIPID LDL \>190 IEN: 7539

Updating record for dialog HF LIPID LDL 160-190 IEN: 7540

Adding Taxonomy HF LIPID LDL \>190 as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HF LIPID LDL 160-190 IEN: 7540

Updating record for dialog HF LIPID LDL 130-159 IEN: 7541

Adding Taxonomy HF LIPID LDL \>190 as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HF LIPID LDL 130-159 IEN: 7541

Updating record for dialog HF LIPID LDL 71-99 IEN: 7542

Adding Taxonomy HF LIPID LDL 71-99 as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HF LIPID LDL 71-99 IEN: 7542

Updating record for dialog HF LIPID LDL \<=70 IEN: 7543

Adding Taxonomy HF LIPID LDL 71-99 as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HF LIPID LDL \<=70 IEN: 7543

Updating record for dialog VA-ECOE DX LIST IEN: 7709

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-ECOE DX LIST IEN: 7709

Updating record for dialog VA-GP IM PNEUMOC PPSV23 PNEUMOVAX IEN: 8228

Adding Taxonomy GP IM PNEUMOC PPSV23 PNEUMOVAX as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-GP IM PNEUMOC PPSV23 PNEUMOVAX IEN: 8228

Updating record for dialog VA-PALLI CONS OUTPT 99245 (E) IEN: 8261

Adding Taxonomy 691 PALL OUTPT 99245 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS OUTPT 99245 (E) IEN: 8261

Updating record for dialog VA-PALLI CONS OUTPT 99244 (E) IEN: 8262

Adding Taxonomy 691 PALL OUTPT 99244 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS OUTPT 99244 (E) IEN: 8262

Updating record for dialog VA-PALLI CONS OUTPT 99243 (E) IEN: 8263

Adding Taxonomy 691 PALL OUTPT 99243 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS OUTPT 99243 (E) IEN: 8263

Updating record for dialog VA-PALLI CONS OUTPT 99242 (E) IEN: 8264

Adding Taxonomy 691 PALL OUTPT 99242 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS OUTPT 99242 (E) IEN: 8264

Updating record for dialog VA-PALLI CONS OUTPT 99241 (E) IEN: 8265

Adding Taxonomy 691 PALL OUTPT 99241 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS OUTPT 99241 (E) IEN: 8265

Updating record for dialog VA-PALLI CONS OUTPT ENCOUNTER GP IEN: 8266

Adding Taxonomy 691 PALL INPT ENCOUNTER as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS OUTPT ENCOUNTER GP IEN: 8266

Updating record for dialog VA-PALLI CONS INPT 99255 (E) IEN: 8267

Adding Taxonomy 691 PALL INPT 99255 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS INPT 99255 (E) IEN: 8267

Updating record for dialog VA-PALLI CONS INPT 99254 (E) IEN: 8268

Adding Taxonomy 691 PALL INPT 99254 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS INPT 99254 (E) IEN: 8268

Updating record for dialog VA-PALLI CONS INPT 99253 (E) IEN: 8269

Adding Taxonomy 691 PALL INPT 99253 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS INPT 99253 (E) IEN: 8269

Updating record for dialog VA-PALLI CONS INPT 99252 (E) IEN: 8270

Adding Taxonomy 691 PALL INPT 99252 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS INPT 99252 (E) IEN: 8270

Updating record for dialog VA-PALLI CONS INPT 99251 (E) IEN: 8271

Adding Taxonomy 691 PALL INPT 99251 as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS INPT 99251 (E) IEN: 8271

Updating record for dialog VA-PALLI CONS INPT ENCOUNTER GP IEN: 8272

Adding Taxonomy 691 PALL INPT ENCOUNTER as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS INPT ENCOUNTER GP IEN: 8272

Updating record for dialog VA-PALLI CONS INFECTIOUS COND TAX GP IEN: 8274

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS INFECTIOUS COND TAX GP IEN: 84

Updating record for dialog VA-PALLI CONS RHEUM/VAS/THROM COND TAX GP IEN: 8275

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS RHEUM/VAS/THROM COND TAX GP I5

Updating record for dialog VA-PALLI CONS DERMATOLOGIC TAX DX GP IEN: 8276

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DERMATOLOGIC TAX DX GP IEN: 86

Updating record for dialog VA-PALLI CONS RENAL COND TAX GP IEN: 8277

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS RENAL COND TAX GP IEN: 8277

Updating record for dialog VA-PALLI CONS GI COND TAX GP IEN: 8278

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS GI COND TAX GP IEN: 8278

Updating record for dialog VA-PALLI CONS CARDIO COND TAX GP IEN: 8279

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS CARDIO COND TAX GP IEN: 8279

Updating record for dialog VA-PALLI CONS CNS COND TAX GP IEN: 8280

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS CNS COND TAX GP IEN: 8280

Updating record for dialog VA-PALLI CONS CANCER/HEMA COND TAX GP IEN: 8281

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS CANCER/HEMA COND TAX GP IEN: 1

Updating record for dialog VA-GP IM PNEUMOC PCV13 PREVNAR IEN: 8307

Adding Taxonomy GP IM PNEUMOC PCV13 PREVNAR as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-GP IM PNEUMOC PCV13 PREVNAR IEN: 8307

Updating record for dialog VA-PALLI CONS PT PREFER DOC NO (E) IEN: 8337

Adding Taxonomy PALLI CONS PT PREFER DOC NO (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS PT PREFER DOC NO (E) IEN: 8337

Updating record for dialog VA-PALLI CONS PT PREFER DOC YES (E) IEN: 8338

Adding Taxonomy PALLI CONS PT PREFER DOC YES (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS PT PREFER DOC YES (E) IEN: 838

Updating record for dialog VA-PALLI CONS SURROGATE INFO DOC NO (E) IEN: 8342

Adding Taxonomy PALLI CONS PT PREFER DOC NO (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS SURROGATE INFO DOC NO (E) IEN2

Updating record for dialog VA-PALLI CONS SURROGATE INFO DOC YES (E) IEN: 8343

Adding Taxonomy PALLI CONS PT PREFER DOC YES (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS SURROGATE INFO DOC YES (E) IE3

Updating record for dialog VA-PALLI CONS DYSPNEA SEVERE (E) IEN: 8476

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA SEVERE (E) IEN: 8476

Updating record for dialog VA-PALLI CONS DYSPNEA MODERATE (E) IEN: 8477

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA MODERATE (E) IEN: 8477

Updating record for dialog VA-PALLI CONS DYSPNEA MILD (E) IEN: 8478

Adding Taxonomy PALLI CONS DYSPNEA MILD (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA MILD (E) IEN: 8478

Updating record for dialog VA-PALLI CONS DYSPNEA NONE (E) IEN: 8479

Adding Taxonomy PALLI CONS DYSPNEA MILD (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA NONE (E) IEN: 8479

Updating record for dialog VA-PALLI CONS DYSPNEA 10 (E) IEN: 8481

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 10 (E) IEN: 8481

Updating record for dialog VA-PALLI CONS DYSPNEA 9 (E) IEN: 8482

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 9 (E) IEN: 8482

Updating record for dialog VA-PALLI CONS DYSPNEA 8 (E) IEN: 8483

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 8 (E) IEN: 8483

Updating record for dialog VA-PALLI CONS DYSPNEA 7 (E) IEN: 8484

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 7 (E) IEN: 8484

Updating record for dialog VA-PALLI CONS DYSPNEA 6 (E) IEN: 8485

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 6 (E) IEN: 8485

Updating record for dialog VA-PALLI CONS DYSPNEA 5 (E) IEN: 8486

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 5 (E) IEN: 8486

Updating record for dialog VA-PALLI CONS DYSPNEA 4 (E) IEN: 8487

Adding Taxonomy PALLI CONS DYSPNEA SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 4 (E) IEN: 8487

Updating record for dialog VA-PALLI CONS DYSPNEA 3 (E) IEN: 8488

Adding Taxonomy PALLI CONS DYSPNEA MILD (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 3 (E) IEN: 8488

Updating record for dialog VA-PALLI CONS DYSPNEA 2 (E) IEN: 8489

Adding Taxonomy PALLI CONS DYSPNEA MILD (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 2 (E) IEN: 8489

Updating record for dialog VA-PALLI CONS DYSPNEA 1 (E) IEN: 8490

Adding Taxonomy PALLI CONS DYSPNEA MILD (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 1 (E) IEN: 8490

Updating record for dialog VA-PALLI CONS DYSPNEA 0 (E) IEN: 8491

Adding Taxonomy PALLI CONS DYSPNEA MILD (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS DYSPNEA 0 (E) IEN: 8491

Updating record for dialog VA-PALLI CONS PAIN SEVERE (E) IEN: 8494

Adding Taxonomy PALLI CONS PAIN SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS PAIN SEVERE (E) IEN: 8494

Updating record for dialog VA-PALLI CONS PAIN MODERATE (E) IEN: 8495

Adding Taxonomy PALLI CONS PAIN SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS PAIN MODERATE (E) IEN: 8495

Updating record for dialog VA-PALLI CONS PAIN MILD (E) IEN: 8496

Adding Taxonomy PALLI CONS PAIN SEVERE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS PAIN MILD (E) IEN: 8496

Updating record for dialog VA-PALLI CONS PAIN NONE (E) IEN: 8497

Adding Taxonomy PALLI CONS PAIN NONE (E) as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog VA-PALLI CONS PAIN NONE (E) IEN: 8497

Updating record for dialog HF LIPID LDL 120-129 IEN: 13223

Adding Taxonomy HF LIPID LDL 120-129 as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HF LIPID LDL 120-129 IEN: 13223

Updating record for dialog HF LIPID LDL 100-119 IEN: 13224

Adding Taxonomy HF LIPID LDL 120-129 as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HF LIPID LDL 100-119 IEN: 13224

Updating record for dialog FLU RECIEVED ELSEWHERE IEN: 442000200

Adding Taxonomy FLU RECIEVED ELSEWHERE as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog FLU RECIEVED ELSEWHERE IEN: 442000200

Updating record for dialog TX NEW EMPLOYEE CODES IEN: 442000227

Updating record for dialog IM PNEUMO-VAC DONE ELSEWHERE IEN: 442000250

Adding Taxonomy IM PNEUMO-VAC DONE ELSEWHERE as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog IM PNEUMO-VAC DONE ELSEWHERE IEN: 442000250

Updating record for dialog IM TD-ADULT DONE ELSEWHERE IEN: 442000265

Adding Taxonomy HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE as an Additional Find.

Updating edit history of the dialog.

Completed record updates for dialog IM TD-ADULT DONE ELSEWHERE IEN: 442000265

Updating record for dialog COLON CANCER IEN: 442000277

Adding Taxonomy COLON CANCER as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog COLON CANCER IEN: 442000277

Updating record for dialog COLONOSCOPY POLYPS IEN: 442000278

Adding Taxonomy COLONOSCOPY POLYPS as a Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog COLONOSCOPY POLYPS IEN: 442000278

Updating record for dialog TX PRIOR DX OF MI IEN: 442000346

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX PRIOR DX OF MI IEN: 442000346

Updating record for dialog HEP A ELSEWHERE IEN: 442000355

Adding Taxonomy IM HEP B DONE ELSEWHERE as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HEP A ELSEWHERE IEN: 442000355

Updating record for dialog HEP B ELSEWHERE IEN: 442000366

Adding Taxonomy HEP B ELSEWHERE as an Additional Finding Item.

Updating edit history of the dialog.

Completed record updates for dialog HEP B ELSEWHERE IEN: 442000366

Updating record for dialog TX TOBACCO USE CODES IEN: 442000839

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX TOBACCO USE CODES IEN: 442000839

Updating record for dialog TX DEPRESSION SCREEN CODE IEN: 567000234

Adding default Header Text for POV.

Adding prompts to the dialog.

Updating edit history of the dialog.

Completed record updates for dialog TX DEPRESSION SCREEN CODE IEN: 567000234

Overview

Created 64 taxonomies

Updated 135 dialogs

Converting ADD TO PROBLEM LIST IEN: 4557

to national value PXRM FV ADD TO PROBLEM LIST

There are 3 Reminder Exchange entries to be installed.

1\. Installing Reminder Exchange entry PXRM PATCH 26 DIALOG UPDATES

2\. Installing Reminder Exchange entry PXRM PATCH 26 ECOE UPDATE

3\. Installing Reminder Exchange entry PXRM PATCH 26 PALLIATIVE CARE UPDATE

Building Selected Codes multiple indexes.

Taxonomy: 691 PALL INPT 99251; IEN=135

Taxonomy: 691 PALL INPT 99252; IEN=134

Taxonomy: 691 PALL INPT 99253; IEN=133

Taxonomy: 691 PALL INPT 99254; IEN=132

Taxonomy: 691 PALL INPT 99255; IEN=131

Taxonomy: 691 PALL INPT ENCOUNTER; IEN=136

Taxonomy: 691 PALL OUTPT 99241; IEN=142

Taxonomy: 691 PALL OUTPT 99242; IEN=141

Taxonomy: 691 PALL OUTPT 99243; IEN=140

Taxonomy: 691 PALL OUTPT 99244; IEN=139

Taxonomy: 691 PALL OUTPT 99245; IEN=137

Taxonomy: 691 PALLI CONS CANCER/HEMA COND; IEN=107

Taxonomy: 691 PALLI CONS CARDIO COND OTHER THAN CA; IEN=105

Taxonomy: 691 PALLI CONS CNS COND OTHER THAN CA; IEN=106

Taxonomy: 691 PALLI CONS DERM CONDITION DX; IEN=102

Taxonomy: 691 PALLI CONS GI OTHER THAN CA; IEN=104

Taxonomy: 691 PALLI CONS INFECTIOUS COND; IEN=100

Taxonomy: 691 PALLI CONS RENAL OTHER THAN CA; IEN=103

Taxonomy: 691 PALLI CONS RHEUM/VASC/THROMB; IEN=101

Taxonomy: ACUTE MI; IEN=442036

Taxonomy: Advance Directives; IEN=43

Taxonomy: BILATERIAL MASTECTOMY; IEN=442014

Taxonomy: CA pneumonia; IEN=53

Taxonomy: CA-ESOPH LIVER PANCREAS; IEN=75

Taxonomy: CANCER OF THE ESOPHAGUS ICD9 150.9; IEN=175

Taxonomy: CANCER OF THE LIVER ICD9 155.2; IEN=174

Taxonomy: CANCER OF THE PANCREAS ICD9 157.9; IEN=173

Taxonomy: CCHT DISEASE INDICATIONS CHF (ICD9); IEN=150

Taxonomy: CCHT DISEASE INDICATIONS COPD (ICD9); IEN=149

Taxonomy: CCHT DISEASE INDICATIONS DEPRESSION (ICD9); IEN=146

Taxonomy: CCHT DISEASE INDICATIONS DIABETES (ICD9); IEN=147

Taxonomy: CCHT DISEASE INDICATIONS HTN (ICD9); IEN=148

Taxonomy: CCHT DISEASE INDICATIONS PTSD (ICD9); IEN=145

Taxonomy: CCHT DISEASE INDICATIONS SUBST ABUSE; IEN=144

Taxonomy: CHEY-BIL AMPUTEE; IEN=442020

Taxonomy: CHEY-CERVICAL CANCER SCREEN; IEN=442013

Taxonomy: CHEY-COPD; IEN=442002

Taxonomy: CHEY-CVA; IEN=442015

Taxonomy: CHEY-EMP; IEN=442011

Taxonomy: CHEY-HEALTHY LIFESTYLE; IEN=442005

Taxonomy: CHEY-HEP A VACCINE; IEN=442012

Taxonomy: CHEY-HEP B VACCINE; IEN=442008

Taxonomy: CHEY-HGB A1C; IEN=442016

Taxonomy: CHEY-HYSTERECTOMY; IEN=442010

Taxonomy: CHEY-MAMMOGRAM SCREENS; IEN=71

Taxonomy: CHEY-PARAPLEGIC; IEN=442017

Taxonomy: CHEY-SPIROMETRY/PFT; IEN=442003

Taxonomy: CHEY-TB HIGH RISK; IEN=442009

Taxonomy: CHEY-TOTAL BLINDNESS; IEN=442019

Taxonomy: CHRONIC OBSTRUCTIVE ASTHMA; IEN=39

Taxonomy: CHRONIC OBSTRUCTIVE BRONCHITIS; IEN=38

Taxonomy: CHY AAA DIAGNOSIS; IEN=69

Taxonomy: CHY-HYPOTHYROIDISM; IEN=68

Taxonomy: COLITIS/ILEITIS(GJ); IEN=442030

Taxonomy: COLON CANCER; IEN=192

Taxonomy: COLON POLYPS; IEN=442028

Taxonomy: COLON REMOVAL; IEN=442001

Taxonomy: COLON REMOVAL-TOTAL; IEN=442023

Taxonomy: COLONOSCOPY; IEN=442022

Taxonomy: COLONOSCOPY POLYPS; IEN=193

Taxonomy: COLORECTAL CANCER; IEN=442024

Taxonomy: CONGESTIVE HEALTH FAILURE; IEN=40

Taxonomy: COPD; IEN=7

Taxonomy: COR PULMONALE; IEN=12

Taxonomy: DEMENTIA CODES - SHERIDAN; IEN=67

Taxonomy: DEPRESSION CODES; IEN=46

Taxonomy: DEPRESSION SCREEN; IEN=567007

Taxonomy: DIABETES; IEN=674022

Taxonomy: DIABETIC EYE EXAM; IEN=442021

Taxonomy: DIABETIC/RENAL DISEASE; IEN=526016

Taxonomy: ECH TOBACCO ADD HX TO PL; IEN=177

Taxonomy: EMPHYSEMA; IEN=3

Taxonomy: ESOPHAGUS CANCER; IEN=54

Taxonomy: EYE LEGAL BLINDNESS ICD9 369.4; IEN=151

Taxonomy: EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23; IEN=152

Taxonomy: EYE NEAR NORMAL ICD9 369.9; IEN=153

Taxonomy: EYE NORMAL VISION ICD9 367.9; IEN=154

Taxonomy: FAMILY HX of Colon CA; IEN=442025

Taxonomy: FEMALE ENDOMETRIUM/OVARIAN(GJ); IEN=442029

Taxonomy: FLU RECIEVED ELSEWHERE; IEN=190

Taxonomy: FOBT COMPLETE; IEN=58

Taxonomy: GP IM PNEUMOC PCV13 PREVNAR; IEN=182

Taxonomy: GP IM PNEUMOC PPSV23 PNEUMOVAX; IEN=181

Taxonomy: GP TOB CURRENT USER OPTIONAL ACTIONS FY07; IEN=143

Taxonomy: HEART FAILURE; IEN=57

Taxonomy: HEP B ELSEWHERE; IEN=194

Taxonomy: HEP C INFECTION; IEN=442007

Taxonomy: HF LIPID LDL 120-129; IEN=189

Taxonomy: HF LIPID LDL 71-99; IEN=180

Taxonomy: HF LIPID LDL \>190; IEN=179

Taxonomy: HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE; IEN=128

Taxonomy: HIGH RISK COLON POLPS; IEN=51

Taxonomy: HIGH RISK COLONOSCOPY; IEN=48

Taxonomy: HIGH RISK FLU/PNEUMONIA; IEN=442004

Taxonomy: HISTORY OF COLON POLYPS; IEN=442035

Taxonomy: HIV TX; IEN=83

Taxonomy: HPV VACCINE CPT CODE; IEN=76

Taxonomy: HYPOXIA; IEN=37

Taxonomy: ICD9 250.01; IEN=163

Taxonomy: ICD9 250.02; IEN=162

Taxonomy: ICD9 250.03; IEN=166

Taxonomy: ICD9 250.50; IEN=155

Taxonomy: ICD9 250.51; IEN=156

Taxonomy: ICD9 250.52; IEN=157

Taxonomy: ICD9 250.53; IEN=158

Taxonomy: ICD9 362.01 ; IEN=159

Taxonomy: ICD9 362.02 ; IEN=161

Taxonomy: ICD9 362.03; IEN=167

Taxonomy: ICD9 362.04; IEN=168

Taxonomy: ICD9 362.05; IEN=169

Taxonomy: ICD9 362.06; IEN=170

Taxonomy: ICD9 362.07; IEN=172

Taxonomy: ICD9 362.10; IEN=171

Taxonomy: ICD9 362.13; IEN=165

Taxonomy: ICD9 NURSE ED REFER PWA; IEN=178

Taxonomy: IHD PROCEDURES; IEN=108

Taxonomy: IM HEP B DONE ELSEWHERE; IEN=129

Taxonomy: IM PNEUMO-VAC DONE ELSEWHERE; IEN=191

Taxonomy: INTERSTITIAL DISEASE; IEN=13

Taxonomy: IRRITABLE BOWEL SYNDROME; IEN=442037

Taxonomy: LESION REMOVAL/COLONOSCOPY; IEN=442034

Taxonomy: LIVER CANCER; IEN=55

Taxonomy: LV NON-VESTED PATIENTS; IEN=109

Taxonomy: MIGRAIN HEADACHES; IEN=14

Taxonomy: NEW EMPLOYEE CODES; IEN=442018

Taxonomy: OBESITY 278.00; IEN=73

Taxonomy: OSTEOPOROSIS; IEN=138

Taxonomy: OVERWEIGHT; IEN=72

Taxonomy: PALLI CONS DYSPNEA MILD (E); IEN=186

Taxonomy: PALLI CONS DYSPNEA SEVERE (E); IEN=185

Taxonomy: PALLI CONS PAIN NONE (E); IEN=188

Taxonomy: PALLI CONS PAIN SEVERE (E); IEN=187

Taxonomy: PALLI CONS PT PREFER DOC NO (E); IEN=183

Taxonomy: PALLI CONS PT PREFER DOC YES (E); IEN=184

Taxonomy: PALLIATIVE CONSULT ENCOUNTER DX; IEN=82

Taxonomy: PANCREAS CANCER; IEN=56

Taxonomy: POSITIVE PPD; IEN=442033

Taxonomy: POST-OP WOUND INFECTION; IEN=59

Taxonomy: REGIONAL ENTERITIS; IEN=442026

Taxonomy: SATP ENROLLMENT; IEN=47

Taxonomy: SCHIZOPHRENIA; IEN=442032

Taxonomy: SECONDARY POLYCYTHEMIA; IEN=41

Taxonomy: SIGMOIDOSCOPY; IEN=442031

Taxonomy: SLC-MOVE CO-MORBIDITIES; IEN=74

Taxonomy: SLEEP APNEA; IEN=42

Taxonomy: TETANUS DIPHTHERIA CHY; IEN=80

Taxonomy: TOBACCO USE; IEN=436024

Taxonomy: TOBACCO USE ACTIVE PROBLEM LIST; IEN=110

Taxonomy: TOBACCO USE DX; IEN=111

Taxonomy: ULCERATIVE COLITIS; IEN=442027

Taxonomy: URINARY INCONTINENCE; IEN=99

Taxonomy: V\*-DG DIAB EYE CODES; IEN=164

Taxonomy: V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM; IEN=130

Taxonomy: V20-DIABETES; IEN=81

Taxonomy: V23 TDAP CPT CODES; IEN=79

Taxonomy: V23 TETANUS DIPHTHERIA; IEN=78

Taxonomy: VA-ABD AORTIC ANEURYSM; IEN=215

Taxonomy: VA-ALCOHOL ABUSE; IEN=17

Taxonomy: VA-ALCOHOLISM SCREENING; IEN=34

Taxonomy: VA-BREAST TUMOR; IEN=18

Taxonomy: VA-CERVICAL CA/ABNORMAL PAP; IEN=5

Taxonomy: VA-CERVICAL CANCER SCREEN; IEN=30

Taxonomy: VA-CHOLESTEROL; IEN=24

Taxonomy: VA-COLORECTAL CA; IEN=4

Taxonomy: VA-COLORECTAL CANCER SCREEN; IEN=31

Taxonomy: VA-DEPRESSION DIAGNOSIS; IEN=49

Taxonomy: VA-DEPRESSION DX OUTPT VISIT; IEN=160

Taxonomy: VA-DIABETES; IEN=28

Taxonomy: VA-DIABETES HEDIS; IEN=317

Taxonomy: VA-DIABETES HEDIS PROB LIST; IEN=316

Taxonomy: VA-ECOE DIAGNOSIS CODES; IEN=115

Taxonomy: VA-EXERCISE COUNSELING; IEN=32

Taxonomy: VA-FLEXISIGMOIDOSCOPY; IEN=15

Taxonomy: VA-FOBT; IEN=27

Taxonomy: VA-HEPATITIS C INFECTION; IEN=2

Taxonomy: VA-HIGH RISK FOR FLU/PNEUMONIA; IEN=9

Taxonomy: VA-HIGH RISK FOR INFLUENZA; IEN=220

Taxonomy: VA-HIGH RISK FOR TB; IEN=11

Taxonomy: VA-HYPERTENSION; IEN=1

Taxonomy: VA-HYPERTENSION CODES; IEN=44

Taxonomy: VA-HYPERTENSION SCREEN; IEN=23

Taxonomy: VA-HYSTERECTOMY; IEN=6

Taxonomy: VA-IHD AND ASVD; IEN=315

Taxonomy: VA-IM FLU H1N1 (1 DOSE); IEN=227

Taxonomy: VA-IM FLU HIGH DOSE; IEN=243

Taxonomy: VA-IMAGING FOR AAA (NON-SPECIFIC); IEN=214

Taxonomy: VA-INFLUENZA IMMUNIZATION; IEN=33

Taxonomy: VA-ISCHEMIC HEART 412 DISEASE; IEN=60

Taxonomy: VA-ISCHEMIC HEART DISEASE; IEN=45

Taxonomy: VA-MAMMOGRAM/SCREEN; IEN=16

Taxonomy: VA-MASTECTOMY; IEN=19

Taxonomy: VA-MHV BILATERAL AMPUTEE; IEN=87

Taxonomy: VA-MHV COLONOSCOPY; IEN=85

Taxonomy: VA-MHV DIABETIC RETINAL DISEASE; IEN=88

Taxonomy: VA-MHV IHD AND ATHERSCLEROSIS; IEN=66

Taxonomy: VA-MHV RETINAL EXAMINATION; IEN=89

Taxonomy: VA-MHV SIGMOIDOSCOPY; IEN=86

Taxonomy: VA-NUTRITION; IEN=21

Taxonomy: VA-OBESITY; IEN=20

Taxonomy: VA-PALLI CONS CANCER/HEMA COND; IEN=127

Taxonomy: VA-PALLI CONS CARDIO COND OTHER THAN CA; IEN=125

Taxonomy: VA-PALLI CONS CNS COND OTHER THAN CA; IEN=126

Taxonomy: VA-PALLI CONS DERM CONDITION DX; IEN=122

Taxonomy: VA-PALLI CONS GI OTHER THAN CA; IEN=124

Taxonomy: VA-PALLI CONS INFECTIOUS COND; IEN=120

Taxonomy: VA-PALLI CONS RENAL OTHER THAN CA; IEN=123

Taxonomy: VA-PALLI CONS RHEUM/VASC/THROMB; IEN=121

Taxonomy: VA-PNEUMOC DZ RISK - CHEMOTHERAPY; IEN=118

Taxonomy: VA-PNEUMOC DZ RISK - HIGH; IEN=77

Taxonomy: VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP; IEN=344

Taxonomy: VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED; IEN=119

Taxonomy: VA-PNEUMOCOCCAL VACCINE; IEN=25

Taxonomy: VA-POLYTRAUMA AMPUTATION; IEN=98

Taxonomy: VA-POLYTRAUMA AUDITORY; IEN=97

Taxonomy: VA-POLYTRAUMA BRAIN INJURY; IEN=96

Taxonomy: VA-POLYTRAUMA BURN; IEN=95

Taxonomy: VA-POLYTRAUMA INPT REHAB; IEN=94

Taxonomy: VA-POLYTRAUMA ORTHO; IEN=93

Taxonomy: VA-POLYTRAUMA PTSD; IEN=92

Taxonomy: VA-POLYTRAUMA SCI; IEN=91

Taxonomy: VA-POLYTRAUMA VISION; IEN=90

Taxonomy: VA-POLYTRAUMA WAR INJURY; IEN=84

Taxonomy: VA-PROSTATE CA; IEN=8

Taxonomy: VA-PSA; IEN=26

Taxonomy: VA-PSYCHOTHERAPY CPT CODES; IEN=50

Taxonomy: VA-PTSD DIAGNOSIS; IEN=70

Taxonomy: VA-PTSD DX OUTPT PRIMARY; IEN=224

Taxonomy: VA-PTSD DX OUTPT VISIT; IEN=176

Taxonomy: VA-SAFETY COUNSELING; IEN=35

Taxonomy: VA-SCHIZOPHRENIA; IEN=52

Taxonomy: VA-TB/POSITIVE PPD; IEN=10

Taxonomy: VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCL (TAXONOMIES); IEN=114

Taxonomy: VA-TERMINAL CANCER PATIENTS; IEN=61

Taxonomy: VA-TETANUS DIPHTHERIA; IEN=29

Taxonomy: VA-TOBACCO USE; IEN=22

Taxonomy: VA-WEIGHT AND NUTRITION SCREEN; IEN=36

Taxonomy: VA-WH BILATERAL MASTECTOMY; IEN=62

Taxonomy: VA-WH HYSTERECTOMY W/CERVIX REMOVED; IEN=64

Taxonomy: VA-WH IUD INSERTION (TAXONOMY); IEN=113

Taxonomy: VA-WH IUD REMOVAL (TAXONOMY); IEN=112

Taxonomy: VA-WH PAP SMEAR OBTAINED; IEN=63

Taxonomy: VA-WH PAP SMEAR SCREEN CODES; IEN=65

Taxonomy: VA-WH TUBAL LIGATION CODES (TAXONOMY); IEN=117

Taxonomy: VA-WH TUBAL REANASTOMOSIS (TAXONOMY); IEN=116

Rebuilding Patient Data Source Index.

Taxonomy: 691 PALL INPT 99251; IEN=135; PDS=

Taxonomy: 691 PALL INPT 99252; IEN=134; PDS=

Taxonomy: 691 PALL INPT 99253; IEN=133; PDS=

Taxonomy: 691 PALL INPT 99254; IEN=132; PDS=

Taxonomy: 691 PALL INPT 99255; IEN=131; PDS=

Taxonomy: 691 PALL INPT ENCOUNTER; IEN=136; PDS=

Taxonomy: 691 PALL OUTPT 99241; IEN=142; PDS=

Taxonomy: 691 PALL OUTPT 99242; IEN=141; PDS=

Taxonomy: 691 PALL OUTPT 99243; IEN=140; PDS=

Taxonomy: 691 PALL OUTPT 99244; IEN=139; PDS=

Taxonomy: 691 PALL OUTPT 99245; IEN=137; PDS=

Taxonomy: 691 PALLI CONS CANCER/HEMA COND; IEN=107; PDS=

Taxonomy: 691 PALLI CONS CARDIO COND OTHER THAN CA; IEN=105; PDS=

Taxonomy: 691 PALLI CONS CNS COND OTHER THAN CA; IEN=106; PDS=

Taxonomy: 691 PALLI CONS DERM CONDITION DX; IEN=102; PDS=

Taxonomy: 691 PALLI CONS GI OTHER THAN CA; IEN=104; PDS=

Taxonomy: 691 PALLI CONS INFECTIOUS COND; IEN=100; PDS=

Taxonomy: 691 PALLI CONS RENAL OTHER THAN CA; IEN=103; PDS=

Taxonomy: 691 PALLI CONS RHEUM/VASC/THROMB; IEN=101; PDS=

Taxonomy: ACUTE MI; IEN=442036; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: Advance Directives; IEN=43; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: BILATERIAL MASTECTOMY; IEN=442014; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CA pneumonia; IEN=53; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CA-ESOPH LIVER PANCREAS; IEN=75; PDS=EN,PL,IN

Taxonomy: CANCER OF THE ESOPHAGUS ICD9 150.9; IEN=175; PDS=

Taxonomy: CANCER OF THE LIVER ICD9 155.2; IEN=174; PDS=

Taxonomy: CANCER OF THE PANCREAS ICD9 157.9; IEN=173; PDS=

Taxonomy: CCHT DISEASE INDICATIONS CHF (ICD9); IEN=150; PDS=

Taxonomy: CCHT DISEASE INDICATIONS COPD (ICD9); IEN=149; PDS=

Taxonomy: CCHT DISEASE INDICATIONS DEPRESSION (ICD9); IEN=146; PDS=

Taxonomy: CCHT DISEASE INDICATIONS DIABETES (ICD9); IEN=147; PDS=

Taxonomy: CCHT DISEASE INDICATIONS HTN (ICD9); IEN=148; PDS=

Taxonomy: CCHT DISEASE INDICATIONS PTSD (ICD9); IEN=145; PDS=

Taxonomy: CCHT DISEASE INDICATIONS SUBST ABUSE; IEN=144; PDS=

Taxonomy: CHEY-BIL AMPUTEE; IEN=442020; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CHEY-CERVICAL CANCER SCREEN; IEN=442013; PDS=IN,INDXLS,INPR,EN,ENPR,L

Taxonomy: CHEY-COPD; IEN=442002; PDS=

Taxonomy: CHEY-CVA; IEN=442015; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CHEY-EMP; IEN=442011; PDS=EN,ENPR,PL

Taxonomy: CHEY-HEALTHY LIFESTYLE; IEN=442005; PDS=

Taxonomy: CHEY-HEP A VACCINE; IEN=442012; PDS=

Taxonomy: CHEY-HEP B VACCINE; IEN=442008; PDS=

Taxonomy: CHEY-HGB A1C; IEN=442016; PDS=

Taxonomy: CHEY-HYSTERECTOMY; IEN=442010; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CHEY-MAMMOGRAM SCREENS; IEN=71; PDS=RA

Taxonomy: CHEY-PARAPLEGIC; IEN=442017; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CHEY-SPIROMETRY/PFT; IEN=442003; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CHEY-TB HIGH RISK; IEN=442009; PDS=

Taxonomy: CHEY-TOTAL BLINDNESS; IEN=442019; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CHRONIC OBSTRUCTIVE ASTHMA; IEN=39; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CHRONIC OBSTRUCTIVE BRONCHITIS; IEN=38; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CHY AAA DIAGNOSIS; IEN=69; PDS=ALL

Taxonomy: CHY-HYPOTHYROIDISM; IEN=68; PDS=ALL

Taxonomy: COLITIS/ILEITIS(GJ); IEN=442030; PDS=

Taxonomy: COLON CANCER; IEN=192; PDS=

Taxonomy: COLON POLYPS; IEN=442028; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: COLON REMOVAL; IEN=442001; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: COLON REMOVAL-TOTAL; IEN=442023; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: COLONOSCOPY; IEN=442022; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: COLONOSCOPY POLYPS; IEN=193; PDS=

Taxonomy: COLORECTAL CANCER; IEN=442024; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: CONGESTIVE HEALTH FAILURE; IEN=40; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: COPD; IEN=7; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: COR PULMONALE; IEN=12; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: DEMENTIA CODES - SHERIDAN; IEN=67; PDS=IN,EN,PL

Taxonomy: DEPRESSION CODES; IEN=46; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: DEPRESSION SCREEN; IEN=567007; PDS=

Taxonomy: DIABETES; IEN=674022; PDS=ALL

Taxonomy: DIABETIC EYE EXAM; IEN=442021; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: DIABETIC/RENAL DISEASE; IEN=526016; PDS=

Taxonomy: ECH TOBACCO ADD HX TO PL; IEN=177; PDS=

Taxonomy: EMPHYSEMA; IEN=3; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: ESOPHAGUS CANCER; IEN=54; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: EYE LEGAL BLINDNESS ICD9 369.4; IEN=151; PDS=

Taxonomy: EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23; IEN=152; PDS=

Taxonomy: EYE NEAR NORMAL ICD9 369.9; IEN=153; PDS=

Taxonomy: EYE NORMAL VISION ICD9 367.9; IEN=154; PDS=

Taxonomy: FAMILY HX of Colon CA; IEN=442025; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: FEMALE ENDOMETRIUM/OVARIAN(GJ); IEN=442029; PDS=

Taxonomy: FLU RECIEVED ELSEWHERE; IEN=190; PDS=

Taxonomy: FOBT COMPLETE; IEN=58; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: GP IM PNEUMOC PCV13 PREVNAR; IEN=182; PDS=

Taxonomy: GP IM PNEUMOC PPSV23 PNEUMOVAX; IEN=181; PDS=

Taxonomy: GP TOB CURRENT USER OPTIONAL ACTIONS FY07; IEN=143; PDS=

Taxonomy: HEART FAILURE; IEN=57; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: HEP B ELSEWHERE; IEN=194; PDS=

Taxonomy: HEP C INFECTION; IEN=442007; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: HF LIPID LDL 120-129; IEN=189; PDS=

Taxonomy: HF LIPID LDL 71-99; IEN=180; PDS=

Taxonomy: HF LIPID LDL \>190; IEN=179; PDS=

Taxonomy: HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE; IEN=128; PDS=

Taxonomy: HIGH RISK COLON POLPS; IEN=51; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: HIGH RISK COLONOSCOPY; IEN=48; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: HIGH RISK FLU/PNEUMONIA; IEN=442004; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: HISTORY OF COLON POLYPS; IEN=442035; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: HIV TX; IEN=83; PDS=ALL

Taxonomy: HPV VACCINE CPT CODE; IEN=76; PDS=ALL

Taxonomy: HYPOXIA; IEN=37; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: ICD9 250.01; IEN=163; PDS=

Taxonomy: ICD9 250.02; IEN=162; PDS=

Taxonomy: ICD9 250.03; IEN=166; PDS=

Taxonomy: ICD9 250.50; IEN=155; PDS=

Taxonomy: ICD9 250.51; IEN=156; PDS=

Taxonomy: ICD9 250.52; IEN=157; PDS=

Taxonomy: ICD9 250.53; IEN=158; PDS=

Taxonomy: ICD9 362.01 ; IEN=159; PDS=

Taxonomy: ICD9 362.02 ; IEN=161; PDS=

Taxonomy: ICD9 362.03; IEN=167; PDS=

Taxonomy: ICD9 362.04; IEN=168; PDS=

Taxonomy: ICD9 362.05; IEN=169; PDS=

Taxonomy: ICD9 362.06; IEN=170; PDS=

Taxonomy: ICD9 362.07; IEN=172; PDS=

Taxonomy: ICD9 362.10; IEN=171; PDS=

Taxonomy: ICD9 362.13; IEN=165; PDS=

Taxonomy: ICD9 NURSE ED REFER PWA; IEN=178; PDS=

Taxonomy: IHD PROCEDURES; IEN=108; PDS=

Taxonomy: IM HEP B DONE ELSEWHERE; IEN=129; PDS=

Taxonomy: IM PNEUMO-VAC DONE ELSEWHERE; IEN=191; PDS=

Taxonomy: INTERSTITIAL DISEASE; IEN=13; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: IRRITABLE BOWEL SYNDROME; IEN=442037; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: LESION REMOVAL/COLONOSCOPY; IEN=442034; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: LIVER CANCER; IEN=55; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: LV NON-VESTED PATIENTS; IEN=109; PDS=EN

Taxonomy: MIGRAIN HEADACHES; IEN=14; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: NEW EMPLOYEE CODES; IEN=442018; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: OBESITY 278.00; IEN=73; PDS=EN,PL

Taxonomy: OSTEOPOROSIS; IEN=138; PDS=IN,EN,PL

Taxonomy: OVERWEIGHT; IEN=72; PDS=EN,PL

Taxonomy: PALLI CONS DYSPNEA MILD (E); IEN=186; PDS=

Taxonomy: PALLI CONS DYSPNEA SEVERE (E); IEN=185; PDS=

Taxonomy: PALLI CONS PAIN NONE (E); IEN=188; PDS=

Taxonomy: PALLI CONS PAIN SEVERE (E); IEN=187; PDS=

Taxonomy: PALLI CONS PT PREFER DOC NO (E); IEN=183; PDS=

Taxonomy: PALLI CONS PT PREFER DOC YES (E); IEN=184; PDS=

Taxonomy: PALLIATIVE CONSULT ENCOUNTER DX; IEN=82; PDS=

Taxonomy: PANCREAS CANCER; IEN=56; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: POSITIVE PPD; IEN=442033; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: POST-OP WOUND INFECTION; IEN=59; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: REGIONAL ENTERITIS; IEN=442026; PDS=

Taxonomy: SATP ENROLLMENT; IEN=47; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: SCHIZOPHRENIA; IEN=442032; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: SECONDARY POLYCYTHEMIA; IEN=41; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: SIGMOIDOSCOPY; IEN=442031; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: SLC-MOVE CO-MORBIDITIES; IEN=74; PDS=

Taxonomy: SLEEP APNEA; IEN=42; PDS=IN,INDXLS,INPR,EN,ENPR,PL

Taxonomy: TETANUS DIPHTHERIA CHY; IEN=80; PDS=

Taxonomy: TOBACCO USE; IEN=436024; PDS=

Taxonomy: TOBACCO USE ACTIVE PROBLEM LIST; IEN=110; PDS=PL

Taxonomy: TOBACCO USE DX; IEN=111; PDS=ALL

Taxonomy: ULCERATIVE COLITIS; IEN=442027; PDS=

Taxonomy: URINARY INCONTINENCE; IEN=99; PDS=

Taxonomy: V\*-DG DIAB EYE CODES; IEN=164; PDS=

Taxonomy: V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM; IEN=130; PDS=

Taxonomy: V20-DIABETES; IEN=81; PDS=

Taxonomy: V23 TDAP CPT CODES; IEN=79; PDS=

Taxonomy: V23 TETANUS DIPHTHERIA; IEN=78; PDS=

Taxonomy: VA-ABD AORTIC ANEURYSM; IEN=215; PDS=

Taxonomy: VA-ALCOHOL ABUSE; IEN=17; PDS=

Taxonomy: VA-ALCOHOLISM SCREENING; IEN=34; PDS=

Taxonomy: VA-BREAST TUMOR; IEN=18; PDS=

Taxonomy: VA-CERVICAL CA/ABNORMAL PAP; IEN=5; PDS=

Taxonomy: VA-CERVICAL CANCER SCREEN; IEN=30; PDS=

Taxonomy: VA-CHOLESTEROL; IEN=24; PDS=

Taxonomy: VA-COLORECTAL CA; IEN=4; PDS=

Taxonomy: VA-COLORECTAL CANCER SCREEN; IEN=31; PDS=

Taxonomy: VA-DEPRESSION DIAGNOSIS; IEN=49; PDS=

Taxonomy: VA-DEPRESSION DX OUTPT VISIT; IEN=160; PDS=EN

Taxonomy: VA-DIABETES; IEN=28; PDS=

Taxonomy: VA-DIABETES HEDIS; IEN=317; PDS=

Taxonomy: VA-DIABETES HEDIS PROB LIST; IEN=316; PDS=PL

Taxonomy: VA-ECOE DIAGNOSIS CODES; IEN=115; PDS=

Taxonomy: VA-EXERCISE COUNSELING; IEN=32; PDS=

Taxonomy: VA-FLEXISIGMOIDOSCOPY; IEN=15; PDS=

Taxonomy: VA-FOBT; IEN=27; PDS=

Taxonomy: VA-HEPATITIS C INFECTION; IEN=2; PDS=

Taxonomy: VA-HIGH RISK FOR FLU/PNEUMONIA; IEN=9; PDS=

Taxonomy: VA-HIGH RISK FOR INFLUENZA; IEN=220; PDS=

Taxonomy: VA-HIGH RISK FOR TB; IEN=11; PDS=

Taxonomy: VA-HYPERTENSION; IEN=1; PDS=

Taxonomy: VA-HYPERTENSION CODES; IEN=44; PDS=

Taxonomy: VA-HYPERTENSION SCREEN; IEN=23; PDS=

Taxonomy: VA-HYSTERECTOMY; IEN=6; PDS=

Taxonomy: VA-IHD AND ASVD; IEN=315; PDS=

Taxonomy: VA-IM FLU H1N1 (1 DOSE); IEN=227; PDS=

Taxonomy: VA-IM FLU HIGH DOSE; IEN=243; PDS=

Taxonomy: VA-IMAGING FOR AAA (NON-SPECIFIC); IEN=214; PDS=

Taxonomy: VA-INFLUENZA IMMUNIZATION; IEN=33; PDS=

Taxonomy: VA-ISCHEMIC HEART 412 DISEASE; IEN=60; PDS=INDXLS,EN,PL

Taxonomy: VA-ISCHEMIC HEART DISEASE; IEN=45; PDS=INDXLS,EN,PL

Taxonomy: VA-MAMMOGRAM/SCREEN; IEN=16; PDS=

Taxonomy: VA-MASTECTOMY; IEN=19; PDS=

Taxonomy: VA-MHV BILATERAL AMPUTEE; IEN=87; PDS=

Taxonomy: VA-MHV COLONOSCOPY; IEN=85; PDS=

Taxonomy: VA-MHV DIABETIC RETINAL DISEASE; IEN=88; PDS=

Taxonomy: VA-MHV IHD AND ATHERSCLEROSIS; IEN=66; PDS=

Taxonomy: VA-MHV RETINAL EXAMINATION; IEN=89; PDS=

Taxonomy: VA-MHV SIGMOIDOSCOPY; IEN=86; PDS=

Taxonomy: VA-NUTRITION; IEN=21; PDS=

Taxonomy: VA-OBESITY; IEN=20; PDS=

Taxonomy: VA-PALLI CONS CANCER/HEMA COND; IEN=127; PDS=

Taxonomy: VA-PALLI CONS CARDIO COND OTHER THAN CA; IEN=125; PDS=

Taxonomy: VA-PALLI CONS CNS COND OTHER THAN CA; IEN=126; PDS=

Taxonomy: VA-PALLI CONS DERM CONDITION DX; IEN=122; PDS=

Taxonomy: VA-PALLI CONS GI OTHER THAN CA; IEN=124; PDS=

Taxonomy: VA-PALLI CONS INFECTIOUS COND; IEN=120; PDS=

Taxonomy: VA-PALLI CONS RENAL OTHER THAN CA; IEN=123; PDS=

Taxonomy: VA-PALLI CONS RHEUM/VASC/THROMB; IEN=121; PDS=

Taxonomy: VA-PNEUMOC DZ RISK - CHEMOTHERAPY; IEN=118; PDS=

Taxonomy: VA-PNEUMOC DZ RISK - HIGH; IEN=77; PDS=

Taxonomy: VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP; IEN=344; PDS=

Taxonomy: VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED; IEN=119; PDS=

Taxonomy: VA-PNEUMOCOCCAL VACCINE; IEN=25; PDS=

Taxonomy: VA-POLYTRAUMA AMPUTATION; IEN=98; PDS=

Taxonomy: VA-POLYTRAUMA AUDITORY; IEN=97; PDS=

Taxonomy: VA-POLYTRAUMA BRAIN INJURY; IEN=96; PDS=

Taxonomy: VA-POLYTRAUMA BURN; IEN=95; PDS=

Taxonomy: VA-POLYTRAUMA INPT REHAB; IEN=94; PDS=INDXLS

Taxonomy: VA-POLYTRAUMA ORTHO; IEN=93; PDS=

Taxonomy: VA-POLYTRAUMA PTSD; IEN=92; PDS=

Taxonomy: VA-POLYTRAUMA SCI; IEN=91; PDS=

Taxonomy: VA-POLYTRAUMA VISION; IEN=90; PDS=

Taxonomy: VA-POLYTRAUMA WAR INJURY; IEN=84; PDS=

Taxonomy: VA-PROSTATE CA; IEN=8; PDS=

Taxonomy: VA-PSA; IEN=26; PDS=

Taxonomy: VA-PSYCHOTHERAPY CPT CODES; IEN=50; PDS=

Taxonomy: VA-PTSD DIAGNOSIS; IEN=70; PDS=

Taxonomy: VA-PTSD DX OUTPT PRIMARY; IEN=224; PDS=ENPD

Taxonomy: VA-PTSD DX OUTPT VISIT; IEN=176; PDS=EN

Taxonomy: VA-SAFETY COUNSELING; IEN=35; PDS=

Taxonomy: VA-SCHIZOPHRENIA; IEN=52; PDS=

Taxonomy: VA-TB/POSITIVE PPD; IEN=10; PDS=

Taxonomy: VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCL (TAXONOMIES); IEN=114; P=

Taxonomy: VA-TERMINAL CANCER PATIENTS; IEN=61; PDS=

Taxonomy: VA-TETANUS DIPHTHERIA; IEN=29; PDS=

Taxonomy: VA-TOBACCO USE; IEN=22; PDS=

Taxonomy: VA-WEIGHT AND NUTRITION SCREEN; IEN=36; PDS=

Taxonomy: VA-WH BILATERAL MASTECTOMY; IEN=62; PDS=

Taxonomy: VA-WH HYSTERECTOMY W/CERVIX REMOVED; IEN=64; PDS=

Taxonomy: VA-WH IUD INSERTION (TAXONOMY); IEN=113; PDS=

Taxonomy: VA-WH IUD REMOVAL (TAXONOMY); IEN=112; PDS=

Taxonomy: VA-WH PAP SMEAR OBTAINED; IEN=63; PDS=

Taxonomy: VA-WH PAP SMEAR SCREEN CODES; IEN=65; PDS=

Taxonomy: VA-WH TUBAL LIGATION CODES (TAXONOMY); IEN=117; PDS=

Taxonomy: VA-WH TUBAL REANASTOMOSIS (TAXONOMY); IEN=116; PDS=

Check the integrity of all reminder taxonomies.

Checking 691 PALL INPT 99251 (IEN=135)

No problems were found.

Checking 691 PALL INPT 99252 (IEN=134)

No problems were found.

Checking 691 PALL INPT 99253 (IEN=133)

No problems were found.

Checking 691 PALL INPT 99254 (IEN=132)

No problems were found.

Checking 691 PALL INPT 99255 (IEN=131)

No problems were found.

Checking 691 PALL INPT ENCOUNTER (IEN=136)

No problems were found.

Checking 691 PALL OUTPT 99241 (IEN=142)

No problems were found.

Checking 691 PALL OUTPT 99242 (IEN=141)

No problems were found.

Checking 691 PALL OUTPT 99243 (IEN=140)

No problems were found.

Checking 691 PALL OUTPT 99244 (IEN=139)

No problems were found.

Checking 691 PALL OUTPT 99245 (IEN=137)

No problems were found.

Checking 691 PALLI CONS CANCER/HEMA COND (IEN=107)

No problems were found.

Checking 691 PALLI CONS CARDIO COND OTHER THAN CA (IEN=105)

No problems were found.

Checking 691 PALLI CONS CNS COND OTHER THAN CA (IEN=106)

No problems were found.

Checking 691 PALLI CONS DERM CONDITION DX (IEN=102)

No problems were found.

Checking 691 PALLI CONS GI OTHER THAN CA (IEN=104)

No problems were found.

Checking 691 PALLI CONS INFECTIOUS COND (IEN=100)

No problems were found.

Checking 691 PALLI CONS RENAL OTHER THAN CA (IEN=103)

No problems were found.

Checking 691 PALLI CONS RHEUM/VASC/THROMB (IEN=101)

No problems were found.

Checking ACUTE MI (IEN=442036)

No problems were found.

Checking Advance Directives (IEN=43)

No problems were found.

Checking BILATERIAL MASTECTOMY (IEN=442014)

No problems were found.

Checking CA pneumonia (IEN=53)

No problems were found.

Checking CA-ESOPH LIVER PANCREAS (IEN=75)

No problems were found.

Checking CANCER OF THE ESOPHAGUS ICD9 150.9 (IEN=175)

No problems were found.

Checking CANCER OF THE LIVER ICD9 155.2 (IEN=174)

No problems were found.

Checking CANCER OF THE PANCREAS ICD9 157.9 (IEN=173)

No problems were found.

Checking CCHT DISEASE INDICATIONS CHF (ICD9) (IEN=150)

No problems were found.

Checking CCHT DISEASE INDICATIONS COPD (ICD9) (IEN=149)

No problems were found.

Checking CCHT DISEASE INDICATIONS DEPRESSION (ICD9) (IEN=146)

No problems were found.

Checking CCHT DISEASE INDICATIONS DIABETES (ICD9) (IEN=147)

No problems were found.

Checking CCHT DISEASE INDICATIONS HTN (ICD9) (IEN=148)

No problems were found.

Checking CCHT DISEASE INDICATIONS PTSD (ICD9) (IEN=145)

No problems were found.

Checking CCHT DISEASE INDICATIONS SUBST ABUSE (IEN=144)

No problems were found.

Checking CHEY-BIL AMPUTEE (IEN=442020)

No problems were found.

Checking CHEY-CERVICAL CANCER SCREEN (IEN=442013)

No problems were found.

Checking CHEY-COPD (IEN=442002)

No problems were found.

Checking CHEY-CVA (IEN=442015)

No problems were found.

Checking CHEY-EMP (IEN=442011)

No problems were found.

Checking CHEY-HEALTHY LIFESTYLE (IEN=442005)

No problems were found.

Checking CHEY-HEP A VACCINE (IEN=442012)

No problems were found.

Checking CHEY-HEP B VACCINE (IEN=442008)

No problems were found.

Checking CHEY-HGB A1C (IEN=442016)

No problems were found.

Checking CHEY-HYSTERECTOMY (IEN=442010)

No problems were found.

Checking CHEY-MAMMOGRAM SCREENS (IEN=71)

No problems were found.

Checking CHEY-PARAPLEGIC (IEN=442017)

No problems were found.

Checking CHEY-SPIROMETRY/PFT (IEN=442003)

No problems were found.

Checking CHEY-TB HIGH RISK (IEN=442009)

No problems were found.

Checking CHEY-TOTAL BLINDNESS (IEN=442019)

No problems were found.

Checking CHRONIC OBSTRUCTIVE ASTHMA (IEN=39)

No problems were found.

Checking CHRONIC OBSTRUCTIVE BRONCHITIS (IEN=38)

No problems were found.

Checking CHY AAA DIAGNOSIS (IEN=69)

No problems were found.

Checking CHY-HYPOTHYROIDISM (IEN=68)

No problems were found.

Checking COLITIS/ILEITIS(GJ) (IEN=442030)

No problems were found.

Checking COLON CANCER (IEN=192)

No problems were found.

Checking COLON POLYPS (IEN=442028)

No problems were found.

Checking COLON REMOVAL (IEN=442001)

No problems were found.

Checking COLON REMOVAL-TOTAL (IEN=442023)

No problems were found.

Checking COLONOSCOPY (IEN=442022)

No problems were found.

Checking COLONOSCOPY POLYPS (IEN=193)

No problems were found.

Checking COLORECTAL CANCER (IEN=442024)

No problems were found.

Checking CONGESTIVE HEALTH FAILURE (IEN=40)

No problems were found.

Checking COPD (IEN=7)

No problems were found.

Checking COR PULMONALE (IEN=12)

No problems were found.

Checking DEMENTIA CODES - SHERIDAN (IEN=67)

No problems were found.

Checking DEPRESSION CODES (IEN=46)

No problems were found.

Checking DEPRESSION SCREEN (IEN=567007)

No problems were found.

Checking DIABETES (IEN=674022)

No problems were found.

Checking DIABETIC EYE EXAM (IEN=442021)

No problems were found.

Checking DIABETIC/RENAL DISEASE (IEN=526016)

No problems were found.

Checking ECH TOBACCO ADD HX TO PL (IEN=177)

No problems were found.

Checking EMPHYSEMA (IEN=3)

No problems were found.

Checking ESOPHAGUS CANCER (IEN=54)

No problems were found.

Checking EYE LEGAL BLINDNESS ICD9 369.4 (IEN=151)

No problems were found.

Checking EYE MODERATE VISUAL IMPAIRMENT ICD9 369.23 (IEN=152)

No problems were found.

Checking EYE NEAR NORMAL ICD9 369.9 (IEN=153)

No problems were found.

Checking EYE NORMAL VISION ICD9 367.9 (IEN=154)

No problems were found.

Checking FAMILY HX of Colon CA (IEN=442025)

No problems were found.

Checking FEMALE ENDOMETRIUM/OVARIAN(GJ) (IEN=442029)

No problems were found.

Checking FLU RECIEVED ELSEWHERE (IEN=190)

No problems were found.

Checking FOBT COMPLETE (IEN=58)

No problems were found.

Checking GP IM PNEUMOC PCV13 PREVNAR (IEN=182)

No problems were found.

Checking GP IM PNEUMOC PPSV23 PNEUMOVAX (IEN=181)

No problems were found.

Checking GP TOB CURRENT USER OPTIONAL ACTIONS FY07 (IEN=143)

No problems were found.

Checking HEART FAILURE (IEN=57)

No problems were found.

Checking HEP B ELSEWHERE (IEN=194)

No problems were found.

Checking HEP C INFECTION (IEN=442007)

No problems were found.

Checking HF LIPID LDL 120-129 (IEN=189)

No problems were found.

Checking HF LIPID LDL 71-99 (IEN=180)

No problems were found.

Checking HF LIPID LDL \>190 (IEN=179)

No problems were found.

Checking HF TD - RECEIVED ELSEWHERE DONE ELSEWHERE (IEN=128)

No problems were found.

Checking HIGH RISK COLON POLPS (IEN=51)

No problems were found.

Checking HIGH RISK COLONOSCOPY (IEN=48)

No problems were found.

Checking HIGH RISK FLU/PNEUMONIA (IEN=442004)

No problems were found.

Checking HISTORY OF COLON POLYPS (IEN=442035)

No problems were found.

Checking HIV TX (IEN=83)

No problems were found.

Checking HPV VACCINE CPT CODE (IEN=76)

No problems were found.

Checking HYPOXIA (IEN=37)

No problems were found.

Checking ICD9 250.01 (IEN=163)

No problems were found.

Checking ICD9 250.02 (IEN=162)

No problems were found.

Checking ICD9 250.03 (IEN=166)

No problems were found.

Checking ICD9 250.50 (IEN=155)

No problems were found.

Checking ICD9 250.51 (IEN=156)

No problems were found.

Checking ICD9 250.52 (IEN=157)

No problems were found.

Checking ICD9 250.53 (IEN=158)

No problems were found.

Checking ICD9 362.01 (IEN=159)

No problems were found.

Checking ICD9 362.02 (IEN=161)

No problems were found.

Checking ICD9 362.03 (IEN=167)

No problems were found.

Checking ICD9 362.04 (IEN=168)

No problems were found.

Checking ICD9 362.05 (IEN=169)

No problems were found.

Checking ICD9 362.06 (IEN=170)

No problems were found.

Checking ICD9 362.07 (IEN=172)

No problems were found.

Checking ICD9 362.10 (IEN=171)

No problems were found.

Checking ICD9 362.13 (IEN=165)

No problems were found.

Checking ICD9 NURSE ED REFER PWA (IEN=178)

No problems were found.

Checking IHD PROCEDURES (IEN=108)

No problems were found.

Checking IM HEP B DONE ELSEWHERE (IEN=129)

No problems were found.

Checking IM PNEUMO-VAC DONE ELSEWHERE (IEN=191)

No problems were found.

Checking INTERSTITIAL DISEASE (IEN=13)

No problems were found.

Checking IRRITABLE BOWEL SYNDROME (IEN=442037)

No problems were found.

Checking LESION REMOVAL/COLONOSCOPY (IEN=442034)

No problems were found.

Checking LIVER CANCER (IEN=55)

No problems were found.

Checking LV NON-VESTED PATIENTS (IEN=109)

No problems were found.

Checking MIGRAIN HEADACHES (IEN=14)

No problems were found.

Checking NEW EMPLOYEE CODES (IEN=442018)

No problems were found.

Checking OBESITY 278.00 (IEN=73)

No problems were found.

Checking OSTEOPOROSIS (IEN=138)

No problems were found.

Checking OVERWEIGHT (IEN=72)

No problems were found.

Checking PALLI CONS DYSPNEA MILD (E) (IEN=186)

No problems were found.

Checking PALLI CONS DYSPNEA SEVERE (E) (IEN=185)

No problems were found.

Checking PALLI CONS PAIN NONE (E) (IEN=188)

No problems were found.

Checking PALLI CONS PAIN SEVERE (E) (IEN=187)

No problems were found.

Checking PALLI CONS PT PREFER DOC NO (E) (IEN=183)

No problems were found.

Checking PALLI CONS PT PREFER DOC YES (E) (IEN=184)

No problems were found.

Checking PALLIATIVE CONSULT ENCOUNTER DX (IEN=82)

No problems were found.

Checking PANCREAS CANCER (IEN=56)

No problems were found.

Checking POSITIVE PPD (IEN=442033)

No problems were found.

Checking POST-OP WOUND INFECTION (IEN=59)

No problems were found.

Checking REGIONAL ENTERITIS (IEN=442026)

No problems were found.

Checking SATP ENROLLMENT (IEN=47)

No problems were found.

Checking SCHIZOPHRENIA (IEN=442032)

No problems were found.

Checking SECONDARY POLYCYTHEMIA (IEN=41)

No problems were found.

Checking SIGMOIDOSCOPY (IEN=442031)

No problems were found.

Checking SLC-MOVE CO-MORBIDITIES (IEN=74)

No problems were found.

Checking SLEEP APNEA (IEN=42)

No problems were found.

Checking TETANUS DIPHTHERIA CHY (IEN=80)

No problems were found.

Checking TOBACCO USE (IEN=436024)

No problems were found.

Checking TOBACCO USE ACTIVE PROBLEM LIST (IEN=110)

No problems were found.

Checking TOBACCO USE DX (IEN=111)

No problems were found.

Checking ULCERATIVE COLITIS (IEN=442027)

No problems were found.

Checking URINARY INCONTINENCE (IEN=99)

No problems were found.

Checking V\*-DG DIAB EYE CODES (IEN=164)

No problems were found.

Checking V\*-HF DIAB TELERET DISPO COMPREHENSIVE EXAM (IEN=130)

No problems were found.

Checking V20-DIABETES (IEN=81)

No problems were found.

Checking V23 TDAP CPT CODES (IEN=79)

No problems were found.

Checking V23 TETANUS DIPHTHERIA (IEN=78)

No problems were found.

Checking VA-ABD AORTIC ANEURYSM (IEN=215)

No problems were found.

Checking VA-ALCOHOL ABUSE (IEN=17)

No problems were found.

Checking VA-ALCOHOLISM SCREENING (IEN=34)

No problems were found.

Checking VA-BREAST TUMOR (IEN=18)

No problems were found.

Checking VA-CERVICAL CA/ABNORMAL PAP (IEN=5)

No problems were found.

Checking VA-CERVICAL CANCER SCREEN (IEN=30)

No problems were found.

Checking VA-CHOLESTEROL (IEN=24)

No problems were found.

Checking VA-COLORECTAL CA (IEN=4)

No problems were found.

Checking VA-COLORECTAL CANCER SCREEN (IEN=31)

No problems were found.

Checking VA-DEPRESSION DIAGNOSIS (IEN=49)

No problems were found.

Checking VA-DEPRESSION DX OUTPT VISIT (IEN=160)

No problems were found.

Checking VA-DIABETES (IEN=28)

No problems were found.

Checking VA-DIABETES HEDIS (IEN=317)

No problems were found.

Checking VA-DIABETES HEDIS PROB LIST (IEN=316)

No problems were found.

Checking VA-ECOE DIAGNOSIS CODES (IEN=115)

No problems were found.

Checking VA-EXERCISE COUNSELING (IEN=32)

No problems were found.

Checking VA-FLEXISIGMOIDOSCOPY (IEN=15)

No problems were found.

Checking VA-FOBT (IEN=27)

No problems were found.

Checking VA-HEPATITIS C INFECTION (IEN=2)

No problems were found.

Checking VA-HIGH RISK FOR FLU/PNEUMONIA (IEN=9)

No problems were found.

Checking VA-HIGH RISK FOR INFLUENZA (IEN=220)

No problems were found.

Checking VA-HIGH RISK FOR TB (IEN=11)

No problems were found.

Checking VA-HYPERTENSION (IEN=1)

No problems were found.

Checking VA-HYPERTENSION CODES (IEN=44)

No problems were found.

Checking VA-HYPERTENSION SCREEN (IEN=23)

No problems were found.

Checking VA-HYSTERECTOMY (IEN=6)

No problems were found.

Checking VA-IHD AND ASVD (IEN=315)

No problems were found.

Checking VA-IM FLU H1N1 (1 DOSE) (IEN=227)

No problems were found.

Checking VA-IM FLU HIGH DOSE (IEN=243)

No problems were found.

Checking VA-IMAGING FOR AAA (NON-SPECIFIC) (IEN=214)

No problems were found.

Checking VA-INFLUENZA IMMUNIZATION (IEN=33)

No problems were found.

Checking VA-ISCHEMIC HEART 412 DISEASE (IEN=60)

No problems were found.

Checking VA-ISCHEMIC HEART DISEASE (IEN=45)

No problems were found.

Checking VA-MAMMOGRAM/SCREEN (IEN=16)

No problems were found.

Checking VA-MASTECTOMY (IEN=19)

No problems were found.

Checking VA-MHV BILATERAL AMPUTEE (IEN=87)

No problems were found.

Checking VA-MHV COLONOSCOPY (IEN=85)

No problems were found.

Checking VA-MHV DIABETIC RETINAL DISEASE (IEN=88)

No problems were found.

Checking VA-MHV IHD AND ATHERSCLEROSIS (IEN=66)

No problems were found.

Checking VA-MHV RETINAL EXAMINATION (IEN=89)

No problems were found.

Checking VA-MHV SIGMOIDOSCOPY (IEN=86)

No problems were found.

Checking VA-NUTRITION (IEN=21)

No problems were found.

Checking VA-OBESITY (IEN=20)

No problems were found.

Checking VA-PALLI CONS CANCER/HEMA COND (IEN=127)

No problems were found.

Checking VA-PALLI CONS CARDIO COND OTHER THAN CA (IEN=125)

No problems were found.

Checking VA-PALLI CONS CNS COND OTHER THAN CA (IEN=126)

No problems were found.

Checking VA-PALLI CONS DERM CONDITION DX (IEN=122)

No problems were found.

Checking VA-PALLI CONS GI OTHER THAN CA (IEN=124)

No problems were found.

Checking VA-PALLI CONS INFECTIOUS COND (IEN=120)

No problems were found.

Checking VA-PALLI CONS RENAL OTHER THAN CA (IEN=123)

No problems were found.

Checking VA-PALLI CONS RHEUM/VASC/THROMB (IEN=121)

No problems were found.

Checking VA-PNEUMOC DZ RISK - CHEMOTHERAPY (IEN=118)

No problems were found.

Checking VA-PNEUMOC DZ RISK - HIGH (IEN=77)

No problems were found.

Checking VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP (IEN=344)

No problems were found.

Checking VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED (IEN=119)

No problems were found.

Checking VA-PNEUMOCOCCAL VACCINE (IEN=25)

No problems were found.

Checking VA-POLYTRAUMA AMPUTATION (IEN=98)

No problems were found.

Checking VA-POLYTRAUMA AUDITORY (IEN=97)

No problems were found.

Checking VA-POLYTRAUMA BRAIN INJURY (IEN=96)

No problems were found.

Checking VA-POLYTRAUMA BURN (IEN=95)

No problems were found.

Checking VA-POLYTRAUMA INPT REHAB (IEN=94)

No problems were found.

Checking VA-POLYTRAUMA ORTHO (IEN=93)

No problems were found.

Checking VA-POLYTRAUMA PTSD (IEN=92)

No problems were found.

Checking VA-POLYTRAUMA SCI (IEN=91)

No problems were found.

Checking VA-POLYTRAUMA VISION (IEN=90)

No problems were found.

Checking VA-POLYTRAUMA WAR INJURY (IEN=84)

No problems were found.

Checking VA-PROSTATE CA (IEN=8)

No problems were found.

Checking VA-PSA (IEN=26)

No problems were found.

Checking VA-PSYCHOTHERAPY CPT CODES (IEN=50)

No problems were found.

Checking VA-PTSD DIAGNOSIS (IEN=70)

No problems were found.

Checking VA-PTSD DX OUTPT PRIMARY (IEN=224)

No problems were found.

Checking VA-PTSD DX OUTPT VISIT (IEN=176)

No problems were found.

Checking VA-SAFETY COUNSELING (IEN=35)

No problems were found.

Checking VA-SCHIZOPHRENIA (IEN=52)

No problems were found.

Checking VA-TB/POSITIVE PPD (IEN=10)

No problems were found.

Checking VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCL (TAXONOMIES) (IEN=114)

No problems were found.

Checking VA-TERMINAL CANCER PATIENTS (IEN=61)

No problems were found.

Checking VA-TETANUS DIPHTHERIA (IEN=29)

No problems were found.

Checking VA-TOBACCO USE (IEN=22)

No problems were found.

Checking VA-WEIGHT AND NUTRITION SCREEN (IEN=36)

No problems were found.

Checking VA-WH BILATERAL MASTECTOMY (IEN=62)

No problems were found.

Checking VA-WH HYSTERECTOMY W/CERVIX REMOVED (IEN=64)

No problems were found.

Checking VA-WH IUD INSERTION (TAXONOMY) (IEN=113)

No problems were found.

Checking VA-WH IUD REMOVAL (TAXONOMY) (IEN=112)

No problems were found.

Checking VA-WH PAP SMEAR OBTAINED (IEN=63)

No problems were found.

Checking VA-WH PAP SMEAR SCREEN CODES (IEN=65)

No problems were found.

Checking VA-WH TUBAL LIGATION CODES (TAXONOMY) (IEN=117)

No problems were found.

Checking VA-WH TUBAL REANASTOMOSIS (TAXONOMY) (IEN=116)

No problems were found.

ENABLE options.

ENABLE protocols.

Enabling reminder evaluation.

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*26 Installed.

May 09, 2014@10:01:53

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

CLINICAL REMINDERS ICD-10 UPDATE 1.0 Installed.

May 09, 2014@10:01:53

No link to PACKAGE file

Install Completed

# Appendix B: Post-Install Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Checksums: DG Routines

DEV5A4:DEMCUR\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: DG\*5.3\*862 REGISTRATION

DG53862I value = 108880036

DGPTDDCR value = 88922399

done

Installation Checksums: GMPL Routines

DEV5A4:DEMCUR\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: GMPL\*2.0\*44 PROBLEM LIST

GMPLP44I value = 86662145

GMPLPXRM value = 41114026

done

Installation Checksums: PXRM Routines

DEV5A4:DEMCUR\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: PXRM\*2.0\*26 CLINICAL REMINDERS

PXRM value = 54398070

PXRMART value = 5789982

PXRMBXTL value = 28912703

PXRMCDEF value = 2371303

PXRMCF value = 63448106

PXRMCOPY value = 21259633

PXRMCPLS value = 12687369

PXRMCSPE value = 1560002

PXRMCSTX value = 2261498

PXRMDATE value = 70140007

PXRMDEDI value = 25523952

PXRMDEDT value = 86565471

PXRMDEV value = 78755601

PXRMDGPT value = 33156979

PXRMDIEV value = 68563179

PXRMDLG1 value = 7385364

PXRMDLG4 value = 91752060

PXRMDLG6 value = 20894000

PXRMDLL value = 137187250

PXRMDLLA value = 84693327

PXRMDLLB value = 33584430

PXRMDLRP value = 96040502

PXRMDTAX value = 200174205

PXRMDUTL value = 11502615

PXRMEFED value = 10725830

PXRMEGED value = 10459294

PXRMENOD value = 24879383

PXRMEPED value = 10154511

PXRMETH value = 101071654

PXRMETX value = 62476117

PXRMETXR value = 76497570

PXRMEXCS value = 15773333

PXRMEXFI value = 55982418

PXRMEXHF value = 49479695

PXRMEXIC value = 84313734

PXRMEXID value = 66152122

PXRMEXIH value = 48820476

PXRMEXIU value = 68841657

PXRMEXLB value = 63445674

PXRMEXLC value = 13059952

PXRMEXLM value = 52621060

PXRMEXLR value = 9879769

PXRMEXMH value = 10764722

PXRMEXMM value = 32677866

PXRMEXPD value = 200143562

PXRMEXPS value = 188507722

PXRMEXU0 value = 23209797

PXRMEXU1 value = 36996811

PXRMEXU2 value = 74659923

PXRMEXU4 value = 182800125

PXRMEXWB value = 1609378

PXRMFF value = 72420410

PXRMFFDB value = 67684724

PXRMFFH value = 11369552

PXRMFRPT value = 184393482

PXRMGEDT value = 45920622

PXRMGEN value = 4344668

PXRMICHK value = 191422911

PXRMINDC value = 76451646

PXRMINDD value = 76803119

PXRMINDL value = 24651910

PXRMINDX value = 36378752

PXRMINTR value = 45347072

PXRMLCR value = 39948429

PXRMLDR value = 15240412

PXRMLEX value = 35438125

PXRMLEXL value = 240921269

PXRMLIST value = 9607187

PXRMLOG value = 65785719

PXRMLPOE value = 15191347

PXRMMSER value = 106758017

PXRMORCH value = 34974913

PXRMOUTC value = 38949930

PXRMOUTU value = 17168118

PXRMP26D value = 226626413

PXRMP26E value = 1814747

PXRMP26I value = 28610158

PXRMP26X value = 39898924

PXRMPARS value = 3546283

PXRMPDS value = 38727338

PXRMPROB value = 47060633

PXRMPTTX value = 39642269

PXRMRCPT value = 24259553

PXRMRDI value = 37867827

PXRMREDF value = 84708461

PXRMREDT value = 70699612

PXRMRUL1 value = 49947013

PXRMSCR value = 126404

PXRMSEL value = 75136649

PXRMSINQ value = 22958302

PXRMSTA1 value = 67419179

PXRMSTA2 value = 22367612

PXRMSTAC value = 10577788

PXRMSTS value = 178092687

PXRMSXRM value = 51532846

PXRMTAX value = 60136875

PXRMTAXD value = 68009180

PXRMTAXL value = 59845028

PXRMTDLG value = 19639441

PXRMTERM value = 55315672

PXRMTIU value = 7669051

PXRMTMED value = 13031751

PXRMTXCE value = 21765274

PXRMTXCR value = 74745189

PXRMTXCS value = 3010053

PXRMTXDL value = 1299916

PXRMTXIC value = 8164040

PXRMTXIH value = 25527600

PXRMTXIM value = 193866629

PXRMTXIN value = 68427938

PXRMTXSM value = 41443129

PXRMUIDR value = 9563816

PXRMUTIL value = 128848927

PXRMVCPT value = 51805382

PXRMVPOV value = 51874901

PXRMXEVL value = 1989772

PXRMXSE1 value = 30616308

PXRMXT value = 32837496

PXRMXTA value = 53931120

PXRMXTB value = 7902302

done

<span id="appendixC" class="anchor"></span>Appendix C: Finding Usage Report ExamplesFinding Usage Report Example – Diagnosis:

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: RP Reminder Reports

> Select Reminder Reports \<TEST ACCOUNT\> Option: FUR Finding Usage Report

> Clinical Reminders Usage Report

> Select from the following reminder findings (\* signifies standardized):

> 1 - DRUG

> 2 - EDUCATION TOPICS

> 3 - EXAM

> 4 - HEALTH FACTOR

> 5 - ICD9 DIAGNOSIS

> 6 - IMMUNIZATION \*

> 7 - LABORATORY TEST

> 8 - MENTAL HEALTH

> 9 - MH TESTS AND SURVEYS

> 10 - ORDER DIALOG

> 11 - ORDERABLE ITEM

> 12 - PROCEDURE

> 13 - RADIOLOGY PROCEDURE

> 14 - REMINDER COMPUTED FINDING

> 15 - REMINDER DEFINITION

> 16 - REMINDER LOCATION LIST

> 17 - REMINDER TAXONOMY

> 18 - REMINDER TERM

> 19 - SKIN TEST \*

> 20 - TAXONOMY

> Enter your list for the report: (1-25): 5

> Search for all or selected ICD9 DIAGNOSIS?

> Select one of the following:

> 1 ALL

> 2 SELECTED

> Enter response: SELECTED// 1 ALL

> SORT DONE

> Browse or Print? B// Print

> DEVICE: HOME// ;;999 HOME

> Clinical Reminders finding usage report.

> The following ICD DIAGNOSIS(s) are used as follows:

> =======================================================

> ICD DIAGNOSIS - 100.9 (IEN=3)

> Is used in the following Reminder Dialog(s):

> Dialog element POV DIAG 1 (IEN=660113), used in the

> Finding Item field

> =======================================================

> ICD DIAGNOSIS - 103.3 (IEN=15)

> ---------------------------------

> Is used in the following Reminder Dialog(s):

> Dialog element CODE SET ICD9 FIND (IEN=336), used in the

> Finding Item field

> =======================================================

> ICD DIAGNOSIS - 174.1 (IEN=335)

> ---------------------------------

> Is used in the following Reminder Dialog(s):

> Dialog element POV 174.1 DONE (IEN=441), used in the

> Finding Item field

> Dialog element POV 174.1 DONE ELSEWHERE (IEN=581), used in the

> Finding Item field

> Press ENTER to continue:

> Deliver the report as a MailMan message? N// Yes

> Finding Usage Report Example –Procedure

> Select Reminder Reports \<TEST ACCOUNT\> Option: FUR Finding Usage Report

> Clinical Reminders Usage Report

> Select from the following reminder findings (\* signifies standardized):

> 1 - DRUG

> 2 - EDUCATION TOPICS

> 3 - EXAM

> 4 - HEALTH FACTOR

> 5 - ICD9 DIAGNOSIS

> 6 - IMMUNIZATION \*

> 7 - LABORATORY TEST

> 8 - MENTAL HEALTH

> 9 - MH TESTS AND SURVEYS

> 10 - ORDER DIALOG

> 11 - ORDERABLE ITEM

> 12 - PROCEDURE

> 13 - RADIOLOGY PROCEDURE

> 14 - REMINDER COMPUTED FINDING

> 15 - REMINDER DEFINITION

> 16 - REMINDER LOCATION LIST

> 17 - REMINDER TAXONOMY

> 18 - REMINDER TERM

> 19 - SKIN TEST \*

> 20 - TAXONOMY

> 21 - VA DRUG CLASS \*

> 22 - VA GENERIC \*

> 23 - VITAL MEASUREMENT \*

> 24 - VITAL TYPE \*

> 25 - WH NOTIFICATION PURPOSE

> Enter your list for the report: (1-25): 12

> Search for all or selected PROCEDURES?

> Select one of the following:

> 1 ALL

> 2 SELECTED

> Enter response: SELECTED// 1 ALL

> SORT DONE

> Browse or Print? B// Print

> DEVICE: HOME// ;;999 HOME

> Clinical Reminders finding usage report.

> The following CPT(s) are used as follows:

> =======================================================

> CPT - 13300 (IEN=13300)

> Is used in the following Reminder Dialog(s):

> Dialog element OI/IMM PNEUMOCOCCAL VACCINE INJ (Disable)

> (IEN=660057), used in the

> Additional Finding field

> =======================================================

> CPT - 23350 (IEN=23350)

> ---------------------------------

> Is used in the following Reminder Dialog(s):

> Dialog element XXX MULTIPLE CODE (IEN=3904), used in the

> Additional Finding field

> Dialog element XXX MULTIPLE CODE ADD ONLY (IEN=3905), used in the

> Additional Finding field

> Dialog element XXX MULTIPLE CODE ADD ONLY 1 (IEN=3906), used in the

> Additional Finding field

> =======================================================

> CPT - 44388 (IEN=44388)

> ---------------------------------

> Is used in the following Reminder Dialog(s):

> Dialog group HF BINGE DRINKING OTHER (Disable) (IEN=660015), used

> in the

> Additional Finding field

> =======================================================

> CPT - 50010 (IEN=50010)

> ---------------------------------

> Is used in the following Reminder Dialog(s):

> Dialog element CODE SET CPT FIND (IEN=335), used in the

> Additional Finding field

> .

> .

> .

> Etc.

> Press ENTER to continue:

> Deliver the report as a MailMan message? N// O

# Appendix D: Check All Active Reminder Dialogs for Invalid Items Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Reminder Dialog Management \<TEST ACCOUNT\> Option: DR Dialog Reports

> OR Reminder Dialog Elements Orphan Report

> ER Empty Reminder Dialog Report

> ALL Check all active reminder dialog for invalid items

> CH Check Reminder Dialog for invalid items

> Select Dialog Reports Option: ALL Check all active reminder dialog for invalid items

> COPY OF AGE TEST contains the following errors.

> The dialog group HF BINGE DRINKING OTHER is disabled.

> XXX INDENT TEST contains the following errors.

> The dialog element 123456789 123456789 123456789 123456789 123456789

> 123456789 123 contains a pointer to an additional finding item that does

> not exist on the system.

> ZZPJH REMINDER contains the following errors.

> The dialog element WH PAP, ANNUAL DUE. contains an a pointer to the

> finding item that does not exist on the system.

> PHARMACY DISCHARGE MEDICATIONS contains the following errors.

> The dialog element PHARMACY DISCHARGE MEDS QUESTIONS contains a reference

> to a TIU Object OUTPATIENT MEDS in the Dialog Text field. This TIU Object

> does not exist on the system.

> The dialog group GRP MOVE! SCREENING 5/2007 contains a reference to a TIU

> Object BMI (BODY MASS INDEX %) in the Dialog Text field. This TIU Object

> does not exist on the system.

> Pap Smear (local) contains the following errors.

> The dialog element EX PAP DONE contains a reference to a TIU Object PAP

> SMEAR in the Dialog Text field. This TIU Object does not exist on the

> system.

> ETC.

> \*\*DONE\*\*

# Appendix E: Install File Print Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> \<I1028\> Select Utilities \<TEST ACCOUNT\> Option: Install File Print

> PACKAGE: PXRM\*2.0\*26 Oct 04, 2013 11:20 am PAGE 1

> COMPLETED ELAPSED

> -------------------------------------------------------------------------------

> STATUS: Install Completed DATE LOADED: OCT 01, 2013@13:47:24

> INSTALLED BY: PROGRAMMER,ONE

> NATIONAL PACKAGE: CLINICAL REMINDERS

> INSTALL STARTED: OCT 01, 2013@13:47:57 13:49:05 0:01:08

> ROUTINES: 13:47:58 0:00:01

> PRE-INIT CHECK POINTS:

> XPD PREINSTALL STARTED 13:47:58

> XPD PREINSTALL COMPLETED 13:47:58

> FILES:

> REMINDER DIALOG 13:47:58

> REMINDER FINDING TYPE PARAMETER 13:47:58

> REMINDER FUNCTION FINDING FUNCTIONS 13:47:58

> REMINDER TAXONOMY 13:47:58

> REMINDER COMPUTED FINDINGS 13:47:58

> REMINDER EXCHANGE 13:47:58

> PRINT TEMPLATE 13:47:58

> INPUT TEMPLATE 13:47:58

> FORM 13:47:59 0:00:01

> PROTOCOL 13:47:59

> LIST TEMPLATE 13:47:59

> OPTION 13:47:59

> POST-INIT CHECK POINTS:

> XPD POSTINSTALL STARTED 13:49:05 0:01:06

> XPD POSTINSTALL COMPLETED 13:49:05

> INSTALL QUESTION PROMPT ANSWER

> XPO1 Want KIDS to Rebuild Menu Trees Upon Completion of Install NO

> MESSAGES:

> Install Started for PXRM\*2.0\*26 :

> Oct 01, 2013@13:47:57

> Build Distribution Date: Sep 30, 2013

> Installing Routines:

> Oct 01, 2013@13:47:58

> Running Pre-Install Routine: PRE^PXRMP26I

> DISABLE options.

> DISABLE protocols.

> Building lists of dialogs to update

> Installing Data Dictionaries:

> Oct 01, 2013@13:47:58

> Installing Data:

> Oct 01, 2013@13:47:58

> Installing PACKAGE COMPONENTS:

> Installing PRINT TEMPLATE

> Installing INPUT TEMPLATE

> Installing FORM

> Installing PROTOCOL

> Installing LIST TEMPLATE

> Installing OPTION

> Oct 01, 2013@13:47:59

> Running Post-Install Routine: POST^PXRMP26I

> Copying all taxonomy Brief Descriptions to Description.

> Working on taxonomy 07 ASTHMA CODES

> Brief description does not exist.

> Etc. See Installation example in [Appendix A](#appendix-a-installation-example)

# Appendix F: Build File Print Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: CLINICAL REMINDERS ICD-10 UPDATE 1.0

> DEVICE: HOME//

> PACKAGE: PXRM\*2.0\*26 Oct 04, 2013 11:23 am PAGE 1

> -------------------------------------------------------------------------------

> TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

> NATIONAL PACKAGE: CLINICAL REMINDERS ALPHA/BETA TESTING: NO

> DESCRIPTION:

> Clinical Reminders ICD-10 changes.

> ENVIRONMENT CHECK: DELETE ENV ROUTINE:

> PRE-INIT ROUTINE: PRE^PXRMP26I DELETE PRE-INIT ROUTINE: No

> POST-INIT ROUTINE: POST^PXRMP26I DELETE POST-INIT ROUTINE: No

> PRE-TRANSPORT RTN:

> UP SEND DATA USER

> DATE SEC. COMES SITE RSLV OVER

> FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

> -------------------------------------------------------------------------------

> 801.41 REMINDER DIALOG YES NO NO

> 801.45 REMINDER FINDING TYPE PARAMETERNO NO YES OVER NO NO

> DATA SCREEN: I Y=20

> 802.4 REMINDER FUNCTION FINDING FUNCTIONSNOYES YES OVER NO NO

> DATA SCREEN: I +Y\>0

> 811.2 REMINDER TAXONOMY YES YES NO

> 811.4 REMINDER COMPUTED FINDINGS NO YES YES OVER NO NO

> DATA SCREEN: I \$\$CFINC^PXRMP26I(Y)

> 811.8 REMINDER EXCHANGE NO NO YES OVER NO NO

> DATA SCREEN: I \$\$EXFINC^PXRMEXSI(Y,"EXARRAY","PXRMP26E")

> PRINT TEMPLATE: ACTION:

> PXRM COMPUTED FINDING INQUIRY FILE \#811.4 SEND TO SITE

> INPUT TEMPLATE: ACTION:

> PXRM EDIT ELEMENT FILE \#801.41 SEND TO SITE

> PXRM EDIT GROUP FILE \#801.41 SEND TO SITE

> PXRM EDIT NATIONAL DIALOG FILE \#801.41 SEND TO SITE

> FORM: ACTION:

> PXRM DIALOG TAXONOMY EDIT FILE \#811.2 SEND TO SITE

> PXRM TAXONOMY CHANGE LOG FILE \#811.2 SEND TO SITE

> PXRM TAXONOMY EDIT FILE \#811.2 SEND TO SITE

> ROUTINE: ACTION:

> PXRM SEND TO SITE

> PXRMART SEND TO SITE

> PXRMBXTL SEND TO SITE

> PXRMCDEF SEND TO SITE

> PXRMCF SEND TO SITE

> PXRMCOPY SEND TO SITE

> PXRMCPLS SEND TO SITE

> PXRMCSPE SEND TO SITE

> PXRMCSTX SEND TO SITE

> PXRMDEDI SEND TO SITE

> PXRMDEDT SEND TO SITE

> PXRMDEV SEND TO SITE

> PXRMDGPT SEND TO SITE

> PXRMDLG1 SEND TO SITE

> PXRMDLG4 SEND TO SITE

> PXRMDLG6 SEND TO SITE

> PXRMDLL SEND TO SITE

> PXRMDLLA SEND TO SITE

> PXRMDLLB SEND TO SITE

> PXRMDLRP SEND TO SITE

> PXRMDTAX SEND TO SITE

> PXRMDUTL SEND TO SITE

> PXRMEFED SEND TO SITE

> PXRMEGED SEND TO SITE

> PXRMENOD SEND TO SITE

> PXRMEPED SEND TO SITE

> PXRMETX SEND TO SITE

> PXRMETXR SEND TO SITE

> PXRMEXCS SEND TO SITE

> PXRMEXFI SEND TO SITE

> PXRMEXHF SEND TO SITE

> PXRMEXIC SEND TO SITE

> PXRMEXID SEND TO SITE

> PXRMEXIH SEND TO SITE

> PXRMEXIU SEND TO SITE

> PXRMEXLB SEND TO SITE

> PXRMEXLC SEND TO SITE

> PXRMEXLM SEND TO SITE

> PXRMEXLR SEND TO SITE

> PXRMEXMM SEND TO SITE

> PXRMEXPD SEND TO SITE

> PXRMEXPS SEND TO SITE

> PXRMEXU0 SEND TO SITE

> PXRMEXU1 SEND TO SITE

> PXRMEXU2 SEND TO SITE

> PXRMEXU4 SEND TO SITE

> PXRMFF SEND TO SITE

> PXRMFFH SEND TO SITE

> PXRMFRPT SEND TO SITE

> PXRMGEDT SEND TO SITE

> PXRMGEN SEND TO SITE

> PXRMICHK SEND TO SITE

> PXRMINDC SEND TO SITE

> PXRMINDD SEND TO SITE

> PXRMINDL SEND TO SITE

> PXRMINDX SEND TO SITE

> PXRMINTR SEND TO SITE

> PXRMLDR SEND TO SITE

> PXRMLEX SEND TO SITE

> PXRMLEXL SEND TO SITE

> PXRMLIST SEND TO SITE

> PXRMLPOE SEND TO SITE

> PXRMOUTC SEND TO SITE

> PXRMOUTU SEND TO SITE

> PXRMP26D SEND TO SITE

> PXRMP26E SEND TO SITE

> PXRMP26X SEND TO SITE

> PXRMPARS SEND TO SITE

> PXRMPDS SEND TO SITE

> PXRMPROB SEND TO SITE

> PXRMRCPT SEND TO SITE

> PXRMREDF SEND TO SITE

> PXRMREDT SEND TO SITE

> PXRMRUL1 SEND TO SITE

> PXRMSCR SEND TO SITE

> PXRMSEL SEND TO SITE

> PXRMSINQ SEND TO SITE

> PXRMSTA1 SEND TO SITE

> PXRMSTA2 SEND TO SITE

> PXRMSTS SEND TO SITE

> PXRMTAX SEND TO SITE

> PXRMTAXD SEND TO SITE

> PXRMTAXL SEND TO SITE

> PXRMTDLG SEND TO SITE

> PXRMTIU SEND TO SITE

> PXRMTXCE SEND TO SITE

> PXRMTXCR SEND TO SITE

> PXRMTXCS SEND TO SITE

> PXRMTXDL SEND TO SITE

> PXRMTXIM SEND TO SITE

> PXRMTXIN SEND TO SITE

> PXRMTXSM SEND TO SITE

> PXRMUIDR SEND TO SITE

> PXRMUTIL SEND TO SITE

> PXRMVCPT SEND TO SITE

> PXRMVPOV SEND TO SITE

> PXRMXEVL SEND TO SITE

> PXRMXSE1 SEND TO SITE

> PXRMXT SEND TO SITE

> PXRMXTA SEND TO SITE

> PXRMXTB SEND TO SITE

> OPTION: ACTION:

> PXRM TAXONOMY DIALOG DELETE AT SITE

> PXRM TAXONOMY MANAGEMENT SEND TO SITE

> PROTOCOL: ACTION:

> PXRM DIALOG COPY COMPONENT SEND TO SITE

> PXRM DIALOG EDIT INQUIRY SEND TO SITE

> PXRM DIALOG SELECTION MENU (DLGE) SEND TO SITE

> PXRM DIALOG TAXONOMY EDIT SEND TO SITE

> PXRM LEXICON ADD SEND TO SITE

> PXRM LEXICON MENU SEND TO SITE

> PXRM LEXICON REMOVE FROM DIALOG SEND TO SITE

> PXRM LEXICON REMOVE FROM TAXONOMY SEND TO SITE

> PXRM LEXICON SAVE SEND TO SITE

> PXRM LEXICON SELECT ENTRY SEND TO SITE

> PXRM LEXICON USE IN DIALOG SEND TO SITE

> PXRM SELECTION ADD SEND TO SITE

> PXRM SELECTION EXIT SEND TO SITE

> PXRM SELECTION PRINT ALL SEND TO SITE

> PXRM SELECTION VIEW (CV) SEND TO SITE

> PXRM TAXONOMY ADD SEND TO SITE

> PXRM TAXONOMY CHANGE LOG SEND TO SITE

> PXRM TAXONOMY CHOOSE ENTRIES SEND TO SITE

> PXRM TAXONOMY CHOOSE ENTRY SEND TO SITE

> PXRM TAXONOMY CHOOSE REMOVE SEND TO SITE

> PXRM TAXONOMY CHOOSE SELECT SEND TO SITE

> PXRM TAXONOMY CODE SEARCH SEND TO SITE

> PXRM TAXONOMY COPY SEND TO SITE

> PXRM TAXONOMY EDIT SEND TO SITE

> PXRM TAXONOMY IMPORT SEND TO SITE

> PXRM TAXONOMY INQUIRE SEND TO SITE

> PXRM TAXONOMY MENU SEND TO SITE

> PXRM TAXONOMY OLD INQUIRE SEND TO SITE

> PXRM TAXONOMY SELECT ENTRY SEND TO SITE

> PXRM TAXONOMY UID REPORT SEND TO SITE

> VALM QUIT ATTACH TO MENU

> LIST TEMPLATE: ACTION:

> PXRM LEXICON SELECT SEND TO SITE

> PXRM SELECTION SEND TO SITE

> PXRM TAXONOMY CHOOSE ENTRIES SEND TO SITE

> PXRM TAXONOMY MANAGEMENT SEND TO SITE

> INSTALL QUESTIONS:

> Default Rebuild Menu Trees Upon Completion of Install: NO

> Default INHIBIT LOGONs during the install: NO

> Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

> REQUIRED BUILDS: ACTION:

> LEX\*2.0\*80 Don't install, leave global

> DG\*5.3\*862 Don't install, leave global

> GMPL\*2.0\*44 Don't install, leave global

> PXRM\*2.0\*24 Don't install, leave global

> Press RETURN to continue: