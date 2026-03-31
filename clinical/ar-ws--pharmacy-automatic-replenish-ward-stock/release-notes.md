---
title: Automatic Replenishment/Ward Stock Version 2.3 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: AR/WS
app_name: "Pharmacy: Automatic Replenish / Ward Stock"
section: CLI
app_status: active
pkg_ns: AR/WS
patch_ver: 2.3
patch_id: AR/WS*2.3
group_key: "AR/WS:AR/WS:2.3"
file_numbers: []
security_keys: []
menu_options: 0
description: Automatic Replenishment (AR)/Ward Stock (WS) is a method of drug distribution and inventory management within a hospital. Drug products can be automatically inventoried and delivered (AR) to an area of use (AOU) or requested on demand (WS). An area of use is the place where commonly stocked items ar
audience: 
keywords: 
  - inventory
  - report
  - stock
  - added
  - cost
  - drug
  - management
  - area
  - under
  - duplicate
page_count: 0
word_count: 343
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/wsrelnts.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/wsrelnts.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=83"
---

Decentralized Hospital Computer Program

INPATIENT PHARMACYAUTOMATIC REPLENISHMENT/WARD STOCK MODULERELEASE NOTES

January 1994

Information Systems Center

Birmingham, Alabama

  
Introduction

Automatic Replenishment (AR)/Ward Stock (WS) is a method of drug distribution and inventory management within a hospital. Drug products can be automatically inventoried and delivered (AR) to an area of use (AOU) or requested on demand (WS). An area of use is the place where commonly stocked items are stored. The area is potentially composed of wards, clinics, and specialties.

Enhancements

The AR/WS module relies on, at least, the following external packages to run effectively:

> KERNEL version 7.0

> VA FileMan version 19.0

> MailMan version 7.0

> MAS version 5.2

> Outpatient Pharmacy version 5.6

> AR/WS version 2.04\*\*Note: Version 2.3 may be installed in an account that did not previously have any versions of AR/WS loaded. If, however, there are previous versions that are before V. 2.04, it will be necessary to load V. 2.04 first.

The following enhancements have been made to the existing functionality found in AR/WS V. 2.2:

> • All device closings have been changed to D ^%ZISC.

> • All occurrences of \$NEXT have been removed.

> • All occurrences of ^UTILITY have been changed to ^TMP.

> • Previously, when the “D” cross-reference on the WARD (FOR ITEM) subfield of the WARD (FOR ITEM) subfile (#58.26) of the ITEM subfile (#58.11) of the PHARMACY AOU STOCK file (#58.1) was reindexed, it would reset all items. Now, only active items will be reset.

> • Previously, under the option *Inactivate AOU Stock Item*, the “D” cross reference for the WARD (FOR ITEM) subfield of the WARD (FOR ITEM) subfile (#58.26) of the ITEM subfile (#58.11) of the PHARMACY AOU STOCK file (#58.1) was being deleted immediately even if the inactive date was in the future. Now the *PSGW UPDATEAMIS STATS* option (nightly job) deletes this “D” cross reference on the actual inactive date.

> • All reports have been changed to form feed only at the end of a report.

> • The INITS now display start and stop times.

> • All appropriate reports have been modified to allow selection of AOUs by Inventory Group.

> • The option *Inactivate AOU* has been enhanced to allow the user to inactivate all items in the AOU as well.

> • Previously, backorders were not allowed for any inactive items in an AOU. Backorders for on-demand items in an AOU will now be allowed with the inactive reason OTHER/ONE TIME REQ.

> • A change has been made to the option *Enter/Edit QuantityDispensed*. When the user chooses an AOU further down the list from the default AOU, they will continue on to the next AOU (the AOU after the chosen AOU) instead of going back up to the default AOU.

> • A change was made to the report List Stock Items. Now, the report shows expiration dates for the items.

> • The field DATE/TIME FOR INVENTORY of the PHARMACY AOU INVENTORY file (#58.19) was modified to allow seconds. Users may now queue one Inventory Sheet immediately after another.

New Menu

The following menu option has been added to the Production menu:

*Crash Cart Menu* - This menu has been added to help Acquisition and Materiel Management (Supply) track Crash Carts. Two options exist under this menu:

> 1\. *Enter/Edit Crash Cart Locations-* This option will allow users to edit the LOCATION field for AOUs that are flagged as Crash Carts.

> 2\. *Print Crash Cart Locations* - This option will print an 80 column report listing all AOUs that are flagged as Crash Carts with their locations.

New Options

On the Supervisor’s Menu, there is now a *Duplicate Entry Report* option and a *Standard Cost Report* option listed under the *Management Reports* submenu.

The *Duplicate Entry Report* option will allow printing of a 132 column report that will display duplicate entries in the ITEM subfile (#58.11) of the PHARMACY  
AOU STOCK file (#58.1). The report will show all inventory, return, and on-demand data for each drug selected.

Using the *Standard Cost Report* option, the supervisor can print a report that lists the cost for items in one AOU, several AOUs, all AOUs, or an inventory group. This cost represents the dollar amount needed to bring each item from zero to its maximum stock level.

The *Single AOU Inventory Print* has been added to the Production menu.

This option will print an inventory sheet for a single AOU that is included in the inventory date/time. This option is meant primarily to be used as a means of avoiding a reprint of a lengthy inventory sheet when there has been a problem, for example, a printer jam.

New Fields

Two new fields have been added under the AOU field in the PHARMACY AOU STOCK file (58.1):

> 1\. CRASH CART FLAG - This field will be set to “1” (for “yes”) if this area of use is a Crash Cart. This flag will be used as a screen to list only Crash Carts for the option *Enter/Edit Crash Cart Locations*.

> 2\. CRASH CART LOCATION - This field is meant to be used to record the location of an area of use that is a Crash Cart. This field will be printed on the Expiration Date report and will be updated in the option *Enter/Edit Crash Cart Locations*.