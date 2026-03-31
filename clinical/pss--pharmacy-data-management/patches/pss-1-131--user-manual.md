---
title: PSS*1*131 User Manual - ePharmacy Phase 4 Iteration II Change Pages
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: ePharmacy Phase 4 Iteration II Change Pages
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*131
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 1
description: > ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/001.png)
audience: 
keywords: 
  - class
  - blockquote
  - even
  - schedule
  - table
  - code
  - drug
  - strong
  - special
  - contents
page_count: 0
word_count: 1306
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p131_um_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p131_um_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/001.png)

PHARMACY DATA MANAGEMENT

USER MANUAL

September 1997

(Revised July 2009)

VistA Health Systems Design & Development

> Revision History

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/09</td>
<td><blockquote>
<p>27-34</p>
</blockquote></td>
<td>PSS*1*131</td>
<td><p>Added explanations of DEA special handling code U for sensitive drug.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/09</td>
<td><blockquote>
<p>81</p>
</blockquote></td>
<td>PSS*1*137</td>
<td><p>Added Automate CPRS Refill field to the <em>Pharmacy System Parameters Edit</em> [PSS MGR] option.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/09</td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td>PSS*1*129</td>
<td><p>Pages renumbered to accommodate added pages. Pharmacy Reengineering (PRE) V.0.5 Pre-Release. <u>Restructured <em>Pharmacy Data Management</em> menu</u>:</p>
<ul>
<li><p>Grouped related options under the following new sub-menus: <em><u>Drug Text Management</u>, <u>Medication Instruction Management</u>, <u>Medication Routes Management</u>,</em> and <em><u>Standard Schedule Management</u></em></p></li>
<li><p>Added <u>temporary <em>Enhanced Order Checks Setup Menu</em></u></p></li>
<li><p>Added the following options: <em><u>Find Unmapped Local Medication Routes</u>, <u>Find Unmapped Local Possible Dosages</u>, <u>Map Local Medication Route to Standard</u>, <u>Map Local Possible Dosage</u>s, <u>Mark PreMix Solutions</u>, <u>Request Change to Dose Uni</u>t</em>, and <em><u>Request Change to Standard Medication Route</u></em></p></li>
<li><p>Added the following reports: <em><u>Administration Schedule File Report</u>, <u>IV Solution Report</u>, <u>Local Possible Dosages Report</u>, <u>Medication Instruction File Report</u>, <u>Medication Route Mapping Report</u>, <u>Medication Route Mapping History Report</u>,</em> and <em><u>Strength Mismatch Report</u></em></p></li>
<li><p>Updated <u>Table of Contents</u>, <u>Index</u>, and <u>Glossary</u> <mark>REDACTED</mark></p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>09/97</p>
</blockquote></td>
<td></td>
<td></td>
<td>Original Release of User Manual</td>
</tr>
</tbody>
</table>

Pharmacy Data Management V. 1.0

July 2009 User Manual i

\<This page left blank for two-sided printing.\>

> ii Pharmacy Data Management V. 1.0 July 2009 User Manual

> Patch PSS\*1\*61 adds a new code “F” for NON REFILLABLE to the DEA, SPECIAL HDLG field of the DRUG file (#50), which will allow sites to mark drugs other than controlled substances or clozapine drugs as NON REFILLABLE.

> Patch PSS\*1\*81 adds a new code “E” to the DEA, SPECIAL HDLG field of the DRUG file (#50) to indicate that the drug is electronically billable. This will allow OTC drugs, supply items, and other drugs that are usually not billable to be marked for electronic billing.

> Patch PSS\*1\*131 adds a new code “U” to the DEA, SPECIAL HANDLING field of the DRUG file (#50) to indicate that the drug is used to treat certain conditions that are deemed “sensitive”. Specifically, the VA may not disclose any information on the following diseases: HIV, drug abuse, alcohol abuse, or sickle cell anemia without a signed consent from the patient. Drugs to mark with “U” include Antiretrovirals, Disulfiram, Naltrexone, and Methadone for maintenance or detox. When a signed Release of Information (ROI) is on file and the drug is marked with the new “U” DEA SPECIAL HANDLING CODE, the drug may be third party billable. Drugs must be manually marked with this new code, and this functionality works in conjunction with ROI modifications made in IB\*2\*384.

Pharmacy Data Management V. 1.0

July 2009 User Manual 27

# DEA Special Handling Code


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [DEA Special Handling Code](#dea-special-handling-code)
- [DEA, SPECIAL HDLG field effects on ePharmacy Billing:](#dea-special-hdlg-field-effects-on-epharmacy-billing)
- [DAW CODE field effects on ePharmacy Billing:](#daw-code-field-effects-on-epharmacy-billing)
- [Example: Setting the DAW CODE at the Prescription Level](#example-setting-the-daw-code-at-the-prescription-level)
- [Example: Setting the DAW CODE at the Drug File Level](#example-setting-the-daw-code-at-the-drug-file-level)
> Sites will need to determine all the nutritional supplements in their drug file and mark the DEA, SPECIAL HDLG field entry for all of their nutritional supplements drug file entries with an “N”. They will also need to append any entries that may be third party reimbursable with an “E”.
> Usually only Rx Only nutritional supplements are third party reimbursable.
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Select OPTION NAME: DRUG ENTER/EDIT PSS DRUG ENTER/EDIT Drug Enter/Edit</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Drug Enter/Edit</td>
</tr>
<tr class="even">
<td>Select DRUG GENERIC NAME: TRAZO</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lookup: GENERIC NAME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1 TRAZODONE 100MG TAB N/F</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2 TRAZODONE 50MG TAB</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CHOOSE 1-2: 1 TRAZODONE 100MG TAB N/F</td>
</tr>
<tr class="odd">
<td>*</td>
</tr>
<tr class="even">
<td>This entry is marked for the following PHARMACY packages:</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Outpatient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Non-VA Med</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>GENERIC NAME: TRAZODONE 100MG TAB//</td>
</tr>
<tr class="even">
<td>VA CLASSIFICATION:</td>
</tr>
<tr class="odd">
<td><strong>DEA, SPECIAL HDLG: 6// ?</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ANSWER MUST BE 1-6 CHARACTERS IN LENGTH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>THE SPECIAL HANDLING CODE IS A 2 TO 6 POSTION FIELD. IF APPLICABLE,</td>
</tr>
<tr class="even">
<td>A SCHEDULE CODE MUST APPEAR IN THE FIRST POSITION. FOR EXAMPLE,</td>
</tr>
<tr class="odd">
<td>A SCHEDULE 3 NARCOTIC WILL BE CODED '3A', A SCHEDULE 3 NON-NARCOTIC WILL BE</td>
</tr>
<tr class="even">
<td>CODED '3C' AND A SCHEDULE 2 DEPRESSANT WILL BE CODED '2L'.</td>
</tr>
<tr class="odd">
<td>THE CODES ARE:</td>
</tr>
<tr class="even">
<td>0 MANUFACTURED IN PHARMACY</td>
</tr>
<tr class="odd">
<td>1 SCHEDULE 1 ITEM</td>
</tr>
<tr class="even">
<td>2 SCHEDULE 2 ITEM</td>
</tr>
<tr class="odd">
<td>3 SCHEDULE 3 ITEM</td>
</tr>
<tr class="even">
<td>4 SCHEDULE 4 ITEM</td>
</tr>
<tr class="odd">
<td>5 SCHEDULE 5 ITEM</td>
</tr>
<tr class="even">
<td>6 LEGEND ITEM</td>
</tr>
<tr class="odd">
<td>9 OVER-THE-COUNTER</td>
</tr>
<tr class="even">
<td>L DEPRESSANTS AND STIMULANTS</td>
</tr>
<tr class="odd">
<td>A NARCOTICS AND ALCOHOLS</td>
</tr>
<tr class="even">
<td>P DATED DRUGS</td>
</tr>
<tr class="odd">
<td>I INVESTIGATIONAL DRUGS</td>
</tr>
<tr class="even">
<td>M BULK COMPOUND ITEMS</td>
</tr>
<tr class="odd">
<td>C CONTROLLED SUBSTANCES - NON NARCOTIC</td>
</tr>
<tr class="even">
<td>R RESTRICTED ITEMS</td>
</tr>
<tr class="odd">
<td>S SUPPLY ITEMS</td>
</tr>
<tr class="even">
<td>B ALLOW REFILL (SCH. 3, 4, 5 ONLY)</td>
</tr>
<tr class="odd">
<td>W NOT RENEWABLE</td>
</tr>
<tr class="even">
<td>F NON REFILLABLE</td>
</tr>
<tr class="odd">
<td>E ELECTRONICALLY BILLABLE</td>
</tr>
<tr class="even">
<td>N NUTRITIONAL SUPPLEMENT</td>
</tr>
<tr class="odd">
<td>U SENSITIVE DRUG</td>
</tr>
<tr class="even">
<td><strong>DEA, SPECIAL HDLG: U//</strong></td>
</tr>
</tbody>
</table>
> 28 Pharmacy Data Management V. 1.0 July 2009 User Manual

# DEA, SPECIAL HDLG field effects on ePharmacy Billing:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/002.png) If the DEA, SPECIAL HDLG field contains an “I” (Investigational), “S” (Supply), or “9” (OTC), the drug is NOT billable. However, if the same drug also contains the “E” (electronically billable), the drug becomes BILLABLE.

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/003.png) If the DEA, SPECIAL HDLG field contains an “M” or “0” (both designating a Compound Drug), the drug is NOT billable. If the same drug contains the “E” (electronically billable), the drug is STILL NOT billable.

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/004.png) If the DEA, SPECIAL HDLG field is NULL (empty), the drug is NOT billable.

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/005.png) If the DEA SPECIAL HDLG field contains a “U” (Sensitive Drug), the drug is only billable if there is a signed Release of Information (ROI) on file. This functionality works in conjunction with ROI modifications made in IB\*2\*384.

> Note that ALL other drugs are billable.

> Follow these guidelines to ensure proper electronic billing:

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/006.png) If an item is to be billed, then there must be an entry in the DEA, SPECIAL HDLG field.

> It is not necessary to include a numeric value; any value (other than the non-billable codes listed above) will allow ePharmacy to submit a bill.

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/007.png) Add an “E” to all items that contain “9”,“I” or “S”, but are actually billable. This will most often occur with Insulin and Glucose test strips, which are usually marked with a 9 but are, in fact, billable for most insurance companies.

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/008.png) Add a “U” to items that are used to treat a diagnosis deemed “sensitive”. Specifically, the VA may not disclose any information on the following diseases without a signed Release of Information (ROI): HIV, drug abuse, alcohol abuse, or sickle cell anemia. Drugs to mark with a “U” include Antiretrovirals, Disulfiram. Naltrexone, and Methadone for maintenance or detox.

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/009.png)Note: The NDF option, *Rematch/Match Single Drugs*, screens out those items with a DEA, SPECIAL HDLG code of “0”, “I”, or “M”. When sites receive NDF data updates that cause one of these items to be unmatched from NDF, they cannot use the *Rematch/Match Single Drugs* option to rematch if they have added “0”, “I”, or “M” to drugs like Antiretrovirals, Disulfiram, Naltrexone, or Methadone for maintenance or detox. Sites can either:

1.  Rematch to NDF using another option, or

Pharmacy Data Management V. 1.0

July 2009 User Manual 29

2.  Remove the DEA, SPECIAL HDLG code, use the *Rematch/Match Single Drugs*

> option, and then add the DEA, SPECIAL HDLG code back in.

> Patch PSS\*1\*90 adds a new multiple field to the DRUG file (#50) to store the latest National Drug Code (NDC) numbers that have been dispensed at window as well as by CMOP for a specific division. This way, when the next prescription is entered by the division for the same drug, the last used NDC is automatically retrieved from this new multiple, saved in the PRESCRIPTION file (#52), and sent to the third party payer through ECME. This field is populated automatically and does not require user input. Below is the multiple field and the fields under it:

> 32 NDC BY OUTPATIENT SITE

> .01 -OUTPATIENT SITE

1.  -LAST LOCAL NDC
2.  -LAST CMOP NDC

# DAW CODE field effects on ePharmacy Billing:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PSS\*1\*90 adds a new DAW CODE field to the DRUG file (#50). DAW stands for Dispense as Written, and refers to a set of ten NCPDP codes (0-9) that tells third party payers why a brand or generic product was selected to fill a prescription. See table below.

> DAW Code DAW Description

1.  No Product Selection Indicated
2.  Substitution Not Allowed by Prescriber
3.  Substitution Allowed-Patient Requested Product Dispensed
4.  Substitution Allowed-Pharmacist Selected Product Dispensed
5.  Substitution Allowed-Generic Drug Not in Stock
6.  Substitution Allowed-Brand Drug Dispensed as a Generic
7.  Override
8.  Substitution Not Allowed-Brand Drug Mandated by Law
9.  Substitution Allowed-Generic Drug Not Available in Marketplace
10. Other

> Since the VA primarily uses generic products, this has not been a major issue to date. The DAW CODE field default is 0, which means the physician did not specify whether to dispense a generic or brand name product. We anticipate getting some rejections from third parties for cases where we still dispense branded products, even though a generic is available in the marketplace. Our use of Coumadin<sup>®</sup> instead of generic Warfarin is one example.

> DAW codes are typically set for individual prescriptions, but can be set at the DRUG file (#50) level as well. An example scenario of each is given below.

> 30 Pharmacy Data Management V. 1.0 July 2009 User Manual

# Example: Setting the DAW CODE at the Prescription Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are informed that a prescription for Coumadin<sup>®</sup> was rejected for DAW reasons, you might try changing the DAW CODE of the prescription and resubmitting. The change can be made through the *Patient Prescription Processing* option or the *Edit Prescriptions* option in Outpatient Pharmacy V. 7.0. The DAW CODE will display for ePharmacy prescriptions. For original fills, this information can be edited by selecting screen field 21. For refills, the user must select screen field 20 (Refill Data), then select the refill number to be edited; the “DAW CODE:” prompt displays after the “DIVISION:” prompt. In the case of the Coumadin<sup>®</sup> reject, you may try changing the field to a 5 or a 1, then resubmitting to see if the claim gets processed. Both 5 and 1 are appropriate choices for the VA setting. Whether or not a claim will get rejected for these reasons and which code to use will vary from third party to third party. We are using brand name products, but are not charging for brand name products. The most common DAW codes are explained as follows:

> \#1: Physician stipulates that a particular brand be used.

> \#5: A brand name product is dispensed even though a generic product exists. Patient will be charged at the generic price.

# Example: Setting the DAW CODE at the Drug File Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are told that almost every prescription for Coumadin<sup>®</sup> is being rejected, you may choose to make the change at the DRUG file (#50) level. Editing the DAW Code field in the DRUG file (#50) for the Coumadin<sup>®</sup> entry will make a global change, such that each ePharmacy prescription filled for that product will use the DAW code you specify.

> Note: Ask your Pharmacy ADPAC to make the change at the DRUG file (#50) level.

> When using the *Drug Enter/Edit* option, a warning message is displayed if a discrepancy is found between the CS FEDERAL SCHEDULE field (#19) of the VA PRODUCT file (#50.68) and the DEA, SPECIAL HDLG field (#3) of the DRUG file (#50). The warning message says, "The CS Federal Schedule associated with this drug in the VA Product file represents a DEA, Special Handling code of XX", where XX is the DEA, SPECIAL HDLG code mapped to corresponding CS FEDERAL SCHEDULE code defined as follows (schedule I, IV and V are identical):

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CS FEDERAL</p>
<p>SCHEDULE</p>
</blockquote></th>
<th><blockquote>
<p>DEA, SPECIAL</p>
<p>HDLG</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Schedule I narcotics 1</td>
<td>1</td>
</tr>
<tr class="even">
<td>Schedule II narcotics 2</td>
<td>2A</td>
</tr>
<tr class="odd">
<td>Schedule II non-narcotics 2n</td>
<td>2C</td>
</tr>
<tr class="even">
<td>Schedule III narcotics 3</td>
<td>3A</td>
</tr>
<tr class="odd">
<td>Schedule III non-narcotics 3n</td>
<td>3C</td>
</tr>
<tr class="even">
<td>Schedule IV narcotics 4</td>
<td>4</td>
</tr>
<tr class="odd">
<td>Schedule V narcotics 5</td>
<td>5</td>
</tr>
</tbody>
</table>

Pharmacy Data Management V. 1.0

July 2009 User Manual 31

> Patch PSS\*1\*129 enhances the *Drug Enter/Edit* option to allow editing of the Numeric Dose and Dose Unit fields defined for Local Possible Dosages.

> If any of the following conditions can be determined at the time of entry, the Numeric Dose and Dose Unit fields for any defined Local Possible Dosage will not be presented for data entry.

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/010.png) Drugs associated with a dosage form that is excluded from dosage checks and the VA Product it is matched to will have the OVERRIDE DF DOSE CHK EXCLUSION field (#31) ) in the VA PRODUCT file (#50.68) file set to „No‟

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/011.png) Drug associated with a dosage form that is NOT excluded from dosage checks, but the VA Product that it is matched to will have the OVERRIDE DF DOSE CHK

> EXCLUSION field set to „Yes‟

> ![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/012.png) Drug is marked as a supply item („S‟ in DEA, SPECIAL HDLG field or assigned a VA Drug Class starting with an „XA‟).

> A warning will be provided if the DRUG file strength does not match the VA Product strength to which it is matched.

> Although ineligible for dosage checks, when editing a Local Possible Dosage for an inactive drug or a drug not matched to NDF, the Numeric Dose and Dose Unit fields will be displayed to the user for data entry.

> Example 1: Drug Enter/Edit (showing Strength mismatch message and new fields)

> 32 Pharmacy Data Management V. 1.0 July 2009 User Manual

> Example 1: Drug Enter/Edit (showing Strength mismatch message and new fields) - continued

> Select SYNONYM: \<ENTER\> MESSAGE: \<ENTER\> RESTRICTION: \<ENTER\> FSN: \<ENTER\>

> NDC: 54-3010-50// \<ENTER\> INACTIVE DATE: \<ENTER\>

> WARNING LABEL SOURCE is not 'NEW'.

> WARNING LABEL will be used until the WARNING LABEL SOURCE is set to 'NEW'. WARNING LABEL: 8// \<ENTER\>

> Current Warning labels for ACETAMINOPHEN ELIX. 120MG/5ML 4OZ

> Labels will print in the order in which they appear for local and CMOP fills:

> 8N Do not drink alcoholic beverages when taking this medication.

> 66N This medicine contains ACETAMINOPHEN. Taking more ACETAMINOPHEN than recommended may cause serious liver problems.

> 70N Do not take other ACETAMINOPHEN containing products at the same time without first checking with your doctor. Check all medicine labels carefully.

> Pharmacy fill card display: DRUG WARNING 8N,66N,70N

> NOTE: Because the NEW WARNING LABEL LIST field is empty, the warnings above are the warnings that our national data source distributes for this drug.

> Would you like to edit this list of warnings? N// \<ENTER\> O ORDER UNIT: \<ENTER\>

> PRICE PER ORDER UNIT: \<ENTER\> DISPENSE UNIT: \<ENTER\>

> DISPENSE UNITS PER ORDER UNIT: 1// \<ENTER\> PRICE PER DISPENSE UNIT: 0.000

points to ACETAMINOPHEN 160MG/5ML ELIXIR in the National Drug file.

> This drug has already been matched and classified with the National Drug file. In addition, if the dosage form changes as a result of rematching, you will have to match/rematch to Orderable Item.

> Do you wish to match/rematch to NATIONAL DRUG file? No// \<ENTER\> (No) Just a reminder...you are editing ACETAMINOPHEN ELIX. 120MG/5ML 4OZ.

> Strength from National Drug File match =\> 160 MG/5ML Strength currently in the Drug File =\> 120

> Press Return to Continue: \<ENTER\>

> Strength =\> 120 Unit =\>

> POSSIBLE DOSAGES:

> DISPENSE UNITS PER DOSE: 2 DOSE: 240 MG/5 ML PACKAGE: I

> LOCAL POSSIBLE DOSAGES:

> LOCAL POSSIBLE DOSAGE: ONE TEASPOONFUL PACKAGE: O

Pharmacy Data Management V. 1.0

July 2009 User Manual 33

> Example 1: Drug Enter/Edit (showing Strength mismatch message and new fields) - continued

![](pss-1-131-user-manual-epharmacy-phase-4-iteration-ii-change-pages/013.png)

> 34 Pharmacy Data Management V. 1.0 July 2009 User Manual