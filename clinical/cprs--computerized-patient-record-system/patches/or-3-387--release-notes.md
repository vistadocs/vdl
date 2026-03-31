---
title: OR*3*387 Release Notes - Patient Centered Management Module (PCMM) CPRS
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Patient Centered Management Module (PCMM) CPRS
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*387
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of these Release Notes is to identify enhancements to Patch OR\3\387 PCMM WEB TEAM DISPLAY ENHANCEMENTS TO CPRS. This VistA patch is required to support changes to PCMM team and provider information displayed in CPRS and is compatible with CPRS version 30 and above.
audience: 
keywords: 
  - table
  - contents
  - cprs
  - pcmm
  - modified
  - primary
  - care
  - patient
  - window
  - remote
page_count: 0
word_count: 503
section_count: 3
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_387_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_387_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Department of Veterans Affairs

  Patient Centered Management Module (PCMM) – OR\*3.0\*387
---

Release Notes

![](or-3-387-release-notes-patient-centered-management-module-pcmm-cprs/001.png)

June 2015

Documentation Version 1.1

Office of Information and Technology

Product Development

.

Revision History

| Date      | Version | Description                                     | Author                             |
|-----------|---------|-------------------------------------------------|------------------------------------|
| June 2015 | 1.1     | Added information about the CPRS 30.0b release. | <span class="mark">REDACTED</span> |
| May 2015  | 1.0     | Initial Version. Technical edit.                | <span class="mark">REDACTED</span> |

Table of Contents

# OR\*3.0\*387


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [OR\3.0\387](#or30387)
  - [Purpose](#purpose)
  - [Primary Care Header and Window Changes](#primary-care-header-and-window-changes)
- [Associated Patches](#associated-patches)
- [Modified Remote Procedure Calls](#modified-remote-procedure-calls)
- [Modified Routine](#modified-routine)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to Patch OR\*3\*387 PCMM WEB TEAM DISPLAY ENHANCEMENTS TO CPRS. This VistA patch is required to support changes to PCMM team and provider information displayed in CPRS and is compatible with CPRS version 30 and above.

## Primary Care Header and Window Changes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the ORWPT1 PRCARE Remote Procedure Call is called by CPRS, the content of the first line of the PCMM Header Button is determined and formatted by PCMM Web. The RPC code has been modified to store and retrieve the data from the Outpatient Profile File (404.41). If the RPC is not called by CPRS, the previous data format remains. Additionally, the Mental Health line in the header was modified to include the MH Team name.

If the ORWPT1 PCDETAIL RPC is called by CPRS, the contents of the Primary Care Detail Window is retrieved from PCMM Web by a web service, then formatted and returned to CPRS, to display in the window. If the RPC is not called by CPRS, the data format remains.

- In the CPRS Primary Care window, users can now view a patient’s Primary Care Team, Provider, Associate Provider, and Non-VA Providers.
- Mental Health Treatment Coordinator and contact information will also display in the CPRS Primary Care Window

![](or-3-387-release-notes-patient-centered-management-module-pcmm-cprs/002.png)

- The Primary Care area of the CPRS header is updated to display:
  - if a patient is assigned to a Primary Care Team and has an active or a pending assignment.
  - local and remote assignments.
  - if the patient is receiving Non-VA Primary Care.
  - if a patient is assigned to a Mental Health Treatment Coordinator. The Staff Name and Team Name display.

> ![](or-3-387-release-notes-patient-centered-management-module-pcmm-cprs/003.png)

> NOTE: These updates to the Primary Care Header and Window Changes will be documented in the CPRS User guides with the release of CPRS 30.b (OR\*3.0\*350).

# Associated Patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches are associated with this release:

PCMM Web Informational Patch:

- WEBP\*1\*1 - PATIENT-CENTERED MANAGEMENT MODULE (PCMM) WEB

VistA Patches:

- SD\*5.3\*603 – PCMM WEB LEGACY CHANGES
  - This VistA patch is required for PCMM Web and VistA systems such as CPRS. It must be installed in close coordination with PCMM Web.

# Modified Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Remote Procedure Calls were modified for OR\*3.0\*387.

| RPC         | Function                                       |
|-----------------|----------------------------------------------------|
| ORWPT1 PRCARE   | Displays the CPRS Primary Care Header information. |
| ORWPT1 PCDETAIL | Displays the CPRS Primary Care Detail window.      |

Modified Remote Procedure Calls table

# Modified Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routine was modified for OR\*3.0\*387.

| Routine Name | Function                                                                                             |
|------------------|----------------------------------------------------------------------------------------------------------|
| ORWPT1           | This routine contains the entry points for the Remote Procedure Calls ORWPT1 PRCARE and ORWPT1 PCDETAIL. |

Modified Routine Table displaying