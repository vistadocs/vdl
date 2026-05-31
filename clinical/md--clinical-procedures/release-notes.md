---
title: MD*1*29 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: MD
patch_ver: 1
patch_id: MD*1*29
group_key: MD:MD:1
file_numbers:
- '702.09'
security_keys: []
menu_options: 0
description: '- Introduction - Purpose - Background - Scope of Changes - Dependencies - Documentation - GUI Installation Instructions - [GUI Installation...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 2305
section_count: 14
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: August 2014
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/ClinProc/icd-10_rn_md_1_29.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/ClinProc/icd-10_rn_md_1_29.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=139
audit_applied: '2026-05-31'
master_source: MD*1*29 Release Notes
master_pub_date: August 2014
consolidated_from: 6 versions
prior_versions:
- MD*1*12 Release Notes (CP Flowsheets)
- MD*1*14 Release Notes
- MD*1*16 Release Notes (CP Flowsheets)
- MD*1*21 Release Notes
- MD*1*23 Release Notes (CP Flowsheets)
consolidated_title: release notes
---

ICD-10 Follow On Class 1 Software Remediation Project

Clinical Procedures

Application Version 1.0

Release Notes

MD\*1.0\*29

![](md-1-29-release-notes/001.png)

August 2014

Office of Information and Technology (OI&T)

Product Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Dependencies](#dependencies)
  - [Documentation](#documentation)
- [GUI Installation Instructions](#gui-installation-instructions)
  - [GUI Installation Steps](#gui-installation-steps)
- [ESRD ICD-10 Diagnosis Code Drop Down List](#esrd-icd-10-diagnosis-code-drop-down-list)
  - [ESRD ICD-10 Diagnosis Code Updating Instructions](#esrd-icd-10-diagnosis-code-updating-instructions)
- [CP Hemodialysis Summary Tab Modifications](#cp-hemodialysis-summary-tab-modifications)
  - [Diagnosis Code Modifications](#diagnosis-code-modifications)
  - [Short Description Display Modifications](#short-description-display-modifications)
- [ICD-10 Searches](#icd-10-searches)
  - [Search Features for ICD Diagnosis Codes](#search-features-for-icd-diagnosis-codes)
  - [ICD-10 Search/Look-Up](#icd-10-searchlook-up)
  - [ICD-10 Search/Look-Up Parameters](#icd-10-searchlook-up-parameters)
- [Technical Information](#technical-information)
  - [Routines](#routines)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Clinical Procedures (CP) package contained in patch MD\*1.0\*29.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 activation date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alphanumeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision-making and outcomes research.

> ICD-9-CM and ICD-10-CM Comparison

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>ICD-9-CM Diagnosis Codes</th>
<th>ICD-10-CM Diagnosis Codes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>13,000 codes</td>
<td>68,000 codes</td>
</tr>
<tr class="even">
<td>3-5 characters</td>
<td>3-7 characters (not including the decimal)</td>
</tr>
<tr class="odd">
<td>Character 1 is numeric (chapters 1-17) or alpha (E or V) (supplemental chapters)</td>
<td>Character 1 is alpha<br />
Character 2 is numeric</td>
</tr>
<tr class="even">
<td>Characters 2-5 are numeric</td>
<td>Characters 3–7 are alpha or numeric<br />
(alpha characters are not case-sensitive)</td>
</tr>
<tr class="odd">
<td>Decimal included after 3rd character</td>
<td>Decimal included after 3rd character</td>
</tr>
</tbody>
</table>

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch MD\*1.0\*29 makes the following changes to the Clinical Procedures application:

- For a period of time, Veterans Health Administration (VHA) will require the use of dual code sets (ICD-9-CM, ICD-10-CM) to accommodate outpatient dates of service (visit date, appointment date) and inpatient discharge dates prior to and following the ICD-10 activation date as well as for reporting and research purposes.
- The VistA Clinical Procedures package does not utilize ICD procedure codes, therefore, there are no changes required for ICD-10-PCS.
- CP Hemodialysis is the only module within Clinical Procedures that will utilize the ICD-10-CM code set.
- VistA Clinical Procedures is a conduit for passing patient results from the vendor specific Commercial-Off-the-Shelf (COTS) instruments and VistA using Health Level 7 (HL7) messaging. The VistA CP MUMPS device interface used for HL7 interfaces with vendor instruments needs no revisions to accept ICD-10 diagnosis codes, because the ICD data are transmitted in a free text field in the HL7 message.
- National Service Request: NSR 20070902, ICD-10-CM Conversion.

The search functionality includes, but is not limited to, the following:

- Diagnosis codes are increased from approximately 13,000 to 68,000.
- Search features for diagnosis codes are standardized and enhanced.
- Selection features for diagnosis codes using Add/Edit/Store can now be done three ways.
- Problem List code replacement of inactive ICD codes with active ICD-10 codes is enabled.
- Online forms will display "ICD-10" instead of "ICD-9" where appropriate.
- Online forms enable selection of multiple or individual patients, and entry of notes and data in respective windows.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

End Stage Renal Disease (ESRD) Diagnosis Codes table  
The ESRD diagnosis codes are selected from the ESRD Diagnosis Codes table, a data list with customized ICD-9 textual data. The business owners/subject matter experts (SMEs) have provided updates to this custom data list with ICD-10-CM diagnoses for testing and implementation purposes.

Lexicon Utility and Patient Care Encounter (PCE) Dependencies  
The VistA Clinical Procedures Hemodialysis module is dependent on the Lexicon Utility to search for the ICD diagnoses and the PCE module to store the patient ICD diagnosis data. The interdependency between these VistA applications makes it essential that the VistA Lexicon and PCE ICD-10 patches be installed prior to the installation of the Clinical Procedures ICD-10 patches.

ICD-10 Clinical Procedures Test Environment  
An ICD-10 test environment needs to be created that mirrors a production medical center and has the ICD-10 Lexicon Utility, PCE and Clinical Procedures patches in place. It is essential to co-install these VistA applications because of the interdependencies for successful ICD-10 end-to-end integration testing and implementation.

ICD Diagnosis Code Transmission  
VistA CP is a conduit for passing patient results from the vendor-specific COTS instruments and VistA using HL7 messaging. The VistA CP MUMPS device interface needs no revisions to accept ICD-10 diagnosis codes from the free text field, but any changes due to ICD-10 implementation must be coordinated with the Hines Office of Information Field Office (OIFO) and the dialysis machine vendors.

The VistA CP application has approved HL7 interfaces with dialysis machines from the following manufacturers: Gambro, Fresenius, and Braun. Diagnosis codes can be passed to CP Hemodialysis from these external software applications using the free text UNIVERSAL SERVICE ID field in the CP INSTRUMENT file (#702.09), which defines what type of procedure the device can perform. Since there is no VA standard list for hemodialysis devices, local facilities may or may not have Class III interfaces with VistA, which may capture ICD data.

> External Dependencies Specific to CP Remote Procedure Calls (RPCs)

| Name/Signature of the Component | Provider Application | Consumer Application | ICR   | ICD Related? |
|---------------------------------|----------------------|----------------------|-------|--------------|
| IN5^VADPT                       | Registration         | Clinical Procedures  | 10061 | Yes          |
| \$\$DATA2PCE^PXAPI              | PCE                  | Clinical Procedures  | 1889  | Yes          |
| \$\$DELVFILE^PXAPI              | PCE                  | Clinical Procedures  | 1890  | Yes          |
| MAKE^TIUSRVP                    | TIU                  | Clinical Procedures  | 3535  | TBD          |
| UPDATE^TIUSRVP                  | TIU                  | Clinical Procedures  | 3535  | TBD          |
| SIGN^TIUSRVP2                   | TIU                  | Clinical Procedures  | 4795  | TBD          |
| GETLST^IBDF18A                  | AICS                 | Clinical Procedures  | 1296  | Yes          |
| CONFIG^LEXSET                   | Lexicon              | Clinical Procedures  | 1609  | Yes          |
| LOOK^LEXA                       | Lexicon              | Clinical Procedures  | 2950  | Yes          |
| \$\$GETENC^PXAPI                | PCE                  | Clinical Procedures  | 1894  | Yes          |
| ENCEVENT^PXAPI                  | PCE                  | Clinical Procedures  | 1894  | Yes          |

Patches  
The following associated patches must be installed prior to installing MD\*1\*29:

- MD\*1\*20
- LEX\*2\*80
- PX\*1\*199
- IBD\*3\*63
- ICD\*18\*57

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Procedures manuals are posted on the Department of Veterans Affairs (VA) Documentation Library (VDL) at [http://www.va.gov/vdl](http://www.va.gov/vdl139).

The following Clinical Procedures user manuals are updated with changes for MD\*1.0\*29:

- VistA Clinical Procedures Technical Manual Version 1.0 and Change Pages
- VistA Clinical Procedures User Manual Version 1.0 Hemodialysis Module and Change Pages

The following manuals do not contain changes relating to MD\*1.0\*29:

- Implementation Guide Version 1.0

The following manual does not exist for this package:

- Security Guide

> **NOTE:** Security Information is contained within the *VistA Clinical Procedures Technical Manual Version 1.0*.

# GUI Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Procedures Graphical User Interface (GUI) client software is being distributed as a self- extracting Install Shield executable. The installed executable for this patch is client version 1.0.29.22 with a size of 4.15 MB.

- Application version: 1.0.29.22
- CRC for Hemodialysis.exe: 30C8789D
- File Name: MD1_0P29GUI_22.ZIP
- GUI changes:
- The default ICD-10 cut-off date is set to the ICD-10 activation date.
- Comments added to the "ICD-10 Implementation date" parameter.

> **NOTE:** This patch includes a revised Graphical User Interface (GUI) application that must be distributed to the appropriate workstations. After the patch is installed correctly, and the GUI is updated, the version of the GUI will be 1.0.29.22.

## GUI Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Unzip the MD1_0P29GUI_22.ZIP into a temporary folder.
2.  Open the temporary folder and double-click the Hemodialysis.exe file to begin the install.
3.  Wait until the setup Wizard prepares the installation procedure. A Welcome message displays.
4.  Click Next to continue the installation.
5.  Select the directory in which to install the CP GUI. We recommend that you accept the default directory:
    1.  Windows XP: C:\Program Files\Vista\Hemodialysis
    2.  Windows 7: C:\Program Files(x86)\Vista\Hemodialysis

> Note: We recommend using the default location if you have desktop shortcuts with parameters.

6.  Click Next to proceed with installation.
7.  Review the installation settings and click Install to proceed. The setup Wizard finishes the installation and a confirmation screen displays.
8.  Click Finish.
9.  This installs or updates the following files:
1.  Hemodialysis.exe , size 4.15MB
2.  Hemodialysis.hlp, size 937KB
3.  Hemodialysis.cnt, size 4KB
4.  RoboEX32.dll, size 1,020KB
5.  Shortcut To Hemodialysis, size 1KB

# ESRD ICD-10 Diagnosis Code Drop Down List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ESRD Diagnosis drop-down list is populated with ICD-9 and/or ICD-10 diagnosis codes, dependent on the Current Treatment Date.

ESRD Diagnosis Drop-Down List

![](md-1-29-release-notes/002.png)

> **NOTE:** The default list of ICD-10 diagnosis codes contains more than 200 codes and can be updated by the Administrative user of the GUI application.

## ESRD ICD-10 Diagnosis Code Updating Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Administrative user only: To update the default list of the ICD-10 codes manually, perform the following steps:

1.  Start the application and log in as Admin user.
2.  On the top left-hand corner of your screen, from the main menu, select Options.
3.  From the drop-down on the left-hand side of your screen, select Custom Data Lists.
4.  Select ESRD Diagnosis ICD10 from the list.

> ESRD Diagnosis with ICD10 Selected

> ![](md-1-29-release-notes/003.png)

5.  Use "Add" and "Delete" buttons to modify the list of codes.
6.  Once the codes have finished loading, click the Save To DB button.

> Browse to ICD10 Diagnosis Code List to Load the List

> ![](md-1-29-release-notes/004.png)

1.  Once the codes have finished loading, click the Save To DB button.

> Save To DB Button for ESRD ICD10

> ![](md-1-29-release-notes/005.png)

2.  The main window populates with the ICD-10 diagnosis codes.

> ICD-10 Diagnosis Codes Loaded and Displayed

> ![](md-1-29-release-notes/006.png)

# CP Hemodialysis Summary Tab Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the CP Hemodialysis Patient Data Page Summary tab window, the ICD-10 diagnosis codes and descriptions display.

> ICD-10 VistA CP Hemodialysis Summary Tab Display

> Diagnosis (ICD Codes)

> T39.011D Poisoning by aspirin, accident Primary

The Diagnosis tab option, within the VistA CP Hemodialysis Patient Data Display Page Summary Tab, now has the ability to handle ICD-10 diagnoses codes from the "Diagnoses (ICD Codes)" prompt.

> **NOTE:** Detailed information on the ICD-10 search ability is in Section 5, ICD-10 Searches.

## Diagnosis Code Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the CP Hemodialysis Patient Data Page Summary Tab window, the VistA CP application can add/edit/store ICD-10 diagnosis codes (up to eight alphanumeric characters including the decimal point that follows the third character), depending on the Current Treatment Date field.

> **NOTE:** Detailed information on the ICD-10 search ability is in Section 5, ICD-10 Searches.

## Short Description Display Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the CP Hemodialysis Patient Data Display Page Summary tab window, primary ICD-10 diagnosis short descriptions are displayed if more than one diagnosis is associated with a treatment.

> Display Primary Diagnosis Selection Example

> ![](md-1-29-release-notes/007.png)

> **NOTE:** Detailed information can be found in Section 5, ICD-10 Searches.

# ICD-10 Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Procedures package provides the ability to search on ICD-10-CM diagnosis codes.

> **NOTE:** The VistA Clinical Procedures package does not utilize ICD procedure codes; therefore, there are no changes required for ICD-10-PCS.

> **NOTE:** Existing ICD-9 functionality has not changed.

## Search Features for ICD Diagnosis Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You are able to search on ICD-10-CM diagnosis codes from the Hemodialysis Patient Data Screen Summary tab through the "Diagnoses (ICD Codes)" prompt found on the Diagnosis tab. The search function allows you to do the following:

- Search results include a manageable list of possible codes with descriptions that consist of any combination of categories, sub-categories, and valid codes.
- You can "drill down" through the categories and sub-categories to identify a code that best matches the diagnosis.
- Short descriptions for the codes can be displayed.
- Partial and full code searches are enabled.
- VistA Clinical Reminders when Clinical Reminders taxonomies are defined

## ICD-10 Search/Look-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA CP User window, Hemodialysis Patient Data Screen Summary tab, allows ICD diagnosis code searches/lookups at the Diagnosis prompt using the Lexicon utility.

> **NOTE:** The "Date of Interest" within the Lexicon Utility Requirements Specification Document (RSD) is equivalent to the PCE Visit date (Outpatient Appointment or Inpatient Encounter Date). Within CP, this date is referred to as Current Treatment Date and displayed in the Summary Tab.

> **NOTE:** If the treatment date is prior to the ICD-10 activation date, the VistA Clinical Procedures Hemodialysis application shall retain the current search functionality for ICD-9-CM diagnosis codes and descriptions/definitions.

The screen below shows the Hemodialysis Patient Data Screen Summary tab. To perform a search and/or add a diagnosis, follow the steps below.

1.  To search for and add an ICD-10 diagnosis for a patient, click the Diagnosis option in the upper right-hand corner of the screen.

> Patient Data Screen Summary Tab Showing Diagnosis Icon

> ![](md-1-29-release-notes/008.png)

2.  A dialogue box appears. Enter the diagnosis code in the Search text box and click Search. For this example, R59 is the code chosen.
3.  The LexiconDiagnosis field populates, as does the Primary Diagnosis field.
4.  Place a checkmark next to the code that is the Primary Diagnosis for that patient.
5.  To add a Lexicon diagnosis to the Primary Diagnosis selected, highlight that Lexicon diagnosis and click the right pointingdouble arrow button between the two fields to move that diagnosis.
6.  The newly added ICD-10 diagnosis now displays under the Primary Diagnosis field.

> Primary Diagnosis Field Displaying the ICD-10 Codes

> ![](md-1-29-release-notes/009.png)

7.  Repeat this process until you have added all the Lexicon diagnoses needed. Once complete, click Save in PCE.
8.  Return to the Hemodialysis Patient Data Screen Summary tab, the newly added diagnosis codes now display on the screen.

> Hemodialysis Patient Data Screen Summary Tab Displaying Added Diagnosis Codes

> ![](md-1-29-release-notes/010.png)

## ICD-10 Search/Look-Up Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Current Treatment Date in CP is prior to the ICD-10 activation date, then the search is conducted on ICD-9 codes. All searches associated with that date are in ICD-9 mode. Likewise, if the Current Treatment Date in CP is on or after to the ICD-10 activation date, then the search is conducted on ICD-10 codes. All searches associated with that date are in ICD-10 mode.

If you try to search for an ICD-9 code under a PCE Visit Date that is on or after the ICD-10 activation date, the search results display a No Matches Found message.

> Search Returns No Matches Example

> ![](md-1-29-release-notes/011.png)

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some Clinical Procedures routines were modified to replace direct global reads and old Application Program Interfaces (APIs) with new Standards and Terminology Services (STS) APIs and Lexicon APIs wherever possible. The following new routines are added:

New Routines

| Modified API     | Function                                                                                       |
|------------------|------------------------------------------------------------------------------------------------|
| \$\$ICDDX^ICDEX  | To validate and retrieve the ICD data.                                                         |
| \$\$ONE^LEXU     | Returns a single code for a given internal entry number (IEN) for a specified date and source. |
| \$\$SINFO^ICDEX  | To determine the active coding system based on a date.                                         |
| \$\$IMPDATE^LEXU | To determine the ICD-10 implementation date.                                                   |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MD*1*23 Release Notes (CP Flowsheets)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MD\*1.0\*23 releases fixes and updates to CP Flowsheets and CP Console. See below for an individual list of fixes released.

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To install patch MD\*1.0\*23, follow the *Clinical Procedures (CP) V1.0 Flowsheets Module Installation Guide* (distributed with patch MD\*1.0\*26) carefully. Although part of CP, CP Flowsheets is independent of CP User, CP Manager, CP Gateway, and CP Hemodialysis.

> ![](md-1-23-release-notes-cp-flowsheets/002.png) Vitals patches GMRV\*5.0\*22, GMRV\*5.0\*23, MD\*1.0\*21, MD\*1.0\*16, MD\*1.0\*26, and MD\*1.0\*12 must be installed prior to the installation of the MD\*1.0\*23 software. A test version of MD\*1.0\*12 is available from the same download site from which you received MD\*1.0\*23.

> ![](md-1-23-release-notes-cp-flowsheets/003.png) It is suggested that the output of the KIDS installation process be saved to a text file for distribution to CACs/Flowsheet administrators at the local site for review. The post

> install process will display a report of terms that were deactivated that are still being used in a flowsheet, allowing local staff to modify those views and flowsheets.

> ![](md-1-23-release-notes-cp-flowsheets/004.png) MD\*1.0\*23 includes *pre-install* routine MDPRE23 and *post-install* routine MDPOST23.

> Verify that these routines are complete before attempting to use CP Flowsheets.

> ![](md-1-23-release-notes-cp-flowsheets/005.png) The IV DOSE Rate observation is deactivated in MD\*1.0\*23 and replaced with a series of dosage/rate specific observations. Before you install MD\*1.0\*23, print reports covering the appropriate time span prior to installation if your site uses IV Dose Rate observations. After the patch is installed, please update observations and views based on need.

## Validated Patient Monitoring Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A supported device is one that has its data elements mapped to the standard terminology of the CliO database. The following devices are currently supported:

> ![](md-1-23-release-notes-cp-flowsheets/006.png)Intesys Clinical Suite (Spacelabs) PC1 (Spacelabs)

> PC2 (Spacelabs)

> Ultraview 1050 (Spacelabs)

> Ultraview 1600 (Spacelabs)

> Ultraview 1700 (Spacelabs) Ultraview SL2200 (Spacelabs) Ultraview SL2400 (Spacelabs) Ultraview SL2600 (Spacelabs) Ultraview SL2700 (Spacelabs) Ultraview SL2800 (Spacelabs) Ultraview SL3800 (Spacelabs) Nihon Koden

## Additional Medical Monitoring Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ICU devices will be added to the list of validated instruments as the devices are certified through the Hines Field Office.

> For sites that want to implement ICU devices, but do not have Clinical Procedures implemented, refer to the *Clinical Procedures (CP) V1.0 Flowsheets Module Implementation Guide*. You do not need to implement the legacy Clinical Procedures.

> For sites that use legacy Clinical Procedures and want to implement the CP Flowsheets patch, continue using the legacy CP modules and use CP Console to configure the ICU devices.

> Note: The CP Manager application is no longer supported after the installation of MD\*1.0\*16, which must be installed prior to the installation of MD\*1.0\*23. Use CP Console to perform the functions previously provided by CP Manager

> *This page intentionally left blank for double-sided printing.*

> .

### From: MD*1*16 Release Notes (CP Flowsheets)

## Interface with Third Party Monitoring Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MD\*1.0\*16 provides an interface for the collection of patient observational data from monitoring devices. The collected data is stored automatically in the appropriate VistA database(s).

## Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MD\*1.0\*16 provides standardized terminology with VA Unique Identifiers (VUIDs). This facilitates exporting CliO data to other VA systems that use standardized terminology.

## GUI Flowsheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets utilizes locally-customizable flowsheets to view, enter, and edit patient data entered manually or received via the CliO infrastructure. Ultimately, this application will provide the front-end for other clinical systems, such as the Renal Dialysis, and Intake and Output (I&O) packages.

## ADT HL7 Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets introduces an Admission Discharge and Transfer (ADT) Health Level 7 (HL7) message feed. The ADT feed monitors the admitted, discharged, and transferred events from the Patient Information Management System (PIMS) and notifies interested patient medical monitoring devices.

## Manual Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets allows you to manually enter data personally observed by clinical staff or collected by monitors that are not able to electronically send that information.

## Data to CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MD\*1.0\*16 is capable of publishing data to CPRS in two ways. Vitals observations entered into the CliO service architecture is directly viewable in Vitals/Vitals Lite in the Computerized Patient Record System (CPRS). All other observational data entered may be published in a Text Integration Utilities (TIU) note, which is then viewable in CPRS.

## GUI Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Console is a user-friendly GUI with which you can configure system parameters and patient medical monitoring devices, schedule background tasks and shifts, and design flowsheet templates to meet site-specific requirements.

## Background Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Console provides specific background tasks to purge and clean up the system with regard to processed flowsheet data and legacy CP studies.

## Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new CP Gateway Service is a service that allows patient monitoring devices to send observational data to VistA.

## List of Outstanding Anomalies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A Request for Concurrence to Release Software with Known Anomalies was submitted containing the following anomalies:

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 22%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Headline/Description</strong></th>
<th><strong>Severity</strong></th>
<th><strong>Priority</strong></th>
<th><strong>Application</strong></th>
<th><p><strong>Workaround/</strong></p>
<p><strong>Comments</strong></p></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CQ580</td>
<td>The general comment given when entering Flowsheet data (shown on same line as location) does not appear on any reports.</td>
<td>Low</td>
<td>Low</td>
<td>CP Flowsheet GUI</td>
<td>User will be advised via training not to use the comment field. Severity Level low determined via discussion of defect with stakeholders and test sites. The design was to document process flow and not actual measurements.</td>
<td><blockquote>
<p>Designated to patch 23</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CQ681</td>
<td>Auto Refresh not working.</td>
<td>Low</td>
<td>Low</td>
<td>CP Flowsheets GUI</td>
<td><p>Impact is minimal because there is no user setting to apply an auto refresh, so users are unaware of the option. Functionality taken away due to system constraints on other functionality and development time needed to analyze functionality further. Training and User</p>
<p>Manual reflect the use of the Manual.</p></td>
<td><blockquote>
<p>Designated to patch 23</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CQ705</td>
<td>Not all of the Column Headings match up with the selections in the Add Data screen of Flowsheets view</td>
<td>Low</td>
<td>Low</td>
<td>CP Flowsheets GUI</td>
<td><p>Impact is minimal as it is not always noticeable by everyone. Training will point out the anomaly. This is only one screen and the information for the column selections is very</p>
<p>distinguishable from one column to the next.</p></td>
<td><blockquote>
<p>Designated to patch 23</p>
</blockquote></td>
</tr>
</tbody>
</table>

### From: MD*1*12 Release Notes (CP Flowsheets)

## Support HL7 ADT Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CP Flowsheets introduced an Admission Discharge and Transfer (ADT) Health Level 7 (HL7) message feed. This ADT feed monitors the admitted, discharged, and transferred events from the Patient Information Management System (PIMS) and notifies interested patient medical monitoring devices via HL7 version 2.4 messages. Patch MD\*1.0\*12 provides HL7 messaging apparatus that eliminates CP Flowsheets' dependency on VDEF. There are occasions during a PIMS ADT discharge/cancel discharge events when room/bed information is not provided. With the support of patch MD\*1.0\*12, CP Flowsheets will transmit ADT discharge (A03)/cancel discharge (A13) messages when those events are triggered by PIMS inpatient activity when there is no room/bed information supplied.

## Support Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Following the release of MD\*1.0\*12, users will enter a Remedy Ticket or contact the VA Service Desk (VASD) directly when a problem arises. Once a Remedy Ticket is logged to the appropriate Category Type and Item either by the site themselves or Tier 1 support(VASD), the appropriate team will receive a Remedy alert. The Tier 2 (Product Support) support specialist assigned to the ticket will contact the site to troubleshoot and resolve the problem. If unable to do so, the ticket is referred to the Tier 3 group MNT-CP or DEV-CP for technical assistance.

> Maintenance priority is a required field to be selected by Tier 2 upon referral. They include:

- Priority 1 – Patient Safety Adversely Affected
- Priority 2 – Logging Software Error, Functionality Essential
- Priority 3 – Systems/Resource Issue
- Priority 4 – Patient Personally Affected
- Priority 5 – Logging Software Error, Functionality Needed
- Priority 6 – Functionality called into question
- Priority 7 – External Database Interface Issue
- Priority 8 – Nuisance Problem, Work Around in Place
- Priority 9 – Miscellaneous/Housekeeping

> Any referred Remedy tickets will be returned to the Tier 2 support for closure by the release coordinator of the resolving patch or original support specialist if a patch is not involved.

> Clinical Procedures MD\*1.0\*12, Clinical Flowsheet, tickets will be received by the Clinical 3 Product Support Team (Clin3). The tickets will be logged under:

- Category: Application-Vista
- Type: Clinical Procedures 1.0
- Item: Clinical Flowsheets

> Product Support maintains four fully patched support accounts which includes the Clinical Procedures application and will be used by Clin3 to troubleshoot flowsheet issues in a non- production environment.

> *This page intentionally left blank for double-sided printing.*
