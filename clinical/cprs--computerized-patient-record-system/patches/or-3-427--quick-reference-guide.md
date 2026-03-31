---
title: OR*3*427 CPRS Quick Reference Guide
doc_type: QRG
doc_label: Quick Reference Guide
doc_layer: patch
doc_subject: 
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*427
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - neutropenia
  - patients
  - override
  - result
  - clozapine
  - emergency
  - strong
page_count: 0
word_count: 786
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
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_p427_qr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_p427_qr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Standard Prescribing](#standard-prescribing)
- [Local Override](#local-override)
- [National Override](#national-override)
- [Mild Neutropenia](#mild-neutropenia)
- [Moderate and Severe Neutropenia](#moderate-and-severe-neutropenia)
- [Patient not registered in the prescriber’s facility– Emergency Registration Override – Temporary Authorization](#patient-not-registered-in-the-prescribers-facility-emergency-registration-override-temporary-authorization)
- [No Matching WBC result](#no-matching-wbc-result)
- [No ANC result within the past 7 days](#no-anc-result-within-the-past-7-days)
- [Auto-Notification to Provider](#auto-notification-to-provider)
- [Complex Clozapine Orders](#complex-clozapine-orders)
- This Quick Reference Guide provides information for prescribers describing the new enhancements to the Clozapine Management System software in CPRS.
- This update will allow a one-time emergency prescription of clozapine under certain circumstances when it is necessary to prevent lapses in treatment. Note that the system does not allow starting patients on clozapine under emergency conditions.
- This update does not include provisions for modifying the frequency of ANC monitoring for patients with Benign Ethnic Neutropenia (BEN) or those in hospice care. Prescribing for patients with BEN in the presence of neutropenia, or hospice patients in the absence of blood tests will continue to require an override.
- This update has not modified the process for registering new and transferring patients with the National Clozapine Coordinating Center (NCCC), updating monitoring frequencies for reporting terminations of clozapine treatment. Please contact the NCCC for information on these procedures via e- mail at [VHACLOZAPINE@VA.GOV.](mailto:VHACLOZAPINE@VA.GOV)
- The ANC is the laboratory blood test required for monitoring patients on clozapine
  - ANC unit of measure: cells per cubic millimeter
> (cmm = cu mm = mm3 = μL)
- VistA requires a matching WBC result from the same draw date/time
- The update is designed to support the
> implementation of the FDA’s Clozapine Risk Evaluation and Mitigation Strategy (REMS) requirements for monitoring.

# Standard Prescribing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a registered patient with temporary or permanent authorization has an ANC result of 1500/cmm or greater with a matching WBC in the last 7 days, prescribing generates a pending order that is sent to the pharmacy. There is no CPRS message to the provider. Prescribing under any other conditions will be locked out. A CPRS message will identify the cause of the lock out, and a local or national override will be required to allow prescribing and dispensing.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 27%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ANC Level</strong></p>
</blockquote></th>
<th><p><strong>ANC</strong></p>
<p><strong>Monitoring</strong></p></th>
<th><blockquote>
<p><strong>Frequency of ANC Lab Tests</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Normal range</p>
</blockquote></td>
<td><p>ANC ≥</p>
<p>1500/cmm</p></td>
<td><ul>
<li><p>Weekly for patients 1 – 6 months on therapy</p></li>
<li><blockquote>
<p>Bi-weekly for patients 6</p>
</blockquote></li>
</ul>
<blockquote>
<p>– 12 months on therapy</p>
</blockquote>
<ul>
<li><blockquote>
<p>Monthly for patients</p>
</blockquote></li>
</ul>
<blockquote>
<p>&gt;12 months on therapy</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Mild neutropenia</p>
</blockquote></td>
<td><p>1000 –</p>
<p>1499/cmm</p></td>
<td><blockquote>
<p>3x weekly until ANC stabilizes to 1500/cmm or</p>
<p>greater</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Moderate neutropenia</p>
</blockquote></td>
<td><p>500 –</p>
<p>999/cmm</p></td>
<td><blockquote>
<p>Daily until ANC stabilizes to 1000/cmm or higher, then 3x weekly until ANC stabilizes to 1500/cmm or</p>
<p>greater</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Severe neutropenia</p>
</blockquote></td>
<td>&lt; 500/cmm</td>
<td><blockquote>
<p>Daily until ANC stabilizes to 1000/cmm or greater, then 3x weekly until ANC stabilizes to 1500/cmm or</p>
<p>greater</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Local Override

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The conditions when a Local Override is allowed include:

- ANC between 1000 – 1499/cmm.
  - To allow continued prescribing for patients with mild neutropenia when the prescriber determines that the benefits outweigh the risks
- No ANC within the past 7 days
  - To allow providing an emergency 4-day supply under special conditions described below
- For patients not registered elsewhere but not at

> the prescriber’s facility

- To allow providing an emergency 4-day supply under a temporary authorization number assigned during non-duty hours

# National Override

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The conditions when a National Override is allowed include:

- Moderate to Severe Neutropenia
- ANC results have No Matching WBC result
- No ANC result in last 7 days (non-emergency)

> To obtain a national override, the prescriber must submit the relevant form, along with the rationale for the override, to the National Clozapine Coordinating Center (NCCC).

# Mild Neutropenia

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a registered patient has an ANC result of 1000- 1499/cmm (Mild neutropenia) with a matching WBC in the last 7 days, clozapine treatment can continue provided that the prescriber, along with the patient, determine that the benefits outweigh the risks. When prescribing, the provider receives a message in CPRS that instructs them to test ANC 3x weekly until ANC stabilizes to greater than or equal to 1500/cmm. A pending order is sent to the pharmacy for a Local Override. Note that even though blood tests are required 3x weekly, the pharmacy can dispense up to 7-day supply of medication.

![](or-3-427-cprs-quick-reference-guide/001.png)

# Moderate and Severe Neutropenia

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a registered patient has an ANC result less than 1000/cmm (Moderate is 500-999/cmm, and Severe is less than 500/cmm), with a matching WBC in the last 7 days, an NCCC-authorized National Override is required before the order can be placed. If the prescriber determines that the benefits of clozapine outweigh the risks, they should submit a request for a national override to NCCC. Please note that the prescriber should work with the patient to make this determination. Once a national override is in place, the provider receives a message in CPRS instructing them to test ANC Daily until ANC stabilizes to greater than or equal to 1000/cmm. Note that once the ANC stabilizes at 1000/cmm, the ANC is to be tested 3x weekly until it stabilizes to 1500/cmm or greater.

> Note that even though blood tests are required daily, the pharmacy can dispense up to 7-day supply of medication.

> ![](or-3-427-cprs-quick-reference-guide/002.png)

![](or-3-427-cprs-quick-reference-guide/003.png)

# Patient not registered in the prescriber’s facility– Emergency Registration Override – Temporary Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For a patient who is not currently registered in the

> prescriber’s facility, but is currently registered and receiving clozapine from another facility, the update allows emergency prescribing during times when it is not possible to register the patient with NCCC when the prescriber determines that it is necessary to prevent a lapse in treatment. In these cases, prescribers will receive a CPRS message instructing them to send a written order to the pharmacy where a temporary local authorization number can be assigned during non-duty hours for a one-time emergency 4-day supply. Emergency prescribing for patients not registered at the prescriber’s facility requires an ANC result of 1500/cmm or greater with a matching WBC in the last 7 days. Note that this type of override can be used to address the needs of traveling patients.

> ![](or-3-427-cprs-quick-reference-guide/004.png)

# No Matching WBC result

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a registered patient has an ANC result in the last 7 days but no Matching WBC result, the CPRS message instructs the provider to redo lab tests or contact NCCC to request a National Override.

![](or-3-427-cprs-quick-reference-guide/005.png)

> If the provider requested and received a National Override for a patient that has an ANC result but no matching WBC, the CPRS message instructs the provider to order ANC and WBC immediately.

> ![](or-3-427-cprs-quick-reference-guide/006.png)

# No ANC result within the past 7 days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a registered patient has no ANC result in the last 7 days, prescribing will be blocked. In a non-emergency situation, the provider can submit the required override form to the NCCC that specifies the rationale for continued prescribing. This form will need to provide the dates and values of the most recent ANC and WBC counts. Once the override is approved, the provider will be allowed to

> prescribe clozapine, and the pharmacy will then be allowed to dispense the patient’s normal weekly, biweekly, or monthly supply. Note that this is the procedure that will need to be followed each month to allow hospice patients to continue receiving clozapine even though they will only need blood tests once every six months

> For outpatients and inpatients going on leave: In certain emergency situations, when the prescriber determines that prescribing and dispensing are necessary to prevent a lapse in treatment and the patient is registered at the prescriber’s facility, but he or she has no ANC result in the last 7 days, the provider can authorize a local override to allow the patient to receive a one-time 4-day supply. Emergency prescribing is allowed when delays in obtaining blood tests or medications are related to whether or to delays in obtaining medications by mail. Because VA policy places limits flexibility in dispensing medications for inpatients going on leave, this provision for emergency prescribing can also be used to supply medications for these patients. When these conditions are met, prescribers should write a prescription or order to the pharmacy, specifying one of the approved reasons: (1) weather-related, (2) mail order delays of clozapine, or (3) inpatient going on leave.

![](or-3-427-cprs-quick-reference-guide/007.png)

> For inpatients: In an emergency situation when a registered inpatient has no ANC result in the last 7 days in the local VistA system but when lab tests have been done elsewhere, the provider can authorize a local override to allow the patient to receive a one-time 4-day supply. The provider can write a prescription/order to the pharmacy and include the Inpatient reason as IP Order Override with Outside Lab Results in addition to recording the ANC results from the outside lab.

> ![](or-3-427-cprs-quick-reference-guide/008.png)

# Auto-Notification to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the prescription/order that required an override is completed/verified, a Vista e-mail auto-notification is sent to both the Provider and the Approving member of the clozapine team to both CPRS GUI mail and the VistA Backdoor Pharmacy.

# Complex Clozapine Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Complex orders for inpatients, such as prescribing clozapine in multiple tablets or capsule sizes, or upward or downward titration while initiating or tapering treatment may lead to problems incorrectly calculating stop dates based on the

> patient’s clozapine REMS monitoring frequency. Although such orders may be processed with a manual pharmacy review of the stop date(s) in the pharmacy package, it is recommended that prescribers avoid the use of complex inpatient medication orders for clozapine until the software issues are resolved.

> Updated by NCCC April 29, 2019