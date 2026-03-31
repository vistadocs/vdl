---
title: PSJ*5*214 Release Notes-Patients on Specific Drug(s) Multidivisional Enhancements
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Patients on Specific Drug(s) Multidivisional Enhancements
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*214
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - ward
  - drug
  - prompt
  - class
  - patients
  - drugs
  - selected
  - table
  - contents
  - orders
page_count: 0
word_count: 1869
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p214_psn_4_p193_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p214_psn_4_p193_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

![](psj-5-214-release-notes-patients-on-specific-drug-s-multidivisional-enhancements/001.png)

Patients on specific drug(s) multidivisional enhancements

Release Notes

PSJ\*5\*214 and PSN\*4\*193

February 2010

Office of Enterprise Development

Table of contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Description of Option](#description-of-option)
- [Discussion of Changes](#discussion-of-changes)
  - [## Prompt User for Selected Division(s)](#prompt-user-for-selected-divisions)
  - [Prompt User for Selected Ward(s)](#prompt-user-for-selected-wards)
  - [Prompt User for a Ward Group](#prompt-user-for-a-ward-group)
  - [Allow Selection of a Parent VA Drug Class](#allow-selection-of-a-parent-va-drug-class)
  - [Number of Matches Prompt Change](#number-of-matches-prompt-change)
The Patients on Specific Drug(s) Multidivisional Enhancements provides modifications to National Drug File and Inpatient Medications. The following patches are included in this release:
- PSN\*4\*193
- PSJ\*5\*214
In combination, the two patches address the need to provide multidivisional functionality within the Inpatient Medications package’s *Patients on Specific Drug(s)* \[PSJ PDV\] option. Patch, PSN\*4\*193 will create the "AC" cross reference on the PARENT CLASS field (#2) of the VA DRUG CLASS file (#50.605).
The new cross reference is utilized by the Patients on Specific Drug(s) Multidivisional Enhancements patch PSJ\*5\*214. The enhancements included in the *Patients on Specific Drug(s)* \[PSJ PDV\] option are as follows:
- Prompt user for selected division(s)
- Prompt user for selected ward(s)
- Prompt user for a ward group
- Allow selection of a parent VA Drug Class
- Change default behavior of the number of matches prompt
*(This page included for two-sided copying.)*

# Description of Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Patients on Specific Drug(s)* \[PSJ PDV\] option creates a report that lists patients on specific Orderable Item(s), Dispense Drug(s), or Veterans Affairs (VA) class(es) of drugs. When more than one of these drugs is chosen, the user will have the option to only display patients with orders containing <u>all</u> of the selected drugs or classes. The default behavior will be to display patients with orders for <u>any</u> of the selected drugs or classes.

The user will be prompted for the start and stop dates. Orders that are active between these two dates will be listed on the report. The user then has the choice to see only IV orders, Unit Dose orders, or both types of orders. These orders may be sorted by patient name or by the start date of the orders. The user will choose to sort by Orderable Items, Dispense Drug, or VA class of drugs and then choose one or multiple drugs or classes. By using the “Select number of matches” prompt, the user may select how many of the items entered must be on a patient’s record in order for the patient to be displayed in the report.

For example: Patient A has an order for ACETAMINOPHEN TAB, patient B has an order for ASPIRIN TAB, and patient C has orders for both. If the user chooses two Orderable Items (ACETAMINOPHEN TAB and ASPIRIN TAB), and enters 1 (default) on the number of matches screen, the orders of all three patients will print. If the user chooses two Orderable Items and enters “2” on the number of matches screen only patient C’s orders will print.

Selecting a parent VA class will function as if the user had selected all of its children classes manually. Users will also be able to select one or more divisions and/or wards which will limit the results to print only patients from the locations entered. When selecting all divisions and all wards, an additional prompt is shown to allow selection of one pharmacy ward group for selected locations.

Example: Patients on Specific Drug(s) Report

Select MANagement Reports Menu Option: Patients on Specific Drug(s)

Enter start date: T-9 (JAN 30, 2001)

Enter stop date: T (FEB 08, 2001)

List IV orders, Unit Dose orders, or All orders: ALL// \<Enter\>

Do you wish to sort by (P)atient or (S)tart Date: Patient// \<Enter\>

List by (O)rderable Item, (D)ispense Drug, or (V)A Class of Drugs: Orderable Item

Select PHARMACY ORDERABLE ITEM NAME: WARFARIN TAB

Dispense Drugs for WARFARIN are:

WARFARIN 10MG U/D

WARFARIN 5MG U/D

WARFARIN 2.5MG U/D

WARFARIN 2MG U/D

WARFARIN 5MG

WARFARIN 7.5MG U/D

WARFARIN 2.5MG

WARFARIN 2MG

WARFARIN 7.5MG

WARFARIN 10MG

Select PHARMACY ORDERABLE ITEM NAME: \<Enter\>

Select number of matches: 1// \<Enter\>

Select division: ALL// \<Enter\>

Select ward: ALL// \<Enter\>

You may optionally select a ward group...

Select a Ward Group: \<Enter\>

Select PRINT DEVICE: NT/Cache virtual TELNET terminal

...this may take a few minutes...

...you really should QUEUE this report, if possible...

Press RETURN to continue "^" to exit: \<Enter\>

02/08/01 PAGE: 1

LISTING OF PATIENTS WITH ORDERS CONTAINING ORDERABLE ITEM(S):

WARFARIN

FROM 01/30/01 00:01 TO 02/08/01 24:00

--------------------------------------------------------------------------------

Start Stop

Patient Order Date Date

--------------------------------------------------------------------------------

PSJPATIENT,ONE WARFARIN TAB 01/30 01/31

000-00-0001 Give: 5MG PO QPM PRN

1 EAST

WARFARIN TAB 01/30 01/31

Give: 5MG PO QPM PRN

# Discussion of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Prompt User for Selected Division(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the “Select division” prompt, the user may take the default of ALL divisions, or choose one or more individual divisions. Only patients whose identified ward is within the chosen divisions will be displayed in the report.

At facilities in which all of the inpatient wards are associated with a single medical center division, this prompt will be suppressed so that it does not unnecessarily present the opportunity to select outpatient divisions, including Community Based Outpatient Clinics (CBOCs).

Select division: ALL// ?

ENTER:

\- Return for all divisions, or

\- A division and return when all divisions have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Answer with MEDICAL CENTER DIVISION NUM, or NAME, or FACILITY NUMBER, or

TREATING SPECIALTY

Choose from:

1 TXXX 500

2 AXXXXX 500

9 CINCINNATI 539

10 ALB-PRRTP 500PA

11 AXXXXX OPC 500A4

Select division: ALL// TXXX 500

Select another division: AXXXXX

1 AXXXXX 500

2 AXXXXX OPC 500A4

CHOOSE 1-2: 1 AXXXXX 500

Select another division:

*(This page included for two-sided copying.)*

## Prompt User for Selected Ward(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the “Select ward” prompt, the user may take the default of ALL wards, or choose one or more individual wards. The selection of wards may be limited to those wards associated with any divisions selected at the previous prompt. Only patients whose identified ward is among the chosen wards will be displayed in the report.

Select ward: ALL// ?

ENTER:

\- Return for all wards, or

\- A ward and return when all wards have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Answer with WARD LOCATION NUMBER, or NAME, or SERVICE, or \*NSERV, or

SYNONYM

Do you want the entire WARD LOCATION List? y (Yes)

Choose from:

13 REHAB

14 NHCU

16 DOMICILLARY

18 5 WEST PSYCH

19 SURGERY

49 ZZ3EN

50 3EN

51 3ES

59 SARRTP

60 INFIRMARY

Select ward: ALL// 3EN

Select another ward: 3ES

Select another ward:

Select PRINT DEVICE:

*(This page included for two-sided copying.)*

## Prompt User for a Ward Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the selections of the division and ward prompts are both entered with the default choice of ALL, the user will be presented with a prompt to select one pharmacy ward group. Ward groups are defined by the *Ward Groups* \[PSJU EWG\] option and are used in conjunction with Pick Lists for dispensing inpatient medications. A ward group may comprise several different ward entries from the WARD LOCATION file (#42) which all represent one physical location within the medical center.

Select division: ALL//

Select ward: ALL//

You may optionally select a ward group...

Select a Ward Group: ?

Answer with WARD GROUP NAME

Choose from:

TST 1 GROUP

PHARMACY BAXTER

TST 2 GROUP

PHARMACY

TST 3

PHARMACY

Select a Ward Group: TST 3

PHARMACY

*(This page included for two-sided copying.)*

## Allow Selection of a Parent VA Drug Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With patch PSJ\*5\*214, entry of a parent VA Drug Class at the selection prompt will act as if the user had manually entered each of its child drug classes individually. This can be useful when looking to identify all patients on a broad category of medications, such as antimicrobials or cardiac medications. The example shown here demonstrates use of VA Drug Class AH000 to identify all of the sub-classes of antihistamines.

List by (O)rderable Item, (D)ispense Drug, or (V)A Class of Drugs: VA Class of Drugs

Select VA DRUG CLASS CODE: AH000

ANTIHISTAMINES

Dispense Drugs for VA Class AH100 are:

PROMETHAZINE 25MG/ML INJ

TRIMEPRAZINE 2.5MG TAB

PROMETHAZINE 25MG SUPP

PROMETHAZINE HCL 50MG TAB

PROMETHAZINE HCL 25MG TAB

PROMETHAZINE HCL 6.25MG/5ML SYRUP

Dispense Drugs for VA Class AH109 are:

LORATADINE 10MG TAB

DESLORATADINE 5MG TAB

Dispense Drugs for VA Class AH102 are:

diphenhydrAMINE HCL 25MG CAP

diphenhydrAMINE HCL 50MG CAP

diphenhydrAMINE HCL 50MG/ML INJ

diphenhydrAMINE 50MG/ML SYR 1ML

diphenhydrAMINE HCL 12.5MG/5ML ELIXIR

diphenhydrAMINE 12.5MG CHEW TABS

DOXYLAMINE SUCCINATE 25MG TAB

Dispense Drugs for VA Class AH103 are:

Dispense Drugs for VA Class AH104 are:

CHLORPHENIRAMINE MALEATE 4MG TAB

DEXCHLORPHENIRAMINE MALEATE 6MG TAB,SA

Dispense Drugs for VA Class AH105 are:

hydrOXYzine HCL 25MG TAB

hydrOXYzine HCL 10MG TAB

hydrOXYzine HCL 50MG/ML INJ

CETIRIZINE HCL 10MG TAB

hydrOXYzine PAMOATE 25MG CAP

Dispense Drugs for VA Class AH106 are:

FEXOFENADINE HCL 180MG TAB

FEXOFENADINE HCL 60MG TAB

Dispense Drugs for VA Class AH107 are:

CYPROHEPTADINE HCL 4MG TAB

*(This page included for two-sided copying.)*

## Number of Matches Prompt Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to patch PSJ\*5\*214, the behavior of the *Patients on Specific Drug(s)* \[PSJ PDV\] option was to allow you to select more than one orderable item, dispense drug or VA class of drugs, and if you selected multiple items, the “number of matches” prompt would default to the total number of items selected. This default would then indicate that a patient had to have <u>all</u> of the selected medications in their profile in order to be listed in the report.

Beginning with patch PSJ\*5\*214, the default response for the “number of matches” prompt is changed to “1”. This functionality will result in a patient being listed in the report if they have <u>any</u> of the selected medications in their profile.

At any time, you may still manually select the desired number of matches to be found within a patient’s medication profile for them to appear in the final report.

Patients on Specific Drug(s)

Enter start date: T (DEC 23, 2008)

Enter stop date: T (DEC 23, 2008)

List IV orders, Unit Dose orders, or All orders: ALL//

Do you wish to sort by (P)atient or (S)tart Date: Patient//

List by (O)rderable Item, (D)ispense Drug, or (V)A Class of Drugs: Dispense Drug

Select DRUG GENERIC NAME: ATENOLOL 100MG TAB CV100

Select DRUG GENERIC NAME: ATENOLOL 50 MG TAB CV100

Select DRUG GENERIC NAME: \<RETURN\>

Select number of matches: 1//