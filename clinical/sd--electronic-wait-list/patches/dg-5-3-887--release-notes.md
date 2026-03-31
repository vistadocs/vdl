---
title: DG*5.3*887 Meaningful Use New VistA Data Elements (MUNVDE) Preferred Language Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Meaningful Use New VistA Data Elements (MUNVDE) Preferred Language
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*887
group_key: "SD:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 7
description: 
audience: 
keywords: 
  - language
  - table
  - preferred
  - contents
  - patient
  - vista
  - date
  - time
  - meaningful
  - class
page_count: 0
word_count: 1050
section_count: 9
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 8/30/2016
revision_oldest: 8/30/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/dg_5_3_887_rel_notes.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/dg_5_3_887_rel_notes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

Meaningful UseNew VistA Data ElementsPreferred LanguageRelease Notes

![](dg-5-3-887-meaningful-use-new-vista-data-elements-munvde-preferred-language-rele/001.png)

Patches DG\*5.3\*887SD\*5.3\*619February 2017V 1.0Revision History

| Date      | Version | Description                                                                                                                                                                                              | Author                             |
|-----------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 8/30/2016 | 1.0     | Technical edits                                                                                                                                                                                          | <span class="mark">REDACTED</span> |
| 8/2014    | 0.1     | Release Notes for patch DG\*5.3\*887, SD\*5.3\*619 that supports changes that allow the electronic filing of Preferred Language elements to meet the Meaningful Use 2014 Edition certification criteria. | <span class="mark">REDACTED</span> |

Table 1 - New Features

#### Table of Contents

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [New Features](#new-features)
  - [Operational Changes](#operational-changes)
  - [Security Considerations](#security-considerations)
  - [Database Impact](#database-impact)
  - [Infrastructure Impact](#infrastructure-impact)
  - [Other Dependencies](#other-dependencies)
  - [Documentation Updated/Created](#documentation-updatedcreated)
  - [Existing Issues and Workarounds](#existing-issues-and-workarounds)
- [Terms, Acronyms, Abbreviations, and Definitions](#terms-acronyms-abbreviations-and-definitions)
The purpose of this Release Notes document is to highlight the changes made to the VistA Registration and Schedulin*g* applications and to CPRS by the Preferred Language patches (DG\*5.3\*887 and SD\*5.3\*619) in order to capture the patient’s preferred language.
These patches are designed to meet the requirements for obtaining the 2011 (formerly Stage 1) Electronic Health Record (EHR) certification to support Meaningful Use (MU) demonstration by the VA in CPRS/VistA for the 2014 Edition certification criteria. Ultimately, VistA will include the functionality needed to obtain both 2014 EHR certifications and to support MU demonstration. However, this first version of the VistA changes provides a partial solution for 2014 EHR certification relative to preferred language MU Stage 1 demonstration.
The intended audience for this document is the facility administrative and clinical personnel who are users of Veterans Health Information Systems and Technology Architecture (VistA) Admissions, Discharges, Transfers (ADT)/Registration, CPRS, and Scheduling/Appointment applications.

## New Features 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement modifies ADT/Registration menu options and Scheduling/Appointment menu options to facilitate the capture of Preferred Language elements of patients.

Table 1 below lists all of the new features added by this enhancement.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">DG*5.3*887, SD*5.3*619</td>
</tr>
<tr class="even">
<td>1</td>
<td>A new multiple field LANGUAGE DATE/TIME, with LANGUAGE DATE/TIME field (#.01) and PREFERRED LANGUAGE field (#.02), is added to the PATIENT file (#2).</td>
</tr>
<tr class="odd">
<td>2</td>
<td>The ADDITIONAL PATIENT DEMOGRAPHIC DATA, SCREEN &lt;1.1&gt; is modified to display Language Date/Time and Preferred Language. These values can be edited on this screen via the Register a Patient [DG REGISTER PATIENT], Load/Edit Patient Data [DG LOAD PATIENT DATA], and Eligibility Verification [DG ELIGIBILITY VERIFICATION] options.</td>
</tr>
<tr class="even">
<td>3</td>
<td>The Patient Inquiry [DG PATIENT INQUIRY] option in VistA is modified to display the patient’s Language Date/Time and Preferred Language. The M routine DGRPD is modified to include the patient’s Language Date/Time and Preferred Language in the patient demographics that are displayed on the Patient Inquiry window within the CPRS GUI.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>A new option, Meaningful Use Language Statistics [DG MEANINGFUL USE LANG STATS], is added to the ADT Manager Menu [DG MANAGER MENU] option. This option generates a report that displays the number of active patients that have provided a response to the preferred language prompt. The report is titled ‘Preferred Language Record for Active Patients’.</td>
</tr>
<tr class="even">
<td>5</td>
<td><p>The Make Appointment [SDM] option is modified to request input of the patient’s preferred language and the date/time the preferred language was added to the system.</p>
<p>When making an appointment, a protocol will check for the patient’s preferred language info and if it is not present, the system will prompt the user to enter the Language Date/Time and the Preferred Language before continuing with scheduling the appointment. If the patient’s preferred language info is already present, the user will not be prompted to provide it again.</p></td>
</tr>
<tr class="odd">
<td>6</td>
<td>The LANGUAGE file (#.85) is updated by VA FileMan 22.2 (DI*22.2*0) to contain the complete set of International Organization for Standardization (ISO) standard languages. The Preferred Language field in the PATIENT file (#2) references the LANGUAGE file (#.85). These languages are used for selection at the Preferred Language prompt during registration, in the ADDITIONAL PATIENT DEMOGRAPHIC DATA, SCREEN &lt;1.1&gt;, during the making of an appointment, and for display within the patient inquiry. Changes to the Preferred Language fields are retained as audited events that are viewable.</td>
</tr>
</tbody>
</table>

## Operational Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This system supports the Meaningful Use (MU) Preferred Language VistA/CPRS Operating Plan element of developing a modular EHR certification with the Dept. of HHS 2014 Edition Certification Criteria in both ambulatory and inpatient settings. This request will furnish Administrative and Clinical Staff with the ability to gather the preferred language data to facilitate better treatment for the patient by allowing precise verbal communication through the use of interpreters, if necessary.

## Security Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement involves no new security changes.

## Database Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch bundle requires the following modifications to VistA Registration and Scheduling systems:

- Dependency patch DI\*22.2\*0 (FileMan 22.2) modifies the LANGUAGE file (#.85) to contain the ISO set of standard languages.
- Patch DG\*5.3\*887 modifies the PATIENT file (#2) to include a multiple field called Language Date/Time that captures the preferred language elements (Language Date/Time and Preferred Language) and references the LANGUAGE file (#.85).
- One new menu option, Meaningful Use Language Statistics \[DG MEANINGFUL USE LANG STATS\], is created and added to the ADT Manager Menu \[DG MANAGER MENU\]. This is a change to the OPTION file (#19).

## Infrastructure Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement does not involve any new hardware or the interfacing of any hardware.

## Other Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*754

DG\*5.3\*871

SD\*5.3\*441

## Documentation Updated/Created

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch bundle creates the following documentation and is available on the VA Software Documentation Library at*:* <http://www4.va.gov/vdl/>.

| File Description                           | Documentation File Name |
|------------------------------------------------|-----------------------------|
| MUNVDE Preferred Language Installation Guide   | DG_5_3_887_Install_Guide    |
| MUNVDE Preferred Language Release Notes        | DG_5_3_887_Rel_Notes        |
| MUNVDE Preferred Language Implementation Guide | DG_5_3_887_Implement_Guide  |
| ADT Module/Registration Menu User Manual       | DG_5_3_p887_reg_um.pdf      |
| PIMS Technical Manual                          | PIMSTM                      |

## Existing Issues and Workarounds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA menu options MUST BE USED for the process of capturing a patient’s preferred language. The use of VA FileMan is discouraged.

# Terms, Acronyms, Abbreviations, and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Terms, Acronyms, Abbreviations | Definitions                                                     |
|--------------------------------|-----------------------------------------------------------------|
| ADT                            | Admission/Discharge/Transfer                                    |
| SD                             | Scheduling                                                      |
| DG                             | Registration Package                                            |
| MU                             | Meaningful Use                                                  |
| VistA                          | Veterans Health Information Systems and Technology Architecture |