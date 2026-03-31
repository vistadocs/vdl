---
title: AICS Modification for Code Set Versioning
doc_type: SUP
doc_label: Supplement
doc_layer: plain
doc_subject: 
app_code: IBD
app_name: Automated Information Collection System (AICS)
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 2
description: - [AICS MODIFICATIONS FOR THE CODE SET VERSIONING PROJECT](#aics-modifications-for-the-code-set-versioning-project) - [AICS OPTIONS](#aics-options) - [SECURITY KEY](#security-key) This patch supports the HIPAA legislation that diagnostic (ICD) and procedure codes (CPT),used for billing purposes, be
audience: 
keywords: 
  - entry
  - aics
  - table
  - contents
  - scanning
  - manual
  - encounter
  - forms
  - form
  - modifications
page_count: 0
word_count: 439
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics3_0modifcations.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics3_0modifcations.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=30"
---

# AICS MODIFICATIONS FOR THE CODE SET VERSIONING PROJECT


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [AICS MODIFICATIONS FOR THE CODE SET VERSIONING PROJECT](#aics-modifications-for-the-code-set-versioning-project)
- [AICS OPTIONS](#aics-options)
- [SECURITY KEY](#security-key)
This patch supports the HIPAA legislation that diagnostic (ICD) and
procedure codes (CPT),used for billing purposes, be date-sensitive.
Modifications have been made to the following AICS functionality
to support date sensitive ICD & CPT codes:
1\. Encounter Forms
a\. Creation
b\. Modification
2\. Maintenance Utilities
3\. Lists sent to outside VistA packages (CPRS, PCE, TIU, etc.)
IBDF18A - API:
==============
Routine IBDF18A has been modified to allow other packages to pass an
encounter date. This will impact integration agreements DB1A 1296,
and DBIA 397
Scanning and Manual Data Entry (MDE)
====================================
Scanning and Manual Data Entry (MDE) functionality in AICS will be terminated
with the installation of this patch. This shutdown is for the following
reasons:
1\. Because this functionality is no longer being enhanced, it is not
compatible with the new diagnostic and procedure codes as defined
by HIPAA. If Scanning & MDE are allowed to continue, encounter data
may be rejected, which would result in the generation of application
errors.
2\. VHA DIRECTIVE 2003-012.
a\. All facilities should only be using "electronic encounter forms"
by October 1, 2003.
b\. All providers should enter their own encounter data using CPRS by
October 1, 2003.
3\. CPRS is now the method of choice for entering outpatient encounter
data.

# AICS OPTIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

============

When using any of the following options, the user will see the message:

==\> Sorry, your Primary Menu is out of order with the message:

\*\* This option is OUT OF ORDER \*\*

---------------------------------------------------------------

AICS Scanning Workstation \[IBD SCANNING WORKSTATION\]

Clinic based Data Entry \[IBD MANUAL DATA ENTRY BY CLIN\]

Data Entry by Form \[IBD MANUAL DATA ENTRY BY FORM\]

Group Clinic Data entry \[IBD MANUAL DATA ENTRY GROUP\]

Form Component Inquiry \[IBD MANUAL DATA DISPLAY\]

Pre-printed Form Data Entry \[IBD MANUAL DATA ENTRY PRE\]

Scanned Forms w/ Bill Gen \[IBDF SCANNED W/BILL GEN\]

Conversion Utility For Scanning \[IBDFC CONVERSION UTILITY\]

Validate Forms \[IBDF VALIDATE FORMS\]

---------------------------------------------------------------

REMOTE PROCEDURE CALLS (SCANNING)

=================================

The following RPC have been marked "INACTIVE":

IBD ELAPSED TIME

IBD EXPAND FORMID

IBD GET FORMSPEC

IBD RECEIVE DATA

IBD RECEIVE FORM DATA

IBD RETURN IMAGE ID

IBD VALIDATE USER

IBD STORE IMAGE NAME

IBD STORE WORKSTATION ERROR

IBD GET ALL PCE DATA

IBD GET PAST APPT LIST

IBD GET FORMSPEC GLOBAL

IBD GET SCAN PAGE INFO

# SECURITY KEY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

============

The following security key will be DELETED at the site:

IBD SCAN MANAGER