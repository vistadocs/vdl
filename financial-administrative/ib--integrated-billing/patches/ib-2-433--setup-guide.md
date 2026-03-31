---
title: IB*2*433 Integrated Billing Version 2.0 Package Security Guide Change Pages
doc_type: SG
doc_label: Security Guide
doc_layer: patch
doc_subject: Integrated Billing Version 2.0 Package  Change Pages
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*433
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the exist
audience: 
keywords: 
  - manual
  - security
  - revised
  - files
  - modified
  - lists
  - pages
  - routines
  - integrated
  - systems
page_count: 0
word_count: 186
section_count: 0
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1994
revision_count: 1
revision_newest: 05/04/2011
revision_oldest: 05/04/2011
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_20_p433_sg_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_20_p433_sg_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

Department of Veterans Affairs Decentralized Hospital Computer Program

INTEGRATED BILLINGPACKAGE SECURITY GUIDE

March 1994

(Revised May 2011)

Information Systems Center Albany, New York

Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

| Date       | Revised Pages | Patch Number | Description                                                                                                                                                                                                                                                                                                                                                               |
|------------|---------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 05/04/2011 | 1, 2          | IB\*2\*433   | A new menu option was added to the Third Party Billing menu to allow claims to be copied and retain the original claim number. This option should now be used for all claims that do not have payments posted to them. The security key for the original option Copy and Cancel was changed and should only be used for claims that already have payments posted to them. |
|            |               |              |                                                                                                                                                                                                                                                                                                                                                                           |

General Security

1.  Integrated Billing files may only be updated through distributed options.
2.  Per VHA Directive 10-93-142 regarding security of software that affects financial systems, most of the IB routines may not be modified. The third line of routines that may not be modified will be so noted. The following routines are exempt from this requirement.

IBD\* - Encounter Form Utilities

IBO\*, IBCO\*, IBTO\* - Non-critical Reports

According to the same directive, most of the IB Data Dictionaries may not be modified. The file descriptions of these files will be so noted. The files which may be modified are Encounter Form files \#357 through \#358.91.

Security Keys

| IB AUTHORIZE            | Holding this key allows the user to authorize charges prior to sending to Accounts Receivable.                                                                                                                              |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IB CLAIMS SUPERVISOR    | This key should only be given to those individuals who may perform supervisory Claims Tracking functions, such as deleting reviews and Claims Tracking entries.                                                             |
| IB CLON                 | Holding this key allows user to access the Copy and Cancel Option. This option is used to correct DENIED claims which have payments posted against them.                                                                    |
| IB EDIT                 | Holding this key allows a user to create and edit claims for reimbursement.                                                                                                                                                 |
| IB INSURANCE SUPERVISOR | This key should only be given to those individuals SUPERVISOR who may perform supervisory insurance functions, such as deleting insurance companies, deleting policies, and inactivating and merging insurance information. |
| IB SUPERVISOR           | Holding this key allows a user to access management reports and options that control billing.                                                                                                                               |
| IBDF IRM                | This key is used to prevent access to Encounter Form Utility options that are for IRM staff only.                                                                                                                           |
| XUMGR                   | This key should be assigned to Kernel site management staff in IRM. It is required in IB to execute archive/purge                                                                                                           |