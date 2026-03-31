---
title: PSB*3*47 PSS*1*141 BCMA Version 3 Release Notes - Immunizations
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: PSS*1*141 BCMA Version 3  - Immunizations
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
  - table
  - contents
  - code
  - medication
  - administration
  - introduction
  - features
  - example
  - manager
  - modifications
page_count: 0
word_count: 101
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p47_pss_1_p141_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p47_pss_1_p141_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

> ![](psb-3-47-pss-1-141-bcma-version-3-release-notes-immunizations/001.png)

IMMUNIZATIONS DOCUMENTATION BY BAR CODE MEDICATION ADMINISTRATION (BCMA)

> PSB\*3\*47 AND PSS\*1\*141 RELEASE NOTES

> October 2009

#### Department of Veterans Affairs Office of Enterprise Development

> October 2009 Immunizations Documentation by BCMA i

> Release Notes PSB\*3\*47 and PSS\*1\*141

#### (This page included for two-sided copying.)

> ii Immunizations Documentation by BCMA October 2009 Release Notes

> PSB\*3\*47 and PSS\*1\*141

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [New Features](#new-features)
    - [Example: Bar Code Medication Administration Manager \[PSB MGR\] Menu](#example-bar-code-medication-administration-manager-psb-mgr-menu)
  - [Modifications](#modifications)
> This document provides a description of changes introduced by the Immunizations Documentation by Bar Code Medication Administration (BCMA) application in patches PSB\*3\*47 and PSS\*1\*141.
> All sites should install these patches, even if they are currently using the BCMA2PCE Class III application. Additionally, all sites are expected to install the patches to their production VistA system. Implementation of the new features, which includes mapping relationships between the PHARMACY ORDERABLE ITEM file (#50.7) and IMMUNIZATION file (#9999999.14) may be performed at the discretion of the local facility.
> Patch PSS\*1\*141 should be installed first, as it is required by patch PSB\*3\*47.

## New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PSB\*3\*47 adds the *Immunizations Documentation by BCMA Nightly Task* \[PSB PX BCMA2PCE TASK\] option to the *Bar Code Medication Administration Manager* \[PSB MGR\] menu. You can use this option to run a task which will create a record within Patient Care Encounter (PCE) for medications marked as given in BCMA that have been identified as immunizations. The primary intended use of this option is to queue it as a nightly background task, which will process the previous day’s BCMA administrations of immunizations.

### Example: Bar Code Medication Administration Manager \[PSB MGR\] Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Effective with PSB\*3\*47, the Patient Care Encounter (PCE) V.1.0 application is added to the list of required packages necessary for BCMA to be fully functional. See the External Relationships section of the PSB\*3\*47 and PSS\*1\*141 Installation Guide for additional detail.

> October 2009 Immunizations Documentation by BCMA 1

> Release Notes PSB\*3\*47 and PSS\*1\*141

## Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PSS\*1\*141 adds the ASSOCIATED IMMUNIZATION field (#9) to the PHARMACY ORDERABLE ITEM file (#50.7). A mapping relationship is created between the PHARMACY ORDERABLE ITEM file (#50.7) and the pointed-to immunization so that a record can be created in the V IMMUNIZATION file (#9000010.11) corresponding to the BCMA administration of an immunization.

> Using the modified *Edit Orderable Items* \[PSS EDIT ORDERABLE ITEMS\] option that is installed with patch PSS\*1\*141, you can create relationships between a given orderable item (e.g., INFLUENZA INJ) and an immunization (e.g., INFLUENZA). These relationships will also be seen in the *Dispense Drug/Orderable Item Maintenance* \[PSS MAINTAIN ORDERABLE ITEMS\] option. Both options appear on the *Orderable Item Management* \[PSS ORDERABLE ITEM MANAGEMENT\] menu.

> Select Orderable Item Management Option: EDIT Orderable Items

> This option enables you to edit Orderable Item names, Formulary status, drug text, Inactive Dates, and Synonyms.

> Select PHARMACY ORDERABLE ITEM NAME: INFLUENZA INFLUENZA INJ

> Orderable Item -\> INFLUENZA Dosage Form -\> INJ

> List all Drugs/Additives/Solutions tied to this Orderable Item? YES// \<Enter\>

> Orderable Item -\> INFLUENZA Dosage Form -\> INJ

> Dispense Drugs:

> INFLUENZA VACCINE

> Are you sure you want to edit this Orderable Item? NO// YES

> Now editing Orderable Item: INFLUENZA INJ

> Orderable Item Name: INFLUENZA// \<Enter\>

> This Orderable Item is Formulary.

> This Orderable Item is marked as a Non-VA Med. Select OI-DRUG TEXT ENTRY: \<Enter\>

> INACTIVE DATE: \<Enter\>

> DAY (nD) or DOSE (nL) LIMIT: \<Enter\>

> MED ROUTE: \<Enter\> SCHEDULE TYPE: \<Enter\> SCHEDULE: \<Enter\>

> PATIENT INSTRUCTIONS: \<Enter\>

> Note: The ASSOCIATED

> IMMUNIZATION field (#9) is only presented when at least one of the dispense drugs tied to the selected orderable item is in a VA Drug Class in the IM100 to IM900 range.

> Immunizations are typically found in VA Drug Classes IM100, IM105, IM109, IM700 or IM900.

> ASSOCIATED IMMUNIZATION: INFLUENZA FLU,3 YRS INFLUENZA

> Select SYNONYM: \<Enter\>

> 2 Immunizations Documentation by BCMA October 2009 Release Notes

> PSB\*3\*47 and PSS\*1\*141