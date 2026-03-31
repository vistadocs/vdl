---
title: SR*3*160 Surgery NSQIP-CICSP 2007 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Surgery NSQIP-CICSP 2007
app_code: SR
app_name: Surgery
section: CLI
app_status: archive
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*160
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - patient
  - class
  - surgery
  - updated
  - contents
  - include
  - hours
  - report
  - cardiac
page_count: 0
word_count: 6431
section_count: 7
table_count: 18
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p160_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p160_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=403"
---

![](sr-3-160-surgery-nsqip-cicsp-2007-release-notes/001.png)

Surgery NSQIP-CICSP Enhancements 2007

Release Notes

SR\*3\*160

VistA Health Systems Design & Development
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Project Enhancements](#project-enhancements)
- [Surgery Enhancements](#surgery-enhancements)
- [NSQIP Enhancements](#nsqip-enhancements)
  - [Field Updates](#field-updates)
  - [Option/Report Updates](#optionreport-updates)
  - [Data Transmissions](#data-transmissions)
- [CICSP Enhancements](#cicsp-enhancements)
  - [Field Updates](#field-updates-1)
  - [Option Updates](#option-updates)
  - [Data Transmissions](#data-transmissions-1)
- [Appendix A: Updated Definitions for Non-Cardiac Fields](#appendix-a-updated-definitions-for-non-cardiac-fields)
- [Appendix B: Updated Definitions for Cardiac Fields](#appendix-b-updated-definitions-for-cardiac-fields)
- [Appendix C: Updated Laboratory Tests](#appendix-c-updated-laboratory-tests)
This project enhances the Surgery Risk Assessment module of the VistA Surgery application. The purpose of the Surgery Risk Assessment module is to facilitate data entry of both preoperative and postoperative patient information pertaining to surgical risk assessments, and to transmit the data to a national database. Although all surgical risk data are transmitted to the national database, the cardiac and non-cardiac programs have separate executive boards, and cardiac surgical cases are assessed and tracked separately from non-cardiac surgical cases.
Clinical nurse reviewers enter both preoperative and postoperative patient data into the electronic data collection instrument in the VistA Surgery Risk Assessment module for both programs. Various reports and screen displays give the local medical center staff a mechanism for tracking and evaluating surgical risk and operative mortality at the local level, while transmission to the national database allows for the statistical analysis of trends and quality improvement on a national scale.
The National Surgical Quality Improvement Program (NSQIP) has changed its way of defining Major and Minor cases. Case selection is no longer based on the Major/Minor categorization; but instead, the Surgery package utilizes only Current Procedural Terminology (CPT) codes to determine if a case should be included or excluded from the risk assessments. Having the functionality in the system to alert the nurse reviewer if a CPT code should be included or excluded would save a tremendous amount of time for the nurse reviewer.
This project entails changes to Surgery Risk Assessment Reports for NSQIP and Continuous Improvement in Cardiac Surgery Program (CICSP), create a new utility to print out the cases that should be assessed according to the new exclusion/inclusion list based on the new CPT code list, add several new fields, remove fields no longer needed, and edit several definitions.

# Project Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software provides the following enhancements:

- Addition of new data fields
- Changes to existing data fields
- Changes to data entry screens
- Changes to reports used in Surgery Risk Assessment management process
- Changes to the Surgery Risk Assessment transmissions

*(This page included for two-sided copying.)*

# Surgery Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the changes made to the VistA Surgery application for the NSQIP-CICSP Enhancements 2007 project.

The updates are described in the following two sections: NSQIP Enhancements and CICSP Enhancements.

# NSQIP Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NSQIP Enhancements include data dictionary updates, option modifications, and data transmission updates.

## Field Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new fields in the SURGERY file (#130) are created to support NSQIP options:

- The INTRAOPERATIVE ASCITES field (#446) accepts either “YES” or “NO” entries, and does not allow an entry of “NO STUDY”. The default value is set to “NO”.
- The CLOSTRIDIUM DIFFICILE COLITIS field (#447) accepts “YES”, “NO” or “NO STUDY” entries.

The following fields in the SURGERY file (#130) are modified:

- The CURRENT SMOKER field (#202) is updated to allow “NO STUDY” as a choice.
- The PREGNANCY field (#269) is updated to accept only three values: “YES”, “NO”, and “NOT APPLICABLE”. Values previously entered are converted after installation of the patch; “P1”, “P2”, “P3”, and “PU” are converted to “YES”, and “U” is changed to “NO”.
- The INTRAOP DISSEMINATED CANCER field (#443) is updated to default to a “NO” value, and does not allow “NA” or “NO STUDY” user entries.
- The REASON FOR NO ASSESSMENT field (#102) is updated to remove “ANESTHESIA TYPE” as a selection.

The following fields in the SURGERY file (#130) are modified to include changes in the field definition or help text.

| Field Name and Number             | Description of Change          |
|---------------------------------------|------------------------------------|
| SURGERY SPECIALTY field (#.04)        | Updated data dictionary for NSQIP. |
| WOUND CLASSIFICATION field (#1.09)    | Updated data dictionary for NSQIP. |
| REASON FOR NO ASSESSMENT field (#102) | Updated data dictionary for NSQIP. |
| HISTORY OF COPD field (#203)          | Updated data dictionary for NSQIP. |
| WEIGHT LOSS \> 10% field (#215)       | Updated data dictionary for NSQIP. |
| BLEEDING DISORDERS field (#216)       | Updated data dictionary for NSQIP. |
| OPEN WOUND field (#218)               | Updated data dictionary for NSQIP. |
| PREOPERATIVE SEPSIS field (#218.1)    | Updated data dictionary for NSQIP. |

| Field Name and Number                     | Description of Change          |
|-----------------------------------------------|------------------------------------|
| PREVIOUS PCI field (#220)                     | Updated data dictionary for NSQIP. |
| SYSTEMIC SEPSIS field (#250)                  | Updated data dictionary for NSQIP. |
| PNEUMONIA field (#251)                        | Updated data dictionary for NSQIP. |
| PULMONARY EMBOLISM field (#252)               | Updated data dictionary for NSQIP. |
| ACUTE RENAL FAILURE field (#254)              | Updated data dictionary for NSQIP. |
| PREGNANCY field (#269)                        | Updated data dictionary for NSQIP. |
| PERIPHERAL NERVE INJURY field (#287)          | Updated data dictionary for NSQIP. |
| DYSPNEA field (#325)                          | Updated data dictionary for NSQIP. |
| CURRENT PNEUMONIA field (#326)                | Updated data dictionary for NSQIP. |
| REST PAIN/GANGRENE (Y/N) field (#330)         | Updated data dictionary for NSQIP. |
| CHEMOTHERAPY IN LAST 30 DAYS field (#338.1)   | Updated data dictionary for NSQIP. |
| QUADRIPLEGIA (Y/N) field (#398)               | Updated data dictionary for NSQIP. |
| TUMOR INVOLVING CNS (Y/N) field (#401)        | Updated data dictionary for NSQIP. |
| DATE COMP NOTED field (#2, sub-file \#130.22) | Updated data dictionary for NSQIP. |
| SEPSIS CATEGORY field (#7, sub-file \#130.22) | Updated data dictionary for NSQIP. |

The following data changes are made to the PERIOPERATIVE OCCURRENCE CATEGORY file (#136.5).

| Occurrence Category                     | Description of Change             |
|---------------------------------------------|---------------------------------------|
| SYSTEMIC SEPSIS                             | Description field update for NSQIP.   |
| PNEUMONIA                                   | Description field update for NSQIP.   |
| PULMONARY EMBOLISM                          | Description field update for NSQIP.   |
| ACUTE RENAL FAILURE                         | Description field update for NSQIP.   |
| PERIPHERAL NERVE INJURY                     | Description field update for NSQIP.   |
| CLOSTRIDIUM DIFFICILE COLITIS (C-DIFFICILE) | New category added to file for NSQIP. |

## Option/Report Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are modified as described.

- The *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\] option is updated to include the following:
  - The PREGNANCY field (#269) is updated to accept only three values: “YES”, “NO”, and “NOT APPLICABLE”. Values previously entered are converted after installation of the patch; “P1”, “P2”, “P3”, and “PU” are converted to “YES”, and “U” is changed to “NO”.
  - The CURRENT SMOKER field (#202) is updated to allow “NO STUDY” as a user entry.
  - The QUADRIPLEGIA (Y/N) field (#398) is updated to display “Quadriplegia/Tetraplegia (Y/N)” as the field prompt.
- The *Laboratory Test Results (Enter/Edit)* \[SROA LAB\] option is updated to include the following:
  - Assume a past date if the user enters a date without a year; this affects all laboratory fields.
  - Add the Hemoglobin A1c field to the list of preoperative lab test results.
- The *Operation Information (Enter/Edit)* \[SROA OPERATION DATA\] option is updated to include the following:
  - The INTRAOPERATIVE ASCITES field (#446) is added to page 1, and defaults to a “NO” value. The value of NO STUDY is not allowed.
  - The INTRAOP DISSEMINATED CANCER field (#443) is updated to default to a “NO” value, and does not allow “NA” or “NO STUDY” user entries.
- The *Patient Demographics (Enter/Edit)* \[SROA DEMOGRAPHICS\] option adds the DATE OF DEATH field (#342) to the screen. If no date is captured, the software stuffs “NA” in the field.
- The *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\] option is updated to include the new fields.
- The *Monthly Surgical Case Workload Report* \[SROA MONTHLY WORKLOAD REPORT\] option is modified to replace references to major/minor with eligible or excluded.
- The *Print 30 Day Follow-up Letters* \[SROA REPRINT LETTERS\] option is modified to display the date of operation and the local surgical specialty.
- The *Quarterly Report — Surgical Service* \[SRO QUARTERLY REPORT\] option is updated to include the new occurrence category CLOSTRIDIUM DIFFICILE COLITIS in the PERIOPERATIVE OCCURRENCE CATEGORIES section.
- These updates include functionality for selecting cases for risk assessment based upon case Current Procedural Terminology (CPT) codes, replacing the use of the Major or Minor surgery definition.
  - When selecting a case to be assessed, the software checks the case CPT codes and display an informational statement if final CPT codes have not been assigned to the case or if the case should be excluded from assessment based upon final CPT codes entered.
  - The MAJOR/MINOR field (#.03) is removed from NSQIP input options and from the *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\] option.
  - The *List of Surgery Risk Assessments* \[SROA ASSESSMENT LIST\] option contains a new report called “List of Eligible Cases”.

## Data Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data transmissions to the national database also include the new data elements for NSQIP.

The following fields are removed from the data transmissions:

- TRAUMA field (#12, subfile 130.06)
- MALLAMPATI SCALE field (#901.1)
- AIRWAY INDEX field (#901)

# CICSP Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CICSP enhancements include data dictionary updates, option modifications, and data transmission updates.

## Field Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields in the SURGERY file (#130) are modified:

- The PREOP CIRCULATORY DEVICE field (#474) is updated to add “ARTIFICIAL HEART” as a choice.
- The CARDIAC SURG PERFORMED NON-VA field (#472) is updated to have “NO” as a default value.

The following fields in the SURGERY file (#130) are modified to include changes in the field definition or help text.

| Field Name and Number             | Description of Change          |
|---------------------------------------|------------------------------------|
| CONGESTIVE HEART FAILURE field (#207) | Updated data dictionary for CICSP. |
| ON VENTILATOR \>48 HOURS field (#285) | Updated data dictionary for CICSP. |
| PERIOPERATIVE MI field (#385)         | Updated data dictionary for CICSP. |
| PREOP CIRCULATORY DEVICE field (#474) | Updated data dictionary for CICSP. |
| AORTIC STENOSIS field (#477)          | Updated data dictionary for CICSP. |

## Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are modified as described.

- The *Laboratory Test Results (Enter/Edit)* \[SROA LAB\] option is updated to include the following:
  - Assume a past date if the user enters a date without a year; this affects all laboratory fields.
- The following fields in the *Resource Data* \[SROA CARDIAC RESOURCE\] option are modified to perform data quality checks:
  - D/T PATIENT EXTUBATED field (#470) should be later than the TIME PAT OUT OR field (#.232), and earlier than the D/T PATIENT DISCH FROM ICU field (#471).
  - The D/T PATIENT DISCH FROM ICU field (#471) should be later than the D/T PATIENT EXTUBATED field (#470) and equal to or earlier than the HOSPITAL DISCHARGE DATE field (#419).

> Data entry that is outside the acceptable criteria is permitted, but a warning message displays to the user, indicating that the data should be checked for accuracy.

- The following fields in the *Operative Risk Summary Data (Enter/Edit)* \[SROA CARDIAC OPERATIVE RISK\] option are modified to perform data quality checks:
  - The ESTIMATE OF MORTALITY, DATE field (#364.1) should be earlier than the TIME PAT IN OR field (#.205). This field is no longer auto-populated.
  - The SURGICAL PRIORITY, DATE field (#414.1) should be earlier than the TIME PAT IN OR field (#.205). This field is no longer auto-populated

> Data entry that is outside the acceptable criteria is permitted, but a warning message displays to the user, indicating that the data should be checked for accuracy.

- The *Cardiac Procedures Operative Data (Enter/Edit)* \[SROA CARDIAC PROCEDURES\] option is updated to perform the following check:
  - If the TOTAL CPB TIME field (#451) \> 0, then the CONVERT FROM OFF PUMP TO CPB field (#469) should not be answered “NO, began off/stayed off”.
- The *Update Assessment Status to 'COMPLETE'* \[SROA COMPLETE ASSESSMENT\] option updates the missing items list as specified:
  - For the NUM OF PRIOR HEART SURGERIES field (#352), the field is corrected to display “Number of Prior Heart Surgeries” instead of “Prior Heart Surgery (Y/N)”.
  - For the PRIOR HEART SURGERIES field (#485), the data input functionality is modified to use the same controlled data input functionality used by the *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\] option.

## Data Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data transmissions to the CICSP database now include the revised data elements.

# Appendix A: Updated Definitions for Non-Cardiac Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following field definitions are updated in patch SR\*3\*160.

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>ACUTE RENAL FAILURE</th>
<th><p>In a patient who did not require dialysis preoperatively, worsening of renal dysfunction postoperatively requiring hemodialysis, peritoneal dialysis, hemofiltration, hemodiafiltration or ultrafiltration.</p>
<p>TIP: If the patient refuses dialysis the answer is Yes to this variable, because he/she did require dialysis.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BLEEDING DISORDERS</td>
<td><p>Any condition that places the patient at risk for excessive bleeding requiring hospitalization due to a deficiency of blood clotting elements (e.g., vitamin K deficiency, hemophilias, thrombocytopenia, chronic anticoagulation therapy that has not been discontinued prior to surgery). Do not include the patient on chronic aspirin therapy. Following is a list of medications that impact the patient's risk for bleeding. Please utilize the associated time frames for discontinuation of medication to determine your answer to this variable. The time frames are up to and including the day or hour listed. If there is no documentation of discontinuation of medication, answer 'yes' for bleeding disorder. Do not utilize the lab values to determine the answer to this variable.</p>
<p> Anticoagulants</p>
<p>Stop before procedure</p>
<p><u>Brand Name (Generic) time</u></p>
<p>Arixtra (Fondaparinux) 4 days</p>
<p>Coumadin (Warfarin 4 days</p>
<p>Fragmin (Dalteparin) 24 hours</p>
<p>Heparin - standard 6 hours</p>
<p>Heparin - unfractionated 6 hours</p>
<p>Heparin - Low molecular weight 24 hours</p>
<p>Lovenox (Enoxaparin) 28 hours</p>
<p>(Pentasaccaride 4 days</p>
<p>(APC) 12 hours</p>
<p>(Ximelagatran) 24 hours</p>
<p>Antiplatelet Agents</p>
<p>Stop before procedure</p>
<p><u>Brand Name (Generic) time</u></p>
<p>Aggrastat (Tirofiban) 12 hours</p>
<p>Aggrenox (ASA/Dipyridamole) 48 hours</p>
<p>Agrylin (Anagrelide HCL) 3 days</p>
<p>Integrilin (Eptifibatide) 12 hours</p>
<p>Persantine (Dipyridamole) 48 hours</p>
<p>Plavix (Clopidogrel) 5 days</p>
<p>Pletal (Cilostazol) 2-4 days</p>
<p>ReoPro (Abciximab) 96 hours</p>
<p>Ticlid (Ticlopidine) 10 days</p></td>
</tr>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>BLEEDING DISORDERS (continued)</th>
<th><p>Thrombin Inhibitors</p>
<p>Stop before procedure</p>
<p><u>Brand Name (Generic) time</u></p>
<p>Angiomax (Bevalirudin 8 hours</p>
<p>Argatroban,</p>
<p>Novastan (Argatroban) 4 hours</p>
<p>Refludan (Lepirudin, hirudin) 8 hours</p>
<p>Xigris (Drotrecogin alpha) 6 hours</p>
<p>Thrombolytic Agents</p>
<p>Stop before procedure</p>
<p><u>Brand Name (Generic) time</u></p>
<p>Activase (Alteplase) 4 hours</p>
<p>Retavase (Reteplase) 4 hours</p>
<p>THKase (Tenecteplase) 8 hours</p>
<p>Streptase,<br />
kabikinase (Streptokinase) 24 hours</p>
<p>Alteplase (tPA) 40 hours</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CLOSTRIDIUM DIFFICILE COLITIS</td>
<td>C. difficile-associated disease occurs when the normal intestinal flora is altered, allowing C. difficile to flourish in the intestinal tract and produce a toxin that causes a watery diarrhea. C. difficile diarrhea is confirmed by the presence of a toxin in a stool specimen. Answer yes only if you have a positive culture for C. difficile with a toxin assay and diagnosis of C. difficile documented in the chart.</td>
</tr>
<tr class="even">
<td>CHEMOTHERAPY IN LAST 30 DAYS</td>
<td>Enter “YES” if the patient had any chemotherapy treatment for cancer in the 30 days prior to surgery. Chemotherapy may include, but is not restricted to, oral and parenteral treatment with chemotherapeutic agents for malignancies such as colon, breast, lung, head and neck, and gastrointestinal solid tumors as well as lymphatic and hematopoietic malignancies such as lymphoma, leukemia, and multiple myeloma. Do not count if treatment consists solely of hormonal therapy. (See Operations Manual for list of chemotherapeutic agents.) Chemotherapy treatment must be for malignancy.</td>
</tr>
<tr class="odd">
<td>CURRENT PNEUMONIA</td>
<td><p>Report patients with evidence of pneumonia at the time the patient is brought to the OR. Patients with pneumonia must meet ONE of the following two criteria:</p>
<p>Criterion 1.</p>
<p>Rales or dullness to percussion on physical examination of chest AND any of the following:</p>
<p>a. New onset of purulent sputum or change in character of sputum</p>
<p>b. Organism isolate from blood culture</p>
<p>c. Isolation of pathogen from specimen obtained by transtracheal aspirate, bronchial brushing, or biopsy</p>
<p>OR</p>
<p>Criterion 2.</p>
<p>Chest radiographic examination shows new or progressive infiltrate, consolidation, cavitation, or pleural effusion AND any of the following:</p>
<p>a. New onset of purulent sputum or change in character of sputum</p>
<p>b. Organism isolated from blood culture</p>
<p>c. Isolation of pathogen from specimen obtained by transtracheal aspirate, bronchial brushing, or biopsy</p>
<p>d. Isolation of virus or detection of viral antigen in respiratory secretions</p>
<p>e. Diagnostic single antibody titer (IgM) or fourfold increase in paired serum samples (IgG) for pathogen</p>
<p>f. Histopathologic evidence of pneumonia</p></td>
</tr>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>DYSPNEA</th>
<th><p>The patient describes difficult, painful, or labored breathing. Dyspnea may be symptomatic of numerous disorders that interfere with adequate ventilation or perfusion of the blood with oxygen. The dyspneic patient is subjectively aware of difficulty with breathing. Select one of the following categories that best indicates the patient's subjective experience coupled with your objective assessment:</p>
<p>(1) No dyspnea</p>
<p>(2) Dyspnea upon moderate exertion (e.g., is unable to climb one flight of stairs without shortness of breath)</p>
<p>(3) Dyspnea at rest (e.g., cannot complete a sentence without needing to take a breath)</p>
<p>The time frame is at the time the patient is being considered as a candidate for surgery (which should be no longer than 30 days prior to surgery). If the patient's dyspnea status worsens prior to surgery, report the most severe.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HISTORY OF COPD</td>
<td><p>Chronic obstructive pulmonary disease (such as emphysema and/or chronic bronchitis) resulting in any one or more of the following:</p>
<p>- Functional disability from COPD (e.g., dyspnea, inability to perform ADLs)</p>
<p>- Hospitalization in the past for treatment of COPD</p>
<p>- Requires chronic bronchodilator therapy with oral or inhaled agents (see list of bronchodilators below)</p>
<p>- An FEV1 of &lt;75% of predicted on pulmonary function testing</p>
<p>Do not include patients whose only pulmonary disease is acute asthma, an acute and chronic inflammatory disease of the airways resulting in bronchospasm. Do not include patients with diffuse interstitial fibrosis or sarcoidosis.</p>
<p>(This list may not be all-inclusive. Please check your hospital formulary)</p>
<p>Bronchodilators</p>
<p><u>Trade Name</u> <u>(Generic)</u></p>
<p>Atrovent (Ipratropium)</p>
<p>Combivent, Duoneb (Ipratropium/Albuterol)</p>
<p>Alupent, Metaprel (Metaproterenol)</p>
<p>Maxair (Pirbuterol)</p>
<p>Serevent (Salmeterol)</p>
<p>Ventolin, Accuneb, Vospire, Proventil, Volmax (Albuterol)</p>
<p>Uniphyll, Theo-Dur, Uni-Dur (Theophylline)</p>
<p>Xopenex (Levalbuterol)</p>
<p>Brethine (Terbutaline)</p>
<p>Lufyllin (Dyphylline)</p>
<p>Spiriva (Tiotropium bromide)</p>
<p>Foradil (Formoterol fumarate)</p></td>
</tr>
<tr class="even">
<td>INTRAOPERATIVE ASCITES</td>
<td>Intraoperative Ascites is defined as the presence of fluid accumulation in the peritoneal cavity noted during the operative procedure.</td>
</tr>
<tr class="odd">
<td>OPEN WOUND</td>
<td>Evidence of an open wound that communicates to the air by direct exposure, with or without cellulitis or purulent exudate. This does not include osteomyelitis or localized abscesses. The wound must communicate to the air by direct exposure. Report mandible fractures under this preoperative variable.</td>
</tr>
<tr class="even">
<td>PERIPHERAL NERVE INJURY</td>
<td>Peripheral nerve damage may result from damage to the nerve fibers, cell body, or myelin sheath during surgery. Peripheral nerve injuries which result in motor deficits only to the cervical plexus, brachial plexus, ulnar plexus, lumbar-sacral plexus (sciatic nerve), peroneal nerve, and/or the femoral nerve should be included.</td>
</tr>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>PNEUMONIA</th>
<th><p>Inflammation of the lungs caused primarily by bacteria, viruses, and/or chemical irritants, usually manifested by chills, fever, pain in the chest, cough, purulent, bloody sputum. Enter YES if the patient has pneumonia meeting the definition of pneumonia below AND pneumonia not present preoperatively.</p>
<p>Pneumonia must meet one of the following TWO criteria:</p>
<p>Criterion 1.</p>
<p>Rales or dullness to percussion on physical examination of chest AND any of the following:</p>
<p>a. New onset of purulent sputum or change in character of sputum</p>
<p>b. Organism isolate from blood culture</p>
<p>c. Isolation of pathogen from specimen obtained by transtracheal aspirate, bronchial brushing, or biopsy</p>
<p>OR</p>
<p>Criterion 2.</p>
<p>Chest radiographic examination shows new or progressive infiltrate, consolidation, cavitation, or pleural effusion AND any of the following:</p>
<p>a. New onset of purulent sputum or change in character of sputum</p>
<p>b. Organism isolated from blood culture</p>
<p>c. Isolation of pathogen from specimen obtained by transtracheal aspirate, bronchial brushing, or biopsy</p>
<p>d. Isolation of virus or detection of viral antigen in respiratory secretions</p>
<p>e. Diagnostic single antibody titer (IgM) or fourfold increase in paired serum samples (IgG) for pathogen</p>
<p>f. Histopathologic evidence of pneumonia</p>
<p>*If pneumonia was present preoperatively and resolved postoperatively and a new pneumonia is identified within 30 days after surgery, the following criteria must be met in order to report as a postoperative pneumonia occurrence:</p>
<p>- Patient must have completed the antibiotic course for the previous pneumonia.</p>
<p>- Patient must have evidence of a clear chest x-ray after the previous pneumonia and prior to the new pneumonia.</p>
<p>- There must be evidence of a new isolate of micro-organism on culture.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PREGNANCY</td>
<td>Pregnancy is the process by which a woman carries a developing fetus in her uterus, beginning at conception and ending in birth, miscarriage or abortion. Answer Yes if there is documentation in the patient's medical record that the patient is currently pregnant.</td>
</tr>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>PREOPERATIVE SEPSIS</th>
<th><p>Sepsis is a vast clinical entity that takes a variety of forms. The spectrum of disorders spans from relatively mild physiologic abnormalities to septic shock. Please report the most significant level using the criteria below:</p>
<p>1. SIRS (Systemic Inflammatory Response Syndrome): SIRS is a widespread inflammatory response to a variety of severe clinical insults. This syndrome is clinically recognized by the presence of two or more of the following:</p>
<p>- Temp &gt;38 degrees C or &lt;36 degrees C</p>
<p>- HR &gt;90 bpm</p>
<p>- RR &gt;20 breaths/min or PaCO2 &lt;32 mmHg(&lt;4.3 kPa)</p>
<p>- WBC &gt;12,000 cell/mm3, &lt;4000 cells/mm3, or &gt;10% immature (band) forms</p>
<p>- Anion gap acidosis: this is defined by either:</p>
<p>[Na + K] - [Cl + HCO3 (or serum CO2)]. If this number is greater than 16, then an anion gap acidosis is present.</p>
<p>or</p>
<p>Na - [Cl + HCO3 (or serum CO2)]. If this number is greater than 12, then an anion gap acidosis is present.</p>
<p>2. Sepsis: Sepsis is the systemic response to infection. Report this variable if the patient has clinical signs and symptoms of SIRS listed above and one of the following:</p>
<p>- positive blood culture</p>
<p>- clinical documentation of purulence or positive culture from any site thought to be causative</p>
<p>3. Severe Sepsis/Septic Shock: Sepsis is considered severe when it is associated with organ and/or circulatory dysfunction. Report this variable if the patient has the clinical signs and symptoms of SIRS or sepsis AND documented organ and/or circulatory dysfunction. Examples of organ dysfunction include: oliguria, acute alteration in mental status, acute respiratory distress. Examples of circulatory dysfunction include: hypotension, requirement of inotropic or vasopressor agents.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PREVIOUS PCI</td>
<td>The patient has undergone or has had an attempt at percutaneous coronary intervention at any time. This includes either balloon dilatation or stent placement. This does not include valvuloplasty procedures.</td>
</tr>
<tr class="even">
<td>PULMONARY EMBOLISM</td>
<td><p>Lodging of a blood clot in a pulmonary artery with subsequent obstruction of blood supply to the lung parenchyma. The blood clots usually originate from the deep leg veins or the pelvic venous system. Enter "YES" if the patient has a V-Q scan interpreted as high probability of pulmonary embolism or a positive pulmonary arteriogram or positive CT angiogram or positive Spiral CT exam. Treatment usually consists of:</p>
<p>- Initiation of anticoagulation therapy</p>
<p>- Placement of mechanical interruption (e.g. Greenfield Filter), for patients in whom anticoagulation is contraindicated or already instituted.</p></td>
</tr>
<tr class="odd">
<td>REST PAIN/GANGRENE (Y/N)</td>
<td>Rest pain is a more severe form of ischemic pain due to occlusive disease, which occurs at rest and is manifested as a severe, unrelenting pain aggravated by elevation and often preventing sleep. Gangrene is a marked skin discoloration and disruption indicative of death and decay of tissues in the extremities due to severe and prolonged ischemia. Include patients with ischemic ulceration and/or tissue loss related to peripheral vascular disease. Do not include Fournier's gangrene. Report only if within the 30 days preoperatively.</td>
</tr>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>SURGERY SPECIALTY</th>
<th>This is the surgical specialty credited for doing this operative procedure. Many reports, including the Annual Report of Surgical Procedures, are sorted by the surgical specialty. This field should be entered prior to completion of this case. (If you enter '?' in the surgical package, it will display the entire local surgical specialty list and a copy of the national list can be found in the Operations Manual.)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SYSTEMIC SEPSIS</td>
<td><p>Sepsis is a vast clinical entity that takes a variety of forms. The spectrum of disorders spans from relatively mild physiologic abnormalities to septic shock. Please report the most significant level using the criteria below:</p>
<p>1. Sepsis: Sepsis is the systemic response to infection. Report this variable if the patient has clinical signs and symptoms of SIRS. SIRS is a widespread inflammatory response to a variety of severe clinical insults. This syndrome is clinically recognized by the presence of two or more of the following:</p>
<p>- Temp &gt;38 degrees C or &lt;36 degrees C</p>
<p>- HR &gt;90 bpm</p>
<p>- RR &gt;20 breaths/min or PaCO2 &lt;32 mmHg(&lt;4.3 kPa)</p>
<p>- WBC &gt;12,000 cell/mm3, &lt;4000 cells/mm3, or &gt;10% immature (band)</p>
<p>forms</p>
<p>- Anion gap acidosis: this is defined by either:</p>
<p>[Na + K] – [Cl + HCO3 (or serum CO2)]. If this number is greater</p>
<p>than 16, then an anion gap acidosis is present.</p>
<p>or</p>
<p>Na – [Cl + HCO3 (or serum CO2)]. If this number is greater than 12,</p>
<p>then an anion gap acidosis is present.</p>
<p>and one of the following:</p>
<p>- positive blood culture</p>
<p>- clinical documentation of purulence or positive culture from any site thought to be causative</p>
<p>2. Severe Sepsis/Septic Shock: Sepsis is considered severe when it is associated with organ and/or circulatory dysfunction. Report this variable if the patient has the clinical signs and symptoms of SIRS or sepsis AND documented organ and/or circulatory dysfunction. Examples of organ dysfunction include: oliguria, acute alteration in mental status, acute respiratory distress. Examples of circulatory dysfunction include: hypotension, requirement of inotropic or vasopressor agents.</p>
<p>* For the patient that had sepsis preoperatively, worsening of any of the above signs postoperatively would be reported as a postoperative sepsis.</p>
<p>Examples:</p>
<p>A patient comes into the emergency room with signs of sepsis - WBC 31, Temperature 104. CT shows an abdominal abscess. He is given antibiotics and is then taken emergently to the OR to drain the abscess. He receives antibiotics intraoperatively. Postoperatively his WBC and Temperature are trending down.</p>
<p>POD#1 WBC 24, Temp 102</p>
<p>POD#2 WBC 14, Temp 100</p>
<p>POD#3 WBC 10, Temp 99</p>
<p>This patient does not have postoperative sepsis as his WBC and Temperature are improving each postoperative day.</p></td>
</tr>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>SYSTEMIC SEPSIS (continued)</th>
<th><p>Patient comes into the ER with s/s of sepsis - WBC 31, Temp 104. CT shows an abdominal abscess. He is given antibiotics and is taken emergently to the OR to drain the abscess. He receives antibiotics intraoperatively. Postoperatively his WBC and Temp are as follows:</p>
<p>POD#1 WBC 28, Temp 103</p>
<p>POD#2 WBC 24, Temp 102.6</p>
<p>POD#3 WBC 22, Temp 102</p>
<p>POD#4 WBC 21, Temp 101.6</p>
<p>POD#5 WBC 30, Temp 104</p>
<p>This patient does have postoperative sepsis because on postoperative day #5, his WBC and Temperature increase. The patient is having worsening of the defined signs of sepsis.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TUMOR INVOLVING CNS (Y/N)</td>
<td>Space-occupying tumor of the brain and spinal cord, which may be benign (e.g., meningiomas, ependymoma, oligodendroglioma) or primary (e.g., astrocytoma, glioma, glioblastoma multiform) or secondary malignancies (e.g., metastatic lung, breast, malignant melanoma). Other tumors that may involve the CNS include lymphomas and sarcomas. Answer "YES" even if the tumor was not treated. A patient with metastatic cancer with boney mets to spine is a CNS tumor. Answer "NO" if tumor was removed.</td>
</tr>
<tr class="even">
<td>WEIGHT LOSS &gt; 10%</td>
<td>A &gt;10% decrease in body weight in the six month interval immediately preceding surgery as manifested by serial weights in the chart, as reported by the patient, or as evidenced by change in clothing size or severe cachexia. Exclude patients who have intentionally lost weight as part of a weight reduction program.</td>
</tr>
<tr class="odd">
<td>WOUND CLASSIFICATION</td>
<td><p>Indicate whether the wound has been classified by the primary surgeon as:</p>
<p>&gt;&gt; Class 1 - Clean (C):</p>
<p>Respiratory, alimentary, genital, or uninfected urinary tracts are not entered. Uninfected surgical wounds. No inflammation is encountered. Closed primarily and, if necessary, drained with closed drainage. Surgical incisional wounds that occur with nonpenetrating (eg blunt) trauma should be included in this category if they meet the criteria.</p>
<p>[No hollow organ (e.g. bladder, stomach, vagina, lung, etc.) is entered; no breaks in aseptic technique.]</p>
<p>Examples:</p>
<p>- Exploratory laparotomy</p>
<p>- Mastectomy or breast reduction</p>
<p>- Neck dissection</p>
<p>- Nonpenetrating blunt trauma</p>
<p>- Thyroidectomy</p>
<p>- Total hip replacement</p>
<p>- Vascular operations (e.g. AAA, AV fistula, CEA, aortoiliac bypass)</p>
<p>- Hernia repair</p>
<p>- CABG, AVR</p>
<p>- Craniotomy, majority neurosurgery</p>
<p>- Pleura biopsy</p>
<p>- Sternotomy</p>
<p>- Abdominoplasty</p>
<p>- Bone anchored hearing aids (BAHA)</p>
<p>- Penile prosthesis placement</p>
<p>- Dupuytren’s release, finger</p>
<p>- Liposuction</p>
<p>- Carpal tunnel release</p>
<p>- Hydrocele repair</p></td>
</tr>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>WOUND CLASSIFICATION (continued)</th>
<th><p>&gt;&gt; Class 2 - Clean/Contaminated (CC):</p>
<p>Respiratory, alimentary, genital, or urinary tracts are entered under controlled conditions and without unusual contamination. Specifically, procedures involving the biliary tract, appendix, vagina, and oropharynx are included in this category, provided no evidence of infection or major breaks in technique are encountered.</p>
<p> </p>
<p>(Hollow organ entered but controlled; no inflammation; primary wound closure; minor break in aseptic technique; mechanical drain used.)</p>
<p>Examples:</p>
<p>- Bronchoscopy</p>
<p>- Routine appendectomy</p>
<p>- Cholecystectomy (e.g., any approach)</p>
<p>- Laryngectomy</p>
<p>- Small bowel resection</p>
<p>- Oropharynx entered</p>
<p>- GYN procedures</p>
<p>- Vagina entered</p>
<p>- Whipple pancreaticoduodenectomy</p>
<p>- Pulmonary resection</p>
<p>- Transurethral resection of prostate</p>
<p>- Head &amp; Neck cancer operations (e.g., oropharynx)</p>
<p>- Sigmoid colectomy</p>
<p>- Minor break in technique</p>
<p>- Gastrointestinal or respiratory tract entered without significant spillage</p>
<p>- Genitourinary tract entered in absence of infected urine</p>
<p>&gt;&gt; Class 3 - Contaminated (D):</p>
<p>Open fresh, accidental (e.g. traumatic) wounds. Procedures that have major breaks in sterile technique (eg, open cardiac massage) or gross spillage from the gastrointestinal tract and incisions in which acute, nonpurulent inflammation is encountered are included in this category.</p>
<p>Examples:</p>
<p>- Appendectomy for gangrenous appendicitis</p>
<p>- Bile spillage during cholecystectomy</p>
<p>- Diverticulitis</p>
<p>- Laparotomy for penetrating injury with intestinal spillage</p>
<p>- Entrance of genitourinary or biliary tracts in presence of infected urine or bile</p>
<p>- Necrotic tissue without evidence of purulent drainage (e.g. dry gangrene)</p>
<p>&gt;&gt; Class 4 - Dirty/Infected (I):</p>
<p>Old traumatic wounds that have retained devitalized tissue and those that involve existing clinical infection or perforated viscera. This definition suggests that the organisms causing postoperative infection were present in the surgical field before the procedure.</p>
<p>[Untreated, uncontrolled spillage from an internal organ; pus in operative wound; open suppurative wound; severe inflammation.]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>WOUND CLASSIFICATION (continued)</th>
<th><p>Examples:</p>
<p>- Excision and drainage of abscess</p>
<p>- Myringotomy for otitismedia</p>
<p>- Perforated bowel</p>
<p>- Peritonitis (abdominal exploration for acute bacterial peritonitis)</p>
<p>- Acute bacterial inflammation, without pus</p>
<p>- Transection of 'clean' tissue for the purpose of surgical access to a collection of pus</p>
<p>- Traumatic wound with foreign bodies, fecal contamination, or delayed treatment, or all of these; or from dirty source</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*(This page included for two-sided copying.)*

# Appendix B: Updated Definitions for Cardiac Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following field definitions are updated in patch SR\*3\*160.

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>AORTIC STENOSIS</th>
<th><p>Indicate the severity of any aortic stenosis documented. This question should be answered using either the left ventricular angiogram (hemodynamic cath data) or the cardiac ultrasound examination. Numbers may be converted to describe the severity of the aortic stenosis on the cardiac cath report to the adjectives describing the severity: 1+ = mild, 2 or 3+ = moderate, and 4+ = severe. Both transvalvular gradient and estimated valve orifice area are used to assess the severity of obstruction (stenosis) of a valve. The transvalvular pressure gradient is obtained by converting the velocity of blood flow across the valve measured by the Doppler principle to pressure drop using the Bernoulli equation. The pressure drop, which is dependent on flow, can be converted to estimated valve orifice area if flow is known. If the echo report uses an adjective to describe the severity of stenosis, indicate the corresponding adjective. Use the following to convert mean (not peak) transvalvular gradients, orifice areas, or both, to the descriptive categories. Indicate the one most appropriate response:</p>
<p>None/Trivial - The mean pressure gradient is &lt; 5 mm Hg, and/or orifice area is &gt; 2.5 cm2, and/or the aortic valve leaflets or aortic flow velocity is stated to be normal (&lt; 1.0 M/sec).</p>
<p>Mild - The mean pressure gradient is 5 - 20 mm Hg and/or the orifice area is 1.7 - 2.5 cm2</p>
<p>Moderate - The mean pressure gradient is &gt;20 - 50 mm Hg and/or the valve orifice area is 1.0 -1.6 cm2</p>
<p>Severe - The mean pressure gradient is &gt; 50 mm Hg and/or the valve orifice area is &lt; 1.0 cm2</p>
<p>NS - If no study was performed, entering "NS" for "No Study/Unknown" is also allowed.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CONGESTIVE HEART FAILURE</td>
<td><p>Indicate whether the patient has congestive heart failure if the patient chart or patient self-report indicates a history of congestive heart failure within the 30 days before surgery. Congestive heart failure is defined as the inability of the heart to pump a sufficient quantity of blood to meet the metabolic needs of the body or can do so only at increased ventricular filling pressure. Common manifestations are identified:</p>
<p>From the history:</p>
<p>1) Abnormal limitation in exercise tolerance due to dyspnea, fatigue or angina.</p>
<p>2) Orthopnea (dyspnea on lying supine).</p>
<p>3) Paroxysmal nocturnal dyspnea (PND) - awakening from sleep with dyspnea which is relieved by assuming an upright posture).</p>
<p>From the physical examination:</p>
<p>4) Increased jugular venous pressure.</p>
<p>5) Pulmonary rales on physical examination.</p>
<p>From the chest x-ray:</p>
<p>6) Cardiomegaly, and</p>
<p>7) Pulmonary vascular engorgement.</p></td>
</tr>
</tbody>
</table>

| Field | Updated Description |
|-------|---------------------|

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>CONGESTIVE HEART FAILURE (continued)</th>
<th><p>The New York Heart Association functional classification is commonly used as a subjective assessment of the severity of congestive heart failure. If none of the above manifestations have been present, or congestive heart failure is not mentioned as an active problem in the 30 days before surgery, indicate Class I. Any mention of above manifestations requires the indication of a stage other than Class I. Indicate the one most appropriate response:</p>
<p>Class I - cardiac disease, but no symptoms of abnormal fatigue, dyspnea or angina.</p>
<p>Class II - slight limitation of physical activity by fatigue, dyspnea, or angina. The patient gets unusual fatigue, dyspnea, and/or angina only upon performing more strenuous activities, such as climbing two or more flights of stairs without stopping.</p>
<p>Class III - marked limitation of physical activity by fatigue, dyspnea, or angina. The patient gets unusual fatigue, dyspnea, and/or angina upon performing ordinary activities, such as walking several blocks or climbing a flight of stairs.</p>
<p>Class IV - symptoms at rest and/or inability to carry out any physical activity without symptoms of fatigue, dyspnea or angina. The patient has symptoms of unusual fatigue, dyspnea, and/or angina at rest or when performing minimal activity, such as walking across the room.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ON VENTILATOR &gt;48 HOURS</td>
<td>Indicate if the total duration of ventilator-assisted respiration within 30 days post-operatively was greater than or equal to 48 hours.</td>
</tr>
<tr class="even">
<td>PERIOPERATIVE MI</td>
<td><p>Indicate the presence of a peri-operative MI if at least one of the following criteria occurs either intraoperatively or postoperatively within 30 days:</p>
<p>1. Evolutionary ST-segment elevations</p>
<p>2. Development of new Q-waves in two or more contiguous ECG leads</p>
<p>3. New or presumably new LBBB pattern on the ECG.</p></td>
</tr>
<tr class="odd">
<td>PREOP CIRCULATORY DEVICE</td>
<td><p>Indicate whether there was any use of any device to assist ventricular function at the time the patient presents for surgery. Indicate the one appropriate response:</p>
<p>None - No New Mechanical Circulatory Device was placed.</p>
<p>IABP - An intra-aortic balloon pump was placed to assist ventricular function. VAD - A ventricular assist device (e.g., LVAD, BIVAD) was placed to assist ventricular function.</p>
<p>Artificial Heart - An artificial heart was placed to assist ventricular function.</p>
<p>Other - An other type of Mechanical Circulatory Device was placed.</p></td>
</tr>
</tbody>
</table>

# Appendix C: Updated Laboratory Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following laboratory tests, accessed using the *Laboratory Test Results (Enter/Edit)* \[SROA LAB\] option, are updated in patch SR\*3\*160.

|                 |                         |
|-----------------|-------------------------|
| Lab Test Result | Change in functionality |

| Hemoglobin A1c | Hemoglobin A1c was added for non-cardiac assessments. Only preoperative values are collected. |
|----------------|-----------------------------------------------------------------------------------------------|

All laboratory fields are updated to assume a past date if the user enters a date without a year.

![](sr-3-160-surgery-nsqip-cicsp-2007-release-notes/002.png) If the medical center is not a cardiac facility, upon completion of the installation of patch SR\*3\*160, use the edit option of VA FileMan to enter the appropriate data name(s) for HEMOGLOBIN A1C in the LABORATORY DATA NAME field (#1) of the RISK MODEL LAB TEST file (#139.2). If an appropriate data name does not exist, leave blank.

If the medical facility is a cardiac facility, this process should have been completed already.

*(This page included for two-sided copying.)*