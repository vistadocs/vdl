---
title: PSGW*2.3*13 Automatic Replenishment/Ward Stock User Manual Change Pages
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Automatic Replenishment/Ward Stock  Change Pages
app_code: AR/WS
app_name: "Pharmacy: Automatic Replenish / Ward Stock"
section: CLI
app_status: active
pkg_ns: PSGW
patch_ver: 2.3
patch_id: PSGW*2.3*13
group_key: "AR/WS:PSGW:2.3"
file_numbers: []
security_keys: []
menu_options: 0
description: The Standard Cost Report lists the cost for items in one AOU, several AOUs, all AOUs, or an inventory group. This cost represents the dollar amount needed to bring each item from zero to its maximum stock level.
audience: 
keywords: 
  - report
  - cost
  - room
  - standard
  - inventory
  - group
  - total
  - aous
  - queue
  - device
page_count: 0
word_count: 529
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/p13.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/p13.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=83"
---

3.7 .ib.Standard Cost Report (132 column); \[PSGW STANDARD COST REPORT\]

The Standard Cost Report lists the cost for items in one AOU, several AOUs, all AOUs, or an inventory group. This cost represents the dollar amount needed to bring each item from zero to its maximum stock level.

The TOTAL COST field is computed by multiplying the item’s stock level by price per dispense unit found in the DRUG file.

The right margin for this report is 132 column. You may queue the report to print at a later time.

Example 1: Standard Cost Report for an Inventory Group

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>S</u>tandard Cost Report (132 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I'): <u>I</u>

Select AOU INVENTORY GROUP NAME: <u>DAY SHIFT</u>

This Inventory Group contains the following AOU(s):

MED ROOM 1

MED ROOM 2

CARDIAC CATH LAB

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to a designated device\]*

report follows

Standard Cost Report PAGE 1

AUG 28,1997

AOU

ITEM LEVEL UNIT COST TOTAL COST

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

==\>MED ROOM 1

DEXTROSE 5% 50ML BAG 5 X 0.8080 = 4.0400

LIDOCAINE 1% INJ VIAL 3 X 0.3550 = 1.0650

ACETAMINOPHEN 325MG 50 X 0.0040 = 0.2000

KETO DIASTIX 100'S 2 X 6.7400 = 13.4800

GLYCERIN SUPPOSITORIES 2 X 0.0360 = 0.0720

DISULFIRAM 250MG TABS 2 X 0.0310 = 0.0620

IPODATE SODIUM 500MG CAP (6'S) 1 X 18.3030 = 18.3030

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Total for MED ROOM 1 -----------------------------------------------------\> 37.2220

Enter RETURN to continue or '^' to exit: <u>\<RET\></u>

Standard Cost Report PAGE 2

AUG 28,1997

AOU

ITEM LEVEL UNIT COST TOTAL COST

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

==\>MED ROOM 2

LIDOCAINE 1% INJ VIAL 5 X 0.3550 = 1.7750

ACETAMINOPHEN 325MG 30 X 0.0040 = 0.1200

GLYCERIN SUPPOSITORIES 1 X 0.0360 = 0.0360

CODEINE SULFATE 30MG 12 X 0.0950 = 1.1400

BETHANECHOL 25MG 5 X 0.0160 = 0.0800

FLUOROURACIL CREAM 1% 30GM 10 X 6.0200 = 60.2000

WARFARIN 10MG U/D 5 X 0.0060 = 0.0300

BENZTROPINE 2MG U/D 6 X 0.0310 = 0.1860

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Total for MED ROOM 2 -----------------------------------------------------\> 63.5670

Example 2: Standard Cost Report for an AOU

Select Management Reports Option: <u>ST</u>andard Cost Report (132 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I'): <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to a designated device\]*

DEVICE: *\[queue report here or send to a designated device\]*

report follows

Standard Cost Report PAGE 1

AUG 28,1997

AOU

ITEM LEVEL UNIT COST TOTAL COST

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

==\>MED ROOM 1

DEXTROSE 5% 50ML BAG 5 X 0.8080 = 4.0400

LIDOCAINE 1% INJ VIAL 3 X 0.3550 = 1.0650

ACETAMINOPHEN 325MG 50 X 0.0040 = 0.2000

KETO DIASTIX 100'S 2 X 6.7400 = 13.4800

GLYCERIN SUPPOSITORIES 2 X 0.0360 = 0.0720

DISULFIRAM 250MG TABS 2 X 0.0310 = 0.0620

IPODATE SODIUM 500MG CAP (6’S) 1 X 18.3030 = 18.3030

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Total for MED ROOM 1 -----------------------------------------------------\> 37.2220

The example of the report previously found on this page has been moved to page 101.