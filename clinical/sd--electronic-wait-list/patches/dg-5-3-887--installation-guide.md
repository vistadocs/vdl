---
title: DG*5.3*887 Meaningful Use New VistA Data Elements (MUNVDE) Preferred Language Implement Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Meaningful Use New VistA Data Elements (MUNVDE) Preferred Language Implement Guide
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
menu_options: 1
description: 
audience: 
keywords: 
  - language
  - table
  - contents
  - preferred
  - vista
  - patient
  - meaningful
  - class
  - changes
  - impact
page_count: 0
word_count: 1012
section_count: 7
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 8/30/2016
revision_oldest: 8/30/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/dg_5_3_887_implement_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/dg_5_3_887_implement_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

Meaningful Use

New VistA Data Elements

Preferred Language

Implementation Plan

![](dg-5-3-887-meaningful-use-new-vista-data-elements-munvde-preferred-language-impl/001.png)

August 2016Version 2.0

Revision History

| Date      | Version | Description                                                                                                                                                                                                         | Author                             |
|-----------|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 8/30/2016 | 2.0     | Updated for the Meaningful Use New VistA Data Elements Preferred Language Patch. (This no longer includes the component for Smoking Use.)                                                                           | <span class="mark">REDACTED</span> |
| 9/2014    | 1.0     | Implementation Plan for DG\*5.3\*887, SD\*5.3\*619 supports changes that allow the electronic filing of Preferred Language elements and Smoking Use to meet the Meaningful Use 2014 Edition certification criteria. | <span class="mark">REDACTED</span> |

#### Table of Contents

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [New Functionality](#new-functionality)
    - [Implementation of the Preferred Language feature](#implementation-of-the-preferred-language-feature)
  - [Operational Changes](#operational-changes)
  - [Database Impact](#database-impact)
  - [Infrastructure Impact](#infrastructure-impact)
  - [Other Dependencies](#other-dependencies)
  - [Documentation Updated/Created](#documentation-updatedcreated)
- [Terms, Acronyms, Abbreviations, and Definitions](#terms-acronyms-abbreviations-and-definitions)

####### Meaningful Use Certification for Preferred Language Capture Process

The purpose of this Implementation plan is to capture the necessary steps required to implement the new software changes made to the VistA Registration and Schedulin*g* applications for the Meaningful Use Preferred Language Patch and defines the capture methodology.
This is to be used to capture the preferred language of Veterans in VA CPRS and VistA Systems. The patches to be installed: DG\*5.3\*887 and SD\*5.3\*619.
These patches are designed to meet the requirements for obtaining the 2011 (formerly Stage 1) Electronic Health Record (EHR) certification to support Meaningful Use (MU) demonstration by the VA in CPRS/VistA for the 2014 Edition certification criteria.
Ultimately, VistA will include the functionality needed to obtain both 2014 EHR certifications and to support MU demonstration. However, this first version of the VistA changes provides a partial solution for 2014 EHR certification relative to preferred language MU Stage 1 demonstration.
Intended audience for this document: Facility administrative and clinical personnel who are users of Veterans Health Information Systems and Technology Architecture (VistA) Admissions, Discharges, Transfers (ADT)/Registration, CPRS, and Scheduling/Appointment applications.
> **NOTE:** PIMS is the Patient Information Management System

## New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Implementation of the Preferred Language feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<td><p>A new multiple field LANGUAGES ENTRY DATE has been added to the PATIENT file (#2) and are utilized by current menu options.</p>
<p>These new selections are available to the PIMS or other authorized users under the ADT Registration Menu, Register a Patient and/or Load/Edit Patient Demographics - screen &lt;1.1&gt;.</p>
<p>Users who have access to these menus will be able to start utilizing the Preferred Language fields.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>If the patient has already been registered, the Make Appointment option in the Scheduling package will capture those patients that make a scheduled or unscheduled visit. No new options are required to access these features in the Scheduling Menus.</p>
<p>Users who have access to these menus will be able to start utilizing the Preferred Language fields.</p>
<p>During Make Appointment a protocol will check for Preferred Language info and if not present will prompt the user to enter the Preferred Language info, if it is present the user will not have to re-enter it unless it is different at the time of the current visit.</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>Users with access with to CPRS may access the Patient Demographics Tab /Patient Inquiry window to display patient demographic information in the CPRS GUI.</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>The LANGUAGE file (#.85) will house the LANGUAGES for selection at the Preferred Language field during registration in the additional patient demographic data screen and for display within the Patient Inquiry.</p>
<p>The Preferred Language field will accept multiple entries by date and time.</p>
<p>The user will enter the date/time of the new entry and view to select the references in the LANGUAGE file.</p>
<p>Changes to this field are date set to retain an audited event and is viewable via FileMan in a format that identifies the changed information for Supervisors or those who have a need to know.</p></td>
</tr>
<tr class="even">
<td>5</td>
<td><p>A new report that displays the number of Veterans who have provided a response to the Preferred Healthcare Language prompt has been created called: Meaningful Use Language Statistics [DG MEANINGFUL USE LANG STATS].</p>
<p>PIMS or other Managers who need to run this report will be able to access this menu option from the ADT Manager Menu. It can also be added as a SECONDARY Menu option if so desired.</p></td>
</tr>
</tbody>
</table>

## Operational Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This system supports the MU Preferred Language VistA/CPRS Operating Plan element of developing a modular EHR certification with the Dept. of HHS 2014 Edition Certification Criteria in both ambulatory and inpatient settings.

This request will furnish Administrative and Clinical Staff with the ability to gather the preferred language data at the time of the veteran’s registration or appointment interview.

The only operational change will be to gather additional information from the Veteran during normal daily operations.

## Database Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch bundle required the following modifications to VistA ADT/Scheduling system:

- Patch DI\*22.2\*0 modified the LANGUAGE file (#.85), to contain the ISO set of standard languages
- Patch DG\*5.3\*887and SD\*5.3\*619 modify the Patient File \#2 to include a multiple field called Language Entry Date that captures the preferred language elements and references the Language File.
- One new menu option called “Meaningful Use Language Statistics” was created and added to the ADT MANAGER Menu.

## Infrastructure Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement involves no new hardware or the interfacing of any hardware.

## Other Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no other dependencies for this enhancement.

## Documentation Updated/Created

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch bundle creates the following documentation and is available on the VA Software Documentation Library at*:* <http://www4.va.gov/vdl/>.

| File Description                           | Documentation File Name |
|------------------------------------------------|-----------------------------|
| MUNVDE Preferred Language Installation Guide   | DG_5_3_887_Install_Guide    |
| MUNVDE Preferred Language Release Notes        | DG_5_3_887_Rel_Notes        |
| MUNVDE Preferred Language Implementation Guide | DG_5_3_887_Implement_Guide  |
| ADT Module/Registration Menu User Manual       | dg_5_3_p887_reg_um          |

# Terms, Acronyms, Abbreviations, and Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term/Acronym | Author                                                          |
|--------------|-----------------------------------------------------------------|
| ADT          | Admission/Discharge/Transfer                                    |
| CBO          | Chief Business Office                                           |
| SD           | Scheduling                                                      |
| DG           | Registration Package                                            |
| MU           | Meaningful Use                                                  |
| VistA        | Veterans Health Information Systems and Technology Architecture |