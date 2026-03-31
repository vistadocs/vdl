---
title: PSO*7*233 Bad Address Enhancements Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Bad Address Enhancements
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*233
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - address
  - patient
  - update
  - temporary
  - table
  - contents
  - profile
  - label
  - pharmacy
  - indicated
page_count: 0
word_count: 2055
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p233_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p233_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](pso-7-233-bad-address-enhancements-release-notes/001.png)

Bad address enhancements

OUTPATIENT PHARMACY

RELEASE NOTES

PSO\*7\*233

September 2006

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Overview of Enhancements](#overview-of-enhancements)
- [Security Key Update](#security-key-update)
- [Field Update](#field-update)
- [Option Updates](#option-updates)
- [Input Template Update](#input-template-update)
- [Laser Label Printing Updates](#laser-label-printing-updates)
- [Transitional Pharmacy Benefits Routine Update](#transitional-pharmacy-benefits-routine-update)
- [Routine Updates](#routine-updates)
PSO\*7\*233 enhances the usage by Outpatient Pharmacy V. 7.0 of Application Program Interfaces (APIs) to the Registration Package V. 3.5 to check the setting of the BAD ADDRESS INDICATOR field (#.121) in the PATIENT file (#2) and to update the permanent and temporary addresses. The BAD ADDRESS INDICATOR is one of the fields presented when using the API to update permanent address fields.
![](pso-7-233-bad-address-enhancements-release-notes/002.png)Note: With the release of Laser Labels Phase I (PSO\*7\*120), dot matrix labels routines will no longer be updated.
Outpatient Pharmacy V. 7.0 options are modified to not print the patient’s address if a bad address is indicated, and to prompt the user to update the patient's address when appropriate. If the patient has the BAD ADDRESS INDICATOR field set and no active temporary address, this is referred to as a “BAI condition.”
![](pso-7-233-bad-address-enhancements-release-notes/003.png)Note: Related changes for the Outpatient Pharmacy Automation Interface (OPAI) and Consolidated Mail Outpatient Pharmacy (CMOP) will be done in patches PSO\*7\*200 and PSX\*2\*54.
*(This page included for two-sided copying.)*

# Overview of Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Outpatient Pharmacy patch PSO\*7\*233 provides the following enhancements:

- A new security key, PSO ADDRESS UPDATE, is added to allow prompting for updating a patient address.
- If a patient’s name is flagged with a Bad Address Indicator, when the patient is selected in the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option, a warning message is displayed.
- If the last label activity for a prescription indicated a BAI condition, the letter “B” (for bad address) is added to the status column in the *Medication Profile* \[PSO P\], *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\], and *Complete Orders from OERR* \[PSO LMOE FINISH\] options. Also, when there is no ending date for a temporary address, a temporary address indication is added, including the text “(no end date)”.
- The Input Template \[PSO OUTPT\] is modified to remove temporary address update prompts. A new API to the Registration Package V. 5.3 is now used to update temporary address for the *Update Patient Record* \[PSO PAT\] option and the *Patient Record Update* \[PU\] action within the patient profile.
- When printing laser labels, if the BAD ADDRESS INDICATOR is set and there is no active temporary address, the mailing label prints \*\*BAD ADDRESS INDICATED\*\* and does not print the rest of the mailing address. A label log entry is added to indicate bad address when the label printed.
- In the *Complete Orders from OERR* \[PSO LMOE FINISH\] option, a warning message is displayed if the patient’s address is flagged with a Bad Address Indicator. If the temporary address is active, that information is displayed. The user will not be prompted to update the address from this option.
- The *Action Profile (132 COLUMN PRINTOUT)* \[PSO ACTION PROFILE\] option will display \*\*BAD ADDRESS INDICATED-(REASON), where REASON can be UNDELIVERABLE, HOMELESS, or OTHER.
- The Transitional Pharmacy Benefits (TPB) options have been disabled, but to keep changes consistent, the routine to print TPB letters is modified to look at the BAI condition and print \*\* BAD ADDRESS INDICATED \*\* if applicable.
- The *Patient Address Changes Report* \[PSO ADDRESS CHANGE REPORT\] option is modified to display additional mailing address­­–related fields. Using FileMan, users can turn on auditing for these fields to be displayed in the report.
- Two new codes are added to the HOLD REASON field (#99) in the PRESCRIPTION file (#52):
  - ‘7’ BAD ADDRESS
  - ‘8’ PER PATIENT REQUEST
- A new menu option, *Bad Address Reporting Main Menu* \[PSO BAI REPORT\], is added under the *Output Reports* \[PSO OUTPUTS\] option to include *Bad Address Suspended List* \[PSO BAI SUSPENDED\] and *List Prescriptions Not Mailed* \[PSO BAI NOT MAILED\].
- The *View Prescriptions* \[PSO VIEW\] option is changed to show Bad Address Indicated if the BAI flag is set and there is no active temporary address.

# Security Key Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the EDIT PATIENT DATA field (#.123) in the OUTPATIENT SITE file (#59) is set to “Yes”, all users will get the prompt to update the address if there is a BAI Condition. If the field is set to “No”, a new security key, PSO ADDRESS UPDATE, can be assigned to those individuals who should be prompted to update a patient’s permanent and/or temporary address.

Either the user must have this new security key or the EDIT PATIENT DATA field (#.123) in the OUTPATIENT SITE file (#59) must be set to “Yes” for the user to be prompted to update the address.

# Field Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reason codes have been added to the HOLD REASON field (#99) in the PRESCRIPTION file (#52):

- ‘7’ BAD ADDRESS
- ‘8’ PER PATIENT REQUEST

# Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are modified as described.

#### *Patient Prescription Processing* 

When a name is selected in the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option, if the patient’s address is flagged with a Bad Address Indicator, a warning message is displayed. If the EDIT PATIENT DATA field (#.123) in the OUTPATIENT SITE file (#59) is set to “Yes” or the user holds the new PSO ADDRESS UPDATE security key, the user will be asked if he/she wants to update the patient’s address. If a valid temporary address exists, a message with that information is displayed before the prompt to update the address.

Example: Warning message for patient flagged with BAI condition

OPPATIENT,ONE (000-00-0777)

> **WARNING:** The patient address is indicated as a bad

address (UNDELIVERABLE).

\* Temporary address is active \*

Do you want to update the address/phone? N// YES

Update (P)ermanent address, (T)emporary, or (B)oth: BOTH//

#### *Patient Prescription Processing, Medication Profile, and Complete Orders from OERR*

The following modifications are made to the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\], *Medication Profile* \[PSO P\], and *Complete Orders from OERR* \[PSO LMOE FINISH\] options:

- When the medication profile is displayed, the letter “B” (for Bad address) is added to the status column if the last label activity for that prescription indicated a BAI Condition. If the address is corrected and the label reprinted, the “B” no longer appears on the profile.

Example: Medication Profile with BAI Condition displayed in Status column

Medication Profile Sorted by ISSUE DATE

REF

Rx# Drug ST REM Issued

Last Fill

--------------------------------------------------------------------------

-----

\$300920A ACETIC ACID 2% OTIC SOL 15 ML A\>B 5 07-20-06

07-20-06

QTY: 1 SIG: INSTILL 2 DROPS AD AS NEEDED

\$100002514C SIMVASTATIN 10 MG S 5 06-29-06

12-10-06

QTY: 90 SIG: TAKE 1 TABLET AT BEDTIME

\$300927 UREA 10% LOTION AB 5 06-29-06

06-29-06

QTY: 1 SIG: APPLY SPARINGLY TO AFFECTED AREA AS NEEDED

- Previously, if no ending date existed for a temporary address, the fact that the address was temporary was not being displayed in the patient profile. Patch PSO\*7\*233 adds the temporary indication, including the text “(no end date)” if no ending temporary date exists.

Example: Indication of temporary address appears in patient profile

Disabilities:

(Temp Address from AUG 28,2006 till (no end date))

STREET ADDRESS LINE1

ANYTOWN PHONE: 555-1212

TEXAS

77379

#### *Complete Orders from OERR*

In the *Complete Orders from OERR* \[PSO LMOE FINISH\] option, after the prompt to display the medication profile and after the patient name and social security number are shown, if the patient’s address is flagged with a Bad Address Indicator, a warning message is displayed. If the temporary address is active, that information is displayed.

Example: Warning message for patient flagged with BAI condition

Do you want to see Medication Profile? Yes// NO

OPPATIENT, ONE (666-00-0777)

> **WARNING:** The patient address is indicated as a bad

address (UNDELIVERABLE).

\* Temporary address is active \*

Press Return to continue:

![](pso-7-233-bad-address-enhancements-release-notes/004.png)Note: In this option, the user is not prompted to update the address.

#### *Action Profile (132 COLUMN PRINTOUT)* 

The *Action Profile (132 COLUMN PRINTOUT)* \[PSO ACTION PROFILE\] option has been modified to display \*\*BAD ADDRESS INDICATED-(REASON). The reason is one of the following:

- UNDELIVERABLE
- HOMELESS
- OTHER

The Bad Address text will now appear on the report.

#### *View Prescriptions*

The *View Prescriptions* \[PSO VIEW\] option is modified to show BAI Condition if the BAI flag is set and no temporary address exists.

Example: BAI condition displayed when no temporary address

Enter RETURN to continue or '^' to exit:

Subj: PSO\*7\*233 PATCH TRACKER \[#44054384\] Page 2

-------------------------------------------------------------------------------

VIEW PRESCRIPTION: 713449A ACETAMINOPHEN 325MG TAB

Rx View (Active) Aug 30, 2006@18:44:09 Page: 1

of 5

OPPATIENT, ONE \*\* BAD ADDRESS INDICATED-(UNDELIVERABLE)

PID: 666-00-0146 Ht(cm): \_\_\_\_\_\_\_

(\_\_\_\_\_\_)

DOB: DEC 00,1953 (52) Wt(kg): \_\_\_\_\_\_\_

(\_\_\_\_\_\_)

#### *Output Reports*

A new menu option, *Bad Address Reporting Main Menu*, has been added to the *Output Reports* \[PSO OUTPUTS\] option. This menu option includes the following sub-menu options:

- *Bad Address Suspended List* \[PSO BAI SUSPENDED\], which identifies prescriptions for veterans with a BAI Condition. It is intended to provide the opportunity for users to be proactive regarding prescriptions that, when “Printed” or “Pulled Early from Suspense”, would be unable to be mailed.
- *List Prescriptions Not Mailed* \[PSO BAI NOT MAILED\], which provides a report of prescriptions with a routing of “Mail” that were not mailed because of a bad address. The Bad Address Condition is based on the last label activity entry being flagged as a bad address and a route other than “WINDOW”. If the address is corrected and a label reprinted, this prescription will no longer show on the report.

#### *Patient Address Changes Report* 

The *Patient Address Changes Report* \[PSO ADDRESS CHANGE REPORT\] option is modified to display additional mailing address–related fields from the PATIENT file (#2) and some fields related to the mail setting from the PHARMACY PATIENT file (#55). Using FileMan, users can turn on auditing for the following fields in order for them to be displayed in this report.

![](pso-7-233-bad-address-enhancements-release-notes/005.png)Note: Fields added to this report by this patch are indicated with an “\*” in front of the field name.

- For the PATIENT file (#2), turn on auditing for:

STREET ADDRESS \[LINE 1\] field (#.111)

ZIP+4 field (#.1112)

STREET ADDRESS \[LINE 2\] field (#.112)

STREET ADDRESS \[LINE 3\] field (#.113)

CITY field (#.114)

STATE field (#.115)

ZIP CODE field (#.116)

\* BAD ADDRESS INDICATOR field (#.121)

\* TEMPORARY ADDRESS ACTIVE? field (#.12105)

TEMPORARY STREET \[LINE 1\] field (#.1211)

TEMPORARY ZIP+4 field (#.12112)

TEMPORARY STREET \[LINE 2\] field (#.1212)

TEMPORARY STREET \[LINE 3\] field (#.1213)

TEMPORARY CITY field (#.1214)

TEMPORARY STATE field (#.1215)

TEMPORARY ZIP CODE field (#.1216)

\* TEMPORARY ADDRESS START DATE field (#.1217)

\* TEMPORARY ADDRESS END DATE field (#.1218)

- For the PHARMACY PATIENT file (#55), turn on auditing for:

\* MAIL field (#.03)

\* MAIL STATUS EXPIRATION DATE field (#.05)

# Input Template Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Input Template \[PSO OUTPT\] is modified to remove temporary address update prompts. Outpatient Pharmacy V. 7.0 uses a new API to the Registration Package V. 3.5 to update temporary addresses for the *Update Patient Record* option and the Patient Record Update action within the patient profile.

This option and action are also changed to check that the user holds the PSO ADDRESS UPDATE security key or the EDIT PATIENT DATA field (#.123) in the OUTPATIENT SITE file (#59) is set to “Yes” before the user is prompted to update the addresses.

# Laser Label Printing Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes are made to laser label printing:

- If the BAD ADDRESS INDICATOR is set and no active temporary address exists, the mailing label prints \*\* BAD ADDRESS INDICATED \*\* and does not print the rest of the mailing address.
- An additional label log entry is added for Bad Address Indicated at the time the label printed.

# Transitional Pharmacy Benefits Routine Update 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although the Transitional Pharmacy Benefits (TPB) options have been disabled, the routine to print TPB letters is modified to look at the BAI Condition and print \*\* BAD ADDRESS INDICATED \*\* if applicable. This modification keeps changes consistent within the software.

# Routine Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*233 adds the following new routines:

- PSOBAI
- PSOBAIR2
- PSOBAIRP

Patch PSO\*7\*233 modifies the following routines:

- PSOADDR
- PSODEM
- PSOLBL4
- PSOLBLN
- PSOLLL1
- PSOLMPAT
- PSOORUT1
- PSOORUT2
- PSOP1
- PSOPAT
- PSORX1
- PSORXVW
- PSOSD1
- PSOSD2
- PSOSD3
- PSOSDP
- PSOTPCLP

*(This page included for two-sided copying.)*