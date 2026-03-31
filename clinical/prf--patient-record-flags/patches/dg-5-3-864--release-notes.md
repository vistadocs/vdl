---
title: DG*5.3*864 USH PRF Legal Solution Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: USH PRF Legal Solution
app_code: PRF
app_name: Patient Record Flags
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*864
group_key: "PRF:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: > Patches DG\5.3\864, GMTS\2.7\103, and TIU\1.0\275 address the Under Secretary of Health(USH) legal solution to provide a new national Category I patient record flag that will inform all Veteran Health Administration (VHA) caregivers of special guidelines that must be followed when documenting note
audience: 
keywords: 
  - flag
  - blockquote
  - table
  - assignment
  - patient
  - urgent
  - address
  - female
  - class
  - legal
page_count: 0
word_count: 1755
section_count: 3
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/dg_5_3_864_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/dg_5_3_864_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=156"
---

> ![](dg-5-3-864-ush-prf-legal-solution-release-notes/001.png)

## USH LEGAL SOLUTION –

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patient Record Flag (PRF) & TIU Note Title

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [USH LEGAL SOLUTION –](#ush-legal-solution)
- [Release Notes](#release-notes)
    - [DG\5.3\864 TIU\1\275 GMTS\2.7\103](#dg53864-tiu1275-gmts27103)
- [Introduction](#introduction)
    - [Required Software for DG\5.3\864, GMTS\2.7\103, and TIU\1.0\275](#required-software-for-dg53864-gmts27103-and-tiu10275)
    - [Registration – Patient Record Flag (DG) Features](#registration-patient-record-flag-dg-features)
    - [Text Integration Utility (TIU)](#text-integration-utility-tiu)
    - [Health Summary (GMTS)](#health-summary-gmts)
  - [Patient Safety Issue and Remedy Ticket](#patient-safety-issue-and-remedy-ticket)

### DG\*5.3\*864 TIU\*1\*275 GMTS\*2.7\*103

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> August 2013
> Department of Veterans Affairs Office of Information (OI) Product Development
1.  [Introduction 1](#introduction)
2.  Required Software 1
Related Documentation 1
3.  Features 2
![](dg-5-3-864-ush-prf-legal-solution-release-notes/002.png)[Registration – Patient Record Flag (DG) Features 3](#registration-patient-record-flag-dg-features)
[Adds New Category I PRF URGENT ADDRESS AS FEMALE 3](#adds-new-category-i-prf-urgent-address-as-female)
[Modifies the “Select a flag for this assignment” prompt to restrict assignment of the URGENT ADDRESS AS FEMALE flag 4](#modifies-the-select-a-flag-for-this-assignment-prompt-to-restrict-assignment-of-the-urgent-address-as-female-flag.)
[Displays a message at the “Assign Flag” action to indicate assignment of the URGENT ADDRESS AS FEMALE PRF is restricted. 5](#displays-a-message-at-the-assign-flag-action-to-indicate-assignment-of-the-urgent-address-as-female-prf-is-restricted.)![](dg-5-3-864-ush-prf-legal-solution-release-notes/003.png)
[Displays a message at the “Edit Flag Assignment” action to indicate editing of the URGENT ADDRESS AS FEMALE PRF assignment is restricted. 5](#displays-a-message-at-the-edit-flag-assignment-action-to-indicate-editing-of-the-urgent-address-as-female-prf-assignment-is-restricted.)![](dg-5-3-864-ush-prf-legal-solution-release-notes/004.png)
[The URGENT ADDRESS AS FEMALE PRF’s owning site assignment is not restricted from changing the owning site 5](#the-urgent-address-as-female-prfs-owning-site-assignment-is-not-restricted-from-changing-the-owning-site.)![](dg-5-3-864-ush-prf-legal-solution-release-notes/005.png)
![](dg-5-3-864-ush-prf-legal-solution-release-notes/006.png) Includes a post-installation routine that loads the URGENT ADDRESS AS FEMALE PRF file entry into the PRF National Flag file (#26.15) 6
![](dg-5-3-864-ush-prf-legal-solution-release-notes/007.png)[Pre-Install Step 7](#pre-install-step)
> GMTS\*2.7\*103 Pre and Post-Routines 9
![](dg-5-3-864-ush-prf-legal-solution-release-notes/008.png)Post-Install Setup
4.  Final Step: One site only - Add flag for designated patient. 10
5.  Patient Safety Issue and Remedy Ticket 10

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patches DG\*5.3\*864, GMTS\*2.7\*103, and TIU\*1.0\*275 address the Under Secretary of Health(USH) legal solution to provide a new national Category I patient record flag that will inform all Veteran Health Administration (VHA) caregivers of special guidelines that must be followed when documenting notes or dealing with a specific patient. This flag will require special permissions in order to be assigned to a patient, and, once assigned, it cannot be modified or inactivated other than allowing the reassignment of the owning facility. These three patches are being distributed as a single bundle.

> NOTE: MPIF\*1\*58, a related patch, is not part of the bundle described in this Release Notes document, but will need to be installed concurrently. The MPIF patch is to aid in the sharing of the patient record flags when the ICN is established by the MPIF LOC/MIS ICN RES background job.

### Required Software for DG\*5.3\*864, GMTS\*2.7\*103, and TIU\*1.0\*275

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Package/Patch                | Namespace | Version | Comments  |
|----------------------------------|---------------|-------------|---------------|
| Health Summary                   | GMTS          | 2.7         | Fully patched |
| Kernel                           | XU            | 8.0         | Fully patched |
| Registration/Patient Record Flag | DG            | 5.3         | Fully patched |
| VA FileMan                       | DI            | 22          | Fully patched |
| Text Integration Utilities (TIU) | TIU           | 1.0         | Fully patched |

1.  Related Documentation

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Documentation</strong></th>
<th><strong>Documentation File name</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>USH LEGAL SOLUTION – CATEGORY I</p>
<p>Patient Record Flag (PRF) Installation Guide</p></td>
<td>DG_5.3_864_IG.PDF</td>
</tr>
<tr class="even">
<td><p>USH LEGAL SOLUTION – CATEGORY I</p>
<p>Patient Record Flag (PRF) Release Notes</p></td>
<td>DG_5.3_864_RN.PDF</td>
</tr>
<tr class="odd">
<td>Patient Record Flag (PRF) User Guide</td>
<td>PatRecFlagUG.PDF</td>
</tr>
<tr class="even">
<td>Health Summary User Manual</td>
<td>HSUM2_7_103_UM.PDF</td>
</tr>
<tr class="odd">
<td>Health Summary Technical Manual</td>
<td>HSUM2_7_103_TM.PDF</td>
</tr>
<tr class="even">
<td>TIU User Manual</td>
<td>TIUUM-275.PDF</td>
</tr>
</tbody>
</table>

2.  Features

> Patch DG\*5.3\*864 will install the new Patient Record Flag. The new PRF must only be used with the guidance from the Office of Under Secretary of Health on a patient-by-patient basis. It may not be used for any other purpose or patient.

> ![](dg-5-3-864-ush-prf-legal-solution-release-notes/009.png) Patch TIU\*1\*275 installs one new Progress Note Title into the TIU DOCUMENT DEFINITION file (8925.1): PATIENT RECORD FLAG CATEGORY I – URGENT

> ADDRESS AS FEMALE. The patch installation links the title to the existing document class, PATIENT RECORD FLAG CAT I. This title will be automatically linked to the URGENT ADDRESS AS FEMALE Patient Record Flag during the install of DG\*5.3\*864.

> ![](dg-5-3-864-ush-prf-legal-solution-release-notes/010.png) Patch GMTS\*2.7\*103 provides two new Health Summary Types: VA-PT RECORD FLAG STATUS for local display of active and inactive patient record flags and REMOTE PT RECORD FLAG STATUS for use from Remote Data Views to see another treating facilities active and inactive patient record flags. Both of these Health Summary Types include a new Health Summary Component, CAT I PT RECORD FLAG STATUS, that displays the active and inactive Category I Patient Record Flags assigned to a given patient.

> ![](dg-5-3-864-ush-prf-legal-solution-release-notes/011.png) Patch DG\*5.3\*864 installs a new national Category I patient record flag: URGENT ADDRESS AS FEMALE PRF and associates the new PATIENT RECORD FLAG CATEGORY I – URGENT ADDRESS AS FEMALE progress note title with the new flag. This Patient Record Flag was established to ensure that a transgender Veteran is addressed as Female per a court order agreement. This flag cannot be used without approval of the Under Secretary for Health.

> The ability to assign the new URGENT ADDRESS AS FEMALE PRF will be limited to one identified IRM staff member with programmer access, or an identified clinician with temporary programmer access assigned by IRM staff at one pre-determined site. The identified person with programmer access at the pre-determined site will assign the URGENT ADDRESS AS FEMALE PRF to a pre-determined patient, identified by Under Secretary of Health (USH). The text used during the assignment will be based on very specific pre-defined text provided by the Office of the Under Secretary of Health.

> Once the USH-specified patient is assigned the URGENT ADDRESS AS FEMALE flag, the PRF cannot be inactivated for the patient. NOTE: Only one site will be assigning this flag to the patient. There will be no Review frequency for this flag assignment.

> The patch also includes a change to the Register a Patient \[DG REGISTER PATIENT\] option and the Load/Edit Patient Data \[DG LOAD PATIENT DATA\] option to ensure that Category I Patient Record Flags are updated when a patient registers at a new facility. The updates are provided from the existing VistA treating facility where the patient has been seen. This change is required to address a Patient Safety Issue (PSPO \#2365) and Remedy Ticket \#801785 – Category I Flag.

> NOTE: MPIF\*1\*58, a related patch, is not part of the bundle described in document, but will need to be installed concurrently. A code change has been made in routine MPIFBT3 to support the Patient Record Flag initiative distributed in VistA patch DG\*5.3\*864.

> For some time, the Register a Patient \[DG REGISTER PATIENT\] and Load/Edit Patient Data \[DG LOAD PATIENT DATA\] options have included the query for the Patient Record Flag. However, when a patient is created outside of these options, the query for the Patient Record Flag was not occurring.

> Also, if a patient does not get an Integration Control Number (ICN) via the direct connect to the Master Veteran Index during registration, that record gets a local ICN. The local ICN is resolved to a national ICN through the Local/Missing ICN Resolution Background Job \[MPIF LOC/MIS ICN RES\] option.

> The Local/Missing ICN Resolution Background Job \[MPIF LOC/MIS ICN RES\] now includes the query for the Patient Record Flag once the ICN has been returned to VistA and the patient is shared with another VAMC.

### Registration – Patient Record Flag (DG) Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Registration provides all facilities with a new national Category I Patient Record Flag (PRF) to be compliant with a legal solution agreed to by the Undersecretary for Health.

#### ![](dg-5-3-864-ush-prf-legal-solution-release-notes/012.png) Adds New Category I PRF URGENT ADDRESS AS FEMALE

> A new Category I Patient Record Flag will be added to the PRF National File (#26.15) with the following information:

- Name : URGENT ADDRESS AS FEMALE.
- Status: ACTIVE (installed as ACTIVE).
- Type: “OTHER”.
- Review Frequency Days): zero (0) – which means no review needed.
- Notification Days: zero (0).
- Flag: No Review Mail Group assigned (not necessary since no review notifications are needed).
- New TIU PN title assigned to it: PATIENT RECORD FLAG CATEGORY I – URGENT ADDRESS AS FEMALE.
- Description This Patient Record Flag was established to ensure that a transgender Veteran is addressed as Female per a court order agreement. This flag cannot be used without approval of the Undersecretary for Health.
- No Principal Investigator (Null - used for RESEARCH type flags only).
- The PRF National Flag File (#26.15) will have no DD changes for special handling of the new URGENT ADDRESS AS FEMALE flag. This will eliminate introduction of new problems with existing Patient Record Flag functionality.

#### ![](dg-5-3-864-ush-prf-legal-solution-release-notes/013.png) Modifies the “Select a flag for this assignment” prompt to restrict assignment of the URGENT ADDRESS AS FEMALE flag.

> The Registration patch modifies the Assign Flag action on the DGPF RECORD FLAG ASSIGNMENT option. The Select a flag for this assignment” prompt is modified to only allow users with programmer access (determined by DUZ(0)=”@”) to select and assign a patient the URGENT ADDRESS AS FEMALE PRF when prompting for a National flag.

> The Assumption is that the URGENT ADDRESS AS FEMALE PRF will display in the list of National flags, but will not be selectable. The alternative of adding screening to prohibit seeing the URGENT ADDRESS AS FEMALE PRF would impact the selection of other National flags and was not viewed as a viable coding solution.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>RECORD FLAG ASSIGNMENT</strong> Nov 16, 2012@11:23:38 Page: 1 of 1</p>
<p>Patient: CRPATIENT,TWO (666554444) DOB: 10/10/40</p>
<p>ICN: 9990000121V144170 CMOR: SALT LAKE CITY OIFO</p>
<p>Flag Assigned Review Date Active Local Owner Site</p>
</blockquote>
<ol type="1">
<li><p>HIGH RISK FOR SUICID 12/21/10 01/20/11 YES YES SALT LAKE CITY H</p></li>
<li><p>HIGH RISK FOR SUICID 01/31/12 04/30/12 YES NO SALT LAKE CITY H</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SP Select Patient EF Edit Flag Assignment</p>
<p>DA Display Assignment Details CO Change Assignment Ownership AF Assign Flag</p>
<p>Select Action:Quit// af Assign Flag Select a flag for this assignment: N.?</p>
<p>Answer with PRF NATIONAL FLAG NAME, or PRINCIPAL INVESTIGATOR(S)</p>
<p>Choose from:</p>
<p>BEHAVIORAL ACTIVE BEHAVIORAL</p>
<p>HIGH RISK FOR SUICIDE ACTIVE CLINICAL URGENT ADDRESS AS FEMALE ACTIVE OTHER</p>
<p>Enter the patient record flag name.</p>
<p>Enter one of the following: N.EntryName to select a National Flag L.EntryName to select a Local Flag</p>
<p>To see the entries in any particular file type &lt;Prefix.?&gt;</p>
<p>Select a flag for this assignment: N.URGENT ADDRESS AS FEMALE PRF</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ![](dg-5-3-864-ush-prf-legal-solution-release-notes/014.png) Displays a message at the “Assign Flag” action to indicate assignment of the URGENT ADDRESS AS FEMALE PRF is restricted.

> The Registration patch modifies options so that when the URGENT ADDRESS AS FEMALE PRF is selected by a user that does not have programmer access (determined by DUZ(0)=”@”), then a message is displayed to the user “This National Flag is limited to purposes authorized by Undersecretary for Health only” and returns the user to the “Select a flag for this assignment” prompt. *The message should not say anything about needing programmer access, to prevent the user from finding a person with programmer access to enter the PRF for a patient.*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select a flag for this assignment: N.URGENT ADDRESS AS FEMALE</p>
<p>“The URGENT: ADDRESS AS FEMALE National flag is limited to purposes authorized by Undersecretary for Health only.”</p>
<p>Answer with PRF NATIONAL FLAG NAME, or PRINCIPAL INVESTIGATOR(S)</p>
<p>Choose from:</p>
<p>BEHAVIORAL ACTIVE BEHAVIORAL</p>
<p>HIGH RISK FOR SUICIDE ACTIVE CLINICAL URGENT: ADDRESS AS FEMALE ACTIVE OTHER</p>
<p>Enter the patient record flag name.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### ![](dg-5-3-864-ush-prf-legal-solution-release-notes/015.png) Displays a message at the “Edit Flag Assignment” action to indicate editing of the URGENT ADDRESS AS FEMALE PRF assignment is restricted.

> A message is displayed to the user that indicates this PRF cannot be edited for the patient. The following text will display: “This URGENT ADDRESS AS FEMALE flag assignment cannot be edited.”

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>RECORD FLAG ASSIGNMENT</strong> Nov 16, 2012@11:31:58 Page: 1 of 1</p>
<p>Patient: CRPATIENT,TWO (666554444) DOB: 10/10/40</p>
<p>ICN: 9990000121V144170 CMOR: SALT LAKE CITY OIFO</p>
<p>Flag Assigned Review Date Active Local Owner Site</p>
</blockquote>
<ol type="1">
<li><p>URGENT ADDRESS AS FE 11/12/12 YES YES SALT LAKE CITY H</p></li>
<li><p>HIGH RISK FOR SUICID 01/31/12 04/30/12 YES NO SALT LAKE CITY H</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SP Select Patient EF Edit Flag Assignment</p>
<p>DA Display Assignment Details CO Change Assignment Ownership AF Assign Flag</p>
<p>Select Action:Quit// ef Edit Flag Assignment Select Record Flag Assignment: (1-2): 1</p>
<p>“This URGENT ADDRESS AS FEMALE flag assignment cannot be edited.”</p>
<p>Select Record Flag Assignment: (1-2):</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ![](dg-5-3-864-ush-prf-legal-solution-release-notes/016.png) The URGENT ADDRESS AS FEMALE PRF’s owning site assignment is not restricted from changing the owning site.

> Existing functionality in the DGPF RECORD FLAG ASSIGNMENT option’s, RECORD FLAG ASSIGNMENT, Change Assignment Ownership action allows changing the owning site for the assignment. No special coding is needed for this functionality.

#### ![](dg-5-3-864-ush-prf-legal-solution-release-notes/017.png) The Registration (DG) patch installation includes a post-installation routine that loads the URGENT ADDRESS AS FEMALE PRF file entry into the PRF National Flag file (#26.15).

> Due to FileMan restrictions, the only way the URGENT ADDRESS AS FEMALE PRF file entry can be added to the PRF National File (#26.15) is from a post-installation routine.

> The URGENT: ADDRESS AS FEMALE PRF file entry should have an Active status, alleviating the need for each site to activate use of the URGENT ADDRESS AS FEMALE PRF flag.

### Text Integration Utility (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new Text Integration Utility (TIU) patch, TIU\*1.0\*275 addresses the following requirements:

#### Adds New national Progress Note Title

> The TIU patch adds a new Progress note title to the TIU Document Definition file (#8925.1) with the following information:

> ![](dg-5-3-864-ush-prf-legal-solution-release-notes/018.png)![](dg-5-3-864-ush-prf-legal-solution-release-notes/019.png) NAME: PATIENT RECORD FLAG CATEGORY I – URGENT ADDRESS AS FEMALE

> PRINT NAME the same as the NAME. TYPE: “DOC”

> CLASS OWNER: CLINICAL COORDINATOR

> STATUS: ACTIVE (installed as ACTIVE) NATIONAL STANDARD: YES

> OK TO DISTRIBUTE: YES

> VHA ENTERPRISE STANDARD TITLE of “PATIENT RECORD FLAG” from the TIU VHA ENTERPRISE STANDARD TITLE (#8926.1) file.

### Health Summary (GMTS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](dg-5-3-864-ush-prf-legal-solution-release-notes/020.png) GMTS\*2.7\*103 provides a new component that displays the Active and Inactive Category I Patient Record Flags assigned to a given patient and also two new Health Summary Types.

> DESCRIPTION: This component displays the Active and Inactive Category 1

> Patient Record Flags assigned to a given patient. The full assignment history is included with each instance of flag assignment. Active

> flag

> assignments are displayed first, followed by Inactive flag assignments.

> HEALTH SUMMARY TYPE (#142)

> VA-PRF CAT 1 STATUS

> NAME: VA-PT RECORD FLAG STATUS LOCK: GMTSMGR

> SUMMARY ORDER: 5

> COMPONENT NAME: CAT I PT RECORD FLAG STATUS

> NATIONALLY EXPORTED TYPE: Nationally Exported, Uneditable

> REMOTE PRF CAT 1 STATUS

> NUMBER: 5000021 NAME: REMOTE PT RECORD FLAG STATUS

> LOCK: GMTSMGR SUMMARY ORDER: 5

> COMPONENT NAME: CAT I PT RECORD FLAG STATUS

> TITLE: Remote Pt Record Flag Status

> NATIONALLY EXPORTED TYPE: Nationally Exported, Uneditable

> HEALTH SUMMARY COMPONENT (#142.1)

> NUMBER: 257 NAME: CAT I PT RECORD FLAG STATUS

> PRINT ROUTINE: EN;GMTSRFHX ABBREVIATION: PRF1

> DESCRIPTION: This component displays the Active and Inactive Category 1 Patient Record Flags assigned to a given patient. The full assignment history is included with each instance of flag assignment. Active flag assignments are displayed first, followed by Inactive flag assignments.

#### ![](dg-5-3-864-ush-prf-legal-solution-release-notes/021.png) Pre-Install Step

> Before installing the bundle, sites will need to check for a local-versus-national conflict for HEALTH SUMMARY COMPONENT file (#142.1) entries. Examine the HEALTH SUMMARY COMPONENT file (#142.1) for any NUMBER (.001), NAME (.01), or

> ABBREVIATION (3) entries that will conflict with the new component exported with this patch. The national component NUMBER, NAME, and ABBREVIATION are as follows:

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 51%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>NUMBER (IEN)</th>
<th><blockquote>
<p>NAME</p>
</blockquote></th>
<th><blockquote>
<p>ABBREVIATION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>257</td>
<td><blockquote>
<p>CAT I PT RECORD FLAG STATUS</p>
</blockquote></td>
<td><blockquote>
<p>PRF1</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Internal Entry Numbers below 100001 are reserved for National health summary components. It is extremely unlikely that your site will have a component stored at IEN 257, as doing so would require programmer access and manual editing of the ^GMR(142.1 global. To check the global on your system, look at ^GMT(142.1,257. That location should be empty. If not, your site will need to submit a Remedy ticket for Health Summary support to assist in cleaning up that global entry. Before submitting the ticket, if the component is actually in use at your site and should be kept, it can be recreated as a local IEN and with a slightly different name. Use the “Create/Modify Health Summary Components” option of the

> GMTS IRM MAINTENANCE MENU to recreate the component. After recreating the component, submit the Remedy ticket requesting Health Summary support with: locating any items pointing to IEN 257, have those items re-pointed to the new local component location, and cleaning up the unwanted entry at IEN 257.

> The "B" cross-reference for the HEALTH SUMMARY COMPONENT file (#142.1), \[^GMR(142.1,"B",\], contains the NAME for each component. Each component entry in the file must have a unique NAME. Examine the global listing for this cross-reference to determine if any local component will need the NAME field edited to avoid collision with the new national component.

> ^GMT(142.1,"B","CAT I PT RECORD FLAG STATUS",660187)="" \<-Example of a

> local component that will conflict with the incoming CAT I PT RECORD FLAG STATUS component NAME.

> The "C" cross-reference for the HEALTH SUMMARY COMPONENT file (#142.1), \[^GMR(142.1,"C",\], contains the ABBREVIATION for each component. Each component entry in the file must have a unique ABBREVIATION. Examine the

> global listing for this cross-reference to determine if any local components will need the ABBREVATION field edited to avoid collision with the new national component.

> ^GMT(142.1,"C","PRF1",660187="" \<-Example of a local component that will conflict with the incoming CAT I PT RECORD FLAG STATUS component ABBREVIATION.

> If a NAME or ABBREVIATION conflict is found, the “Create/Modify Health Summary Components" option of the GMTS IRM MAINTENANCE MENU should be used to edit the local component's NAME or ABBREVIATION.

> ![](dg-5-3-864-ush-prf-legal-solution-release-notes/022.png) GMTS\*2.7\*103 Pre and Post-Routines

> GMTS\*2.7\*103 runs an environment check routine to ensure that IEN 257 in ^GMT(142.1 is unused and will also check for any NAME (.01) or ABBREVIATION (3) conflicts with the new component. If any conflicts are found, the environment check will indicate the conflict, the install will abort, and the transport global will be unloaded from the system.

> The pre-install routine will remove any previous version of the Reminder Exchange file that is used to install the two new Health Summary Types. In the event of multiple installations, this step ensures that the Reminder Exchange file used during installation is from the build instead of the version stored in the REMINDER EXCHANGE file (#811.9).

> The post-install routine will install the Health Summary Component into the HEALTH SUMMARY COMPONENT file (#142.1). This routine will also initiate the Reminder Exchange installation for the Health Summary Types.

> ![](dg-5-3-864-ush-prf-legal-solution-release-notes/023.png) Post-Install Setup

> Add the two new Health Summary Types, VA-PT RECORD FLAG STATUS and REMOTE PT RECORD FLAG STATUS to the list of available reports viewable in CPRS GUI. This can be done in different ways and from several different menus. Depending on local configuration, all health summary types may be available for selection or the selection may be configured to a defined list. See “Health Summary Configuration” in the Reports section of the CPRS Technical Manual: GUI Version for further information.

> Always follow your site’s local policies on how to assign these items to the list of available reports. Any users with a CPRS session open during the time of installation will need to close and re-open CPRS in order to see the new Health Summary Types on the Reports tab.

#### Example

> This example uses the Health Summary Coordinator's menu \[GMTS COORDINATOR\] to add the items for use at the System level.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>2</th>
<th><blockquote>
<p>User</p>
</blockquote></th>
<th>USR</th>
<th><blockquote>
<p>[choose from NEW PERSON]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td><blockquote>
<p>[choose from INSTITUTION]</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td><blockquote>
<p>[XXX.XX.XXXXXXXX]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td><blockquote>
<p>[choose from SERVICE/SECTION]</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Final Step: One site only will add the flag for designated patient.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>After all sites have completed the install, one site will be instructed, by the Office of Under Secretary for Health, to add the URGENT ADDRESS AS FEMALE flag for a specified patient.</strong> Any site that has treated this patient will be updated automatically by the patient record flag software after the flag is added for the patient.</p>
<p>New sites registering the patient will either be updated during the Registration process or by the Master Patient Index process that updates the patient’s national ICN and treating facility list.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Patient Safety Issue and Remedy Ticket

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following PSI and Remedy Ticket, which were logged previous to this project, are corrected with this patch bundle.

#### Patient Safety Issue (PSI)

> PSPO \#2365 - During testing of new software it was found when a patient registers at a new facility the backward look-up to determine of a Category I Record Flag exists for that patient at any other facility does not function correctly.

#### Remedy Ticket \#801785 - Category I Flag

> The automatic update (a routine unseen by users) of the Category I Flag to the new facility the patient is registering at does not work correctly.

> Corrections are made in the DG patch to the Patient Record Flag transmission routines addressed in this patch.