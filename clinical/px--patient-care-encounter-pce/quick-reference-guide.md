---
title: Patient Care Encounter Version 1 Quick Reference Card
doc_type: QRG
doc_label: Quick Reference Guide
doc_layer: anchor
doc_subject: Quick Reference Card
app_code: PX
app_name: Patient Care Encounter (PCE)
section: CLI
app_status: active
pkg_ns: PX
patch_ver: 1
patch_id: PX*1
group_key: "PX:PX:1"
file_numbers: []
security_keys: []
menu_options: 1
description: "<table> <colgroup> <col style=\\"width: 31%\\" /> <col style=\\"width: 32%\\" /> <col style=\\"width: 35%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><p>![](patient-care-encounter-version-1-quick-reference-card/001.png)<strong>Functionality</strong></p> <blockquote> <p>Version 1.0 of PCE provides options tha"
audience: 
keywords: 
  - strong
  - encounter
  - blockquote
  - patient
  - outpatient
  - clinical
  - diagnoses
  - clinic
  - style
  - width
page_count: 0
word_count: 1176
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/pxqr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/pxqr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=82"
---

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>![](patient-care-encounter-version-1-quick-reference-card/001.png)<strong>Functionality</strong></p>
<blockquote>
<p>Version 1.0 of PCE provides options that allow:</p>
</blockquote>
<ol>
<li><p>Collection and management of outpatient encounter data</p></li>
</ol>
<ol>
<li><p>Presentation of outpatient encounter data through Health Summary components and Clinical Reports.</p></li>
</ol>
<ol>
<li><p>Capture of outpatient encounter data through interactive and non-interactive interfaces.</p></li>
</ol>
<blockquote>
<p><em>Interactive interfaces</em></p>
</blockquote>
<ol>
<li><p>Online data capture using a user interface developed with List Manager tools.</p></li>
</ol>
<ol>
<li><p>Online data capture in which Scheduling integrates with PCE to collect checkout information.</p></li>
</ol>
<blockquote>
<p><em>Non-interactive interfaces</em></p>
</blockquote>
<ol>
<li><p>PCE Device Interface, which supports the collection of encounter form data from scanners such as PANDAS, Pen-based Teleform, and Automated Information Collection System (AICS). The interface also supports workstation collection of outpatient encounter data.</p></li>
</ol>
<ol>
<li><p>PCE application programming interface (API) which supports the collection of outpatient encounter data from ancillary packages such as Laboratory, Radiology, Text Integration Utility (TIU), and Computerized Record Patient System (CPRS).</p></li>
</ol>
<p>![](patient-care-encounter-version-1-quick-reference-card/002.png)</p></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 34%" />
<col style="width: 32%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Adding Encounter Data</strong></p>
<blockquote>
<p><em>With the Update Encounter action you can add or edit encounter information, either through the Edit an Item or Delete an Item actions, or by choosing one of the other actions shown below.</em></p>
<p><em><strong>Steps to add an Immunization</strong></em></p>
<p><strong>1.</strong> Select UE from the PCE Appointment List screen.</p>
<p><strong>2.</strong> Select IM from the PCE Update Encounter screen.</p>
</blockquote>
<p><u><strong>PCE Update Encounter</strong> Nov 10, 1994 10:36:29 Page:1 of 1</u></p>
<p>PCEPATIENT,ONE 000456789 Clinic or Ward: ORTHOPEDICS</p>
<p><u>Encounter Date 11/07/94 08:00 Clinic Stop: ORTHOPEDICS</u></p>
<p>1 Encounter: 11/07/94 08:00</p>
<p>Encounter Type: X Appointment</p>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
<blockquote>
<p>ED Edit an Item TR Treatment DD Display Detail</p>
<p>DE Delete an Item IM Immunization DB Display Brief</p>
<p>EN Encounter PE Patient Ed IN Checkout Interview</p>
<p>PR Provider ST Skin Test SC Stop Code</p>
<p>DX Diagnosis (ICD 9) XA Exam QU Quit</p>
<p>CP CPT (Procedure) HF Health Factors</p>
</blockquote>
<p>Select Action: Quit/// <strong>IM</strong> Immunization</p>
<p><strong>3.</strong> Respond to the following prompts for the immunization, as appropriate.</p>
<blockquote>
<p>Immunization: <strong>POLIOMYELITIS</strong> SALK</p>
<p>Encounter Provider: PCEPROVIDER,ONE//<strong>[RET]</strong> PCEPROVIDER,ONE</p>
<p>Is this provider Primary or Secondary? P// <strong>[RET]</strong></p>
<p>Series: <strong>B</strong></p>
<p>Reaction: <strong>[RET]</strong></p>
<p>Repeat Contraindicated: NO// <strong>[RET]</strong> NO (OK TO USE IN THE FUTURE)</p>
<p>Administered Date and (optional) Time:(4/21/96-5/22/96): <strong>[RET]</strong></p>
<p>Comments: <strong>[RET]</strong></p>
<p>Immunization: <strong>[RET]</strong></p>
<p><strong>4.</strong> The edited screen is then displayed.</p>
</blockquote></td>
<td><p><strong>Clinical Reminders</strong></p>
<p><em>The PCE Clinical Reminders functionality works in conjunction with Health Summary to provide providers with timely information about their patients' heatlh maintenance schedules. Providers can work with their local ADP coordinators to set up customized schedules based on local and national guidelines for patient education, immunizations, and other procedures.</em></p>
<p><em><strong>Example of Health Summary showing clinical reminders</strong></em></p>
<p>10/11/96 16:03<br />
CONFIDENTIAL OUTPATIENT SUMMARY *</p>
<p>PCEPATIENT,TWO 666-45-6789 SURG-ICU DOB: 10/03/50</p>
<p>------------------------- DEM - Demographics -------------------</p>
<p>Address: HEARTATTACK &amp; VINE Phone: 703-450-8010</p>
<p>LOS ANGELES, CA 23077 County: LOS ANGELES</p>
<p>Marital Status: NEVER MARRIED Age: 40</p>
<p>Religion: OTHER Sex: MALE</p>
<p>Period of Service: VIETNAM ERA</p>
<p>Branch of Service: MARINE CORPS 08/07/70 TO 04/15/75</p>
<p>Eligibility: SC LESS THAN 50% Status: VERIFIED</p>
<p>S/C %: 0</p>
<p>NOK: LEONARD &amp; JEANNINE Relation: PARENTS</p>
<p>135 BLACKHAWK Phone: 314-820-1111</p>
<p>DINER, MISSOURI 63122</p>
<p>--------------------- CVP - Past Clinic Visits -----------------</p>
<p>10/09/96 08:45 BLUE-ORTHOPEDIC-JC</p>
<p>10/03/96 13:00 GREEN-DERMATOLOGY PM-JC</p>
<p>09/19/96 10:00 PSYCHOLOGY L KANTON PHD JC</p>
<p>----- BLO - Brief Lab Orders (max 6 occurrences or 1 year) ------</p>
<p>Collection DT Test Name Specimen Urgency Status</p>
<p>09/25/96 GLUCOSE SERUM ROUTINE ORDERED</p>
<p>09/13/96 CHEM 7 SERUM ROUTINE COMPLETED</p>
<p>05/22/96 CBC BLOOD ROUTINE PROCESSING</p>
<p>--------------------- RXOP - Outpatient Pharmacy --------------------</p>
<p>Outpatient prescriptions are cancelled 72 hours after admission</p>
<p>Last Drug Rx # St Qty Issued Filled Rem</p>
<p>THEOPHYLLINE 200MG 5174091A A 90 10/04/95 10/04/96 (5)</p>
<p>T1.5T PO BID NH</p>
<p>TRIAMCINOLONE (AZMA 5174100A A 1 10/04/95 10/04/96 (5)</p>
<p>-----------------------CLINICAL REMINDERS ----------------------</p>
<p>LAST NEXT</p>
<p>CHOLESTEROL 4/12/96 DUE NOW</p>
<p>BLOOD PRESS 4/12/96 DUE NOW</p>
<p>SMOKING EDU 4/12/96 DUE NOW</p>
<p><u>* END *</u></p></td>
<td><p><strong>Clinical Reports</strong></p>
<blockquote>
<p><em>The PCE Clinical Reports options provide clinicians and managers with summary data about their patients, workload activity, and encounter counts.</em></p>
<p><strong>PCE Clinical Reports Menu</strong></p>
<p>PP Patient Profile by Clinic</p>
<p>PA Patient Activity by Clinic</p>
<p>WL Workload by Clinic</p>
<p>DX Diagnoses Ranked by Frequency</p>
<p>CE Location Encounter Counts</p>
<p>PE Provider Encounter Counts</p>
</blockquote>
<p>Aug 22, 1996 11:20:38 am Page 1</p>
<p>PCE Diagnosis Ranked by Frequency</p>
<p>Criteria for Frequency of Diagnoses Report</p>
<p>Encounter diagnoses: Primary Diagnoses )</p>
<p>Encounter date range: Jul 27, 1995 - May 22, 1996</p>
<p>Selected clinics: YES</p>
<p>Service categories: AHIT</p>
<p>Patient Ages.................ALL</p>
<p>Patient Sex..................ALL</p>
<p>Maximum number of diagnoses to be displayed: 10</p>
<p>Facility: SALT LAKE CITY 660</p>
<p>Clinic Stop: CARDIOLOGY (143)</p>
<p>Total number of Encounters meeting the selection criteria: 71</p>
<p>Total number of Diagnoses for these Encounters: 45</p>
<p>Diagnoses/Encounter ratio: 0.63</p>
<p>PCE Diagnosis Ranked by Frequency</p>
<p>10 Most Frequent ICD Diagnoses:</p>
<p>Code Description frequency</p>
<p>------ ------------------------------ -------</p>
<p>1. 100.0 LEPTOSPIROS ICTEROHEM 6</p>
<p>2. 401.1 BENIGN HYPERTENSION 6</p>
<p>3. 100.81 LEPTOSPIRAL MENINGITIS 3</p>
<p>4. 342.01 FLAC HEMIPLEG &amp; HEMIPAR, DOM. 2</p>
<p>5. 501. ASBESTOSIS 2</p>
<p>6. 142.0 MALIG NEO PAROTID 2</p>
<p>7. 429.3 CARDIOMEGALY 2</p>
<p>8. 100.89 LEPTOSPIRAL INFECT NEC 2</p>
<p>9. 701.0 CIRCUMSCRIBE SCLERODERMA 1</p>
<p>10. 500. COAL WORKERS' PNEUMOCON 1</p>
<p>10 Most Frequent Diagnostic Categories:</p>
<p>Diagnostic Category Count</p>
<p>------------------------------ -------</p>
<p>1. CIRCULATORY SYSTEM 10</p>
<p>2. INFECTIOUS &amp; PARASITIC 8</p>
<p>3. NERVOUS SYSTEM 8</p>
<p>4. MENTAL DISEASES &amp; DISORDERS 4</p>
<p>5. SKIN,BREAST,SUBCUTANEOUS T 3</p>
<p>6. RESPIRATORY SYSTEM 3</p>
<p>7. MYELOPROLIFERATIVE,NEOPLASIA 2</p>
<p>8. DIGESTIVE SYSTEM 2</p>
<p>9. EAR, NOSE, MOUTH &amp; THROAT 2</p>
<p>10. INJURY,POISONING,DRUG TOXICITY 1</p>
<p>Facility: SALT LAKE CITY 660</p>
<p>End of the report.</p></td>
</tr>
</tbody>
</table>