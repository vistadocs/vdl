---
title: DG*5.3*650 Patient Record Flags Phase III Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Patient Record Flags Phase III
app_code: PRF
app_name: Patient Record Flags
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*650
group_key: "PRF:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: The security key structure for controlling access to the Patient Record Flag (PRF) options has been simplified by reducing the number of security keys from four to three.
audience: 
keywords: 
  - flag
  - dgpf
  - record
  - assignment
  - report
  - security
  - enable
  - divisions
  - action
  - site
page_count: 0
word_count: 731
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/dg_53_650_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/dg_53_650_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=156"
---

![](dg-5-3-650-patient-record-flags-phase-iii-release-notes/001.png)

Patient Record Flags Phase IIIRelease Notes

DG\*5.3\*650

November 2006

Health Systems Design & Development (HSD&D)

Table of Contents

Modified Security Key Structure 1

Menu Structure 2

PRF Assignment Ownership in Multi-Divisional Systems 3

What was the Problem? 3

Detailed Solution 3

New Option 3

Modified Option 4

Modified Security Key Structure

The security key structure for controlling access to the Patient Record Flag (PRF) options has been simplified by reducing the number of security keys from four to three.

The DGPF PRF ACCESS and DGPF PRF CONFIG security keys are obsolete and have been deleted.

The DGPF LOCAL FLAG EDIT security key has been renamed to DGPF MANAGER. Users who were previously allocated the DGPF LOCAL FLAG EDIT will retain their access to the Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\] option. Additionally, holders of the DGPF MANAGER security key will have access to the new Record Flag Enable Divisions \[DGPF ENABLE DIVISIONS\] option.

The DGPF RECORD FLAG ASSIGNMENT security key has been renamed to DGPF ASSIGNMENT. Users who were previously allocated the DGPF RECORD FLAG ASSIGNMENT security key will retain their access to the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option.

The new DGPF TRANSMISSIONS key is used to control access to the new options Record Flag Transmission Errors \[DGPF TRANSMISSION ERRORS\] and Record Flag Manual Query \[DGPF MANUAL QUERY\].

Menu Structure

Patient Record Flags Main Menu (DGPF RECORD FLAGS MAIN MENU)

\|

\|---RM Record Flag Reports Menu \[DGPF RECORD FLAG REPORTS MENU\]

\| \|-----NLR Assignment Action Not Linked Report \[DGPF ACTION NOT LINKED REPORT\]

\| \|-----FAR Flag Assignment Report \[DGPF FLAG ASSIGNMENT REPORT\]

\| \|-----PAR Patient Assignments Report \[DGPF PATIENT ASSIGNMENT REPORT\]

\| \|-----ADR Assignments Due For Review Report \[DGPF ASSIGNMENT DUE REVIEW RPT\]

\| \|-----BAR Assignments Approved By Report \[DGPF APPROVED BY REPORT\]

\| \|-----IAR Assignments by Principal Investigator Report \[DGPF PRINCIPAL INVEST REPORT\]

\|

\|---FA Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\]

\| \*\*LOCKED: DGPF ASSIGNMENT\*\*

\|

\|---FM Record Flag Management \[DGPF RECORD FLAG MANAGEMENT\]

\| \*\*LOCKED: DGPF MANAGER\*\*

\|

\|---TM Record Flag Transmission Mgmt \[DGPF TRANSMISSION MGMT\]

\| \*\*LOCKED: DGPF TRANSMISSIONS\*\*

\| \|-----TE Record Flag Transmission Errors \[DGPF TRANSMISSION ERRORS\]

\| \*\*LOCKED: DGPF TRANSMISSIONS\*\*

\| \|-----MQ Record Flag Manual Query \[DGPF MANUAL QUERY\]

\| \*\*LOCKED: DGPF TRANSMISSIONS\*\*

\|---ED Record Flag Enable Divisions \[DGPF ENABLE DIVISIONS\]

\| \*\*LOCKED: DGPF MANAGER\*\*

PRF Assignment Ownership in Multi-Divisional Systems

What was the problem?

The original design of the Assign Flag action of the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option allowed the user to select the Owner Site of a PRF assignment from the list of all available Institutions. If the user chose an Owner Site that was not the primary site of a multi-divisional system, the user would be prevented from editing the assignment using the Edit Flag Assignment action or the Change Assignment Ownership action.

Detailed Solution

*New Option*

A new Record Flag Enable Divisions \[DGPF ENABLE DIVISIONS\] option has been added.

This new option has been added to allow multi-divisional sites to control which sites may act as PRF assignment owners by setting an Enable or Disable flag on each of the facilities in the MEDICAL CENTER DIVISION (#40.8) file.

The installation of patch DG\*5.3\*650 automatically enables the primary site station number as a PRF assignment owner. A divisional facility that has not been enabled as a PRF assignment owner using this option is treated as disabled and will not be available when selecting an Owner Site for a PRF assignment.

Enabling any additional divisions as PRF assignment owners will be the responsibility of the sites.

The following are Frequently Asked Questions regarding the Record Flag Enable Divisions option.

- *Why does site “ABC” not show up in the list of facilities to enable?*

> The following conditions must be met to “Enable” a facility as a PRF assignment owner.

1.  The facility must be defined in the MEDICAL CENTER DIVISION (#40.8) file.
2.  The INACTIVE FACILITY FLAG (#101) field in the INSTITUTION (#4) file must not be set to INACTIVE.
3.  The PARENT OF ASSOCIATION (#14, subfield \#1) field in the INSTITUTION (#4) file must be defined.
- *Why does site “XYZ” not show up in the list of facilities to disable?*

> A facility cannot be disabled when it is an Owner Site for any active PRF assignments.

- *How do I disable a facility that is currently used as an Owner Site for active PRF assignments?*

> Either inactivate each of the PRF assignments or change the ownership to another facility for each of the PRF assignments.

*Modified Options*

- The Assign Flag action of the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option has been modified.

> Assigning Category II (Local) patient record flags now requires that the user select an Owner Site for the assignment. The “Enter Owner Site” prompt for both Category I and Category II PRF assignments restricts facility selection to facilities that have been enabled as PRF assignment owners in the MEDICAL CENTER DIVISION (#40.8) file.

- The Edit Flag Assignment action of the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option has been modified.

> The editing of a PRF assignment is allowed only when the division assigned to the user at the time of VistA login matches the current Owner Site for the assignment.

- The Change Assignment Ownership action of the Record Flag Assignment \[DGPF RECORD FLAG ASSIGNMENT\] option has been modified.

> As in the Edit Flag Assignment action, the editing of a PRF assignment is allowed only when the division assigned to the user at the time of VistA login matches the current Owner Site for the assignment.

> The Owner Site of Category II PRF assignments may now be changed using this action. The “Select new owner site for this record flag assignment” prompt for Category II PRF assignments restricts facility selection to facilities that have been enabled as PRF assignment owners in the MEDICAL CENTER DIVISION (#40.8) file.

> The “Select new owner site for this record flag assignment” prompt for Category I PRF assignments now restricts the selection of facilities to the patient’s list of treating facilities in the TREATING FACILITY LIST (#391.91) file and facilities that have been enabled as PRF assignment owners in the MEDICAL CENTER DIVISION (#40.8) file.