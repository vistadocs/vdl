---
title: SCIDO Version 3 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: SPN
app_name: Spinal Cord Injury and Disorders Outcomes (SCIDO)
section: GUI
app_status: active
pkg_ns: SPN
patch_ver: 3
patch_id: SPN*3
group_key: "SPN:SPN:3"
file_numbers: []
security_keys: []
menu_options: 1
description: The Spinal Cord Injury and Disorders Outcomes (SCIDO) application is a system for compiling spinal cord injury and disorders information. The SCIDO application accesses several other Veterans Health Information Systems and Technology Architecture (VistA) programs that contain information regarding d
audience: 
keywords: 
  - care
  - assessment
  - score
  - patient
  - date
  - table
  - contents
  - report
  - form
  - scido
page_count: 0
word_count: 34538
section_count: 80
table_count: 23
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: 
revision_count: 12
revision_newest: 5/16/2011
revision_oldest: 09/12/2003
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Spinal_Cord_Injury_Disorders_Outcomes/scido_3_0_interim_user_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Spinal_Cord_Injury_Disorders_Outcomes/scido_3_0_interim_user_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=196"
---

# # ![](scido-version-3-user-manual/001.png)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# ![](scido-version-3-user-manual/001.png)](#scido-version-3-user-manual001png)
- [# <span class="smallcaps">Spinal Cord Injury</span> and <span class="smallcaps">Disorders Outcomes Interim User Manual</span>](#span-classsmallcapsspinal-cord-injuryspan-and-span-classsmallcapsdisorders-outcomes-interim-user-manualspan)
- [# # # ![](scido-version-3-user-manual/002.png)](#scido-version-3-user-manual002png)
- [# Version 3.0](#version-30)
- [Office of Enterprise Development](#office-of-enterprise-development)
- [# Revision History](#revision-history)
- [Introduction](#introduction)
  - [Recommended Users](#recommended-users)
  - [Related Manuals or Documents](#related-manuals-or-documents)
  - [VistA Document Library](#vista-document-library)
  - [Section 508 Compliance](#section-508-compliance)
  - [VA Service Desk](#va-service-desk)
- [Overview and Features](#overview-and-features)
  - [Subject Tabs](#subject-tabs)
  - [Tab Header](#tab-header)
    - [Buttons Used on Tabs](#buttons-used-on-tabs)
  - [Instruments](#instruments)
- [Accessing the System](#accessing-the-system)
  - [Logging In](#logging-in)
  - [Patient Lookup](#patient-lookup)
- [Cover Sheet Tab](#cover-sheet-tab)
- [Registration Tab](#registration-tab)
    - [Registering a Patient](#registering-a-patient)
  - [Registration Tab Information](#registration-tab-information)
    - [Registration and Network Status Section](#registration-and-network-status-section)
    - [ASIA Information Section](#asia-information-section)
    - [Primary Care Information Section](#primary-care-information-section)
    - [Etiology Information Section](#etiology-information-section)
    - [Annual Evaluation Information Section](#annual-evaluation-information-section)
  - [Registration Additional Information](#registration-additional-information)
  - [Registration Display Information](#registration-display-information)
- [Episodes of Care](#episodes-of-care)
  - [Episode of Care Management](#episode-of-care-management)
    - [Current Open Episode of Care](#current-open-episode-of-care)
    - [Create a New Episode of Care](#create-a-new-episode-of-care)
    - [Closing an Episode of Care](#closing-an-episode-of-care)
    - [Previous Episodes of Care](#previous-episodes-of-care)
    - [Associating a Follow-up Date with a Closed Episode of Care](#associating-a-follow-up-date-with-a-closed-episode-of-care)
  - [Episodes of Care within Instruments/Assessments](#episodes-of-care-within-instrumentsassessments)
  - [Graphs on Impairments Tab](#graphs-on-impairments-tab)
  - [Body Mass Index (BMI)](#body-mass-index-bmi)
  - [Conditions, Diagnoses, and Procedures](#conditions-diagnoses-and-procedures)
  - [Assessment Entry Forms on Impairments Tab](#assessment-entry-forms-on-impairments-tab)
  - [Graphs on Medical Complications Tab](#graphs-on-medical-complications-tab)
  - [Pneumonia and Respiratory Section](#pneumonia-and-respiratory-section)
  - [Influenza Section](#influenza-section)
  - [Urinary Tract Infections Section](#urinary-tract-infections-section)
  - [Pressure Ulcers Section](#pressure-ulcers-section)
    - [Pressure Ulcer Risk Subsection](#pressure-ulcer-risk-subsection)
    - [Pressure Ulcer Scale for Healing (PUSH](#pressure-ulcer-scale-for-healing-push)
    - [Pressure Ulcer Report](#pressure-ulcer-report)
    - [Pressure Ulcer Finish Subsection](#pressure-ulcer-finish-subsection)
  - [Pain Section](#pain-section)
    - [Short Form McGill Pain Questionnaire (SF-MPQ)](#short-form-mcgill-pain-questionnaire-sf-mpq)
    - [Pain Assessment & Treatment Report](#pain-assessment-treatment-report)
  - [Graphs on Activities Tab](#graphs-on-activities-tab)
  - [Activities Tab Assessment Entry Forms, Scores, and Benchmarks](#activities-tab-assessment-entry-forms-scores-and-benchmarks)
    - [Functional Independence Measure (FIM)](#functional-independence-measure-fim)
    - [Functional Assessment Measure (FAM)](#functional-assessment-measure-fam)
    - [MNFM Form](#mnfm-form)
    - [Kurtzke Expanded Disability Status Scale (EDSS)](#kurtzke-expanded-disability-status-scale-edss)
    - [Kurtzke Functional Systems Scale (FSS)](#kurtzke-functional-systems-scale-fss)
- [Participation & SWLS Tab](#participation-swls-tab)
  - [Graphs on Participation & SWLS Tab](#graphs-on-participation-swls-tab)
  - [Attendant Care Section of Participation and SWLS Tab](#attendant-care-section-of-participation-and-swls-tab)
  - [Social Section of Participation and SWLS Tab](#social-section-of-participation-and-swls-tab)
  - [Assessment Entry Forms on Participation & SWLS Tab](#assessment-entry-forms-on-participation-swls-tab)
    - [CHART-SF Assessment Entry Form](#chart-sf-assessment-entry-form)
    - [Diener’s Satisfaction with Life Scale (SWLS) Assessment Entry Form](#dieners-satisfaction-with-life-scale-swls-assessment-entry-form)
  - [CHART-SF Subscales Section](#chart-sf-subscales-section)
  - [Occupation and Education Section](#occupation-and-education-section)
- [Assessment Entry Forms](#assessment-entry-forms)
  - [Header of Assessments](#header-of-assessments)
  - [Button Functions on Assessments](#button-functions-on-assessments)
  - [General Procedure for Creating Assessments](#general-procedure-for-creating-assessments)
  - [Editing Assessments](#editing-assessments)
  - [Progress Notes](#progress-notes)
- [Reports Tab](#reports-tab)
  - [Custom Reports](#custom-reports)
  - [Impairments and Medical Complications Reports](#impairments-and-medical-complications-reports)
  - [Cumulative Reports](#cumulative-reports)
  - [Patient Listing(s) Reports](#patient-listings-reports)
  - [Filtered Reports](#filtered-reports)
  - [Report Filters](#report-filters)
- [Administration and Information Resource Management](#administration-and-information-resource-management)
  - [Administration Tab](#administration-tab)
    - [User Roles and Record Access](#user-roles-and-record-access)
    - [SCI Region List of Institutions](#sci-region-list-of-institutions)
    - [Import Patient Records](#import-patient-records)
    - [Activate or Inactivate a Patient’s Status](#activate-or-inactivate-a-patients-status)
  - [Information Resource Management (IRM) Page](#information-resource-management-irm-page)
    - [Regional Attributes](#regional-attributes)
    - [Regional Institutions](#regional-institutions)
    - [Monitor System Activity](#monitor-system-activity)
    - [National/Regional Update](#nationalregional-update)
- [Appendix A: Definitions and Acronyms](#appendix-a-definitions-and-acronyms)
- [Appendix B: Copyright Information](#appendix-b-copyright-information)
- [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms)
  - [American Spinal Injury Association (ASIA)](#american-spinal-injury-association-asia)
  - [Alcohol Use Disorders Identification Test (AUDIT) Instrument](#alcohol-use-disorders-identification-test-audit-instrument)
  - [Body Mass Index (BMI) Instrument](#body-mass-index-bmi-instrument)
  - [CAGE](#cage)
  - [Center for Epidemiologic Studies Depression Scale (CES-D)](#center-for-epidemiologic-studies-depression-scale-ces-d)
  - [Craig Handicap Assessment and Reporting Technique Short Form (CHART-SF)](#craig-handicap-assessment-and-reporting-technique-short-form-chart-sf)
  - [Check Your Health (CYH) and Secondary Conditions](#check-your-health-cyh-and-secondary-conditions)
  - [Drug Abuse Screening Test (DAST)](#drug-abuse-screening-test-dast)
  - [Duke Severity of Illness (DUSOI) Checklist](#duke-severity-of-illness-dusoi-checklist)
  - [Duke Severity of Illness Analog (DUSOI-A) Scale](#duke-severity-of-illness-analog-dusoi-a-scale)
  - [Functional Assessment Measure (FAM)](#functional-assessment-measure-fam-1)
  - [Functional Independence Measure (FIM)](#functional-independence-measure-fim-1)
  - [Kurtzke Expanded Disability Status Scale (EDSS)](#kurtzke-expanded-disability-status-scale-edss-1)
  - [Kurtzke Functional Systems Scale (FSS)](#kurtzke-functional-systems-scale-fss-1)
  - [Medical Needs Function Modifiers (MNFM)](#medical-needs-function-modifiers-mnfm)
  - [PRIME-MD® Depression Screening](#prime-md-depression-screening)
  - [Pressure Ulcer Scale for Healing (PUSH)](#pressure-ulcer-scale-for-healing-push-1)
  - [Satisfaction with Life Scale (SWLS) (Diener’s)](#satisfaction-with-life-scale-swls-dieners)
  - [SF-8 Health Survey](#sf-8-health-survey)
  - [Short Form McGill Pain Questionnaire (SF-MPQ)](#short-form-mcgill-pain-questionnaire-sf-mpq-1)
  - [Registration Ancillary Data Entry Form](#registration-ancillary-data-entry-form)
  - [Patient Education Form](#patient-education-form)
- [Appendix D: Reports](#appendix-d-reports)
  - [Influenza Diagnoses and Treatment Report](#influenza-diagnoses-and-treatment-report)
  - [Influenza Immunizations Report](#influenza-immunizations-report)
  - [Pain Assessment and Treatment Report](#pain-assessment-and-treatment-report)
  - [Pneumonia and Respiratory Report](#pneumonia-and-respiratory-report)
  - [Pneumococcal Immunizations Report](#pneumococcal-immunizations-report)
  - [Pressure Ulcer Report](#pressure-ulcer-report-1)
  - [Urinary Tract Infections Report](#urinary-tract-infections-report)
  - [RAI-MDS Quality Indicators Report](#rai-mds-quality-indicators-report)
  - [RAI-MDS Resource Utilization Groups (RUGS) Report"](#rai-mds-resource-utilization-groups-rugs-report)
  - [Cumulative Reports](#cumulative-reports-1)
  - [Custom Reports](#custom-reports-1)
- [Index](#index)

# # <span class="smallcaps">Spinal Cord Injury</span> and <span class="smallcaps">Disorders Outcomes Interim User Manual</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # # ![](scido-version-3-user-manual/002.png)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Version 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

May 2011

# Office of Enterprise Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|            |             |                                                                                                                                                             |                                    |
|------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Date   | Version | Description                                                                                                                                             | Author/Project Manager         |
| 5/16/2011  | 3.0         | Minor updates – vdl publication                                                                                                                             | <span class="mark">REDACTED</span> |
| 9/14/2010  | 3.0         | Update – Product Support Review                                                                                                                             | <span class="mark">REDACTED</span> |
| 6/21/2010  | 3.0         | Update                                                                                                                                                      | <span class="mark">REDACTED</span> |
| 11/13/2009 | 3.0         | Update per WPR                                                                                                                                              | <span class="mark">REDACTED</span> |
| 08/07/2009 | 3.0         | Inserted a Note in Tab Header and Patient Lookup paragraphs that Date of Birth does not display in SCIDO or in Patient Service Lookup for Veteran employees | <span class="mark">REDACTED</span> |
| 02/02/2009 | 3.0         | Update                                                                                                                                                      | <span class="mark">REDACTED</span> |
| 06/21/2007 | 3.0         | Updated                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 02/05/2007 |             |                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 01/15/2007 |             | Corrections                                                                                                                                                 | <span class="mark">REDACTED</span> |
| 06/16/2006 |             | Corrections, reformatted manual.                                                                                                                            | <span class="mark">REDACTED</span> |
| 09/16/2005 |             | Revisions                                                                                                                                                   | <span class="mark">REDACTED</span> |
| 09/12/2003 |             | Create draft                                                                                                                                                | <span class="mark">REDACTED</span> |

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Spinal Cord Injury and Disorders Outcomes (SCIDO) application is a system for compiling spinal cord injury and disorders information. The SCIDO application accesses several other Veterans Health Information Systems and Technology Architecture (VistA) programs that contain information regarding diagnoses, prescriptions, surgical procedures, laboratory tests, radiological exams, patient demographics, hospital admissions, and clinical visits. This access allows clinical staff to take advantage of the data supported by VistA. Information can be summarized at three levels: local medical center, SCI&D region, or national research access.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SCIDO application is designed for clinicians, administrators, and researchers who provide care to Veterans with spinal cord injury or disorders.

## Related Manuals or Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SCIDO 3.0 Interim Regional J2EE Installation Guide

SCIDO 3.0 Deployment Guide

SCIDO 3.0 Interim Technical Manual/Security Guide

SCIDO 3.0 Interim VistA Installation Guide

SCIDO 3.0 Interim Release Notes

## VistA Document Library

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online documentation for this product is available in the VistA Document Library (VDL) . Use the following internet address to access the VistA Document Library: <http://www.va.gov/vdl/>. Select the Spinal Cord Injury and Disorders Outcomes link to access the SCIDO documentation.

## Section 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) fully supports Section 508 of The Rehabilitation Act and is committed to equal access for all users. Every effort has been made to ensure that the SCIDO application meets Section 508 compliance. The SCIDO application was assigned a status of Section 508 compliant on May 10, 2010.

## VA Service Desk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

# Overview and Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SCIDO application has been organized using World Health Organization concepts. After a cover sheet summarizing the patient’s status and a registration sheet, tabs address impairments, medical complications, activities, and participation. The reports tab and administration tab follow these health domain tabs.

## Subject Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The footer of each page contains seven tabs representing the pages of the application. Moving from one page to another is possible by simply selecting the tabs located at the bottom of each page. For example, if the user is on the Activities tab and wants to open the Impairments tab, the user selects the Impairments tab in the footer.

![](scido-version-3-user-manual/003.png)

Subject Tabs

The SCIDO application can be navigated through the following tabs:

<u>Cover Sheet</u> – displays a summary of the patient’s status. It displays recent diagnoses and CPT codes from the past five years. The Cover Sheet also displays information the user may have entered through three other tabs of the application. If the information has not been entered, these fields will be blank. The patient record opens to the Cover Sheet unless the Veteran has not been registered in the SCIDO application.

<u>Registration Tab</u> – used to register Veterans into the SCIDO application and to enter data, which allows staff access to valuable regional and local program data. This information is designed to simplify your job. Investing a small amount of time entering registration and other useful information will return valuable dividends when the information is needed in reports or displayed.

<u>Impairments Tab</u> – Impairments refer to any loss of psychological, physiological, or anatomical structure or function. Impairments affect organ systems, thought, or emotion. Information about impairments is provided on both the Impairments Tab and the Medical Complications Tab.

<u>Medical Complications</u> Tab – Medical Complications are impairments that are commonly associated with spinal cord injury; therefore, this tab focuses on respiratory complications, urinary tract infections, influenza, pressure ulcers, and pain. These secondary complications are common, costly, and can be disruptive to activities, participation, and satisfaction with life.

<u>Activities Tab</u> – activities are tasks and actions by an individual at the level of a person rather than the anatomic, physiological, or social levels. Activities have been associated traditionally with abilities, disabilities, or independence. This tab summarizes common activity limitation measures such as the FIM, FAM, and Kurtzke EDSS and FSS measures, which are used specifically for multiple sclerosis.

<u>Participation & SWLS Tab</u> – participation reflects the nature and extent of a person’s involvement in life situations at a social or societal level and often pertains to participating in meaningful social roles. This tab summarizes participation information based on the CHART-SF and also includes Diener’s Satisfaction with Life Scale (SWLS).

<u>Reports Tab</u> – reports reflect the benefits of accurately maintaining the SCIDO application for the Veterans you serve. Templated reports regarding impairments and medical complications, aggregate outcome reports, and patient listings are available for ready review. Filtered reports allow the selection of specific portions of the population for review before the reports are generated. For unique reports that affect your practice, you can learn how to use the Report Designer to generate custom reports for the population.

<u>Administration Tab</u> – provides the functionality to display user names and roles; SCI Regional definitions; activate or inactivate a patient status; activate or inactivate patient assessments; activate or inactivate Episodes of Care; import patient records from the national database; and add or delete SCI and Multiple Sclerosis (MS) mail groups.

<u>Information Resource Management (IRM) tab</u> – allows a person within the IRM/ISS/ITS user role to add or delete medical centers from SCI&D regions, modify regional attributes, perform a national or regional audit, and monitor system activity.

## Tab Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each tab has a standard header , which contains information from the following sources:

- Veteran's Last Name, Veteran's First Name MI (VistA)
- Veteran's Social Security Number (VistA)
- Veteran's Date of Birth (VistA)

> NOTE: Date of Birth does not display in SCIDO for Veteran employees

- Veteran's Computed Age (VistA)
- Highest Level of Education (Registration Tab)
- ASIA Highest Neurological Level (ASIA Form)
- Current Employment Status (Participation Tab)
- ASIA Impairment Scale (ASIA Form)
- Bladder Drainage Method (Medical Complications Tab)
- Next Annual Evaluation Due (Registration Tab)
- Stage of most severe Pressure Ulcer (PUSH form)

![](scido-version-3-user-manual/004.png)

Tab Header

A *Patient Search* button is provided in the header. When the *Patient Search* button is selected, the Patient Lookup window allows the selection of a different patient. Refer to the [Patient Lookup](#patient-lookup) section of this document for more information.

A *Logout* button is provided in the header. When the *Logout* button is selected, the application logs the current user out of the application and returns to the main login page. Refer to the [Accessing the System](#accessing-the-system) section of this document for more information.

### Buttons Used on Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Print*, *Reset*, *Submit*, and *Help* buttons are located at the bottom of most, but not all tabs. The Cover Sheet and Activities tabs have only the *Print* and *Help* buttons. In the case of these tabs, nothing needs to be submitted or reset since all fields are display-only.

> ![](scido-version-3-user-manual/005.png)

#### Print Button

To print the current page, select the *Print* button.

#### Reset Button

Selecting the *Reset* button will return the previously saved values on the tab.

For assessments, the *Reset* button is similar to the Tab reset button. The *Reset* button will return previously saved values or the values present when the *Calculate* function was last used.

#### Submit Button

Select the *Submit* button to save and record the values entered in the tab fields.

If data is not entered in all required fields, a reminder will prompt the user to enter the required data. For example, on the Registration tab, if any of the required fields (Registration, SCI Network, and Date Changed) are not populated, the user will be alerted with a message, such as the following.

![](scido-version-3-user-manual/006.png)

Select *OK* to return to the Registration page to complete the fields.

Once required fields are complete and the *Submit* button has been selected, a message will confirm the information was saved. The following is an example from the Registration Tab.

![](scido-version-3-user-manual/007.png)

Select *OK* to return to the Registration Tab for viewing and navigation to other pages of the SCIDO application or for selecting a new patient.

#### Help Button

To access SCIDO Online Help, select any *Help* button. The Online Help includes instructions, procedures, and other information to help you use the SCIDO application. By default, the Online Help provides information about the particular page from which it was launched. For example, pressing *Help* on the Registration Tab displays information about the Registration page and provides links to other related information, such as the Registration Additional Information section.

#### Calendar

![](scido-version-3-user-manual/008.png)

Select the Calendar Icon located to the right of a date field to modify or add a date to a field. The calendar for the current month is displayed by default.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>![](scido-version-3-user-manual/009.png)</th>
<th>Select the ≤≤  symbol to access the previous year.<br />
Select the ≤  symbol to access the previous month.<br />
Select the <em>Print</em> button to print the calendar.<br />
Select the ≥≥  symbol to access the next year.<br />
Select the ≥ symbol to access the next month.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Window Expander Icon

![](scido-version-3-user-manual/010.png)

Selecting the Window Expander Icon opens a separate window with a scrollbar. The Window Expander is useful when there is too much detailed information to be displayed in the space available on the screen. The SCIDO application often displays only the most recent value or values on the tab itself. For example, on the Impairments tab, the Pre-Existing Diagnoses field may have room to show just two diagnoses.

![](scido-version-3-user-manual/011.png)

If the Window Expander Icon for the Pre-Existing Diagnoses is selected, a separate window is displayed showing all diagnoses. Use the scrollbar to view all pre-existing diagnoses.

![](scido-version-3-user-manual/012.png)

#### History Fields

History fields show fields’ historic values or a historic listing of completed assessments. History fields have a dropdown arrow that, when selected, displays the list of historic values for that field in descending order. For example, the Network History field on the Registration page has a dropdown that shows all historical values for the Registration and SCI Network fields.

| ![](scido-version-3-user-manual/013.png) | ![](scido-version-3-user-manual/014.png) |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|

For another example, on the Impairments Tab, next to the ASIA assessment entry button, is a field that shows the most recently completed ASIA Neurological Level, Impairment Scale, record date, and score type. Select the dropdown to view a listing of the neurological levels, impairment scales, record dates, and score types for all ASIA assessments You can view (and edit) individual assessments by selecting one of the assessment history lines.

| ![](scido-version-3-user-manual/015.png) | ![](scido-version-3-user-manual/016.png) |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|

## Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SCIDO application provides twenty instruments (assessment entry forms) for creating assessments for patients.

#### SCIDO Instruments

|              |                                                                                                                                                                                                                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ASIA         | The American Spinal Injury Association Standard Neurological Classification of Spinal Cord Injury (ASIA) instrument uses findings from the neurological examination to identify and classify different injuries and degrees of spinal cord damage.                                                                   |
| AUDIT        | The Alcohol Use Disorders Identification Test (AUDIT) instrument is derived from the World Health Organization’s Alcohol Use Disorders Identification Test and provides questions about a person’s alcohol use.                                                                                                      |
| BMI          | The Body Mass Index (BMI) form provides calculation of a Body Mass Index as a measure of body fat based on height and weight that applies to both adult men and women.                                                                                                                                               |
| CAGE         | Brief four-item alcohol disorder assessment instrument.                                                                                                                                                                                                                                                              |
| CES‑D        | The Center for Epidemiologic Studies - Depression Scale (CES-D) is a short, self-reporting scale intended for measuring current depressive symptoms in the general population. ‑                                                                                                                                     |
| CHART-SF     | The Craig Handicap Assessment and Reporting Technique – Short Form (CHART-SF) was designed to provide a simple, objective measure of the degree to which impairments and disabilities result in limitations to participation in meaningful social roles.                                                             |
| CYH          | The Check Your Health and Secondary Conditions Checklist (CYH) is designed to help identify people who are at risk for secondary conditions.                                                                                                                                                                         |
| DAST         | Drug Abuse Screening Test. The purpose of the DAST is to provide a brief, practical, but valid method for identifying individuals who are abusing psychoactive drugs and to yield a quantitative index score of the degree of problems related to drug use and misuse.                                               |
| DUSOI        | The Duke Severity of Illness (DUSOI) Checklist Scale is a generic assessment of the patient’s comorbidities.                                                                                                                                                                                                         |
| DUSOI-A      | Duke Severity of Illness Analog is single-item generic assessment of the overall comorbidity experienced by a patient based on the clinician’s judgment.                                                                                                                                                             |
| FAM          | The Functional Assessment Measure is an activity measure used as an adjunct to the FIM to address the major functional areas less emphasized in the FIM, including cognitive, behavioral, communication, and community functioning measures.                                                                         |
| FIM          | The Functional Independence Measure (Guide for the Uniform Data Set for Medical Rehabilitation, 1996) is the most widely used activity or functional assessment measure in the rehabilitation community.                                                                                                             |
| Kurtzke EDSS | Kurtzke Expanded Disability Status Scale (used for Multiple Sclerosis).                                                                                                                                                                                                                                              |
| Kurtzke FSS  | Kurtzke Functional Systems Scale Rating (used for Multiple Sclerosis).                                                                                                                                                                                                                                               |
| MNFM         | Medical Needs/Function Modifiers contains items from the Inpatient Rehabilitation Facility – Patient Assessment Instrument (IRF-PAI) pertaining to swallowing status, clinical signs of dehydration, bladder frequency of accidents in the past seven days, and bowel frequency of accidents in the past seven days. |
| PRIME-MD     | The Primary Care Evaluation of Mental Disorders (PRIME-MD) Depression Screening is a short instrument useful for detecting depression in primary care.                                                                                                                                                               |
| PUSH         | The Pressure Ulcer Scale for Healing instrument is a quick, reliable tool to monitor change in pressure ulcer status over time.                                                                                                                                                                                      |
| SF-MPQ       | McGill Pain Questionnaire (Short Form) measures a patient’s subjective pain experience by using two dimensions of pain, sensory pain rating index (S-PRI) and affective pain rating index (A-PRI), and a total pain rating index (T-PRI).                                                                            |
| SF-8         | The SF-8 Health Survey is a generic multipurpose survey of health status.                                                                                                                                                                                                                                            |
| SWLS         | Diener’s Satisfaction with Life Scale (SWLS) is a global measure of life satisfaction.                                                                                                                                                                                                                               |

Refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms) for a visual representation and functionality of each instrument.

# Accessing the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To launch the SCIDO application, double-click on the SCIDO icon located on the desktop or use your own method, such as typing in the URL in your browser. The Login window is displayed:

![](scido-version-3-user-manual/017.png)

## Logging In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To Login, enter an access code, a verify code, and select your institution. Select the *Login* button. This opens the Patient Lookup window.

## Patient Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Lookup window is opened after successful login. It may also be accessed by selecting the *Patient Search* button located on the page header. The Patient Lookup screen appears as follows:

![](scido-version-3-user-manual/018.png)

The Patient Lookup window will default to the user’s medical center. Enter a patient’s name or at least two characters of their last name in the Select Patient field and select the *Search* button. The results of the search are displayed as a list with each matching Patient Name, Social Security Number (SSN), Date of Birth (DOB), Gender, Patient Type, and Eligibility.

> **NOTE:** Date of Birth does not display in Patient Lookup for Veteran employees

> **NOTE:** Patient picture functionality is unavailable at this time.

![](scido-version-3-user-manual/019.png)

Click on the patient’s name, and a Patient Lookup Status Notification window is displayed:

![](scido-version-3-user-manual/020.png)

Review the Patient Lookup Status Notification. Select the *Cancel* button to return to the Patient Lookup screen. Select the *Continue* button to continue to the patient’s SCIDO records. Several Patient Lookup Status Notifications may be displayed. Only one example of a Patient Lookup Status notification has been represented here. Continue reviewing the notifications and selecting the *Continue* button until the Spinal Cord Injury and Disorders (SCIDO) system opens to either the Cover Sheet (if the patient is already registered) or the Registration page.

| Cover Sheet Tab                                                                                                               | or  | Registration Tab                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------|
| ![](scido-version-3-user-manual/021.png) |     | ![](scido-version-3-user-manual/022.png) |

#### Patient Lookup: Limit Patient Selection

The following criteria may be used to limit the search for patient data:

| Inpatient Provider | Clinic    |
|--------------------|-----------|
| Ward               | Specialty |

For example, to limit by specialty, select the *Specialty* button. From the list of available specialties, use the right \> and left \< buttons to move the specialty in or out of the selected box on the right. To select more than one specialty at one time, hold down the Ctrl Key and highlight all desired specialties. To select a range of specialties, select the first specialty, hold down the Shift Key, make the final specialty selection, and then select the *Search* button.

![](scido-version-3-user-manual/023.png)

From the list of matching results, click on the patient’s name. One or more Patient Lookup Status Notification windows will display. Continue until the SCIDO patient record displays.

# Cover Sheet Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cover Sheet displays recent diagnoses and CPT codes from the past five years. The summary sheet also displays information the user may have entered through three other SCIDO tabs ([Medical Complications](#graphs-on-medical-complications-tab), [Participation](#participation-swls-tab), and [Activities](#activities-tab-assessment-entry-forms-scores-and-benchmarks)). If the information has not been entered, these fields will be blank. For the Medical Complications section, Present Pain Index (PPI) scores with a value of “99=Unable to Respond” are excluded from graphical display on the Cover Sheet.

The data presented on the Cover Sheet may not be selected or modified. The Cover Sheet is used only for viewing, printing, selecting Help, and navigation to other pages within the application.

If the patient is already registered in the application, the Cover Sheet opens by default. If a patient is not registered in the application, the Registration page opens. For registration information, refer to the section titled [Registration Tab](#registration-tab).

# Registration Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Registering a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a patient is not yet registered in the application, the Registration page will open first, rather than the Cover Sheet. Three fields in the Registration Tab must be completed to submit registration information:

Registration (Status)

SCI Network?

Date Changed

These fields are marked with a red asterisk as a reminder of their required status. A patient is considered registered when information has been submitted for these required fields.

![](scido-version-3-user-manual/024.png)

The Registration page is organized in three columns: the main Registration Information in the middle, Registration Additional Information on the left, and Registration Display Information on the right.

## Registration Tab Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The center salmon-colored column of the Registration tab records information recommended in VHA Handbook 1176.1 “Spinal Cord Injury & Disorders System of Care Procedures” as a basic data set. The center Registration Information column has the following five sections:

### Registration and Network Status Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first section of the middle column of the Registration Tab is the Registration and Network Status section, which pertains to information about the patient’s registration status and SCIDO network status.

![](scido-version-3-user-manual/025.png)

#### Registration (Status) Field

To enter a patient’s registration status, select one of the following values from the Registration Status dropdown:

NS = Not SCD – Designates a person who does not have a true spinal cord injury or disorder but might have paralysis due to another cause, such as stroke, peripheral nerve disorder, or mental health disorder.

SN =SCD – Not Currently Served – Designates a person with a spinal cord injury or disorder who is not being seen at a VHA facility. Examples include Veterans who have relocated, who have not returned for follow-up appointments, or who have not had an appointment in two to four years.

SS = SCD – Currently Served

X = Expired

#### SCI Network? Field

To record the patient’s SCIDO Network status, select either the *Yes* or *No* radio button.

Selecting *Yes* indicates that the Veteran receives clinical and follow-up services, including annual evaluations, within the SCI&D system of care. The Veteran should either be offered or referred for annual evaluations at the SCI Center or approved SCI Outpatient Support Clinic if the SCI Network is marked Yes.

Selecting *No* indicates that the patient is followed primarily by Neurology Service, Rehabilitation Care Service, or another professional service.

#### Date Changed Field

Record the date or use the Calendar icon to designate the date the patient entered or left the SCI Network. When the SCI Network field? is changed to or from Yes or No, the date should be changed in the Date Changed field.

#### Network History Field

The Network History field displays information about when a patient entered or left the SCI Network. This field displays the historic values from two fields: Yes or No from the SCI Network? field and the corresponding date in the Date Changed field.

### ASIA Information Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASIA Information section pertains to the patient’s ASIA assessment values. If these fields are blank, an ASIA assessment has not been completed yet for the patient. A health care provider can complete an ASIA assessment form within the application.

![](scido-version-3-user-manual/026.png)

#### Highest Neurological Level Field

The ASIA Highest Neurological Level field is a display-only field that is populated from the most recently completed ASIA Non-Goal assessment. This value is the most cephalic (closest to the head) of the values in the Neurological Levels section (Sensory Right, Motor Right, Sensory Left, Motor Left). See the Instruments section for detailed information on the ASIA instrument. Neurological Level values include the following:

C01 = Cervical 01 T08 = Thoracic 08

C02 = Cervical 02 T09 = Thoracic 09

C03 = Cervical 03 T10 = Thoracic 10

C04 = Cervical 04 T11 = Thoracic 11

C05 = Cervical 05 T12 = Thoracic 12

C06 = Cervical 06 L01 = Lumbar 01

C07 = Cervical 07 L02 = Lumbar 02

C08 = Cervical 08 L03 = Lumbar 03

T01 = Thoracic 01 L04 = Lumbar 04

T02 = Thoracic 02 L05 = Lumbar 05

T03 = Thoracic 03 S01 = Sacral 01

T04 = Thoracic 04 S02 = Sacral 02

T05 = Thoracic 05 S03 = Sacral 03

T06 = Thoracic 06 S04 = Sacral 04

T07 = Thoracic 07 S05 = Sacral 05

UNK = Unknown

> **NOTE:** A new ASIA assessment needs to be completed to change the displayed value.

#### Impairment Scale Field

The ASIA Impairment Scale field is a display-only field that is populated from the most recently completed ASIA Non-Goal assessment. (See the Instruments section for detailed information on the ASIA assessment.) Impairment Scale values that can be displayed include the following:

A = Complete: No sensory or motor function is preserved in the sacral segments S4-S5

B = Incomplete: Sensory but not motor function is preserved below the neurological level and includes the sacral segments S4-S5

C = Incomplete: Motor function is preserved below the neurological level, and more than half of key muscles below the neurological level have a muscle grade less than 3 (Grades 0-2)

D = Incomplete: Motor function is preserved below the neurological level, and at least half of key muscles below the neurological level have a muscle grade greater than or equal to 3.

E = Normal: Sensory and motor function are normal.

UNK = Unknown

> **NOTE:** A new ASIA assessment needs to be completed to change the value of this display.

### Primary Care Information Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary Care Information section pertains to information about the patient’s primary care physician and medical center.

![](scido-version-3-user-manual/027.png)

#### Primary Care VA Medical Center Field

In the Primary Care VAMC field, select the VA Medical Center where the patient receives most of their primary care. To select the VAMC from the dropdown, type the first letter of the medical center name, and the list will start from that alphabetical section.

> **NOTE:** SCI Center staff should enter the VA Medical Center where the patient receives primary care locally. This ensures the local VAMC may receive e-mail notifications of patient admissions, discharges, and transfers.

#### Primary Care Provider Field

Select the *Search* button and enter part of the provider’s last name. The application will display matching names from which the primary care provider can be selected.

### Etiology Information Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fourth section of the middle column of the Registration Tab pertains to information about the patient’s etiology or etiologies.

![](scido-version-3-user-manual/028.png)

#### (Etiology) Trauma or Non-Trauma

Select either Trauma (Traumatic) or Non-Trauma (Non-Traumatic) to describe the overall category of the cause of the Veteran’s spinal cord injury or disorder.

#### (Etiology) Field)

In the Etiology field next to the Trauma and Non-Trauma buttons, select a category from the dropdown list that best describes the cause of the patient’s spinal cord injury or disorder. If the Traumatic radio button was selected, one of the following six traumatic causes may be selected:

TFA = Fall

TSA = Sports Activity

TVE = Vehicular

TVI = Violence

TOT = Other (Traumatic)

TUN = Unknown (Traumatic)

If the Non-Trauma was selected, one of the following non-traumatic causes may be selected:

NIA = Infection or Abscess

NMN = Motor Neuron Disease

NMS = Multiple Sclerosis

NPM = Poliomyelitis

NSY = Syringomyelia

NTU = Tumor

NOT = Other (Non-Traumatic)

NTV = Vascular

NUN = Unknown (Non-Traumatic)

NAD = Arthritic Disease or Cervical Stenosis

> **NOTE:** If either “TOT Other (Traumatic)” or “NOT = Other (Non-Traumatic)” is selected, enter a description of the cause of the Veteran’s spinal cord injury or disorder in the “Describe Other Etiology” field (See [Describe Other Etiology Field](#describe-other-etiology-field) below).

#### Date of Onset Field

In the Date of Onset field, manually enter a date or select the Calendar icon to designate the date when the spinal cord injury occurred or the spinal cord disorder began.

#### Describe Other Etiology Field

The Describe Other Etiology field is a text-entry field for entering etiology descriptions that are not listed in the Etiology dropdown. A description of up to 35 characters in length may be entered to describe the cause of the patient’s spinal cord injury or disorder.

> **NOTE:** The Describe Other Etiology field is not available for text entry unless either “TOT = Other (Traumatic)” or “NOT = Other (Non-Traumatic)” has been selected in the Etiology field.

#### MS Subtype Field

Select the MS Subtype that best describes the patient’s multiple sclerosis diagnosis:

UN = Unknown

RR = Relapsing-Remitting

PP = Primary Progressive

SP = Secondary Progressive

PR = Progressive Relapsing

> **NOTE:** The MS Subtype field is available when there has been an etiology of multiple sclerosis. If the Etiology field has once had a value of “NMS = Multiple Sclerosis”, then the user may enter a value in the MS Subtype field.

#### (Etiology) History Field

The Etiology History field is a dropdown that displays historic etiology values and dates of onset for the patient.

### Annual Evaluation Information Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fifth section of the middle column of the Registration Tab is the Annual Evaluation Information section, which pertains to information about the patient’s annual evaluations (AE).

![](scido-version-3-user-manual/029.png)

#### (Annual Evaluation) Offered Field

In the Annual Evaluation Offered field, manually enter a date or select the Calendar icon to designate the date when the patient was offered the opportunity to schedule an annual evaluation.

> **NOTE:** This is the date when the SCI coordinator offered the evaluation, not the actual date of the anticipated annual evaluation.

#### Veteran declines further Annual Evaluation Field

If the patient declines future annual evaluations, select the “Veteran Declines Future Annual Evaluation” field. A checkmark will indicate that the patient does not want to be reminded about future annual evaluations. To uncheck this field, select this field again.

#### (Annual Evaluation) Received Field

In the Annual Evaluation Received field, manually enter a date or select the Calendar icon to designate the date when the patient actually received an annual evaluation.

#### (Annual Evaluation) Next Due Field

The Next Due field automatically displays a date one year from the date listed in the Annual Evaluation Received field. This date may be changed manually or by selecting the Calendar icon.

#### (Annual Evaluation) AE VAMC Field

Select the VA Medical Center where the patient receives an annual evaluation.

## Registration Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The left column of the Registration page displays additional patient information. The lower gray area of the column provides buttons that open the [Episodes of Care Management](#episodes-of-care) page and the [Patient Education](#patient-education-form) and [Ancillary Data Entry forms](#registration-ancillary-data-entry-form).

![](scido-version-3-user-manual/030.png)

#### Highest Level of Education Field

In the Highest Level of Education field, select from the dropdown one of the following values that best describes the patient’s education level:

LH = Less than High School Graduate

HS = High School Graduate or GED

SC = Some College, Technical School, AA, or AS

CG = College Graduate

PR = Graduate or Professional School

#### Occupation at Time of Injury Field

In the Occupation at Time of Injury field, select from the dropdown one of the following values that best describes the patient’s occupation at the time of spinal cord injury or onset:

PR = Professional and technical

EX = Executive

SL = Sales

AD = Administrative support

PP = Precision Production

MO = Machine Operators

TR = Transportation

HA = Handlers

SV = Service

Refer to the Department of Labor’s Dictionary of Occupational Titles for a detailed description of these categories.

> **NOTE:** The patient’s current occupation is entered in the CHART-SF instrument and can be viewed on the [Participation & SWLS page](#participation-swls-tab).

#### Service-Connected for SCI Field

To indicate if the patient’s spinal cord injury or disorder was incurred in or aggravated by military service, select either the *Yes* or *No* radio button.

#### First Seen in VA for SCI Field

The First Seen in VA for SCI field is used to designate the date when the patient was first treated at a VA medical center for spinal cord injury or disorder. Manually enter the date or select the Calendar icon.

#### Amount VA is Used Field

To indicate how much care the patient receives at VA and/or non-VA facilities, select from the dropdown one of the following values:

VA = VA Only

VM = Mostly VA/Some Non-VA

HF = Half VA/Half Non-VA

NM = Some VA/Mostly Non-VA

NN = Non-VA Only

NH = Did not see doctor/nurse last 5 years

#### SCI&D Outcomes Coordinator Field

Select the name of the SCIDO Outcomes Coordinator responsible for maintaining current patient information. The SCI Coordinator at non-SCI Center facilities typically has this responsibility.

Select the *Search* button and enter part of the SCIDO coordinator’s last name. The system will display matching names from which you can select the coordinator.

#### Historic SCI&D Outcomes Coordinators Field

The Historic SCI&D Outcomes Coordinators field displays a list of previous SCIDO Coordinators. When the SCI&D Outcomes Coordinator field is updated, the previous coordinator’s name is added to this history field.

#### Episode of Care Button

The Episodes of Care Management page is accessed from the Registration tab. For more information, refer to the [Episode of Care Management](#episode-of-care-management) section.

#### Ancillary Data Entry Button and Patient Education Button

The following forms are provided in the application and may be accessed from the Registration Tab:

Ancillary Data Entry

Patient Education

The Ancillary Data Entry Form is used to record sources of care, referral sources, bowel care information, and remarks. The form is described in Appendix C: Instruments and Forms in the section titled [Registration Ancillary Data Entry Form](#registration-ancillary-data-entry-form).

The Patient Education form is used to record the dates the patient is given educational materials on sixteen health-related topics. For a description of the form, refer to [Patient Education Form](\l) in [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms).

## Registration Display Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The right column of the Registration page is populated from other applications. The information, with the exception of Date of Death, is display-only and not editable.

![](scido-version-3-user-manual/031.png)

#### Metro/Micro/Rural Field

The Metro/Micro/Rural field displays the classification of the patient’s residence:

MT = Metropolitan areas have more than 50,000 residents

MC = Micropolitan areas have 10,000 to 49,999 residents.

RL = Rural areas have less than 10,000 residents

The field may also be blank

#### Veteran’s Home Address Field

This field displays the Veteran’s home address.

#### Registration Date Field

This field displays the date that the Veteran was first registered into the SCIDO application.

#### Date of Last Review Field

This field displays the most recent date that the Veteran’s SCIDO information was accessed or reviewed.

#### Last Updated By Field

This field displays the name of the VA staff member who last updated or changed the patient’s SCIDO information. The field may also display "Nightly Demographic Update" if the SCIDO system was updated during the nightly demographic batch run. The demographic update batch process looks for demographic changes in Vista and updates the following SCIDO cache date base items:

- Address Line 1 (home_address1)
- Address Line 2 (home_address2)
- City (city)
- State (state)
- Zip Code (zip)
- Residence Phone \#
- Date of Death
- Enrollment Priority
- Ethnicity
- Marital Status
- Race
- VA SCI Status

#### VA SCI Status Field

This field displays the Veteran’s self-reported SCI Status at the time of registration for VA healthcare. The displayed values include the following:

1 = Paraplegia-Traumatic

2 = Quadriplegia-Traumatic

3 = Paraplegia-Nontraumatic

4 = Quadriplegia-Nontraumatic

X = Not Applicable

#### Date of Death Field

If the patient has died, this field displays the date of death recorded in the patient treatment file or Common Services. If the information is not accurate or has not been recorded, a SCI Coordinator may enter the date or select the date from the Calendar icon. Changing the date of death in the SCIDO application will not change the Date of Death in other VistA applications.

#### Enrollment Priority Field

This field displays the patient’s enrollment priority as a value from 1 to 8.

> **NOTE:** Patients with spinal cord injury diagnoses may be reclassified as catastrophically disabled (priority 4) if they have enrollment priorities of 5, 6, 7, or 8.

#### Medical Centers Visited Field

A dropdown list of VA Medical Centers at which the patient has received care is displayed. The most recent care location is displayed at the top of the list.

# Episodes of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Episode of Care can be described as health care services provided during a certain period of time, focused on a particular goal. In the SCIDO application, assessments within an episode of care will have the same care type and care start date. Episodes provide a useful basis for analyzing quality of care and utilization patterns.

In the application, outcomes information is related to a care type for every assessment. The following three care types require episode of care management: Inpatient Rehabilitation, Outpatient Rehabilitation, and Continuum of Care – Inpatient. Other care types do not use episode of care management.

The rules for entering assessments within an episode of care are described in the section titled [Episodes of Care within Instruments/Assessments](#episodes-of-care-within-instrumentsassessments).

## Episode of Care Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Episodes of care are managed using the Episodes of Care Management Page, where the user may create a new episode of care, close an episode of care, and associate a follow-up date with a closed episode of care. The user may review current (open) and previous (closed) episodes of care for a specified patient, including a list of assessment record dates, score types, and assessment types.

The Episodes of Care Management page is accessed from the Registration Tab. Select the button labeled *Episode of Care*, and the Episodes of Care Management window is displayed.

| ![](scido-version-3-user-manual/032.png) |
|------------------------------------------------------------------------------------------------------------------------------------------|

### Current Open Episode of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a current open episode of care exists, the information will be displayed on the left side of the Episodes of Care Management page. The Episode of Care (EoC) care type and start date are displayed, and completed assessments are listed by record date and score type for the open episode of care. Only one episode of care may be open at one time for a specific patient. When an episode of care is open, the *Create Episode of Care* button is not selectable.

| ![](scido-version-3-user-manual/033.png) |
|-----------------------------------------------------------------------------------------------------------------------------------------|

### Create a New Episode of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When no episode of care is open, the *Create Episode of Care* button is selectable.

![](scido-version-3-user-manual/034.png)

Select the *Create Episode of Care* button to create a new episode of care, and the New Episode of Care form is displayed.

![](scido-version-3-user-manual/035.png)![](scido-version-3-user-manual/036.png)

For the new episode of care, select one care type from the following choices:

Inpatient Rehabilitation

Outpatient Rehabilitation

Continuum of Care - Inpatient

Provide the Episode of Care (EoC) Start Date for the episode of care by either manually entering the date or selecting the date from the calendar icon. The EoC Start date may be any time up to, and including, the current date. A future date may not be used. It is important to note that the EoC start date is not necessarily related to admission date.

When the *Submit* button is selected, the application closes the Open New Episode of Care form and returns to the Episodes of Care Management page. The Open Episode of Care section will show the care type and EoC start date for the new episode of care. Assessments may be added to the open episode of care until it is closed.

For each assessment type (for example, ASIA assessments) within an Episode of Care, only one:

Start score type per instrument is allowed.

Goal score type per instrument is allowed.

Finish score type per instrument is allowed.

For a closed episode of care, only one Follow-up score type per instrument is allowed.

### Closing an Episode of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Episode of Care should be closed when the treatment has been completed or finished. Do not wait until a follow-up evaluation to close an Episode of Care. It is important to note that the EoC close date is not necessarily related to a discharge date.

> **NOTE:** the EOC closed date is stored in SCIDO cache table EPISODE_OF_CARE, column CLOSED_DATE. The cache column CARE_END_DATE is used for migrated data. One day is subtracted from the migrated CARE_END_DATE to obtain the CLOSED_DATE for migrated data.

After an episode of care is closed, assessments may no longer be added, with the exception of those assessments with a score type of Follow-up. Please review the assessments before closing an Episode of Care to ensure that none have been overlooked or omitted. To close an episode of care from the Episodes of Care Management page, select the *Close Episode of Care* button.

![](scido-version-3-user-manual/037.png)

The application displays the Close Episode of Care window with the care type and EoC Start Date for the current open episode of care.

Enter the Episode of Care (EoC) Close Date, either by manually entering the date or by selecting it from the calendar icon. The EoC Close Date is the date the episode of care was closed by the Clinician. It must be later than the EoC start date and later than or the same as the most recent record date of any assessment belonging to the episode of care. The EoC Close date may be before or the same as the current date. Future dates may not be used.

After entering the Close Date, select the *Submit* button to close the episode of care. The application will return to the Episodes of Care Management page and re-display the recently closed episode of care summary in the display area entitled Previous Episodes of Care.

### Previous Episodes of Care 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The right side of the Episodes of Care Management page displays information about Previous (Closed) Episodes of Care. The Care Type, Start Date, Closed Date, and Follow-up Date are displayed for each episode of care. Highlight an episode of care line, and a list of assessments in that selected episode are displayed by record date, score type, and instrument name in the section below. In the section below, double-click on an assessment record date to view and edit that assessment.

![](scido-version-3-user-manual/038.png)

### Associating a Follow-up Date with a Closed Episode of Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a Follow-up Date to a closed episode of care, select the appropriate episode of care in the Previous Episodes of Care section. Select the *Add Follow-up Date* button, and the Add Follow-up Date form is displayed:

![](scido-version-3-user-manual/039.png)

In the Add Follow-up Date form for the selected episode of care, enter the follow-up date, either manually or by selecting it from a calendar. The EoC Follow-up Date is the approximate date the Clinician conducted follow-up assessments for the chosen episode of care. The Follow-up date may be before or on the current date and must be at least one day later than the EoC close date. Select the *Submit* button to assign the follow-up date to the closed episode of care.

Once an assessment with a score type of Follow-up has been added to an episode of care, the EoC Follow-up Date may not be changed.

> **NOTE:** Use the EoC follow-up date for all follow-up information entered through the assessment forms. This one date will be used to identify all related follow-up data, even if follow-up assessments were actually conducted on several different dates.

## Episodes of Care within Instruments/Assessments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the SCIDO application, assessments within an episode of care will have the same care type and care start date. It is suggested, but not required, that the ASIA assessment data be entered before other assessments. The application will remind the user to enter an ASIA assessment before all others.

The header of each assessment form has four fields that are important to episodes of care: Record Date, Care Type, Care Start Date, and Score Type.

![](scido-version-3-user-manual/040.png)

Header of Instrument

#### Record Date Field

Enter the record date, the date the assessment was conducted, manually or by using the calendar to select the date.

#### Care Type Field

There are many different care types available, but episode of care management is used only if the care type is one of the following types:

Inpatient Rehabilitation

Outpatient Rehabilitation

Continuum of Care - Inpatient

For any given patient, only one episode of care may be open at a time. If an episode of care is open when a new assessment is created, the care type for the current episode of care defaults into this field.

#### Care Start Date Field

If an episode of care is open, the application will display the care start date for that episode of care. If no episode of care is open, the application will display the Care Start Date field after an EoC care type value is entered. This field will have no value if the care type is not an EoC care type.

#### Score Type Field

Within an episode of care for each instrument type, the user may create only one assessment with a score type of Start, Goal, Finish, or Follow-up. For example, an episode of care may have only one ASIA assessment with a score type of Start. There may be more than one assessment with a score type of Interim. The score type of Unknown is not used with episodes of care. For example, the Unknown score type may be used with assessments with a care type of Annual Evaluation.

The following score types are used with episodes of care:

Start = ST A score type of “Start” is used to identify the beginning of a treatment or rehabilitation episode of care. It rarely is the same date that the patient is admitted to the medical center. For example, a patient with a new onset of spinal cord injury may receive days of care to achieve medical or surgical stability before beginning rehabilitation; therefore, a rehabilitation episode of care begins on the day when the patient is participating in active rehabilitation but not before.

Goal = GL A “Goal” score type is used to identify goals that are realistically expected to be achieved on a particular assessment at the close of an episode of care. The goal scores are usually determined by the health care or rehabilitation team including and in conjunction with the patient. Clinical practice guidelines and research articles are sometimes useful in establishing goals.

Interim = IN “Interim” score types are used to track progress in increments between the start and finish of treatment services. Only “Interim” score types can be used multiple times for one instrument within an episode of care.

Finish = FI A “Finish” score type is used to identify status at the end of a treatment or rehabilitation episode of care. It is rarely the same date that the patient is discharged from the medical center. For example, a patient may complete treatment for a certain condition but need to wait for the delivery of supplies and services to their home before they are discharged from the medical center. An episode of care should be closed when the particular type of treatment has been completed or finished. Do not wait until follow-up evaluation to close an episode of care.

Follow-up = FO A “Follow-up” score type is used to identify if the patient’s status has been maintained at some time following completion of treatment or rehabilitation. For inpatient rehabilitation, it is customary to follow-up with patients three months after “Finish,” but other follow-up intervals may be used. There can only be one “Follow-up” date. This one date will be used to identify all related follow-up data even if follow-up assessments were actually conducted on several different dates. Follow-up information is an indication of treatment durability regarding whether treatment gains have been maintained after finishing active treatment or rehabilitation.

Unknown = UN An “Unknown” score type should be used when a sequencing of score types is not indicated or when none of the previous score types are applicable. For example, a care type of Annual Evaluation (non-episode of care) would be likely to have all assessments associated with “Unknown” score types.

#### Adding Follow-up Assessments

Assessments with a score type of Follow-up may be added to closed episodes of care for which a follow-up date has been associated. The EoC Follow-up Date is the approximate date the Clinician conducted follow-up assessments for the chosen episode of care. This one date will be used to identify all related follow-up data, even if follow-up assessments were actually conducted on several different dates.

The follow-up date is entered on the Episodes of Care Management page for all follow-up information. Assessments with a score type of Follow-up cannot be added to that episode of care, until a Follow-up Date is assigned to the episode of care. For example, the previous episodes of care include the episodes of care shown in the following:

![](scido-version-3-user-manual/041.png)

Because there is no Follow-up Date for the episode of care beginning on 04/01/2005, assessments with a score type of Follow-up cannot be added to that episode of care, until a Follow-up Date is assigned to it. The episode of care beginning on 05/01/2004 has a follow-up date of 07/16/2004 so new assessments with a Follow-up score type and a record date of 07/16/2004 may be added to this episode of care.

<span id="_Impairments_Tab" class="anchor"></span>Impairments Tab

Impairments refer to any loss of psychological, physiological, or anatomical structure or function. Impairments affect organ systems, thought, or emotion. Information about impairments is provided on both the Impairments Tab and the Medical Complications Tab.

![](scido-version-3-user-manual/042.png)

## Graphs on Impairments Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Impairments page, the following three graphs are populated after their corresponding assessments have been completed and submitted.

Check Your Health (CYH) Changes Over Time

SF-8 Health Survey Changes Over Time

Duke Severity of Illness Scale (DUSOI) Changes Over Time

By resting the mouse over one of the data points on any of these graphs, the date and the score for that assessment are displayed.

## Body Mass Index (BMI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BMI section of the Impairments tab displays the patient’s current weight (in pounds or kilograms), the patient's height (in inches or centimeters), and the patient's body mass index. The Body Mass Index (BMI) form calculates a Body Mass Index as a measure of body fat based on height and weight that applies to both adult men and women.

To create a new BMI assessment, select the *BMI* button. To view a historic listing of the patient's BMI scores, select the BMI History dropdown. From the BMI History listing, you can select an assessment history line to view and edit an individual assessment.

For more information about the BMI instrument, refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms).

## Conditions, Diagnoses, and Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Secondary Conditions, Pre-Existing Diagnoses, and Pre-Existing Procedures

The Secondary Conditions, Pre-Existing Diagnoses, and Pre-Existing Procedures display-only fields list the patient’s Secondary Conditions excluding SCI Diagnoses, Pre-Existing Diagnoses before the date of SCI onset, and Pre-Existing Procedures occurring before the date of SCI onset within VA health care settings. This information is populated through other applications and cannot be entered or edited.

To view a history of the patient’s Secondary Conditions, Pre-Existing Diagnoses, or Pre-Existing Procedures, select the Window Expander icon next to each field.

#### Swallowing Status Field

The Swallowing Status field is populated from values entered in the Medical Needs and Function Modifiers (MNFM) instrument. The information is display-only text and may be updated only by performing a new MNFM Non-Goal assessment through the Activities page.

#### Dehydration Signs Field

The Dehydration Signs field is populated from values entered in the Medical Needs and Function Modifiers (MNFM) instrument. The information is display-only text and may be updated by performing a new MNFM assessment through the Activities page.

#### Brain Injury Field

To indicate whether the patient has ever had a brain injury, select either the *Yes* or *No* radio button.

#### Other Injury Field

To indicate whether the patient had any injury other than a brain injury at the time of SCID onset, select either the *Yes* or *No* radio button.

#### Describe Other Field

If the *Yes* button is selected in the Other Injury field, a description of the injury may be entered into the Describe Other field.

## Assessment Entry Forms on Impairments Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Eleven instruments pertaining to loss of psychological, physiological, or anatomical structure or function are accessed or launched from the Impairments tab:

ASIA - American Spinal Injury Association Standard Neurological Classification of Spinal Cord Injury

AUDIT - Alcohol Use Disorders Identification Test

BMI – Body Mass Index Calculator

CAGE - Brief alcohol disorder assessment instrument

CES-D - Center for Epidemiologic Studies - Depression Scale

CYH - Check Your Health and Secondary Conditions Checklist

DAST - Drug Abuse Screening Test

DUSOI - Duke Severity of Illness Checklist Scale

DUSOI-A - Duke Severity of Illness Analog

PRIME-MD - PRIME-MD Depression Screening

SF-8 Health Survey

To access an instrument form, select the button next to the instrument name. For example, select the *ASIA* button to launch the ASIA instrument to create a new ASIA assessment.

Refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms) for more information on each instrument.

> **NOTE:** The term “assessment” refers to an instrument that has been completed. In this manual, the term “instrument” will be used for the form that is completed during the assessment process.

#### Assessment Scores/Dates on Impairments Tab

Next to each assessment entry button is a history field that displays the score(s), score type, and the record date for the most recent assessment. Select the history dropdown to view a listing of the score(s), record dates, and score types for all assessments. You can view (and edit) individual assessments by selecting one of the assessment history lines. Editing assessments is covered in the [Editing Assessments](#editing-assessments) section of this manual.

<span id="_Toc288036217" class="anchor"></span>Medical Complications Tab

Medical complications are impairments that are commonly associated with spinal cord injury. Respiratory complications are the most frequent cause of mortality in the SCI&D population. Urinary tract infections occur frequently but with less mortality than in the past. Pressure ulcers are costly and disruptive to participation in meaningful social roles. Chronic and acute pain is commonly reported by spinal cord injury patients and can be disruptive to activities, participation, and satisfaction with life.

![](scido-version-3-user-manual/043.png)

## Graphs on Medical Complications Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The two graphs on the Medical Complications page, *PUSH Over Time* and *SF-MPQ and PPI*, are populated after the corresponding assessment has been completed and submitted. Present Pain Intensity (PPI) ratings are entered on the SF-MPQ form and may also be displayed from the VistA Vitals application. PPI scores with a value of “99=Unable to Respond” are not graphed. By resting the mouse over one of the data points on any of these graphs, the date and the score for that assessment are displayed.

Located under the *PUSH Over Time* graph is the Recent PUSH Scores history field that shows PUSH scores, their associated record dates, and score types. Select the dropdown to view a listing of the score(s), record dates, and score types for all PUSH assessments. You can view (and edit) individual assessments by selecting one of the PUSH Total Score assessment history lines.

## Pneumonia and Respiratory Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Ventilator Equip./Supplies Field

The Ventilator Equip./Supplies field is populated from other applications with either *Yes* or *No*. *Yes* will be populated in this field when one or more of the specified CPT and HCPCS codes are recorded within the interval from the present day to five years before. This field may be overwritten. To change the value, select the desired value (*Yes* or *No*) from the dropdown.

#### Pneumonia and Respiratory Reports 

To view the Pneumonia and Respiratory report, select the *Pneumonia & Respiratory Report* button. The Pneumonia and Respiratory Report displays VistA information about increased aspiration risks due to swallowing difficulties or feeding tubes, pneumonia or atelectasis diagnoses, intubation procedures, chest radiology results, sputum laboratory results, and discharge locations following inpatient treatment of pneumonias.

To view the Pneumonia Immunizations report, select the *Pneumonia Immunizations Report* button. The Pneumococcal Immunizations Report displays VistA information about pneumococcal vaccination medications ordered for the patient, and pneumococcal vaccination diagnoses and procedure codes recorded. This report cannot be used to document performance measure conformance due to various methods of recording doses.

Refer to the [Reports Tab](#_Reports_Tab_1) section of this manual for more information.

> **NOTE:** All reports are view-only. Information within these reports may not be edited.

## Influenza Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Influenza Reports

To view the Influenza Diagnoses & Treatment report, select the *Influenza Dxs & Treatment Report* button. The Influenza Diagnoses and Treatment Report displays VistA information about influenza-related diagnoses, antiviral medications prescribed, influenza-related microbiology and chemistry laboratory reports, chest radiology results, and discharge locations following inpatient treatment of influenza incidents.

To view the Influenza Immunizations report, select the *Influenza Immunizations R*eport button. The Influenza Immunizations Report displays VistA information about influenza vaccination medications ordered for the patient, and influenza vaccination diagnoses and procedure codes recorded. This report cannot be used to document performance measure conformance due to various methods of recording doses.

Refer to the [Reports Tab](#_Reports_Tab_1) section of this manual for more information.

> **NOTE:** All reports are view-only. Information within these reports may not be edited.

## Urinary Tract Infections Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Bladder Drainage Field 

In the Bladder drainage field, select the predominant urinary device type used by the patient. Multiple options cannot be selected. To view a history of the patient’s use of urinary device types, select the history dropdown.

BA = Bladder Augmentation

EC = Condom/External Catheter

IC = Intermittent Catheterization

IN = Indwelling Catheter

IP = Ileal Pouch

SC = Suprapubic Catheter

SS = Surgical Stent

#### Urinary Tract Infections Reports

To launch the Urinary Tract Infections report, select the *Urinary Tract Infections Report* button. The Urinary Tract Infections Report displays VistA information about urinary tract diagnoses, surgical procedures, radiological studies of the urinary tract, and urinalysis, microbiology, and CBC laboratory results related to urinary tract infections.

Refer to the [Reports Tab](#_Reports_Tab_1) section of this manual for more information.

> **NOTE:** All reports are view-only. Information within these reports may not be edited.

## Pressure Ulcers Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pressure ulcers are costly and disruptive. Pressure ulcer prevention and treatment information can be tracked in the Pressure Ulcer Section. There are two subsections, separated by the PUSH Instrument form and the *Pressure Ulcer Report* button. The first subsection allows collection of information regarding pressure ulcer risk assessments, and the second subsection allows collection of information after a period of treatment focused on healing of a pressure ulcer.

![](scido-version-3-user-manual/044.png)

### Pressure Ulcer Risk Subsection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first subsection that allows collection of information regarding pressure ulcer risk assessment includes four fields. Complete the first three fields and select the *Submit* button to create a Pressure Ulcer Risk Assessment.

Whenever the Risk Record Date field is modified and submitted, if values are present in the Press. Ulcer Risk and Risk Instrument Used fields, a new assessment line is created in the Risk Instrument History field. If the user modifies saved values in the Pressure Ulcer Risk field and/or Risk Instrument Used field and does not modify the Record Date, if the user selects Submit, a message “Duplicate Risk Date” is displayed.

#### Pressure Ulcer Risk

To indicate the patient’s risk for pressure ulcers, select from the dropdown one of the following values:

0 = Not Assessed

1 = Very Low Risk

2 = Low Risk

3 = Average Risk

4 = High Risk

5 = Very High Risk

#### Risk Record Date

Record the date the pressure ulcer risk assessment occurred. The date can be manually entered or selected from the Calendar icon.

#### Risk Instrument Used

To indicate the instrument used to determine the patient’s risk for pressure ulcers, select from the dropdown one of the following commonly used pressure ulcer risk assessment instruments:

AN = Anderson

BB = Braden, and Modified Braden

CJ = Cuben and Jackson Scale

GM = Gosnell and Modified Gosnell

KN = Knoll

NR = Norton

PS = Pressure Sore Prediction Scale

SL = Salzberg, Lehman, or Rodriguez

WP = Waterlow Pressure Sore Risk Calculator

WT = Watkinson Scale

NN = None of the Above

#### Risk Instrument History

The Risk Instrument History field displays the historical values for the patient’s pressure ulcer risk level, the risk instrument used, and the date that the risk assessment was taken. To view a complete history of the patient’s pressure ulcer risk assessments, select the dropdown next to the field.

### Pressure Ulcer Scale for Healing (PUSH

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pressure Ulcer Scale for Healing (PUSH) instrument ) is included to allow recording specific information regarding the patient’s most severe pressure ulcer. To access the PUSH instrument, select the *PUSH Instrument Form* button.

The pressure ulcer is assessed and scored on the four elements in the tool: length of the open wound, width of the open would, exudate amount, and tissue type. The highest current pressure ulcer stage and number of current pressure ulcers are recorded on the form.

Push scores are displayed under the PUSH Over Time graph in the Recent PUSH Scores field. For more information about the PUSH, refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms).

### Pressure Ulcer Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pressure Ulcer Report displays SCIDO information entered on the Medical Complications Tab and PUSH assessments. VistA information about pharmacy supplies and prosthetic devices, diagnoses, surgeries, complications, radiological studies, and laboratory results related to pressure ulcers is also displayed.

To view the Pressure Ulcer Report, select the *Pressure Ulcer Report* button.

### Pressure Ulcer Finish Subsection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second Pressure Ulcer subsection allows collection of information after a period of treatment focused on healing of a pressure ulcer. Complete the first five fields and select the *Submit* button to create a Pressure Ulcer Finish Assessment.

Whenever the Finish Record Date field is modified and submitted, if values are present in the other required fields, a new assessment line is created in the Pressure Ulcer Finish History field. If the user modifies saved values in the other fields and does not modify the Finish Record Date, if the user selects Submit, a message “Duplicate Finish Date” is displayed.

#### Predominant Position at Finish

To indicate the patient’s predominant position at the finish of their pressure ulcer healing, select from the dropdown one of the following values:

Sitting

Bedrest

#### Finish Record Date

Next to the Predominant Position at Finish field is a date field for recording when the assessment occurred. The date can be manually entered or selected by selecting the Calendar icon.

#### Is Ulcer Closed/Healed

Select either the *Yes* or *No* radio button to indicate whether the patient’s pressure ulcer is closed or healed.

#### Sitting Time (Hours/Day)

Enter the number of hours of sitting tolerance time per day, for example 5.25. Valid values are 0 to 24.00.

#### Time to Achieve Healing (Days)

Enter the time in days that it took for the highest staged ulcer to heal.

#### Pressure Ulcer Finish History

This field displays the most recent Pressure Ulcer Finish values for the patient’s predominant position at finish, whether the pressure ulcer is closed and healed, the sitting time, the time to achieve healing, and the date that the assessment was conducted. To view a complete history of the patient’s pressure ulcer periods of treatment, select the history dropdown next to the field.

## Pain Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Short Form McGill Pain Questionnaire (SF-MPQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Short Form McGill Pain Questionnaire (SF-MPQ) is included to allow recording of a patient’s subjective pain experience along two dimensions of pain, sensory pain rating index (S-PRI) and affective pain rating index (A-PRI), and a total pain rating index (T-PRI). The patient is also provided the opportunity to rate their present pain intensity index (PPI) and use a visual analogue scale to rate their pain from zero (lowest severity) to one-hundred (highest severity).

#### SF-MPQ History

The SF-MPQ History field displays the patient’s Short Form McGill Pain Questionnaire assessment scores with the score type and record date. To view a complete history of the patient’s SF-MPQ assessments, select the dropdown next to the field.

### Pain Assessment & Treatment Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pain Assessment & Treatment Report displays SF-MPQ and PPI scores, pain alleviation drugs, pain management diagnoses and procedures, and Transcutaneous Electrical Nerve Stimulation (TENS) trial dates. Present Pain Intensity ratings may be from either the SF-MPQ or the VistA Vitals application. To view the Pain Assessment & Treatment Report, select the *Pain Assessment & Treatment Report* button.

<span id="_Toc288036230" class="anchor"></span>Activities Tab

Activities are tasks and actions by an individual at the level of a person rather than the anatomic/physiological level or social level. Activities have been associated traditionally with abilities, disabilities, or independence.

![](scido-version-3-user-manual/045.png)

## Graphs on Activities Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The four graphs on the Activities page, Functional Independence Measure (FIM), Functional Assessment Measure (FAM), Kurtzke FSS & EDSS, and Accident Frequency graphs, are populated after their corresponding assessment has been completed and submitted. By resting the mouse over one of the data points on any of these graphs, the date and the score for that assessment are displayed.

## Activities Tab Assessment Entry Forms, Scores, and Benchmarks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Benchmarks will not display for ASIA Impairment E or Unknown.

### Functional Independence Measure (FIM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Independence Measure (FIM) is the most widely used activity or functional assessment measure in the rehabilitation community. To access the FIM instrument, select the *FIM* button. For more information about the FIM, refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms).

#### FIM Total Score, Date, and Benchmark

The FIM Total score, date, score types, and benchmark fields are populated after a FIM assessment has been completed and submitted. FIM Total scores, dates, and score types are displayed in a FIM history field, starting with the most recent assessment. Select the dropdown to view a listing of the score(s), record dates, and score types for all FIM assessments. You can view (and edit) individual assessments by selecting one of the FIM Total Score assessment history lines.

#### FIM Motor Score, Date, and Benchmark

FIM Motor scores, dates, score types, and benchmarks are displayed in a history field. Select the dropdown to view a listing of all FIM Motor score(s), record dates, and score types. To view (and edit) individual assessments, select one of the assessment history lines for the FIM Total Score field.

#### FIM Cognitive Score, Date, and Benchmark

FIM Cognitive scores, dates, score types, and benchmarks are displayed in a history field. Select the dropdown to view a listing of all FIM Cognitive score(s), record dates, and score types. To view (and edit) individual assessments, select one of the assessment history lines for the FIM Total Score field.

### Functional Assessment Measure (FAM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Assessment Measure (FAM) was developed as an activity measure and as an adjunct to the Functional Independence Measure (FIM). To access the FAM instrument, select the *FAM* button. For more information about the FAM, refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms).

#### FAM Scores 

Beside the *FAM* button is a history field that displays the most recent FAM score. This field is populated after a FAM assessment has been completed and submitted. Select the dropdown to view a listing of the scores, record dates, and score types for all FAM assessments. You can view (and edit) an individual FAM assessment by selecting one of the FAM assessment history lines.

### MNFM Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the Medical Needs and Function Modifiers (MNFM) instrument, select the *MNFM* button. For more information about the MNFM instrument, refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms).

#### Bowel Accident Frequency

The Bowel Accident Frequency field is populated after an MNFM assessment has been completed and submitted. The frequency of bowel accident rating, record dates, and score types are displayed in a history field. Select the dropdown to view a listing of the score(s), record dates, and score types for all MNFM assessments. You can view (and edit) an individual MNFM assessment by selecting one of the assessment history lines.

To access the MNFM instrument, select the *MNFM* button.

#### Bladder Accidents Frequency

The Bladder Accident Frequency field is populated after an MNFM assessment has been completed and submitted. The frequency of bladder accident rating and dates are displayed in a history field. Select the dropdown to view a listing of the score(s), record dates, and score types for all MNFM assessments. You can view (and edit) individual MNFM assessments by selecting one of the assessment history lines.

To access the MNFM instrument, select the *MNFM* button.

### Kurtzke Expanded Disability Status Scale (EDSS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the Kurtzke EDSS instrument, select the *EDSS* button.

> **NOTE:** The EDSS and FSS assessments will only be available if the patient holds an etiology of Multiple Sclerosis.

Refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms) for more information on the Kurtzke EDSS instrument. The Kurtzke EDSS Rating field is populated after a Kurtzke EDSS assessment has been completed and submitted. Kurtzke EDSS scores, record dates, and score types are displayed in a history field. Select the dropdown to view a listing of the score(s), record dates, and score types for all EDSS assessments You can view (and edit) individual assessments by selecting one of the assessment history lines.

### Kurtzke Functional Systems Scale (FSS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the Kurtzke FSS instrument, select the *FSS* button. Refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms) for more information on the Kurtzke FSS instrument.

FSS scores and dates are displayed in a history field next to the *FSS* button. Select the history dropdown to view a listing of the score(s), record dates, and score types for all FSS assessments. You can view (and edit) individual FSS assessments by selecting one of the assessment history lines.

# Participation & SWLS Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Participation reflects the nature and extent of a person’s involvement in life situations at a social or societal level and often pertains to participating in meaningful social roles. This tab summarizes participation information based on the Craig Handicap Assessment and Reporting Technique Short Form (CHART-SF). It also includes Diener’s Satisfaction with Life Scale (SWLS). Global life satisfaction from the patient’s perspective is distinguished from affective appraisal in that it is more cognitively than emotionally driven.

![](scido-version-3-user-manual/046.png)

## Graphs on Participation & SWLS Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The two graphs on the Participation & SWLS page are populated after the corresponding assessment (CHART-SF or SWLS) has been completed and submitted. CHART-SF benchmark information is not provided in the graph but is available in the center column of the tab. The SWLS Over Time graph displays benchmark information based on the highest ASIA Neurological level, ASIA impairment scale, clinical practices guideline, and research publications.

> **NOTE:** Benchmarks will not display for ASIA Impairment E or Unknown.

By resting the mouse over one of the data points on any of these graphs, the date and the score for that assessment are displayed.

## Attendant Care Section of Participation and SWLS Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Attendant Care Field

The Attendant Care field displays the sum of the number of paid and unpaid hours of attendant care per day. The Attendant Care field is populated after the Physical Independence subscale of a CHART-SF Non-Goal assessment has been completed and submitted.

#### Paid Attendant Care Field

The Paid Attendant Care field displays the number of hours of paid attendant care per day. This field is populated after the Physical Independence subscale of a CHART-SF Non-Goal assessment has been completed and submitted.

#### Unpaid Attendant Care Field

The Unpaid Attendant Care field displays the number of hours of unpaid attendant care per day. This field is populated after the Physical Independence subscale of a CHART-SF Non-Goal assessment has been completed and submitted.

#### Att. Care Interruption Dates Field

The Attendant Care Interruption Dates field has a date field for recording when the patient experienced an unplanned disruption in personal attendant care. The date can be manually entered or selected by selecting the Calendar icon to designate the date when the incident occurred.

#### Attendant Loss Admissions Field

The Attendant Loss Admissions field has a date field for recording when the patient had to be admitted to a health care or extended care facility due to an unplanned disruption in personal attendant care. The date can be manually entered or selected by selecting the Calendar icon to designate the date when the incident occurred.

#### Attendant Care Interruptions in 5 Years Field

The Attendant Care Interruptions in 5 Yrs field is display-only and is calculated and populated from the Attendant Care Interruption Dates.

#### Attendant Loss Admissions in 5 Years Field

The Attendant Loss Admissions in 5 Yrs. field is display-only and is calculated and populated from the Attendant Loss Admissions field.

## Social Section of Participation and SWLS Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Marital Status Field

The Marital Status field is display-only and is populated by other applications.

#### Number in Household Field

The Number in Household Field is display-only and is populated after the Social Integration subscale of a CHART-SF Non-Goal assessment has been completed and submitted.

#### Metro/Micro/Rural Field

The Metro/Micro/Rural field is display-only and is populated by other applications. This field displays the classification of the patient’s residence based on their home address. A metropolitan area is one that has more than 50,000 residents. A micropolitan area has 10,000 to 49,999 residents. Areas with less than 10,000 residents are considered rural.

## Assessment Entry Forms on Participation & SWLS Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two instruments, the CHART-SF and Diener’s SWLS, are accessed from the Participation & SWLS tab.

### CHART-SF Assessment Entry Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select the *CHART-SF* button to launch the Craig Handicap Assessment and Reporting Technique – Short Form (CHART-SF) instrument. For more information, refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms).

#### CHART-SF History

The CHART-SF History field displays CHART-SF scores, record dates, and score types. Clicking on an assessment history line will open that assessment for viewing and editing.

### Diener’s Satisfaction with Life Scale (SWLS) Assessment Entry Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select the *SWLS* button to launch Diener’s Satisfaction with Life Scale (SWLS) instrument.

For more information about the SWLS instrument, refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms).

#### SWLS History

The SWLS History field displays SWLS scores, record dates, and score types. Clicking on an assessment history line will open that assessment for viewing and editing.

## CHART-SF Subscales Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CHART-SF Subscales section of the Participation & SWLS page contains the following subscales:

Physical (Current, Historic, Benchmark)

Cognitive (Current, Historic)

Mobility (Current, Historic, Benchmark)

Occupation (Current, Historic, Benchmark)

Social (Current, Historic, Benchmark)

Economic (Current, Historic, Benchmark)

Next to the subscales are fields that display CHART-SF scores and their associated record dates and score types. These fields are populated after a CHART-SF Non-Goal assessment has been completed and submitted. Clicking on an assessment history line will open that assessment for viewing and editing.

> **NOTE:** if any CHART-SF sub-section besides the required Physical Independence section, is not completed, the CHART-SF Total score and edit/view total score is blank

Next to the subscale field is the CHART-SF Benchmark for that particular subscale. The Benchmark fields are view-only and are based upon the Veteran’s ASIA neurological level and ASIA impairment derived from the Consortium for Spinal Cord Medicine (CSCM) Outcomes Clinical Practices Guideline (CPG) or Model Spinal Cord Injury System (MSCIS) data. Benchmark information for the Cognitive Independence subscale is currently unavailable.

## Occupation and Education Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](scido-version-3-user-manual/047.png)

The Occupation and Education Section of the Participation & SWLS tab includes the following fields:

#### Employment Status Field

Select the Veteran’s current employment status from the following:

EF = Employed Full Time

EP = Employed Part Time

RT = Retired

UU = Unemployed

NN = Unknown

#### Education Field

This field displays the value selected and saved in the [Highest Level of Education](#highest-level-of-education-field) field on the Registration page.

LH = Less than High School Graduate

HS = High School Graduate or GED

SC = Some College, Technical School, AA, or AS

CG = College Graduate

PR = Graduate or Professional School

#### Student? Field

Select either *Yes* or *No* to indicate whether the Veteran participates in education activities.

In the date field to the right, enter the date the person participated in education activities.

#### Student History

Previous student entries and associated dates are displayed in a history dropdown.

#### Volunteer? Field

Select either *Yes* or *No* to indicate whether the Veteran participates in volunteer activities. In the date field to the right, enter the date the Veteran participated in volunteer activities. Previous volunteer entries and associated dates are displayed in a dropdown, starting with the most recent entry.

#### Current Occupation Field

This field displays the occupation text entered in the most recently completed CHART-SF assessment.

#### Occupation at Injury Field

This field displays the patient’s type of occupation at the time of spinal cord injury or onset. It is populated from the [Occupation at Time of Injury](#occupation-at-time-of-injury-field) field in the Registration Tab. Department of Labor Occupation types include:

PR = Professional and technical

EX = Executive

SL = Sales

AD = Administrative support

PP = Precision Production

MO = Machine Operators

TR = Transportation

HA = Handlers

SV = Service

#### Information from the CHART-SF Assessment

The following information from the most recently completed CHART-SF assessment is displayed:

School Hours/Week

Employment Hours/Week

Homemaking Hours/Week

Home Maintenance Hours/Week

Recreation Hours/Week

# Assessment Entry Forms 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SCIDO application contains 20 instruments or assessment entry forms. The headers of most instruments are similar in appearance.

![](scido-version-3-user-manual/048.png)

After an assessment entry button has been selected from a Tab, the application displays the instrument with the patient name and division in the header of that instrument. Other values, such as Care Type and Care start date, may default into the form, but usually can be modified.

Some instruments do not contain a score field in the header. Some instruments such as Check Your Health (CYH) and SF-8 Health Survey will have extra score fields in the header.

Fields that must be completed to calculate or save the assessment are marked with a red asterisk as a reminder of their required status. Other unmarked fields may be required for some assessments depending on the values selected for the form. For example, if part of one section of the CHART-SF is completed, then that entire section must be completed.

## Header of Assessments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The header of most assessment forms contains the following fields.

#### Name Field

The Name field is display-only.

#### Record Date Field

The Record date is the date the assessment was performed by the Clinician or other care provider. This may be any date up to and including the current date. A future date cannot be used. The user may either manually enter the date or select the date from a calendar supplied with the form.

#### Division Field

The Division field is display-only and is populated by the application.

#### Care Type Field

The Care Type field may contain one of the following values:

Inpatient Rehabilitation

Outpatient Rehabilitation

Continuum of Care - Inpatient

Continuum of Care - Outpatient

Annual Evaluation

SCI Home Care

Extended Care

End of Life Care

Numeric Protocol Codes = 9-99

> **NOTE:** The care types of Inpatient Rehabilitation, Outpatient Rehabilitation, or Continuum of Care - Inpatient are used if there is an Episode of Care associated with the assessment. Refer to the [Episodes of Care](#episodes-of-care) section of this manual for further information.

#### Care Start Date Field

The Care Start Date field is display-only and is populated by the application when an assessment belongs to an episode of care. Refer to the section in this manual on [Episodes of Care](#episodes-of-care).

#### Score Field

Most assessment forms have one or more score fields, calculated by the application.

#### Score Type Field

For the Score Type, the following choices are available.

Start = ST A score type of “Start” is used to identify the beginning of a treatment or rehabilitation episode of care. It rarely is the same date that the patient is admitted to the medical center.

Goal = G A “Goal” score type is used to identify goals that the patient is realistically expected to achieve on a particular assessment at the close of an episode of care.

Interim = IN “Interim” score types are used to track patient progress in increments between the start and finish of treatment services.

Finish = FI A “Finish” score type is used to identify the patient’s status at the end of a treatment or rehabilitation episode of care. It is rarely the same date that the patient is discharged from the medical center

Follow-up = FO A “Follow-up” score type is used to identify if the patient’s status has been maintained at some time following completion of treatment or rehabilitation. The score type of Follow-Up may be used if there is a closed Episode of Care associated with the assessment.

Unknown = UN An “Unknown” score type should be used when a sequencing of score types is not indicated or when none of the previous score types are applicable. For example, assessments with a care type of Annual Evaluation would likely have “Unknown” score types.

If an assessment is part of an Episode of Care, rules will apply to which score types are available for each instrument type. Refer to the [Episodes of Care](#episodes-of-care) section in this manual for further information.

> **NOTE:** The term “assessment” refers to an instrument that has been completed. In this manual, the term “instrument” is used for the form completed during the assessment process.

## Button Functions on Assessments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most instrument forms contain the following buttons on each form.

#### Back Button

Select the *Back* button to return to the previous page.

#### Print Button

Select the *Print* button to print the assessment, including all responses that have been entered or selected.

The print function may be used at any time to make a paper copy of the completed assessment. The *Print* button is often used after the calculate function and before the submit function is used.

#### Blank Forms

Select the *Blank Forms* button to print a blank form in PDF format. The application will display the Blank Forms page with a list of all instruments. Select the Print icon by the desired instrument to print a blank instrument form. To view the Blank Forms page, refer to the section called [Blank Assessment Forms](#_Blank_Assessment_Forms).

#### Cancel Button

Select the *Cancel* button to exit the assessment form and return to the page from which it was launched. For example, when in the ASIA instrument, selecting the *Cancel* button returns the user to the Impairments page.

> **NOTE:** If any information was entered into the instrument or form, it will be lost when the *Cancel* button is selected.

#### Reset Button on Instruments

Select the *Reset* button to return to the most recently saved values on the form.

> **NOTE:** When the Calculate function has been used on a form, the Reset function on instruments returns the values entered or edited up to the Calculate function. The form values are not necessarily returned as the values when the form was first opened, but to the values when the form was last calculated.

#### Calculate Button on Assessments

Select the *Calculate* button to calculate and display the instrument score(s), if any.

#### Submit Button on Assessments

Select the *Submit* button to submit the data to the regional database. The system will display either an information message or a message that the assessment information was saved successfully.

Select OK to return to the previous page.

#### Help Button on Assessments

Select the *Help* button to access Online Help.

#### Calendar on Assessments

The Calendar icon provides the user with a calendar from which to select a date. The calendar function in an instrument works the same as the Calendar icon on tabs. Refer to the section called [Calendar](#calendar) in this manual.

## General Procedure for Creating Assessments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on the assessment type, the rules for creating, calculating, and submitting an assessment will vary. The basic procedure for creating a new assessment is described below.

#### Creating a New Assessment 

1\. Gather the assessment information.

2\. Use Patient Look-up to locate the patient in the application.

3\. Open the appropriate SCI Tab to locate the assessment form button.

4\. Select the assessment form button. The application will display the selected online form with the patient’s name and division.

5\. Manually enter the Record Date on which the assessment information was gathered or select the date from the Calendar.

6\. Select one of the following Care Types:

Inpatient Rehabilitation (requires episode of care \[EoC\] management)

Outpatient Rehabilitation (requires episode of care \[EoC\] management)

Continuum of Care – Inpatient (requires episode of care \[EoC\] management)

Continuum of Care – Outpatient

Annual Evaluation

SCI Home Care

Extended Care

End of Life Care

Or one of 91 specific protocols of care

7\. For some types of assessments (those with an EoC care type) a value may be displayed in the Care Start Date field. For EoC care types with Follow-up score types, a value is selected from the Care Start Date field.

8\. Select one of the following score types:

Start

Goal

Interim

Finish

Follow-up

Unknown

9\. Complete all required fields. Complete any desired optional fields.

10\. Select the *Calculate* button. The application will calculate the score(s).

11\. Select the *Submit* button. The application will provide notification when the assessment information was saved successfully.

12\. Select *OK*. The application will return to the tab from which the instrument is accessed.

## Editing Assessments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assessments may be viewed and edited. Some fields in the header, such as the care type and score type fields, cannot be modified. Special rules may apply for some assessments. For example, when editing a DUSOI assessment, the user will not be able to edit the record date.

> **NOTE:** The user may modify the responses on the assessment form, subject to the rules that apply to entering an assessment and the rules that apply for the particular assessment form.

#### Editing an Assessment, General Procedure

1\. Open the appropriate Tab page. See the [Instruments](#appendix-c-instruments-and-forms) section in this manual for the tab location of each assessment entry form button.

2\. Next to the desired assessment entry form button, select the History dropdown to display a listing of score(s), record dates, and score types for all assessments.

3\. Select the desired assessment history line by clicking on it.

4\. The application asks if you are sure you want to edit the assessment. Select *OK*.

5\. The Application displays the completed assessment form.

6\. View and modify the form subject to the rules that apply to creating, modifying, and saving all assessments and subject to the rules that apply to that particular assessment form.

7\. Upon completion of all edits, select the *Calculate* button.

8\. Select the *Submit* button.

Refer to [Appendix C: Instruments and Forms](#appendix-c-instruments-and-forms) for details about individual assessments or instruments.<span id="_Blank_Assessment_Forms" class="anchor"></span>  
<span id="_Toc183308852" class="anchor"></span>Blank Assessment Forms

Select the *Blank Forms* button from any assessment form to print a blank form in PDF format. The application will display the Blank Forms page with a list of all instruments. Select the Print icon by the desired instrument to print a blank instrument form. These forms are particularly useful for completion at the bedside. The assessment information can be entered into the application later from the handwritten form.

![](scido-version-3-user-manual/049.png)

## Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Progress notes may be created, signed, and submitted to CPRS-R for the following instruments:

Craig Handicap Assessment and Reporting Technique – Short Form (CHART-SF)

Functional Independence Measure (FIM)

Satisfaction with Life Survey (SWLS) (Diener’s)

For all three instruments, the system will prompt the user to write progress notes for the following combinations of score type and care type:

Score Type of Start and Care Type of Inpatient Rehabilitation (Goal-setting)

Score Type of Start and Care Type of Outpatient Rehabilitation (Goal-setting)

Score Type of Finish and Care Type of Inpatient Rehabilitation

Score Type of Finish and Care Type of Outpatient Rehabilitation

Score Type of Follow-up and Care Type of Inpatient Rehabilitation

Score Type of Follow-up and Care Type of Outpatient Rehabilitation

For the Functional Independence Measure (FIM), the user can elect to enter a free-text progress note that will be sent to CPRS for further authentication and entry. In addition to the combinations listed above, for the FIM, the system will prompt the user to write a progress note for the following combinations of score type and care type:

Score Type of Goal and Care Type of Inpatient Rehabilitation

Score Type of Goal and Care Type of Outpatient Rehabilitation

Score Type of Goal and Care Type of Continuum of Care--Inpatient

Score Type of Start and Care Type of Continuum of Care—Inpatient

Score Type of Finish and Care Type of Continuum of Care—Inpatient

Score Type of Follow-up and Care Type of Continuum of Care—Inpatient

Any Score Type and Care Type that is a Non-Episode of Care

Score Type of Interim and any Episode of Care Type

Score Type of Unknown and any Episode of Care Type

In addition to care type and score type, other variables or conditions (e.g., the ASIA Neurologic Level value and ASIA Impairment value), will determine whether the user is prompted with an information message with an opportunity to write a progress note. After submitting one of these assessments, within the information message about progress note, the user can select either *Yes* to write a progress note or *No* to not write a progress note. For example, after creating and selecting the *Submit* button for a CHART-SF with a score type of Start and care type of Inpatient Rehabilitation, the system responds with an information message:

![](scido-version-3-user-manual/050.png)

#### Example of a CHART-SF Progress Note with Goal Template

The application displays a goal template when the score type for the patient is Start and the care type is either Inpatient Rehabilitation or Outpatient Rehabilitation.

![](scido-version-3-user-manual/051.png)

Select the Visit Location from the list in the dropdown field.

Select the Service Type from the list of types in the dropdown field.

Enter the goal for each subscale and select *Submit*. The application responds with the form that will be submitted to CPRS.

Motor Efficiency and Cognitive Efficiency display up to 2 post-decimal places:

> <u>Motor Efficiency</u> = (Motor Finish Score - Motor Start Score)/Length of Rehab

> <u>Cognitive Efficiency</u> = (Cognitive Finish Score - Cognitive Start Score)/Length of

> Rehab

> <u>Length of Rehabilitation</u> = (Care finish date - Care start date - \[Length of 3 longest

> interruptions in care\])

To save the progress note, the user must enter their electronic signature code and select *Submit*.

> **NOTE:** the Visit Location, Service Type, and Electronic Signature Code are required fields.

| ![](scido-version-3-user-manual/052.png) |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Reports_Tab_1" class="anchor"></span>

# Reports Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports Tab provides access to the various reports that can be generated by the application. The benefits of accurately maintaining the SCIDO application for Veterans with spinal cord injuries or disorders are reflected in the reports.

> **NOTE:** Access to certain reports is limited to the specific role of the user (Administration, Clinician, or Researcher).

![](scido-version-3-user-manual/053.png)

The Reports page contains reports sorted into the following groups:

Impairments and Medical Complications Reports

Cumulative Reports

Patient Listing(s) Reports

Filtered Reports

Custom Reports

Preformatted reports regarding impairments and medical complications, aggregate outcome reports, and patient listings are on the left side of the Reports Tab. These preformatted reports require few or no additional selections from the user once the report is selected. Select the report title to open the report.

Reports in the Impairments and Medical Complications section contain no intermediary filters. For reports in the Cumulative reports and Patient Listings, the application will provide the required or optional parameters, such as start date and end date.

For the filtered reports, a report filters page displays first. This provides the user with an option of filtering these reports. Filters allow the selection of specific portions of the population to be included in the report while excluding all others. Refer to the section [Filtered Reports](#filtered-reports) in this manual.

The Cumulative, Patient Listing(s), Filtered, and Custom Reports may be converted to one of two formats:

Comma Separated Values (CSV)

Excel

Select the format after the Export Options label by clicking on either CSV or Excel.

![](scido-version-3-user-manual/054.png)

## Custom Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Custom reports for the SCIDO population can be created using the Report Designer, located on the right side of the Reports Tab. The Report Designer allows the user to select the criteria, format, and information needed for a report. Custom reports output displays all applicable records within the filter criteria.

To generate a custom report, first select a category and subject area of information to use in the report. Then select specific attributes to print in the report or to use as filters or sorting criteria. Sorting determines the order in which the rows of information occur. Filters allow the selection of specific portions of the population to be included in the report while excluding all others.

For more information, refer to the section in this manual called [Custom Reports](#custom-reports-1).

## Impairments and Medical Complications Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Impairments and Medical Complications reports provide information regarding diagnoses, procedures, treatments, medications, laboratory results, radiological findings, and outcomes that pertain to a specific health condition, status, or concern:

Influenza Diagnoses and Treatment

Influenza Immunizations

Pain Assessment and Treatment

Pneumococcal Immunizations

Pneumonia and Respiratory

Pressure Ulcer Report

Urinary Tract Infections

After the user has selected a date range for a report, information regarding the above topics is displayed from other VistA applications. This information is display-only. The default is five years if another date range is not selected.

Two of the reports in the Impairments and Medical Complications section of the Tab provide summary information for Veterans with SCI&D from the Resident Assessment Instrument–Minimum Data Set (RAI-MDS):

RAI-MDS Quality Indicators Report

RAI-MDS Resource Utilization Groups

The RAI-MDS is used in all VA Community Living Centers (CLC) and VA Spinal Cord Injury (SCI) Units surveyed under the Joint Commission on Accreditation of Healthcare Organizations (JCAHO) Long-Term Care (LTC) standards. The standardized RAI-MDS has been shown to contribute to improvement of care quality, nursing record documentation, and in resident cooperation and engagement.

The <u>RAI-MDS Quality Indicators</u> Report provides information for a specific patient on twenty-five quality indicators derived from the Resident Assessment Instrument–Minimum Data Set (RAI-MDS). The default date for this report is the previous month. The user can also select a different month from the dropdown for a report. Information regarding these twenty-five quality indicators is displayed if the patient is in a Joint Commission on Accreditation of Healthcare Organizations (JCAHO) Long-Term Care (LTC) setting in the VA. Even though information may not be available for the specific patient, summary information regarding these twenty-five quality indicators at both the regional and national levels will be provided.

The <u>RAI-MDS Resource Utilization Groups (RUG)</u> Report provides information about resource utilization groups, assessment activities of daily living, and RUG case mix index weights for all Veterans at the SCI regional level. This information will be provided for Veterans with SCI in JCAHO Long-Term Care Settings in the VA.

## Cumulative Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cumulative Reports produce statistical reports of Outcomes information across diagnostic categories, based on user-selected range of care end dates. A definition of each row displayed in the reports is provided in [Appendix D.](#_Appendix_D:_Reports)

Annual Evaluation Outcomes Report

Continuum of Care Inpatient Outcomes

Inpatient Rehabilitation Outcomes

Outpatient Rehabilitation Outcomes

## Patient Listing(s) Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Patient Listing(s) Reports provide summary displays of information about patients either at your medical center or throughout the SCI region depending on the settings chosen on the Administration page when setting up the application. Some reports, such as the Inpatient/Outpatient Report and Inpatient/Outpatient Specific report, may have slow response times.

<u>Admissions (SCI&D)</u> Report provides a list of SCI&D patients who have been admitted within a user-specified date range. The list consists of admitted patients who are either in the SCIDO application or who have been marked as SCI in the Patient file (i.e., field 57.4, "SPINAL CORD INJURY"). This option is useful in highlighting patient records that are not yet in the SCIDO application.

The <u>Applications for Inpatient Care</u> Report produces a report on applications for inpatient care during a specific range of dates.

The <u>Community Discharges</u> Report provides a list of SCI&D patients who have been discharged within a user-specified date range and discharge destinations. A discharge to independent living (community discharge) rate is also calculated.

The <u>Discharges (SCI&D)</u> Report produces reports on discharged patients for a user-selected date range displaying discharge dates, discharge location, diagnosis codes, and other information.

The <u>ICD Code Search</u> Report allows users to find patients in or out of the SCIDO application who have one particular ICD code, have several ICD codes, or fall within a range of ICD codes. The report searches the patients in the inpatient PTF file (#45) according to user-specified admission dates and will include patients who have any of the specified inpatient ICD codes This report has a 90 limit maximum for ICD Code items.

The <u>Patient Education</u> Report provides a list of SCI&D patients who have a date of onset within a user-specified date range and a user-selected date range of educational sessions. This report displays their completion of sixteen educational modules and calculates completion rates for sixteen educational topics.

The <u>Patient Summary</u> Report provides basic registration information for either one patient or all SCI&D patients. The value that displays in the SCI Level column corresponds to the ASIA Neuro Level. The value that displays in the Extent of SCI column corresponds to Complete or Incomplete from ASIA.

The <u>Readmissions Report</u> displays a list of SCI&D patients based on user-selected date range of discharge dates. The number of readmissions to a VA Medical Center within thirty days of discharge from an index hospitalization is displayed by medical center division and ward at time of discharge.

## Filtered Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Filtered reports allow the selection of specific portions of the population for review before the reports are generated.

Filters are used to include only certain types of data in a report while excluding others. For example, the user can restrict a report to only persons who are over the age of 65 and are ≥ 70% Service - Connected. No filtering is performed if a value is not selected for a filter. Filtered reports include:

<u>Basic Patient Information</u> Report displays the patient's Name, Social Security Number (SSN), Date of Birth, Telephone Number, Street Address 1, Street Address 2, City, State, and ZIP Code.

<u>Breakdown of Patient</u>s Report uses demographic categories to summarize characteristics of a caseload of Veterans. This report may be limited to a specific time interval in addition to all the standard filter options.

<u>Current Inpatients</u> Report displays those patients in the SCIDO application who currently have an inpatient status. This report displays the patient’s Name, Last Four of the SSN, Ward, Admission Date, Current Length of Stay, Fiscal Year to Date Length of Stay, Admission Diagnosis, Patient’s Room and Bed.

<u>Expanded Patient Listing</u> Report displays the Patient Name, SSN, Home Telephone, Network Status, Registration Status, Address (including county), Last AE Offered, Last AE Received, Eligibility, Primary Care VAMC, Provider, Neuro Level, Etiology, and Date of Onset.

<u>Patients with Future Appointments</u> Report displays patients having future clinic appointments within a user specified date range. The user may select SCI&D patients both from within and outside the application. The report displays the appointment date and time, Clinic Name, Patient Name, and Last Four Numbers of the SSN.

<u>Follow-Up Last A.E. Received</u> Report identifies patients who have not had an annual evaluation within a specified period of time. The user will be prompted to select a period of time.

<u>Follow-Up (Last Seen)</u> Report identifies patients who have not been seen for VA health care within a specified period of time. The user will be prompted to select a period of time.

<u>Inpatient Outpatient Activity</u> Report produces reports on inpatient stays and outpatient stops and visits over a specific range of dates.

> **NOTE:** A "stop" is credited for each entry of a stop code. A "visit" is distributed among each stop credited on a given date. A single visit with two stop codes credited shows as 0.5 visits for each stop code. A total of 1.00 visits is given for outpatient activity on a given date. The "Number of highest users to identify" refers to the number of patients that were the most active that should be shown on the report.

<u>Inpatient Outpatient Specific at Your Divisio</u>n Report displays information on patients who have used specific inpatient or outpatient resources. For outpatient activity, the option indicates the number of visits to the clinic STOP CODE(s) specified during the indicated time period. The number of stays and length of stay within a specific Specialty indicate inpatient activity. The user can select a date range, specific clinics, specific bed sections, and select clinics and statistics and/or patient usage data.

<u>Laboratory Utilization at Your Division</u> Report summarizes laboratory use by patients in the application over a selected date range.

<u>Lab Utilization (Specific)</u> at Your Division Report produces specific laboratory utilization displays for patients in the application. The user is prompted to enter a Range of Dates, Laboratory Test Names (can select up to 20 laboratory test names), and select specific laboratory tests and statistics and/or patient usage data.

<u>Mailing Labels</u> Report produces information to produce mailing labels for patients in the application. Mailing label information may be downloaded into an electronic spreadsheet that could be used with mail merge functionality to produce formatted labels for specific mailing label products.

<u>MS (Kurtzke) Measures</u> Report displays MS (Kurtzke) Functional System Scale Scores (FSS) and Expanded Disability Summary Scale Scores (EDSS) for selected patients. It also displays patient date of birth (DOB) and social security number (SSN).

<u>New SCI&D Patients</u> Report lists SCI&D patients who have a recent registration date within a user-selected registration date range. The report displays the patient’s Registration Date, Name, SSN, Etiology, and VA SCI Status in the Patient File.

<u>Patient Listing Report</u> displays Patient Name, SSN, Date of Birth, Eligibility, Means Test, Neurological Level, Primary Care Provider, AE Received, AE Next Due Etiology, and Date of Onset

<u>Patient Listing by State and County</u> Report provides basic patient information sorted by county and state. Information displayed includes state, county, patient name, social security number, date of birth, eligibility, means, neurological level, primary care provider, annual evaluation received date, annual evaluation next due date, etiology, and date of onset.

<u>Pharmacy Utilization at Your Division</u> Report displays use of pharmacy medications and some supplies for patients in the application. A user-selected date range, minimum number of fills to display, minimum dollar cost of dispensed fills to display, the highest number of users to identify, and the method for computing dollar costs are options for defining report parameters.

> **NOTE:** the output may contain other medications in the report output if other fills are attached to the patients within the time frame regardless of the medications selected on the filters page. If the user wants to see only specific drugs in the report, the user must run the Pharmacy Utilization (Specific) report.

Pharmacy Utilization (Specific) at Your Division Report displays use of a specific generic medication name for patients in the application and displays the dollar cost of prescriptions. The user is prompted to enter a range of dates, select a generic drug name (can select up to 20 generic drug names), and select specific medication fills and statistics and/or patient usage data.

<u>Prosthetics Utilization at Your Division</u> Report displays use of prosthetic devices and sensory aids for patients in the application. A user-selected date range can be specified for generating the report.

<u>Prosthetics Utilization (Specific) at Your Division</u> Report displays use of a specific prosthetic device or sensory aid for patients in your SCIDO application and displays the dollar cost of these items. The user is prompted to enter a range of dates and select a prosthetic item, multiple items, or a range of items (can select up to 20 prosthetic items).

<u>The Radiology Utilization at Your Division Report</u> has multiple sections showing the various completed radiology procedures and their associated costs (if the cost data is present) during the user-selected date range. Minimum number of procedures, minimum dollar cost of procedures, and highest number of users to identify are also user-selected parameters for the report.

## Report Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Report Filters page is used to select criteria for reports. After launching a filtered report from the middle Filtered Reports section of the Reports page, the Report Filters page displays.

![](scido-version-3-user-manual/055.png)

For filters with a dropdown, such as Primary Care VA, enter the first letter, and the system will go to that alphabetical section. If a filter can have more than one criterion, to select more than one criterion at one time, hold down the Ctrl Key and highlight all desired criteria. To select a range of criteria, select the first criterion, hold down the Shift key, and make the final selection.

> **NOTE:** The filter parameters selected on the Filters Page are displayed following the data in the report output.

The following filters are available:

Additional Care VA – Select the facility and facility number from the dropdown. Enter the first letter of the facility and the system will go to that alphabetical section.

Age

Youngest

to Oldest

Annual Evaluation Next Due

Start Date

to End Date

Annual Evaluation VA – Select the facility and facility number from the dropdown. Enter the first letter of the facility and the system will go to that alphabetical section.

ASIA Impairment - multiple selections are allowed. The ASIA Impairment Scale is filtered based on most recent Non-Goal ASIA.

A

B

C

D

E

Unknown

ASIA Neurological Level. The ASIA Neurological Level is filtered based on most recent Non-Goal ASIA.

Top Neuro. Level

to Lowest Neuro. Level

Category of Injury

Tetraplegia

This filter selection returns records with Computed ASIA Neurologic Level is equal to C01, C02, C03, C04, C05, C06, C07, or C08

Paraplegia

This filter selection returns records with Computed ASIA Neurologic Level equal to T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, L01, L02, L03, L04, L05, S01, S02, S03, S04, or S05.

Cause of Injury

Traumatic

Non-Traumatic

County

State

County

Division – Select the division from the dropdown. Enter the first letter of the division and the system will go to that alphabetical section.

Etiology – Multiple selections are allowed. Select the etiology from the following:

TFA = Fall

TSA = Sports Activity

TVE = Vehicular

TVI = Violence

TOT = Other (Traumatic)

TUN = Unknown (Traumatic)

NAD = Arthritic Disease or Cervical Stenosis

NIA = Infection or Abscess

NMN = Motor Neuron Disease

NMS = Multiple Sclerosis

NPM = Poliomyelitis

NSY = Syringomyelia

NTU = Tumor

NOT = Other (Non-Traumatic)

NUN = Unknown (Non-Traumatic)

NTV = Vascular

Fee Basis

Start Date

to End Date

Geographic Area

Start Zip Code (Five Digits)

to End Zip Code (Five Digits)

Hours of Help Needed (from the CHART-SF)

Low Value to High Value

Start Date to End Date

Inpatient Visit

Start Date

to End Date

Medications (Under Construction) – Select the medications from the dropdown. Enter the first letter of the medication, and the system will go to that alphabetical section.

Start Date

to End Date

Outpatient Visit (Under Construction) – Select the Outpatient Clinic(s) from the dropdown. Enter the first letter of the clinic name, and the system will go to that alphabetical section.

Start Date

to End Date

Primary Care VA – Select the facility and facility number from the dropdown. Enter the first letter of the facility, and the system will go to that alphabetical section.

Prosthetics (Under Construction) –Select the prosthetics item(s) from the dropdown. Enter the first letter of the prosthetic item, and the system will go to that alphabetical section (CPT code and or Description).

Race – Multiple selections are allowed from the following:

American Indian or Alaskan Native

Asian

Black or African American

Hispanic or Latino

Native Hawaiian or Pacific Islander

White

Unknown or Refused

Ethnicity

Hispanic or Latino

Not Hispanic or Latino

Unknown

Registration Status – Multiple selections are allowed

Not SCD

SCD – Currently Served

SCD – Not Currently Served

Expired

SCI Network

Yes

No

Service Connection

% Start Value

% End Value

Sex

Male

Female

Total FIM Change

Smallest Change

Largest Change

Start Date

To End Date

Vital Status

Alive

Dead

Walk/Wheelchair (Under Construction) – Select one button from Walk, Wheelchair, or Both.

Start Date

to End Date

# Administration and Information Resource Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Administration Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Administration Page provides the functionality to

- View user roles and record access permissions
- Activate or inactivate patient status
- Import patient records from the national database
- Activate or inactive Episodes of Care
- Activate or inactivate patient assessments
- View patient identity values and acquire a national Integration Control Number (ICN)
- Add or delete SCI, Multiple Sclerosis (MS), and application support mail groups
- View medical centers in SCI regions (also known as catchments)

![](scido-version-3-user-manual/056.png)

> **NOTE:** In order to access the Administration Page, the user must be assigned the role of Administrator. Users may have roles of clinician, administrator, or researcher. Another role of IRM is for an information resource management role, described in the IRM section. When a user with an administrator role accesses the application, an additional tab labeled Admin is located in the footer of the application to permit access to Administrator functions.

### User Roles and Record Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application displays user roles and system access to records for either the local institution or the entire SCI region. User roles and system access are defined in VistA. Roles and access are assigned through VistA File 200, the “New Person” File. The Automated Data Processing Applications Coordinator (ADPAC) can modify the user’s SCIDO profile in VistA File 200. The ADPAC will need to know whether the user has the role of a clinician, administrator, or researcher. Most SCI Coordinators at SCI Primary Care Teams need to be assigned the role of administrator (which includes the capabilities of the Clinician role). Research access is limited to those who have an approved VA research project and approval from an Institutional Review Board (IRB).

#### Regional or Institutional View

The user can request from an ADPAC either an institutional or regional view of information. An institutional view is recommended to improve response time. Users should note that access to the SCI region may provide a more comprehensive view of patient status and the SCI&D population. However, response times may be slower. An institutional view is recommended for most clinicians.

#### User Roles

The application allows a user to access the application and to work within an assigned area of the application. Valid roles are Clinician, Administrator, Researcher, and IRM.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Role</strong></th>
<th><strong>Access</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinician</td>
<td>Clinicians who have clinical privileges to create, modify, display, store, and sign patient information into the computerized patient record system (CPRS). </td>
</tr>
<tr class="even">
<td>Administrator</td>
<td>Individuals who have SCIDO application management permissions for identifying mail groups and deleting records (SCIDO Coordinators, CACs, ADPACs, etc.). The administrator role includes Clinician role capabilities.</td>
</tr>
<tr class="odd">
<td>Researcher</td>
<td><p>Researchers are provided limited access to aggregate patient data only (national access only).</p>
<p>Researchers are allowed to query and generate reports from the national SCIDO database after they have documented they have an approved VA research project, approval from an Institutional Review Board, and an approved Data Transfer and Data Use Agreement from VHA Patient Care Services. </p></td>
</tr>
<tr class="even">
<td>IRM</td>
<td>The Information Resource Management (IRM) role allows modification of the SCIDO application, such as being able to add or delete medical centers from SCI regions, modify regional attributes, perform database seeding, perform a national or regional audit, and monitor system activity.</td>
</tr>
</tbody>
</table>

### SCI Region List of Institutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SCI regions (also known as catchments) include SCI centers and associated SCI primary care team facilities. Institutions belonging to the SCI region are displayed by Number and Name. A user with Admin permission can view the medical centers within their region, but only the IRM can add or delete medical centers from the SCI Region list on the IRM page. Refer to the section on the IRM tab.

### Import Patient Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A SCIDO Administrator may import patient records from the national database. This function is useful for patients who relocate to or from an area. The patient’s records may not be available at the current location, so the Administrator is asked to import their records. This function imports all SCIDO records for a patient.

#### Import Patient Records

Before this procedure starts, you have already navigated to the correct patient record and the Admin Tab page.

1\. The patient ID and Patient Status (Active or Inactive) is displayed in the Patient Information Management section of the Admin page.

2\. Select the *Import* button to import the patient’s records from the national database.

3\. A message is displayed asking if you are sure you want to import the current patient from the national SCIDO database. The system displays OK and Cancel options.

4\. Select the *OK* button to continue the import process.

5\. If the system matches at least one record to the SSN, a window labeled “Import Patient from National SCIDO Registry” displays the Patient Name, SSN, Institution, Status, and Date of last Review.

![](scido-version-3-user-manual/057.png)

6\. Select the button in the Select column by the patient name whose records you want to import and select the *Submit* button to request the import process for this patient’s records to continue.

7\. The system displays a message “The local SCIDO has been updated with the selected patient’s information.”

8\. Select the *OK* button.

### Activate or Inactivate a Patient’s Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A SCIDO Administrator may activate or inactivate a patient’s status locally. This function is used for patients who relocate to or from the SCI region. Activation of a Veteran’s status indicates a non-deleted status. When a Veteran’s status is inactivated, medical information for the Veteran will not be displayed or included in SCIDO application reports for that institution.

#### Activate a Patient within the SCI institution

Before this procedure starts, you have already navigated to the correct patient record and the Admin Tab page.

1\. The application displays the Administration page with the patient’s ID and Patient Status displayed in the Patient Information Management section.

2\. Select the *Activate* button.

3\. The system asks, “Are sure you want to activate the current patient?”

4\. Select the OK option.

5\. The patient’s status is displayed as “Active.”

#### Inactivate a Patient within the SCI Institution

Before this procedure starts, you have already navigated to the correct patient record and the Admin Tab page.

1\. The Administration page with the patient’s ID and Patient Status displayed in the Patient Information Management section.

2\. Select the *Inactivate* button.

3\. The system asks, “Are sure you want to inactivate the current patient?”

4\. Select the OK option.

5\. The patient’s status is displayed as “Inactive.”

#### Activate or Inactivate Episodes of Care

A SCIDO Administrator may cautiously activate or inactivate a patient’s episodes of care. This can be useful when records are initially migrated or after patients imported records have time conflicts between records. Activation or inactivation of episodes of care should be done with great caution as problems can be created for assessments.

When an episode of care is inactive, it will no longer be displayed on the Episodes of Care Management page. To active or inactive an episode of care, select the Window Expander icon, and a new window is displayed with a list of episodes of care for the patient. Select the Active or Inactive from the dropdown by the episode of care and select the *Submit* button to submit the information.

The SCIDO system prevents activating overlapping EOCs by displaying the following message: “Episode of Care overlap detected. Changes were not saved.”

#### Activate or Inactivate Assessments

A SCIDO Administrator may activate or inactivate a patient’s assessments within an SCI facility. Inactivation is used to inactivate erroneous records that cannot be appropriately modified through the assessment editing process.

To activate or inactivate an assessment, select the Window Expander icon ![](scido-version-3-user-manual/058.png) next to the Assessments field, and a new Window opens with a list of assessments for the patient:

![](scido-version-3-user-manual/059.png)

Select the *Active* or *Inactive* from the dropdown by the assessment and select the *Submit* button to submit the information.

The system displays all assessment summary information for the selected patient as contained in the local SCIDO, sorted alphabetically with the ASIA first in Record Date order from the most recent to the most remote.

#### Acquire National Integration Control Number (ICN)

The Administrator selects the *Acquire National ICN* button to acquire an Integration Control Number (ICN) from the Master Patient Index (MPI) Service for the selected patient at the national level. After this option is selected and the *OK* button selected, the System displays a message: “A request has been sent to the Master Patient Index (MPI) to assign a National ICN. Check back in a few minutes to see if it has been assigned.”

The System sends a query to MPI for a national ICN, which will be used to link patients to their records across VHA systems, the Master Patient Index (MPI/PD) at the national database, and across regions within SCIDO. The system will display the national ICN after a few minutes in the Patient Identity Values section as a Type, which is a GLOBAL_ICN. The Value is a unique number in MPI. The institution is the institution that the Administrator is logged into and at which the patient is registered.

![](scido-version-3-user-manual/060.png)

#### Establish or Remove Mail Groups

A SCIDO Administrator can modify, add, or delete mail groups. If a site wants to be able to notify a specific group when patients with SCI or MS are admitted or discharged, VistA mail groups can be created for that purpose. Only the names of VistA mail groups should be entered since other e-mail systems are not HIPAA or Privacy Act compliant. There are three types of e-mail groups that can be entered: SCI Notification Mail Group(s), MS Notification Mail Group(s), and SCIDO Application Support Group(s).

![](scido-version-3-user-manual/061.png)

Mail Group Management Section of the Administration Page

To add an SCI mail group, select the group type from the dropdown, enter the group address, and select the *Submit* button. The group address must be entered correctly since no matching or global directory functionality exists. The same process is done to add a Multiple Sclerosis (MS) or Application Support mail group.

To remove a mail group, select the Trashcan icon in the Delete column for that mail group.

#### SCI Region Definition

The SCI Region Definition section displays the SCI Region name and a list of the institutions (by name and number) that belong to that region. This information can only be viewed. Refer to the Information Resource Management (IRM) section for information on how SCI regions are defined.

![](scido-version-3-user-manual/062.png)

## Information Resource Management (IRM) Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Information Resource Management (IRM) tab allows a user with the IRM role to modify regional attributes, add or delete medical centers from their SCI region, perform a national or regional update, and monitor system activity. This section provides a brief description of the IRM capabilities.

The functionality exists on this page to update the region based on data for the specific region in the National Repository or to update the National Repository based on data for the specific region held in the local repository.

> **WARNING:** a reverse seeding has the potential to overwrite data at the National level and this action should be coordinated.

![](scido-version-3-user-manual/063.png)

### Regional Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM/ISS/ITC staff may modify the SCI region by specifying regional and national endpoints, the MPI Application Name, and Database Version. Great care should be exercised in modifying these parameters since it is likely to have profound effects on the functionality of the SCIDO application and regional versus institutional views of information for the users.

### Regional Institutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SCI Regions (also known as catchments) include SCI centers and associated SCI primary care team facilities. Institutions belonging to the SCI region are displayed by Number and Name. Only an IRM can add or delete medical centers from the SCI Region list.

### Monitor System Activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An IRM may monitor system activities, which include the following:

Record locks

Audit log report (list of persons who have entered or edited information within the application)

#### Record Locks

IRM/ISS/ITC staff can view details about the system, such as which patient records are being viewed by users, and which user has Assessment or Episode of Care (EoC) locks on patients’ records by selecting the *Locking Detail* button. In the example shown below, a user (USER Gui SCIclinician) is adding an assessment for the patient SPINALCORD, NINETEEN, so a record lock is created so that other users may not add assessments for that patient as long as another assessment is in the process of being created.

![](scido-version-3-user-manual/064.png)

#### Audit Log Report

The Audit Log Report allows IT staff to report information about the SCIDO system at the local division. IT staff can create reports to display user data, such as how many assessments have been created and who has entered or modified an assessment for a particular patient or for all patients during any time period. For example, it can determine by date and time, which users logged in to or out of the system.

| ![](scido-version-3-user-manual/065.png) |
|--------------------------------------------------------------------------------------------------------------------------|

### National/Regional Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IT staff can synchronize data between the regional database and the national database by using the *National/Region Update* button. IT staff can choose to either update the regional database based on data for this region in the national database or update the national database with information from the regional database.

> **NOTE:** A valid email address must be entered for completion of notification. Entering an invalid address will cause the system to notify the user that the format is invalid.

| ![](scido-version-3-user-manual/066.png) |
|---------------------------------------------------------------------------------------------------------------------------------------------|

# Appendix A: Definitions and Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Definitions

| Term      | Definition                                                                                                                                                                                                                                                                                        |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Assessment    | An instrument, measure, or other survey in the SCIDO application, such as the CHART-SF or the ASIA, after it has been completed and contains patient data                                                                                                                                             |
| Audit Trail   | A history of the changes made to a record including the name of the user who made the change                                                                                                                                                                                                          |
| Division      | A subunit of the institution list.                                                                                                                                                                                                                                                                    |
| Institution   | A hospital with or without subdivisions.                                                                                                                                                                                                                                                              |
| Instrument    | A measurement form or questionnaire that is used to evaluate a patient’s impairments, medical complications, activities, participation, or satisfaction with life. The instrument does not contain data, but is used to capture data specifically related to one patient at a specified point in time |
| MH Assistant  | Mental Health Assistant                                                                                                                                                                                                                                                                               |
| Outcomes      | Documented results or changes in patient’s performance and conditions in relation to the interventions or services used                                                                                                                                                                               |
| Thin-client   | A simple client program, which relies on most of the function of the system being in the server, usually the Web browser in a Web domain                                                                                                                                                              |
| User          | An Administrator, a Clinician, or a Researcher who uses the application                                                                                                                                                                                                                               |
| VistA         | Veterans Health Information System and Technology Architecture                                                                                                                                                                                                                                        |
| VistA MailMan | VistA’s electronic mail system                                                                                                                                                                                                                                                                        |

#### Acronyms

| Acronym  | Definition                                                                                                             |
|--------------|----------------------------------------------------------------------------------------------------------------------------|
| ADPAC        | Automated Data Processing Application Coordinator                                                                          |
| ASIA         | American Spinal Injury Association                                                                                         |
| AUDIT        | Alcohol Use Disorders Identification Test                                                                                  |
| BMI          | Body Mass Index                                                                                                            |
| CAGE         | Brief alcohol disorder assessment instrument (CAGE is not an acronym)                                                      |
| CARF         | Rehabilitation Accreditation Commission previously known as Commission on the Accreditation of Rehabilitation Facilities   |
| CES-D        | Center for Epidemiologic Studies Depression Scale                                                                          |
| CHART-SF     | Craig Handicap Assessment and Reporting Technique – Short Form                                                             |
| CCOW         | Clinical Context Object Workgroup                                                                                          |
| CCR          | Computerized Clinical Reminder                                                                                             |
| CPRS         | Computerized Patient Record System                                                                                         |
| CPT          | Current Procedural Terminology                                                                                             |
| VS           | Vital Signs                                                                                                                |
| DAST         | Drug Abuse Screening Test                                                                                                  |
| DBIA         | Database Integration Agreement                                                                                             |
| DUSOI        | Duke Severity of Illness                                                                                                   |
| DUSOI-A      | Duke Severity of Illness Analog Scale, an instrument that is faster to complete than the DUSOI, but provides fewer details |
| FAM          | Functional Assessment Measure                                                                                              |
| FIM          | Functional Independence Measure                                                                                            |
| GUI          | Graphical User Interface                                                                                                   |
| HCPCS        | Healthcare Common Procedure Coding System                                                                                  |
| HL7          | Health Level Seven (standard for electronic data exchange/messaging protocol)                                              |
| HSD&D        | Health Systems Design and Development                                                                                      |
| HTTP         | HyperText Transfer Protocol                                                                                                |
| HTTPS        | HyperText Transfer Protocol Secure                                                                                         |
| ICN          | Integration Control Number                                                                                                 |
| IE           | Internet Explorer                                                                                                          |
| IEN          | Internal Entry Number                                                                                                      |
| JCAHO        | Joint Commission on Accreditation of Healthcare Organizations                                                              |
| Kurtzke EDSS | Kurtzke Expanded Disability Status Scale (used for Multiple Sclerosis)                                                     |
| Kurtzke FSS  | Kurtzke Functional Systems Scale (used for Multiple Sclerosis)                                                             |
| LOINC        | Logical Observation Identifiers, Names, and Codes                                                                          |
| MNFM         | Medical Needs and Function Modifiers                                                                                       |
| NOIS         | National Online Information System                                                                                         |
| PCE          | Patient Care Encounter                                                                                                     |
| PIMS         | Patient Information Management System                                                                                      |
| PRIME-MD     | Primary Care Evaluation of Mental Disorders                                                                                |
| PSL          | Person Service Lookup                                                                                                      |
| PTF          | Patient Treatment File                                                                                                     |
| PUSH         | Pressure Ulcer Scale for Healing                                                                                           |
| SCD Registry | Spinal Cord Dysfunction Registry                                                                                           |
| SCI&D        | Spinal Cord Injury and Disorders                                                                                           |
| SCIDO        | Spinal Cord Injury and Disorders Outcomes Application                                                                      |
| SF-8         | SF-8 Health Survey                                                                                                         |
| SF-MPQ       | Short Form McGill Pain Questionnaire                                                                                       |
| SRS          | Software Requirements Specifications                                                                                       |
| SSO          | Single Sign-On                                                                                                             |
| SWLS         | Satisfaction with Life Scale (Diener’s)                                                                                    |
| TBI          | Traumatic Brain Injury                                                                                                     |
| TCP/IP       | Transmission Control Protocol/Internet Protocol                                                                            |
| TIU          | Text Integration Utility                                                                                                   |
| VA           | Department of Veterans Affairs                                                                                             |
| VHA          | Veterans Health Administration                                                                                             |
| VISN         | Veterans Integrated Service Network                                                                                        |

# Appendix B: Copyright Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASIA: Reproduced with permission from the American Spinal Injury Association. Copyright © 2003 American Spinal Injury Association (ASIA). All rights reserved.

AUDIT: Reproduced with permission from the World Health Organization. Copyright © World Health Organization, Geneva.

CAGE: In the public domain from JA Ewing, ‘Detecting Alcoholism: The CAGE Questionnaire’ JAMA 252: 1905-1907, 1984.

CES-D: Reproduced by permission. Copyright © 1977 West Publishing Company/Applied Psychological Measurement, Inc.

CHART-SF: Reproduced with permission from Craig Hospital Research Department. Copyright © 1988, 1992, 1996 Craig Hospital.

CYH: Reproduced with permission from the University of Montana Rural Institute: A Center for Excellence in Disability Research, Education and Services. Copyright © 1990 University of Montana Rural Institute.

CYH – Secondary Conditions: Reproduced with permission from the University of Montana Rural Institute: A Center for Excellence in Disability Research, Education and Services. Copyright © 1990 University of Montana Rural Institute.

DAST: Reproduced or adapted with permission from the Centre for Addiction and Mental Health. Copyright © 1982 Centre for Addiction and Mental Health.

DUSOI: Used and reformatted with permission of Duke University. Copyright © 1993 Duke University Office of Science and Technology.

DUSOI-A: “Used and reformatted with permission of Duke University. Copyright © 1993 Duke University Office of Science and Technology.

EDSS: Reproduced with permission from John F. Kurtzke, M.D. Copyright © 1983 John F. Kurtzke, M.D.

FAM: Reproduced with permission from Karyl Hall, Ed.D. Copyright 1995 © Santa Clara Valley Medical Center.

FIM™ Instrument: Reprinted with the permission of Uniform Data System for Medical Rehabilitation and Carl V. Granger, M.D. Copyright © 1993, 2001 Uniform Data System for Medical Rehabilitation, UB Foundation Activities, Inc. FIM is a trademark of the Uniform Data System for Medical Rehabilitation, a division of UB Foundation Activities, Inc.

FSS: Reproduced with permission from John F. Kurtzke, M.D. Copyright © 1983 John F. Kurtzke, M.D.

MNFM: In the public domain. No copyright is claimed in government works.

PRIME-MD: Reproduced with permission to use the two-question depression screening instrument from Mary A. Whooley, M.D. PRIME-MD ® is a registered trademark of Pfizer Inc. Copyright  1999 Pfizer Inc.

PUSH: The Pressure Ulcer Scale for Healing (PUSH Tool v. 3.0) is reprinted with permission from the National Pressure Ulcer Advisory Panel (NPUAP). Copyright © 2003 NPUAP.

SF-8: Reproduced under License from QualityMetric, Inc. SF-8<sup>TM</sup> Health Survey © 1999, 2000 by QualityMetric Incorporated. All rights reserved. SF-8<sup>TM</sup> is a trademark of QualityMetric Incorporated. \*Item 2b is not part of the SF-8<sup>TM</sup> Health Survey.

SF-MPQ: Reproduced and reformatted with permission from Ronald Melzack, Ph.D. Copyright © 1987 Ronald Melzack.

SWLS: Reproduced with permission from Ed Diener, Ph.D. Copyright Ed Diener. Placed in public domain by Ed Diener.

# Appendix C: Instruments and Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Appendix C provides information about SCIDO instruments (Assessment Entry Forms) and two patient information forms.

> **NOTE:** All assessments that allow the user to edit or view history always displays the most recent assessment first in the History List

The following twenty instruments are described in this section:

The following two patient information forms are described in this section:

[Registration Ancillary Data Entry Form](#registration-ancillary-data-entry-form)

[Patient Education Form](#patient-education-form)

## American Spinal Injury Association (ASIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ASIA instrument is derived from the American Spinal Injury Association Standard Neurological Classification of Spinal Cord Injury. The ASIA uses the findings from the neurological examination to classify injury types into specific categories. These categories allow clinicians to identify and classify different injuries and degrees of spinal cord damage. The ASIA Spinal Cord Injury Classification approach is the internationally accepted standard for spinal cord injury classification and has been adopted by most major organizations associated with spinal cord injury. This has resulted in more consistent, worldwide terminology used to describe the findings in spinal cord injury.

Before completing an ASIA Classification, clinicians should have completed professional training regarding its use. ASIA has offered its Neurological Classification Teaching Package since 1994. Recently, the Neurological Standards Committee completed an extensive revision of the manual, and a new version is available.

The ASIA also provides a companion graphic that shows dermatomes. Dermatomes are characteristic areas of the body surface from which each nerve root receives sensory input. Each dermatome on the diagram corresponds to a neurological level on the ASIA form.

Refer to the Reference Manual for the International Standards for Neurological Classification of Spinal Cord Injury.

To launch the ASIA instrument, select the *ASIA* button in the Assessment Entry Forms area of the Impairments page.

For the ASIA instrument to be calculated and saved, the following fields, other than Record Date, Care Type, and Score Type, require values.

Neurological Level - four fields \[Sensory (R), Sensory (L), Motor (R), Motor (L)\] Complete/Incomplete (Extent of Injury – Incomplete = Presence of any sensory or motor function in lowest sacral segment)

ASIA Impairment Scale field.

> NOTE: However, if one or more of the Motor Key Muscle fields or Key Sensory Point fields have been completed, then completion of all these fields is required.  

> To enter data into any of the Motor Key Muscle fields or Key Sensory Point fields, complete all the remaining ASIA fields to submit the instrument

> **NOTE:** The care types of Inpatient Rehabilitation, Outpatient Rehabilitation, or Continuum of Care - Inpatient are used if there is an Episode of Care associated with the assessment. Refer to the Episode of Care section of this manual for further information.

Many outcome reports, benchmarks, and other SCIDO information are dependent on an accurate ASIA classification. Therefore, it is strongly recommended that ASIA information be entered before other information in an Episode of Care.

Within the SCIDO application, the ASIA appears as follows:

![](scido-version-3-user-manual/067.png)

#### ASIA Instrument Fields

#### Neurological Level

For the Neurological Level field, the valid responses are as follow:

C01 = Cervical 01 T08 = Thoracic 08

C02 = Cervical 02 T09 = Thoracic 09

C03 = Cervical 03 T10 = Thoracic 10

C04 = Cervical 04 T11 = Thoracic 11

C05 = Cervical 05 T12 = Thoracic 12

C06 = Cervical 06 L01 = Lumbar 01

C07 = Cervical 07 L02 = Lumbar 02

C08 = Cervical 08 L03 = Lumbar 03

T01 = Thoracic 01 L04 = Lumbar 04

T02 = Thoracic 02 L05 = Lumbar 05

T03 = Thoracic 03 S01 = Sacral 01

T04 = Thoracic 04 S02 = Sacral 02

T05 = Thoracic 05 S03 = Sacral 03

T06 = Thoracic 06 S04 = Sacral 04

T07 = Thoracic 07 S05 = Sacral 05

UNK = Unknown

#### Complete or Incomplete

Select Complete or Incomplete to denote any sensory or motor function detected in lowest sacral segment.

#### ASIA Impairment Scale

For the ASIA Impairment Scale, select one of the following options listed in the dropdown:

A = Complete: No sensory or motor function is preserved in the sacral segments S4–S5.

B = Incomplete: Sensory but not motor function is preserved below the neurological level and includes the sacral segments S4–S5.

C = Incomplete: Motor function is preserved below the neurological level, and more than half of key muscles below the neurological level have a muscle grade greater than or equal to 3.

D = Incomplete: Motor function is preserved below the neurological level, and at least half of key muscles below the neurological level have a muscle grade greater than or equal to 3.

E = Normal: Sensory and motor functions are normal.

UNK = Unknown.

After all mandatory information has been entered, select either the *Calculate* or *Submit* button. After selecting *Calculate*, the ASIA instrument calculates and provides the Neurological Level and ASIA Impairment score in the header of the instrument.

On the Impairments Tab in the ASIA Scores/Date (history) field, ASIA scores, record date, and score type are displayed for the most recent ASIA assessment. Select the ASIA Scores/Dates history dropdown to view a listing of the scores, record dates, and score types for all ASIA assessments. You can view (and edit) an individual ASIA assessment by selecting one of the assessment history lines<span id="_AUDIT_Instrument" class="anchor"></span>

*\[For scoring information, refer to the ASIA Scoring Algorithm or to the ASIA Manual.\]*

## Alcohol Use Disorders Identification Test (AUDIT) Instrument

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AUDIT instrument is derived from the World Health Organization’s Alcohol Use Disorders Identification Test and provides questions about a person’s alcohol use. The AUDIT was developed by the World Health Organization to identify persons whose alcohol consumption may become hazardous or harmful to their health. The AUDIT is a ten-item screening questionnaire with three questions on the amount and frequency of drinking, three questions on alcohol dependence, and four questions on problems caused by alcohol.

In most cases, a CAGE assessment is completed before the AUDIT. This allows a shorter screening process. Based on the CAGE score, the clinician may follow up with the AUDIT to gather more information about possible alcohol use and abuse. Refer to the [CAGE Instrument](#cage) section of this manual for more information.

The Alcohol Use Disorders Identification Test (AUDIT) assessment form may be accessed from the Assessment Entry Forms area of the Impairments tab.

Within the SCIDO application, the AUDIT appears as follows:

![](scido-version-3-user-manual/068.png)

Select the most appropriate answer from the dropdown for each question. For the AUDIT instrument to be calculated and saved, the following fields, other than the header fields, require values.

Questions 1 through 10 (If the answer to Question 1 is Never, the evaluator can skip to Questions 9 and 10).

> **NOTE:** The Care Types of Inpatient Rehabilitation, Outpatient Rehabilitation, or Continuum of Care - Inpatient are used if there is an Episode of Care associated with the assessment. Refer to the Episode of Care section of this manual for further information.

#### AUDIT Form Scoring

If the AUDIT Total Score is 8 or more, then the following is displayed:

“A score of 8 or more indicates a strong likelihood of hazardous or harmful alcohol consumption. Please consider referral to available resources for further evaluation or intervention. Brief intervention can work. Linking patients immediately to services can be successful.”

Refer to the Alcohol Use Disorders Identification Test Guidelines for Use in Primary Care manual.

The score, record date, and score type for the most recent AUDIT is displayed on the Impairments tab in the Score/Dates (history) field. To view a listing of all AUDIT assessments, select the history field dropdown. You can view (and edit) an individual AUDIT assessment by selecting one of the assessment history lines.

\[For scoring information, refer to the AUDIT Scoring Algorithm.\]

## Body Mass Index (BMI) Instrument

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Body Mass Index (BMI) instrument calculates a Body Mass Index as a measure of body fat based on height and weight that applies to both adult men and women.

The BMI instrument is accessible from the Impairments Tab and appears as follows:

![](scido-version-3-user-manual/069.png)

Care Type and Score Type are not required for the BMI instrument. For the BMI instrument to be calculated and saved, the following fields, besides Record Date, require values.

Care Type and Score Type are not required for non-EOC assessments. However, if a Care type is entered on for either EOC or non-EOC BMI assessments, a Score type is required.

Weight (Pounds or Kilograms)

Height (Inches or Centimeters)

To use the BMI instrument, complete the following steps:

1\. Enter the patient’s weight in the Weight field and choose either pounds or kilograms from the dropdown.

2\. Enter the patient’s height in the Height text field, and choose either inches or centimeters (cm.) from the dropdown.

3\. Select the *Calculate* button to calculate the patient’s BMI.

4\. The patient’s BMI is displayed in the Body Mass Index field.

5\. Select the *Submit* button to submit the Body Mass Index calculation.

6\. The application returns to the Impairments Tab.

On the Impairments Tab, the score, date, and score type are not required or optional because the most recent BMI are displayed in the Body Mass Index (BMI) History field. Select the dropdown to view a listing of the scores, record dates, and score types for all BMI assessments. You can view (and edit) an individual BMI assessment by selecting one of the BMI assessment history lines.

\[For scoring information, refer to the BMI Scoring Algorithm.\]

## CAGE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CAGE instrument is one of two instruments that may be used to screen for alcohol abuse The CAGE screening questionnaire is short and simple to administer. The CAGE instrument is most often the first instrument used to screen for alcohol abuse. Based on the CAGE score, the Clinician may then use the AUDIT instrument to gather more information about possible alcohol use and abuse.

To launch the CAGE instrument, select the *CAGE* button in the Assessment Entry Forms area of the Impairments page. The CAGE appears as follows:

![](scido-version-3-user-manual/070.png)

> **NOTE:** The Care Types of Inpatient Rehabilitation, Outpatient Rehabilitation, or Continuum of Care - Inpatient are used if there is an Episode of Care associated with the assessment. Refer to the Episode of Care section of this manual for further information.

For the CAGE instrument to be calculated and saved, all four questions must have responses. After all mandatory information has been entered, select either the *Calculate* or *Submit* button.

By selecting *Calculate*, the overall score is calculated and displayed in the header of the CAGE. By selecting *Submit*, if a patient’s score is one or greater, the following message appears describing further action to be taken:

![](scido-version-3-user-manual/071.png)

Select *OK* to return to the Impairments page. Select *AUDIT* to create an AUDIT assessment for the patient. Refer to the [Alcohol Use Disorders Identification Test (AUDIT) Instrument](#_AUDIT_Instrument) section of this manual for information on completing an AUDIT assessment.

On the Impairments Tab, the score, date, and score type for the most recent CAGE are displayed in the Scores/Dates (history) field. Select the dropdown to view a listing of the scores, record dates, and score types for all CAGE assessments. You can view (and edit) an individual CAGE assessment by selecting one of the assessment history lines.

\[For scoring information, refer to the CAGE Scoring Algorithm.\]

## Center for Epidemiologic Studies Depression Scale (CES-D)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Center for Epidemiologic Studies Depression Scale (CES-D) form is a short, self-reporting scale intended for measuring current depressive symptoms in the general population. It can be accessed from the Impairments Tab or from the PRIME-MD® information form.

It is suggested that the Clinician complete the CES-D form if there is one Yes reply on the PRIME-MD assessment form. It is strongly recommended that the Clinician complete the CES-D form if there are two Yes replies on the PRIME-MD assessment form.

The CES-D assessment form contains twenty statements describing how the patient might have felt, thought, or behaved during the past week. The form appears as follows:

![](scido-version-3-user-manual/072.png)

Enter the patient’s responses into the CES-D form by choosing one response from the following choices:

Rarely or None of the Time (Less than 1 Day)

Some or a Little of the Time (1-2 Days)

Occasionally or a Moderate Amount of Time (3-4 Days)

Most or All of the Time (5-7 Days)

To calculate and save the patient information in the CES-D form, all items must be complete.

On the Impairments Tab, the score, date, and score type for the most recent CES-D are displayed in the Scores/Dates (history) field. Select the dropdown to view a listing of the scores, record dates, and score types for all CES-D assessments. You can view (and edit) an individual CES-D assessment by selecting one of the assessment history lines.

## Craig Handicap Assessment and Reporting Technique Short Form (CHART-SF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Craig Handicap Assessment and Reporting Technique-Short Form (CHART-SF) was designed to provide a simple, objective measure of the degree to which impairments and disabilities result in limitations to participation in meaningful social roles. The CHART-SF has nineteen items that yield the same subscales as the original thirty-two item CHART.

The CHART-SF form has different types of response choices, such as Yes or No, number entry, text entry, and multiple-choice responses. The CHART-SF has six subscale (dimension) sections:

Physical Independence (physical activities, such as dressing, toileting, mobility)

Cognitive Independence (remembering, decision-making, judgment)

Mobility (typical activities)

Occupation (work, home, recreational activities)

Social Integration (family and friends; social associations)

Economic Self-sufficiency (financial resources, including earnings)

#### CHART-SF Submission Requirements

For the CHART-SF instrument to be calculated and saved, the following fields, along with the required Record Date, Care Type, and Score Type fields, require values.

Hours Paid Assistance

Hours Unpaid (Family, Others)

To submit the CHART-SF form, the two fields in the Physical Independence section described above must have responses. Within any one of the subscale sections, if any one of the fields within that section is completed, then all fields in that section are required to save the form.

The Craig Handicap Assessment and Reporting Technique Short Form (CHART-SF) assessment form may be accessed from the Participation and SWLS tab.

#### CHART-SF Scoring

CHART-SF items are grouped by subscales, also known as dimensions. A dimension score (instrument subscale score) can be calculated only when all items in that dimension have responses; other requirements may apply as well. If the response to questions 18 or 19 is either Don’t Know or Refused, the Economic Self-Sufficiency score cannot be calculated.

> **NOTE:** When the Unreimbursed medical expenses exceed the combined annual income for the economic self-sufficiency section, the Economic Self-Sufficiency Score will calculate a zero (0) score.

\[For scoring information, refer to the CHART-SF Scoring Algorithm.\]

#### CHART-SF Progress Notes

Progress notes may be written in the application depending on the score type and the care type. For more information about Progress notes, see section [Progress Notes](#progress-notes).

#### CHART-SF History

On the Participation & SWLS Tab, the total score, date, and score type for the most recent CHART-SF are displayed in the CHART-SF History field. Select the history dropdown to view a listing of the scores, record dates, and score types for all CHART-SF assessments. You can view (and edit) an individual CHART-SF assessment by selecting one of the assessment history lines.

The subscale scores for the CHART-SF are displayed in the CHART-SF Subscales section of the Participation & SWLS tabs.

In the application, the CHART-SF appears as follows:

![](scido-version-3-user-manual/073.png)

## Check Your Health (CYH) and Secondary Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Check Your Health (CYH) form is designed to help identify people who are at risk for secondary conditions. The Secondary Conditions Checklist is designed to highlight the most problematic secondary conditions. These conditions have been grouped into four basic areas: environmental obstacles, medical conditions, adjustment issues, and health and lifestyle issues. The user may select as many secondary conditions as apply.

The Check Your Health (CYH) form appears as follows:

![](scido-version-3-user-manual/074.png)

The top section is the Check Your Health (CYH) portion of the form, which has three questions. The lower section is the Secondary Conditions Checklist. These two related instruments have been combined into one form in this application.

For the CYH instrument to be calculated and saved, in addition to the Record Date, Care Type, and Score Type fields, questions 1, 2, and 3 require values.

The Check Your Health (CYH) and Secondary Conditions assessment form can be accessed from the Impairments page. On the Impairments Tab, the score, record date, and score type for the most recent CYH are displayed in the Scores/Dates (history field). Select the history dropdown to view a listing of the score(s), record dates, and score types for all CYH assessments. You can view (and edit) individual assessments by selecting one of the CYH assessment history lines.

#### Check Your Health Scoring

The following scores are calculated: the Overall Health score, Overall Independence score, Depression score, and the Total Score.

A graph showing the changes in the Check Your Health (CYH) total score over time is displayed on the Impairments Tab.

#### Secondary Conditions Checklist

The Secondary Conditions Checklist allows the selection of secondary conditions from each of four categories (environmental obstacles, medical conditions, adjustment issues, and health and lifestyle issues). Select as many secondary conditions as apply.

\[For scoring information, refer to the CYH Scoring Algorithm.\]

## Drug Abuse Screening Test (DAST)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the Drug Abuse Screening Test (DAST) is to provide a brief, simple, practical, but valid method for identifying individuals who are abusing drugs and to yield a quantitative index score of the degree of problems related to drug use and misuse. The DAST is able to discriminate drug-related problems from alcohol-related problems, indicating that the DAST is sensitive to problems resulting from drug use in particular and not to problems relating more generally to alcohol abuse.

The Drug Abuse Screening Test (DAST) assessment form can be accessed from the Impairments Tab. The DAST form appears as follows:

![](scido-version-3-user-manual/075.png)

Patient’s responses to the DAST instrument questions may be entered into the form by selecting either *Yes* or *No* for each question. The assessment time frame covers the past 12 months. All questions require responses for the DAST instrument to be calculated and saved.

On the Impairments Tab, the score, record date, and score type for the most recent DAST are displayed in a history field. Select the history dropdown to view a listing of the score(s), record dates, and score types for all DAST assessments. You can view (and edit) individual DAST assessments by selecting one of the assessment history lines.

## Duke Severity of Illness (DUSOI) Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Duke Severity of Illness Checklist (DUSOI) is a generic assessment of the morbidity experienced by a patient. The most serious illness weights the score most heavily, but co-morbidity is included. The DUSOI is computed based on the three most serious conditions, but as many conditions as the clinician desires may be entered. The DUSOI Assessment form appears as follows:

![](scido-version-3-user-manual/076.png)

The left side of the form contains the individual diagnosis or health problem section. The Related Diagnoses section on the right side displays the related diagnoses associated with this cluster of diagnoses. The DUSOI Related Diagnoses list displays the associated DUSOI Health Problem, with ICD, Health Problem or diagnosis, score, and record date, which will be shown in order with the highest Score first.

1.  Refer to the section “[Sample of Completed DUSOI Assessment](\l)” for an example.

Clinicians use the term “clustering” for the grouping of DUSOI health or diagnosis forms.

The following is a summary of steps used to create a DUSOI assessment cluster:

1\. Select the ICD for the Diagnosis or Health Problem field. Refer to the “Diagnosis or Health Problem Field” section for details.

2\. Select responses for the Symptoms, Complications, and Prognosis fields.

3\. In the Treatability/Need for Treatment field, either select the *Questionable*, *No*, or *Yes* button

4\. If the Treatability/Need for Treatment field is *Yes*, select a value for the Expected Response to Treatment field.

5\. Select the *Calculate* button to view the score for the individual diagnosis or health problem.

> **NOTE:** The calculated Overall DUSOI score for associated DUSOI forms displays in the Score field in the header of the DUSOI form.

6\. If all diagnoses have been added, select the *Submit* button to save the DUSOI assessment.

7\. If there are more diagnoses to be added to this cluster, select the *Add more Diagnoses* button. A summary of the individual health diagnosis or problem is displayed in the Related Diagnoses section. The left side of the form is blank for entry of a new ICD. Repeat this process from step 1.

#### Button Functions within DUSOI

The following is a general overview of special functionality on the DUSOI assessment.

The *Add More Diagnoses* function is used to create a new associated DUSOI form. This function saves the individual DUSOI assessment temporarily and displays a listing of this diagnosis with its individual score on the right side of the page. The values in the individual DUSOI assessment fields on the left side are removed, and a new diagnosis can be added.

> **NOTE:** The assessments are not saved until the *Submit* button is selected. If individual diagnoses have been added to a cluster, even though a listing of each diagnosis appears on the right, if they have not been submitted, these diagnoses will be deleted if the *Cancel* button is used.

The *Submit* function is used to end the process of creating associated DUSOI forms. This function causes the overall DUSOI score to be calculated and the forms to be submitted.

#### Diagnosis or Health Problem Field

Diagnoses codes can be selected from the International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) codes, including V codes. Select the *ICD Search* button, and the SCI ICD Search window is displayed.

![](scido-version-3-user-manual/077.png)

Enter part of the diagnosis or ICD code in the Search text field. Select the *Submit* button, and the system returns a list of matching ICD codes, along with the short name and long name for the diagnosis or health problem. The ICD Code search utilizes a Remote Procedure Call (RPC) to VistA for ICD lookups.

![](scido-version-3-user-manual/078.png)

From the list of matching diagnoses, select the desired diagnosis. The selected code and short diagnosis name are displayed in the Diagnosis or Health Problem field on the DUSOI form.

You can add as many DUSOI individual diagnoses as are needed to capture all the patient’s diagnoses or health problems.

#### DUSOI Scoring

Calculate the value of responses to obtain both the Diagnosis or Health Problem Score and the Overall DUSOI Score for all diagnoses or problems. A Diagnosis or Health Problem Score is computed and displayed on each individual DUSOI form. The DUSOI Overall Score for all associated diagnoses or problems is computed using the three highest Diagnosis or Health Problem scores of associated DUSOI forms.

\[For scoring information, refer to the DUSOI Scoring Algorithm.\]

#### Associated DUSOI Forms 

DUSOI Forms that are entered from an open DUSOI form using the *Add More Diagnoses* function will be associated with each other. When editing an archived DUSOI assessment, using the *Add More Diagnoses* function will cause new DUSOI forms to be associated with the current group of DUSOI forms. When editing a DUSOI assessment, the user will not be able to modify the record date.

#### History of Completed DUSOI Forms 

On the Impairments Tab, the most recent DUSOI Overall score, record date, and score type is displayed in a history field next to the *DUSOI* button. Select the history dropdown to view a listing of the overall scores, record dates, and score types for all DUSOI assessments. You can view (and edit) DUSOI assessments by selecting one of the assessment history lines.

#### Sample of Completed DUSOI Assessment

The following example of a completed DUSOI shown below demonstrates the Related Diagnoses section on the right side, with the information for the diagnosis of 826.0 displayed and editable on the left side. The diagnosis of 826.0 has an individual score of 50.

![](scido-version-3-user-manual/079.png)

## Duke Severity of Illness Analog (DUSOI-A) Scale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Duke Severity of Illness Analog Scale (DUSOI-A) is a single-item generic assessment of the overall morbidity experienced by a patient based on the clinician’s judgment. The patient’s overall severity of illness during the past week is rated by the clinician by assigning a score from zero through one hundred or by moving a slider along an analog scale. The lowest severity applies to someone whose total set of diagnoses or health conditions results in the fewest symptoms and complications, the least disability and threat to life, the least need for treatment, and the best expected response to treatment if needed. Conversely, the highest severity applies to someone whose total set of diagnoses results in the most symptoms and complications, the most disability and greatest threat to life, the most need for treatment, and the worst expected response to treatment if needed.

The DUSOI-A Assessment form appears as follows:

![](scido-version-3-user-manual/080.png)

For the DUSOI-A instrument to be calculated and saved, the following fields, along with the Record Date, Care Type, and Score Type fields, require values:

Instrument Slider or the field “If unable to use the slider control”

“How confident are you that your rating of this patient’s severity of illness is accurate”

The Duke Severity of Illness Analog (DUSOI-A) Scale assessment form can be accessed from the Impairments tab. On the Impairments Tab, the score, record date, and score type for the most recent DUSOI-A are displayed in a history field next to the *DUSOI-A* button. Select the history dropdown to view a listing of the scores, record dates, and score types for all assessments. You can view (and edit) individual assessments by selecting one of the DUSOI-A assessment history lines.

\[For scoring information, refer to the DUSOI-A Scoring Algorithm.\]

## Functional Assessment Measure (FAM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Assessment Measure (FAM) was developed as an activity measure and as an adjunct to the Functional Independence Measure (FIM) to specifically address the major functional areas that are relatively less emphasized in the FIM, including cognitive, behavioral, communication and community functioning measures. The FAM consists of 12 items, which were developed by clinicians representing each of the disciplines in an inpatient rehabilitation program. The Functional Assessment Measure (FAM) assessment form can be accessed from the Activities tab.

The Functional Assessment Measure (FAM) Assessment form appears as follows:

![](scido-version-3-user-manual/081.png)

Values may be selected for any of the twelve items from the corresponding dropdown. An item may be left blank, which indicates it is either “not applicable”, “untested”, or “unknown”. For the FAM instrument to be calculated and saved, at least one item requires a response.

This assessment does not have a total score, only a score or rating for each individual activity measure. The most recently completed FAM assessment score(s) and record date are included and displayed on the Activities page. The displayed scores are the ratings for each available individual activity measure, (e.g., Swallowing 7, Car Transfers 5).

On the Activities Tab, the score(s), record date, and score type for the most recent FAM are displayed in a history field next to the *FAM* button. Select the history dropdown to view a listing of the scores, record dates, and score types for all FAM assessments. You can view (and edit) a FAM assessment by selecting one of the assessment history lines.

\[For scoring information, refer to the FAM Scoring Algorithm.\]

## Functional Independence Measure (FIM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Independence Measure (Guide for the Uniform Data Set for Medical Rehabilitation, 1996) is the most widely used activity or functional assessment measure in the rehabilitation community. The FIM is an 18-item ordinal scale, used with all diagnoses within a rehabilitation population. The FIM should be completed by appropriately trained professional staff.

The Functional Independence Measure (FIM) Assessment form appears as follows:

![](scido-version-3-user-manual/082.png)

It is required that all fields in the right side column and three fields (Military Status, Admission Class, and Impairment Group) in the left column of the FIM Online form be completed prior to submitting the form.

The user is not required to complete the *Check if program is interrupted* box, the Transfer Date fields, or the Return Date fields. These fields are used only for FIMs with a score type of Finish.

The fields on the right side of the form require a rating from 1 to 7 based on the following scale:

Complete Independence 7

Modified Independence 6

Supervision or Setup 5

Minimal Contact Assistance 4

Moderate Assistance 3

Maximal Assistance 2

Total Assistance 1

A FIM Polar graph is created and saved when the form is calculated or submitted.

For Inpatient Rehabilitation Care Types with a score type of Start, Function Related Group (FRG) classes are calculated in the background and saved to the SCIDO regional database for research purposes. The instrument form does not display any FRG scores when the FRG scores are calculated.

The FIM assessment form can be accessed from the Activities tab. On the Activities Tab, the scores, record dates, and score types for the most recent FIM assessment are displayed in history fields. Select the FIM Total, FIM, Motor, or FIM Cognitive history dropdown to view a listing of the score(s), record dates, and score types for all assessments. You can view (and edit) individual assessments by selecting one of the assessment history lines on the FIM Total Score history list.

\[For scoring information, refer to the FIM Scoring Algorithm.\]

## Kurtzke Expanded Disability Status Scale (EDSS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kurtzke Expanded Disability Status Scale (EDSS) is one instrument that has been commonly used in outcome assessment of individuals with multiple sclerosis. The EDSS is an ordinal scale with some rater variability that has an emphasis on mobility status. It may be relatively insensitive to change at certain levels of disability or activity restrictions.

The EDSS is a single-item generic assessment of the overall activity restrictions experienced by a patient based on the clinician’s judgment. The patient’s functioning is rated from zero for a normal neurological examination to ten for death due to multiple sclerosis. Levels five through ten reflect some degree of ambulation restriction or disability. It is recommended that the Kurtzke Functional Systems Scale (FSS) be completed before the EDSS since it is associated with neurological testing of eight functional systems, pyramidal, cerebellar, brain stem, sensory, bowel and bladder, visual or optic, mental or cerebral, and other functions. These FSS ratings are then used in conjunction with observations and information concerning gait and use of assistive devices to rate the EDSS. The EDSS form appears as follows:

![](scido-version-3-user-manual/083.png)

For the Kurtzke EDSS instrument to be calculated and saved, a response must be selected for the “Enter EDSS Scale value” field. The Kurtzke Expanded Disability Status Scale (EDSS) assessment form may be accessed from the Activities tab if the patient has an etiology of multiple sclerosis. On the Activities Tab, the most recent EDSS score, record date, and score type is displayed in a history field. Select the history dropdown to view a listing of the score, record dates, and score types for all assessments. You can view (and edit) individual assessments by selecting one of the assessment history lines.

\[For scoring information, refer to the Kurtzke EDSS Scoring Algorithm.\]

## Kurtzke Functional Systems Scale (FSS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kurtzke Functional Systems Scale (FSS) constitutes one of the most widely used assessment instruments in Multiple Sclerosis. Based on a standard neurological examination, the seven functional systems plus "other" are rated. Each of the FSS is an [ordinal](http://www.nationalmssociety.org/MUCS_glossary2.asp#ordinalscale) clinical rating scale ranging from zero to five or six. It is recommended that the Kurtzke Functional Systems Scale (FSS) be completed before the EDSS since it is associated with neurological testing of eight functional systems, pyramidal, cerebellar, brain stem, sensory, bowel and bladder, visual or optic, mental or cerebral, and other functions.

The FSS Assessment form appears as follows:

![](scido-version-3-user-manual/084.png)

The two check boxes and text-entry box for “Specify Function” are not required for the Kurtzke FSS instrument to be calculated and saved. The following fields require values:

Pyramidal Functions

Cerebellar Functions

Brain Stem Functions

Sensory Functions

Bowel and Bladder Functions

Visual or Optic Functions

Mental or Cerebral Functions

Other Functions

The Kurtzke Functional Systems Scale (FSS) assessment form can be accessed from the Activities tab if the patient has an etiology of multiple sclerosis.

On the Activities Tab, the most recent FSS score(s), record date, and score type are displayed in a history field. Select the history dropdown to view a listing of all assessments. You can view (and edit) an individual assessment by selecting one of the assessment history lines.

*\[For scoring information, refer to the Kurtzke FSS Scoring Algorithm.\]*

## Medical Needs Function Modifiers (MNFM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medical Needs and Function Modifiers (MNFM) form contains four items from the Inpatient Rehabilitation Facility – Patient Assessment Instrument (IRF-PAI) form pertaining to swallowing status, clinical signs of dehydration, bladder frequency ratings of accidents in the past seven days, and bowel frequency ratings of accidents in the past seven days. The IRF-PAI is a common instrument used to assess patients in inpatient rehabilitation facilities to establish case complexities and progress during rehabilitation.

The MNFM form appears as follows:

![](scido-version-3-user-manual/085.png)

For the MNFM instrument to be calculated and saved, at least one field must be completed, along with the Record Date, Care Type, and Score Type fields.

The Medical Needs Function Modifier (MNFM) assessment form can be accessed from the Activities tab. The most recent Bowel Accident Frequency rating and Bladder Accident Frequency rating is displayed on the Activities Tab. There is no total score for the MNFM form. To view a listing of all MNFM assessments, select the history field of either the Bowel Accident Frequency or the Bladder Accident Frequency fields on the Activities tab. You can view (and edit) an individual MNFM assessment by selecting one of the assessment history lines.

If responses were selected for the Swallowing Status and Dehydration fields on the MNFM, these values are displayed on the Impairments tab.

\[For scoring information, refer to the MNFM Scoring Algorithm.\]

## PRIME-MD® Depression Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary Care Evaluation of Mental Disorders (PRIME-MD) Depression Screening consists of two items to be used as a case-finding depression instrument. The two-question case-finding instrument is a useful measure for detecting depression in primary care. It has similar test characteristics to other case-finding instruments and is less time-consuming. One "Yes" reply is considered a positive screening for depression; further screening for depression is suggested. If there are two "Yes" replies, complete the Center for Epidemiologic Studies Depression Scale (CES-D) form.

The PRIME-MD form appears as follows:

![](scido-version-3-user-manual/086.png)

For the PRIME-MD instrument to be calculated and saved, both questions must be completed along with the Record Date, Care Type, and Score Type fields.

The PRIME-MD Depression Screening assessment form can be accessed from the Impairments tab. On the Impairments tab, the most recent PRIME-MD score(s), record date, and score type are displayed in a history field. Select the history dropdown to view a listing of all assessments. You can view (and edit) an individual PRIME-MD assessment by selecting one of the assessment history lines.

\[For scoring information, refer to the PRIME-MD Scoring Algorithm.\]

## Pressure Ulcer Scale for Healing (PUSH)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pressure Ulcer Scale for Healing (PUSH) was developed by the National Pressure Ulcer Advisory Panel (NPUAP) as a quick, reliable tool to monitor the change in pressure ulcer status over time. To use the PUSH Tool, the pressure ulcer is assessed and scored on four elements: length of the open wound, width of the open would, exudate amount, and tissue type. Record the highest current pressure ulcer stage and number of current pressure ulcers on the form. Estimate the amount of exudate after removal of the dressing and before applying any topical agents. Identify the type of tissue. If there is any necrotic tissue, it is scored as 4. If there is any slough, it is scored as 3, even if most of the wound is covered with granulation tissue.

It can be a clinically practical, evidence-based tool for tracking changes in pressure ulcer status when applied at weekly intervals.

The PUSH form appears as follows:

![](scido-version-3-user-manual/087.png)

For the PUSH instrument to be calculated and saved, all fields must be completed, along with the Record Date, Care Type, and Score Type fields. The length and width field entries are limited to two post decimal places (i.e. 2.53).

The Pressure Ulcer Scale for Healing (PUSH) assessment form can be accessed from the Medical Complications tab.

On the Medical Complications Tab, the most recent PUSH score, record date, and score type are displayed in a history field. Select the history dropdown to view a listing of the scores, record dates, and score types for all PUSH assessments. You can view (and edit) an individual assessment by selecting one of the PUSH assessment history lines.

\[For scoring information, refer to the PUSH Scoring Algorithm.\]

## Satisfaction with Life Scale (SWLS) (Diener’s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Satisfaction with Life Scale (SWLS) is a global measure of life satisfaction developed by Diener, Emmons, Larsen & Griffin, 1985. Life satisfaction is distinguished from affective appraisal in that it is more cognitively than emotionally driven. The SWLS consists of 5-items that are completed by the individual whose life satisfaction is being measured.

The SWLS form appears as follows:

![](scido-version-3-user-manual/088.png)

For the SWLS instrument to be calculated and saved, all fields require a response.

On the Participation & SWLS Tab, the total score, date, and score type for the most recent SWLS are displayed in the SWLS History field. Select the history dropdown to view a listing of the scores, record dates, and score types for all SWLS assessments. You can view (and edit) an individual SWLS assessment by selecting one of the assessment history lines.

\[For scoring information, refer to the SWLS Scoring Algorithm.\]

## SF-8 Health Survey

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SF-8 Health Survey (SF-8) is a generic multipurpose short form (SF) survey of health status. It contains eight questionnaire items plus one item (2b) that has been revised for people who cannot walk or climb stairs. The survey seeks the patient’s observations regarding their health during the past four weeks.

The SF-8 is reproduced under License from QualityMetric, Inc. SF-8 ™ Health Survey © 1999, 2000 by QualityMetric Incorporated. All rights reserved. SF-8 ™ is a trademark of QualityMetric Incorporated. \*Item 2b is <u>not</u> part of the SF-8 ™ Health Survey.

The SF-8 Health Survey form appears as follows:

![](scido-version-3-user-manual/089.png)

For the SF-8 instrument to be calculated and saved, all fields require responses. After completion of the mandatory SF-8 information, select either Calculate or Submit.

By selecting *Calculate*, the SF-8 instrument displays graphs of the eight scale scores and two component scores. On the SF-8 Scale Scores graph page, after the *Back* button is selected, the SF-8 instrument refreshes and provides the component scores in the header of the instrument.

The SF-8 Health Survey assessment form can be accessed from the Impairments tab. On the Impairments tab, the most recent SF-8 scores, record date, and score type are displayed in a history field. Select the history dropdown to view a listing of all assessments. You can view (and edit) an individual SF-8 assessment by selecting one of the assessment history lines.

Two composite scores are calculated:

Physical Component Summary (PCS8)

Mental Component Summary (MCS8)

Eight subscales are calculated:

PF - Physical Functioning

RP - Role Physical

BP - Bodily Pain

GH - General Health

VT - Vitality

SF - Social Functioning

RE - Role Emotional

MH - Mental Health

\[For scoring information, refer to the SF-8 Scoring Algorithm.\]

## Short Form McGill Pain Questionnaire (SF-MPQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Short Form McGill Pain Questionnaire (SF-MPQ) measures a patient’s subjective pain experience by using two dimensions of pain, sensory pain rating index (S-PRI) and affective pain rating index (A-PRI), and a total pain rating index (T-PRI). The objective of the MPQ is to facilitate the communication regarding pain between patients and health care professionals. The patient is also provided the opportunity to rate their present pain intensity index (PPI) and use a visual analogue scale to rate their pain from zero (lowest severity) to one-hundred (highest severity). The SF-MPQ form appears as follows:

![](scido-version-3-user-manual/090.png)

For the SF-MPQ instrument to be calculated and saved, all fields require responses.

The Short Form McGill Pain Questionnaire (SF-MPQ) assessment form can be accessed from the Medical Complications tab. On the Medical Complications tab, the most recent SF-MPQ scores, record date, and score type are displayed in a history field. Select the history dropdown to view a listing of all SF-MPQ assessments. You can view (and edit) an individual SF-MPQ assessment by selecting one of the assessment history lines.

## Registration Ancillary Data Entry Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Ancillary Data Entry Form may be accessed from the Registration page. Ancillary data consists of sources of care, referral sources, bowel care information, and remarks.

![](scido-version-3-user-manual/091.png)

For the Ancillary Date Entry form to be submitted and saved, at least one field must be completed.

#### Additional Care VAMC

To fill in the Additional Care VAMC field, select the site where additional VAMC care is provided.

#### Non-VA Care

The Non-VA Care field is text entry. To fill in the field, type in the site where non-VA care is provided.

#### Referral Source

The Referral Source field shows the type of facility that referred the patient to the VA. Select from the following.

VA = Other VA

CH = Community Hospital

NH = Nursing Home

PV = PVA

SF = Self

DD = Dept of Defense

NN = Non-VA Care

UN = Unknown or Other

#### Referral VA

The Referral VA field can be selected from the dropdown list.

#### Initial Rehabilitation Site

To indicate the patient’s Initial Rehabilitation Site, select from the dropdown one of the following values:

CH = Community Hospital

VS = VAMC with SCI Center

VN = VAMC without SCI Center

UN = Unknown or Other

#### Initial Rehabilitation Discharge Date

The Initial Rehabilitation Discharge Date is a date field for recording when the rehabilitation discharge occurred. The date can be manually entered or selected by selecting the Calendar icon to designate the date when the patient was discharged from rehabilitation.

#### Bowel Care Reimbursement (BCR)

To indicate whether the patient is being reimbursed for their bowel care, select either the *Yes* or *No*.

#### BCR Certified

The BCR Certified field is a date field for recording if the patient has been certified for bowel care. The date can be manually entered or selected by selecting the Calendar icon to designate the date when the patient received certification for bowel care.

#### BCR Provider

The BCR Provider field is text entry. Enter the patient’s bowel care provider.

#### Remarks

The Remarks field is text entry. To complete the field, type in any remarks (limited to 65 characters) to enhance care or outcomes.

## Patient Education Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Education form is used to record the dates the patient was given educational materials or training on sixteen health-related topics. The Patient Education form is accessible from the Registration tab.

![](scido-version-3-user-manual/092.png)

Once a patient has received educational material on one of the sixteen subjects, select the *Yes* button and enter the date that the information was given in the date box. Manually enter the date or select the date from the calendar icon. If the patient was offered the educational material but declined, select the *No* button and enter the date the material was offered.

To submit and save the form, at least one selection with an associated date must be completed.

# Appendix D: Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports are described in this section:

All the reports can be accessed from the Reports tab. Some of the reports can be accessed from another Tab. For example, the first seven reports listed above can be accessed from the Medical Complications tab as well as the Reports Tab.

## Influenza Diagnoses and Treatment Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Influenza Diagnoses and Treatment Report displays VistA information about influenza-related diagnoses, antiviral medications prescribed, influenza-related microbiology and chemistry laboratory reports, chest radiology results, and discharge locations following inpatient treatment of influenza incidents.

The Influenza Diagnoses and Treatment Report may be accessed from the Medical Complications tab as well as from the Reports tab.

| ![](scido-version-3-user-manual/093.png) |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|

## Influenza Immunizations Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Influenza Immunizations Report displays VistA information about influenza vaccination medications ordered for the patient, and influenza vaccination diagnoses and procedure codes recorded. This report cannot be used to document performance measure conformance due to various methods of recording doses.

The Influenza Immunizations Report may be accessed from the Medical Complications tab as well as from the Reports tab.

| ![](scido-version-3-user-manual/094.png)               |
|-------------------------------------------------------------------------------------------------------------------------------------------|
| ![](scido-version-3-user-manual/095.png) |

![](scido-version-3-user-manual/096.png)

## Pain Assessment and Treatment Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pain Assessment and Treatment Report displays SF-MPQ and PPI scores, pain alleviation drugs, pain management diagnoses and procedures, and Transcutaneous Electrical Nerve Stimulation (TENS) trial dates.

The Pain Assessment and Treatment Report may be accessed from the Medical Complications tab as well as from the Reports tab.

| ![](scido-version-3-user-manual/097.png) |
|-------------------------------------------------------------------------------------------------------------------------------------------------|

## Pneumonia and Respiratory Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pneumonia and Respiratory Report displays VistA information about increased aspiration risks due to swallowing difficulties or feeding tubes, pneumonia or atelectasis diagnoses, intubation procedures, chest radiology results, sputum laboratory results, and discharge locations following inpatient treatment of pneumonias.

The Pneumonia and Respiratory Report may be accessed from the Medical Complications tab as well as from the Reports tab.

![](scido-version-3-user-manual/098.png)

## Pneumococcal Immunizations Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pneumococcal Immunizations Report displays VistA information about pneumococcal vaccination medications ordered for the patient, and pneumococcal vaccination diagnoses and procedure codes recorded. This report cannot be used to document performance measure conformance due to various methods of recording doses.

The Pneumococcal Immunizations Report may be accessed from the Medical Complications tab as well as from the Reports tab.

![](scido-version-3-user-manual/099.png)

## Pressure Ulcer Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pressure Ulcer Treatment Report displays SCIDO information entered on the Medical Complications Tab and PUSH assessments and also displays VistA information about pharmacy supplies and prosthetic devices, diagnoses, surgeries, complications, radiological studies, and laboratory results related to pressure ulcers.

The Pressure Ulcer Treatment Report may be accessed from the Medical Complications tab as well as from the Reports tab.

The Treatment Completion Information field is populated from Pressure Ulcer Finish data entered on the Medical Complications Tab. The Pressure Ulcer Risk field is populated from Risk data entered on the Medical Complications Tab.

| ![](scido-version-3-user-manual/100.png) |
|----------------------------------------------------------------------------------------------------------------------------------|

## Urinary Tract Infections Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Urinary Tract Infections Report displays VistA information about urinary tract diagnoses, surgical procedures, radiological studies of the urinary tract, and urinalysis, microbiology, and CBC laboratory results related to urinary tract infections.

The Urinary Tract Infections Report may be accessed from the Medical Complications tab as well as from the Reports tab.

| ![](scido-version-3-user-manual/101.png) |
|---------------------------------------------------------------------------------------------------------------------------------------------|

## RAI-MDS Quality Indicators Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RAI-MDS Quality Indicators Report provides information for a specific patient on twenty-four quality indicators derived from the RAI-MDS. The default date for this report is the previous month. The user can also select a different month from the dropdown for a report. Information regarding these twenty-four quality indicators is displayed if the patient is in a JCAHO Long-Term Care Setting in the VA. Even though information may not be available for the specific patient, summary information regarding these twenty-four quality indicators at both the regional and national levels will be provided.

![](scido-version-3-user-manual/102.png)

## RAI-MDS Resource Utilization Groups (RUGS) Report" 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RAI-MDS Resource Utilization Groups (RUG) Report provides information about resource utilization groups, assessment activities of daily living, and RUG case mix index weights for all Veterans at the SCI regional level for Veterans with SCI in JCAHO Long-Term Care Settings in the VA.

![](scido-version-3-user-manual/103.png)

## Cumulative Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cumulative Reports produce statistical reports of Outcomes information across diagnostic categories. A definition of each row displayed in the reports is provided in this section for four reports:

Inpatient Rehabilitation Outcomes displays demographics, length of stay, a variety of inpatient rehabilitation effectiveness and efficiency indices, and benchmarks from the MSCIS for some of these indices. This report may be useful in summarizing inpatient rehabilitation outcomes for interested stakeholders, patients, and accreditation organizations. A user-selected date range of care close dates reflects Inpatient Rehabilitation Episodes of Care for inclusion in this report.

Outpatient Rehabilitation Outcomes displays demographics, FIM and SWLS Change, FIM Goal Attainment, and FIM and SWLS durability for Outpatient Rehabilitation Episodes of Care having care close dates within a user-selected date range.

Continuum of Care Inpatient Outcomes Report displays a summary of demographics, length of stay, FIM and SWLS Change, FIM Efficiency, FIM goal attainment, and FIM and SWLS durability for patients within a selected range of assessment close dates for continuum of care inpatient care type.

Annual Evaluation Outcomes Report displays a summary of demographics, FIM, CHART-SF, and Diener’s SWLS assessments that have been provided within a selected date range.

The report topics are broken down by the following diagnostic categories:

Diagnostic Categories

Hi-Tetra Neurological Level is C1-C4 and ASIA Impairment = A, B, or C

Lo-Tetra Neurological Level is C5-C8 and ASIA Impairment = A, B, or C

Paraplegia Neurological Level is T1-S5 and ASIA Impairment = A, B, or C

ASIA D Any Neurological Level and ASIA Impairment = D

ALL All Neurological Levels and all ASIA Impairment values (except Unknown)

#### Inpatient Rehabilitation Outcomes Report Topics Descriptions 

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Inpatient Rehabilitation Outcomes Report Topics</strong></th>
</tr>
<tr class="odd">
<th><strong>Report Topic</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td># and % of Patients</td>
<td><p>Number of patient datasets in the diagnostic category and Percentage of datasets in all diagnostic categories that number represents.</p>
<p>% is the number of diagnostic datasets divided by number of all datasets.</p></td>
</tr>
<tr class="even">
<td>Age (yrs)</td>
<td><p>Calculate age of individual patient for each dataset in diagnostic category.</p>
<p>Calculate Average patient age for each diagnostic category</p></td>
</tr>
<tr class="odd">
<td>Age Range</td>
<td>Range of ages in datasets, from the age of the youngest person to the age of the oldest person for each diagnostic category.</td>
</tr>
<tr class="even">
<td>Gender (% Male pts)</td>
<td>Percentage of males in diagnostic category.</td>
</tr>
<tr class="odd">
<td>Length of Rehab (days)</td>
<td><p>To use a dataset, Care Close Date and Care Start Date must have non-null values. If Return Date and Transfer Date are null, then the length of interruption is 0 days.</p>
<p>First calculate the individual patient’s length of rehab for each dataset:</p>
<p>(Care Close Date - Care Start Date - Interruption in Care Length 1 - Interruption in Care Length 2 - Interruption in Care Length 3)</p>
<p>Then using the individual values for dataset’s length of rehabilitation, calculate the average length of rehabilitation for each diagnostic category.</p>
<p>Interruption in Care Length = Return Date - Transfer Date</p></td>
</tr>
<tr class="even">
<td>Length of Rehab Range</td>
<td>Range of length of rehabilitation from the fewest number of days to the most number of days within datasets used for each diagnostic category.</td>
</tr>
<tr class="odd">
<td>Total FIM Change</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Start; FIM total score for each assessment must have a non-null value.</p>
<p>First calculate each individual’s FIM Change for each dataset:</p>
<p>Total FIM Change = FIM Total score at Finish - FIM Total score at Start</p>
<p>Then calculate the Average value of FIM Change for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>MSCIS Total FIM Change</td>
<td><p>Constant values populated by system. Display only:</p>
<p>Hi Tetra 12.4</p>
<p>Lo Tetra 27.8</p>
<p>Para 41.5</p>
<p>ASIA D 41.2</p>
<p>ALL 35.9</p></td>
</tr>
<tr class="odd">
<td>FIM Efficiency</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Start; FIM total score for each assessment must have a non-null value; the system must be able to calculate the length of rehabilitation.</p>
<p>First calculate individual’s FIM Efficiency for each dataset within each diagnostic category:</p>
<p>FIM Efficiency = Total FIM Change / Length of Rehabilitation</p>
<p>Then calculate the Average FIM Efficiency value for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>MSCIS FIM Efficiency</td>
<td><p>Constant values populated by system. Display only:</p>
<p>Hi Tetra 0.13</p>
<p>Lo Tetra 0.28</p>
<p>Para 0.76</p>
<p>ASIA D 0.84</p>
<p>ALL 0.55</p></td>
</tr>
<tr class="odd">
<td>FIM Goal Attainment</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Goal; FIM total score for each assessment must have a non-null value.</p>
<p>First calculate the individual values for FIM Goal attainment for each dataset in the diagnostic category:</p>
<p>FIM Total at Finish - FIM Total at Goal</p>
<p>Then calculate the Average value for FIM Goal attainment for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>FIM Durability</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Follow-up and a FIM assessment of score type Finish; the FIM total score for each assessment must have a non-null value.</p>
<p>First calculate individual values for FIM Durability for each dataset within each diagnostic category:</p>
<p>FIM Durability =FIM Total at Follow-up - FIM Total at Finish</p>
<p>Calculate the Average FIM Durability for each diagnostic category.</p></td>
</tr>
<tr class="odd">
<td>Diener SWLS Change</td>
<td><p>To use a dataset, it must have a Diener’s SWLS assessment of score type Start and a Diener’s SWLS assessment of score type Finish; the Diener’s SWLS score for each assessment must have a non-null value.</p>
<p>Calculate individual values for Diener’s SWLS Change for each dataset within each diagnostic category:</p>
<p>Diener’s SWLS Change = Score at Finish - Diener’s SWLS Score at Start</p>
<p>Calculate the Average value of Diener’s SWLS Change for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>Diener SWLS Durability</td>
<td><p>To use a dataset, it must have a Diener’s SWLS assessment of score type Follow-up and a Diener’s SWLS assessment of score type Finish; Diener’s SWLS score for each assessment must have a non-null value.</p>
<p>Calculate individual values for Diener’s SWLS Durability for each dataset within each diagnostic category:</p>
<p>SWLS Durability = Diener’s SWLS at Follow-up - Diener’s SWLS at Finish.</p>
<p>Calculate the Average value of Diener’s SWLS Durability for each diagnostic category.</p></td>
</tr>
</tbody>
</table>

#### Outpatient Rehabilitation Outcomes Report Topics Descriptions 

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Report Topic</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td># and % of Patients</td>
<td><p>Number of patient datasets in the diagnostic category and Percentage of datasets in all diagnostic categories that number represents.</p>
<p>% is the number of diagnostic datasets divided by number of all datasets.</p></td>
</tr>
<tr class="even">
<td>Age (yrs)</td>
<td><p>Calculate of individual patient for each dataset in diagnostic category.</p>
<p>Calculate Average patient age for each diagnostic category.</p></td>
</tr>
<tr class="odd">
<td>Age Range</td>
<td>Range of ages in datasets, from the age of the youngest person to the age of the oldest person for each diagnostic category.</td>
</tr>
<tr class="even">
<td>Gender (% Male pts)</td>
<td>Percentage of males in diagnostic category.</td>
</tr>
<tr class="odd">
<td>Total FIM Change</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Start; FIM total score for each assessment must have a non-null value.</p>
<p>First calculate each individual’s FIM Change for each dataset:</p>
<p>Total FIM Change = FIM Total score at Finish - FIM Total score at Start</p>
<p>Then calculate the Average value of FIM Change for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>FIM Goal Attainment</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Goal; FIM total score for each assessment must have a non-null value.</p>
<p>First calculate the individual values for FIM Goal attainment for each dataset in the diagnostic category: FIM Total at Finish - FIM Total at Goal</p>
<p>Then calculate the Average value for FIM Goal attainment for each diagnostic category.</p></td>
</tr>
<tr class="odd">
<td>FIM Durability</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Follow-up; FIM total score for each assessment must have a non-null value.</p>
<p>First calculate individual values for FIM Durability for each dataset within each diagnostic category:</p>
<p>FIM Durability = FIM Total at Follow-up - FIM Total at Finish</p>
<p>Calculate the Average FIM Durability for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>Diener SWLS Change</td>
<td><p>To use a dataset, it must have a Diener’s SWLS assessment of score type Finish and a Diener’s SWLS assessment of score type Start; Diener’s SWLS total score for each assessment must have a non-null value.</p>
<p>Calculate individual values for Diener’s SWLS Change for each dataset within each diagnostic category:</p>
<p>Diener’s SWLS Change = Score at Finish - Diener’s SWLS Score at Start</p>
<p>Calculate the Average value of Diener’s SWLS Change for each diagnostic category.</p></td>
</tr>
<tr class="odd">
<td>Diener SWLS Durability</td>
<td><p>To use a dataset, it must have a Diener’s SWLS assessment of score type Finish and a Diener’s SWLS assessment of score type Follow-up; Diener’s SWLS total score for each assessment must have a non-null value.</p>
<p>Calculate individual values for Diener’s SWLS Durability for each dataset within each diagnostic category:</p>
<p>SWLS Durability = Diener’s SWLS at Follow-up - Diener’s SWLS at Finish.</p>
<p>Calculate the Average value of Diener’s SWLS Durability for each diagnostic category.</p></td>
</tr>
</tbody>
</table>

#### Continuum of Care Inpatient Outcomes Report Topics Descriptions 

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Continuum of Care Inpatient Outcomes Report Topics</strong></th>
</tr>
<tr class="odd">
<th><strong>Report Topic</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td># and % of Patients</td>
<td><p>Number of patient datasets in the diagnostic category and Percentage of datasets in all diagnostic categories that number represents.</p>
<p>% is the number of diagnostic datasets divided by number of all datasets.</p></td>
</tr>
<tr class="even">
<td>Age (yrs)</td>
<td><p>Calculate age of individual patient for each dataset in diagnostic category.</p>
<p>Calculate Average patient age for each diagnostic category.</p></td>
</tr>
<tr class="odd">
<td>Age Range</td>
<td>Range of ages in datasets, from the age of the youngest person to the age of the oldest person for each diagnostic category</td>
</tr>
<tr class="even">
<td>Gender (% Male pts)</td>
<td>Percentage of males in diagnostic category.</td>
</tr>
<tr class="odd">
<td>Length of Stay (days)</td>
<td>Length of Stay = Care Close Date - Care Start Date</td>
</tr>
<tr class="even">
<td>Length of Stay Range</td>
<td>Range of length of stay from least number of days to most number of days within datasets used for each diagnostic category.</td>
</tr>
<tr class="odd">
<td>Total FIM Change</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Start; FIM total score for each assessment must have a non-null value.</p>
<p>First calculate each individual’s FIM Change for each dataset:</p>
<p>Total FIM Change = FIM Total score at Finish - FIM Total score at Start</p>
<p>Then calculate the Average value of FIM Change for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>FIM Efficiency</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Start; FIM total score for each assessment must have a non-null value; the system must be able to calculate the Length of Stay.</p>
<p>First calculate individual’s FIM Efficiency for each dataset within each diagnostic category:</p>
<p>FIM Efficiency = Total FIM Change / Length of Stay</p>
<p>Then calculate the Average FIM Efficiency value for each diagnostic category.</p></td>
</tr>
<tr class="odd">
<td>FIM Goal Attainment</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Goal; FIM total score for each assessment must have a non-null value.</p>
<p>First calculate the individual values for FIM Goal attainment for each dataset in the diagnostic category:</p>
<p>FIM Total at Finish - FIM Total at Goal</p>
<p>Then calculate the Average value for FIM Goal attainment for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>FIM Durability</td>
<td><p>To use a dataset, it must have a FIM assessment of score type Finish and a FIM assessment of score type Follow-up; FIM total score for each assessment must have a non-null value.</p>
<p>First calculate individual values for FIM Durability for each dataset within each diagnostic category:</p>
<p>FIM Durability = FIM Total at Follow-up - FIM Total at Finish</p>
<p>Calculate the Average FIM Durability for each diagnostic category.</p></td>
</tr>
<tr class="odd">
<td>Diener SWLS Change</td>
<td><p>To use a dataset, it must have a Diener’s SWLS assessment of score type Finish and a Diener’s SWLS assessment of score type Start; Diener’s SWLS total score for each assessment must have a non-null value.</p>
<p>Calculate individual values for Diener’s SWLS Change for each dataset within each diagnostic category:</p>
<p>Diener’s SWLS Change = Score at Finish - Diener’s SWLS Score at Start</p>
<p>Calculate the Average value of Diener’s SWLS Change for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>Diener SWLS Durability</td>
<td><p>To use a dataset, it must have a Diener’s SWLS assessment of score type Finish and a Diener’s SWLS assessment of score type Follow-up; Diener’s SWLS total score for each assessment must have a non-null value.</p>
<p>Calculate individual values for Diener’s SWLS Durability for each dataset within each diagnostic category:</p>
<p>SWLS Durability = Diener’s SWLS at Follow-up - Diener’s SWLS at Finish.</p>
<p>Calculate the Average value of Diener’s SWLS Durability for each diagnostic category.</p></td>
</tr>
</tbody>
</table>

#### Annual Evaluation Outcomes Report Topics Descriptions

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Annual Evaluation Outcomes Report Topics</strong></th>
</tr>
<tr class="odd">
<th><strong>Report Topic</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td># and % of Patients</td>
<td><p>Number of patient datasets in the diagnostic category and Percentage of datasets in all diagnostic categories that number represents.</p>
<p>% is the number of diagnostic datasets divided by number of all datasets.</p></td>
</tr>
<tr class="even">
<td>Age (yrs)</td>
<td>Calculate age of individual patient for each dataset in diagnostic category; then Calculate Average age for each diagnostic category.</td>
</tr>
<tr class="odd">
<td>Age Range</td>
<td>Range of ages in datasets, from the age of the youngest person to the age of the oldest person for each diagnostic category.</td>
</tr>
<tr class="even">
<td>Gender (% Male pts)</td>
<td>Percentage of males in diagnostic category.</td>
</tr>
<tr class="odd">
<td>Total FIM Score</td>
<td><p>To use a FIM assessment in this calculation, it must have a FIM Total score.</p>
<p>Calculate the Average FIM Total Score for each diagnostic category.</p></td>
</tr>
<tr class="even">
<td>Motor FIM Score</td>
<td>To use a FIM assessment in this calculation, it must have a FIM Motor score. Calculate the Average FIM Motor Score for each diagnostic category.</td>
</tr>
<tr class="odd">
<td>Cognitive FIM Score</td>
<td>To use a FIM assessment in this calculation, it must have a FIM Cognitive score. Calculate the Average FIM Cognitive Score for each diagnostic category.</td>
</tr>
<tr class="even">
<td>CHART Physical Indep</td>
<td><p>To use a CHART-SF assessment in this calculation, it must have a CHART-SF Physical Independence Score.</p>
<p>Calculate the Average CHART Physical Independence score for each diagnostic category.</p></td>
</tr>
<tr class="odd">
<td>CHART Cognitive Indep</td>
<td>To use a CHART-SF assessment in this calculation, it must have a CHART-SF Cognitive Independence Score. Calculate the Average CHART Cognitive score for each diagnostic category.</td>
</tr>
<tr class="even">
<td>CHART Mobility</td>
<td>To use a CHART-SF assessment in this calculation, it must have a CHART-SF CHART Mobility Score. Calculate the Average CHART Mobility score for each diagnostic category.</td>
</tr>
<tr class="odd">
<td>CHART Occupation</td>
<td>To use a CHART-SF assessment in this calculation, it must have a CHART-SF Occupation Score. Calculate the Average CHART Occupation score for each diagnostic category.</td>
</tr>
<tr class="even">
<td>CHART Social Interaction</td>
<td>To use a CHART-SF assessment in this calculation, it must have a CHART-SF Social Interaction Score. Calculate the Average CHART Social Interaction score for each diagnostic category.</td>
</tr>
<tr class="odd">
<td>CHART Economic</td>
<td>To use a CHART-SF assessment in this calculation, it must have a CHART-SF Economic Score. Calculate the Average CHART Economic score for each diagnostic category.</td>
</tr>
<tr class="even">
<td>Diener SWLS</td>
<td>To use a Diener’s SWLS assessment in this calculation, it must have a Diener’s SWLS Total Score. Calculate the Average Diener SWLS Score for each diagnostic category.</td>
</tr>
</tbody>
</table>

## Custom Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can generate custom reports to your specifications by learning to use the Report Designer, which allows you to select the criteria, format, and information needed for a report.

To generate a custom report, select the *Report Designer* button. Select a category and subject area of information to use in the report, and then select specific attributes to print in the report or to use as filters or sorting criteria. Sorting determines the order in which the rows of information occur. Filters allow the selection of specific portions of the population to be included in the report while excluding all others.

On the custom report definition page, a right arrow ![](scido-version-3-user-manual/104.png) allows movement of information from the attributes to be used in printing, sorting, or filtering. The ![](scido-version-3-user-manual/105.png) allows deletion of attributes from printing, sorting, or filtering. Up ![](scido-version-3-user-manual/106.png) and down ![](scido-version-3-user-manual/107.png) arrows are used to change the order of printed attributes or sorting criteria. Once filters have been selected, a second page will allow definition of values or ranges, if needed, for the selected filters.

When the Custom Report page first opens, it appears as follows with the categories listed and three print columns of Name, SSN, and Division already established. You can delete Name, SSN, or Division from the print column by selecting them and using the deletion function. ![](scido-version-3-user-manual/108.png)

| ![](scido-version-3-user-manual/109.png) |
|--------------------------------------------------------------------------------------------------------------------------------------------|

Select the category, subject area, and attributes of subject area and add them to the print, sort, and filter columns, one at a time. As you select a category, the available subject areas for that category are displayed. After you choose a subject area, the available attributes become available.

In the example that follows, the Category ASIA was selected. Then the Subject area of ASIA was selected. From the ASIA attributes of subject area, ASIA Impairment was chosen and added to the Print, Sort, and Filter columns, using the arrows. From the ASIA attributes of subject area, Neurological Level was chosen and added to the print and filter columns using the arrows.

![](scido-version-3-user-manual/110.png)

Select *Submit* to submit your custom report definitions. The Custom Filter Criteria window displays the filter options you selected in your definition. In the previous example, the filters selected were ASIA Impairment and Neurological Level. In the example below, we chose to highlight C as the only choice for ASIA Impairment and entered C07 for Neurological Level.

| ![](scido-version-3-user-manual/111.png) |
|---------------------------------------------------------------------------------------------------------------------------------|

To select more than one ASIA Impairment filter criteria, hold down the Ctrl Key and highlight all desired filter criteria from the list. To select a range of filter criteria values, hold down the Shift key and select a beginning and end value. For example, for the ASIA Impairment, you could select “C” and then move down the list to “E”. For the ASIA Impairment list, there is a value of “UNK = Unknown” that is not visible in the example above, but can be viewed by scrolling down the filter list. Being able to select a range is useful when selecting from a large filter criteria list. For some criteria, such as the Neurological Level, there is no list to choose from, and values must be entered accurately.

After selecting the *Submit* button, the Custom Report Results are displayed. The Custom Report Result page shows the Template (Print) Columns that were selected on the Custom Report Definition page. The report parameters, including the filters used as criteria, are displayed at the bottom of the report.

| ![](scido-version-3-user-manual/112.png) |
|----------------------------------------------------------------------------------------------------------------------------------------|

If there are no report results, the System returns a message that “Your filter criteria returned no patients. Please check your selections and try again.”

You have the option of exporting the report results into a comma-separated value (CSV) file format or into an Excel spreadsheet format using the Export Option commands <u>CSV</u> and <u>Excel</u> at the bottom of the report.

From the Custom Report Result page, select *Cancel* to return to the Reports tab. The *Back* button will take you back to the Custom Filter Criteria page, where you can re-select filter criteria, then rerun the report. It is often prudent when rerunning reports to return to the Reports tab to reselect all the criteria, rather than using the *Back* function.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access and Permission 9, 69
Activate
assessment(s) 69, 72
episode(s) of care 72
patient status 69, 71
Activities Tab 2
Additional Care VA
filter 66
Administration tab 69–74
Administration Tab 3
Administrator role 69, 70
Admissions (SCI&D) report 61
Age
filter 66
in tab header 3
Aggregate report *See* Reports, Cumulative
Alcohol Abuse *See* AUDIT and CAGE
Alcohol Use Disorders Identification Test (AUDIT) 7, 34
assessment form 89–90
used with CAGE 92
American Spinal Injury Association Standard Neurological Classification of Spinal Cord Injury *See* ASIA
Ancillary Data Entry form 22, 116–17
Fields
Additional Care VAMC 116
BCR Certified 117
BCR Provider 117
Bowel Care Reimbursement (BCR) 117
Initial Rehabilitation Discharge Date 117
Initial Rehabilitation Site 117
Non-VA Care 116
Referral Source 116
Referral VA 116
Remarks 117
Annual Evaluation
information on Registration tab 15, 20
Next Due
filter 66
in tab header 3
on Registration tab 20
Annual Evaluation Outcomes report 61, 129, 135
Annual Evaluation VAMC
filter 66
Registration tab 20
Applications for Inpatient Care report 61
ASIA 7, 34
assessment form 86–88
Complete/Incomplete 86, 88
impairment scale
filter 66
in tab header 3
on ASIA form 86, 88
on Registration tab 17
Information Section on Registration tab 15, 16–17
neurological level
filter 66
in tab header 3
on ASIA form 86, 88
on Registration tab 17
recommended to be entered first 29
Assessment(s) 49
activating or inactivating 72
blank forms 53, 56
button functions 53
creating 54
editing 55
entry forms 85
follow-up score type 30–31
forms 85–115
header 29, 52, 53, 52–53
header fields 29
in SCIDO application 7–8
on Impairments tab 34
versus instrument 35
Attendant Care 48
hours of assistance on CHART-SF 94
Interruptions 48
loss admissions 48
AUDIT *See* Alcohol Use Disorders Identification Test
Audit Log report 76
Back function 53
Basic Patient Information report 62
Benchmarks
CHART-SF 49
FIM 43, 44, 47
MSCIS 49, 130
SWLS 47
Bladder Accident Frequency 7, 44, 109
Bladder Drainage 39
Body Mass Index (BMI) 7, 34
assessment form 91
description 33–34
Bowel Accident Frequency 7, 44, 109
Bowel Care Reiumbursement (BCR) 117
Breakdown of Patients report 62
CAGE (<u>C</u>ut Down, <u>A</u>nnoy, <u>G</u>uilt, <u>E</u>ye-Opener) 7, 34
assessment form 92
Calculate function 54
Calendar 4, 54
Cancel function 11, 54
Care Close Date
episode of care 27
previous episode(s) of care 28
Care Start Date
episode of care 25, 26, 27
on assessments 29, 52, 53
previous episodes of care 28
Care types 52, 55
episode of care 25, 26, 27, 29
Catastrophically disabled 24
Catchment *See* SCI region
Category of Injury filter 66
Cause of Injury filter 66
Center for Epidemiologic Studies Depression Scale (CES‑D) 7, 34
Center for Epidemiologic Studies Depression Scale (CES-D) form 93
CES-D *See* Center for Epidemiologic Studies Depression Scale
CHART-SF 7, 51
assessment history 49
progress notes *See* Progress Notes
subscales 49
Check Your Health (CYH) 7, 34
assessment form 97–98
Clinician role 70
Community Discharges report 61
Continuum of Care Inpatient Outcomes report 61, 129, 133–34
Coordinator, SCI 22, 70
Copyright information 83–84
County, filter 66
Cover Sheet tab 2, 13
Craig Handicap Assessment and Reporting Technique *See* CHART-SF
Cumulative Reports *See* Reports, cumulative
Current Inpatients report 62
Custom reports *See* Reports, custom
CYH *See* Check Your Health (CYH)
Date of Death field 23, 24
Definitions 79
Deployment Guide, SCIDO 1
Diagnoses 41, 42
Impairments & Medical Complications reports 60
on Cover Sheet 2, 13
on Urinary Tract Infections report 126
pneumonia or atelectasis 38
pre-existing 5, 34
secondary 2, 5, 34
urinary tract 39
Diagnosis or Health Problem field 101
Diagnostic Categories, cumulative reports 129
Diener's SWLS *See* Satisfaction with Life Scale (SWLS)
Discharges (SCI&D) report 62
Division filter 66
Drug Abuse Screening Test (DAST) 7, 34
DUSOI 7, 34
DUSOI-A 7, 35
assessment form 103
EDSS *See* Kurtzke Expanded Disability Status Scale
Education
form *See* Patient Education form
on Participation tab 50
on Registration tab 21
report 62
Employment status 50
Employment, hours per week 51
Enrollment Priority 24
EoC Close Date *See* Care Close Date
EoC Start Date *See* Care Start Date, episode of care
Episode of Care 22
activation or inactivation 72
close date 27
closing 27
creating 26–27
follow-up date 28–29
previous 28
start date *See* Care Start Date
Ethnicity filter 68
Etiology
filter 66
information on Registration tab 15, 18–20
Trauma or Non-Trauma 18
Expanded Patient Listing report 62
FAM *See* Functional Assessment Measure
Fee Basis filter 67
FIM *See* Functional Independence Measure (FIM)
Follow-Up (Last Seen) report 63
Follow-up date 28–29
Follow-Up Last A.E. Received report 62
*FSSSee Kurtzke Functional Systems Scale (FSS)*
Function Related Group (FRG) 106
Functional Assessment Measure (FAM) 7, 44
assessment form 104
Functional Independence Measure (FIM) 7, 43
assessment form 105–6
average change 130
change 132
cognitive score 44
durability 130, 132, 133
efficiency 130, 133
filter 68
goal attainment 130, 132, 133
motor score 44
polar graph 106
progress notes *See* Progress Notes
Geographic Area filter 67
Graphs
Activities tab 43
FIM Polar 106
Impairments tab 33
Medical Complications tab 37
Participation & SWLS tab 47
Help 4, 54
History fields 5
Home Maintenance, hours per week 51
Homemaking, hours per week 51
Hours of Help filter 67
Household, number in 48
ICD Code Search report 62
ICD Search 101
Impairments
and Medical Complications reports 60–61
reports 59
tab 2, 33–35
Import Record 69, 70, 71
Inactivate
assessment(s) 69, 72
episode(s) of care 72
patient status 69, 71
Influenza 2, 38
Diagnoses and Treatment report 60
Immunizations report 60
Influenza Diagnoses and Treatment Report 120
Influenza Immunizations Report 121
Information Resource Management (IRM)
monitoring of system activities 76
role 69, 70
tab 75–77
Tab 3
Inpatient Outpatient Activity report 63
Inpatient Outpatient Specific at Your Division report 63
Inpatient Rehabilitation Outcomes report 61, 129–31
Inpatient Visit filter 67
Institutional view 70
Instrument(s) *Seealso* Assessment(s)
in SCIDO application 7–8
versus assessment 35
Instruments 85
Integration Control Number (ICN) 69, 72
IRF-PAI 7, 109
IRM *See* Information Resource Management
Kurtzke Expanded Disability Status Scale (EDSS) 7
assessment form 107
Kurtzke Functional Systems Scale (FSS) 7
assessment form 108
Lab Utilization (Specific) at Your Division report 63
Laboratory Utilization at Your Division report 63
Locked Records 76
Login 9
Logout 3
Mail Groups 69, 73
Mailing Labels report 63
Master Patient Index (MPI) 72, 75
McGill Pain Questionnaire *See* Short Form McGill Pain Questionnaire (SF-MPQ)
Medical Complications reports 59
Medical Complications tab 2, 37–42
Pain section 42
Pressure Ulcer Finish section 41
Pressure Ulcer Risk section 40
Medical Needs Function Modifiers 7, 34, 44
assessment form 109
bladder accidents frequency rating 44
bowel accident frequency rating 44
Medications filter 67
Metro/Micro/Rural 49
MNFM *See* Medical Needs Function Modifiers
Motor Key Muscle fields *See* ASIA, assessment form
MS (Kurtzke) Measures report 63
Multiple Sclerosis 2
EDSS *See* Kurtzke Expanded Disability Status Scale
etiology 19
filter 67
FSS *See* Kurtzke Functional Systems Scale (FSS)
mail group 3, 69, 73
report *See* MS (Kurtzke) Measures report
subtype 19
National/Regional Update 77
Neuro. Level *See* ASIA, neurological level
Neurological Classification of Spinal Cord Injury *See* ASIA
Neurological Level"*See*ASIA,neurologicallevel 57
New SCI&D Patients report 63
Occupation
at Injury 51
current 51
Occupation and Education 50–51
Outpatient Rehabilitation Outcomes report 61, 129–31, 132
Outpatient Visit filter 67
Pain 2, 37, 42, 114
Assessment and Treatment report 60, 122
SF-MPQ 8
Participation & SWLS tab 2, 47–51
assessments 49
attendant care 48
CHART-SF subscales 49
Occupation and Education 50–51
Patient Education form 22, 118
Patient Education report 62
Patient Listing by State and County report 63
Patient Listing report 63
Patient listing(s) reports 61–62
Patient Lookup 3
Patient search 3, 9
Patient status 69, 71
Patient Summary report 62
Patients with Future Appointments report 62
PDF *See* Assessment(s), blank forms
Pharmacy Utilization at Your Division report 63, 64
Pneumococcal Immunizations report 60, 124
Pneumonia and Respiratory report 37–38, 60, 123
Pneumonia on Medical Complications tab 37–38
Pressure Ulcer Scale for Healing (PUSH) 8, 40
assessment form 111
Pressure Ulcer(s) 39–41
Finish section 41
PUSH instrument *See* Pressure Ulcer Scale for Healing (PUSH)
report 60, 126
Risk section 40
stage in tab header 3
Primary Care information on Registration tab 15, 18
Primary Care VA filter 67
PRIME-MD 8, 35
assessment form 110
Print function 4, 53
Procedures, pre-existing 34
Progress Notes 56–58
Prosthetics filter 67
Prosthetics Utilization (Specific) at Your Division report 64
Prosthetics Utilization at Your Division report 64
PUSH *See* Pressure Ulcer Scale for Healing (PUSH)
Race filter 67
Radiology Utilization at Your Division report 64
RAI-MDS 61
RAI-MDS Quality Indicators Report 127
RAI-MDS Resource Utilization Groups (RUGS) Report 128
Readmissions report 62
Recreation, hours per week 51
Regional attributes 3, 70, 75
Regional view 70
Registration Ancillary Data Entry form *See* Ancillary Data Entry form
Registration Status 15, 16
filter 68
Registration tab 2, 15–16
Additional Information Section 20–22
Annual Evaluation Information Section 20
ASIA Information section 16–17
Etiology Information Section 18–20
Primary Care Information 18
Registration and Network Section 16
required fields 15
Report Designer *See* Reports, custom
Reports
cumulative 59, 61, 129–35
custom 2, 59, 60, 136–38
export options 60
filtered 59, 68
filters 64–68
patient listing(s) 59, 61–62
tab 59–68
Tab 2
Required fields
marked on assessments 52
Researcher role 70
Reset function 4, 54
Roles 69, 70
Sample DUSOI
assessment form 100–102
Satisfaction with Life Scale (SWLS) 8, 49, 131
assessment form 112
progress notes *See* Progress Notes
School, hours per week 51
SCI Network 15
filter 68
SCI Network? 16
SCI region(s)
on Administration tab 70, 73
SCI Network 15
SCIDO Outcomes Coordinator *See* Coordinator, SCI
SCI region(s)
on Administration tab 69
on IRM tab 76
Score type(s)
episode of care 25, 26, 27, 29
finish 27, 30, 53
follow-up 30, 53
goal 27, 30, 53
interim 30, 53
on assessments 29, 53, 55
start 30, 53
unknown 30, 53
Secondary Conditions Checklist *See* Check Your Health (CYH)
Secondary conditions, on Impairments tab 34
Section 508 Compliance 1
Sensory Point fields *See* ASIA, assessment form
Separate window *See* Window Expander Icon
Service Connection filter 68
Sex filter 68
SF-8 Health Survey 8, 35
assessment form 113–14
Short Form McGill Pain Questionnaire (SF-MPQ) 8, 42
assessment form 115
Social section, Participation tab 48–49
State filter 66
Submit function 4, 54
assessment 55
progress note 58
Substance abuse assessments
Alcohol Use Disorders Identification Test (AUDIT) 89
CAGE 92
System Activities 76
Tabs
Fields
Age 3
Amount VA is Used 22
Annual Evaluation VAMC 20
Annual Evaluation, Next Due 20
Annual Evaluation, Offered 20
Annual Evaluation, Received 20
ASIA 3
Bladder Drainage 3, 39
Brain Injury 34
Current Occupation 51
Date Changed 16
Date of Birth 3
Date of Death Field 24
Date of Last Review 23
Date of Onset 19
Dehydration Signs 34
Describe Other 34
Describe Other Etiology 19
Education 3, 50
Employment 3
Employment Status 50
Enrollment Priority 24
Etiology 19
Etiology History 20
Finish Record Date 41
First Seen in VA for SCI 22
Highest Level of Education 21
Highest Neurological Level 17
Historic SCI&D Outcomes Coordinators 22
Impairment Scale 17
Is Ulcer Closed/Healed 41
Last Updated By 24
Medical Centers Visited 24
Metro/Micro/Rural 23
MS Subtype 19
Name 3
Network History 16
Neurological Level 3
Next AE Due 3
Occupation at Injury 51
Occupation at Time of Injury 21
Other Injury 34
Predominant Position at Finish 41
Pre-Existing Diagnoses 34
Pre-Existing Procedures 34
Pressure Ulcer (stage) 3
Pressure Ulcer Finish History 41
Pressure Ulcer Risk 40
Primary Care Provider 18
Primary Care VA Medical Center 18
Registration (Status) 16
Registration Date 23
Risk Instrument History 40
Risk Instrument Used 40
Risk Record Date 40
SCI Network? 16
SCI&D Outcomes Coordinator 22
Secondary Conditions 34
Service-Connected for SCI 21
SF-MPQ History 42
Sitting Time 41
Social Security Number 3
Student History 50
Student? 50
Swallowing Status 34
Time to Achieve Healing 41
Trauma or Non-Trauma 18
VA SCI Status 24
Ventilator Equip./Supplies 37
Veteran’s Home Address 23
Volunteer 50
header (of tabs) 3
Urinary Tract Infections
Impairments tab 38–39
report 60
Urinary Tract Infections Report 126
User Role *See* Roles
VA SCI status 24, 63
VA Service Desk 1
Verify Code 9
VHA National SCI Help Desk 1
VistA
document library 1
installation guide 1
report information 38, 39, 41
Vitals application 37, 42
Vital Status filter 68
Walk/Wheelchair filter 68
Window Expander Icon 5
Zip Code filter *See* Geographic Area filter
