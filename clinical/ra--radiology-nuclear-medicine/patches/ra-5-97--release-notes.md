---
title: RA*5*97 Release Note
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Release Note
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5*97
group_key: "RA:RA:5"
file_numbers: []
security_keys: []
menu_options: 0
description: Patch RA\5.0\97 exports ten diagnostic codes into the DIAGNOSTIC CODES file (#78.3); seven BI-RADS codes and three AAA codes. These codes are assigned internal record numbers (IENs) 1100-1106 and 1200-1202, respectively.
audience: 
keywords: 
  - diagnostic
  - rads
  - codes
  - patch
  - report
  - code
  - table
  - contents
  - category
  - radiology
page_count: 0
word_count: 2527
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p97.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p97.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

![](ra-5-97-release-note/001.png)

Radiology/Nuclear Medicine  
Release Notes

Patch RA\*5.0\*97  
August 2009

Health Systems Design & Development

Provider Systems

# Release Notes for Patch RA\*5.0\*97


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes for Patch RA\5.0\97](#release-notes-for-patch-ra5097)
  - [Overview](#overview)
  - [General Installation Notes](#general-installation-notes)
  - [Specific Installation Notes](#specific-installation-notes)
- [Patch RA\5.0\97 Enhancement Features](#patch-ra5097-enhancement-features)
- [Patch RA\5.0\97 Maintenance Features](#patch-ra5097-maintenance-features)
- [Components in Patch RA\5.0\97 from the Host File](#components-in-patch-ra5097-from-the-host-file)
  - [Files and Fields](#files-and-fields)
  - [## Routines New and Modified](#routines-new-and-modified)
  - [Post Installation](#post-installation)
- [Notes from the Radiology Program Office](#notes-from-the-radiology-program-office)
Patch RA\*5.0\*97 is an enhancement patch that provides for the entering of Breast Imaging Reporting and Data System (BI-RADS™) codes from mammogram studies and for the entering of Abdominal Aortic Aneurysm (AAA) codes into the Primary or Secondary Diagnostic Code fields.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RA\*5.0\*97 exports ten diagnostic codes into the DIAGNOSTIC CODES file (#78.3); seven BI-RADS codes and three AAA codes. These codes are assigned internal record numbers (IENs) 1100-1106 and 1200-1202, respectively.

After the ten codes are added to the DIAGNOSTIC CODES file (#78.3), users of the VistA Radiology/Nuclear Medicine 5.0 package can enter them into Primary or Secondary Diagnostic Code fields. Certain codes will trigger alerts for the cases with those codes and cause the cases to display on the Abnormal Diagnostic Report.

## General Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Patch RA\*5\*97 is released with LEX\*2\*55 in a host file.
- Patches RA\*5\*70, RA\*5\*85, RA\*5\*95, and LEX\*2\*55 must be installed before Patch RA\*5\*97. Patch LEX\*2\*55 comes with the host file.
- LEX\*2.0\*55 must be the first patch in the host file, because during the installation it provides the APIs needed by Patch RA\*5.0\*97. Those APIs are used to add the BI-RADS records to the DIAGNOSTIC CODES file (#78.3), using the Mammography Quality Standards Act of 1992 (MQSA) coding system.

## Specific Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LEX\*2.0\*55 is the first patch in the host file and Patch RA\*5.0\*97 is the second patch.

- The instructions for installing the host file, LEX_RA_BIRADS_97.KID, are only in the patch description for LEX\*2\*55; refer to the Forum NPM for LEX\*2\*55.
- All Radiology users must be off the system during installation, because Patch 97 adds data to the DIAGNOSTIC CODES file (#78.3) and changes APIs.

# Patch RA\*5.0\*97 Enhancement Features 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Patch RA\*5.0\*97 adds BI-RADS codes to the DIAGNOSTIC CODES file (#78.3), using internal entry numbers (IENs) 1100 through 1106.

> The MQSA coding text associated with a BI-RADS code is displayed wherever BI-RADS codes are displayed.

- File lookup of DIAGNOSTIC CODES file (#78.3)
- The Radiology interpreted reports under the ‘Films Reporting Menu’
- Display a Rad/Nuc Med Report \[RA RPTDISP\]
- Draft Report (Reprint) \[RA REPRINT\]
- Select Report to Print by Patient \[RA RPTPAT\]
- The Radiology interpreted report in the Report tab of CPRS
- The Vista email that is sent to the requesting physician when a report is verified

> Example of the lookup of BI-RADS from the DIAGNOSTIC CODES file (#78.3) and the display of MQSA coding text (in parentheses)

PRIMARY DIAGNOSTIC CODE: ??

. . . . .

Choose from:

1 NORMAL

. . . .

1100 BI-RADS CATEGORY 0 (Incomplete: Need Additional Imaging  
Evaluation)

1101 BI-RADS CATEGORY 1 (Negative)

1102 BI-RADS CATEGORY 2 (Benign)

1103 BI-RADS CATEGORY 3 (Probably Benign)

1104 BI-RADS CATEGORY 4 (Suspicious)

1105 BI-RADS CATEGORY 5 (Highly Suggestive of Malignancy)

1106 BI-RADS CATEGORY 6 (Known Biopsy Proven Malignancy)

2.  RA\*5.0\*97 adds AAA codes to the DIAGNOSTIC CODES file (#78.3), using IENs 1200 through 1202.

> Example of the lookup of AAA codes from the DIAGNOSTIC CODES file (#78.3) and the display of the Description (in parentheses)

PRIMARY DIAGNOSTIC CODE: ??

. . . . .

Choose from:

1 NORMAL

. . . .

1200 ABDOMINAL AORTIC ANEURYSM NOT PRESENT (The maximum width of the  
infrarenal aorta is less than three centimeters.)

1201 ABDOMINAL AORTIC ANEURYSM PRESENT (The maximum width of the  
infrarenal aorta is at least three centimeters.)

1202 DOES NOT SATISFY SCREEN FOR AAA (Exam is not technically  
adequate for AAA screening.)

3.  The ‘Outside Report Entry/Edit’ \[RA OUTSIDE RPTENTRY\] option was updated to check whether or not a BI-RADS diagnostic code is required for Electronically Filed reports.
- When a required BI-RADS code is missing, a warning message displays.
- The requirement for a BI-RADS diagnostic code is determined from the data in the RADIOLOGY CPT BY PROCEDURE TYPE file (#73.2), which is updated annually by a Radiology patch with data supplied by Sherrill Snuggs from the Program Office.
- The following fields from file (#73.2) are used to determine if a BI-RADS diagnostic code is required for an Electronically Filed report. All conditions must be met for the code to be required.
1.  The CPT code of the procedure is a record in the RADIOLOGY CPT BY PROCEDURE TYPE file (#73.2).
2.  Field \#3, PROCEDURE SUBCATEGORY of this record is IMAGING.
3.  Field \#4, RVU PROCEDURE TYPE of this record is MAMMOGRAPHY.
4.  Field \#8, BIRADS PROCEDURE of this record is YES.
4.  The ‘Delinquent Status Report’ \[RA DELINQUENT\] option was updated to display the Electronically Filed report status.
- Prior to Patch RA\*5.0\*97, No Report displayed for a report entered via the ‘Outside Report Entry/Edit’ \[RA OUTSIDE RPTENTRY\], where the exam status did not reach COMPLETE because of missing BI-RADS data.
- A screen pause is added at the end of the last screen, so the display will not scroll off the screen.
5.  The ‘Diagnostic Code and Interpreter Edit by Case No.’ \[RA DIAGCN\] option was updated to disallow the use of this option when:
1.  a case does not yet have a report, or
2.  a case has a stub report (a record made in file (#74) to link a case to an image, but the record has neither report text nor impression), or
3.  a case has an electronically filed report.
6.  The ‘Abnormal Exam Report’ \[RA ABNORMAL\] option was updated to allow the user to select data by VA radiologist only, Electronically Filed only, or both.
- If a case does not yet have a report, the case will be included in all selections.
- If the abnormal diagnosis code is one of the BI-RADS codes, the text of the MQSA coding system displays beneath the BI-RADS code.
- An issue, a case \# had two abnormal diagnostic codes, found during development testing was corrected. The case \# displayed under the first abnormal diagnostic code, but not under the second, because it was the last case with the first abnormal diagnostic code and the first case with the second abnormal diagnostic code.

# Patch RA\*5.0\*97 Maintenance Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Routine RABWORD1 is modified to use Lexicon APIs instead of reading directly from Lexicon fields that are scheduled for deletion.
- Routine RABWORD1 uses the Lexicon API, \$\$ICDDX^ICDCODE, to retrieve ICD9 ordering diagnoses.
- This change affects the sending of ICD9 ordering diagnoses from Vista Radiology to CPRS, when an order is placed through Vista Radiology (back door) and the CIDC switch is turned on.
7.  Two print templates, RA IMAGE LOC LIST and RA PROCEDURE LIST, are modified to use Lexicon APIs instead of reading directly from Lexicon fields that are scheduled for deletion.  
    The print templates use the Lexicon API, \$\$MOD^ICPTMOD, to retrieve CPT Modifiers when displayed from these options.
- Location Parameter List \[RA SYSLOCLIST\]
- Active Procedure List (Long) \[RA PROCLONG\]
- Inactive Procedure List (Long) \[RA INACPRCLONG\]
- Series of Procedures List \[RA PROCSERIES\]
8.  Patch RA\*5.0\*97 addresses Remedy tickets 325445 and 324541 - *The 'Outside Report Entry/Edit' option doesn't generate an "Imaging Results" alert in CPRS*.  
    Routine RARTE7 is modified to generate an *Imaging Results, Non Critical* alert when an outside report is entered for the first time, even though the report does not include an abnormal diagnostic code.

# Components in Patch RA\*5.0\*97 from the Host File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files and fields are included in patch RA\*5.0\*97.

| File | Field \# | New Field ? | Field Name  |
|----------|--------------|-----------------|-----------------|
| 78.3     | .001         |                 | Number          |
| 78.3     | .01          |                 | Diagnostic Code |
| 78.3     | .6           | Yes             | Expression      |

## ## Routines New and Modified 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These following routines are in Patch RA\*5\*97, which is the second patch in the host file, LEX_RA_BIRADS_97.KID.

| RA97PST  | RAEDCN   | RART   |
|----------|----------|--------|
| RA97PST1 | RAO7PC2  | RARTE5 |
| RABIRAD  | RAPRINT  | RARTE7 |
| RABWORD1 | RAPRINT1 | RARTR1 |
| RADLQ1   |          |        |

## Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  For sites that will use the exported BI-RADS and AAA codes from Voice Recognition (VR) systems, such as PowerScribe or TalkStation, the VR systems manager must add the BI-RADS and AAA codes exported from Patch RA\*5\*97 into the diagnostic file of the VR system. The exported BI-RADS and AAA field values are described in item 2.  
      
    It is known that PowerScribe has an inactivation feature and TalkStation does not. For sites that will not use the exported BI-RADS and AAA codes from VR systems with the inactivation feature, the VR systems manager can add the exported codes into the diagnostic file of the VR system and inactivate the codes. This keeps the diagnostic codes in VistA in sync with the diagnostic codes on the VR system.
9.  The post installation routines (RA97PST and RA97PST1) add the following records to the DIAGNOSTIC CODES file (#78.3).

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 21%" />
<col style="width: 26%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field .001</strong></th>
<th><strong><br />
Field .01</strong></th>
<th><strong><br />
Field 2</strong></th>
<th><strong><br />
Field 3</strong></th>
<th><strong><br />
Field 4</strong></th>
<th><strong>Field 6 (New)<br />
(Display Value)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1100</td>
<td>BI-RADS CATEGORY 0</td>
<td>Incomplete: Need Additional Imaging Evaluation</td>
<td>Y</td>
<td>y</td>
<td>Incomplete: Need Additional Imaging Evaluation</td>
</tr>
<tr class="even">
<td>1101</td>
<td>BI-RADS CATEGORY 1</td>
<td>Negative</td>
<td>N</td>
<td>n</td>
<td>Negative</td>
</tr>
<tr class="odd">
<td>1102</td>
<td>BI-RADS CATEGORY 2</td>
<td>Benign</td>
<td>N</td>
<td>n</td>
<td>Benign</td>
</tr>
<tr class="even">
<td>1103</td>
<td>BI-RADS CATEGORY 3</td>
<td>Probably Benign</td>
<td>Y</td>
<td>y</td>
<td>Probably Benign</td>
</tr>
<tr class="odd">
<td>1104</td>
<td>BI-RADS CATEGORY 4</td>
<td>Suspicious</td>
<td>Y</td>
<td>y</td>
<td>Suspicious</td>
</tr>
<tr class="even">
<td>1105</td>
<td>BI-RADS CATEGORY 5</td>
<td>Highly Suggestive of Malignancy</td>
<td>Y</td>
<td>y</td>
<td>Highly Suggestive of Malignancy</td>
</tr>
<tr class="odd">
<td>1106</td>
<td>BI-RADS CATEGORY 6</td>
<td>Known Biopsy Proven Malignancy</td>
<td>Y</td>
<td>y</td>
<td>Known Biopsy Proven Malignancy</td>
</tr>
<tr class="even">
<td>1200</td>
<td>ABDOMINAL AORTIC ANEURYSM NOT PRESENT</td>
<td>The maximum width of the infrarenal aorta is less than three centimeters.</td>
<td>N</td>
<td>n</td>
<td></td>
</tr>
<tr class="odd">
<td>1201</td>
<td>ABDOMINAL AORTIC ANEURYSM PRESENT</td>
<td>The maximum width of the infrarenal aorta is at least three centimeters.</td>
<td>Y</td>
<td>y</td>
<td></td>
</tr>
<tr class="even">
<td>1202</td>
<td>DOES NOT SATISFY SCREEN FOR AAA</td>
<td>Exam is not technically adequate for AAA screening.</td>
<td>N</td>
<td>n</td>
<td></td>
</tr>
</tbody>
</table>

- If your site already has data in the ranges 1100-1106 and/or 1200-1202, the post installation does not add any of the ten records to the DIAGNOSTIC CODES file (#78.3); instead, two email messages are sent by the Postmaster.
1.  One message is a VistA mail message to the IRM staff that installed this patch.

> Example

> Subj: DIAGNOSTIC CODES file IEN issue @ HINES ISC \[#87895\] 05/05/09@12:16 2 lines

> From: POSTMASTER In 'IN' basket. Page 1

> ------------------------------------------------------------------

> HINES ISC has a conflict with one or more IENS in file 78.3,

> DIAGNOSTIC CODES, in the range 1100-1106 and 1200-1202.

> Enter message action (in IN basket): Ignore//

5.  Second message is an Outlook message to the VA OIT VHIT Radiology Facility Level Application Issues mail group.

> Example

> From: POSTMASTER@TST.DEV.FO-HINES.MED.VA.GOV

> Sent: Thursday, May 05, 2009 12:16 AM

> To: VA OIT VHIT Radiology Facility Level Application Issues

> Subject: DIAGNOSTIC CODES file IEN issue @ HINES ISC

> HINES ISC has a conflict with one or more IENS in file 78.3,

> DIAGNOSTIC CODES, in the range 1100-1106 and 1200-1202.

- If your site does not have data in the ranges 1100-1106 and/or 1200-1202, the post installation displays a success message on the installation screen and resets the third piece of the RA file to the highest IEN under 999.

\*\*\* 10 of 10 BI-RADS and Abdominal Aortic Aneurysm codes

have been successfully added to the DIAGNOSTIC CODES file \#78.3. \*\*\*

10. The description of the diagnostic code from the ‘Diagnostic Code List’ \[RA DIAGP\] option is taken from the Description field of the DIAGNOSTIC CODES file (#78.3). But the MQSA coding system’s text of BI-RADS from the following options and features is taken from the EXPRESSIONS file (#757.01) of the Lexicon application:
- ‘Display a Rad/Nuc Med Report’ \[RA RPTDISP\]
- ‘Draft Report (Reprint)’ \[RA REPRINT\]
- ‘Select Report to Print by Patient’ \[RA RPTPAT\]
- CPRS Report tab
- Email message of a verified report sent to the requester

> The description and the MQSA coding system’s text from the options will remain identical as long as there are no local changes made to the Description field in the DIAGNOSTIC CODES file (#78.3) or national changes made to the Displayable Text field in the EXPRESSIONS file (#757.01).

# Notes from the Radiology Program Office

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In addition to BI-RADS and AAA diagnostic codes, a radiologist can enter local diagnostic codes. 

> Example  
> If the aorta is normal on a screening ultrasound study, but a liver mass is identified, a radiologist can enter both the code for AAA not present and for significant abnormality. 

> If a hospital created its own BI-RADS and AAA diagnostic codes, the hospital must stop using the local codes and begin using the national codes.

#### BI-RADS Codes

2.  The Radiology Program Office will write and distribute a short educational sheet to aid physicians in identifying the BI-RADS assessment category and corresponding BI-RADS code.
3.  Entry of a diagnostic code for mammograms that corresponds to the BI-RADS assessment category will be mandatory. 
- This requirement applies to mammograms performed in-house and to mammograms performed on contract or Fee Basis. 
- The requirement to use the BI-RADS codes will be published in an upcoming VHA Mammography Handbook. 
- The reason for this requirement is to ensure tracking of mammographic screening and for the follow-up of abnormal results. 

> The Principle Deputy Under Secretary for Health has determined that mammographic screening of veterans lags behind the private sector.

- He has asked for a national registry of women veterans to better identify which patients are screened and to ensure that prompt follow-up is made. 
- The diagnostic codes entered with the mammographic report will automatically populate the future women’s health registry. 

> **NOTE:** Because the FDA mandates that a BI-RADS assessment be indicated on every report, all outside reports will specify an assessment category.

11. When writing in-house mammographic reports, a radiologist must include the FDA mandated BI-RADS assessment language in the impression of the report, as well as enter the corresponding BI-RADS diagnostic code.
12. When a radiologist is tasked with the duty of reading outside mammographic reports and of determining the BI-RADS assessment code.
1.  It is recommended that the radiologist write the code on the hardcopy report with a signature next it, and
4.  The radiologist must be given DSS labor mapping administrative time by the service chief, so this duty does not detract from the clinical productivity calculation. 

#### AAA Codes

13. It is the policy of the VA to screen all men, age 65 to 75 who have ever smoked, for the presence of an Abdominal Aortic Aneurysm (AAA). 
- In order to coordinate this effort, a clinical reminder was written that displays whenever a patient visits a clinic. 
- When a successful AAA diagnostic code is entered, the reminder is removed and the clinician is no longer prompted to order a screening exam.
14. The AAA diagnostic code must be entered when reporting a study, which was ordered to rule out an AAA. The code can be entered for any study (US, CT, MR) that includes the infrarenal aorta.
- A code indicating an aneurysm is not present, must not be entered for conventional angiography because the outer wall of the aorta cannot be seen. 
- Mural thrombus and variations in geometric projection make conventional angiography unsuitable to rule out an AAA, but it can be used to rule in an AAA. 
- If a study is ordered to rule out an AAA, and a prior study (US, CT or MR) was performed after the patient was 60 years of age that adequately evaluated the aorta, the radiologist can amend the prior study to add an AAA diagnostic code, thereby eliminating the need for the screening study.
15. In addition to entering an AAA diagnostic code, a radiologist must mention the aorta in the text of the report, as has always been done.