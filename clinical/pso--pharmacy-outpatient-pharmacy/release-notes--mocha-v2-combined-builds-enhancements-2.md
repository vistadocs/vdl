---
title: MOCHA Version 2 Combined Builds Enhancements 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: Combined Builds Enhancements 2
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 2
patch_id: PSO*2
group_key: "PSO:PSO:2"
file_numbers: []
security_keys: []
menu_options: 0
description: The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues.
audience: 
keywords: 
  - order
  - drug
  - pharmacy
  - table
  - contents
  - checks
  - inpatient
  - allergy
  - check
  - outpatient
page_count: 0
word_count: 3081
section_count: 7
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_psj_5_pso_7_rn_r0416.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_psj_5_pso_7_rn_r0416.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

![](mocha-version-2-combined-builds-enhancements-2-release-notes/001.png)

Medication Order Check Healthcare Application (MOCHA)

Enhancements 2

GMRA\*4\*46, OR\*3\*269, PSJ\*5\*281 and PSO\*7\*411  
(MOCHA ENH 2 COMBINED BUILD 1.0)

Stand Alone Patch PSS\*1\*175

Release Notes

April 2016

Product Development

*(This page included for two-sided copying.)*Table of Contents

# *(This page included for two-sided copying.)*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Introduction](#introduction)
- [Enhancements/Corrections](#enhancementscorrections)
- [Menu Changes](#menu-changes)
- [New Options](#new-options)
  - [Changed Options](#changed-options)
  - [Deleted Options](#deleted-options)
  - [New Files](#new-files)
  - [New Fields](#new-fields)
- [Other Functionality](#other-functionality)
  - [Clinical Reminder Order Checks](#clinical-reminder-order-checks)
  - [Add CPRS Order Checks on Inpatient Medications Unit Dose Orders when Editing the Dosage of an Existing Order](#add-cprs-order-checks-on-inpatient-medications-unit-dose-orders-when-editing-the-dosage-of-an-existing-order)
- [<span class="mark"> </span>Impacts to Other Packages](#span-classmark-spanimpacts-to-other-packages)
- [Known Anomalies](#known-anomalies)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues.

The first phase, Medication Order Check Healthcare Application (MOCHA) v1.0, implemented enhanced order checking functionality utilizing Health*e*Vet (H*e*V) compatible architecture and First Data Bank (FDB), Drug Information Framework (DIF), and Application Program Interfaces (APIs). A Graphical User Interface (GUI) application was developed for maintenance of FDB custom tables. A process to automatically update the standard and custom FDB data at each instance of the Cache’ database was provided.

The second phase, MOCHA v2.0, included the modifications to implement Max Single Dose order checks for the Order Entry Results Reporting (OERR), Inpatient Medications and Outpatient Pharmacy applications. It added a maximum single dose order check to the current VistA medication order checking system that uses the FDB business logic and database and is displayed to the user.

This release notes document provides a brief description of the new features and functions of the MOCHA Enhancements 2 (ME2) patches listed in the table below. More detailed information on the functionality can be found in the Application user and technical manuals found on the VistA Documentation Library (VDL).

| Application                    | Patch       |
|--------------------------------|-------------|
| Adverse Reaction Tracking      | GMRA\*4\*46 |
| Order Entry/Results Reporting  | OR\*3\*269  |
| Outpatient Pharmacy            | PSO\*7\*411 |
| Inpatient Medications          | PSJ\*5\*281 |
| Pharmacy Data Management (PDM) | PSS\*1\*175 |

> **IMPORTANT:** Recently released patch GMRA\*4\*48 contains an Allergy Assessment

Clean Up utility tool that produces a report that identifies discrepancies between

the ADVERSE REACTION ASSESSMENT file (#120.86) and the PATIENT ALLERGIES

file (#120.8). It is imperative that GMRA\*4\*48 be installed prior to the installation of

these ME2 patches, and that all data discrepancies identified by GMRA\*4\*48 have been

corrected. If not, installing the ME2 patches may result in drug allergy order checks

not displaying in CPRS and pharmacy during the medication order entry processes.

# Enhancements/Corrections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ME2 provides the following enhancements/corrections:

- Adds functionality to use Clinical Reminder Order Checks (CROCs) in Inpatient Medications and Outpatient Pharmacy backdoor order entry.
- Adds order status to order check messages for order checks against a Patient’s Active Medication Profile (CK Hidden Action) for Inpatient Medications and Outpatient Pharmacy.
- Provides Computerized Patient Record System (CPRS) order checks on Inpatient Unit Dose Orders when editing the dosage of an existing order.
- Corrects the problem where order checks performed during the AudioCare renewal process were stored in the ORDER CHECK INSTANCES (#100.05) File using the user who processed the refills, rather than the proxy user.
- Modifies the Outpatient Pharmacy to display CPRS order check messages before CROC messages.
- Adds functionality to Inpatient Medications edit sequence to perform order checks when the dosage field is modified.
- Corrects Outpatient Pharmacy backdoor order entry (CK Hidden Action) when a supply item is listed first on the med profile. The CK action displays the supply item error message and will now perform any subsequent order checks.
- Corrects the issue of a user having to press return twice to continue display on Inpatient Medications backdoor order entry (CK Hidden Action).
- Corrects an issue in Outpatient Pharmacy backdoor order entry. When editing a non-verified order, the dosing warning is displayed after accepting the order and then again when the user selects to verify the order.
- When editing the Med route for a Non-Verified IV fluid order in Inpatient Medications, a new order is not created and CPRS doesn't get an update for the change. This happens when the “USED IN IV FLUID ORDER ENTRY field (#13)” of the IV ADDITIVE file (#52.6) is set to Yes. This fix will cause a new order to be created and send an update to CPRS.
- Order checks are not performed when verifying a Non-Verified Unit Dose order. This happened when the "SO (Select Order)" action was used to select the order for verification from the profile after an edit was made to a Dosage Ordered field or any of the starred fields. If a number was entered instead of entering "SO" to select the order, the order checks worked correctly.
- When editing Dosage Ordered (or any of the starred fields) of a Non-Verified Unit Dose order, the Dosing check was performed but the Drug Interactions and Duplicate Therapy checks were not done during the verification process. This is corrected with the installation of the ME2 patches.
- Corrects a hard error when finishing a Unit Dose order using the Speed Finish (SF) action.
- Corrects the display of the drug interaction order check when a drug is on the remote profile but not on the local profile for Outpatient Pharmacy order entry.
- Corrects a problem for an inpatient to outpatient transfer of a pending order. The free text dosage is displayed in the dosage field when an order is entered through CPRS and is finished through backdoor order entry. Upon finish, the “&” ampersands were returned to CPRS within the updated order information which perpetuated the problem.
- Corrects a problem reported where an incorrect Causative Agent was displayed on an Allergy Alert due to a look up issue between file VA Product File (#50.68), VA Generic File (#50.6), and Drug Ingredient File (#50.416).

  Example: Patient has an allergy to Hydrochlorothiazide and a new order is being entered for Hydrochlorothiazide 25MG tab and the user sees the following:

  Now doing allergy checks. Please wait…

  A Drug-Allergy Reaction exists for this medication and/or class!

  Prospective Drug: HYDROCHLOROTHIAZIDE 25MG TAB

  Causative Agent: LATEX

  Historical/Observed: HISTORICAL

  Severity: Not Entered

  Signs/Symptoms: None Entered

  Provider Override Reason: N/A – Order Entered Through VistA

  The software incorrectly showed Latex as the Causative Agent.
- Adds Body Surface Area (BSA) to the Outpatient Pharmacy Medication Profile \[PSO P\] option header display.
- Modifies the order entry process in Outpatient Pharmacy and Inpatient Medications to show multiple allergy order checks when a single drug selection generates multiple allergy order checks. Also modifies the DA Hidden Action in both applications to display all of the order checks in this same scenario.

The following Patient Safety issues are addressed:

- PSPO \# 2530/2549, Remedy tickets 960690/960714/975660 - Under certain circumstances, ordering a drug for which a patient has a remote allergy but no local allergy, an allergy warning is not displayed in Outpatient Pharmacy.
- PSPO \# 281/457/2072 - Remedy tickets 130757/173383/510151/536052 - The wrong reactant is

  being displayed in the allergy check. The drug being ordered is being

  displayed as the causative agent, but now the actual causative agent will

  be displayed correctly, from the PATIENT ALLERGIES (#120.8) File.
- PSPO \# 2124, NSR 20100825 - Frivolous Dextrose warning with clindamycin allergy.
- PSPO \#2585, Remedy tickets 1004240/1015745/1043694/1093605 - Erroneous Allergy/Interaction display.
- PSPO \#2545 - An Inpatient Medications order entered via the Inpatient Order Entry \[PSJ OE\] option with the "Nature of Order" prompt delineated as "Written" and a documented pharmacy intervention, did not display on the BCMA Coversheet in the highlighted format to alert the BCMA end user of the intervention.
- PSPO \#2561 - For Outpatient Pharmacy if there is a drug on the remote profile, not on the local profile and you enter a drug that will cause a drug-drug interaction order check, the order check is occurring in CPRS but not backdoor pharmacy.
- PSPO \#2383, Remedy tickets 823464/453615 - During the drug-allergy order check process, the ordered drug's VA CLASSIFICATION value is examined to determine if a patient will have a reaction to the drug. This examination looks at the first four characters for non-analgesics and all five characters for analgesics. For non-analgesics, if a patient's profile lists multiple drug classes with the same first four characters as the ordered drug, only the last drug class listed is returned. Many times, the returned class is less clinically important than the other classes on the list.
- PSPO \#2069 - When a provider is shown an adverse reaction order check message, the provider has to cancel the order and then navigate to the coversheet to review both the severity and the signs and symptoms of the reaction. This patch addresses this issue by including the reaction's severity and its signs and symptoms in the order check message. For example, Previous MODERATE adverse reaction to IODINE resulted in VOMITTING.
- PSPO \#2099 - When a provider is shown an adverse reaction order check message with (LOCAL) at the end of the message, providers have misinterpreted this to mean the patient experienced a localized reaction (such as a rash) instead of the fact that the reaction was documented locally. This patch addresses this issue by replacing the site designation (local/remote) with the name of the site that documented the allergy and the date and time of when the documentation was entered.

The following remedy tickets are addressed:

- Remedy Ticket 933381 - Incorrect allergy/drug order checks reported by the site for Outpatient Pharmacy backdoor order entry.
- Remedy Ticket 589406 - When entering an IV order in Inpatient Medications for an IMO patient at a clinic, if that patient has an appointment scheduled at an IMO clinic, then exiting out of the order and viewing the Patient Information can cause an UNDEFINED error.
- Remedy Ticket 861870 - Unable to verify an active IV order in Inpatient Medications.
- Remedy Ticket 769980 - Enhanced order checks not occurring with Speed Renew in Outpatient Pharmacy backdoor order entry.
- Remedy Ticket 1055309 – In Outpatient Pharmacy a Pharmacist does not see the Provider Override Reason for an allergy alert when verifying an order that was finished by a technician.
- Remedy Ticket 1232967 - Drug Interactions against pending outpatient orders with only

a PHARMACY ORDERABLE ITEM (#50.7) File entry assigned, but no DRUG (#50)

File entry assigned, do not display in Outpatient Pharmacy.

The following New Service Requests (NSR) are addressed:

> 20080334 - A Clinical decision Support System is being requested to further enhance drug

order checking to improve patient care and reduce costs. This request is to address work

mandated as determined by Patient Safety Incident (PSI) evaluation.

> 20100825 *– *Add Signs/Symptoms and severity data to the drug-allergy order check message. Replace the site designation (local/remote) with the name of the site that documented the allergy and the date and time of when the documentation was entered. Populate the DRUG ALLERGIES (#17) Field in the ORDER CHECK INSTANCES (#100.05) File for drug-allergy order checks.

The following Change Requests (CRs) and Code Change Requests(CCRs) are addressed:

- CCR6596 - Edited Med Route on a Non-Verified IV Fluid order is not updated in CPRS.
- CR6812 - Service Correction inserting DRUG NAME or STRENGTH/DOSE UNIT into OR GTX DOSE INSTRUCTIONS for Unit Dose FREE TEXT CPRS Order.
- CR6938 - INPATIENT - Active Outpatient to Inpatient order (free text dose displayed) - "&" passed to CPRS.
- CR5297 - Adding Severity = Severe Intervention functionality to Allergy Sign/Symptoms Display for Inpatient Medications and Outpatient Pharmacy backdoor order entry. Also will require an intervention for a severe allergy in Inpatient Medications and Outpatient Pharmacy.
- CR5422 - Add sign/symptoms to Allergy/ADR order check display (Remote HDR) for Inpatient Medications and Outpatient Pharmacy backdoor order entry.
- CR6268 - Replace Local or Remote verbiage with Actual Station Name and sort message sets by SEVERITY for Inpatient Medications and Outpatient Pharmacy backdoor order entry.

  The following Rational Team Concert (RTC) defects are addressed:
- 153518 - When editing the Orderable Item of a unit dose order in Inpatient Medications, the Dosage Ordered is cleared. Based on the messages from Inpatient to CPRS resulting from the

> edit, CPRS would discontinue the original order, but CPRS did not create the new order

> as a result of the pharmacy edit. Inpatient will now send "DOSAGE NOT FOUND" in

> the message to CPRS when the Dosage Ordered is null on the newly created order, and

CPRS now creates the new order appropriately.

ME2 consists of five VistA patches which will be released together and must be installed together. Full installation instructions can be found in the Installation Guide, however the list of patches and the order in which they should be installed are as follows:

1.  PSS\*1.0\*175.
2.  MOCHA ENH 2 COMBINED BUILD 1.0 Host file which consists of four patches: GMRA\*4.0\*46, OR\*3.0\*269, PSJ\*5.0\*281, PSO\*7.0\*411.

# Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new menu changes introduced with these patches.

# New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new options introduced with these patches.

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Deleted Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pre-Init routine for patch OR\*3.0\*269 deletes the entire Data Dictionary of the ORDER CHECK INSTANCES File (#100.05). Then the new Data Dictionary is brought back in again with the build. There are new fields, and some of the pre-existing fields have been moved to different global locations. For that reason we will show the files in its global structure before the install and after the install.

Before Install:

^ORD(100.05,D0,0)= (#.01) ORDER \[1P:100\] ^ (#1) STATUS \[2P:100.01\] ^ (#2)

==\>OCCURRENCE \[3F\] ^ (#3) USER \[4P:200\] ^ (#4) OCCURRENCE D/T

==\>\[5D\] ^

^ORD(100.05,D0,1)= (#5) ORDER CHECK \[1P:100.8\] ^ (#6) CLINICAL DANGER LEVEL

==\>\[2S\] ^

^ORD(100.05,D0,2,0)=^100.58^^ (#8) ORDER CHECK MESSAGE

^ORD(100.05,D0,2,D1,0)= (#.01) ORDER CHECK MESSAGE \[1W\] ^

^ORD(100.05,D0,3,0)=^100.57^^ (#7) OVERRIDE REASON

^ORD(100.05,D0,3,D1,0)= (#.01) OVERRIDE REASON \[1W\] ^

^ORD(100.05,D0,4,0)=^100.517PA^^ (#17) DRUG ALLERGIES

^ORD(100.05,D0,4,D1,0)= (#.01) INTERACTING MEDICATION \[1P:50\] ^ (#1) LOCATION

==\>\[2S\] ^ (#2) CAUSATIVE AGENT \[3V\] ^ (#6) REMOTE

==\>LOCATION \[4P:4\] ^ (#7) INTERVENTION \[5P:9009032.4\] ^

==\>(#8) DATABASE \[6S\] ^ (#9) OBSERVED/HISTORICAL \[7S\] ^

==\>(#10) SEVERITY \[8S\] ^

^ORD(100.05,D0,4,D1,1,0)=^100.5173PA^^ (#3) VA DRUG CLASS

^ORD(100.05,D0,4,D1,1,D2,0)= (#.01) VA DRUG CLASS \[1P:50.605\] ^

^ORD(100.05,D0,4,D1,2,0)=^100.5174PA^^ (#4) DRUG INGREDIENTS

^ORD(100.05,D0,4,D1,2,D2,0)= (#.01) DRUG INGREDIENT \[1P:50.416\] ^

^ORD(100.05,D0,4,D1,3,0)=^100.5175PA^^ (#5) SIGNS/SYMPTOMS

^ORD(100.05,D0,4,D1,3,D2,0)= (#.01) SIGN/SYMPTOM \[1P:120.83\] ^

^ORD(100.05,D0,11)= (#13) PHARMACIST OVERRIDE COMMENTS \[1F\] ^ (#14)

==\>PHARMACIST \[2P:200\] ^

^ORD(100.05,D0,15)= (#14.1) PHARMACIST COMMENTS D/T \[1D\] ^

^ORD(100.05,D0,16,0)=^100.515^^ (#15) MONOGRAPH

^ORD(100.05,D0,16,D1,0)= (#.01) MONOGRAPH \[1W\] ^

^ORD(100.05,D0,17)= (#16) MONOGRAPH TERM \[1F\] ^

After Install:

^ORD(100.05,D0,0)= (#.01) ORDER \[1P:100\] ^ (#1) STATUS \[2P:100.01\] ^ (#2)

==\>OCCURRENCE \[3F\] ^ (#3) USER \[4P:200\] ^ (#4) OCCURRENCE

==\>DATE/TIME \[5D\] ^

^ORD(100.05,D0,1)= (#5) ORDER CHECK \[1P:100.8\] ^ (#6) CLINICAL DANGER LEVEL

==\>\[2S\] ^

^ORD(100.05,D0,2,0)=^100.58^^ (#8) ORDER CHECK MESSAGE

^ORD(100.05,D0,2,D1,0)= (#.01) ORDER CHECK MESSAGE \[1W\] ^

^ORD(100.05,D0,3,0)=^100.57^^ (#7) OVERRIDE REASON

^ORD(100.05,D0,3,D1,0)= (#.01) OVERRIDE REASON \[1W\] ^

^ORD(100.05,D0,4,0)=^100.517A^^ (#17) DRUG ALLERGIES

^ORD(100.05,D0,4,D1,0)= (#.01) REACTANT \[1F\] ^ (#2) CAUSATIVE AGENT \[2V\] ^

==\>(#6) LOCATION TYPE \[3S\] ^ (#7) REMOTE LOCATION \[4P:4\]

==\>^ (#8) ORIGINATION DATE/TIME \[5D\] ^ (#9)

==\>OBSERVED/HISTORICAL \[6S\] ^ (#10) SEVERITY \[7S\] ^

^ORD(100.05,D0,4,D1,1,0)=^100.5173PA^^ (#3) VA DRUG CLASSES

^ORD(100.05,D0,4,D1,1,D2,0)= (#.01) VA DRUG CLASS \[1P:50.605\] ^

^ORD(100.05,D0,4,D1,2,0)=^100.5174PA^^ (#4) DRUG INGREDIENTS

^ORD(100.05,D0,4,D1,2,D2,0)= (#.01) DRUG INGREDIENT \[1P:50.416\] ^

^ORD(100.05,D0,4,D1,3,0)=^100.5175PA^^ (#5) SIGNS/SYMPTOMS

^ORD(100.05,D0,4,D1,3,D2,0)= (#.01) SIGN/SYMPTOM \[1P:120.83\] ^

^ORD(100.05,D0,5,0)=^100.06PA^^ (#50) DISPENSE DRUGS

^ORD(100.05,D0,5,D1,0)= (#.01) DISPENSE DRUG \[1P:50\] ^

^ORD(100.05,D0,6,0)=^100.07VA^^ (#60) GROUP ONE PHARMACY ORDERS

^ORD(100.05,D0,6,D1,0)= (#.01) GROUP ONE PHARMACY ORDER \[1V\] ^

^ORD(100.05,D0,6,D1,1,0)=^100.14P^^ (#1) ADDITIVE

^ORD(100.05,D0,6,D1,1,D2,0)= (#.01) ADDITIVE \[1P:52.6\] ^

^ORD(100.05,D0,6,D1,2,0)=^100.72P^^ (#2) SOLUTION

^ORD(100.05,D0,6,D1,2,D2,0)= (#.01) SOLUTION \[1P:52.7\] ^

^ORD(100.05,D0,7,0)=^100.11A^^ (#70) GROUP TWO PHARMACY ORDERS

^ORD(100.05,D0,7,D1,0)= (#.01) GROUP TWO PHARMACY ORDER \[1F\] ^ (#2) REMOTE

==\>LOCATION \[2P:4\] ^

^ORD(100.05,D0,7,D1,1,0)=^100.113P^^ (#3) ADDITIVE

^ORD(100.05,D0,7,D1,1,D2,0)= (#.01) ADDITIVE \[1P:52.6\] ^

^ORD(100.05,D0,7,D1,2,0)=^100.114P^^ (#4) SOLUTION

^ORD(100.05,D0,7,D1,2,D2,0)= (#.01) SOLUTION \[1P:52.7\] ^

^ORD(100.05,D0,8)= (#81) INTERVENTION \[1P:9009032.4\] ^ (#82) CLOZAPINE

==\>DISPENSING FREQUENCY \[2S\] ^ (#83) DRUG INTERACTION

==\>SEVERITY \[3S\] ^ (#84) DATABASE \[4S\] ^

^ORD(100.05,D0,9,0)=^100.08P^^ (#90) CLOZAPINE LAB RESULTS

^ORD(100.05,D0,9,D1,0)= (#.01) CLOZAPINE LAB RESULT \[1P:63\] ^

^ORD(100.05,D0,10,0)=^100.13^^ (#100) CLINICAL EFFECTS

^ORD(100.05,D0,10,D1,0)= (#.01) CLINICAL EFFECTS \[1W\] ^

^ORD(100.05,D0,11)= (#13) PHARMACIST OVERRIDE COMMENTS \[1F\] ^ (#14)

==\>PHARMACIST \[2P:200\] ^ (#14.1) PHARMACIST COMMENTS

==\>DATE/TIME \[3D\] ^

^ORD(100.05,D0,12)= (#85) CROC OI \[1P:101.43\] ^ (#86) CROC RULE \[2P:801.1\] ^

^ORD(100.05,D0,16,0)=^100.515^^ (#15) MONOGRAPH

^ORD(100.05,D0,16,D1,0)= (#.01) MONOGRAPH \[1W\] ^

^ORD(100.05,D0,17)= (#16) MONOGRAPH TERM \[1F\] ^

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 4.3 for new Data Dictionaries.

# Other Functionality 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A summary of delivered functionality follows. Complete details can be found in the respective User Manuals for each package on the VDL.

## Clinical Reminder Order Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Reminder Order Checks (CROC’s) were introduced to the Provider community via CPRS v.28. These patches will introduce the same CROC’s to the Pharmacy user in the VistA Outpatient Pharmacy and Inpatient Medications packages. These order checks will occur after allergy processing, and before Enhanced Drug-Drug Interaction and Therapeutic Duplication Order Checks.

## Add CPRS Order Checks on Inpatient Medications Unit Dose Orders when Editing the Dosage of an Existing Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Release of MOCHA 1 in April 2011 introduced three “CPRS” order checks to the VistA Outpatient Pharmacy and Inpatient Medications packages:

- AminoGlycoside Ordered
- Dangerous Medications for patients \> 64
- Glucophage

It was found that these order checks were not being triggered when editing the dosage on an Inpatient Unit Dose order. This patch will add the execution of these three order checks when editing the dosage of an existing Inpatient Medications Unit Dose order.

# <span class="mark"> </span>Impacts to Other Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no impacts to other packages introduced with these patches.

# Known Anomalies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Summary:  Problem with local station name display in allergy message

Description:  Missing the display of the station name for an historical local allergy when remote allergies to the same causative agent are present.  However, the signs and symptoms from all stations will still display.  All of the information, including the station name, will display in the CPRS order checks section when finishing an order and will show when using the DA action. The fix will be in ME2 follow up patch PSO\*7.0\*458.

Summary: Free-Text dosage does not generate adverse reaction order check message.

Description: A patient must have an allergy to a Drug Ingredient. Then in CPRS, if a medication order is placed and a free-text dosage is entered, and one or all of the drugs match to the selected orderable item contains the ingredient of the allergy, the allergy check will not display to the user in CPRS. The fix will be in ME2 follow up patch GMRA\*4.0\*52.

Summary: “Press return to continue:” displays twice when editing/renewing/copying or finishing certain orders.

Description: When editing/renewing/copying or finishing an active Outpatient prescription that causes a new order to be created and that order has therapeutic duplications against at least one discontinued prescription on the patient’s current profile, a “Press return to continue” prompt may display twice without anything between the 2 prompts. The fix will be in ME2 follow up patch PSO\*7.0\*458.