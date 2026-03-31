---
title: Benefits Management Version 4 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: PSU
app_name: "Pharmacy: Benefits Management"
section: CLI
app_status: active
pkg_ns: PSU
patch_ver: 4
patch_id: PSU*4
group_key: "PSU:PSU:4"
file_numbers: 
  - 50
  - 58
  - 442
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - class
  - patient
  - strong
  - example
  - pharmacy
  - drug
  - table
  - message
  - even
  - statistics
page_count: 0
word_count: 29843
section_count: 21
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_um_r0714.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_um_r0714.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=91"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Pharmacy Benefits Management (PBM)

  User Manual
---

![](benefits-management-version-4-user-manual/001.png)

Software Version 4.0

June 2005

Office of Information and Technology (OI&T)

Product Development

|                      |
|----------------------|
| Revision History |

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Date</p>
</blockquote></td>
<td><strong>Revised Pages</strong></td>
<td><strong>Patch Number</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>7/2014</td>
<td>i, <a href="#mailman-messages">19</a>, <a href="#example-mailman-messages">27</a>, <a href="#example-mailman-messages-1">36</a>, <a href="#example-mailman-messages-2">45</a>, <a href="#example-mailman-messages-3">56</a>, <a href="#example-mailman-messages-4">72</a>, <a href="#example-mailman-messages-5">78</a>, <a href="#example-mailman-messages-6">83</a>, <a href="#statistics-format-7">85-88</a>, <a href="#ICDp90">90</a>-<a href="#ICDp92">92</a>, <a href="#example-mailman-messages-9">95</a>, <a href="#example-mailman-messages-10">101</a>, <a href="#example-mailman-messages-11">106</a>, <a href="#example-mailman-messages-12">111</a></td>
<td>PSU*4*19</td>
<td><p>Revised title page.</p>
<p>Updated Inpatient and Outpatient Extracts to include a new Code Set Indicator field in sections 4.8.1 and 4.9.1, and include ICD10 in Data Element field name.</p>
<p>Updated MailMan Message examples to reflect the addition of Code Set Indicators.</p>
<p>Changed all instances of “double up arrow (^^)” to “up arrow (^)” within MailMan message descriptions.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>1/2008</td>
<td>6-9</td>
<td>PSU*4*12</td>
<td><p>Move a Note from section 3.5 to section 3.2 and 3.3 to correspond with a change in patch PSU*4*12 that moves the trigger of the Patient demographic purge from the Retransmit Patient Demographic Data option to the PSU PSM Manual option and to the PSU PBM Auto option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/2006</td>
<td>100-102</td>
<td>PSU*4*10</td>
<td><p>Updated Allergies/Adverse Events Information Statistics chart in section 4.11.1 Statistics Format and updated the example of the MailMan messages in section 4.11.2 Example MailMan Messages for patch PSU*4*10.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/2006</td>
<td><p>iv,</p>
<p>115-132</p></td>
<td>PSU*4*3</td>
<td><p>PBM Extract Enhancements #3 project. Added Section 5. to Table of Contents. Added Section 5. HL7 Messages and 5.1. Data Specifications. Updated Glossary to include definitions of HL7 and HLO, and for page numbering purposes. Updated Index to include items from new section on HL7 Messages, and for page numbering purposes.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/2005</td>
<td>All</td>
<td></td>
<td>Original Release of PBM V. 4.0 User Manual<br />
<mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

*(This page included for two-sided copying.)*

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Orientation](#orientation)
- [PBM Options](#pbm-options)
  - [PBM Manager Menu](#pbm-manager-menu)
  - [Manual Pharmacy Statistics](#manual-pharmacy-statistics)
  - [Automatic Pharmacy Statistics](#automatic-pharmacy-statistics)
  - [Pharmacy Background Job Check](#pharmacy-background-job-check)
  - [Retransmit Patient Demographic Data](#retransmit-patient-demographic-data)
  - [Map Pharmacy Locations](#map-pharmacy-locations)
    - [Mapping Instructions](#mapping-instructions)
    - [Mapped/Unmapped Location Report](#mappedunmapped-location-report)
- [MailMan Messages](#mailman-messages)
  - [IV Extract](#iv-extract)
    - [Statistics Format](#statistics-format)
    - [Example MailMan Messages](#example-mailman-messages)
  - [UD Extract](#ud-extract)
    - [Statistics Format](#statistics-format-1)
    - [Example MailMan Messages](#example-mailman-messages-1)
  - [AR/WS Extract](#arws-extract)
    - [Statistics Format](#statistics-format-2)
    - [Example MailMan Messages](#example-mailman-messages-2)
  - [Prescription Extract](#prescription-extract)
    - [Statistics Format](#statistics-format-3)
    - [Example MailMan Messages](#example-mailman-messages-3)
  - [Procurement Extract](#procurement-extract)
    - [Statistics Format](#statistics-format-4)
    - [Example MailMan Messages](#example-mailman-messages-4)
  - [Controlled Substances Extract](#controlled-substances-extract)
    - [Statistics Format](#statistics-format-5)
    - [Example MailMan Messages](#example-mailman-messages-5)
  - [Patient Demographics Extract](#patient-demographics-extract)
    - [Statistics Format](#statistics-format-6)
    - [Example MailMan Messages](#example-mailman-messages-6)
  - [Outpatient Visits Extract](#outpatient-visits-extract)
    - [Statistics Format](#statistics-format-7)
    - [Example MailMan Messages](#example-mailman-messages-7)
  - [Inpatient PTF Record Extract](#inpatient-ptf-record-extract)
    - [Statistics Format](#statistics-format-8)
    - [Example MailMan Messages](#example-mailman-messages-8)
  - [Provider Data Extract](#provider-data-extract)
    - [Statistics Format](#statistics-format-9)
    - [Example MailMan Messages](#example-mailman-messages-9)
  - [Allergies/Adverse Events Extract](#allergiesadverse-events-extract)
    - [Statistics Format](#statistics-format-10)
    - [Example MailMan Messages](#example-mailman-messages-10)
  - [Vitals/Immunizations Information Extract](#vitalsimmunizations-information-extract)
    - [Statistics Format](#statistics-format-11)
    - [Example MailMan Messages](#example-mailman-messages-11)
  - [Lab Extract](#lab-extract)
    - [Statistics Format](#statistics-format-12)
    - [Example MailMan Messages](#example-mailman-messages-12)
- [HL7 Messages](#hl7-messages)
  - [Data Specifications](#data-specifications)
- [Glossary](#glossary)
- [Index](#index)
Pharmacy Benefits Management (PBM) V. 4.0 is a new enhanced version of the software and replaces PBM V. 3.0. In a series of three enhancements, new extracts and reports were created, existing extracts were modified, and some options were modified to increase the functionality of this software package. For more detail, refer to the *Pharmacy Benefits Management V. 4.0 Release Notes* document.
The software extracts medication dispensing data elements from the Outpatient Pharmacy, Inpatient Medications Intravenous (IV) and Unit Dose (UD), Automatic Replenishment/Ward Stock (AR/WS), Controlled Substances (CS) modules, Procurement information from Drug Accountability, Integrated Funds Control, Accounting and Procurement (IFCAP), and a limited amount of Laboratory data on a monthly basis.
The extracted data is electronically exported via MailMan to the PBM section in Hines, Illinois." MailMan messages are downloaded to text files onto the PBM network. These electronic messages are then passed through a translation process, which pulls text files into a database format and is checked for quality assurance and converts all local drug names to a common drug name and all local dispensing units to a common dispensing unit if possible. After translation, the information is added to the PBM national database.
Through an option placed on the pharmacy supervisor menu, the software makes data extraction reports available at local Veterans Affairs Medical Centers (VAMCs) and allows local management to use this data to project local drug usage and identify potential drug accountability problem areas. The PBM section is able to provide information on Local Facility, Veterans Integrated Service Network (VISN), and National product use on monthly, quarterly, and annual intervals. Pharmacy personnel at VAMCs and VISNs shall use this application to collect and report on pharmacy and patient statistics through user-executed options. Users of the database include the PBM, VAMCs, VISNs, and the research community.
PBM V. 4.0 extracts additional data elements and modifies current extracts to take advantage of enhancements made to the other Pharmacy modules since the release of previous versions (D&PPM V. 2.0) and PBM V. 3.0.
Related Documentation
*Pharmacy Benefits Management V. 4.0 Release NotesPharmacy Benefits Management V. 4.0 Installation GuidePharmacy Benefits Management V. 4.0 Technical Manual/Security Guide(This page included for two-sided copying.)*

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

> Example: *Manual Pharmacy Statistics* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them.

> Example: “Select DRUG:” indicates a screen prompt.

- Responses in bold face indicate what the user is to type in.

> Example: Printing a MAR report by ward group G, by ward W or by patient P.

- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.

> Example: Press \<Tab\> to move the cursor to the next field.

> Press \<Enter\> to select the default.

- ![](benefits-management-version-4-user-manual/002.png)Note: Indicates especially important or helpful information.
- Some of the menu options have several letters that are capitalized. By entering in the letters and pressing \<Enter\>, the user can go directly to that menu option (the letters do not have to be entered as capital letters).

> Example: From the *Unit Dose Medications* option: the user can key INQ and proceed directly into the *Inquiries Menu* option.

- ?, ??, ??? One, two, or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.
- ^ Caret (up arrow or a circumflex) and pressing \<Enter\> can be used to exit the current option.

*(This page included for two-sided copying.)*

# PBM Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes options that are available in PSU 4.0.

## PBM Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSU PBM MANAGER MENU\]

The *PBM Manager Menu* \[PSU PBM MANAGER MENU\] option grants the user access to the following options:

- *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] allows the user to manually run individual or combined extracts for a time period of their own choosing.
- *Retransmit Patient Demographic Data* \[PSU RETRANSMIT PATIENT DATA\] allows the user to resend the prior month’s patient demographic data to the PBM national database should the background job be interrupted. Patient demographic data is held for a period of 75 days before being purged.
- *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] allows the user to map Area of Uses (AOUs) from the AR/WS application, Narcotic Area of Uses (NAOUs) from the Controlled Substances application, and Pharmacy Locations from the Drug Accountability application to a specific Medical Center Division or Outpatient site.

## Manual Pharmacy Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSU PBM MANUAL\]

The *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option is used to gather the statistical information for a selected date range from the following files:

1.  Pharmacy Patient IV Subfile File \# 55.01
2.  Pharmacy Patient UD Subfile File \# 55.06
3.  AR/WS Stats File File \# 58.5
4.  Prescription File \# 52
5.  Procurement File \#442, \# 58.811, \# 58.81
6.  Controlled Substances File \# 58.81
7.  Patient Demographics File \# 2
8.  Outpatient Visits File \# 9000010, \# 9000010.07
9.  Inpatient PTF Record File \# 45
10. Provider Data File \# 200, \# 7, \# 49, \#8932.1
11. Allergy/Adverse Event File \# 120.8, \# 120.85
12. Vitals/Immunization Record File \# 120.5, \#9999999.14
13. Laboratory File \# 60, \# 63

This data can be collected for ALL of the files listed or for one or more specific files. A summary of data or a detailed report by drug can be delivered in a mail message or in a hard copy report.

![](benefits-management-version-4-user-manual/003.png)Note: Patient demographic data is retained in the PBM file for 75 days, after which time it is purged.

Example: Generating a Monthly Report for a Specific Package and Transmitting it Via MailMan

Select OPTION NAME: PSU PBM

1 PSU PBM AUTO Automatic Pharmacy Statistics

2 PSU PBM JOB CHECK Pharmacy Background Job Check

3 PSU PBM MANAGER MENU Manager Menu Options

4 PSU PBM MANUAL Manual Pharmacy Statistics

CHOOSE 1-4: 4 PSU PBM MANUAL Manual Pharmacy Statistics

Manual Pharmacy Statistics

The Pharmacy Benefits Management (PBM) report will extract

statistics from one or more of the following files:

1\. Pharmacy Patient IV Sub-file File \# 55.01

2\. Pharmacy Patient UD Sub-file File \# 55.06

3\. AR/WS Stats File \# 58.5

4\. Prescription File \# 52

5\. Procurement File \# 442,# 58.811,# 58.81

6\. Controlled Substances File \# 58.81

7\. Patient Demographics File \# 2

8\. Outpatient Visits File \# 9000010,# 9000010.07

9\. Inpatient PTF Record File \# 45

10\. Provider Data File \# 200,# 7,# 49,# 8932.1

11\. Allergy/Adverse Event File \# 120.8,# 120.85

12\. Vitals/Immunization Record File \# 120.5,# 9999999.14

13\. Laboratory File \# 60,# 63

This data can be collected for ALL of the files listed or for one or

more specific files. A summary of data or a detailed report by drug

can be delivered to you in a mail message or in a hard copy report.

Is this the monthly report? YES

Select Month/Year: 09/01 (SEP 2001)

Do you want a copy of this report sent to you in a MailMan message? NO// YES

Send this to the PBM section for addition to the master file? NO// YES

Select one or more of the following:

1\. IVs

2\. Unit Dose

3\. AR/WS

4\. Prescription

5\. Procurement

6\. Controlled Substances

7\. Patient Demographics

8\. Outpatient Visits

9\. Inpatient PTF Records

10\. Provider Data

11\. Allergies/Adverse Events

12\. Vitals/Immunizations Information

----------------------------------*report continues*------------------------------------

Laboratory data and a Patient Demographic summary report will be automatically

generated if IVs, Unit Dose, or Prescription extracts are chosen.

You may select all of the modules by entering “A” for ALL or by using “1:12”.

The Provider Data report may take an extended amount of time to run.

It is recommended that it be run during off peak hours.

Select the code(s) associated with the data requested: 1

You have selected: 1 - IVs

13 - Laboratory Results

Patient Demographic Summary

Print Summary Only? NO// YES

This report will automatically run as a background job.

REQUESTED TIME TO RUN: NOW// (JUL 14, 2004@16:10)

Tasked with 107699

If the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option completes successfully, the following two additional reports are generated. Examples are provided in the MailMan Messages section of this document.

PBM Timing Report: The PBM Timing report displays the start and stop date/time of each extract and a final calculation of how long it took to run. Extract times will vary depending on the system performance, the time that the extract is run (early in the morning, on a weekend versus in the middle of the day), and the amount of data extracted.

Confirmation Message: The confirmation message shows the package(s) whose dispensing statistics were extracted by the PBM Manual Pharmacy Statistics option.

## Automatic Pharmacy Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSU PBM AUTO\]

The site should assign the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option to the Pharmacy Supervisor’s menu. This option is used to gather the pharmacy statistics for the previous month from the following files:

1.  Pharmacy Patient IV Subfile File \# 55.01
2.  Pharmacy Patient UD Subfile File \# 55.06
3.  AR/WS Stats File File \# 58.5
4.  Prescription File \# 52
5.  Procurement File \#442, \# 58.811, \# 58.81
6.  Controlled Substances File \# 58.81
7.  Patient Demographics File \# 2
8.  Outpatient Visits File \# 9000010, \# 9000010.07
9.  Inpatient PTF Record File \# 45
10. Provider Data File \# 200, \# 7, \# 49, \#8932.1
11. Allergy/Adverse Event File \# 120.8, \# 120.85
12. Vitals/Immunization Record File \# 120.5, \#9999999.14
13. Laboratory File \# 60, \# 63

This option is executed as a background job each month. The statistics are gathered and then sent to the national PBM section <span class="mark">REDACTED</span> via MailMan messages. When scheduling the monthly frequency for this option to be executed, please remember to schedule it to run after the *Update AMIS Stats File* \[PSGW UPDATE AMIS STATS\] option has been executed.

![](benefits-management-version-4-user-manual/004.png)Note: To decrease the running time of the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option, the ability to extract all patient records from the PATIENT file (#2) every month is no longer provided. This functionality is still available through the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option.

![](benefits-management-version-4-user-manual/005.png)Note: Patient demographic data is retained in the PBM file for 75 days, after which time it is purged.

If the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option completes successfully, the following two additional reports are generated. Examples are provided in the MailMan Messages section of this manual.

PBM Timing Report: The PBM Timing report displays the start and stop date/time of each extract and a final calculation of how long it took to run. Extract times will vary depending on the system performance, the time that the extract is run (early in the morning, on a weekend versus in the middle of the day), and the amount of data extracted.

Confirmation Message: The confirmation message shows the package(s) whose dispensing statistics were extracted by the PBM Manual Pharmacy Statistics option.

## Pharmacy Background Job Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSU PBM JOB CHECK\]

The *Pharmacy Background Job Check* \[PSU PBM JOB CHECK\] option checks to see if the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option ran to completion. A MailMan message will be sent to the local and remote members of the facility’s PSU PBM mail group and to the PBM national database at Hines if the report has not completed in six days. Population of the PSU PBM JOB field (#90) in the PHARMACY SYSTEM file (#59.7) with a date/time verifies completion. This option is scheduled automatically by the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option and normally does not need user intervention. In case of computer outage, it could be run manually.

Example: Pharmacy Background Job Check MailMan Message

Subj: PBM Automatic Statistics Job 437 FARGO \[#3526219\] 17 Sep 98 06:07 3 Lines

From: PBMpharmacist,One in 'IN' basket. Page 1

------------------------------------------------------------------------------

The PBM Automatic Statistics background job did not run to completion.

Please correct the problem and retransmit the data to the National PBM

section at Hines.

Select MESSAGE Action: IGNORE (in IN basket)// \<Enter\>

## Retransmit Patient Demographic Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSU RETRANSMIT PATIENT DATA\]

This option retransmits patient demographic data stored in the PBM file. When a user first enters the option, the software displays the purpose of this option and the first date there is data available for retransmission. The user shall be asked if this is a monthly report. If the response is “Yes”, the user shall be prompted to enter a Month/Year. If the response is ‘No’, the user shall be asked to enter a start date and end date. The user shall not be allowed to retransmit data for the current date. A message shall be displayed to the user stating that the current date is not selectable. If statistical data is not available for the entire month/year, start date, or end date selected, the software shall display a message to the user indicating either the range of dates for which statistical data is available or the start or end date of selectable data. The user shall be prompted to reenter the month/year, start date, or end date.

Example: Retransmission For a Month of Statistical Data.

Select OPTION NAME: Retransmit Patient Demographic Data

This option will allow the retransmission of Patient Demographic data stored in the XXXXXXX file. Statistical data starting from March 5, 2003 through May 3, 2003 is available for retransmission.

Is this the monthly report? YES

Select Month/Year: 3/03 (MAR 2003) *\<message shall display\>*

Data for the entire month of March 2003 is not available. Please reenter the month/year.

Select Month/Year: 4/03 (APRIL 2003)

Do you want a copy of this report sent to you in a MailMan message? NO// YES

Send this to the PBM section for addition to the master file? NO// YES

REQUESTED TIME TO RUN: NOW// *\<User can run immediately or queue for later date/time\>*  
Example: Retransmission For Two Weeks of Statistical Data.

Select OPTION NAME: Retransmit Patient Demographic Data

This option will allow the retransmission of Patient Demographic data stored in the PBM Patient Demographic file. Statistical data starting from March 5, 2003 through May 3, 2003 is available for retransmission.

Is this the monthly report? No

Select Start Date: 3/1/03 *\<message is displayed.\>*

Statistical data is only available starting March 5, 2003. Please reenter start date.

Select Start Date: 3/5/03 (MAR 5, 2003)

Select End Date: <u>T</u> *\<entry of current date not allowed\>*

Statistical data has not been compiled for current date. Please reenter stop date.

Select End Date: 3/17/03 (MAR 17, 2003)

*\<Both of the checks/messages illustrated shall be available at the start date and end date prompts.\>*

Do you want a copy of this report sent to you in a MailMan message? NO// YES

REQUESTED TIME TO RUN: NOW// QUEUE

QUEUE TO RUN AT: <T@1300>

*\<User can run immediately or queue for later date/time\>*

The user shall then be prompted with “Do you want a copy of this report sent to you in a MailMan message?”. If the user responds Yes, the message shall be sent to the user executing the option, and to local and remote members of the PSU PBM mail group. The user shall then be prompted with “Send this to the PBM section for addition to the master file?”. If the user responds Yes, the message shall be sent to the PBM national database. Only monthly reports shall be transmittable to the PBM national database. The user shall not be prompted to send the message to the master file if the user enters a timeframe other than a month.

The user shall be asked when they wish to run the job. The user shall be able to immediately run the job or queue it at a later date/time.

  
Example: Retransmit Patient Demographic Data MailMan Message

Subj: V. 4.0 PBMPD 30407 1/1 605 JERRY L PETTIS VAMC \[#8814\]

08/16/04@15:00 31 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^^^2191002^84^WHITE, NOT OF HISPANIC ORIGIN^M^NSC^REQUIRED^6^000007844^^^^^

2870722^H^^^^^^^^^^^^

^605^^^2240319^80^^M^SC LESS THAN 50%^REQUIRED^5^000000441^1001359871^^^^287072

2^H^^^^^^^^^^^^

^605^^^2411007^62^^M^SERVICE CONNECTED 50% to 100%^^1^000001038^1002931171^2965

27541^5547^^2870731^H^^^^^^^^^^^^

^605^^^2210812^83^^M^PRISONER OF WAR^^3^000005380^1008817231^^^^^^^^^^^^^^^^^

^605^^^2211022^82^^M^NSC^REQUIRED^^000001938^^^^^2870731^H^^^^^^^^^^^^

^605^^^2401211^63^^M^NSC, VA PENSION^NO LONGER REQUIRED^5^000008896^1002139837^

^^^2880814^H^^^^^^^^^^^^

^605^^^2360530^68^^M^SERVICE CONNECTED 50% to 100%^^1^000009397^^^^^2881016^H^^

^^^^^^^^^^

^605^^^2591112^44^^M^SC LESS THAN 50%^^3^000003720^1006067257^^^2880422^^^^^^^^

^^^^^^

^605^^^2230308^81^^M^NSC^REQUIRED^000008997^1009246561^^^2880514^2890430^H^^^^

^^^^^^^^

^605^^^2220616^82^WHITE, NOT OF HISPANIC ORIGIN^M^SC LESS THAN 50%^^3^000005299

^^^^2890223^2911022^H^^^^^^^^^^^^

Enter RETURN to continue or '^' to exit:

Subj: V. 4.0 PBMPD 30407 1/1 605 JERRY L PETTIS VAMC \[#8814\] Page 2

-------------------------------------------------------------------------------

^605^^^2540714^50^^M^SHARING AGREEMENT^^^000009841^1007950742^^^2900907^^^^^^^^

^^^^^^

^605^^^2280602^76^^M^NSC^REQUIRED^^000009837^^^^2910827^^^^^^^^^^^^^^

^605^^^2470121^57^WHITE, NOT OF HISPANIC ORIGIN^M^NSC^REQUIRED^^000004829^^^^29

20523^2930914^H^^^^^^^^^^^^

^605^^^2530916^50^^M^NSC^REQUIRED^^000007332^^^^2920803^^^^^^^^^^^^^^

^605^^3010517^2470805^53^WHITE, NOT OF HISPANIC ORIGIN^M^NSC^MT COPAY EXEMPT^5^

000004670^1002942817^^^2930422^2971119^H^^^^^^^^^^^^

^605^^^2461118^57^^M^SC LESS THAN 50%^REQUIRED^6^000003004^1008474662^^^2930424

^2950224^H^^^^^^^^^^^^

^605^^^2530509^51^^M^NSC^MT COPAY EXEMPT^5^000004701^^^^2930617^2950224^H^^^^^^

^^^^^^

^605^^^2510116^53^^M^NSC^MT COPAY EXEMPT^^000005315^^^^2930623^^^^^^^^^^^^^^

^605^^^2740701^30^^M^NSC^REQUIRED^^000008331^1009246519^^^2950112^^^^^^^^^^^^^^

^605^^^2640801^40^^F^SHARING AGREEMENT^^^000005772^1002971515^^^2980307^^^^^^^^

^^^^^^

^605^^^2590819^44^WHITE, NOT OF HISPANIC ORIGIN^M^SERVICE CONNECTED 50% to 100%

^^1^000005416^1002932269^568611354^10202^2980914^2981007^H^^^^^^^^^^^^

^605^^^2380915^65^WHITE, NOT OF HISPANIC ORIGIN^M^NSC^MT COPAY EXEMPT^5^0000030

25^1002945274^296527541^5547^2981130^2990812^H^^^^^^^^^^^^

Enter RETURN to continue or '^' to exit: ^

Enter message action (in IN basket): Ignore//

IN Basket Message: 660//

## Map Pharmacy Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSU MAP PHARMACY LOCATIONS\]

The *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option allows a user to map AOUs from the AR/WS application, NAOUs from the CS application, and Pharmacy Locations from the Drug Accountability application to a specific Medical Center Division or Outpatient Site.

![](benefits-management-version-4-user-manual/006.png)Note: Pharmacy locations must be mapped in order to receive a breakdown of data from those mapped sites for the AR/WS, CS, and Procurement extracts. If the locations are not mapped, the data on those extracts will be included in data from the parent facility.

### Mapping Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructs the user on how to map a Pharmacy location to an Outpatient Site or Division. This includes selecting the correct options, selecting the dispensing/ procurement location, selecting an AOU for mapping, and selecting an Outpatient Site or Division.

STEP 1: Select the *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option.

In the *PBM Manager Menu* \[PSU PBM MANAGER MENU\] option, select the *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option from the menu.

Example: *PBM Manager Menu* \[PSU PBM MANAGER MENU\] Option Menu

Select OPTION NAME: PSU

1 PSU MAP PHARMACY LOCATIONS Map Pharmacy Locations

2 PSU PBM AUTO Automatic Pharmacy Statistics

3 PSU PBM JOB CHECK Pharmacy Background Job Check

4 PSU PBM MANAGER MENU Manager Menu Options

5 PSU PBM MANUAL Manual Pharmacy Statistics

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 PSU MAP PHARMACY LOCATIONS Map Pharmacy Locations

Map Pharmacy Locations

A description of the option is initially displayed on the screen.

Example: Option Description

MAPPING PHARMACY LOCATIONS FOR PBM EXTRACTS

This option allows the mapping of dispensing/procurement locations

from the AR/WS, Controlled Substances, and Drug Accountability

applications to either a Medical Center Division or an Outpatient Site.

Any dispensing/procurement data associated with an AR/WS AOU, CS NAOU

or DA Pharmacy Location that has not been mapped will be attributed to

to the facility at which the database resides. Any unmapped locations

will be displayed upon entering the option.

The software checks for unmapped (active or inactive) locations, which are displayed to the user.

The following AR/WS AOUs are not mapped:

2AS

4AS \*\*Inactive\*\*

The following CS NAOUs are not mapped:

6AS

Anesthesia

The following DA Pharmacy Locations are not mapped:

Outpatient Pharmacy

Inpatient Pharmacy

STEP 2: Select the Dispensing/Procurement Location.

The system then prompts the user to select the dispensing location. The user may select one specific location type by entering the number associated with the desired location or select all locations by entering A, which grants an opportunity to print a report of mapped/unmapped locations.

Example: Selecting the AR/WS AOU Dispensing/Procurement Location

Select the dispensing location to map:

1\. AR/WS Area of Use (AOU)

2\. Controlled Substances (CS) Narcotic Area of Use (NAOU)

3\. Drug Accountability (DA) Pharmacy location

4\. Print Report of Mapped/Unmapped Locations

You may select all by entering 'A' for ALL or by using '1:4'.

Select the dispensing/procurement location: 1

You have selected:

1\. AR/WS Area of Use (AOU)

EDITING Mapping of AR/WS AOUs

Select PBM AR/WS AOU MAPPINGS:

The four menu options in the previous example are described below.

1)  AR/WS AOU - The user is allowed to select an active or inactive AOU. \*\*Inactive\*\* shall be displayed next to a selected inactive AOU. If the AOU has already been mapped, the Medical Center Division or Outpatient Site shall be displayed next to the selected AOU.
2)  CS NAOU - Only NAOUs that do not have a “P” for “Primary” in the LOCATION TYPE field (#1) of the DRUG ACCOUNTABILITY STATS file (#58.8) shall be selectable. The user is allowed to select an active or inactive NAOU. \*\*Inactive\*\* shall be displayed next to a selected inactive NAOU. If the NAOU has already been mapped, the Medical Center Division or Outpatient Site shall be displayed next to the selected NAOU.
3)  DA Pharmacy location - Only Pharmacy locations that have a “P” for “Primary” in the LOCATION TYPE field (#1) of the DRUG ACCOUNTABILITY STATS file (#58.8) shall be selectable. The user is allowed to select an active or inactive Pharmacy Location. \*\*Inactive\*\* shall be displayed next to a selected inactive Pharmacy location. If the Pharmacy location has already been mapped, the Medical Center Division or Outpatient Site shall be displayed next to the selected Pharmacy location.
4)  Print Report of Mapped/Unmapped Locations - The user is given the opportunity to print a report of mapped/unmapped locations. When choosing to print a report, the user shall be prompted to select a device and time that the report should be run.

![](benefits-management-version-4-user-manual/007.png)Note: If the user enters a ? at the “Select the dispensing/procurement location:” prompt, the following help text shall be displayed.

Enter: A single code number to print just that report.

A range of code numbers. Example: 1:3

Multiple code numbers separated by commas. Example: 2,4

The letter A to select ALL.

A single up-arrow (^) to exit the option.

The following example illustrates selecting all dispensing/procurement location for mapping. The user enters \<A\> at the prompt and must specify an output device on which to print the report. The user shall not be allowed to run the report to the screen.

Example: Selecting All Dispensing/Procurement Locations

Select the dispensing/procurement location: A

Select Device: PRINTER ONE

REQUESTED TIME TO RUN: NOW // (SEP 22, [2003@21:15](mailto:2003@21:15)) *\<default to NOW\>*

Mapping AR/WS AOUs…

  
STEP 3: Select an AOU for Mapping

To select an AOU for mapping, the user may enter a ? at the prompt and press \<Enter\>, which will display a list from which to choose for the selected location. In the example below, two locations are not mapped. The remaining locations are mapped either to a Division (Div) or to an Outpatient Site (OP).

Example: Results of Entering a “?” at the Prompt

Select PBM AR/WS AOU MAPPINGS: ?

Answer with PBM AR/WS AOU MAPPINGS

Choose from:

1SE NURSING HOME CARE UNIT

1SOUTH PYXIS UNIT OP: CORONA CBOC

1SW PYXIS UNIT

2ND FLOOR DENTAL X 3127 Div: JERRY L PETTIS VAMC

2NE M.H. CLINIC Div: JERRY L PETTIS VAMC

3NW ORTHO POD 2338 Div: JERRY L PETTIS VAMC

CHF CLINIC 3NE Div: JERRY L PETTIS VAMC

DIABETES CARE INPATIENT Div: JERRY L PETTIS VAMC

Example: Selecting an AOU for Mapping

You may enter a new PBM AR/WS AOU MAPPINGS, if you wish

Answer with PHARMACY AOU STOCK AREA OF USE (AOU)

Do you want the entire 122-Entry PHARMACY AOU STOCK List? N (No)

Select PBM AR/WS AOU MAPPINGS: 1SW PYXIS UNIT

...OK? Yes// (Yes) \<Enter\>

AR/WS AOU: 1SW PYXIS UNIT

STEP 4: Selecting an Outpatient Site or a Division

The user may map an AOU to either a Medical Center Division or to an Outpatient Site. If a location is mapped to a Medical Center Division, the user shall not be prompted to enter an Outpatient Site and vice versa. To map to an Outpatient Site, the Medical Center Division mapping must be deleted.

Mapping to an Outpatient Site

Once the AOU has been selected for mapping, the user bypasses the “DIVISION:” prompt by pressing \<Enter\> and selects a location at the “OUTPATIENT SITE:” prompt. If a ? is entered at the prompt, help text will provide a list of sites from which to choose.

  
Example: Results of Entering \<?\> at the “OUTPATIENT SITE:” Prompt

AR/WS AOU : 1SW PYXIS UNIT//

DIVISION: \<Enter\>

OUTPATIENT SITE: ?

An AR/WS AOU CANNOT be mapped to BOTH a division and an outpatient site

Answer with OUTPATIENT SITE NAME, or SITE NUMBER, or

RELATED INSTITUTION

Choose from:

CMO-LOMA LINDA 605M

CORONA CBOC 605GD

LOMA LINDA VA 605

PALM DESERT CBOC 605GC

PASS MEDS 605P

STATE HOME 605DT

SUN CITY CBOC 605GB

UPLAND CBOC 605GE

VICTORVILLE-CBOC 605GA

The user may select an Outpatient Site by typing a portion of the location name or the number designation assigned to that location at the “OUTPATIENT SITE:” prompt and pressing \<Enter\>. In the following example, the user typed COR at the prompt, which selected the CORONA CBOC 605GD Outpatient Site.

Example: Entering a Partial Location Name to Select the Outpatient Site

OUTPATIENT SITE: COR \<Enter\>

OUTPATIENT SITE: CORONA CBOC 605GD

Once the mapping is complete, the user will receive an AR/WS MailMan message from each of the mapped sites.

Mapping to a Division

The process to map to a Division is the same as outlined above, except the user will respond to the “Division:” prompt, which was bypassed in the previous examples.

If the user chooses to delete the division value and not enter a new one, the user shall be prompted to enter an Outpatient Site.

Example: Deleting a Division Without Entering a New One

Select AOU: 4AS DIV: GLRISC *\<If a location has been already mapped, the division or outpatient site, preceded by a “DIV’ or ‘OP’ respectively shall be displayed when the location is selected.*

DIVISION: GLRISC// @

SURE YOU WANT TO DELETE? Yes

DIVISION: \<Enter\>

OUTPATIENT SITE: SUPPORT

If the user does not make a selection, the next type of location shall be presented for mapping.

Example: Making No Selection

Select AOU: \<Enter\>

If any dispensing/procurement location is inactive, that information and the date of inactivation shall be displayed to the user.

Example: Displaying Inactive Dispensing/Procurement Location

Mapping CS NAOUs…

Select NAOU: MASTER VAULT \*\*Inactive\*\*

If the Outpatient Site is inactive, that information and the date of inactivation shall be displayed to the user.

Example: Displaying Inactive Outpatient Site

OUTPATIENT SITE: HINES ISC \*\*Inactive\*\*

If the user does not make a selection, the user shall be exited from the option.

Example: User Exiting From the Option

Select NAOU: \<Enter\>

Mapping DA Pharmacy locations…

Select Pharmacy location: INPATIENT DIV: GLRISC

DIVISION: GLRISC// \<Enter\>

Select Pharmacy location: \<Enter\>

### Mapped/Unmapped Location Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mapped/Unmapped Location Report lists all AR/WS, AOUs, CS NAOUs, and DA Pharmacy Locations that are mapped or not mapped to a Medical Center Division or Outpatient Site.

The following information shall be provided:

- Name of Location
- Medical Center Division/Outpatient Site
- Inactivation Date

  
Example: Mapped/Unmapped Location Report

Mapped/Unmapped Location Report PAGE 1

<u>AR/WS AOU</u>

<u>NAME</u> <u>DIVISION/OUTPATIENT SITE</u> <u>INACTIVE DATE</u>

2AS DIV: GLRISC

4AS Jan 15, 2003

6AS DIV: GLRISC

ER OP: SUPPORT

<u>CS NAOU</u>

ANESTHESIA DIV: GLRISC

<u>DA PHARMACY LOCATION</u>

OUTPATIENT PHARMACY DIV: GLRISC

INPATIENT PHARMACY DIV: GLRISC Jun 18, 1998

# MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how the data is extracted and formatted into the MailMan messages. The MailMan messages are sent in an up-arrow (^) delimited format. Messages begin and end a dispensing record with a single up-arrow (^). When the package is extracting the data, a check is done on each free text field to see if an up-arrow is part of the text. If an up-arrow is discovered in the text, it will be converted to an apostrophe (').

The subject of each message is composed for easier data manipulation and will look like the following:

Example: Subject of MailMan Message

Subj: V. 4.0 PBMIV 29810 1/3 499B4 GLRISC \[message number\], etc., etc.,

- V. 4.0 Indicates that this data is from PBM V. 4.0.
- PBM PBM represents Pharmacy Benefits Management. The next two letters attached represent the package from which the data was extracted.
- IV – Pharmacy Patient IV Module
- UD – Pharmacy Patient Unit Dose Module
- AR – Automatic Replenishment/Ward Stock Module
- OP – Prescription Module
- PR – Procurement Module
- CS – Controlled Substances Module
- PD – Patient Demographics Module
- OV – Outpatient Visits Module
- PTF – Inpatient PTF Records Module
- PRO – Provider Information Module
- AA – Allergies/Adverse Events
- VI – Vitals/Immunizations Information Module
- LR – Laboratory Module
- 29810 The date of the reporting period, in this example October 1998.
- 1/3 “1” represents the message number and “3” represents the total number of messages sent from this facility for this particular module. In this example, the header would indicate the first message of a total of 3 messages generated for the IV module.
- 499B4 The station number with suffix (broken down to the outpatient clinic or the inpatient division).
- GLRISC The name of the facility/outpatient clinic/division.

When the data is being formatted into MailMan messages, additional lines will be added for records exceeding 235 characters. The first character of each additional line will be an asterisk (\*). A record will never be broken within a data piece. If a conversion of MailMan messages is being performed on a PC in a language such as FoxPro, ProComm, Keaterm, etc., the asterisk at the beginning of a line will inform the user that this line and the previous line should be concatenated together, thus validating the definitions of the delimited fields explained later in this document.

A confirmation message will be generated whenever the program extracts data to be transmitted to the PBM section <span class="mark">REDACTED</span> for addition to the national database. Only those packages with requested data to be extracted will be listed. If no data is found for a package, the confirmation will list the module with “0” lines extracted and “1” message transmitted. A MailMan message will be generated if the extract program did not find any data for a specific module.

Example confirmation messages are provided in the MailMan Messages section of this manual.

If the *Automatic Pharmacy Statistics* option or *Manual Pharmacy Statistics* option complete successfully, a PBM Timing report is generated. This report displays the start and stop date/time of each extract and a final calculation of how long it took to run. Examples are provided in the MailMan Messages section of this document.

![](benefits-management-version-4-user-manual/008.png)Note: Extract times will vary depending on the system performance, the time extract is run (early in the morning or on a weekend versus in the middle of the day), and the amount of data extracted.

## IV Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New data elements have been added to the IV extract to support AMIS reporting.

![](benefits-management-version-4-user-manual/009.png)Note: When the IV extract is run, the Patient Demographic Summary Report and Lab reports are automatically generated.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications for an IV Parent record are defined in the table below.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>IV STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong>DATA ELEMENT</strong></th>
<th><strong>FILE #</strong></th>
<th><strong>FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender</td>
<td>Medical Center Division file (#40.8)</td>
<td>Facility Number<br />
field (#1)</td>
<td>2</td>
<td>Facility number and suffix</td>
</tr>
<tr class="even">
<td>Start Date of Order</td>
<td>IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td>Start Date/time field (#.02)</td>
<td>3</td>
<td></td>
</tr>
<tr class="odd">
<td>IV Order #</td>
<td>IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td>Order Number field (#.01)</td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>Order Indicator</td>
<td>N/A</td>
<td>N/A</td>
<td>5</td>
<td>“P” is sent for the Parent order, because multiple records will be sent for each IV additive and solution.</td>
</tr>
<tr class="odd">
<td>IV Type</td>
<td>IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td>Type sub-field (#.04)</td>
<td>6</td>
<td>“A” for Admixture<br />
“P” for Piggyback<br />
“H” for Hyperal<br />
“S” for Syringe<br />
“C” for Chemotherapy</td>
</tr>
<tr class="even">
<td>Outpatient IV</td>
<td>IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td>Ward sub-field (#104)</td>
<td>7</td>
<td>If value is .5, “Y” is sent for Yes ; otherwise “N” for No.</td>
</tr>
<tr class="odd">
<td>Patient SSN</td>
<td>Patient file (#2)</td>
<td><p>Social Security</p>
<p>Number field (#.09)</p></td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>Dosing Instructions<br />
(schedule or<br />
infusion rate)</td>
<td>IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td>Schedule sub-field (#.09) or Infusion rate sub-field (#.08)</td>
<td>9</td>
<td>Which data field is extracted depends on IV type.</td>
</tr>
<tr class="odd">
<td>Provider ID (SSN)</td>
<td>New Person file (#200)</td>
<td>SSN field (#9)</td>
<td>10</td>
<td></td>
</tr>
<tr class="even">
<td>Net Dispensing Occurrences</td>
<td>Label Tracking multiple (#111) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Action sub-field (#2)</p>
<p>Daily usage sub-field (#6)</p></td>
<td>11</td>
<td><p>The following formula is used to calculate dispensing occurrences:</p>
<p>Dispensing occurrences = Dispensed<sup>1</sup>- Returned (recycled) - Cancelled</p>
<p>If a label tracking record has an action of “1” for dispensed and has Daily usage set to “Yes”, the value will be included in the Dispensed<sup>1</sup>count.</p></td>
</tr>
<tr class="odd">
<td>VA Product Name</td>
<td>Drug file (#50)</td>
<td>VA Product Name field (#21)</td>
<td>12</td>
<td></td>
</tr>
<tr class="even">
<td>VA Drug Class</td>
<td>Drug file (#50)</td>
<td>VA Classification field (#2)</td>
<td>13</td>
<td></td>
</tr>
<tr class="odd">
<td>NDC</td>
<td>Drug file (#50)</td>
<td>NDC field (#31)</td>
<td>14</td>
<td></td>
</tr>
<tr class="even">
<td>Formulary/Non-Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>LOCAL NON-FORMULARY field (#51)</td>
<td>15</td>
<td>If field is set to “1”, the program sends “N/F”.</td>
</tr>
<tr class="odd">
<td>National Formulary Indicator</td>
<td>VA Product file (#50.68)</td>
<td>#17 National Formulary Indicator</td>
<td>16</td>
<td>Send “1” for Yes; “0” for No; otherwise null if no data found.</td>
</tr>
<tr class="even">
<td>National Formulary Restriction</td>
<td>national formulary restriction multiple (#18) within the VA Product file (#50.68)</td>
<td>National Formulary Restriction sub-field (#.01)</td>
<td>17</td>
<td>If data is found, send “1”; otherwise “0”.</td>
</tr>
<tr class="odd">
<td>IV Additive or Solution Print Name</td>
<td><p>IV Additive file (#52.6)</p>
<p>IV SolutionS file (#52.7)</p></td>
<td><p>Print Name field (#.01)</p>
<p>Print Name field (#.01)</p></td>
<td>18</td>
<td></td>
</tr>
<tr class="even">
<td>IV Additive or Solution Indicator</td>
<td>N/A</td>
<td>N/A</td>
<td>19</td>
<td><p>If the record contains an additive, program sends “A”;</p>
<p>If solution, sends “S”.</p></td>
</tr>
<tr class="odd">
<td>Generic Drug Name</td>
<td>Drug file (#50)</td>
<td>Generic name field (#.01)</td>
<td>20</td>
<td></td>
</tr>
<tr class="even">
<td>Drug Unit</td>
<td>IV Additive file (#52.6) (for additive)</td>
<td>Drug Unit field (#2)</td>
<td>21</td>
<td><p>gm, mg, ml, etc.</p>
<p>(ml is always sent for a solution)</p></td>
</tr>
<tr class="odd">
<td>Drug Cost Per Unit</td>
<td><p>IV Additive file (#52.6)</p>
<p>IV SolutionS file (#52.7)</p></td>
<td><p>Average drug cost per unit field (#7)</p>
<p>Average drug cost field (#7)</p></td>
<td>22</td>
<td></td>
</tr>
<tr class="even">
<td>Total Net Units Dispensed</td>
<td>IV additive multiple (#1) or IV SolutionS multiple (#3) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Strength sub-field (#.02) (truncate units)</p>
<p>or</p>
<p>Volume sub-field (#1) (truncate “ML”)</p></td>
<td>23</td>
<td>Dispensing Occurrences * Strength or Volume</td>
</tr>
<tr class="odd">
<td>VISN Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>VISN Non-Formulary field (#52)</td>
<td>24</td>
<td>If “1” is found, send “N/F”, otherwise null if no data is found.</td>
</tr>
<tr class="even">
<td>DEA Special Handling</td>
<td>Drug file (#50)</td>
<td>DEA, Special Hdlg field (#3)</td>
<td>25</td>
<td></td>
</tr>
<tr class="odd">
<td>Patient ICN</td>
<td>PATIENT file (#2)</td>
<td><p>INTEGRATION CONTROL NUMBER field</p>
<p>(# 991.01)</p>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
<p>(Values in both fields are concatenated with a “V”.)</p></td>
<td>26</td>
<td><p>Free Text</p>
<p>Example: “1010185893V199552”</p>
<p>If an ICN does not exist, send null.</p></td>
</tr>
<tr class="even">
<td>Provider Local IEN</td>
<td>New Person file (#200)</td>
<td>Internal Entry Number (IEN)</td>
<td>27</td>
<td></td>
</tr>
<tr class="odd">
<td>Stop Date/Time of Order</td>
<td>IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td>STOP DATE/TIME sub-field (#.03)</td>
<td>28</td>
<td></td>
</tr>
<tr class="even">
<td># of IV Bag/Syringes Dispensed</td>
<td>Label Tracking multiple (#111) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Action sub-field (#2)</p>
<p>Daily usage sub-field (#6)</p></td>
<td>29</td>
<td><p>If the DAILY USAGE is set to “Yes” and the ACTION is set to “Dispensed”, the number of LABELS (1 label = 1 bag/syringe) shall be counted.</p>
<p>If there are no LABELS with the ACTION of “Dispensed” to be counted for the reporting period, a value of “0” shall be transmitted.</p></td>
</tr>
<tr class="odd">
<td># of IV Bag/Syringes Recycled</td>
<td>Label Tracking multiple (#111) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Action sub-field (#2)</p>
<p>Daily usage sub-field (#6)</p></td>
<td>30</td>
<td><p>If the DAILY USAGE is set to “Yes” and the ACTION is set to “Recycled”, the number of LABELS (1 label = 1 bag/syringe) shall be counted.</p>
<p>If there are no LABELS with the ACTION of “Recycled” to be counted for the reporting period, a value of “0” shall be transmitted.</p></td>
</tr>
<tr class="even">
<td># of IV Bag/Syringes Destroyed</td>
<td>Label Tracking multiple (#111) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Action sub-field (#2)</p>
<p>Daily usage sub-field (#6)</p></td>
<td>31</td>
<td><p>If the DAILY USAGE is set to “Yes” and the ACTION is set to “Destroyed”, the number of LABELS (1 label = 1 bag/syringe) shall be counted.</p>
<p>If there are no LABELS with the ACTION of “Destroyed” to be counted for the reporting period, a value of “0” shall be transmitted.</p></td>
</tr>
<tr class="odd">
<td># of IV Bag/Syringes Cancelled</td>
<td>Label Tracking multiple (#111) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Action sub-field (#2)</p>
<p>Daily usage sub-field (#6)</p></td>
<td>32</td>
<td><p>If the DAILY USAGE is set to “Yes” and the ACTION is set to “Cancelled”, the number of LABELS (1 label = 1 bag/syringe) shall be counted.</p>
<p>If there are no LABELS with the ACTION of “Cancelled” to be counted for the reporting period, a value of “0” shall be transmitted.</p></td>
</tr>
<tr class="even">
<td>Total Units Dispensed</td>
<td>IV additive multiple (#1) or IV SolutionS multiple (#3) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Strength sub-field (#.02) (truncate units)</p>
<p>or</p>
<p>Volume sub-field (#1) (truncate “ML”)</p></td>
<td>33</td>
<td># of IV dispensed * Strength or Volume</td>
</tr>
<tr class="odd">
<td>Total Units Recycled</td>
<td>IV additive multiple (#1) or IV SolutionS multiple (#3) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Strength sub-field (#.02) (truncate units)</p>
<p>or</p>
<p>Volume sub-field (#1) (truncate “ML”)</p></td>
<td>34</td>
<td># of IV recycled * Strength or Volume</td>
</tr>
<tr class="even">
<td>Total Units Destroyed</td>
<td>IV additive multiple (#1) or IV SolutionS multiple (#3) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Strength sub-field (#.02) (truncate units)</p>
<p>or</p>
<p>Volume sub-field (#1) (truncate “ML”)</p></td>
<td>35</td>
<td># of IV destroyed * Strength or Volume</td>
</tr>
<tr class="odd">
<td>Total Units Cancelled</td>
<td>IV additive multiple (#1) or IV SolutionS multiple (#3) within the IV multiple (#100) within the Pharmacy Patient file (#55)</td>
<td><p>Strength sub-field (#.02) (truncate units)</p>
<p>or</p>
<p>Volume sub-field (#1) (truncate “ML”)</p></td>
<td>36</td>
<td># of IV cancelled * Strength or Volume</td>
</tr>
</tbody>
</table>

![](benefits-management-version-4-user-manual/010.png)Note: Pieces 12-25 and 33-36 in the table refer to a specific IV additive or solution. Pieces 2 through 11 and 26 through 28 shall repeat with each distinct IV additive/solution with the exception of the following:

- Order Indicator
- IV Type
- Outpatient IV
- Net Dispensing Occurrences

The four data elements above shall only be sent with the parent record.  
The data elements for subsequent IV records for each additional IV Additive or IV solution shall be sent in the following order for the MailMan message.

> Up-arrow(^)

> <u>Title</u> <u>Piece Number</u>

> Sender (facility number + suffix) 2

> Start Date of Order 3

> IV Order \# 4

> NO DATA 5

> NO DATA 6

> NO DATA 7

> Patient SSN 8

> Dosing Instructions (schedule or infusion rate) 9

> Provider ID (SSN) 10

> NO DATA 11

> VA Product Name 12

> VA Drug Class 13

> NDC 14

> Formulary/Non-Formulary Indicator 15

> National Formulary Indicator 16

> National Formulary Restriction 17

> IV Additive or Solution Print Name 18

> IV Additive or Solution Indicator 19

> Generic Drug Name 20

> Drug Unit (gm, mg, ml, etc.) 21

> Drug Cost per Unit 22

> Total Units Dispensed 23

> VISN Formulary Indicator 24

> DEA Special Handling 25

> Patient ICN 26

> Provider Local IEN 27

> Stop Date/Time of Order 28

> NO DATA 29

> NO DATA 30

> NO DATA 31

> NO DATA 32

> Units Dispensed 33

> Units Recycled 34

> Units Destroyed 35

> Units Cancelled 36

Within the IV extract, the ACTION sub-field (#2), DATE sub-field (#1), LABELS sub-field (#4) and DAILY USAGE sub-field (#6) within the LABEL TRACKING multiple (#111) within the IV multiple (#100) in the PHARMACY PATIENT file (#55) shall be used to determine what was dispensed, recycled, destroyed or canceled. If there is no dispensing activity for an IV order within the reporting period , that IV record is not extracted. This existing requirement shall not change.

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format. The following is an example of the first (parent) data record sent for an IV order. Each IV additive and solution within an order will be sent as a separate data record.

Example: IV – Detail Report Message

Subj: V. 4.0 PBMIV 30109 1/1 605 JERRY L PETTIS VAMC \[#10684\]

11/16/04@19:00 7132 lines

From: PBMPHARMACIST,FOUR In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^3010901^120^P^A^N^000006404^11 ml/hr^000002705^1^RANITIDINE HCL 25MG/ML IN

J^GA301^00173-0363-39^^1^0^RANITIDINE (ZANTAC)^A^RANITIDINE HCL 25MG/ML INJ 10M

L VI^MG^.0362^150^^6^1002929700V843567^13868^3010901^1^0^0^0^150^0^0^0^

^605^3010901^120^^^^000006404^11 ml/hr^000002705^^SODIUM CHLORIDE 0.9% INJ^TN10

2^00264-1400-20^^1^0^0.9% NACL^S^SODIUM CHLORIDE 0.9% INJ 250ML^ML^0^250^^6^100

2929700V843567^^3010901^^^^^250^0^0^0^

^605^3010831^7^P^P^N^000007287^Q24H^000002224^1^CEFTRIAXONE NA 1GM/VIL INJ^AM10

3^00004-1964-01^^1^0^CEFTRIAXONE SOD INJ^A^CEFTRIAXONE SOD 1GM INJ VI^GM^19.01^

2^^6RO^1002931500V483685^11247^3010901^1^0^0^0^2^0^0^0^

^605^3010831^7^^^^000007287^Q24H^000002224^^SODIUM CHLORIDE 0.9% INJ^TN102^0033

8-0049-18^^1^0^0.9% NACL^S^SODIUM CHLORIDE 0.9% INJ 100ML^ML^0^100^^6^100293150

0V483685^^3010901^^^^^100^0^0^0^

^605^3010831^124^P^P^Y^000003563^Q48H^000004287^1^GENTAMICIN SO4 40MG/ML INJ^AM

300^63323-0010-20^^1^0^GENTAMICIN^A^GENTAMICIN SULFATE 40MG/ML INJ^MG^.0015^70^

^6^1001835792V911934^4081^3010901^1^0^0^0^70^0^0^0^

^605^3010831^124^^^^000003563^Q48H^000004287^^SODIUM CHLORIDE 0.9% INJ^TN102^00

338-0049-18^^1^0^0.9% NACL^S^SODIUM CHLORIDE 0.9% INJ 100ML^ML^0^100^^6^1001835

792V911934^^3010901^^^^^100^0^0^0^

Enter RETURN to continue or '^' to exit:

Subj: V. 4.0 PBMIV 30109 1/1 605 JERRY L PETTIS VAMC \[#10684\] Page 2

-------------------------------------------------------------------------------

^605^3010831^21^P^P^N^000002676^QD^000003129^1^LEVOFLOXACIN 25MG/ML INJ^AM900^0

0045-0068-01^^0^0^LEVOFLOXACIN^A^LEVOFLOXACIN 25MG/ML INJ^MG^.038^500^^6^100293

1930V108442^11037^3010901^1^0^0^0^500^0^0^0^

^605^3010831^21^^^^000002676^QD^000003129^^DEXTROSE 5% INJ^TN101^00338-0017-18^

^1^0^D5W^S^DEXTROSE 5% IN WATER 100ML INJ^ML^0^100^^6^1002931930V108442^^301090

1^^^^^100^0^0^0^

^605^3010901^16^P^A^N^000004708^62 ml/hr^000001783^1^MAGNESIUM SO4 4MEQ/ML INJ^

TN406^00517-2602-25^^1^0^MAGNESIUM SULFATE^A^MAGNESIUM SULFATE 50% INJ 2ML^MEQ^

.18^16^^6^1002194529V799884^9883^3010901^1^0^0^0^16^0^0^0^

^605^3010901^16^^^^000004708^62 ml/hr^000001783^^SODIUM CHLORIDE 0.9% INJ^TN102

^00264-1400-20^^1^0^0.9% NACL^S^SODIUM CHLORIDE 0.9% INJ 250ML^ML^0^250^^6^1002

194529V799884^^3010901^^^^^250^0^0^0^

^605^3010901^4^P^P^N^000007971^A24H^000008484^1^LEVOFLOXACIN 25MG/ML INJ^AM900^

00045-0068-01^^0^0^LEVOFLOXACIN^A^LEVOFLOXACIN 25MG/ML INJ^MG^.038^500^^6^10029

74553V713729^13892^3010901^1^0^0^0^500^0^0^0^

^605^3010901^4^^^^000007971^A24H^000008484^^DEXTROSE 5% INJ^TN101^00338-0017-18

^^1^0^D5W^S^DEXTROSE 5% IN WATER 100ML INJ^ML^0^100^^6^1002974553V713729^^30109

01^^^^^100^0^0^0^

^605^3010901^5^P^P^N^000007971^A24H^000008484^1^LEVOFLOXACIN 25MG/ML INJ^AM900^

00045-0068-01^^0^0^LEVOFLOXACIN^A^LEVOFLOXACIN 25MG/ML INJ^MG^.038^500^^6^10029

  
Example: IV - Statistical Data Message

Subj: V. 4.0 PBMIV 30109 605 JERRY L PETTIS VAMC \[#7569\] 07/16/04@14:39

139 lines

From: PBMPHARMACIST,FIVE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

IV Statistical Data for SEP 1,2001 through SEP 30,2001

Drug Total Number

Drug Name Strength Dispensed of bags

------------------------------------------------------------------------------

ACYCLOVIR NA 500MG/VI INJ MG 5600.00 7

ALBUMIN HUMAN 25% USP 50ML VI ML 350.00 4

ALEMTUZUMAB 10MG INJ \*# MG 220.00 8

ALPHA 1-PROTEINASE INHIBITOR(HUMAN) \*# MG 47319.00 9

ALTEPLASE RECOMBINANT 50MG INJ W/DIL VI MG 252.00 25

AMIKACIN SULFATE 250MG/ML INJ MG 30250.00 35

AMINO ACID III 10% 1000ML ML 258930.00 267

AMINOCAPROIC ACID 250MG/ML INJ 20ML VI MG 84000.00 14

AMIODARONE HCL 50MG/ML, 3ML AMP MG 900.00 2

AMPHOTERICIN B 50MG INJ VI MG 1675.00 35

AMPHOTERICIN B LIPOSOME 50MG INJ \*# MG 8100.00 18

AMPICILLIN NA 1GM/VI INJ GM 2704.50 210

AMPICILLIN NA/SULBACTAM NA 1.5GM/VI INJ GM 1105.50 375

Subj: V. 4.0 PBMIV 30109 605 JERRY L PETTIS VAMC \[#7569\] Page 2

-------------------------------------------------------------------------------

AMPICILLIN NA/SULBACTAM NA 3GM/VI INJ GM 123.00 41

CALCIUM GLUCONATE 10% INJ 100ML VI MEQ 2861.00 267

CALCIUM GLUCONATE 10% INJ 10ML VI MEQ 144.15 22

CARBOPLATIN 150MG INJ VI MG 5250.00 13

CEFAZOLIN NA 1GM/VI INJ GM 1520.50 1152

CEFOTAXIME 1GM INJ VI GM 48.00 24

CEFOTETAN DISODIUM 1GM INJ VI GM 208.00 126

CEFOTETAN DISODIUM 2GM INJ VI GM 7.00 7

CEFTAZIDIME 1GM INJ VI GM 601.00 335

CEFTRIAXONE SOD 1GM INJ VI GM 336.00 209

CEFTRIAXONE SOD 2GM INJ VI GM 8.00 4

CIMETIDINE 300MG/2ML INJ VI MG 26300.00 36

CIPROFLOXACIN 10MG/ML INJ 40ML VI MG 52265.00 162

CLADRIBINE 1MG/ML INJ 10ML MG 30.00 3

CLINDAMYCIN PHOS 600MG/4ML INJ AMP MG 419800.00 533

CO-TRIMOXAZOLE 10ML INJ (SEPTRA INJ) ML 21.80 1

CYCLOPHOSPHAMIDE 500MG INJ VI MG 7400.00 11

DACARBAZINE 200MG INJ VI MG 1700.00 1

DAKINS SOLN MODIFIED HALF STRENGTH \* ML 1000.00 1

DESMOPRESSIN ACE 4MCG/ML INJ 1ML AMP MCG 330.00 2

  
Example: IV –Patient Demographic Summary Report Message

Subj: V. 4.0 PBMPD 30109 605 JERRY L PETTIS VAMC \[#7570\] 07/16/04@14:39

18 lines

From: PBMPHARMACIST,FIVE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

PHARMACY INPATIENT (IV) UNIQUE PATIENTS REPORT JUL 16, 2004

-------------------------------------------------------------------------------

SEP 01, 2001 through SEP 30, 2001

===============================================================================

UNIQUE

---------------------------------------------------------------------

Total unique Inpatients across all divisions: 330

Total unique Outpatients across all divisions: 169

---------------------------------------------------------------------

JERRY L PETTIS VAMC Division: 451

------------

Total of all Divisions: 451

\* This report includes Outpatients receiving IV orders.

\*\*PLEASE NOTE: Final TOTAL may not match sum of all SUBTOTALS. A patient may

have been provided pharmacy services at more than one outpatient and/or inpatient division.

Example: IV – AMIS Summary Report Message

Subj: V.4.0 PBMIV 30109 605 JERRY L PETTIS VAMC \[#7571\] 07/16/04@14:39

62 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

------------------------------------------------------------------------------

IV AMIS Summary for SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

NET Cost/

LVPs LVPs LVPs LVPs LVPs Total NET LVPs

Division DISP RET DES CAN DISP Cost DISP

------------------------------------------------------------------------------

JERRY L PETTIS VA 884 0 0 0 883 \$ 417.05 \$ .47

------------------------------------------------------------------------------

Total 884 0 0 0 883 \$ 417.05 \$ .47

NET Cost/

IVPBs IVPBs IVPBs IVPBs IVPBs Total NET IVPBs

Division DISP RET DES CAN DISP Cost DISP

------------------------------------------------------------------------------

> *\[A portion of this statistical data message has been removed to save space.\]*

Subj: V.4.0 PBMIV 30109 605 JERRY L PETTIS VAMC \[#7571\] Page 3

------------------------------------------------------------------------------

NET Cost/

CHEMO CHEMO CHEMO CHEMO CHEMO Total NET CHEMOs

Division DISP RET DES CAN DISP Cost DISP

------------------------------------------------------------------------------

JERRY L PETTIS VA 145 0 0 0 141 \$ 1019.50 \$ 7.23

------------------------------------------------------------------------------

Total 145 0 0 0 141 \$ 1019.5 \$ 7.23

NET Cost/

SYRs SYRs SYRs SYRs SYRs Total NET SYRs

Division DISP RET DES CAN DISP Cost DISP

------------------------------------------------------------------------------

JERRY L PETTIS VA 98 0 0 0 98 \$ 454.79 \$ 4.64

------------------------------------------------------------------------------

Total 98 0 0 0 98 \$ 454.79 \$ 4.64

  
Example: IV – Detail Report Message

Subj: V. 4.0 PBMLR 30109 1/1 605 JERRY L PETTIS VAMC \[#7572\]

07/16/04@14:39 279 lines

From: PBMPHARMACIST,FIVE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^000008748^23^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^1.6 MG/DL^H^3

010831.06^

^605^000006697^27^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^1.0 MG/DL^^30

10831.043024^

^605^000002156^48^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^1.4 MG/DL^^30

10830.123015^

^605^000003488^1^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^1.1 MG/DL^^301

0831.060001^

^605^000009400^71^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^0.9 MG/DL^^30

10828.060001^

^605^000006550^47^^^ENALAPRILAT 1.25MG/ML 2ML VI^CREATININE^1.3 MG/DL^^3010831.

06^

^605^000006550^47^^^ENALAPRILAT 1.25MG/ML 2ML VI^POTASSIUM^4.5 mmol/L^^3010831.

06^

^605^000006594^14^^^CIMETIDINE 300MG/2ML INJ VI^CREATININE^1.3 MG/DL^^3010831.2

03326^

^605^000006759^5^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^1.0 MG/DL^^301

0831.231723^

Subj: V. 4.0 PBMLR 30109 1/1 605 JERRY L PETTIS VAMC \[#7572\] Page 2

-------------------------------------------------------------------------------

^605^000006404^120^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^6.8 MG/DL^H^

3010831.102428^

^605^000006404^121^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^6.8 MG/DL^H^

3010831.102428^

^605^000006550^49^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^1.3 MG/DL^^30

10831.06^

^605^000007725^30^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^1.3 MG/DL^^30

10831.04103^

^605^000007278^46^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^0.8 MG/DL^^30

10830.06^

^605^000006404^122^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^6.8 MG/DL^H^

3010831.102428^

^605^000006404^124^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^6.8 MG/DL^H^

3010831.102428^

^605^000005582^123^^^DILTIAZEM HCL 5MG/ML 10ML INJ VI^CREATININE^1.1 MG/DL^^301

0831.04301^

^605^000006404^125^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^6.8 MG/DL^H^

3010831.102428^

^605^000007278^47^^^RANITIDINE HCL 25MG/ML INJ 10ML VI^CREATININE^0.8 MG/DL^^30

10830.06^

Example: IV – Laboratory Statistical Summary Message

Subj: V. 4.0 PBMLR 30109 605 JERRY L PETTIS VAMC \[#7573\] 07/16/04@14:39

6 lines

From: PBMPHARMACIST,FIVE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Laboratory Statistical Summary

SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

Total Patients 45

Total Laboratory Tests 51

  
Example: IV – Laboratory Data Summary Message

Subj: V. 4.0 PBMLR 30109 605 JERRY L PETTIS VAMC \[#7574\] 07/16/04@14:39

57 lines

From: PBMPHARMACIST,FIVE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Laboratory Data Summary

SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

Patient SSN VA CODE Laboratory Results Flag Date/Time Taken

------------------------------------------------------------------------------

000005033 CV200 CREATININE 2.5 MG/DL H 08/31/01 0753

000006461 GA301 CREATININE 0.9 MG/DL 07/23/01 0950

000006759 GA301 CREATININE 1.0 MG/DL 08/31/01 2317

000003536 CV200 CREATININE 6.6 MG/DL H 08/10/01 1041

000005913 CV200 CREATININE 1.5 MG/DL 07/24/01 1255

000003488 GA301 CREATININE 1.1 MG/DL 08/31/01 0600

000006404 GA301 CREATININE 6.8 MG/DL H 08/31/01 1024

000006072 GA301 CREATININE 1.7 MG/DL H 06/01/01 0917

000001984 GA301 CREATININE 0.9 MG/DL 04/09/01 0600

000002226 CV200 CREATININE 10.7 MG/DL H 08/14/01 1240

000002156 CV200 CREATININE 1.4 MG/DL 08/30/01 1230

GA301 CREATININE 1.4 MG/DL 08/30/01 1230

000006550 CV800 CREATININE 1.3 MG/DL 08/31/01 0600

Subj: V. 4.0 PBMLR 30109 605 JERRY L PETTIS VAMC \[#7574\] Page 2

-------------------------------------------------------------------------------

POTASSIUM 4.5 mmol/L 08/31/01 0600

GA301 CREATININE 1.3 MG/DL 08/31/01 0600

000003573 CV800 CREATININE 1.2 MG/DL 04/06/01 0600

POTASSIUM 4.2 mmol/L 04/06/01 0600

000003573 CV800 CREATININE 0.7 MG/DL 08/31/01 0342

POTASSIUM 4.3 mmol/L 08/31/01 0342

000009400 GA301 CREATININE 0.9 MG/DL 08/28/01 0600

000005687 GA301 CREATININE 0.7 MG/DL 08/27/01 1439

000007278 GA301 CREATININE 0.8 MG/DL 08/30/01 0600

000008805 GA301 CREATININE 0.9 MG/DL 08/30/01 1034

000005079 GA301 CREATININE 1.3 MG/DL 08/27/01 0938

000005582 CV200 CREATININE 1.1 MG/DL 08/31/01 0430

000006697 GA301 CREATININE 1.0 MG/DL 08/31/01 0430

000007437 CV200 CREATININE 1.1 MG/DL 10/23/00 1045

000003245 GA301 CREATININE 1.0 MG/DL 04/25/01 1309

000002486 CV200 CREATININE 1.4 MG/DL 03/26/01 1300

000004381 GA301 CREATININE 15.3 MG/DL 06/05/01 1030

000008266 GA301 CREATININE 0.8 MG/DL 08/29/01 0746

000006642 GA301 CREATININE 1.2 MG/DL 08/31/01 0600

000008748 GA301 CREATININE 1.6 MG/DL H 08/31/01 0600

Example: IV – Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY

\[#7575\] 07/16/04@14:39 7 lines

From: PBMPHARMACIST,FIVE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

IVs JUL 16,2004@14:35 JUL 16,2004@14:39 0 hrs, 4 min

Laboratory Results JUL 16,2004@14:39 JUL 16,2004@14:39 0 hrs, 0 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

  
Example: IV – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI

\[#7576\] 07/16/04@14:39 7 lines

From: PBMPHARMACIST,FIVE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

IVs 6964 1

Laboratory Results 279 1

## UD Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New data elements have been added to the UD extract.

![](benefits-management-version-4-user-manual/011.png)Note: When the UD extract is run, the Patient Demographic Summary Report and Lab reports are automatically generated.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications are defined in more detail in the table below.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>UNIT DOSE STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender</td>
<td>Medical Center Division file (#40.8)</td>
<td>Facility Number field (#1)</td>
<td>2</td>
<td></td>
</tr>
<tr class="even">
<td>Start Date of Order</td>
<td>Unit DoSE multiple (#62) within the Pharmacy Patient file (#55)</td>
<td>Start date/time sub-field (#10)</td>
<td>3</td>
<td></td>
</tr>
<tr class="odd">
<td>Unit Dose Order #</td>
<td>Unit DoSE multiple (#62) within the Pharmacy Patient file (#55)</td>
<td>Order Number sub-field (#.01)</td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>Patient SSN</td>
<td>Patient file (#2)</td>
<td>Social Security Number field (#.09)</td>
<td>5</td>
<td></td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>Unit DoSE multiple (#62) within the Pharmacy Patient file (#55)</td>
<td>Schedule sub-field (#26)</td>
<td>6</td>
<td></td>
</tr>
<tr class="even">
<td>Provider ID (SSN)</td>
<td>New Person file (#200)</td>
<td>SSN field (#9)</td>
<td>7</td>
<td></td>
</tr>
<tr class="odd">
<td>VA Product Name</td>
<td>Drug file (#50)</td>
<td>VA Product Name field (#21)</td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>VA Drug Class</td>
<td>Drug file (#50)</td>
<td>VA Classification field (#2)</td>
<td>9</td>
<td></td>
</tr>
<tr class="odd">
<td>Generic Drug Name</td>
<td>Drug file (#50)</td>
<td>Generic name field (#.01)</td>
<td>10</td>
<td></td>
</tr>
<tr class="even">
<td>NDC</td>
<td>Drug file (#50)</td>
<td>NDC field (#31)</td>
<td>11</td>
<td></td>
</tr>
<tr class="odd">
<td>Formulary/Non-Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>LOCAL Non formulary field (#51)</td>
<td>12</td>
<td>If field set to “1”, the program sends “N/F”</td>
</tr>
<tr class="even">
<td>National Formulary Indicator</td>
<td>VA Product file (#50.68)</td>
<td>National Formulary Indicator field (#17)</td>
<td>13</td>
<td>Send “1” for Yes; “0” for No; otherwise null if no data found.</td>
</tr>
<tr class="odd">
<td>National Formulary Restriction</td>
<td>national formulary restriction multiple (#18) within the VA Product file (#50.68)</td>
<td>National Formulary Restriction sub-field (#.01)</td>
<td>14</td>
<td>If data is found, send “1”; otherwise “0”.</td>
</tr>
<tr class="even">
<td>Units Per Dose</td>
<td><p>Dispense drug multiple (#2) within the</p>
<p>Unit DoSE multiple (#62) within the Pharmacy Patient file (#55)</p></td>
<td>Units Per Dose sub-field (#.02)</td>
<td>15</td>
<td></td>
</tr>
<tr class="odd">
<td>Dispense Unit</td>
<td>Drug file( #50)</td>
<td>Dispense Unit field (#14.5)</td>
<td>16</td>
<td></td>
</tr>
<tr class="even">
<td>Price Per Dispense Unit</td>
<td>Drug file (#50)</td>
<td>Price Per Dispense Unit field (#16)</td>
<td>17</td>
<td></td>
</tr>
<tr class="odd">
<td>Net Dispensed Amount</td>
<td>Dispense Log multiple (#71) within the Unit DoSE multiple (#62) within the Pharmacy Patient file (#55)</td>
<td><p>AmounT sub-field (#.03)</p>
<p>How sub-field (#.05)</p></td>
<td>18</td>
<td>Formula = Units dispensed (pick list, pre exchange, extra units) – Returns</td>
</tr>
<tr class="even">
<td>VISN Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>VISN Non-Formulary field (#52)</td>
<td>19</td>
<td>If “1” is found, send “N/F”, otherwise null if no data is found.</td>
</tr>
<tr class="odd">
<td>DEA, Special Handling</td>
<td>Drug file (#50)</td>
<td>DEA, Special Hdlg field (#3)</td>
<td>20</td>
<td></td>
</tr>
<tr class="even">
<td>Patient ICN</td>
<td>PATIENT file (#2)</td>
<td><p>INTEGRATION CONTROL NUMBER field</p>
<p>(# 991.01)</p>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
<p>(Values in both fields are concatenated with a “V”.)</p></td>
<td>21</td>
<td><p>Free Text.</p>
<p>Example: “1010185893V199552”</p>
<p>If an ICN does not exist, send null.</p></td>
</tr>
<tr class="odd">
<td>Provider Local IEN</td>
<td>New Person file (#200)</td>
<td>Internal Entry Number (IEN)</td>
<td>22</td>
<td></td>
</tr>
<tr class="even">
<td>Stop Date/Time of Order</td>
<td>Unit DoSE multiple (#62) within the Pharmacy Patient file (#55)</td>
<td>Stop date/time sub-field (#34)</td>
<td>23</td>
<td></td>
</tr>
<tr class="odd">
<td>Dispensed Amount</td>
<td>Dispense Log multiple (#71) within the Unit DoSE multiple (#62) within the Pharmacy Patient file (#55)</td>
<td><p>AmounT sub-field (#.03)</p>
<p>How sub-field (#.05)</p></td>
<td>24</td>
<td><p>If the HOW sub-field (#.05) is set to “1” from Pick list, “2” Pre-exchange units, or “3” Extra Units dispensed, the AMOUNT sub-field (#.03) for each dispense drug shall be counted.</p>
<p>The total dispensed amount shall be transmitted. If there is no amount to be counted for the reporting period, a value of “0” shall be transmitted.</p></td>
</tr>
<tr class="even">
<td>Returned Amount</td>
<td>Dispense Log multiple (#71) within the Unit DoSE multiple (#62) within the Pharmacy Patient file (#55)</td>
<td><p>AmounT sub-field (#.03)</p>
<p>How sub-field (#.05)</p></td>
<td>25</td>
<td><p>If the HOW sub-field (#.05) is set to “4” returns, the AMOUNT sub-field (#.03) for each dispense drug shall be counted.</p>
<p>The total returned amount shall be transmitted. If there is no returned amount to be counted for the reporting period, a value of “0” shall be transmitted.</p></td>
</tr>
</tbody>
</table>

![](benefits-management-version-4-user-manual/012.png)Note: Data pieces 2-7 and 21-23 in the table above shall repeat for each unit dose order containing more than one dispense drug. Data pieces 8-20 and 24-25 will hold specific dispense drug information.

Within the UD extract, the DISPENSE DATE/TIME sub-field (#.01), DISPENSE DRUG sub-field (#.02), AMOUNT sub-field (#.03) and HOW sub-field (#.05) within the DISPENSE LOG multiple (#71) within the UNIT DOSE multiple (#62) in the PHARMACY PATIENT file (#55) shall be used to determine what was dispensed or returned. The Unit Dose record, with the current functionality, is not extracted if there is no dispensing activity (nothing dispensed or returned). This requirement shall not change.

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format. The following is an example of a data record sent. Each dispense drug within an order will be sent as a separate data record (pieces 22-45). Pieces 2-20 will repeat for each unit dose order containing more than one dispense drug.

  
Example: Unit Dose – Detail Report Message

Subj: V. 4.0 PBMUD 3010900 1/1 605 JERRY L PETTIS VAMC \[#7680\]

07/19/04@17:04 9942 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^3010901^174068^000003330^ONCE^000002224^INSULIN REG HUMAN 100 U/ML INJ NOV

OLIN R^HS501^INSULIN REG HUMAN 100 U/ML INJ NOVOLIN R^00169-1833-11^^1^0^1^VI^4

.390^1^^9^1002942768^11247^3010901^1^0^

^605^3010901^174069^000002930^ONCE^000002224^INSULIN REG HUMAN 100 U/ML INJ NOV

OLIN R^HS501^INSULIN REG HUMAN 100 U/ML INJ NOVOLIN R^00169-1833-11^^1^0^1^VI^4

.390^1^^9^1002961216^11247^3010901^2^0^

^605^3010817^225^000005243^BID^000009953^BUPROPION HCL 100MG TAB^CN609^BUPROPIO

N HCL 100MG TAB^00173-0178-55^^1^0^1^TAB^0.467^6^^6RO^6050024053^1793^3010901^1

9^0^

^605^3010901^151^000004791^ONCE^000002705^DEXTROSE 50% INJ^HS503^DEXTROSE 50% I

NJ 50ML^00074-4902-34^^0^0^1^SYR^2.032^1^^6^1008234143^13868^3010901^1^0^

^605^3010901^37^000008132^ONCE^000002705^FUROSEMIDE 10MG/ML INJ^CV702^FUROSEMID

E 10MG/ML INJ 10ML AMP^00039-0061-08^^1^1^1^AMP^1.824^1^^6^1002926820^13868^301

0901^1^0^

^605^3010901^85^000000702^ONCE^000008484^MEPERIDINE HCL 50MG/ML INJ^CN101^MEPER

IDINE HCL 50MG/ML INJ TUBEX^00074-1178-31^N/F^1^0^1^TUBEX^0.357^1^N/F^2A^100292

6572^13892^3010901^2^0^

^605^3010901^174070^000001512^QD PRN/DRY-NOSE^000008484^SODIUM CHLORIDE 0.65% S

Subj: V. 4.0 PBMUD 3010900 1/1 605 JERRY L PETTIS VAMC \[#7680\] Page 2

-------------------------------------------------------------------------------

OLN,NASAL^NT900^SODIUM CHLORIDE 0.65% NASAL SOLN^00256-0152-01^^1^0^1^ML^0.058^

1^^9^1002930345^13892^3010901^2^0^

^605^3010901^174071^000005474^Q6H PRN/PAIN^000002705^OXYCODONE HCL 5MG/ACETAMIN

OPHEN 325MG TAB^CN101^OXYCODONE 5MG ACETAMINOP 325MG TAB U/D^00060-0127-65^^1^0

^1^TAB^0.098^1^^2A^1004887216^13868^3010901^1^0^

^605^3010901^24^000003573^ONCE^000002224^LOPERAMIDE HCL 2MG CAP^GA400^LOPERAMID

E HCL 2MG CAP U/D^50458-0400-01^^1^0^2^CAP^0.140^2^^6^1003571292^11247^3010901^

6^0^

^605^3010901^174084^000002876^QD^000002224^ASCORBIC ACID 100MG/ML SOLN^VT400^AS

CORBIC ACID 100MG/ML SOLN^00074-3492-01^^1^0^1^ML^0.166^1^^9^1002933134^11247^3

010901^1^0^

^605^3010901^68^000002909^Q8H PRN^000009953^NIFEDIPINE 10MG CAP^CV200^NIFEDIPIN

E 10MG CAP U/D^00069-2600-41^^1^1^1^CAP^0.430^2^^6R^1002928869^1793^3010901^2^0

^

^605^3010901^174073^000007715^HSPRN INSOMNIA^000009621^TEMAZEPAM 15MG CAP^CN302

^TEMAZEPAM 15MG CAP U/D^51079-0418-20^^1^0^1^CAP^0.064^1^^4^1002937819^13860^30

10901^1^0^

^605^3010901^27^000003703^ONCE^000005115^POTASSIUM CHLORIDE 10MEQ TAB,SA^TN403^

POTASSIUM CHLORIDE 10MEQ SA TAB^00245-0041-15^^1^0^4^TAB^0.035^4^^6^1002928901^

10910^3010901^16^0^

  
Example: Unit Dose - Statistical Data Message

Subj: V. 4.0 PBMUD 3010900 605 JERRY L PETTIS VAMC \[#7681\]

07/19/04@17:04 691 lines

From: PBMPHARMACIST,SEVEN In 'IN' basket. Page 1

----------------------------------------------------------------------------

Unit Dose Statistical Data for SEP 01, 2001 through SEP 30, 2001

Total Total

Dispensed Dispensed

Drug Name Units Cost

----------------------------------------------------------------------------

ABACAVIR SUL 300MG TAB 57.00 204.23

ABSORBASE TOP OINT 14.00 0.07

ACCU-CHEK COMFORT CV(GLUCOSE) TEST STRIP 12.00 3.98

ACETAMINOP 300MG/COD 30MG/12.5ML ELI U/D 133.00 25.80

ACETAMINOPHEN 300MG/COD 30MG TAB U/D 945.00 153.09

ACETAMINOPHEN 325MG TAB U/D 2181.00 28.35

ACETAMINOPHEN 325MG/10.15ML ELIXIR U/D 2.00 0.27

ACETAMINOPHEN 500MG TAB U/D 134.00 3.89

ACETAMINOPHEN 650MG RTL SUPP 19.00 6.02

ACETAMINOPHEN 650MG/25ML ELIXIR U/D 280.00 37.80

ACETYLCYSTEINE 10% INHL SOLN 1.00 0.18

Subj: V. 4.0 PBMUD 3010900 605 JERRY L PETTIS VAMC \[#7681\] Page 2

----------------------------------------------------------------------------

ACETYLCYSTEINE 20% INHL SOLN 12.00 3.17

ACYCLOVIR 200MG CAP 64.00 3.21

ACYCLOVIR 800MG TAB 9.00 1.19

ALBUTEROL 0.5% INHL SOLN 12.00 3.73

ALBUTEROL 2MG TAB U/D 57.00 5.13

ALBUTEROL 4MG TAB U/D 60.00 8.16

ALBUTEROL 90/IPRATROP 18MCG 200D PO INHL 23.00 460.00

ALBUTEROL 90MCG 200D ORAL INHL 398.00 656.70

ALBUTEROL SO4 0.083% INHL 3ML 55.00 10.69

ALENDRONATE 10MG TAB \# 63.00 65.65

ALENDRONATE 40MG TAB \# 10.00 26.39

ALLOPURINOL 100MG TAB U/D 55.00 1.71

ALLOPURINOL 300MG TAB U/D 61.00 3.36

ALOH/MGOH/SIMTH REG STRENGTH LIQ \* 39.00 17.16

ALOH/MGOH/SIMTH XTRA STRENGTH LIQ 43.00 19.01

ALPRAZOLAM 0.5MG TAB U/D 39.00 1.83

ALPRAZOLAM 1MG TAB U/D 7.00 0.46

AMANTADINE HCL 100MG CAP U/D 22.00 3.06

AMINOCAPROIC ACID 500MG TAB \# 10.00 11.01

AMIODARONE HCL (CORDARONE) 200MG TAB 197.00 229.31

  
Example: Unit Dose – AMIS Summary Report Message

Subj: V.4.0 PBMUD 3010900 605 JERRY L PETTIS VAMC \[#7682\] 07/19/04@17:04

31 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

---------------------------------------------------------------------------

UD AMIS Summary for SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

NET

DOSES DOSES DOSES TOTAL AVG COST

DIVISION DISP RET DISP COST PER DOSE

---------------------------------------------------------------------------

JERRY L PETTIS VA 444958 0 444958 \$ 397864.51 \$ .89

---------------------------------------------------------------------------

Total 444958 0 444958 \$ 397864.51 \$ .89

Division Specialty Total Patient Days of Care

---------------------------------------------------------------------------

JERRY L PETTIS VAMC PSYCHIATRY 320

INTERMEDIATE -30

MEDICINE 1664

NEUROLOGY 53

REHAB MEDICINE 0

Subj: V.4.0 PBMUD 3010900 605 JERRY L PETTIS VAMC \[#7682\] Page 2

---------------------------------------------------------------------------

SURGERY 961

VA NURSING HOME 2974

---------------------------------------------------------------------------

JERRY L PETTIS VAMC Total 5942

---------------------------------------------------------------------------

Grand Total 5942

Example: Unit Dose –Patient Demographic Summary Report Message

Subj: V. 4.0 PBMPD 30109 605 JERRY L PETTIS VAMC \[#7683\] 07/19/04@17:06

15 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

--------------------------------------------------------------------------

PHARMACY INPATIENT (UD) UNIQUE PATIENTS REPORT JUL 19, 2004

--------------------------------------------------------------------------

SEP 01, 2001 through SEP 30, 2001

==========================================================================

UNIQUE

---------------------------------------------------------------------

TOTAL patients across all divisions: 637

---------------------------------------------------------------------

JERRY L PETTIS VAMC Division: 637

----------

Inpatient Total of all Divisions: 637

\*\*PLEASE NOTE: Final TOTAL may not match sum of all SUBTOTALS. A patient may

have been provided pharmacy services at more than one outpatient and/or

inpatient division.

Example: Unit Dose – Detail Report Message

Subj: V. 4.0 PBMLR 30109 1/1 605 JERRY L PETTIS VAMC \[#7684\]

07/19/04@17:06 2811 lines

From: PBMPHARMACIST,SEVEN In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^000004791^^121^^GLYBURIDE 5MG TAB^GLUCOSE^48 MG/DL^L^3010830.13^

^605^000004791^^121^^GLYBURIDE 5MG TAB^SGOT (AST)^37 IU/L^^3010830.13^

^605^000004791^^121^^GLYBURIDE 5MG TAB^HEMOGLOBIN A1C (LAB)^8.9 % ^H^3010724.13

^

^605^000004791^^121^^GLYBURIDE 5MG TAB^SGPT (ALT)^61 IU/L^^3010830.13^

^605^000004791^^122^^GLYBURIDE 5MG TAB^GLUCOSE^48 MG/DL^L^3010830.13^

^605^000004791^^122^^GLYBURIDE 5MG TAB^SGOT (AST)^37 IU/L^^3010830.13^

^605^000004791^^122^^GLYBURIDE 5MG TAB^HEMOGLOBIN A1C (LAB)^8.9 % ^H^3010724.13

^

^605^000004791^^122^^GLYBURIDE 5MG TAB^SGPT (ALT)^61 IU/L^^3010830.13^

^605^000002909^^68^^NIFEDIPINE 10MG CAP U/D^CREATININE^0.9 MG/DL^^3010809.06000

1^

^605^000007287^^50^^NIFEDIPINE 60MG SA TAB^CREATININE^1.9 MG/DL^H^3010831.19000

1^

^605^000005137^^5^^FOSINOPRIL NA 40MG TAB^CREATININE^1.3 MG/DL^^3010831.175508^

^605^000005137^^5^^FOSINOPRIL NA 40MG TAB^POTASSIUM^5.2 mmol/L^H^3010831.175508

^

^605^000005137^^8^^FOSINOPRIL NA 20MG TAB^CREATININE^1.3 MG/DL^^3010831.175508^

Subj: V. 4.0 PBMLR 30109 1/1 605 JERRY L PETTIS VAMC \[#7684\] Page 2

-------------------------------------------------------------------------------

^605^000005137^^8^^FOSINOPRIL NA 20MG TAB^POTASSIUM^5.2 mmol/L^H^3010831.175508

^

^605^000001512^^6^^FELODIPINE 5MG SA TAB^CREATININE^1.0 MG/DL^^3010831.140818^

^605^000001512^^10^^LISINOPRIL 20MG TAB U/D^CREATININE^1.0 MG/DL^^3010831.14081

8^

^605^000001512^^10^^LISINOPRIL 20MG TAB U/D^POTASSIUM^4.1 mmol/L^^3010831.14081

8^

^605^000001512^^12^^SIMVASTATIN 20MG TAB U/D^CHOLESTEROL^152 MG/DL^^3010622.120

715^

^605^000001512^^12^^SIMVASTATIN 20MG TAB U/D^SGOT (AST)^14 IU/L^^3010831.140818

^

^605^000001512^^12^^SIMVASTATIN 20MG TAB U/D^TRIGLYCERIDE^309 MG/DL^H^3010622.1

20715^

^605^000001512^^12^^SIMVASTATIN 20MG TAB U/D^HDL CHOLESTEROL^35 MG/DL^L^3010622

.120715^

^605^000001512^^12^^SIMVASTATIN 20MG TAB U/D^LDL CHOLESTEROL^55.2 MG/DL^^301062

2.120715^

^605^000001512^^12^^SIMVASTATIN 20MG TAB U/D^SGPT (ALT)^26 IU/L^L^3010831.14081

8^

^605^000008018^^65^^RANITIDINE HCL 150MG TAB^CREATININE^3.1 MG/DL^H^3010830.06^

Example: Unit Dose – Laboratory Statistical Summary Message

Subj: V. 4.0 PBMLR 30109 605 JERRY L PETTIS VAMC \[#7685\] 07/19/04@17:06 6 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

----------------------------------------------------------------------------------

Laboratory Statistical Summary

SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

Total Patients 328

Total Laboratory Tests 1490

  
Example: Unit Dose – Laboratory Data Summary Message

Subj: V. 4.0 PBMLR 30109 605 JERRY L PETTIS VAMC \[#7686\] 07/19/04@17:06 1496 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

------------------------------------------------------------------------------------

Laboratory Data Summary

SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

Patient SSN VA CODE Laboratory Results Flag Date/Time Taken

------------------------------------------------------------------------------------

000006505 CV350 CHOLESTEROL 128 MG/DL L 08/09/01 0752

SGOT (AST) 18 IU/L 08/09/01 0752

TRIGLYCERIDE 48 MG/DL 08/09/01 0752

HDL CHOLESTEROL 50 MG/DL 08/09/01 0752

LDL CHOLESTEROL 68.4 MG/DL 08/09/01 0752

SGPT (ALT) 33 IU/L 08/09/01 0752

CV800 CREATININE 0.8 MG/DL 08/09/01 0752

POTASSIUM 4.9 mmol/L 08/09/01 0752

GA301 CREATININE 0.8 MG/DL 08/09/01 0752

000008660 CV350 CHOLESTEROL 113 MG/DL L 08/30/01 1021

SGOT (AST) 16 IU/L 08/30/01 1021

TRIGLYCERIDE 95 MG/DL 08/30/01 1021

HDL CHOLESTEROL 32 MG/DL 08/30/01 1021

> *\[A portion of this statistical data message has been removed to save space.\]*

Subj: V. 4.0 PBMLR 30109 605 JERRY L PETTIS VAMC \[#7686\] Page 3

------------------------------------------------------------------------------------

000006224 CV200 CREATININE 1.2 MG/DL 08/31/01 0600

CV800 CREATININE 1.2 MG/DL 08/31/01 0600

POTASSIUM 3.2 mmol/L L 08/31/01 0600

000003822 CV200 CREATININE 1.8 MG/DL H 08/30/01 0813

CV350 CHOLESTEROL 124 MG/DL L 04/18/01 1018

SGOT (AST) 23 IU/L 08/30/01 0813

TRIGLYCERIDE 80 MG/DL 04/18/01 1018

HDL CHOLESTEROL 44 MG/DL 04/18/01 1018

LDL CHOLESTEROL 64.0 MG/DL 04/18/01 1018

SGPT (ALT) 38 IU/L 08/30/01 0813

GA301 CREATININE 1.8 MG/DL H 08/30/01 0813

545568208 HS502 GLUCOSE 155 MG/DL H 04/26/01 1508

SGOT (AST) 23 IU/L 01/19/01 0600

SGPT (ALT) 48 IU/L 01/19/01 0600

000008739 CV350 CHOLESTEROL 280 MG/DL H 04/03/01 0839

SGOT (AST) 18 IU/L 07/24/01 1706

TRIGLYCERIDE 189 MG/DL H 04/03/01 0839

HDL CHOLESTEROL 47 MG/DL 04/03/01 0839

LDL CHOLESTEROL 195.2 MG/DL H 04/03/01 0839

SGPT (ALT) 40 IU/L 07/24/01 1706

Example: Unit Dose – Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY

\[#7687\] 07/19/04@17:06 7 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Unit Dose JUL 19,2004@16:00 JUL 19,2004@17:06 1 hrs, 6 min

Laboratory Results JUL 19,2004@17:06 JUL 19,2004@17:06 0 hrs, 0 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Unit Dose – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI

\[#7688\] 07/19/04@17:06 7 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-----------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were

Extracted by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-----------------------------------------------------------------------

Unit Dose 9942 1

Laboratory Results 2811 1

## AR/WS Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality created in recent enhancements provides a means to break down all AR/WS dispensing workload by division or outpatient site.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications are defined in detail in the tables below.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>AR/WS STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender (facility number)</td>
<td><p>Medical Center Division file (#40.8)</p>
<p>or</p>
<p>Outpatient Site file (#59)</p></td>
<td><p>Facility Number field (#1)</p>
<p>or</p>
<p>Site Number field (#.06)</p></td>
<td>2</td>
<td>The division or outpatient site that the AOU is mapped to will determine the sender.</td>
</tr>
<tr class="even">
<td>Breakdown by Outpatient Division or Inpatient Site not possible indicator</td>
<td></td>
<td></td>
<td>3</td>
<td>If records could not be broken down to an Outpatient Site or Inpatient division, an “H” is sent.</td>
</tr>
<tr class="odd">
<td>Month &amp; Year of Report</td>
<td></td>
<td></td>
<td>4</td>
<td>Sent in the following format:<br />
“29808” represents 8/98</td>
</tr>
<tr class="even">
<td>VA Product Name</td>
<td>Drug file (#50)</td>
<td>VA Product Name field (#21)</td>
<td>5</td>
<td></td>
</tr>
<tr class="odd">
<td>VA Drug Class</td>
<td>Drug file (#50)</td>
<td>VA Classification field (#2)</td>
<td>6</td>
<td></td>
</tr>
<tr class="even">
<td>NDC</td>
<td>Drug file (#50)</td>
<td>NDC field (#31)</td>
<td>7</td>
<td></td>
</tr>
<tr class="odd">
<td>Generic Drug Name</td>
<td>Drug file (#50)</td>
<td>Generic name field (#.01)</td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>Formulary/Non-Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>Non –Formulary field (#51)</td>
<td>9</td>
<td>If field set to “1”, the program sends “N/F”.</td>
</tr>
<tr class="odd">
<td>National Formulary Indicator</td>
<td>VA Product file (#50.68)</td>
<td>National Formulary Indicator field (#17)</td>
<td>10</td>
<td>Send “1” for Yes; “0” for No; otherwise null if no data found.</td>
</tr>
<tr class="even">
<td>National Formulary Restriction</td>
<td>VA Product file (#50.68)</td>
<td>National Formulary Restriction sub-field (#.01)</td>
<td>11</td>
<td>If data is found, send “1”; otherwise “0”</td>
</tr>
<tr class="odd">
<td>Dispense Unit</td>
<td>Drug file (#50)</td>
<td>Dispense Unit field (#14.5)</td>
<td>12</td>
<td></td>
</tr>
<tr class="even">
<td>Cost Per Dispense Unit</td>
<td>Drug file (#50)</td>
<td>Price Per Dispense Unit field (#16)</td>
<td>13</td>
<td></td>
</tr>
<tr class="odd">
<td>AMIS Category</td>
<td>Drug file (#50)</td>
<td>AR/WS AMIS Category field (#301)</td>
<td>14</td>
<td><p>IF “0”, Send 03 or 04.</p>
<p>If “1”, Send 06 or 07.</p>
<p>If “2”, Send 17.</p>
<p>If “3”, Send 22.</p></td>
</tr>
<tr class="even">
<td>AMIS Conversion Number</td>
<td>Drug file (#50)</td>
<td>AR/WS AMIS Conversion Number field (#302)</td>
<td>15</td>
<td></td>
</tr>
<tr class="odd">
<td>Total Quantity Dispensed (Net)</td>
<td>CATEGORY multiple (#1) within the RECALCULATE AMIS multiple (#2) within the INPATIENT SITE multiple (#1) within the AR/WS STATS file (#58.5)</td>
<td><p>QUANTITY Dispensed sub-field (#1)</p>
<p>CATEGORY sub-field (#.01)</p></td>
<td>16</td>
<td><p>Qty Dispensed:<br />
If category is “A” or “W” –dispensed.</p>
<p>Qty Returned:<br />
If category is “RA” or “RW” –returned.</p>
<p>Net amount dispensed = Qty dispensed – Qty returned.</p></td>
</tr>
<tr class="even">
<td>VISN Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>VISN Non-Formulary field (#52)</td>
<td>17</td>
<td>If “1” is found, send N/F, otherwise null if no data is found.</td>
</tr>
<tr class="odd">
<td>DEA, Special Handling</td>
<td>Drug file (#50)</td>
<td>DEA, Special Hdlg field (#3)</td>
<td>18</td>
<td></td>
</tr>
<tr class="even">
<td>Total Quantity Dispensed</td>
<td>CATEGORY multiple (#1) within the RECALCULATE AMIS multiple (#2) within the INPATIENT SITE multiple (#1) within the AR/WS STATS file (#58.5)</td>
<td><p>QUANTITY DISPENSED sub-field (#1)</p>
<p>CATEGORY sub-field (#.01)</p></td>
<td>19</td>
<td>If the CATEGORY sub-field (#.01) is set to “Automatic Replenishment” or “ Ward Stock”, the QUANTITY DISPENSED sub-field (#1) shall be counted for each dispense drug. The sum of all quantities dispensed shall be transmitted as the Total Quantity Dispensed data element.</td>
</tr>
<tr class="odd">
<td>Total Quantity Returned</td>
<td>CATEGORY multiple (#1) within the RECALCULATE AMIS multiple (#2) within the INPATIENT SITE multiple (#1) within the AR/WS STATS file (#58.5)</td>
<td><p>QUANTITY DISPENSED sub-field (#1)</p>
<p>CATEGORY sub-field (#.01)</p></td>
<td>20</td>
<td>If the CATEGORY sub-field (#.01) is set to “Returns – Auto Replenished” or “Returns – Ward Stocked”, the QUANTITY DISPENSED sub-field (#1) shall be counted for each dispense drug. The sum of all quantities returned shall be transmitted as the Total Quantity Returned data element.</td>
</tr>
</tbody>
</table>

Within the AR/WS extract, Medical Center Divisions are selected from the MEDICAL CENTER DIVISION file (#40.8) NAME field (#.01). Outpatient Sites are selected from the OUTPATIENT SITE file (#59) NAME field (#.01). The user may select an active or inactive Outpatient Site. \*\*Inactive\*\* shall be displayed next to a selected inactive Outpatient Site.

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

Example: AR/WS – Detail Report Message

Subj: V. 4.0 PBMAR 30109 1/1 605 JERRY L PETTIS VAMC \[#7421\]

07/15/04@16:56 383 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^^30109^Unknown VA Product Name^CN103^00839-6001-92^ACETAMINOPHEN 650MG RTL

SUPP^^^0^EA^0.317^03 or 04^1^12^^9R^12^^

^605^^30109^Unknown VA Product Name^RE400^00087-0572-03^ACETYLCYSTEINE 20% INHL

SOLN^^^0^ML^0.264^06 or 07^1^3^^6^3^^

^605^^30109^ALBUTEROL 90MCG/SPRAY INHL,ORAL^RE102^59930-1560-01^ALBUTEROL 90MCG

200D ORAL INHL^^1^0^EA^1.650^06 or 07^1^99^^6^99^^

^605^^30109^ALCOHOL,ISOPROPYL 70% LIQUID,TOP^DE101^00574-0067-16^ALCOHOL ISOPRO

PYL 70%^^1^0^ML^0.004^06 or 07^1^88318^^9^88318^^

^605^^30109^AMIODARONE HCL (CORDARONE) 200MG TAB^CV300^00008-4188-04^AMIODARONE

HCL (CORDARONE) 200MG TAB^^1^0^TAB^1.164^06 or 07^1^15^^6RO^15^^

^605^^30109^COMPOUND BENZOIN CONC LIQUID,TOP^DE900^10648-0800-08^BENZOIN TINCTU

RE SPRAY 135GM U4070^^0^0^BT^4.500^06 or 07^1^13^^9^13^^

^605^^30109^BENZOCAINE 20% SPRAY,TOP^DE700^00283-0679-02^BENZOCAINE 20% TOP SPR

AY^^0^0^ML^0.203^06 or 07^60^1683^^6^1683^^

^605^^30109^BENZOCAINE 20% GEL^NT300^00283-0871-31^BENZOCAINE 20% TOP GEL^^1^0^

GM^4.700^06 or 07^1^6^^9^6^^

^605^^30109^BISACODYL 10MG SUPP,RTL^RS300^00597-0052-50^BISACODYL 10MG RTL SUPP

^^1^0^EA^0.027^03 or 04^1^62^^9^62^^

Subj: V. 4.0 PBMAR 30109 1/1 605 JERRY L PETTIS VAMC \[#7421\] Page 2

-------------------------------------------------------------------------------

^605^^30109^CALCITRIOL 0.25MCG CAP^VT502^00004-0143-01^CALCITRIOL 0.25MCG CAP^^

1^0^CAP^0.746^06 or 07^1^300^^6^300^^

^605^^30109^COLCHICINE 0.6MG TAB^MS400^00143-1201-10^COLCHICINE 0.6MG TAB^^1^0^

TAB^0.0386^06 or 07^1^16^^6^16^^

^605^^30109^B-TRACIN 400UNT/HC 1%/N-MYCIN 3.5MG/POLYMYX 10000UNT/GM OINT,OPH^OP

350^00081-0196-88^BACITRACIN/HC 1%/NEO/POLYMYX OPH OINT^^1^0^TUBE^11.140^06 or

07^2^140^^6^140^^

^605^^30109^HC 1%/N-MYCIN 3.5MG/POLYMYX 10000UNT/ML SUSP,OTIC^OT250^24208-0635-

62^HC 1%/NEOMYCIN 3.5MG/POLYMYXIN OTIC SUSP^^1^0^ML^0.126^06 or 07^1^6^^6^6^^

^605^^30109^CYANOCOBALAMIN 1000MCG/ML INJ^VT101^00517-0031-25^CYANOCOBALAMIN 10

00MCG/ML INJ^^1^0^ML^0.450^03 or 04^10^160^^6^160^^

^605^^30109^CYCLOPENTOLATE HCL 1% SOLN,OPH^OP600^17478-0100-12^CYCLOPENTOLATE H

CL 1% OPH SOLN^^1^0^ML^0.2713^06 or 07^1^4^^6^4^^

^605^^30109^DACRIOSE SOLN,OPH,IRRG^OP500^00058-0727-15^DACRIOSE OPH IRRG^^0^0^M

L^0.015^06 or 07^30^8^^9^8^^

^605^^30109^DEXAMETHASONE NA PHOSPHATE 4MG/ML INJ,SOLN^HS051^63323-0165-05^DEXA

METHASONE SOD PHOS 4MG/ML 5ML VI^^1^0^VI^2.540^03 or 04^5^51^^6^51^^

^605^^30109^DIBUCAINE 1% OINT,TOP^DE700^00143-5012-31^DIBUCAINE 1% OINT^^1^0^GM

^0.026^06 or 07^1^2^^9^2^^

^605^^30109^DIPHENHYDRAMINE HCL 50MG/ML INJ^AH200^00071-4259-03^DIPHENHYDRAMINE

  
Example: AR/WS - Data Records Not Broken Down To Outpatient Site or Inpatient Division Message

Subj: V. 4.0 PBMAR 30109 1/1 605 JERRY L PETTIS VAMC \[#8977\]

08/18/04@14:06 9 lines

From: PBMPHARMACIST,TEN In 'IN' basket. Page 1

--------------------------------------------------------------------------------------^605^^30109^Unknown VA Product Name^RE400^00087-0572-03^ACETYLCYSTEINE 20% INHL

SOLN^^^0^ML^0.264^06 or 07^1^3^^6^3^^

^605^^30109^ALBUTEROL 90MCG/SPRAY INHL,ORAL^RE102^59930-1560-01^ALBUTEROL 90MCG

200D ORAL INHL^^1^0^EA^1.650^06 or 07^1^8^^6^8^^

^605^^30109^SODIUM CHLORIDE 0.9% SOLN^PH000^49502-0830-05^SODIUM CHLORIDE 0.9%

INHL 5ML^^0^0^5ML^0.071^03 or 04^100^500^^9^500^^

^605^^30109^IPRATROPIUM BR 18MCG/SPRAY AEROSOL,INHL^RE105^00597-0082-14^IPRATRO

PIUM BROMIDE 18MCG 200D ORAL INHL^^1^1^EA^17.580^06 or 07^1^8^^6^8^^

^605^^30109^ALBUTEROL 0.5% SOLN,INHL^RE102^0173-0385-58^ALBUTEROL 0.5% INHL SOL

N^^1^0^ML^0.311^06 or 07^1^30^^6^30^^

Example: AR/WS - Statistical Data Message

Subj: V. 4.0 PBMAR 30109 605 JERRY L PETTIS VAMC \[#7422\] 07/15/04@16:56

396 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Automatic Replenishment/Ward Stock Data Summary

SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

Total Total

Dispensed Dispensed AMIS

DRUG NAME Units Cost Category

------------------------------------------------------------------------------

ABSORB GEL COMP SPONGE STERILE SIZE 24.00 334.87 06 or 07

ABSORB GEL SPONGE STERILE SIZE 100 20.00 254.46 06 or 07

ABSORB HEMOSTAT 4IN X 8IN PKT \# 18.00 356.63 06 or 07

ACCU-CHEK COMFORT CURVE HI/LO CONTL 36.00 151.92 06 or 07

ACCU-CHEK COMFORT CV(GLUCOSE) TEST 311.00 103.25 06 or 07

ACETAMINOPHEN 325MG TAB U/D 1174.00 15.26 03 or 04

ACETAMINOPHEN 325MG/10.15ML ELIXIR 170.00 23.29 06 or 07

ACETAMINOPHEN 650MG RTL SUPP 12.00 3.80 03 or 04

ACETAMINOPHEN 650MG/25ML ELIXIR U/D 11.00 1.48 03 or 04

ACETIC ACID 2/HC 1% OTIC SOLN 4.00 0.74 06 or 07

ACETYLCYSTEINE 20% INHL SOLN 3.00 0.79 06 or 07

*\[A portion of this statistical data message has been removed to save space.\]*

Subj: V. 4.0 PBMAR 30109 605 JERRY L PETTIS VAMC \[#7422\] Page 20

-------------------------------------------------------------------------------

TROPICAMIDE 1% OPH SOLN 310.00 456.94 06 or 07

TUBERCULIN PPD 5TU/0.1ML 1ML VIAL 27.00 70.20 03 or 04

TUBEX INJECTOR, 1 & 2 ML SIZE,PLAST \# 14.00 28.00 06 or 07

VERAPAMIL HCL 120MG TAB U/D 10.00 0.76 06 or 07

VERAPAMIL HCL 240MG SR TAB U/D 20.00 5.38 06 or 07

VITAMIN E 400 UNT CAP 20.00 0.82 06 or 07

WARFARIN (COUMADIN) NA 2MG TAB 16.00 2.01 06 or 07

WARFARIN SOD 5MG TAB U/D 6.00 0.02 06 or 07

WATER STERILE FOR INJ USP 10ML VI 10.00 1.76 06 or 07

X-PREP LIQUID 74ML \# 20.00 106.00 06 or 07

ZZDIVALPROEX SODIUM 250MG EC TAB U/ 26.00 8.84 06 or 07

ZZPSYLLIUM SF ORAL PWD 62.00 2.29 06 or 07

------------------------------------------------------------------------------

TOTALS 358359.0 233776.1

\* Non-Formulary

\# Not on National Formulary

  
Example: AR/WS - AMIS Summary Report Message

Subj: V. 4.0 PBMAR 30109 605 JERRY L PETTIS VAMC \[#7423\] 07/15/04@16:56

43 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Automatic Replenishment/Ward Stock AMIS Summary

SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

AR/WS DOSES:

DOSES DOSES NET DOSES TOTAL AVE COST

DIVISION DISPENSED RETURNED DISPENSED COST PER DOSE

-----------------------------------------------------------------------------

JERRY L PETTIS VAM 33017.00 1656.00 31361.00 \$ 178015.49 \$ 5.67

-----------------------------------------------------------------------------

Total 33017.00 1656.00 31361.00 \$ 178015.49 \$ 5.67

AR/WS UNITS:

UNITS UNITS NET UNITS TOTAL AVE COST

DIVISION DISPENSED RETURNED DISPENSED COST PER UNIT

-----------------------------------------------------------------------------

JERRY L PETTIS VAM 326745.00 15.00 326730.00 \$ 57943.48 \$ .17

-----------------------------------------------------------------------------

Subj: V. 4.0 PBMAR 30109 605 JERRY L PETTIS VAMC \[#7423\] Page 2

-------------------------------------------------------------------------------

Total 326745.00 15.00 326730.00 \$ 57943.48 \$ .17

FLUIDS/SETS:

FLUIDS/SETS FLUIDS/SETS FLUIDS/SETS TOTAL AVE COST

DIVISION DISPENSED RETURNED DISPENSED COST PER

FLUIDS/SETS

-----------------------------------------------------------------------------

JERRY L PETTIS VAM 268.00 0.00 268.00 \$ 6099.46 \$ 22.75

-----------------------------------------------------------------------------

Total 268.00 0.00 268.00 \$ 6099.46 \$ 22.75

BLOOD PRODUCTS

BLOOD PROD BLOOD PROD BLOOD PROD TOTAL AVE COST

DIVISION DISPENSED RETURNED DISPENSED COST PER

BLOOD PROD

-----------------------------------------------------------------------------

JERRY L PETTIS VAM 0.00 0.00 0.00 \$ 0.00 \$ 0.00

-----------------------------------------------------------------------------

Subj: V. 4.0 PBMAR 30109 605 JERRY L PETTIS VAMC \[#7423\] Page 3

-------------------------------------------------------------------------------

Total 0.00 0.00 0.00 \$ 0.00 \$ 0.00

Example: AR/WS - Unmapped Locations Message

Subj: PBM Unmapped Locations for SEP 1,2001 to SEP 30,2001 from 605 LOM

\[#7424\] 07/15/04@16:56 7 lines

From: PBMPHARMACIST,THREE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The locations listed below have not been mapped to a Medical Center

Division or Outpatient Site. All data extracted from these locations have

been attributed to 605 LOMA LINDA

AOUs:

There are no unmapped AOU's for the dates of this extract

Example: AR/WS - Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY

\[#7425\] 07/15/04@16:56 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

AR/WS JUL 15,2004@16:55 JUL 15,2004@16:56 0 hrs, 1 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: AR/WS - Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI

\[#7426\] 07/15/04@16:56 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

AR/WS 383 1

## Prescription Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Active Prescription order records with dispensing activity for the time period the extract is run will be extracted.

![](benefits-management-version-4-user-manual/013.png)Note: When the Prescription extract is run, the Patient Demographic Summary Report and Lab reports are automatically generated.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications for the Prescription extract are defined in the table below.

![](benefits-management-version-4-user-manual/014.png)Note: Pieces 38-46 can repeat for a complex outpatient medication order (\>1 dosing sequence). When a prescription is extracted that has more than one dosing sequence the prescription record with the first dosing sequence shall be transmitted in the PBMOP MailMan message. The prescription record with ALL dosing sequences will be transmitted in the new PBMOP(MULTIDOSE) MailMan message. In this MailMan message pieces 38-46 will repeat for each additional dosing sequence.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>PRESCRIPTION STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender</td>
<td>Outpatient Site file (#59)</td>
<td>site number field (#.06)</td>
<td>2</td>
<td></td>
</tr>
<tr class="even">
<td><p>Fill date</p>
<p>Refill date</p>
<p>Partial date</p></td>
<td><p>Prescription file (#52)</p>
<p>Refill multiple (#52)</p>
<p>Partial multiple (#60)</p></td>
<td><p>Fill date field (#22 )</p>
<p>Refill date field</p>
<p>(#.01)</p>
<p>Partial date field (#.01)</p></td>
<td>3</td>
<td></td>
</tr>
<tr class="odd">
<td>Release date</td>
<td><p>Prescription file (#52)</p>
<p>Refill multiple (#52)</p>
<p>Partial multiple (#60)</p></td>
<td><p>Released Date/time field (#31)</p>
<p>Released date/time field (#17)</p>
<p>Released date/time field (#8)</p></td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>Prescription #</td>
<td>Prescription file (#52 )</td>
<td>RX # field (#.01)</td>
<td>5</td>
<td></td>
</tr>
<tr class="odd">
<td>Prescription Patient status</td>
<td>Rx Patient Status file (#53)</td>
<td><p>SC/A&amp;A/OTHER/</p>
<p>INPATIENT field</p>
<p>(# 6)</p></td>
<td>6</td>
<td>If “1” send “SC”; If “2” send “AA”; If “3” send “OT”; If “4” send “IP”</td>
</tr>
<tr class="even">
<td>Patient SSN</td>
<td>Patient file (#2)</td>
<td>Social Security Number field (#.09)</td>
<td>7</td>
<td></td>
</tr>
<tr class="odd">
<td>VA Product Name</td>
<td>Drug file (#50)</td>
<td>VA Product Name field (#21)</td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>VA Drug Class</td>
<td>Drug file (#50)</td>
<td>VA Classification field (#2)</td>
<td>9</td>
<td></td>
</tr>
<tr class="odd">
<td>Generic Drug Name</td>
<td>Drug file (#50)</td>
<td>Generic name field (#.01)</td>
<td>10</td>
<td></td>
</tr>
<tr class="even">
<td>NDC</td>
<td><p>Prescription file</p>
<p>(#52)</p>
<p>CMOP Event multiple (#400)</p>
<p>Refill multiple (#52)</p>
<p>Partial multiple (#60)</p>
<p>Drug file (#50)</p></td>
<td>See description</td>
<td>11</td>
<td><p>1) If CMOP Rx data: CMOP Event Multiple (#400), NDC field (#4)</p>
<p>2 ) If data not found or not CMOP Rx:</p>
<p>(Original fill) - NDC field (#27)</p>
<p>(Refills) - REFILL multiple (#52) NDC field (#11)</p>
<p>(Partials) - PARTIAL multiple (#60) NDC field (#1)</p>
<p>3) If data not found:</p>
<p>DRUG file (#50) NDC field (#31)</p>
<p>4) If data not found - program sends “No NDC”</p></td>
</tr>
<tr class="odd">
<td>Formulary/Non-Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>LOCAL Non-formulary field (#51)</td>
<td>12</td>
<td>If field set to “1” the program sends “N/F”</td>
</tr>
<tr class="even">
<td>National Formulary Indicator</td>
<td>VA Product file (#50.68)</td>
<td>National Formulary Indicator field (#17)</td>
<td>13</td>
<td>Send “1” for Yes; “0” for No; otherwise null if no data found</td>
</tr>
<tr class="odd">
<td>National Formulary Restriction</td>
<td><p>VA Product File (#50.68)</p>
<p>National Formulary Restriction multiple (#18)</p></td>
<td>National Formulary Restriction field (#.01)</td>
<td>14</td>
<td>If data is found send “1” ; otherwise “0”</td>
</tr>
<tr class="even">
<td>DEA Special Handling Field</td>
<td>Drug File (#50)</td>
<td>DEA, Special hdlg field (# 3)</td>
<td>15</td>
<td></td>
</tr>
<tr class="odd">
<td>New/Refill/Partial Indicator</td>
<td>N/A</td>
<td>N/A</td>
<td>16</td>
<td>If Rx is new/original, send “N”; refill Rx, send “R”; partial Rx, send “P”.</td>
</tr>
<tr class="even">
<td>CMOP Indicator</td>
<td>N/A</td>
<td>N/A</td>
<td>17</td>
<td><p>Send “Y” for Yes and “N” for No.</p>
<p>Conditions apply. See user /technical manual for details</p></td>
</tr>
<tr class="odd">
<td>Mail/Window Indicator</td>
<td><p>Prescription file (#52)</p>
<p>Refill multiple (#52)</p>
<p>Partial multiple</p>
<p>(#60)</p></td>
<td><p>Original Fill: Mail/Window field (#11)</p>
<p>Refills: Mail/Window field (#2)</p>
<p>Partials: Mail/Window field (#.02)</p></td>
<td>18</td>
<td>Send “M” for mail; “W” for window.</td>
</tr>
<tr class="even">
<td>Provider ID (SSN)</td>
<td>New Person File (#200)</td>
<td>SSN field (#9)</td>
<td>19</td>
<td>If no SSN is found, a null value will be transmitted</td>
</tr>
<tr class="odd">
<td>Provider Type</td>
<td>New Person File (#200)</td>
<td>Provider type field (#53.6)</td>
<td>20</td>
<td>If “4” send “F” for Fee; otherwise send “S” for Staff</td>
</tr>
<tr class="even">
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>21</td>
<td>The free text ”signa” (SIG) shall no longer be extracted with the second enhancement patch. A null value will always be sent.</td>
</tr>
<tr class="odd">
<td>Medication Counseling</td>
<td>Prescription file (#52)</td>
<td>Was the Patient Counseled field (#41)</td>
<td>22</td>
<td><p>Send “Y” for Yes or</p>
<p>“N” for No</p></td>
</tr>
<tr class="even">
<td>Dispense Unit</td>
<td>Drug file (#50)</td>
<td>Dispense Unit field (#14.5)</td>
<td>23</td>
<td></td>
</tr>
<tr class="odd">
<td>Price Per Dispense Unit</td>
<td><p>Prescription file (#52)</p>
<p>Refill multiple (#52)</p>
<p>Partial multiple (#60)</p></td>
<td><p>Original Fill: Unit Price of Drug field (#17)</p>
<p>Refills: Current Unit Price of Drug (#1.2)</p>
<p>Partials: Current Unit Price of Drug field (#.042)</p></td>
<td>24</td>
<td></td>
</tr>
<tr class="even">
<td>Days Supply</td>
<td><p>Prescription file (#52)</p>
<p>Refill multiple (#52)</p>
<p>Partial multiple (#60)</p></td>
<td><p>Original Fill: Days SUPPLY field (#8)</p>
<p>Refills: DAYS SUPPLY field (#1.1)</p>
<p>Partials: DAYS SUPPLY field (#.041)</p></td>
<td>25</td>
<td></td>
</tr>
<tr class="odd">
<td>Total Qty Dispensed</td>
<td><p>Prescription file (#52)</p>
<p>Refill multiple (#52)</p>
<p>Partial multiple (#60)</p></td>
<td><p>Original Fill: Qty field (#7)</p>
<p>Refills: QTY field (#1)</p>
<p>Partials: QTY field (#.04)</p></td>
<td>26</td>
<td></td>
</tr>
<tr class="even">
<td>VISN Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>VISN Non-Formulary field (#52)</td>
<td>27</td>
<td>If “1” is found, send “N/F”, otherwise null if no data is found.</td>
</tr>
<tr class="odd">
<td>Patient ICN</td>
<td>PATIENT file (#2)</td>
<td><p>INTEGRATION CONTROL NUMBER field</p>
<p>(# 991.01)</p>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
<p>(Values in both fields are concatenated with a “V”.)</p></td>
<td>28</td>
<td><p>Free Text</p>
<p>Example: “1010185893V199552”</p>
<p>If an ICN does not exist send null.</p></td>
</tr>
<tr class="even">
<td>Provider Local IEN</td>
<td>New Person file (#200)</td>
<td>Internal Entry Number (IEN)</td>
<td>29</td>
<td></td>
</tr>
<tr class="odd">
<td>Cancel Date</td>
<td>Prescription file (#52)</td>
<td>Cancel Date field (#26.1)</td>
<td>30</td>
<td><p>If no cancel date is found, a null value will be sent.</p>
<p>If a value is found, the internal format will be transmitted.</p>
<p>Example: “3011001.0134”</p></td>
</tr>
<tr class="even">
<td>Clinic</td>
<td>HOSPITAL LOCATION file (#44)</td>
<td>NAME field (#.01)</td>
<td>31</td>
<td>If no clinic is found, a null value will be sent.</td>
</tr>
<tr class="odd">
<td>CMOP ID</td>
<td>DRUG file (#50)</td>
<td>CMOP ID field (#27)</td>
<td>32</td>
<td>If no data is found in the CMOP ID field (#27), a null value will be sent.</td>
</tr>
<tr class="even">
<td>Finishing RPh</td>
<td>New Person file (#200)</td>
<td>Internal Entry Number (IEN)</td>
<td>33</td>
<td><p>Facility # + IEN</p>
<p>Data identified from the FINISHING PERSON field (#38) in the PRESCRIPTION file (#52).</p></td>
</tr>
<tr class="odd">
<td>Login Date</td>
<td><p>Prescription file (#52)</p>
<p>Refill multiple (#52)</p>
<p>Partial multiple (#60)</p></td>
<td><p>Original fill: LOGIN DATE field (#21)</p>
<p>Refills: LOGIN DATE field (#7)</p>
<p>Partials: LOGIN DATE field (#.08)</p></td>
<td>34</td>
<td><p>The internal format will be transmitted.</p>
<p>Example: “3011001.0900”.</p></td>
</tr>
<tr class="even">
<td>Copay Status</td>
<td>Prescription file (#52)</td>
<td>COPAY TRANSACTION TYPE field (#105)</td>
<td>35</td>
<td>If a “1” or “2” is found send a “Y” for copay eligible; If no value is found send “N” for not copay eligible.</td>
</tr>
<tr class="odd">
<td>Expanded Patient Instructions</td>
<td><p>Prescription file (#52)</p>
<p>EXPANDED PATIENT INSTRUCTIONS multiple (#115)</p></td>
<td>EXPANDED PATIENT INSTRUCTIONS field (#.01)</td>
<td>36</td>
<td>If no expanded patient instructions are found, a null value will be sent.</td>
</tr>
<tr class="even">
<td>Multidose Flag</td>
<td>N/A</td>
<td>N/A</td>
<td>37</td>
<td><p>For a complex prescription record the following data elements that comprise the dosing sequence will repeat.</p>
<p>Dosage Ordered</p>
<p>Dispense Units Per Dose</p>
<p>Units</p>
<p>Noun</p>
<p>Duration</p>
<p>Conjunction</p>
<p>Route</p>
<p>Schedule</p>
<p>Verb</p>
<p>If a prescription record contains more than one dosing sequence, an “M” shall be transmitted to flag the prescription record as having a multiple dosing sequence. If only one dosing sequence exits, a null value shall be transmitted.</p></td>
</tr>
<tr class="odd">
<td>Dosage Ordered</td>
<td><p>Prescription file (#52)</p>
<p>MEDICATION INSTRUCTION multiple (#113)</p></td>
<td>DOSAGE ORDERED field (#.01)</td>
<td>38</td>
<td></td>
</tr>
<tr class="even">
<td>Dispense Units Per Dose</td>
<td><p>Prescription file (#52)</p>
<p>MEDICATION INSTRUCTION multiple (#113)</p></td>
<td>DISPENSE UNITS PER DOSE field (#1)</td>
<td>39</td>
<td></td>
</tr>
<tr class="odd">
<td>Units</td>
<td>DRUG UNITS file (#50.607)</td>
<td>NAME field (#.01)</td>
<td>40</td>
<td></td>
</tr>
<tr class="even">
<td>Noun</td>
<td><p>Prescription file (#52)</p>
<p>MEDICATION INSTRUCTION multiple (#113)</p></td>
<td>NOUN field (#3)</td>
<td>41</td>
<td>If a noun does not exist, a null value will be transmitted.</td>
</tr>
<tr class="odd">
<td>Duration</td>
<td><p>Prescription file (#52)</p>
<p>MEDICATION INSTRUCTION multiple (#113)</p></td>
<td>DURATION field (#4)</td>
<td>42</td>
<td>Duration can be entered in minutes, hours, days, weeks, or months. The internal format of the data shall be extracted, e.g. “14D or 14” represents 14 days, “1W” represents 1 week. If no duration exists a null value shall be transmitted.</td>
</tr>
<tr class="even">
<td>Conjunction</td>
<td><p>Prescription file (#52)</p>
<p>MEDICATION INSTRUCTION multiple (#113)</p></td>
<td>CONJUNCTION field (#5)</td>
<td>43</td>
<td><p>The internal format of the data shall be extracted.<br />
Example: “A” for And, “T” for Then, and “X” for Except.</p>
<p>If no conjunction exists, a null value shall be transmitted.</p></td>
</tr>
<tr class="odd">
<td>Route</td>
<td><p>MEDICATION ROUTES</p>
<p>file (#51.2)</p></td>
<td>NAME field (#.01)</td>
<td>44</td>
<td></td>
</tr>
<tr class="even">
<td>Schedule</td>
<td><p>Prescription file (#52)</p>
<p>MEDICATION INSTRUCTION multiple (#113)</p></td>
<td>SCHEDULE field (#7)</td>
<td>45</td>
<td></td>
</tr>
<tr class="odd">
<td>Verb</td>
<td><p>Prescription file (#52)</p>
<p>MEDICATION INSTRUCTION multiple (#113)</p></td>
<td>VERB field (#8)</td>
<td>46</td>
<td>If no verb is found, a null value will be transmitted.</td>
</tr>
</tbody>
</table>

![](benefits-management-version-4-user-manual/015.png)Note: Pieces 38-46 can repeat for a complex outpatient medication order (\>1 dosing sequence). When a prescription is extracted that has more than one dosing sequence, the prescription record with the first dosing sequence shall be transmitted in the PBMOP MailMan message. The prescription record with ALL dosing sequences will be transmitted in the new PBMOP(MULTIDOSE) MailMan message. In this MailMan message pieces 38-46 will repeat for each additional dosing sequence.

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format. The following is an example of the first (parent) data record sent for a Prescription order. Each IV additive and solution within an order will be sent as a separate data record.

Example: Prescription – Detail Report Message

Subj: V. 4.0 PBMOP 30109 1/13 605 LOMA LINDA VA \[#7597\] 07/16/04@19:09

10000 lines

From: PBMPHARMACIST,SIX In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^3010523^3010907^437316A^OT^000008194^IPRATROPIUM BR 0.03% SOLN,SPRAY,NASAL

^NT900^IPRATROPIUM BR 0.03% NASAL SPRAY^00597-0081-30^^1^0^6^R^N^M^000008204^F^

\*^N^ML^.6897^50^30^^1002937743^2723^3010830^^I0198^^^N^^AS NEEDED FOR PAIN^^10

CC (=2 TEASPOONSFUL)^^^^^^ORAL^Q4-6H^TAKE^

^605^3010830^3010904^3410498B^SC^000001852^IBUPROFEN 800MG TAB^MS102^IBUPROFEN

800MG TAB^353746137906^^1^0^6^R^Y^M^000009577^S^

\*^N^TAB^.024^30^90^^1002944235^8893^^^I0006^^^N^^FOR PAIN^^1-2 TABLETS^^^^^^ORA

L^Q4-6H P^TAKE^

^605^3010830^3010904^3609546^SC^000005458^SERTRALINE HCL 100MG TAB^CN609^SERTRA

LINE HCL 100MG TAB^0049491073^^1^0^6RO^R^Y^M^000006209^S^

\*^N^TAB^1.164^30^60^^1002940453^8547^^^S0013^^^N^^FOR DIARRHEA \*\*DO NOT EXCEED

8 CAPSULES PER DAY\*\*^^2^1^MG^CAPSULE^^^ORAL^Q4-6H P ^TAKE^

^605^3010830^3010904^3609547^SC^000005458^DIVALPROEX NA 250MG TAB,EC^CN400^DIVA

LPROEX NA 250MG EC TAB^0074621453^^1^0^6^R^Y^M^000006209^S^

\*^N^TAB^.367^30^90^^1002940453^8547^^^D0564^^^N^^FOR DIARRHEA \*\*DO NOT EXCEED 8

CAPSULES PER DAY\*\*^^2^1^MG^CAPSULE^^^ORAL^Q4-6H P ^TAKE^

^605^3010830^3010904^3609549^SC^000005458^BUPROPION HCL (ZYBAN) 150MG TAB,SA^CN

609^BUPROPION (ZYBAN) 150MG SA TAB PACK 60^301730556011^^1^0^6^R^Y^M^000006209^

Subj: V. 4.0 PBMOP 30109 1/13 605 LOMA LINDA VA \[#7597\] Page 2

-------------------------------------------------------------------------------

S^

\*^N^TAB^48.33^30^1^^1002940453^8547^^^B0395^^^N^^FOR DIARRHEA \*\*DO NOT EXCEED 8

CAPSULES PER DAY\*\*^^2^1^MG^CAPSULE^^^ORAL^Q4-6H P ^TAKE^

^605^3010830^3010904^3534711B^SC^000006593^CIMETIDINE 400MG TAB^GA301^CIMETIDIN

E 400MG TAB^5011155102^^1^0^6^R^Y^M^000007891^S^

\*^N^TAB^.065^90^180^^1002935868^712^^^C0255^^^N^^FOR STOMACH ACID^^300^1^MG^TAB

LET^^^ORAL^BID^TAKE^

^605^3010906^3010906^3611451^SC^000009381^ALCOHOL PREP PAD^XA105^ALCOHOL PREP P

AD^00536-9920-01^^1^0^9S^R^N^W^000009999^S^

\*^N^EA^.009^90^200^^1002940819^3926^^^XS678^^^N^^AFTER THE MORNING MEAL //TO RE

PLACE LANSOPROZOLE FOR STOMACH //^^1-2 TEASPOONSFUL^^^^^^ORAL^Q46H PRN^TAKE^

^605^3010830^3010906^3217544H^OT^000006338^BECLOMETHASONE DIPROPIONATE 42MCG/AC

TUAT POCKETHALER,INHL,NASAL^NT200^BECLOMETHASONE 42MCG 200D NASAL POCKETHL^3017

30336026^^0^0^6^R^Y^M^000001743^S^

\*^N^EA^3.49^30^1^^1002932885^1610^3011120^^B0392^^^N^^AFTER THE MORNING MEAL //

TO REPLACE LANSOPROZOLE FOR STOMACH //^^1-2 TEASPOONSFUL^^^^^^ORAL^Q46H PRN^TAK

E^

^605^3010907^3010912^3289451B^OT^000001647^COLCHICINE 0.6MG TAB^MS400^COLCHICIN

E 0.6MG TAB^0143120110^^1^0^6^R^Y^M^000000057^S^

\*^N^TAB^.007^30^30^^1002931852^1809^^^C0311^^^N^^AS NEEDED^^1 TABLET^^^^^^ORAL^

  
Example: Prescription – Detail Report Message

Subj: V. 4.0 PBMOP 30109 2/13 605 LOMA LINDA VA \[#7598\] 07/16/04@19:09

10000 lines

From: PBMPHARMACIST,THREE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^3010921^3010926^3653895A^SC^000006904^FLUNISOLIDE 250MCG/SPRAY/MENTHOL INH

L,ORAL^RE101^FLUNISOLIDE 250MCG/MENTHOL 100D ORAL INH^304560670995^^0^1^6^R^Y^M

^000006394^S^

\*^N^EA^2.81^25^1^^1002926903^5316^3011221^^F0121^^^N^^FOR DIARRHEA^^1 CAPSULE^^

^CAPSULE(S)^^^ORAL^Q46H P^TAKE^

^605^3010909^3010913^3686296^SC^000007472^SULFASALAZINE 500MG TAB^GA900^SULFASA

LAZINE 500MG TAB^352544796056^^1^0^6^R^Y^M^000007891^S^

\*^N^TAB^.054^30^120^^1002940246^712^3020326^^S0054^^^N^^FOR PAIN /HEADACHE \*\*DO

NOT TAKE MORE THAN 4000MG OF ACETAMINOPHEN PER DAY\*\*^^1/2 TABLET (=10MG) ^^^TA

BLET(S)^^^ORAL^QD FBP^TAKE^

^605^3010831^3010905^3686316^OT^000001556^ACCU-CHEK COMFORT CURVE (GLUCOSE) TES

T STRIP^DX900^ACCU-CHEK COMFORT CV(GLUCOSE) TEST STRIP^075537303733^^1^0^9S^R^Y

^M^000009999^S^

\*^N^EA^.3324^30^100^^1002926538^3926^3020207^^A1015^^^N^^\*\* TAKE AFTER MEAL \*\*

FOR STOMACH ACID^^1 TABLET^^^TABLET(S)^^^ORAL^QD^TAKE^

^605^3010831^3010905^3686319^OT^000001556^ACCU-CHEK COMFORT CURVE (GLUCOSE) HI/

LO CONTROL SOLN^DX900^ACCU-CHEK COMFORT CURVE HI/LO CONTL SOLN^075537304112^^1^

0^9S^R^Y^M^000009999^S^

Subj: V. 4.0 PBMOP 30109 2/13 605 LOMA LINDA VA \[#7598\] Page 2

-------------------------------------------------------------------------------

\*^N^EA^4.22^90^1^^1002926538^3926^3020207^^A1014^^^N^^\*\* TAKE AFTER MEAL \*\* FOR

STOMACH ACID^^1 TABLET^^^TABLET(S)^^^ORAL^QD^TAKE^

^605^3010831^3010904^421078D^OT^000005528^LEVOTHYROXINE NA 0.1MG TAB (SYNTHROID

)^HS851^LEVOTHYROXINE NA (SYNTHROID) 0.1MG TAB^0048107005^^1^0^6^R^Y^M^00000081

4^F^

\*^N^TAB^.016^90^90^^1002943527^12163^3020123^^L0139^^^N^^FOR PAIN^^1-2 TABLETS^

^^^^^ORAL^Q4-6H P^TAKE^

^605^3010911^3010913^3350431D^OT^000002872^CYCLOBENZAPRINE HCL 10MG TAB^MS200^C

YCLOBENZAPRINE HCL 10MG TAB^0378075110^^1^0^6^R^Y^M^000002462^S^

\*^N^TAB^.02^30^60^^1002928548^7181^3011231^^C0325^^^N^^FOR PAIN /HEADACHE \*\*DO

NOT TAKE MORE THAN 4000MG OF ACETAMINOPHEN PER DAY\*\*^^2 TABLETS^^^TABLET(S)^^^O

RAL^Q4-6H P^TAKE^

^605^3010829^3010901^3332150D^OT^000006597^Unknown VA Product Name^DX900^ADVANT

AGE ACCU-CHEK GLUCOSE TEST STRIP^075537005538^^^0^9SW^R^Y^M^000005262^S^

\*^N^STRIP^.431^90^50^^1002931623^9399^3011228^^^^^N^^^^^^^^^^^^^

^605^3010829^3010901^3207413E^OT^000006597^ASPIRIN 325MG TAB,EC^CN103^ASPIRIN 3

25MG EC TAB^006030167218^^1^0^9^R^Y^M^000005262^S^

\*^N^TAB^.011^90^100^^1002931623^9399^3011029^^A0414^^^N^^^^^^^^^^^^^

^605^3010831^3010901^3686381^OT^000006597^ISOSORBIDE DINITRATE 10MG TAB,ORAL^CV

250^ISOSORBIDE DINITRATE 10MG ORAL TAB^0781155610^^1^0^6^R^Y^M^000005262^S^

Example: Prescription – Outpatient Statistical Data Summary Message

Subj: V. 4.0 PBMOP 30109 605 LOMA LINDA VA \[#7610\] 07/16/04@19:10

10 lines

From: PBMPHARMACIST,THREE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Outpatient Statistical Data Summary for SEP 1,2001 through SEP 30,2001

Consolidated Mail Out Pharmacy (CMOP)

Total Total

Partials Fills Refills Cost Fills Refills Cost

-------------------------------------------------------------------------------

538 13694 4609 621735.95 12846 29984 1179339.55

Avg. Cost/Fill = \$33.00 Avg. Cost/Fill = \$27.54

Example: Prescription – Outpatient Statistical Data Message

Subj: V. 4.0 PBMOP 30109 605 LOMA LINDA VA \[#7611\] 07/16/04@19:10 2225 lines

From: PBMPHARMACIST,THREE In 'IN' basket. Page 1

-------------------------------------------------------------------------------------------

Outpatient Statistical Data for SEP 1,2001 through SEP 30,2001

Total Total Qty

Drug Name Partials Fills Refills Cost Dispensed

-------------------------------------------------------------------------------------------

A & D OINT 0 1 0 0.30 60.00

ABACAVIR SUL 300MG TAB 1 10 27975 9.36 2760.00

ABSORBASE TOP OINT 1 43 510 4.45 20887.00

ACARBOSE 50MG TAB 0 3 117 9.55 630.00

Enter RETURN to continue or '^' to exit:

Subj: V. 4.0 PBMOP 30109 605 LOMA LINDA VA \[#7611\] Page 2

------------------------------------------------------------------------------------------

ACCU-CHEK COMFORT CURVE HI/LO CONTL SOLN 1 61 2 270.08 64.00

ACCU-CHEK COMFORT CV(GLUCOSE) TEST STRIP 13 130 63 5157.18 15515.00

ACETAMINOP 120MG/COD 12MG/5ML ELIX 0 12 4 150.00 10000.00

ACETAMINOPHEN 160MG/5ML LIQUID 0 1 0 1.92 480.00

ACETAMINOPHEN 300MG/COD 30MG TAB 1 306 81 1318.07 22417.00

ACETAMINOPHEN 300MG/COD 60MG TAB 0 20 39 2272.68 7890.00

ACETAMINOPHEN 325MG TAB 0 38 9 52.62 5262.00

ACETAMINOPHEN 500MG TAB 0 95 27 96.63 13804.00

ACETAZOLAMIDE 250MG TAB 0 1 0 1.74 30.00

ACETAZOLAMIDE 500MG SA CAP 0 1 0 33.12 60.00

  
Example: Prescription – Detail Report Message

Subj: V. 4.0 PBMOP(MULTIDOSE) 30109 1/1 605 LOMA LINDA VA \[#7630\]

07/16/04@19:10 8 lines

From: PBMPHARMACIST,SIX In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^3010924^3010924^3661331C^SC^000001672^INSULIN NOVOLIN 70/30 (NPH/REG) INJ

NOVO^HS501^INSULIN NOVOLIN 70/30 (NPH/REG) INJ NOVO^00169-1837-11^^1^0^9D^R^N^W

^000005782^S^

\*^N^VI^4.49^30^1^^1003299051^9173^^^I0164^^^N^^FOR DIABETES --NOTE-- 90 DAY SUP

PLY GIVEN--^M^28 UNITS^^^^^T^SUB Q^QAM^INJECT^14 UNITS^^^^^^SUB Q^QPM^INJECT^

^605^3010926^3010929^3797392A^OT^000000815^INSULIN REG HUMAN 100 U/ML INJ NOVOL

IN R^HS501^INSULIN REG HUMAN 100 U/ML INJ NOVOLIN R^732849707016^^1^0^9^N^Y^M^0

00002494^S^

\*^N^VI^4.49^90^3^^1008437887^3236^^IC/TRIAGE WALK-IN^I0153^605DANG,CHINH T^3010

926.112314^N^^AND PER SLIDING SCALE FOR DIABETES^M^13 UNITS^^^^^A^SUB Q^QAM^INJ

ECT^10 UNITS^^^^^^SUB Q^QPM^INJECT^

^605^3010926^3010926^3818361^SC^000008537^INSULIN NOVOLIN 70/30 (NPH/REG) INJ N

OVO^HS501^INSULIN NOVOLIN 70/30 (NPH/REG) INJ NOVO^00169-1837-11^^1^0^9D^N^N^W^

000001019^S^

\*^Y^VI^4.49^60^2^^1002928600^5582^3011204^MODULE 2 PHYSICIAN WALK-INS^I0164^605

CHAU,TOT VAN^3010926.12012^N^^FOR MUSCLE SPASM^M^22 UNITS^^^^^A^SUB Q^QAM^INJEC

T^10 UNITS^^^^^^SUB Q^QPM^INJECT^

^605^3010926^3010926^3682503A^SC^000003228^GABAPENTIN 300MG CAP^CN400^GABAPENTI

Subj: V. 4.0 PBMOP(MULTIDOSE) 30109 1/1 605 LOMA LINDA VA \[#7630\]

Page 2

-------------------------------------------------------------------------------

N 300MG CAP^00071-0805-24^^1^0^6^N^N^W^000006386^S^

\*^Y^CAP^.617^30^90^^1002934089^1613^^GIM/CASTRO M1^G0104^605CHAU,TOT VAN^301092

6.135259^N^^FOR NERVES^M^1 CAPSULE^^^CAPSULE(S)^^A^ORAL^QAM^TAKE^2 CAPSULES ^^^

CAPSULE(S)^^^ORAL^QPM^TAKE^

  
Example: Prescription - Patient Demographic Summary Report

Subj: V. 4.0 PBMPD 30109 605 JERRY L PETTIS VAMC \[#7631\] 07/16/04@19:14

22 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

PHARMACY OUTPATIENT UNIQUE PATIENTS REPORT JUL 16, 2004

-------------------------------------------------------------------------------

SEP 01, 2001 through SEP 30, 2001

===============================================================================

UNIQUE

---------------------------------------------------------------------

TOTAL Pharmacy patients across all divisions: 16877

---------------------------------------------------------------------

CORONA CBOC Division: 14

LOMA LINDA VA Division: 16190

PALM DESERT CBOC Division: 302

PASS MEDS Division: 24

SUN CITY CBOC Division: 401

UPLAND CBOC Division: 17

VICTORVILLE-CBOC Division: 782

---------

Outpatient Total of all Divisions: 17730

Subj: V. 4.0 PBMPD 30109 605 JERRY L PETTIS VAMC \[#7631\] Page 2

-------------------------------------------------------------------------------

\*\*PLEASE NOTE: Final TOTAL may not match sum of all SUBTOTALS. A patient may

have been provided pharmacy services at more than one outpatient and/or

inpatient division.

Example: Prescription - Outpatient AMIS Summary Report Message

Subj: V.4.0 PBMOP 30109 605 JERRY L PETTIS VAMC \[#7632\] 07/16/04@19:14 30 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

------------------------------------------------------------------------------------------------

Outpatient AMIS Summary for SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

Unadj 30 Day Cost/

30 Day 60 Day 90 Day Total Equiv Total Unadj Cost/30Day

Division Fills Fills Fills Fills Fills Cost Fill Fill

------------------------------------------------------------------------------------------------

LOMA LINDA VA 38364 2783 20524 61671 105502 \$205037160 \$3324.69 \$1943.44

VICTORVILLE-CBOC 673 102 1086 1861 4135 \$670774 \$5196.54 \$2338.76

SUN CITY CBOC 337 59 546 942 2093 \$4876793 \$5177.06 \$2330.04

PALM DESERT CBOC 134 30 434 598 1496 \$3708526 \$6201.54 \$2478.96

*\[A portion of this statistical data message has been removed to save space.\]*

Subj: V.4.0 PBMOP 30109 605 JERRY L PETTIS VAMC \[#7632\] Page 3

-------------------------------------------------------------------------------

LOMA LINDA VA 26540 35131 16708(1946)44963(656)42830 18841(2602) 51390 10281

VICTORVILLE-CBOC 1657 204 18(5) 1843(35) 1711 150(40) 126 1735

SUN CITY CBOC 909 33 16(5) 926(4) 850 92(9) 4 938

PALM DESERT CBOC 571 27 0(0) 598(4) 567 31(4) 14 584

CORONA CBOC 17 3 3(3) 17(0) 16 4(3) 0 20

UPLAND CBOC 21 2 1(0) 22(0) 20 3(0) 1 22

PASS MEDS 223 0 223(44) 0(0) 0 223(44) 223 0

------------------------------------------------------------------------------------------------

Total 29938 35400 16969(2003)48369(699) 45994 19344(2702) 51758 13580

Example: Prescription – Detail Report Message

Subj: V. 4.0 PBMLR 30109 1/2 605 LOMA LINDA VA \[#7633\] 07/16/04@19:18

15000 lines

From: PBMPHARMACIST,SIX In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^000000230^^^^RANITIDINE HCL 150MG TAB^CREATININE^1.1 MG/DL^^3010723.080027

^

^605^000000250^^^^LOVASTATIN 40MG TAB^CHOLESTEROL^120 MG/DL^L^3010807.1028^

^605^000000250^^^^LOVASTATIN 40MG TAB^SGOT (AST)^16 IU/L^^3010807.1028^

^605^000000250^^^^LOVASTATIN 40MG TAB^TRIGLYCERIDE^146 MG/DL^^3010807.1028^

^605^000000250^^^^LOVASTATIN 40MG TAB^HDL CHOLESTEROL^45 MG/DL^^3010807.1028^

^605^000000250^^^^LOVASTATIN 40MG TAB^LDL CHOLESTEROL^45.8 MG/DL^^3010807.1028^

^605^000000250^^^^LOVASTATIN 40MG TAB^SGPT (ALT)^39 IU/L^^3010807.1028^

^605^000000250^^^^METFORMIN HCL 850MG TAB^GLUCOSE^193 MG/DL^H^3010807.1028^

^605^000000250^^^^METFORMIN HCL 850MG TAB^SGOT (AST)^16 IU/L^^3010807.1028^

^605^000000250^^^^METFORMIN HCL 850MG TAB^HEMOGLOBIN A1C (LAB)^5.9 % ^^3010807.

102802^

^605^000000250^^^^METFORMIN HCL 850MG TAB^SGPT (ALT)^39 IU/L^^3010807.1028^

^605^000008909^^^^DILTIAZEM (TIAZAC) 240MG SA CAP^CREATININE^0.8 MG/DL^^3010523

.081317^

^605^000008909^^^^LOVASTATIN 40MG TAB^CHOLESTEROL^183 MG/DL^^3010523.081317^

^605^000008909^^^^LOVASTATIN 40MG TAB^SGOT (AST)^19 IU/L^^3010523.081317^

^605^000008909^^^^LOVASTATIN 40MG TAB^TRIGLYCERIDE^99 MG/DL^^3010523.081317^

Subj: V. 4.0 PBMLR 30109 1/2 605 LOMA LINDA VA \[#7633\] Page 2

-------------------------------------------------------------------------------

^605^000008909^^^^LOVASTATIN 40MG TAB^HDL CHOLESTEROL^65 MG/DL^^3010523.081317^

^605^000008909^^^^LOVASTATIN 40MG TAB^LDL CHOLESTEROL^98.2 MG/DL^^3010523.08131

7^

^605^000008909^^^^LOVASTATIN 40MG TAB^SGPT (ALT)^43 IU/L^^3010523.081317^

^605^000009969^^^^FOSINOPRIL NA 40MG TAB^CREATININE^0.9 MG/DL^^3010208.102846^

^605^000009969^^^^FOSINOPRIL NA 40MG TAB^POTASSIUM^4.6 mmol/L^^3010208.102846^

^605^000009969^^^^ATORVASTATIN CA 80MG TAB^CHOLESTEROL^194 MG/DL^^3010208.10284

6^

^605^000009969^^^^ATORVASTATIN CA 80MG TAB^SGOT (AST)^20 IU/L^^3010208.102846^

^605^000009969^^^^ATORVASTATIN CA 80MG TAB^TRIGLYCERIDE^205 MG/DL^H^3010208.102

846^

^605^000009969^^^^ATORVASTATIN CA 80MG TAB^HDL CHOLESTEROL^35 MG/DL^^3010208.10

2846^

^605^000009969^^^^ATORVASTATIN CA 80MG TAB^LDL CHOLESTEROL^118.0 MG/DL^^3010208

.102846^

^605^000009969^^^^ATORVASTATIN CA 80MG TAB^SGPT (ALT)^45 IU/L^^3010208.102846^

^605^000001251^^^^LISINOPRIL 20MG TAB^CREATININE^1.4 MG/DL^^3010829.163356^

^605^000001251^^^^LISINOPRIL 20MG TAB^POTASSIUM^4.7 mmol/L^^3010829.163356^

^605^000001251^^^^RANITIDINE HCL 150MG TAB^CREATININE^1.4 MG/DL^^3010829.163356

^

Example: Prescription – Detail Report Message

Subj: V. 4.0 PBMLR 30109 2/2 605 LOMA LINDA VA \[#7634\] 07/16/04@19:19

12516 lines

From: PBMPHARMACIST,SIX In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^000009152^^^^GLYBURIDE 5MG TAB^GLUCOSE^211 MG/DL^H^3010709.210734^

^605^000009152^^^^GLYBURIDE 5MG TAB^SGOT (AST)^14 IU/L^^3010709.210734^

^605^000009152^^^^GLYBURIDE 5MG TAB^HEMOGLOBIN A1C (LAB)^7.9 % ^H^3010709.09593

^

^605^000009152^^^^GLYBURIDE 5MG TAB^SGPT (ALT)^30 IU/L^^3010709.210734^

^605^000009152^^^^METFORMIN HCL 500MG TAB^GLUCOSE^211 MG/DL^H^3010709.210734^

^605^000009152^^^^METFORMIN HCL 500MG TAB^SGOT (AST)^14 IU/L^^3010709.210734^

^605^000009152^^^^METFORMIN HCL 500MG TAB^HEMOGLOBIN A1C (LAB)^7.9 % ^H^3010709

.09593^

^605^000009152^^^^METFORMIN HCL 500MG TAB^SGPT (ALT)^30 IU/L^^3010709.210734^

^605^000009152^^^^SIMVASTATIN 80MG TAB^CHOLESTEROL^153 MG/DL^^3010709.095931^

^605^000009152^^^^SIMVASTATIN 80MG TAB^SGOT (AST)^14 IU/L^^3010709.210734^

^605^000009152^^^^SIMVASTATIN 80MG TAB^TRIGLYCERIDE^637 MG/DL^H^3010709.095931^

^605^000009152^^^^SIMVASTATIN 80MG TAB^HDL CHOLESTEROL^23 MG/DL^L^3010709.09593

1^

^605^000009152^^^^SIMVASTATIN 80MG TAB^LDL CHOLESTEROL^canc MG/DL^^3010709.0959

31^

^605^000009152^^^^SIMVASTATIN 80MG TAB^SGPT (ALT)^30 IU/L^^3010709.210734^

Example: Prescription – Laboratory Statistical Summary Message

Subj: V. 4.0 PBMLR 30109 605 LOMA LINDA VA \[#7641\] 07/16/04@19:19

6 lines

From: PBMPHARMACIST,THREE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Laboratory Statistical Summary

SEP 1,2001 through SEP 30,2001 for LOMA LINDA VA

Total Patients 5625

Total Laboratory Tests 24254

Example: Prescription – Laboratory Data Summary Message

Subj: V. 4.0 PBMLR 30109 605 LOMA LINDA VA \[#7642\] 07/16/04@19:19

24260 lines

From: PBMPHARMACIST,THREE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Laboratory Data Summary

SEP 1,2001 through SEP 30,2001 for LOMA LINDA VA

Patient SSN VA CODE Laboratory Results Flag Date/Time Taken

------------------------------------------------------------------------------

000006505 CV800 CREATININE 0.8 MG/DL 08/09/01 0752

POTASSIUM 4.9 mmol/L 08/09/01 0752

GA301 CREATININE 0.8 MG/DL 08/09/01 0752

000008660 CV350 CHOLESTEROL 113 MG/DL L 08/30/01 1021

SGOT (AST) 16 IU/L 08/30/01 1021

TRIGLYCERIDE 95 MG/DL 08/30/01 1021

HDL CHOLESTEROL 32 MG/DL 08/30/01 1021

LDL CHOLESTEROL 62.0 MG/DL 08/30/01 1021

SGPT (ALT) 29 IU/L L 08/30/01 1021

CV800 CREATININE 1.0 MG/DL 08/30/01 1021

POTASSIUM 4.5 mmol/L 08/30/01 1021

GA301 CREATININE 1.0 MG/DL 08/30/01 1021

000000300 CV800 CREATININE 1.2 MG/DL 04/13/01 1309

  
Example: Prescription – Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY

\[#7655\] 07/16/04@19:19 7 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Prescription JUL 16,2004@16:57 JUL 16,2004@19:14 2 hrs, 17 min

Laboratory Results JUL 16,2004@19:14 JUL 16,2004@19:19 0 hrs, 5 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Prescription – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI

\[#7656\] 07/16/04@19:19 8 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

Prescription 123342 13

Prescription MultiDose 8 1

Laboratory Results 27516 2

*(This page included for two-sided copying.)*

## Procurement Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality created in recent enhancements provides a means to break down all procurement data by division or outpatient site.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications are defined in detail in the tables below.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>PROCUREMENT STATISTICS DATA FIELD SPECIFICATIONS<br />
(IFCAP FILE #442)</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender (facility number)</td>
<td>MEDICAL CENTER DIVISION file (#40.8)<br />
<br />
or<br />
<br />
OUTPATIENT SITE file (#59)</td>
<td><p>FACILITY NUMBER field (#1)</p>
<p>or<br />
<br />
SITE NUMBER field (#.06)</p></td>
<td>2</td>
<td>The software shall use the pharmacy location mappings to determine the division or outpatient site.</td>
</tr>
<tr class="even">
<td>Breakdown by Outpatient Division or Inpatient Site not possible indicator</td>
<td></td>
<td></td>
<td>3</td>
<td>If records could not be broken down to an outpatient site or inpatient division, an “H” is sent.</td>
</tr>
<tr class="odd">
<td>P.O. Date</td>
<td></td>
<td></td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>VA Product Name</td>
<td>DRUG file (#50)</td>
<td>VA PRODUCT NAME field (#21)</td>
<td>5</td>
<td>If no data found, send “Unknown VA Product Name”.</td>
</tr>
<tr class="odd">
<td>VA Drug Class</td>
<td>DRUG file (#50)</td>
<td>VA CLASSIFICATION field (#2)</td>
<td>6</td>
<td></td>
</tr>
<tr class="even">
<td>Generic Drug Name</td>
<td>DRUG file (#50)</td>
<td>GENERIC NAME field (#.01)</td>
<td>7</td>
<td></td>
</tr>
<tr class="odd">
<td>P.O. Description</td>
<td></td>
<td></td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>NDC</td>
<td>Drug file (#50)</td>
<td>NDC field (#31)</td>
<td>9</td>
<td>If no data found, send “No NDC”.</td>
</tr>
<tr class="odd">
<td>NO DATA</td>
<td></td>
<td></td>
<td>10</td>
<td></td>
</tr>
<tr class="even">
<td>NO DATA</td>
<td></td>
<td></td>
<td>11</td>
<td></td>
</tr>
<tr class="odd">
<td>Dispense Unit</td>
<td>DRUG file (#50)</td>
<td>DISPENSE UNIT field (#14.5)</td>
<td>12</td>
<td></td>
</tr>
<tr class="even">
<td>Unit of Purchase</td>
<td></td>
<td></td>
<td>13</td>
<td></td>
</tr>
<tr class="odd">
<td>Packaging Multiple</td>
<td></td>
<td></td>
<td>14</td>
<td></td>
</tr>
<tr class="even">
<td>DISPENSING UNIT file (#445)</td>
<td></td>
<td></td>
<td>15</td>
<td></td>
</tr>
<tr class="odd">
<td>Disp. Unit Conversion Factor</td>
<td></td>
<td></td>
<td>16</td>
<td></td>
</tr>
<tr class="even">
<td>Total Quantity</td>
<td></td>
<td></td>
<td>17</td>
<td></td>
</tr>
<tr class="odd">
<td>Actual Unit Cost</td>
<td></td>
<td></td>
<td>18</td>
<td></td>
</tr>
<tr class="even">
<td>Total Cost</td>
<td></td>
<td></td>
<td>19</td>
<td>Formula = Qty Invoice/ Disp Units Per Order Unit * Price Per Order Unit</td>
</tr>
<tr class="odd">
<td>Vendor Name</td>
<td>DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td>VENDOR NAME sub-field (#1)</td>
<td>20</td>
<td></td>
</tr>
<tr class="even">
<td>NO DATA</td>
<td></td>
<td></td>
<td>21</td>
<td></td>
</tr>
<tr class="odd">
<td>Fund Control Point</td>
<td></td>
<td></td>
<td>22</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>PROCUREMENT STATISTICS DATA FIELD SPECIFICATIONS<br />
(PRIME VENDOR FILE #58.811)</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender (facility number)</td>
<td><p>Medical Center Division file (#40.8)</p>
<p>or</p>
<p>Outpatient Site file (#59)</p></td>
<td><p>Facility Number field (#1)</p>
<p>or</p>
<p>Site Number field (#.06)</p></td>
<td>2</td>
<td>The software shall use the mapped pharmacy locations to determine the division or outpatient site.</td>
</tr>
<tr class="even">
<td>Breakdown by Outpatient Division or Inpatient Site not possible indicator</td>
<td></td>
<td></td>
<td>3</td>
<td>If records could not be broken down to an outpatient site or inpatient division, an “H” is sent.</td>
</tr>
<tr class="odd">
<td>Verification Date (#58.111)</td>
<td>LINE ITEM DATA multiple (#5) within the INVOICE DATA multiple (#2) within the DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td>Date verified sub-field (#7)</td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>VA Product Name</td>
<td>Drug file (#50)</td>
<td>VA Product Name field (#21)</td>
<td>5</td>
<td></td>
</tr>
<tr class="odd">
<td>VA Drug Class</td>
<td>Drug file (#50)</td>
<td>VA Classification field (#2)</td>
<td>6</td>
<td></td>
</tr>
<tr class="even">
<td>Generic Drug Name or Supply Description</td>
<td><p>Drug file (#50)</p>
<p>Or</p>
<p>LINE ITEM DATA multiple (#5) within the INVOICE DATA multiple (#2) within the DRUG ACCOUNTABILITY ORDER file (#58.811)</p></td>
<td><p>Generic name field (#.01)</p>
<p>Drug sub-field (#1) (can be pointer to file #50 or free text)</p></td>
<td>7</td>
<td></td>
</tr>
<tr class="odd">
<td>NO DATA</td>
<td></td>
<td></td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>NDC</td>
<td>LINE ITEM DATA multiple (#5) within the INVOICE DATA multiple (#2) within the DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td>NDC sub-field (#13) (for a drug) or “S” concatenated with the UPC if supply item</td>
<td>9</td>
<td>If no data is found in field #13, then the NDC is extracted from the drug file #50, field #31. If no data is found in field #31, “No NDC” is sent.</td>
</tr>
<tr class="odd">
<td>VSN</td>
<td>LINE ITEM DATA multiple (#5) within the INVOICE DATA multiple (#2) within the DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td>VSN sub-field (#14)</td>
<td>10</td>
<td></td>
</tr>
<tr class="even">
<td>UPC</td>
<td>LINE ITEM DATA multiple (#5) within the INVOICE DATA multiple (#2) within the DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td>UPC sub-field (#15)</td>
<td>11</td>
<td></td>
</tr>
<tr class="odd">
<td>Dispense Unit</td>
<td>Drug file (#50)</td>
<td>Dispense Unit field (#14.5)</td>
<td>12</td>
<td></td>
</tr>
<tr class="even">
<td>Order Unit</td>
<td>Order Unit file (#51.5)</td>
<td>Abbreviation field (#.01)</td>
<td>13</td>
<td></td>
</tr>
<tr class="odd">
<td>NO DATA</td>
<td></td>
<td></td>
<td>14</td>
<td></td>
</tr>
<tr class="even">
<td>NO DATA</td>
<td></td>
<td></td>
<td>15</td>
<td></td>
</tr>
<tr class="odd">
<td>Disp Unit Per Order Unit</td>
<td>Synonym multiple (#9) within DRUG file (#50)</td>
<td>Dispense Units per Order Unit sub-field (#403)</td>
<td>16</td>
<td></td>
</tr>
<tr class="even">
<td>Qty Invoiced</td>
<td>LINE ITEM DATA multiple (#5) and ADJUSTMENTS multiple (#9) within the INVOICE DATA multiple (#2) within the DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td>Quantity Invoiced sub-field (#2) in conjunction with Verifier Adjustment field (#5)</td>
<td>17</td>
<td>If an adjustment has been made, the adjustment is added to the quantity invoiced; otherwise the quantity invoiced is extracted.</td>
</tr>
<tr class="odd">
<td>Price Per Order Unit</td>
<td>LINE ITEM DATA multiple (#5) and ADJUSTMENTS multiple (#9) within the INVOICE DATA multiple (#2) within the DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td><p>Verifier Adjustment sub-field (#5)</p>
<p>Price Per Order Unit sub-field (#4)</p></td>
<td>18</td>
<td>If there has been a Price Per Order Unit adjustment made, that value is extracted; otherwise the Original Price Per Order Unit.</td>
</tr>
<tr class="even">
<td>Total Cost</td>
<td></td>
<td></td>
<td>19</td>
<td>Formula = Qty Invoiced * Price Per Order Unit.</td>
</tr>
<tr class="odd">
<td>Vendor name</td>
<td>DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td>Vendor Name sub-field (#1)</td>
<td>20</td>
<td></td>
</tr>
<tr class="even">
<td>Invoice Number</td>
<td>INVOICE DATA multiple (#2) within the DRUG ACCOUNTABILITY ORDER file (#58.811)</td>
<td>Invoice Number sub-field (#.01)</td>
<td>21</td>
<td></td>
</tr>
<tr class="odd">
<td>NO DATA</td>
<td></td>
<td></td>
<td>22</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>PROCUREMENT STATISTICS DATA FIELD SPECIFICATIONS<br />
(DRUG ACCOUNTABILITY FILE #58.81)</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender (facility number)</td>
<td>Medical Center Division file (#40.8)<br />
<br />
or<br />
<br />
Outpatient Site file (#59)</td>
<td><p>Facility Number field (#1)</p>
<p>or<br />
<br />
Site Number field (#.06)</p></td>
<td>2</td>
<td>The software shall use the pharmacy location mappings to determine the division or outpatient site.</td>
</tr>
<tr class="even">
<td>Breakdown by Outpatient Division or Inpatient Site not possible indicator</td>
<td></td>
<td></td>
<td>3</td>
<td>If records could not be broken down to an outpatient site or inpatient division, an “H” is sent.</td>
</tr>
<tr class="odd">
<td>Transaction Date</td>
<td>Drug Accountability Transaction file (#58.81)</td>
<td>Date/time field (#3)</td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>VA Product Name</td>
<td>Drug file (#50)</td>
<td>VA Product Name field (#21)</td>
<td>5</td>
<td>If no data found, send “Unknown VA Product Name”.</td>
</tr>
<tr class="odd">
<td>VA Drug Class</td>
<td>Drug file (#50)</td>
<td>VA Classification field (#2)</td>
<td>6</td>
<td></td>
</tr>
<tr class="even">
<td>Generic Drug Name</td>
<td>Drug file (#50)</td>
<td>Generic name field (#.01)</td>
<td>7</td>
<td>If no data found, send “Unknown Generic Name”.</td>
</tr>
<tr class="odd">
<td>NO DATA</td>
<td></td>
<td></td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>NDC</td>
<td>Drug file (#50)</td>
<td>NDC field (#31)</td>
<td>9</td>
<td>If no data found, send “No NDC”.</td>
</tr>
<tr class="odd">
<td>NO DATA</td>
<td></td>
<td></td>
<td>10</td>
<td></td>
</tr>
<tr class="even">
<td>NO DATA</td>
<td></td>
<td></td>
<td>11</td>
<td></td>
</tr>
<tr class="odd">
<td>Dispense Unit</td>
<td>Drug file (#50)</td>
<td>Dispense Unit field (#14.5)</td>
<td>12</td>
<td></td>
</tr>
<tr class="even">
<td>Order Unit</td>
<td>Order Unit file (#51.5)</td>
<td>Abbreviation field (#.01)</td>
<td>13</td>
<td></td>
</tr>
<tr class="odd">
<td>NO DATA</td>
<td></td>
<td></td>
<td>14</td>
<td></td>
</tr>
<tr class="even">
<td>NO DATA</td>
<td></td>
<td></td>
<td>15</td>
<td></td>
</tr>
<tr class="odd">
<td>Disp Unit Per Order Unit</td>
<td>Drug file (# 50)</td>
<td>DISPENSE UnitS Per Order Unit field (#15)</td>
<td>16</td>
<td></td>
</tr>
<tr class="even">
<td>Qty Invoiced</td>
<td>Drug Accountability Transaction file (#58.81)</td>
<td>Quantity field (#5)</td>
<td>17</td>
<td></td>
</tr>
<tr class="odd">
<td>Price Per Order Unit</td>
<td>Drug file (#50)</td>
<td>Price Per Order Unit field (#13)</td>
<td>18</td>
<td></td>
</tr>
<tr class="even">
<td>Total Cost</td>
<td></td>
<td></td>
<td>19</td>
<td>Formula = Qty Invoice/ Disp Units Per Order Unit * Price Per Order Unit</td>
</tr>
<tr class="odd">
<td>Manufacturer</td>
<td>Drug Accountability Transaction file (#58.81)</td>
<td>Manufacturer field (#12)</td>
<td>20</td>
<td></td>
</tr>
<tr class="even">
<td>Invoice Number</td>
<td>Drug Accountability Transaction file (#58.81)</td>
<td>Prime Vendor Invoice field (#71)</td>
<td>21</td>
<td></td>
</tr>
<tr class="odd">
<td>NO DATA</td>
<td></td>
<td></td>
<td>22</td>
<td></td>
</tr>
</tbody>
</table>

Within the Procurement extract, procurement data is extracted from the IFCAP file (#442), the DRUG ACCOUNTABILITY file (#58.81), and the DRUG ACCOUNTABILITY ORDER (Prime Vendor) file (#58.811). How much or how little data is extracted is dependent on what is implemented at the facility.

Procurement data from the IFCAP file (#442) is limited to transactions with a cost center of 822400 (Pharmacy) and 828100 (SPD). Only completed prime vendor invoice data from the DRUG ACCOUNTABILITY ORDER (Prime Vendor) file (#58.811) will be extracted. Procurement data with dispensing transaction type of “1” (Receipt into Pharmacy) will be extracted from the DRUG ACCOUNTABILITY file (#58.81).

Medical Center Divisions are selected from the MEDICAL CENTER DIVISION file (#40.8) NAME field (#.01). Outpatient Sites are selected from the OUTPATIENT SITE file (#59) NAME field (#.01). The user may select an active or inactive Outpatient Site. \*\*Inactive\*\* shall be displayed next to a selected inactive Outpatient Site.

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown below.

Example: Procurement – Detail Report Message

Subj: V. 4.0 PBMPR 30109 1/1 605 JERRY L PETTIS VAMC \[#7558\]

07/16/04@13:56 921 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^CATHETER FOLEY 25F

^0^O^3001016^xxxxxxxxx^5000000019V796730^800.00^^^^^^^^^^^^^^^^^^^^9

R^No NDC^^^^CS^12^^^5^129.24^646.2^PBMVENDOR ONE^^053 PHARMACY S&S^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^AEROCHAMBER AEROSO

L INHALER^No NDC^^^^CS^50^^^6^281.25^1687.5^PBMVENDOR TWO^^053 PHARMACY S&S^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^FOAM ALLEVYN 8X8 L

OC; (NEW ITEM)^No NDC^^^^CS^20^^^1^216.54^216.54^PBMVENDOR THREE^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^COVER - AMEDIC STE

RILE ULTRASOUND TRANSDUCER. STER^No NDC^^^^BX^20^^^1^220.00^220^PBMVENDOR FOUR^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^FILM POLAROID TWIN

PAK HIGH DEFINITION 600(LOC: 1C^No NDC^^^^EA^1^^^10^15.38^153.8^PBMVENDOR FOUR^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^BLADE SHARP POINT

3.0MM MICROSURGICALSLIT KNIFE (L^No NDC^^^^BX^6^^^3^84.00^252^PBMVENDOR FIVE^^074 SPD^

Subj: V. 4.0 PBMPR 30109 1/1 605 JERRY L PETTIS VAMC \[#7558\] Page 2

-------------------------------------------------------------------------------

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^CATHETER BALLOON P

OWERFLEX PLUS 5FR 8MM X 4CM X 80^No NDC^^^^EA^1^^^3^185.00^555^PBMVENDOR SIX^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^CATHETER BALLOON D

ILATION POWERFLEX PLUS 7MM X 2CM^No NDC^^^^EA^1^^^2^185^370^PBMVENDOR SIX^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^PATTIES SPONGE X-R

AY 1/2 X 1 1/2 ^No NDC^^^^CS^200^^^2^92.77^185.54^PBMVENDOR SIX^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^CATHETER 24FR 30CC

SIMPLASTIC 3 WAY (LOC: 02-C)^No NDC^^^^BX^10^^^1^135.55^135.55^PBMVENDOR SEVEN^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^SPLINT SYSTEM ORTH

O-GLASS 4X15" ROLL2RL/CS (LOC: 4^No NDC^^^^CS^2^^^2^154.5^309^PBMVENDOR EIGHT^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^LEADWIRE LW SPCH S

TANDARD PINCH 40"^No NDC^^^^PG^5^^^5^36.43^182.15^PBMVENDOR NINE^^074 SPD^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^CATHETER PRUITT OC

CULSION IRRIGATION SZ 5^No NDC^^^^EA^1^^^2^70.00^140^PBMVENDOR TEN^^074 SPD^

Example: Procurement - Data Records Not Broken Down To Outpatient Site or Inpatient Division Message

Subj: V. 4.0 PBMPR 30109 1/1 605 JERRY L PETTIS VAMC \[#8728\]

08/11/04@15:22 921 lines

From: PBMPHARMACIST,TWO In 'WASTE' basket. Page 1

-------------------------------------------------------------------------------

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^CATHETER FOLEY 25F

R^No NDC^^^^CS^12^^^5^129.24^646.2^PBMVENDOR ONE^^053 PHARMACY S&S^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^AEROCHAMBER AEROSO

L INHALER^No NDC^^^^CS^50^^^6^281.25^1687.5^PBMVENDOR TWO^^053 PHARMACY S&S^

^605^H^3010904^Unknown VA Product Name^^Unknown Generic Name^FOAM ALLEVYN 8X8 L

OC; (NEW ITEM)^No NDC^^^^CS^20^^^1^216.54^216.54^PBMVENDOR THREE^^074 SPD^

Example: Procurement – Statistical Summary Message

Subj: V. 4.0 PBMPR 30109 605 JERRY L PETTIS VAMC \[#7559\] 07/16/04@13:56 6 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

---------------------------------------------------------------------------------

Procurement Statistical Summary SEP 1,2001 through SEP 30,2001@24:00 for JERRY L PETTIS VAMC

Total of Drug/Supply Items: 687

Total Cost: \$ 263526.69

Example: Procurement – Data Summary Message

Subj: V. 4.0 PBMPR 30109 605 JERRY L PETTIS VAMC \[#7560\] 07/16/04@13:56 668 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Procurement Data Summary

SEP 1,2001 through SEP 30,2001@24:00 for JERRY L PETTIS VAMC

Dispense Total Total

Drug/Supply Name Unit Qty Cost

------------------------------------------------------------------------------

' 1 152.00

\(1\) IFCAP \#61 1 CASE @ \$132.86 0 0.00

. SPLINT FINGER SMALL 4 PRONG 1 13.53

1 EACH VSN# LPEA-681 VEST ERGO 0 0.00

1004 - 2" SUPERCEL 2 320.00

2.7MM TI CORTEX SCREW SELF-TAP 8 242.00

3.5MM TI CORTEX SCREW SELF-TAP 8 118.00

3000ML EMPTY AD SURE CONTAINER 20 4519.60

33 BAGS OF SANITARY NAPKINS 0 0.00

4002 - 2" THERMAL PAPER 2 390.00

ACCU-CHEK GOV'T OUTPT METER KI 100 20400.00

ACCU-CHEK SAFE-T-PRO LANCET FO 54 1458.00

*\[A portion of this statistical data message has been removed to save space.\]*

Subj: V. 4.0 PBMPR 30109 605 JERRY L PETTIS VAMC \[#7560\] Page 34

-------------------------------------------------------------------------------

WIRE GUIDE TEFLON CURVED MOVAB 68 1275.00

WIRE HYDROSTEER .038 180CM 1 225.00

WIRE KIRSCHNER SS 22.9CM PLAIN 1 33.00

WIRE MC 3MM J .035 X 150CM X S 1 83.20

WIRE STARTER ROSEN 35-180-1.5 19 351.50

WRIST JACK FRACTURE REDUCTION 3 3600.00

WRIST SPLINT RIGHT X LARGE FOR 10 41.60

------------------------------------------------------------------------------

Total 271537 263526.6

  
Example: Procurement –Unmapped Locations Message

Subj: PBM Unmapped Locations for SEP 1,2001 to SEP 30,2001 from 605 LOM \[#7561\]

07/16/04@13:56 7 lines

From: PBMPHARMACIST,NINE In 'IN' basket. Page 1

---------------------------------------------------------------------------------

The locations listed below have not been mapped to a Medical Center Division or

Outpatient Site. All data extracted from these locations have been attributed to

605 LOMA LINDA

DA Pharmacy Locations:

There are no unmapped DA Pharmacy Locations for the dates of this extract

Example: Procurement –Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY \[#7562\]

07/16/04@13:56 6 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

----------------------------------------------------------------------------------

Procurement JUL 16,2004@13:55 JUL 16,2004@13:56 0 hrs, 1 min

----------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the IV,

Unit Dose, Prescription, and Patient Demographics extracts are run concurrently.

## Controlled Substances Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality created in recent enhancements provides a means to break down all Controlled Substance dispensing workload by division or outpatient site.

Controlled Substances data is extracted by dispensing transaction records. Only dispensing transaction types of “17” (Logged for Patient) and “2” (Dispensed from Pharmacy) will be extracted.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications are defined in detail in the table below.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>CONTROLLED SUBSTANCES STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender (facility number)</td>
<td><p>Medical Center Division file (#40.8)</p>
<p>or</p>
<p>Outpatient Site file (#59)</p></td>
<td><p>Facility Number field (#1)</p>
<p>or</p>
<p>Site Number field (#.06)</p></td>
<td>2</td>
<td>The software shall use the NAOU mappings to determine the sending division or outpatient site.</td>
</tr>
<tr class="even">
<td>Breakdown by Outpatient Division or Inpatient Site not possible indicator</td>
<td></td>
<td></td>
<td>3</td>
<td>If records could not be broken down to an outpatient site or inpatient division, an “H” is sent.</td>
</tr>
<tr class="odd">
<td>Dispense (transaction) date</td>
<td>Drug Accountability Transaction file (#58.81)</td>
<td>Date/time field (#3)</td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>NAOU</td>
<td>Drug Accountability STATS file (#58.8)</td>
<td>Pharmacy Location field (#.01)</td>
<td>5</td>
<td></td>
</tr>
<tr class="odd">
<td>Patient SSN</td>
<td>Patient file (#2)</td>
<td>Social Security Number field (#.09)</td>
<td>6</td>
<td></td>
</tr>
<tr class="even">
<td>VA Product Name</td>
<td>Drug file (#50)</td>
<td>VA Product Name field (#21)</td>
<td>7</td>
<td></td>
</tr>
<tr class="odd">
<td>VA Drug Class</td>
<td>Drug file (#50)</td>
<td>VA Classification field (#2)</td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>Generic Drug Name</td>
<td>Drug file (#50)</td>
<td>Generic name field (#.01)</td>
<td>9</td>
<td></td>
</tr>
<tr class="odd">
<td>Formulary/Non-Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>LOCAL Non formulary field (#51)</td>
<td>10</td>
<td>If field set to “1”, the program sends “N/F”.</td>
</tr>
<tr class="even">
<td>National Formulary Indicator</td>
<td>VA Product file (#50.68)</td>
<td>National Formulary Indicator field (#17)</td>
<td>11</td>
<td>Send “1” for Yes; “0” for No; otherwise null if no data found.</td>
</tr>
<tr class="odd">
<td>National Formulary Restriction</td>
<td>NATIONAL FORMULARY RESTRICTION multiple (#18) within the VA Product file (#50.68)</td>
<td>National Formulary Restriction sub- field (#.01)</td>
<td>12</td>
<td>If data is found, send “1”; otherwise “0”.</td>
</tr>
<tr class="even">
<td>NDC</td>
<td>Drug file (#50)</td>
<td>NDC field (#31)</td>
<td>13</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Breakdown Unit</p>
<p>OR</p>
<p>Dispense unit</p></td>
<td><p>Drug multiple (#10) within the DRUG Accountability Stats file (#58.8)</p>
<p>or</p>
<p>DRUG file (#50)</p></td>
<td><p>Breakdown Unit sub-field (#7)</p>
<p>or</p>
<p>Dispense Unit sub-field (#14.5)</p></td>
<td>14</td>
<td><p>Breakdown unit is used for dispensing type=2 transactions.</p>
<p>Dispense unit is used for dispensing type=17 transactions.</p></td>
</tr>
<tr class="even">
<td>Package size (dispensing type =2 only)</td>
<td>Drug multiple (#10) within the DRUG Accountability Stats file (#58.8)</td>
<td>Package Size sub-field (#8)</td>
<td>15</td>
<td>Extracted for dispensing type=2 transactions.</td>
</tr>
<tr class="odd">
<td>Unit Cost</td>
<td>Drug file (#50)</td>
<td>Price Per Dispense Unit field (#16)</td>
<td>16</td>
<td></td>
</tr>
<tr class="even">
<td>Total Qty Dispensed (NAOU) or Total Doses Dispensed (SSN)</td>
<td>Drug Accountability Transaction file (#58.81)</td>
<td><p>Quantity field (#5)</p>
<p>New Quantity field (#50) (if adjustments are made)</p></td>
<td>17</td>
<td>All quantities or doses dispensed within the timeframe specified will be totaled.</td>
</tr>
<tr class="odd">
<td>VISN Formulary Indicator</td>
<td>Drug file (#50)</td>
<td>VISN Non-Formulary field (#52)</td>
<td>18</td>
<td>If “1” is found, send N/F; otherwise null if no data is found.</td>
</tr>
<tr class="even">
<td>DEA Special Handling</td>
<td>Drug file (#50)</td>
<td>DEA, Special Hdlg field (#3)</td>
<td>19</td>
<td></td>
</tr>
<tr class="odd">
<td>Patient ICN</td>
<td>PATIENT file (#2)</td>
<td><p>INTEGRATION CONTROL NUMBER field</p>
<p>(# 991.01)</p>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
<p>(Values in both fields are concatenated with a ‘V’.)</p></td>
<td>20</td>
<td><p>Free Text.<br />
Example: “1010185893V199552”</p>
<p>If an ICN does not exist, send null.</p></td>
</tr>
</tbody>
</table>

Within the CS extract, Medical Center Divisions are selected from the MEDICAL CENTER DIVISION file (#40.8) NAME field (#.01). Outpatient Sites are selected from the OUTPATIENT SITE file (#59) NAME field (#.01). The user may select an active or inactive Outpatient Site. \*\*Inactive\*\* shall be displayed next to a selected inactive Outpatient Site.

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

Example: Controlled Substances – Detail Report Message

Subj: V. 4.0 PBMCS 30109 1/1 605 JERRY L PETTIS VAMC \[#7673\]

07/19/04@12:24 1091 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^H^3010902^INPATIENT^^CHLORDIAZEPOXIDE HCL 25MG CAP^CN302^CHLORDIAZEPOXIDE

HCL 25MG CAP U/D^^1^0^00615-0437-13^PACK^100^0.105^40^^4CL^^

^605^H^3010902^INPATIENT^^CODEINE 30MG/ACETAMINOPHEN 300MG TAB^CN101^ACETAMINOP

HEN 300MG/COD 30MG TAB^^1^0^00406-0484-01^BT^100^0.069^300^^3^^

^605^H^3010902^INPATIENT^^HYDROCODONE 5MG/ACETAMINOPHEN 500MG TAB^CN101^HYDROCO

DONE 5/ACETAMINOPHEN 500MG TAB^^1^0^00406-0357-05^TAB^100^0.015^300^^3C^^

^605^H^3010904^GI LAB^^MEPERIDINE HCL 50MG/ML INJ^CN101^MEPERIDINE HCL 50MG/ML

INJ TUBEX^1^1^0^00074-1178-31^PACK^10^0.357^20^N/F^2A^^

^605^H^3010904^GI LAB^^MEPERIDINE HCL 50MG/ML INJ^CN101^MEPERIDINE HCL 50MG/ML

INJ TUBEX^1^1^0^00074-1178-31^PACK^10^0.357^20^N/F^2A^^

^605^H^3010904^GI LAB^^MEPERIDINE HCL 50MG/ML INJ^CN101^MEPERIDINE HCL 50MG/ML

INJ TUBEX^1^1^0^00074-1178-31^PACK^10^0.357^20^N/F^2A^^

^605^H^3010904^GI LAB^^MEPERIDINE HCL 50MG/ML INJ^CN101^MEPERIDINE HCL 50MG/ML

INJ TUBEX^1^1^0^00074-1178-31^PACK^10^0.357^20^N/F^2A^^

^605^H^3010904^GI LAB^^MIDAZOLAM HCL 1MG/ML INJ^CN302^MIDAZOLAM 1MG/ML INJ 2ML

VI^^1^0^00004-1998-06^PACK^10^0.469^20^^4CLR^^

^605^H^3010904^GI LAB^^MIDAZOLAM HCL 1MG/ML INJ^CN302^MIDAZOLAM 1MG/ML INJ 2ML

VI^^1^0^00004-1998-06^PACK^10^0.469^20^^4CLR^^

Subj: V. 4.0 PBMCS 30109 1/1 605 JERRY L PETTIS VAMC \[#7673\] Page 2

-------------------------------------------------------------------------------

^605^H^3010904^GI LAB^^MIDAZOLAM HCL 1MG/ML INJ^CN302^MIDAZOLAM 1MG/ML INJ 2ML

VI^^1^0^00004-1998-06^PACK^10^0.469^20^^4CLR^^

^605^H^3010904^GI LAB^^MIDAZOLAM HCL 1MG/ML INJ^CN302^MIDAZOLAM 1MG/ML INJ 2ML

VI^^1^0^00004-1998-06^PACK^10^0.469^20^^4CLR^^

^605^H^3010904^RX WINDOW^^DIAZEPAM 5MG TAB^CN302^DIAZEPAM 5MG TAB^^1^0^00555-03

63-05^BT^500^0.048^3000^^4LCZ^^

^605^H^3010904^RX WINDOW^^HYDROCODONE 5MG/ACETAMINOPHEN 500MG TAB^CN101^HYDROCO

DONE 5/ACETAMINOPHEN 500MG TAB^^1^0^00406-0357-05^TAB^100^0.015^6000^^3C^^

^605^H^3010904^RX WINDOW^^MORPHINE SO4 10MG/5ML SOLN,ORAL^CN101^MORPHINE SULF 2

MG/ML ORAL SOLN 500ML^^1^0^00054-3785-63^BT^500^0.025^5000^^2AQ^^

^605^H^3010904^RX WINDOW^^OXYCODONE HCL 5MG/ACETAMINOPHEN 325MG TAB^CN101^OXYCO

DONE 5MG ACETAMINOP 325MG TAB^^1^0^60951-0602-70^BT^100^0.038^4800^^2AW^^

^605^H^3010904^RX WINDOW^^PROPOXYPHENE N 100MG TAB^CN101^PROPOXYPHENE N 100MG T

AB^1^0^0^00002-0353-03^BT^500^0.360^3000^^4C^^

^605^H^3010904^RX WINDOW^^OXYCODONE HCL 5MG TAB^CN101^OXYCODONE 5MG TAB^^1^0^00

054-4657-25^BT^100^0.091^5000^^2A^^

^605^H^3010904^3SICU^^METHADONE HCL 10MG TAB^CN101^METHADONE HCL 10MG TAB U/D^^

1^0^00054-8554-24^PACK^25^0.224^25^^2A^^

^605^H^3010904^3SE^^Unknown VA Product Name^CN101^HYDROMORPHONE 50MG/50ML PCA S

YRINGE^^^0^00338-9367-75^SYRINGE^1^9.500^3^^2^^

  
Example: Controlled Substances - Data Records Not Broken Down To Outpatient Site or  
Inpatient Division Message

Subj: V. 4.0 PBMCS 30109 1/1 605 JERRY L PETTIS VAMC \[#8731\]

08/11/04@15:23 1091 lines

From: PBMPHARMACIST,TWO In 'WASTE' basket. Page 1

-------------------------------------------------------------------------------

^605^H^3010902^INPATIENT^^CHLORDIAZEPOXIDE HCL 25MG CAP^CN302^CHLORDIAZEPOXIDE

HCL 25MG CAP U/D^^1^0^00615-0437-13^PACK^100^0.105^40^^4CL^^

^605^H^3010902^INPATIENT^^CODEINE 30MG/ACETAMINOPHEN 300MG TAB^CN101^ACETAMINOP

HEN 300MG/COD 30MG TAB^^1^0^00406-0484-01^BT^100^0.069^300^^3^^

^605^H^3010902^INPATIENT^^HYDROCODONE 5MG/ACETAMINOPHEN 500MG TAB^CN101^HYDROCO

DONE 5/ACETAMINOPHEN 500MG TAB^^1^0^00406-0357-05^TAB^100^0.015^300^^3C^^

^605^H^3010904^GI LAB^^MEPERIDINE HCL 50MG/ML INJ^CN101^MEPERIDINE HCL 50MG/ML

INJ TUBEX^1^1^0^00074-1178-31^PACK^10^0.357^20^N/F^2A^^

Example: Controlled Substances - Statistical Data Message

Subj: V. 4.0 PBMCS 30109 605 JERRY L PETTIS VAMC \[#7674\] 07/19/04@12:24

118 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Controlled Substance Statistical Data

SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

Breakdown Package Quantity

Drug Name Unit Size Dispensed

---------------------------------------------------------------------------

ACETAMINOP 120MG/COD 12MG/5ML ELIX BT 473 11352

ACETAMINOP 300MG/COD 30MG/12.5ML ELI U/D PACK 10 165

ACETAMINOPHEN 300MG/COD 30MG TAB BT 100 23220

ACETAMINOPHEN 300MG/COD 30MG TAB U/D PACK 10 1200

ACETAMINOPHEN 300MG/COD 60MG TAB BT 100 4800

ALPRAZOLAM 0.25MG TAB BT 500 1800

ALPRAZOLAM 0.25MG TAB U/D PACK 100 50

ALPRAZOLAM 0.5MG TAB BT 500 1500

ALPRAZOLAM 0.5MG TAB U/D PACK 100 80

ALPRAZOLAM 1MG TAB BT 500 1700

ASPIRIN 325MG/COD 30MG TAB \# BT 100 400

BUTORPHANOL TART 2MG/ML INJ pg 10 10

*\[A portion of this statistical data message has been removed to save space.\]*

Subj: V. 4.0 PBMCS 30109 605 JERRY L PETTIS VAMC \[#7674\] Page 6

-------------------------------------------------------------------------------

PHENOBARBITAL 100MG TAB BT 100 200

PHENOBARBITAL 15MG TAB U/D PACK 100 75

PHENOBARBITAL 30MG TAB \# BT 1000 3050

PHENOBARBITAL 30MG TAB U/D PACK 100 150

PROPOXYPHENE N 100MG TAB \#\* BT 500 3000

PROPOXYPHENE NAP 100MG TAB U/D \#\* PACK 100 26

TEMAZEPAM 15MG CAP BT 100 2000

TEMAZEPAM 15MG CAP U/D PB 100 1040

TESTOSTERONE CYP 200MG/ML INJ 10ML VI ML 1 35

TESTOSTERONE CYP 200MG/ML INJ 1ML VI VI 1 163

TESTOSTERONE TRANSDERMAL 5MG SYSTEM PG 30 1440

THIOPENTAL SOD 500MG/2.5% KIT 20ML KIT 1 15

ZOLPIDEM TARTRATE 10MG TAB \# BT 100 500

ZOLPIDEM TARTRATE 10MG U/D \# PG 10 5

ZOLPIDEM TARTRATE 5MG TAB U/D \# PG 100 15

---------------------------------------------------------------------------

Totals: 250098

\* Non-Formulary

\# Not on National Formulary

  
Example: Controlled Substances – AMIS Summary Report Message

Subj: V. 4.0 PBMCS 30109 605 JERRY L PETTIS VAMC \[#7675\] 07/19/04@12:24

13 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Controlled AMIS Summary for SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS V

AMC

INPATIENT CONTROLLED SUBSTANCE ORDERS:

ORDERS TOTAL AVE COST

DIVISION DISPENSED COST PER ORDER

-----------------------------------------------------------------------------

JERRY L PETTIS VA 1091 \$ 45761.75 \$ 41.94

-----------------------------------------------------------------------------

Total 1091 \$ 45761.75 \$ 41.94

Example: Controlled Substances –Unmapped Locations Message

Subj: PBM Unmapped Locations for SEP 1,2001 to SEP 30,2001 from 605 LOM

\[#7676\] 07/19/04@12:24 8 lines

From: PBMPHARMACIST,NINE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The locations listed below have not been mapped to a Medical Center

Division or Outpatient Site. All data extracted from these locations have

been attributed to 605 LOMA LINDA

NAOUs:

VAULT

METHADONE

Example: Controlled Substances –Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY

\[#7677\] 07/19/04@12:24 6 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Controlled Substance JUL 19,2004@12:23 JUL 19,2004@12:24 0 hrs, 1 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Controlled Substances – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI

\[#7678\] 07/19/04@12:24 6 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

Controlled Substances 1091 1

## Patient Demographics Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To decrease the running time of the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option, the ability to extract all patient records from the PATIENT file every month shall no longer be provided. The ability to extract all patient records from the PATIENT file shall be retained with the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option.

A new PBM PATIENT DEMOGRAPHICS file (#59.9) was added to PBM V. 4.0 as a repository in which to temporarily store new or updated patient demographic data in real time until the data is compiled and transmitted on a monthly basis to the PBM national database. Only one demographics record per patient shall be retained in the file for a reporting period. The data is retained in this file for 75 days, after which time it is purged.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications for the current Patient Demographic extract are provided in the table below. Pieces 20-29 can repeat. Multiple races may be entered.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>PATIENT DEMOGRAPHICS STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender (Facility #)</td>
<td>Institution file (#4)</td>
<td>Station Number field (#99)</td>
<td>2</td>
<td></td>
</tr>
<tr class="even">
<td>Date Extract Run</td>
<td></td>
<td></td>
<td>3</td>
<td></td>
</tr>
<tr class="odd">
<td>Date of Death</td>
<td>Patient file (#2)</td>
<td>Date of Death field (#.351)</td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>Date of Birth</td>
<td>Patient file (#2)</td>
<td>Date of Birth field (#.03)</td>
<td>5</td>
<td></td>
</tr>
<tr class="odd">
<td>Age</td>
<td></td>
<td>Calculated</td>
<td>6</td>
<td>This is a calculated value. It will be based on the Date of Birth and the date the patient demographic extract is run.</td>
</tr>
<tr class="even">
<td>Race (OLD)</td>
<td>Patient file (#2)</td>
<td>Race field (#.06)</td>
<td>7</td>
<td></td>
</tr>
<tr class="odd">
<td>Gender</td>
<td>Patient file (#2)</td>
<td>SEX field (#.02)</td>
<td>8</td>
<td>“M” for Male<br />
“F” for Female</td>
</tr>
<tr class="even">
<td>Primary eligibility code</td>
<td>Patient file (#2)</td>
<td>Primary Eligibility Code field (#.361)</td>
<td>9</td>
<td></td>
</tr>
<tr class="odd">
<td>Current Means Test Status</td>
<td>Patient file (#2)</td>
<td>Current Means Test Status field (#.14)</td>
<td>10</td>
<td></td>
</tr>
<tr class="even">
<td>Enrollment Priority</td>
<td>Patient Enrollment file (#27.11)</td>
<td>Enrollment Priority field (#.07)</td>
<td>11</td>
<td>“1” for Group 1<br />
“2” for Group 2<br />
“3” for Group 3<br />
“4” for Group 4<br />
“5” for Group 5<br />
“6” for Group 6<br />
“7” for Group 7</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>Patient file (#2)</td>
<td>Social Security Number field (#.09)</td>
<td>12</td>
<td></td>
</tr>
<tr class="even">
<td>ICN</td>
<td>Patient file (#2)</td>
<td>Integration Control Number field (#991.01)</td>
<td>13</td>
<td></td>
</tr>
<tr class="odd">
<td>Primary Care Provider SSN</td>
<td>New Person file (#200)</td>
<td>SSN field (#9)</td>
<td>14</td>
<td></td>
</tr>
<tr class="even">
<td>Primary Care Provider Local IEN</td>
<td>New Person file (#200)</td>
<td>Internal Entry Number (IEN)</td>
<td>15</td>
<td></td>
</tr>
<tr class="odd">
<td>Date Patient First Seen At Facility</td>
<td>Patient file (#2)</td>
<td>Date Entered Into File field (#.097)</td>
<td>16</td>
<td></td>
</tr>
<tr class="even">
<td>Date Patient First Provided Pharmacy Services</td>
<td>Pharmacy Patient file (#55)</td>
<td>First Service DATE field (#.07)</td>
<td>17</td>
<td></td>
</tr>
<tr class="odd">
<td>Whether Date Patient First Provided Pharmacy Services is Actual or Historical</td>
<td>Pharmacy Patient file (#55)</td>
<td>ACTUAL/ HISTORICAL FLAG field (#.08)</td>
<td>18</td>
<td>“A” for Actual<br />
“H” for Historical</td>
</tr>
<tr class="even">
<td>Ethnicity</td>
<td>EtHnicity information multiple (#6) within the Patient file (#2)</td>
<td>ETHNICITY INFORMATION field (#.01)</td>
<td>19</td>
<td></td>
</tr>
<tr class="odd">
<td>Race (new)</td>
<td>race information multiple (#2) within the Patient file (#2)</td>
<td>RACE INFORMATION field (#.01)</td>
<td>20-29</td>
<td></td>
</tr>
</tbody>
</table>

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

Example: Patient Demographics – Detail Report Message

Subj: V. 4.0 PBMPD 30109 1/20 605 JERRY L PETTIS VAMC \[#7732\]

07/20/04@18:22 10000 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^3040720^^2210000^83^^M^NSC^REQUIRED^^000003689^^^^^2870723^H^^^^^^^^^^^^

^605^3040720^^2521229^51^^M^NSC^MT COPAY EXEMPT^5^000002816^1002935271^00000611

8^1880^^2980322^H^^^^^^^^^^^^

^605^3040720^^2190822^84^WHITE, NOT OF HISPANIC ORIGIN^F^SERVICE CONNECTED 50%

to 100%^^1^000006505^1002191464^000007541^5547^^2870722^H^^^^^^^^^^^^

^605^3040720^^2570407^47^WHITE, NOT OF HISPANIC ORIGIN^M^SC LESS THAN 50%^^3^00

0005710^6050032171^^^^3011210^H^^^^^^^^^^^^

^605^3040720^^2500000^54^BLACK, NOT OF HISPANIC ORIGIN^M^^^^000007523^^^^^^^^^^

^^^^^^^^

^605^3040720^^2500210^54^WHITE, NOT OF HISPANIC ORIGIN^M^SERVICE CONNECTED 50%

to 100%^^1^000008107^1002929577^000005697^12166^^2870731^H^^^^^^^^^^^^

^605^3040720^^2430516^61^WHITE, NOT OF HISPANIC ORIGIN^M^NSC^MT COPAY REQUIRED^

7^000004336^^^^^2940219^H^^^^^^^^^^^^

^605^3040720^^2300000^74^^M^NSC^REQUIRED^^000008604^^^^^^^^^^^^^^^^^^

^605^3040720^^2380523^66^HISPANIC, BLACK^M^SERVICE CONNECTED 50% to 100%^^1^569

485541^1002927098^000002716^5504^^2870723^H^^^^^^^^^^^^

^605^3040720^^2220000^82^WHITE, NOT OF HISPANIC ORIGIN^M^SERVICE CONNECTED 50%

to 100%^^1^000000881^1002927422^000000814^12163^^2870725^H^^^^^^^^^^^^

*Report continued on next page*Example: Patient Demographics – Detail Report Message (continued)

Subj: V. 4.0 PBMPD 30109 1/20 605 JERRY L PETTIS VAMC \[#7732\] Page 2

-------------------------------------------------------------------------------

^605^3040720^^2380312^66^BLACK, NOT OF HISPANIC ORIGIN^M^NSC^REQUIRED^^00000532

7^1002969417^^^^^^^^^^^^^^^^^

^605^3040720^^2540714^50^^M^^^^000007650^^^^^^^^^^^^^^^^^^

^605^3040720^^2541004^49^WHITE, NOT OF HISPANIC ORIGIN^M^SERVICE CONNECTED 50%

to 100%^^1^000009865^1001267489^^^^2911114^H^^^^^^^^^^^^

^605^3040720^^2260517^78^^M^SC LESS THAN 50%^NO LONGER REQUIRED^3^000008563^100

7732203^^^^2870725^H^^^^^^^^^^^^

^605^3040720^^^^^M^NSC^REQUIRED^^000003514^^^^^^^^^^^^^^^^^^

^605^3040720^^2280223^76^WHITE, NOT OF HISPANIC ORIGIN^M^NSC^MT COPAY EXEMPT^^0

00004548^^^^^2870504^H^^^^^^^^^^^^

^605^3040720^^2220107^82^^M^SC LESS THAN 50%^NO LONGER REQUIRED^2^000006404^100

3690806^^^^^^^^^^^^^^^^^

^605^3040720^^2240000^80^^M^SC LESS THAN 50%^^^000001541^^^^^^^^^^^^^^^^^^

^605^3040720^^2460228^58^UNKNOWN^M^SERVICE CONNECTED 50% to 100%^NO LONGER REQU

IRED^1^000002529^1002945819^^^^2961231^H^^^^^^^^^^^^

^605^3040720^^2280503^76^BLACK, NOT OF HISPANIC ORIGIN^M^SC LESS THAN 50%^^^000

001662^^^^^2911024^H^^^^^^^^^^^^

^605^3040720^^2280109^76^WHITE, NOT OF HISPANIC ORIGIN^M^NSC^MT COPAY EXEMPT^5^

000009473^1002932146^000003389^12508^^2870725^H^^^^^^^^^^^^

^605^3040720^^2450610^59^^M^^^^000006444^^^^^^^^^^^^^^^^^^

Example: Patient Demographics –Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY

\[#7752\] 07/20/04@18:23 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Patient Demographics JUL 20,2004@14:05 JUL 20,2004@18:23 4 hrs, 18 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Patient Demographics – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI

\[#7753\] 07/20/04@18:23 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

Patient Demographics 193959 20

## Outpatient Visits Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to decrease the running time of the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option, the ability to extract a month’s worth of outpatient visit records from the VISIT file (#9000010) shall no longer be provided. The ability to extract outpatient visit records for any given timeframe directly from the VISIT file (#9000010) shall be retained with the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option.

Outpatient Visit records extracted on a daily basis shall be stored in the new PBM PATIENT DEMOGRAPHICS file (#59.9) until they are compiled for transmission when the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option is run.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications for the current Outpatient Visit extract are provided in the table below.

<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>OUTPATIENT VISITS STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender</td>
<td>Institution file (#4)</td>
<td>Station Number field (#99)</td>
<td>2</td>
<td></td>
</tr>
<tr class="even">
<td>Encounter Patient Status</td>
<td>Visit file (#9000010)</td>
<td>Patient Status In/Out field (#15002)</td>
<td>3</td>
<td><p>“I” will be sent for Inpatient “O” will be sent for Outpatient</p>
<p>If no data exists, a null value is sent.</p></td>
</tr>
<tr class="odd">
<td>Date of Visit</td>
<td>Visit file (#9000010)</td>
<td>Visit/Admit Date &amp; Time field (#.01)</td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>Patient SSN</td>
<td><p>Visit file<br />
(# 9000010)</p>
<p>Patient file (#2)</p></td>
<td>Social Security Number field (#.09)</td>
<td>5</td>
<td></td>
</tr>
<tr class="odd">
<td>Patient ICN</td>
<td>PATIENT file (#2)</td>
<td><p>INTEGRATION CONTROL NUMBER field</p>
<p>(# 991.01)</p>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
<p>(Values in both fields are concatenated with a “V”.)</p></td>
<td>6</td>
<td><p>Free Text.</p>
<p>Example: “1010185893V199552”</p>
<p>If an ICN does not exist, send null.</p></td>
</tr>
<tr class="even">
<td>ICD codes –<br />
Diagnosis</td>
<td><p>V POV file (#9000010.07)<br />
&amp;<br />
V CPT file (#9000010.18)</p>
<p>ICD Diagnosis file (#80)</p></td>
<td>POV field (#.01)<br />
<br />
&amp;<br />
DIAGNOSIS field (#.05)</td>
<td>7-16</td>
<td><p>Diagnosis data is pulled from the POV field (#.01) in the V POV file (#9000010.07) and from the DIAGNOSIS field (#.05) in the V CPT file (#9000010.18).</p>
<p>Number of codes is limited to 10. If over 10, they will be truncated.</p></td>
</tr>
<tr class="odd">
<td>CPT codes</td>
<td>CPT file (#81)</td>
<td>CPT CODE field (#.01)</td>
<td>17-26</td>
<td></td>
</tr>
<tr class="even">
<td>Code Set Indicator</td>
<td>N/A</td>
<td>N/A</td>
<td>27</td>
<td>Code set indicator values include 9 (contains ICD-9 codes only), 10 (contains ICD-10 codes only, U (contains ICD-9 and ICD-10 codes), and “” (Null – contains no ICD-9 or ICD-10 codes).</td>
</tr>
</tbody>
</table>

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

Example: Outpatient Visits – Detail Report Message

Subj: V. 4.0 PBMOV 29806 1/1 0 \[#33424\] 03/02/12@11:42 23 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-----------------------------------------------------------------------------

^0^O^3001016^xxxxxxxxx^5000000019V796730^800.00^^^^^^^^^^^^^^^^^^^^9

^0^O^3000101^xxxxxxxxx^5000000000V196703^291.9^^^^^^^^^^32160^^^^^^^^^^9

^0^O^3000101^xxxxxxxxx^5000000019V796730^800.00^^^^^^^^^^32100^^^^^^^^^^9

^0^I^3010604^xxxxxxxxx^5000000003V639492^800.00^^^^^^^^^^20924^^^^^^^^^^9

^0^O^3010606^xxxxxxxxx^^144.1^^^^^^^^^^00100^^^^^^^^^^9

^0^O^3010606^xxxxxxxxx^^850.1^^^^^^^^^^85002^^^^^^^^^^9

Example: Outpatient Visits – Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 XXXXXXXX

\[#7256\] 07/12/04@10:45 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Outpatient Visits JUL 11,2004@18:00 JUL 12,2004@10:45 16 hrs, 45 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Outpatient Visits – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 XXXXXXXX

\[#7257\] 07/12/04@10:45 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

Outpatient Visits 32807 4

## Inpatient PTF Record Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Recent enhancements include an Inpatient Patient Treatment File (PTF) Record extract to collect inpatient treatment file data.

For inpatient stays, the discharge date is used to identify and extract PTF records. The start date of this extract shall be the discharge date 30 days prior to the first date of the reporting period. For example, if the reporting period is the month of August, the start date for this extract shall be 8/1 minus 30 days. If a PTF record is identified twice, within the same reporting month, the record shall only be sent once.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications for the Inpatient PTF Record extract are defined in detail in the table below.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 25%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>INPATIENT PTF RECORD STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sender (facility #)</td>
<td>INSTITUTION file (#4)</td>
<td>STATION NUMBER field (#99)</td>
<td>2</td>
<td>The software extracts the facility number at which the database resides to identify the sender of the MailMan message.</td>
</tr>
<tr class="even">
<td>Unique PTF ID</td>
<td>PTF file (#45)</td>
<td></td>
<td>3</td>
<td>A unique ID established by concatenating the facility number to the Internal Entry Number of the PTF record in the PTF file (#45).</td>
</tr>
<tr class="odd">
<td>Admission Date for Inpatient Encounter</td>
<td>PTF file (#45)</td>
<td>ADMISSION DATE field (#2)</td>
<td>4</td>
<td>Internal format (minus time)<br />
Example: “2980409”</td>
</tr>
<tr class="even">
<td>Discharge Date for Inpatient Encounter</td>
<td>PTF file (#45)</td>
<td>DISCHARGE DATE field (#70)</td>
<td>5</td>
<td>Internal format (minus time)<br />
Example: “2980409”</td>
</tr>
<tr class="odd">
<td>Patient SSN</td>
<td>PATIENT file (#2)</td>
<td>SOCIAL SECURITY NUMBER field (#.09)</td>
<td>6</td>
<td>Internal format<br />
Example: “123456789”</td>
</tr>
<tr class="even">
<td>ICN</td>
<td>PATIENT file (#2)</td>
<td>INTEGRATION CONTROL NUMBER field (#991.01)</td>
<td>7</td>
<td><p>Internal format<br />
Example: “1234”</p>
<p>If ICN does not exist, send null.</p></td>
</tr>
<tr class="odd">
<td><span id="ICDp90" class="anchor"></span>ICD codes – Diagnosis</td>
<td>ICD Diagnosis file (#80)</td>
<td>Code Number field (#.01)</td>
<td>8-27</td>
<td>Internal format<br />
Example: “341.8, 341.9”</td>
</tr>
<tr class="even">
<td>CPT Codes</td>
<td>ICD OPERATION/<br />
PROCEDURE file (#80.1)</td>
<td>CODE NUMBER field (#.01)</td>
<td>28-43</td>
<td>Internal format<br />
Example: “99.10,75.37”</td>
</tr>
<tr class="odd">
<td>Code Set Indicator</td>
<td>N/A</td>
<td>N/A</td>
<td>44</td>
<td>Code set indicator values include 9 (contains ICD-9 codes only), 10 (contains ICD-10 codes only, U (contains ICD-9 and ICD-10 codes), and “” (Null – contains no ICD-9 or ICD-10 codes).</td>
</tr>
</tbody>
</table>

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

Example: Inpatient PTF Records – Detail Report Message

Subj: V. 4.0 PBMPTF 29806 1/1 0 \[#33425\] 03/02/12@11:42 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-----------------------------------------------------------------------------

^0^04^3020802^3030113^xxxxxxxxx^5000000001V324625^E955.6^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^9

^0^06^3020830^3031006^xxxxxxxxx^5000000042V640365^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

^0^08^3040421^3061026^xxxxxxxxx^5000000001V324625^295.01^295.02^295.10^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^9

^0^014^3120227^3120227^xxxxxxxxx^5000000008V200916^K71.51^A20.7^Q27.8^V70.2XXD^^^^^^^^^^^^^^^^^0016070^0016378^^^^^^^^^^^^^^^10

 Example: Inpatient PTF Record – Timing Report Message

<span id="ICDp92" class="anchor"></span> \[#7268\] 07/12/04@12:57 6 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Inpatient PTF Record JUL 12,2004@12:56 JUL 12,2004@12:57 0 hrs, 1 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Inpatient PTF Record – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 XXXXXXXX

\[#7269\] 07/12/04@12:57 6 lines

From: PBMPHARMACIST,EIGHT In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

Inpatient PTF Records

1481 1

## Provider Data Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Recent enhancements include a new Provider Data extract to incorporate provider data elements currently pulled from IV, Unit Dose, and Prescription as well as additional elements requested.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications are defined in detail in the table below.

<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>PROVIDER DATA STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Provider Station</td>
<td>INSTITUTION file (#4)</td>
<td>NAME field (#.01)</td>
<td>2</td>
<td></td>
</tr>
<tr class="even">
<td>Provider SSN</td>
<td>NEW PERSON file (#200)</td>
<td>SOCIAL SECURITY NUMBER field (#.09)</td>
<td>3</td>
<td></td>
</tr>
<tr class="odd">
<td>Provider Local IEN</td>
<td><p>PHARMACY PATIENT IV SUB-FILE file (#55.01)</p>
<p>Or</p>
<p>PHARMACY PATIENT UD SUB-FILE file<br />
(#55.06)</p>
<p>Or</p>
<p>PRESCRIPTION file (#52)</p></td>
<td><p>PROVIDER field (#.06)</p>
<p>Or</p>
<p>PROVIDER field (#1)</p>
<p>Or</p>
<p>PROVIDER field (#4)</p></td>
<td>4</td>
<td></td>
</tr>
<tr class="even">
<td>Provider Name</td>
<td>NEW PERSON file (#200)</td>
<td>NAME field (#.01)</td>
<td>5</td>
<td></td>
</tr>
<tr class="odd">
<td>Provider Class</td>
<td>PROVIDER CLASS file (#7)</td>
<td><p>ABBREV TITLE field (#1)</p>
<p>Or</p>
<p>NAME field (#.01)</p></td>
<td>6</td>
<td><p>If the ABBREV TITLE field (#1) does not contain data, data from the NAME field (#.01) in the PROVIDER CLASS file (#7) shall be extracted.</p>
<p>Transmission format: Internal value</p></td>
</tr>
<tr class="even">
<td>Provider Service/Section</td>
<td>SERVICE/SECTION file (#49)</td>
<td>NAME field (#.01)</td>
<td>7</td>
<td>Refer to the <strong>Note</strong> below for name abbreviations.</td>
</tr>
<tr class="odd">
<td>Provider Specialty</td>
<td>PERSON CLASS file (#8932.1)</td>
<td>CLASSIFICATION field (#1)</td>
<td>8</td>
<td></td>
</tr>
<tr class="even">
<td>Provider Subspecialty</td>
<td>PERSON CLASS file (#8932.1)</td>
<td>AREA OF SPECIALIZATION field (#2)</td>
<td>9</td>
<td></td>
</tr>
</tbody>
</table>

![](benefits-management-version-4-user-manual/016.png)Note: If the names listed below are found in the NAME field (#.01) of the SERVICE/SECTION file (#49), the associated abbreviation shall be extracted.

<u>TEXT</u> <u>ABBREVIATION</u> <u>REPRESENTS</u>

AMBU AMB Ambulatory Care

PRIMARY AMB Ambulatory Care

CBOC AMB Ambulatory Care

ANESTH ANES Anesthesiology

CARDIO CV Cardiology

PHARM CPHAR Clinical Pharmacy

DENT DDS Dental

INTERMED IM Intermediate Medicine

MEDIC MED Medicine

NEUROL NEUR Neurology

NUCLEAR NUM Nuclear Medicine

NURSING RN Nursing

OPHTH OPH Ophthalmology

ORTHOPED ORTHO Orthopedics

PSYCHIA PSY Psychiatry

MENTAL PSY Psychiatry

PULM PUL Pulmonary

RADIOL RAD Radiology

SURG SUR Surgery

UROLOG U Urology

Transmission format: Abbreviation specified above. If specified names not found, send null.

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

Example: Provider Data – Detail Report Message

Subj: V. 4.0 PBMPRO 30109 1/1 605 JERRY L PETTIS VAMC \[#7667\]

07/18/04@19:41 637 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^^3^MD^AMB^Physician/Osteopath^Nephrology^

^605^000001535^31^M.D.^MED^Physician/Osteopath^Family Practice^

^605^000001512^55^M.D.^MED^Physician/Osteopath^^

^605^000000036^78^^MED^Physician/Osteopath^Psychiatry^

^605^000005698^238^M.D.^MED^^^

^605^000005168^252^M.D.^NUM^Physician/Osteopath^Nuclear Medicine^

^605^000002791^299^M.D.^ANES^Physician/Osteopath^Pain Management - Anesthesiolo

gy^

^605^000001548^323^RPH^CPHAR^Pharmacist^^

^605^000007790^365^M.D.^MED^Physician/Osteopath^^

^605^000000667^388^RN^MED^Clinical Nurse Specialist^Medical-Surgical^

^605^^549^M.D.^MED^^^

^605^000006026^607^^MED^Physician/Osteopath^Psychiatry, Geriatric^

^605^000009499^642^^MED^Physician/Osteopath^Psychiatry^

^605^000001826^658^M.D.^^Physician/Osteopath^Hematology & Oncology^

^605^000007891^712^M.D.^MED^Physician/Osteopath^Internal Medicine^

^605^000009092^1128^RN^RN^Registered Nurse^^

^605^000006200^1131^M.D.^^Physician/Osteopath^Gastroenterology^

Subj: V. 4.0 PBMPRO 30109 1/1 605 JERRY L PETTIS VAMC \[#7667\] Page 2

-------------------------------------------------------------------------------

^605^000000342^1138^DDS^DDS^Dentist^^

^605^000009983^1143^DDS^DDS^Dentist^Prosthodontics^

^605^000004539^1156^M.D.^NEUR^Physician/Osteopath^Neurology^

^605^000004031^1159^M.D.^NEUR^Physician/Osteopath^Neurology^

^605^000002889^1177^M.D.^^Physician/Osteopath^Nephrology^

^605^000003132^1382^M.D.^MED^Physician/Osteopath^Internal Medicine^

^605^000006385^1495^^SUR^Physician/Osteopath^Ophthalmology^

^605^000005911^1599^M.D.^^Physician/Osteopath^Oncology, Medical^

^605^000001743^1610^M.D.^MED^Physician/Osteopath^Internal Medicine^

^605^000006386^1613^M.D.^MED^Physician/Osteopath^Internal Medicine^

^605^000004511^1618^M.D.^^Physician/Osteopath^Nephrology^

^605^000000910^1633^M.D.^MED^Physician/Osteopath^Endocrinology, Diabetes & Meta

bolism^

^605^000002392^1654^M.D.^RAD^Physician/Osteopath^Radiology, Diagnostic^

^605^000002747^1699^M.D.^MED^Physician/Osteopath^Internal Medicine^

^605^000009105^1741^M.D.^AMB^Physician/Osteopath^^

^605^000008461^1763^M.D.^MED^Physician/Osteopath^Emergency Medicine^

^605^000009953^1793^M.D.^MED^Physician/Osteopath^Geriatric Medicine: Internal M

edicine^

^605^000000057^1809^M.D.^MED^Physician/Osteopath^Internal Medicine^

> *  
> *Example: Provider Data – Provider Summary Report Message

Subj: V. 4.0 PBMPRO 30109 605 JERRY L PETTIS VAMC \[#7668\] 07/18/04@19:41

432 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Provider Summary Report JUL 18, 2004

SEP 01, 2001 through SEP 30, 2001

-------------------------------------------------------------------------------

Total Number of Incomplete Provider Records Extracted: 252

-------------------------------------------------------------------------------

IEN Provider Name (SSN) Missing Data

-------------------------------------------------------------------------------

3 PBMPROVIDER,ONE (????) SSN

78 PBMPROVIDER,TWO (0036) PROVIDER CLASS

238 PBMPROVIDER,THREE (5698) SPECIALTY

SUBSPECIALTY

549 PBMPROVIDER,FOUR (????) SSN

SPECIALTY

SUBSPECIALTY

607 PBMPROVIDER,FIVE (6026) PROVIDER CLASS

Subj: V. 4.0 PBMPRO 30109 605 JERRY L PETTIS VAMC \[#7668\] Page 2

-------------------------------------------------------------------------------

642 PBMPROVIDER,SIX (9499) PROVIDER CLASS

658 PBMPROVIDER,SEVEN (1826) SERVICE/SECTION

1131 PBMPROVIDER,EIGHT (6200) SERVICE/SECTION

1177 PBMPROVIDER,NINE (2889) SERVICE/SECTION

1495 PBMPROVIDER,TEN (6385) PROVIDER CLASS

1599 PBMPROVIDER,ELEVEN (5911) SERVICE/SECTION

1618 PBMPROVIDER,TWELVE (4511) SERVICE/SECTION

1834 PBMPROVIDER,THIRTEEN (3045) PROVIDER CLASS

1868 PBMPROVIDER,FOURTEEN (0711) PROVIDER CLASS

SERVICE/SECTION

SPECIALTY

SUBSPECIALTY

1883 PBMPROVIDER,FIFTEEN (0660) SERVICE/SECTION

1896 PBMPROVIDER,SIXTEEN (7456) PROVIDER CLASS

SPECIALTY

SUBSPECIALTY

1897 PBMPROVIDER,SEVENTEEN (9472) PROVIDER CLASS

1919 PBMPROVIDER,EIGHTEEN (9754) PROVIDER CLASS

2001 PBMPROVIDER,NINETEEN (2958) PROVIDER CLASS

2023 PBMPROVIDER,TWENTY (0582) PROVIDER CLASS

Example: Provider Data – Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY

\[#7669\] 07/18/04@19:41 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Provider Information JUL 18,2004@13:01 JUL 18,2004@19:41 6 hrs, 40 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Provider Data – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI

\[#7670\] 07/18/04@19:41 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

Provider Information 637 1

*(This page included for two-sided copying.)*

## Allergies/Adverse Events Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Allergies/Adverse Events extract collects allergy and adverse reactions documented for a patient.

Allergy and adverse reaction data documented for a patient is extracted using the verification date/time for the reporting period. Only verified allergy and adverse reactions are extracted in this manner.

The following data is not extracted:

- Allergy or adverse reactions marked as entered in error.
- Allergy or adverse reactions entered for a test patient, identified by having five leading zeros in the SOCIAL SECURITY NUMBER field (#.09) and/or having the TEST PATIENT INDICATOR field (#.6) set to “Yes” in the PATIENT file (#2).
- Allergy or adverse reactions to an immunization recorded in the PCE application.

Allergy or adverse reactions shall only be extracted from the PATIENT ALLERGIES file (#120.8). All event date/time(s) recorded in the ADVERSE REACTION REPORT file (#120.85) within the reporting period for a verified allergy/adverse reaction shall be extracted.

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific data elements are extracted for allergy and adverse reactions. The following chart explains the format for Allergies/Adverse Events Information Statistics as they appear in the MailMan message.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>ALLERGIES/ADVERSE EVENTS INFORMATION STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Allergy/Adverse Event ID = Facility station number + IEN in Patient Allergies File</td>
<td><p>INSTITUTION file (#4)</p>
<p>PATIENT ALLERGIES file (#120.8)</p></td>
<td>STATION NUMBER field (#99)</td>
<td>2</td>
<td><p>The facility is the default institution found in the MailMan domain site parameters.</p>
<p>The facility station number will be concatenated with the IEN of the Allergy/Adverse Event in the Patient Allergies file to create the Allergy/Adverse Event ID.</p></td>
</tr>
<tr class="even">
<td>Patient SSN</td>
<td>PATIENT file (#2)</td>
<td>SOCIAL SECURITY NUMBER field (#.09)</td>
<td>3</td>
<td>If the SSN does not exist, send null.</td>
</tr>
<tr class="odd">
<td>Patient ICN</td>
<td>PATIENT file (#2)</td>
<td><p>INTEGRATION CONTROL NUMBER field</p>
<p>(# 991.01)</p>
<p>ICN CHECKSUM</p>
<p>field (#991.02)</p>
<p>(Values in both fields are concatenated with a “V”.)</p></td>
<td>4</td>
<td><p>Free Text.</p>
<p>Example:<br />
“1010185893V199552”</p>
<p>If an ICN does not exist, send null.</p></td>
</tr>
<tr class="even">
<td>Reactant</td>
<td>PATIENT ALLERGIES file (#120.8)</td>
<td><p>REACTANT</p>
<p>field (#.02)</p></td>
<td>5</td>
<td><p>User may select from the following files:</p>
<p>VA Drug Class file (#50.605)</p>
<p>VA GENERIC file ( #50.6)</p>
<p>DRUG file (#50)</p>
<p>DRUG INGREDIENTS file (#50.416)</p>
<p>GMR ALLERGIES file (#120.82)</p></td>
</tr>
<tr class="odd">
<td>Reactant File</td>
<td>PATIENT ALLERGIES file (#120.8)</td>
<td><p>GMR ALLERGY</p>
<p>field (#1)</p></td>
<td>6</td>
<td>When the user selects a reactant from one of the files listed above, the file number will be extracted..</td>
</tr>
<tr class="even">
<td>Allergy Type</td>
<td>PATIENT ALLERGIES file (#120.8)</td>
<td>ALLERGY TYPE field (#3.1)</td>
<td>7</td>
<td><p>Internal Format.</p>
<p>“D” for Drug<br />
“F” for Food<br />
“O” for Other</p>
<p>or</p>
<p>combination, such as “DF” for Drug, Food</p></td>
</tr>
<tr class="odd">
<td>Origination Date/time</td>
<td>PATIENT ALLERGIES file (#120.8)</td>
<td>ORIGINATION DATE/TIME field (#4)</td>
<td>8</td>
<td><p>Internal Format (date).</p>
<p>Example: “3011001.0900”</p></td>
</tr>
<tr class="even">
<td>Originator’s Service/Section</td>
<td>SERVICE/SECTION file (#49)</td>
<td>NAME field (#.01)</td>
<td>9</td>
<td><p>Internal Format (free text).</p>
<p>Example: “NURSING”</p></td>
</tr>
<tr class="odd">
<td>Observed/Historical Flag</td>
<td>PATIENT ALLERGIES file (#120.8)</td>
<td>OBSERVED/HISTORICAL field (#6)</td>
<td>10</td>
<td><p>Internal Format.</p>
<p>“o” for Observed<br />
“h” for Historical</p></td>
</tr>
<tr class="even">
<td>Mechanism</td>
<td>PATIENT ALLERGIES file (#120.8)</td>
<td>MECHANISM field (#17)</td>
<td>11</td>
<td><p>Internal format.</p>
<p>“A” for Allergy<br />
“P” for Pharmacologic<br />
“U” for Unknown</p></td>
</tr>
<tr class="odd">
<td>Event Date/Time</td>
<td>ADVERSE REACTION REPORTING file (#120.85)</td>
<td>DATE/TIME OF EVENT field (#.01)</td>
<td>12</td>
<td><p>Internal Format (date).</p>
<p>Example: “3011001.0900”</p></td>
</tr>
<tr class="even">
<td>Observed – Severity</td>
<td>ADVERSE REACTION REPORTING file (#120.85)</td>
<td>SEVERITY field (#14.5)</td>
<td>13</td>
<td><p>External format.</p>
<p>Mild<br />
Moderate<br />
Severe</p></td>
</tr>
<tr class="odd">
<td>Sign/Symptom(s)</td>
<td>REACTIONS multiple (#10) in PATIENT ALLERGIES file (#120.8)</td>
<td><p>REACTION sub-field (#.01)</p>
<p>or</p>
<p>OTHER REACTION sub-field (#1) (Free text)</p></td>
<td>14-19</td>
<td>If the sign/symptom entered in the REACTION sub-field (#.01) equals “OTHER REACTION”, the value for the sign/symptom shall be extracted from the OTHER REACTION sub-field (#1). This is where the free text sign/symptom is stored.</td>
</tr>
</tbody>
</table>

![](benefits-management-version-4-user-manual/017.png)Note: Pieces 14-19 of this record will repeat for each sign/symptom. The record will allow for up to six sign/symptoms to be extracted and transmitted.

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

Example: Allergies/Adverse Events – Detail Report Message

Subj: V. 4.0 PBMAA 30106 1/1 605 JERRY L PETTIS VAMC \[#8672\]

08/10/04@11:48 5 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^60581857^000009999^1012237589V692969^TERAZOSIN^50.6^D^3061002.05^MEDICINE/NEUR

OLOGY^h^P^^^DIZZINESS^^^^^^

^60581858^000009999^1006029646V215983^PENICILLIN^50.6^D^3061002.0812^NURSING SE

RVICE^h^A^^^RASH^FEVER^^^^^

^60581867^000009999^1008969114V872239^OMEPRAZOLE^50.6^D^3061002.131^MEDICINE/NE

UROLOGY^o^P^3061002^MILD^DIARRHEA^^^^^^

^60581869^000009999^1005629866V604195^ORAL CONTRAST MEDIA^120.82^D^3061002.1358

^MEDICINE/NEUROLOGY^h^P^^^DIARRHEA^^^^^^

^60581925^000009999^1009057832V771463^PENICILLIN^50.6^D^3061005.1238^NURSING SE

RVICE^h^A^^^DYSPNEA^RASH^SWELLING^^^^

^60581926^000009999^1002670370V354180^INTRAVASCULAR CONTRAST MEDIA^120.82^D^306

1005.1331^NURSING SERVICE^h^A^^^RASH^^^^^^

^60581942^000009999^1012385894V929522^PENICILLIN^50.6^D^3061006.1012^NURSING SE

RVICE^h^P^^^DYSPNEA^RASH^SWELLING^^^^

Example: Allergies/Adverse Events –Timing Report Message

Subj: PBM TIMING for report JUN 01, 2001 to JUN 30, 2001 from 605 JERRY

\[#8673\] 08/10/04@11:48 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Allergies/Adverse Ev AUG 10,2004@11:47 AUG 10,2004@11:48 0 hrs, 1 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Allergies/Adverse Events – Confirmation Message

Subj: PBM Stats for JUN 01, 2001 to JUN 30, 2001 from 605 JERRY L PETTI

\[#8674\] 08/10/04@11:48 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

Allergies/Adverse Events 7 1

## Vitals/Immunizations Information Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vital/Immunization Extract collects patient vital and immunization records. Both types of records are transmitted in the same MailMan message.

Vital measurements are extracted using the date/time the vitals were taken for the reporting period. The latest vital measurement for each vital type requested shall be extracted for the reporting period. Any vital measurement marked as entered in error is screened out. Vital measurements for the following vital types are extracted:

- Blood Pressure
- Height
- Weight
- Pain
- Pulse
- Pulse Oximetry

Vital measurements for a test patient shall not be extracted. Test patients are identified by having five leading zeros in the SOCIAL SECURITY NUMBER field (#.09) and/or having the TEST PATIENT INDICATOR field (#.6) set to “Yes” in the PATIENT file (#2).

Immunization data is extracted using the date/time of the visit when the immunization was recorded as given for the reporting period. Immunization data for a test patient shall not be extracted. Test patients are identified by having five leading zeros in the SOCIAL SECURITY NUMBER field (#.09) and/or having the TEST PATIENT INDICATOR field (#.6) set to “Yes” in the PATIENT file (#2).

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific data elements are extracted for a vital measurement and immunization record. The following chart explains the format for the Vitals/Immunizations Information Statistics as they appear in the MailMan message.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>VITALS/IMMUNIZATIONS INFORMATION STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Facility Station<br />
Number</td>
<td>INSTITUTION file (#4)</td>
<td>STATION NUMBER field (#99)</td>
<td>2</td>
<td>The facility is the default institution found in the MailMan domain site parameters.</td>
</tr>
<tr class="even">
<td><p>Date/Time Vital Taken</p>
<p>- OR -</p>
<p>Immunization Date/time (date of visit when immunization was given)</p></td>
<td><p>GMRV VITAL MEASUREMENT file (#120.5)</p>
<p>V Immunization file (#9000010.11)</p></td>
<td><p>DATE/TIME VITALS TAKEN field (#.01)</p>
<p>EVENT DATE AND TIME field (#1201)</p></td>
<td>3</td>
<td><p>Internal format.</p>
<p>Example: “3011010.0900” (vital &amp; immunization)</p></td>
</tr>
<tr class="odd">
<td>Record type</td>
<td>N/A</td>
<td>N/A</td>
<td>4</td>
<td>To differentiate between a vital and immunization record, a “V” for Vital record and an “I” for Immunization record will be transmitted.</td>
</tr>
<tr class="even">
<td>Patient SSN</td>
<td>PATIENT file (#2)</td>
<td>SOCIAL SECURITY NUMBER field (#.09)</td>
<td>5</td>
<td><p>Internal format.</p>
<p>Example: “123456789”</p>
<p>If SSN does not exist, a null value will be transmitted.</p></td>
</tr>
<tr class="odd">
<td>Patient ICN</td>
<td>PATIENT file (#2)</td>
<td><p>INTEGRATION CONTROL NUMBER field<br />
(# 991.01)</p>
<p>ICN CHECKSUM<br />
field (#991.02)</p>
<p>(Values in both fields are concatenated with a “V”.)</p></td>
<td>6</td>
<td><p>Free text.</p>
<p>Example:<br />
“1010185893V199552”</p>
<p>If an ICN does not exist, send a null value.</p></td>
</tr>
<tr class="even">
<td>Immunization</td>
<td>Immunization file (#9999999.14)</td>
<td><p>IMMUNIZATION</p>
<p>field (#.01)</p></td>
<td>7</td>
<td><p>Free text.</p>
<p>Example: “INFLUENZA”</p></td>
</tr>
<tr class="odd">
<td>Vital Type</td>
<td>GMRV VITAL TYPE file (#120.51)</td>
<td>NAME field (#.01)</td>
<td>8</td>
<td><p>Free Text.</p>
<p>Example:<br />
“BLOOD PRESSURE”</p></td>
</tr>
<tr class="even">
<td><p>Rate</p>
<p>(a numeric value associated with this vital measurement)</p></td>
<td>GMRV Vital Measurement file (#120.5)</td>
<td>RATE field (#1.2)</td>
<td>9</td>
<td><p>Free text.</p>
<p>Example: “70” for weight;<br />
“140/80” for blood pressure.<br />
Or<br />
Users can enter a reason for omission, such as “REFUSE, PASS, or UNAVAILABLE.”</p>
<p>Pain scale codes:<br />
0 – Patient verbalizes no pain.<br />
1-10 – Patient verbalizes pain with “1” representing minimal pain and “10” representing worst imaginable pain.<br />
99 – Patient unable to respond/communicate pain level.</p></td>
</tr>
<tr class="odd">
<td>Unit associate with rate ( if applicable)</td>
<td>N/A</td>
<td>N/A</td>
<td>10</td>
<td><p>Free text.</p>
<p>Regardless of how the user enters a measurement, the software automatically converts the value and stores it in a standard format. The following units will be transmitted for a specific vital type:</p>
<p>Weight – “lb”<br />
Height – “in”<br />
Pulse Oximetry – “%”</p>
<p>Null value will be sent for Blood Pressure, Pain, and Pulse since there is no unit associated with these vital types.</p></td>
</tr>
<tr class="even">
<td>Qualifier(s) 1 - 4</td>
<td>GMRV VITAL QUALIFIER file (#120.52)</td>
<td>QUALIFIER field (#.01)</td>
<td>11-14</td>
<td><p>Free text</p>
<p>Example: weight may have the following qualifiers: “dry” or “actual”.</p>
<p>Not all measurements will have an associated qualifier. A measurement can have multiple qualifiers. Currently, the maximum number of qualifiers a vital may have is 4.</p></td>
</tr>
</tbody>
</table>

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following example.

Example: Vitals/Immunizations Information – Detail Report Message

Subj: V. 4.0 PBMVI 30109 1/4 605 JERRY L PETTIS VAMC \[#8675\]

08/10/04@11:55 10000 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

^605^3010901.1055^V^000007446^1006019979V41089^^BLOOD PRESSURE^146/83^^^^^^

^605^3010901.1055^V^000007446^1006019979V41089^^PAIN^6^^^^^^

^605^3010901.1055^V^000007446^1006019979V41089^^PULSE^93^^^^^^

^605^3010921.07^V^000003035^1002936262V619083^^BLOOD PRESSURE^112/50^^^^^^

^605^3010916.1714^V^000003035^1002936262V619083^^HEIGHT^71^IN^^^^^

^605^3010921.07^V^000003035^1002936262V619083^^PAIN^0^^^^^^

^605^3010921.07^V^000003035^1002936262V619083^^PULSE^80^^^^^^

^605^3010916.1714^V^000003035^1002936262V619083^^WEIGHT^150^LBS^^^^^

^605^3010927.1002^V^000004026^1002930709V651569^^BLOOD PRESSURE^112/40^^^^^^

^605^3010927.1002^V^000004026^1002930709V651569^^HEIGHT^66^IN^^^^^

^605^3010927.1002^V^000004026^1002930709V651569^^PAIN^7^^^^^^

^605^3010927.1002^V^000004026^1002930709V651569^^PULSE^52^^^^^^

^605^3010927.1002^V^000004026^1002930709V651569^^WEIGHT^200.9^LBS^^^^^

^605^3010919.1034^V^000000971^1002929377V415816^^BLOOD PRESSURE^110/58^^^^^^

^605^3010919.1034^V^000000971^1002929377V415816^^PULSE^62^^^^^^

^605^3010919.1034^V^000000971^1002929377V415816^^WEIGHT^185.2^LBS^^^^^

^605^3010919.0743^V^000004414^1002946917V569685^^BLOOD PRESSURE^115/63^^^^^^

^605^3010917.0949^V^000004414^1002946917V569685^^HEIGHT^70^IN^^^^^

Enter RETURN to continue or '^' to exit:

Subj: V. 4.0 PBMVI 30109 1/4 605 JERRY L PETTIS VAMC \[#8675\] Page 2

-------------------------------------------------------------------------------

^605^3010919.0743^V^000004414^1002946917V569685^^PAIN^0^^^^^^

^605^3010919.0743^V^000004414^1002946917V569685^^PULSE^56^^^^^^

^605^3010917.0949^V^000004414^1002946917V569685^^WEIGHT^175^LBS^^^^^

^605^3010920.0824^V^000001991^1002948737V812618^^BLOOD PRESSURE^140/60^^^^^^

^605^3010920.0824^V^000001991^1002948737V812618^^HEIGHT^67^IN^^^^^

^605^3010920.0824^V^000001991^1002948737V812618^^PAIN^0^^^^^^

^605^3010920.0824^V^000001991^1002948737V812618^^PULSE^76^^^^^^

^605^3010920.0824^V^000001991^1002948737V812618^^WEIGHT^214^LBS^^^^^

^605^3010927.1043^V^000006972^1007413451V523412^^BLOOD PRESSURE^140/48^^^^^^

^605^3010927.1043^V^000006972^1007413451V523412^^PAIN^3^^^^^^

^605^3010927.1043^V^000006972^1007413451V523412^^PULSE^56^^^^^^

^605^3010927.1043^V^000006972^1007413451V523412^^WEIGHT^207.2^LBS^^^^^

^605^3010925.1132^V^000003049^1002956604V989529^^BLOOD PRESSURE^138/81^^^^^^

^605^3010925.1132^V^000003049^1002956604V989529^^PAIN^0^^^^^^

^605^3010925.1132^V^000003049^1002956604V989529^^PULSE^107^^^^^^

^605^3010925.1132^V^000003049^1002956604V989529^^WEIGHT^301^LBS^^^^^

^605^3010913.1035^V^000001787^1002928955V238845^^BLOOD PRESSURE^148/76^^^^^^

^605^3010913.1035^V^000001787^1002928955V238845^^PAIN^0^^^^^^

^605^3010913.1035^V^000001787^1002928955V238845^^PULSE^76^^^^^^

^605^3010913.1035^V^000001787^1002928955V238845^^WEIGHT^175.7^LBS^^^^^

Example: Vitals/Immunizations –Timing Report Message

Subj: PBM TIMING for report SEP 01, 2001 to SEP 30, 2001 from 605 JERRY

\[#7592\] 07/16/04@15:49 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Vitals/Immunizations JUL 16,2004@15:45 JUL 16,2004@15:49 0 hrs, 4 min

-------------------------------------------------------------------------------

\*\*NOTE: Timing for the Provider Data extract is not recorded when the

the IV, Unit Dose, Prescription, and Patient Demographics extracts

are run concurrently.

Example: Vitals/Immunizations – Confirmation Message

Subj: PBM Stats for SEP 01, 2001 to SEP 30, 2001 from 605 JERRY L PETTI

\[#7593\] 07/16/04@15:49 6 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The chart below shows the package(s) whose dispensing statistics were extracted

by the PBM Manual Pharmacy Statistics option.

PACKAGE \# Line items \# MailMan msgs

-------------------------------------------------------------------------------

Vitals/Immunizations Information34471 4

## Lab Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Extracted data is electronically exported via MailMan to the PBM national database at Hines from each VA Medical Center or Outpatient Clinic. MailMan messages are downloaded to text files onto the PBM network and run through a translation program. The data is then appended to an existing PBM Pharmacy dispensing master file.

If an IV order has multiple IV additives/solutions that are assigned the same VA drug class that requires laboratory data extraction, repetitive laboratory data will be sent. The same rule applies for a UD order with multiple dispense drugs that have the same VA drug class. If an IV order, UD order, or a Prescription contains a drug for which more than one laboratory test is extracted, all pieces of information will be repeated with the exception of the laboratory data.

Specific laboratory test results for IV additive(s) or solution(s), dispensed drug(s), and prescription drugs that have designated VA Drug Classes will be extracted (see table below). The latest test result going back one year will be extracted.

| VA Drug Class Code | Laboratory Test Name         | Wkld code |
|------------------------|----------------------------------|---------------|
| AN500                  | Testosterone                     | 83405.0000    |
| AN500                  | Testosterone Free                | 81062.0000    |
| CV200                  | Creatinine                       | 82565.0000    |
| CV350                  | Cholesterol LDL                  | 83017.0000    |
| CV350                  | Cholesterol HDL                  | 83013.0000    |
| CV350                  | Triglycerides w o extract        | 84480.0000    |
| CV350                  | Cholesterol Total                | 82466.0000    |
| CV350                  | Transferase Aspartate (SGOT)     | 84455.0000    |
| CV350                  | Transferase Alanine Amino (SGPT) | 84465.0000    |
| CV800                  | Creatinine                       | 82565.0000    |
| CV800                  | Potassium                        | 84140.0000    |
| GA301                  | Creatinine                       | 82565.0000    |
| HS502                  | Glucose Quant                    | 84330.0000    |
| HS502                  | Glycohemoglobin HbA 1c           | 85053.0000    |
| HS502                  | Glycohemoglobin HbA 1c           | 85052.0000    |
| HS502                  | Transferase Aspartate (SGOT)     | 84455.0000    |
| HS502                  | Transferase Alanine Amino (SGPT) | 84465.0000    |

### Statistics Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications for the Lab extract are defined in detail in the table below.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><strong>LAB INFORMATION STATISTICS DATA FIELD SPECIFICATIONS</strong></th>
</tr>
<tr class="odd">
<th><strong><br />
<br />
<br />
DATA ELEMENT</strong></th>
<th><strong><br />
<br />
<br />
FILE #</strong></th>
<th><strong><br />
<br />
<br />
FIELD #</strong></th>
<th><strong>PIECE # IN RECORD SENT</strong></th>
<th><strong><br />
<br />
<br />
DESCRIPTION</strong></th>
</tr>
<tr class="header">
<th>Sender<br />
(facility # and suffix)</th>
<th><p>MEDICAL CENTER DIVISION file (#40.8)<br />
Or</p>
<p>OUTPATIENT SITE file (#59)</p></th>
<th><p>FACILITY NUMBER field (#1)<br />
<br />
Or</p>
<p>SITE NUMBER field (#.06)</p></th>
<th>2</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient SSN</td>
<td>PATIENT file (#2)</td>
<td>SOCIAL SECURITY NUMBER field (#.09)</td>
<td>3</td>
<td></td>
</tr>
<tr class="even">
<td>IV Order #</td>
<td>PHARMACY PATIENT IV sub-file (#55.01)</td>
<td>ORDER NUMBER field (#.01)</td>
<td>4</td>
<td></td>
</tr>
<tr class="odd">
<td>UD Order #</td>
<td>PHARMACY PATIENT –UNIT DOSE sub-file (#55.06)</td>
<td>ORDER NUMBER field (#.01)</td>
<td>5</td>
<td></td>
</tr>
<tr class="even">
<td>Prescription #</td>
<td>PRESCRIPTION file (#52)</td>
<td>RX # field (#.01)</td>
<td>6</td>
<td></td>
</tr>
<tr class="odd">
<td>Generic Drug Name</td>
<td>DRUG file (#50)</td>
<td>GENERIC NAME field (#.01)</td>
<td>7</td>
<td></td>
</tr>
<tr class="even">
<td>Laboratory Test Name</td>
<td>LABORATORY TEST file (#60)</td>
<td>NAME field (#.01)</td>
<td>8</td>
<td></td>
</tr>
<tr class="odd">
<td>Results + Units</td>
<td><p>CHEM, HEM, TOX, RIA, SER, etc., multiple (#63.04) within the LAB DATA file (#63)</p>
<p>SITE/SPECIMEN multiple (#60.01) within the LABORATORY TEST file (#60)</p></td>
<td><p>LOCATION (data name) field (#5)</p>
<p>UNITS field (#6)</p></td>
<td>9</td>
<td></td>
</tr>
<tr class="even">
<td>Hi/Lo Flag</td>
<td>LAB DATA file (#63)</td>
<td>Results node, 2<sup>nd</sup> global piece</td>
<td>10</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Date/Time Specimen Collected</td>
<td>CHEM, HEM, TOX, RIA, SER, etc., multiple (#63.04) within the LAB DATA file (#63)</td>
<td>DATE/TIME SPECIMEN TAKEN field (#.01)</td>
<td>11</td>
<td></td>
</tr>
</tbody>
</table>

### Example MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is constructed in an up-arrow (^) delimited format as shown in the following examples.

Example: Lab – Detail Report Message

Subj: V. 4.0 PBMLR 29808 1/1 556 NORTH CHICAGO \[#7571106\] 17 Sep 98 02:55 5725 Lines

From: PBMPHARMACIST,ELEVEN in 'IN' basket. Page 1

------------------------------------------------------------------------------

^556^000003333^1^^^FAMOTIDINE 10MG/ML INJ 4ML^CREATININE^.9 mg/dL^^2980731.08001^

^556^000007777^32^^^FAMOTIDINE 10MG/ML INJ 4ML^CREATININE^2.3 mg/dL^H^2980731.083934^

^556^000005555^3^^^FAMOTIDINE 10MG/ML INJ 4ML^CREATININE^1.4 mg/dL^^2980730.143023^

^556^000008888^^14^^GEMFIBROZIL 600MG TAB^CHOLESTEROL^192. mg/dL^^2980507.08^

^556^000008888^^14^^GEMFIBROZIL 600MG TAB^SGOT^33. U/L^^2980507.08^

^556^000008888^^14^^GEMFIBROZIL 600MG TAB^TRIGLYCERIDES^107. mg/dL^^2980507.08^

^556^000008888^^14^^GEMFIBROZIL 600MG TAB^HDL CHOLESTEROL^65 mg/dl^^2980507.08^

^556^000008888^^14^^GEMFIBROZIL 600MG TAB^LDL CHOLESTEROL^106 mg/dl^^2980507.08^

^556^000008888^^^1317395^LISINOPRIL 5MG TAB^CREATININE^.8 mg/dL^^2971230.083336^

^556^000002222^^^1317395^LISINOPRIL 5MG TAB^POTASSIUM^4.6 mmol/L^^2971230.083336^

^556^000004444^^^1319160^NIFEDIPINE (ADALAT CC) 60MG SA TAB^CREATININE^1.0 mg/dL^^

2980105.105717^

Example: Lab - Laboratory Statistical Summary Message

Subj: V. 4.0 PBMLR 29808 556PA NC-PRRTP \[#7571162\] 17 Sep 98 02:55 4 Lines

From: PBMPHARMACIST,TWELVE in 'IN' basket. Page 1

------------------------------------------------------------------------------

Laboratory Statistical Summary Data for AUG 1,1998 through AUG 31,1998

Total Patients 9

Total Laboratory Tests 35

Select MESSAGE Action: IGNORE (in IN basket)// \<Enter\>  
Example: Laboratory Statistical Data Message

Subj: V. 4.0 PBMLR 29808 556PA NC-PRRTP \[#7571163\] 17 Sep 98 02:55 39 Lines

From: PBMPHARMACIST,TWELVE in 'IN' basket. Page 1

------------------------------------------------------------------------------

Laboratory Statistical Data for AUG 1,1998 through AUG 31,1998

Patient SSN VA CODE Laboratory Results Flag Date/Time Taken

------------------------------------------------------------------------------

000004322 CV800 CREATININE 1.0 mg/dL 07/01/98 0818

POTASSIUM 3.8 mmol/L 07/01/98 0818

000008348 HS502 GLUCOSE 211. mg/dL H 07/28/98 0718

HEMOGLOBIN A1C 10.9 % H 07/28/98 0718

000002996 CV200 CREATININE 1.3 mg/dL 02/10/98 0718

CV350 CHOLESTEROL 175. mg/dL 02/10/98 0718

SGOT 26. U/L 02/10/98 0718

TRIGLYCERIDES 268. mg/dL H 02/10/98 0718

HDL CHOLESTEROL 31 mg/dl 02/10/98 0718

LDL CHOLESTEROL 90 mg/dl 02/10/98 0718

CV800 CREATININE 1.3 mg/dL 02/10/98 0718

POTASSIUM 4.7 mmol/L 02/10/98 0718

HS502 GLUCOSE 155. mg/dL H 02/10/98 0718

SGOT 26. U/L 02/10/98 0718

HEMOGLOBIN A1C 5.8 % 02/10/98 0719

000003405 CV200 CREATININE .9 mg/dL 03/31/98 0724

000009656 CV350 CHOLESTEROL 281. mg/dL H 06/03/98 0725

SGOT 23. U/L 06/03/98 0725

TRIGLYCERIDES 239. mg/dL H 06/03/98 0725

HDL CHOLESTEROL 37 mg/dl 06/03/98 0725

LDL CHOLESTEROL 196 mg/dl H 06/03/98 0725

000006829 CV200 CREATININE .9 mg/dL 07/14/98 0723

GA301 CREATININE .9 mg/dL 07/14/98 0723

HS502 GLUCOSE 286. mg/dL H 07/31/98 0723

SGOT 83. U/L H 07/14/98 0723

GLUCOSE, 2HR PP 405. mg/dl H 07/31/98 1010

HEMOGLOBIN A1C 7.4 % H 07/14/98 0723

000006902 CV200 CREATININE 1.1 mg/dL 06/23/98 1442

GA301 CREATININE 1.1 mg/dL 06/23/98 1442

000003405 CV350 CHOLESTEROL 237. mg/dL H 07/29/98 0707

*(This page included for two-sided copying.)*

# HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Recent enhancements allow real-time transmission of all verified Chemistry Laboratory tests via Health Level 7 (HL7) messaging to port 5001 in the Consolidated Mail Outpatient Pharmacy National Server (CMOP-NAT).

HL7 and TCP/IP are the communication protocols that are used to transmit messages between VistA databases and the VistA HL7 Optimized (HLO) process on the CMOP-NAT server.

Two links are required for message transactions:

1.  The VMAC sending link sends HL7 messages to Pharmacy Benefits Management (PBM) at the CMOP-NAT server.
2.  The PBM HL7 listener link receives the HL7 messages.

No data is transmitted for patients who are employees; otherwise, each VAMC will send all verified Chemistry Lab tests results to PBM, including hematology and urinalysis.

On the CMOP-NAT server, a daily job processes all the HL7 messages received the previous day. The Chemistry Lab test results at each site are stored in a delimited flat file in a predefined Windows directory on the CMOP-NAT server.

![](benefits-management-version-4-user-manual/018.png)Note: The event protocols for the HL7 sending link and the lab results need to be loaded at all facilities. In addition, the listening link must be set up on the CMOP-NAT server for the messaging to function properly.

## Data Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data element specifications that make up the new HL7 Lab extract are defined in detail in the table below.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>DATA ELEMENT</strong></th>
<th><strong>HL7 SEGMENT</strong></th>
<th><strong>SOURCE</strong></th>
<th><strong>FORMAT</strong></th>
<th><strong>FIELD LENGTH (UL)</strong></th>
<th><strong>COMMENTS</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Facility</td>
<td>OBX-15</td>
<td>INSTITUTION field (#.01) within the ACCESSION AREA multiple (#60.11) within the LABORATORY TEST file (#60)</td>
<td><p>Internal number</p>
<p>Example: ‘578’</p></td>
<td>3</td>
<td></td>
</tr>
<tr class="even">
<td>Patient SSN</td>
<td>PID-19</td>
<td>SOCIAL SECURITY NUMBER field (#.09) of PATIENT file (#2)</td>
<td>Internal format<br />
Example: ‘123456789’</td>
<td>10</td>
<td></td>
</tr>
<tr class="odd">
<td>Patient ICN</td>
<td>PID-12</td>
<td><p>INTEGRATION CONTROL NUMBER field</p>
<p>(# 991.01)</p>
<p>ICN CHECKSUM</p>
<p>field (#991.02) of PATIENT file (#2)</p>
<p>(Values in both fields are concatenated with a ‘V’.)</p></td>
<td>Free Text<br />
Example: ‘1010185893V199552’</td>
<td>12</td>
<td>If ICN does not exist send null</td>
</tr>
<tr class="even">
<td>Local Laboratory Test Name</td>
<td>OBX-3</td>
<td>NAME field (#.01) of LABORATORY TEST file (#60)</td>
<td>Internal format<br />
Example: ‘Potassium’</td>
<td>Up to 40 characters</td>
<td></td>
</tr>
<tr class="odd">
<td>LOINC Code</td>
<td><p>OBX-3</p>
<p>.</p></td>
<td><p>CODE field (#.01) of LAB LOINC file (#95.3) pointer by</p>
<p>LOINC CODE field (#95.3) within the SITE/SPECIMEN multiple (#60.1) within the LABORATORY TEST file (#60)</p></td>
<td>Internal format<br />
Example: ‘269’</td>
<td>Up to 9 characters</td>
<td></td>
</tr>
<tr class="even">
<td>National Lab test (NLT) Code</td>
<td>OBX-3</td>
<td><p>ORDERED TEST field (#.35)</p>
<p>within the CHEM, HEM, TOX, RIA, SER, etc. multiple (#63.04) within the LAB DATA file (#63)</p></td>
<td>Internal format</td>
<td>Up to 10 characters</td>
<td></td>
</tr>
<tr class="odd">
<td>Site/Specimen</td>
<td>OBX-3</td>
<td><p>NAME field (#.01) within the TOPOGRAPHY FIELD file (#61) pointer by</p>
<p>SITE/SPECIMEN field (#.01) within the SITE/SPECIMEN multiple (#60.01) within the LABORATORY TEST file (#60)</p></td>
<td>Internal format</td>
<td>Up to 80 characters</td>
<td></td>
</tr>
<tr class="even">
<td>Results</td>
<td>OBX-5</td>
<td>Field is dependent on test.</td>
<td>Internal format<br />
Example: ‘5.0’</td>
<td></td>
<td>Field is dependent on test</td>
</tr>
<tr class="odd">
<td>Units</td>
<td>OBX-6</td>
<td>UNITS field (#6) within the SITE/SPECIMEN multiple (#60.01)</td>
<td>Internal format<br />
Example: ‘mg/dl’</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>High Range</td>
<td>OBX-7</td>
<td>REFERENCE HIGH field (#2) within the SITE/SPECIMEN multiple (#60.01) within the LABORATORY TEST file (#60)</td>
<td>Internal format<br />
Example: “200” or<br />
“REACTIVE”</td>
<td>Up to 50 characters</td>
<td></td>
</tr>
<tr class="odd">
<td>Low Range</td>
<td>OBX-7</td>
<td>REFERENCE LOW field (#1) within the SITE/SPECIMEN multiple (#60.01) within the LABORATORY TEST file (#60)</td>
<td>Internal format<br />
Example: “60” or<br />
“NEGATIVE”</td>
<td>Up to 50 characters</td>
<td></td>
</tr>
<tr class="even">
<td>Date/time Specimen Collected</td>
<td>OBR-7</td>
<td>DATE/TIME SPECIMEN TAKEN field (#.01) within the CHEM, HEM, TOX, RIA, SER, etc. multiple (63.04) within the multiple LAB DATA file (#63)</td>
<td>Internal format<br />
Example: 2970814.1400</td>
<td>12 characters</td>
<td></td>
</tr>
</tbody>
</table>

*(This page included for two-sided copying.)*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Additive A drug that is added to an IV solution for the purpose of parenteral administration. An additive can be an electrolyte, a vitamin or other nutrient, or an antibiotic, but only electrolyte—or multivitamin-type additives can be entered as IV fluid additives in CPRS.
> Admixture A type of intravenously administered medication comprised of any number of additives (including zero) in one solution. It is given at a specified flow rate; when one bottle or bag is empty, another is hung.
> Adverse Reaction Any condition precipitated by a drug, which requires patient treatment, admission, or transfer; prompts a specialty consultation; or causes injury or death. Every allergy is an adverse reaction, but every adverse reaction is not an allergy.
> Allergy A state of hypersensitivity induced by exposure to a certain agent.
> Allergy Type The type of causative agent, such as FOOD or DRUG.
> AMIS Category Classification of AR/WS drugs for AMIS purposes. There are four AMIS categories:
| Category | Description                                                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0            | Drug is classified as field 03 or 04, which includes tablets, capsules, multidose vials, etc. It does not include multiple-dose externals, liquids, or antacids. |
| 1            | Drug is classified as field 06 or 07, which includes multiple-dose externals, liquids, antacids, otics, ophthalmic, and inhalations.                             |
| 2            | Drug is classified as field 17, which includes solutions and administration sets.                                                                                |
| 3            | Drug is classified as field 22, which includes blood and blood products.                                                                                         |
> AMIS Conversion Number Reflects the number of doses/units contained in a single quantity dispensed. For example, for a 20cc vial, the quantity dispensed is 1, and the AMIS conversion number is 20.
> Area of Use (AOU) A place where commonly stocked items are stored for use by wards or treatment areas. An AOU may serve one or more wards or clinics, or, as in the case of “cardiac cath lab”, no ward.
> Automatic Replenishment/ A method of drug distribution and inventory
> Ward Stock (AR/WS) management within a hospital. Drug products can be automatically inventoried and delivered to an Area of Use (AOU) or requested on demand.
> Average Unit Drug Cost The total drug cost divided by the total number of units of measurement.
> Chemotherapy Chemotherapy is the treatment or prevention of cancer with chemical agents. The chemotherapy IV type can be administered as a syringe, admixture, or a piggyback. Once the subtype (syringe, piggyback, etc.) is selected, the order entry follows the same procedure as the type that corresponds to the selected subtype (example: piggyback type of chemotherapy follows the same entry procedure as regular piggyback IV).
> Conjunction A term used to build a SIG for a complex medication order. Conjunctions used are ‘AND’, ‘THEN’, or ‘EXCEPT’.
> Controlled Substance A drug that has been marked for tracking through the Controlled Substances package. It is usually narcotic.
> CPRS Acronym for Computerized Patient Record System.
> Credit This is money due to the VA facility from the prime vendor. When an invoice dollar amount is more than the adjusted dollar amount, Drug Accountability flags it as an outstanding credit. When the facility receives a credit memo, the credit data is entered in Drug Accountability.
> DEA Special Handling The Drug Enforcement Agency special handling code used for drugs to designate if they are over-the-counter, narcotics, bulk compounds, supply items, etc.
> Dispense Units per Dose The number of units (tablets, capsules, etc.) to be dispensed as a dose for an order.
> Dispense Units per Order Unit This is the total number of dispense units contained in one order unit. For example, if you order a case containing 12 bottles with 1,000 tablets in each bottle, the dispense unit per order unit is 12,000 per the following equation:
> Dispense Units: TAB
> Order Unit: CS
> The case contains 12 bottles of 1,000 tablets
> 12 x 1,000 = 12,000
> DISPENSE UNITS PER ORDER UNIT: 12,000
> Dispensing Unit This field is used to indicate the pharmacy dispensing units when converting the unit per issue to the pharmacy dispensing units.
> Dosage Ordered A single dose of medication that the patient will receive for a prescription (outpatient medication) order.
> Drug A substance used to treat illness or disease.
> DRUG file (#50) A VistA file used by Pharmacy software products. This file is used to list generic drug products and holds the information related to each drug that can be used to fill a prescription.
> Duration The length of time a medication should be given. A numeric value is usually entered followed by one of the following:  
> M = Minutes  
> H = Hours  
> D = Days  
> W = Weeks  
> L = Months
> HL7 Health Level Seven. Application protocol for electronic data exchange in health care environments.
> HLO Optimized version of HL7, designed to provide significantly improved messaging.
> Historical An allergy that has been stated by some source versus one that is actually witnessed by some personnel at the facility.
> Hyperalimentation (Hyperal) Long term feeding of a protein-carbohydrate solution. Electrolytes, fats, trace elements, and vitamins can be added. Since this solution generally provides all necessary nutrients, it is commonly referred to as Total Parenteral Nutrition (TPN). A hyperal is composed of many additives in two or more solutions. When the labels print, they show the individual electrolytes in the hyperal order.
> IFCAP Integrated Funds Distribution Control Point Activity, Accounting and Procurement. A VA software package that tracks procurement
> and payment.
> Infusion Rate The designated rate of flow of IV fluids into the patient.
> Inpatient Site An area within a facility that treats patients that have been admitted. If the facility has more than one Inpatient dispensing area, it is necessary to link each pharmacy location to the appropriate Inpatient site (area) for the collection of dispensing data.
> Invoice A bill for ordered goods. Each invoice is numbered. See entry for Order Number vs. Item Number.
> IV Additive A drug that is added to an IV solution for the purpose of parenteral administration. An additive can be an electrolyte, a vitamin, or other nutrient; or an antibiotic. Only electrolyte or multivitamin type additives can be entered as IV fluid additives in CPRS.
> IV Piggyback (IVPB) Small volume parenteral solution for intermittent infusion. A piggyback is comprised of any number of additives, including zero, and one solution; the mixture is made in a small bag. The piggyback is given on a schedule (for example, Q6H). Once the medication flows in, the piggyback is removed; another is not hung until the administration schedule calls for it.
> IV Solution Usually a Large Volume Parenteral (LVP), administered as a vehicle for additive(s) or for pharmacological effect of the solution itself. Infusion is generally continuous. An LVP or piggyback has only one solution (primary solution). A hyperal can have one or more solutions.
> IV SOLUTIONS file (#52.7) Contains drugs, which are used as primary solutions in the IV room. The solution must already exist in the DRUG file (#50) to be selected. Data in this file includes drug generic name, print name, status, drug information, synonym(s), volume, and electrolytes.
> LVP Large Volume Parenteral—Admixture. A solution intended for continuous parenteral infusion administered as a vehicle for additive(s) or for the pharmacological effect of the solution itself. Composed of any number of additives, including zero, in one solution. An LVP runs continuously, with another bag hung when one bottle or bag is empty.
> Line Item This is the information on the invoice for an ordered drug.
> MailMan An electronic mail, teleconferencing, and networking system.
> Master Vault An inventory location created to store a select group of controlled substances and track their balance and activity.
> Mechanism In the context of Adverse Reaction Tracking (ART), this is an indicator of whether the data for the patient is just an adverse reaction or an allergy.
> Narcotic Area of Use (NAOU) A place where commonly stocked Controlled Substances drugs are stored for use by pharmacy, wards, or treatment areas. There are three types of NAOUs: 1) Master Vault, 2) Satellite Vault, and  
> 3) Narcotic Locations.
> NDC Acronym for National Drug Code. A field (with various field numbers) that exists in the DRUG file (#50), ITEM MASTER file (#441). With some formatting adjustments the field is used to match entries in otherwise unlinked files and open the door for comparative displays and reports. The code itself contains a maximum of 12 digits. The first six digits are the manufacturer’s code, the next four are the product code, and the last two digits are the package code.
> Noun A term associated with the dosage form assigned to the drug; used by the Outpatient Pharmacy software to build a SIG for a prescription order.
> Observed An allergy or adverse reaction that has actually been witnessed by some personnel at the facility.
> Order VA’s request for goods from the vendor.
> Order Number vs. An order number is a VA number by which
> Invoice Number to charge the ordered goods. The invoice number is the vendor’s number for billing the ordered goods. There can be many invoice numbers assigned to one order number because by law, certain drugs have to be placed on an invoice by itself. Also drugs can come from different distribution centers, which necessitates different invoice numbers.
> Origination Date/Time The date/time the allergy or adverse reaction was entered into the system.
> Originator The person who entered the allergy or adverse reaction into the system.
> Outpatient Site An area within a facility that treats patients that are not admitted to the facility. If a facility has more than one Outpatient dispensing area, it is necessary to link each pharmacy location to the appropriate Outpatient site (area) for the collection of Outpatient dispensing data.
> PBM Acronym for Pharmacy Benefits Management.
> Pharmacy Location An inventory location created to store a select group or all of non-controlled drugs and track their balance and activity.
> Piggyback Small volume parental solution for intermittent infusion. A piggyback is composed of any number of additives, including zero, and one solution; the mixture is made in a small bag. The piggyback is given on a schedule (example: Q6H). Once the medication flows in, the piggyback is removed; another is not hung until the administration schedule calls for it.
> Pre-Exchange Units The number of actual units required for an order until the next cart exchange.
> Prescription This term is now referred to throughout the software as medication orders.
> Prime Vendor A procurement system where each section orders pharmaceutical supplies directly from one primary vendor via computer link.
> Print Name Drug generic name as it is to appear on pertinent IV output, such as labels and reports. Volume is not part of the print name.
> Process Process is matching invoice data with data in VistA and validating the data. Matching is accomplished by comparing the line item data on the invoice with its entry in the DRUG file (#50). Validating is accomplished by confirming the quantity received vs. the quantity invoiced. Anyone holding the PSA ORDERS key can process the invoice.
> Provider The person who authorized an order. Only users identified as providers who are authorized to write medication orders may be selected.
> Reactant The causative agent that caused a patient to have an allergy or adverse reaction.
> Record Type In the context of this document, a code to differentiate a vital from an immunization record.
> Refill A second or subsequent filling authorized by the provider.
> Reporting Period The period for the Start/Stop dates entered by the user for the PBM extract.
> Route How the medication is taken, administered, or used.
> Schedule The frequency by which the doses are to be administered, such as Q8H, BID, NOW, etc.
> Severity An index of how the allergy or adverse reaction affected the patient.
> SIG The Latin term “signa” meaning “label.” SIG refers to instructions printed on the prescription label.
> Sign/Symptom Something that could be subjectively or objectively measured that indicates an allergy or adverse reaction.
> Syringe Type of IV that uses a syringe rather than a bottle or bag. The method of infusion for a syringe-type IV may be continuous or intermittent.
> Unit A standard form of measure.
> VA Drug Class Code A drug classification system used by VA that separates drugs into different categories based upon their characteristics. IV cost reports can be run for VA Drug Class Codes, provided the Outpatient Pharmacy V. 5.6 or later package has been installed at the site.
> Verb A term that helps to describe how the medication will be taken/used.
> VA Generic Name A name given to an item (drug, supply, etc.) in pharmacy files. It is this name which is matched with the entry in the GENERIC NAME field (#.01) of the local DRUG file.
> VA Product Name The unique name assigned to each drug product. This name includes strength, unit, and dosage form.
> VistA Veterans Health Information Systems and Technology Architecture.
> Vital Qualifier Further defines the vital sign; a word that gives a more detailed description of an item.
> Vital Type A category of a vital sign or measurement (for example, pulse, respiration, or blood pressure).
*(This page included for two-sided copying.)*

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Allergies/Adverse Events Extract, 99
AR/WS Extract, 43
C
Controlled Substances Extract, 75
H
HL7 Messages, 115
Data Specifications, 116
I
Inpatient PTF Record Extract, 89
Introduction, 1
IV Extract, 21, 27
L
Lab Extract, 109
M
MailMan Messages, 19
Allergies/Adverse Events Extract
Confirmation Message, 103
Detail Report, 102
Statistics Data Field Specifications, 99
Timing Report, 102
AR/WS Extract
AMIS Summary Report, 47
Confirmation Message, 48
Detail Report, 45
Statistical Data, 46
Statistics Data Field Specifications, 43
Timing Report, 48
Unmapped Locations, 48
Controlled Substances Extract
AMIS Summary Report, 80
Confirmation Message, 80
Detail Report, 78
Statistical Data, 79
Statistics Data Field Specifications, 75
Timing Report, 80
Unmapped Locations, 80
Inpatient PTF Record Extract
Confirmation Message, 92
Detail Report, 91
Statistics Data Field Specifications, 89
Timing Report, 92
IV Extract
AMIS Summary Report, 29
Confirmation Message, 32
Detail Report, 27, 30
Laboratory Data Summary, 31
Laboratory Statistical Summary, 30
Patient Demographic Summary Report, 29
Statistical Data, 28
Statistics Data Field Specifications, 21
Timing Report, 31
Lab Extract
Detail Report, 112
Laboratory Statistical Data, 113
Laboratory Statistical Summary, 112
Statistics Data Field Specifications, 110
Outpatient Visits Extract
Confirmation Message, 88
Detail Report, 87
Statistics Data Field Specifications, 85
Timing Report, 88
Patient Demographics Extract
Confirmation Message, 84
Detail Report, 83
Statistics Data Field Specifications, 81
Timing Report, 84
Prescription Extract
Confirmation Message, 63
Detail Report, 56, 57, 59, 61, 62
Laboratory Data Summary, 62
Laboratory Statistical Summary, 62
Outpatient AMIS Summary Report, 60
Outpatient Statistical Data, 58
Outpatient Statistical Data Summary, 58
Patient Demographic Summary, 60
Statistics Data Field Specifications, 49
Timing Report, 63
Procurement Extract
Data Summary, 73
Detail Report, 72
Statistical Summary, 73
Statistics Data Field Specifications/DRUG ACCOUNTABILITY file (#58.81), 69
Statistics Data Field Specifications/IFCAP file (#442), 65
Statistics Data Field Specifications/PRIME VENDOR file (#58.811), 67
Timing Report, 74
Unmapped Locations, 74
Provider Data Extract
Confirmation Message, 97
Detail Report, 95
Provider Summary Report, 96
Statistics Data Field Specifications, 93
Timing Report, 97
UD Extract
AMIS Summary Report, 39
Confirmation Message, 42
Detail Report, 37, 40
Laboratory Data Summary, 41
Laboratory Statistical Summary, 40
Patient Demographic Summary Report, 39
Statistical Data, 38
Statistics Data Field Specifications, 33
Timing Report, 42
Vitals/Immunizations Information Extract
Confirmation Message, 108
Detail Report, 107
Statistics Data Field Specifications, 105
Timing Report, 108
O
Options, 5
*Automatic Pharmacy Statistics* \[PSU PBM AUTO\], 7
*Manual Pharmacy Statistics* \[PSU PBM MANUAL\], 5
*Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\], 12
*PBM Manager Menu* \[PSU PBM MANAGER MENU\], 5
*Pharmacy Background Job Check* \[PSU PBM JOB CHECK\], 8
*Retransmit Patient Demograhic Data* \[PSU RETRANSMIT PATIENT DATA\], 9
Orientation, 3
Outpatient Visits Extract, 85
P
Patient Demographics Extract, 81
Pharmacy Background Job Check, 8
Prescription Extract, 49
Procurement Extract, 65
Provider Data Extract, 93
R
Related Manuals, 1
Retransmit Patient Demographic Data, 9
U
UD Extract, 33
V
Vitals/Immunizations Information Extract, 104
