---
title: Clinical Reminders Version 2 Clinician Guide Appendix D - GEC Reports
doc_type: APX
doc_label: Appendix
doc_layer: anchor
doc_subject: Clinician Guide  D - GEC Reports
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 1
description: > In December 2003, a Healthcare Inspection by the Department of Veteran Affairs Office of Inspector General was conducted on the Homemaker/Home Health Aide Program to evaluate Department of Veteran Affairs (VA) Medical facilities compliance with the Veteran Health Administration (VHA) policy for pr
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - last
  - criteria
  - number
  - class
  - crpatient
  - only
  - home
page_count: 0
word_count: 1827
section_count: 17
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: December 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_2_um_appd.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_2_um_appd.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> Appendix D: VA GEC Reports

> In December 2003, a Healthcare Inspection by the Department of Veteran Affairs Office of Inspector General was conducted on the Homemaker/Home Health Aide Program to evaluate Department of Veteran Affairs (VA) Medical facilities compliance with the Veteran Health Administration (VHA) policy for providing services to patients that were clinically appropriate, cost effective, and met customer expectations. The outcome of that Inspection revealed a lack of supportable data for placement of patients.

> As part of the Undersecretary for Health’s commitment to complying with VA policy, the need for accurately documenting and reporting patient placements is needed. VA Geriatric Extended Care (VA GEC) Reports will serve as an interim reporting method until the national rollup of VA GEC Referral data is provided through Computerized Patient Record System Reengineered (CPRS-R). VA GEC Reports will display the percent of patients referred to select GEC programs who meet the eligibility criteria as outlined in the Under Secretary for Health’s Information Letter IL 10-2003-005 and VHA Handbook 1140.2.

> VA GEC Reports will provide quarterly statistical reports on the following VA funded programs.

- Homemaker/Home Health Aide, when Funding Source=VA
- Adult Day Health Care, when Funding Source=VA
- VA In-Home Respite, when Funding Source=VA
- Care Coordination, when Funding Source=VA

> Select data from the VA Geriatric Extended Care Referral screening tool, released with Clinical Reminders 2.0, will be used in calculating the criteria totals for patients screened and referred for each of the four programs listed above.

## Data Elements for Reporting taken from the VA GEC Referral Screening of the following:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Source
- Living Situation
- Instrumental Activities of Daily Living
- Basic Activities of Daily Living
- Patient Behaviors and Symptoms
- Cognitive Status
- Prognosis

## Data Elements for Reporting taken from Patient File and Scheduling File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Age of Patient is 75 years or greater

> Patient Identified as a High Utilizer of Medical Services

## Implementation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The stakeholder will create an Excel spreadsheet for the purpose of importing the data received from the local sites, according to the specifications provided in the Algorithm that follows.

> Local sites must task the job by setting the queue to automatically generate the quarterly reports.

> The Office of Geriatric and Extended Care is responsible for importing data received, via electronic email, into a GEC created excel spreadsheet.

# Product Features


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Data Elements for Reporting taken from the VA GEC Referral Screening of the following:](#data-elements-for-reporting-taken-from-the-va-gec-referral-screening-of-the-following)
  - [Data Elements for Reporting taken from Patient File and Scheduling File](#data-elements-for-reporting-taken-from-patient-file-and-scheduling-file)
  - [Implementation Requirements](#implementation-requirements)
- [Product Features](#product-features)
  - [New Option](#new-option)
  - [New Mail Group](#new-mail-group)
  - [Important NOTE:](#important-note)
  - [Potential issues if you use Event Capture](#potential-issues-if-you-use-event-capture)
- [Algorithm For GEC (Next Generation) Software](#algorithm-for-gec-next-generation-software)
  - [Criteria \#1 : “Three or more Activities of Daily Living (ADL) dependencies.”](#criteria-1-three-or-more-activities-of-daily-living-adl-dependencies)
  - [OR](#or)
  - [OR](#or-1)
  - [OR](#or-2)
  - [AND](#and)
  - [OR](#or-3)
  - [OR](#or-4)
  - [OR](#or-5)
  - [OR](#or-6)
- [Example: Home Health Eligibility Report (All patients)](#example-home-health-eligibility-report-all-patients)
- [Example 2: Home Health Eligibility Report (Multiple patients)](#example-2-home-health-eligibility-report-multiple-patients)
- [Example: National Data Report](#example-national-data-report)
> The main feature of this product is the creation of a report that will allow monitoring compliance of VA patients referred to specified VA funded Geriatric Extended Care programs.
- Create a tool that will extract the data on patients meeting the criteria from the VA funded GEC program.
- The extracted data will be emailed to appropriate compliance office.

## New Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> GEC Fiscal Quarterly Rollup \[PXRM GEC2 QUARTERLY ROLLUP\]

> This is a queueable option that will gather and report to Washington DC the Fiscal Quarterly information. This option should never be placed on an individual’s menu. It should be scheduled for the 8th day of the first month of the next calendar quarter at any time of the facility’s choosing. The rescheduling frequency should be set to “3M” (every three months).

## New Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> GEC2 NATIONAL ROLLUP

> When this mail group is installed, it will contain the email address of the two individuals in Washington DC who will receive the quarterly data. These names should not be removed. Names of local individuals (for example, CACs) may be added, if they desire to receive these reports.

## Important NOTE:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> We recommend thorough testing of GEC reminder dialogs by staff prior to implementation to avoid GEC report roll-up inaccuracies. Testing of GEC reminder dialogs and reports in a test account should mimic the actual processes and workload capture used in the site's production environment.

> Informatics staff and GEC referral staff should work together to identify potential issues that arise during testing that may require modification of clinical processes and/or workload capture. Accurate capture and reporting of GEC referral health factors may require careful analysis of workload capture processes at sites that use Event Capture software. Inaccurate reporting may lead to questions from the Inspector General’s office concerning funding for the patients referred to the “Home Help” type of programs.

## Potential issues if you use Event Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> (reported by a test site):

1)  Event capture does not pass workload to PCE in real time. Data is not passed to PCE until after hours, so this needs to be taken into account when testing.
2)  There are several steps where real front-line users could make minor mistakes that would result in data entry/workload not matching up with the Care coordination note.
    1.  Event capture date/time must be an exact match to the date/time of PCE/TIU
    2.  Clinic location must be the same.
    3.  Data passes after hours from EC to PCE.
    4.  There is no drop-down menu to select from. 1 and 2 above must be manually entered.
    5.  Patient name must be re-selected (or use spacebar return).

# Algorithm For GEC (Next Generation) Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The information for the “criteria” is taken from the letter \# IL 10-2004-005 entitled UNDER SECRETARY FOR HEALTH’S INFORMATION LETTER dated May 3 2004. pages B-2 and B-3

> The following is the Algorithm or thought process that will be used in the software to determine if a patient meets the criteria necessary to be placed in one of the monitored programs. HEALTH FACTORS that are part of the patient record for an evaluation, are designated with capital letters (below).

> 7D = 7 days

> YES or NO = Yes or No response from the Dialog Additional explanations found to the right of health factor

> Initial Requirement is to be referred to one of the following VA funded programs. ( Requires 1 or 6, plus one of the other Health Factors)

1.  GEC ADULT DAY HEALTH CARE (REFERRED TO)
2.  GEC HOMECARE FUNDING-VA
3.  GEC HOMEMAKER/HOME HEALTH AIDE
4.  GEC VA IN-HOME RESPITE
5.  GEC HOME TELEHEALTH (REFERRED TO)
6.  GEC TELEHEALTH FUNDING-VA

## Criteria \#1 : “Three or more Activities of Daily Living (ADL) dependencies.”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> (Any 3 of the ADL’s below)

- GEC BATHING HELP/SUPERVISION LAST 7D-YES
- GEC BED POSITIONING HELP LAST 7D-YES
- GEC DRESS HELP/SUPERVISION LAST 7D-YES
- GEC EATING HELP/SUPERVISION LAST 7D-YES
- GEC INDEPENDENT IN WC LAST 7D-YES
- GEC MOVING AROUND INDOORS LAST 7D-YES
- GEC TOILET HELP/SUPERVISION LAST 7D-YES
- GEC TRANSFERS HELP/SPRVISION LAST 7D-YES

## OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Criteria \#2 : “Significant cognitive impairment” (Any 1 of those indicated below)

- GEC CAN BE UNDERSTOOD LAST 7D-NO
- GEC ENDANGERED SAFETY LAST 90D-YES
- GEC MADE REASONABLE DECISIONS LAST 7D-NO
- GEC HALLUCINATIONS/DELUSIONS LAST 7D-YES
- GEC PHYSICALLY ABUSIVE LAST 7D-YES
- GEC RESISTS CARE LAST 7D-YES
- GEC VERBALLY ABUSIVE LAST 7D-YES
- GEC WANDERING LAST 7D-YES

## OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Criteria \#3 “ Prognosis of Life Expectancy of less than 6 months”

> (Any 1 of these health factors )

- GEC LIFE EXPECTANCY \< 6MO-YES

## OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Criteria \#4 : “Two ADL dependencies and two or more of the following conditions:”

> (Any 2 of the ADL’s below and the additional requirements)

- GEC BATHING HELP/SUPERVISION LAST 7D-YES
- GEC BED POSITIONING HELP LAST 7D-YES
- GEC DRESS HELP/SUPERVISION LAST 7D-YES
- GEC EATING HELP/SUPERVISION LAST 7D-YES
- GEC INDEPENDENT IN WC LAST 7D-YES
- GEC MOVING AROUND INDOORS LAST 7D-YES
- GEC TOILET HELP/SUPERVISION LAST 7D-YES
- GEC TRANSFERS HELP/SPRVISION LAST 7D-YES

## AND

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “(a) Dependency in three or more Instrumental ADL (IADL)” (Any 3 of the IADL)

- GEC DIFFICULT TRANSPORTATION/LAST 7D-YES
- GEC DIFFICULTY MANAGING MEDS/LAST 7D-YES
- GEC DIFFICULTY MNG FINANCES/LAST 7D-YES
- GEC DIFFICULTY PREPARE MEALS/LAST 7D-YES
- GEC DIFFICULTY USING PHONE/LAST 7D-YES
- GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-YES
- GEC DIFFICULTY WITH SHOPPING/LAST 7D-YES

## OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “(b) Recent discharge from a nursing home, or upcoming nursing home discharge plan contingent

> on receipt of home and community – based care services.”

- GEC COMMUNITY NRSNG HOME (REFERRED FROM)
- GEC VA DOMICILIARY (REFERRED FROM)
- GEC VA NURSING HOME

## OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “(c) Seventy Five Years old , or older.”

> (Obtained from the Patient’s Records using an API call)

## OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “(d) High use of medical services defined as three or more hospitalizations in the past year and/or utilization of outpatient and/or emergency evaluation units twelve or more times in the past year.

> ( The API ….GETAPPT^SDAMA201(…) to retrieve appointments etc.)

## OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “(f) Living alone in the Community”

- GEC ALONE

# Example: Home Health Eligibility Report (All patients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the GEC Referral Report on the Reminder Managers Menu to produce reports.

> Y YES

> N NO

> Select Show Test Patients in this Report? Y or N or ^ to exit: YES

> DEVICE: HOME// ;;999 ANYWHERE Right Margin: 80//

> Please wait ...

> =============================================================================

> Referred to Homemaker/Home Health Aide(HHHA) or Adult Day Health Care(ADHC) or VA In-Home Respite(VAIHR) or Care Coordination programs(CC)

> From: 01/01/2005 To: 03/31/2005

> Fiscal Quarter: 2 (Calendar Quarter 1)

Criteria Measured

Name SSN Prog. 0 \#1 \#2 \#3 \#4 Date Criteria

> =============================================================================

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CRPATIENT,ONE</p>
</blockquote></th>
<th>C0000</th>
<th><blockquote>
<p>VAIHR</p>
</blockquote></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>01/27/2005</p>
</blockquote></th>
<th><blockquote>
<p>NOT</p>
</blockquote></th>
<th>MET</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,TWO</p>
</blockquote></td>
<td>C6667</td>
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td><blockquote>
<p>01/28/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRPATIENT,THREE</p>
</blockquote></td>
<td>C6668</td>
<td><blockquote>
<p>ADHC</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td>X</td>
<td><blockquote>
<p>02/09/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,FOUR</p>
</blockquote></td>
<td>C6669</td>
<td><blockquote>
<p>ADHC</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>01/31/2005</p>
</blockquote></td>
<td><blockquote>
<p>NOT</p>
</blockquote></td>
<td>MET</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRPATIENT,FIVE</p>
</blockquote></td>
<td>C6660</td>
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>01/27/2005</p>
</blockquote></td>
<td><blockquote>
<p>NOT</p>
</blockquote></td>
<td>MET</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,SIX</p>
</blockquote></td>
<td>C6661</td>
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>01/27/2005</p>
</blockquote></td>
<td><blockquote>
<p>NOT</p>
</blockquote></td>
<td>MET</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRPATIENT,SEVEN</p>
</blockquote></td>
<td>C6668</td>
<td><blockquote>
<p>ADHC</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td><blockquote>
<p>01/28/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,EIGHT</p>
</blockquote></td>
<td>C6663</td>
<td><blockquote>
<p>VAIHR</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>01/31/2005</p>
</blockquote></td>
<td><blockquote>
<p>NOT</p>
</blockquote></td>
<td>MET</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRPATIENT,NINE</p>
</blockquote></td>
<td>C6664</td>
<td><blockquote>
<p>ADHC</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td><blockquote>
<p>02/09/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,TEN</p>
</blockquote></td>
<td>C6670</td>
<td><blockquote>
<p>ADHC</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td><blockquote>
<p>02/09/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRPATIENT,ELEVEN</p>
</blockquote></td>
<td>C6671</td>
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td><blockquote>
<p>01/27/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,TWELVE</p>
</blockquote></td>
<td>C6663</td>
<td><blockquote>
<p>ADHC</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>02/09/2005</p>
</blockquote></td>
<td><blockquote>
<p>NOT</p>
</blockquote></td>
<td>MET</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRPATIENT,THIRTEEN</p>
</blockquote></td>
<td>C6662</td>
<td><blockquote>
<p>VAIHR</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>02/03/2005</p>
</blockquote></td>
<td><blockquote>
<p>NOT</p>
</blockquote></td>
<td>MET</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,THIRTEEN</p>
</blockquote></td>
<td>C6662</td>
<td><blockquote>
<p>ADHC</p>
</blockquote></td>
<td></td>
<td>X X</td>
<td>X</td>
<td></td>
<td><blockquote>
<p>02/10/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CRPATIENT,THIRTEEN</p>
</blockquote></td>
<td>C6662</td>
<td><blockquote>
<p>ADHC</p>
</blockquote></td>
<td></td>
<td>X X</td>
<td></td>
<td></td>
<td><blockquote>
<p>02/09/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRPATIENT,FOURTEEN</p>
</blockquote></td>
<td>C6622</td>
<td><blockquote>
<p>HHHA</p>
</blockquote></td>
<td></td>
<td>X</td>
<td>X</td>
<td></td>
<td><blockquote>
<p>02/03/2005</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Criteria

> 0: Not eligible under any criteria. 1: Problems with 3 or more ADL's.

> 2: 1 or more patient behavior or cognitive problem. 3: Expected life limit of less than 6 months.

> 4: Combination of the following:

> 2 or more ADL dependencies

> \<AND\> 2 or more of the following: Problems with 3 or more IADL's

> \<OR\> age of patients is 75 or more.

> \<OR\> living alone in the community.

> \<OR\> utilizes the clinics 12 or more time in the preceding 12 months.

> Enter RETURN to continue or '^' to exit:

# Example 2: Home Health Eligibility Report (Multiple patients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lets you select individual patient names.

# Example: National Data Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 673,7,ADHC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,8,ADHC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,9,ADHC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,7,CC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,8,CC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,9,CC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,7,HHHA,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,8,HHHA,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,9,HHHA,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,7,VAIHR,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,8,VAIHR,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> 673,9,VAIHR,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

> The above information is Geriatric Extended Care "Home" Referral data from TAMPA VAMC \#673 for Fiscal Quarter \# 4 of 2008. (Calendar Quarter 3)

> Each section of data is separated by a comma. The table below defines the sections. Numbers represent Patients. Patient only counted once.

1.  Number for the site.
2.  Number that stands for the Month (1=January)...
3.  Acronym for the Program (ADHC,HHHA,VAIHR,CC)
4.  Total number of patients referred to the program that month
5.  Number that DID NOT MEET ANY of the criteria
6.  Number that only met criteria 1
7.  Number that only met criteria 2
8.  Number that only met criteria 3
9.  Number that only met criteria 4
10. Number that only met both criteria's 1 and 2
11. Number that only met both criteria's 1 and 3
12. Number that only met both criteria's 1 and 4
13. Number that only met both criteria's 2 and 3
14. Number that only met both criteria's 2 and 4
15. Number that only met both criteria's 3 and 4
16. Number that only met the criteria's 1 and 2 and 3
17. Number that only met the criteria's 1 and 2 and 4
18. Number that only met the criteria's 1 and 3 and 4
19. Number that only met the criteria's 2 and 3 and 4
20. Number that met all criteria's, 1 and 2 and 3 and 4

> The Basic Criteria for Eligibility is shown below.

> 1: Problems with 3 or more ADL's.

> 2: 1 or more patient behavior or cognitive problem. 3: Expected life limit of less than 6 months.

> 4: Combination of the following:

> 2 or more ADL dependencies.

> \<AND\> 2 or more of the following: problems with 3 or more IADL's.

> \<OR\> age of patients is 75 or more.

> \<OR\> living alone in the community.

> \<OR\> utilizes the clinics 12 or more times in the preceding 12 months.