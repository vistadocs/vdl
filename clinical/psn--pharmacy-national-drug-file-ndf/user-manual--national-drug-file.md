---
consolidated_title: "national drug file - user manual"
app_code: PSN
doc_type: UM
master_source: "National Drug File - User Manual (Updated PSN*4.0*575)"
master_pub_date: October 1998
consolidated_from: 2 versions
prior_versions:
  - "National Drug File - User Manual (Updated PSN*4.0*576)"
---

<!-- image -->

# National Drug File
(NDF)

# # user manual


October 1998

(Revised July 2024)

<!-- image -->

Product Development

########### Revision History

The table below lists changes made since the initial release of this manual. Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. Either update the existing manual with the Change Pages document, or replace it with the updated manual.

**Note:** The Change Pages document may include unedited pages needed for two-sided copying. Only edited pages display the patch number and revision date in the page footer.

| **Date**   | **Revised Pages**                                            | **Patch Number**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------|--------------------------------------------------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 07/2024    | 95, 98, 103-104                                              | PSN*4.0*575        | Added reference to ECDSA encryption key, removed reference to DSA encryption key which is no longer supported                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 04/2022    | 73                                                           | PSN*4.0*572        | - Replaced the 4 examples in the **Display FDA Medication Guide** section with 2 examples - Updated Title page, Revision History, Table of Contents, Index, and Footers - See the unredacted version of this document, on the SOFTWARE library, to view PSN*4.0*572 REDACTED information                                                                                                                                                                                                                                                                    |
| 12/2017    | i-iv  4-5, 79-102, 108                                       | PSN*4*513          | Update Revision history, TOC, and Glossary.  New sections added related to the new PPS-N Menu                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 07/2017    | i-iv  4-6, 10-12,  48-60, 63-69 , 80-81, 83-84               | PSN*4.0*396        | Update Revision history and TOC Update Revision History &amp; TOC.  Update formatting to match standards.  Added text and screen captures for the following options:  Inquire to National Files [NAT]  Inquire to VA Product Info for Local Drug [PSIN]  Rematch/Match Single Drugs [REMA]  Verify Matches [VER]  Verify Single Match [SVER]  to display the new fields created by PSN*4*396 for CLINICAL EFFECTS OF DRUGS, HAZARDOUS WASTE and FORMULARY DESIGNATOR.  Update Glossary  REDACTED                                                            |
| 12/2016    | Title page                                                   | PSN*4.0*492        | Updated revised date to December 2016 to match release date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 11/2016    | 8, 9,  44, 45, 46, 47, 48, 49, 52, 53, 55, 56, 57-58, 68, 69 | PSN*4.0*492        | Added the Copay fields for Tier and Effective date on the screens for Drug Enter Edit (matching), PSNLOOK and PSNACT (inquires) for NDF.  Added specific detail about Fixed Medication Copayment Tiers and a screen capture for [PSNACT]. Also added 2 terms in the glossary to represent Copay Tier and Fixed Medication Copay Tier.                                                                                                                                                                                                                       |
| 12/2011    | i- iv, 40e-f, 41e-41h                                        | PSN*4*296          | Added text and screen captures for options  *Inquire to National Files*  [PSNACT] and  *Inquire to VA Product Info for Local Drug*  [PSNLOOK] to display the new fields created by PSN*4*296. These fields reflect changes to the Enhancements to Prescription Copayments  Project.  REDACTED                                                                                                                                                                                                                                                               |
| 04/2011    | i-iv, 40b-d, 41a-f                                           | PSN*4*262          | Added text and screen captures for options  *Inquire to National Files*  [PSNACT] and  *Inquire to VA Product Info for Local Drug*  [PSNLOOK] to display the three new fields created by PSN*4*261. These fields reflect enhancements to prevent the inadvertent  creation of supra-therapeutic possible dosages for high risk medications during the dosage creation segment of Pharmacy Data Management and National Drug File updates.  Updated Table of Contents.  REDACTED                                                                             |
| 04/2011    | i-iii, 45-46, 46a-d                                          | PSN*4*263          | Modifications to section on Displaying an FDA Medication Guide. New examples added.  Documentation released with PSN*4*262.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 05/2010    | i-iv, 4, 45-46, 47, 54                                       | PSN*4*108          | Added a new option, Display FDA Medication Guide  [PSN MED GUIDE].  Added a new section, Displaying an FDA Medication Guide.  Added FDA Medication Guide to the Glossary and Index.  REDACTED                                                                                                                                                                                                                                                                                                                                                               |
| 02/2009    | 40, 40a-b, 41a-d                                             | PSN*4*169          | Updated screen captures for options Inquire to VA Product Info For Local Drug [PSNLOOK] and Inquire to National Files [PSNACT] to reflect additional data displayed and minor changes to the display.  REDACTED                                                                                                                                                                                                                                                                                                                                             |
| 09/03      | iii, 4, 7, 16, 37b-37d,  53-54                               | PSN*4*70           | - Added the new options,  *Local Drugs Excluded from Drug-Drug Interactions*  and  *VA Products Excluded from Drug-Drug Interactions*  to the Menu list and the Reports section.  - Corrected the name of the DEA, SPECIAL HDLG field.  - Corrected a drug name in the  *Local Drug/VA Print Name Report*  .  - Updated the TOC and the Index with the new reports.                                                                                                                                                                                         |
| 07/03      | Title Page, i, 7-10,  25-26, 41a-c                           | PSN*4*65           | -Replaced the Title Page and Revision History page.  -Updated introduction to include DEA/PKI changes.  -Updated screen captures changed by this patch.                                                                                                                                                                                                                                                                                                                                                                                                     |
| 02/2003    | Title Page,  i-ii, 41d-46, 51, 52                            | PSN*4*62           | -Replaced the Title Page and Revision History page.  -Updated the  *Print a PMI Sheet*  option and example.  -Updated the Glossary for the PMI Sheet term.  - (Included pages for double-sided printing.)                                                                                                                                                                                                                                                                                                                                                   |
| 09/2001    | Title Page,  i, ii, 41d,42                                   | Developer  Request | - Replaced the Title Page (and associated blank page) and the Revision History page (and associated blank page after it p. ii.)  - The  *Print a PMI Sheet*  option stated that a specific vendor supplied the information for these sheets and the verbiage was changed to a “commercial vendor”.                                                                                                                                                                                                                                                          |
| 03/2001    | Title Page, i, ii, iii, iv, 4, 37a-b, 53                     | PSN*4*48           | – Replaced the Title Page (and associated blank page), and pages i, ii (blank), iii, and iv (blank), which include the Revision History and Table of Contents. Pages ii and iv have no changes, but were included for two-sided printing only.  – Replaced pages 4 and 53 with the new pages. Pages 3 and 54 have no changes, but were included for two-sided printing only.  – Inserted pages 37A-37B, which introduce the new  *Local Drug/VA Print Name Report*  option. Pages 37 and 38 have no changes, but were included for two-sided printing only. |
| 02/2000    | 4, 5, 6, 8, 9, 17, 34, 41, 41a-c                             | PSN*4*22           | Added a new option called  *Inquire to National Files*  .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

**Table of Contents**

Introduction	1

Related Manuals	1

Icons	3

Pharmacy Pre-Installation Preparation	5

Entering National Drug Codes	5

Menu	7

National Drug File V. 4.0 Menu	7

Using the Matching Options	10

Rematch/Match Single Drugs	10

Verify Matches	16

Verify Single Match	18

Merge National Drug File Data Into Local File	20

Allow Unmatched Drugs to be Classed	22

Using the National Drug File Reports Menu	26

National Drug File Reports Menu	26

Local Drug File Report	27

Report of VA Generic Names from National Drug	28

Report of Attempted Match Drugs	29

VA Product Names Matched Report	30

Local Drugs with No VA Drug Class Report	33

VA Drug Classification	35

NDF Info From Your Local Drug File	36

Supply (XA000) VA Class Report	40

Manually Classed Drugs Report	41

Local Drugs with No Match to NDF Report	42

Local Formulary Report	43

National Formulary Report	46

Drug-Drug Interaction Report	47

VA Products Marked for CMOP Transmission	48

VA Product Names By Class Report	50

Local Drug/VA Print Name Report	51

Local Drugs Excluded from Drug-Drug Interactions	53

VA Products Excluded from Drug-Drug Interactions	54

Using the Inquire Options	56

Inquiry Options	56

Inquire to Local Drug File	56

Inquire to VA Product Info For Local Drug	57

Auto-Creation of Supra-Therapeutic Possible Dosages	61

Fixed Medication Copayment Tier	64

Inquire to National Files	67

Fixed Medication Copay Tier Enhancements	72

Clinical Effects of Drugs	76

Printing a Patient Medication Information Sheet	78

Print a PMI Sheet	78

Displaying an FDA Medication Guide	81

Display FDA Medication Guide	81

PPS-N Menu	83

Schedule download of NDF update file	83

Schedule Install of NDF Update file	85

Manual Download of NDF Update file	87

Manual Install of NDF Update file	89

Reject/Complete of NDF Update file	94

PPS-N Site Parameters (Enter/Edit)	95

Vista Comparison Report	98

Download/Install Status Report	100

Manage Secure Shell (SSH) Keys	103

Glossary	107

Index	115

## ## Introduction

The National Drug File (NDF) V. 4.0 software module provides standardization of the local drug files in all Department of Veterans Affairs Medical Centers (VAMCs). Standardization includes the adoption of new drug nomenclature and drug classification, and links the local drug file entries to data in the National Drug files.

For drugs approved by the Food and Drug Administration (FDA), VAMCs have access to information concerning dosage form, strength and unit; package size and type; manufacturer’s trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among VAMCs.

With this version of NDF, a new design of the NATIONAL DRUG file (#50.6) will lay the foundation for timely data releases by Pharmacy Benefits Management (PBM) personnel to field facilities using the NDF Management System. As new drug products are released, this information can be quickly sent to facilities. Pharmacy end users will be able to match (classify) a greater percentage of their local drug files for new products. Update/delivery of data will be controlled by PBM personnel. Frequent updating of NDF will be possible with minimal time for installation and downtime.

In addition to the redesign of NATIONAL DRUG file (#50.6), Version 4.0 will provide the following enhancements:

- Addition of new fields to NDF, such as National Formulary and restriction indicators.
- Lay foundation for interfaces to other Commercial Off The Shelf (COTS) software to update NDF fields for new/revised drug information.
- Update current NDF with new/revised product information.
- Creation of an Application Programmer’s Interface (API) to accommodate all existing VISTA software Database Integration Agreements (DBIAs) with NDF.
- A clean-up of associated files, such as DRUG MANUFACTURER (#55.95), DRUG UNITS (#50.607), etc.
- Incorporation of approved enhancement requests by Pharmacy/Information Resources Management (IRM) end users.

### Related Manuals

*National Drug File V. 4.0 Release Notes*

*National Drug File V. 4.0 Installation Guide*

*National Drug File V. 4.0 Technical Manual/Security Guide*

### Icons

Icons used to highlight key points in this manual are defined as follows:

<!-- image -->

Indicates the user should take note of the information.

## Pharmacy Pre-Installation Preparation

### Entering National Drug Codes

The National Drug File (NDF) software uses National Drug Codes (NDCs) in an initial automatic process of matching a drug in the local DRUG file (#50) with a drug in the National Drug files. It is important to make sure that as many drugs as possible have been assigned their correct NDCs.

The more complete and accurate the NDC fields in the local DRUG file (#50), the more effective the automatic matching process.

It is important that you enter all National Drug Codes (NDCs) in the local DRUG file (#50) using Pharmacy Data Management’s (PDM) option *Drug Enter/Edit* [PSS DRUG ENTER/EDIT] before the IRM staff installs this version of the software. The correct NDC format is

Manufacturer Code	-	Product Code	-	Package Code

(1 - 6 characters)	(1 - 4 characters)	(1-2 characters)

The correct NDC format:   4-4-2,   5-3-2,   5-4-1,   or   5-4-2 (e.g., 0023-2323-01)

Please note that the software ***will not*** insert the dashes in the NDC for you; therefore, you must include the dashes when you enter the information.

## Menu

### National Drug File V. 4.0 Menu

REMA	Rematch/Match Single Drugs  [PSNDRUG]

VER	Verify Matches  [PSNVFY]

SVER	Verify Single Match  [PSNVER]

MERG	Merge National Drug File Data Into Local File  [PSNMRG]

AUTO	Automatic Match of Unmatched Drugs  [PSNAUTO]

CLAS	Allow Unmatched Drugs to be Classed  [PSNSTCL]

[Locked:  PSNMGR]

RPRT	National Drug File Reports [PSNSUBM]

LDF	Local Drug File Report  [PSNLDG]

VAGN	Report of VA Generic Names from National Drug  [PSNVAGN]

ATMP	Report of Attempted Match Drugs  [PSNEXC]

PROD	VA Product Names Matched Report  [PSNPFN]

NOCL	Local Drugs with No VA Drug Class Report  [PSNOCLS]

CLVA	VA Drug Classification  [PSNCLS]

DFL	NDF Info from Your Local Drug File  [PSNRPT]

SUPL	Supply (XA000) VA Class Report  [PSNSUPLY]

MANC	Manually Classed Drugs Report  [PSNMCLS]

NMAT	Local Drugs with NO Match to NDF Report  [PSNONDF]

***** LOCF	Local Formulary Report  [PSNFRMLY]  [Locked: PSNMGR]

NATF	National Formulary Report  [PSNNFL]

DDIN	Drug-Drug Interaction Report  [PSNTER]

CMOP	VA Products Marked for CMOP Transmission  [PSNCMOP]

PNCL	VA Product Names By Class Report  [PSNCLPR]

LDPN	Local Drug/VA Print Name Report [PSNVAPRINT]

LDRG	Local Drugs Excluded from Drug-Drug Interactions [PSNODDI]

VDRG	VA Products Excluded from Drug-Drug Interactions [PSNEXMPT]

INQ	Inquiry Options  [PSNQUER]

LINQ	Inquire to Local Drug File  [PSNVIEW]

****** PNIN	Inquire to VA Product Info For Local Drug [PSNLOOK]

NDCU	NDC/UPN Inquiry  [PSNUPN]

NAT	Inquire to National Files [PSNACT]

PMIS	Print a PMI Sheet  [PSNPMIS]

FDA	Display FDA Medication Guide  [PSN MED GUIDE]

PPS	PPS-N Menu ...

SD     	Schedule download of NDF update file

SI    	Schedule Install of NDF Update file

MD     	Manual Download of NDF Update file

MI     	Manual Install of NDF Update file

RJ     	Reject/Complete of NDF Update file

SP     	PPS-N Site Parameters (Enter/Edit)

VC     VistA Comparison Report

DIS    Download/Install Status Report

SSH    Manage Secure Shell (SSH) Keys

***** Formerly *Formulary Report*

****** Formerly *Lookup National Drug Info in Local File.*

## Using the Matching Options

### Rematch/Match Single Drugs

### [PSNDRUG]   Synonym: REMA

This option allows you to rematch entries that are incorrectly matched or could not be matched automatically. *Report of Attempted Match Drugs* will list those items that the software attempted to match but could not; it should be printed before this option is executed. This option may be used until all entries in the local DRUG file (#50) that can be matched have been matched. It should be used to match any new drug added to the local DRUG file (#50). This option screens for inactive date and searches the DEA, SPECIAL HDLG field (# 3) to determine if one of the following values exists in the field:

0 (zero)	Manufactured in Pharmacy

I	Investigational Drug

M	Bulk Compound Item

You must verify all matches made with this option. Failure to verify a drug that has been matched will prevent that drug from being merged when the *Merge National Drug File into Local File* option is executed.

Patch PSN*4*396 add the display of the FORMULARY DESIGNATOR field (#109) only in the selection list of the drug if defined in the VA PRODUCT file (#50.68).  With patch PSN*4*513, this field can be populated as part of the PPS-N Update process.

Example:

Select DRUG GENERIC NAME: OMEP

1   OMEPARZOLE 40MG EC CAP UD

2   OMEPRAZOLE 10MG CAP   PA-F Tier 4

CHOOSE 1-2: 1  OMEPARZOLE 40MG EC CAP UD

**Example 1: Rematch Manually Classed Drugs**

Select National Drug File Menu Option: REMA  Rematch / Match Single Drugs

Enter name of drug from your local drug file and a match

with the National Drug File will be attempted.

Press return at the "Select DRUG GENERIC NAME: " prompt to exit.

Select DRUG GENERIC NAME: VAPONEPHRINE  EPINEPHRINE RACEMIC 2.25% SOL.

N/F

Match local drug  EPINEPHRINE RACEMIC 2.25% SOL.                N/F    with

ORDER UNIT:

DISPENSE UNITS/ORDER UNITS: 1

DISPENSE UNIT:

No NDC to match...

I will attempt to match the NDCs from your SYNONYMS.

Match made with EPINEPHRINE RACEMIC 2.25% SOL.                N/F

Now select VA Product Name

1 EPINEPHRINE (EPI-PEN JR) 0.15MG/0.3ML INJECTOR     INJ,SOLN  AU100  E0198

2 EPINEPHRINE (EPI-PEN) 0.3MG/0.3ML INJECTOR     INJ,SOLN  AU100  E0197

3 EPINEPHRINE 0.15MG/0.3ML INJ     INJ,SOLN  AU100  E0099

4 EPINEPHRINE 0.16MG/SPRAY SUSP,INHL,ORAL     INHL,ORAL  RE102

5 EPINEPHRINE 0.1MG/ML INJ     INJ,SOLN  AU100  E0100

6 EPINEPHRINE 0.2MG/SPRAY INHL,ORAL     AEROSOL,ORAL  RE102

7 EPINEPHRINE 0.3MG/ML INJ     INJ,SOLN  AU100  E0101

examples continue on the next page

**Example 1: Rematch Manually Classed Drugs (cont.)**

8 EPINEPHRINE 0.5MG/ML INJ     INJ,SOLN  AU100

9 EPINEPHRINE 1MG/ML INJ     INJ,SOLN  AU100  E0015

10 EPINEPHRINE 1MG/ML INJ,SYRINGE,1ML     INJ,SOLN  AU100  E0205

Enter your choice or press return to continue: **1**

Is this a match  &lt; Reply Y, N or press return to continue &gt; : **Y**

CHOOSE FROM:

1    1  SYRINGE

2    0.3 ML  INJECTOR,AUTOMATIC

3    6 X 0.3 ML  INJECTOR,AUTOMATIC

4    OTHER  OTHER

Enter Package Size &amp; Type Combination: **2**

Local drug EPINEPHRINE RACEMIC 2.25% SOL.

matches    EPINEPHRINE (EPI-PEN JR) 0.15MG/0.3ML INJECTOR

PACKAGE SIZE: 0.3 ML

PACKAGE TYPE: INJECTOR,AUTOMATIC

&lt; Enter "Y" for yes &gt;

&lt; Enter "N" for no &gt;

&lt; Press return for next drug or "^" to quit&gt;      OK? : **Y**

Select DRUG GENERIC NAME: **&lt;RET&gt;**

Remember, these matches must be verified using the options "Verify Matches" or

"Verify Single Match" and then merged using the option "Merge National Drug File

Data Into Local File".

Select National Drug File Menu Option: **&lt;RET&gt;**

**Example 2: Rematching Drugs Matched, Verified, and Merged to NDF**

Select National Drug File Menu Option: **REMA** Rematch / Match Single Drugs

Enter name of drug from your local drug file and a match

with the National Drug File will be attempted.

Press return at the "Select DRUG GENERIC NAME: " prompt to exit.

Select DRUG GENERIC NAME: **TIMOLOL** 0.5% OPHT SOLN 5ML           OP101

This drug has already been matched and classified with the

National Drug File.

Do you wish to match/rematch it? N// **Y**

Match local drug  TIMOLOL 0.5% OPHT SOLN 5ML

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 1

DISPENSE UNIT: BT(5ML)

I will try to match NDC:   0006-3367-03   to NDF.

Local drug TIMOLOL 0.5% OPHT SOLN 5ML

matches    TIMOLOL MALEATE 0.5% SOLN,OPH

PACKAGE SIZE: 5 ML

PACKAGE TYPE: BOTTLE

Is this a match ?

Enter Yes or No: YES// &lt;RET&gt;

Select DRUG GENERIC NAME: **&lt;RET&gt;**

Remember, these matches must be verified using the options "Verify Matches" or

"Verify Single Match" and then be merged using the option "Merge National Drug File Data Into Local File".

examples continue on the next page

**Example 3: Rematch—Selecting Inactive Drug**

Select National Drug File Menu Option: **REM** Rematch / Match Single Drugs

Enter name of drug from your local drug file and a match

with the National Drug File will be attempted.

Press return at the "Select DRUG GENERIC NAME: " prompt to exit.

Select DRUG GENERIC NAME: **MORPHINE SO4** 200MG TAB,SA      CN101       08-21-03     OUTPATIENT REQUIRES "WET" SIGNATURE

This drug has an Inactivation date in the future. Do you want to continue? **Y**

(Yes)

This drug has been manually classed but not matched (merged with NDF).

Do you wish to match/rematch it? N// **Y**

Deleting Possible Dosages...

Match local drug  MORPHINE SO4 200MG TAB,SA

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 100

DISPENSE UNIT: TAB

I will try to match NDC:   00034-513-10   to NDF.

Local drug MORPHINE SO4 200MG TAB,SA

matches    MORPHINE SO4 200MG TAB,SA

PACKAGE SIZE: 100

PACKAGE TYPE: BOTTLE

Is this a match ?

Enter Yes or No: YES// &lt; **ENTER** &gt;

The CS Federal Schedule associated with this drug in the VA Product file

represents a DEA, Special Handling code of 2A

Enter RETURN to continue...

A warning message displays if a discrepancy is found between entries in the CS FEDERAL SCHEDULE field and the DEA, SPECIAL HDLG field when using the *Rematch / Match Single Drugs* [PSNDRUG] option. The following warning displays: "The CS Federal Schedule associated with this drug in the VA Product file represents a DEA, Special Handling code of XX,” where XX is the DEA, SPECIAL HDLG code mapped to the corresponding CS FEDERAL SCHEDULE code as shown here:

| **Schedule description**   | **If a drug entry has a**  **CS FEDERAL SCHEDULE of:**   | **And its corresponding DEA, SPECIAL HDLG field is blank, the following DEA, SPECIAL HDLG code will be inserted:**   |    |
|----------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----|
| Schedule I narcotics       | 1                                                        | 1                                                                                                                    | 1  |
| Schedule II narcotics      | 2                                                        | 2A                                                                                                                   | 2A |
| Schedule II non-narcotics  | 2n                                                       | 2C                                                                                                                   | 2C |
| Schedule III narcotics     | 3                                                        | 3A                                                                                                                   | 3A |
| Schedule III non-narcotics | 3n                                                       | 3C                                                                                                                   | 3C |
| Schedule IV narcotics      | 4                                                        | 4                                                                                                                    | 4  |
| Schedule V narcotics       | 5                                                        | 5                                                                                                                    | 5  |

#### Verify Matches

**[PSNVFY]   Synonym: VER**

With this option you can loop through the list of matched but unverified drugs and verify each one. It is not necessary to verify all matches at once. You can press the Return key to skip any entries you do not want to verify. It will also allow you to rematch a drug if you do not like the match. This option can be used any time after drugs from the local DRUG file (#50) have been matched with drugs in the National Drug files using the options *Rematch/Match Single Drugs* , or *Automatic Match of Unmatched Drugs* .

All matched drugs must be verified. Unverified matches are stored in the NATIONAL DRUG TRANSLATION file (#50.612), and will not merge until they are verified. To ensure accuracy one individual should match the drugs and another verify the matches.

Print VA Product Names Matched report to have a list of unverified matched drugs in the same order they will appear on the screen for verification.

Patch PSN*4*396 added FORMULARY DESIGNATOR field (#109) and

FORMULARY DESIGNATOR TEXT field (#110) if defined.

Example:

National Formulary Indicator: Yes

FORMULARY DESIGNATOR: PA-N

NATIONAL FORMULARY RESTRICTION:

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE.

Copay Tier: 1

**Example: Verify Match**

Select National Drug File Menu Option: **VER** Verify Matches

LOCAL DRUG NAME: **MORPHINE SO4** 200MG TAB,SA

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 100

DISPENSE UNIT: TAB

VA PRODUCT NAME: MORPHINE SO4 200MG TAB,SA

VA PRINT NAME: MORPHINE SO4 200MG SA TAB                 CMOP ID: M0532

VA DISPENSE UNIT: TAB                                    MARKABLE FOR CMOP: NOT

MARKED

PACKAGE SIZE: 100

PACKAGE TYPE: BOTTLE

VA CLASS: CN101  OPIOID ANALGESICS

CS FEDERAL SCHEDULE: 2

INGREDIENTS:

NATIONAL FORMULARY INDICATOR: YES

FORMULARY DESIGNATOR: PA-N

NATIONAL FORMULARY RESTRICTION:

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE.

Copay Tier: 3

Copay Effective Date: APR 1, 2016

&lt; Enter "Y" for yes, "N" for no &gt;

&lt; Press RETURN to Pass to Next Drug &gt;

Is this a match ?

#### #### Verify Single Match

**[PSNVER]   Synonym: SVER**

This option allows you to verify a single, selected match rather than looping through all matched, unverified drugs. You will be prompted for the drug name from the local DRUG file (#50).

All matched drugs must be verified. Unverified matches are stored in the NATIONAL DRUG TRANSLATION file (#50.612) and will not merge until they are verified. To ensure accuracy one individual should match the drugs and another verify the matches.

**Example 1: Verify Single Match**

Select National Drug File Menu Option: **SVER** Verify Single Match

Enter name of drug from your local drug file and if the drug has been matched, you will be asked to verify the match.

Press return at the "Select DRUG GENERIC NAME: " prompt to exit.

Select DRUG GENERIC NAME: **MORPHINE SO4** 200MG TAB,SA      CN101         OUTP

ATIENT REQUIRES "WET" SIGNATURE

LOCAL DRUG NAME: MORPHINE SO4 200MG TAB,SA

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 100

DISPENSE UNIT: TAB

VA PRODUCT NAME: MORPHINE SO4 200MG TAB,SA

VA PRINT NAME: MORPHINE SO4 200MG SA TAB             CMOP ID: M0532

VA DISPENSE UNIT: TAB                                MARKABLE FOR CMOP: NOT

MARKED

PACKAGE SIZE: 100

PACKAGE TYPE: BOTTLE

VA CLASS: CN101  OPIOID ANALGESICS

CS FEDERAL SCHEDULE: 2

INGREDIENTS:

NATIONAL FORMULARY INDICATOR: YES

FORMULARY DESIGNATOR: PA-N

NATIONAL FORMULARY RESTRICTION:

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE.

Copay Tier: 3

Copay Effective Date: APR 1, 2016

&lt; Enter "Y" for yes, "N" for no &gt;

&lt; Press RETURN to Pass to Next Drug &gt;

Is this a match ?

examples continue on the next page

Example 2: Verify Single Match, Drug Not Matched

Select DRUG GENERIC NAME: **BLEOMYCIN 15 UNIT INJ**

This entry has not been matched to verify.

Select DRUG GENERIC NAME: **&lt;RET&gt;**

Example 3: Verify Single Match, Drug Already Verified

Select DRUG GENERIC NAME: **FLUOROURACIL 500MG/10ML INJ** AN300

CHEMOTHERAPY

This entry has already been verified.

Select DRUG GENERIC NAME: **&lt;RET&gt;**

**NOTE ON CS FEDERAL SCHEDULE:** Patches PSN*4*64 and 66 assign a CS Federal Schedule to controlled substances and identify controlled substances as narcotic or non-narcotic by populating the CS FEDERAL SCHEDULE field (#19) of the VA PRODUCT FILE (#50.68). Patch PSN*4*65 changes the *Merge National Drug File Data Into Local File* [PSNMRG] option so that the software checks each entry to see if the CS FEDERAL SCHEDULE field contains data. If an entry has a value for the CS FEDERAL SCHEDULE but its corresponding DEA, SPECIAL HDLG field (#3) of the DRUG file (#50) is blank, the DEA, SPECIAL HDLG field will be populated with the corresponding value using the following table:

|                            | If a drug entry has a CS FEDERAL SCHEDULE of:   | And its corresponding DEA, SPECIAL HDLG field is blank, the following DEA, SPECIAL HDLG code will be inserted:   |
|----------------------------|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Schedule I narcotics       | 1                                               | 1                                                                                                                |
| Schedule II narcotics      | 2                                               | 2A                                                                                                               |
| Schedule II non-narcotics  | 2n                                              | 2C                                                                                                               |
| Schedule III narcotics     | 3                                               | 3A                                                                                                               |
| Schedule III non-narcotics | 3n                                              | 3C                                                                                                               |
| Schedule IV narcotics      | 4                                               | 4                                                                                                                |
| Schedule V narcotics       | 5                                               | 5                                                                                                                |

Patch PSN*4*65 ensures that the newly populated CS FEDERAL SCHEDULE field is included as part of the National Drug File details in the *Inquire to National Files* [PSNACT], *NDF Info From Your Local Drug File* [PSNRPT], *Verify Matches* [PSNVFY] and *Verify Single Match* [PSNVER] options.

#### Merge National Drug File Data Into Local File

**[PSNMRG]   Synonym: MERG**

Before proceeding you should contact the IRM site Manager to back up the local DRUG file (#50) and the NATIONAL DRUG TRANSLATION file (#50.612). Back-up should be done each time prior to executing this option.

This option merges the matched/verified data from the NATIONAL DRUG TRANSLATION file (#50.612) into the local DRUG file (#50). As the merge is taking place, the software will print a report listing any drugs in the NATIONAL DRUG TRANSLATION file (#50.612) that were not merged (referred to as errors to the merge). Errors are defined as the entries in the NATIONAL DRUG TRANSLATION file (#50.612) that do not have corresponding matches in the local DRUG file (#50). If no errors exist, the report will say “No Errors Found.”

With patch PSN*4*65, when using this option to merge data from the VA Product file into the local drug file the software will check to see if the

You may execute this option at the conclusion of the entire matching/verifying process or after a section of the local DRUG file (#50) has been matched/verified. It is not important that the entire matching or verifying process be complete since only the matched and verified drugs in the NATIONAL DRUG TRANSLATION file (#50.612) will be merged. There must be at least one matched and verified drug in the NATIONAL DRUG TRANSLATION file (#50.612) for the merge to be completed successfully.

You can determine the time that the report will print. To delay the execution of this option, enter the letter Q at the “Select Printer” prompt and you will be prompted to queue the report to the printer.

Merging the NDF fields into the local DRUG file (#50) will not change the contents of the local GENERIC NAME field (# .01). You may wish to edit this field to make the local name match the NDF name.

**Example: Merge National Drug File Data Into Local File**

Select National Drug File Menu Option: **MERG** Merge National Drug File Data Into Local File

This option will merge NDF fields into your local drug file. This will also

produce an Error Report for entries in the translation file which are not

in the local file if they should exist. These exceptions will not be merged.

You may queue this report if you wish.

Select Printer: *[Select Print Device]*

Do you want your output QUEUED? NO// **&lt;RET&gt;** (NO)

**Automatic Match of Unmatched Drugs**

**[PSNAUTO]   Synonym: AUTO**

This option allows automatic matching by NDC of newer FDA-released drugs in your local file which are manually classed, or have no VA Class assigned. This option proceeds through the local DRUG file (#50) and attempts to match each drug encountered with a drug in the National Drug files. When a match is made, the drug is added to the NATIONAL DRUG TRANSLATION file (#50.612) and must be verified and merged.

Before the automatic matching begins, the prompt below will be displayed on the screen.

AUTOMATIC MATCH by NDC Code process will begin. It will begin. It will attempt to match all items that are not presently MATCHED to the National Drug File.

Are you sure you want to continue?  N//

If you answer YES, the automatic matching process will begin and you will proceed as described below. If you answer NO, or press the Enter key, you will exit from the option.

It is extremely important that as many drugs in the local DRUG file (#50) as possible have correct NDCs assigned to them. If the NDC fields (NDC (#31), SYNONYM (#50.1)) in the local DRUG file (#50) are complete and accurate, the overall effectiveness of the automatic matching process will be greatly improved. If a drug’s NDC in the local DRUG file (#50) matches a like NDC in the National Drug files, a match will be made. These matches must be verified and merged. The VA Class assigned by the matching process will override any class previously assigned. This option will screen an inactive past date.

**Example: Automatic Match of Unmatched Drugs**

Select National Drug File Menu Option: **AUTO** Automatic Match of Unmatched Drugs

This option will attempt to automatically match by NDC code, drugs which have

not been matched to the National Drug File. These matches must be verified

and merged.

AUTOMATIC MATCH by NDC Code process will begin. It will attempt to match

all items that are not presently MATCHED to the National Drug File.

Are you sure you want to continue ?  N// **Y** ......................................

................................................................................

........................................

OK, I'm through. Please verify these matches.

#### Allow Unmatched Drugs to be Classed

**[PSNSTCL]   Synonym: CLAS   Locked:  PSNMGR**

It will be helpful to print the Local Drugs With No VA Drug Class report before executing this option. This option is locked, so only users with the PSNMGR key have access. There will be some drugs in the local DRUG file (#50) that cannot be matched. Examples are investigational drugs, supply items, and drugs that are manufactured on site. You may use this option to enter the local DRUG file and assign VA classifications to these drugs.

<!-- image -->

This option should not be run until at least one merge using the menu option *Merge National Drug File Data Into Local File* has been executed.

There are two sub-options to this option. You will be prompted to answer the question, “Do you wish to automatically loop through all unmatched drugs?” If you answer NO, you may class one drug at a time by entering the local drug generic name or internal number. If you answer YES, the software will loop alphabetically through all drugs that do not have an inactive date and have not been matched, verified, and merged.

If the drug you select was previously classified, the present classification is displayed as a default. You can accept the default by pressing the Enter key, or you can enter a new classification.

Example: Allow Unmatched Drugs to be Classed (Single Drug)

Select National Drug File Menu Option: **CLAS** Allow Unmatched Drugs To Be Classed

This option allows a VA Drug Classification to be entered for

a drug in your local drug file, however, if the drug has been

classed through "the National Drug File merge procedure" you cannot change it!

Do you wish to automatically loop through all unmatched drugs?

&lt;Reply Y,N or "^" to quit&gt;  : **N**

Select DRUG GENERIC NAME: **CALAMINE LOTION**

1   CALAMINE LOTION (OZ)           DE900

2   CALAMINE LOTION, 4OZ BT        DE900   USE FOR INPATIENT WARD STOCK  Tier: 0

CHOOSE 1-2: 1

Select VA DRUG CLASS CODE: DE900 // **&lt;RET&gt;**

Select DRUG GENERIC NAME: **&lt;RET&gt;**

examples continue on the next page

Example: Allow Unmatched Drugs to be Classed (Loop)

Select National Drug File Menu Option: **CLAS** Allow Unmatched Drugs To Be Classed

This option allows a VA Drug Classification to be entered for

a drug in your local drug file, however, if the drug has been

classed through "the National Drug File merge procedure" you cannot change it!

Do you wish to automatically loop through all unmatched drugs?

&lt;Reply Y,N or "^" to quit&gt;  : **Y**

ABSORBABLE GELATIN FILM (EACH)

Select VA DRUG CLASS CODE: XA900 // **&lt;RET&gt;**

ABSORBABLE GELATIN SPONGE ,SZ 100,6/BX

Select VA DRUG CLASS CODE: XA900 // **&lt;RET&gt;**

ABSORBABLE GELATIN SPONGE,SZ 12X7,12/BX

Select VA DRUG CLASS CODE: XA900 // **&lt;RET&gt;**

ACCUTANE 20MG

Select VA DRUG CLASS CODE: **DE751**

ACE BANDAGE,3 IN,ELASTIC

Select VA DRUG CLASS CODE: XA100 // **&lt;RET&gt;**

ACE BANDAGE,4 IN,ELASTIC

Select VA DRUG CLASS CODE: XA100 // **&lt;RET&gt;**

ACE BANDAGE,6 IN,ELASTIC

Select VA DRUG CLASS CODE: XA100 // **&lt;RET&gt;**

ACEBUTOLOL 200MG CAP

Select VA DRUG CLASS CODE: CV100 // **^**

You can stop the looping process at any time by entering an up-arrow (^) and pressing the Enter key at the “Select VA DRUG CLASS CODE” prompt. The software will flag the last drug you classified and will begin the loop with this drug when you resume the looping process. This will allow you to review the last drug classified before continuing.

**Note:** If a drug has **no default classification** and you press the Enter key rather than enter a class, the software will return you to the main menu.

Example: Loop Interrupted When No Default Class and No Value Entered

Select National Drug File Menu Option: **CLAS** Allow Unmatched Drugs To Be Classed

This option allows a VA Drug Classification to be entered for

a drug in your local drug file, however, if the drug has been

classed through "the National Drug File merge procedure" you cannot change it!

Do you wish to automatically loop through all unmatched drugs?

&lt;Reply Y,N or "^" to quit&gt;  : **Y**

ABSORBABLE GELATIN FILM (EACH)

Select VA DRUG CLASS CODE: XA900 // **&lt;RET&gt;**

ABSORBABLE GELATIN SPONGE ,SZ 100,6/BX

Select VA DRUG CLASS CODE: XA900 // **&lt;RET&gt;**

ABSORBABLE GELATIN SPONGE,SZ 12X7,12/BX

Select VA DRUG CLASS CODE: XA900 // **&lt;RET&gt;**

ACCUTANE 20MG

Select VA DRUG CLASS CODE: **&lt;RET&gt;**

Select National Drug File Menu Option: **&lt;RET&gt;**

**Note:** The software will not allow you to reassign the VA Classification to a drug that has already been matched, verified, and merged.

Example: Attempt to Class Item already Matched, Classed, and Merged

Select DRUG GENERIC NAME: **SODIUM METHOHEXITAL 5GM S.P.** CN202        N/F

SORRY, CLASSIFICATION CANNOT BE CHANGED

Select DRUG GENERIC NAME: **&lt;RET&gt;**

After this option has been completed, print and review *Local Drug With No VA Class Report* .

<!-- image -->

To change the VA Drug Classification of a drug previously matched automatically by NDC, first attempt to rematch the drug using the *Rematch/Match Single Drugs* option. If that fails, classify the drug manually using this option.

## Using the National Drug File Reports Menu

### National Drug File Reports Menu

**[PSNSUBM]   Synonym: RPRT**

This option is a sub-menu containing the following reports:

*LDF	Local Drug File Report*

*VAGN	Report of VA Generic Names From National Drug*

*ATMP	Report of Attempted Match Drugs*

*PROD	VA Product Names Matched Report*

*NOCL	Local Drug with No VA Drug Class Report*

*CLVA	VA Drug Classification*

*DFL	NDF Info From Your Local Drug File*

*SUPL	Supply (XA000) VA Class Report*

*MANC	Manually Classed Drugs Report*

*NMAT	Local Drugs With NO Match to NDF Report*

*LOCF	Local Formulary Report*

*NATF	National Formulary Report*

*DDIN	Drug-Drug Interaction Report*

*CMOP	VA Products Marked for CMOP Transmission*

*PNCL	VA Product Names By Class*

*LDPN	Local Drug/VA Print Name Report*

*LDRG		Local Drugs Excluded from Drug-Drug Interactions*

*VDRG	VA Products Excluded from Drug-Drug Interactions*

### Local Drug File Report

**[PSNLDG]   Synonym: LDF**

This option generates a report containing selected information about drugs in the local DRUG file (#50). This report lists the local drug name, inactive date, NDC number, and the Drug Enforcement Agency (DEA) value. If your local drug is matched to NDF, and National Formulary and/or Restriction information exists, this is also displayed after the drug name. This report is in a 132 column format and must be sent to a printer.

**Example: Local Drug File Report**

Select National Drug File Reports Menu Option: **LDF** Local Drug File Report This report gives you a printed copy of the local drug name, inactive date, NDC, and the DEA value. If your local drug is matched to NDF and National Formulary and/or Restriction information exists, this is also displayed after the drug name. This report requires 132 columns. You may queue the report to print, if you wish.

START WITH GENERIC NAME: FIRST//

DEVICE: 0;500;132  DECSERVER

LOCAL DRUG LIST (ALPHABETIC)

# Not on National Formulary

R   National Formulary Restriction

| LOCAL DRUG NAME                   | INACTIVE DATE   | DEA   | NDC            |
|-----------------------------------|-----------------|-------|----------------|
| 10% FREE AMINE SOLUTION W/O EL    |                 |       |                |
| A AND Z OINTMENT                  |                 |       | 85-0096-04     |
| A-METHYL-PARA-TYROSINE CAPS,25    |                 | I     |                |
| ABDOMINAL BINDER                  |                 | S     |                |
| ABDOMINAL PAD 7 1/2 X 8  STERI    |                 | S     |                |
| ABSORBABLE GELATIN FILM  #        |                 | 6P    | 9-0433-01      |
| ABSORBABLE GELATIN SPONGE SZ.     |                 |       | 9-0031-01      |
| ABSORBABLE GELATIN SPONGE SZ.     |                 | S     | 9--0349-01     |
| ABSORBABLE GELATIN SPONGE SZ.7  # |                 | S     | 9-0315-02      |
| ABSORBABLE GELATIN SPONGE-100  #  |                 | S     | 9-0353-01      |
| ACE BANDAGE 4 INCH                |                 | S     | 8290-0073-13   |
| ACETAMINOPHEN 1000MG TABLET       |                 |       |                |
| ACETAMINOPHEN 325MG C.T.          |                 | 6P    | 333333-3333-33 |
| ACETAMINOPHEN 325MG TABLET        |                 |       | 839-5080-16    |
| ACETAMINOPHEN 650MG SUPPOS.       |                 | 9PR   | 839-6001-92    |
| ACETAMINOPHEN AND CODEINE 30MG  R |                 | 3     | 0045-0513-80   |
| ACETAMINOPHEN ELIX. 160MG/5ML     |                 | 6     | 54-3010-50     |
| ACETAMINOPHEN, CODEINE ELIXIR  R  |                 | 2A    | 51079-0500-38  |
| ACETAMINPHEN 325MG CT             |                 |       | 839-5080-16    |
| ACETAZOLAMIDE 250MG S.T.          |                 | 6P    | 364-0400-02    |
| ACETAZOLAMIDE 500MG INJ           |                 | 6P    | 205-4466-96    |
| ACETAZOLAMIDE 500MG SEQUELS       |                 | 6P    | 5-4465-23      |
| ACETEST 100'S  #                  |                 | S     | 193-2381-21    |
| ACETIC ACID 0.25% IRRIG. 500ML    |                 | S     | 0074-6143-09   |
| ACETIC ACID 2% OTIC SOL 15 ML     |                 | 9P    | 536-2102-72    |

### Report of VA Generic Names from National Drug

**[PSNVAGN]   Synonym: VAGN**

This option prints a report of VA Generic Names. You can print all or a specified range of names. This report might be useful during the match and verify options. If you cannot find a match and are asked to type in a VA Generic Name, you can use this list to find the correct generic name. VA Generic Names with more than one ingredient are given alphabetically by ingredient (e.g., acetaminophen/butalbital/caffeine/codeine).

This report requires 80 columns. You can print the report immediately, or delay printing until a later time.

**Example: Report of VA Generic Names From National Drug**

Select National Drug File Reports Menu Option: **VAGN** Report of VA Generic Names From National Drug

This report gives you a printed copy of the VA Generic Names from the National Drug File. This report may assist you in the matching process.

You may queue the report to print, if you wish.

START WITH VA GENERIC NAME: FIRST// **&lt;RET&gt;**

DEVICE: *[Select Print Device]*

VA GENERIC NAMES FROM THE NATIONAL DRUG FILE

OCT 11,1998  14:46    PAGE 1

VA GENERIC NAME

--------------------------------------------------

ACEBUTOLOL

ACETAMINOPHEN

ACETAMINOPHEN/ALUMINUM ACETATE/CHLORPHENIRAMINE/PHENYLPROPANOLAM

ACETAMINOPHEN/ALUMINUM HYDROXIDE/ASPIRIN/SALICYLAMIDE

ACETAMINOPHEN/ASPIRIN

ACETAMINOPHEN/ASPIRIN/CAFFEINE/CODEINE/SALICYLAMIDE

ACETAMINOPHEN/ASPIRIN/CAFFEINE/HYDROCODONE

ACETAMINOPHEN/ASPIRIN/CAFFEINE/SALICYLAMIDE

ACETAMINOPHEN/ASPIRIN/CODEINE

ACETAMINOPHEN/ATROPINE/ETHAVERINE/SALICYLAMIDE

ACETAMINOPHEN/BUTALBITAL

ACETAMINOPHEN/BUTALBITAL/CAFFEINE

ACETAMINOPHEN/BUTALBITAL/CAFFEINE/CODEINE

ACETAMINOPHEN/BUTALBITAL/CAFFEINE/HYDROCODONE

ACETAMINOPHEN/BUTALBITAL/CODEINE

ACETAMINOPHEN/CAFFEINE/CHLORPHENIRAMINE/HYDROCODONE/PHENYLEPHRIN

### Report of Attempted Match Drugs

**[PSNEXC]   Synonym: ATMP**

This option generates a report listing all drugs you attempted to match, but for which a match could not be made during the matching process. Even though these drugs were not matched, the software “flagged” each of these drugs and an entry was made in the NATIONAL DRUG TRANSLATION file (#50.612).

This report will include the contents of the DEA, SPECIAL HDLG field (# 3) if the field contains one of the following values:

0 (zero)	Manufactured in Pharmacy

I	Investigational Drug

M	Bulk Compound Item

The report will also include any ***inactive*** dates found in the local DRUG file (#50).

This report should be printed after the option *Verify Matche* s is executed

and before the *Merge National Drug File Data Into Local File* option is

executed. This is a cumulative report and will include all entries from the

very beginning of the matching process until each drug is manually classed. Once a drug has been manually classed, it is automatically deleted from the report.

You may print the report immediately, or delay printing until a later time.

**Example: Report of Attempted Match Drugs**

Select National Drug File Reports Menu Option: **ATMP** Report of Attempted Match Drugs

This report should be run after the menu option "Verify Matches" and

before the menu option "Merge National Drug File Data Into Local File".

It gives you a hard copy of the items from your local file for which

a match was attempted, but no match was made from the National Drug File.

You may queue the report to queue if you wish.

Select Printer: *[Select Print Device]*

REPORT OF ATTEMPTED MATCH DRUGS

Date printed: OCT 13,1998

Page: 1

LOCAL DRUG NAME                           INACTIVE               DEA

--------------------------------------------------------------------------------

AZATHIOPRINE 50MG ***** N/F TAB

HALOPERIDOL  0.5MG U/D TAB                1-15-98

CYCLOPHOSPHAMIDE  200MG INJ

PHENYTOIN SUSP 150MG/6ML U/D                                     0

OXIDIZED CELLULOSE PADS                                          S

IV INJECTION SET NO.2C0012                                       S

CODEINE PHOS. 15MG C.T.

ANTILYMPHOCYTE GLOBULIN STUDY DRUG                               I

BEPRIDIL STUDY CAPSULES, 100MG.                                  I

### VA Product Names Matched Report

**[PSNPFN]   Synonym: PROD**

This option generates a report listing all drugs that have been matched. The report is not cumulative and will not include entries that have been previously merged into the local DRUG file (#50). The VA Product Names matched report can be printed before and/or after the menu option Verify Matches. It should be printed and reviewed before the *Merge National Drug File Data Into Local File* option is executed. This report may also be printed after the auto-match process to review what was matched. It generates a hard copy of the matches selected in the menu option *Automatic Match of Unmatched Drugs* and the option *Verify Matches.*

The data for this report is stored in the NATIONAL DRUG TRANSLATION file (#50.612). If a matched entry has not been verified, it will appear on the report with a special notation NOT VERIFIED. (Refer to the first entries on the following sample report.) User names will only print on the report when those names change; the user who began the automatic match by NDC process will have his or her name printed on the report for those matches.

After reviewing this report, incorrect matches may be rematched by using the menu option *Rematch/Match Single Drugs* .

This report requires 132 columns. You may print the report immediately, or delay printing until a later time.

**Example: VA Product Names Matched Report**

Select National Drug File Reports Menu Option: **PROD** VA Product Names Matched Report

This report can be run before and/or after the menu option "Verify Matches".

It should be run before the menu option "Merge National Drug File Data Into

Local File". This report may also be run after the auto-match process to review

what was matched. It generates a hard copy of the matches selected in the menu

option "Automatic Match of Unmatched Drugs" and the menu option "Verify

Matches". This report requires 132 columns.

You may queue the report to print, if you wish.

Select Printer: *[Select Print Device]*

report follows on the next page

**Example: VA Product Names Matched Report (cont.)**

DRUG NAME FROM LOCAL DRUG FILE WITH MATCH FROM NATIONAL DRUG FILE

Date printed: OCT 2,1998

Page: 1

LOCAL DRUG NAME                                   VA PRODUCT NAME

-------------------------------------------------------------------------------------------------

CHLORAMBUCIL 2MG S.C.T.                           CHLORAMBUCIL 2MG TAB

ORDER UNIT:                                       PKG SIZE: 50

DISPENSE UNITS/ORDER UNITS: 1                     PKG TYPE: BOTTLE

DISPENSE UNIT:                                    VA CLASS: AN100  ANTINEOPLASTICS,ALKYLATING AGENTS

** NOT VERIFIED **

CYTARABINE 500MG COMB.PK                          CYTARABINE 500MG/VIL INJ

ORDER UNIT:                                       PKG SIZE: 10 ML

DISPENSE UNITS/ORDER UNITS: 1                     PKG TYPE: VIAL

DISPENSE UNIT:                                    VA CLASS: AN300  ANTINEOPLASTICS,ANTIMETABOLITES

** NOT VERIFIED **

DACARBAZINE 200MG INJ                             DACARBAZINE 200MG/VIL INJ

ORDER UNIT:                                       PKG SIZE: 12 X 200 MG

DISPENSE UNITS/ORDER UNITS: 1                     PKG TYPE: VIAL

DISPENSE UNIT:                                    VA CLASS: AN900  ANTINEOPLASTIC,OTHER

** NOT VERIFIED **

DACTINOMYCIN 0.5MG INJ                            DACTINOMYCIN 0.5MG/VIL INJ

ORDER UNIT:                                       PKG SIZE: 3 ML

DISPENSE UNITS/ORDER UNITS: 1                     PKG TYPE: VIAL

DISPENSE UNIT:                                    VA CLASS: AN200  ANTINEOPLASTIC ANTIBIOTICS

** NOT VERIFIED **

FLUOROURACIL 500MG/10ML INJ                       FLUOROURACIL 50MG/ML INJ

ORDER UNIT:                                       PKG SIZE: 10 X 10 ML

DISPENSE UNITS/ORDER UNITS:                       PKG TYPE: AMP

DISPENSE UNIT:                                    VA CLASS: AN300  ANTINEOPLASTICS,ANTIMETABOLITES

** NOT VERIFIED **

MORPHINE SULF 4MG/ML INJ TUBEX                    FLUOROURACIL 1% CREAM,TOP

ORDER UNIT: PG                                    PKG SIZE: 30 GM

DISPENSE UNITS/ORDER UNITS: 10                    PKG TYPE: TUBE

DISPENSE UNIT: TUBEX                              VA CLASS: DE600  ANTINEOPLASTIC,TOPICAL

** NOT VERIFIED **

FLUOROURACIL 2% TOP.SOL.                          FLUOROURACIL 5% CREAM,TOP

ORDER UNIT: PG                                    PKG SIZE: 25 GM

DISPENSE UNITS/ORDER UNITS: 1                     PKG TYPE: TUBE

DISPENSE UNIT:                                    VA CLASS: DE600  ANTINEOPLASTIC,TOPICAL

** NOT VERIFIED **

ZZDICHLORPHENAMIDE 50MG TAB                       LOMUSTINE DOSEPAK (300MG TOTAL) CAP

ORDER UNIT: BT                                    PKG SIZE: 2 X 100 MG/2 X 40 MG/2 X 10 MG

DISPENSE UNITS/ORDER UNITS: 100                   PKG TYPE: PACKAGE

DISPENSE UNIT: TAB                                VA CLASS: AN100  ANTINEOPLASTICS,ALKYLATING AGENTS

** NOT VERIFIED **

MECHLORETHAMINE 10MG INJ                          MECHLORETHAMINE HCL 10MG/VIL INJ

ORDER UNIT: BT                                    PKG SIZE: 4 X 20 ML

DISPENSE UNITS/ORDER UNITS: 1                     PKG TYPE: VIAL

DISPENSE UNIT:                                    VA CLASS: AN100  ANTINEOPLASTICS,ALKYLATING AGENTS

** NOT VERIFIED **

### Local Drugs with No VA Drug Class Report

**[PSNOCLS]   Synonym: NOCL**

This option generates a report of drugs from the local DRUG file (#50) which have no VA drug classification. It will print only the active drugs in the file. This report should be generated after using the *Merge National Drug File Data Into Local File* option. You may wish to print this report ***before*** and ***after*** executing the *Allow Unmatched Drugs To Be Classed* option.

This report will display the contents of the DEA, SPECIAL HDLG field (#3) if the field contains one of the following values:

0 (zero)	Manufactured in Pharmacy

I	Investigational Drug

M	Bulk Compound Item

You can print the report immediately, or delay printing until a later time.

**Example: Local Drugs with No VA Drug Class Report**

Select National Drug File Reports Menu Option: **NOCL** Local Drugs With No VA Drug Class Report

This report should be run after executing the menu option "Merge National Drug

File Data Into Local File". It may be useful to print this report before and

after executing the "Allow Unmatched Drugs To Be Classed" option. It gives you

a hard copy of the drugs from your local drug file which are "active" and have

no VA Drug Classification.

You may queue the report to print, if you wish.

Select Printer: *[Select Print Device]*

LOCAL DRUGS WITH NO VA CLASSIFICATION

Date printed: OCT 2,1998                               Page: 1

NUMBER    LOCAL DRUG GENERIC NAME                                  DEA

--------------------------------------------------------------------------------

3         BLEOMYCIN 15 UNIT INJ

4         PEN

5         CHLORAMBUCIL 2MG S.C.T.

6         CYCLOPHOSPHAMIDE 50MG C.T.

7         CYCLOPHOSPHAMIDE 200MG INJ

8         CYCLOPHOSPHAMIDE 500MG INJ

report continues on the next page

**Example: Local Drugs with No VA Drug Class Report (cont.)**

10        CYTARABINE 500MG COMB.PK

12        DACARBAZINE 200MG INJ

13        DACTINOMYCIN 0.5MG INJ

14        DOXORUBICIN 10MG S.P.

15        DOXORUBICIN 50MG S.P.

16        FLUOROURACIL 500MG/10ML INJ

18        FLUOROURACIL 2% TOP.SOL.

20        HYDROXYUREA 500MG CAP

22        MECHLORETHAMINE 10MG INJ

24        MELPHALAN 2MG S.T.

26        METHOTREXATE 2.5MG C.T.

27        METHOTREXATE 25MG/ML S.S.

29        MITHRAMYCIN 2.5MG L.P.

30        MITOMYCIN 5MG INJ

32        PROCARBAZINE 50MG CAP

*[This report has been abbreviated to save space.]*

### VA Drug Classification

**[PSNCLS]   Synonym: CLVA**

This option generates a report of all VA Drug Classification codes and classes. You are given the option of having the classification descriptions printed in the report. You can choose to print all of the drug classifications or a range of classifications. In the following example, the “START WITH” and “GO TO” prompts refer to an alphabetical range in the classification code.

You may print the report immediately, or delay printing until a later time.

**Example: VA Drug Classification Report**

Select National Drug File Reports Menu Option: CLVA  VA Drug Classification

This report will display the VA Drug Classification code and class name.

Would you also like to see the class descriptions? N// **Y**

START WITH CODE: FIRST// **A**

GO TO CODE: LAST// **C**

DEVICE: *[Select Print Device]*

VA DRUG CLASSIFICATION CODES

OCT 15,1998  09:25    PAGE 1

--------------------------------------------------------------------------------

AD000         ANTIDOTES,DETERRENTS AND POISON CONTROL

> **NOTE:** Includes nicotine polacrilex and other deterrents (AD900).

Excludes anticoagulant antagonists (BL200,VT700);

antifolate antagonists (VT102); antivenins (IM300);

dialysis solutions (IR200); emetics (GA600); opioid

antagonists (CN102).

AD100       ALCOHOL DETERRENTS

AD200       CYANIDE ANTIDOTES

AD300       HEAVY METAL ANTAGONISTS

AD400       ANTIDOTES,DETERRENTS,AND POISON CONTROL EXCHANGE RESINS

AD900       ANTIDOTES/DETERRENTS,OTHER

AH000         ANTIHISTAMINES

> **NOTE:** Excludes H2-antagonists (GA301); combination cold

products (RE500).

AH100       ANTIHISTAMINES,PHENOTHIAZINE

AH200       ANTIHISTAMINES,ETHANOLAMINE

AH300       ANTIHISTAMINES,ETHYLENEDIAMINE

AH400       ANTIHISTAMINES,ALKYLAMINE

*[This report has been abbreviated to save space.]*

### NDF Info From Your Local Drug File

**[PSNRPT]   Synonym: DFL**

This option generates a report containing information for a given range of drugs or for all drugs that have been merged. This option should be executed after the *Merge National Drug File Data Into Local File* option has been completed. The report contains data that is stored in the NDF fields of the local DRUG file (#50). Any drugs that do not contain NDF information (i.e., the drug has not been matched, verified, and merged) will be ignored. In the following example, the “START WITH” and “GO TO” prompts refer to an alphabetical range in the GENERIC NAME field (# .01).

To print a list of drugs by VA Drug Classification, you can use the *Formulary Report* option.

You can print the report immediately, or delay printing until a later time.

**Example: NDF Info from Local Drug File**

Select National Drug File Reports Menu Option: **DFL** NDF Info From Your Local Drug File

This report gives a printed copy of the drugs from your local drug file that

have been matched to the National Drug File. This report requires 132 columns.

You may queue the report to print, if you wish.

START WITH GENERIC NAME: FIRST// **&lt;ENTER&gt;**

DEVICE: *[Select Print Device]*

NATIONAL DRUG INFO FROM YOUR LOCAL FILE

Date printed: OCT 2,1998

Page: 1

LOCAL DRUG INFO                           NDF INFO                           NDF         NDF

LOCAL DRUG NAME                           VA PRODUCT NAME                    PKG SIZE    PKG TYPE

-------------------------------------------------------------------------------------------------

ACETAMINOPHEN 160MG/5ML ELIXIR

ATROPINE SO4 0.8MG/ML INJ

30 ML

BOTTLE

ORDER UNIT: PT                            VA CLASS: CN103    NON-OPIOID ANALGESICS

CS FEDERAL SCHEDULE:

DISPENSE UNITS/ORDER UNITS: 16

DISPENSE UNIT: OZ                         INGREDIENTS:

ATROPINE SULFATE  0.8 MG/ML

ACETAMINOPHEN 650MG RECT SUPP

ACETAMINOPHEN 600MG SUPP,RTL

12

PACKAGE

ORDER UNIT: BX                            VA CLASS: CN103    NON-OPIOID ANALGESICS

CS FEDERAL SCHEDULE:

DISPENSE UNITS/ORDER UNITS: 1

DISPENSE UNIT: BX(12s)                    INGREDIENTS:

ATROPINE SULFATE  0.4 MG/ML

report continues on the next page

**Example: NDF Info from Local Drug File (cont.)**

ACETAMINOPHEN 650MG RECT SUPP

ACETAMINOPHEN 600MG SUPP,RTL

12

PACKAGE

ORDER UNIT: BX                            VA CLASS: CN103    NON-OPIOID ANALGESICS

CS FEDERAL SCHEDULE:

DISPENSE UNITS/ORDER UNITS: 1

DISPENSE UNIT: BX(12s)                    INGREDIENTS:

ATROPINE SULFATE  0.4 MG/ML

ACETAMINOPHEN W/CODEINE 12.5MG

CODEINE 12MG/ACETAMINOPHEN 120MG/5ML ELIXIR

480 ML

BOTTLE

ORDER UNIT: PT                            VA CLASS: CN101    OPIOID ANALGESICS

CS FEDERAL SCHEDULE:

DISPENSE UNITS/ORDER UNITS: 128

DISPENSE UNIT: OZ                         INGREDIENTS:

ATROPINE SULFATE  0.5 %

ACETAMINOPHEN W/CODEINE 15MG T

CODEINE 15MG/ACETAMINOPHEN 300MG TAB

100

BOTTLE

ORDER UNIT: BT                            VA CLASS: CN101    OPIOID ANALGESICS

CS FEDERAL SCHEDULE:

DISPENSE UNITS/ORDER UNITS: 100

DISPENSE UNIT: TAB                        INGREDIENTS:

ATROPINE SULFATE  1 %

TOLMETIN 400MG DS CAP

TOLMETIN NA 400MG CAP

100

BOTTLE

ORDER UNIT: BT                            VA CLASS: MS102    NONSALICYLATE NSAIs

CS FEDERAL SCHEDULE:

,ANTIRHEUMATIC

DISPENSE UNITS/ORDER UNITS: 100

DISPENSE UNIT: CAP                        INGREDIENTS:

ATROPINE SULFATE  0.4 MG/ML

ACETAMINOPHEN W/CODEINE 30MG T

CODEINE 30MG/ACETAMINOPHEN 300MG TAB

100

BOTTLE

ORDER UNIT: BT                            VA CLASS: CN101    OPIOID ANALGESICS

CS FEDERAL SCHEDULE: 3

DISPENSE UNITS/ORDER UNITS: 100

DISPENSE UNIT: TAB                        INGREDIENTS:

ATROPINE SULFATE  0.4 MG/ML

ACETAMINOPHEN W/CODEINE 30MG T

CODEINE 30MG/ACETAMINOPHEN 300MG TAB

20 X 25

UNIT DOSE

ORDER UNIT: BX                            VA CLASS: CN101    OPIOID ANALGESICS

CS FEDERAL SCHEDULE:

DISPENSE UNITS/ORDER UNITS: 500

DISPENSE UNIT: TAB                        INGREDIENTS:

ATROPINE SULFATE  0.4 MG/ML

*[This report has been abbreviated to save space.]*

### Supply (XA000) VA Class Report

**[PSNSUPLY]   Synonym: SUPL**

This option generates a report of all the items from the local DRUG file (#50) which have an “XA” VA Drug Classification. It will print only the active items in the file, and will sort by local DRUG file (#50) generic name.

You may print the report immediately, or delay printing until a later time.

**Example: Supply (XA000) VA Class Report**

Select National Drug File Reports Menu Option: **SUPL** Supply (XA000) VA Class Report

This report should be run if you have already classed your local drugs/items

using Version 1.0 of NDF. After the installation of Version 2.0 of NDF and the

VA DRUG CLASS file is re-installed, you may wish to re-class your local items

with an "XA" classification using the newly expanded "XA000" classification. It

gives you a hard copy of the items from your local drug file which are "active"

and have an "XA" VA Drug Classification.

You may queue the report to print, if you wish.

Select Printer: *[Select Print Device]*

LOCAL ITEMS WITH A "PROSTHETICS/SUPPLIES/DEVICES" VA CLASSIFICATION

Date printed: OCT 15,1998                              Page: 1

NUMBER    LOCAL DRUG GENERIC NAME                        VA CLASS     NEW CLASS

--------------------------------------------------------------------------------

10515     ABDOMINAL BINDER SIZE 24-50IN                  XA900        \_\_\_\_\_\_\_

10516     ABDOMINAL BINDER SIZE 48-64IN                  XA900        \_\_\_\_\_\_\_

10638     ADHES DISC OSTOMY RELIASEAL #121200 1IN        XA900        \_\_\_\_\_\_\_

8664      ADHESIVE CEMENT 120ML (SKIN BOND) U#4000       XA900        \_\_\_\_\_\_\_

9869      ADHESIVE FORMULA 120ML #0024 (ATLANTIC)        XA900        \_\_\_\_\_\_\_

10543     ADHESIVE GASKET SEAL-TITE U#2687 1&amp;1/4IN       XA900        \_\_\_\_\_\_\_

10177     ADHESIVE GASKET SEAL-TITE U#2687 1&amp;1/8IN       XA900        \_\_\_\_\_\_\_

12239     ADHESIVE GASKET SEAL-TITE U#2687 1/2IN         XA900        \_\_\_\_\_\_\_

10175     ADHESIVE GASKET SEAL-TITE U#2687 1IN           XA900        \_\_\_\_\_\_\_

10178     ADHESIVE GASKET SEAL-TITE U#2687 5/8IN         XA900        \_\_\_\_\_\_\_

*[This report has been abbreviated to save space.]*

### Manually Classed Drugs Report

**[PSNMCLS] Synonym: MANC**

This option generates a report, listing all active drugs in the local DRUG file (#50) that have been manually assigned a VA Drug Classification. The report will sort alphabetically by local drug generic name and will exclude supply items which have been assigned an “XA” classification.

You may print the report immediately, or delay printing until a later time.

**Example: Manually Classed Drugs Report**

Select National Drug File Reports Menu Option: MANC  Manually Classed Drugs Report

This report will give you an alphabetic listing, by local generic name, of the

drugs from your local drug file which are "active" and have been assigned a

manual VA Drug Classification through the option "Allow Unmatched Drugs To Be

Classed". This report will exclude your supply items that have been assigned

an "XA" class.

You may queue the report to print, if you wish.

Select Printer: *[Select Print Device]*

MANUALLY CLASSED DRUGS REPORT

Date printed: OCT 2,1998                               Page: 1

NUMBER    LOCAL DRUG GENERIC NAME                              VA DRUG CLASS

--------------------------------------------------------------------------------

12354     A NEW STICKY DRUG FOR TESTING BRAIN POWE             CN103

10790     ACEBUTOLOL HCL 200MG CAP                             CV100

10455     ACEBUTOLOL HCL 400MG CAP                             CV100

263       SACCHARIN SODIUM 30MG SOL TAB 500/BT                 PH000

292       ACETAMINOPHEN 325MG TAB                              CN103

294       ACETAMINOPHEN 325MG TAB                              CN103

11369     ACETAMINOPHEN 325MG TAB U/D                          CN103

10372     ACETAMINOPHEN 325MG/10.15ML ELIXIR U/D               CN103

5826      ACETAMINOPHEN 500MG CAP                              CN103

11531     ACETAMINOPHEN 500MG CAPLET                           CN103

10373     ACETAMINOPHEN 650MG/20.3ML ELIXIR U/D                CN103

604       ACETAMINOPHEN W/CODEINE 30MG TAB                     CN101

*[This report has been abbreviated to save space.]*

### Local Drugs with No Match to NDF Report

**[PSNONDF] Synonym: NMAT**

This option generates a report that contains entries in your local DRUG file (#50) with no match to the National Drug files. You can print all drugs or only those marked for Outpatient Pharmacy use.

**Example: Local Drugs with No Match to NDF Report**

Select National Drug File Reports Menu Option: **NMAT** Local Drugs With NO Match to NDF Report

This report should be run after executing the menu option "Merge National Drug

File Data Into Local File". It gives you a hard copy of the drugs from your

local DRUG file which are "active" and have no match to NDF. You have the choice

to print ALL drugs or only drugs marked for Outpatient use. If you answer "yes" to the question, you will print all. If you answer "

no", you will print only

Outpatient use drugs.

You may queue the report to print, if you wish.

Do you wish to print ALL drugs from your local file?

Enter Yes or No: **YES**

Select Printer: *[Select Print Device]*

LOCAL DRUGS WITH NO MATCH TO NDF

Date printed: OCT 2,1998                               Page: 1

DEA,

MANUAL  SPCL   INACTIVE

NUMBER LOCAL DRUG GENERIC NAME                       CLASS   HDLG   DATE

--------------------------------------------------------------------------------

1196   A AND D OINTMENT

12354  A NEW STICKY DRUG FOR TESTING BRAIN POWE      CN103   9L

6284   A-200 PYRINATE GEL                                    9

12287  A-AIR

12310  A-ALBUTEROL

12302  A-ALFENTANIL

12251  A-AMINOPHYLLINE

12306  A-ATRACURIUM

12269  A-ATROPINE SULFATE

12290  A-BEZOCAINE 14%/TETRACAINE 2% SPRAY

*[This report has been abbreviated to save space.]*

### Local Formulary Report

**[PSNFRMLY] Synonym: LOCF  Locked:  PSNMGR**

This option is locked with the PSNMGR key, so only user with the PSNMGR key can access it. This report gives you a printed copy of formulary drugs from your local file with synonyms not marked as quick codes. You are asked first whether or not to include supply items. Next you are asked to type in a title for this report. You can print by Generic Name/Tradename (see Example 1) or VA Class Code (see Example 2). If you choose to print by VA Class code, the software will ask you to pick a range of VA Drug Class Codes. Only active drugs will print.

<!-- image -->

This report should only be run ***after*** executing the NDF software.

You may print the report immediately, or delay printing until a later time.

**Example 1: Formulary Report sorted by Generic/Tradename**

Select National Drug File Reports Menu Option: **LOCF** Local Formulary Report

This report gives you a printed copy of formulary drugs from your local file

with synonyms marked as trade names. You will be asked if you want to include

supply items. You are asked to type in a title for this report.

You are then asked to print by Generic Name/Trade name or VA Class Code.

If you choose to print by VA Class Code, it will ask you to pick a range

of VA Drug Class Codes. Only active drugs will print. Drugs with

a future inactive date will print as well.

You may queue the report to print, if you wish.

Do you wish to include supply items? NO// **&lt;RET&gt;**

Enter title for report: HOSPITAL// **&lt;RET&gt;**

You may print by DRUG GENERIC NAME/TRADENAME or VA CLASS CODE.

Enter a &lt;RET&gt; or "G" to print by DRUG GENERIC NAME/TRADENAME or

"C" for VA CLASS CODE.

Print by:

DRUG GENERIC NAME/TRADENAME// **G** GENERIC/TRADE

report follows on the next page

**Example 1: Formulary Report sorted by Generic/Tradename (cont.)**

HOSPITAL FORMULARY                                     Date printed: SEP 21,1998

Page: 1

GENERIC/TRADE NAME

GENERIC/TRADE NAME                         CLASS        PRICE / DISP UNT

-------------------------------------------------------------------------------

A &amp; D OINT. 5GM PK.

DE350        0.04 / PK

ACETA 325MG TABS

ACETAMINOPHEN 325MG TAB UD                 CN103        0.01 / TAB

ACETA-GESIC

ACETAMINOPHEN 325MG TAB UD                 CN103        0.01 / TAB

ACETAMIN W/CODEINE 30MG(TYLENOL#3)TAB UD

CN101        0.05 / BX

ACETAMIN W/CODEINE 30MG/12.5ML LIQ UD

CN101        0.22 / CUP

ACETAMIN W/OXYCODONE 5MG(PERCOCET)TAB UD

CN101        0.00 / TAB

ACETAMINOPHEN &amp; OXYCODONE 5MG UD CAP

CN101        0.05 / CAP

ACETAMINOPHEN 325MG C.T.

CN103        0.01 / TAB

ACETAMINOPHEN 325MG TAB UD

ACETA 325MG TABS                           CN103        0.01 / TAB

ACETA-GESIC                                CN103        0.01 / TAB

ACETAMINOPHEN 325MG TABLETS                CN103        0.01 / TAB

ALPRA 325                                  CN103        0.01 / TAB

*[This report has been abbreviated to save space.]*

**Example 2: Formulary Report sorted by VA Drug Class Code**

Select National Drug File Reports Menu Option: **LOCF** Local Formulary Report

This report gives you a printed copy of formulary drugs from your local file

with synonyms marked as trade names. You will be asked if you want to include

supply items. You are asked to type in a title for this report.

You are then asked to print by Generic Name/Trade name or VA Class Code.

If you choose to print by VA Class Code, it will ask you to pick a range

of VA Drug Class Codes. Only active drugs will print. Drugs with

a future inactive date will print as well.

You may queue the report to print, if you wish.

Do you wish to include supply items? NO// **&lt;RET&gt;**

Enter title for report: HOSPITAL// **HOSPITAL FORMULARY**

You may print by DRUG GENERIC NAME/TRADENAME or VA CLASS CODE.

Enter a &lt;RET&gt; or "G" to print by DRUG GENERIC NAME/TRADENAME or

"C" for VA CLASS CODE.

Print by:

DRUG GENERIC NAME/TRADENAME// **C** CLASS

START WITH VA CLASSIFICATION: FIRST// **&lt;RET&gt;**

report follows on the next page

**Example 2: Formulary Report sorted by VA Drug Class Code (cont.)**

HOSPITAL FORMULARY FORMULARY  (BY VA DRUG CLASS)       Date printed: SEP 21,1998

Page: 1

VA DRUG CLASS

PRICE /

GENERIC NAME                               DISP UNT    TRADE NAME(S)

--------------------------------------------------------------------------------

AD100  ALCOHOL DETERRENTS

DISULFIRAM 125MG TAB UD                    0.060 / EA

DISULFIRAM 250MG S.T.                      0.211 / TAB

DISULFIRAM 62.5MG.TAB UD                   0.050 / EA

AD300  HEAVY METAL ANTAGONISTS

EDETATE CALCIUM DISODIUM INJ 5ML AMP       10.968 / AMP

AD400  ANTIDOTES,DETERRENTS,AND POISON CONTROL EXCHANGE RESINS

SOD POLYSTYRENE SULF SUSP 15GM/60ML 1PT    2.600 / EA

SOD POLYSTYRENE SULF SUSP 15GM/60ML U.D.   3.000 / EA

SODIUM POLYSTYRENE SULFONATE PWD 1LB       28.860 / EA

AD900  ANTIDOTES/DETERRENTS,OTHER

CHARCOAL 50GM W/SORBITOL IN SUSP 8OZ       3.250 / BT

CHARCOAL POWDER 30GM U.D.                  3.250 / EA

DIGOXIN IMMUNE Fab F/INJ 40MG/VIAL         215.400 / EA

FLUMAZENIL 0.5mg/5ml INJ                   22.310 / AMP

PRALIDOXIME 1GM INJ                        7.848 / VI

### National Formulary Report

**[PSNNFL] Synonym:  NATF**

This option allows you to generate a report of National Formulary names marked for National Formulary. This report can be sorted by National Formulary Name or VA Class. This information comes from the VA PRODUCTS file (# 50.68).

**Example: National Formulary Report**

Select National Drug File Reports Menu Option: **NATF** National Formulary Report

This report will print out all National Formulary marked for National

Formulary. You may sort by National Formulary Name or by VA Class.

This information comes from the VA Product file.

This report requires 132 columns. You may queue the report to print,

if you wish.

Sort by VA Class (C) or National Formulary Name (N)? **NAME**

Select Printer: *[Select Print Device]*

VHA NATIONAL FORMULARY    (BY NAME) Date printed: OCT 2,1998

Page: 1

NATIONAL FORMULARY NAME                                                     VA CLASS  RESTRICTION

-------------------------------------------------------------------------------------------------

ACARBOSE TAB                                                                HS502     R

ACETAMINOPHEN ELIXIR                                                        CN103

ACETAMINOPHEN LIQUID                                                        CN103

ACETAMINOPHEN SUSP                                                          CN103

ACETAMINOPHEN TAB                                                           CN103

ACETAMINOPHEN/CODEINE ELIXIR                                                CN101

ACETAMINOPHEN/CODEINE TAB                                                   CN101

ACETAMINOPHEN/HYDROCODONE TAB                                               CN101

ACETAMINOPHEN/OXYCODONE TAB                                                 CN101

ACETAZOLAMIDE INJ                                                           CV703

ACETAZOLAMIDE TAB                                                           CV703

ACETIC ACID LIQUID                                                          GU900

PH000

ACYCLOVIR INJ                                                               AM800     R

ACYCLOVIR SUSP                                                              AM800

*[This report has been abbreviated to save space.]*

### Drug-Drug Interaction Report

**[PSNTER]  Synonym: DDIN**

This option allows you to generate a report of all drug-drug interactions, both critical and significant, contained in the DRUG INTERACTION file (#56).

**Example: Drug-Drug Interaction Report**

Select National Drug File Reports Menu Option: **DDIN** Drug-Drug Interaction Report

This report gives you a printed copy of the Drug Interaction name, Severity,

and whether it was entered Nationally.

You may queue the report to print, if you wish.

START WITH NAME: FIRST// **&lt;RET&gt;**

DEVICE: *[Select Print Device]*

DRUG INTERACTION LIST                          OCT  2,1998  14:35    PAGE 1

NATIONALLY

NAME                                               SEVERITY       ENTERED

--------------------------------------------------------------------------------

ACEBUTOLOL/ACETOHEXAMIDE                           SIGNIFICANT    YES

ACEBUTOLOL/CHLORPROPAMIDE                          SIGNIFICANT    YES

ACEBUTOLOL/CLONIDINE                               SIGNIFICANT    YES

ACEBUTOLOL/DISOPYRAMIDE                            SIGNIFICANT    YES

ACEBUTOLOL/EPINEPHRINE                             SIGNIFICANT    YES

ACEBUTOLOL/FELODIPINE                              SIGNIFICANT    YES

ACEBUTOLOL/GLIPIZIDE                               SIGNIFICANT    YES

ACEBUTOLOL/GLYBURIDE                               SIGNIFICANT    YES

ACEBUTOLOL/INDOMETHACIN                            SIGNIFICANT    YES

ACEBUTOLOL/INSULIN                                 SIGNIFICANT    YES

ACEBUTOLOL/PIROXICAM                               SIGNIFICANT    YES

ACEBUTOLOL/SULINDAC                                SIGNIFICANT    YES

ACEBUTOLOL/TOLAZAMIDE                              SIGNIFICANT    YES

ACEBUTOLOL/TOLBUTAMIDE                             SIGNIFICANT    YES

ACEBUTOLOL/VERAPAMIL                               CRITICAL       YES

ACETAMINOPHEN/SULFINPYRAZONE                       SIGNIFICANT    YES

ACETOHEXAMIDE/ATENOLOL                             SIGNIFICANT    YES

ACETOHEXAMIDE/BETAXOLOL                            SIGNIFICANT    YES

ACETOHEXAMIDE/BISOPROLOL                           SIGNIFICANT    YES

ACETOHEXAMIDE/CARTEOLOL                            SIGNIFICANT    YES

ACETOHEXAMIDE/LABETALOL                            SIGNIFICANT    YES

ACETOHEXAMIDE/METOPROLOL                           SIGNIFICANT    YES

ACETOHEXAMIDE/NADOLOL                              SIGNIFICANT    YES

ACETOHEXAMIDE/PENBUTOLOL                           SIGNIFICANT    YES

ACETOHEXAMIDE/PINDOLOL                             SIGNIFICANT    YES

ACETOHEXAMIDE/PROPRANOLOL                          SIGNIFICANT    YES

ACETOHEXAMIDE/SOTALOL                              SIGNIFICANT    YES

ACETOHEXAMIDE/TIMOLOL                              SIGNIFICANT    YES

ACYCLOVIR/RIFAMPIN                                 CRITICAL       YES

ALFENTANIL/ERYTHROMYCIN                            SIGNIFICANT    YES

ALLOPURINOL/AZATHIOPRINE                           CRITICAL       YES

ALLOPURINOL/MERCAPTOPURINE                         CRITICAL       YES

ALPRAZOLAM/CLOZAPINE                               SIGNIFICANT    YES

*[This report has been abbreviated to save space.]*

### VA Products Marked for CMOP Transmission

**[PSNCMOP] Synonym: CMOP**

This option allows you to generate a report of all VA Product Names marked for Consolidated Mail Outpatient Pharmacy (CMOP) transmission. You can sort by VA Product Name or by the VA Identifier. This information comes from the VA PRODUCT file (# 50.68).

**Example 1: VA Product Marked for CMOP Transmission printed by VA Identifier**

Select National Drug File Reports Menu Option: **CMOP** VA Products Marked for CMOP Transmission

This report will print out all VA Product Names marked for CMOP transmission.

You may either sort by VA Product Name or by VA Identifier.

This information comes from the VA Products file (NATIONALLY MARKED).

*** This is a long report ***

You may queue the report to print, if you wish.

Sort by VA Identifier (I) or VA Product Name (N)? **I** DENTIFIER

DEVICE: *[Select Print Device]*

VA PRODUCT LIST                                          Oct 02, 1998 13:57:31 PAGE 1

ID#       VA PRINT NAME                                VA DISP UNIT

-------------------------------------------------------------------------------------------------

A0001     ACEBUTOLOL HCL 200MG CAP                          CAP

A0002     A &amp; D OINT                                        GM

A0003     ACEBUTOLOL HCL 400MG CAP                          CAP

A0004     ACETAMINOPHEN 100MG/ML SF DROPS                   ML

A0005     ACETAMINOPHEN 100MG/ML DROPS                      ML

A0007     ACETAMINOPHEN 120MG/5ML ELIXIR                    ML

A0009     ACETAMINOPHEN 130MG/5ML SOLN                      ML

A0010     ACETAMINOPHEN 160MG SPRINKLE CAP                  CAP

A0011     ACETAMINOPHEN 160MG TAB                           TAB

A0013     ACETAMINOPHEN 160MG/5ML LIQUID                    ML

A0015     APAP 200/PSEUDOEPHEDRINE 30MG CAP                 CAP

A0016     APAP 200/PSEUDOEPHEDRINE 30MG TAB                 TAB

A0017     APAP 250/SALICYLAMIDE 250MG CAP                   CAP

A0018     APAP 250/SALICYLAMIDE 600MG TAB                   TAB

A0019     APAP 300/CHLORZOXAZONE 250MG CAP                  CAP

A0020     APAP 300/CHLORZOXAZONE 250MG TAB                  TAB

A0021     ACETAMINOPHEN 325MG RTL SUPP                      EA

*[This report has been abbreviated to save space.]*

**Example 2: VA Product Marked for CMOP Transmission printed by VA Product Name**

Select National Drug File Reports Menu Option: **CMOP** VA Products Marked for CMOP Transmission

This report will print out all VA Product Names marked for CMOP transmission.

You may either sort by VA Product Name or by VA Identifier.

This information comes from the VA Products file (NATIONALLY MARKED).

*** This is a long report ***

You may queue the report to print, if you wish.

Sort by VA Identifier (I) or VA Product Name (N)? NAME

DEVICE: *[Select Print Device]*

VA PRODUCT LIST                   Oct 02, 1998 13:57:55 PAGE 1

VA PRODUCT NAME

VA PRINT NAME                                     VA DISP UNIT   ID#

--------------------------------------------------------------------------------

A &amp; D OINT

A &amp; D OINT                                           GM        A0002

ABCIXIMAB 2MG/ML INJ

ABCIXIMAB 2MG/ML INJ                                 ML        A0578

ABSORBASE TOP OINT

ABSORBASE TOP OINT                                   GM        A0489

ABSORBTIVE DRESSING 6GM #740036

ABSORBTIVE DRESSING 6GM #740036                      6GM PKT   XA011

ACACIA POWDER

ACACIA POWDER                                        GM        A0617

ACARBOSE 100MG TAB

ACARBOSE 100MG TAB                                   TAB       A0600

ACARBOSE 100MG TAB UD

ACARBOSE 100MG TAB UD                                TAB       A0996

ACARBOSE 25MG TAB

ACARBOSE 25MG TAB                                    TAB       A0987

ACARBOSE 50MG TAB

ACARBOSE 50MG TAB                                    TAB       A0599

ACARBOSE 50MG TAB UD

ACARBOSE 50MG TAB UD                                 TAB       A0997

ACCU-CHEK II CONTROL

ACCU-CHEK II CONTROL                                 EA        XA012

ACEBUTOLOL HCL 200MG CAP

ACEBUTOLOL HCL 200MG CAP                             CAP       A0001

ACEBUTOLOL HCL 400MG CAP

ACEBUTOLOL HCL 400MG CAP                             CAP       A0003

ACEL-IMUNE INJ

ACEL-IMUNE INJ                                       ML        A0618

ACETAMINOPHEN 100MG/ML DROPS

ACETAMINOPHEN 100MG/ML DROPS                         ML        A0005

ACETAMINOPHEN 100MG/ML SF DROPS

ACETAMINOPHEN 100MG/ML SF DROPS                      ML        A0004

ACETAMINOPHEN 120MG RTL SUPP

ACETAMINOPHEN 120MG RTL SUPP                         EA        A0006

ACETAMINOPHEN 120MG/5ML ELIXIR

ACETAMINOPHEN 120MG/5ML ELIXIR                       ML        A0007

ACETAMINOPHEN 125MG RTL SUPP

ACETAMINOPHEN 125MG RTL SUPP                         EA        A0008

*[This report has been abbreviated to save space.]*

### VA Product Names By Class Report

**[PSNCLPR]    Synonym: PNCL**

This option generates a report of all VA Product Names sorted by VA Drug Class. You can sort by Primary, Secondary, or Both classes. The information for this report comes from the VA PRODUCT file (# 50.68).

**Example: VA Product Names by Class**

Select National Drug File Reports Menu Option: **PNCL** VA Product Names By Class Report

This report will print out all VA Product Names by VA Drug Class. You may

sort by Primary, Secondary, or Both Classes. This information comes from

the VA Products file.

You may queue the report to print, if you wish.

Sort by Primary (P), Secondary (S), or Both (B) Classes? **PRIMARY**

DEVICE: *[Select Print Device]*

VA PRODUCT LIST                               Oct 02, 1998 13:58:32 PAGE 1

PRIMARY

VA CLASS

CODE        VA PRODUCT NAME

--------------------------------------------------------------------------------

AD100     DISULFIRAM 250MG TAB

AD100     DISULFIRAM 500MG TAB

AD200     CYANIDE ANTIDOTE PACKAGE INJ

AD200     METHYLENE BLUE 1% INJ

AD200     NA SULFITE 0.0125%/NA THIOSULFATE 10%/NACL 0.3% INJ

AD200     SODIUM THIOSULFATE 100MG/ML INJ

AD200     SODIUM THIOSULFATE 250MG/ML INJ

AD300     DEFEROXAMINE MESYLATE 100MG/ML INJ

AD300     DIMERCAPROL 100MG/ML INJ

AD300     EDETATE CA DISODIUM 200MG/ML INJ

AD300     EDETATE DISODIUM 150MG/ML INJ

AD300     SUCCIMER 100MG CAP

AD300     TRIENTINE HCL 250MG CAP

AD400     SODIUM POLYSTYRENE SULFONATE 15GM/60ML SUSP

AD400     SODIUM POLYSTYRENE SULFONATE 30GM/120ML RTL

AD400     SODIUM POLYSTYRENE SULFONATE 50GM/200ML SUSP,RTL

AD400     SODIUM POLYSTYRENE SULFONATE PWDR

AD900     CHARCOAL 260MG CAP,ORAL

AD900     CHARCOAL 60ML #4/IPECAC SYRUP 30ML/KIT

AD900     CHARCOAL,ACTIVATED 15GM/120ML LIQUID

AD900     CHARCOAL,ACTIVATED 15GM/75ML LIQUID

AD900     CHARCOAL,ACTIVATED 25GM/120ML LIQUID

AD900     CHARCOAL,ACTIVATED 25GM/SORBITOL 120ML LIQUID

AD900     CHARCOAL,ACTIVATED 30GM/120ML LIQUID

AD900     CHARCOAL,ACTIVATED 30GM/SORBITOL 70% 150ML LIQUID

AD900     CHARCOAL,ACTIVATED 50GM/240ML LIQUID

AD900     CHARCOAL,ACTIVATED 50GM/SORBITOL 240ML LIQUID

AD900     CHARCOAL,ACTIVATED PWDR

AD900     CHLORPHENIRAMINE 2MG TAB #4/EPINEPHRINE 1MG SYR/KIT

AD900     DEXTRAN-1,150MG/ML INJ

AD900     DIGOXIN IMMUNE FAB (OVINE) 40MG/VIL INJ

AD900     FLUMAZENIL 0.1MG/ML INJ

AD900     FOMEPIZOLE 1GM/ML INJ

*[This report has been abbreviated to save space.]*

### Local Drug/VA Print Name Report

**[PSNVAPRINT]  Synonym: LDPN**

This option generates a report listing all active entries in the local DRUG file (#50) for which the Generic Name does not match the VA Print Name stored in the National Drug File. You can sort this report alphabetically using a range of letters, or display all entries in the file that meet this criteria.

**Example: Local Drug/VA Print Name Report**

Select National Drug File Reports Menu Option:  Local Drug/VA Print Name Report

This report shows a list of the active drugs in local DRUG file where the

GENERIC NAME does not match the VA PRINT NAME.

Select one of the following:

A         ALL

S         SELECT A RANGE

Print Report for (A)ll Drugs or (S)elect a Range of Drugs: S// SELECT A RANGE

There are drugs in the Drug file with leading numerics.

Print report for drugs with leading numerics? N// O

To see drugs beginning with the letter 'A', enter 'A', or whichever letter you

wish to see. To see drugs in a range, for example drugs starting with the

letters 'G', 'H', 'I' and 'J', enter in the format 'G-J'.

Select a Range: A-B

This report will include drugs starting with the letter A,

and ending with drugs starting with the letter B.

Is this correct? Y// ES

DEVICE: HOME//   VIRTUAL    Right Margin: 80//

report follows on the next page

**Example: Local Drug/VA Print Name Report (cont.)**

Local Drug/VA Print Name Report

for Drug Names Beginning with the letter A through B

Date printed: MAR 16,2001                                            Page: 1

Generic Name                               VA Print Name

-------------------------------------------------------------------------------

A AND D OINTMENT                           A &amp; D OINT

ABSORBABLE GELATIN FILM

ABSORBABLE GELATIN SPONGE SZ. 12           HYDROCORTISONE 10MG TAB

ABSORBABLE GELATIN SPONGE SZ.7

ABSORBABLE GELATIN SPONGE-100

ACE BANDAGE 4 INCH                         ADHESIVE ELASTIC BANDAGE

ACETAMINOPHEN 325MG TABLET                 ACETAMINOPHEN 325MG TAB

ACETAMINOPHEN 650MG SUPPOS.                ACETAMINOPHEN 650MG RTL SUPP

ACETAMINOPHEN AND CODEINE 30MG             CODEINE 30/ACETAMINOPHEN 300MG TAB

ACETAMINOPHEN, CODEINE ELIXIR (OZ)         CODEINE 12/APAP 120MG/5ML ELIXIR

ACETAMINPHEN 325MG CT                      ACETAMINOPHEN 325MG TAB

ACETAZOLAMIDE 250MG S.T.                   ACETAZOLAMIDE 250MG TAB

ACETAZOLAMIDE 500MG INJ                    ACETAZOLAMIDE NA 500MG/VIL INJ

ACETAZOLAMIDE 500MG SEQUELS                ACETAZOLAMIDE 500MG SA CAP

ACETEST 100'S                              ACETEST TAB (NOT FOR ORAL USE)

ACETIC ACID 0.25% IRRIG. 500ML             ACETIC ACID 0.25% IRRG SOLN

ACETIC ACID 2% OTIC SOL 15 ML              ACETIC ACID 2% OTIC SOLN

ACETIC ACID 2%/HC 1% OTIC SOL              ACETIC ACID 2/HC 1% OTIC SOLN

ACETYLCHOLINE CHL INTRAOCULAR              ACETYLCHOLINE CHLORIDE 1% OPH SOLN

ACETYLCYSTEINE 20% 30ML                    ACETYLCYSTEINE 20% INHL SOLN

ACTIVATED CHARCOAL USP                     ACTIVATED CHARCOAL 250MG TAB

*[This report has been abbreviated to save space.]*

### Local Drugs Excluded from Drug-Drug Interactions

**[PSNODDI]  Synonym: LDRG**

This option generates a report of local dispense drugs which are matched to VA Products that are marked as EXCLUDE from drug-drug interaction checking.

**Example: Local Drugs Excluded from Drug-Drug Interactions**

Select National Drug File Reports Menu Option: **LDRG** Local Drugs Excluded from Drug-Drug Interactions

This report gives you a printed copy of Dispense Drugs from your

local file which are matched to VA Products that are marked as

EXCLUDE from Drug-Drug Interaction checking.

You may queue the report to print, if you wish.

START WITH GENERIC NAME: FIRST// **&lt;ENTER&gt;**

DEVICE:  GENERIC INCOMING TELNET

DISPENSE DRUGS MATCHED TO VA PRODUCTS EXCLUDED FROM DRG-DRG INTERACTION CHECKING

GENERIC NAME                                     VA DRUG CLASS   DOSE FORM

VA PRODUCT NAME

A AND Z OINTMENT                                  DE350           OINT,TOP

VITAMIN A/VITAMIN D OINT,TOP

ABSORBABLE GELATIN SPONGE SZ.7                    BL300           SPONGE

GELATIN,ABSORBABLE SPONGE,SZ 12,7MM

ABSORBABLE GELATIN SPONGE-100                     BL300           SPONGE

GELATIN,ABSORBABLE SPONGE,SZ 100

ACE BANDAGE 4 INCH                                XA108           BANDAGE

ADHESIVE BANDAGE,ELASTIC

ACETIC ACID 0.25% IRRIG. 500ML                    IR100           SOLN,IRRG

ACETIC ACID 0.25% SOLN,IRRG

*[This report has been abbreviated to save space.]*

### VA Products Excluded from Drug-Drug Interactions

**[PSNexmpt]  Synonym: VDRG**

This option generates a report of active VA Products marked as EXCLUDE from drug-drug interaction checking.

**Example: VA Products Excluded from Drug-Drug Interactions**

Select National Drug File Reports Menu Option: **VDRG** VA Products Excluded from Drug-Drug Interactions

This report gives you a printed copy of active VA Products marked as

EXCLUDE from Drug-Drug Interaction checking.

You may queue the report to print, if you wish.

START WITH NAME: FIRST// **&lt;ENTER&gt;**

DEVICE:   GENERIC INCOMING TELNET

VA Products Marked As Exclude From Drg-Drg Interaction Checking

JUL 29,2003  14:33    PAGE 1

--------------------------------------------------------------------------------

ABSORBASE OINT,TOP

ABSORBTIVE DRESSING 6GM #740036

ACCESS PIN, NEEDLE-FREE ALARIS #2200E

ACCU-CHEK ACTIVE (GLUCOSE) HI/LO CONTROL SOLN

ACCU-CHEK ACTIVE (GLUCOSE) TEST STRIP

ACCU-CHEK COMFORT CURVE (GLUCOSE) HI/LO CONTROL SOLN

ACCU-CHEK COMFORT CURVE (GLUCOSE) HI/MED/LO CONTROL SOLN

ACCU-CHEK COMFORT CURVE (GLUCOSE) TEST STRIP

ACCU-CHEK COMFORT CURVE-H (GLUCOSE) HI/LO CONTROL SOLN

ACCU-CHEK COMFORT CURVE-H (GLUCOSE) TEST STRIP

ACCU-CHEK COMPACT (GLUCOSE) TEST DRUM,17

ACCU-CHEK II CONTROL

ACCU-CHEK INSTANT (GLUCOSE) CONTROL SOLN

ACCU-CHEK INSTANT (GLUCOSE) METER

ACCU-CHEK INSTANT (GLUCOSE) TEST STRIP

ACCU-CHEK INSTANT DM (GLUCOSE) METER

## Using the Inquire Options

### ### Inquiry Options

**[PSNQUER]   Synonym: INQ**

This sub-menu contains all the inquiry options in the National Drug File package.

*LINQ	Inquire To Local Drug File*

*PNIN	Inquire to VA Product Info For Local Drug* *******

*NDCU	NDC/UPN Inquiry*

*NAT	Inquire to National Files*

*Formerly *Lookup National Drug Info In Local File.*

### Inquire to Local Drug File

**[PSNVIEW]   Synonym: LINQ**

This option allows you to view the local DRUG file (#50) by Generic Name/Synonym or VA Drug Class Code. If you choose a VA Drug Class Code, you may enter either the code or the class name. For VA Drug Class Code, the software will sort by the least expensive price in the PRICE PER DISPENSE UNIT field (#16). The Generic Name, VA Drug Class Code, Price Per Dispense Unit, Message, and Synonyms not marked as quick codes are displayed. Only active formulary drugs can be viewed.

**Example 1: Inquire to Local Drug File by Generic Name Chosen**

Select Inquiry Options Option: **LINQ** Inquire To Local Drug File

You may look-up by DRUG GENERIC NAME or VA CLASS CODE

Enter a "G" for GENERIC NAME or a "C" for VA CLASS CODE: **G** GENERIC

Select DRUG GENERIC NAME : **NORPACE**

1   NORPACE  PENICILLAMINE 125MG CAP           MS104

2   NORPACE  DISOPYRAMIDE 150MG CAP                     Tier 3

3   NORPACE 100MG CAP  DISOPYRAMIDE 100MG CAP           CV300

4   NORPACE 150MG CAP  DISOPYRAMIDE 150MG CAP           CV300

5   NORPACE CR 100MG CAP  DISOPYRAMIDE **CR** 100MG CAP           CV300

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **2** DISOPYRAMIDE 150MG CAP

report follows on the next page

**Example 1: Inquire to Local Drug File by Generic Name Chosen (cont.)**

GENERIC NAME:  DISOPYRAMIDE 150MG CAP

VA DRUG CLASS CODE:

PRICE/DISPENSING UNIT:  0.160

MESSAGE:

SYNONYM(S):

NORPACE

You may look-up by DRUG GENERIC NAME or VA CLASS CODE

Enter a "G" for GENERIC NAME or a "C" for VA CLASS CODE: **&lt;RET&gt;**

#### #### ### Inquire to VA Product Info For Local Drug

**[PSNLOOK] Synonym:   PNIN**

This option was formerly known as *Lookup National Drug Info in Local File* . This option allows you to look up entries in the local DRUG file (#50). It will display information found in the VA PRODUCT file (# 50.68) for the VA Product Name to which the local drug is matched.

Patch PSN*4*396 modified this option to include the following fields from

the VA PRODUCT file (#50.68) when values are defined:

HAZARDOUS TO HANDLE field (#101)

HAZARDOUS TO DISPOSE field (#102)

PRIMARY EPA CODE field (#103)

WASTE SORT CODE field (#104)

DOT SHIPPING CODE field (#105)

FORMULARY DESIGNATOR field (#109)

FORMULARY DESIGNATOR TEXT field (#110)

CLINICAL EFFECT multiple (#50.68108)

PACKAGE field (#.01)

OMIT EXP/DC ORDER CHECK field (#1)

DURATION LIMIT field (#2)

With patch PSN*4*513 users will see these fields populated or displayed.

When data is populated, the hazardous waste group of  fields will display after

Maximum Days Supply. FORMULARY DESIGNATOR  field (#109) will display

after NATIONAL FORMULARY INDICATOR and FORMULARY DESIGNATOR

TEXT field (#110) will display as "Product Text" after NATIONAL

RESTRICTION". The CODING SYSTEM multiple (#43) will be populated with

RxNorm data.

The DURATION LIMIT field (#2) of the CLINICAL EFFECTS multiple

(#50.68108) defines the time frame that expired and discontinued

orders are omitted from Medication Order Check Application (MOCHA)

enhanced order checking.  The default value of NO will be displayed

after Override DF Exclude from Dosage Checks.  The CLINICAL EFFECTS fields

will not be populated until a future patch and until that time the default value of

NO will be displayed.

**Example: Lookup National Drug Info in Local File**

Select Inquiry Options Option: **PNIN** Inquire to VA Product Info For Local Drug

This option will allow you to look up entries in your local DRUG file. It will

display National Drug File software match information.

**Exclude Interaction check=Y, Override DF Exclude from Dosage Check =N**

Note that the Exclude Drg-Drg Interaction Ck field only displays when set to ‘Yes.’ If a dosage form has been excluded from dosage checks that fact will be displayed next to the dosage form.

Select DRUG GENERIC NAME: HYDROCORTISONE 1% CREAM         DE200

DRUG Generic Name:  HYDROCORTISONE 1% CREAM

VA Product Name: HYDROCORTISONE 1% CREAM,TOP

VA Generic Name: HYDROCORTISONE

Dosage Form: CREAM,TOP  (Exclude from Dosing Cks)

Strength: 1 Units: %

National Formulary Name: HYDROCORTISONE CREAM,TOP

VA Print Name: HYDROCORTISONE 1% CREAM

VA Product Identifier: H0055                      Transmit To CMOP: YES

VA Dispense Unit: GM

PMIS: HYDROCORTISONE - TOPICAL

Active Ingredients:

HYDROCORTISONE                                 Str: 1         Unt: %

Press Return to Continue:

Primary Drug Class: DE200

CS Federal Schedule:   None

Single/Multi Source Product:

Max Single Dose:                             Min Single Dose:

Max Daily Dose:                              Min Daily Dose:

Max Cumulative Dose:

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE. Copay Tier: 2

Copay Effective Date: APR 1, 2016

Exclude Drg-Drg Interaction Ck: Yes (No check for Drug-Drug Interactions)

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

Press Return to Continue:

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

Press Return to Continue:

Coding System: RxNorm

Code: 898587

Restriction:

Refer to VA/DoD Hyperlipidemia treatment guidelines

Select DRUG GENERIC NAME:

In this example, the Dosage Form of ‘Oil’ is excluded from dosage checks, but since the Override DF Exclude from Dosage Checks is set to ‘Yes’, dosage checks will be performed for the VA Product, ‘Cod Liver Oil.’

Select DRUG GENERIC NAME: Cod liver oil

1   COD LIVER OIL           VT801

2   COD LIVER OIL/TALC/ZINC OXIDE 40% OINT           DE900

CHOOSE 1-2: 1  COD LIVER OIL         VT801

DRUG Generic Name:  COD LIVER OIL

VA Product Name: COD LIVER OIL

VA Generic Name: COD LIVER OIL

Dosage Form: OIL  (Exclude from Dosing Cks)

Strength:

National Formulary Name: COD LIVER OIL OIL

VA Print Name: COD LIVER OIL

VA Product Identifier: C0504                      Transmit To CMOP: YES

VA Dispense Unit: ML

PMIS: None

Active Ingredients:

COD LIVER OIL                                  Str:

Press Return to Continue:

Primary Drug Class: VT801

CS Federal Schedule:   None

Single/Multi Source Product:

Max Single Dose:                             Min Single Dose:

Max Daily Dose:                              Min Daily Dose:

Max Cumulative Dose:

National Formulary Indicator: No

Copay Tier: 0

Copay Effective Date: APR 1, 2016

Override DF Exclude from Dosage Checks: Yes (Dosage Checks shall be performed)

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

Press Return to Continue:

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

Press Return to Continue:

Coding System: RxNorm

Code: 89800

Restriction:

Refer to VA/DoD Hyperlipidemia treatment guidelines

Select DRUG GENERIC NAME:

**Exclude Interaction check=not set, Override DF Exclude from Dosage Check =Y**

In this example, the Dosage Form of ‘Powder,Oral’ IS NOT excluded from dosage checks, but since the Override DF Excluded from Dosage Checks is set to ‘Yes’, dosage checks will not be performed for the VA Product , ‘Thick-It Powder’.

Select DRUG GENERIC NAME: THICK-IT POWDER           TN200

DRUG Generic Name:  THICK-IT POWDER

VA Product Name: THICK-IT POWDER

VA Generic Name: THICK-IT

Dosage Form: POWDER,ORAL

Strength:

National Formulary Name: THICK-IT POWDER,ORAL

VA Print Name: THICK-IT POWDER

VA Product Identifier: T0557                      Transmit To CMOP: YES

VA Dispense Unit: GM

PMIS: None

Active Ingredients:

CORN STARCH                                    Str:

Press Return to Continue: &lt;ENTER&gt;

Primary Drug Class: TN200

CS Federal Schedule: 0  Unscheduled

Single/Multi Source Product:

Max Single Dose:                             Min Single Dose:

Max Daily Dose:                              Min Daily Dose:

Max Cumulative Dose:

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE. Copay Tier: 0

Copay Effective date: APR 1, 2016

Override DF Exclude from Dosage Checks: Yes (No Dosage Checks performed)

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

Press Return to Continue:

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

Press Return to Continue:

Coding System: RxNorm

Code: 8987

Restriction:

Refer to VA/DoD Hyperlipidemia treatment guidelines

Select DRUG GENERIC NAME:

### Auto-Creation of Supra-Therapeutic Possible Dosages

In order to prevent inadvertent creation of supra-therapeutic possible dosages for high risk medications during the dosage creation segment of Pharmacy Data Management and National Drug File updates, three patches have been released. Patch PSN*4*261 added three new fields to the VA PRODUCT file (#50.68). Patch PSN*4*262, in conjunction with Pharmacy Data Management patch PSS*1*155, provides the functionality to determine if possible dosages should be auto-created or not during the match/re-match process.

PSN*4*262 contains changes to the *Inquire to VA Product Info For Local Drug* [PSNLOOK] option to include the display of the new fields.

<!-- image -->

For more information about the new fields, refer to PSN*4*261. For information on how the new fields affect auto-creation of possible dosages during the match and re-match process, refer to patch PSS*1*155. For more information about the supra-therapeutic dosages project, refer to the Release Notes for these patches.

**Example 1: Auto-Create Default Possible Dosage=Yes [PSNLOOK]**

Select OPTION NAME: PSNLOOK

This option will allow you to look up entries in your local DRUG file. It will display National Drug File software match information.

Select DRUG GENERIC NAME:    NIFEDIPINE 20MG CAPS         CV200

DRUG Generic Name:  NIFEDIPINE 20MG CAPS

VA Product Name: NIFEDIPINE 20MG CAP

VA Generic Name: NIFEDIPINE

Dosage Form: CAP,ORAL

Strength: 20 Units: MG

National Formulary Name: NIFEDIPINE CAP,ORAL

VA Print Name: NIFEDIPINE 20MG CAP

VA Product Identifier: N0042                      Transmit To CMOP: YES

VA Dispense Unit: CAP

PMIS: NIFEDIPINE - ORAL

Active Ingredients:

NIFEDIPINE                                     Str: 20        Unt: MG

Press Return to Continue:

Primary Drug Class: CV200

CS Federal Schedule:   None

Single/Multi Source Product:

Max Single Dose:                             Min Single Dose:

Max Daily Dose:                              Min Daily Dose:

Max Cumulative Dose:

National Formulary Indicator: No

Copay Tier: 3

Copay Effective Date: APR 1, 2016

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

Restriction:

Refer to PBM/MAP criteria for use of long-acting dihydropyridine calcium

antagonists

Press Return to Continue:

**Example 2: Auto-Create Default Possible Dosage= No, and No Possible Dosages Created [PSNLOOK]**

…

National Formulary Indicator: No

Copay Tier: 3

Copay Effective Date: APR 1, 2016

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? No

Possible Dosages To Auto-Create: No Possible Dosages

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

**Example 3: Auto-Create Default Possible Dosage= No, and Create One Possible Dosage [PSNLOOK]**

…

National Formulary Indicator: No

Copay Tier: 3

Copay Effective Date: APR 1, 2016

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? No

Possible Dosages To Auto-Create: 1x Possible Dosages

Package: Inpatient

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

**Example 4: Auto-Create Default Possible Dosage= No, and Create Two Possible Dosages [PSNLOOK]**

…

National Formulary Indicator: No

Copay Tier: 3

Copay Effective Date: APR 1, 2016

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? No

Possible Dosages To Auto-Create: 2x Possible Dosages

Package: Inpatient and Outpatient

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

### Fixed Medication Copayment Tier

PSN*4.0*492 contains changes to the *Inquire to VA Product Info For Local Drug* [PSNLOOK] option to include the display of the new fields as part of the Fixed Medication Copay Tier project.

#### <!-- image -->

For more information about the new fields, refer to the patch description for PSN*4.0*492 in Forum.

The Copay Tier fields will be displayed after the National Formulary Indicator Field.

Primary Drug Class: BL110

CS Federal Schedule: 0  Unscheduled

Single/Multi Source Product: Multi

Max Single Dose:                             Min Single Dose:

Max Daily Dose:                              Min Daily Dose:

Max Cumulative Dose:

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE. Copay Tier:

Copay Effective Date:

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

**Example 1:  Auto-Create Default Possible Dosage= No, and Create One and Two Possible Dosages [PSNLOOK]**

Select Inquiry Options Option: PNIN  Inquire to VA Product Info For Local Drug

This option will allow you to look up entries in your local DRUG file. It will

display National Drug File software match information.

Select DRUG GENERIC NAME: DICLOX

1   DICLOXACILLIN 250MG CAP           AM112

2   DICLOXACILLIN SUSP 62.5MG/5ML 80ML           AM112

CHOOSE 1-2: 1  DICLOXACILLIN 250MG CAP         AM112

DRUG Generic Name:  DICLOXACILLIN 250MG CAP

VA Product Name: DICLOXACILLIN NA 250MG CAP

VA Generic Name: DICLOXACILLIN

Dosage Form: CAP,ORAL

Strength: 250 Units: MG

National Formulary Name: DICLOXACILLIN CAP,ORAL

VA Print Name: DICLOXACILLIN NA 250MG CAP

VA Product Identifier: D0064                      Transmit To CMOP: YES

VA Dispense Unit: CAP

PMIS: DICLOXACILLIN - ORAL

Active Ingredients:

DICLOXACILLIN                                  Str: 250       Unt: MG

Press Return to Continue:

Primary Drug Class: AM112

CS Federal Schedule:   None

Single/Multi Source Product:

Max Single Dose:                             Min Single Dose:

Max Daily Dose:                              Min Daily Dose:

Max Cumulative Dose:

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE. Copay Tier: 3

Copay Effective Date: APR 05, 2016

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? No

Possible Dosages To Auto-Create: 1x and 2x Possible Dosages

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

Press Return to Continue:

### NDC/UPN Inquiry

**[PSNUPN] Synonym: NDCU**

With this option you can enter an NDC or UPN to get the corresponding information displayed to the screen. This data comes from the NDC/UPN file (#50.67).

**Example: Inquiry using an NDC**

Select Inquiry Options Option: **NDC** NDC/UPN Inquiry

This option allows you to pick an NDC or UPN and the corresponding

information from NDC/UPN file will be displayed to the screen.

Do you want to Inquire on an NDC or UPN:

Select one of the following:

N         NDC

U         UPN

Enter response: NDC// **&lt;ENTER&gt;**

Select NDC/UPN: **510002014150**

1   510002014150  86849

2   510002014150  86850

CHOOSE 1-2: **2** 86850

NDC: 510002014150                            OTX/RX Indicator:

Manufacturer: FEDERAL SUPPLY

Trade Name: COTTON BALL

Package Size: 2000                           Package Type: BAG

Do you want to Inquire on an NDC or UPN:

Select one of the following:

N         NDC

U         UPN

Enter response: NDC// **&lt;ENTER&gt;**

Select NDC/UPN: **&lt;ENTER&gt;**

### Inquire to National Files

[PSNACT] Synonym:  NAT

The Inquire to National Files displays information related to products contained within the national files. The product may be selected by entering the VA Product Name, CMOP ID or NDC.

Select Inquiry Options Option: **NAT** Inquire to National Files

This option allows you to lookup NDF file information three ways (VA Product Name, NDC, or CMOP ID number).

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ?

*Auto-Creation of Supra-Therapeutic Possible Dosages*

In order to prevent inadvertent creation of supra-therapeutic possible dosages for high risk medications during the dosage creation segment of Pharmacy Data Management and National Drug File updates, three patches have been released. Patch PSN*4*261 added three new fields to the VA PRODUCT file (#50.68). Patch PSN*4*262, in conjunction with Pharmacy Data Management patch PSS*1*155, provides the functionality to determine if possible dosages should be auto-created or not during the match/re-match process.

PSN*4*262 contains changes to the *Inquire to National Files* [PSNACT] option to include the display of the new fields.

<!-- image -->

For more information about the new fields, refer to PSN*4*261. For information on how the new fields affect auto-creation of possible dosages during the match and re-match process, refer to patch PSS*1*155.

Patch PSN*4*396 modified this option to include the following fields from

the VA PRODUCT file (#50.68) when values are defined:

HAZARDOUS TO HANDLE field (#101)

HAZARDOUS TO DISPOSE field (#102)

PRIMARY EPA CODE field (#103)

WASTE SORT CODE field (#104)

DOT SHIPPING CODE field (#105)

FORMULARY DESIGNATOR field (#109)

FORMULARY DESIGNATOR TEXT field (#110)

CLINICAL EFFECT multiple (#50.68108)

PACKAGE field (#.01)

OMIT EXP/DC ORDER CHECK field (#1)

DURATION LIMIT field (#2)

With patch PSN*4*513 users will see these fields populated or displayed.

When data is populated, the hazardous waste group of  fields will display after

Maximum Days Supply. FORMULARY DESIGNATOR  field (#109) will display

after NATIONAL FORMULARY INDICATOR and FORMULARY DESIGNATOR

TEXT field (#110) will display as "Product Text" after NATIONAL

RESTRICTION".  The CODING SYSTEM multiple (#43) will be populated with

RxNorm data.

The DURATION LIMIT field (#2) of the CLINICAL EFFECTS multiple

(#50.68108) defines the time frame that expired and discontinued

orders are omitted from Medication Order Check Application (MOCHA)

enhanced order checking.  The default value of NO will be displayed

after Override DF Exclude from Dosage Checks.  The CLINICAL EFFECTS fields

will not be populated until a future patch and until that time the default value of

NO will be displayed.

**Example 1: NDF Inquiry by VA Product Name**

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? **VA** VA PRODUCT

Select VA PRODUCT NAME: hydrocortisone

1   HYDROCORTISONE 0.1% CREAM,TOP Tier 0

2   HYDROCORTISONE 0.25% CREAM,TOP

3   HYDROCORTISONE 0.25% LOTION

4   HYDROCORTISONE 0.25%/NEOMYCIN SO4 0.5% CREAM,TOP

5   HYDROCORTISONE 0.5% AEROSOL,TOP

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 1  HYDROCORTISONE 0.1% CREAM,TOP

VA Product Name: HYDROCORTISONE 0.1% CREAM,TOP

VA Generic Name: HYDROCORTISONE

Dose Form: CREAM,TOP  (Exclude from Dosing Cks)

Strength: 0.1 Units: %

National Formulary Name: HYDROCORTISONE CREAM,TOP

VA Print Name: HYDROCORTISONE 0.1% CREAM

report continues on the next page

**Example 1: NDF Inquiry by VA Product Name (cont.)**

VA Product Identifier: H0161 Transmit to CMOP: Yes VA Dispense Unit: GM

PMIS: None

Active Ingredients:    HYDROCORTISONE  Strength: 0.1 Units: %

Primary VA Drug Class: DE200

Secondary VA Drug Class:

CS Federal Schedule:

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE.

National Formulary Restriction:

Copay Tier: 1

Copay Effective Date: APR 1, 2016

Exclude Drg-Drg Interaction Ck: Yes (No check for Drug-Drug Interactions)

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

**Auto-Create Default Possible Dosage** is set to Yes.

<!-- image -->

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

Auto-Create Default Possible Dosages? Yes

Maximum Days Supply:

Coding System: RxNorm

Code: 898587

Press return to continue or '^' to exit:

NDC: 000749040201  UPN:

VA Product Name: HYDROCORTISONE 0.1% CREAM,TOP

Manufacturer: MILL MARK PHARM  Trade Name: HYDROCORTISONE

Route: TOPICAL

Package Size: 20 GM  Package Type: TUBE

NDC: 000166069539  UPN:

VA Product Name: HYDROCORTISONE 0.1% CREAM,TOP

Manufacturer: MALLARD  Trade Name: HYDROCORTISONE

Route: TOPICAL

Package Size: 454 GM  Package Type: JAR

**Example 2: NDF Inquiry by NDC**

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? **n** NDC

NDC (N) or UPN (U) ? **n** NDC

Enter NDC with or without Dashes (-): **000223145302** 98650

...OK? Yes// &lt; **ENTER** &gt;  (Yes)

NDC: 000223145302  UPN:

VA Product Name: PLACEBO TAB

Manufacturer: CONSOLIDATED MC  Trade Name: PLACEBO

Route: ORAL

Package Size: 1000  Package Type: BOTTLE

VA Product Name: PLACEBO TAB

VA Generic Name: PLACEBO

Dose Form: TAB

Strength:  Units:

National Formulary Name: PLACEBO TAB

VA Print Name: PLACEBO CAP/TAB

VA Product Identifier: P0256 Transmit to CMOP: Yes VA Dispense Unit: CAP/TAB

PMIS: None

report continues on the next page

**Example 2: NDF Inquiry by NDC (cont.)**

Active Ingredients:    LACTOSE  Strength: 10 Units: %WW

CELLULOSE  Strength: 3 Units: %WW

STARCH  Strength: 87 Units: %WW

Primary VA Drug Class: XX000

Secondary VA Drug Class:

CS Federal Schedule:

Press return to continue or '^' to exit:

**Exclude Drg-Drg Interaction Ck** will only display if it is set to Yes.

<!-- image -->

National Formulary Restriction:

Copay Tier: 1

Copay Effective Date:

Override DF Exclude from Dosage Checks: Yes (No dosage checks performed)

CLINICAL EFFECT DURATION: NO

**Auto-Create Default Possible Dosage** is set to No and no Possible Dosages are auto-created.

<!-- image -->

Auto-Create Default Possible Dosage? No

Possible Dosages To Auto-Create: No Possible Dosages

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

Press return to continue or '^' to exit:

**Example 3: NDF Inquiry by CMOP ID Number**

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? c  CMOP ID

CMOP ID: c0504  COD LIVER OIL

VA Product Name: COD LIVER OIL

VA Generic Name: COD LIVER OIL

Dose Form: OIL  (Exclude from Dosing Cks)

Strength:  Units:

National Formulary Name: COD LIVER OIL OIL

VA Print Name: COD LIVER OIL

VA Product Identifier: C0504 Transmit to CMOP: Yes VA Dispense Unit: ML

PMIS: None

Active Ingredients:    COD LIVER OIL  Strength:  Units:

Primary VA Drug Class: VT801

Secondary VA Drug Class:

CS Federal Schedule:

National Formulary Indicator: No

National Formulary Restriction:

Copay Tier: 1

Copay Effective Date: APR 1, 2016

Exclude Drg-Drg Interaction Ck: Yes (No check for Drug-Drug Interactions)

Override DF Exclude from Dosage Checks: Yes (Dosage Checks shall be performed)

CLINICAL EFFECT DURATION: NO

**Example 3: NDF Inquiry by CMOP ID Number (cont.)**

Auto-Create Default Possible Dosage? No

Possible Dosages To Auto-Create: 1x and 2x Possible Dosages

Package: Both Inpatient and Outpatient

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

**Auto-Create Default Possible Dosage** is set to No and  Possible Dosages  are auto-created for both Inpatient and Outpatient packages.

<!-- image -->

Press return to continue or '^' to exit:

NDC: 000395063594  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: WALMEAD  Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 120 ML  Package Type: BOTTLE

NDC: 000395063794  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: WALMEAD  Trade Name: COD LIVER OIL, MINT FLAVORED

Route: ORAL

Package Size: 120 ML  Package Type: BOTTLE

NDC: 000003092630  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: BRISTOL-MYERS SQUIBB  Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 120 ML  Package Type: BOTTLE

NDC: 000395063516  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: WALMEAD  Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 473 ML  Package Type: BOTTLE

Press return to continue or '^' to exit:

NDC: 000003092630  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: BRISTOL-MYERS SQUIBB  Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 120 ML  Package Type: BOTTLE

NDC: 000395063516  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: WALMEAD  Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 473 ML  Package Type: BOTTLE

Press return to continue or '^' to exit:

NDC: 000395063716  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: WALMEAD  Trade Name: COD LIVER OIL, MINT FLAVORED

Route: ORAL

Package Size: 473 ML  Package Type: BOTTLE

NDC: 000527073427  UPN:

report continues on the next page

**Example 3: NDF Inquiry by CMOP ID Number (cont.)**

VA Product Name: COD LIVER OIL

Manufacturer: LANNETT  Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 473 ML  Package Type: BOTTLE

NDC: 000395063528  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: WALMEAD  Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 3840 ML  Package Type: BOTTLE

NDC: 000527073428  UPN:

VA Product Name: COD LIVER OIL

Manufacturer: LANNETT  Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 3840 ML  Package Type: BOTTLE

Press return to continue or '^' to exit:

#### ### Fixed Medication Copay Tier Enhancements

PSN*4.0*492 contains changes to the *Inquire to National Files* [PSNACT] option to include the display of the new fields.

<!-- image -->

For more information about the new fields, refer to the patch description on Forum for PSN*4.0*492.

**Example 1: Fixed Medication Copay Tier Enhancement by VA Product Name**

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? VA PRODUCT

Select VA PRODUCT NAME: DICLOX

1   DICLOXACILLIN NA 125MG CAP

2   DICLOXACILLIN NA 250MG CAP  Tier 2

3   DICLOXACILLIN NA 500MG CAP

4   DICLOXACILLIN NA 62.5MG/5ML SUSP

CHOOSE 1-4: 2  DICLOXACILLIN NA 250MG CAP

VA Product Name: DICLOXACILLIN NA 250MG CAP

VA Generic Name: DICLOXACILLIN

Dose Form: CAP,ORAL

Strength: 250 Units: MG

National Formulary Name: DICLOXACILLIN CAP,ORAL

VA Print Name: DICLOXACILLIN NA 250MG CAP

**Example 1: Fixed Medication Copay Tier Enhancement by VA Product**

**Name (cont.)**

VA Product Identifier: D0064 Transmit to CMOP: Yes VA Dispense Unit: CAP

PMIS: DICLOXACILLIN – ORAL

Active Ingredients:    DICLOXACILLIN  Strength: 250 Units: MG

Primary VA Drug Class: AM112

Secondary VA Drug Class:

CS Federal Schedule:

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE. National Formulary Restriction:

Copay Tier: 2

Copay Effective Date: APR 1, 2016

Override DF Exclude from Dosage Checks: No

report continues on the next page

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? No

Possible Dosages To Auto-Create: 1x and 2x Possible Dosages

Package: Both Inpatient and Outpatient

Press return to continue or '^' to exit:

NDC: 000005313523  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

Manufacturer: LEDERLE LABS  Trade Name: DICLOXACILLIN

Route: ORAL

Package Size: 100  Package Type: BOTTLE

NDC: 000008036002  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

Manufacturer: WYETH-AYERST  Trade Name: PATHOCIL

Route: ORAL

Package Size: 100  Package Type: BOTTLE

NDC: 0000157893F3  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

Manufacturer: BRISTOL-MYERS SQUIBB   Trade Name: DYNAPEN

Route: ORAL

Package Size: 100  Package Type: BOTTLE

NDC: 000015789360  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

Manufacturer: BRISTOL-MYERS SQUIBB   Trade Name: DYNAPEN

Route: ORAL

Package Size: 100  Package Type: BOTTLE

Press return to continue or '^' to exit:

NDC: 000029635130  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

**Example 1: Fixed Medication Copay Tier Enhancement by VA Product Name (cont.)**

Manufacturer: GLAXO SMITHKLINE  Trade Name: DYCILL

Route: ORAL

Package Size: 100  Package Type: BOTTLE

NDC: 000182150601  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

Manufacturer: IVAX  Trade Name: DICLOXACILLIN SODIUM

Route: ORAL

Package Size: 100  Package Type: BOTTLE

NDC: 000228244310  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

Manufacturer: PUREPAC CORP  Trade Name: DICLOXACILLIN SODIUM

Route: ORAL

Package Size: 100  Package Type: BOTTLE

report continues on the next page

NDC: 000302170001  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

Manufacturer: GENETCO  Trade Name: DICLOXACILLIN SODIUM

Route: ORAL

Package Size: 100  Package Type: BOTTLE

Press return to continue or '^' to exit:

**Example 2: Fixed Medication Copay Tier by (N)DC**

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? ndc  NDC

NDC (N) or UPN (U) ? n  NDC

Enter NDC with or without Dashes (-): 000093312301  89897

...OK? Yes//   (Yes)

NDC: 000093312301  UPN:

VA Product Name: DICLOXACILLIN NA 250MG CAP

Manufacturer: TEVA PHARM  Trade Name: DICLOXACILLIN NA 250MG CAPSULE

Route: ORAL

Package Size: 100  Package Type: BOTTLE

VA Product Name: DICLOXACILLIN NA 250MG CAP

VA Generic Name: DICLOXACILLIN

Dose Form: CAP,ORAL

Strength: 250 Units: MG

National Formulary Name: DICLOXACILLIN CAP,ORAL

VA Print Name: DICLOXACILLIN NA 250MG CAP

VA Product Identifier: D0064 Transmit to CMOP: Yes VA Dispense Unit: CAP

PMIS: DICLOXACILLIN - ORAL

Active Ingredients:    DICLOXACILLIN  Strength: 250 Units: MG

Primary VA Drug Class: AM112

Secondary VA Drug Class:

CS Federal Schedule:

National Formulary Indicator: Yes Formulary Designator: PA-N

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE.

National Formulary Restriction:

**Example 2: Fixed Medication Copay Tier by (N)DC (cont.)**

Copay Tier: 2

Copay Effective Date: APR 1, 2016

Press return to continue or '^' to exit:

**Example 3: Fixed Medication Copay Tier by (C)MOP ID**

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? c  CMOP ID

CMOP ID: D0064  DICLOXACILLIN NA 250MG CAP

report continues on the next page

VA Product Name: DICLOXACILLIN NA 250MG CAP

VA Generic Name: DICLOXACILLIN

Dose Form: CAP,ORAL

Strength: 250 Units: MG

National Formulary Name: DICLOXACILLIN CAP,ORAL

VA Print Name: DICLOXACILLIN NA 250MG CAP

VA Product Identifier: D0064 Transmit to CMOP: Yes VA Dispense Unit: CAP

PMIS: DICLOXACILLIN - ORAL

Active Ingredients:    DICLOXACILLIN  Strength: 250 Units: MG

Primary VA Drug Class: AM112

Secondary VA Drug Class:

CS Federal Schedule:

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: THIS PRODUCT REQUIRED APPROVAL AT THE NATIONAL LEVEL PRIOR TO DISPENSING. SEE PBM CRITERIA FOR USE. National Formulary Restriction:

Copay Tier: 2

Copay Effective Date: APR 1, 2016

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECTS DURATION: NO

Auto-Create Default Possible Dosage? No

Possible Dosages To Auto-Create: 1x and 2x Possible Dosages

Package: Both Inpatient and Outpatient

Maximum Days Supply:

Hazardous to Handle: YES

Hazardous to Dispose: YES

Primary EPA Code: DEA

Waste Sort Code: UPC3

DOT Shipping Name: FLAMMABLE

Press return to continue or '^' to exit:

### Clinical Effects of Drugs

PSN*4*396 added a fields multiple to the VA PRODUCT file (#50.68) at 50.68108.  Fields included are PACKAGE (#.01), OMIT EXP/DC ORDER CHECK (#1) and DURATION LIMIT (#2). The default value of NO will be displayed. These fields will only be populated and displayed if data is present. A future patch will populate the Clinical Effects of Drug field (#108) with other values.

<!-- image -->

For more information about the new fields, refer to the patch description on Forum for PSN*4.0*396.

**Example 1: Clinical Effects of Drug by VA Product Name**

VA Product Name: ATROPINE SO4 0.05MG/ML INJ ***INACTIVE: SEP 28,2007 ***

VA Generic Name: ATROPINE

Dose Form: INJ,SOLN

Strength: 0.05 Units: MG/ML

National Formulary Name: ATROPINE INJ,SOLN

VA Print Name: ATROPINE SULFATE 0.05MG/ML INJ

VA Product Identifier: A0928  Transmit to CMOP: No  VA Dispense Unit: ML

PMIS: None

Active Ingredients:    ATROPINE  Strength: 0.05 Units: MG/ML

Primary VA Drug Class: AU350

Secondary VA Drug Class:

CS Federal Schedule: 0  Unscheduled

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: This product requires approval at the national level

prior to  dispensing.  See PBM Criteria for Use.

National Formulary Restriction:

Copay Tier:

Copay Effective Date:

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

NDC: 000074789701  UPN:

VA Product Name: ATROPINE SO4 0.05MG/ML INJ

Manufacturer: ABBOTT  Trade Name: ATROPINE 0.05MG/ML INJ

Route: INTRAVENOUSINTRAMUSCULARSUBCUTANEOUS

Package Size: 10 X 5 ML  Package Type: SYRINGE

NDC: 000074789715  UPN:

VA Product Name: ATROPINE SO4 0.05MG/ML INJ

Manufacturer: ABBOTT  Trade Name: ATROPINE 0.05MG/ML INJ

Route: INTRAVENOUSINTRAMUSCULARSUBCUTANEOUS

Package Size: 1  Package Type: SYRINGE

This option allows you to lookup NDF file information three ways (VA Product

Name, NDC, or CMOP ID number).

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ?

**Example 2: Clinical Effects of Drug by NDC**

This option allows you to lookup NDF file information three ways (VA Product

Name, NDC, or CMOP ID number).

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? NDC

NDC (N) or UPN (U) ? NDC

Enter NDC with or without Dashes (-): 000074789701  48  ATROPINE SO4 0.05MG/ML I

NJ  09/28/2007

...OK? Yes//   (Yes)

NDC: 000074789701 ***INACTIVE: SEP 28,2007 ***  UPN:

VA Product Name: ATROPINE SO4 0.05MG/ML INJ

Manufacturer: ABBOTT  Trade Name: ATROPINE 0.05MG/ML INJ

Route: INTRAVENOUS INTRAMUSCULAR SUBCUTANEOUS

Package Size: 10 X 5 ML  Package Type: SYRINGE

VA Product Name: ATROPINE SO4 0.05MG/ML INJ ***INACTIVE: SEP 28,2007 ***

VA Generic Name: ATROPINE

Dose Form: INJ,SOLN

Strength: 0.05 Units: MG/ML

National Formulary Name: ATROPINE INJ,SOLN

VA Print Name: ATROPINE SULFATE 0.05MG/ML INJ

VA Product Identifier: A0928  Transmit to CMOP: No  VA Dispense Unit: ML

PMIS: None

Active Ingredients:    ATROPINE  Strength: 0.05 Units: MG/ML

Primary VA Drug Class: AU350

Secondary VA Drug Class:

CS Federal Schedule: 0  Unscheduled

National Formulary Indicator: Yes

Formulary Designator: PA-N

Product Text: This product requires approval at the national level

prior to  dispensing.  See PBM Criteria for Use.

National Formulary Restriction:

Copay Tier:

Copay Effective Date:

Override DF Exclude from Dosage Checks: No

CLINICAL EFFECT DURATION: NO

Auto-Create Default Possible Dosage? Yes

Maximum Days Supply:

This option allows you to lookup NDF file information three ways (VA Product

Name, NDC, or CMOP ID number).

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ?

## Printing a Patient Medication Information Sheet

### Print a PMI Sheet

**[PSNPMIS]   Synonym: PMIS**

This option allows you to print a Patient Medication Information Sheet (PMI).

These medication information sheets can be provided to patients, explaining

how and why to take a medication and the possible side effects. A commercial vendor supplies the information provided in the Patient Medication Information Sheets. This information is updated periodically to provide new medication information sheets and changes to existing sheets.

If the PMI Sheet does not print and the message “Drug is not linked to a valid Medication Information Sheet for language selected” is printed instead, the user should select another language and re-print the medication sheet. If this still does not work, then the user should contact the NDF Manager for further assistance.

**Example: Print a PMI Sheet**

Select National Drug File Menu Option: **PMIS** Print a PMI Sheet

Select DRUG GENERIC NAME: **ACET** &lt;RET&gt;

1   ACETAMINOPHEN 160MG/5ML (TYLENOL) ELIX     CN103         DISP/ML (120ML/BT)

2   ACETAMINOPHEN 160MG/5ML SUGAR-ALC-FREE     CN103     N/F       FOR SPECIAL USE IN SELECT DIABETIC PATIENTS

3   ACETAMINOPHEN 160MG/5ML UNIT DOSE CUP      CN103         (TK) INPATIENT USE ONLY. AVAILABLE 10ML/CUP

4   ACETAMINOPHEN 325MG (NONRENEWABLE) 12'S    CN103         CHOOSE ONLY TO REFLECT ACUTE CARE DISPENSING

5   ACETAMINOPHEN 325MG (TYLENOL) TAB          CN103         CMOP DISP/MULT 100'S

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **5** ACETAMINOPHEN 325MG (TYLENOL) TAB    CN103         CMOP DISP/MULT 100'S

Select DRUG GENERIC NAME: **&lt;RET&gt;**

Select one of the following:

1    English

2    Spanish

Select Language : **1** English

How many copies? :  (1-100): 1// **&lt;RET&gt;**

DEVICE: *[Select Print Device]*

example continues on the next page

**Example: Print a PMI sheet (cont.)**

Medication instructions for ACETAMINOPHEN 325MG (TYLENOL) TAB      Page 1

**IMPORTANT NOTE** :  The following information is intended to supplement,

not substitute for, the expertise and judgment of your physician, pharmacist or

other healthcare professional. It should not be construed to indicate that use

of the drug is safe, appropriate, or effective for you. Consult your healthcare

professional before using this drug.

**ACETAMINOPHEN - ORAL** (uh-seet-uh-MEE-no-fen)

**COMMON BRAND NAME(S)** : APAP, Liquiprin, Panadol, Tylenol

**USES** :  This drug is used to relieve mild to moderate pain and to reduce

fever.

**HOW TO USE** :  Take this medication as directed. Do not take more than

recommended. Do not use for more than 10 days without consulting your doctor.

This medication is not to be given to children under 3 years of age without

your doctor's approval.

**SIDE EFFECTS** :  When taken as directed, most people experience little or

no side effects with this medication.    Tell your doctor immediately if any of

these highly unlikely but very serious side effects occur: easy bruising or

bleeding, persistent sore throat or other signs of infection.    In the

unlikely event you have an allergic reaction to this drug, seek medical

attention immediately. Symptoms of an allergic reaction include: rash, itching,

swelling, dizziness, trouble breathing.    If you notice other effects not

listed above, contact your doctor or pharmacist.

**PRECAUTIONS** :  If you have any of the following health problems, consult

your doctor before using this medication: severe liver disease, alcohol

dependency, any allergies.    Acetaminophen may cause liver damage. Daily use

of alcohol, especially when combined with acetaminophen, may increase your risk

for liver damage. Check with your doctor or pharmacist for more information.

Acetaminophen is often used instead of aspirin. They are equally effective in

relieving pain; however, acetaminophen does not reduce swelling and

inflammation like aspirin does.    There are many brands and forms of

acetaminophen on the market. Read the dosing instructions carefully as the

amount of acetaminophen may vary among products.    Acetaminophen appears to be

safe for use during pregnancy. Use only if clearly needed.    Acetaminophen is

found in breast milk, but side effects in nursing infants have not been

reported. Consult your doctor if you are breast-feeding.

**DRUG INTERACTIONS** :  Tell your doctor of all nonprescription and

prescription drugs you use especially: isoniazid, phenobarbital, phenytoin,

zidovudine, sulfinpyrazone.    Check the labels on all your medicines because

they may also contain acetaminophen. Ask your pharmacist about the safe use of

those products.    Do not start or stop any medicine without doctor or

pharmacist approval.

**OVERDOSE** :  If overdose is suspected, contact your local poison control

center or emergency room immediately. Symptoms of overdose may include

vomiting, excessive sweating, dark urine, stomach pain, and extreme fatigue.

example continues on the next page

**Example: Print a PMI sheet (cont.)**

**NOTES** :  Acetaminophen does not cause the stomach and intestinal ulcers

that aspirin and aspirin-like NSAIDs (e.g., ibuprofen, ketoprofen) may cause.

**MISSED DOSE** :  If you miss a dose, take as soon as remembered; do not

take if it is almost time for the next dose, instead, skip the missed dose and

resume your usual dosing schedule. Do not "double-up" the dose to catch up.

**STORAGE** :  Store at room temperature between 59 and 86 degrees F

(between 15 and 30 degrees C) away from moisture and sunlight. Do not store in

the bathroom. Do not freeze liquid forms.

Select DRUG GENERIC NAME: **&lt;RET&gt;**

Select National Drug File Menu Option: **&lt;RET&gt;**

## Displaying an FDA Medication Guide

### Display FDA Medication Guide

**[PSN MED GUIDE]   Synonym: FDA**

This option allows you to display a Food and Drug Administration (FDA) Medication Guide.

Medication guides are paper handouts that come with many prescription medicines. These guides address issues that are specific to particular drugs and drug classes, and they contain FDA approved information that can help patients avoid serious adverse events. The FDA requires that medication guides be issued with certain prescribed drugs and biological products when the agency determines that: certain information is necessary to prevent serious adverse effect; patient decision-making should be informed by information about a known serious side effect with a product; or patient adherence to directions for the use of a product are essential to its effectiveness.

The system allows the user to select the appropriate document through the generic drug name. If there is no associated medication guide, the system shall inform the user and allow the user to select another drug.

If there is no medication guide associated with the medication, the message: “There is no FDA Medication Guide associated with this medication” is displayed.

**Example 1:** When a VA Product does not have a Medication Guide Associated:

Select OPTION NAME: PSNMGR       National Drug File Menu

WELCOME TO THE NATIONAL DRUG FILE


REMA   Rematch / Match Single Drugs

VER    Verify Matches

SVER   Verify Single Match

MERG   Merge National Drug File Data Into Local File

AUTO   Automatic Match of Unmatched Drugs

CLAS   Allow Unmatched Drugs To Be Classed

RPRT   National Drug File Reports Menu ...

INQ    Inquiry Options ...

PMIS   Print a PMI Sheet

FDA    Display FDA Medication Guide

PPS    PPS-N Menu ...

Select National Drug File Menu Option: FDA  Display FDA Medication Guide

Select VA PRODUCT NAME: METOPROLOL

1   METOPROLOL SUCCINATE 100MG 24HR CAP,SPRINKLE,SA

2   METOPROLOL SUCCINATE 100MG TAB,SA

3   METOPROLOL SUCCINATE 200MG 24HR CAP,SPRINKLE,SA

4   METOPROLOL SUCCINATE 200MG TAB,SA

5   METOPROLOL SUCCINATE 25MG 24HR CAP,SPRINKLE,SA

Press &lt;Enter&gt; to see more, '^' to exit this list,  OR

CHOOSE 1-5: 2  METOPROLOL SUCCINATE 100MG TAB,SA

There is no FDA Medication Guide associated with this medication.

Enter RETURN to continue or '^' to exit:

If a Medication Guide exists, a URL link will display for the user to copy/paste into a browser to retrieve it.

**Example 2:** When a VA Product has a Medication Guide Associated:

Select OPTION NAME: PSNMGR       National Drug File Menu

WELCOME TO THE NATIONAL DRUG FILE


REMA   Rematch / Match Single Drugs

VER    Verify Matches

SVER   Verify Single Match

MERG   Merge National Drug File Data Into Local File

AUTO   Automatic Match of Unmatched Drugs

CLAS   Allow Unmatched Drugs To Be Classed

RPRT   National Drug File Reports Menu ...

INQ    Inquiry Options ...

PMIS   Print a PMI Sheet

FDA    Display FDA Medication Guide

PPS    PPS-N Menu ...

Select National Drug File Menu Option: FDA  Display FDA Medication Guide

Select VA PRODUCT NAME: IBUPROFEN

1   IBUPROFEN 10% CREAM,KIT       JAN 22, 2016

2   IBUPROFEN 100MG TAB

3   IBUPROFEN 100MG TAB,CHEW

4   IBUPROFEN 100MG/5ML SUSP,BTL,5ML

5   IBUPROFEN 100MG/5ML SUSP,ORAL

Press &lt;Enter&gt; to see more, '^' to exit this list,  OR

CHOOSE 1-5: 2  IBUPROFEN 100MG TAB

The following URL provides the link to the FDA Medication Guide associated

with this medication. Copy/paste the URL below into a browser to access

the FDA Medication Guide for this drug:

file://REDACTED/PBM/Workgroup/VistA\_MedGuides/NSAIDs\_(Class)\_(2022).pdf

Enter RETURN to continue or '^' to exit:

## PPS-N Menu

This sub-menu contains all PPS-N options in the National Drug File package.

SD     Schedule download of NDF update file

SI     Schedule Install of NDF Update file

MD     Manual Download of NDF Update file

MI     Manual Install of NDF Update file

RJ     Reject/Complete of NDF Update file

SP     PPS-N Site Parameters (Enter/Edit)

VC     Vista Comparison Report

DIS    Download/Install Status Report

SSH    Manage Secure Shell (SSH) Keys

### Schedule download of NDF update file

**[PSN PPS SCHEDULE DOWNLOAD]   Synonym: SD**

This option allows you to schedule the download for the Pharmacy Product System – National (PPS-N) NDF Update files.  The scheduled background job can be created to run weekly or daily at a specific time.

<!-- image -->

Before scheduling a download, the PPS-N Site Parameters and the Secure Shell (SSH) keys must be defined.

There can only be one scheduled job to download the PPS-N Update files.  When you select this option and change the schedule, the old job will be deleted and a new one will be created.  The scheduled job name is PSN TASK SCHEDULED DOWNLOAD.

If a job is scheduled, it will be displayed under “Scheduled downloads are:” section (Example 2 below).  If there is not a scheduled job, nothing will display (Example 1).

The process of downloading an update file does not impact users currently using VistA and can be done at any time.

**Example 1:** **Scheduling a weekly download**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: SD  Schedule download of NDF update file

This option allows you to schedule a recurring TaskMan job to

perform the NDF update file download from PPS-N.

Warning! This download should be scheduled during non-peak hours.

You will need to select a date/time and how often this download should reoccur.

Do you want to schedule an automatic NDF download in TaskMan? NO// YES

Enter date/time: ?

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T   (for TODAY),  T+1 (for TOMORROW),  T+2,  T+7,  etc.

T-1 (for YESTERDAY),  T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer assumes a date in the FUTURE.

If only the time is entered, the current date is assumed.

Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc.

You may enter a time, such as NOON, MIDNIGHT or NOW.

You may enter   NOW+3'  (for current date and time Plus 3 minutes

*Note--the Apostrophe following the number of minutes)

Enter a date which is greater than or equal to NOV 15, 2017@08:52:02.

Enter date/time: T@10A  (NOV 15, 2017@10:00)

Should this download be re-scheduled at the same time weekly? NO// ??

Please enter Y or N.

Should this download be re-scheduled at the same time weekly? NO// YES

Your start time is:  (NOV 15, 2017@10:05)

The download will automatically be re-scheduled Weekly

Press ENTER to Continue:

**Example 2:** **Scheduling a daily download**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: SD  Schedule download of NDF update file

This option allows you to schedule a recurring TaskMan job to

perform the NDF update file download from PPS-N.

Warning! This download should be scheduled during non-peak hours.

You will need to select a date/time and how often this download should reoccur.

Scheduled Downloads are:

-----------------------

6264759  NOV 15, 2017@10:05  7D

Do you want to schedule an automatic NDF download in TaskMan? NO// YES

Enter date/time: T@10P  (NOV 15, 2017@22:00)

Should this download be re-scheduled at the same time weekly? NO// NO

Should this download be re-scheduled at the same time daily? NO//  YES

Your start time is:  (NOV 15, 2017@22:06)

The download will automatically be re-scheduled Daily

Press ENTER to Continue:

**Example 3:** **Scheduling a one-time download**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: SD  Schedule download of NDF update file

This option allows you to schedule a recurring TaskMan job to

perform the NDF update file download from PPS-N.

Warning! This download should be scheduled during non-peak hours.

You will need to select a date/time and how often this download should reoccur.

Scheduled Downloads are:

-----------------------

6264759  NOV 15, 2017@10:05  7D

Do you want to schedule an automatic NDF download in TaskMan? NO// YES

Enter date/time: T@10P  (NOV 15, 2017@22:00)

Should this download be re-scheduled at the same time weekly? NO// NO

Should this download be re-scheduled at the same time daily? NO//

Warning! The download you have scheduled will occur only once.

Your start time is:  (NOV 15, 2017@22:05)

The download will NOT automatically be re-scheduled

Press ENTER to Continue:

**Note:**

Time and Frequency of this Task can be viewed by going back into the same option and not making any changes. It can also be viewed under kernel option:

Schedule/Unschedule Options [ XUTM SCHEDULE] and selecting option “PSN TASK SCHEDULED DOWNLOAD”

### Schedule Install of NDF Update file

**[PSN PPS SCHEDULE INSTALL]   Synonym: SI**

This option allows you to schedule install for the Pharmacy Product System – National (PPS-N) NDF Update files.  The scheduled background job can be created to run weekly or daily at a specific time.

<!-- image -->

Before scheduling an install, the PPS-N Site Parameters and the Secure Shell (SSH) keys must be defined.  In addition, the scheduled install will need to be scheduled an hour after the scheduled download.  This gives time for the download to finish.

There can only be one scheduled job to install the PPS-N Update files.  When you select this option and change the schedule, the old job will be deleted and a new one will be created.  The scheduled job name is PSN TASK SCHEDULED INSTALL.

If a job is scheduled, it will be displayed under the “Scheduled installs are:” section (Example 2 below).  If there is not a scheduled job, nothing will display (Example 1).

Scheduling an install will impact users currently using the Pharmacy VistA applications and will need to be schedule during off peak hours.

**Example 1:** **Scheduling a weekly install**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: SI  Schedule Install of NDF Update file

This option allows you to schedule a recurring TaskMan job to perform the NDF

update installation from PPS-N.

Warning! This NDF update install should be scheduled during non-peak hours.

You will need to select a date/time and how often this update should reoccur.

Do you want to schedule an automatic NDF update install in TaskMan? NO// ??

Please enter Y or N.

Do you want to schedule an automatic NDF update install in TaskMan? NO// YES

Enter date/time: T+1@1a  (NOV 16, 2017@01:00)

Should this NDF update install be re-scheduled at the same time weekly? NO// y

YES

Your start time is:  (NOV 16, 2017@01:05)

The NDF update install will automatically be re-scheduled Weekly

Press ENTER to Continue:

**Example 2:** **Scheduling a daily install**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: si  Schedule Install of NDF Update file

This option allows you to schedule a recurring TaskMan job to perform the NDF

update installation from PPS-N.

Warning! This NDF update install should be scheduled during non-peak hours.

You will need to select a date/time and how often this update should reoccur.

Scheduled Installs are:

-----------------------

6265150  NOV 16, 2017@01:05  7D

Do you want to schedule an automatic NDF update install in TaskMan? NO// YES

Enter date/time: T+1@2A  (NOV 16, 2017@02:00)

Should this NDF update install be re-scheduled at the same time weekly? NO// NO

Should this NDF update install be re-scheduled at the same time daily? NO// YES

Your start time is:  (NOV 16, 2017@02:05)

The NDF update install will automatically be re-scheduled Daily

Press ENTER to Continue:

**Example 3:** **Scheduling a one-time install**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: SI  Schedule Install of NDF Update file

This option allows you to schedule a recurring TaskMan job to perform the NDF

update installation from PPS-N.

Warning! This NDF update install should be scheduled during non-peak hours.

You will need to select a date/time and how often this update should reoccur.

Scheduled Installs are:

-----------------------

6265154  NOV 16, 2017@02:05  1D

Do you want to schedule an automatic NDF update install in TaskMan? NO// YES

Enter date/time: T+1@3A  (NOV 16, 2017@03:00)

Should this NDF update install be re-scheduled at the same time weekly? NO//

Should this NDF update install be re-scheduled at the same time daily? NO//

Warning! The NDF update install you have scheduled will occur only once.

Your start time is:  (NOV 16, 2017@03:05)

The NDF update install will NOT automatically be re-scheduled

Press ENTER to Continue:

**Note:**

Time and Frequency of this Task can be viewed by going back into the same option and not making any changes. It can also be viewed under kernel option:

Schedule/Unschedule Options [ XUTM SCHEDULE] sand selecting option “PSN TASK SCHEDULED INSTALL”

### Manual Download of NDF Update file

**[PSN PPS MANUAL DOWNLOAD]   Synonym: MD**

This option will start the download of any new NDF update files from PPS-N.

**Example 1: D** **ownload non-existing NDF data file PPS\_30PRV\_31NEW.DAT’**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: MD  Manual Download of NDF Update file

> **WARNING:** This download should only be done during off peak hours!

Are you sure you want to immediately start an NDF update download? NO// YES

Please stand-by NDF update download may take up to 30 minutes...

Beginning download for Update file name: PPS\_30PRV\_31NEW.DAT

Server ping successful 3-LINUX rc=1

This  U.S.  Government  system  is  intended  for  official  and  authorized

use  only by  authorized  users with no reasonable  expectation of  privacy.

The system  may  include  records  protected  by  various  Federal  statutes

including  the  Privacy  Act (5 U.S.C. ' 552a)  and  38 U.S.C. ''  5701  and

7332.  Access to data  is on  a need-to-know  basis  only.  All use  of this

system  constitutes user  understanding of  unconditional  consent to review

and action including (but not limited to)  monitoring,  recording,  copying,

auditing, inspecting, investigating, restricting access, blocking, tracking,

disclosing to authorized personnel, or any other authorized  actions  by all

authorized VA and  law  enforcement  personnel.  Unauthorized  access  to or

misuse of this  system is strictly prohibited may result in criminal, civil,

or administrative penalties.

**Couldn't stat remote file: No such file or directory**

**File "/u02/pps-n/dev/app82/approved/PPS\_30PRV\_31NEW.DAT" not found.**

**Example 2:** **Download existing NDF data file ‘PPS\_30PRV\_31NEW.DAT’**

Select PPS-N Menu Option: **MD** Manual Download of NDF Update file

> **WARNING:** This download should only be done during off peak hours!

Are you sure you want to immediately start an NDF update download? NO// YES

Please stand-by NDF update download may take up to 30 minutes...

Beginning download for Update file name: PPS\_30PRV\_31NEW.DAT

Server ping successful 3-LINUX rc=1

This  U.S.  Government  system  is  intended  for  official  and  authorized

use  only by  authorized  users with no reasonable  expectation of  privacy.

The system  may  include  records  protected  by  various  Federal  statutes

including  the  Privacy  Act (5 U.S.C. ' 552a)  and  38 U.S.C. ''  5701  and

7332.  Access to data  is on  a need-to-know  basis  only.  All use  of this

system  constitutes user  understanding of  unconditional  consent to review

and action including (but not limited to)  monitoring,  recording,  copying,

auditing, inspecting, investigating, restricting access, blocking, tracking,

disclosing to authorized personnel, or any other authorized  actions  by all

authorized VA and  law  enforcement  personnel.  Unauthorized  access  to or

misuse of this  system is strictly prohibited may result in criminal, civil,

or administrative penalties.

file transfer successful 3-LINUX rc=1

**Completed download for: PPS\_30PRV\_31NEW.DAT**

Continuing with the next file sequence. Attempting download

for: PPS\_32PRV\_33NEW.DAT

Server ping successful 3-LINUX rc=1

This  U.S.  Government  system  is  intended  for  official  and  authorized

use  only by  authorized  users with no reasonable  expectation of  privacy.

The system  may  include  records  protected  by  various  Federal  statutes

including  the  Privacy  Act (5 U.S.C. ' 552a)  and  38 U.S.C. ''  5701  and

7332.  Access to data  is on  a need-to-know  basis  only.  All use  of this

system  constitutes user  understanding of  unconditional  consent to review

and action including (but not limited to)  monitoring,  recording,  copying,

auditing, inspecting, investigating, restricting access, blocking, tracking,

disclosing to authorized personnel, or any other authorized  actions  by all

authorized VA and  law  enforcement  personnel.  Unauthorized  access  to or

misuse of this  system is strictly prohibited may result in criminal, civil,

or administrative penalties.

Couldn't stat remote file: No such file or directory

File "/u02/pps-n/dev/app82/approved/PPS\_32PRV\_33NEW.DAT" not found.

#### ### Manual Install of NDF Update file

**[PSN PPS MANUAL INSTALL]   Synonym: MI**

Using this option, you can immediately begin the process that checks for any PPS-N update files that are available and, if valid, update your VistA NDF files. Normally, this process should be executed during off-peak hours to ensure that users are not using the Pharmacy VistA applications.

**Example 1: No data files to be installed**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: MI  Manual Install of NDF Update file

> **WARNING:** The NDF update should only be done during off duty hours!

Installation may take up to 30 minutes, and the following options

will automatically be disabled during installation then enabled

once installation has completed.

* Print A PMI Sheet      * Patient Prescription Processing

* Release Medication     * Reprint an Outpatient Rx Label

Are you sure you want to immediately begin an NDF Update? NO// YES

The following PPS-N/NDF Update file(s) are available for install:

There are no files to install.

Enter to continue...

**Example 2: Installation of all data files**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: MI  Manual Install of NDF Update file

> **WARNING:** The NDF update should only be done during off duty hours!

Installation may take up to 30 minutes, and the following options

will automatically be disabled during installation then enabled

once installation has completed.

* Print A PMI Sheet      * Patient Prescription Processing

* Release Medication     * Reprint an Outpatient Rx Label

Are you sure you want to immediately begin an NDF Update? NO// YES

The following PPS-N/NDF Update file(s) are available for install:

1)     PPS\_30PRV\_31NEW.DAT

2)     PPS\_31PRV\_32NEW.DAT

The files must be installed in sequential order and take around

30 minutes each to install. Pharmacy will be down for that period

of time.  Do you want to install just the first one or all of them?

(F)irst file only or (A)ll files: A

Please stand-by NDF update processing can take around 30 minutes...

> **WARNING:** File has already been installed.

Do you want to proceed with the installation? YES//

Beginning install for PPS\_30PRV\_31NEW.DAT

Background monitoring started:   (NOV 16, 2017@09:09:20)

Importing the Update file into VistA...

Parsing the data...

Disabling mandatory options... NOV 16,2017@08:05:03

Disabling user defined Scheduled Options...

Disabling user defined Menu Options...

Disabling user defined Protocols...

Storing PMI data...

Storing data into the rest of the NDF files...

Sending mail messages...

Beginning un-match/re-match to local drug file...

Generating mail messages for unmatched/re-matched drugs...

Validating cross references...

Enabling options...NOV 16,2017@08:05:17

Enabling user defined Scheduled Options...

Enabling user defined Menu Options...

Enabling user defined Protocols...

Options and protocols enabled: NOV 16,2017@08:05:17

Processing Interactions...

Processing allergies...

Sending install completion message to PPS-N...

Installation completed.

**Beginning install for PPS\_31PRV\_32NEW.DAT**

Background monitoring started:   (NOV 16, 2017@09:10:32)

Importing the Update file into VistA...

Parsing the data...

Disabling mandatory options... NOV 16,2017@08:06:15

Disabling user defined Scheduled Options...

Disabling user defined Menu Options...

Disabling user defined Protocols...

Storing PMI data...

Storing data into the rest of the NDF files...

Sending mail messages...

Beginning un-match/re-match to local drug file...

Generating mail messages for unmatched/re-matched drugs...

Validating cross references...

Enabling options...NOV 16,2017@08:06:29

Enabling user defined Scheduled Options...

Enabling user defined Menu Options...

Enabling user defined Protocols...

Options and protocols enabled: NOV 16,2017@08:06:29

Processing Interactions...

Processing allergies...

Sending install completion message to PPS-N...

Installation completed.

**Example 3: Installation of first data files**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: MI  Manual Install of NDF Update file

> **WARNING:** The NDF update should only be done during off duty hours!

Installation may take up to 30 minutes, and the following options

will automatically be disabled during installation then enabled

once installation has completed.

* Print A PMI Sheet      * Patient Prescription Processing

* Release Medication     * Reprint an Outpatient Rx Label

Are you sure you want to immediately begin an NDF Update? NO// YES

The following PPS-N/NDF Update file(s) are available for install:

1)     PPS\_30PRV\_31NEW.DAT

2)     PPS\_31PRV\_32NEW.DAT

The files must be installed in sequential order and take around

30 minutes each to install. Pharmacy will be down for that period

of time.  Do you want to install just the first one or all of them?

(F)irst file only or (A)ll files: F

Please stand-by NDF update processing can take around 30 minutes...

> **WARNING:** File has already been installed.

Do you want to proceed with the installation? YES//

Beginning install for PPS\_30PRV\_31NEW.DAT

Background monitoring started:   (NOV 16, 2017@09:09:20)

Importing the Update file into VistA...

Parsing the data...

Disabling mandatory options... NOV 16,2017@08:05:03

Disabling user defined Scheduled Options...

Disabling user defined Menu Options...

Disabling user defined Protocols...

Storing PMI data...

Storing data into the rest of the NDF files...

Sending mail messages...

Beginning un-match/re-match to local drug file...

Generating mail messages for unmatched/re-matched drugs...

Validating cross references...

Enabling options...NOV 16,2017@08:05:17

Enabling user defined Scheduled Options...

Enabling user defined Menu Options...

Enabling user defined Protocols...

Options and protocols enabled: NOV 16,2017@08:05:17

Processing Interactions...

Processing allergies...

Sending install completion message to PPS-N...

Installation completed.

**Example 4: Installation, when there is one data file**

Select PPS-N Menu &lt;FLD DDEV&gt; Option: MI  Manual Install of NDF Update file

> **WARNING:** The NDF update should only be done during off duty hours!

Installation may take up to 30 minutes, and the following options

will automatically be disabled during installation then enabled

once installation has completed.

* Print A PMI Sheet      * Patient Prescription Processing

* Release Medication     * Reprint an Outpatient Rx Label

Are you sure you want to immediately begin an NDF Update? NO// YES

The following PPS-N/NDF Update file(s) are available for install:

1)     PPS\_32PRV\_33NEW.DAT

Please stand-by NDF update processing can take around 30 minutes...

> **WARNING:** File has already been installed.

Do you want to proceed with the installation? YES//

Beginning install for PPS\_32PRV\_33NEW.DAT

Background monitoring started:   (NOV 16, 2017@09:02:08)

Importing the Update file into VistA...

Parsing the data...

Disabling mandatory options... NOV 16,2017@07:57:51

Disabling user defined Scheduled Options...

Disabling user defined Menu Options...

Disabling user defined Protocols...

Storing PMI data...

Storing data into the rest of the NDF files...

Sending mail messages...

Beginning un-match/re-match to local drug file...

Generating mail messages for unmatched/re-matched drugs...

Validating cross references...

Enabling options...NOV 16,2017@07:58:14

Enabling user defined Scheduled Options...

Enabling user defined Menu Options...

Enabling user defined Protocols...

Options and protocols enabled: NOV 16,2017@07:58:14

Processing Interactions...

Processing allergies...

Sending install completion message to PPS-N...

Installation completed.

### TaskMan scheduled install verify of data file

**[PSN PPS INSTALL VERIFY]**

This option runs automatically by the NDF data file install process and is used to verify and monitor installation. If installation is not completed within an hour, it will send the following error message to the holders of the PSNMGR security key,  as well as to the primary and secondary PPS-N Mail Group  fields defined under the PPS-N Site Parameters (Enter/Edit) [PSN PPS PARAM] option.

**Example:**

<!-- image -->

### Reject/Complete of NDF Update file

**[PSN PPS REJECT FILE]   Synonym: RJ**

This option is used by SQA to identify installation problems in the National VistA account before the file is released nationally. Local VistA users will only have access to send completion messages for the compliance report in PPS-N.

If the site is set (field 10 in the PPS-N Site Parameters (Enter/Edit) option) as PRODUCTION, PRODUCT SUPPORT, and TEST ACCOUNT then this option can only be used to send COMPLETE messages to the PPS-N server, or in the event that PPS-N did not get a complete message during installation.

**Example 1: Send complete message to PPS-N server.**

Select PPS-N Menu &lt;TEST ACCOUNT&gt; Option: RJ  Reject/Complete of NDF Update file

Enter the PPS-N data file name to be Updated: PPS\_57PRV\_58NEW.DAT

Complete message was sent to PPS-N. File should be approved/rejected

in PPS-N side.

Press Return to Continue:

### PPS-N Site Parameters (Enter/Edit)

**[PSN PPS PARAM]   Synonym: SP**

This option is used to create or update site parameters for the Pharmacy Product System - National (PPS-N).

The option is intended to be used by the Pharmacy ADPAC to correctly enter the PPS-N Site parameters used for the communication with the PPS-N server for downloading and installing National Drug file data.

<!-- image -->

The *PPS-N Site Parameters (Enter/Edit)* [PSN PPS PARAM] option requires the ‘PSN PPS ADMIN’ Security Key for editing the parameters.

Select PPS-N Menu &lt;FLD DDEV&gt; Option: SP  PPS-N Site Parameters (Enter/Edit)

Pharmacy Product System-National(PPS-N) Site Parameters

-------------------------------------------------------------------------------

1.  PPS-N Install Version       : 29

2.  PPS-N Download Version      : 29

3. *Open VMS Local Directory    : USER$:[ABC]

4. *Unix/Linux Local Directory  : /xxx/xxxxxx/xxx/xxxx/xxxx/xxx/PPSN/

5. *Remote Server Address       : xxxxxxxxxxxxxxxx.aac.va.gov

6. *Remote Server Directory     : /xxxxx/xxxxxxx/xxxxxxxxx/xxxxx/approved

7. *Remote SFTP Username        : xxxxxxxx

8.  Primary PPS-N Mail Group    : local\_outlook\_mail\_GROUP@va.gov

9.  Secondary PPS-N Mail group  : FIRST.LAST@VA.GOV

10. *PPS-N Account Type          : P - Production

11. *Legacy Update Processing    : NO

12. *Download Status             : NOT IN PROGRESS

13. *Install Status              : NOT IN PROGRESS

14.  Disable Menus, Options, etc :

15. *ECDSA/EDDSA keys            : NOT ALLOWED

-------------------------------------------------------------------------------

Select field number to Edit:

<!-- image -->

An '*' (asterisk) before the field name indicates that PSN PPS COORD security key is required for editing these fields/parameters.

Field description of the *PPS-N Site Parameters (Enter/Edit) screen:*

**Install Version Number:**

This field contains the current version number of the last successful Pharmacy Product System - National (PPS-N) Update file that was last installed.  For example if the last PPS-N Update file installed was PPS\_25PRV\_26NEW.DAT, this field would contain 26.  When sites are brought on line with PPS-N, this parameter should equate to the last update file created by PPS-N at the time of configuration.

**Download Version Number:**

This field contains the version number for the last Pharmacy Product System - National (PPS-N) Update file downloaded.   For example if the last PPS-N Update file downloaded was PPS\_25PRV\_26NEW.DAT, this field would contain 26.  When sites are brought on line with PPS-N, this parameter should equate to the last update file created by PPS-N at the time of configuration.

**OpenVMS Local Directory:**

This field should only be defined for sites that run on OpenVMS operating system.  The example display above shows both OpenVMS and Linux.  This field contains the full path directory structure of where the PPS-N update file will be located (e.g., USER$:[SFTP.PPSN]).

**Unix/Linux Local Directory:**

This field should only be defined for sites that run on a Linux operating system.  The example display above shows both OpenVMS and Linux. This field contains the name of the local Unix/Linux secure directory where the Pharmacy Product System - National (PPS-N) Update file will be stored on the local system after download from the PPS-N server (e.g. /user/sftp/PPSN/).  The option may prompt you for the following after enter the data and press  &lt;Enter&gt; through it:

The directory above could not be found.

Would you like to create it now? N//

Answer **YES.**

**Remote Server Address:**

This is the secure FTP IP address of the Pharmacy Product System-National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

**Remote Server Directory:**

This is the directory name at the Pharmacy Product System-National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

**Remote SFTP User ID:**

This field contains the secure FTP username at the Pharmacy Product System – National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

**Primary PPS-N Mail Group:**

Sites can set up an Outlook mail group consisting of individuals who need to receive notifications generated during PPS-N Update file processing.  Holders of the PSNMGR key will continue to receive email notifications, but the Outlook mail group gives flexibility.  The Outlook mail group will need to be defined in the *PPS-N Site Parameters (Enter/Edit)* [PSN PPS PARAM] option.

This field is used to store the MS Outlook email group or individual Outlook email address that will receive a copy of the PPS-N update messages.  These messages include download and install information, Data Update for NDF report message, Updated Interactions and FDA Med Guide, Drugs Unmatched from National Drug file, Local Drugs Re-matched to NDF, and error messages.  The Interactions and Allergies Updated email report will not be sent to Outlook email as it contains patient information.  All users that hold the PSNMGR security key will continue to receive the report emails via MailMan.

**Secondary PPS-N Mail group:**

This field is used to store the secondary MS Outlook email group that will receive a copy of the PPS-N update messages.  These messages include download and install information, Data Update for NDF report message, Updated Interactions and FDA Med Guide, Drugs Unmatched from National Drug file, Local Drugs Re-matched to NDF, and error messages.  The Interactions and Allergies Updated email report will not be sent to Outlook email as it contains patient information.  All users that hold the PSNMGR security key will continue to receive the report emails via MailMan.

**PPS-N Account Type:**

This field defines the type of Pharmacy Product System - National (PPS-N) account.  The account type can be one of the following: "Q" for National Test SQA system, "T" for Test/Mirror Account, "S" for Product Support, "N" for QA NDFMS account, or "P" for Production account. Local VA sites will use "P" for their production accounts and "T" for their test/mirror accounts.

**Legacy Update:**

This field denotes YES or NO if the National Drug File will be updated by the legacy FORUM patch release process or the PPS-N 3.0 Update process.  When NO is entered, sites will not be allowed to install patches from legacy FORUM patch process.  Only PPS-N update files will be allowed.

**Download Status:**

This field is used to track the status of a PPS-N/NDF Update file download from the PPS-N sftp server.

**Install Status:**

This field is used to track the status of a PPS-N/NDF Update file install into the National Drug file package.

**DISABLE Scheduled Options, Menu Options and Protocols:**

Under this field, the site will select scheduled options, menu options, and protocols that needs be marked out of order during the data file installation process.

**ECDSA keys:**

This field is used to allow the creation of the ECDSA keys.  If this parameter is set to NOT ALLOWED users will not have the option of creating  ECDSA keys under option Manage Secure Shell (SSH) Keys.

### Vista Comparison Report

**[PSN PPS VISTA COMPARISON RPT]   Synonym: VC**

This option allows the user to view or print a report of the NDF changes for a date range.  This report is meant for National SQA use but if a site wants to utilize this report they will need to turn auditing on for the NDF files.  This was not done programmatically to leave the decision up to the site if they want to turn auditing on for all fields, but doing so would increase disk space usage.  The following example shows how to turn auditing on for fields within a file.  For multiple fields, you must list each out to see if the fields are audited.  Note that word processing fields cannot be audited.  The files utilized for NDF are:

50.416   DRUG INGREDIENTS

50.6     VA GENERIC

50.605   VA DRUG CLASS

50.606   DOSAGE FORM

50.607   DRUG UNITS

50.608   PACKAGE TYPE

50.609   PACKAGE SIZE

50.64    VA DISPENSE UNIT

50.67    NDC/UPN

50.68    VA PRODUCT

55.95    DRUG MANUFACTURER

56       DRUG INTERACTION

Auditing might be turned on for some of the files, however, for full utilization of the new option you would need to turn auditing on for all fields.

VA FileMan 22.0

Select OPTION: OTHER OPTIONS

Select OTHER OPTION: ??

Choose from:

1            FILEGRAMS

2            ARCHIVING

3            AUDITING

4            SCREENMAN

5            STATISTICS

6            EXTRACT DATA TO FILEMAN FILE

7            DATA EXPORT TO FOREIGN FORMAT

8            IMPORT DATA

9            BROWSER

Select OTHER OPTION: AUDITING

Select AUDIT OPTION: ??

Choose from:

1            FIELDS BEING AUDITED

2            DATA DICTIONARIES BEING AUDITED

3            PURGE DATA AUDITS

4            PURGE DD AUDITS

5            TURN DATA AUDIT ON/OFF

Select AUDIT OPTION: 5  TURN DATA AUDIT ON/OFF

AUDIT FROM WHAT FILE: VA PRODUCT// 50.68  VA PRODUCT  (27674 entries)

Select FIELD: ??

Choose from:

.01          NAME   y

.05          VA GENERIC NAME   y

1            DOSAGE FORM   y

2            STRENGTH   y

3            UNITS   y

4            NATIONAL FORMULARY NAME   y

5            VA PRINT NAME   y

6            VA PRODUCT IDENTIFIER   y

7            TRANSMIT TO CMOP   y

8            VA DISPENSE UNIT   y

11           GCNSEQNO   n

12           PREVIOUS GCNSEQNO   n

13           NDC LINK TO GCNSEQNO   y

14           ACTIVE INGREDIENTS  (multiple)

15           PRIMARY VA DRUG CLASS   y

16           SECONDARY VA DRUG CLASS  (multiple)

17           NATIONAL FORMULARY INDICATOR   y

19           CS FEDERAL SCHEDULE   y

20           SINGLE/MULTI SOURCE PRODUCT   y

21           INACTIVATION DATE   y

23           EXCLUDE DRG-DRG INTERACTION CK   y

25           MAX SINGLE DOSE   y

26           MIN SINGLE DOSE   y

27           MAX DAILY DOSE   y

28           MIN DAILY DOSE   y

29           MAX CUMULATIVE DOSE   y

30           DSS NUMBER   y

31           OVERRIDE DF DOSE CHK EXCLUSION   y

32           MAXIMUM DAYS SUPPLY   y

40           CREATE DEFAULT POSSIBLE DOSAGE   y

41           POSSIBLE DOSAGES TO CREATE   y

42           PACKAGE   y

43           CODING SYSTEM  (multiple)

45           COPAY TIER  (multiple)

99.98        MASTER ENTRY FOR VUID   y

99.99        VUID   y

99.991        EFFECTIVE DATE/TIME  (multiple)

100          FDA MED GUIDE   y

101          HAZARDOUS TO HANDLE   y

102          HAZARDOUS TO DISPOSE   y

103          PRIMARY EPA CODE   y

104          WASTE SORT CODE   y

108          CLINICAL EFFECTS OF DRUG  (multiple)

109          FORMULARY DESIGNATOR   y

2000         SERVICE CODE   y

Select FIELD: 11  GCNSEQNO   n

AUDIT: n// YES, ALWAYS

Select FIELD: 12  PREVIOUS GCNSEQNO   n

AUDIT: n// YES, ALWAYS

Select FIELD: 45  COPAY TIER  (multiple)

Select COPAY TIER SUB-FIELD: ??

Choose from:

.01          COPAY TIER LEVEL   y

1            COPAY EFFECTIVE DATE   y

2            COPAY END DATE   y

Select COPAY TIER SUB-FIELD:

Select AUDIT OPTION:

Select OTHER OPTION:

### Download/Install Status Report

**[PSN PPS DNLD/INST STATUS REP]   Synonym: DIS**

This option is used to display information regarding the status of the DOWNLOAD or INSTALL of files found in the PPS-N UPDATE CONTROL file (#57.23).

**Example 1:**

Select PPS-N Menu &lt;TEST ACCOUNT&gt; Option: **DIS** Download/Install Status Report

Select (D)ownload Detail, (I)nstall Detail or (Q)uit: **DOWNLOAD**

Enter Start Date: T-3  (DEC 08, 2017)

Enter End Date: T  (DEC 11, 2017)

DOWNLOAD FILE NAME              DOWNLOAD BEGIN DT/TM   COMPLETION DT/TM

Dec 08, 2017 to Dec 11, 2017                                        PAGE: 1

-----------------------------------------------------------------------------

(1) PPS\_50PRV\_51NEW.DAT         DEC 08, 2017@15:56:35  DEC 08, 2017@15:56:41

(2) PPS\_51PRV\_52NEW.DAT         DEC 10, 2017@15:15:44  DEC 10, 2017@15:15:50

(3) PPS\_52PRV\_53NEW.DAT         DEC 10, 2017@15:33:06  DEC 10, 2017@15:33:12

Select a Download File for greater detail. Choose 1-3 or '^' to Quit: **3**

DOWNLOAD INFORMATION FOR FILE PPS\_52PRV\_53NEW.DAT

PAGE: 1

-----------------------------------------------------------------------------

Download File Name:              PPS\_52PRV\_53NEW.DAT

Download Begin Date/Time:        Dec 10, 2017@15:33:06

Download Complete Date/Time:     Dec 10, 2017@15:33:12

Download File Size:              4884321

Download Error Message:

Press Return to Continue:

DOWNLOAD FILE NAME              DOWNLOAD BEGIN DT/TM   COMPLETION DT/TM

Dec 08, 2017 to Dec 11, 2017                                        PAGE: 1

-----------------------------------------------------------------------------

(1) PPS\_50PRV\_51NEW.DAT         DEC 08, 2017@15:56:35  DEC 08, 2017@15:56:41

(2) PPS\_51PRV\_52NEW.DAT         DEC 10, 2017@15:15:44  DEC 10, 2017@15:15:50

(3) PPS\_52PRV\_53NEW.DAT         DEC 10, 2017@15:33:06  DEC 10, 2017@15:33:12

Select a Download File for greater detail. Choose 1-3 or '^' to Quit:

**Example 2:**

Select PPS-N Menu &lt;TEST ACCOUNT&gt; Option: **DIS  Download/Install Status Report**

Select (D)ownload Detail, (I)nstall Detail or (Q)uit: **INSTALL**

Enter Start Date: **T-3** (DEC 08, 2017)

Enter End Date: **T** (DEC 11, 2017)

INSTALL FILE NAME               INSTALL BEGIN DT/TM    COMPLETION DT/TM

Dec 08, 2017 to Dec 11, 2017                                        PAGE: 1

-----------------------------------------------------------------------------

(1) PPS\_50PRV\_51NEW.DAT;1       DEC 10, 2017@11:37:54  DEC 10, 2017@11:42:21

(2) PPS\_50PRV\_51NEW.DAT;1       DEC 10, 2017@12:18:20  DEC 10, 2017@12:19:43

(3) PPS\_50PRV\_51NEW.DAT;1       DEC 10, 2017@13:31:53  DEC 10, 2017@13:33:14

(4) PPS\_51PRV\_52NEW.DAT;1       DEC 10, 2017@15:15:57  DEC 10, 2017@15:17:16

Select an Install File for greater detail. Choose 1-4 or '^' to Quit: **4**

Current Install Status:

-----------------------

Name:                         PPSN

Open VMS Local Directory:

UNIX/LINUX Local Directory:   REDACTED

PPS-N Install Version:        52

PPS-N Mail Group:             REDACTED

Secondary Mail Group:         REDACTED VA.GOV

PPS-N Download Version:       53

Download Status:              NOT IN PROGRESS

Install Status:               NOT IN PROGRESS

Install Information for file PPS\_51PRV\_52NEW.DAT;1:

--------------------------------------------------

Install Begin Date/Time:      DEC 10, 2017@15:15:57

Install Completion Date/Time: DEC 10, 2017@15:17:16

Last VistA file processed:    50.68

Last File IEN processed:      24282,

Last TMP file subscript:      TMP(PSN PPSN PARSED,29495,DATAO,50.68,99

Last Update file section:     DATA

Displayed Last:               Installation completed.

Select (E)rror Detail or (Q)uit: ERROR

ERROR INFORMATION FOR FILE PPS\_51PRV\_52NEW.DAT;1

PAGE: 1

-----------------------------------------------------------------------------

No Error Information for this file

Press Return to Continue:

Current Install Status:

-----------------------

Name:                         PPSN

Open VMS Local Directory:

UNIX/LINUX Local Directory:   REDACTED /

PPS-N Install Version:        52

PPS-N Mail Group:            REDACTED V

Secondary Mail Group:         REDACTED

PPS-N Download Version:       53

Download Status:              NOT IN PROGRESS

Install Status:               NOT IN PROGRESS

Install Information for file PPS\_51PRV\_52NEW.DAT;1:

--------------------------------------------------

Install Begin Date/Time:      DEC 10, 2017@15:15:57

Install Completion Date/Time: DEC 10, 2017@15:17:16

Last VistA file processed:    50.68

Last File IEN processed:      24282,

Last TMP file subscript:      TMP(PSN PPSN PARSED,29495,DATAO,50.68,99

Last Update file section:     DATA

Displayed Last:               Installation completed.

Select (E)rror Detail or (Q)uit: QUIT

INSTALL FILE NAME               INSTALL BEGIN DT/TM    COMPLETION DT/TM

Dec 08, 2017 to Dec 11, 2017                                        PAGE: 1

-----------------------------------------------------------------------------

(1) PPS\_50PRV\_51NEW.DAT;1       DEC 10, 2017@11:37:54  DEC 10, 2017@11:42:21

(2) PPS\_50PRV\_51NEW.DAT;1       DEC 10, 2017@12:18:20  DEC 10, 2017@12:19:43

(3) PPS\_50PRV\_51NEW.DAT;1       DEC 10, 2017@13:31:53  DEC 10, 2017@13:33:14

(4) PPS\_51PRV\_52NEW.DAT;1       DEC 10, 2017@15:15:57  DEC 10, 2017@15:17:16

Select an Install File for greater detail. Choose 1-4 or '^' to Quit: **^**

Select (D)ownload Detail, (I)nstall Detail or (Q)uit: ^

### Manage Secure Shell (SSH) Keys

**[PSN PPS SSH KEY MANAGEMENT]   Synonym: SSH**

This option is used for managing SSH encryption keys used in PPS-N data file download from the server.

Once the PPS-N parameters have been entered the next step is to create a pair of SSH encryption keys that will be used for authenticating the sFTP connection to the state automatically bypassing the need for the user to type in a sFTP password. This will enable the data file download from the PPS-N server. Use the Manage Secure Shell (SSH) Keys [PSO PPS-N SSH KEY MANAGEMENT] option and follow the steps below:

<!-- image -->

The Manage Secure Shell (SSH) Keys [PSN PPS SSH KEY MANAGEMENT]  option requires the PSN PPS COORD Security Key for creating or deleting SSH Key pairs.

- **Verify that you don’t have an SSH Key pair in place. You can use the Action ‘V’ (View Public SSH Key) for this purpose, as seen in the example below:**

Select one of the following:

V         View Public SSH Key

C         Create New SSH Key Pair

D         Delete SSH Key Pair

H         Help with SSH Keys

Action: V// v  View Public SSH Key

**[No SSH Key Pair found]**

Press Return to continue:

The message [No SSH Key Pair found] displayed above indicates that there are no SSH keys meaning that it is okay to proceed with the creation of a new SSH Key Pair.

- If you are not sure how to create and share the Public SSH Key invoke the Action ‘H’ for detailed information to help you successfully create and share the key with the state.  It is recommended that you use ECDSA.

Action: V// **h** Help with SSH Keys

Secure SHell (SSH) Encryption Keys are used to allow data file download.

Follow the steps below to successfully setup data file download from Austin

server to VistA sites:

Step 1: Select the 'C' (Create New SSH Key Pair) Action and follow the prompts

to create a new pair of SSH keys. If you already have an existing SSH

Key Pair you can skip this step.

You can check whether you already have an existing SSH Key Pair

through the 'V' (View Public SSH Key) Action.

Encryption Type: RSA or ECDSA?

-----------------------------------

Rivest, Shamir &amp; Adleman (RSA) has been one of the most common

encryption algorithms used by the IT industry for securely sharing data.

Elliptic Curve Digital Signature Algorithm (ECDSA) is a more complex

public key cryptography encryption algorithm that is now supported by

the VA. If ECDSA is selected you will be prompted to enter the Bit size.

Valid selections are 256, 384 or 521.

You will need to contact the Austin SFTP server support to determine

which type to select.

Press Return to continue:

Step 2: Share the Public SSH Key content with the PPS-N SFTP server (Austin).

In order to successfully establish the data download files, the SFTP

server at Austin needs to install/configure the new SSH Key created in

step 1 for the user id they assigned to your site. Use the 'V' (View

Public SSH Key) Action to retrieve the content of the Public SSH key.

The Public SSH Key should not contain line-feed characters, therefore

after you copy &amp; paste it from the terminal emulator into an email or

text editor make sure it contains only one line of text (no wrapping).

- Once you have read the Help text above proceed to creating the SSH Key Pair by selecting the Action ‘C’ (Create New SSH Key Pair)

Action: V// **C** Create New SSH Key Pair

Enter your Current Signature Code:    SIGNATURE VERIFIED

Select one of the following:

RSA       Rivest, Shamir &amp; Adleman (RSA)

ECDSA     Elliptic Curve Digital Signature Algorithm (ECDSA)

SSH Key Encryption Type: RSA// ?

Encryption Type: RSA or ECDSA?

-----------------------------------

Rivest, Shamir &amp; Adleman (RSA) has been one of the most common

encryption algorithms used by the IT industry for securely

sharing data.

Elliptic Curve Digital Signature Algorithm (ECDSA) is a more complex public key cryptography encryption algorithm that is now supported by the VA. If ECDSA is selected you will be prompted to enter the Bit size. Valid selections are 256, 384 or 521.

You will need to contact the Austin SFTP server support to determine which type to select

Select one of the following:

RSA       Rivest, Shamir &amp; Adleman (RSA)

ECDSA     Elliptic Curve Digital Signature Algorithm (ECDSA)

SSH Key Encryption Type: RSA//   Rivest, Shamir &amp; Adleman (RSA))

Confirm Creation of SSH Keys? NO// YES

Creating New SSH Keys, please wait...Done.

- Once you have created the new SSH Key Pair use the Action ‘V’ (View Public SSH Key) one more time to retrieve the content of the Public SSH Key so that you can share with the sftp server.

Public SSH Key (RSA) content (does not include dash lines):

--------------------------------------------------------------------------------

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDfdQ3vqmqVKT2V6gn34Q42fGJz7hYgEGaP48Hpxk7u

ZKid0DkUnk4NKI4bf5uwng2TeT5/fPDAzUuTRJCWwJ2hmpBaUXJ+y9b+E5jXsjk8cWRz4frjGz38PTE1

J0205eYTwRoAeK9qYxVyBiYd7GJjzZkaNL32P3tfMQfBb09bhdeMwtarkPSo6gh65rXGS+3R4DgU5xFd

QeUU7SGXaVxTEXAsKQagaPIClXrk4wFZ8Q3JvDviWHrKXGb3gmg5RWXC7pHTuZf7LRzhBaDYUbqXN+6k

x06CycvB6GanQAf1cf1+AO2O9pdJ1J4DN2lA/HDV3BsjNLI926zgMa7ci8kL

--------------------------------------------------------------------------------

- Send the key to AITC to be added.

| <!-- image -->   | REDACTED    |
|------------------|-------------|

Example: A screen shot of a request

<!-- image -->

## Glossary

**Automatic Matching by** This is the pairing of a drug from the local

**NDC Matching** DRUG file (#50) with a drug in the National Drug files with the same NDC number. This matching will be accomplished when the option *Automatic Match of Unmatched Drugs* is executed for the first time.

**Active Drug** Drugs that contain no inactivation date in the INACTIVE DATE field (#100) of the local DRUG file (#50).

**Bulk Compound** An item manufactured by the pharmacy in a large quantity (gallons, pounds, etc.) and kept on hand to be dispensed in smaller 0quantities (ounces, grams, etc.). Identified by the code “M” in the DEA, SPECIAL HDLG field (#3) of the local DRUG file (#50).

**CLINICAL EFFECTS OF DRUG** This field contains the package associated

**Field (#50.68108)** with the clinical effect duration. Only the default value of NO will be displayed and other fields will not be populated.

**CMOP** Consolidated Mail Outpatient Pharmacy.

**Copay Tier** This VistA field indicates the level of copayment a Pharmacy product has as it relates to the calculation of the copayment amount.  The tier levels include Tier 0, Tier 1, Tier 2 and Tier 3. See **Fixed Medication Copay Tier** definition below for the types of products associated with each tier.

**DOT SHIPPING CODE** This field contains the DOT shipping code

**Field (#105)** associated with the disposal of the drug.

**DEA, SPECIAL HDLG** A field of the local DRUG file (#50). Contains

**Field (#3)** one or more codes representing special characteristics of a product.

**DRUG File** *See* Local DRUG File (#50).

**DRUG INGREDIENTS** A file that contains individual generic

**File (#50.416)** drugs that are components of various drug products.

**Error** In the National Drug File (NDF) software, an error is an entry in the NATIONAL DRUG TRANSLATION file (#50.612) that does not have a match in the local DRUG file (#50).

**FDA Medication Guide** Paper handouts that come with many prescription medicines given to the patient. The guides address issues that are specific to particular drugs and drug classes, and contain FDA-approved information that can help patients avoid serious adverse events.

**Fixed Medication Copay Tier** **Mandated Criteria specifying how copay amounts will be calculated determined by the Tier level designated for a Pharmacy Product including: Tier 1 - selected generic, Tier 2 - generic and Tier 3 - brand name products.  A Tier 0 will be used for Supplies, and other exempt products.**

**FORMULARY DESIGNATOR** This field is used to classify prior

**Field (#109)** authorization levels before dispensing. Prior authorization is used to ensure that the medication is appropriate for each individual veteran. Examples are: **.**

- Prior Authorization-National (PA-N) refers

to medications that are formulary, but

require prior approval at the national

level before dispensing.

- Prior Authorization-VISN (PA-V) refers

to medications that are formulary, require

prior approval at the VISN level before

dispensing.

- Prior Authorization-Facility (PA-F) refers

to medications that are formulary, but

require prior approval at the facility

level before dispensing.

- Prior Authorization-DOD COC refers to

medications that are formulary, but

require prior approval for Department of

Defense Continuity of Care.

**FORMULARY DESIGNATOR** This field contains the descriptive text

**TEXT Field (#50.681)** of the formulary designator.

**FSN** Federal Stock Number. A unique identifying number assigned by the Federal Supply system to a product (drug, supply, food item, etc.) for ordering and accounting purposes. Synonymous with the National Stock Number (NSN). One of the fields in the local DRUG file (#50).

**HAZARDOUS TO HANDLE** This field indicates whether a drug exhibits

**Field (#101)** one or more characteristics that makes it hazardous to handle (i.e. toxicity, carcinogenicity, etc.)

**HAZARDOUS TO DISPOSE** This field indicates whether a drug exhibits

**Field (#102)** one or more characteristics that makes it hazardous to dispose (i.e. toxicity, carcinogenicity, etc.)

**Investigational Drug** A new drug for which an investigational new drug application has been filed with, and approved by the Food and Drug Administration (FDA). The drug may be a new chemical compound which has not been released for general use and is not available through regular channels of interstate commerce, or it may be an approved drug with a new use, different dosage level, different route of administration, or a new combination of drugs. Identified by the code “I” in the DEA, SPECIAL HDLG field (# 3) of the local DRUG file (#50).

**Local DRUG File** This file contains the local GENERIC NAME (#.01), INACTIVE DATE (#100), DEA, SPECIAL HDLG (#3), and NDC fields, as well as others. NDF software attempts to match products from this file with products in the VA GENERIC file (#50.6) and the VA PRODUCT file (#50.58).

**Local Generic Name** Field #.01.The first field in the local DRUG file (#50). This is the identifying name for the item. It is this name that is routinely printed on prescription labels, medication administration records, inventory sheets, etc. The field name is GENERIC NAME (#.01). These terms are interchangeable throughout this document. This field is automatically stuffed with the VA Print Name when an item is marked for CMOP transmission.

**Manually Classed Drug** A drug from the local DRUG file (#50) which could not be matched to the National Drug files, but has been assigned a VA Drug Classification through the use of the *Allow Unmatched Drugs to be Classed* menu option.

**Manufacturer Code** The first portion of the NDC number (the first 4-6 digits). Identifies the manufacturer of the product.

**Manufactured in Pharmacy** An item which is manufactured (or compounded) by pharmacy services on a prescription-by-prescription basis (as opposed to a bulk compound). Identified by the code “0” in the DEA, SPECIAL HDLG field (#3) of the local DRUG file (#50).

**National Drug File Package** or	This software package attempts to match

**National Drug File Software** the National Drug files entries with local DRUG file (#50) entries using both automatic matching and manual matching. The automatic matching is by NDC number only.

**National Drug files** VA GENERIC file (#50.6), VA PRODUCT file (# 50.68), NDC/UPN file (#50.67). Three files that contain a list of available drug products. Includes specific information for each product, including trade name, NDC number manufacturer, VA Drug Class code, dosage form, route of administration, strength, units, ingredients, ingredient strength and units, package code, package size, package type, VA product name, and VA generic name. NDF software attempts to match products from this file with products in the local DRUG file (#50).

**National Drug Identifier** A unique, HL7 compatible code assigned to all products marked for CMOP transmission. This code is utilized to transmit VA Print name and dispense unit from **V** *IST* **A** to the vendor.

**NATIONAL DRUG** File #50.612. A temporary file that is created

**TRANSLATION File** by the NDF software. This file will contain information on drugs that have been matched, or for which a match was attempted.

**NDC (NDC Number)** National Drug Code. A unique number assigned to a drug by the manufacturer for identification purposes. The NDC is in one of three formats: 4-4-2, 5-3-2, or 5-4-1. The first part is the manufacturer’s code, the second part is the product number, and the last is the code for the package size and type. This is one of the fields in the local DRUG file (#50).

**NDF** National Drug File. In this document, NDF refers to either the National Drug file software. ( *See National Drug File Package or National Drug File Software.* )

**OTC** Over-the-Counter. A term used to describe a product that may be supplied or purchased without a physician’s prescription. Identified by the code “9” in the DEA, SPECIAL HDLG field (#3) of the local DRUG file (#50).

**Package Code** The last portion of the NDC number (the last two digits). This identifies the package type and size in which the product is supplied.

**Package Size** The actual (physical) amount of a drug in the individual package (i.e., 5000 capsules per bottle).

**Package Type** The physical container in which a drug is supplied (i.e., bottle, vial).

**PMI Sheet** Patient Medication Information Sheet. Medication information sheets given to the patient to explain how and why to take a medication and the possible side effects. The information supplied in the PMI sheet is supplied by a commercial vendor.

**PPS-N** The Pharmacy Product System-National (PPS-N) is a Web-based application that provides the ability to manage pharmacy-specific data across the VA enterprise, ensuring that all facilities are using the same base data for their operations. It allows approved national VA personnel to easily, quickly, and safely manage the VA National Formulary which directs which products (such as medications and supplies) are to be purchased and used by the VA hospital system.

**PRIMARY EPA CODE Field (#103)** This field contains the Environmental Protection Agency (EPA) waste code which identifies the drugs hazardous waste characteristics. For example: EPA waste code P001 for Warfarin, and salts, when present, at concentrations greater than 0.3%.

**Product Code** The second portion of the NDC number (the second four digits) that identifies the specific drug.

**PSNMGR** The name of the primary menu option and of the key that must be assigned to the pharmacy coordinator and supervisors using the National Drug File software.

**Supply Item** A non-drug item entered into the GENERIC NAME field (#.01) of the local DRUG file (#50) that may be a prosthetic or expendable item such as ostomy supply, alcohol pads, syringes, bed pans, etc. identified by the code “S” in the DEA, SPECIAL HDLG field (#3) of the local DRUG file (#50).

**Trade Name** This is the brand name. The name given to a generic product to distinguish it as one produced and sold by a specific manufacturer.

**UPC** Universal Product Code. A unique number assigned to a product by a manufacturer commonly used for supply items. These may be found in the NDC/UPN file (#50.67).

**VA Dispense Unit** The standardized unit assigned to a product when the product is marked for CMOP transmission.

**VA DRUG CLASS File** File (#50.605). This file contains the VA Drug Classification codes and their descriptions. Each product in the National Drug files has one of these codes assigned.

**VA Generic Name** A name given to an item (drug, supply, etc. in the VA GENERIC file (#50.6)). It is this name which is matched with the entry in the GENERIC NAME (local generic name) field (#.01) of the local DRUG file (#50). This name does not contain strength, unit, or dosage form.

**VA Print Name** The forty-character name assigned as the name that prints on all prescription labels for products marked for CMOP transmission.

**VA Product Name** The unique name assigned to each drug product in the National Drug files. This name comes from the VA PRODUCT file (#50.68) and includes strength, unit, and dosage form.

**VISTA** Veterans Health Information Systems and Technology Architecture.

**WASTE SORT CODE Field (#104)** This field contains the waste sort code associated with disposal of the drug.

## Index

## A

Allow Unmatched Drugs to be Classed · **16**

Allow Unmatched Drugs to be Classed (Loop) · **17**

Allow Unmatched Drugs to be Classed (Single Drug) · **16**

Attempt to Class Item already Matched, Classed, and Merged · **18**

**Automatic Match of Unmatched Drugs** · **15**

## D

Drug-Drug Interaction Report · **37**

## E

Entering National Drug Codes · **3**

## I

Icons · **2**

Inquire to Local Drug File · **45** , **75** , **77** , **79** , **81** , **86** , **87** , **90** , **92** , **95**

**Inquire to Local Drug File by Generic Name Chosen** · **45**

**Inquire to Local Drug File by Generic Name Chosen (cont.)** · **46**

Inquire to National Files · ii, 57

Inquire to VA Product Info For Local Drug · **ii** , **46**

Inquiry Options · **45**

Introduction · **1**

## L

Local Drug File Report · **20**

Local Drug/VA Print Name Report · **41**

Local Drugs Excluded from Drug-Drug Interactions · **43**

Local Drugs with No Match to NDF Report · **32**

Local Drugs with No VA Drug Class Report · **25**

Local Formulary Report · **33**

Loop Interrupted When No Default Class and No Value Entered · **17**

## M

Manually Classed Drugs Report · **31**

Menu · **4**

Merge National Drug File Data Into Local File · **14**

## N

National Drug File Reports Menu · **19**

National Drug File V. 4.0 Menu · **4**

National Formulary Report · **36**

NDC/UPN Inquiry · **55**

NDF Info From Your Local Drug File · **28**

## P

Pharmacy Pre-Installation Preparation · **3**

Print a PMI Sheet · **70** , **73**

Printing a Patient Medication Information Sheet · **70** , **73** , **75**

## R

Related Manuals · **1**

Rematch/Match Single Drugs · **6**

Report of Attempted Match Drugs · **22**

Report of VA Generic Names from National Drug · **21**

## S

Supply (XA000) VA Class Report · **30**

## U

Using the Inquire Options · **45**

Using the Matching Options · **6**

Using the National Drug File Reports Menu · **19**

## V

VA Drug Classification · **27**

VA Product Names By Class Report · **40**

VA Product Names Matched Report · **23**

VA Products Excluded from Drug-Drug Interactions · **44**

VA Products Marked for CMOP Transmission · **38**

Verify Matches · **10**

Verify Single Match · **12**

Verify Single Match, Drug Already Verified · **13**

Verify Single Match, Drug Not Matched · **13**