---
title: PSS*1*131 Release Notes - ePharmacy Phase 4 Iteration II
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ePharmacy Phase 4 Iteration II
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*131
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - drug
  - special
  - billable
  - code
  - hdlg
  - drugs
  - pharmacy
  - schedule
  - table
  - contents
page_count: 0
word_count: 990
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p131_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p131_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

![](pss-1-131-release-notes-epharmacy-phase-4-iteration-ii/001.png)

pharmacy data management (PDM)

ePharmacy Phase 4 Iteration II

Release Notes

PSS\*1\*131

July 2009

Veterans Health Information Technology

*(This page included for two-sided copying.)*Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pharmacy Data Management V. 1.0 - PSS\1\131](#pharmacy-data-management-v-10-pss1131)
  - [DEA SPECIAL HANDLING CODE](#dea-special-handling-code)
This patch has enhancements which extend the capabilities of the Veterans Health Information Systems and Technology Architecture (VistA) electronic pharmacy (ePharmacy) billing system. Below is a list of all the applications involved in this project along with their patch number:
APPLICATION/VERSION PATCH
--------------------------------------------------------------
CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP) V. 2.0 PSX\*2\*65
PHARMACY DATA MANAGEMENT (PDM) V. 1.0 PSS\*1\*131
OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*289
INTEGRATED BILLING (IB) V. 2.0 IB\*2\*384
ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*7
The last three patches (PSO\*7\*289, IB\*2\*384 and BPS\*1\*7) will be released in the Kernel Installation and Distribution System (KIDS) multi-build distribution BPS PSO IB BUNDLE 3.0. Patches PSX\*2\*65 and PSS\*1\*131 will be released as stand-alone patches. Since there is an implementation
dependency between the multi-build distribution and the stand-alone patches, PSX\*2\*65 and PSS\*1\*131 must be installed prior to the installation of the multi-build. For more specific instructions please
refer to the installation steps provided in each of the patches.

# Pharmacy Data Management V. 1.0 - PSS\*1\*131

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*131 includes the following enhancements:

- A new Drug Enforcement Administration (DEA) Special Handling code, U for Sensitive Drug, was added as a selection to the DEA SPECIAL HDLG prompt for DRUG ENTER/EDIT \[PSS DRUG ENTER/EDIT\] option.

## DEA SPECIAL HANDLING CODE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*131 adds a new code “U” to the DEA, SPECIAL HANDLING field of the DRUG file (#50) to indicate that the drug is used to treat certain conditions that are deemed “sensitive”. Specifically, the VA may not disclose any information on the following diseases: HIV, drug abuse, alcohol abuse, or sickle cell anemia without a signed consent from the patient. Drugs to mark with “U” include Antiretrovirals, Disulfiram, Naltrexone, and Methadone for maintenance or detox. When a signed Release of Information (ROI) is on file and the drug is marked with the new “U” DEA SPECIAL HANDLING CODE, the drug may be third party billable. Drugs must be manually marked with this new code, and this functionality works in conjunction with ROI modifications made in IB\*2\*384.

DEA, SPECIAL HDLG: 6P// ?

ANSWER MUST BE 1-6 CHARACTERS IN LENGTH

THE SPECIAL HANDLING CODE IS A 2 TO 6 POSTION FIELD. IF APPLICABLE,

A SCHEDULE CODE MUST APPEAR IN THE FIRST POSITION. FOR EXAMPLE,

A SCHEDULE 3 NARCOTIC WILL BE CODED '3A', A SCHEDULE 3 NON-NARCOTIC WILL BE

CODED '3C' AND A SCHEDULE 2 DEPRESSANT WILL BE CODED '2L'.

THE CODES ARE:

0 MANUFACTURED IN PHARMACY

1 SCHEDULE 1 ITEM

2 SCHEDULE 2 ITEM

3 SCHEDULE 3 ITEM

4 SCHEDULE 4 ITEM

5 SCHEDULE 5 ITEM

6 LEGEND ITEM

9 OVER-THE-COUNTER

L DEPRESSANTS AND STIMULANTS

A NARCOTICS AND ALCOHOLS

P DATED DRUGS

I INVESTIGATIONAL DRUGS

M BULK COMPOUND ITEMS

C CONTROLLED SUBSTANCES - NON NARCOTIC

R RESTRICTED ITEMS

S SUPPLY ITEMS

B ALLOW REFILL (SCH. 3, 4, 5 ONLY)

W NOT RENEWABLE

F NON REFILLABLE

E ELECTRONICALLY BILLABLE

N NUTRITIONAL SUPPLEMENT

U SENSITIVE DRUG

DEA, SPECIAL HDLG: 6P//

DEA, SPECIAL HDLG field effects on ePharmacy Billing:

- If the DEA, SPECIAL HDLG field contains an “I” (Investigational), “S” (Supply), “N” (Nutritional Supplement), or “9” (OTC), the drug is NOT billable. However, if the same drug also contains the “E” (electronically billable), the drug becomes BILLABLE.
- If the DEA, SPECIAL HDLG field contains an “M” or “0” (both designating a Compound Drug), the drug is NOT billable. If the same drug contains the “E” (electronically billable), the drug is STILL NOT billable.
- If the DEA, SPECIAL HDLG field is NULL (empty), the drug is NOT billable .
- If the DEA SPECIAL HDLG filed contains a “U” (Sensitive Drug), the drug is only billable if there is a signed Release of Information (ROI) on file. This functionality works in conjunction with ROI modifications made in IB\*2\*384.

Note that ALL other drugs are billable.

Follow these guidelines to ensure proper electronic billing:

- When a signed Release of Information (ROI) is on file and the drug is marked with the “U”(Sensitive Drug), it may be third party billable. This functionality works in conjunction with ROI modifications made in IB\*2\*384.
- If an item is to be billed, then there must be an entry in the DEA, SPECIAL HDLG field. It is not necessary to include a numeric value; any value (other than the non-billable codes listed above) will allow ePharmacy to submit a bill.
- Add an “E” to all items that contain “9”, “N”, “I”, or “S”, but are actually billable. This will most often occur with Insulin and Glucose test strips, which are usually marked with a 9 but are, in fact, billable for most insurance companies.
- Add a “U” to items that are used to treat a diagnosis deemed “sensitive”.  Specifically, the VA may not disclose any information on the following diseases without a signed Release of Information (ROI): HIV, drug abuse, alcohol abuse, or sickle cell anemia.  Drugs to mark with a “U” include Antiretrovirals, Disulfiram. Naltrexone, and Methadone for maintenance or detox.

![](pss-1-131-release-notes-epharmacy-phase-4-iteration-ii/002.png)Note: The NDF option, *Rematch/Match Single Drugs*, screens out those items with a DEA, SPECIAL HDLG code of “0”, “I”, or “M”. When sites receive NDF data updates that cause one of these items to be unmatched from NDF, they cannot use the *Rematch/Match Single Drugs* option to rematch if they have added “0”, “I”, or “M” to drugs like Antiretrovirals, Disulfiram, Naltrexone, or Methadone for maintenance or detox. Sites can either:

1.  Rematch to NDF using another option, or
2.  Remove the DEA, SPECIAL HDLG code, use the *Rematch/Match Single Drugs* option, and then add the DEA, SPECIAL HDLG code back in.