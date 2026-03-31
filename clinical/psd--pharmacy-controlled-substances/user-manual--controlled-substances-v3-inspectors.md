---
title: Controlled Substances Version 3 Inspector's User Manual (Updated PSD*3*82)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Inspector's  (Updated PSD*3*82)
app_code: PSD
app_name: "Pharmacy: Controlled Substances"
section: CLI
app_status: active
pkg_ns: PSD
patch_ver: 3
patch_id: PSD*3
group_key: "PSD:PSD:3"
file_numbers: []
security_keys: []
menu_options: 1
description: > The Controlled Substances (CS) computer software package V. 3.0 is one segment of the Veterans Health Information Systems and Technology Architecture (VISTA) in use at the Department of Veterans Affairs Medical Centers (VAMCs). This package provides functionality to monitor and track the receipt,
audience: 
keywords: 
  - report
  - controlled
  - date
  - substances
  - pharmacy
  - inspector
  - table
  - contents
  - trakker
  - green
page_count: 0
word_count: 5796
section_count: 17
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Controlled_Substances/psd_3_insp_um_r0618.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Controlled_Substances/psd_3_insp_um_r0618.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=86"
---

> ![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/001.png)

CONTROLLED SUBSTANCES (CS)

####### INSPECTOR’S USER MANUAL 

March 1997

(Revised June 2018)

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Orientation](#orientation)
- [Controlled Substances Inspector Menu](#controlled-substances-inspector-menu)
  - [Controlled Substance Balances Report](#controlled-substance-balances-report)
  - [Inspector’s Log for Controlled Substances](#inspectors-log-for-controlled-substances)
  - [Inspector’s Log by Rec’d Date](#inspectors-log-by-recd-date)
  - [Inventory Sheet Print](#inventory-sheet-print)
  - [Barcode TRAKKER for CS Inspections](#barcode-trakker-for-cs-inspections)
    - [Load Software and Insp. Inventory into TRAKKER](#load-software-and-insp-inventory-into-trakker)
    - [Send Inspections Inventory TRAKKER Data to DHCP](#send-inspections-inventory-trakker-data-to-dhcp)
  - [Place Green Sheet on Hold](#place-green-sheet-on-hold)
  - [Remove Green Sheet from Hold](#remove-green-sheet-from-hold)
  - [Under Inspector’s Review—Green Sheets](#under-inspectors-reviewgreen-sheets)
  - [Green Sheet History](#green-sheet-history)
- [CS Monitoring Menu](#cs-monitoring-menu)
  - [CS Application Security Key Report](#cs-application-security-key-report)
  - [CS Balance Adjustments Report](#cs-balance-adjustments-report)
  - [CS RXs by Same Person Report](#cs-rxs-by-same-person-report)
  - [Label Reprint for CS RXs Report](#label-reprint-for-cs-rxs-report)
  - [Option Access by User](#option-access-by-user)
  - [Partial Request for CS RXs Report](#partial-request-for-cs-rxs-report)
  - [Patients Without VA Visit Report](#patients-without-va-visit-report)
- [# # Glossary](#glossary)
- [Index](#index)
The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revised Pages</strong></td>
<td><strong>Patch Number</strong></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>06/2018</td>
<td><a href="#PSD_3_82"><u>25</u></a></td>
<td>PSD*3*82</td>
<td><p>Added NAOU Usage Report [PSD NAOU USAGE] option to the PSD TECH ADV key.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2013</td>
<td>i, ii, 25-26, 27-28</td>
<td>PSD*3*76</td>
<td><p>Updated Glossary with description of patch’s new security key PSDRPH</p>
<p>Updated Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>25-26</td>
<td>PSD*3*71</td>
<td><p>Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2010</td>
<td>24-26, 28</td>
<td>PSD*3*69</td>
<td><p>Added description of patch’s new security key PSD TECH ADV, and PSD TECH key.</p>
<p>Added PSD TECH ADV and PSD TECH key to index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/03</td>
<td>All</td>
<td>PSD*3*41</td>
<td>Updated the manual to Standards. Added the <em>CS Monitoring Menu</em> options.</td>
</tr>
<tr class="odd">
<td>03/97</td>
<td></td>
<td></td>
<td>Original Released Inspector’s Manual.</td>
</tr>
</tbody>
</table>
\<This page is intentionally left blank.\>
Table of Contents
\<This page is intentionally left blank.\>

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Controlled Substances (CS) computer software package V. 3.0 is one segment of the Veterans Health Information Systems and Technology Architecture (V*IST*A) in use at the Department of Veterans Affairs Medical Centers (VAMCs). This package provides functionality to monitor and track the receipt, inventory, and dispensing of all controlled substances. It also provides the pharmacy with the capability to define a controlled substance location and a list of controlled substances to maintain a perpetual inventory.

> This package provides the capability for pharmacy personnel to receive a Controlled Substances order, automatically update the quantity on hand, and view a receipt history. Nursing personnel are provided with the ability to request orders for Controlled Substances via on-demand requests. Pharmacy may dispense controlled substances via the software automating all necessary documents (VA FORMs 10-2321 and 10-2638) to complete an order request. The software provides functionality to record Automated Management Information System (AMIS) and cost data, address returns to stock, destructions, order cancellations, transfers between locations, and log outpatient prescriptions.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

> Example: *Controlled Substance Balances Report* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them.

> Example: “Select INPATIENT SITE NAME” indicates a screen prompt.

- Responses in bold face indicate what the user is to type in.

> Example: Okay to Continue? No// YES.

- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be pressed. \<Tab\> indicates that the Tab key must be pressed.

> Example: Press \<Tab\> to move the cursor to the next field.

> Press \<Enter\> to select the default.

- 
- ![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/002.png)Note: Indicates especially important or helpful information.
- ![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/003.png) Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.

Example: ![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/004.png) The PSDMGR key is required. Please contact the Pharmacy Supervisor.

- ?, ??, ??? One, two, or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.
- ^ Up Caret (arrow or a circumflex) and pressing \<Enter\> can be used to exit the current option.

# Controlled Substances Inspector Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD INSPECTOR MENU\]

This menu contains some options associated with a Controlled Substances narcotic inspection. This menu should be assigned to the CS Inspector prior to starting the inspection process. Access to this menu should be removed after the inspection is completed.

Example: Controlled Substances Inspector Menu

Select Controlled Substances Inspector Menu Option: ?

Controlled Substance Balances Report

Inspector's Log for Controlled Substances

Inspector's Log by Rec'd Date

Inventory Sheet Print

Barcode TRAKKER for CS Inspections ...

Place Green Sheet on Hold

Remove Green Sheet from Hold

Under Inspector's Review - Green Sheets

Green Sheet History

## Controlled Substance Balances Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD NAOU BALANCE REPORT\]

The *Controlled Substance Balances Report* option will show the balance for one or all drugs on a ward.

## Inspector’s Log for Controlled Substances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSD PRINT INSPECTOR LOG\]

The *Inspector’s Log for Controlled Substances* option will allow Pharmacy personnel to list all active Green Sheets and ones that are flagged ready for pharmacy pickup.

## Inspector’s Log by Rec’d Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD INSP LOG BY RECD DATE\]

The *Inspector’s Log by Rec’d Date* option will allow pharmacy personnel to list all dispensing transactions for a Narcotic Area of Use (NAOU) received within a given date range. It also includes any Returns to Stock.

## Inventory Sheet Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD INVEN SHEET PRT\]

The *Inventory Sheet Print* option prints an inspector’s report that is used to inventory on-hand balances within a pharmacy-dispensing site (vault).

## Barcode TRAKKER for CS Inspections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD IRL INSP MENU\]

The *Barcode TRAKKER for CS Inspections* menu contains the access to download an Interactive Reader Language (IRL) program and the vault inventory to the TRAKKER, and also upload inventory data from the TRAKKER to V*IST*A.

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/005.png) The PSDMGR key is required. Please contact the Pharmacy Supervisor.

Example: Barcode TRAKKER for CS Inspections Menu

Select Controlled Substances Inspector Menu Option: ?

Load Software and Insp. Inventory into TRAKKER

Send Inspections Inventory TRAKKER Data to DHCP

### Load Software and Insp. Inventory into TRAKKER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD IRL INSPECTOR INV\]

The *Load Software and Insp. Inventory into TRAKKER* option enables pharmacy personnel to download an IRL program to the TRAKKER, download the vault drug balances to the TRAKKER, and perform the inventory via the TRAKKER.

Example: Load Software and Insp. Inventory into TRAKKER

Turn the TRAKKER on and the following will be displayed:

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/006.png)

-----------------------------------------*example follows*-----------------------------------------

Example: Load Software and Insp. Inventory into TRAKKER (continued)

Select Controlled Substances Inspector Menu Option: BARcode TRAKKER for CS Inspections

Load Software and Insp. Inventory into TRAKKER

Send Inspections Inventory TRAKKER Data to DHCP

Select Barcode TRAKKER for CS Inspections Option: LOAd Software and Insp. Inventory into TRAKKER

Select Dispensing site to Inventory: INPATIENT//\<Enter\>

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/007.png)Note: This prompt is displayed if more than one dispensing vault is defined for the site. If the default dispensing site is selected upon entering the *Controlled Substances Menu* option, it will be offered as the default.

Compiling inventory data...

DEVICE: TRAKKERSL

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/008.png)

Awaiting TRAKKER signal

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/009.png)

-----------------------------------------*example follows*-----------------------------------------

Example: Load Software and Insp. Inventory into TRAKKER (continued)

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/010.png)

You can now disconnect the TRAKKER.

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/011.png)

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/012.png)

*\[Scan your user ID barcode\]*

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/013.png)Note: The system will check the files for a match. If no match is found, the system will inform the user that this drug is not in the files. If a match is found, the drug name and quantity will be displayed as follows:

-----------------------------------------*example follows*-----------------------------------------

Example: Load Software and Insp. Inventory into TRAKKER (continued)

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/014.png)

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/015.png)Note: At this point, an N can be entered to adjust the count.

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/016.png)

### Send Inspections Inventory TRAKKER Data to DHCP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD IRL INSP DATA\]

The *Send Inspections Inventory TRAKKER Data to DHCP* option enables pharmacy personnel to upload the inventory data from the TRAKKER to V*IST*A.

Example: Load Software and Insp. Inventory into TRAKKER

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/017.png)

b

Select Controlled Substances Inspector Menu Option: <u>SEN</u>d Inspections Inventory TRAKKER Data to DHCP

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/018.png)Note: Use the Send data to DHCP option on the TRAKKER at this time.

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/019.png)

-----------------------------------------*example follows*-----------------------------------------

Example: Load Software and Insp. Inventory into TRAKKER (continued)

*\[When you press F1, the data will print across the terminal screen\]*

P123-45-6767^\>94/08/22:10:23:44\*12

P123-45-6767^614^DIAZEPAM 2MG TAB^337^^^^335^^^^\>94/08/22:10:24:07

P123-45-6767^614^DIAZEPAM 2MG TAB^335^^^^^^^^\>94/08/22:10:24:22

P123-45-6767^615^DIAZEPAM 10MG TAB^421^^^^^^^^\>94/08/22:10:24:22

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/020.png)

\<Enter\>

Updating DHCP now...done

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/021.png)Note: Anyone holding the appropriate security key will also receive a MailMan message on the adjustment.

Example: MailMan Message

Subj: CS PHARM TRAKKER ADJUSTMENT \[#3194\] 22 Aug 94 13:23 7 Lines

From: CONTROLLED SUBSTANCES PHARMACY in 'IN' basket. Page 1

------------------------------------------------------------------------------

CS PHARM TRAKKER adjustment/error has been filed.

Adjustment/Error Date/Time: AUG 22,1994@13:23:46

Dispensing Site: INPATIENT

Drug: DIAZEPAM 2MG TAB

Quantity Adjusted: -3

Adjusted by: CSPHARMACIST,ONE

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/022.png)Note: Data should be cleared out or deleted from the TRAKKER to avoid duplication of inventory information.

After the upload is completed, the user should clear the TRAKKER’s data files. To accomplish this, press \<Ctrl\> \<Enter\> \<E\> to end the IRL session, then press \<Ctrl\> \<Enter\> \<C\>. The user will be asked if the data files are to be cleared, enter Y (YES).

To restart the IRL session press \<Ctrl\> \<Enter\> \<B\>.

## Place Green Sheet on Hold

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD INSP PLACE HOLD\]

The *Place Green Sheet on Hold* option provides the Controlled Substances Narcotic Inspector the tools to place a Green Sheet on hold for review. The status of this Green Sheet will remain UNDER REVIEW BY INSPECTOR until the review is completed. This option should be utilized when removing both the Green Sheet and drug from an NAOU for further investigation.

## Remove Green Sheet from Hold

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD INSP REMOVE HOLD\]

The *Remove Green Sheet from Hold* option provides the Controlled Substances Narcotic Inspector the tools to replace a Green Sheet back on the NAOU after review. The status of the Green Sheet will return to DELIVERED - ACTIVELY ON NAOU. This option should be utilized when returning both the Green Sheet and drug to an NAOU after completing the investigation.

## Under Inspector’s Review—Green Sheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD PRT GS INSP HOLD\]

The *Under Inspector’s Review – Green Sheets* option lists all Green Sheets placed on hold for review by a Controlled Substances Narcotic Inspector.

## Green Sheet History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSD GS HISTORY\]

The *Green Sheet History* option provides pharmacy with a detailed account of every transaction affecting this VA FORM 10-2638. This history may be displayed to the user’s screen or directed to a printer.

# CS Monitoring Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSD NM MENU\]

The *CS Monitoring Menu* option is a standalone menu that contains the CS Monitoring reports to help facilitate the monitoring of controlled substances and Schedule II narcotics. The menu should be assigned to the appropriate CS Inspectors and Pharmacy Managers at the site. The menu options are shown below.

Example: CS Monitoring Menu

Select CS Monitoring Menu Option: ?

CS Application Security Key Report

CS Balance Adjustments Report

CS RXs by Same Person Report

Label Reprint for CS RXs Report

Option Access By User

Partial Request for CS RXs Report

Patients Without VA Visit Report

## CS Application Security Key Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSD NM SECURITY KEY\]

The *CS Application Security Key Report* option lists holders of the PSJ RPHARM and/or PSDMGR security keys. The holders of these keys have the ability to override discrepancies, make controlled substance vault inventory adjustments and transfer medications between vaults. The list requires routine monitoring and validation for accuracy.

Example: CS Application Security Key Report

Select CS Monitoring Menu Option: CS Application Security Key Report

This report lists current holders of the

PSJ RPHARM and/or PSDMGR security keys.

Okay to Continue? No// YES

DEVICE: HOME// \<Enter\> UCX DEVICE Right Margin: 80// \<Enter\>

Compiling report, please wait ...

-----------------------------------------*report follows*------------------------------------------

Example: CS Application Security Key Report (continued)

CS Monitoring - Security Key Report

SECURITY KEY: PSDMGR & PSJ RPHARM

Station: 677 Report Run Date: Feb 27, 2003@13:34:32 PAGE: 1

================================================================================

Name Title Termination Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SERVICE/SECTION: INFO RESOURCES MANAGEMENT SERV

CSSPECIALIST,ONE COMPUTER SPECIALIST

SERVICE/SECTION: INFORMATION MANAGEMENT

CSSPECIALIST,TWO COMPUTER SPECIALIST

SERVICE/SECTION: RX PHARMACY SERVICE

CSPHARMACIST,TWO PHARMACIST

CSPHARMACIST,THREE PHARMACIST

CSPHARMACIST,FOUR CHIEF,PHARMACY SERVICE

CS Monitoring - Security Key Report

SECURITY KEY: PSDMGR

Station: 677 Report Run Date: Jan 29, 2003@13:34:32 PAGE: 1

================================================================================

Name Title Termination Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SERVICE/SECTION: INFO RESOURCES MANAGEMENT SERV

CSSPECIALIST,THREE COMPUTER SPECIALIST

CS Monitoring - Security Key Report

SECURITY KEY: PSJ RPHARM

Station: 677 Report Run Date: Jan 29, 2003@13:34:32 PAGE: 1

================================================================================

Name Title Termination Date

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

SERVICE/SECTION: BEHAVIORAL HEALTH

CSPHARMACIST,FIVE PHARM D CANDIDATE

CSPHARMACIST,SIX STAFF PHARMACIST

SERVICE/SECTION: CLINICAL SUPPORT

CSPHARMACIST,SEVEN PHARMACIST

CSPHARMACIST,EIGHT CLINICAL PHARMACIST

SERVICE/SECTION: CONSOLIDATED MAIL OUT PHARMACY

CSPHARMACIST,NINE PHARMACIST

SERVICE/SECTION: FISCAL

CSDIRECTOR,ONE ISC DIRECTOR

SERVICE/SECTION: INFORMATION MANAGEMENT

CSSPECIALIST,FOUR INTEGRATION SPECIALIST

SERVICE/SECTION: RX PHARMACY SERVICE

CSPHARMACIST,TEN PHARMACY STUDENT JUN 10, 1998

CSPHARMACIST,ELEVEN PROGRAM

CSPHARMACIST,TWELVE PHARMACY TECH

CSPHARMACIST,THIRTEEN PHARMACIST

CSPHARMACIST,FOURTEEN PHARMACY STUDENT OCT 13, 2000

CSPHARMACIST,FIFTEEN PHARMACY STUDENT

CSPHARMACIST,SIXTEEN PHARMACY STUDENT AUG 31, 2000

CSPHARMACIST,SEVENTEEN PHARMACY TECH

## CS Balance Adjustments Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSD NM CS ADJ\]

The *CS Balance Adjustments Report* option lists Drug Accountability transactions in which the controlled substances vault inventory balance was manually adjusted during the date range entered. The adjuster and reason will display on the report for the CS Inspectors and Pharmacy Managers to review regularly for appropriateness and authorization.

Example: CS Balance Adjustments Report

Select CS Monitoring Menu Option: CS BALance Adjustments Report

This report lists Drug Accountability Balance Adjustments

made for the Inpatient Site Pharmacy Location(s) entered.

Select INPATIENT SITE NAME: XXXXXX

Select 'ALL' XXXXXX Pharmacy locations? Yes// \<Enter\> NOTE: If No, the Select XXXXXX Pharmacy Location prompt displays.

Start with Balance Adjustment Date: 1-1-00 (JAN 01, 2000)

End with Balance Adjustment Date: 1-5-00 (JAN 05, 2000)

Okay to Continue? No// YES

This report should be queued to run during non-peak hours.

DEVICE: HOME// \<Enter\> \*\*\* Right Margin: 80// \<Enter\>

Compiling report, please wait ...

CS Monitoring - Balance Adjustments Report

Inpatient Site: XXXXXX all Pharmacy Locations

Balance Adjustments made: JAN 01, 2000 thru JAN 05, 2000

Report Run: Feb 05, 2003@14:46 PAGE: 1

================================================================================

Trans. \# Date Quantity Drug

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Pharmacy Location: 1-3C

NO DATA FOUND

Pharmacy Location: 1-4A

NO DATA FOUND

Pharmacy Location: 1-4C

NO DATA FOUND

Pharmacy Location: 1-5C

NO DATA FOUND

Pharmacy Location: 2-2

NO DATA FOUND

Pharmacy Location: 2-3B

NO DATA FOUND

Enter RETURN to continue or '^' to exit: \<Enter\>-----------------------------------------*report continues*----------------------------------------

Example: CS Balance Adjustments Report (continued)

CS Monitoring - Balance Adjustments Report

Inpatient Site: XXXXXX all Pharmacy Locations

Balance Adjustments made: JAN 01, 2000 thru JAN 05, 2000

Report Run: Feb 05, 2003@14:47 PAGE: 2

================================================================================

Trans. \# Date Quantity Drug

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Pharmacy Location: EMERGENCY NARCOTIC BOX

NO DATA FOUND

Pharmacy Location: ICU

NO DATA FOUND

Pharmacy Location: LAB

NO DATA FOUND

Pharmacy Location: MASTER VAULT

TRANSACTOR: CSPHARMACIST,EIGHTEEN

409112 JAN 03, 2000@12:56 20 MIDAZOLAM HCL 5MG/ML INJ 1ML

Reason: RETURNED TO STOCK FROM ICU--NOT USED

410131 JAN 03, 2000@15:45 5 MORPHINE SO4 1MG/ML INJ 30ML

Reason: RETURNED TO STOCK FROM 1-4A

Enter RETURN to continue or '^' to exit: \<Enter\>

CS Monitoring - Balance Adjustments Report

Inpatient Site: XXXXXX all Pharmacy Locations

Balance Adjustments made: JAN 01, 2000 thru JAN 05, 2000

Report Run: Feb 05, 2003@14:47 PAGE: 3

================================================================================

Trans. \# Date Quantity Drug

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

411182 JAN 04, 2000@08:29 10 METHYLPHENIDATE HCL 5MG TAB

Reason: RETURNED TO STOCK FROM WARD 3-1B-OUTDATED

411166 JAN 04, 2000@12:46 -100 LORAZEPAM 2MG TAB

Reason: CHANGED TO U/D FOR SPECIAL PACKAGING

411167 JAN 04, 2000@12:46 100 LORAZEPAM 2MG TAB UD

Reason: CHANGED FROM BULK FOR U/D PACKAGING

Pharmacy Location: OPT WORKING STOCK

NO DATA FOUND

Pharmacy Location: RECOVERY ROOM

NO DATA FOUND

Pharmacy Location: SURG RM307

NO DATA FOUND

Pharmacy Location: SURG RM308

NO DATA FOUND

## CS RXs by Same Person Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSD NM RX SAME PERSON\]

The *CS RXs by Same Person Report* option lists the controlled substance prescriptions that were entered, finished and released by the same person for the date range entered. Different pharmacists in the prescription filling process normally perform these functions. This process is frequently necessary on off-shifts and weekends also. Inspectors and Pharmacy Managers should monitor this activity very closely.

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/023.png)Note: This report should be queued to run during non-peak hours.

Example: CS RXs by Same Person Report

Select CS Monitoring Menu Option: CS RXs by Same Person Report

This report lists CS prescriptions that were entered,

finished and released by the same person.

Select Outpatient Division: XXXXXX 677

Select another Outpatient Division: XXXXXXXXXXX 677A4

Select another Outpatient Division: \<Enter\>

Start with Fill Date: 8-27-98 (AUG 27, 1998)

End with Fill Date: 8-27-98 (AUG 27, 1998)

Include RXs with CS schedule(s): (2-5): 2-5// ?

Enter range or combination of DEA Codes (schedules) between 2 and 5.

Enter '^' to exit.

Include RXs with CS schedule(s): (2-5): 2-5// 2-4

Okay to Continue? No// YES

This report should be queued to run during non-peak hours.

DEVICE: HOME// \<Enter\> UCX DEVICE Right Margin: 80// \<Enter\>

Compiling report, please wait ...

CS Monitoring - RX by Same Person Report

Outpatient Division(s): 677, 677A4

Fill Date range: AUG 27, 1998 thru AUG 27, 1998

Controlled Substance schedule(s): 2,3,4

Station: XXXXXX Report Run Date: Feb 03, 2003@14:18:06 PAGE: 1

================================================================================

Pharmacy User

RX# Fill Date Drug Name

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CSPHARMACIST,NINETEEN

1231550 AUG 27, 1998 NARCOTIC HCL 5MG TAB

CSPHAMACIST,TWENTY

1231555 AUG 27, 1998 CONTROLLED SUB 10MG CAP

1231567 AUG 27, 1998 NARCOTIC 80MG CAP

## Label Reprint for CS RXs Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSD NM RX REPRINT\]

The *Label Reprint for CS RXs Report* option lists the controlled substance prescriptions for which a prescription label reprint was requested. An individual could fill the same prescription more than once and be diverting prescription drugs. CS Inspectors and Pharmacy Managers should monitor this activity very closely.

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/024.png)Note: This report should be queued to run during non-peak hours.

Example: Label Reprint for CS RXs Report

Select CS Monitoring Menu Option: LAbel Reprint for CS RXs Report

This report lists CS Prescriptions with label reprint

request activity within the issue date range entered.

Select Outpatient Division: XXXXXX 677

Select another Outpatient Division: XXXXXXXXXXX 677A4

Select another Outpatient Division: \<Enter\>

Start with Issue Date: 1-5-00 (JAN 05, 2000)

End with Issue Date: 1-6-00 (JAN 06, 2000)

Include RXs with CS schedule(s): (2-5): 2-5// 2-4

Okay to Continue? No// YES

This report should be queued to run during non-peak hours.

DEVICE: HOME// \<Enter\> \*\*\* Right Margin: 80// \<Enter\>

Compiling report, please wait ...

CS Monitoring - Label Reprint Request Report

Outpatient Division(s): 677, 677A4

Issue Date range: JAN 05, 2000 thru JAN 06, 2000

Controlled Substance schedule(s): 2,3,4

Division: XXXXXXXXXXX Report Run Date: Feb 05, 2003@08:32:19 PAGE: 1

================================================================================

RX# Activity Log Date Initiator of Activity

Activity Log Comment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ALPRAZOLAM 0.5MG TAB

1314827B JAN 06, 2000@16:34:08 CSPHARMACIST,TWENTYONE

NNNNN (1 COPIES)

1314827B MAR 16, 2000@08:35:53 CSPHARMACIST,TWENTYTWO

NEED LABEL (1 COPIES)

-----------------------------------------*report continues*----------------------------------------

Example: Label Reprint for CS RXs Report (continued)

CS Monitoring - Label Reprint Request Report

Outpatient Division(s): 677, 677A4

Issue Date range: JAN 05, 2000 thru JAN 06, 2000

Controlled Substance schedule(s): 2,3,4

Division: XXXXXX Report Run Date: Feb 05, 2003@08:32:19 PAGE: 1

================================================================================

RX# Activity Log Date Initiator of Activity

Activity Log Comment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CLONAZEPAM 0.5MG TAB

1118067F JAN 13, 2000 CSPHARMACIST,TWENTYTHREE

GROUP REPRINT

PHENOBARBITAL 65MG TAB

1112651A APR 10, 2000@12:50:18 CSPHARMACIST,TWENTYFOUR

label lost (1 COPIES)

## Option Access by User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[XUOPTWHO\]

The *Option Access by User* option prompts for a menu option and then lists the users who can access this option. The list can be printed with or without the menu paths to the option.

Example: Option Access by User

Select CS Monitoring Menu Option: OPtion Access By User

Select OPTION NAME: PSD MENU Controlled Substances Menu

Show menu paths? No// \<Enter\> (No)

DEVICE: HOME// \<Enter\> UCX DEVICE Right Margin: 80// \<Enter\>

Page 1 Feb 27, 2003 7:33:09 am

Access to 'Controlled Substances Menu' \[PSD MENU\]

USER NAME LAST ON PRIMARY MENU

------------------------- -------- ----------------------------------------

CSPHARMACIST,TWENTYFIVE 02/26/03 PSZPHARM (Secondary menu) 132M-U

CSPHARMACIST,TWENTYSIX 02/26/03 PSZPHARM (Secondary menu) 132MU

CSPHARMACIST,TWENTYSEVEN 02/26/03 PSZSUPV (Secondary menu) 119

CSPHARMACIST,TWENTYEIGHT 02/26/03 PSZPHARM (Secondary menu) 119

CSPHARMACIST,TWENTYNINE 02/27/03 PSZPHARM (Secondary menu) 119

CSPHARMACIST,THIRTY 02/26/03 PSZTECH (Secondary menu) 132M-U

Press return to continue or '^' to escape ^

## Partial Request for CS RXs Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSD NM RX PARTIAL\]

The *Partial Request for CS RXs Report* option lists the controlled substance prescriptions for which a prescription partial fill was requested. An individual could partially fill the same prescription more than once and be diverting prescription drugs. CS Inspectors and Pharmacy Managers should monitor this activity very closely.

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/025.png)Note: This report should be queued to run during non-peak hours.

Example: Partial Request for CS RXs Report

Select CS Monitoring Menu Option: PARtial Request for CS RXs Report

This report lists CS Prescriptions with Partial Fill

request activity within the fill date range entered.

Select Outpatient Division: XXXXXX 677

Select another Outpatient Division: XXXXXXXXXXX 677A4

Select another Outpatient Division: \<Enter\>

Start with Fill Date: 1-1-00 (JAN 01, 2000)

End with Fill Date: 1-3-00 (JAN 03, 2000)

Include RXs with CS schedule(s): (2-5): 2-5// \<Enter\>

Okay to Continue? No// YES

This report should be queued to run during non-peak hours.

DEVICE: HOME// \<Enter\> \*\*\* Right Margin: 80// \<Enter\>

Compiling report, please wait ...

CS Monitoring - Partial Request Report

Outpatient Division(s): 677, 677A4

Fill Date range: JAN 01, 2000 thru JAN 03, 2000

Controlled Substance schedule(s): 2,3,4,5

Division: XXXXXXXXXXX Report Run Date: Feb 05, 2003@09:05:29 PAGE: 1

================================================================================

RX# Activity Log Date Initiator of Activity

Activity Log Comment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CODEINE 30/ACETAMINOPHEN 300MG TAB

171027 MAR 17, 2000 CSPHARMACIST,TWENTYONE

OK'ED BY DR EXXXXXX ON 3-17-00. PT CLAIMS MED NEVER ARRIVED.

PAREGORIC

119827A JAN 04, 2000 CSPHARMACIST,TWENTYTWO

OWE PATIENT.

-----------------------------------------*report continues*----------------------------------------

Example: Partial Request for CS RXs Report (continued)

CS Monitoring - Partial Request Report

Outpatient Division(s): 677, 677A4

Fill Date range: JAN 01, 2000 thru JAN 03, 2000

Controlled Substance schedule(s): 2,3,4,5

Division: XXXXXX Report Run Date: Feb 05, 2003@09:05:29 PAGE: 1

================================================================================

RX# Activity Log Date Initiator of Activity

Activity Log Comment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

LORAZEPAM 1MG TAB

1161823 JAN 05, 2000 CSPHARMACIST,THIRTYTHREE

13 - RCVD FROM PYXIS

PROPOXYPHENE N 100/APAP 650MG TAB

1111458D FEB 26, 2000 CSPHARMACIST,THIRTYFOUR

13-MED SENT TO WRONG PT. (N8838)

1111372 DEC 02, 1999 CSPHARMACIST,THIRTYFIVE

13--DISPENSED FROM PYXIS 11/30--DR KXXXXXXX

VALSARTAN 80MG CAP

1111825 NOV 01, 1999 CSPHARMACIST,THIRTYSIX

08

## Patients Without VA Visit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSD NM RX WITHOUT VA\]

The *Patients Without VA Visit Report* option prompts for a date range and then lists patients that receive prescriptions but have not had a VA clinic visit within one year of a prescription release. This option excludes prescriptions that were released on the same day as a discharge and within a user defined discharge date range. Patients in Fee Basis and Aid and Attendance programs may be included on the list and should be reviewed. This report does display a message of the prescriptions that meet the sort criteria and were released after the entered date of death for that patient. This list represents a potential diversion tactic that could be employed to prevent detection and suspicion.

![](controlled-substances-version-3-inspector-s-user-manual-updated-psd-3-82/026.png)Note: This report should be queued to run during non-peak hours.

Example: Patients Without VA Visit Report

Select CS Monitoring Menu Option: PATients Without VA Visit Report

This report lists released RXs without a visit within 12 months of the

RX Release date. Excluding RXs released on the same day as a discharge

and within a user defined discharge date range.

-----------------------------------------*report continues*----------------------------------------

Example: Patients Without VA Visit Report (continued)

Select Outpatient Division: XXXXXX 677

Select another Outpatient Division: \<Enter\>

Start with RX Release Date: T-1M (JAN 27, 2003)

End with RX Release Date: T (FEB 27, 2003)

Number of days to ignore BEFORE discharge date: (0-3): 0// ?

Enter number of days (0-3) to ignore BEFORE discharge date. Enter '^'

to Exit.

Number of days to ignore BEFORE discharge date: (0-3): 0// 1

Number of days to ignore AFTER discharge date: (0-3): 0// ?

Enter number of days (0-3) to ignore AFTER discharge date. Enter '^' to

Exit.

Number of days to ignore AFTER discharge date: (0-3): 0// 2

Screen for controlled substance RXs? Yes// \<Enter\> YES

Okay to Continue? No// YES

This report should be queued to run during non-peak hours.

DEVICE: HOME// \<Enter\> \*\*\* Right Margin: 80// \<Enter\>

Compiling report, please wait

CS Monitoring - No Visits within 12 months of RX Release Report

Outpatient Division(s): 677

Prescriptions released: JAN 03, 2000 thru JAN 03, 2000

Exclude RXs released: 1 day(s) before 2 day(s) after a discharge date

Division: XXXXXX Report Run Date: Feb 11, 2003@17:18:33 PAGE: 1

================================================================================

RX# Release Date Drug

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RX PATIENT STATUS: FEE A&A

PATIENT NAME: CSPATIENT,ONE (11-1111)

1119358 JAN 03, 2000@10:20:21 LEVOTHYROXINE NA (SYNTHROID) 0.075MG TAB

\* Date of Death JAN 1,2000 before RX Release Date!

RX PATIENT STATUS: PENSION NSC

PATIENT NAME: CSPATIENT,ONE (11-1111)

1117993A JAN 03, 2000@10:20:21 NIFEDIPINE (ADALAT CC) 30MG SA TAB

\* Date of Death JAN 1,2000 before RX Release Date!

RX PATIENT STATUS: SELF MED

PATIENT NAME: CSPATIENT,TWO (22-2222)

1291358 JAN 03, 2000@10:20:21 LEE NA (SYNTHROID) 0.075MG TAB

PATIENT NAME: CSPATIENT,THREE (12-3456)

Enter RETURN to continue or '^' to exit: ^

# # # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Completion Status A review status is attached to each Controlled Substances Green Sheet returned to pharmacy. The following are valid:

> NO DISCREPANCY—No discrepancy found.

> TURN IN FOR DESTRUCTION—CS drug turned in to be destroyed.

> RETURNED TO STOCK—CS Drug returned to stock. The dispensing site inventory balance will be updated.

> MATH ERROR—CS drug discrepancy found.

> GREEN SHEET NOT SIGNED BY NURSE—GS missing nurse’s signature.

> OTHER—REFERRED TO PHARMACY SUPERVISOR—CS drug discrepancy referred to supervisor for resolution.

Dispensing Number Control number assigned by pharmacy when dispensing a Controlled Substances drug. This number is used to track the Green Sheet and drug. Also referred to as the Disp \#, Green Sheet \#, GS \#, or transaction \# throughout the CS package.

Dispensing/Receiving This report can be printed in lieu of VA Form 2321 and

Report lists all Controlled Substances orders dispensed to an

(in lieu of VA Form 10-2321) NAOU. The signatures of the dispensing pharmacist and the nurse receiving the drug are required.

Dispensing Site An NAOU set up as a pharmacy vault that dispenses Controlled Substances drugs.

Dispensing Worksheet This worksheet compiles a list of all pending Controlled Substances request orders for a selected dispensing site. A worksheet number, drug name, quantity ordered, requesting NAOU, ordered by, comments, and blanks for pharmacy dispensing number, manufacturer, lot number, and expiration date are listed on the worksheet.

  
Drug Address Code A code that represents the location of a drug in the NAOU

(Location Code) . For example, if TYLOX is stored in an NAOU on the second set of shelves, third shelf from the top, its drug address code could be expressed as S,2,3. The address code can consist of up to three levels separated by a comma. Each level should further define the exact location. The code is associated with an expansion code for clarity.

Drug Address Code Text used to clarify the meaning of a drug address code.

Expansion For example, the code S would be expanded and printed as shelf. (These codes and expansions are locally created terms.)

Green Sheet The CONTROLLED SUBSTANCE ADMINISTRATION RECORD (VA Form 10-2638) is referred to as a Green Sheet or GS throughout the Controlled Substances V. 3.0 package. Pharmacy dispensing number, drug name, expiration date, quantity dispensed, lot number, ordered by, dispensed by, and ward (NAOU) are printed on the form.

Green Sheet number Control number assigned by pharmacy when dispensing a Controlled Substances drug. This number is used to track the Green Sheet and drug. It is also referred to as the GS \#, dispensing \#, or disp \#, or transaction \# throughout the Controlled Substances V. 3.0 package.

Inpatient Site Inpatient Site must be defined for each NAOU. The Controlled Substances V. 3.0 software utilizes this data to distinguish multi-divisional sites.

Inspector’s Log This report lists all active Green Sheets by NAOU. It includes the following information: Green Sheet \#, drug name, date dispensed, quantity dispensed, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.

Intranet A company wide computer network available via modem that connects users.

Master Vault An NAOU set up as your primary dispensing site.

NAOU - Narcotic Area A Narcotic Area of Use (NAOU) is a place where

of Use commonly stocked Controlled Substances drugs are stored for use by pharmacy, wards or treatment areas. There are three types of NAOUs: Master Vault, Satellite Vault, and

Narcotic Locations.

NAOU Inventory Group An NAOU Inventory Group is defined by pharmacy to represent the Narcotic Areas of Use, which are inventoried together as a group. By grouping the commonly inventoried NAOUs under an easy to remember group name, the elements of the inventory are established, and do not have to be redefined every time an inventory is scheduled.

Narcotic Location An NAOU set up for the nursing wards, pharmacy IV room, or a pharmacy working stock area.

Order Entry Banner Provides a free text field as a site parameter to appear upon Nursing CS Order Entry. When the user accesses the following 3 options, the free text field will be displayed:

> 1\) Nursing Order Entry

> 2\) Pharmacy Order Entry from Nursing

> 3\) Infusion Order Entry

Order Status A processing status is attached to each Controlled Substances request order. The following are valid:

> REQUESTED—NOT ORDERED

> Requests created by batch processing but not yet approved.

> ORDERED—NOT PROCESSED

> Ordered by nursing but not processed by pharmacy.

> PROCESSED—NOT DISPENSED Processed (filled) by pharmacy but not yet dispensed.

> FILLED—NOT DELIVERED Dispensed and verified by pharmacy but not delivered to the requesting NAOU.

> DELIVERED—ACTIVELY ON NAOU Drug stored on the NAOU.

> COMPLETED—GREEN SHEET READY FOR PICKUP Nursing has flagged the Green Sheet ready for pharmacy pickup.

Order Status(cont.)COMPLETED—GREEN SHEET PICKED UP Green Sheet returned to pharmacy but not yet reviewed.

> COMPLETED—REVIEWED Pharmacy has reviewed the Green Sheet .

> COMPLETED—PENDING PROBLEM

> RESOLUTION Pharmacy has reviewed the Green Sheet and a problem exists

> CANCELLED Order cancelled.

> TRANSFERRED TO ANOTHER NAOU Order and drug transferred to another NAOU.

> UNDER REVIEW BY INSPECTOR Order and drug pulled from NAOU by CS Inspector for review.

> LOGGED BY TRAKKER All drug doses from this order have been logged out to patients using the TRAKKER.

PSD ERROR This key should be allocated to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various error and exception conditions generated when entries are filed from the barcode TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER.

PSD NURSE This key should be allocated to nurses, usually LPNs, who may only receive and administer controlled substances but cannot place the order requests.

PSD PARAM This key should be allocated only to the Inpatient Pharmacy Package Coordinator(s). This lock controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site (vault).

PSD TECH Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* \[PSD ON-HAND TECH\], *Transfer Drugs between Dispensing Sites Report* \[PSD PRINT VAULT TRANSFERS TECH\], and the *Daily Activity Log (in lieu of VA FORM 10-2320)*\[PSD DAILY LOG TECH\] options on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\].

PSD TECH ADV Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the *Receipts Into Pharmacy* \[PSD RECEIPTS MENU\], *Dispensing Menu* \[PSD DISPENSING MENU\], *Destructions Menu* \[PSD DESTROY MENU\], *Manufacturer, Lot \#, and Exp. Date - Enter/Edit* \[PSD MFG/LOT/EXP\], *Outpatient Rx's* \[PSD OUTPATIENT\], *Complete Green Sheet* \[PSD COMPLETE GS\], *Destroyed Drugs Report* \[PSD DEST DRUGS REPORT\], *DEA Form 41 Destroyed Drugs Report* \[PSD DESTROY DEA41\], *Destructions Holding Report* \[PSD DESTRUCTION HOLDING\], *Add Existing Green Sheets at Setup* \[PSD EXISTING GS\], *Green Sheet Transfer Between NAOUs Report* \[PSD GS TRANSFER (NAOU) REPORT\], *NAOU* <span id="PSD_3_82" class="anchor"></span>*Usage Report* \[PSD NAOU USAGE\], *Transfer Drugs between Dispensing Sites* \[PSD TRANSFER VAULT DRUGS\] options on the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\]. The CS technician may perform all functions of the *Outpatient Rx’s* \[PSD OUTPATIENT\] option except releasing prescriptions.

PSD TRAN This key should be allocated to the Inpatient Pharmacy Coordinator(s). This key controls the access to the *NAOU to NAOU Transfer Stock Entries* \[PSD TRANSFER NAOU\] option. Users can copy stock entries from one NAOU into another NAOU or from an AR/WS AOU into an NAOU.

PSDMGR This key should be allocated to the Inpatient Pharmacy Supervisor and Package Coordinator(s) or his/her designee. This lock controls the editing of Controlled Substances V. 3.0 files for package set up. This key locks the *Supervisor (CS) Menu* \[PSD MGR\] option.

PSDRPH This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.

PSJ PHARM TECH This key should be allocated to pharmacy technicians handling narcotic orders.

PSJ RNURSE This key should be allocated to nurses who request narcotic orders, receive, and administer controlled substances on the wards.

PSJ RPHARM This key should be given to pharmacists dispensing and receiving narcotic orders.

Satellite Vault An NAOU set up as a secondary dispensing site.

Stock Drug A drug (from the drug file) stored in an NAOU.

Stock Level The quantity of a drug stocked in a specific NAOU.

V*IST*A Veterans Health Information Systems and Technology Architecture

Ward (for Drug) The name of the ward or wards that will use this particular drug. It is important to accurately answer this prompt because this is the link between the Inpatient Medications V. 5.0 package and the Controlled Substances V. 3.0 package. The Inpatient Medications V. 5.0 package looks at this field to know if the drug is a Controlled Substances stocked drug.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Aid and Attendance 19
AMIS 1
B
Barcode TRAKKER for CS Inspections 4
C
Controlled Substance Balances Report 3
Controlled Substances Inspector Menu 3
CS Inspector 3, 10, 11, 13, 15, 16, 18
D
DELIVERED - ACTIVELY ON NAOU 10
Drug Accountability 13
F
Fee Basis 19
G
Green Sheet 3, 10, 21, 22, 23, 24
Green Sheet History 10
H
Hidden Actions 2
I
Inspector’s Log by Rec’d Date 3
Inspector’s Log for Controlled Substances 3
IRL 4, 9
L
Load Software and Insp. Inventory into TRAKKER 4
M
MailMan Message 9
N
NAOU 3, 10, 21, 22, 23, 24, 26
P
Place Green Sheet on Hold 10
PSD ERROR 24
PSD NURSE 24
PSD PARAM 24
PSD TECH 24
PSD TECH ADV 25
PSD TRAN 25
PSDMGR 25
PSDRPH 25
PSJ PHARM TECH 25
PSJ RNURSE 26
PSJ RPHARM 26
R
Remove Green Sheet from Hold 10
S
Send Inspections Inventory TRAKKER Data to DHCP 8
T
TRAKKER 4, 8, 9, 24
U
Under Inspector’s Review—Green Sheets 10
UNDER REVIEW BY INSPECTOR 10
V
VA FORM 10-2321 1
VA FORM 10-2638 1, 10
VAMCs 1
Vault 4, 5, 11, 13, 21, 24
V*IST*A 1, 4, 8, 26
