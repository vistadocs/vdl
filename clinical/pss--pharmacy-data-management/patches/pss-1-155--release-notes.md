---
title: PSS*1*155 PSN*4*261/262 Release Notes - Supra Therapeutic Dosages
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: PSN*4*261/262  - Supra Therapeutic Dosages
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*155
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - possible
  - dosages
  - drug
  - national
  - create
  - dosage
  - auto
  - units
  - match
  - package
page_count: 0
word_count: 3136
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/supra_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/supra_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

![](pss-1-155-psn-4-261-262-release-notes-supra-therapeutic-dosages/001.png)

NATIONAL DRUG FILE

PHARMACY DATA MANAGEMENT

Analysis to Prevent Creation of  
Supra-therapeutic Dosages

Release Notes

PSN\*4\*261, PSN\*4\*262, PSS\*1\*155

April 2011

Product Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [National Drug File V. 4.0](#national-drug-file-v-40)
  - [Creation of New Fields – PSN\4\261](#creation-of-new-fields-psn4261)
  - [Display of New Fields – PSN\4\262](#display-of-new-fields-psn4262)
- [Pharmacy Data Management V. 1.0](#pharmacy-data-management-v-10)
  - [Create Default Possible Dosage = Yes](#create-default-possible-dosage-yes)
  - [Create Default Possible Dosage = No](#create-default-possible-dosage-no)
The Analysis to Prevent Creation of Supra-therapeutic Dosages release includes patches PSN\*4\*261, PSN\*4\*262, and PSS\*1\*155. The scope of the Analysis to Prevent Creation of Supra-therapeutic Dosages project is to correct specific Patient Safety Issues and to address specific functional enhancements to the software as approved by the Health Provider Systems Enterprise Systems Manager.
These patches provide functionality to prevent the inadvertent creation of supra-therapeutic possible dosages for high risk medications during the dosage creation segment of Pharmacy Data Management and National Data File updates.
A supra-therapeutic dosage is one that far exceeds the normal therapeutic range. A sub-therapeutic dosage is one that is far below the normal therapeutic range. Certain drugs with an automatically calculated dosage of one time or two times the base strength that is supra- or sub-therapeutic will be adjusted to not auto-create those default possible dosages during the matching and rematching process. The monthly National Data File update patch will flag those drugs that are identified as supra-therapeutic.
Installation instructions are included in the patch descriptions. Below is a list of the applications involved in this project along with their associated patch number:
<u>APPLICATION/VERSION PATCH</u>
1\. NATIONAL DRUG FILE V. 4.0 PSN\*4\*261 (released October 2010)
2\. NATIONAL DRUG FILE V.4.0 PSN\*4\*262
3\. PHARMACY DATA MANAGEMENT V. 1.0 PSS\*1\*155
The patches should be installed in the order outlined above.

# National Drug File V. 4.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches PSN\*4\*261 and PSN\*4\*262 include the following enhancements. The items listed below describe the features that will be active upon installation of both National Drug File patches.

- PSN\*4\*261 created three new fields in the Data Dictionary for the VA PRODUCT file (#50.68).
- PSN\*4\*262 contains changes to the *Inquire to National Files* \[PSNACT\] and *Inquire to VA Product Info For Local Drug* \[PSNLOOK\] options to include the display of the new fields.

NOTE

Patch PSN\*4\*262 is being released in conjunction with Pharmacy Data Management patch PSS\*1\*155, which has the functionality in place to determine if possible dosages should be  
auto-created or not during the match/re-match process.

## Creation of New Fields – PSN\*4\*261

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSN\*4\*261 was released in October 2010 in preparation for the Supra-therapeutic Dosages project. It contains the following three new fields that were added to the VA PRODUCT file (#50.68).

#### CREATE DEFAULT POSSIBLE DOSAGE Field (#40)

#### Field Description

> Indicates whether Possible Dosages should be auto-created based on Dosage Form/Dispense Unit (Default) or if you want to control the Possible Dosage auto-creation process for the Dispense Drugs matched/re-matched to this VA Product.

> YES—Possible Dosages will be auto-created based upon Dosage Form/Dispense Unit combination (Default).

> NO—Possible Dosages will be auto-created according to the rule set by the POSSIBLE DOSAGES TO CREATE (#41) and PACKAGE (#42) fields.

#### POSSIBLE DOSAGES TO CREATE Field (#41)

#### Field Description 

> Indicates which Possible Dosages or if no Possible Dosages should be auto-created for Dispense Drugs matched/re-matched to this VA Product.

> N—No Possible Dosages are auto-created for Dispense Drugs matched to this VA PRODUCT entry during the match/re-match process.

> O—Only 1x Possible Dosage is auto-created for Dispense Drugs Dispense Drugs matched to this VA PRODUCT entry during the match/re-match process.

> B—Both 1x and 2x Possible Dosages are auto-created for Dispense Drugs Dispense Drugs matched to this VA PRODUCT entry during the match/re-match process.

#### PACKAGE Field (#42)

#### Field Description

> Indicates the Package(s) use for the Possible Dosage(s) auto-created.

> I—Possible Dosages auto-created for Dispense Drugs matched/re-matched to this VA PRODUCT entry will be available for the Inpatient application only.

> O—Possible Dosages auto-created for Dispense Drugs matched/re-matched to this VA PRODUCT entry will be available for the Outpatient application only.

> IO—Possible Dosages auto-created for Dispense Drugs matched/re-matched to this VA PRODUCT entry will be available for both, Outpatient and Inpatient applications.

## Display of New Fields – PSN\*4\*262

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSN\*4\*262 contains changes to the *Inquire to National Files* \[PSNACT\] and *Inquire to VA Product Info For Local Drug* \[PSNLOOK\] options to include the display of the new fields. Below are screen captures of how the new fields will display to the screen for both options.

\[PSNLOOK\] – Auto-Create Default Possible Dosage=Yes

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

Override DF Exclude from Dosage Checks: No

Auto-Create Default Possible Dosage? Yes

Restriction:

Refer to PBM/MAP criteria for use of long-acting dihydropyridine calcium

antagonists

Press Return to Continue:

\[PSNLOOK\] – Auto-Create Default Possible Dosage=No, and No Possible Dosages Created

…

National Formulary Indicator: No

Override DF Exclude from Dosage Checks: No

Auto-Create Default Possible Dosage? No

    Possible Dosages To Auto-Create: No Possible Dosages

\[PSNLOOK\] – Auto-Create Default Possible Dosage=No, and Create One Possible Dosage

…

National Formulary Indicator: No

Override DF Exclude from Dosage Checks: No

Auto-Create Default Possible Dosage? No

    Possible Dosages To Auto-Create: 1x Possible Dosages

                            Package: Inpatient

\[PSNLOOK\] – Auto-Create Default Possible Dosage=No, and Create Two Possible Dosages

…

National Formulary Indicator: No

Override DF Exclude from Dosage Checks: No

Auto-Create Default Possible Dosage? No

    Possible Dosages To Auto-Create: 2x Possible Dosages

                            Package: Inpatient and Outpatient

  
\[PSNACT\] – NDF Inquiry by VA Product Name, Auto-Create Possible Dosage=Yes

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? <u>VA</u> VA PRODUCT

Select VA PRODUCT NAME: hydrocortisone

1 HYDROCORTISONE 0.1% CREAM,TOP

2 HYDROCORTISONE 0.25% CREAM,TOP

3 HYDROCORTISONE 0.25% LOTION

4 HYDROCORTISONE 0.25%/NEOMYCIN SO4 0.5% CREAM,TOP

5 HYDROCORTISONE 0.5% AEROSOL,TOP

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 HYDROCORTISONE 0.1% CREAM,TOP

VA Product Name: HYDROCORTISONE 0.1% CREAM,TOP

VA Generic Name: HYDROCORTISONE

Dose Form: CREAM,TOP (Exclude from Dosing Cks)

Strength: 0.1 Units: %

National Formulary Name: HYDROCORTISONE CREAM,TOP

VA Print Name: HYDROCORTISONE 0.1% CREAM

VA Product Identifier: H0161 Transmit to CMOP: Yes VA Dispense Unit: GM

PMIS: None

Active Ingredients: HYDROCORTISONE Strength: 0.1 Units: %

Primary VA Drug Class: DE200

Secondary VA Drug Class:

CS Federal Schedule:

National Formulary Indicator: Yes

National Formulary Restriction:

Exclude Drg-Drg Interaction Ck: Yes (No check for Drug-Drug Interactions)

Override DF Exclude from Dosage Checks: No

Auto-Create Default Possible Dosage? Yes

Press return to continue or '^' to exit:

NDC: 000749040201 UPN:

VA Product Name: HYDROCORTISONE 0.1% CREAM,TOP

Manufacturer: MILL MARK PHARM Trade Name: HYDROCORTISONE

Route: TOPICAL

Package Size: 20 GM Package Type: TUBE

NDC: 000166069539 UPN:

VA Product Name: HYDROCORTISONE 0.1% CREAM,TOP

Manufacturer: MALLARD Trade Name: HYDROCORTISONE

Route: TOPICAL

Package Size: 454 GM Package Type: JAR

\[PSNACT\] – NDF Inquiry by NDC, Auto-Create Possible Dosages=No, and No Possible Dosages Auto-Created

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? <u>n</u> NDC

NDC (N) or UPN (U) ? <u>n</u> NDC

Enter NDC with or without Dashes (-): <u>000223145302</u> 98650

...OK? Yes// \<ENTER\> (Yes)

NDC: 000223145302 UPN:

VA Product Name: PLACEBO TAB

Manufacturer: CONSOLIDATED MC Trade Name: PLACEBO

Route: ORAL

Package Size: 1000 Package Type: BOTTLE

VA Product Name: PLACEBO TAB

VA Generic Name: PLACEBO

Dose Form: TAB

Strength: Units:

National Formulary Name: PLACEBO TAB

VA Print Name: PLACEBO CAP/TAB

VA Product Identifier: P0256 Transmit to CMOP: Yes VA Dispense Unit: CAP/TAB

PMIS: None

Active Ingredients: LACTOSE Strength: 10 Units: %WW

CELLULOSE Strength: 3 Units: %WW

STARCH Strength: 87 Units: %WW

Primary VA Drug Class: XX000

Secondary VA Drug Class:

CS Federal Schedule:

Press return to continue or '^' to exit:

National Formulary Indicator: No

National Formulary Restriction:

Override DF Exclude from Dosage Checks: Yes (No dosage checks performed)

Auto-Create Default Possible Dosage? No

    Possible Dosages To Auto-Create: No Possible Dosages

Press return to continue or '^' to exit:

  
\[PSNACT\] – NDF Inquiry by CMOP ID Number, Auto-Create Possible Dosages=No, and Possible Dosages Auto-Created for Inpatient and Outpatient Packages

LOOKUP BY (VA) PRODUCT, (N)DC, OR (C)MOP ID ? c CMOP ID

CMOP ID: c0504 COD LIVER OIL

VA Product Name: COD LIVER OIL

VA Generic Name: COD LIVER OIL

Dose Form: OIL (Exclude from Dosing Cks)

Strength: Units:

National Formulary Name: COD LIVER OIL OIL

VA Print Name: COD LIVER OIL

VA Product Identifier: C0504 Transmit to CMOP: Yes VA Dispense Unit: ML

PMIS: None

Active Ingredients: COD LIVER OIL Strength: Units:

Primary VA Drug Class: VT801

Secondary VA Drug Class:

CS Federal Schedule:

National Formulary Indicator: No

National Formulary Restriction:

Override DF Exclude from Dosage Checks: Yes (Dosage Checks shall be performed)

Auto-Create Default Possible Dosage? No

    Possible Dosages To Auto-Create: 1x and 2x Possible Dosages

                            Package: Both Inpatient and Outpatient

Press return to continue or '^' to exit:

NDC: 000395063594 UPN:

VA Product Name: COD LIVER OIL

Manufacturer: WALMEAD Trade Name: COD LIVER OIL

Route: ORAL

Package Size: 120 ML Package Type: BOTTLE

…

# Pharmacy Data Management V. 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*155 retires the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option. This option is retired because, if it is run inadvertently, it will delete all existing “Possible Dosages” and “Local Possible Dosages” and will reset the Possible Dosages back to NDF settings. The changes that were entered locally by the site for “Possible Dosages” and “Local Possible Dosages” will be lost. Upon patch installation, this option will be removed from the *Dosages* \[PSS DOSAGES MANAGEMENT\] menu.

This patch uses the three new fields that were added to the VA PRODUCT file (#50.68) as part of patch PSN\*4\*261. These fields will be used during the match/rematch process of the *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] and the *Enter/Edit Dosages* \[PSS EDIT DOSAGES\] options to determine if possible dosages should be auto-created or not. The three fields are:

CREATE DEFAULT POSSIBLE DOSAGE field (#40)

POSSIBLE DOSAGES TO CREATE field (#41)

PACKAGE field (#42)

When the CREATE DEFAULT POSSIBLE DOSAGE field is “YES”, then the existing functionality of auto-creating possible dosages will be retained. When this field is “NO”, it will be used in combination with the value in the POSSIBLE DOSAGES TO CREATE field to determine the auto-creation of possible dosages.

The following conditions will apply when the CREATE DEFAULT POSSIBLE DOSAGE field is “NO”:

> If POSSIBLE DOSAGES TO CREATE field is “NO”, no possible dosages will be auto-created and the following message will be displayed:

> “Due to National Drug File settings no possible dosages were auto-created.”

> If POSSIBLE DOSAGES TO CREATE field is “O”, 1x possible dosage will be auto-created for the package specified by the new PACKAGE field and the following message will be displayed:

> “Due to National Drug File settings only ONE possible dosage will be auto-created.

> If other dosages are needed, create POSSIBLE DOSAGES or LOCAL POSSIBLE DOSAGES as appropriate.”

> If POSSIBLE DOSAGES TO CREATE field is “B”, 1x and 2x possible dosages will be auto-created for the package specified by the new PACKAGE field.

## Create Default Possible Dosage = Yes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screen captures illustrate the conditions when the CREATE DEFAULT POSSIBLE DOSAGE field in the VA PRODUCT file is set to Yes.

*Drug Enter/Edit* option -- Message displayed when no possible dosages are auto-created

Do you wish to match/rematch to NATIONAL DRUG file? No// YES (Yes)

Deleting Possible Dosages...

Match local drug INSULIN NPH U-100 INJ

ORDER UNIT: VI

DISPENSE UNITS/ORDER UNITS: 1

DISPENSE UNIT:

I will try to match NDC: 2-8310-01 to NDF.

I will attempt to match the NDCs from your SYNONYMS.

ORDER UNIT: VI

Match made with INSULIN NPH U-100 INJ

Now select VA Product Name

18 INSULIN NPH HUMAN 100 U/ML INJ HUMULIN N INJ HS501 I0160

19 INSULIN NPH HUMAN 100 U/ML INJ INNOLET 3ML INJ HS501 I0356

20 INSULIN NPH HUMAN 100 U/ML INJ NOVOLIN N INJ HS501 I0161

Enter your choice or press return to continue: 18

Is this a match \< Reply Y, N or press return to continue \> : y

CHOOSE FROM:

1 10 ML VIAL

2 OTHER OTHER

Enter Package Size & Type Combination: 1

Local drug INSULIN NPH U-100 INJ

matches INSULIN NPH HUMAN 100 U/ML INJ HUMULIN N

PACKAGE SIZE: 10 ML

PACKAGE TYPE: VIAL

\< Enter "Y" for yes \>

\< Enter "N" for no \> OK? : Y

LOCAL DRUG NAME: INSULIN NPH U-100 INJ

ORDER UNIT: VI

DISPENSE UNITS/ORDER UNITS: 1

DISPENSE UNIT:

VA PRODUCT NAME: INSULIN NPH HUMAN 100 U/ML INJ HUMULIN N

VA PRINT NAME: INSULIN NPH HUMAN 100 UNIT/ML HUMULIN N CMOP ID: I0160

VA DISPENSE UNIT: VI MARKABLE FOR CMOP: YES

PACKAGE SIZE: 10 ML

PACKAGE TYPE: VIAL

VA CLASS: HS501 INSULIN

CS FEDERAL SCHEDULE:

INGREDIENTS:

INSULIN,NPH,HUMAN/rDNA 100 UNT/ML

NATIONAL FORMULARY INDICATOR: NO

NATIONAL FORMULARY RESTRICTION:

\< Enter "Y" for yes, "N" for no \>

Is this a match ? Y

continued on next page

You have just VERIFIED this match and MERGED the entry.

Resetting Possible Dosages..

Press Return to continue:

Just a reminder...you are editing INSULIN NPH U-100 INJ.

Strength from National Drug File match =\> 100 UNT/ML

Strength currently in the Drug File =\> 100

Strength =\> 100 Unit =\>

Press Return to continue,'^' to exit:

POSSIBLE DOSAGES:

LOCAL POSSIBLE DOSAGES:

Due to National Drug File settings no possible dosages were auto-created.

Do you want to manually enter possible dosages? N// YES

Changing the strength will update all possible dosages for this Drug.

STRENGTH: 100//

Select DISPENSE UNITS PER DOSE: ?

You may enter a new POSSIBLE DOSAGES, if you wish

Type a Number between 0 and 99999999, 4 Decimal Digits

Select DISPENSE UNITS PER DOSE: 1

Are you adding '1' as a new POSSIBLE DOSAGES (the 1ST for this DRUG)? No// Y

(Yes)

Dosage = 100

POSSIBLE DOSAGES DOSE: 100// (No Editing)

DISPENSE UNITS PER DOSE: 1// 0.1

PACKAGE: IO

BCMA UNITS PER DOSE:

Select DISPENSE UNITS PER DOSE:

NOTE

The prompt “Do you want to manually enter possible dosages? N//” is displayed only when no possible dosages were auto-created.

*Drug Enter/Edit* option -- Message displayed when 1 possible dosage is auto-created

Do you wish to match/rematch to NATIONAL DRUG file? No// YES (Yes)

Deleting Possible Dosages...

Match local drug LOMUSTINE 100MG CAP

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 20

DISPENSE UNIT:

I will try to match NDC: 15-3032-20 to NDF.

Local drug LOMUSTINE 100MG CAP

matches LOMUSTINE 100MG CAP

PACKAGE SIZE: 20

PACKAGE TYPE: BOTTLE

Is this a match ?

Enter Yes or No: YES// YES

LOCAL DRUG NAME: LOMUSTINE 100MG CAP

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 20

DISPENSE UNIT:

VA PRODUCT NAME: LOMUSTINE 100MG CAP

VA PRINT NAME: LOMUSTINE 100MG CAP CMOP ID: L0055

VA DISPENSE UNIT: CAP MARKABLE FOR CMOP: YES

PACKAGE SIZE: 20

PACKAGE TYPE: BOTTLE

VA CLASS: AN100 ANTINEOPLASTICS,ALKYLATING AGENTS

CS FEDERAL SCHEDULE:

INGREDIENTS:

LOMUSTINE 100 MG

NATIONAL FORMULARY INDICATOR: YES

NATIONAL FORMULARY RESTRICTION:

\< Enter "Y" for yes, "N" for no \>

Is this a match ? Y

You have just VERIFIED this match and MERGED the entry.

Resetting Possible Dosages..

Press Return to continue:

Just a reminder...you are editing LOMUSTINE 100MG CAP.

Strength from National Drug File match =\> 100 MG

Strength currently in the Drug File =\> 100 MG

Strength =\> 100 Unit =\> MG

Press Return to continue,'^' to exit:

POSSIBLE DOSAGES:

DISPENSE UNITS PER DOSE: 1 DOSE: 100MG PACKAGE: IO

continued on next page

LOCAL POSSIBLE DOSAGES:

Due to National Drug File settings only ONE possible dosage was auto-created. If other dosages are needed, create POSSIBLE DOSAGES or LOCAL POSSIBLE DOSAGES as appropriate.

Do you want to edit the dosages? N// YES

Changing the strength will update all possible dosages for this Drug.

STRENGTH: 100//

Select DISPENSE UNITS PER DOSE: ?

Answer with POSSIBLE DOSAGES DISPENSE UNITS PER DOSE

Choose from:

1 100 IO

You may enter a new POSSIBLE DOSAGES, if you wish

Type a Number between 0 and 99999999, 4 Decimal Digits

Select DISPENSE UNITS PER DOSE:

*Drug Enter/Edit* option -- Message displayed when 2 possible dosages are auto-created

Do you wish to match/rematch to NATIONAL DRUG file? No// Y (Yes)

Deleting Possible Dosages...

Match local drug DACARBAZINE 200MG INJ

ORDER UNIT: BX

DISPENSE UNITS/ORDER UNITS: 12

DISPENSE UNIT:

I will try to match NDC: 26-8151-20 to NDF.

Local drug DACARBAZINE 200MG INJ

matches DACARBAZINE 200MG/VIL INJ

PACKAGE SIZE: 12 X 200 MG

PACKAGE TYPE: VIAL

Is this a match ?

Enter Yes or No: YES// YES

LOCAL DRUG NAME: DACARBAZINE 200MG INJ

ORDER UNIT: BX

DISPENSE UNITS/ORDER UNITS: 12

DISPENSE UNIT:

VA PRODUCT NAME: DACARBAZINE 200MG/VIL INJ MARKABLE FOR CMOP: NOT

MARKED

PACKAGE SIZE: 12 X 200 MG

PACKAGE TYPE: VIAL

VA CLASS: AN900 ANTINEOPLASTIC,OTHER

CS FEDERAL SCHEDULE:

INGREDIENTS:

DACARBAZINE 200

NATIONAL FORMULARY INDICATOR: YES

NATIONAL FORMULARY RESTRICTION:

continued on next page

\< Enter "Y" for yes, "N" for no \>

Is this a match ? Y

You have just VERIFIED this match and MERGED the entry.

Resetting Possible Dosages..

Press Return to continue:

Just a reminder...you are editing DACARBAZINE 200MG INJ.

Strength from National Drug File match =\> 200 MG/VIAL

Strength currently in the Drug File =\> 200

Strength =\> 200 Unit =\>

Press Return to continue,'^' to exit:

POSSIBLE DOSAGES:

DISPENSE UNITS PER DOSE: 1 DOSE: 200MG/1VIAL PACKAGE: IO

DISPENSE UNITS PER DOSE: 2 DOSE: 400MG/2VIAL PACKAGE: IO

LOCAL POSSIBLE DOSAGES:

Due to National Drug File settings TWO possible dosages were auto-created.

Do you want to edit the dosages? N//

## Create Default Possible Dosage = No

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screen captures illustrate the conditions when the CREATE DEFAULT POSSIBLE DOSAGE field in the VA PRODUCT file is set to No.

*Drug Enter/Edit* option -- Message displayed when NDF is set to not auto-create Possible Dosages

Do you wish to match/rematch to NATIONAL DRUG file? No// (No)

Just a reminder...you are editing LOMUSTINE 10MG CAP

Strength from National Drug File match =\> 10 MG

Strength currently in the Drug File =\> 10 MG

Strength =\> 10 Unit =\> MG

POSSIBLE DOSAGES:

LOCAL POSSIBLE DOSAGES:

This drug has been set within the National Drug File to not auto create possible dosages.

Do you want to manually enter possible dosages? N//

*Drug Enter/Edit* option -- Message displayed when NDF is set to auto-create 1 Possible Dosage

Do you wish to match/rematch to NATIONAL DRUG file? No// (No)

Just a reminder...you are editing LOMUSTINE 10MG CAP

This drug can have Possible Dosages, but currently does not have any.

This drug has been set within the National Drug File to auto create only one

possible dosage.

Create Possible Dosages for this drug? N// YES

Resetting Possible Dosages..

Due to National Drug File settings only ONE possible dosage was auto-created. If other dosages are needed, create POSSIBLE DOSAGES or LOCAL POSSIBLE DOSAGES as appropriate.

Press Return to continue:

Strength from National Drug File match =\> 10 MG

Strength currently in the Drug File =\> 10 MG

Strength =\> 10 Unit =\> MG

POSSIBLE DOSAGES:

DISPENSE UNITS PER DOSE: 1 DOSE: 10 MG PACKAGE: IO

LOCAL POSSIBLE DOSAGES:

This drug has been set within the National Drug File to auto create only one possible dosage.

Do you want to edit the dosages? N//

*Drug Enter/Edit* option -- Message displayed when NDF is set to auto-create 2 Possible Dosages

Do you wish to match/rematch to NATIONAL DRUG file? No// (No)

Just a reminder...you are editing LOMUSTINE 10MG CAP

This drug can have Possible Dosages, but currently does not have any.

This drug has been set within the National Drug File to auto create two

possible dosages.

Create Possible Dosages for this drug? N// YES

Resetting Possible Dosages..

Due to National Drug File settings TWO possible dosages were auto-created.

Press Return to continue:

Strength from National Drug File match =\> 10 MG

Strength currently in the Drug File =\> 10 MG

Strength =\> 10 Unit =\> MG

POSSIBLE DOSAGES:

DISPENSE UNITS PER DOSE: 1 DOSE: 10 MG PACKAGE: IO

DISPENSE UNITS PER DOSE: 2 DOSE: 20 MG PACKAGE: IO

LOCAL POSSIBLE DOSAGES:

This drug has been set within the National Drug File to auto create two possible dosages.

Do you want to edit the dosages? N//

NOTE

When using the *Enter/Edit Dosages* option for drugs that have been matched/rematched, the functionality and messages are similar to the *Drug Enter/Edit* option information illustrated above.