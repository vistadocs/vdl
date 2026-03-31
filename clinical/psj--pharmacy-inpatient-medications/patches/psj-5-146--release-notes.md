---
title: PSJ*5*146 Release Notes-Remote Data Interoperability Project
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Remote Data Interoperability Project
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*146
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - order
  - remote
  - outpatient
  - drug
  - checks
  - table
  - contents
  - medications
  - inpatient
  - project
page_count: 0
word_count: 1266
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_pso_7_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_pso_7_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](psj-5-146-release-notes-remote-data-interoperability-project/001.png)

Remote Data Interoperability (RDI)

####### RELEASE NOTES 

PSJ\*5\*146

PSO\*7\*207

December 2005

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Project Overview](#project-overview)
- [Inpatient Medications](#inpatient-medications)
  - [Inpatient Medications V. 5.0](#inpatient-medications-v-50)
- [Outpatient Pharmacy](#outpatient-pharmacy)
  - [Outpatient Pharmacy V. 7.0](#outpatient-pharmacy-v-70)
This document provides a brief description of the new features and functions of the Remote Data Interoperability (RDI) project. This project consists of five patches:
- Inpatient Medications patch PSJ\*5\*146
- Outpatient Pharmacy patch PSO\*7\*207
- Order Entry and Results Reporting Patch OR\*3\*232
- Adverse Reaction Tracking patch GMRA\*4\*26
- RDI trigger patch OR\*3\*238 (which must be installed for the functionality to perform)
![](psj-5-146-release-notes-remote-data-interoperability-project/002.png)Note: No changes in current order check functionality are expected with the installation of the PSO and PSJ patches listed above. The information referenced in this document pertaining to remote order checks will not be in effect until a future date when the RDI trigger patch (OR\*3\*238) is installed. The RDI trigger patch turns on remote order checking.
This product runs on standard hardware platforms used by the Department of Veterans Affairs (VA) Healthcare facilities. These systems consist of standard or upgraded Alpha AXP clusters and run VMS DSM, or Cache VMS.

## Project Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RDI project provides a method of comparing clinical data about a patient received from all VA Medical Centers (VAMCs), as well as clinical data from military facilities where active dual consumers are treated. Active dual consumers may be military personnel treated at a VHA facility or VA patients treated at a military facility. The medication orders and allergies will be compared across all sites to determine if any orders are contraindicated based on clinical data originating at any other site.

The RDI project consists of two distinct components.

One component enhances the current Remote Data Views (RDV) to add the display of clinical data stored in the Health Data Repository Historical (HDR-Hx) and Health Data Repository Interim Messaging Solution (HDR-IMS). The other component of the RDI project provides the ability to do drug and allergy order checks against data from all sites stored within the HDR. The HDR-IMS includes only the domains that have been standardized by the Data Standardization initiative. At this time those domains include allergies, outpatient medications, and vital signs.

The Computerized Patient Record System (CPRS), Outpatient Pharmacy and the Adverse Reaction Tracking System (ARTS) retrieve the aggregated data via the Clinical Data Service (CDS) to perform order checks for medication orders. CPRS, Outpatient Pharmacy, Inpatient Medications, and ARTS use the data provided by CDS to support order checking for medication orders and drug-drug allergy data from any site transmitting to the HDR. These order checks include drug-drug, drug-drug class, duplicate drug, and drug-drug allergy. For the purpose of clarification this document uses RDI/OC when discussing the order checking portion of the project.

Order checking and RDV changes remain dormant until such time that the HDR and CDS are ready to receive and transmit data. A patch will be issued by CPRS to turn on the RDI/OC and RDI/RDV functionality at that time.

# Inpatient Medications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features and enhancements of the Inpatient Medications application are discussed below. These changes will expand the current order check functionality by adding remote order checks.

## Inpatient Medications V. 5.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, all pending, non-verified, active and renewed Inpatient orders, active Outpatient orders and active Non-VA Meds documented in CPRS are included in the Inpatient Medications order check process. With the release of PSJ\*5\*146, PSO\*7\*207, GMRA\*4\*26, OR\*3\*232, and OR\*3\*238, order checks will be available using data from the HDR-Hx and the HDR-IMS. This will contain both Outpatient orders from other VAMCs as well as from DoD facilities, if available. Any remote Outpatient order that has been expired for 120 days or less will be included in the list of medications to be checked.

There is a slight difference in the display of local Outpatient orders compared with remote Outpatient orders. Below are examples of the two displays:

Example: Local Outpatient Order Display

The patient has this Outpatient order:

-----------------------------------------------------------------------------

Rx \#: 40074 PHENYTOIN 100MG (Extended) CAP

Status: Active Issued: 07/11/05

SIG: TAKE ONE CAPSULE BY MOUTH TWICE A DAY

QTY: 60 \# of refills: 11

Provider: PSOPROVIDER,ONE Refills remaining: 11

Last filled on: 07/11/05

Days Supply: 30

-----------------------------------------------------------------------------

Example: Remote Outpatient Order Display

----------------------------------------------------------------------------

DAYTON Rx \#: 2663878 WARFARIN NA 10MG TAB

Status: ACTIVE Issued: 07/11/05

SIG: TAKE ONE-HALF TABLET BY MOUTH BEFORE BREAKFAST --TO

THIN BLOOD--

QTY: 4

Provider: PSOPROVIDER,TWO Refills remaining: 0

Last filled on: 07/11/05

Days Supply: 1

-----------------------------------------------------------------------------

In the Remote Outpatient Order Display example above, notice the name of the remote location has been added. In addition, the number of refills is not available.

*(This page included for two-sided copying.)*

# Outpatient Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features and enhancements of the Outpatient Pharmacy application are discussed below. These changes will expand the current order check functionality by adding remote order checks.

## Outpatient Pharmacy V. 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a new drug order is processed (new, renewal, finish, verify, copy, or an edit that creates a new order), order checks are performed. These include checking for duplicate drug, duplicate drug class, drug-drug interaction, and drug-drug allergy.

Following the installation of patches PSO\*7\*207 and OR\*3\*238 (RDI trigger patch), order checks will be made using additional data from the HDR-IMS and the HDR-Hx. This will contain both Outpatient orders from other VAMCs as well as from DoD facilities, if available. All remote prescription statuses will be included in order checking for a new order being processed from within backdoor outpatient pharmacy and for new orders placed through CPRS or Inpatient Medications. Any remote Outpatient order that has been expired for 120 days or less will be included in the list of medications to be checked.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](psj-5-146-release-notes-remote-data-interoperability-project/003.png)<strong>Note</strong>: Once the above patches have been installed, a new comment for remote order checks is displayed: “Now doing remote order checks. Please wait..."<br />
<br />
The previous comment, "Now doing order checks. Please wait..." is replaced by: "Now doing drug interaction and allergy checks. Please wait..."<br />
<br />
If, for any reason, remote order checks cannot be performed, the following message displays: "Remote data not available – Only local order checks processed."</td>
</tr>
</tbody>
</table>

  
Example: Local and Remote Order Checks

CHOOSE 1-5: 2 ACETAMINOPHEN 325MG TAB CN103 (OTC) - \*30 DAY SUP

PLY\* - MULTIPLES OF 100 - MAX QTY = (200)

-------------------------------------------------------------------------------

\*\*\* SAME CLASS \*\*\* OF DRUG IN RX \#46309525 FOR ACETAMINOPHEN 500MG TAB

CLASS: CN103

Status: Active Issued: 09/21/05

SIG: TAKE ONE TABLET BY MOUTH EVERY SIX(6) HOURS AS NEEDED

QTY: 360 \# of refills: 3

Provider: PROVIDER, ONE Refills remaining: 3

Last filled on: 09/21/05

Days Supply: 90

-------------------------------------------------------------------------------

Discontinue RX \# 46309525? NO -Prescription was not discontinued...

Now doing remote order checks. Please wait...

------------------------------------------------------------------------------

\*\*\* SAME CLASS \*\*\* OF DRUG IN REMOTE RX FOR ASPIRIN 325MG BUFFERED TAB

\>\> CHEYENNE VAMROC

CLASS: CN103

Rx \#: 712996

Status: ACTIVE Issued: 09/21/05

SIG: TAKE ONE TABLET BY MOUTH EVERY DAY

QTY: 30

Provider: PROVIDER, TWO Refills remaining: 11

Last filled on: 09/21/05

Days Supply: 30

Press Return to continue...\<Enter\>

Now doing drug interaction and allergy checks. Please wait...

A Drug-Allergy Reaction exists for this medication and/or class!

Drug: ACETAMINOPHEN 325MG TAB

Ingredients: ACETAMINOPHEN,

Do you want to Intervene? Y// NO

VERB: TAKE