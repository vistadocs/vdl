---
title: PSO*7*170 PBM Demographics Enhancements Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: PBM Demographics Enhancements
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*170
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - pharmacy
  - changes
  - management
  - interface
  - patch
  - modifications
  - benefits
  - inpatient
page_count: 0
word_count: 363
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/psj_5_pso_7_psu_4_dg_5_3_pss_1_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/psj_5_pso_7_psu_4_dg_5_3_pss_1_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-170-pbm-demographics-enhancements-release-notes/001.png)

PHARMACY ENHANCEMENTS TO SUPPORT PHARMACY BENEFITS MANAGEMENT

RELEASE NOTES

## PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, DG\*5.3\*671, PSS\*1\*99 May 2009

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Office of Enterprise Development

TABLE OF CONTENTS

> May 2009 Pharmacy Enhancements to Support Pharmacy Benefits Management Release Notes i PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, DG\*5.3\*671, PSS\*1\*99

*(This page included for two-sided copying.)*

> ii Pharmacy Enhancements to Support Pharmacy Benefits Management Release Notes May 2009 PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, DG\*5.3\*671, PSS\*1\*99

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [PSJ\5\161, PSO\7\170, PSU\4\5, DG\5.3\671, PSS\1\99 May 2009](#psj5161-pso7170-psu45-dg53671-pss199-may-2009)
- [Introduction](#introduction)
- [Inpatient Medications Changes](#inpatient-medications-changes)
    - [WARNING: If your facility has the Pyxis/Omnicell/McKesson interface from ILC, this patch will overwrite any "local" modifications in routine PSGOETO. This could affect certain orders being sent across this interface. The modifications will have to be reintroduced following installation of this patch.](#warning-if-your-facility-has-the-pyxisomnicellmckesson-interface-from-ilc-this-patch-will-overwrite-any-local-modifications-in-routine-psgoeto-this-could-affect-certain-orders-being-sent-across-this-interface-the-modifications-will-have-to-be-reintroduced-following-installation-of-this-patch)
- [Outpatient Pharmacy Changes](#outpatient-pharmacy-changes)
- [Pharmacy Benefits Management Changes](#pharmacy-benefits-management-changes)
- [Registration Changes](#registration-changes)
- [Pharmacy Data Management Changes](#pharmacy-data-management-changes)
> The Pharmacy Benefits Management (PBM) set of patches provides enhancements for the following applications.
> Application Patch
- Inpatient Medications PSJ\*5\*161
- Outpatient Pharmacy PSO\*7\*170
- Pharmacy Benefits Management (PBM) PSU\*4\*5
- Pharmacy Data Management (PDM) PSS\*1\*99 (Released Separately)
- Registration DG\*5.3\*671
> The patches PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, and DG\*5.3\*671 are being released in a single KIDS software distribution host file, PSU_4_P5.KID, as part of the Pharmacy Benefits Management (PBM) Extracts Enhancement \#3 project. PSS\*1\*99, which is also part of this enhancement, is being released separately.
> These patches address a request which supports the Pharmacy Benefits Management (PBM) Extracts Enhancement \#3 project. In order to allow the retransmission of only those patients who have had demographic updates, Pharmacy Benefits Management V. 4.0, Inpatient Medications
> V. 5.0, Outpatient Pharmacy V. 7.0, Registration V. 5.3, and Pharmacy Data Management V. 1.0 were modified to build an entry for retransmission in the PBM PATIENT DEMOGRAPHICS file (#59.9).
> These patches do not affect the applications’ interfaces, rather provide more sound and proficient application use through behind-the-scenes improvements. The following lists any patch details that may be useful to the users.
> May 2009 Pharmacy Enhancements to Support Pharmacy Benefits Management Release Notes 1
> PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, DG\*5.3\*671, PSS\*1\*99

# Inpatient Medications Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSJ\*5\*161 supports the PBM Extracts Enhancement by correctly handling a patient’s update to a demographic field and queuing the entry for transmission (uses API LOGDFN^PSUHL). Users will not see any noticeable changes to the application interface; however the following should be noted.

### WARNING: If your facility has the Pyxis/Omnicell/McKesson interface from ILC, this patch will overwrite any "local" modifications in routine PSGOETO. This could affect certain orders being sent across this interface. The modifications will have to be reintroduced following installation of this patch.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Outpatient Pharmacy Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSO\*7\*170 supports the PBM Extracts Enhancement by correctly handling a patient’s update to a demographic field and queuing the entry for transmission (uses API LOGDFN^PSUHL). Users will not see any noticeable changes to the application interface.

# Pharmacy Benefits Management Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSU\*4\*5 supports the PBM Extracts Enhancement by correctly handling a patient’s update to two demographic fields and queuing the entry for transmission (uses API LOGDFN^PSUHL). Users will not see any noticeable changes to the application interface.

> The following issues are addressed in this patch, also.

- A \<SUSBCRIPT\> error was created when the Automatic Pharmacy Statistics \[PSU PBM AUTO\] report was run before any monthly data was filed. This has been corrected. *(Remedy Tickets 115651 and 228928)*
- A \<STORE\>SETDPT+9^DPTLK1 error was reported by sites. This error has been corrected. *(Remedy Tickets 124653 and 132211)*

# Registration Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DG\*5.3\*671 supports the PBM Extracts Enhancement by correctly handling a patient’s update to six demographic fields and queuing the entry for transmission (uses API LOGDFN^PSUHL).

> Users will not see any noticeable changes to the application interface.

# Pharmacy Data Management Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSS\*1\*99 supports the PBM Extracts Enhancement by adding a New-Style cross-reference. The cross-reference is triggered when a patient record is updated and queues the patient for transmission (uses API LOGDFN^PSUHL). Users will not see any noticeable changes to the application interface.

> 2 Pharmacy Enhancements to Support Pharmacy Benefits Management Release Notes May 2009 PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, DG\*5.3\*671, PSS\*1\*99