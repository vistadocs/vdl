---
title: Automatic Replenishment/Ward Stock Version 2.3 Technical Manual
doc_type: TM
doc_label: Technical Manual
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
description: "<table> <colgroup> <col style=\\"width: 13%\\" /> <col style=\\"width: 15%\\" /> <col style=\\"width: 12%\\" /> <col style=\\"width: 27%\\" /> <col style=\\"width: 15%\\" /> <col style=\\"width: 15%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th><strong>Date</strong></th> <th><p><strong>Version/</strong></p> <p><strong>"
audience: 
keywords: 
  - routine
  - psgw
  - inventory
  - print
  - report
  - amis
  - stock
  - span
  - column
  - items
page_count: 0
word_count: 9624
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
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/wstech.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/wstech.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=83"
---

Decentralized Hospital Computer Program

INPATIENT PHARMACYAUTOMATIC REPLENISHMENT/WARD STOCK MODULETECHNICAL MANUAL

January 1994

(Revised April 2018)

Information Systems Center

Birmingham, Alabama

  
REVISION HISTORY

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 27%" />
<col style="width: 15%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><p><strong>Version/</strong></p>
<p><strong>Patch</strong></p></th>
<th><strong>Page</strong></th>
<th><strong>Change</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/2018</td>
<td>PSGW*2.3*19</td>
<td><a href="#PSGW_23_19_PackageParametersDefinition"><u>32</u></a>, <a href="#_Toc511398569"><u>37</u></a>, <a href="#PSGW_23_19_PackageParametersBuildFiles"><u>41</u></a></td>
<td>Added information about the new PSGW PACKAGE PARAMETERS option and added a new General Parameters section with information about the new WARD STOCK LEVEL DISPLAY ON parameter, which turns the maximum ward stock display on or off.</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>01/1994</td>
<td>1.0</td>
<td></td>
<td>Initial Release</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

  
Preface

This technical manual is designed to provide the VAMC’s Site Manager and IRM/ADP staff with the information necessary to install, maintain, and troubleshoot Version 2.3 of the Automatic Replenishment/Ward Stock module of the DHCP Inpatient Pharmacy software.

Table of Contents

Introduction [1](#_Toc511398549)

Orientation [3](#_Toc511398550)

Special Notations [3](#_Toc511398551)

About Change Pages [3](#_Toc511398552)

Package Functional Description [3](#_Toc511398553)

Package Management [3](#_Toc511398554)

Implementation and Maintenance [5](#_Toc511398555)

Resource Requirements [5](#_Toc511398555)

Site Configuration [5](#_Toc511398557)

Routine List [7](#_Toc511398558)

Routine Descriptions [7](#_Toc511398559)

File List [11](#_Toc511398560)

File Descriptions [11](#_Toc511398561)

Exported Options [15](#_Toc511398562)

Menus [15](#_Toc511398563)

Keys [15](#_Toc511398564)

Stand-Alone Options [16](#_Toc511398565)

Option Descriptions [17](#_Toc511398566)

General Parameters (XPAR) [37](#_Toc511398567)

Parameter Descriptions [37](#_Toc511398568)

WARD STOCK LEVEL DISPLAY ON \[PSGW_WS_LVL_ON\] [37](#_Toc511398569)

Parameter Templates [37](#_Toc511398570)

PSGW Package Lvl Param Edit \[PSGW PKG PAR\] [37](#_Toc511398571)

File Diagram [38](#_Toc511398572)

Menu Outline [41](#_Toc511398573)

Supervisor’s Menu [41](#_Toc511398573)

Production Menu [43](#_Toc511398575)

Nurses’ Menu [44](#_Toc511398576)

Archiving and Purging [46](#_Toc511398577)

Archiving [46](#_Toc511398577)

Manual Purging [46](#_Toc511398579)

Auto-Purging [47](#_Toc511398580)

Callable Routines [49](#_Toc511398581)

Routine Mapping [49](#_Toc511398582)

Deleting Init Routines [49](#_Toc511398583)

External Relations [51](#_Toc511398584)

Integration Agreement [51](#_Toc511398585)

Internal Relations [53](#_Toc511398586)

Package-Wide Variables [55](#_Toc511398587)

On-Line Documentation [57](#_Toc511398588)

Templates [58](#_Toc511398589)

Glossary [61](#_Toc511398590)

Index [67](#_Toc511398591)

<span id="_Toc511398549" class="anchor"></span>

Automatic Replenishment (AR)/Ward Stock (WS) is a method of drug distribution and inventory management within a hospital. Drug products can be automatically inventoried and delivered (AR) to an area of use (AOU) or requested on demand (WS). An area of use is the place where commonly stocked items are stored. The area is potentially composed of wards, clinics, and specialties.

<span id="_Toc511398550" class="anchor"></span>

This manual is divided into sections addressing such items as routines, files, security, options, etc. to provide a method of quick reference for the Site Manager and IRM/ADP staff. For more detailed information about the package functionality, refer to the Inpatient Pharmacy Automatic Replenishment/Ward Stock Module V. 2.3 User Manual. Additionally, there is a section in the User Manual called Working with the System which presents information which will be useful to persons who have not previously used DHCP software.

<span id="_Toc511398551" class="anchor"></span>

The following notations are used in this manual:

> Description Notation

> Return or Enter key \<RET\> if in text, <u>\<RET\></u> if in screen example

> User response on computer Underlined and bold (they

> screen example will not appear this way on the screen). After a user

> response on a screen example,

> \<RET\> is implied.

> Editor’s note Inside square brackets: \[ \]

> Explanation interrupting computer Inside square brackets: \[ \], and

> screen example bold.

About Change Pages<span id="_Toc511398552" class="anchor"></span>

Future modifications to the software may require changes to the documentation. Change pages will reflect the new version number and date in the footer. Vertical lines in the margin may also be used to further highlight changes on a page.

<span id="_Toc511398553" class="anchor"></span>

The Automatic Replenishment process usually consists of the following functions: 1) select the AOUs and types of items within each AOU to be inventoried, 2) visit each AOU and take inventory, 3) determine the quantity to be dispensed for each item, and 4) dispense the item. The Automatic Replenishment package is designed to allow each VAMC to adapt the system to its own needs.

<span id="_Toc511398554" class="anchor"></span>/Legal Requirements

This package does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements.

<span id="_Toc511398555" class="anchor"></span>

There are 93 AR/WS routines that take up approximately 222K of disk space. Additionally, there are 48 Init routines (including the PSGWPOST and PSGWPRE\* routines) that take up approximately 168K of disk space.

<span id="_Toc511398557" class="anchor"></span>

The following is a list of the site parameters that are used in defining the Automatic Replenishment/Ward Stock module for your site.

MERGE INVENTORY SHEET AND PICK LIST:

> If “1” is entered, the Automatic Replenishment inventory sheet and pick list are merged. A separate pick list does not have to be printed. The inventory sheet contains the quantity dispensed column. The on hand values do not have to be input. The user only enters the actual quantity dispensed. If “0” is entered, the inventory sheet and pick list are not merged. The user prints the inventory sheet, enters on hand amounts, prints the pick list, and dispenses the items.

How should the “MERGE INV. SHEET AND PICK LIST” prompt be answered? This prompt will be answered “YES” if a site does not physically inventory all items in each AOU when Automatic Replenishment occurs. “YES” will be used by sites that stock the AOU with the needed supplies, noting quantity dispensed on an inventory sheet. This prompt will be answered “NO” if a site conducts a manual inventory prior to the stocking process.

PRINT RETURN COLUMNS?:

> If “1” is entered, the return quantity column and the return reason column will appear on the inventory sheet in the Automatic Replenishment package. If “0” is entered, the return columns do not appear on the inventory sheet.

How should the “PRINT RETURN COLUMNS?” prompt be answered? If you wish to have a column to record return quantity and return reason on the inventory sheet, enter “YES” to this prompt. If you answer “NO”, then these columns will not be printed.

BEGIN COLLECTING AMIS DATA NOW?: NO//

> \*\*\*WARNING\*\*\*

> The setting of this parameter directly affects the accuracy of the AMIS report. This parameter should be set to “NO” until you have completed

> *all* of the *Prepare AMIS Data* options on the *Supervisor’sMenu*. Carefully examine the reports produced by the *Data for AMIS Stats -Print* option and the *Show AOU Status for AMIS* option. When you are sure that the data is accurate, then and only then, set this site parameter to “YES”. Once the parameter is set to “YES”, you should under *no circumstances* flip the setting back and forth. While this parameter is set to “NO”, *no data* is collected in the AR/WS STATS file (#58.5) for AMIS statistics.

How should the “BEGIN COLLECTING AMIS DATA NOW?” prompt be answered? Initially this parameter is set to “NO”. The setting of this parameter directly affects the accuracy of the AMIS report. This parameter *should not* be set to “YES” until all of the *Prepare AMIS Data* options have been completed and checked for accuracy. Carefully examine the reports produced by the *Data for AMIS Stats - Print* option and the *Show AOU Status for AMIS* option. When you are sure that the data is accurate, then set this parameter to “YES”. You should set this AMIS parameter to “YES” for all inpatient site names which have the “IS SITE SELECTABLE FOR AR/WS?” parameter set to “YES”. Once the parameter is set to “YES”, you should under *no circumstances* flip the setting back and forth. After this parameter is set to “YES”, data entered during normal use of the package will accumulate to produce the AMIS report.

IS SITE SELECTABLE FOR AR/WS?:

> Should this inpatient site name be shown for use by AR/WS users? When users sign into the module to carry out AR/WS functions, should this site name be displayed? If you answer “YES”, the software will display or allow you to pick this site name when you enter the module. If you answer “NO”, the software will screen out the site name so that AR/WS users will not see or be able to select the site name while in the AR/WS module.

The “IS SITE SELECTABLE FOR AR/WS?” parameter was created because Unit Dose and AR/WS share the INPATIENT SITE file (#59.4). Inpatient site names may be created for Unit Dose to affect order stop dates, etc., and those site names may be confusing to AR/WS users. Therefore, this parameter will screen out inpatient site names which are not used by AR/WS. For every entry in File 59.4, determine if the site name should be shown to users of the AR/WS package. If the site name should be shown, enter “1” or “Yes” for this parameter, otherwise, enter “0” or “NO”.

AR/WS V. 2.3 will enable sites that are multi-divisional to separate their AMIS Statistics by assigning an INPATIENT SITE to each active AOU in the PHARMACY AOU STOCK file (#58.1). Only inpatient sites that have been designated “Selectable for AR/WS” may be assigned to AOUs.

<span id="_Toc511398558" class="anchor"></span>

The following routines are used by the Automatic Replenishment/Ward Stock module.

Routine List and <span id="_Toc511398559" class="anchor"></span>

Routine Routine<u>Names</u> <u>Descriptions</u>

PSGWADE Enter AMIS Data for All Drugs in All AOUs

PSGWADE1 Enter AMIS Data for All Drugs in All AOUs - CONTINUED

PSGWADP Print Data for AMIS Stats

PSGWADP1 Print Data for AMIS Stats - CONTINUED

PSGWAIO AOU Inventory Outline for Selected Date Range

PSGWAOU Identify How Returns Are to be Credited & if Inventories for the AOU are to be Counted in AMIS

PSGWAOUI Enter/Edit AOU Inactivation Dates

PSGWAP Purge Old AMIS Data

PSGWAR Print AMIS Report

PSGWAR1 Print AMIS Report

PSGWARP Print AMIS Report - CONTINUED

PSGWATR Item Activity Inquiry

PSGWATR1 Print Item Activity Inquiry (80 column)

PSGWBGIN AR/WS Item Inactivation

PSGWBO Enter/Edit Actual Dispensed/Backorder Values

PSGWBO1 Enter/Edit Actual Dispensed/Backorder Values - CONTINUED

PSGWBOA Print Backorder Report by AOU or Item (ALL Current Backorders)

PSGWBOE Backorder Input Routine to replace 'PSGW BACKORDER INPUT' Template

PSGWBOI Print Backorder Report by Specific Item (Single or Multiple)

PSGWBOIP Print Backorder Report by Specific Item (Single or Multiple) - CONTINUED

PSGWBOS Print Backorder Report by AOU

PSGWCAD Calculate and Store AMIS Data

PSGWCAD1 Send 'Update AMIS Stats' MailMan message for missing Inpatient Site assignment

PSGWCAD2 Send 'Update AMIS Stats' MailMan message for invalid Inpatient Site assignment

PSGWCAD3 Check for non-pharmacy items in AOUs before updating AMIS Stats

PSGWCCE INPUT AOU LOCATION field

PSGWCCP Print Crash Cart Location List

PSGWCHG AR/WS Mass Ward Conversion

PSGWCL Clear AMIS Exceptions

PSGWCLP Clear AMIS Exceptions Print

PSGWCPA Cost Per AOU for Selected Date Range

PSGWCPA1 Print Cost Per AOU Report for Selected Date Range - CONTINUED

PSGWDEL Delete Inventory Sheets

PSGWDR Returns Breakdown Report for Selected Date Range

PSGWDUP Report for Duplicate Entries in ITEM subfile

PSGWDUP Report for Duplicate Entries in ITEM subfile - CONTINUED

PSGWEDI Enter/Edit of AOU Inventory Values

PSGWEDI1 Enter/Edit of AOU Inventory Values - CONTINUED

PSGWEDIS Input AOU 'INPATIENT SITE' field

PSGWEE Enter/Edit all types of data

PSGWEXP Enter/Edit Drug Expiration Dates

PSGWEXR Drug Expiration Date Report by Selected Date Range/AOU

PSGWEXR1 Print Drug Expiration Date Report by Selected Date Range/AOU

PSGWEXR2 Print Drug Expiration Date Report by Selected Date Range/AOU for AOUs with Locations

PSGWFIL Fill Backorder

PSGWFLBO Enter/Edit Backorders

PSGWHC High Cost for Selected Date Range (Single AOU or Cumulative)

PSGWHC0 High Cost for Selected Date Range (Single AOU or Cumulative) - CONTINUED

PSGWHC1 Print High Cost Report for Selected Date Range - CONTINUED

PSGWHV High Volume for Selected Date Range (Single AOU or Cumulative)

PSGWHV0 High Volume for Selected Date Range (Single AOU or Cumulative) - CONTINUED

PSGWHV1 Print High Volume Report for Selected Date Range - CONTINUED

PSGWKINV Purge ^PSI(58.19,"AINV") Global of Inventory Over 100 days Old

PSGWL Build AOU Inventory List

PSGWLSI List Active Stock Items for AOU(s)

PSGWLSI1 Print Stock Items in Order by Type/Location

PSGWLSI2 Print Stock Items in Alphabetical Order

PSGWNTEG Package checksum checker

PSGWNTE0 Package checksum checker

PSGWNU Print Drugs (Items) with NO Usage for Selected Date Range

PSGWNU1 Print Drugs (Items) with NO Usage for Selected Date Range - CONTINUED

PSGWOD2 Enter an On-Demand Request (for Pharmacy Use) - CONTINUED

PSGWODP Print an On-Demand Report by Date/AOU

PSGWODPR Print an On-Demand Report by Date/AOU - CONTINUED

PSGWODRN Enter an On-Demand Request - for Nursing Staff

PSGWOLD Purge Old Inventory Data (Auto Replenish, On-Demands, Returns & Backorder Data)

PSGWOLD1 Purge Old Inventory Data - CONTINUED (Delete Drugs Inactivated in AOU & Delete AOUs with No Drugs or Pointers to 58.2)

PSGWOND Delete an On-Demand Request

PSGWONDM Enter an On-Demand Request - for Pharmacy Use

PSGWPAW Print AMIS Data Worksheet for All Drugs in All AOUs

PSGWPAW1 Print AMIS Data Worksheet for All Drugs in All AOUs - CONTINUED

PSGWPERC Print Percentage Stock On Hand

PSGWPERE Edit person doing inventory

PSGWPI Print AOU Inventory Sheet

PSGWPI1 Print AOU Inventory Sheet - CONTINUED

PSGWPI2 Print AOU Inventory Sheet - CONTINUED

PSGWPIG Print AOU Inventory Group List

PSGWPIS Print AOU Inventory Sheet for a single AOU

PSGWPL Print AOU Inventory Pick List

PSGWPL0 Print AOU Inventory Pick List - CONTINUED

PSGWPL1 Print AOU Inventory Pick List - CONTINUED

PSGWPOST Post Init Conversion Routine

PSGWPRE1 Pre-init for AR/WS V3.0

PSGWPSI Print Data for AR/WS Stock Items

PSGWPSI1 Print Data for AR/WS Stock Items - CONTINUED

PSGWST1 Post-Init Conversion Routine - CONTINUED

PSGWRA Recalculate AMIS Data

PSGWRAC Print AOU Status for AMIS - Inpatient Site, Returns, and AMIS Count

PSGWRI Return Items for AOU

PSGWSC Cost Report for Single Item for Selected Date Range

PSGWSC1 Print Cost Report for Single Item for Selected Date Range - CONTINUED

PSGWSET Set Inpatient Site

PSGWSIG Build Sort Key for AOUs in Inventory Group

PSGWSTD Standard Cost Report

PSGWSTKI Stock Item Enter/Edit

PSGWTOT Usage Report for an Item

PSGWTOT1 Print Usage Report for All Drugs for a single AOU or ALL AOUs

PSGWTOT2 Print Usage Report for Single Drug for One or ALL AOUs

PSGWTR Transfer Stock Entries from One AOU to Another

PSGWTR1 Transfer Stock Entries from One AOU to Another - CONTINUED

PSGWUAS Update AMIS Stats File

PSGWUTL Utility routine for VA FileMan functions

PSGWUTL1 Utility routine for HELP functions

PSGWVW Lookup Item and List Wards/AOUs Which Stock It

PSGWWRD Add/Delete Ward (for Item) assignments

PSGWXREF Background job to re-index the AMIS cross-reference for inventories, on-demands, and returns

<span id="_Toc511398560" class="anchor"></span>

This package requires 10 files. Information about all files including these can be obtained by using the VA FileMan to generate a list of file attributes.

<u>File Numbers</u> <u>File Names</u>

> 50 DRUG

> 58.1 PHARMACY AOU STOCK

> 58.16 AOU INVENTORY TYPE

> 58.17 AOU ITEM LOCATION

> 58.19 PHARMACY AOU INVENTORY

> 58.2 AOU INVENTORY GROUP

> 58.3 PHARMACY BACKORDER

> 58.5 AR/WS STATS

> 59.4 INPATIENT SITE

> 59.7 PHARMACY SYSTEM

<span id="_Toc511398561" class="anchor"></span>

The following are files exported and used by the Automatic Replenishment/Ward Stock module.

50 DRUG FILE

This file holds the information related to each drug that can be used to fill a prescription.

58.1 PHARMACY AOU STOCK FILE

This file defines the items, their location, and quantity for each Area of Use (AOU) in the hospital. Additionally, information for each inventory, by item, is stored for an audit trail of usage.

58.16 AOU INVENTORY TYPE FILE

Defines the inventory types which are used to group related items in or across areas of use. This file is defined by the user to allow for maximum flexibility in adapting to the system of inventory in each hospital.

58.17 AOU ITEM LOCATION FILE

Expansions of the codes used to indicate storage location of item in the area of use.

58.19 PHARMACY AOU INVENTORY FILE

This file contains information that pertains to each individual inventory such as date/time of inventory, responsible employee, ID number, and inventory group.

> **NOTE:** There is a cross-reference called AINV that is not VA FileMan compatible and has the Standards and Conventions Committee (SACC) exemption which allows its use. If you create any local cross-references for this file *do not* use the name AINV as this will overwrite the existing cross-reference.

58.2AOU INVENTORY GROUP FILE

Entries in this file define standard inventories by defining the areas of use and type of inventory items inventoried. This saves the user from having to re-define the inventory boundaries every time a particular inventory is scheduled. Instead, the user can name inventory groups and the computer then knows what will be inventoried by accessing this file.

This file is designed to be used by both the Automatic Replenishment/Ward Stock module and the Controlled Substance module. Areas of use intended for AR/WS are defined in Field \#1 (AREA OF USE ). Areas of use intended for CS are defined in Field \#3 (NARCOTIC AREA OF USE).

58.3 PHARMACY BACKORDER FILE

This file contains information that pertains to backorders, such as the date/time of backorder, the AOU for which the item is backordered, and the quantity backordered.

58.5 AR/WS STATS FILE

This file contains the data necessary to generate the AMIS statistics for AR/WS. This data is accumulated automatically by a queued nightly job.

> **NOTE:** There are two cross-references that exist under this file that are created in the PHARMACY AOU STOCK file (#58.1). The cross-reference names are AMIS and AMISERR, if you create any local cross-references for this file (#58.5) *do not* use these names as it will overwrite the existing cross-references.

  
59.4 INPATIENT SITE

This file contains the site parameters for the various inpatient packages, giving the various VAMCs the ability to tailor the packages to their needs. The following fields are used by the AR/WS package:

59.7 PHARMACY SYSTEM

This file contains data that pertains to the entire Pharmacy System of a medical center, and not to any one site or division. The number ranges for the nodes and field numbers are as follows:

> 0 - 9.99 RESERVED

> 10 - 19.99 National Drug File

> 20 - 29.99 Inpatient

> 30 - 39.99 IVs

> 40 - 49.99 Outpatient

> 50 - 59.99 AR/WS

> 60 - 69.99 Unit Dose

THERE SHOULD BE ONLY ONE ENTRY IN THIS FILE.

> **NOTE:** Because of the nature of this file and the fact that *all* the Pharmacy packages use this file, it is *very important* to stress that sites *do not* edit fields or make local field additions to the PHARMACY SYSTEM file.

<u>  
</u>

<span id="_Toc511398562" class="anchor"></span>

For package security information for this module refer to the Inpatient Pharmacy Automatic Replenishment/Ward Stock Module Package Security Guide.

<span id="_Toc511398563" class="anchor"></span>

All pharmacy personnel may be assigned the *PSGWMGR* option as the primary menu option.

If Pharmacy wishes to give the Auto Replenishment/Ward Stock Nurses’ Menu to Nursing, then nursing personnel may be assigned the *PSGW RN* menu option. Read “On-Demand Requests” in the AR/WS User Manual before assigning this menu, as some coordination between services is required.

Some stations design their own menus for individual users. If this is the case, then the top level AR/WS menu must contain the following enter and exit code in the OPTION file:

EXIT ACTION : K PSGWSITE

ACTION : I '\$D(PSGWSITE) D ^PSGWSET

This enter and exit code must be present because the PSGWSITE variable is set as users enter the package. If the Kernel’s ^OPTION NAME feature is used to jump directly into lower levels of the AR/WS package, then the “Select INPATIENT SITE NAME” prompt *must be* answered in order to define the PSGWSITE variable. All options are independently invocable, however, if the instructions above are not followed, users will be repeatedly asked to select an Inpatient Site if there are two or more sites that are flagged for AR/WS use.

<span id="_Toc511398564" class="anchor"></span>

After the users are assigned the primary menu option, it is necessary to give the appropriate security keys to each user as required. There are four keys associated with AR/WS:

PSGWMGR This key must be given to the Inpatient Pharmacy Package Coordinator and other users who are allowed to edit AR/WS files and run the AMIS report. This key locks the *Supervisor’sMenu* options \[PSGW WARD STOCK MAINT\].

PSGW PURGE This key should be given *only* to the Inpatient Pharmacy Package Coordinator or his/her designee. This lock controls the deletion of data from the AR/WS files and should be assigned with discretion. This key locks the *Obsolete Data Purge* options \[PSGW PURGE\].

PSGW PARAM This key should be given *only* to the Inpatient Pharmacy Package Coordinator. This lock controls when the collection of AMIS data begins. This key locks the *Site Parameters* option \[PSGW SITE\] on the *Supervisor’s Menu*.

PSGW TRAN This key should be given *only* to the Inpatient Pharmacy Package Coordinator or his/her designee. The key controls access to the T*ransfer AOU Stock Entries* option \[PSGW TRANSFER ENTRIES\]. Using the transfer option, users may copy the stock entries from one Area of Use into other AOUs.

<span id="_Toc511398565" class="anchor"></span>

All of the Automatic Replenishment/Ward Stock package options have been designed to stand alone. Each option requires the use of the package-wide variable PSGWSITE that is set as users enter the package. Even though *all* options are independently invokable, users will be repeatedly asked to select an Inpatient Site (if there are two or more sites that are flagged as selectable for AR/WS use) if top level AR/WS menus do not contain the following enter and exit code in the OPTION file:

EXIT ACTION: K PSGWSITE

ACTION: I '\$D(PSGWSITE) D ^PSGWSET

<span id="_Toc511398566" class="anchor"></span>

PSGW ADD/DEL WARD Add/Delete Ward (for Item)

This option will allow a user to add or delete a Ward (for Item) assignment for all stock items in one or more active AOUs.

Type: run routine Routine: PSGWWRD

------------------------------------------------------------

PSGW AMIS AR/WS AMIS Report

MENU

Main option for clearing exceptions, printing, and recalculating the AMIS report.

Type: menu

Menu Items:

Incomplete AMIS Data

Print AMIS Report (132 column)

Recalculate AMIS

------------------------------------------------------------

PSGW AOU INACTIVATION Inactivate AOU

This option will allow a user to inactivate an AOU. An Inactive Date may be in the future.

Type: run routine Routine: PSGWAOUI

------------------------------------------------------------

PSGW AOU INV GROUP EDIT AOU Inventory Group - Enter Edit

This option supports entering and editing inventory groups. These groups define a cluster of AOUs and for each AOU, an inventory type which may be multiple. This lets pharmacy define a list of standard AOUs and inventory types that can be selected easily when doing inventory.

Type: run routine Routine: GROUP^PSGWEE

------------------------------------------------------------

  
PSGW AOU INV GROUP PRINT Inventory Group List (80 column)

This option prints a list of the currently defined AOU inventory groups with their associated wards and inventory types.

Type: run routine Routine: PSGWPIG

------------------------------------------------------------

PSGW AOU INV GROUP SORT Sort AOUs in Group

This option allows the user to change the order in which the AOUs within an inventory group will sort. AOUs should sort in the order that they will be visited.

Type: run routine Routine: PSGWSIG

------------------------------------------------------------

PSGW AOU INVENTORY INPUT Input AOU Inventory

This option supports the entry of the inventory results as recorded on the AOU inventory sheet. Items within an AOU are prompted in the order that they appear on the AOU inventory sheet.

Type: run routine Routine: PSGWEDI

------------------------------------------------------------

PSGW AOU RET/AMIS CT PRINT Show AOU Status for AMIS (80 column)

This option shows the method of distribution credited for RETURNS for each AOU, and if the AOU is to be counted in AMIS stats.

Type: run routine Routine: PSGWRAC

------------------------------------------------------------

PSGE AOU RETURNS & AMIS COUNT Identify AOU Returns & AMIS Count

For AMIS purposes, the system must know how to credit returns. This option allows the user to identify the usual method of drug distribution to be credited for each AOU. All returns from the AOU will be credited to this method. For AMIS purposes, the system must know if the inventories for each AOU are to be counted in the AR/WS STATS file. Most AOUs will count on AMIS, however, an AOU used for internal inventory purposes within the pharmacy should not.

Type: run routine Routine: PSGAOU

------------------------------------------------------------

PSGW AREA OF USE EDIT Create an Area of Use

This option allows the user to initially define the Areas of Use and the wards and services within the area.

Type: run routine Routine: AOU^PSGWEE

------------------------------------------------------------

PSGW BACKORDER Backorder Requests

Menu giving access to the backorder options.

Type: menu

Menu Items:

Enter Backorders

Fill Requests for Backorder Items

AOU Backorder Report (80 column)

Current (ALL) Backorder Report (80 column)

Single Item Report (80 column)

Multiple Items Report (80 column)

------------------------------------------------------------

PSGW BACKORDER (ALL)PRINT Current (ALL) Backorder Report(80 column)

This option will print a list of ALL current backorders sorted by AOU or by ITEM.

Type: run routine Routine: PSGWBOA

-------------------------------------------------------------

PSGW BACKORDER AOU PRINT AOU Backorder Report (80 column)

Prints all items backordered for selected Areas Of Use.

Type: run routine Routine: PSGWBOS

------------------------------------------------------------

PSGW BACKORDER EDIT Fill Requests for Backorder Items

Allows the user to fill a backordered request by entering the date filled field. The user must know the item, Area of Use, and the date of backorder.

Type: run routine Routine: PSGWFIL

------------------------------------------------------------

PSGW BACKORDER IN Enter Backorders

Used to create backorders for items stocked in an AOU. User must enter item, AOU, backorder date, and current backorder (amount to back order).

Type: run routine Routine: PSGWBOE

------------------------------------------------------------

PSGW BACKORDER ITEM PRINT Single Item Report (80 column)

Prints a list of all backorders for a specific item.

Type: run routine Routine: SINGLE^PSGWBOI

------------------------------------------------------------

PSGW BACKORDER ITEMS PRINT Multiple Items Report (80 column)

The user may select several items. The report will then print the backorder information for each of the items selected.

Type: run routine Routine: MULTI^PSGWBOS

------------------------------------------------------------

PSGW CLEAR AMIS EXCEPTIONS Incomplete AMIS Data

This option loops through the AEX - exceptions cross-reference in the AR/WS STATS file (#58.5). Drugs in this cross-reference had data missing from the DRUG file at the time the quantity was dispensed, and thus could not be added to the cumulative AMIS statistics. For the selected date range, the drug will be shown, and the user will be asked to supply the missing data. At that time, the routine will update the AMIS statistics, and delete the AEX cross-reference.

Type: run routine Routine: PSGWCL

------------------------------------------------------------

  
PSGW COST PER AOU Cost Report Per AOU (80 column)

For a user selected date range, this report will show all active drugs for one AOU, several AOUs, or ALL AOUs, with total quantity dispensed and cost. (It will print only Bottom Totals if desired.) The report gives a total of all quantities dispensed and all drug costs for that AOU. Also, if wards/locations and services have been defined for the AOU, a breakdown report will print. It shows the defined wards/locations, percentage of total, and cost per ward/location. If services are defined, it shows the defined services, percentage of ward/location, and cost per service. The report may be queued to print at a later time.

Type: run routine Routine: PSGCPA

------------------------------------------------------------

PSGW CRASH CART LOCATION EDIT Enter/Edit Crash Cart Locations

This option will allow users to edit the LOCATION field for AOUs that are flagged as Crash Carts.

Type: run routine Routine: PSGWCCE

-------------------------------------------------------------

PSGW CRASH CART LOCATION PRINT Print Crash Cart Locations

This option will print an 80 column report listing all AOUs that are flagged as Crash Carts with their locations.

Type: run routine Routine: PSGWCCP

-------------------------------------------------------------

PSGW CRASH CART MENU Crash Cart Menu

This menu contains the crash cart options for production.

Type: menu

Menu Items:

Enter/Edit Crash Cart Locations

Print Crash Cart Locations

-------------------------------------------------------------

  
PSGW DELETE INVENTORY Delete Inventory Date/Time

This option will allow a user to delete an Inventory Sheet that has no entries in the PHARMACY AOU STOCK file (#58.1), or in the PHARMACY BACKORDER file (#58.3).

Type: run routine Routine: PSGWDEL

------------------------------------------------------------

PSGW DUPLICATE REPORT Duplicate Entry Report (132 column)

This 132 column report will display one or all drugs with duplicate entries in the ITEM subfile (#58.11) of the PHARMACY AOU STOCK file (#58.1). For each drug the report will show all inventory, return, and on-demand data.

Type: run routine Routine: PSGWDUP

------------------------------------------------------------

PSGW EDIT AOU STOCK Stock Items - Enter/Edit

Provides access to enter or edit items stocked in an Area of Use. This is how the list of items an AOU stocks is created or changed.

Type: run routine Routine: PSGWSTKI

------------------------------------------------------------

PSGW EDIT INVENTORY USER Edit’ Person Doing Inventory’

This option will allow editing of the field PERSON DOING INVENTORY in the

PHARMACY AOU INVENTORY file (#58.19) for a selected Date/Time for Inventory.

Type: run routine Routine: PSGWPERE

------------------------------------------------------------

PSGW ENTER AMIS DATA/ALLDRUGSEnter AMIS Data for AllDrugs/All AOUs

This routine will display for the user, all drugs in all AOUs, allowing the entry of data needed for AMIS calculations. The drugs will be displayed alphabetically by type. For each drug, the user will be asked for AMIS category and AMIS conversion number.

Type: run routine Routine: PSGWADE

------------------------------------------------------------

  
PSGW ENTER/EDIT AMIS DATA AMIS Data Enter/Edit (Single Drug)

This option allows the entry of AMIS category and conversion number for those drugs used in the Automatic Replenishment/Ward Stock package. The user must select the drug for which data is to be entered. This option is most likely to be used to edit data entered in the *Enter AMIS Data for All Drugs/All AOUs* option.

Type: edit file File: PSDRUG(

------------------------------------------------------------

PSGW EXP REPORT Expiration Date Report (80 column)

This option will print an Expiration Date Report for a single, several, or all AOUs. For multiple AOUs it can be sorted by Date/Drug/AOU or by Date/AOU/Drug.

Type: run routine Routine: PSGWEXR

------------------------------------------------------------

PSGW EXPIRATION ENTER/EDIT Expiration Date Enter/Edit

This option will allow the entry of expiration dates for items in an AOU.

Type: run routine Routine: PSGWEXP

------------------------------------------------------------

PSGW HIGH COST High Cost Report (80 column)

This option allows the user to see drugs/items dispensed in AR/WS in alphabetical or cost order. The user selects a date range, and a cut off amount for the report. The report may be calculated for a single AOU, or cumulatively for all AOUs. Report may be queued to print at a later time.

Type: run routine Routine: PSGWHC

------------------------------------------------------------

PSGW HIGH VOLUME High Volume Report (80 column)

For a selected date range, the user may print a report showing drug usage in decreasing order for either a selected AOU or for all AOUs combined.

Type: run routine Routine: PSGWHV

------------------------------------------------------------

  
PSGW INACTIVATE AOU STOCK ITEM Inactivate AOU Stock Item

Use this option to inactivate an item that is currently on an AOU’s stock list. Items should not be deleted, but simply made inactive.

Type: run routine Routine: PSGWBGIN

------------------------------------------------------------

PSGW INPUT AOU INP SITE Identify AOU INPATIENT SITE

This option will loop through the PHARMACY AOU STOCK file (#58.1) and locate all active AOUs that do not have the INPATIENT SITE field defined.

Type: run routine Routine: PSGWEDIS

-------------------------------------------------------------

PSGW INV TYPE Print Inventory Types (80 column)

Print the file of INVENTORY TYPES used to classify Area of Use items.

Type: print file File: PSI(58.16,

------------------------------------------------------------

PSGW INV TYPE EDIT Enter/Edit Inventory Types

Edit the file INVENTORY TYPES used to classify Area of Use items.

Type: run routine Routine: INVENT^PSGWEE

------------------------------------------------------------

PSGW INVENTORY DISPENSE Enter/Edit Quantity Dispensed

Allows the user to enter the actual quantity dispensed from the inventory pick list or from the inventory sheet depending on how the site parameters are set up. If the MERGE INV. SHEET AND PICK LIST site parameter is set to NO, the quantity dispensed figure is then used to automatically compute the amount on backorder.

Type: run routine Routine: PSGWBO

------------------------------------------------------------

  
PSGW INVENTORY PICK LIST Pick List (132 column)

Prints the Inventory Pick list for the inventory specified by the user.

Type: run routine Routine: PSGWPL

------------------------------------------------------------

PSGW INVENTORY SHEET Inventory Sheet Print (132 column)

This option prints the AOU inventory reporting sheet. This contains a listing, by AOU, of all the items for specific inventory types.

Type: run routine Routine: PSGWL

------------------------------------------------------------

PSGW INVENTORY SINGLE Single AOU Inventory Print (132 column)

This option will print an inventory sheet for a single AOU that is included in the inventory date/time. This option is meant primarily to be used as a means of avoiding a reprint of a lengthy inventory sheet when there has been a problem such as a printer jam.

Type: run routine Routine: EN^PSGWPIS

------------------------------------------------------------

PSGW ITEM INQUIRY Item Activity Inquiry (80 column)

This option will display all activity (inventories, on-demands, and returns) for a specified item in a specified AOU for a specified date range. This option is primarily meant to be used as a tool to identify bad data input.

Type: run routine Routine: PSGWATR

------------------------------------------------------------

PSGW ITEM LOC EDIT Item Location Codes - Enter/Edit

This option supports editing of codes used to define the location of items in Areas of Use or in the pharmacy.

Type: run routine Routine: ITEMLOC^PSGWEE

------------------------------------------------------------

  
PSGW ITEM LOC PRINT List Location Codes (80 column)

Produces report of codes used to define the location of items in Areas of Use or in the pharmacy.

Type: print file File: PSI (58.17,

------------------------------------------------------------

PSGW LOOKUP ITEM Ward/AOU List for an Item (80 column)

This option prints a list of all the wards and their associated AOUs that stock a particular item. The user must specify the item to be looked up.

Type: run routine Routine: PSGWVW

------------------------------------------------------------

PSGW MGT REPORTS Management Reports

This menu gives access to various management reports, including the AMIS report.

Type: menu

Menu Items:

AR/WS AMIS Report

Cost Report Per AOU (80 column)

Single Item Cost Report (80 column)

High Cost Report (80 column)

High Volume Report (80 column)

Duplicate Entry Report (132 column)

------------------------------------------------------------

PSGW ON-DEMAND On-Demand Requests

Menu giving access to the On-Demand options.

Type: menu

Menu Items:

Enter/Edit On-Demand Request (80 column)

Delete an On-Demand Request

Print an On-Demand Report by Date/AOU

------------------------------------------------------------

  
PSGW ON-DEMAND DELETE Delete an On-Demand Request

Allows the user to delete the On-Demand request. The user must enter the Area of Use, item name, and the inventory date (date of request).

Type: run routine Routine: PSGWOND

------------------------------------------------------------

PSGW ON-DEMAND EDIT Enter/Edit On-Demand Request (80 column)

Allows the user to edit an On-Demand request and change the inactive date fields and the quantity requested.

Type: run routine Routine: PSGWONDM

------------------------------------------------------------

PSGW ON-DEMAND NURSING EDIT Enter/Edit Nurses’ On-DemandRequest

This option is used to enter an On-Demand request by the Nursing Staff. An On-Demand request is the non-scheduled distribution of an item to an AOU. If there is a backorder on the requested item, the backorder total is displayed, but the user is not allowed to enter quantity to be dispensed. If the item requested is currently not stocked in that AOU, the user is *not* allowed to add it with this option. Requests for non-standard items must be made through the pharmacy by phone or form. After entering the request, the user may print a report of the request.

Type: run routine Routine: PSGWODRN

------------------------------------------------------------

PSGW ON-DEMAND PRINT Print an On-Demand Report by Date/AOU(80 column)

Prints an On-Demand report which lists the on-demand requests within a user selected date range. The user can also select the Areas of Use to be checked. Standard stock items which have been requested on-demand are flagged.

Type: run routine Routine: PSGWODP

------------------------------------------------------------

  
PSGW PREPARE AMIS DATA Prepare AMIS Data

Main option for preparing data base with AR/WS AMIS data.

Type: menu

Menu Items:

Print AMIS Worksheet (80 column)

Enter AMIS Data for All Drugs/All AOUs

Data for AMIS Stats - Print (132 column)

AMIS Data Enter/Edit (Single Drug)

Identify AOU Returns & AMIS Count

Identify AOU INPATIENT SITE

Show AOU Status for AMIS 980 column)

------------------------------------------------------------

PSGW PRINT AMIS REPORT Print AMIS Report (132 column)

This option prints the AMIS report. Right margin should be at 132. The report may be queued to print at a later time.

Type: run routine Routine: PSGWAR

------------------------------------------------------------

PSGW PRINT AMIS WORKSHEET Print AMIS Worksheet (80 column)

This option prints a worksheet to be used in classifying AR/WS drugs for AMIS. The print order is by type, and within type the drug listing is alphabetical.

Type: run routine Routine: PSGWPAW

------------------------------------------------------------

PSGW PRINT AOU STOCK List Stock Items (132 column)

This option prints all items currently available for inventory, by AOU. You may print the report for one AOU, several AOUs, or enter ^ALL to print the report for all Areas of Use. The report may be printed (1) in order by AOU/TYPE/LOCATION, or (2) in alphabetical order by item.

Type: run routine Routine: PSGWLSI

------------------------------------------------------------

  
PSGW PRINT DATA FOR AMISSTATS Data for AMIS Stats -Print (132 column)

This report will show the current data stored in the DRUG File which will affect AR/WS AMIS statistics.

Type: run routine Routine: PSGWADP

------------------------------------------------------------

PSGW PRINT SETUP LISTS Print Set Up Lists

This option contains all reports or lists associated with setting up the files for AR/WS.

Type: menu

Menu Items:

Print Inventory Types (80 column)

List Location Codes (80 column)

Show AOU/Ward/Service (132 column)

Print AR/WS Stock Item Data (132 column)

List Stock Items (132 column)

Inventory Group List (80 column)

------------------------------------------------------------

PSGW PURGE Obsolete Data Purge

This option is the main menu driver for purging AR/WS files.

Type: menu

Menu Items:

AMIS Data Purge

Purge Dispensing Data

------------------------------------------------------------

PSGW PURGE AMIS AMIS Data Purge

This option allows the user to delete data from the AR/WS STATS file (#58.5). Data should be kept in this file for at least one quarter. The routine will not allow users to delete data that is less than 100 days old. The option is automatically queued.

Type: run routine Routine: PSGWAP

------------------------------------------------------------

  
PSGW PURGE FILES Purge Dispensing Data

This option allows the user to delete data from Files 58.1, 58.3, and 58.19. Data should be kept in these files for at least one quarter. The routine will not allow users to delete data that is less than 100 days old. Since the option is CPU intensive, it should be queued to run during the off hours.

Type: run routine Routine: PSGWOLD

------------------------------------------------------------

PSGW PURGE INVENTORY Purge Old Inventories fromPSI(58.19,AINV)

This option is not on a menu, as it is a background job scheduled to run each night. This option purges the ^PSI(58.19,"AINV") global. Inventory information that is over 100 days old is removed. The program is automatically queued and is transparent to the users of the system.

Type: run routine Routine: PSGWKINV

------------------------------------------------------------

PSGW RE-INDEX AMIS Re-index AMIS Cross-Reference

This option will queue a background job that will re-index the AMIS cross-reference for inventories, on-demands, and returns. This cross-reference is important because this is where the nightly job to update the AR/WS STATS file (#58.5) gets the data for the update. If this cross-reference is somehow destroyed, it is very important to rebuild it. Though it is possible to accomplish this through VA FileMan, this option is a much quicker and easier alternative. This option is not tied to any menu, but may be hooked into a menu at the site’s discretion.

> **NOTE:** This option is CPU intensive and should be queued only in the off hours. Also, it should *only* be run if there is strong evidence the AMIS cross-reference has been destroyed or corrupted.

Type: run routine Routine: PSGWXREF

-----------------------------------------------------------

PSGW RECALCULATE AMIS Recalculate AMIS

This option should be used *only* after the AMIS report has been run, results have been found to be in error, and data in the DRUG file has been changed to reflect the correct information. The purpose of this option is to correct the AMIS when data entry errors have caused the results to be inaccurate.

Type: run routine Routine: PSGWRA

------------------------------------------------------------

  
PSGW REPORTS Auto Replenishment Reports

Menu giving access to various report options for Automatic Replenishment data.

Type: menu

Menu Items:

List Stock Items (132 column)

Expiration Date Report (80 column)

Inventory Outline (80 column)

Ward/AOU List for an Item (80 column)

Item Activity Inquiry (80 column)

Percentage Stock On Hand (132 column)

Returns Analysis Report (80 column)

Usage Report for an Item (80 column)

Zero Usage Report (80 column)

------------------------------------------------------------

PSGW RETURN ITEMS Return Items for AOU

Used to record items returned from an AOU.

Type: run routine Routine: PSGWRIS

-------------------------------------------------------------

PSGW RETURNS BREAKDOWN Returns Analysis Report (80 column)

For a user selected date range, this report shows the breakdown of returns information. The report may be printed for one AOU, several AOUs, or for all AOUs. Return date, return quantity, and return reason are shown for each drug.

Type: run routine Routine: PSGWDR

------------------------------------------------------------

PSGW RN Auto Replenishment/Ward Stock Nurses’ Menu

This is the main menu driver for *Automatic Replenishment/Ward Stock* options for nurses.

Type: menu

Menu Items:

Enter/Edit Nurses’ on-Demand Request (80 column)

List Stock Items (132 column)

Ward/AOU List for an Item (80 column)

------------------------------------------------------------

  
PSGW SETUP Set Up AR/WS (Build Files)

Options that support management of files typically created and edited during initial set up of Automatic Replenishment/Ward Stock.

Type: menu

Menu Items:

Enter/Edit Inventory Types

Item Location Codes - Enter/Edit

Create the Area of Use

Stock Items - Enter/Edit

Expiration Date - Enter/Edit

Ward (For Item) Conversion

Add/Delete Ward (for Item)

Transfer AOU Stock Entries

Inactivate AOU

Inactivate AOU Stock item

AOU Inventory Group - Enter/Edit

Print Set Up Lists

Edit ‘Person Doing Inventory’

Sort AOUs in Group

Site Parameters

<span id="PSGW_23_19_PackageParametersDefinition" class="anchor"></span>AR/WS Package-wide Parameter Edit

------------------------------------------------------------

PSGW PACKAGE PARAMETERS AR/WS Package-wide Parameter Edit

This option allows the user to edit general system parameters that affect the entire AR/WS package. Refer to <u>General Parameters (XPAR)</u> on page [<u>37</u>](#PSGW_23_19_GenParametersSectionBegin) for information on these parameters.

Type: Action

------------------------------------------------------------

PSGW SHOW AREA OF USE Show AOU/Ward/Service (132 column)

This option allows the user to see the AOUs/wards/services created in the *Createthe Area of Use* option.

Type: print file File: PSI (58.1,

------------------------------------------------------------

PSGW SINGLE ITEM COST Single Item Cost Report (80 column)

For a selected date range, this option gives total cost for a single item from one AOU, several AOUs, or ALL AOUs.

Type: run routine Routine: PSGWSC

------------------------------------------------------------

PSGW SITE Site Parameters

Allows user to set site parameters for Automatic Replenishment package. A site parameter called AR/WS AMIS FLAG controls when the collection of AMIS data begins. Read all available documentation before setting this parameter!

Type: run routine Routine: SITE^PSGWEE

------------------------------------------------------------

PSGW STANDARD COST REPORT Standard Cost Report (132 column)

This report prints the cost for items in one AOU, several AOUs, all AOUs, or an Inventory Group. This cost represents the dollar amount needed to bring each item from zero to its maximum stock level.

Type: run routine Routine: PSGWSTD

------------------------------------------------------------

PSGW STOCK ITEM DATA Print AR/WS Stock Item Data (132 column)

This option will print a listing of *all* items defined in the PHARMACY AOU STOCK file (#58.1) in alphabetical order. The report will show all AOUs that stock the item, stock levels, all Wards (for Item), all Types, and location.

Type: run routine Routine: PSGWPSI

------------------------------------------------------------

PSGW STOCK PERCENTAGE Percentage Stock On Hand (132 column)

Report which extracts inventory data by percentage of stock on hand for a given inventory date range. Percentage and date range can be specified.

Type: print file File: PSI(58.1,

------------------------------------------------------------

PSGW TRANSFER ENTRIES Transfer AOU Stock Entries

This option will copy the active stock entries from a selected Area of Use into one or more selected Areas. As many as 10 Areas may be chosen for transfer at one time. You may transfer either the drug name only, or the drug name, stock level,  
and location code. The copy process will not copy inactive drugs or duplicate entries. The actual transfer takes place in a background job which is automatically queued. When the transfer is complete, you will be notified by a MailMan message.

Type: run routine Routine: PSGWTR

------------------------------------------------------------

PSGW UPDATE AMIS STATS Update AMIS Stats File

This option is not on a menu, as it is a background job scheduled to run each night. The purpose of the option is to loop through the temporary inventory global and move the data into the AMIS subfile. The rescheduling frequency for this option is one day.

Type: run routine Routine: PSGWUAS

------------------------------------------------------------

PSGW USAGE REPORT Usage Report for an Item (80 column)

This option prints a usage report for (1) a specific item in an AOU, (2) a specific item for all AOUs, (3) all items for an AOU, or (4) all items for all AOUs. The user must specify AOU, item name and the start and stop dates for the report. The report prints AOU, item, the date of inventory, total quantity dispensed, quantity dispensed by auto-replenishment, quantity dispensed by on-demand requests, and quantity returned.

Type: run routine Routine: PSGWTOT

------------------------------------------------------------

PSGW WARD CONVERSION Ward (For Item) Conversion

This option will enable a user to change the Ward (for Item) designation from the old ward to a new ward for all items in all AOUs or in a single AOU. This can be used, for example, when a ward is closed down for construction. A background job can be queued for a later time to do the conversion and a MailMan message will be sent to the person who queued the job when it has run to completion.

Type: run routine Routine: PSGWCHG

------------------------------------------------------------

  
PSGW WARD INV PRINT Inventory Outline (80 column)

This option lists the principal information for a date range of inventories.

Type: run routine Routine: PSGWAIO

------------------------------------------------------------

PSGW WARD STOCK Production Menu

This menu provides access to the options that are used routinely in the normal Automatic Replenishment/Ward Stock operations.

Type: menu

Menu Items:

Inventory Sheet Print (132 column)

Single AOU Inventory Print (132 column)

Delete Inventory Date/Time

Input AOU Inventory

Pick List (132 column)

Enter/Edit Quantity Dispensed

On-Demand Requests

Backorder Requests

Return Items for AOU

Crash Cart Menu

Auto Replenishment Reports

------------------------------------------------------------

PSGW WARD STOCK MAINT Supervisor’s Menu

This option supports activities to build and maintain the files needed to operate Automatic Replenishment/Ward Stock. It also contains the necessary options to prepare the files to collect AMIS reporting information, run the AMIS report, and purge the system of obsolete data. Additionally, cost management reports are located on this menu.

Type: menu

Menu Items:

Set Up AR/WS (Build Files)

Prepare AMIS Data

Management Reports

Obsolete Data Purge

------------------------------------------------------------

PSGW ZERO USAGE Zero Usage Report (80 column)

For a user selected time frame, this report prints all items with no usage. The report may be printed for one AOU, several AOUs, or for ALL AOUs.

Type: run routine Routine: PSGWNU

------------------------------------------------------------

PSGWMGR Automatic Replenishment

Access to all options associated with Automatic Replenishment and Ward Stock.

Type: menu

Menu Items:

Production Menu

Supervisor’s Menu

------------------------------------------------------------

<span id="PSGW_23_19_GenParametersSectionBegin" class="anchor"></span>General Parameters (XPAR)<span id="_Toc511398567" class="anchor"></span>

Parameter Descriptions <span id="_Toc511398568" class="anchor"></span>

WARD STOCK LEVEL DISPLAY ON \[PSGW_WS_LVL_ON\]<span id="_Toc511398569" class="anchor"></span>

The system-level parameter WARD STOCK LEVEL DISPLAY ON \[PSGW_WS_LVL_ON\] allows for display of the maximum ward stock level in the Enter/Edit Nurses' On-Demand Request (80 column) \[PSGW ON‑DEMAND NURSING EDIT\] option and in the Print an On-Demand Report by Date/AOU (80 column) \[PSGW ON‑DEMAND PRINT\] option. The PSGW_WS_LVL_ON parameter definition is stored in the PARAMETER DEFINITION file (#8989.51). The value that the user assigns to the parameter is stored in the PARAMETER file (#8989.5).

To set the parameter, select the AR/WS Package-wide Parameter Edit \[PSGW PACKAGE PARAMETERS\] option from the Set Up AR/WS (Build Files) \[PSGW SETUP\] menu.

If set to YES, then the permitted ward stock level will appear in the Enter/Edit Nurses’ On-Demand Request (80 column) \[PSGW ON‑DEMAND NURSING EDIT\] option and in the Print an On-Demand Report by Date/AOU (80 column) \[PSGW ON‑DEMAND PRINT\] option. If set to NO, then the permitted ward stock level will not appear in these options.

Parameter Templates <span id="_Toc511398570" class="anchor"></span>

PSGW Package Lvl Param Edit \[PSGW PKG PAR\]<span id="_Toc511398571" class="anchor"></span>

NAME: PSGW PKG PAR

  DISPLAY TEXT: PSGW Package Lvl Param Edit

SEQUENCE: 1                             PARAMETER: PSGW_WS_LVL_ON

  
File Diagram<span id="_Toc511398572" class="anchor"></span>

The diagram on the next page points out the interrelationships of Automatic Replenishment/Ward Stock files. The AOU INVENTORY TYPE file entries must be defined first. These names are pointed to by two other files. AOU Item Location address codes should be established next. Five fields in the PHARMACY AOU STOCK file are pointers to the other files: ITEM points to the generic drug name from the DRUG file. TYPE is linked to the Type name from the AOU INVENTORY TYPE file, INPATIENT SITE points to the INPATIENT SITE file, WARD/LOCATION (FOR PERCENTAGE) points to the HOSPITAL LOCATION file, and LOCATION points to the address code from the AOU ITEM LOCATION file. The AOU field in the PHARMACY AOU STOCK file is pointed to by the AREA OF USE field from the AOU INVENTORY GROUP file. The AOU INVENTORY GROUP file, defined last, establishes inventory boundaries under an easy to remember group name.

![](automatic-replenishment-ward-stock-version-2-3-technical-manual/001.png)

<span id="_Toc511398573" class="anchor"></span>

; \[PSGW WARD STOCK MAINT\] \*\*Locked with PSGWMGR

> Set Up AR/WS (Build Files) \[PSGW SETUP\]

> Enter/Edit Inventory Types \[PSGW INV TYPE EDIT\]

> Item Location Codes - Enter/Edit \[PSGW ITEM LOC EDIT\]

> Create the Area of Use \[PSGW AREA OF USE EDIT\]

> Stock Items - Enter/Edit \[PSGW EDIT AOU STOCK\]

> Expiration Date - Enter/Edit \[PSGW EXPIRATION ENTER/EDIT\]

> Ward (For Item) Conversion \[PSGW WARD CONVERSION\]

> Add/Delete Ward (for Item) \[PSGW ADD/DEL WARD\]

> Transfer AOU Stock Entries \[PSGW TRANSFER ENTRIES\] \*\*Locked with PSGW TRAN

> Inactivate AOU \[PSGW AOU INACTIVATION\]

> Inactivate AOU Stock Item \[PSGW INACTIVATE AOU STOCK ITEM\]

> AOU Inventory Group - Enter/Edit \[PSGW AOU INV GROUP EDIT\]

> Print Set Up Lists \[PSGW PRINT SETUP LISTS\]

> Print Inventory Types (80 column) \[PSGW INV TYPE\]

> List Location Codes (80 column) \[PSGW ITEM LOC PRINT\]

> Show AOU/Ward/Service (132 column) \[PSGW SHOW AREA OF USE\]

> Print AR/WS Stock Item Data (132 column) \[PSGW STOCK ITEM DATA\]

> List Stock Items (132 column) \[PSGW PRINT AOU STOCK\]

> Inventory Group List (80 column) \[PSGW AOU INV GROUP PRINT\]

> Edit ‘Person Doing Inventory’ \[PSGW EDIT INVENTORY USER\]

> Sort AOUs in Group \[PSGW AOU INV GROUP SORT\]

> Site Parameters \[PSGW SITE\] \*\*Locked with PSGW PARAM

> <span id="PSGW_23_19_PackageParametersBuildFiles" class="anchor"></span>AR/WS Package-wide Parameter Edit \[PSGW PACKAGE PARAMETERS\] \*\*Locked with PSGWMGR

> Prepare AMIS Data \[PSGW PREPARE AMIS DATA\]

> Print AMIS Worksheet (80 column) \[PSGW PRINT AMIS WORKSHEET\]

> Enter AMIS Data for All Drugs/All AOUs \[PSGW ENTER AMIS DATA/ALL DRUGS\]

> Data for AMIS Stats - Print (132 column) \[PSGW PRINT DATA FOR AMIS STATS\]

> AMIS Data Enter/Edit (Single Drug) \[PSGW ENTER/EDIT AMIS DATA\]

> Identify AOU Returns & AMIS Count \[PSGW AOU RETURNS & AMIS COUNT\]

> Identify AOU INPATIENT SITE \[PSGW INPUT AOU INP SITE\]

> Show AOU Status for AMIS (80 column) \[PSGW AOU RET/AMIS CT PRINT\]

> Management Reports \[PSGW MGT REPORTS\]

> AR/WS AMIS Report \[PSGW AMIS\]

> Incomplete AMIS Data \[PSGW CLEAR AMIS EXCEPTIONS\]

> Print AMIS Report (132 column) \[PSGW PRINT AMIS REPORT\]

> Recalculate AMIS \[PSGW RECALCULATE AMIS\]

> Cost Report Per AOU (80 column) \[PSGW COST PER AOU\]

> Single Item Cost Report (80 column) \[PSGW SINGLE ITEM COST\]

> High Cost Report (80 column) \[PSGW HIGH COST\]

> High Volume Report (80 column) \[PSGW HIGH VOLUME\]

> Duplicate Entry Report (132 column) \[PSGW DUPLICATE REPORT\]

> Standard Cost Report (132 column) \[PSGW STANDARD COST\]

> Obsolete Data Purge \[PSGW PURGE\] \*\* Locked with PSGW PURGE

> AMIS Data Purge \[PSGW PURGE AMIS\]

> Purge Dispensing Data \[PSGW PURGE FILES\]

> **NOTE:** The following three options are background jobs and should be scheduled through TaskMan.

> \[PSGW PURGE INVENTORY\]

> \[PSGW RE-INDEX AMIS\]

> \[PSGW UPDATE AMIS STATS\]  
<span id="_Toc511398575" class="anchor"></span>; \[PSGW WARD STOCK\]

> Inventory Sheet Print (132 column) \[PSGW INVENTORY SHEET\]

> Single AOU Inventory Print (132 column) \[PSGW INVENTORY SINGLE\]

> Delete Inventory Date/Time \[PSGW DELETE INVENTORY\]

> Input AOU Inventory \[PSGW AOU INVENTORY INPUT\]

> Pick List (132 column) \[PSGW INVENTORY PICK LIST\]

> Enter/Edit Quantity Dispensed \[PSGW INVENTORY DISPENSE\]

> On-Demand Requests \[PSGW ON-DEMAND\]

> Enter/Edit On-Demand Request (80 column) \[PSGW ON- DEMAND EDIT\]

> Delete an On-Demand Request \[PSGW ON-DEMAND DELETE\]

> Print an On-Demand Report by Date/AOU (80 column) \[PSGW ON-DEMAND PRINT\]

> Backorder Requests \[PSGW BACKORDER\]

> Enter Backorders \[PSGW BACKORDER IN\]

> Fill Requests for Backorder Items \[PSGW BACKORDER EDIT\]

> AOU Backorder Report (80 column) \[PSGW BACKORDER AOU PRINT\]

> Current (ALL) Backorder Report (80 column) \[PSGW BACKORDER (ALL) PRINT\]

> Single Item Report (80 column) \[PSGW BACKORDER ITEM PRINT\]

> Multiple Items Report (80 column) \[PSGW BACKORDER ITEMS PRINT\]

> Return Items for AOU \[PSGW RETURN ITEMS\]

> Crash Cart Menu \[PSGW CRASH CART MENU\]

> Enter/Edit Crash Cart Locations \[PSGW CRASH CART LOCATION EDIT\]

> Print Crash Cart Locations \[PSGW CRASH CART LOCATION PRINT\]

> Auto Replenishment Reports \[PSGW REPORTS\]

> List Stock Items (132 column) \[PSGW PRINT AOU STOCK\]

> Expiration Date Report (80 column) \[PSGW EXP REPORT\]

> Inventory Outline (80 column) \[PSGW WARD INV PRINT\]

> Ward/AOU List for an Item (80 column) \[PSGW LOOKUP ITEM\]

> Item Activity Inquiry (80 column) \[PSGW ITEM INQUIRY\]

> Percentage Stock On Hand (132 column) \[PSGW STOCK PERCENTAGE\]

> Returns Analysis Report (80 column) \[PSGW RETURNS BREAKDOWN\]

> Usage Report for an Item (80 column) \[PSGW USAGE REPORT\]

> Zero Usage Report (80 column) \[PSGW ZERO USAGE\]

<span id="_Toc511398576" class="anchor"></span>;

> Auto Replenishment/Ward Stock Nurses’ Menu \[PSGW RN\]

> Enter/Edit Nurses’ On-Demand Request (80 column) \[PSGW ON- DEMAND NURSING EDIT\]

> List Stock Items (132 column) \[PSGW PRINT AOU STOCK\]

> Ward/AOU List for an Item (80 column) \[PSGW LOOKUP ITEM\]

Archiving and Purging<span id="_Toc511398577" class="anchor"></span>

At present, the Automatic Replenishment/Ward Stock module does not provide for the archiving of its data.

<span id="_Toc511398579" class="anchor"></span>

There are currently two options on the AR/WS Supervisor’s Menu allowing files to be purged. They are *AMIS Data Purge* and *Purge Dispensing Data*.

The amount of old data to be retained is a site specific decision. It is highly recommended that you keep data for at least one quarter. Use caution when choosing dates for deletion so as not to destroy needed data. These options delete the data from your files, and it is *not recoverable.AMIS Data Purge* \[PSGW PURGE AMIS\]

The purpose of this option is to purge old data from File 58.5 - AR/WS STATS file. Data should be kept in the file for at least one quarter to be able to produce the quarterly AMIS report. Use caution when choosing dates for deletion so as not to destroy needed data. The routine will not allow data newer than “T-100 days” to be deleted. The routine is automatically queued to run in the background.

*Purge Dispensing Data* \[PSGW PURGE FILES\]

The purpose of this option is to purge old data from Files 58.1 (PHARMACY AOU STOCK), File 58.3 (PHARMACY BACKORDER), and File 58.19 (PHARMACY AOU INVENTORY). Data should be kept in the files for at least one quarter or as far back as your site might choose to know usage, cost, etc. Use caution when choosing dates for deletion so as not to destroy needed data. The routine will not allow data newer than “T-100 days” to be deleted. The routine is queued to run in the background at a time that you select. Since the routine is CPU intensive, it should be queued to run in the off hours. It is highly recommended that you delete no more than two months data at a time.

The routine looks at inventory numbers that fall in the delete date range you selected. It loops through all automatic replenishment inventories, on-demand requests, and returns. Any inventories with outstanding backorders will not be deleted until the backorder is marked filled. (It may be beneficial to print the AOU Backorder Report to see if there are any old backorders that have been forgotten before running the *Purge Dispensing Data* option.) Inventory data that falls within the selected date range will be deleted in this loop. If there are drugs in an AOU which are inactivated and the inactivation date is before the “end date for  
deletion”, and the drugs have no inventory activity, these will be deleted from the AOU. Finally, any AOU which is not in an AOU Inventory Group and which contains no drugs (because they were inactivated and thus deleted in the above loop), will be deleted from File 58.1.

> **NOTE:** As long as an AOU is in an AOU Inventory Group, it will not be deleted. This relates to those AOUs which have no standard stock because they are used for on-demand requests only.

<span id="_Toc511398580" class="anchor"></span>

There is additionally, a background job which should be scheduled through TaskMan to run each night at a convenient time. The routine should run nightly, therefore the rescheduling frequency is “1D”. The purpose of the option is to purge the ^PSI(58.19,"AINV") global. This global location is the storage place for inventory sheets which have been printed. The data should remain in the global for a 100 day period. After that time, it is unlikely that the data will be needed. Therefore the data is purged from the system through this background job.

Using the TaskMan Manager’s *Schedule/unschedule Task Manager tasks* option, select the *PSGW PURGE INVENTORY* option. At the “QUEUED TO RUN AT WHAT TIME:” prompt, enter “T@” followed by the time you choose for the job to begin. The time should be one that does not conflict with system backup. At the “RESCHEDULING FREQUENCY:” prompt, enter “1D”. The “DEVICE” prompt should remain blank since this is a background job.

Example: How to Schedule a TaskMan Task

Select Systems Manager Menu Option: <u>TASK</u>Man Manager

Select TaskMan Manager Option: <u>SCH</u>edule/unschedule Task Manager tasks

Select OPTION to schedule or re-schedule: <u>PSGW PURGE INV</u>ENTORY

QUEUED TO RUN AT WHAT TIME: <u>T@2200</u>

DEVICE FOR QUEUED JOB OUTPUT: <u>\<RET\></u>

RESCHEDULING FREQUENCY: <u>1D</u>

QUEUED TO RUN ON VOLUME SET: *\[At this prompt, select the Volume Set name that the option should run on.\]*

Select OPTION to schedule or re-schedule: <u>\<RET\></u>

<span id="_Toc511398581" class="anchor"></span>

None of the Automatic Replenishment/Ward Stock routines have been designed to be called outside of the package. A package-wide variable, PSGWSITE, is set as users enter the package.

<span id="_Toc511398582" class="anchor"></span>

When possible, the following routines are recommended for routine mapping. Any routines not listed below may be mapped if you so desire.

PSGWAR PSGWAR1 PSGWARP PSGWATR PSGWATR1

PSGWBGIN PSGWBO PSGWBO1 PSGWBOE PSGWBOI

PSGWBOIP PSGWBOS PSGWCAD PSGWCAD1 PSGWCAD2

PSGWCAD3 PSGWCHG PSGWCL PSGWCLP PSGWEDI

PSGWEDI1 PSGWEXP PSGWKINV PSGWL PSGWOD2

PSGWODP PSGWODPR PSGWODRN PSGWOND PSGWONDM

PSGWPI PSGWPI1 PSGWPI2 PSGWPL PSGWPL0

PSGWPL1 PSGWSET PSGWSTKI PSGWUAS PSGWUTL

PSGWUTL1 PSGWVW PSGWWRD

<span id="_Toc511398583" class="anchor"></span>

If you choose to delete the Init routines (PSGWI\*), you may also delete routines PSGWPOST, PSGWPST1, and PSGWPRE\* as they are used only by the initialization process.

<span id="_Toc511398584" class="anchor"></span>

The Automatic Replenishment/Ward Stock module relies on, at least, the following external packages to run effectively:

> <u>Package</u> <u>Minimum Version Needed</u>

> Kernel 7.0

> VA FileMan 19.0

> MailMan 7.0

> MAS 5.2

> Outpatient Pharmacy 5.6

> AR/WS 2.04\*

AR/WS references the HOSPITAL LOCATION file (#44), so that AOUs may be assigned to specific Hospital Locations for statistical purposes.

AR/WS also has a tie to the Unit Dose package, so that Unit Dose will know which items in your DRUG file are Ward Stock items for each ward.

<span id="_Toc511398585" class="anchor"></span>

An integration agreement has been granted between Automatic Replenishment/Ward Stock and Drug Accountability. The ^PSGWUAS routine contains a call to ^PSARWS. ^PSARWS will traverse the ^PSI(58.5,”AMIS”) cross-reference to update the AR/WS dispensing in Drug Accountability.

SAC Exemption^PSI(58.19,"AINV", Global Exception Granted to Standards

A MUMPS cross-reference - ^PSI(58.19,"AINV", - contains the sort order for the inventory sheets used in the Automatic Replenishment/Ward Stock package. The sort order must be captured because later routines use the sort order for various input processes. If the files have been updated, re-creation of the sort order will result in a discrepancy between the printed page and what the user views on the screen.

AR/WS creates an inventory sheet which is sorted by: Area of Use, 1st location, 2nd location, 3rd location, inventory type, and drug name. The global layout is: ^PSI(58.19,"AINV",INV#,AOU,LOC1,LOC2,LOC3,TYPE,DRUG).

> INV# is the internal number from File 58.19 of the inventory being done.

> AOU is the internal number from File 58.1 of the AOU being inventoried.

> LOC1 is the 1st piece (delimiter is a comma) of the item location from File 58.1.

> LOC2 is the 2nd piece (delimiter is a comma) of the item location from File 58.1.

> LOC3 is the 3rd piece (delimiter is a comma) of the item location from file 58.1.

> TYPE is the internal number from file 58.16 of the inventory type for the item.

> DRUG is the actual drug name from file 50 for the item.

The cross-reference is hard coded in the inventory sheet routine - ^PSGWPI1. The cross-reference is killed periodically by a background job (PSGWKINV), because the inventory sheet has a limited life span of 100 days. This global must be translated.

The ^PSI global is currently journaled which means the inventory sheet is also journaled. ^PSI must be journaled because all AR/WS files live in ^PSI. ^PSI(58.19,"AINV", does not have to be journaled because it could be recreated and once created it has a 100 day life cycle. There are currently no globals in AR/WS that are not journaled.

If destroyed through some mishap, the cross-reference is easily recreated by running the inventory sheet(s) again. This can be accomplished by the user or Site Manager. Not all inventory sheets would need to be re-created; just those outstanding. There are no restrictions on when this can be re-created.

In AR/WS version 1.0, this data was stored in a non-Fileman global ^PSG("PSGW"). The global was changed for version 1.1 to its current format (a cross-reference) based on discussion and recommendations at a peer review of another Inpatient Pharmacy package.

Since this cross-reference cannot be recreated by use of Fileman in this version reindexing and is created and killed through routines, its Fileman compatibility was questioned. Thus, the request for an exception to the standard was made. The request was passed by the SAC Committee on March 24,1988.

<span id="_Toc511398586" class="anchor"></span>

All of the Automatic Replenishment/Ward Stock package options have been designed to stand alone. Each option requires the use of the package-wide variable PSGWSITE that is set as users enter the package. Even though all options are able to be independently invoked, users will be repeatedly asked to select an Inpatient Site (if there are two or more sites that are flagged for AR/WS use) if top level AR/WS menus do not contain the following enter and exit code in the OPTION file:

EXIT ACTION : K PSGWSITE

ACTION : I '\$D(PSGWSITE) D ^PSGWSET

<span id="_Toc511398587" class="anchor"></span>

Automatic Replenishment/Ward Stock contains only one package-wide variable PSGWSITE. This variable must be defined and is required for the package to run. PSGWSITE is set in the routine ^PSGWSET as package users enter the module.

Some stations design their own menus for individual users. If this is the case, then the top level AR/WS menu must contain the following enter and exit code in the OPTION file:

EXIT ACTION : K PSGWSITE

ACTION : I '\$D(PSGWSITE) D ^PSGWSET

This enter and exit code must be present because the PSGWSITE variable is set as users enter the package. If the Kernel’s ^OPTION NAME feature is used to jump directly into lower levels of the AR/WS package, then the “Inpatient Site Name” prompt *must be* answered in order to define the PSGWSITE variable. All options are independently invokable, however, if the instructions above are not followed, users will be repeatedly asked to select an Inpatient Site if there are two or more sites that are flagged as selectable for AR/WS use.

<span id="_Toc511398588" class="anchor"></span>

Throughout the entire Inpatient Automatic Replenishment/Ward Stock module, you may obtain on-line help. You may enter a question mark (?) at any prompt to assist you in your choice of actions.

The Data Dictionaries (DDs) are considered part of the on-line documentation for this software application. Use VA FileMan option *LIST FILE ATTRIBUTES* to print the DDs. The following are the files for which you should print DDs:

> \#50 DRUG

> \#58.1 PHARMACY AOU STOCK

> \#58.16 AOU INVENTORY TYPE

> \#58.17 AOU ITEM LOCATION

> \#58.19 PHARMACY AOU INVENTORY

> \#58.2 AOU INVENTORY GROUP

> \#58.3 PHARMACY BACKORDER

> \#58.5 AR/WS STATS FILE

> \#59.4 INPATIENT SITE

> \#59.7 PHARMACY SYSTEM

The namespace for the Automatic Replenishment/Ward Stock module is PSGW.

<span id="_Toc511398589" class="anchor"></span>

Stations may delete all templates for the AR/WS files except those listed below (and except for any local templates created):

FILE \#58.1 PHARMACY AOU STOCK

<u>Input Templates</u>

PSGW AREA OF USE EDIT

PSGW INACTIVATE ITEM

<u>Print Templates</u>

PSGW PERCENTAGE

PSGW SHOW AREA OF USE

<u>Sort Templates</u>

PSGW PERCENTAGE

PSGW SHOW AREA OF USE

FILE \#58.16 AOU INVENTORY TYPE

<u>Print Template</u>

PSGW INV TYPE

<u>Sort Template</u>

PSGW INV TYPE

FILE \#58.17 AOU ITEM LOCATION

<u>Print Template</u>

PSGW ITEM LOC

<u>Sort Template</u>

PSGW ITEM LOC

  
FILE \#58.2 AOU INVENTORY GROUP

<u>Input Template</u>

PSGW WARD INVENTORY

AR/WS Template in Shared Files

<u>Input Templates</u> <u>File</u>

PSGW ENTER/EDIT AMIS DATA DRUG file (#50)

<span id="_Toc511398590" class="anchor"></span>

> AMIS Category The AMIS category will classify AR/WS drugs for AMIS purposes. The four AMIS categories are “0”, “1”, “2”, and “3”. “0” means the drug is classified as field 03 or 04. This includes tablets, capsules, multi-dose vials, etc. It does not include multiple- dose externals, liquids, or antacids. “1” means the drug is classified as field 06 or 07. This includes multiple-dose externals, liquids, antacids, otics, ophthalmic, and inhalations. “2” means the drug is classified as field 17. This includes solutions and administration sets. “3” means the drug is classified as field 22. This includes blood and blood products.

> AMIS Conversion The AMIS conversion number reflects the

> Number number of doses/units contained in a single quantity dispensed. For example, for a 20cc vial, the quantity dispensed is 1, and the AMIS conversion number is 20.

> AOU - Area of Use An Area of Use is a place where commonly stocked items are stored for use by wards or treatment areas. An AOU may serve one or more wards or clinics, or, as in the case of “cardiac cath lab”, no ward.

> AOU Inventory Group An AOU Inventory Group is defined by pharmacy to represent the Areas which are inventoried together as a “batch” or “cluster”. This is a way to “group” commonly inventoried AOUs under an easy to remember inventory group name. For each AOU in the inventory group, you may specify which inventory types will be included for this specific inventory group. By defining the inventory groups initially, you do not have to re-define the inventory boundaries every time a particular inventory is scheduled.

> Automatic A method of drug distribution and inventory

> Replenishment/Ward management within a hospital. Drug

> Stock products can be automatically inventoried and delivered to an Area of Use (AOU) or requested on demand.

> Backorder Amount A backorder occurs when the actual amount dispensed is less than the “to be dispensed” amount (i.e., pharmacy did not have sufficient stock to fill the total number requested). The difference between these two amounts is the total that should be on backorder. Backorder amount is figured by the computer if both the inventory sheet and pick list are printed. If the MERGE INV. SHEET AND PICK LIST site parameter is set to “YES”, then the backorder amount must be entered using the *Enter Backorders* option.

> Backorder File Backorder requests are created automatically by the computer when the inventory sheet and pick list are not merged. File 58.3 contains item name, AOU, date of backorder, quantity backordered, and date filled.

> Inpatient Site The INPATIENT SITE field for each AOU defined in the PHARMACY AOU STOCK file (#58.1) contains the name of the Inpatient Site (from the INPATIENT SITE file, see the next definition below) that will receive credit for all AMIS transactions that occur in the AOU. It is *very important* that this field be defined!! If it is not, all transactions for the AOU will be ignored and will directly affect the accuracy of the AMIS Stats Report.

> Inpatient Site File The INPATIENT SITE file contains site

> (#59.4) parameters which allow a station to “customize” the software. AR/WS parameters affect (1) whether or not a separate inventory sheet and pick list are printed, (2) whether or not columns are printed on the inventory sheet for returns, (3) when the collection of AMIS data begins, and (4) whether the site name is used for Automatic Replenishment or Unit Dose.

> Inventory Sheet The printed form used to take inventory. Includes item location within AOU, item name, stock level required, a column to record the amount on-hand, and a column to record returns. (Return column prints only if the PRINT RETURN COLUMNS site parameter is set to “YES”).

> Inventory Type Name or names linked to items found in the AOU allowing you to inventory BY THIS TYPE. For example, isopropyl alcohol could be classified as an External. An item may have more than one inventory type. This will allow the item to be selected for inventory by either type.

> Item Address Code A code that represents the location of an

> (Location Code) item in the AOU. For example, if isopropyl alcohol is stored in an AOU on the second set of shelves, third shelf from the top, its item address code could be expressed as S,2,3. The address code can consist of up to three levels separated by a comma. Each level should further define the exact location. The code is associated with an expansion for clarity.

> Item Address Code Text used to clarify the meaning of an item

> Expansion address code. For example, on the inventory sheet and pick list, the code S would be expanded and printed as shelf. (These codes and expansions are locally created terms.)

> Minimum Quantity The least amount of an item to be

> to Dispense dispensed. If defined for an item it will be used by a site as a guideline for dispensing items that are best dispensed in bulk quantities.

> On Demand Request Non-scheduled distribution of an item to an AOU.

> PSGW PARAM The PSGW PARAM key should be given *only* to the Inpatient Pharmacy Package Coordinator. This lock controls when the collection of AMIS data begins.

> PSGW PURGE The PSGW PURGE key should be given *only* to the Inpatient Pharmacy Package Coordinator or his/her designee. This lock controls the deletion of data from the AR/WS files and should be assigned with discretion.

> PSGW TRAN The PSGW TRAN key should be given *only* to the Inpatient Pharmacy Package Coordinator or his/her designee. The key controls access to the *Transfer AOU StockEntries* option. Using the transfer option, users may “copy” the stock entries from one Area of Use into other Areas.

> PSGW RN Primary menu option for the Automatic Replenishment/Ward Stock Nurses’ Menu. This menu allows nursing to enter on demand requests, list stock items, and locate AOUs which stock a specified item.

> PSGWMGR The name of the key that must be assigned to Inpatient Pharmacy Package Coordinators using the AR/WS package. This key allows access to the *Supervisor’sMenu* options. Also, the name of the primary menu option to be assigned to all pharmacy personnel using the AR/WS package.

> Pick List Used to dispense the inventory. This is a two part report. The first part prints in the same format as the inventory sheet. It shows: item location, item name, stock level, on-hand amount, total backorders, the amount to be dispensed, and a column to enter the amount dispensed if it is less than the number in the “to be dispensed” column. The second part of the pick list is used by the pharmacy to pick the items. It contains item name, quantity to be dispensed, and a column to record actual quantity dispensed.

> Quick Code An abbreviated form of the drug generic name (from 1 to 10 characters). Lookup is done on print name, QUICK CODE, or synonym. Quick codes are displayed on the Inventory Sheet.

> Reorder Level If defined for an item, this is the stock level an item should reach before it can be replenished.

> Service Service is located under Ward (For Percentage) in the Pharmacy AOU Stock File. It is the name of the service which composes the ward. For example, cardiology and neurology are services.

> Service Percentage The percentage of ward use by a particular service. For example, 40 beds used by Cardiology out of 100 would be 40%.

> Stock Item An item (from the drug file) stored in the AOU.

> Stock Level The quantity of an item stocked in a specific AOU.

> Ward (for item) The name of the ward or wards that will use this particular item. It is important to accurately answer this prompt because this is the link between the AR/WS package and the Unit Dose package. The Unit Dose package looks at this field to know if the drug is a Ward Stock item.

> Ward/Location The name of the MAS location that is served

> (for percentage) partially or totally by an Area of Use. This field will generally be used for reporting purposes. If the AOU is *not* composed of any wards, enter “^” at the “Ward/Location (for percentage)” prompt.

Index<span id="_Toc511398591" class="anchor"></span>

A

Agreement 49

AMIS Data Purge 45

Archiving 45

Auto-Purging 46C

Callable Routines 47

Change Pages 3D

Deleting Init Routines 47E

Exported Options 15

External Relations 49F

File Descriptions 11

File Diagram 37

File List 11G

Glossary 59I

Implementation and Maintenance 5

Internal Relations 51

Introduction 1K

Keys 15  
L

Legal Requirements 3M

Manual Purging 45

Menu Outline 39

Menus 15N

Nurses’ Menu 43O

On-Line Documentation 55

Option Descriptions 17

Orientation 3P

Package Functional Description 3

Package Management 3

Package-Wide Variables 53

Production Menu 41

Purge Dispensing Data 45R

Resource Requirements 5

Routine Descriptions 7

Routine List 7

Routine Mapping 47S

Site Configuration 5

Special Notations 3

Stand-Alone Options 16

Supervisor’s Menu 39T

Templates 56