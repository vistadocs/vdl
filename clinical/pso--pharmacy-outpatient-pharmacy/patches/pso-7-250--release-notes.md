---
title: PSO*7*250/258 FY07 Qtr 1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: FY07 Qtr 1
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*250
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - quantity
  - pharmacy
  - outpatient
  - patch
  - profile
  - patient
  - calculated
  - action
page_count: 0
word_count: 685
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p258_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p258_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](pso-7-250-258-fy07-qtr-1-release-notes/001.png)

Pharmacy FY07 Q1

Release Notes

PSO\*7\*258

PSO\*7\*250

December 2006

VistA Health Systems Design & Development
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Outpatient Pharmacy V. 7.0](#outpatient-pharmacy-v-70)
- [Option Updates](#option-updates)
- [Defect Fixes](#defect-fixes)
  - [Calculated Quantities of Clozapine](#calculated-quantities-of-clozapine)
  - [Updates Related to PSO\7\233](#updates-related-to-pso7233)
The Pharmacy Fiscal Year 2007 Quarter 1 (FY07 Q1) release includes two patches for the Outpatient Pharmacy V. 7.0 package. These patches include software enhancements and defect fixes.
The FY07 Q1 release includes the following software patches:
- Outpatient Pharmacy V. 7.0
  - PSO\*7\*250
  - PSO\*7\*258
For installation instructions, see the patch description for the appropriate package.
*(This page included for two-sided copying.)*

# Outpatient Pharmacy V. 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy V. 7.0 is updated for the FY07 Q1 release with these two patches: PSO\*7\*250 and PSO\*7\*258.

Patch PSO\*7\*250 is a “tally” patch; it produces a tally report in the form of a MailMan message for all prescriptions with missing expiration dates and prescriptions that are past their expiration dates but have an active status. It also contains corrections for two remedy tickets.

Patch PSO\*7\*258 contains software enhancements as well as defect fixes.

# Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are modified as described.

- Updated the *Action Profile (132 COLUMN PRINTOUT)* \[PSO ACTION PROFILE\] option and the *Medication Profile* \[PSO P\] option to print only the last four digits of the patient’s Social Security Number (SSN).
- Updated the *Action Profile (132 COLUMN PRINTOUT)* \[PSO ACTION PROFILE\] option to print the Prescription status as Active/Susp, instead of Suspended.
- Updated the *Action Profile (132 COLUMN PRINTOUT)* \[PSO ACTION PROFILE\] option to remove the reason for BAD ADDRESS INDICATED.
- Updated the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option and the *Complete Orders from OERR* \[PSO LMOE FINISH\] option to display the provider comments when the “Copy Provider Comments into the Patient Instructions?” prompt displays during the pending order finish process.

# Defect Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes were made to the Outpatient Pharmacy V. 7.0 software.

## Calculated Quantities of Clozapine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A problem was reported with the calculated quantity for the drug Clozapine during the pending order finish process. A patient safety incident (PSI-06-146) was entered. The solution provided is as follows:

If the drug has possible dosages defined, a quantity can be calculated. If this quantity is less than the quantity placed in CPRS, the calculated quantity will be displayed. Otherwise, the quantity placed in CPRS will be displayed. If there are no possible dosages defined then a quantity cannot be calculated and the message "Unable to calculate the quantity, enter a quantity" is displayed to the user in the ListMan message bar as a warning of a possible quantity issue. Since Outpatient Pharmacy might change the days supply and quantity of Clozapine orders placed in CPRS, the days supply and quantity have been added to the existing refill message.

Here is an example of an order placed in CPRS with a days supply of 60 and a quantity of 60 for a patient eligible for 28-days supply:

\(6\) Issue Date: OCT 26,2006 (7) Fill Date: OCT 27,2006

Patient Eligible for 28 Day Sup. or 14 Day with 1 refill or 7 Day

with 3 refill

\(8\) Days Supply: 28 (9) QTY (TAB): 28

Provider ordered 0 refills, days supply of 60 and a qty of 60

## Updates Related to PSO\*7\*233

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the release of patch PSO\*7\*233, some issues were identified and are being corrected in this patch:

If a hold reason of “8 (PER PATIENT REQUEST)” or “99 (OTHER--SEE COMMENTS)” was entered, the reason “7 (BAD ADDRESS)” was displayed. The reason is stored correctly, but this patch corrects the display in the following:

- “AL” action (activity log display) from within the patient profile
- *View Prescriptions* \[PSO VIEW\] option

A potential problem was identified with a function call (\$\$CHKRX^PSOBAI) that was not set up correctly. This code will probably never be used, but this patch ensures that the function call will work appropriately.