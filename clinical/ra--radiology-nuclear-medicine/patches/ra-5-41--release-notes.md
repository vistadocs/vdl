---
title: RA*5*41 Clinical Indicator Capture (CIDC) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Clinical Indicator Capture (CIDC)
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5*41
group_key: "RA:RA:5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Release Notes](#release-notes) - [Clinical Indicator Data Capture](#clinical-indicator-data-capture) - [Changed Options](#changed-options) - [Data Definition Changes](#data-definition-changes)
audience: 
keywords: 
  - clinical
  - order
  - radiology
  - table
  - contents
  - ordering
  - diagnosis
  - modified
  - location
  - date
page_count: 0
word_count: 892
section_count: 2
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2005
revision_count: 4
revision_newest: 08/02/05
revision_oldest: 12/15/04
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_p41_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_p41_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

![](ra-5-41-clinical-indicator-capture-cidc-release-notes/001.png)

RADIOLOGY/NUCLEAR MEDICINE

CLINICAL INDICATOR CAPTURE (CIDC)

PATCH RA\*5.0\*41

RELEASE NOTES

#### Version 5.0

August 2005

VistA Health System Design & Development

Revision History

| Date | Page | Description                                                                                 |
|----------|----------|-------------------------------------------------------------------------------------------------|
| 09-10-03 | All      | New Functionality based on Clinical Indicator Data Capture (CIDC)                               |
| 06-16-04 | All      | Edited previous notes to reflect changes in phase 2 of CIDC                                     |
| 12/15/04 | 8        | Edited previous notes to mention PROVIDER and ORES keys                                         |
| 12/29/04 | 5        | Edited previous notes to remove ORES key where not needed, and to also explain the CIDC switch. |
| 01/03/05 | 1        | Changed "CIDC" to "CIDC compliant"                                                              |
| 08/02/05 | All      | Remove ORES key everywhere it is mentioned                                                      |

Table of Contents

# Release Notes 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes](#release-notes)
  - [Clinical Indicator Data Capture](#clinical-indicator-data-capture)
- [Changed Options](#changed-options)
- [Data Definition Changes](#data-definition-changes)

## Clinical Indicator Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current radiology application has been modified to become "CIDC compliant". This involves capturing data not previously captured in the application in order to submit a “Clean Claim".

Several changes have been made to the Radiology package.

When an order is placed from the Radiology application, and the person who is entering the order has the PROVIDER key, then the following questions are now asked:

- Primary Ordering International Classification of Diseases(ICD) Diagnosis
  - (Clinical Indicators related to this ICD Diagnosis)

> SC - Service Connected MST - Military Sexual Trauma

> AO - Agent Orange HNC - Head & Neck Cancer

> IR - Ionizing Radiation CV - Combat Vet

> EC - Environmental Contaminant

- Secondary Ordering ICD Diagnosis
  - (Clinical Indicators related to this ICD Diagnosis)

> SC - Service Connected MST - Military Sexual Trauma

> AO - Agent Orange HNC - Head & Neck Cancer

> IR - Ionizing Radiation CV - Combat Vet

> EC - Environmental Contaminant

When a report is entered or edited, the following question is now asked:

- Interpreting Imaging Location

The following data elements have been added to the Radiology database:

- Primary Ordering ICD Diagnosis and related Clinical Indicators
- Secondary Ordering ICD Diagnosis and related Clinical Indicators
- Interpreting Imaging Location

All of the Ordering ICD Diagnosis questions call the new Code Set Versioning (CSV) Application Program Interface (API) to verify that the ICD Diagnosis is active on the date of the order. The data screen is DIC("S")="I \$P(\$\$ICDDX^ICDCODE(Y,DT),U,10)”

Orders will no longer be able to be purged from the Radiology Package.

# Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Several options have been modified to ask, capture, and display the necessary information related to the Clinical Indicator Data Capture (CIDC) project.

Radiology/Nuclear Med Order Entry Menu \[RA ORDER\]Request an Exam \[RA ORDEREXAM\] has been modified to ask for additional data: Primary and Secondary Ordering ICD Diagnosis along with their related clinical indicators. These are sent to the Patient Care Encounter (PCE) package for both inpatients and outpatients. But the prompts for the additional data will only appear if the user has the PROVIDER key and if the "CIDC Insurance and switch" function returns a non-zero value. This function evaluates the patient's billable insurance and checks the CIDC "ask questions" switch.

This option will also include another prompt, "Copy a previous order's ICD codes and SC/EC values? NO//". (The Service Connected/ (SC/EC) will not appear if the patient is not Service Connected according to the Enrollment package.) If the user enters "Y", then selects a previous order, the system will copy the selected previous order's ICD and SC/EC values and display them as default values to the ICD and SC/EC prompts that will appear later in the processing of the new order.

Radiology will store the new ordering data and also send them to CPRS.

If the Computerized Patient Record System (CPRS) Graphical User Interface (GUI) application was used to place the order, then the CPRS GUI application will store the new ordering data in its database and also send them to Radiology.

The new Primary and Secondary Ordering ICD Diagnoses and their related clinical indicators, if previously prompted for, will be displayed later along with the other data entered during 'Request an Exam', so the user can double-check the entries before submitting the order.

Print Rad/Nuc Med Requests by Date \[RA ORDERPRINTS\] and Print Selected Requests by Patient \[RA ORDERPRINTPAT\] have been modified to display the new Primary and secondary Ordering ICD Diagnosis and their related clinical indicators.

Also, the DIC(“S”), the entry/edit screen for the Requesting Physician field, has been modified to check that the Requesting Physician has the "PROVIDER" security key and doesn't have a TERMINATION DATE before current date.

<u>Films Reporting Menu \[RA RPT\]</u>

Report Entry/Edit \[RA RPTENTRY\] has a new prompt, "INTERPRETING IMAGING LOCATION". This new prompt will allow users to enter the location where the procedure was interpreted.

In addition, the Credit Method field has been modified to allow for partial crediting

Resident On-Line Pre-Verification \[RA RESIDENT PRE-VERIFY\] has a new prompt added to this option. The new prompt is "INTERPRETING IMAGING LOCATION". It will allow users to enter the location where the procedure was interpreted.

The RAPCE routine has been modified to send the INTERPRETING IMAGING LOCATION to Patient Care Encounter (PCE) if it exists; otherwise, the previous Imaging Location where the exam was performed will be sent to PCE. This routine is used by several options, when any one of those options causes the exam's status to reach "COMPLETE".

Also, the Credit Method field has been modified to allow for partial crediting.

> The default Interpreting Imaging Location will be calculated from the current sign-on or switched-to location, if possible. If not, a warning message will be displayed. So there are four possible displays after the Interpreting Imaging Location prompt:

> 1\) the user's sign-on Radiology location

> 2\) a warning message -- if the sign-on or switched-to location is "Technical Component only" :

> "Your signed-on or switched-to location is AAAAA which has a Credit Method of 'Technical Component Only'. This Credit Method does not allow for Interpretation work."

> 3\) a warning message -- if the sign-on location's Imaging Type doesn't match the exam's Imaging Type :

> "Your signed-on or switched-to location is AAAAA which has an Imaging Type of MMMMM. But the exam has an Imaging Type of GGGGG."

> 4\) a reminder message -- if (2) and (3) :

> "You may optionally switch your current location to a location

> that allows either Regular or Interpretation credit. This will facilitate subsequent report entries, if you have more than one report to enter."

> Since this field will be added to the report instead of the exam, for a print set (two or more cases share the same report), the user would only have to enter its value once for the report.

> If the home site uses a remote site to do the interpretation, and the remote site isn't already defined in file \#79.1, then the Automated Data Processing Application Coordinator (ADPAC) will have to use the 'Location Parameter Set-up' option to create a new imaging location for the remote site. Then he must use the 'Division Parameter Set-up' option to link the new Imaging Location to a Division.

System Definition Menu ... \[RA SYSDEF\]

> 'Location Parameter Set-up' has a modification in the Credit Method field to allow for partial crediting. Now, all four credit methods are selectable:

0 : Regular Credit

1 : Interpretation Only

2 : No Credit

3 : Technical Component Only

IRM Menu \[RA SITEMANAGER\]Purge Data Function \[RA PURGE\] option has been modified to remove all references to purging orders. Orders will no longer be able to be purged from the Radiology package.

# Data Definition Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rad/Nuc Med Patient file \#70, subfile \#70.03

> Field Modified:

Requesting Physician \#14

> DIC(“S”), the entry/edit screen for the Requesting Physician field has been

modified to check for the PROVIDER key and that the requester

does not have a TERMINATION DATE before current date.

> Modified DIC(“S”) from:

> S DIC("S")="I \$S('\$D(^(""PS"")):1,'\$P(^(""PS""),U,4):1,DT'\>\$P(^(""PS"")

> ,U,4):1,1:0)&(\$D(^XUSEC(""PROVIDER"",Y)))"

> to:

> S DIC("S")="I \$\$PROV^RABWORD()"

> Credit Method \#26

> will now accept partial crediting

Rad/Nuc Med Orders file \#75.1

> Field Modified:

Requesting Physician \#14

> DIC(“S”), the entry/edit screen for the Requesting Physician field has been modified to check for the PROVIDER key and that the requester

does not have a TERMINATION DATE before current date.

> Modified DIC(“S”) from:

> S DIC("S")="I \$S('\$D(^(""PS"")):1,'\$P(^(""PS""),U,4):1,DT'\>\$P(^(""PS"")

> ,U,4):1,1:0)&(\$D(^XUSEC(""PROVIDER"",Y)))"

> to:

> S DIC("S")="I \$\$PROV^RABWORD()"

> Fields Added:

> Primary Ordering ICD Diagnosis \#91

> Primary DX Related to SC \#92

> Primary DX Related to AO \#93

> Primary DX Related to IR \#94

> Primary DX Related to EC \#95

> Primary DX Related to MST \#96

> Primary DX Related to HNC \#97

> Primary DX Related to CV \#99

> Secondary Ordering ICD Diagnosis \#98

> Subfile \#75.13

> Fields Added:

> Secondary Ordering ICD Diag. \#.01

> Secondary DX Related to SC \#2

> Secondary DX Related to AO \#3

> Secondary DX Related to IR \#4

> Secondary DX Related to EC \#5

> Secondary DX Related to MST \#6

> Secondary DX Related to HNC \#7

> Secondary DX Related to CV \#8

> Rad/Nuc Med Reports \#74

> Field Added:

> Interpreting Imaging Location \#86

Imaging Locations file \#79.1

> Field Modified:

> Credit Method \#21

> will now accept partial crediting