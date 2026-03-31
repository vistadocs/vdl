---
consolidated_title: "mental health assistant phase 3 release notes"
app_code: YS
doc_type: RN
master_source: "YS*5.01*105 Mental Health Assistant Phase 3 Release Notes"
master_pub_date: September 2013
consolidated_from: 3 versions
prior_versions:
  - "YS*5.01*103 Mental Health Assistant Phase 3 Release Notes"
  - "YS*5.01*106 Mental Health Assistant Phase 3 Release Notes"
---

Mental Health AssistantVersion 3 (MHA3)Patch YS\*5.01\*105

Release Notes

![](ys-5-01-105-mental-health-assistant-phase-3-release-notes/001.png)

September 2013

Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 54%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>9/9/13</td>
<td>0.10</td>
<td>Updated Inactivated Instruments section and Defect Fixes sections. Added PCLS - PTSD Checklist Stressor Specific to list of instruments. Added HD0000000824422 to Associated Remedy Tickets. Added Backout Plan section.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>8/23/2013</td>
<td>0.9</td>
<td>Updated list of instruments.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/17/2013</td>
<td>0.8</td>
<td>Peer review, editing review complete.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/14/2013</td>
<td>0.7</td>
<td>Added HD0000000507076 to list of Remedy tickets to match what is in the patch description.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/31/2013</td>
<td>0.6</td>
<td><p>Page 2: Added the PCLS (PTSD Checklist Stressor Specific) instrument to the table list.</p>
<p>Page 3: Added tickets to the Remedy list and additional verbiage.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/11/2012</td>
<td>0.5</td>
<td>Added content to reflect the scoring of WHODAS-2, and the changes to FAST, PCLS, PLCM, and PCLC from Patch 103.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/22/2012</td>
<td>0.4</td>
<td>Removed PCLS from instrument list; removed ROM from instrument list and added VRA; removed Patch 96 from Required Patches list per Vickey Elijah’s SQA recommendations.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/19/2012</td>
<td>0.3</td>
<td>Added Remedy Ticket Information; added the deletion of PCL-SZ and addition of PCLS to instrument list.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/7/2012</td>
<td>0.2</td>
<td>Added Remedy Ticket information</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/18/2012</td>
<td>0.1</td>
<td>Initial Draft</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

# # # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# # Introduction](#introduction)
- [Installation Requirements](#installation-requirements)
- [Required Patches](#required-patches)
- [Related Patches](#related-patches)
- [Release Method](#release-method)
- [New Functionality](#new-functionality)
  - [Scoring Considerations in WHODAS2](#scoring-considerations-in-whodas2)
- [Inactivated Mental Health InstrumentPTSD Checklist Stressor Specific - PCL-SZ](#inactivated-mental-health-instrumentptsd-checklist-stressor-specific-pcl-sz)
- [Defect Fixes](#defect-fixes)
- [Associated Remedy Tickets](#associated-remedy-tickets)
- [Associated Patient Safety Issues (PSIs)](#associated-patient-safety-issues-psis)
- [Backout Plan](#backout-plan)
- [Reference Documents](#reference-documents)
The purpose of this document is to provide an overview of the Mental Health Enhancements – Outcomes Monitoring (MHE-OM) functionality for Patch YS\*5.01\*105 in support of the Improve Veteran Mental Health (IVMH) initiative. This Patch includes the addition of 23 instruments to the Mental Health Application (MHA) and the modification of an existing instrument.

# Installation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software applications MUST be installed prior to installing MHA3 Patch YS\*5.01\*105

| Software Applications | Version |
|---------------------------|-------------|
| Kernel                    | 9.0         |
| VA FileMan                | 22.0        |
| Mailman                   | 8.0         |
| RPC Broker                | 1.1         |
| Toolkit                   | 7.3         |
| Mental Health             | 5.01        |
| CPRS                      | 28 or later |
| Text Integration Utility  | 1.0         |
| Consult/Request Tracking  | 3.0         |

# Required Patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patch MUST be installed prior to installing MHA3 Patch YS\*5.01\*105:

Software Applications Patch

Mental Health Version 5.01 YS\*5.01\*83

Mental Health Version 5.01 YS\*5.01\*103

# Related Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no other related patches in this release

# Release Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no other patches bundled into this release.

# New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality in Patch 105 provides enhancements with the addition of 22 new instruments:

> **NOTE:** this includes one update and three retired instruments.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Short Name</strong></th>
<th><blockquote>
<p><strong>Full Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AAQ-2</td>
<td>The Acceptance and Action Questionnaire (AAQ-2)            </td>
</tr>
<tr class="even">
<td>BAM-C</td>
<td>Brief Addiction Monitor - Consumption Items</td>
</tr>
<tr class="odd">
<td>BAM-IOP</td>
<td>Brief Addiction Monitor - IOP version  </td>
</tr>
<tr class="even">
<td>BAM-R</td>
<td>Brief Addiction Monitor - Revised                          </td>
</tr>
<tr class="odd">
<td>BARTHEL INDEX</td>
<td>Barthel Index of Activities of Daily Living                </td>
</tr>
<tr class="even">
<td>FFMQ</td>
<td>Five Facet Mindfulness Questionnaire                        </td>
</tr>
<tr class="odd">
<td>GPCOG</td>
<td>General Practitioner Assessment of Cognition               </td>
</tr>
<tr class="even">
<td>IADL</td>
<td>Lawton-Brody Instrumental Activities of Daily Living Scale </td>
</tr>
<tr class="odd">
<td><p>MBMD   </p>
<p>Note: this is an updated instrument.</p></td>
<td>Millon Behavioral Medicine Diagnostic--Bariatric Norms</td>
</tr>
<tr class="even">
<td>MHLC-C</td>
<td>Multidimensional Health Locus of Control: Form C </td>
</tr>
<tr class="odd">
<td>MINICOG</td>
<td>Mini-Cog                                                   </td>
</tr>
<tr class="even">
<td>MMPI-2-RF</td>
<td><p>Minnesota Multiphasic Personality Inventory-2-Restructured</p>
<p> Form   </p></td>
</tr>
<tr class="odd">
<td>MOCA</td>
<td>Montreal Cognitive Assessment                              </td>
</tr>
<tr class="even">
<td>MOCA ALT 1</td>
<td>Montreal Cognitive Assessment, Alternate 1                 </td>
</tr>
<tr class="odd">
<td>MOCA ALT 2</td>
<td>Montreal Cognitive Assessment, Alternate 2                 </td>
</tr>
<tr class="even">
<td>NEO-PI-3</td>
<td>NEO Personality Inventory-3                                </td>
</tr>
<tr class="odd">
<td>PCLS</td>
<td>Post Traumatic Stress Disorder (PTSD) Checklist Stressor Specific</td>
</tr>
<tr class="even">
<td>PHQ-15</td>
<td><p>Patient Health Questionnaire 15-Item Somatic Symptom</p>
<p>Severity Scale                                             </p></td>
</tr>
<tr class="odd">
<td>QOLI</td>
<td>Quality of Life Inventory                                  </td>
</tr>
<tr class="even">
<td>SSF</td>
<td>Status of Suicide Form </td>
</tr>
<tr class="odd">
<td>STMS</td>
<td>Short Test of Mental Status                                </td>
</tr>
<tr class="even">
<td>VR-12</td>
<td>Veterans Rand 12 Item Health Survey                        </td>
</tr>
<tr class="odd">
<td>VRA</td>
<td>Veteran Recovery Assessment                                </td>
</tr>
<tr class="even">
<td>WHODAS 2</td>
<td><p>World Health Organization Disability Assessment</p>
<p>Schedule 2.0                                               </p></td>
</tr>
</tbody>
</table>

## Scoring Considerations in WHODAS2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WHODAS2 (World Health Organization Disability Assessment Schedule 2.0) is an instrument that measures health and disability. It asks about difficulties due to health conditions over the past 30 days. Responses to questions H1, H2, and H3 of the instrument are entered in spin boxes with possible responses ranging from 1 day to 30 days.

Question H1 asks the total number of days, out of the last thirty, that difficulties were present; question H2 asks how many of the last thirty days the patient was <u>unable</u> to carry out usual activities because of any health conditions, and question H3 asks how many days the patient cut back on activities, <u>not counting</u> the days they were totally unable (H2). The responses by the patient to H2 and H3 should not exceed the value of H1. However, please note that the system does not prevent the patient from entering responses to questions H2 and H3 with combined values that exceed the value of H1.

# Inactivated Mental Health InstrumentPTSD Checklist Stressor Specific - PCL-SZ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After consultation with several Posttraumatic Stress Disorder (PTSD) experts involved in performance measure, joint Veterans Administration-Department of Defense (VA-DoD) initiatives, the National

Center for Posttraumatic Stress Disorder (NC-PTSD), and the Evidence-Based Psychotherapy (EBP) dissemination project, the PTSD Checklist Stressor Specific (PCL-SZ) instrument released in Patch YS\*5.01\*103 is inactivated because of its negative effects on the Evidence-Based Psychotherapy (EBP)

initiative.

MMPI 2 Short Form - MMP2S

This test is outdated and no longer supported by the test publisher. It has been replaced by the new version, Minnesota Multiphasic Personality Inventory-2-Restructured Form (MMPI2-RF).

Millon Clinical Multiaxial Inventory-II - MCMI2

This test is outdated and no longer supported by the test publisher. It has been replaced by the new version, Millon Clinical Multiaxial Inventory-III (MCMI3).

# Defect Fixes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Grammatical errors from Patch 103 that are fixed in Patch 105 include the following:

- Instrument FAST, question 6b, parenthesis is now closed.
- Instrument FAST, questions 6d and 6e, the word “incontinence” now has consistent capitalization.
- Instruments PCLC, and PCLM, question 10 in each, in the phrase “DISTANT OR CUT OFF,” “OR” is now in lower case to be consistent with other questions in the instrument.
- IADL  \#4 - Maintains house alone or with occasional assistance (e.g. heavy work domestic help).
- FAST 6b - Unable to bathe properly; (e.g. difficulty adjusting)
- PCLM \#9 - Loss of Interest in Activities you used to enjoy.  
- CIWA-AR-#11 Choice \#0 changed to Not Present

# Associated Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HD0000000290418 - The bariatric norm has been added to the MBMD (Millon Behavioral Medicine Diagnostic).
- HD0000000721216 - The scoring issue with two digit values is fixed in the

YS_MHA_AUX.dll file included in Patch 105.

- HD0000000739365 - The BAI (Beck Anxiety Index) report display has been changed to more clearly explain the results.
- HD0000000738279 - The BDI2 (Beck Depression Inventory - Second Edition) report display has been changed to more clearly explain the results. In addition, the BSI (Beck Scale for Suicide Ideation) and the BHS (Beck Hopelessness Scale) report displays have been changed to more clearly explain the results.
- HD0000000722890 - The problem with the ASI exam changing from Lite to Full when edited has been fixed.
- HD0000000537915 - The PHQ-2 (Patient Health Questionnaire-2) and PC PTSD (Primary Care PTSD Screen) report displays have been changed to include the verbiage requested.
- HD0000000507076 - An \<UNDEFINED\> error occurred at BDI2+1^YTBI because

a global node was missing.

- HD0000000754691, HD0000000779663, HD0000000805126, HD0000000824422 - Instruments with more than 200 questions were not displaying completely on workstations running Windows 7 operating system.

# Associated Patient Safety Issues (PSIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSPO 2299 - The Beck Anxiety Inventory (BAI) MH instrument done through the MHA is not displaying the correct scores for interpretation.

There are 21 questions each with four choice numbers ranging from 1 to 4. Some users who score it by hand count the choice number as the score (for example, choice 1 is worth 1 point and so on). However, the score is the choice number minus 1 (for example, choice 1 is worth no points, choice 2 is worth 1 point and so on).

With the install of patch YS\*5.01\*105, the report for the BAI will clearly document the patient's answers and their point value.

# Backout Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This project is adding additional instruments to an existing system. Any instruments that have defects can be easily disabled from use. 

# Reference Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information in this document is derived from the following sources:

- Mental Health Assistant Version 3 (MHA3) Installation Guide, Patch YS\*5.01\*105
- Mental Health Assistant Version 3 (MHA3) User Manual, Patch YS\*5.01\*105

The VistA MHA3 Installation Guide (i.e., YS501105_MHA3_IG.pdf and YS501105_MHA3_IG.doc), and User Manual (i.e., YS501105_MHA3_UM.pdf and YS501105_MHA3_UM.doc) are available in MS Word Format (doc) and Portable Document Format (pdf) on the [MHA3 VDL](http://www.va.gov/vdl/application.asp?appid=78) webpage.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: YS*5.01*103 Mental Health Assistant Phase 3 Release Notes

## Required Patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patch MUST be installed prior to installing MHA3 Patch YS\*5.01\*103:

Software Applications Patch

Mental Health V. 5.01 YS\*5.01\*96

## Related Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no other related patches in this release.

## Release Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no other patches bundled into this release.
