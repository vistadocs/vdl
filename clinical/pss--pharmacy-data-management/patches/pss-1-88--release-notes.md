---
title: PSS*1*88 Release Notes - Medication Route Changes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Medication Route Changes
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*88
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - medication
  - route
  - bcma
  - changes
  - table
  - contents
  - patch
  - routes
  - prompt
  - order
page_count: 0
word_count: 747
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p88_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p88_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

![](pss-1-88-release-notes-medication-route-changes/001.png)

medication route changes

Release Notes

PSS\*1\*88

PSJ\*5\*159

PSB\*3\*38

July 2007

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pharmacy Data Management Changes](#pharmacy-data-management-changes)
    - [Post-Install Routine](#post-install-routine)
- [Medication Route Changes](#medication-route-changes)
- [Inpatient Medications Changes](#inpatient-medications-changes)
There have been several patient safety incidents (PSI) reported that revolved around Medication Route information. This series of patches is designed to address the issue of the Medication Route being blank on the Bar Code Medication Administration (BCMA) Virtual Due List (VDL).
In order to correct this problem, the decision was made to always display the full medication route, rather than only an abbreviation, on the VDL and the Order Detail. During research for this PSI, it was determined that another issue existed with the Medication Route abbreviation. The decision on whether or not to prompt for an injection was based on a certain combination of characters being contained in the Medication Route abbreviation. These patches also address this issue.
Three patches work together to perform these tasks.
- Patch PSS\*1\*88 adds a prompt to the PSS MEDICATION ROUTES input template. A new field (#8), PROMPT FOR INJ. SITE IN BCMA, is added to the MEDICATION ROUTES file (#51.2).
- Patch PSJ\*5\*159 sends the value of this new field to BCMA, as well as adding the Medication Route full name to both of the BCMA Application Programming Interfaces (API)s.
- Patch PSB\*3\*38 uses this new information to display full name on the VDL and order detail. In addition, it uses the new information supplied to prompt for an injection site.
*(This page included for two-sided copying.)*

# Pharmacy Data Management Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*88 adds prompts for an injection site in Bar Code Medication Administration (BCMA) and for displaying the IVP/IVPB tab in BCMA. The screen below illustrates these prompts:

Select OPTION NAME: PSS MEDICATION ROUTES EDIT Medication Route File Enter/Edit

Medication Route File Enter/Edit

Select MEDICATION ROUTES NAME: INTRAVE

1 INTRAVENOUS IV

2 INTRAVENOUS INFILTRATION MISCELLANEOUS IV IF MISC

3 INTRAVENOUS INH MISC IV INH MISC

4 INTRAVENOUS INHALATION MISCELLANEOUS IV INH MISC

5 INTRAVENOUS INTRA-ARTERIAL IV IAER

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 INTRAVENOUS IV

NAME: INTRAVENOUS//

ABBREVIATION: IV//

PACKAGE USE: ALL PACKAGES//

OUTPATIENT EXPANSION:

OTHER LANGUAGE EXPANSION:

IV FLAG: YES//

PROMPT FOR INJ. SITE IN BCMA: //

DSPLY ON IVP/IVPB TAB IN BCMA? //

There is no default for these two new prompts. Responses can be:

- NO or 0
- YES or 1

### Post-Install Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to assist the Pharmacy staff with the updating of the new field, a post-install routine has been added to the PSS\*1\*88 patch. This routine will search for all medication routes that contain IV, SC, IM or … in the ABBREVIATION field (#1) of the MEDICATION ROUTES file (#51.2).

The list of medication routes is sent to the person installing the patch. The message should be forwarded to the appropriate Pharmacy personnel.

*(This page included for two-sided copying.)*

# Medication Route Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the installation of Patch PSB\*3\*38, the Coversheet display in BCMA now looks as illustrated below.

![](pss-1-88-release-notes-medication-route-changes/002.png)

With the installation of Patch PSB\*3\*38, the Virtual Due List display in BCMA now looks as illustrated below.

![](pss-1-88-release-notes-medication-route-changes/003.png)

With the installation of Patch PSB\*3\*38, the Order Detail display in BCMA now looks as illustrated below.

![](pss-1-88-release-notes-medication-route-changes/004.png)

*(This page included for two-sided copying.)*

# Inpatient Medications Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*88 adds the PROMPT FOR INJ. SITE IN BCMA field (#8) to the MEDICATION ROUTES file (#51.2).

PSS\*1\*88 also adds the prompt DSPLY ON IVP/IVPB TAB IN BCMA? field (#9) to the MEDICATION ROUTES file (#51.2).

Patch PSJ\*5\*159 adds two new items to the Application Programming Interface (API) from Inpatient Medications V. 5.0 to BCMA. The NAME field (#.01) and the PROMPT FOR INJ. SITE IN BCMA field (#8) from the MEDICATION ROUTES file (#51.2) are now sent in both the PSJBCMA and PSJBCMA1 APIs.

PSJ\*5\*159 also corrects a problem found with the API that determines whether or not a STAT order notification should be sent on an Inpatient Meds order.  
 

> **NOTE:** Once you have installed this patch, if you want the “STAT icon” in BCMA to function properly, you will need to define the parameter PRIORITIES FOR ACTIVE NOTIFY in the Systems Parameters in Inpatient Meds. However, you do not need to set up pagers, email, etc.

*(This page included for two-sided copying.)*