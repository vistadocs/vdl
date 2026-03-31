---
title: SD*5.3*264/277 PCMM Enhancements for Direct Primary Care User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: PCMM Enhancements for Direct Primary Care
app_code: PCMM
app_name: Primary Care Management Module
section: CLI
app_status: active
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*264
group_key: "PCMM:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/001.png)
audience: 
keywords: 
  - care
  - direct
  - primary
  - time
  - table
  - contents
  - patient
  - ftee
  - pcmm
  - patients
page_count: 0
word_count: 5395
section_count: 15
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_277.um-final.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/sd_53_277.um-final.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=95"
---

![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/001.png)

Scheduling V. 5.3Primary Care Management Module (PCMM)ENHANCEMENTS forDIRECT PRIMARY CARE(SD\*5.3\*264)User Guide

January 2003

#######  

####### Table of Contents

DETERMINING PRIMARY CARE DIRECT PATIENT CARE TIME

# I. BACKGROUND


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [I. BACKGROUND](#i-background)
- [II. PURPOSE](#ii-purpose)
- [III. RESPONSIBILITY](#iii-responsibility)
- [IV. PROCEDURES](#iv-procedures)
- [Local facilities will continue to determine panel size for their individual providers. Only the local level knows what level of support staff, space, team structure etc exist that may affect appropriate panel expectations. Because all facilities will be using the same definition of PCDPC, time allotted to non-direct care will be consistent. (See “Definitions.”)](#local-facilities-will-continue-to-determine-panel-size-for-their-individual-providers-only-the-local-level-knows-what-level-of-support-staff-space-team-structure-etc-exist-that-may-affect-appropriate-panel-expectations-because-all-facilities-will-be-using-the-same-definition-of-pcdpc-time-allotted-to-non-direct-care-will-be-consistent-see-definitions)
- [# # V. DEFINITIONS](#v-definitions)
  - [A. Direct Patient Care](#a-direct-patient-care)
  - [B. Primary Care Direct Patient Care](#b-primary-care-direct-patient-care)
  - [> Primary Care Direct Patient Care (PCDPC) is defined as the time to prepare for, provide for, and follow-up on the clinical care needs of outpatient, primary care patients.](#primary-care-direct-patient-care-pcdpc-is-defined-as-the-time-to-prepare-for-provide-for-and-follow-up-on-the-clinical-care-needs-of-outpatient-primary-care-patients)
  - [## C. Administration](#c-administration)
  - [D. Education](#d-education)
  - [E. Research](#e-research)
- [# VI. EXAMPLES](#vi-examples)
- [# VII. FREQUENTLY ASKED QUESTIONS (FAQs)](#vii-frequently-asked-questions-faqs)
  - [> 1. Administrative Time](#1-administrative-time)
- [How do I account for Women’s Clinic?](#how-do-i-account-for-womens-clinic)
- [VIII. USING THE PCMM ENHANCEMENTS SOFTWARE](#viii-using-the-pcmm-enhancements-software)
- [## A. Background](#a-background)
  - [B. Introduction](#b-introduction)
  - [B. Orientation](#b-orientation)
- [This user manual will assume that readers have a working knowledge of the PCMM Graphical User Interface (GUI) and VistA software, also other VistA software applications. Screen displays may vary among different sites and you may not see the data on your monitor exactly as shown in this manual. Although screens are subject to modification, the major menu options, as they appear in this manual, are fixed and are not subject to modification (except by the package developer).](#this-user-manual-will-assume-that-readers-have-a-working-knowledge-of-the-pcmm-graphical-user-interface-gui-and-vista-software-also-other-vista-software-applications-screen-displays-may-vary-among-different-sites-and-you-may-not-see-the-data-on-your-monitor-exactly-as-shown-in-this-manual-although-screens-are-subject-to-modification-the-major-menu-options-as-they-appear-in-this-manual-are-fixed-and-are-not-subject-to-modification-except-by-the-package-developer)
  - [## C. The new PCMM enhancements:](#c-the-new-pcmm-enhancements)
  - [ENTER AND EDIT THE “DIRECT PC FTEE” for Primary Care](#enter-and-edit-the-direct-pc-ftee-for-primary-care)
  - [Providers (PCPs) who are already assigned to a PC Position.](#providers-pcps-who-are-already-assigned-to-a-pc-position)
    - [CREATE A NEW STAFF ASSIGNMENT AND ENTER “DIRECT PC FTEE.”](#create-a-new-staff-assignment-and-enter-direct-pc-ftee)
    - [### ### ### Direct PC FTEE REPORT](#direct-pc-ftee-report)
    - [#### The PCMM Direct Primary Care FTEE Report can only be printed from VistA. Starting at the “Scheduling Manager’s Menu,” enter/select the “Outputs Option,”](#the-pcmm-direct-primary-care-ftee-report-can-only-be-printed-from-vista-starting-at-the-scheduling-managers-menu-enterselect-the-outputs-option)
- [Select \<SMA\> Scheduling Manager's Menu Option: ?](#select-sma-scheduling-managers-menu-option)
  - [D. AUTOMATIC INACTIVATION UPON DATE OF DEATH ENTRY](#d-automatic-inactivation-upon-date-of-death-entry)
  - [> Automatic inactivation of patients from their Primary Care team and provider panels will occur following entry of a date of death. On installing SD\5.3\264 a postinit routine, POST^SCMCTSK, is initiated that identifies patients with a date of death at that time. If deceased patients have active team/position assignments, it discharges/ inactivates them from their panels.](#automatic-inactivation-of-patients-from-their-primary-care-team-and-provider-panels-will-occur-following-entry-of-a-date-of-death-on-installing-sd53264-a-postinit-routine-postscmctsk-is-initiated-that-identifies-patients-with-a-date-of-death-at-that-time-if-deceased-patients-have-active-teamposition-assignments-it-discharges-inactivates-them-from-their-panels)
- [# # IX. TRANSMISSION TO NPCDB](#ix-transmission-to-npcdb)
- [X. SECURITY](#x-security)
- [XI. TECHNICAL INFORMATION](#xi-technical-information)
The Assistant Deputy Undersecretary for Health, in a memo to the VHA CIO dated February 1, 2002, expressed concern with our <u>capacity</u> within the system to take care of patients seeking VA care. One vehicle used to assess capacity is the VistA Primary Care Management Module (PCMM.) This application is used to assign patients to primary care providers and is an important component of waiting time reduction. That memo set forth the task to include the amount of time that each primary care provider is available to see patients in their primary care clinics in PCMM.
Patch SD\*5.3\*264 was released at the same time as the Electronic Wait List patch, SD\*5.3\*263, since it includes the PCMM functionally related to the Electronic Wait List.
During “Patient Assignment” to a PC Team or Position/Provider, if the Team or Position
is over it’s maximum panel size, the user will be asked if the patient should be put on the
Electronic Wait List.

# II. PURPOSE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this paper is to Provide Clear and Consistent Guidelines to VHA Primary Care Practices.

A. A PCMM enhancement was developed to meet the pressing need for consistent and accurate data that reflects the capacity of each site and the VHA system to make primary care available to patients. This, in part, was accomplished with the assistance of a user group made up of physicians and PCMM users, who determined the most reliable way to collect data is for each facility to document direct patient care time and non-patient care time in the same manner.
2.  DSS (Decision Support System) already has an established set of guidelines

for the definition of Direct Patient Care, which are applicable to Primary Care Direct Patient Care (PCDPC) and are incorporated into the definition of PCDPC. The advantage of using the DSS guidelines is that these guidelines have been in use and have been tested over time.

# III. RESPONSIBILITY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Development team: Develops enhancements and guarantees release of national packages.
2.  User Group: Defines requirements for the PCMM enhancements.

# IV. PROCEDURES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each facility’s DSS Coordinator will need to insure that the DSS subgroup "Primary Care," under Direct Patient Care, is used to map the time Primary Care Providers spend in taking care of primary care panels. DSS definitions of Administration, Education, and Research are also utilized in determining the Primary Care Direct Patient Care time.

Thus, the DSS Primary Care time and the Direct Primary Care FTEE need to reflect the same accurate information. The DSS Coordinator and the PCMM Coordinator need to

assure this consistency.

Each facility’s DSS Coordinator will need to review their DSS mapping to ensure that activities of each clinician are allocated to the appropriate service. Many clinicians, for example, provide primary care and specialty care services.

Rather than adding up available hours, DSS works from the approach that a clinical provider's time is involved in those tasks that are necessary to provide clinical care. Resources are subtracted only if the individual is doing something that meets the criteria for exclusions to direct patient care. The definition of hours worked for a full time Primary Care Provider (PCP) assumes that vacation time, sick time, break time, and other incidental times are taken into account when determining workload.

# Local facilities will continue to determine panel size for their individual providers. Only the local level knows what level of support staff, space, team structure etc exist that may affect appropriate panel expectations. Because all facilities will be using the same definition of PCDPC, time allotted to non-direct care will be consistent. (See “Definitions.”)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # V. DEFINITIONS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The definitions of Direct Patient Care, Administration, Research and Education listed below are taken from the DSS definitions. The Primary Care Direct Patient Care term and definition were developed using the DSS definition of Direct Patient Care. It’s

purpose is to provide guidance in determining the Direct PC FTEE (Direct Primary Care Full Time Equivalent Employee) value to enter in PCMM.

## A. Direct Patient Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Direct patient care is defined as the time to prepare for, provide for, and follow-up on the clinical care needs of patients. This will include all time spent in reviewing patient data, discussions about the care with colleagues, reviewing the medical literature, and contacting the patient or caregivers to discuss their needs. In DSS, this time is allocated to various direct care departments in proportion to the time spent in each of these activities.

> *EXAMPLES:*

- Time spent rendering care to patients by physicians, nurses, residents, technicians, and other allied health personnel.
- Time spent in direct supervision of house staff providing direct patient

care, for example, serving as an attending for house staff clinics.

- Time spent charting patient treatment as well as ordering and reviewing

patient tests and consultations.

## B. Primary Care Direct Patient Care 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## > Primary Care Direct Patient Care (PCDPC) is defined as the time to prepare for, provide for, and follow-up on the clinical care needs of outpatient, primary care patients.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Primary Care Direct Patient Care covers all those activities involved in providing primary care to a panel of patients. These include the following:

- Time with patients and family in clinic
- Review of patient records
- Documentation of patient care
- Telephone care
- Group clinics
- Discussion of patient care issues with consultants and other staff members
- Attendance at educational programs aimed at maintaining or improving

clinical skills

- Participation in staff meetings, which are focused on the delivery of primary

care

- Time spent in delivering patient care with medical students present
- Precepting residents while they deliver primary care
- Precepting midlevel providers while they deliver primary care

> <u>Activities that should not be mapped to Primary Care Direct Patient Care</u> include the following:

- Provision of specialty care to patients who are not in your primary care panel.
- Inpatient hospital care (even for your own primary care patients). To maintain comparability across the system, the decision has been made that determination of primary care panel size should be based on outpatient care only.
- Activities which meet criteria for Administration
- Activities which meet criteria for Education
- Activities which meet criteria for Research

## ## C. Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Administrative time includes time spent on managerial or administrative duties generally at the level of the service, Medical Center or nationally, both within and outside the VA. This time for professional staff is allocated as administrative time.

> *EXAMPLES:*

- Time spent in support of service-wide administrative activities, such as completing performance reviews, hospital and Headquarters reporting requirements.
- Time spent managing a program within the service or hospital-wide
- Time spent working on service of hospital-wide committees
- Time spent working on medical school committees
- Time spent serving on state and national committees, advisory boards or professional societies

## D. Education

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Education is defined as time spent in formal training activities (didactic education) generally not directly involving patient care. This can include preparation and actual classroom or lecture time for educators or presenters. If the education is directly related to the staff’s patient care responsibilities or an expectation of their supervisor to maintain their employment, it is considered the cost of direct patient care. For example, learning about the operation of new equipment in the cardiac catheterization lab or attending a mandatory QM in-service, are both considered the cost of direct patient care activities and not education. In addition, time spent on house staff teaching rounds is considered the cost of direct patient care and not education.

> *EXAMPLES:*

- Time spent giving conferences in the community or nationally
- Time spent in classroom teaching of medical school curriculum
- Time spent in classroom teaching of residents and fellows
- Time spent in managing a resident, fellow or student teaching program
- Time spent in the administrative support of a VA approved educational program in including such activities as processing the paperwork to bring the trainees and residents on-board, processing of timecards for the residents and trainees, and preparing rotation schedules for the residents.

## E. Research

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Research is defined as the time spent performing formal approved research or in activities directly in support of approved research. Formal approved research is research that either is approved through the hospital research review process or has the approval of the employee’s service chief. Support activities include time spent by the investigator in direct support of research activities. Research can be laboratory, clinical or health services research.

> *EXAMPLES:*

- Time spent working in an actual research laboratory or controlled type setting, which involves no direct patient care or treatment.
- Time spent serving on hospital or affiliate research committees
- Time spent in supervision of student, resident or fellow research
- Time spent writing for publication
- Time spent attending meetings explicitly related to research activities
- Time spent presenting papers at research meetings
- Time spent sitting on a national study section or grant approving board.

# # VI. EXAMPLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following examples help illustrate how the DSS Coordinator determines what time to map for Primary Care Providers with a range of different responsibilities. The DSS Coordinator and the PCMM Coordinator must review this information together and assure that DSS and PCMM contain the same accurate values for each Primary Care Provider’s time.

1. Full time Primary Care. Dr. Jones is a full-time VA staff physician working in a Community Based Outpatient Clinic. His clinical responsibilities consist entirely of providing outpatient primary care to a panel of patients. He does not provide any specialty care or inpatient care. He is not responsible for managing any programs and does not serve on any medical center or VISN committees. He is not involved in any educational programs or research.

Dr. Jones should be mapped as 1.00 Direct PC FTEE (Direct Primary Care FTEE.)

2. Administration. Dr. Sanchez is the Associate Chief of Staff/Ambulatory Care at a VAMC. She spends half of her time in her administrative responsibilities as ACOS/AC. She manages the outpatient programs and serves on a variety of medical center and VISN committees. She spends the other half of her time as a primary care provider and follows a panel of patients that is half the size of the full-time primary care providers at her practice site. She does not provide any specialty care or inpatient care. She is not involved in any educational programs or research.

Dr. Sanchez should be mapped 0.50 Direct PC FTEE and 0.50 FTEE Administration.

3. Education. Dr. Shah is an academic primary care general internist working at a VAMC affiliated with a medical school. He is the Clerkship Director for the third year medical student Ambulatory Care rotation. He spends one hour a day giving a lecture to the medical students. In addition, he spends approximately three hours a week in various administrative tasks arising from this position such as developing curriculum, planning schedules and attending meetings at the medical school. He spends the remaining 80% of his time providing primary care to a panel of patients that is 80% the size of full-time primary care providers in his practice. He provides no specialty or inpatient care, and is not involved in research.

Dr. Shah should be mapped 0.80 Direct PC FTEE and 0.20 FTEE Education.

4. Research. Dr. Gray is a VA staff physician who recently received a full-time career development award in health services research. She continues to see patients and provide primary care to a panel of patients one day a week. The other four days a week she spends involved in her research activities. She provides no specialty care or inpatient care. She is not involved in any educational activities.

Dr. Gray should be mapped 0.20 Direct PC FTEE and 0.80 FTEE Research.

5. Specialty Care. Dr. Li is a full-time VA staff physician who spends ½ of his time providing primary care to a panel of patients and ½ of his time as pulmonary consultant providing consultation on patients followed by other primary care providers. He is assigned a panel ½ the size of the full-time primary care providers in his practice. He provides no inpatient care. He is not involved in any educational programs or research.

Dr. Li should be mapped 0.50 Direct PC FTEE and 0.50 FTEE to Pulmonary Medicine Direct Patient Care.

6. Inpatient Care. Dr. Smith is a full-time staff physician at a VAMC, which has an inpatient medical acute care unit. For about 6 months of the year, she serves as attending physician for one of the inpatient medicine teams. This activity takes about 4 hours per day so when she is attending she spends about ½ of her time on inpatient care and ½ on outpatient primary care. During the six months when she is not attending, she spends full time providing care to her panel of primary care patients. She follows a panel that is 75% size of full time primary care providers. She does not provide any specialty care and is not involved in any educational programs or research.

Dr. Smith should be mapped 0.75 Direct PC FTEE and 0.25 FTEE to Acute Inpatient Direct Patient Care.

# # VII. FREQUENTLY ASKED QUESTIONS (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## > 1. Administrative Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The providers at our clinic are given ½ a day a week where no patients are scheduled into their clinics. This allows them to catch up on telephone calls, filling out forms, writing letters, etc. We have called this “Administrative Time”. Should this be mapped to administrative time or to Primary Care Direct Patient Care?Response: It should be mapped to Primary Care Direct Patient Care. Administrative time includes the management of medical center programs or participation at medical center, VISN etc level committees. Providing primary care to a panel of patients involves a significant amount of activity outside of face-to-face time with the patients in the clinic office. The activities described for this “administrative time” relate to providing patient care to a panel of patients. These other activities are important components of direct patient care and should be included in the time mapped to Primary Care Direct Patient Care.

2. Telephone care

#### Is time to return phone calls from my patients direct patient care?Response. Yes. Time to return phone calls or complete telephone follow-up for your patients is part of providing primary care to a panel of patients and should be included as part of PCDPC. If you schedule a “Telephone Visit” with a patient in lieu of a face-to-face visit or create a “Telephone Visit Clinic,” this time is included in primary care direct patient care hours. This type of visit or clinic is one of the high leverage changes included in the Advance Clinic Access program and may serve to de-compress a provider’s schedule and in some cases, may save the patient from having to travel a long distance for a clinic visit.

#### #### Appointment length

#### #### Does patient appointment length or the use of “carve outs” (open time without prescheduled appointments) for urgent visits affect the measurement of Primary Care Direct Patient Care?

> Response. No. PCDPC represents the net total of the time dedicated to providing primary care to a panel of patients. Some providers find 15 or 20 minute appointments work best for their practice style and others find 30 minutes is needed. Some providers use “carve outs” in which time in clinic is kept open for urgent visits, and others have all their time available in the scheduling package. In either case, the idea is to manage your patient panel, not visits.

4\. Midlevel Supervision

> I have a certain number of hours set aside to supervise midlevels while they provide care in Primary Care clinic. Should this be counted as Primary Care Direct Patient Care?

> Response. Yes. Midlevel supervision usually occurs one of two ways: either scheduled interaction time, or questions that are asked in the midst of the clinic day – between patient visits. In either case, it is time dedicated to the provision of primary care to a panel of primary care patients. Of note, in PCMM, a midlevel can be either a Primary Care Provider, or an Associate Provider with a Precepting Physician. This decision is up to local discretion. If the medical center decides to have the midlevel as an Associate Provider, and the MD as the Precepting Physician, the patients would be included in the MD’s panel, as precepted patients, with the midlevel as the associate provider. Thus, Osteopaths, Nurse Practitioners, and Physician Assistants may be Associate Providers or Primary Care Providers.

5. Precepting Students and Residents in the Clinic

> Sometimes in clinic, I have a medical student accompanying me while I see patients. I also spend ½ day a week precepting residents while they see patients in a residency primary care continuity clinic. Should this time be mapped to education?Response. No. Even if students or residents are present, time spent providing direct patient care is mapped to Direct Patient Care. Education time should only include time that does not involve providing patient care. See definitions and criteria given above.

6. CMEOur staff generally spends an hour a week at a Medical Grand Rounds. The topics are clinical and related to their patient care responsibilities. Should these be mapped to education?Response. No. Continuing medical education that is related to direct patient care falls into the direct patient care category. Education activities should include only those activities such as giving lectures or managing educational programs that do not involve providing care to patients. See the definitions and criteria given above.
7. Level of Clinic Support.There are two CBOCs at our Medical Center. In each CBOC, there is one full-time physician and one full-time nurse practitioner. At CBOC A, there is a high level of support staff. There are seven exam rooms, two for each of the providers and one for each of the support staff. The providers are allowed to dictate their notes. In CBOC B, there is only one medical clerk, one room for each provider and no dictation. Should the amount of provider time in primary care direct patient care be different in the two CBOCs?Response. No. In each CBOC, the amount of provider resources is the same; 1.0 MD and 1.0 NP. However, many factors affect the appropriate number of patients that should be in a provider’s panel. The amount of support staff, space and administrative support can affect the number of patients that a given provider can follow. Therefore, the VA does not set a national policy on the specific number of patients that must be provided for by each provider FTEE. This is left as a local decision. Determination of the amount of provider resources, as measured by PCDPC, is only one factor that determines the appropriate panel size.
8. Staff MeetingsOur staff meets on a regular basis to discuss management of the clinic. We review policies related to and problems encountered in delivering patient care. Should this be mapped to administrative time or direct patient care?Response. Conceptually the administration category involves responsibilities and activities that are distinct from patient care responsibilities. Examples would include time required to manage a program (writing policies, collecting QA data, attending meetings, planning meetings, etc). A certain number of team and staff meetings are required for communication among a team providing direct patient care. Staff meetings involving patient care providers, which focus on the functioning of the clinic and the delivery of direct patient care, are most appropriately included in direct patient care time. It is acknowledged that sometimes the border between these activities can get difficult to delineate and a degree of local decision-making and differentiation is allowed for such decisions.
9. Salary SourceWe have a career development awardee that spends one week providing care to a panel of primary care patients. This physician’s salary comes from a career development award and is not part of our Primary Care Service Budget. Should this individual’s time still be mapped to Primary Care Direct Patient Care?Response. Yes. The key point is this individual’s time is available to provide primary care to a panel of patients. In some cases, the salary may be paid by other clinical services, by Research, by contract or the employee may even be a WOC (Without Compensation) volunteer physician. However, in all cases, the provider’s time is available to provide primary care to a panel of patients and thus should be included in PCMM as Primary Care Direct Patient Care, regardless of the source of their salary.
10. Our medical residents spend ½ a day a week in the clinic. Should their time bemapped as physician time?Response. No. Each resident must have a precepting physician. The time of the precepting physician should be mapped to Primary Care Direct Patient Care. However, residents are a different category and their time should not to be included for the purposes of provider resource mapping for PCMM.
11. Mapping General Internal Medicine FellowsWe have a general internal medicine fellow at our medical center. He spends one day a week following a panel of primary care patients. He has completed his Medicine Residency Program and is board certified in Internal Medicine. Should his time be mapped as physician time?Response. No. The VA has decided that all staff that is being paid as house staff by the VA must have a precepting physician. General internal medicine fellows are unique in that they are already board certified in the field in which they are receiving advanced training. This particular situation is a “gray area” but the VA has decided that they should not be considered staff physicians and are mapped in the same way as residents.
12. Contract ClinicsWe have a CBOC that provides primary care under a contract. Should these patients be entered into PCMM and how should we handle the mapping of provider resources and expected panel?Response. The VA would like all patients being provided primary care to be entered into PCMM and assigned a provider and team. This is true for contract primary care services as well as services provided by VA staff. Therefore, in the case of a contract clinic, a PCMM team should be created and these patients enrolled into that team. A best estimate of the provider FTEE and the number of patients that can be followed at that clinic should be made and entered into PCMM.
13. Women’s Clinic

# How do I account for Women’s Clinic?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Response. It depends upon whether the Women’s Clinic in question is providing primary care or specialty care. Some women’s clinics serve as primary care clinics, providing ongoing primary care for women, including preventive care and care for common outpatient gynecological problems. The scope of Women’s Health Primary Care is defined in the VHA Handbook 1330.1 VHA Services for Women Veterans. Such clinics should have the clinic stop code 322, and the provider’s time included in PCDPC. Other Women’s clinics function as specialty consult clinics for Ob/Gyn problems.

> A specialist evaluates problems outside the scope of the patient’s primary care provider’s expertise. Such clinics should have the clinic stop code 404.

14. Inpatient Attending Months

> At our medical center, many Primary Care physicians spend two months a year as inpatient attending. Should the amount of time mapped to PCDPC be changed for those two months, or can we average it over the year?

> Response. For many providers, their responsibilities can change from month to month. Providing primary care involves establishing an ongoing relationship, and the expected panel size cannot be expected to change from month to month. In most institutions, responsibilities such as these are assigned on a yearly schedule. It is better to consider time allocation on a yearly basis.

# VIII. USING THE PCMM ENHANCEMENTS SOFTWARE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ## A. Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary Care Management Module is one of the ways that VHA measures its’ capacity for patient care. These PCMM enhancements were developed to meet the pressing need for consistent and accurate data on the capacity to provide primary care to patients. The most reliable way to collect data is for each facility to document direct patient care time and non-patient care time in the same manner. The Decision Support System (DSS) already has an established set of guidelines for the definition of Direct Patient Care that is applicable to Primary Care Direct Patient Care (PCDPC.) Therefore, DSS guidelines are incorporated into the definition of Primary Care Direct Patient Care (PCDPC). The entry of PCDPC in PCMM must be consistent with the Direct Primary Care time entered in DSS. Thus, the PCMM and DSS Coordinators need to collaborate to assure the same accurate and consistent data is entered in both packages. For guidance in arriving at the FTEE for each Primary Care Provider (PCP), please refer to the previous section of this document and DSS documents.

## B. Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary addition to the Primary Care Management Module (PCMM) with this release is the creation of a Primary Care Direct Patient Care time field called Direct PC FTEE (Full Time Equivalent Employee.) This PCMM Enhancements for Direct Primary Care (SD\*5.3\*264) User Guide provides instruction in the use of the new field and report for Primary Care Direct Patient Care (PCDPC) time.

Access to entering and editing this new field, called Direct PC FTEE (Full Time Equivalent Employee,) is only through the PCMM GUI screens. The FTEE Report is available only through PCMM VistA. Each Primary Care Provider needs their Direct PC FTEE entered. Only medical doctors, doctors of osteopathy, nurse practitioners, and physician assistants designated as Primary Care Providers (PCP) should have an entry in the Direct PC FTEE field.

The Direct PC FTEE can be entered and edited for existing positions from the Team Menu in PCMM GUI. For new staff assignments to positions, the FTEE can be entered on the Staff Assignment screen. After being entered, the FTEE cannot be edited from the Staff Assignment screen. See screen shots on the following pages.

Another enhancement is that patients will be automatically inactivated from their Primary Care team and provider panels when a date of death is entered. A postinit routine will run that will discharge patients from active Team/Position Assignments who have a Date of Death entered at the time of the installation. A new protocol will continue to discharge/inactivate patients from panels upon entry of a date of death. If a date of death is entered in error and then deleted, the patient’s previous panel assignments will be restored.

In summary, the changes to PCMM with this patch and the new executable file include:

1.  Entering and editing the new field called “Direct PC FTEE” (Full Time Equivalent Employee.)
2.  Printing the “Direct PC FTEE Report.”
3.  Automated inactivation of patients from Primary Care Team and Provider panels when a date of death is entered in the Registration package.
4.  Restoring Primary care panel assignments when a patient’s date of death was entered in error.

## B. Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# This user manual will assume that readers have a working knowledge of the PCMM Graphical User Interface (GUI) and VistA software, also other VistA software applications. Screen displays may vary among different sites and you may not see the data on your monitor exactly as shown in this manual. Although screens are subject to modification, the major menu options, as they appear in this manual, are fixed and are not subject to modification (except by the package developer).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## C. The new PCMM enhancements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ENTER AND EDIT THE “DIRECT PC FTEE” for Primary Care 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Providers (PCPs) who are already assigned to a PC Position. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only medical doctors, doctors of osteopathy, nurse practitioners, and physician assistants may be Primary Care Providers. Each PCP should have their “Direct PC FTEE” entered. The Direct PC FTEE must coincide with the entry in DSS for the provider’s Direct Primary Care time. The DSS Labor Mapping Definitions need to be adhered to. Therefore, PCMM and DSS Coordinators need to collaborate on this.

a. Select “TEAM” on the menu bar on the PCMM GUI screen.

![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/002.png)

b. Then, select “Direct PC FTEE” at the bottom of the drop down menu.

> ![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/003.png)

> c. Next, select the desired Team by highlighting it and double clicking on it, or highlight it and select “OK.”

> ![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/004.png)

4.  Next, Enter or edit the “Direct PC FTEE” for existing positions in the “Direct

Care FTEE” column on the right of the window as shown below. Enter a value between 0.00 and 1.00. Two decimal places are provided and the decimal is already entered. Use the down arrow key on the keyboard to move down the column. After entering and editing all the FTEE fields, press the downward arrow key until reaching the FTEE total.

> ![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/005.png)

### CREATE A NEW STAFF ASSIGNMENT AND ENTER “DIRECT PC FTEE.” 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “Direct PC FTEE” can be entered in the staff assignment window when

assigning a staff member to a position. Note: The “Direct PC FTEE” <u>can only</u> be entered in the staff assignment window when creating a new assignment.The FTEE cannot be entered or edited here after the provider is assigned to the position. Once the FTEE is entered and saved in the Staff Assignment window, changes

to the “Direct PC FTEE,” field must be edited using the “Direct PC FTEE” option on

the “TEAM” Menu as in \#1 above. (See the prior sample screens for entering and editing

the FTEE data for assigned providers.)

> a. Select the icon for position set-up.

![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/006.png)

b. Or, Select Team from the menu bar, then select Positions.

![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/007.png)

1.  Select “New” to create a new Primary Care position. Enter a position and

> assign the role.

> ![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/008.png)

> d. Next, Select the “Staff” button on the same screen to assign a provider to the position.

![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/009.png)  
e. First, assign a provider to a position. Click on the “ASSIGN” button.

![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/010.png)

> f. Next look-up the provider’s name.Step 1: Enter the Provider’s name in the look-up box.Step 2: Click on the “SEARCH” button to locate the provider’s name.Step 3: Click on the correct provider’s name in the list box byhighlighting the name.Step 4: Click on the “OK” button.

![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/011.png)

g. After assigning the provider to a position, enter the provider’s “Direct PC FTEE” on the bottom of the following screen. The FTEE must be between 0.00 and 1.00 with two decimal places. The decimal is already provided.

Check that the entry is correct. Then, Click on “SAVE” and then

> “CLOSE” to exit the screen. The FTEE entry may also be seen on the

Direct PC FTEE option on the “TEAM MENU,” which is on the opening PCMM window.

![](sd-5-3-264-277-pcmm-enhancements-for-direct-primary-care-user-guide/012.png)

### ### ### ### Direct PC FTEE REPORT 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### #### The PCMM Direct Primary Care FTEE Report can only be printed from VistA. Starting at the “Scheduling Manager’s Menu,” enter/select the “Outputs Option,”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### then enter/select the “PCMM Reports Option.” Next, enter/select the “PCMM Direct Primary Care FTEE Option. These options are shown below. The next page shows needed entries once the Direct PC FTEE Report is entered.

# Select \<SMA\> Scheduling Manager's Menu Option: ?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ACR Ambulatory Care Reporting Menu ...

> Appointment Menu ...

> <u>Outputs ...</u>

> Supervisor Menu ...

> Select \<SMA\> <u>Outputs</u> Option: ?

> Appointment List

> Appointment Management Report

> Clinic Assignment Listing

> Clinic List (Day of Week)

> Clinic Next Available Appt. Monitoring Report

> Clinic Profile

> Display Clinic Availability Report

> Enrollments \> X Days

> File Room List

> Future Appointments for Inpatients

> Inpatient Appointment List

> Management Report for Ambulatory Procedures

> No-Show Report

> Patient Profile MAS

> <u>PCMM Reports ...</u>

> Print Scheduling Letters

> Provider/Diagnosis Report

> Radiology Pull List

> Routing Slips

> Visit Rpt by Transmitted OPT Encounter

> Workload Report

> Select \<SMA\> <u>PCMM Reports</u> Option:

> \[SC PCMM REPORTS MENU\]

> <u>FTEE PCMM Direct Primary Care FTEE</u>

> DPA Detailed Patient Assignments

> HAR Historical Assignment Reports ...

> INCR PCMM Inconsistency Report

> ITP Individual Team Profile

> PATA Patient Listing for Team Assignments

> PD Practitioner Demographics

> PP Practitioner's Patients

> SLT Summary Listing of Teams

> TML Team Member Listing

> TPL Team Patient Listing

> Select\<SMA\> PCMM Reports Option: <u>PCMM Direct Primary Care FTEE</u>

> Previous selection: INSTITUTION not null

> START WITH INSTITUTION: FIRST// <u>\<ENTER\></u>

> <u>NOTE: TO PRINT THIS REPORT FOR ALL INSTITUTIONS, ACCEPT THIS DEFAULT BY PRESSING THE \<ENTER\> KEY.</u>

> If only one institution is desired, enter the institution name after the prompt,

> Note: If the institution name is used at the FIRST and LAST prompts, it must be exact and complete as it is in the Institution file (file \#4), or there will be no data

> for the report. For example, enter VAMC ALBANY not just ALBANY.

> Another way to get this report for all “FIRST//”…, then enter the same institution after the prompt “LAST//” followed by “ZZ.”

> Example:

> START WITH INSTITUTION: FIRST// VAMC ALBANY

> LAST// VAMC ALBANY<u>ZZ</u>

> DEVICE: TELNET PORT Right Margin: 80//

> MARGIN WIDTH IS NORMALLY AT LEAST 132. ARE YOU SURE? No// y (Yes)

> Direct PC FTEE SEP 11,2002 10:37 PAGE 1

######### PRACTITIONER TEAM Direct PC

> POSITION CLINIC FTEE

> -----------------------------------------------------------------

> INSTITUTION: ALBANY VAMC

######### TEST, JAMES RED TEAM 1.0 

> MD1

> SUBTOTAL 1.0

> SMITH, LUTHER RED TEAM 0.8

> PA1

######### SUBTOTAL 0.8 

> SMITH, NANCY RED TEAM 0.3

> NP2 GREEN TEAM 0.7

> SUBTOTAL 1.0

> TOTAL 2.8

## D. AUTOMATIC INACTIVATION UPON DATE OF DEATH ENTRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## > Automatic inactivation of patients from their Primary Care team and provider panels will occur following entry of a date of death. On installing SD\*5.3\*264 a postinit routine, POST^SCMCTSK, is initiated that identifies patients with a date of death at that time. If deceased patients have active team/position assignments, it discharges/ inactivates them from their panels.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Following the initial inactivations, every time a date of death is entered in the “Death Entry” field \[DG DEATH ENTRY\] in the Registration package, the automatic inactivation from the PC teams and positions will occur. The new protocol, \[SCMC PCMM INACTIVATE ON DATE OF DEATH\], provides this functionality. A status of “Death Unassignment” will be entered in PCMM’s Patient Assignment file (SD\*5.3\*404.52) when a Date of Death is entered. If a Date of Death is entered erroneously, then deleted, the patient’s previously active panel assignments will be reactivated a status of “Reassigned after Date of Death” will be entered in PCMM’s Patient Assignment file (SD\*5.3\*404.52.) Examples are shown below.

 

\#1 Entry of DATE of Death in Registration package - Example:

> SELECT REGISTRATION MENU OPTION: DEATH ENTRY

> Select PATIENT NAME: TEST, JOHN 9-1-64 999999999 NO NSC VETERAN C

> (1 note) D: 03/09/01 15:13

> Enrollment Priority: GROUP 7c Category: NOT ENROLLED End Date:

> <u>DATE OF DEATH: JAN 9,2003//</u>

> \#2 Checking PCMM Patient Assignment file (404.52) for Death

> Unassigned (DU) status - Example:

> SELECT VA FILEMAN OPTION: INQUIRE TO FILE ENTRIES

> OUTPUT FROM WHAT FILE: OPTION// 404.42 PATIENT TEAM ASSIGNMENT

> (25345 entries)

> Select PATIENT TEAM ASSIGNMENT: TEST, JOHN 9-1-64 999999999

> NO NSC VETERAN C

> Enrollment Priority: GROUP 7c Category: NOT ENROLLED

> End Date: 01/09/2003

> PATIENT: TEST, JOHN TEAM ASSIGNED DATE: FEB 17, 1999

> TEAM ASSIGNMENT: BLUE TEAM ASSIGNMENT TYPE: PRIMARY CARE

> TEAM DISCHARGE DATE: JAN 10, 2003 USER ENTERING: TEST, TEST

> DATE/TIME ENTERED: FEB 18, 1999@15:16:35

> <u>STATUS: DEATH UNASSIGNMENT</u>\#3 Checking PCMM Patient Assignment file (404.52) for REASSIGNED

> AFTER DATE OF DEATH IS DELETED. (DU) status - Example:

> SELECT VA FILEMAN OPTION: INQUIRE TO FILE ENTRIES

> OUTPUT FROM WHAT FILE: OPTION// 404.42 PATIENT TEAM ASSIGNMENT (25345

> entries)

> Select PATIENT TEAM ASSIGNMENT: TEST, JOHN

> PATIENT: TEST, DON TEAM ASSIGNED DATE: FEB 17, 1999

> TEAM ASSIGNMENT: BLUE TEAM ASSIGNMENT TYPE: PRIMARY CARE

> USER ENTERING: TEST, TEST DATE/TIME ENTERED: DEC 27, 1999@09:52:22

> <u>STATUS: REASSIGNED AFTER DATE OF DEATH REMOVED</u>

> A new Registration patch, DG\*5.3\*273, must be installed BEFORE patch SD\*5.3\*264 for the inactivation on death entry functionality to work. DG\*5.3\*273, Field Change Monitoring Utility, is a patch for Date of Death and is noted as the Date of Death patch. It was not created within this package but it must be installed prior to installing SD\*5.3\*264. Taskman must be running for this functionality to work. If Taskman is

> down when a Date of Death is entered, the PCMM status will change when Taskman

> is restarted.

# # # IX. TRANSMISSION TO NPCDB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functionality is being created to allow the PC Direct Care FTEE to be transmitted

to the Austin Automation Center (AAC.) AAC will process the data and send it to the National Patient Care Data Base (NPCDB). This will aid in assessing the capacity for primary care within VHA.

This functionality will be released in an upcoming patch, which will create a new HL7 message. Data will be captured through the PCMM GUI interface. A nightly background job will send the HL7 messages for each change in a Direct Patient Care FTEE designation and in a Maximum Panel size.

# X. SECURITY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security for entering and editing data in the Direct PC FTEE field is controlled by the previously existing PCMM set up key, \[SC PCMM SETUP\]. The FTEE report, PCMM Direct Primary Care FTEE, is on the PCMM Reports menu, which existed before this patch. There is no key for this menu or for the report. Security is based on the assignment of the PCMM Reports menu

\[SC PCMM REPORTS MENU\] or individual reports to appropriate staff.

# XI. TECHNICAL INFORMATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional technical information is provided in: the Patch message for SD\*5.3\*264, the Electronic Wait List (EWL) Release Notes, and the EWL Installation Guide. An EWL User Manual is also available which describes how to use the Electronic Wait List in PCMM and Scheduling. These documents are in the VistA Document Library on the VHA intranet at <http://www.va.gov/vdl/Clinical.asp?appID=131>