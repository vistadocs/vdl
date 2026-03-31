---
title: PSJ*5*160/175 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*160
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - duplicate
  - order
  - orders
  - inpatient
  - table
  - contents
  - remote
  - check
  - modifications
  - allergies
page_count: 0
word_count: 777
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p175_p160_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p175_p160_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](psj-5-160-175-release-notes/001.png)

Inpatient Medications

PSJ\*5\*175

PSJ\*5\*160

####### (released 3/29/2007)

####### RELEASE NOTES 

October 2007

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Patch PSJ\5\175 – Duplicate Order Check Modifications](#patch-psj5175-duplicate-order-check-modifications)
  - [Patch PSJ\5\160 – Modifications for Remote Allergies](#patch-psj5160-modifications-for-remote-allergies)
- [Duplicate Order Check Enhancements](#duplicate-order-check-enhancements)
  - [Outpatient Duplicate Orders](#outpatient-duplicate-orders)
  - [Inpatient Duplicate Orders](#inpatient-duplicate-orders)
  - [Discontinuing Duplicate Inpatient Orders](#discontinuing-duplicate-inpatient-orders)
- [Modifications for Remote Allergies](#modifications-for-remote-allergies)
This document provides a brief description of the enhanced features of the Duplicate Order Check Modifications and Modifications for Remote Allergies projects. These Release Notes address Inpatient Medications patches PSJ\*5\*175 and PSJ\*5\*160, respectively.

## Patch PSJ\*5\*175 – Duplicate Order Check Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSJ\*5\*175 changes Order Check to allow users to select for discontinuation any duplicate Inpatient orders found. The Outpatient Pharmacy medication-related order checks are grouped together on the first screen as information only, and Inpatient Medications order checks are displayed in a numbered list. Results from both Duplicate Drug and Duplicate Drug Class order checks are displayed together. The user is prompted to select which, if any, of the listed duplicate orders should be discontinued. The user may choose to select none, thus leaving all orders intact.

Duplicate order checks are performed on the following order processes:

- Entering a New Medication Order
- Selecting an Existing Medication Order
- Finishing a Medication Order
- Renewing a Medication Order
- Order Set Entry

## Patch PSJ\*5\*160 – Modifications for Remote Allergies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSJ\*5\*160 provides the following functionality:

- Order checks for remote allergies using VA Drug Class now include all remote allergies.
- Order checks for Analgesics match only against the specific class. For example, CN101 matches only to CN101, not to CN102 also, as was previously the case.
- The check for remote data availability is now performed when entering the patient’s chart, not on each order, as was previously the case.
- The list of remote allergies has been added to the Patient Information screen. If a patient has the same allergy information from several remote sites, it will only be listed once.

*(This page included for two-sided copying.)*

# Duplicate Order Check Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements to Outpatient and Inpatient Duplicate Order Check displays provided in Patch PSJ\*5\*175, as seen in the screen capture on page 4, are described in the following sections.

## Outpatient Duplicate Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient duplicate order check results display together on the first screen before all other order check information. These results are displayed for informational purposes only. The header for Outpatient duplicate orders reads as follows:

> The patient has the following Outpatient order(s):

## Inpatient Duplicate Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Duplicate drug and duplicate drug class Inpatient orders display together in a numbered sequence. The user selects from the numbered sequence the order(s) to be discontinued, if any. The header for Inpatient duplicate orders reads as follows:

> This patient is already receiving the following INPATIENT order(s) for the same drug or in the same drug class as WARFARIN SOD. 50MG COMB. PACK.:

After the user has discontinued an order, if any duplicate Inpatient orders remain, they are displayed again in a numbered list. The following header is displayed:

> Now, this patient is already receiving the following INPATIENT order(s) for the same drug or in the same drug class as WARFARIN SOD. 50MG COMB. PACK.:

This cycle repeats until there are no more duplicate Inpatient orders or until the user indicates there are no more duplicate Inpatient orders they wish to discontinue.

  
Example: Duplicate Order Entry Screen

> Unit Dose Order Entry Jun 27, 2006@16:08:46 Page: 1 of 1

> PSJPATIENT,ONE Ward: 7B A

> PID: 666-666-1234 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> DOB: --/--/70 (35) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> Sex: MALE Admitted: 03/08/06

> Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

> -------------------------------------------------------------------------------

> Select DRUG: warf

> Lookup: DRUG GENERIC NAME

> 1 WARFARIN 2MG TABS BL110

> 2 WARFARIN SOD. 50MG COMB.PACK. BL110

> 3 WARFARIN SODIUM 5MG S.T. BL110

> CHOOSE 1-3: 2 WARFARIN SOD. 50MG COMB.PACK. BL110

> The patient has the following Outpatient order(s):

> -------------------------------------------------------------------------------

> Rx \#: 300410 ASPIRIN BUFFERED 325MG TAB

> Status: Active Issued: 06/08/06

> SIG: TAKE TWO TABLETS BY MOUTH AFTER MEALS TAKE THESE

> AFTER YOU GET HOME

> QTY: 100 \# of refills: 0

> Provider: PSOPROVIDER,ONE Refills remaining: 0

> Last filled on: 06/08/06

> Days Supply: 90

> -------------------------------------------------------------------------------

> This patient is receiving the following medication that has an interaction

> with WARFARIN SOD. 50MG COMB.PACK.:

> ASPIRIN TAB,EC C 06/19 07/03 A

> Give: 324MG PO Q4H

> This patient is already receiving the following INPATIENT order(s) for the same drug or in the same drug class as WARFARIN SOD. 50MG COMB.PACK.:

> 1\. WARFARIN TAB C 06/27 07/03 A

> Give: 2MG PO Q6H PSJProvider, One

> 2\. WARFARIN TAB C 06/27 07/03 A

> Give: 2MG PO Q2H PSJProvider, Two

> Do you wish to continue with the current order? YES// yes YES

> Do you wish to DISCONTINUE any of the listed orders? NO// Y

> Choose for DISCONTINUE 1-2: 1

> NATURE OF ORDER: (TBD)// \<cr\>

> REQUESTING PROVIDER: PSJProvider, One P1O

> *------------------screen continues on next page------------------*

> Now, this patient is already receiving the following INPATIENT order(s) for the same drug or drug class as WARFARIN SOD. 50MG COMB.PACK.:

> 1\. WARFARIN TAB C 06/27 07/03 A

> Give: 2MG PO Q2H PSJProvider, Two

> Do you wish to DISCONTINUE any of the listed orders? NO// \<cr\> NO

> There is a CRITICAL interaction, you must enter an intervention log to continue

> Do you wish to log an intervention? NO// yes YES

> Now creating Pharmacy Intervention

> PROVIDER: PSJPROVIDER,ONE BIRMINGHAM ALABAMA RR SYSTEMS ANALYST

> RECOMMENDATION: no change

## Discontinuing Duplicate Inpatient Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When duplicate Inpatient orders are found, the following prompt is presented after each display or redisplay of a numbered list:

> Do you wish to DISCONTINUE any of the listed orders? NO//

> Note: If the user selects the default of NO, the order process continues.

If the user enters YES to the DISCONTINUE prompt, the following prompt is presented to allow selecting orders:

> Choose for DISCONTINUE 1-N:

> Note: N represents the highest numbered duplicate order in the numbered list.

#### Exiting the Order Process

When duplicate Inpatient orders have been found, the following prompt is displayed after the first numbered list of duplicate Inpatient orders:

> Do you wish to continue with the current order? YES//

> Note: The wording of this existing prompt has been slightly modified. Also, the current default of NO has been changed to YES.

Each time a user chooses to discontinue an Inpatient duplicate order(s), a prompt is presented to enter a value for NATURE OF ORDER. This value applies to all of those orders just selected to be discontinued.

Also, each time a user chooses to discontinue an Inpatient duplicate order(s), a prompt is presented to enter a value for Requesting PROVIDER. This value applies to all of those orders just selected to be discontinued.

*(This page included for two-sided copying.)*

# Modifications for Remote Allergies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The modifications to Remote Allergies now provides a list of remote allergies on the Patient Information screen.

> Note: If a patient has the same allergy information from several remote sites, it will only be listed once.

> Patient Information Feb 01, 2007@20:25:28 Page: 1 of 1

> PSJCRUMLEY,TEST Ward: 7B A

> PID: 666-00-0737 Room-Bed: Ht(cm): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> DOB: 01/01/51 (56) Wt(kg): \_\_\_\_\_\_ (\_\_\_\_\_\_\_\_)

> Sex: FEMALE Admitted: 05/22/06

> Dx: SICK Last transferred: \*\*\*\*\*\*\*\*

> Allergies - Verified: PENICILLIN

> Non-Verified:

> Remote: PENICILLIN, SOYBEAN

> Adverse Reactions:

> Inpatient Narrative:

> Outpatient Narrative:

> Enter ?? for more actions

> PU Patient Record Update NO New Order Entry

> DA Detailed Allergy/ADR List IN Intervention Menu

> VP View Profile

> Select Action: View Profile//

*(This page included for two-sided copying.)*