---
title: PSO*7*222 FDA Regulatory Changes for Clozapine Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: FDA Regulatory Changes for Clozapine
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*222
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - clozapine
  - results
  - table
  - drug
  - class
  - patient
  - override
  - contents
  - patch
  - changes
page_count: 0
word_count: 1245
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p222_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p222_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](pso-7-222-fda-regulatory-changes-for-clozapine-release-notes/001.png)

FDA rEGULATORY CHANGES FOR CLOZAPINE

OUTPATIENT PHARMACY

RELEASE NOTES

PSO\*7\*222

September 2006

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [New Features, Functions, and Enhancements](#new-features-functions-and-enhancements)
- [Updated Fields](#updated-fields)
- [New Messages for Clozapine Drug Selection](#new-messages-for-clozapine-drug-selection)
This document provides a brief description of enhancements required to meet revisions in the Food and Drug Administration (FDA) requirements for blood monitoring in patients being treated with Clozapine.
![](pso-7-222-fda-regulatory-changes-for-clozapine-release-notes/002.png)Note: The information referenced in this document pertaining to Clozapine dispensing functionality is available through Backdoor Pharmacy with the installation of the PSO\*7\*222 patch. Corresponding changes in the Computerized Patient Record System (CPRS) will be available as part of Patch OR\*3\*243.
![](pso-7-222-fda-regulatory-changes-for-clozapine-release-notes/003.png)Note: The PSO\*7\*222 patch is associated with the Mental Health patch YS\*5.01\*90. Patch YS\*5.01\*90 is a required patch for PSO\*7\*222.
> Successful implementation of the Mental Health patch YS\*5.01\*90 is very important for Pharmacy and CPRS. The Mental Health Clinician, with the help of the LAB ADPAC, have to ensure that the LAB tests, White Blood Count (WBC) and Absolute Neutrophil Count (ANC), are set up correctly in the Mental Health package using the CLOZAPINE MULTI TEST LINK option. Also, with the release of YS\*5.01\*90, providers must also hold the YSCL AUTHORIZED security key.

# New Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement allows for a Monthly (28-Day) supply of Clozapine for patients that meet specific criteria.

The following table displays the number of refills allowed for each range of prescription fills.

#### Clozapine Refills Allowed

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><p id="patient-status" class="heading unnumbered"><strong>Patient Status</strong></p></th>
<th><p id="maximum-prescription-fills" class="heading unnumbered"><strong>Maximum<br />
Prescription Fills</strong></p></th>
<th><p id="refills-allowed" class="heading unnumbered"><strong>Refills Allowed</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3">Monthly</td>
<td>7-Day</td>
<td>3</td>
</tr>
<tr class="even">
<td>14-Day</td>
<td>1</td>
</tr>
<tr class="odd">
<td>28-Day</td>
<td>0</td>
</tr>
<tr class="even">
<td rowspan="2">Bi-Weekly</td>
<td>7-Day</td>
<td>1</td>
</tr>
<tr class="odd">
<td>14-Day</td>
<td>0</td>
</tr>
<tr class="even">
<td>Weekly</td>
<td>7-Day</td>
<td>0</td>
</tr>
</tbody>
</table>

This Outpatient Pharmacy patch contains the following enhancements for Clozapine dispensing:

- Adjust the business rules to disallow prescription processing without override if 3500/mm3\>WBC\>3000/mm3 and 2000/mm3\>ANC\>1500/mm3. Prior to this patch, override restrictions were very lenient. Once this patch is installed, dispensing is no longer allowed if the WBC \<3000/mm3 or ANC \<1500/mm3. However, if the WBC is between 3000/mm3 and 3500/mm3 or if ANC is between 1500/mm3 and 2000/mm3, dispensing will be allowed with an overriding reason. These levels require twice weekly blood testing until the WBC stabilizes above 3500/mm3 and ANC above 2000/mm3 with no signs of infection.
- Recognize the new 28-day prescription fill status and apply the appropriate restrictions for LAB draw checks.
- Add a new field to store ANC value and require both a WBC and ANC be drawn and reported before drug dispensing is allowed.
- Prevent local users from editing the Patient Status within the Clozapine module.

# Updated Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new ANC RESULTS field (#304) is created in the PRESCRIPTION file (#52) to store the ANC value.

The REASON FOR LOCKOUT field (#4) in the CLOZAPINE PRESCRIPTION OVERRIDES file (#52.52) is changed to REASON FOR OVERRIDE field (#4). The set of codes have been modified and three new codes (5, 6, 7) were added to accommodate the override conditions for the new ANC LAB test:

- ‘1’ FOR NO WBC IN LAST 7 DAYS
- ‘2’ FOR NO VERIFIED WBC
- ‘3’ FOR LAST WBC RESULT \< 3500
- ‘4’ FOR 3 SEQ. WBC DECREASE
- ‘5’ FOR LAST ANC RESULT \< 2000
- ‘6’ FOR 3 SEQ. ANC DECREASE
- ‘7’ FOR NCCC AUTHORIZED.

# New Messages for Clozapine Drug Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Clozapine drug has been selected, the following messages have been introduced for dispensing Clozapine according to the scenarios shown in the examples below.

![](pso-7-222-fda-regulatory-changes-for-clozapine-release-notes/004.png)Note: All messages are processed through communication with Mental Health patch YS\*5.01\*90.

![](pso-7-222-fda-regulatory-changes-for-clozapine-release-notes/005.png)Note: The “NEUTROPHIL MATURITY, MEAN (ANC) results” verbiage shown in these examples is for illustration only. This can vary, depending on the site definition for ANC calculation.

Example 1: Patient not registered (not eligible) in the Clozapine program

Now doing drug interaction and allergy checks. Please wait...

Permission to dispense clozapine has been denied. Please contact the

Director of the VA National Clozapine Coordinating Center

(<span class="mark">REDACTED</span>

Example 2: Patient discontinued from the Clozapine program

Now doing drug interaction and allergy checks. Please wait...

\*\*\* This patient has been discontinued from the clozapine treatment program \*\*\*

\*\*\* and must have a new registration number assigned \*\*\*

Permission to dispense clozapine has been denied. Please contact the

Director of the VA National Clozapine Coordinating Center

<span class="mark">REDACTED</span>

Example 3: Clozapine Patient with no LAB work in the past 7 days or if labs are available which have not been entered in VistA, the site will receive the following warning

Now doing drug interaction and allergy checks. Please wait...

Permission to dispense clozapine has been denied. If the results of the latest

Lab Test drawn in the past 7 days show WBC\>3000/mm3 and ANC\>1500/mm3 and

you wish to dispense outside the FDA and VA protocol WBC/ANC limits, document

your request to Director of the VA National Clozapine Coordinating Center

<span class="mark">REDACTED</span> for a one-time override permission.

A CBC/Differential including WBC and ANC Must Be Ordered and Monitored on a

Twice weekly basis until the WBC STABILIZES above 3500/mm3 and ANC above

2000/mm3 with no signs of infection.

Also make sure that the LAB tests, WBC and ANC are set up correctly in the

Mental Health package using the CLOZAPINE MULTI TEST LINK option.

If the Patient has paper documentation to prove laboratory tests were done (for example, outside the VA system) and the results were within accepted limits, the NCCC can authorize a onetime override. After the NCCC has received and approved this documentation, the following message will display.

Example 4: Onetime override authorized by NCCC

Now doing drug interaction and allergy checks. Please wait...

Permission to dispense clozapine has been authorized by NCCC

Override reason being: NCCC AUTHORIZED

Do you want to override and issue this prescription? N//

Example 5: When the Patient’s WBC \<3500 (range 3000 to 3500 for overriding)

Now doing drug interaction and allergy checks. Please wait...

\*\*\* Most recent WBC and NEUTROPHIL MATURITY, MEAN (ANC) results \*\*\*

performed on JUL 27,2006 are:

WBC: 3100

ANC: 1900

\*\*\* Last Four WBC and ANC results were:

WBC ANC

05/20/2006@14:53 Results: 4900 - 2800

05/27/2006@14:53 Results: 1900 - 2500

06/27/2006@14:53 Results: 3900 - 2500

07/27/2006@15:06 Results: 3100 – 1900

Override reason being: LAST WBC RESULT \< 3500

![](pso-7-222-fda-regulatory-changes-for-clozapine-release-notes/006.png)Note: Up to four of the last LAB results can be displayed in the message.

Example 6: When the Patient’s WBC is above range but ANC \<2000 (range 1500 to 2000 for overriding)

Now doing drug interaction and allergy checks. Please wait...

\*\*\* Most recent WBC and NEUTROPHIL MATURITY, MEAN (ANC) results \*\*\*

performed on JUL 26,2006 are:

WBC: 3900

ANC: 1900

\*\*\* No previous results to display \*\*\*

Override reason being: LAST ANC RESULT \< 2000

Do you want to override and issue this prescription? N//

![](pso-7-222-fda-regulatory-changes-for-clozapine-release-notes/007.png)Note: In Example 6, previous LAB results did not exist.

Example 7: Patient meets all criteria

Now doing drug interaction and allergy checks. Please wait...

\*\*\* Most recent WBC and NEUTROPHIL MATURITY, MEAN (ANC) results \*\*\*

performed on JUL 27,2006 are:

WBC: 3900

ANC: 2000

CLOZAPINE dosage (mg/day) ? : (12.5-3000):