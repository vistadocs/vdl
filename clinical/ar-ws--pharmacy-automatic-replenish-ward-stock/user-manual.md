---
title: Automatic Replenishment/Ward Stock Version 2.3 User Manual
doc_type: UM
doc_label: User Manual
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
description: "<table> <colgroup> <col style=\\"width: 13%\\" /> <col style=\\"width: 16%\\" /> <col style=\\"width: 12%\\" /> <col style=\\"width: 27%\\" /> <col style=\\"width: 15%\\" /> <col style=\\"width: 15%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th><strong>Date</strong></th> <th><p><strong>Version/</strong></p> <p><strong>"
audience: 
keywords: 
  - report
  - stock
  - amis
  - inventory
  - date
  - pharmacy
  - inpatient
  - print
  - room
  - replenishment
page_count: 0
word_count: 43564
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: January 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/wsuser.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/wsuser.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=83"
---

Decentralized Hospital Computer Program

INPATIENT PHARMACYAUTOMATIC REPLENISHMENT/WARD STOCK MODULEUSER MANUAL

January 1994

(Revised April 2018)

Information Systems Center

Birmingham, Alabama

\[This page intentionally left blank.\]

REVISION HISTORY

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
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
<td><a href="#StdStockLvlMenuUpdate"><u>10</u></a>, <u><a href="#PSGWSiteOptionBegin">58</a>-<a href="#PSGWSiteOptionEnd">59</a></u>, <a href="#StockLvlSection"><u>63</u></a>, <a href="#MaxStockExpl2"><u>140</u></a>-<a href="#StdStockScreen3"><u>141</u></a>, <a href="#StockLvlAllowedText"><u>188</u></a>-<a href="#StdStockScreen4_end"><u>190</u></a></td>
<td>Added information about setting a designated printer to auto-print ward stock medications in a pharmacy and displaying ward stock level in Nurses' and Pharmacy on-demand reports.</td>
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

PREFACE

The Automatic Replenishment/Ward Stock User Manual discusses capabilities, uses, and features of the AR/WS module for Inpatient Pharmacy Package Coordinators, Inpatient Pharmacists, and Pharmacy Technicians. There is additionally, an AR/WS Nurses’ Menu described which some stations may elect to use.

Table of ContentsIntroduction [1](#_Toc511400081)

Package Functional Description [1](#_Toc511400082)

How This Manual Is Organized [1](#_Toc511400083)

Special Instructions for the [1](#_Toc511400084)

Special Notations [2](#_Toc511400085)

Package Management/Legal Requirements [2](#_Toc511400086)

Menu Outline [3](#_Toc511400087)

Supervisor’s Menu [3](#_Toc511400087)

Production Menu [5](#_Toc511400089)

Nurses’ Menu [6](#_Toc511400090)

Package Operation Section [7](#_Toc511400091)

Chapter One: Supervisor’s Menu [9](#_Toc511400092)

1.0 Set Up AR/WS (Build Files) [10](#_Toc511400093)

1.1 Enter/Edit Inventory Types [12](#_Toc511400094)

1.2 Item Location Codes - Enter/Edit [14](#_Toc511400095)

1.3 Create the Area of Use [17](#_Toc511400096)

1.4 Stock Items - Enter/Edit [24](#_Toc511400097)

1.5 Expiration Date - Enter/Edit [29](#_Toc511400098)

1.6 Ward (For Item) Conversion [30](#_Toc511400099)

1.7 Add/Delete Ward (for Item) [32](#_Toc511400100)

1.8 Transfer AOU Stock Entries [35](#_Toc511400101)

1.9 Inactivate AOU [37](#_Toc511400102)

1.10 Inactivate AOU Stock Item [38](#_Toc511400103)

1.11 AOU Inventory Group-Enter/Edit [39](#_Toc511400104)

1.12 Print Set Up Lists [43](#_Toc511400105)

1.12.1 Print Inventory Types [44](#_Toc511400106)

1.12.2 List Location Codes [45](#_Toc511400107)

1.12.3 Show AOU/Ward/Service [46](#_Toc511400108)

1.12.4 Print AR/WS Stock Item Data [47](#_Toc511400109)

1.12.5 List Stock Items [49](#_Toc511400110)

1.12.6 Inventory Group List [53](#_Toc511400111)

1.13 Edit ‘Person Doing Inventory’ [55](#_Toc511400112)

1.14 Sort AOUs in Group [56](#_Toc511400113)

1.15 Site Parameters [58](#_Toc511400114)

1.16 .AR/WS Package-wide Parameter Edit \[PSGW PACKAGE PARAMETERS\] [63](#_Toc511400115)

2.0 Prepare AMIS Data [64](#_Toc511400116)

2.1 Print AMIS Worksheet [65](#_Toc511400117)

2.2 Enter AMIS Data for All Drugs/All AOUs [68](#_Toc511400118)

2.3 Data for AMIS Stats - Print [70](#_Toc511400119)

2.4 AMIS Data Enter/Edit (Single Drug) [72](#_Toc511400120)

2.5 Identify AOU Returns & AMIS Count [73](#_Toc511400121)

2.6 Identify AOU INPATIENT SITE [75](#_Toc511400122)

2.7 Show AOU Status for AMIS [77](#_Toc511400123)

3.0 Management Reports [78](#_Toc511400124)

3.1 AR/WS AMIS Report [79](#_Toc511400125)

3.1.1 Incomplete AMIS Data [82](#_Toc511400126)

3.1.2 Print AMIS Report [84](#_Toc511400127)

3.1.3 Recalculate AMIS [86](#_Toc511400128)

3.2 Cost Report Per AOU [88](#_Toc511400129)

3.3 Single Item Cost Report [92](#_Toc511400130)

3.4 High Cost Report [93](#_Toc511400131)

3.5 High Volume Report [96](#_Toc511400132)

3.6 Duplicate Entry Report [98](#_Toc511400133)

3.7 Standard Cost Report (132 column) [101](#_Toc511400134)

4.0 Obsolete Data Purge [105](#_Toc511400135)

4.1 AMIS Data Purge [106](#_Toc511400136)

4.2 Purge Dispensing Data [107](#_Toc511400137)

5.0 \[PSGW PURGE INVENTORY [109](#_Toc511400138)

6.0 \[PSGW RE-INDEX AMIS [110](#_Toc511400139)

7.0 \[PSGW UPDATE AMIS STATS [112](#_Toc511400140)

Chapter Two: Production Menu [117](#_Toc511400141)

Production Menu [117](#_Toc511400141)

1.0 Inventory Sheet Print [118](#_Toc511400143)

2.0 Single AOU Inventory Print [122](#_Toc511400144)

3.0 Delete Inventory Date/Time [124](#_Toc511400145)

4.0 Input AOU Inventory [125](#_Toc511400146)

5.0 Pick List [128](#_Toc511400147)

6.0 Enter/Edit Quantity Dispensed [132](#_Toc511400148)

7.0 On-Demand Requests [135](#_Toc511400149)

7.1 Enter/Edit On-Demand Request [136](#_Toc511400150)

7.2 Delete an On-Demand Request [139](#_Toc511400151)

7.3 Print an On-Demand Report by Date/AOU [140](#_Toc511400152)

8.0 Backorder Requests [142](#_Toc511400153)

8.1 Enter Backorders [143](#_Toc511400154)

8.2 Fill Requests for Backorder Items [145](#_Toc511400155)

8.3 AOU Backorder Report (80 column) [146](#_Toc511400156)

8.4 Current (ALL) Backorder Report (80 column) ; [148](#_Toc511400157)

8.5 Single Item Report (80 column) [152](#_Toc511400158)

8.6 Multiple Items Report (80 column) [153](#_Toc511400159)

9.0 Return Items for AOU [155](#_Toc511400160)

10.0 Crash Cart Menu [156](#_Toc511400161)

10.1 Enter/Edit Crash Cart Locations [157](#_Toc511400162)

10.2 Print Crash Cart Locations [158](#_Toc511400163)

11.0 Auto Replenishment Reports [159](#_Toc511400164)

11.1 List Stock Items (132 column) [160](#_Toc511400165)

11.2 Expiration Date Report (80 column) [164](#_Toc511400166)

11.3 Inventory Outline (80 column) [169](#_Toc511400167)

11.4 Ward/AOU List for an Item (80 column) [171](#_Toc511400168)

11.5 Item Activity Inquiry (80 column) [172](#_Toc511400169)

11.6 Percentage Stock On Hand (132 column) [174](#_Toc511400170)

11.7 Returns Analysis Report (80 column) [176](#_Toc511400171)

11.8 Usage Report for an Item (80 column) [178](#_Toc511400172)

11.9 Zero Usage Report (80 column) [182](#_Toc511400173)

Chapter Three: Auto Replenishment/Ward Stock Nurses’ Menu [187](#_Toc511400174)

1.0 Enter/Edit Nurses’ On-Demand Request (80 column) [188](#_Toc511400175)

2.0 List Stock Items (132 column) [191](#_Toc511400176)

3.0 Ward/AOU List for an Item (80 column) [194](#_Toc511400177)

Appendices [198](#appendices)

Appendix A. How To Work With The System [198](#_Toc511400179)

Glossary [209](#_Toc511400180)

Index [217](#_Toc511400181)

Introduction<span id="_Toc511400081" class="anchor"></span>

Automatic Replenishment (AR)/Ward Stock (WS) is a method of drug distribution and inventory management within a hospital. Drug products can be automatically inventoried and delivered (AR) to an area of use (AOU) or requested on demand (WS). An area of use is the place where commonly stocked items are stored. The area is potentially composed of wards, clinics, and specialties.

<span id="_Toc511400082" class="anchor"></span>

The Automatic Replenishment process usually consists of the following functions: 1) select the AOUs and types of items within each AOU to be inventoried, 2) visit each AOU and take inventory, 3) determine the quantity to be dispensed for each item, and 4) dispense the item. The Automatic Replenishment module is designed to allow each VAMC to adapt the system to its own needs.

Version 2.3 of the AR/WS package contains several new features. Several new options have been added. On the Supervisor’s Menu there is now a *DuplicateEntry Report* option that prints a report of duplicate entries. The report will show all inventory, return, and on-demand data for each drug selected. The *SingleAOU Inventory Print* option has been added to the Production menu. This option will print an inventory sheet for a single AOU that is included in the inventory date/time. In addition, a new Crash Cart Menu has been added, and all reports have been modified to allow selection of AOUs by Inventory Group and changed to form feed only at the end of a report.

<span id="_Toc511400083" class="anchor"></span>

This User Manual is divided into three parts. Chapter One contains the “Supervisor’s Menu”; Chapter Two, the “Production Menu”; and Chapter Three, the “Nurses’ Menu”. Each of these chapters gives the purpose of each option contained on the specific menu and is followed by an example of how to use the option. Chapter Three is followed by an Appendices which contains a section on “Working with the System”. “Working with the System” presents information which will be useful to persons who have not previously used DHCP software.

<span id="_Toc511400084" class="anchor"></span>

If you are unfamiliar with the AR/WS module or other DHCP software applications, we recommend that you study the DHCP *Users Guide to Computing.* This orientation guide is a comprehensive handbook benefiting first time users of any DHCP application. The purpose of the introductory material is to help you become familiar with basic computer terms and the components of a computer. It is reproduced and distributed periodically by the Kernel Development Group. To request a copy, contact your local Information Resource Management (IRM) staff.

<span id="_Toc511400085" class="anchor"></span>

In this manual, the user’s response is <u>underlined</u> and in bold type, but will not appear on the screen underlined and bold. The underlined and bold part of the entry is the letter or letters that must be typed so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy.

Every response you type in must be followed by pressing the Return key (or Enter key for some keyboards). Whenever the Return or Enter key should be pressed, you will see the symbol <u>\<RET\></u>. This symbol is not shown but is implied if there is underlined input.

Within the examples representing actual terminal dialogues, the author may offer information about the dialogue. This information is enclosed in brackets

(e.g., *\[Screen Clears\]*) and will not appear on the screen.

<span id="_Toc511400086" class="anchor"></span>

This package does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements.

<span id="_Toc511400087" class="anchor"></span>

> Set Up AR/WS (Build Files)

> Enter/Edit Inventory Types

> Item Location Codes - Enter/Edit

> Create the Area of Use

> Stock Items - Enter/Edit

> Expiration Date - Enter/Edit

> Ward (For Item) Conversion

> Add/Delete Ward (for Item)

> Transfer AOU Stock Entries

> Inactivate AOU

> Inactivate AOU Stock Item

> AOU Inventory Group - Enter/Edit

> Print Set Up Lists

> Print Inventory Types (80 column)

> List Location Codes (80 column)

> Show AOU/Ward/Service (132 column)

> Print AR/WS Stock Item Data (132 column)

> List Stock Items (132 column)

> Inventory Group List (80 column)

> Edit ‘Person Doing Inventory’

> Sort AOUs in Group

> Site Parameters

> Prepare AMIS Data

> Print AMIS Worksheet (80 column)

> Enter AMIS Data for All Drugs/All AOUs

> Data for AMIS Stats - Print (132 column)

> AMIS Data Enter/Edit(Single Drug)

> Identify AOU Returns & AMIS Count

> Identify AOU INPATIENT SITE

> Show AOU Status for AMIS (80 column)

> Management Reports

> AR/WS AMIS Report

> Incomplete AMIS Data

> Print AMIS Report (132 column)

> Recalculate AMIS

> Cost Report Per AOU (80 column)

> Single Item Cost Report (80 column)

> High Cost Report (80 column)

> High Volume Report (80 column)

> Duplicate Entry Report (132 column)

> Standard Cost Report (132 column)

> Obsolete Data Purge

> AMIS Data Purge

> Purge Dispensing Data

> **NOTE:** The following three options are background jobs and should be scheduled through Taskman.

> \[PSGW PURGE INVENTORY\]

> \[PSGW RE-INDEX AMIS\]

> \[PSGW UPDATE AMIS STATS\]  
<span id="_Toc511400089" class="anchor"></span>

> Inventory Sheet Print (132 column)

> Single AOU Inventory Print (132 column)

> Delete Inventory Date/Time

> Input AOU Inventory

> Pick List (132 column)

> Enter/Edit Quantity Dispensed

> On-Demand Requests

> Enter/Edit On-Demand Request (80 column)

> Delete an On-Demand Request

> Print an On-Demand Report by Date/AOU (80 column)

> Backorder Requests

> Enter Backorders

> Fill Requests for Backorder Items

> AOU Backorder Report (80 column)

> Current (ALL) Backorder Report (80 column)

> Single Item Report (80 column)

> Multiple Items Report (80 column)

> Return Items for AOU

> Crash Cart Menu

> Enter/Edit Crash Cart Locations

> Print Crash Cart Locations

> Auto Replenishment Reports

> List Stock Items (132 column)

> Expiration Date Report (80 column)

> Inventory Outline (80 column)

> Ward/AOU List for an Item (80 column)

> Item Activity Inquiry (80 column)

> Percentage Stock On Hand (132 column)

> Returns Analysis Report (80 column)

> Usage Report for an Item (80 column)

> Zero Usage Report (80 column)

<span id="_Toc511400090" class="anchor"></span>

> Auto Replenishment/Ward Stock Nurses’ Menu

> Enter/Edit Nurses’ On-Demand Request (80 column)

> List Stock Items (132 column)

> Ward/AOU List for an Item (80 column)

Package Operation Section<span id="_Toc511400091" class="anchor"></span>

Chapter One: Supervisor’s Menu<span id="_Toc511400092" class="anchor"></span>

Supervisor’s Menu \[PSGW WARD STOCK MAINT\]

This option supports activities to build and maintain the files needed to operate Automatic Replenishment/Ward Stock. It also contains the necessary options to prepare the files to collect AMIS (Automated Management Information System) reporting information, run the AMIS and other management reports, and purge the system of obsolete data.

There are currently four options on this menu. They include

> *Set Up AR/WS (Build Files)*

> *Prepare AMIS Data*

> *Management Reports*

> *Obsolete Data Purge*

The *Supervisor’s Menu* option is locked. Access to the above four options is limited to those who are given the PSGWMGR key. The PSGWMGR key should be assigned to the Inpatient Pharmacy Package Coordinator and/or a designee.

Getting Out of an Option

To stop what you are doing, enter an up-arrow (^). You can use the up-arrow at any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering up-arrows to completely exit from the system.

1.0 Set Up AR/WS (Build Files)<span id="_Toc511400093" class="anchor"></span>; \[PSGW SETUP\]

The *Set Up AR/WS (Build Files)* menu supports the management of files used during the initial set up of Automatic Replenishment/Ward Stock. It includes the creating, editing, listing, and deleting of data in the AR/WS files. You should be forewarned that it takes a considerable amount of time and effort to set up this module. Numerous worksheets and diagrams are provided to assist you in this endeavor.

There are currently <span id="StdStockLvlMenuUpdate" class="anchor"></span>16 sub options on this menu. They include

> *Enter/Edit Inventory Types*

> *Item Location Codes - Enter/Edit*

> *Create the Area of Use*

> *Stock Items - Enter/Edit*

> *Expiration Date - Enter/Edit*

> *Ward (For Item) Conversion*

> *Add/Delete Ward (for Item)*

> *Transfer AOU Stock Entries*

> *Inactivate AOU*

> *Inactivate AOU Stock Item*

> *AOU Inventory Group - Enter/Edit*

> *Print Set Up Lists . . .*

> *Edit ‘Person Doing Inventory’*

> *Sort AOUs in Group*

> *Site Parameters*

> *AR/WS Package-wide Parameter Edit*

The diagram on the next page points out the interrelationships of AUTOMATIC REPLENISHMENT/WARD STOCK files. The AOU INVENTORY TYPE file entries must be defined first. These names are pointed to by two other files. AOU Item Location address codes should be established next. Five fields in the PHARMACY AOU STOCK file are “pointers” to the other files: ITEM points to the generic drug name from the DRUG file. TYPE is linked to the Type name from the AOU INVENTORY TYPE file, INPATIENT SITE points to the INPATIENT SITE file, WARD/LOCATION (FOR PERCENTAGE) points to the HOSPITAL LOCATION file, and LOCATION points to the address code from the AOU ITEM LOCATION file. The AOU field in the PHARMACY AOU STOCK file is pointed to by the AREA OF USE field from the AOU INVENTORY GROUP file. The AOU INVENTORY GROUP file, defined last, establishes inventory boundaries under an easy to remember group name.

![](automatic-replenishment-ward-stock-version-2-3-user-manual/001.png)  
1.1 Enter/Edit Inventory Types<span id="_Toc511400094" class="anchor"></span>; \[PSGW INV TYPE EDIT\]

This option is used to enter and edit the data in the AOU INVENTORY TYPE file (#58.16). Inventory types are used to classify the items in an Area of Use. Inventories in the Automatic Replenishment/Ward Stock module are defined around these inventory types. Each user defines his own types, the types may be as broad or as narrow as desired. For example, externals, oral solids, oral liquids, internals, and solutions and sets might all be inventory types. However, if you wish to break it down even further, you may. For example, if you wish to inventory externals that come in tubes separately from externals that do not come in tubes, you could create two inventory types: 1) external - tube, and 2) external - no tube.

Data must be entered into the following fields to set up the AOU INVENTORY TYPE file:

> NAME:

> Enter the name of an inventory type, i.e., injections, external, internal, oral liquid, or oral solid. This will be used to group items in each Area of Use.

> TYPE DESCRIPTION:

> Enter information that describes this inventory type. Make the definition as clear as possible (e.g., External at this site means...) This field is purely informational.

You must make your entries into the AOU INVENTORY TYPE file before editing any other files, because other files point to these entries.

All types are defined by you, with one exception. You *must* enter “ALL” as an inventory type. “ALL” is used when you wish to inventory all types on the same inventory sheet. Enter the name as “ALL”, with a description of “Used to select all types”.

Various printouts in the AR/WS module are sorted by the types defined in this file. The Inventory Sheet and Pick List sort by item location, and within location by type. The *Prepare AMIS Data* options present the drug items in order by type. Also, the *List Stock Items* option may be printed in order by type and location.

After inventory types have been entered, a printout of the file data may be obtained by using the *Print Inventory Types* option located on the *Print Set Up Lists* option on the *Set Up AR/WS (Build Files)* option.

  
Example: Enter/Edit Inventory Types

Select INPATIENT PHARMACY MENU Option: <u>AUTO</u>Matic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>ENTER</u>/Edit Inventory Types

Select AOU INVENTORY TYPE NAME: <u>INJECTABLE</u>

ARE YOU ADDING 'INJECTABLE' AS A NEW AOU INVENTORY TYPE (THE 1ST)? <u>Y</u> (YES)

NAME: INJECTABLE// <u>\<RET\></u>

TYPE DESCRIPTION:

1\><u>DRUGS, EXCLUDING IV SOLUTIONS, WHICH ARE GIVEN BY INJECTION.</u>

2\> <u>\<RET\></u>

EDIT Option: <u>\<RET\></u>

Select AOU INVENTORY TYPE NAME: <u>\<RET\></u>1.2 Item Location Codes - Enter/Edit<span id="_Toc511400095" class="anchor"></span> ; \[PSGW ITEM LOC EDIT\]

This option is used to enter and edit the data in the AOU ITEM LOCATION file (#58.17). Location codes identify the specific location of an item in an Area of Use. Up to 3 levels of coding are possible; thus from the code, it could be determined, for example, that an item is located in the medicine room, cabinet A, shelf 2. On the Inventory Sheet, items will be grouped together by item location.

Data must be entered into the following fields to set up the AOU ITEM LOCATION file:

> ITEM ADDRESS CODE:

> Enter the code (1 to 3 characters) that represents a portion of an item’s location address in an Area of Use. This code is associated with an expansion for clarity.

> CODE EXPANSION:

> Enter the text that will clarify the meaning of the associated code. This field is primarily used for report information.

The following are examples of item address codes and code expansions that a site might use:

> Item Address CodeCode Expansion

> MCA MEDICINE CABINET A

> MCB MEDICINE CABINET B

> CUR CLEAN UTILITY ROOM

> D1 DRAWER 1

> D2 DRAWER 2

> B1 BIN 1

> B2 BIN 2

> MR MEDICINE ROOM

> NRC NARCOTICS CABINET

> RA RACK A

> RB RACK B

> REF REFRIGERATOR

> S1 SHELF 1

> S2 SHELF 2

At the time that the AR/WS module is implemented, consideration should be given to establish uniformity and consistency within all Areas of Use, if possible. Determine a consistent way to code the locations. Be consistent in organizing the Areas, such as, always number or letter from left to right, and top to bottom, or in some other consistent fashion. This uniformity will allow new employees to locate items easier, and will enable one technician to more easily check another’s wards during times of leave.

The diagram on the next page illustrates how the item address codes and expansions might be applied to a prototype AOU.

When item location codes have been entered, a printout of the data may be obtained by using the *List Location Codes* option located on the *Print Set Up Lists* option on the *Set Up AR/WS (Build Files)* option.

Example: Item Location Codes - Enter/Edit

Select INPATIENT PHARMACY MENU Option: <u>AUTO</u>Matic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>ITEM</u> Location Codes - Enter/Edit

Select AOU ITEM LOCATION ITEM ADDRESS CODE: <u>MR</u>

ARE YOU ADDING 'MR' AS A NEW AOU ITEM LOCATION (THE 1ST)? <u>Y</u> (YES)

AOU ITEM LOCATION CODE EXPANSION: <u>MEDICINE ROOM</u>

ITEM ADDRESS CODE: MR// <u>\<RET\></u>

CODE EXPANSION: MEDICINE ROOM// <u>\<RET\></u>

Select AOU ITEM LOCATION ITEM ADDRESS CODE: <u>CUR</u>

ARE YOU ADDING 'CUR' AS A NEW AOU ITEM LOCATION (THE 2ND)? <u>Y</u> (YES)

AOU ITEM LOCATION CODE EXPANSION: <u>CLEAN UTILITY ROOM</u>

ITEM ADDRESS CODE: CUR// <u>\<RET\></u>

CODE EXPANSION: CLEAN UTILITY ROOM// <u>\<RET\></u>

Select AOU ITEM LOCATION ITEM ADDRESS CODE: <u>\<RET\></u>Item Address Code/Expansion

This diagram illustrates possible Item Address Codes and Expansions for a prototype Area of Use called Medication Room 1:

![](automatic-replenishment-ward-stock-version-2-3-user-manual/002.png)

1.3 Create the Area of Use<span id="_Toc511400096" class="anchor"></span> ; \[PSGW AREA OF USE EDIT\]

An Area of Use is a place where commonly stocked items are stored for use by wards or treatment areas. An AOU may serve one or more wards or clinics. The purpose of this option is to create or edit the Areas of Use and their associated wards/locations/services.

> **NOTE:** Some Areas of Use are not associated with a MAS ward or clinic. For these Areas, at the “Select WARD/LOCATION (FOR PERCENTAGE):” prompt, enter “^”.

To set up PHARMACY AOU STOCK file (#58.1), data must be entered into the following fields using the *Create the Area of Use* option:

> AREA OF USE:

> Enter the name of the Area of Use. The area of use may represent a single ward, a combination of wards, or, as in the case of cardiac cath lab, no ward.

> INPATIENT SITE:

> Enter the name of the inpatient site (from the INPATIENT SITE file (#59.4)) that will receive credit for the AMIS Statistics for the AOU. It is *very important* that this field be defined if the AOU is to be counted on the AMIS Report.

> RETURNS CREDITED TO:

> For AMIS purposes, identify the usual method of drug distribution for this AOU. All returns from the AOU will be credited to this usual method on the AMIS report. Select (A) automatic replenishment, or (W) ward stock - on-demand. Leave the field blank if the AOU is used for internal Inpatient Pharmacy inventory purposes.

> COUNT ON AMIS?:

> Some AOUs are created for internal Inpatient Pharmacy inventory purposes and should not be included in the AMIS report. If you answer “YES”, then this AOU will be counted on AMIS, if you answer “NO”, then no data is collected for AMIS calculation.

> ASK EXPIRATION DATE?:

> It may be necessary to frequently change expiration date data for some AOUs such as crash carts. If you answer “YES” to this question then users will be prompted for expiration dates for items in the AOU when entering on-demands or quantities dispensed. If you answer “NO” to this question then users may edit the expiration date for items through the option *Expiration Date - Enter/Edit*.

> CRASH CART FLAG:

> This field will be set to “1” (for “YES”) if this area of use is a crash cart. This flag will be used as a screen to list only crash carts for the option *Enter/Edit Crash Cart Locations*.

> CRASH CART LOCATION:

> This field used to record the location of an area of use that is a crash cart. This field will be printed on the Expiration Date report and will be updated in the option *Enter/Edit Crash Cart Locations*.

> WARD/LOCATION (FOR PERCENTAGE):

> Enter the name of the MAS location (ex. ward or clinic) that is served partially or totally by this Area of Use. If the AOU is *not* composed of any locations, enter “^” at this prompt. This field is a pointer to the MAS HOSPITAL LOCATION file (#44).

> WARD/LOCATION % OF USE:

> What percentage of the items in the AOU will be used by this ward/location? Enter the percentage.

> SERVICE:

> Enter the name of the service served partially or totally by this ward/location. This field is a pointer to the SPECIALTY file in the MAS package. There can be multiple services per ward/location.

> SERVICE % OF USE:

> Enter the percentage which represents the use of space by this service. This is the percentage of the ward/location used by the service. For example, if 16 of the 40 beds on a ward are used by one service, then the service percentage of use is 40%.

Again, it is important to realize that there is a difference between the MAS and Pharmacy definitions for Ward and Service. There may be more than one MAS ward on one physical ward. For example, for purposes of admission, discharge, and transfer, physical ward “2B” may be broken down into “2B General Surgery” and “2B Neurosurgery”. This package uses the MAS ward definition (and clinic definition) from the HOSPITAL LOCATION file, and the MAS service definition from the SPECIALTY file. It may be useful to contact the MAS Package Coordinator or refer to the Gains and Losses Sheet for specific information.

The diagram on page 22 illustrates how an Area of Use might be defined in a prototype hospital. The worksheet found on page 23 may be useful in organizing the wards/locations and services for creating the Areas of Use. It is essential that  
the percentages for the wards/locations in an Area of Use should equal 100%, and that the percentages for the services on a ward/location equal 100%. The “Cost Report Per AOU” printout uses these percentages in calculating the breakdown cost per ward/location and cost per service.

When the Areas of Use have been created, a printout of the data may be obtained by using the *Show AOU/Ward-Location/Service* option.

Example 1: AOU with associated wards

Select INPATIENT PHARMACY MENU Option: <u>AUTO</u>Matic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>CREATE</u> the Area of Use

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

ARE YOU ADDING 'MED ROOM 1' AS A NEW PHARMACY AOU STOCK (THE 1ST)? <u>Y</u> (YES)

AREA OF USE (AOU): MED ROOM 1// <u>\<RET\></u>

INPATIENT SITE: <u>GEN</u>eral Hospital

RETURNS CREDITED TO: <u>A</u> AUTOMATIC REPLENISHMENT

COUNT ON AMIS?: <u>YES</u>

ASK EXPIRATION DATE?: <u>YES</u>

CRASH CART FLAG: <u>YES</u>

CRASH CART LOCATION: <u>1 NORTH</u>

Select WARD/LOCATION (FOR PERCENTAGE): <u>1 WEST</u>

ARE YOU ADDING '1 WEST' AS A NEW WARD (THE 1ST FOR THIS PHARMACY AOU

STOCK)? <u>Y</u> (YES)

WARD/LOCATION % OF USE: <u>50</u>

Select SERVICE: <u>GENERAL SURGERY</u>

ARE YOU ADDING 'GENERAL SURGERY' AS A NEW SERVICE (THE 1ST FOR THIS

WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>75</u>

Select SERVICE: <u>ENT</u>

ARE YOU ADDING 'ENT' AS A NEW SERVICE (THE 2ND FOR THIS WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>25</u>

Select SERVICE: <u>\<RET\></u>

Select WARD/LOCATION (FOR PERCENTAGE): <u>1 NORTH</u>

ARE YOU ADDING '1 NORTH' AS A NEW WARD (THE 2ND FOR THIS PHARMACY AOU STOCK)? <u>Y</u> (YES)

WARD/LOCATION % OF USE: <u>50</u>

Select SERVICE: <u>ALCOHOL TREATMENT</u>

ARE YOU ADDING 'ALCOHOL TREATMENT' AS A NEW SERVICE (THE 1ST FOR THIS

WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>50</u>

Select SERVICE: <u>DRUG TREATMENT</u>

ARE YOU ADDING 'DRUG TREATMENT' AS A NEW SERVICE (THE 2ND FOR THIS

WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>50</u>

Select SERVICE: <u>\<RET\></u>

Select WARD/LOCATION (FOR PERCENTAGE): <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>Example 2: AOU with associated clinics

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 3</u>

ARE YOU ADDING 'MED ROOM 3' AS A NEW PHARMACY AOU STOCK (THE 3RD)? <u>Y</u> (YES)

AREA OF USE (AOU): MED ROOM 3// <u>\<RET\></u>

INPATIENT SITE: <u>GEN</u>eral Hospital

RETURNS CREDITED TO: <u>W</u> WARD STOCK - ON DEMAND

COUNT ON AMIS?: <u>YES</u>

ASK EXPIRATION DATE?: <u>YES</u>

CRASH CART FLAG: <u>NO</u>

Select WARD/LOCATION (FOR PERCENTAGE): <u>DERMATOLOGY</u>

ARE YOU ADDING 'DERMATOLOGY' AS A NEW WARD (THE 1ST FOR THIS PHARMACY AOU STOCK)? <u>Y</u> (YES)

WARD/LOCATION % OF USE: <u>33</u>

Select SERVICE: <u>DERMATOLOGY</u>

ARE YOU ADDING 'DERMATOLOGY' AS A NEW SERVICE (THE 1ST FOR THIS

WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>100</u>

Select SERVICE: <u>\<RET\></u>

Select WARD/LOCATION (FOR PERCENTAGE): <u>ORTHO</u>

ARE YOU ADDING 'ORTHO' AS A NEW WARD (THE 2ND FOR THIS PHARMACY AOU

STOCK)? <u>Y</u> (YES)

WARD/LOCATION % OF USE: <u>33</u>

Select SERVICE: <u>ORTHOPEDIC</u>

ARE YOU ADDING 'ORTHOPEDIC' AS A NEW SERVICE (THE 1ST FOR THIS WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>60</u>

Select SERVICE: <u>PODIATRY</u>

ARE YOU ADDING 'PODIATRY' AS A NEW SERVICE (THE 2ND FOR THIS

WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>40</u>

Select SERVICE: <u>\<RET\></u>

Select WARD (FOR PERCENTAGE): <u>REHAB</u>

ARE YOU ADDING 'REHAB' AS A NEW WARD (THE 3RD FOR THIS PHARMACY AOU

STOCK)? <u>Y</u> (YES)

WARD/LOCATION % OF USE: <u>34</u>

Select SERVICE: <u>ALCOHOL TREATMENT</u>

ARE YOU ADDING 'ALCOHOL TREATMENT' AS A NEW SERVICE (THE 1ST FOR THIS

WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>10</u>

Select SERVICE: <u>DRUG TREATMENT</u>

ARE YOU ADDING 'DRUG TREATMENT' AS A NEW SERVICE (THE 2ND FOR THIS

WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>60</u>

Select SERVICE: <u>SUBSTANCE ABUSE</u>

ARE YOU ADDING 'SUBSTANCE ABUSE' AS A NEW SERVICE (THE 3RD FOR THIS

WARD)? <u>Y</u> (YES)

SERVICE % OF USE: <u>30</u>

Select SERVICE: <u>\<RET\></u>

Select WARD/LOCATION (FOR PERCENTAGE): <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>Example 3: AOU with NO associated wards

Select Set Up AR/WS (Build Files) Option: <u>CREATE</u> the Area of Use

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>DENTAL CLINIC</u>

ARE YOU ADDING 'DENTAL CLINIC' AS A NEW PHARMACY AOU STOCK (THE 4TH)? <u>Y</u> (YES)

AREA OF USE (AOU): DENTAL CLINIC// <u>\<RET\></u>

RETURNS CREDITED TO: <u>W</u> WARD STOCK - ON DEMAND

COUNT ON AMIS?: <u>YES</u>

ASK EXPIRATION DATE?: <u>YES</u>

CRASH CART FLAG: <u>NO</u>

Select WARD/LOCATION (FOR PERCENTAGE): <u>^</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>  
![](automatic-replenishment-ward-stock-version-2-3-user-manual/003.png)  
<u>Worksheet for Creating the Area of Use</u>

<u>AOU Name:</u>

<u>Inpatient Site:</u>

<u>Ward Location: % of AOU:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

100%

<u>Ward Location: % of AOU:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

100%

<u>Ward Location: % of AOU:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

100%

<u>Ward Location: % of AOU:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

100%

<u>Ward Location: % of AOU:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

100%

> <u>Ward Location: % of AOU:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

<u>Service: % of Ward/Loc:</u>

<u>100%</u>

100%

1.4 Stock Items - Enter/Edit<span id="_Toc511400097" class="anchor"></span> ; \[PSGW EDIT AOU STOCK\]

Using this option, you may enter or edit the list of items to be stocked in an Area of Use. This is the most time consuming part of setting up the package. You may wish to begin by entering all items that Nursing is accustomed to stocking for the AOU. However, the AR/WS package can be used to trim this stock list to only those items and stock levels that are actually used. The Usage Report for an Item, Zero Usage Report, and Returns Analysis Report will supply information for this purpose.

To set up PHARMACY AOU STOCK file (#58.1), data must be entered into the following fields using the *Stock Items - Enter/Edit* option:

> AREA OF USE:

> Enter the name of the Area of Use.

> Note: When an item has been entered for the AOU, the AOU *maynotbe deleted*! Because of the extensive pointers involved, deletion is not allowed.

> ITEM:

> Enter the generic name (from the DRUG file) of the item being stocked in the Area of Use. Items *maynot be deleted* from an Area of Use. Because of the extensive pointers involved, if an item is no longer used in an AOU, it should be *inactivated* using the *Inactivate AOU Stock Item* option.

> STOCK LEVEL:

> Enter the quantity that is the determined stock level for this item in the AOU.

> REORDER LEVEL:

> Enter the level of the on-hand amount that should be reached before this item is dispensed. This is an optional field and may be left blank if so desired.

> MINIMUM QUANTITY TO DISPENSE:

> Enter the quantity that is the least amount of the item that can be dispensed. For example, if an item is to be dispensed only in packages of 6 units, then the minimum quantity to dispense for the item would be 6. This field is optional and may be left blank if so desired.

> TYPE:

> Inventory types are used to select groups of items for inventory. Enter the name of the type of inventory which will include this item. You may enter more than one type. This will allow the item to be selected for inventory by either type. The inventory type must be defined in AOU INVENTORY TYPE file (# 58.16).

> LOCATION:

> Location should be composed of ITEM ADDRESS CODES from AOU ITEM LOCATION file (#58.17). Enter an address describing the location of this item in the AOU. It should consist of up to 3 levels separated by commas. For example, “MR,CA,S3” could equal “medicine room, cabinet A, shelf 3”. Each of the 3 levels should further define the exact location. Only up to 3 levels will be utilized to sort AOU items on inventory sheets and other reports. The reports will be sorted primarily by the first level defined, and then by subsequent levels.

> WARD (FOR ITEM):

> Enter the name of the ward or wards (from the WARD LOCATION file in the MAS program) that will use this particular item. It is important to accurately answer this prompt because this is the link between the AR/WS package and the Unit Dose package. The Unit Dose package looks at this field to know if the drug is a Ward Stock item. Enter only those wards associated with this Area of Use.

The sample and worksheet found on pages 27 - 28 may be used to help determine inventory to be stocked in each AOU.

After all items are entered for an AOU, a printout of the data may be obtained by using the *List Stock Items* option.

Example 1: Stock Items - Enter/Edit

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>STOCK</u> Items - Enter/Edit

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select ITEM: <u>BACITRACIN OINTMENT (1OZ)</u>

ARE YOU ADDING 'BACITRACIN OINTMENT (1OZ)' AS A NEW ITEM (THE 1ST FOR THIS

PHARMACY AOU STOCK)? <u>Y</u> (YES)

ITEM STOCK LEVEL: <u>3</u>

ITEM LOCATION: <u>MR,CA,S1</u>

STOCK LEVEL: 3// <u>\<RET\></u>

REORDER LEVEL: <u>1</u>

MINIMUM QUANTITY TO DISPENSE: <u>2</u>

Select TYPE: <u>EXTERNAL (TOPICAL)</u>

Select TYPE: <u>\<RET\></u>

LOCATION: MR,CA,S1// <u>\<RET\></u>

Select WARD (FOR ITEM): 1 NORTH// <u>1 WEST</u>

Select WARD (FOR ITEM): <u>\<RET\></u>

Select ITEM: <u>PHENYTOIN 250MG SYRINGE</u>

ARE YOU ADDING 'PHENYTOIN 250MG SYRINGE' AS A NEW ITEM (THE 2ND FOR THIS

PHARMACY AOU STOCK)? <u>Y</u> (YES)

ITEM STOCK LEVEL: <u>2</u>

ITEM LOCATION: <u>MR,CC,S1</u>

STOCK LEVEL: 2// <u>\<RET\></u>

REORDER LEVEL: <u>1</u>

MINIMUM QUANTITY TO DISPENSE: <u>1</u>

Select TYPE: <u>INJECTABLE</u>

Select TYPE: <u>\<RET\></u>

LOCATION: MR,CC,S1// <u>\<RET\></u>

Select WARD (FOR ITEM): 1 NORTH// <u>1 WEST</u>

Select WARD (FOR ITEM): <u>\<RET\></u>

Select ITEM: <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>Example 2: Non-Pharmacy Items in AR/WS

Non-Pharmacy packages, such as Surgery, have the ability to flag certain drugs in the DRUG file (#50) for their exclusive use. This is accomplished by putting a package specific code in the DRUG file field called APPLICATION PACKAGES’ USE. Drugs that are flagged for non-pharmacy packages are *not* selectable by AR/WS for on-demands or to be used as stock items in AOUs. It is possible, however, for non-pharmacy packages to flag drugs *after* they have been defined in an AOU. This can cause a very confusing situation for AR/WS users when they are unable to do an on-demand request on the drug in question. The following is an example of what they would see if they try to look at the drug through the option *Stock Items - Enter/Edit*:

Select Set Up AR/WS (Build Files) Option: <u>STOCK</u> Items - Enter/Edit

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>DRUG CLOSET</u>

Select ITEM: <u>DIAZEPAM</u>

...OK? YES// <u>Y</u> (YES)

MR,C1,S1

This item is currently defined for this AOU but appears to be a

non-pharmacy drug. It has been inactivated as of Nov 1,1993.

Select ITEM: <u>\<RET\></u>

At this point it would be necessary for pharmacy to determine if the drug is truly a non-pharmacy item, in which case it should remain inactivated in the AOU. It will eventually be purged from the AOU by the option *Purge Dispensing Data.* If, however, pharmacy determines that the drug has been incorrectly flagged by the non-pharmacy package it will be necessary to have that package remove the non-pharmacy code from the field APPLICATION PACKAGES’ USE in the DRUG file.

Sample Worksheet:<u>PHARMACY AOU STOCK File Worksheet</u>

Make copies of this worksheet to help determine inventory to be stocked in each AOU. For each AOU, list all drugs to be stocked.

<u>AOU: Med Room 1</u>

> <u>Select Item: Bacitracin Ointment (1oz)</u>

> <u>Stock Level: 3</u>

> <u>Reorder Level: 1</u>

> <u>Min. Qty. To Dispense: 2</u>

> <u>Select Type: External (Topical)</u>

> <u>Location: MR, CA, S1</u>

> <u>Ward(For Item): 1 West, 1 North</u>

> <u>Select Item: Phenytoin 250mg Syringe</u>

> <u>Stock Level: 2</u>

> <u>Reorder Level: 1</u>

> <u>Min. Qty. To Dispense: 6</u>

> <u>Select Type: Injectable</u>

> <u>Location: MR, CC, S1</u>

> <u>Ward(For Item): 1 West, 1 North</u>

> <u>Select Item: Keto-Diastix Strips (100’s)</u>

> <u>Stock Level: 2</u>

> <u>Reorder Level: 1</u>

> <u>Min. Qty. To Dispense: 3</u>

> <u>Select Type: Reagent/Test Item</u>

> <u>Location:MR, CB, S1</u>

> <u>Ward(For Item): 1 West, 1 North</u>

> <u>Select Item: Kaolin and Pectin Suspension (16 oz BT)</u>

> <u>Stock Level: 3</u>

> <u>Reorder Level: 1</u>

> <u>Min. Qty. To Dispense: 1</u>

> <u>Select Type: Internal (Oral Liquid)</u>

> <u>Location: MR, CC, S1</u>

> <u>Ward(For Item): 1 West, 1 North</u>

> <u>Select Item: Milk of Magnesia 480ml</u>

> <u>Stock Level: 3</u>

> <u>Reorder Level: 1</u>

> <u>Min. Qty. To Dispense: 3</u>

> <u>Select Type: Oral Liquid</u>

> <u>Location: MR, CC, S4</u>

> <u>Ward(For Item): 1 West, 1 North</u>

<u>PHARMACY AOU STOCK File Worksheet</u>

Make copies of this worksheet to help determine inventory to be stocked in each AOU. For each AOU, list all drugs to be stocked.

<u>AOU:</u>

> <u>Select Item:</u>

> <u>Stock Level:</u>

> <u>Reorder Level:</u>

> <u>Min. Qty. To Dispense:</u>

> <u>Select Type:</u>

> <u>Location:</u>

> <u>Ward(For Item):</u>

> <u>Select Item:</u>

> <u>Stock Level:</u>

> <u>Reorder Level:</u>

> <u>Min. Qty. To Dispense:</u>

> <u>Select Type:</u>

> <u>Location:</u>

> <u>Ward(For Item):</u>

> <u>Select Item:</u>

> <u>Stock Level:</u>

> <u>Reorder Level:</u>

> <u>Min. Qty. To Dispense:</u>

> <u>Select Type:</u>

> <u>Location:</u>

> <u>Ward(For Item):</u>

> <u>Select Item:</u>

> <u>Stock Level:</u>

> <u>Reorder Level:</u>

> <u>Min. Qty. To Dispense:</u>

> <u>Select Type:</u>

> <u>Location:</u>

> <u>Ward(For Item):</u>

> <u>Select Item:</u>

> <u>Stock Level:</u>

> <u>Reorder Level:</u>

> <u>Min. Qty. To Dispense:</u>

> <u>Select Type:</u>

> <u>Location:</u>

> <u>Ward(For Item):</u>

1.5 Expiration Date - Enter/Edit<span id="_Toc511400098" class="anchor"></span> ; \[PSGW EXPIRATION ENTER/EDIT\]

This option is used to enter expiration dates for stock items in the PHARMACY AOU STOCK file (#58.1). This field, when defined, will be displayed on Inventory Sheets and printouts of On-Demand Requests.

Example: Expiration Date - Enter/Edit

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>EXPIR</u>ation Date - Enter/Edit

Enter Expiration Dates for Stock Items

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select ITEM: <u>ACETAMINOPHEN TAB 325 MG</u>

EXPIRATION DATE: <u>2/1/91</u> (FEB 01, 1991)

Select ITEM: <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>  
1.6 Ward (For Item) Conversion<span id="_Toc511400099" class="anchor"></span> ; \[PSGW WARD CONVERSION\]

This option will allow the mass conversion of the WARD (FOR ITEM) field for all items in a single AOU, several AOUs, or ALL AOUs from a selected *old* ward designation to a *new* ward designation. This capability was designed especially for situations like the closing of a ward for construction. It would be too time consuming to edit the WARD (FOR ITEM) field for each item in an AOU individually, especially when the Ward closing will only be temporary.

This option may be queued to run as a background job at a later time. When the job is complete, a MailMan message will be sent to the user who queued the job, listing the number of AOU(s) and stock items that were converted. In the following example, a ward (2 WEST) that has been inactivated by MAS will be replaced by a new ward (2 EAST) for MED ROOM 3.

> **NOTE:** Selection of the *new* ward will be limited to active Wards only.

Example: Ward (For Item) Conversion

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>WARD</u> (For Item) Conversion

This routine will allow you to do a mass conversion of all items in an

active AOU from an old Ward designation to a new Ward designation.

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 3</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

Select OLD WARD: <u>2 WEST</u>

Select NEW WARD: <u>2 EAST</u>

Do you want to queue this job? YES// <u>\<RET\></u>

You will notified by MailMan when the job is completed.

Requested Start Time: NOW// *\[Enter the date/time you want to queue the job to run\]*

Select Set Up AR/WS (Build Files) Option: <u>\<RET\></u>  
Example: MailMan message for Ward (For Item) Conversion

Subj: AR/WS MASS WARD CONVERSION SUMMARY \[#21111\] 10 Jun 93 10:23 6 lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

AR/WS Ward Conversion Background job has run to completion.

Run Date: JUN 10,1993

Old Ward: 2 WEST converted to New Ward: 2 EAST

Total number of AOUs converted: 1

Total number of Stock Items converted: 15

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>  
1.7 Add/Delete Ward (for Item) <span id="_Toc511400100" class="anchor"></span>; \[PSGW ADD/DEL WARD\]

This option is similar to the option to do mass Ward (for Item) conversions except that in this case the user can ADD or DELETE a Ward (for Item) assignment for all stock items in one, several, or all active AOUs.

If the user chooses to queue this as a background job, a MailMan message is sent to the user when the job is complete.

Example 1: Addition of a Ward (for Item) assignment

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>ADD</u>/Delete Ward (for Item)

This option will allow you to add or delete a WARD (for Item) assignment for

all stock items in one or more ACTIVE AOUs.

Do you wish to (A)dd or (D)elete? (Enter 'A', 'D', or '^' to Exit)=\> <u>A</u>DD

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 2</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

Select Ward (for Item) to ADD: <u>1 EAST</u>

Do you want to queue this job? YES// <u>Y</u> (YES)

You will be notified by MailMan when the job is completed.

Requested Start Time: NOW// *\[Enter the date/time you want to queue the job to run\]*

Select Set Up AR/WS (Build Files) Option: <u>\<RET\></u>

*\[An example of the MailMan message follows on the next page.\]*Example: MailMan message for Addition of a Ward (For Item) assignment

Subj: AR/WS WARD (FOR ITEM) ADDITION SUMMARY \[12222\] 10 Jun 93 10:26 5 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

AR/WS WARD (For Item) ADDITION Background job has run to completion.

Run Date: JUN 10,1993

WARD (For Item) assignment of 1 EAST has been Added to:

Total AOU(s): 1 Total Stock Items: 26

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>Example 2: Deletion of a Ward (for Item) assignment

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>ADD</u>/Delete Ward (for Item)

This option will allow you to add or delete a WARD (for Item) assignment for

all stock items in one or more ACTIVE AOUs.

Do you wish to (A)dd or (D)elete? (Enter 'A', 'D', or '^' to Exit)=\> <u>D</u>ELETE

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>I</u>

Select AOU INVENTORY GROUP NAME: <u>SECOND FLOOR</u>

This Inventory Group contains the following AOU(s):

MED ROOM 1

MED ROOM 2

DRUG CLOSET

Select Ward (for Item) to DELETE: <u>1 EAST</u>

Do you want to queue this job? YES// <u>Y</u> (YES)

You will be notified by MailMan when the job is completed.

Requested Start Time: NOW// *\[Enter the date/time you want to queue the job to run.\]*

Select Set Up AR/WS (Build Files) Option: <u>\<RET\></u>

*\[An example of the MailMan message follows.\]*Example: MailMan message for Deletion of a Ward (For Item) assignment

Subj: AR/WS WARD (FOR ITEM) DELETION SUMMARY 10 Jun 93 13:18 5 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

AR/WS WARD (For Item) DELETION Background job has run to completion.

Run Date: JUN 10,1993

WARD (For Item) assignment of 1 EAST has been Deleted from:

Total AOU(s): 1 Total Stock Items: 26

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>  
1.8 Transfer AOU Stock Entries <span id="_Toc511400101" class="anchor"></span>; \[PSGW TRANSFER ENTRIES\]

This option is locked with the PSGW TRAN key, and *only* the Inpatient Pharmacy Package Coordinator or a designee should be assigned the key.

This option will copy the active stock entries from a selected Area of Use into one or more selected Areas. The ability to copy stock entries could be useful in at least three cases. First of all, for stations setting up AR/WS initially, you could establish a “Master” AOU with standard items which will be stocked by ALL AOUs. Using the transfer option, these items could then be copied into all Areas. You would then have to edit each item in each AOU to enter the stock level, type, ward (for item), and location. A second application might be for the creation of crash carts or after-hours dispensing machines, i.e., DOCUMED. These are likely to have identical stock items, stock levels, and location codes. Therefore, after one has been created, the transfer option could be used to clone all others. A final use for the option would be for adding new items to a number of Areas of Use. For example, the option would be useful if an item has been recently approved by the FDA, and has been added to your formulary. Using the transfer option, you could add this item (or group of items) to a selected group of Areas of Use.

As many as ten Areas may be chosen to be transferred into at one time. Also, there is a choice as to exactly what is copied. You may choose (1) to transfer only the item name, (2) to transfer the item name, stock level and location code, or (3) to transfer item name, stock level, location code, and ALL types. The copy process will not copy inactive drugs or duplicate entries. Thus, if an Area of Use already contains Bacitracin Ointment 1OZ, and that item is in the “Master” AOU, the item will not be duplicated.

After you have selected the AOU to be transferred from, and the Area or Areas to be transferred into, the actual transfer takes place in a background job which is automatically queued. The amount of time needed to complete the transfer depends upon the number of items to be copied and the number of Areas to be “copied into”. When the transfer is complete, you will be notified by a MailMan message. You may then go into the AOU and edit, as mentioned above, if necessary.

Example: Transfer AOU Stock Entries

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>TRANS</u>fer AOU Stock Entries

This option will copy the stock entries from one AOU into AOUs

you select. Inactive or duplicate items will not be transferred.

Choosing to copy stock items into multiple AOUs will allow you

to choose up to 10 AOUs at one time.

Do you wish to copy stock items INTO:

\(1\) ONE Area of Use, or

\(2\) multiple Areas of Use

Select "1" or "2": <u>2</u>

Do you wish to transfer:

\(1\) Drug (item) name only, or

\(2\) Drug name, stock level, and location, or

\(3\) Drug name, stock level, location, and type.

Select "1", "2", or "3": <u>2</u>

Select AOU to transfer stock list FROM: <u>MASTER</u> CRASH CART

Select AOU to transfer stock list INTO: <u>FIRST</u> FLOOR CRASH CART

Select AOU to transfer stock list INTO: <u>SECOND</u> FLOOR CRASH CART

Select AOU to transfer stock list INTO: <u>\<RET\></u>

I will now COPY the ENTIRE stock list from

MASTER CRASH CART into

FIRST FLOOR CRASH CART

SECOND FLOOR CRASH CART

I will transfer drug name, stock level, and location.

Are you SURE that is what you want to do? NO// <u>YES</u>

This job will automatically be queued to run in the background.

You will be notified by MailMan when the transfer is completed.

TRANSFER FILE ENTRIES queued!

*\[An example of the MailMan message follows.\]*Example: MailMan Message for Transfer AOU Stock Entries

Subj: AR/WS AOU ENTRY TRANSFER COMPLETED \[#12495\] 10 Jun 93 10:32 3 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

Stock items from MASTER CRASH CART have been transferred into:

FIRST FLOOR CRASH CART

SECOND FLOOR CRASH CART

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>1.9 Inactivate AOU<span id="_Toc511400102" class="anchor"></span> ; \[PSGW AOU INACTIVATION\]

Use this option to inactivate AOUs in the PHARMACY AOU STOCK file (#58.1). This function will enable the user to be informed of an AOU’s inactivation when they attempt to choose the AOU or do a look-up listing of AOUs. Inactive AOUs will be excluded from Stock Item Listings and Zero Usage reports that are done on ALL AOUs. Please note that an *inactive* AOU will be included on reports covering a period of time when the AOU was *active* and had activity. On-Demand Requests will not be permitted for inactive AOUs, however, activity that is tied to an Inventory Date/Time such as inputting quantity dispensed and returns will be allowed since an inventory sheet may have been created before the AOU was inactivated. Under these circumstances, though, the AOU name will be displayed with an “\*\*\* INACTIVE \*\*\*” flag.

AOUs are inactivated by entering a date that can be past, present, or future.

Example: Inactivate AOU

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>INACTIVATE AOU</u>

Enter AOU Inactivation Dates

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 3</u>

INACTIVE DATE: <u>12/2/93</u> (DEC 02, 1993)

...One moment, please...

There are items in this AOU that are currently active.

You may, at this time, inactivate all of them as of DEC 2,1993.

Do you want to do this? YES// <u>\<RET\></u> (YES)

Now inactivating all currently active items as of DEC 2,1993..

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>  
1.10 Inactivate AOU Stock Item<span id="_Toc511400103" class="anchor"></span>; \[PSGW INACTIVATE AOU STOCK ITEM\]

Use this option to inactivate an item that is currently stocked in an Area of Use. Items should *not be deleted*, but simply made inactive. Inactivated items will not be included on the inventory sheet or on the AOU stock list. However, after an item has been inactivated, it will print one final time on the inventory sheet. At that time, a message will indicate that the item has been inactivated and should be pulled from stock.

After selecting the Area of Use and the item, this option asks you to enter the inactivation date. Enter the date, e.g., “T”. Finally, you are asked for an inactivation reason. The reason may be item not used, item deleted from formulary, or other, a free text reason you enter.

To reactivate the item use this option and delete the inactive date.

Example: Inactivate AOU Stock Item

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>INACTIVATE AOU STOCK ITEM</u>

You may inactivate a Stock Item for a single AOU,

or enter "^ALL" to inactivate the Item in ALL AOUs.

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select ITEM: <u>PHEN</u>YTOIN 250MG SYRINGE

...OK? YES// <u>Y</u> (YES)

MR,CC,S1

INACTIVATION DATE: <u>T</u> (JAN 26, 1993)

INACTIVATION REASON: <u>??</u>

This contains the reason that the item has been inactivated from the list

of items normally stocked in this Area of Use.

CHOOSE FROM:

N NOT USED

O OTHER

DF DELETED FROM FORMULARY

INACTIVATION REASON: <u>N</u> NOT USED

Select ITEM: <u>BACIT</u>RACIN OINTMENT (1OZ)

...OK? YES// <u>Y</u> (YES)

MR,CA,S1

INACTIVATION DATE: <u>T</u> (JAN 26, 1993)

INACTIVATION REASON: <u>O</u> OTHER

INACTIVATION REASON (OTHER): *\[Enter your free text reason here.\]*

Select ITEM: <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>1.11 AOU Inventory Group-Enter/Edit<span id="_Toc511400104" class="anchor"></span> ; \[PSGW AOU INV GROUP EDIT\]

An AOU Inventory Group is defined by pharmacy to represent the Areas which are inventoried together as a “batch” or “cluster”. By grouping the commonly inventoried AOUs under an easy to remember group name, the elements of the inventory are established, and do not have to be redefined every time the inventory is scheduled.

AOU Inventory Groups may be established to reflect variations at the VAMC. Inventories may be grouped by: 1) location - for example, Emergency Room, clinic or ward. 2) time - when the inventory takes place, e.g., “Monday Day Shift”, “M-W-F/Evenings”. 3) category or “type” of item to be inventoried, e.g., IV solutions & sets, narcotics, or bulk externals. Also, a Group could include any combination of the following categories.

Data must be entered into the following fields to set up AOU INVENTORY GROUP file (#File 58.2):

> NAME:

> Enter the name of the inventory group. The name cannot be more than 30 characters, and cannot begin with punctuation. A name may typically include the name of the Tech who performs inventory, day of week of inventory, ward or AOU involved, and/or types.

> AREA OF USE: (Required Field)

> Enter the name of the AOU that is to be inventoried when selecting this inventory group. The AOU must have been defined in PHARMACY AOU STOCK file (#58.1) via the *Create the Area of Use* option.

> INVENTORY TYPE: (Required Field)

> Enter the inventory type that is to be inventoried within the AOU. More than one inventory type can be entered. The inventory types must have been previously defined in AOU INVENTORY TYPE file (#58.16) by using the *Enter/Edit InventoryTypes* option. If all items within an AOU are to be inventoried, you may specify “ALL” as an inventory type or if you prefer, you may enter each type individually. If you enter “ALL”, when the inventory sheet prints, the type names are suppressed and do not show. If you want the type names to show on the inventory sheet, then you should list all of the inventory types to be inventoried within the AOU.

> GROUP DESCRIPTION:

> Enter text that describes this inventory group, its use, and perhaps the times when normally processed. This field is purely informational.

The diagram on page 42 shows a prototype AOU Inventory Group and how it relates to the Areas of Use, wards, and services.

You may get a printout of the data entered for your AOU Inventory Groups by using the *Inventory Group List* option.

Example: AOU Inventory Group-Enter/Edit

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>AOU</u> Inventory Group-Enter/Edit

Select AOU INVENTORY GROUP NAME: <u>FIRST FLOOR (M-W-F)</u>

ARE YOU ADDING 'FIRST FLOOR (M-W-F)' AS A NEW AOU INVENTORY GROUP (THE 1ST)? <u>Y</u> (YES)

NAME: FIRST FLOOR (M-W-F)// <u>\<RET\></u>

GROUP DESCRIPTION:

1\><u>INVENTORY IS FOR ALL TYPES FOR MED ROOM 1 AND 2, CONDUCTED M,W,&F.</u>

2\> <u>\<RET\></u>

EDIT Option: <u>\<RET\></u>.

Select AREA OF USE (AOU): <u>MED ROOM 1</u>

ARE YOU ADDING 'MED ROOM 1' AS A NEW AREA OF USE (AOU) (THE 1ST FOR THIS AOU INVENTORY GROUP)? <u>Y</u> (YES)

Select INVENTORY TYPE: <u>INJ</u>ECTABLE

Select INVENTORY TYPE: <u>EXT</u>ERNAL (TOPICAL)

Select INVENTORY TYPE: <u>INTERNAL (ORAL LIQ</u>UID)

Select INVENTORY TYPE: <u>INTERNAL (ORAL SOL</u>ID)

Select INVENTORY TYPE: <u>SOLUTION,IRR</u>IGATION

Select INVENTORY TYPE: <u>SOLUTION,IV</u>

Select INVENTORY TYPE: <u>REA</u>GENT/TEST ITEM

Select INVENTORY TYPE: <u>SUPPOS</u>ITORY

Select INVENTORY TYPE: <u>INH</u>ALER (ORAL, NASAL)

Select INVENTORY TYPE: <u>OP</u>HTHALMIC,OTIC

Select INVENTORY TYPE: <u>\<RET\></u>

Select AREA OF USE (AOU): <u>MED ROOM 2</u>

ARE YOU ADDING 'MED ROOM 2' AS A NEW AREA OF USE (AOU) (THE 2ND FOR THIS AOU INVENTORY GROUP)? <u>Y</u> (YES)

Select INVENTORY TYPE: <u>INJ</u>ECTABLE

Select INVENTORY TYPE: <u>EXT</u>ERNAL (TOPICAL)

Select INVENTORY TYPE: <u>INTERNAL (ORAL LIQ</u>UID)

Select INVENTORY TYPE: <u>INTERNAL (ORAL SOL</u>ID)

Select INVENTORY TYPE: <u>SOLUTION,IRR</u>IGATION

Select INVENTORY TYPE: <u>SOLUTION,IV</u>

Select INVENTORY TYPE: <u>REA</u>GENT/TEST ITEM

Select INVENTORY TYPE: <u>SUPPOS</u>ITORY

Select INVENTORY TYPE: <u>INH</u>ALER (ORAL, NASAL)

Select INVENTORY TYPE: <u>OP</u>HTHALMIC,OTIC

Select INVENTORY TYPE: <u>\<RET\></u>

Select AREA OF USE (AOU): <u>\<RET\></u>

Select AOU INVENTORY GROUP NAME: <u>SECOND FLOOR (TU-F)</u>

ARE YOU ADDING 'SECOND FLOOR (TU-F)' AS A NEW AOU INVENTORY GROUP (THE 2ND)? <u>Y</u> (YES)

NAME: SECOND FLOOR (TU-F)// <u>\<RET\></u>

GROUP DESCRIPTION:

1\><u>INVENTORY COVERS ALL TYPES FOR MED ROOM 3; CONDUCTED ON TU-&F.</u>

2\> <u>\<RET\></u>

EDIT Option: <u>\<RET\></u>

Select AREA OF USE (AOU): <u>MED ROOM 3</u>

ARE YOU ADDING 'MED ROOM 3' AS A NEW AREA OF USE (AOU) (THE 1ST FOR THIS AOU INVENTORY GROUP)? <u>Y</u> (YES)

Select INVENTORY TYPE: <u>ALL</u>

Select INVENTORY TYPE: <u>\<RET\></u>

Select AREA OF USE (AOU) <u>\<RET\></u>

Select AOU INVENTORY GROUP NAME: CRASH CARTS

ARE YOU ADDING 'CRASH CARTS' AS A NEW AOU INVENTORY GROUP (THE 3RD)? <u>Y</u> (YES)

NAME: CRASH CARTS// <u>\<RET\></u>

GROUP DESCRIPTION:

1\><u>INVENTORY OF ALL ITEMS FOR ALL CRASH CARTS.</u>

2\> <u>\<RET\></u>

EDIT Option: <u>\<RET\></u>

Select AREA OF USE (AOU): <u>FIRST FLOOR CRASH CART</u>

ARE YOU ADDING 'FIRST FLOOR CRASH CART' AS A NEW AREA OF USE (AOU) (THE 1ST FOR THIS AOU INVENTORY GROUP)? <u>Y</u> (YES)

Select INVENTORY TYPE: <u>ALL</u>

Select INVENTORY TYPE: <u>\<RET\></u>

Select AREA OF USE (AOU): <u>SECOND FLOOR CRASH CART</u>

ARE YOU ADDING 'SECOND FLOOR CRASH CART' AS A NEW AREA OF USE (AOU) (THE 2ND FOR THIS AOU INVENTORY GROUP)? <u>Y</u> (YES)

Select INVENTORY TYPE: <u>ALL</u>

Select INVENTORY TYPE: <u>\<RET\></u>

Select AREA OF USE (AOU): <u>\<RET\></u>

Select AOU INVENTORY GROUP NAME: <u>CLINICS</u>

ARE YOU ADDING 'CLINICS' AS A NEW AOU INVENTORY GROUP (THE 4TH)? <u>Y</u> (YES)

NAME: CLINICS// <u>\<RET\></u>

GROUP DESCRIPTION:

1\><u>INVENTORY OF ALL TYPES FOR ALL CLINICS.</u>

2\> <u>\<RET\></u>

EDIT Option: <u>\<RET\></u>

Select AREA OF USE (AOU): <u>DENTAL CLINIC</u>

ARE YOU ADDING 'DENTAL CLINIC' AS A NEW AREA OF USE (AOU) (THE 1ST FOR THIS AOU INVENTORY GROUP)? <u>Y</u> (YES)

Select INVENTORY TYPE: <u>ALL</u>

Select INVENTORY TYPE: <u>\<RET\></u>

Select AREA OF USE (AOU): <u>\<RET\></u>

Select AOU INVENTORY GROUP NAME: <u>\<RET\></u>Prototype AOU Inventory Group

Refer back to the diagram on page 22 of the prototype hospital to illustrate the creation of the AOUs. In this hospital, automatic replenishment of ward stock is done by two technicians. One technician services 1 North, 1 West, and 1 South on Mondays, Wednesdays, and Fridays. A second technician services Ortho, Dermatology, and Rehab on Tuesdays and Fridays. During these times, all drugs are inventoried.

![](automatic-replenishment-ward-stock-version-2-3-user-manual/004.png)P1.12 Print Set Up Lists<span id="_Toc511400105" class="anchor"></span> ; \[PSGW PRINT SETUP LISTS\]

This menu contains all reports or lists associated with setting up the files for AR/WS. There are currently six options on this menu.

> *Print Inventory Types (80 column)*

> *List Location Codes (80 column)*

> *Show AOU/Ward/Service (132 column)*

> *Print AR/WS Stock Item Data (132 column)*

> *List Stock Items (132 column)*

> *Inventory Group List (80 column)*1.12.1 Print Inventory Types<span id="_Toc511400106" class="anchor"></span> (80 column) ; \[PSGW INV TYPE\]

This option allows you to print the list of inventory types defined in AOU INVENTORY TYPE file (#58.16). These types are used to classify the items in an Area of Use for inventory purposes.

Example: Print Inventory Types (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>PRINT</u> Set Up Lists

Select Print Set Up Lists Option: <u>PRINT INV</u>entory Types (80 column)

DEVICE: *\[Queue report here or send to designated device\]*

report follows

AREA OF USE INVENTORY TYPES MAY 26,1993 09:34 PAGE 1

NAME TYPE DESCRIPTION

------------------------------------------------------------------------------

> ALL ALL ITEMS IN AN AOU

> CONTROLLED DRUG (II) ANY DRUG IN SCHEDULE II

> CONTROLLED DRUG (III, IV, V) ANY DRUG IN SCHEDULE III,IV, OR V

> EXTERNALS ALL ITEMS THAT USED EXTERNALLY

> INHALER ANY ITEM USED FOR INHALATION

> INJECTION ANY INJECTABLE DRUG

> OINTMENTS SALVES, CREAMS, ETC.

> OPHTHALMIC, OTIC ANY PREPARATION FOR EYE OR EAR

> (SOLN. OINT.)

> ORAL LIQUID ALL ITEMS THAT ARE INTERNAL ORAL

> LIQUIDS

> ORAL SOLID ALL ITEMS THAT ARE INTERNAL ORAL

> SOLIDS

> REAGENT/TEST ITEM USED IN DIAGNOSTIC OR MEASUREMENT

> TESTS

> REFRIGERATED ITEMS ITEMS WHICH REQUIRE REFRIGERATION

> •

> •

> • *\[This report has been abbreviated to save space.\]*1.12.2 List Location Codes<span id="_Toc511400107" class="anchor"></span> (80 column); \[PSGW ITEM LOC PRINT\]

This option allows you to print the list of location codes entered into AOU ITEM LOCATION file (#58.17). These codes are used to define the location of items in an Area of Use.

Example: List Location Codes (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>PRINT</u> Set Up Lists

Select Print Set Up Lists Option: <u>LIST LOC</u>ation Codes (80 column)

DEVICE: *\[Queue report here or send to designated device\]*

report follows

AREA OF USE ITEM LOCATION EXPANSIONS MAY 26,1993 09:34 PAGE 1

ITEM

ADDR

CODE CODE EXPANSION

------------------------------------------------------------------------------

B BIN

B1 BIN 1

B2 BIN 2

D DRAWER

DR1 DRAWER 1

ER EMERGENCY ROOM

IVR IV ROOM

MC MEDICINE CABINET

MC4 MEDICINE CABINET 4

MR MEDICINE ROOM

NAR NARCOTICS STORAGE CABINET

REF REFRIGERATOR

AREA OF USE ITEM LOCATION EXPANSIONS MAY 26,1993 09:34 PAGE 2

ITEM

ADDR

CODE CODE EXPANSION

------------------------------------------------------------------------------

S SHELF

S3 SHELF 3

S5 SHELF 5

S8 SHELF 8

SC1 SECTION 1

SC2 SECTION 2

s2 SHELF 2

1.12.3 Show AOU/Ward/Service<span id="_Toc511400108" class="anchor"></span> (132 column) ; \[PSGW SHOW AREA OF USE\]

This option allows you to print the AOUs/Wards (or Locations)/Services defined in PHARMACY AOU STOCK file (#58.1). This information was entered via the *Create the Area of Use* option. If you have more than one Inpatient Site defined for your AOUs, this report will sort the data by Inpatient Site and print a separate report for each site.

Example: Show AOU/Ward/Service (132 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>PRINT</u> Set Up Lists

Select Print Set Up Lists Option: <u>SHOW</u> AOU/Ward/Service (132 column)

DEVICE: *\[Queue report here or send to designated device\]*

report follows

AREA OF USE / WARDS AND SERVICES MAY 26,1993 09:30 PAGE 1

SERVICE

WARD/LOCATION % OF

AREA OF USE (AOU) WARD/LOCATION (FOR PERCENTAGE) % OF USE SERVICE USE

---------------------------------------------------------------------------------------------

INPATIENT SITE: DAN'S HOSPITAL

\#1 MEDICATION ROOM 1 WEST 50 GENERAL SURGERY 75

ENDOCRINOLOGY 25

1 NORTH 50 ALCOHOL TREATMENT 50

\#2 MEDICATION ROOM 1 SOUTH 100 CARDIOLOGY 40

PULMONARY, TUBERCULOSIS 30

GASTROENTEROLOGY 30

\#3 MEDICATION ROOM 33 33 NHCU 60

GERONTOLOGY 40

2 EAST 33 NEUROLOGY 100

2 NH 33 PODIATRY 10

UROLOGY 60

GYNECOLOGY 30

AREA OF USE / WARDS AND SERVICES MAY 26,1993 09:30 PAGE 2

SERVICE

WARD/LOCATION % OF

AREA OF USE (AOU) WARD/LOCATION (FOR PERCENTAGE) % OF USE SERVICE USE

---------------------------------------------------------------------------------------------

INPATIENT SITE: HOOVER

DRUG CLOSET 1 WEST 50 SURGICAL ICU 75

1 NORTH 50 ORTHOPEDIC 50

1.12.4 Print AR/WS Stock Item Data<span id="_Toc511400109" class="anchor"></span> (132 column); \[PSGW STOCK ITEM DATA\]

This option will print an alphabetical listing of “ALL” active items you have defined in the PHARMACY AOU STOCK file (#58.1). The following information will be displayed for each item:

> 1\. All AOUs that stock the item and the LOCATION in the AOUs.

> 2\. Stock levels for item in each AOU

> 3\. All WARD (FOR ITEM) assignments

> 4\. All TYPE definitions

This report would be especially helpful for sites that are trying to update their AOU stock items.

Example: Print AR/WS Stock Item Data (132 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>PRINT</u> Set Up Lists

Select Print Set Up Lists Option: <u>PRINT AR/</u>WS Stock Item Data (132 column)

This report shows data stored for AR/WS Stock Items.

Right Margin for this report is 132 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

JUN 10,1993 PAGE: 1

DATA FOR AR/WS STOCK ITEMS

=\> ITEM

STOCK

AOU LOCATION LEVEL WARD (FOR ITEM) TYPE

---------------------------------------------------------------------------------------------

=\> BACLOFEN 10MG TAB

DRUG CLOSET MR,CA,S1 2 1 SOUTH EXTERNAL

=\> DEXTROTHYROXINE SODIUM 2MG TAB

\#1 MEDICATION ROOM B,3 6 1 NORTH EXTERNAL

\#2 MEDICATION ROOM B,2 6 1 SOUTH EXTERNAL

\#3 MEDICATION ROOM B,3 6 33 EXTERNAL

2 NH

2 EAST

=\> DYPHYLLINE GG ELIXIR

\#1 MEDICATION ROOM B,2 100 1 WEST ORAL SOLID

1 NORTH

\#2 MEDICATION ROOM MC,1,2 100 1 SOUTH ORAL SOLID

\#3 MEDICATION ROOM D,3 100 33 ORAL SOLID

2 NH

2 EAST

=\> LIDOCAINE 40MG/ML INJ

\#2 MEDICATION ROOM NONE 10 NONE EXTERNAL

=\> MEPHOBARBITAL 50MG TAB

\#1 MEDICATION ROOM MC,2,4 2 1 NORTH INTERNAL

\#3 MEDICATION ROOM MC,1,3 2 33 INTERNAL

2 NH

2 EAST

=\> MESORIDAZINE 25MG/ML SOLN

\#2 MEDICATION ROOM MC,2,2 10 1 SOUTH INJECTION

\#3 MEDICATION ROOM MC,2,2 10 1 SOUTH INJECTION

DRUG CLOSET MC,2,2 10 NONE INJECTION

=\> METHYL SALICYLATE BALM 30GM

•

•

•

*\[This report has been abbreviated to save space.\]*1.12.5 List Stock Items<span id="_Toc511400110" class="anchor"></span> (132 column) ; \[PSGW PRINT AOU STOCK\]

This option allows you to print the items entered as active stock for an Area of Use in PHARMACY AOU STOCK file (#58.1). The report prints all items currently available for inventory, by AOU and will display the following information:

> 1\. Item TYPE (for the report sorted by TYPE/LOCATION/ITEM)

> 2\. Current Stock Level

> 3\. Current Reorder Level

> 4\. Current Minimum Quantity to Dispense

> 5\. Expiration Date

The report may be printed for a single AOU, several AOUs, or you may enter “^ALL” to print the report for all Areas of Use. Also, the report may be printed by two different sort order methods. You may print the stock list in order by type, and within type, by location. An alternate method is to print the stock list in alphabetical order.

Example 1: List Stock Items (132 column) By Type/Location/Item

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>PRINT</u> Set Up Lists

Select Print Set Up Lists Option: <u>LIST STOCK</u> Items (132 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

You may print by either of these sorting methods:

\(1\) By TYPE/LOCATION/ITEM

\(2\) Alphabetical by ITEM

Select SORT ORDER for report (enter 1 or 2): <u>1</u>

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

AOU STOCK LIST BY TYPE/LOCATION - DATE: JUN 10,1993 PAGE: 1

AREA OF USE

TYPE MINIMUM QTY EXPIRATION

LOCATION ITEM STOCK LEVEL REORDER LEVEL TO DISPENSE DATE

---------------------------------------------------------------------------------------------

==\> MED ROOM 1

TYPE: EXTERNALS

MR,CA,S1 BACITRACIN OINTMENT 1OZ 3 1 2 DEC 02,1993

MR,CA,S1 CLOTRIMAZOLE 1% CREAM 4 1 2 DEC 02,1993

MR,CA,S1 HYDROCORTISONE 1% CREAM 30G 4 2 2 AUG 13,1993

MR,CA,S2 DOMOL BATH & SHOWER OIL 8 2 6 DEC 02,1993

MR,CA,S2 HEXACHLOROPHENE DET. 5OZ 6 1 6 NOT LISTED

MR,CA,S2 HYDROGEN PEROXIDE SOLN 480ML 2 1 1 NOV 05,1993

MR,CA,S2 ISOPROPYL ALCOHOL 70% 480ML 6 1 6 DEC 02,1993

MR,CD,S3 BENZOIN COMP TINCT 1 NOT LISTED NOT LISTED

NOT LISTED ACETONE 10 5 5 DEC 02,1993

TYPE: ORAL LIQUID

MR,CC,S2 ACETAMINOPHEN 500MG/15CC ELIX 2 1 1 DEC 02,1993

MR,CC,S2 CASTOR OIL 60ML U.D. 2 1 1 SEP 25,1993

MR,CC,S2 MILK OF MAGNESIA 480ML 4 2 2

MR,CC,S3 ALUM.& MAG. HYDROXIDE GEL 6 2 6 NOT LISTED

MR,CC,S3 KAOLIN AND PECTIN SUSP 360ML 2 1 1

MR,CC,S3 MAGNESIUM CITRATE SOLN 300ML 3 1 3

TYPE: ORAL SOLID

MR,B2,S1 BUSULFAN TAB 2MG 10 5 5

MR,CA,S3 CHLORAMBUCIL TAB 2MG 5 1 3 DEC 02,1993

MR,CC,S4 ACETAMINOPHEN TAB 325MG 50 10 25

MR1,S1,D2 DIGOXIN TAB 0.125MG 2 NOT LISTED NOT LISTED

TYPE: INJECTION

MR,CC,S1 DEXTROSE 50% 50ML SYRINGE 5 1 4

MR,CC,S1 DIAZEPAM 5MG/ML 2ML AMP 10 2 6 SEP 10,1993

MR,CC,S1 GLUCAGON INJ 1MG 3 1 2 DEC 02,1993

MR,CC,S1 LIDOCAINE 1% INJ 30ML 3 2 1

TYPE: OPHTHALMIC, OTIC

MR,CA,S4 TIMOLOL 0.25% OP.SOL. 10ML 3 1 2 NOT LISTED

TYPE: SUPPOSITORY

MR,REF,S2 ACETAMINOPHEN SUPP 650MG 12 1 6 NOT LISTED

MR,REF,S2 ASPIRIN SUPP 650MG 12 1 6 NOT LISTED

MR,REF,S2 GLYCERIN SUPPOSITORIES 12'S 2 1 1

TYPE: CONTROLLED DRUG (II)

MR,CC,S1 DIAZEPAM 5MG/ML 2ML AMP 10 4 6 SEP 10,1993

TYPE: REAGENT/TEST ITEM

MR,CB,S1 KETO-DIASTIX 100'S 2 1 1

Example 2: List Stock Items (132 column) Alphabetical by ITEM

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>PRINT</u> Set Up Lists

Select Print Set Up Lists Option: <u>LIST STOCK</u> Items (132 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

You may print by either of these sorting methods:

\(1\) By TYPE/LOCATION/ITEM

\(2\) Alphabetical by ITEM

Select SORT ORDER for report (enter 1 or 2): <u>2</u>

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

ALPHABETICAL LISTING OF AOU STOCK - DATE: AUG 10,1993 PAGE: 1

AREA OF USE

TYPE MINIMUM QTY EXPIRATION

ITEM LOCATION STOCK LEVEL REORDER LEVEL TO DISPENSE DATE

---------------------------------------------------------------------------------------------------------------------

==\> MED ROOM 1

ACETAMINOPHEN 500MG/15CC ELIX. MR,CC,S2 2 1 1 DEC 02,1993

ACETAMINOPHEN SUPP 650MG MR,REF,S2 12 1 6 DNOT LISTED

ACETAMINOPHEN TAB 325MG MR,CC,S4 50 10 25 DEC 02,1993

ACETONE NOT LISTED 10 5 5 DEC 02,1993

ALUM.& MAG. HYDROXIDE GEL MR,CC,S3 6 2 6 DEC 02,1993

ASPIRIN SUPP 650MG MR,REF,S2 12 1 6 NOT LISTED

ATROPINE SULFATE INJ 0.4MG/ML,20ML MR,CC,S1 3 2 1

BACITRACIN OINTMENT 1OZ MR,CA,S1 3 1 2 DEC 02,1993

BECLOMETHASONE ORAL.INHALER 16.8GM MR,CC,S5 6 1 5

BENZOIN COMP TINC MR,CD,S3 1 NOT LISTED NOT LISTED

BLEOMYCIN INJ 15 UNIT NOT LISTED 3 1 2

BUSULFAN TAB 2M MR,B2,S1 10 5 5

CASTOR OIL 60ML U.D. MR,CC,S2 2 1 1 SEP 25,1993

CHLORAMBUCIL TAB 2MG MR,CA,S3 5 1 3 DEC 02,1993

CLOTRIMAZOLE 1% CREAM MR,CA,S1 4 1 2 DEC 02,1993

DEXTROSE 50% 50ML SYRINGE MR,CC,S1 5 1 4

DIAZEPAM 5MG/ML 2ML AMP MR,CC,S1 10 2 6 SEP 10,1993

DIGOXIN TAB 0.125MG MR1,S1,D2 2 NOT LISTED NOT LISTED

DISULFIRAM TAB 250MG MR,C1,C2 2 1 1 DEC 02,1993

DOMOL BATH & SHOWER OIL MR,CA,S2 8 2 6

EPINEPHRINE INJ 1:1000 1ML (AMPUL) MR,CC,S1 3 1 2

GLUCAGON INJ 1MG MR,CC,S1 3 1 2

GLYCERIN SUPPOSITORIES 12'S MR,REF,S2 2 1 1

HEPARIN 1,000 UNIT/ML 10ML INJ MR,CC,S1 12 6 6

HEXACHLOROPHENE DET. 5OZ MR,CA,S2 6 1 6 NOT LISTED

HYDROCORTISONE 1% CREAM 30GM MR,CA,S1 4 2 2 AUG 13,1993

HYDROGEN PEROXIDE SOLN 480ML MR,CA,S2 2 1 1 NOV 05,1993

ISOPROPYL ALCOHOL 70% 480ML MR,CA,S2 6 1 6 DEC 02,1993

KAOLIN AND PECTIN SUSP 360ML MR,CC,S3 2 1 1

KETO-DIASTIX 100'S MR,CB,S1 2 1 1

LACTULOSE SYRUP 10GM/15ML 480ML MR,CC,S3 2 1 1

LIDOCAINE 1% INJ 30ML MR,CC,S1 3 2 1

MAGNESIUM CITRATE SOLN 300ML MR,CC,S3 3 1 3

MILK OF MAGNESIA 480ML MR,CC,S2 4 2 2

POTASSIUM CHLORIDE 20MEQ EFF. T. MR,CC,S4 30 10 20

PSYLLIUM HYDROPHILIC MUCILLOID 14OZ MR,CC,S4 2 NOT LISTED NOT LISTED

SODIUM BICARBONATE 50ML SYR 8.4% MR,CC,S1 5 1 4

SODIUM CHLORIDE 0.9% 1000ML IRRIGATION CUR,CB,S3 12 1

TIMOLOL 0.25% OP.SOL. 10ML MR,CA,S4 3 1 2 NOT LISTED

1.12.6 Inventory Group List<span id="_Toc511400111" class="anchor"></span> (80 column); \[PSGW AOU INV GROUP PRINT\]

This option allows you to print the data from AOU INVENTORY GROUP file (#58.1). The report prints a list of the currently defined inventory groups with their associated Areas of Use and inventory types.

Example: Inventory Group List (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTO</u>Matic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>PRINT</u> Set Up Lists

Select Print Set Up Lists Option: <u>INV</u>entory Group List (80 column)

This report shows data stored for AOU Inventory Groups.

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

AOU INVENTORY GROUP LIST PAGE: 1

PRINTED: JUN 14,1993

=\> INVENTORY GROUP

AREA OF USE

TYPE

------------------------------------------------------------------------------

=\> 3RD FLOOR (T-TH)

CARDIAC CATH LAB

INJECTION

ORAL SOLID

=\> FIRST FLOOR

CARDIAC CATH LAB

ALL

MED ROOM 1

ALL

MED ROOM 2

ALL

=\> INJECTABLES

CARDIAC CATH LAB

INJECTION

MED ROOM 1

INJECTION

MED ROOM 2

INJECTION

MED ROOM 3

INJECTION

==\> MED ROOM 1 (ONLY)

MED ROOM 1

ALL

=\> MONDAY/DAY SHIFT

CARDIAC CATH LAB

INHALER

INJECTION

MED ROOM 1

EXTERNALS

INJECTION

ORAL LIQUID

MED ROOM 3

EXTERNALS

INJECTION

ORAL LIQUID

ORAL SOLID

=\> TEST

DRUG CLOSET

CONTROLLED DRUG (II)

1.13 Edit ‘Person Doing Inventory’<span id="_Toc511400112" class="anchor"></span>; \[PSGW EDIT INVENTORY USER\]

This option will allow editing of the field PERSON DOING INVENTORY in the PHARMACY AOU INVENTORY file (#58.19) for a selected Date/Time for Inventory.

Example: Edit ‘Person Doing Inventory’

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>EDIT</u> 'Person Doing Inventory'

This option will allow editing of the PERSON DOING INVENTORY field

in the Pharmacy AOU Inventory file for a selected Date/Time for Inventory.

Select PHARMACY AOU INVENTORY DATE/TIME FOR INVENTORY: <u>49</u> 6-3-1993@13:13:00

CLEAVER,WARD THU

PERSON DOING INVENTORY: CLEAVER,WARD// <u>CLINE,PATSY</u>

Select PHARMACY AOU INVENTORY DATE/TIME FOR INVENTORY: <u>\<RET\></u>  
1.14 Sort AOUs in Group<span id="_Toc511400113" class="anchor"></span>; \[PSGW AOU INV GROUP SORT\]

This option allows the user to change the order in which the AOUs within an inventory group will sort. Normally, the AOUs should print on the inventory sheet, etc., in the order in which they will be visited. However, VA FileMan puts them in the order in which they were defined. The process uses a “Make...Follow” logic. Select the group for which the order needs to be changed. You will be shown the current order. After the “Make...” prompt, enter the name of the AOU to be moved. Then, at the “Follow...” prompt, enter the name of the AOU that it should be inserted after. You may now view the new order, and make any other necessary changes.

Example: Sort AOUs in Group

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>SORT</u> AOUs in Group

Select AOU INVENTORY GROUP NAME: <u>MONDAY/DAY SHIFT</u>

DEVICE: *\[queue report here or send to designated device\]*

report follows

AOU Inventory Group List JUN 10,1993@10:54

Current AOU Sort Order for MONDAY/DAY SHIFT

------------------------------------------------------------------------------

MED ROOM 1

CARDIAC CATH LAB

MED ROOM 2

MED ROOM 3

Make..... <u>?</u>

Enter the name of the AOU you wish to move to another location.

Enter \<RET\> or "^" to Exit.

Make..... <u>CARDIAC CATH LAB</u>

Follow... <u>?</u>

Enter the name of the AOU you wish CARDIAC CATH LAB to follow.

Enter \<RET\> or "^" to Exit.

Follow... <u>MED ROOM 3</u>

Do you wish to print the AOU List again ? NO// <u>Y</u> (YES)

DEVICE: *\[queue report here or send to designated device\]*

AOU Inventory Group List JUN 10,1993@10:54

Current AOU Sort Order for MONDAY/DAY SHIFT

------------------------------------------------------------------------------

MED ROOM 1

MED ROOM 2

MED ROOM 3

CARDIAC CATH LAB

Make..... <u>\<RET\></u>

Select Set Up AR/WS (Build Files) Option: <u>\<RET\></u>1.15 Site Parameters<span id="_Toc511400114" class="anchor"></span> ; \[PSGW SITE\]

This option is locked with the PSGW PARAM key, and *only* the Inpatient Pharmacy Package Coordinator should be assigned this key.

Using this option, you may enter or edit the data in INPATIENT SITE file (#59.4). Site parameters allow you to customize the package to suit the needs of your VAMC. There are currently f<span id="PSGWSiteOptionBegin" class="anchor"></span>ive site parameters you need to answer: 1) “MERGE INV. SHEET AND PICK LIST?”, 2) “PRINT RETURN COLUMNS?”, 3) “BEGIN COLLECTING AMIS DATA NOW?”, 4) “IS SITE SELECTABLE FOR AR/WS?”, and 5) “DEFAULT WS REQUESTS PRINTER.”

Note : If you change a site parameter, you must exit the AR/WS module and re-enter in order for the change to be in effect.

The “MERGE INV. SHEET AND PICK LIST” prompt will be answered “YES” if a site does not physically inventory all items in each AOU when Automatic Replenishment occurs. “YES” will be used by sites that stock the AOU with the needed supplies, noting quantity dispensed on an inventory sheet. This prompt will be answered “NO” if a site conducts a manual inventory prior to the stocking process.

How should the “PRINT RETURN COLUMNS?” question be answered? If you wish to have a column to record return quantity and return reason on the inventory sheet, enter “YES” to this prompt. If you answer “NO”, then these columns will not be printed.

Initially the “BEGIN COLLECTING AMIS DATA NOW?” prompt is set to “NO”.

The setting of this parameter *directly affects the accuracy* of the AMIS report and

this parameter *shouldnot* be set to “YES” until all of the *Prepare AMIS Data* options have been completed and checked for accuracy. Carefully examine the reports produced by the *Data for AMIS Stats - Print* option and the *Show AOU Status for AMIS* option. When you are sure that the data is *accurate*, then set this parameter to “YES”. You should set this AMIS parameter to “YES” for all inpatient site names which have the “IS SITE SELECTABLE FOR AR/WS?” parameter set to “YES”. Once the parameter is set to “YES”, you should under *nocircumstances* flip the setting back and forth. After this parameter is set to “YES”, data entered during normal use of the package will accumulate to produce the AMIS report.

The “IS SITE SELECTABLE FOR AR/WS?” parameter was created because Unit Dose and AR/WS share INPATIENT SITE file (#59.4). Inpatient site names may be created for Unit Dose to affect order stop dates, etc., and those site names may be confusing to AR/WS users. Therefore, this parameter will screen out inpatient site names which are not used by AR/WS. For every entry in File 59.4, determine if the site name should be shown to users of the AR/WS package. If the site name should be shown, enter “1” or “YES” for this parameter, otherwise, enter “0” or “NO”. This site parameter is especially important for multi-divisional sites since AOUs are assigned an Inpatient Site that will receive credit for the AMIS Statistics for the AOU. For this reason, care should be taken in the creation of entries in the INPATIENT SITE file for AR/WS use.

The “DEFAULT WS REQUESTS PRINTER” parameter allows you to set a designated printer within a pharmacy to automatically print requested ward stock medications when a request is made using the Enter/Edit Nurses' On-Demand Request \[PSGW ON-DEMAND NURSING EDIT\] option. This allows pharmacy technicians to determine which ward stock medications need to be delivered to the various wards and clinics. To use this functionality, a printer from the DEVICE file (#3.5) is entered at the prompt. Leaving this field blank effectively bypasses this auto-print functionality. For sites with multiple location entries in the INPATIENT SITE file (#59.4), managers can designate a default printer for each <span id="PSGWSiteOptionEnd" class="anchor"></span>location.

There is a prescribed sequence of events that must occur based on the answer to the “MERGE INV. SHEET AND PICK LIST” site parameter. This sequence is diagramed for you on page 61. The sequence is as follows:

If the “MERGE INV. SHEET AND PICK LIST” prompt is answered “YES”, the Automatic Replenishment inventory sheet and the pick list are merged. The inventory sheet contains the quantity dispensed column. The *Input AOU Inventory* option and a separate pick list are omitted. The *Enter/Edit Quantity Dispensed* option is used to input all quantities dispensed. You must enter your own backorders, using the *Enter Backorders* option.

If the “MERGE INV. SHEET AND PICK LIST” prompt is answered “NO”, the inventory sheet prints without the quantity dispensed column. You will manually inventory the AOU. Use the *Input AOU Inventory* option to establish on hand quantities. Run the Pick List to show quantities to dispense. Use the *Enter/Edit Quantity Dispensed* option only if the amount dispensed was different from the amount requested. This will automatically create the backorders if the amount was less than the amount requested.

Example: Site Parameters

Select INPATIENT PHARMACY MENU Option: <u>AUTO</u>Matic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>SET</u> Up AR/WS (Build Files)

Select Set Up AR/WS (Build Files) Option: <u>SITE</u> Parameters

Select INPATIENT SITE NAME: <u>GENERAL HOSPITAL</u>

> MERGE INV. SHEET AND PICK LIST: <u>??</u>

> If 1 is entered, the Automatic Replenishment inventory sheet and pick list are merged - a separate pick list does not have to be printed. The inventory sheet contains the quantity dispensed column. The on hand values do not have to be input. The user only enters the actual quantity dispensed. If 0 is entered, the inventory sheet and pick list are not merged.

> The user prints the inventory sheet, enters on hand amounts, prints the pick list, and dispenses the items.

CHOOSE FROM:

0 NO

1 YES

MERGE INV. SHEET AND PICK LIST: <u>YES</u>

PRINT RETURN COLUMNS?: <u>??</u>

> If 1, the return quantity column and the return reason column will appear on the inventory sheet in the Automatic Replenishment package.

> If 0, the return columns do not appear on the inventory sheet.

CHOOSE FROM:

0 NO

1 YES

PRINT RETURN COLUMNS?: <u>NO</u>

BEGIN COLLECTING AMIS DATA NOW?: NO// <u>??</u>

\*\*\*WARNING\*\*\*

The setting of this parameter DIRECTLY AFFECTS THE ACCURACY of the

AMIS report! This parameter should be set to "NO" until you have

completed ALL of the "Prepare AMIS Data" options on the

"Supervisor's Menu". Carefully examine the reports produced by the

"Data for AMIS Stats - Print" option and the "Show AOU Status for

AMIS" option. When you are sure that the data is accurate, then

AND ONLY THEN, set this site parameter to "YES". Once the parameter

is set to "YES", you should under NO CIRCUMSTANCES flip the setting

back and forth. While this parameter is set to "NO", NO DATA is

collected in the AR/WS Stats File - 58.5 for AMIS statistics!

CHOOSE FROM:

0 NO

1 YES

BEGIN COLLECTING AMIS DATA NOW?: NO// <u>\<RET\></u>

IS SITE SELECTABLE FOR AR/WS?: <u>??</u>

> Should this inpatient site name be shown for use by AR/WS users? When users sign into the module to carry out AR/WS functions, should this site name be displayed? If you answer "yes", the software will display or allow you to pick this site name when you enter the module. If you answer "no", the software will "screen out" the site name so that AR/WS users will not see or be able to select the site name while in the AR/WS module.

CHOOSE FROM:

0 NO

1 YES

IS SITE SELECTABLE FOR AR/WS?: <u>YES</u>

Select INPATIENT SITE NAME: <u>\<RET\></u>

![](automatic-replenishment-ward-stock-version-2-3-user-manual/005.png)  
<span id="StockLvlSection" class="anchor"></span>1.16 AR/WS Package-wide Parameter Edit \[PSGW PACKAGE PARAMETERS\] <span id="_Toc511400115" class="anchor"></span>

This option edits general system parameters that effect the entire AR/WS package. The option is locked by the security key PSGWMGR. Currently, the only parameter included is WARD STOCK LEVEL DISPLAY ON \[PSGW_WS_LVL_ON\]. If set to YES, then the permitted ward stock level will appear on the “Enter/Edit Nurses’ On-Demand Request (80 column)” \[PSGW ON-DEMAND NURSING EDIT\] option and on the “Print an On-Demand Report by Date/AOU (80 column)” \[PSGW ON-DEMAND PRINT\] option. If set to NO, then the permitted ward stock level will not appear on these options.  
2.0 Prepare AMIS Data<span id="_Toc511400116" class="anchor"></span>; \[PSGW PREPARE AMIS DATA\]

In order for AMIS to have the necessary data to compile AMIS statistics, and in order for cost reports to be accurate, needed information must be supplied. The following options included in the *Prepare AMIS Data* menu are used for preparing the data base with AR/WS AMIS data.

> *Print AMIS Worksheet (80 column)*

> *Enter AMIS Data for All Drugs/All AOUs*

> *Data for AMIS Stats - Print (132 column)*

> *AMIS Data Enter/Edit (Single Drug)*

> *Identify AOU Returns & AMIS Count*

> *Identify AOU INPATIENT SITE*

> *Show AOU Status for AMIS (80 column)*

The *Prepare AMIS Data* options should be done as soon as possible after the software is installed. The AMIS report and many of the cost reports are dependent on the information you supply through these options. Also, it is recommended that the *Prepare AMIS Data* options should be done in the sequence presented.

After all *Prepare AMIS Data* options are completed, reviewed, and verified as accurate, the Inpatient Pharmacy Package Coordinator should return to the *SiteParameters* option on the *Set Up AR/WS (Build Files)* menu. Only at this point should the “BEGIN COLLECTING AMIS DATA NOW?” site parameter be set to “YES” to start accumulating AMIS statistics. The AMIS parameter should be set to “YES” for all inpatient site names for which the “IS SITE SELECTABLE FOR AR/WS?” prompt is answered “YES”.

2.1 Print AMIS Worksheet <span id="_Toc511400117" class="anchor"></span>(80 column) ; \[PSGW PRINT AMIS WORKSHEET\]

The purpose of this option is to provide a worksheet for the user so that the AMIS category and AMIS conversion number can be determined for all AR/WS drugs in all AOUs. The worksheet presents all AR/WS drugs by type, and within type, the drugs are listed alphabetically. Some drugs may not be classified by type (e.g., on-demands); these items will be presented at the end of the list as “Unclassified by type”. There are columns on the worksheet for the user to write down the AMIS category and AMIS conversion number.

Before the list of AR/WS drugs prints out, a page of instructions prints first. This information gives an explanation of the AMIS category and AMIS conversion number.

The AMIS category will classify the drug for AMIS purposes. The user will enter 0, 1, 2, or 3. A 0 means that the drug is classified as field 03 or 04 on AMIS (i.e., doses). 1 means that the drug is classified as field 06 or 07 on AMIS (i.e., units). 2 means that the drug is classified as field 17 on AMIS (i.e., solutions or sets) and 3 means the drug is classified as field 22 (i.e., blood and blood products).

The AMIS conversion number is a number which reflects the number of doses contained in a single quantity dispensed. For example, a 20cc multi-dose vial has an AMIS conversion number of 20.

Using the completed worksheet, the data may be entered into the computer using the *Enter AMIS Data for All Drugs/All AOUs* option.

Example: Print AMIS Worksheet (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>PRINT</u> AMIS Worksheet (80 column)

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or select print device\]*

report follows

AMIS DATA WORKSHEET

For each drug listed on the following page(s), determine the AMIS category and AMIS conversion number to be entered for AR/WS AMIS statistics.

AMIS CATEGORY will classify the drug for AR/WS AMIS.

You will enter "0", "1", "2", or "3".

==\> "0" Means the drug is classified as field 03 or 04.

Include tablets, capsules, multi-dose vials, etc.

Exclude multiple-dose externals, liquids, or antacids.

==\> "1" Means the drug is classified as field 06 or 07.

Include multiple-dose externals, liquids, antacids, otics,

ophthalmics, and inhalations.

==\> "2" Means the drug is classified as field 17.

Include solutions and administration sets.

==\> "3" Means the drug is classified as field 22.

Include blood and blood products.

AMIS CONVERSION NUMBER:

This number reflects the number of doses/units contained in a single

quantity dispensed. For example:

For a 20cc vial, quantity dispensed is 1, and conversion number is 20.

For 5oz. antacid, quantity dispensed is 1, and conversion number is 1.

For a bottle of 100 aspirin, quantity dispensed is 1, and conversion

number is 100.

PAGE: 1 DATE: MAY 26,1993

AMIS DATA WORKSHEET

TYPE AMIS CATEGORY AMIS CONVERSION

DRUG NAME (0,1,2, or 3) NUMBER

==============================================================================

EXTERNAL

DEXTROTHYROXINE SODIUM 2MG TAB \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

LIDOCAINE 40MG/ML INJ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

METHYL SALICYLATE BALM 30GM \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

METOPROLOL TARTRATE 50MG TAB \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

INJECTION

MESORIDAZINE 25MG/ML SOLN \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PAGE: 2 DATE: MAY 26,1993

AMIS DATA WORKSHEET

TYPE AMIS CATEGORY AMIS CONVERSION

DRUG NAME (0,1,2, or 3) NUMBER

==============================================================================

INTERNAL

MEPHOBARBITAL 50MG TAB \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

METHYL SALICYLATE BALM 30GM \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ORAL LIQUID

METHYL SALICYLATE BALM 30GM \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ORAL SOLID

DYPHYLLINE GG ELIXIR \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PAGE: 3 DATE: MAY 26,1993

AMIS DATA WORKSHEET

TYPE AMIS CATEGORY AMIS CONVERSION

DRUG NAME (0,1,2, or 3) NUMBER

==============================================================================

SACCHARIN SODIUM 30MG SOL TAB \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ALL

METOPROLOL TARTRATE 50MG TAB \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\*\* UNCLASSIFIED BY TYPE:

Select Prepare AMIS Data Option: <u>\<RET\></u>2.2 Enter AMIS Data for All Drugs/All AOUs<span id="_Toc511400118" class="anchor"></span>

> \[PSGW ENTER AMIS DATA/ALL DRUGS\]

This option allows the entry of AMIS data for all drugs in all AOUs used in AR/WS. The drugs are presented by type, and within type, in alphabetical order. For each drug, you are asked to enter the AMIS category and AMIS conversion number. If the conversion number for a drug is “1”, then you must key in “1”; no defaults are assumed. The drugs will be shown in the same order as on the AMIS worksheet, with one exception. If a drug is defined as more than one type, it will be asked only once.

If you do not want to enter all of this information at one time, simply enter “^” to quit. The next time you return to this option, you will only be asked to enter data for those drugs which were previously unanswered. If you are unsure of an answer and wish to leave it blank, press \<RET\>; the drug will be asked again the next time the option is selected.

All of the information is complete for all AR/WS drugs, if you select the option, and it loops through all of your types without displaying any drugs. A message will print stating, “All drugs in all AOUs contain AMIS data”; then you are through with the entry process.

If an error was made while entering the data, make note of the drug name (i.e., mark it on the AMIS worksheet), and continue with the process. It is easier to deal with these exceptions at the end. Later, use the *AMIS DataEnter/Edit (Single Drug)* option to make your corrections.

When you see the “All drugs in all AOUs contain AMIS data” message, you are ready to proceed to the next step. Use the *Data for AMIS Stats - Print (132 column)* option to get a printout of the information entered.

Example: Enter AMIS Data for All Drugs/All AOUs

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>ENTER</u> AMIS Data for All Drugs/All AOUs

You must enter "^" at any prompt to quit.

Press \<RETURN\> at any prompt to skip that drug.

If the conversion number is "1", then YOU MUST

KEY IN "1"; no defaults are assumed!

I need to gather some information now.

This may take a little while.........

TYPE: INJECTABLE

==\> AMPICILLIN SOD. 1GM S.P.

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>1</u>

==\> ARTERIAL BLOOD GAS KIT

Enter AMIS Category: <u>1</u>

Enter AMIS Conversion Number: <u>1</u>

==\> ATROPINE 1MG/10ML SYRINGE (BRISTOJECT)

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>1</u>

==\> CEFAZOLIN SOD 1GM S.P.

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>1</u>

==\> DEXTROSE 50%,50ML W/SYRINGE

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>1</u>

==\> DIAZEPAM 5MG/ML 2ML S.S.

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>1</u>

==\> DIGOXIN 0.5MG/2ML S.S.

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>1</u>

==\> GLUCAGON 1MG S.P.

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>1</u>

==\> HEPARIN 1,000 UNIT/ML S.S. (10ML)

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>10</u>

==\> LIDOCAINE 2% INJ. 20ML.

Enter AMIS Category: <u>0</u>

Enter AMIS Conversion Number: <u>20</u>

•

•

•

*\[This report has been abbreviated to save space.\]*2.3 Data for AMIS Stats - Print<span id="_Toc511400119" class="anchor"></span> (132 column);

> \[PSGW PRINT DATA FOR AMIS STATS\]

This option prints the pertinent data from the DRUG file which will be used to calculate the AMIS report and various cost reports. The data on the printout should be inspected for accuracy and any discrepancies marked for correction.

For each AR/WS drug, the report shows order unit, price per order unit, dispense units per order unit, price per dispense unit, AMIS category, and AMIS conversion number. The drugs are presented in order by type, and within type they are alphabetical. On-demands which are not classified by type will be listed last. If any of these necessary fields are missing, the message “NO DATA” will be printed on the report.

Using this report, you should be able to locate inaccurate data. Corrections should be made through the *Enter/Edit AMIS Data (Single Drug)* option.

Example: Data for AMIS Stats - Print (132 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>DATA</u> for AMIS Stats - Print (132 column)

This report shows data stored for AR/WS AMIS statistics.

Use Enter/Edit AMIS Data (Single Drug) to make corrections.

Right margin for this report is 132 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

![](automatic-replenishment-ward-stock-version-2-3-user-manual/006.png)  
2.4 AMIS Data Enter/Edit (Single Drug)<span id="_Toc511400120" class="anchor"></span>; \[PSGW ENTER/EDIT AMIS DATA\]

This option is a VA FileMan input template on the DRUG file (#50). After selecting a drug from the DRUG file, you may enter/edit the following fields: ORDER UNIT, PRICE PER ORDER UNIT, DISPENSE UNITS PER ORDER UNIT, AR/WS AMIS CATEGORY, and AR/WS AMIS CONVERSION NUMBER. PRICE PER DISPENSE UNIT is a computed field and does not require editing.

This option is most likely to be used to make corrections to the cost and AMIS data for AR/WS drugs which were found to be in error on the Data for AR/WS AMIS Stats printout. It may also be used periodically to update cost information.

Example: AMIS Data Enter/Edit (Single Drug)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>AMIS</u> Data Enter/Edit (Single Drug)

Select DRUG GENERIC NAME: <u>ARTERIAL BLOOD GAS KIT</u>

ORDER UNIT: <u>EA</u> EACH

PRICE PER ORDER UNIT: <u>2.78</u>

DISPENSE UNITS PER ORDER UNIT: <u>1</u>

AR/WS AMIS CATEGORY: Field 06 or 07 - Units of Issue// <u>\<RET\></u>

AR/WS AMIS CONVERSION NUMBER: 1// <u>\<RET\></u>

Select DRUG GENERIC NAME: <u>LIDOCAINE 2% S.S. (100MG IN 5ML SYRINGE)</u>

ORDER UNIT: PG// <u>^AR/WS AMIS CAT</u>EGORY

AR/WS AMIS CATEGORY: <u>0</u> Field 03 or 04 - Doses by Type

AR/WS AMIS CONVERSION NUMBER: <u>1</u>

Select DRUG GENERIC NAME: <u>DARVON-N SUSP</u>,50MG/5ML (16OZ BT)

ORDER UNIT: <u>BT</u> BOTTLE

PRICE PER ORDER UNIT: <u>12.96</u>

DISPENSE UNITS PER ORDER UNIT: <u>1</u>

AR/WS AMIS CATEGORY: Field 06 or 07 - Units of Issue // <u>^</u>

Select DRUG GENERIC NAME: <u>KAOLIN AND PECTIN SUSP</u>ENSION (16OZ BT)

ORDER UNIT: BT// <u>^AR/WS AMIS CAT</u>EGORY

AR/WS AMIS CATEGORY: <u>1</u> Field 06 or 07 - Units of Issue

AR/WS AMIS CONVERSION NUMBER: <u>1</u>

Select DRUG GENERIC NAME: <u>\<RET\></u>2.5 Identify AOU Returns & AMIS Count<span id="_Toc511400121" class="anchor"></span>; \[PSGW AOU RETURNS & AMIS COUNT\]

For AMIS purposes, information must be entered about each AOU. This option loops through all of your AOUs, and asks 1) how to credit returns, and 2) if inventories on the AOU are to be counted on the AMIS report.

The system must know how to credit returns for each AOU. This option allows the user to identify the usual method of drug distribution for the AOU. This usual method will be credited with all returns for that AOU for AMIS purposes. The usual method will be either 1) automatic replenishment, or 2) ward stock-on-demand. If this information is not available when a returned item is entered into the system, the default method of automatic replenishment will be credited.

The system must know, for AMIS purposes, if the inventories for an AOU are to be counted in AR/WS STATS file (#58.5). Some creative stations are using the AR/WS package for internal Inpatient Pharmacy inventory purposes. Naturally, the inventory counts for these AOUs should not show up on the AMIS report. If you answer “YES” to the “COUNT ON AMIS?” prompt, then this AOU will be counted on AMIS. If you answer “NO”, then NO DATA is collected in the AR/WS STATS file for AMIS calculation. This is *not* a field to be switched back and forth. Again, if this field is answered “NO”, then *no* data is collected for calculations for AMIS.

Since this option loops through all of the AOUs in PHARMACY AOU STOCK file (#58.1), you may wish to have another method of pulling up this data for a single AOU. Use the *Create the Area of Use* option if necessary to make corrections for a single AOU.

After the data for all AOUs has been entered, you may wish to view this data to verify accuracy. The *Show AOU Status for AMIS* option will present the information for you.

Example: Identify AOU Returns & AMIS Count

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>IDENTIFY</u> AOU Returns & AMIS Count

For AMIS purposes, the system must know how to credit returns.

Identify the "usual" method of drug distribution to be credited

for each AOU. Answer "A" for Automatic Replenishment or

"W" for Ward Stock - On Demand.

For AMIS purposes, the system must know if inventories for this AOU

are to be counted in the AMIS Stats File.

For each AOU, answer "yes" or "no".

> Area of Use: MED ROOM 1

> Returns credited to: <u>A</u>

> Count on AMIS? <u>Y</u>

> Area of Use: MED ROOM 2

> Returns credited to: <u>W</u>

> Count on AMIS? <u>Y</u>

> Area of Use: MED ROOM 3

> Returns credited to: <u>A</u>

> Count on AMIS? <u>Y</u>

> Area of Use: DENTAL CLINIC

> Returns credited to: <u>W</u>

> Count on AMIS? <u>Y</u>

> Area of Use: CARDIAC CATH LAB

> Returns credited to: <u>A</u>

> Count on AMIS? <u>Y</u>

> Area of Use: DRUG CLOSET

> Returns credited to: <u>A</u>

> Count on AMIS? <u>Y</u>2.6 Identify AOU INPATIENT SITE<span id="_Toc511400122" class="anchor"></span>; \[PSGW INPUT AOU INP SITE\]

AR/WS AMIS Statistics are stored in the AR/WS STATS file (#58.5) by date and by Inpatient Site. This was done so that medical centers that are multi-divisional may report their AR/WS Stats separately for each division. In order to accomplish this separation of data it is necessary for single division sites, as well as multi-divisional sites, to assign an Inpatient Site (from the INPATIENT SITE file (#59.4)) to each AOU in the PHARMACY AOU STOCK file (#58.1).

> **NOTE:** It is very important that these assignments be made since failure to do so will directly affect the accuracy of the AR/WS AMIS report.

This option is a quick way to go through the PHARMACY AOU STOCK file and identify all active AOUs that are missing an Inpatient Site designation. The user will be allowed to choose an Inpatient Site from the entries in the INPATIENT SITE file (#59.4) that have been defined as “selectable for AR/WS”. If the user “up-arrows” out of the loop at any point, he/she will be prompted to finish the editing as soon as possible. When the user comes back into the option later, the editing will pick up at the point where it was interrupted. If there are no AOUs found without an Inpatient Site designation, a message will be displayed to inform the user of this fact. Since this option was designed as a quick method of looping through File 58.1, users may not edit existing Inpatient Site definitions for AOUs. This may be accomplished through the *Create the Area of Use* option under the Supervisor’s *Set Up AR/WS (Build Files)* option.

Example 1: Identify AOU INPATIENT SITE with an Interrupted Loop

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> HOSPITAL

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>IDENTIFY AOU</u> INPATIENT SITE

This option will loop thru the PHARMACY AOU STOCK FILE (#58.1) and

locate all "ACTIVE" AOUs that do not have an INPATIENT SITE defined.

=\> CARDIAC CATH LAB

INPATIENT SITE: <u>SOUTH</u> HOSPITAL

=\> DENTAL CLINIC

INPATIENT SITE: <u>SOUTH</u> HOSPITAL

=\> DRUG CLOSET

INPATIENT SITE: <u>^</u>

LOOP INTERRUPTED!

\*\*\* Please complete this editing soon, it is VERY IMPORTANT that \*\*\*

\*\*\* all your AOUs have the INPATIENT SITE field defined. \*\*\*Example 2: Identify AOU INPATIENT SITE with a Completed Loop

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> HOSPITAL

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>IDENTIFY AOU</u> INPATIENT SITE

This option will loop thru the PHARMACY AOU STOCK FILE (#58.1) and

locate all "ACTIVE" AOUs that do not have an INPATIENT SITE defined.

=\> DRUG CLOSET

INPATIENT SITE: <u>SOUTH</u> HOSPITAL

=\> MED ROOM 1

INPATIENT SITE: <u>SOUTH</u> HOSPITAL

=\> MED ROOM 2

INPATIENT SITE: <u>SOUTH</u> HOSPITAL

=\> MED ROOM 3

INPATIENT SITE: <u>SOUTH</u> HOSPITAL

LOOP COMPLETED!

Example 3: No AOUs found without an Inpatient Site

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> HOSPITAL

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>IDENTIFY AOU</u> INPATIENT SITE

This option will loop thru the PHARMACY AOU STOCK FILE (#58.1) and

locate all "ACTIVE" AOUs that do not have an INPATIENT SITE defined.

ALL ACTIVE AOUs HAVE INPATIENT SITE DEFINED!!

  
2.7 Show AOU Status for AMIS<span id="_Toc511400123" class="anchor"></span> (80 column); \[PSGW AOU RET/AMIS CT PRINT\]

The data presented in this report was entered using the *Identify AOU Returns & AMIS Count* option. The fields shown to you on this report include AREA OF USE NAME, INPATIENT SITE, RETURNS CREDITED TO, and COUNT ON AMIS. It would be advantageous for you to make sure that this data is correct before conducting inventories with version 2.3 of the AR/WS software. If information is not entered for these fields for each AOU, the software will use these defaults: For each AOU, returns will be credited to automatic replenishment, and the AOU will be counted for AMIS statistics when the “BEGIN COLLECTING AMIS DATA NOW?” site parameter is set to “YES”.

Example: Show AOU Status for AMIS (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> HOSPITAL

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>SHOW</u> AOU Status for AMIS (80 column)

This option prints a list of active AOUs displaying the following data:

1\. INPATIENT SITE

2\. RETURNS CREDITED TO

3\. COUNT ON AMIS

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

AOU LISTING - RETURNS AND AMIS COUNT PAGE: 1

PRINTED: MAY 26,1993

COUNT

RETURNS ON

AREA OF USE (AOU) INPATIENT SITE CREDITED TO AMIS?

------------------------------------------------------------------------------CARDIAC CATH LAB SOUTH HOSPITAL AR YES

DENTAL CLINIC SOUTH HOSPITAL WS YES

MED ROOM 1 SOUTH HOSPITAL AR YES

MED ROOM 2 SOUTH HOSPITAL WS YES

MED ROOM 3 SOUTH HOSPITAL AR YES

DRUG CLOSET SOUTH HOSPITAL AR YES

END OF REPORT! Press \<RETURN\> to return to Menu:<u>\<RET\></u>3.0 Management Reports<span id="_Toc511400124" class="anchor"></span>; \[PSGW MGT REPORTS\]

This menu gives access to various management reports, including the printing of the AMIS report. There are currently seven options on this menu.

> *AR/WS AMIS Report . . .*

> *Cost Report Per AOU (80 column)*

> *Single Item Cost Report (80 column)*

> *High Cost Report (80 column)*

> *High Volume Report (80 column)*

> *Duplicate Entry Report (132 column)*

> *Standard Cost Report (132 column)*

After the *Prepare AMIS Data* options are completed, you may get printouts from all of the above reports (with the exception of the AMIS report) on existing data in your data base. Thus, you will be able to print out historical cost and volume reports. These reports must sort through large amounts of data, especially if the report is printed for a number of months.

> **NOTE:** It is highly recommended that you queue the reports to run during the off hours at a time that does not conflict with system backup.

In order to queue a report, at the “DEVICE” prompt, enter a “Q”. You will then be asked, “QUEUE TO PRINT ON DEVICE:”. Enter the device number of the printer to which you wish to send the report. The next question is: “REQUESTED START TIME: NOW//”. Enter the time that you wish for the report to begin.

3.1 AR/WS AMIS Report<span id="_Toc511400125" class="anchor"></span>; \[PSGW AMIS\]

This menu contains options which allow you to 1) supply missing information which is needed before the AMIS report will print; 2) print the AMIS report; and 3) recalculate the AMIS report. The three sub options on this menu are

> *Incomplete AMIS Data*

> *Print AMIS Report (132 column)*

> *Recalculate AMIS*

How does the AR/WS AMIS work? How is the data stored and printed? The diagram on page 79 illustrates this process. Basically, the data is input by any of five options: *Enter/Edit Quantity Dispensed, Input AOU Inventory, Enter/Edit On-Demand Request,Delete an On-Demand Request,* or *Return Items for AOU*. The data collected includes date of inventory, method of order, AOU, drug number, and quantity. This data is stored in a “temporary” location in order to speed up the interactive on-line input process. Each night, the TaskMan queues an option (*PSGW UPDATE AMIS STATS*) to loop through this “temporary” location. For each entry, the routine to calculate the AMIS data is called to store the data in AR/WS STATS file (#58.5). If complete information is available in the DRUG file for the drug/item, then AMIS data is calculated and stored in the “cumulative” portion of the AR/WS STATS file. However, if complete information is not available in the DRUG file for an item, then drug information is stored in the “incomplete” portion of the AR/WS STATS file. The missing data must be supplied via the *Incomplete AMIS Data* option before the AMIS report will print. When you select the *Print AMIS Report* option, if the needed data is available (drug cost, AMIS conversion number, AMIS field), then the report prints for the selected date range. After checking the report, if the numbers are inconsistent with manual estimates, it is possible that you may need to adjust AMIS conversion numbers, cost, etc. Refer back to the Data for AMIS Stats Report. Use the *AMIS DataEnter/Edit (Single Drug)* option to adjust drug data. Then use the *RecalculateAMIS* option to recompile the AMIS data. After the recompilation has finished, return to the *Print AMIS Report* option to reprint the report.

Since the data in the AR/WS STATS file is stored by Inpatient Site as well as by date, any of the AMIS transactions (described above) for AOUs that do not have an Inpatient Site designation or have an INVALID Inpatient Site will be flagged by the nightly job (PSGW UPDATE AMIS STATS). A MailMan message will be sent to all holders of the PSGWMGR security key informing them of the need to supply the missing information.

*\[Examples of the MailMan messages follows on the next page.\]*Example: Message sent for MISSING DATA:

Subj. UPDATE AR/WS AMIS STATS/MISSING DATA 06 AUG 93 09:30 19 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket.

------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\* MISSING DATA NOTIFICATION \*\*\*\*\*\*\*\*\*\*

On AUG 6,1993, the nightly job to update AR/WS AMIS Stats file (#58.5)

was unable to process the AMIS activity for the following AOU:

1\. MED ROOM 3

The above AOU is missing an INPATIENT SITE assignment in the PHARMACY AOU

STOCK file (#58.1). Until this information is supplied, NO AMIS data can

be stored for the AOU.

One of the following Supervisor options may be used to supply the missing

data: 1. Create the Area of Use

2\. Identify AOU INPATIENT SITE

\*\*\* Please note that the AMIS data for the listed AOU has NOT been lost.

It will be picked up the next time the nightly job runs AFTER an Inpatient

Site assignment has been made!!

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>Example: Message sent for INVALID DATA:

Subj. UPDATE AR/WS AMIS STATS/INVALID DATA 06 AUG 93 09:30 18 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket.

------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\* INVALID DATA NOTIFICATION \*\*\*\*\*\*\*\*\*\*

On AUG 6,1993, the nightly job to update AR/WS AMIS Stats file (#58.5)

identified INVALID Inpatient Site data in the PHARMACY AOU STOCK file (#58.1)

for the following AOU:

1\. MED ROOM 3

=\>currently has an Inpatient Site assignment of NURSING HOME

Until a VALID Inpatient Site selection (i.e. an Inpatient Site that has been

flagged as 'Selectable for AR/WS' in the INPATIENT SITE file (#59.4)) is made

for the above AOU, NO AMIS data can be stored. The Inpatient Site field

can be edited through the Supervisor option 'Create the Area of Use'.

\*\*\* Please note that the AMIS data for the listed AOU has NOT been lost.

It will be picked up the next time the nightly job runs AFTER a VALID

Inpatient Site assignment has been made!!

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>  
![](automatic-replenishment-ward-stock-version-2-3-user-manual/007.png)  
3.1.1 Incomplete AMIS Data<span id="_Toc511400126" class="anchor"></span>; \[PSGW CLEAR AMIS EXCEPTIONS\]

When quantity dispensed is entered for an item on an inventory or an on-demand is entered for an item or a returned item is entered into the computer, the system saves the data in a “temporary” location. A background job runs at night to calculate and move the information out of this “temporary” location into the AR/WS STATS file. If data is not available in the DRUG file for the item (cost data, AMIS category, or AMIS conversion number), then the system did not have the information to calculate AMIS. So, the date, drug number, quantity dispensed, and method (e.g., AR, WS, or return) are “saved”. Also, an “exceptions” cross-reference is set for the date/drug.

Before an accurate AMIS report can be printed for a selected date range, these “exceptions” must be cleared up. In fact, if you attempt to print the AMIS report and there are “exceptions” in the cross-reference, you will not be allowed to continue until needed data is supplied. If you have completed all of the *PrepareAMIS Data* options, then the only exceptions will likely come from on-demands which were not previously in the AR/WS drug list.

This option loops through the “exceptions” cross-reference for the selected date range. You will be shown the drugs which had incomplete data on those dates, and will be asked to supply the needed information. After the system verifies that the needed data is indeed in the DRUG file, the doses/units and cost are calculated and added to the AMIS statistics, and the “exceptions” cross-reference is deleted.

If there are no exceptions for the date range, the following message is displayed: “No AMIS exceptions for selected dates.”

Example: Incomplete AMIS Data

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>AR/WS</u> AMIS Report

Select AR/WS AMIS Report Option: <u>INC</u>omplete AMIS Data

This option will show AR/WS drugs for which information is missing.

The information MUST be supplied before the AMIS report can be printed.

BEGINNING date for AMIS report: <u>3 1 93</u> (MAR 01, 1993)

ENDING date for AMIS report: <u>T</u> (JUN 10, 1993)

Do you want to print a worksheet first? NO// <u>Y</u> (YES)

The right margin for this worksheet is 80

You may queue it to run at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

INCOMPLETE AMIS DATA WORKSHEET PAGE 1

FOR PERIOD MAR 1,1993 to JUN 10,1993 JUN 10,1993@16:28

=\> DRUG PRICE PER DISPENSE UNITS AR/WS AMIS AR/WS AMIS

ORDER UNIT PER ORDER UNIT CATEGORY CONVERSION \#

------------------------------------------------------------------------------

=\> ACETONE

2.00 \_\_\_\_\_\_\_ 1 1

=\> DIGOXIN TAB 0.125MG

0.74 30 1 \_\_\_\_\_\_\_

=\> POLYESTRADIOL INJ 40MG

\_\_\_\_\_\_\_ 1 \_\_\_\_\_\_\_ 1

*\[If you queued the report, it would be necessary to go back into the option from the beginning to do the editing of the missing data.\]\[If you did not queue the report, you will see the following prompt:\]*

Do you wish to edit incomplete data now? YES// <u>Y</u> (YES)

==\> Information incomplete for: ACETONE

PRICE PER ORDER UNIT: 2// <u>\<RET\></u>

DISPENSE UNITS PER ORDER UNIT: <u>240</u>

AR/WS AMIS CATEGORY: 1 // <u>\<RET\></u>

AR/WS AMIS CONVERSION NUMBER: 1// <u>\<RET\></u>

==\> Information incomplete for: DIGOXIN TAB 0.125MG

PRICE PER ORDER UNIT: .74// <u>\<RET\></u>

DISPENSE UNITS PER ORDER UNIT: 30// <u>\<RET\></u>

AR/WS AMIS CATEGORY: 1 // <u>\<RET\></u>

AR/WS AMIS CONVERSION NUMBER: <u>1</u>

==\> Information incomplete for: POLYESTRADIOL INJ 40MG

PRICE PER ORDER UNIT: <u>8.90</u>

DISPENSE UNITS PER ORDER UNIT: 1// <u>\<RET\></u>

AR/WS AMIS CATEGORY: <u>1</u> Field 06 or 07 - Units of Issue

AR/WS AMIS CONVERSION NUMBER: 1// <u>\<RET\></u>

DATA COMPLETE!!

Select AR/WS AMIS Report Option: <u>\<RET\></u>

<u>  
</u>3.1.2 Print AMIS Report <span id="_Toc511400127" class="anchor"></span>(132 column); \[PSGW PRINT AMIS REPORT\]

This option prints the AR/WS AMIS report for a selected date range. The report will detail doses by type, units of issue, fluids and administration sets, and blood products. For each of these categories, the report lists the AMIS field, doses or units dispensed, cost of dispensed, doses or units returned, cost of returns, total dispensed, total cost, and average cost per dose or unit and identifies whether the category is associated with the Inpatient Segment 158 or the Outpatient Segment 157.

The doses or units dispensed column is computed by multiplying the quantity dispensed by the AMIS conversion number entered by the *Prepare AMIS Data* options. The cost column is computed by multiplying the quantity dispensed by the price per dispense unit from the DRUG file. At the bottom of the AMIS report, there is a summary of the fields which are to be recorded on AMIS broken down by Inpatient Segment 158 and Outpatient Segment 157.

If a site is reporting multiple Inpatient Site AMIS statistics this option will print a separate AMIS report for each Inpatient Site. The report may be queued to run at a later time. However as this report is *not* CPU intensive, you may print the report immediately with no adverse effects.

Example: Print AMIS Report (132 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>AR</u>/WS AMIS Report

Select AR/WS AMIS Report Option: <u>PRINT</u> AMIS Report (132 column)

Earliest date for which you have AMIS data is: JAN 29,1993

OCT 31, 1993 at 23:23:24 is the last date that AMIS Statistics

were updated by the nightly TaskMan routine.

BEGINNING date for AMIS report: <u>6-1</u> (JUN 01, 1993)

ENDING date for AMIS report: <u>6-30</u> (JUN 30, 1993)

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

AUTOMATIC REPLENISHMENT/WARD STOCK AMIS REPORT

FOR INPATIENT SITE: SOUTH HOSPITAL

FROM JUN 1,1993 TO JUN 30,1993 PRINTED ON: NOV 1,1993@13:04

---------------------------------------------------------------------------------------------

(INPATIENT SEGMENT 158)

DOSES BY TYPE:

AVERAGE

FIELD DOSES COST OF DOSES COST OF TOTAL TOTAL COST PER

DISPENSED DISPENSED RETURNED RETURNS DISPENSED COST DOSE

------------------------------------------------------------------------------------------

03 505 205.81 0 0.00 505 205.81 0.41

04 0 0.00 0 0.00 0 0.00 0.00

----------------------------------------------------------------------------------

05 505 205.81 0 0.00 505 205.81 0.41

UNITS OF ISSUE:

AVERAGE

FIELD UNITS COST OF UNITS COST OF TOTAL TOTAL COST PER

DISPENSED DISPENSED RETURNED RETURNS DISPENSED COST UNIT

------------------------------------------------------------------------------------------

06 89 5967.75 0 0.00 89 5967.75 67.05

07 40 0.90 0 0.00 40 0.90 0.02

----------------------------------------------------------------------------------

08 129 5968.65 0 0.00 129 5968.65 46.27

FLUIDS AND ADMINISTRATION SETS:

AVERAGE

FIELD COST OF COST OF TOTAL TOTAL COST PER

DISPENSED DISPENSED RETURNED RETURNS DISPENSED COST DOSE

------------------------------------------------------------------------------------------

17 4 23.92 0 0.00 4 23.92 5.98

----------------------------------------------------------------------------------

18 4 23.92 0 0.00 4 23.92 5.98

(OUTPATIENT SEGMENT 157)

BLOOD AND BLOOD PRODUCTS:

AVERAGE

FIELD COST OF COST OF TOTAL TOTAL COST PER

DISPENSED DISPENSED RETURNED RETURNS DISPENSED COST DOSE

------------------------------------------------------------------------------------------

22 1043 1336.61 78 213.19 965 1123.41 1.16

SUMMARY OF REPORTED FIELDS:

INPATIENT SEGMENT 158 OUTPATIENT SEGMENT 157

---------------------- ----------------------

FIELD 03 505 FIELD 22 1123.41

FIELD 04 0

FIELD 05 0.41

FIELD 06 89

FIELD 07 40

FIELD 08 46.27

FIELD 17 4

FIELD 18 5.98

3.1.3 Recalculate AMIS<span id="_Toc511400128" class="anchor"></span>; \[PSGW RECALCULATE AMIS\]

The purpose of this option is to correct the AMIS when data entry errors have caused the results to be inaccurate. After the AMIS report has been printed, if you discover that the price per order unit, dispense units per order unit, AMIS category, or AMIS conversion number is incorrect for any item, this option allows you to recalculate the AMIS report. If the *Prepare AMIS Data* options were done carefully, and the Data for AMIS Stats report was reviewed and corrected, recalculation should not be necessary.

If data entry errors are discovered, use the *AMIS Data Enter/Edit (Single Drug)* option to enter the correct information. Then use *Recalculate AMIS* to recompile AMIS data for the selected date range. After you enter the beginning and ending dates for recalculation, the job is automatically queued to run in the background. Obviously, recalculation for a short period of time (i.e., a few days), will be much quicker than recalculating an entire month. You will be notified by MailMan when the recalculation is completed.

Finally, after MailMan notification, return to the *Print AMIS Report* option to print the corrected AMIS. It is suggested, at least at first, that you print the AMIS frequently and compare with manual records for accuracy.

Example: Recalculate AMIS \[PSGW RECALCULATE AMIS\]

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>AR</u>/WS AMIS Report

Select AR/WS AMIS Report Option: <u>RE</u>calculate AMIS

This option should be used ONLY if you have discovered and CHANGED

cost data, AMIS category, or AMIS conversion number in the Drug file.

Recalculation will use the new data to calculate AMIS stats.

BEGINNING date for RECALCULATION : <u>6-1</u> (JUN 01, 1993)

ENDING date for RECALCULATION: <u>6-30</u> (JUN 30, 1993)

I will now DELETE ALL AMIS DATA from JUN 1,1993 to JUN 30,1993 and RECALCULATE.

Are you SURE that is what you want to do? NO// <u>YES</u>

This job will automatically be queued to run in the background.

You will be notified by MailMan when the recalculation is completed.

RECALCULATE AMIS DATA queued!

*\[An example of the MailMan message follows.\]*Example: MailMan Message for Recalculate AMIS Data

Subj: AR/WS AMIS RECALCULATION 30 Jun 93 11:28 2 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket.

------------------------------------------------------------------------------

AR/WS AMIS RECALCULATION FROM JUN 1,1993

TO JUN 30,1993 IS NOW COMPLETED.

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>3.2 Cost Report Per AOU<span id="_Toc511400129" class="anchor"></span> (80 column) ; \[PSGW COST PER AOU\]

In order for this report to be accurate, the DRUG file must contain the correct price per dispense unit. This data should have been entered through the *PrepareAMIS Data* options on the *Supervisor’s Menu*.

This report may be printed for a date range which you select, and you may choose to print it for a single Area of Use, several Areas of Use, or for ALL Areas. You will be given the option of printing a “complete report” or a “summary report”. The report is in three parts. The first section will show, for the date range and AOU, all drugs with total quantity dispensed and cost (if you opt for the “complete report”) or just a total line for quantity dispensed and cost (if you opt for the “summary report”).

The second part of the report occurs *only* if the Area of Use has wards or locations and services defined for the AOU. This part presents a breakdown of cost by ward/location and cost by service. It shows the defined wards/locations, percentage of total, and cost per ward/location. If services are defined, it shows the defined services, percentage of ward/location, and cost per service.

The third part of the report occurs *only* if more than one AOU is selected. Summary pages print at the end giving total costs for all wards/locations and services for the reporting period. Obviously, AOU’s with no associated wards/locations or services will not be included in this summary.

Right margin for this report is 80. You may queue the report to print at a later time.

Example 1: Complete Cost Report Per AOU (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>COST</u> Report Per AOU (80 column)

Before printing this report, be sure accurate data exists for drug cost.

Use "Prepare AMIS Data": "Enter AMIS Data for All Drugs/All AOUs".

BEGINNING date for report: <u>6/1</u> (JUN 26, 1993)

ENDING date for report: <u>6/30</u> (JUN 10, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

Do you want to print:

\(1\) A complete report

\(2\) Totals and Summaries only

Enter '1' or '2': <u>1</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to a designated device\]*

report follows

COST REPORT FROM JUN 1,1993 TO JUN 30,1993 PAGE 1

DATE: JUN 10,1993@13:18

AREA OF USE

QUANTITY

ITEM DISPENSED COST

------------------------------------------------------------------------------

==\> MED ROOM 1

ACETAMINOPHEN 500MG/15CC ELIX. 1 0.01

ACETAMINOPHEN SUPP 650MG 1 100.00

ACETONE 7 0.06

ASPIRIN SUPP 650MG 100 100.00

BUSULFAN TAB 2MG 3 0.30

CASTOR OIL 60ML U.D. 1 0.40

DISULFIRAM TAB 250MG 3 0.01

SODIUM BICARBONATE 50ML SYR 8.4% 2 5.50

--------------------------------

TOTAL 118 206.28

MED ROOM 1 COST PER WARD/LOCATION

WARD/LOC % OF TOTAL COST

-----------------------------------------------------------

2 WEST 50 103.14

2 NORTH 50 103.14

COST PER SERVICE

WARD/LOC

SERVICE % OF WARD/LOC COST

-----------------------------------------------------------

2 WEST:

NEUROLOGY 100 103.14

2 NORTH:

CARDIOLOGY 100 103.14

Example 2: Totals ONLY and Summary Cost Report Per AOU (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> HOSPITAL

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>COST</u> Report Per AOU (80 column)

Before printing this report, be sure accurate data exists for drug cost.

Use "Prepare AMIS Data": "Enter AMIS Data for All Drugs/All AOUs".

BEGINNING date for report: <u>6/1</u> (JUN 26, 1993)

ENDING date for report: <u>6/30</u> (JUN 10, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

Do you want to print:

\(1\) A complete report

\(2\) Totals and Summaries only

Enter '1' or '2': <u>2</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

COST REPORT FROM JUN 1,1993 TO JUN 30,1993 PAGE 1

DATE: JUN 10,1993@13:18

QUANTITY

AREA OF USE DISPENSED COST

------------------------------------------------------------------------------

==\> MED ROOM 1

--------------------------------

TOTAL 118 206.28

MED ROOM 1 COST PER WARD/LOCATION

WARD/LOC % OF TOTAL COST

-----------------------------------------------------------

2 WEST 50 103.14

2 NORTH 50 103.14

COST PER SERVICE

WARD/LOC

SERVICE % OF WARD/LOC COST

-----------------------------------------------------------

2 WEST:

NEUROLOGY 100 103.14

2 NORTH:

CARDIOLOGY 100 103.14

3.3 Single Item Cost Report <span id="_Toc511400130" class="anchor"></span>(80 column); \[PSGW SINGLE ITEM COST\]

In order for this report to be accurate, the DRUG file must contain the correct price per dispense unit. This data should have been entered through the *PrepareAMIS Data* options on the *Supervisor’s Menu*.

This report may be printed for a date range which you select, and you may choose to print it for a single Area of Use, several Areas of Use, or for ALL Areas. The report shows, for the date range and item, the Areas of Use, quantity dispensed for each Area, and cost for that AOU. There is also a total line giving total quantity dispensed and cost for the item.

Right margin for this report is 80. You may queue the report to print at a later time.

Example: Single Item Cost Report (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>SING</u>le Item Cost Report (80 column)

Before printing this report, be sure accurate data exists for drug cost.

Use "Prepare AMIS Data": "Enter AMIS Data for All Drugs/All AOUs".

BEGINNING date for report: <u>6 1 93</u> (JAN 01, 1993)

ENDING date for report: <u>6 30 93</u> (JUN 30, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>^ALL</u>

Select ITEM: <u>ACETA</u>MINOPHEN 325 MG/CODEINE 30 MG

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

COST REPORT FROM JUN 1,1993 TO JUN 30,1993 PAGE 1

DATE: AUG 10,1993@13:07

ITEM: ACETAMINOPHEN 325MG/CODEINE 30MG TAB

QUANTITY

AREA OF USE DISPENSED COST

------------------------------------------------------------------------------

DRUG CLOSET 29 1.02

1 WEST MEDS 21 0.74

-----------------------------------

TOTAL 50 1.75

3.4 High Cost Report<span id="_Toc511400131" class="anchor"></span> (80 column); \[PSGW HIGH COST\]

In order for this report to be accurate, the DRUG file must contain the correct price per dispense unit. This data should have been entered through the *PrepareAMIS Data* options on the *Supervisor’s Menu*.

This option allows you to see drugs/items dispensed in order of cost (highest to lowest) or alphabetically by item. This report may be printed for a selected date range, and for one or all Areas of Use. If you select ALL AOUs, the drug costs will be totaled for all AOUs for which the “COUNT ON AMIS?” field is set to “YES”. Thus if you select all AOUs, this report *will not* include totals from those AOUs set up for internal inventory purposes. It shows cost and quantity dispensed for the drug during the time frame.

You will be asked for a cut off amount for the report. For example, you may only want to see drugs with a total cost greater than or equal to \$25. If you press \<RETURN\> at the “Select CUT OFF amount” prompt, then all drugs will be shown on the report.

The right margin for this report is 80. You may queue the report to print at a later time.

Example 1: High Cost Report (80 column) Sorted by Cost, Highest to Lowest

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>HIGH COST</u> Report (80 column)

Before printing this report, be sure accurate data exists for drug cost.

Use "Prepare AMIS Data": "Enter AMIS Data for All Drugs/All AOUs".

BEGINNING date for report: <u>6 1 93</u> (JUN 01, 1993)

ENDING date for report: <u>6 30 93</u> <u>(</u>JUN 30, 1993)

You may select a single AOU,

or enter "^ALL" to get cumulative volume for all AOUs.

ALL will show only AOUs with "Count on AMIS" field set to "YES".

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>^ALL</u>

The High Cost Report will show all drugs with a total cost greater

than a specified cut off amount. It will NOT list costs less than

the amount you specify below.

Select CUT OFF amount: <u>1</u>

You may print by either of these sorting methods:

\(1\) By COST (Highest to Lowest)

\(2\) Alphabetical by ITEM

Select SORT ORDER for report (enter 1 or 2): <u>1</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

HIGH COST REPORT AR/WS - FOR ALL AOUS PAGE 1

TOTAL COST GREATER THAN OR EQUAL TO \$1

FROM JUN 1,1993 TO JUN 30,1993

DATE: AUG 10,1993@13:09

ITEM TOTAL COST QUANTITY DISPENSED

------------------------------------------------------------------------------

HETASTARCH INJ 6% 500ML 141.90 6

ALBUMIN, NORMAL SERUM HUMAN 12.5GM/50ML 138.00 5

ACETAMINOPHEN SUPP 650MG 100.00 1

ASPIRIN SUPP 650MG 100.00 100

ACETAZOLAMIDE INJ 500MG 11.96 2

SODIUM BICARBONATE 50ML SYR 8.4% 5.50 2

ACETAMINOPHEN 325MG/CODEINE 30MG TAB 1.75 50

HEPARIN 1,000 UNIT/ML 10ML INJ 1.26 30

\# of Items: 8

Example 2: High Cost Report (80 column) Sorted Alphabetically by Item

Select Management Reports Option: <u>HIGH COST</u> Report (80 column)

Before printing this report, be sure accurate data exists for drug cost.

Use "Prepare AMIS Data": "Enter AMIS Data for All Drugs/All AOUs".

BEGINNING date for report: <u>6 1 93</u> (JUN 01, 1993)

ENDING date for report: <u>6 30 93</u> (JUN 30,1993)

You may select a single AOU,

or enter "^ALL" to get cumulative cost for all AOUs.

ALL will show only AOUs with "Count on AMIS" field set to "YES".

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>^ALL</u>

The High Cost Report will show all drugs with a total cost greater

than a specified cut off amount. It will NOT list costs less than

the amount you specify below.

Select CUT OFF amount: <u>1</u>

You may print by either of these sorting methods:

\(1\) By COST (Highest to Lowest)

\(2\) Alphabetical by ITEM

Select SORT ORDER for report (enter 1 or 2): <u>2</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

HIGH COST REPORT AR/WS - FOR ALL AOUS PAGE 1

TOTAL COST GREATER THAN OR EQUAL TO \$1

FROM JUN 1,1993 TO JUN 30,1993

DATE: AUG 10,1993@13:10

ITEM TOTAL COST QUANTITY DISPENSED

------------------------------------------------------------------------------

ACETAMINOPHEN 325MG/CODEINE 30MG TAB 1.75 50

ACETAMINOPHEN SUPP 650MG 100.00 1

ACETAZOLAMIDE INJ 500MG 11.96 2

ALBUMIN, NORMAL SERUM HUMAN 12.5GM/50ML 138.00 5

ASPIRIN SUPP 650MG 100.00 100

HEPARIN 1,000 UNIT/ML 10ML INJ 1.26 30

HETASTARCH INJ 6% 500ML 141.90 6

SODIUM BICARBONATE 50ML SYR 8.4% 5.50 2

\# of Items: 8

3.5 High Volume Report <span id="_Toc511400132" class="anchor"></span>(80 column); \[PSGW HIGH VOLUME\]

In order for this report to be accurate, the DRUG file must contain the correct price per dispense unit. This data should have been entered through the *PrepareAMIS Data* options on the *Supervisor’s Menu*.

This option allows you to see drugs/items in order of quantity dispensed. This report may be printed for a selected date range, and for one or all Areas of Use. If you select ALL AOUs, the quantity dispensed will be totaled for all AOUs for which the “Count on AMIS?” field is set to “YES”. Thus if you select all AOUs, this report *will not* include totals from those AOUs set up for internal inventory purposes. The report prints all drugs in order by total quantity dispensed, for the AOU (or for all AOUs). It shows total quantity dispensed and cost for the drug during the time frame.

You will be asked for a “cut off” quantity for the report. For example, if you only want to see drugs with a total quantity dispensed greater than or equal to 50, enter “50” at the “Select CUT OFF quantity:” prompt. If you press \<RETURN\> at the “CUT OFF quantity” prompt, then all drugs will be shown on the report.

The right margin for this report is 80. You may queue the report to print at a later time.

Example: High Volume Report (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>HIGH VOL</u>ume Report (80 column)

BEGINNING date for report: <u>6 1 93</u> (JUN 01, 1993)

ENDING date for report: <u>6 30 93</u> (JUN 30, 1993)

You may select a single AOU,

or enter "^ALL" to get cumulative volume for all AOUs.

ALL will show only AOUs with "Count on AMIS" field set to "YES".

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>^ALL</u>

The High Volume Report will show all drugs with a total quantity

dispensed greater than a specified cut off amount. It will NOT list

quantities less than the amount you specify below.

Select CUT OFF quantity: <u>1</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

HIGH VOLUME REPORT AR/WS - FOR ALL AOUS PAGE 1

TOTAL QUANTITY DISPENSED GREATER THAN OR EQUAL TO 1

FROM JUN 01,1993 TO JUN 30,1993

DATE: JUL 02,1993@14:26

ITEM QUANTITY DISPENSED TOTAL COST

------------------------------------------------------------------------------ASPIRIN SUPP 650MG 100 100.00

ACETAMINOPHEN 325MG/CODEINE 30MG TAB 50 1.75

HEPARIN 1,000 UNIT/ML 10ML INJ 30 1.26

ACETONE 7 0.06

HETASTARCH INJ 6% 500ML 6 141.90

ALBUMIN, NORMAL SERUM HUMAN 12.5GM/50ML 5 138.00

BUSULFAN TAB 2MG 3 0.30

DISULFIRAM TAB 250MG 3 0.01

ACETAZOLAMIDE INJ 500MG 2 11.96

SODIUM BICARBONATE 50ML SYR 8.4% 2 5.50

ACETAMINOPHEN 500MG/15CC ELIX. 1 0.01

ACETAMINOPHEN SUPP 650MG 1 100.00

CASTOR OIL 60ML U.D. 1 0.40

\# of Items: 13

3.6 Duplicate Entry Report <span id="_Toc511400133" class="anchor"></span>(132 column); \[PSGW DUPLICATE REPORT\]

This option lists all duplicate entries in the ITEM subfile (#58.11) of the PHARMACY AOU STOCK file (#58.1). The user can choose to print the report for one item, a few items, or all of the items. The report will give a listing of all inventory, return, and on-demand activity for the items chosen.

If duplicate entries do exist, please execute the following procedures to clean the subfile:

> 1\. With the information on the report, choose the duplicate that needs to be removed.

> 2\. Inactivate the chosen item in the option *Inactivate AOU Stock Item*.

> 3\. Enter a phrase such as “Do not choose” in the LOCATION field of the inactivated item. The option Item Location Codes - Enter/Edit will allow the user to edit the LOCATION field.

The inactive item will be purged from the subfile 100 days from the date of the item’s last activity.

Example: Duplicate Entry Report

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>SOUTH</u> Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>MAN</u>agement Reports

Select Management Reports Option: <u>D</u>uplicate Entry Report (132 column)

Duplicate Entries Exist in the ITEM subfile (58.11) of the

PHARMACY AOU STOCK file (#58.1) for the Following Drugs:

1\. BLEOMYCIN INJ 15 UNIT: DRUG CLOSET

2\. DEXTROTHYROXINE SODIUM 2MG TAB AOU: DRUG CLOSET

You may select one drug or

enter "^ALL" to select all drugs.

Print report for which drug: <u>1</u>

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

\*\*\* DUPLICATE ENTRY REPORT \*\*\*

DRUG: BLEOMYCIN INJ 15 UNIT PAGE 1

AOU: DRUG CLOSET

Internal Entry \#: 5

Pointer in file 50: 3

---------------------------------------------------------------------------------------------INVENTORIES:

DATE/TIME COMPILED

FOR INTO DISPENSE

INVENTORY AMIS QUANTITY ON HAND

----------------------------------------------------------------------------------------

JUN 15,1993@15:42 NO 9 3

RETURNS:

COMPILED

DATE OF RETURN INTO RETURN

RETURN QUANTITY AMIS REASON(S)

----------------------------------------------------------------------------------------

YES

JUN 15,1993 2 NO OVER STOCK

EXPIRED

ON-DEMANDS:

COMPILED

DATE/TIME QUANTITY INTO DATE/TIME

FOR ON-DEMAND DISPENSED ENTERED BY AMIS EDITED BY LAST EDITED

----------------------------------------------------------------------------------------

MAR 1,1993@15:54 NURSE,NANCY YES

MAR 5,1993@12:31 NURSE,NANCY YES

MAR 5,1993@14:26 NURSE,NANCY YES

MAR 26,1993@10:03 NURSE,NANCY YES

APR 8,1993@14:16 NURSE,NANCY YES

APR 8,1993@14:23 NURSE,NANCY YES

MAY 9,1993@12:15 NURSE,NANCY YES

MAY 10,1993@11:49 NURSE,NANCY YES

JUN 1,1993@15:33 50 NURSE,NANCY YES

DRUG: BLEOMYCIN INJ 15 UNIT PAGE 2

AOU: DRUG CLOSET

Internal Entry \#: 5

Pointer in file 50: 3

---------------------------------------------------------------------------------------------INVENTORIES:

DATE/TIME COMPILED

FOR INTO DISPENSE

INVENTORY AMIS QUANTITY ON HAND

----------------------------------------------------------------------------------------

JUN 15,1993@15:42 NO 9 3

RETURNS:

No returns shown

ON-DEMANDS:

No returns shown

3.7 Standard Cost Report (132 column)<span id="_Toc511400134" class="anchor"></span>; \[PSGW STANDARD COST REPORT\]

The Standard Cost Report lists the cost for items in one AOU, several AOUs, all AOUs, or an inventory group. This cost represents the dollar amount needed to bring each item from zero to its maximum stock level.

The TOTAL COST field is computed by multiplying the item’s stock level by the AR/WS conversion factor found in the DRUG file and then by price per dispense unit found in the DRUG file.

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

\#1 MEDICATION ROOM

\#2 MEDICATION ROOM

\#3 MEDICATION ROOM

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to a designated device\]*

report follows

![](automatic-replenishment-ward-stock-version-2-3-user-manual/008.png)  
Example 2: Standard Cost Report for an AOU

Select Management Reports Option: <u>ST</u>andard Cost Report (132 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I'): <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\#1 M</u>EDICATION ROOM

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to a designated device\]*

DEVICE: *\[queue report here or send to a designated device\]*

report follows

![](automatic-replenishment-ward-stock-version-2-3-user-manual/009.png)

4.0 Obsolete Data Purge<span id="_Toc511400135" class="anchor"></span> ; \[PSGW PURGE\]

This option is locked with the “PSGW PURGE” key, and only the Inpatient Pharmacy Package Coordinator, or his/her designee should be assigned this key. There are currently two sub options allowing files to be purged.

> *AMIS Data Purge*

> *Purge Dispensing Data*

The amount of old data to be retained is a site specific decision. It is highly recommended that you keep data for at least one quarter. Use caution when choosing dates for deletion so as not to destroy needed data. These options delete the data from your files, and it is *not able to be recovered.*4.1 AMIS Data Purge<span id="_Toc511400136" class="anchor"></span> ; \[PSGW PURGE AMIS\]

The purpose of this option is to purge old data from AR/WS AMIS STATS file (#58.5). Data should be kept in the file for at least one quarter to be able to produce the quarterly AMIS report. Use caution when choosing dates for deletion so as not to destroy needed data. The routine will not allow data newer than “T-100 days” to be deleted. The routine is automatically queued to run in the background.

Example: AMIS Data Purge

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>OBS</u>olete Data Purge

Select Obsolete Data Purge Option: <u>AMIS</u> Data Purge

This option will purge data from file PSI(58.5) - AMIS stats file.

You should retain the data for at least 1 quarter.

Therefore, the option will NOT ALLOW DELETION of data newer than "T-100".

Purge AMIS data older than (and including): T-100// <u>\<RET\></u> (MAY 01,1993)

I will now delete AMIS data that is older than (and including) MAY 01,1993

Are you SURE that is what you want to do? NO// <u>?</u>

Answer "yes" if you wish to purge AMIS data.

Answer "no" or \<return\> if you do not.

I will now delete AMIS data that is older than (and including) MAY 01,1993

Are you SURE that is what you want to do? NO// <u>YES</u>

AMIS purge queued!

4.2 Purge Dispensing Data<span id="_Toc511400137" class="anchor"></span>; \[PSGW PURGE FILES\]

The purpose of this option is to purge old data from files PHARMACY AOU STOCK file (#58.1), PHARMACY BACKORDER file (#58.3), and PHARMACY AOU INVENTORY file (#58.19). Data should be kept in the files for at least one quarter or as far back as your site might choose to know the usage, cost, etc. Use caution when choosing dates for deletion so as not to destroy needed data. The routine will not allow data newer than “T-100 days” to be deleted. The routine is queued to run in the background at a time that you select. Since the routine is CPU intensive, it should be queued to run in the off hours. It is highly recommended that you delete no more than 2 months data at a time.

The routine looks at inventory numbers that fall in the delete date range you selected. It loops through all automatic replenishment inventories, on-demand requests, and returns. Any inventories with outstanding backorders will not be deleted until the backorder is marked filled. (It may be beneficial to print the AOU Backorder Report to see if there are any old backorders that have been forgotten before running the *Purge Dispensing Data* option.) Inventory data that falls within the selected date range will be deleted in this loop. If there are drugs in an AOU which are inactivated and the inactivation date is before the “end date for deletion”, and the drugs have no inventory activity, these will be deleted from the AOU. Finally, any AOU which is not in an AOU Inventory Group and which contains no drugs (because they were inactivated and thus deleted in the above loop), will be deleted from File 58.1.

> **NOTE:** As long as an AOU is in an AOU Inventory Group, it will not be deleted. This relates to those AOUs which have no standard stock because they are used for on-demand requests only.

Example: Purge Dispensing Data

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>OBS</u>olete Data Purge

Select Obsolete Data Purge Option: <u>PURGE</u> Dispensing Data

This option will purge data from files PSI(58.1), PSI(58.3), and PSI(58.19).

You should retain the data for at least 1 quarter.

Therefore, the option will NOT ALLOW DELETION of data newer than "T-100".

\*\*WARNING\*\*

Since this option is CPU intensive,

it should be QUEUED to run in the "off" hours!

Purge INVENTORY data older than (and including): T-100// <u>\<RET\></u> (MAY 01,1993)

I will now delete INVENTORY data that is older than (and including) MAY 01,1993

Are you SURE that is what you want to do? NO// <u>YES</u>

Requested Start Time: NOW//<u>AUG 30@2000</u> (AUG 30,1993@20:00)

INVENTORY purge queued!

5.0 \[PSGW PURGE INVENTORY<span id="_Toc511400138" class="anchor"></span>\]

This option is a background job which should be scheduled through TaskMan to run each night at a convenient time. The routine should run nightly; therefore, the rescheduling frequency is “1D”. The purpose of the option is to purge the ^PSI(58.19,"AINV") global. This global location is the storage place for inventory sheets which have been printed. The data should remain in the global for a 100 day period. After that time, it is unlikely that the data will be needed. Therefore the data is purged from the system through this background job.

Using the TaskMan Manager’s *Schedule/unschedule Task Man tasks* option, select the *PSGW PURGE INVENTORY* option. At the “QUEUED TO RUN AT WHAT TIME:” prompt, enter “T@” followed by the time you choose for the job to begin. The time should be one that does not conflict with system backup. At the “RESCHEDULING FREQUENCY:” prompt, enter “1D”. The “DEVICE” prompt should remain blank since this is a background job.

Example: How to Schedule a TaskMan Task

Select Systems Manager Menu Option: <u>TASK</u>Man Manager

Select TaskMan Manager Option: <u>SCH</u>edule/unschedule Task Manager tasks

Select OPTION to schedule or re-schedule: <u>PSGW PURGE INV</u>ENTORY

QUEUED TO RUN AT WHAT TIME: <u>T@2200</u>

DEVICE FOR QUEUED JOB OUTPUT: <u>\<RET\></u>

RESCHEDULING FREQUENCY: <u>1D</u>

Select OPTION to schedule or re-schedule: <u>\<RET\></u>6.0 \[PSGW RE-INDEX AMIS<span id="_Toc511400139" class="anchor"></span>\]

This option will allow a user to queue a background job that will re-index the “AMIS” cross-reference for inventories, on-demands, and returns from a user selected date in the past to the present. This cross-reference is important because this is where the nightly job to update the AMIS STATS file (#58.5) gets the data for the update. If this cross-reference is somehow destroyed, it is very important to rebuild it. Though it is possible to accomplish this through VA FileMan (by re-indexing the INVENTORY subfield DISPENSE QUANTITY, the RETURNS subfield RETURN QUANTITY, and the ON-DEMAND subfield ON-DEMAND QUANTITY in the PHARMACY AOU STOCK file (#58.1)), this option is a quicker and easier alternative. This option is not tied to any menu, but may be hooked into a menu at the site’s discretion.

> **NOTE:** This option is CPU intensive and should be queued only in the “off” hours. Also, it should only be run if there is strong evidence that the “AMIS” cross-reference has been destroyed or corrupted.

The following is an example of how a site might choose to place this option on a menu. For this example, suppose a site has chosen to place it under the Supervisor’s menu *Prepare AMIS Data*:

Example: Editing an option through MENU MANAGEMENT:

Select OPTION NAME: <u>EVE</u> Systems Manager Menu

Select Systems Manager Menu Option: <u>MENU</u> management

Select Menu Management Option: <u>EDIT</u> options

Select OPTION to edit: <u>PSGW PREPARE AMIS DATA</u> Prepare AMIS Data

NAME: PSGW PREPARE AMIS DATA// <u>\<RET\></u>

MENU TEXT: Prepare AMIS Data// <u>\<RET\></u>

OUT OF ORDER MESSAGE: <u>\<RET\></u>

LOCK: <u>\<RET\></u>

DESCRIPTION:

1\>Main option for preparing data base with AR/WS AMIS data.

EDIT Option: <u>\<RET\></u>

CREATOR: POSTMASTER// (No Editing)

HELP FRAME: <u>\<RET\></u>

PRIORITY: <u>\<RET\></u>

PROHIBITED TIMES: <u>\<RET\></u>

TYPE: menu// <u>\<RET\></u>

Select ITEM: <u>PSGW RE-INDEX AMIS</u> Re-index AMIS Cross-Reference

ARE YOU ADDING 'PSGW RE-INDEX AMIS' AS A NEW MENU (THE 8TH FOR THIS

OPTION)? <u>Y</u> (YES)

MENU SYNONYM: <u>\<RET\></u>

SYNONYM: <u>\<RET\></u>

DISPLAY ORDER: <u>\<RET\></u>

Select ITEM: <u>\<RET\></u>

CODE XECUTED WHEN LEAVING THIS MENU:

MENU EXIT ACTION: <u>\<RET\></u>

CODE XECUTED WHEN ENTERING THIS MENU:

ACTION: <u>\<RET\></u>

Select OPTION to edit: <u>\<RET\></u>

Select Menu management Option: <u>\<RET\></u>Example: Re-index AMIS Cross-Reference

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>SUP</u>ervisor's Menu

Select Supervisor's Menu Option: <u>PREP</u>are AMIS Data

Select Prepare AMIS Data Option: <u>RE</u>-index AMIS Cross-Reference

This option will re-index the "AMIS" cross-reference for Inventories, On-Demand Requests, and Returns for a date range beginning with the START DATE you specify to the time the job runs.

\*\* WARNING \*\*

Since this option is CPU intensive,

it should be QUEUED to run in the "off" hours!

Select START DATE for re-index: <u>1 1 93</u> (JAN 01, 1993)

The "AMIS" cross-reference will now be re-indexed starting from JAN 1,1993.

Are you SURE that is what you want to do? NO// <u>?</u>

Enter 'YES' if you are satisfied with the selected date range.

Enter 'NO' or '^' if you wish to abort the re-indexing.

Are you SURE that is what you want to do? NO// <u>Y</u> (YES)

Requested Start Time: NOW// *\[At this point, queue the job for the desired time.\]*

"AMIS" cross reference re-indexing queued!

7.0 \[PSGW UPDATE AMIS STATS<span id="_Toc511400140" class="anchor"></span>\]

This option is a background job which should be scheduled through TaskMan to run each night at a convenient time. The routine should run nightly; therefore, the rescheduling frequency is “1D”. The purpose of the option is to loop through the “temporary” storage location where the day’s inventory data is stored. The routine calculates the AMIS field, AMIS quantities and cost. It then stores the data in the AR/WS STATS file and finally, deletes the data from the “temporary” storage area.

Using the TaskMan Manager’s *Schedule/unschedule Task Manager tasks* option, select the *PSGW UPDATE AMIS STATS* option. At the “QUEUED TO RUN AT WHAT TIME:” prompt, enter “T@” followed by the time you choose for the job to begin. At the “RESCHEDULING FREQUENCY:” prompt, enter “1D”. The “DEVICE” prompt should remain blank since this is a background job.

Example: How to Schedule a TaskMan Task

Select Systems Manager Menu Option: <u>TASK</u>Man Manager

Select TaskMan Manager Option: <u>SCH</u>edule/unschedule Task Manager tasks

Select OPTION to schedule or re-schedule: <u>PSGW UPDATE</u> AMIS STATS

QUEUED TO RUN AT WHAT TIME: <u>T@2200</u>

DEVICE FOR QUEUED JOB OUTPUT: <u>\<RET\></u>

RESCHEDULING FREQUENCY: <u>1D</u>

Select OPTION to schedule or re-schedule: <u>\<RET\></u>Possible problems encountered by PSGW UPDATE AMIS STATS:

In the course of updating the AR/WS Stats File (#58.5), this option may identify several problems that will result in a MailMan message being sent to holders of the PSGWMGR key. The following are examples of the problems and the messages that they would generate:

Example 1: Missing or invalid Inpatient Site data

Since the data in the AR/WS STATS file is stored by Inpatient Site as well as by date, any of the AMIS transactions for AOUs that do not have an Inpatient Site designation or have an INVALID Inpatient Site will be flagged by the nightly job PSGW UPDATE AMIS STATS. A MailMan message will be sent to all holders of the PSGWMGR security key informing them of the need to supply the missing information.

*\[ Examples of the MailMan messages follow on the next page.\]*  
Example: Message sent for Missing Data:

Subj. UPDATE AR/WS AMIS STATS/MISSING DATA 06 AUG 93 09:30 19 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket.

------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\* MISSING DATA NOTIFICATION \*\*\*\*\*\*\*\*\*\*

On AUG 6,1993, the nightly job to update AR/WS AMIS Stats file (#58.5)

was unable to process the AMIS activity for the following AOU:

1\. MED ROOM 3

The above AOU is missing an INPATIENT SITE assignment in the PHARMACY AOU

STOCK file (#58.1). Until this information is supplied, NO AMIS data can

be stored for the AOU.

One of the following Supervisor options may be used to supply the missing

data: 1. Create the Area of Use

2\. Identify AOU INPATIENT SITE

\*\*\* Please note that the AMIS data for the listed AOU has NOT been lost.

It will be picked up the next time the nightly job runs AFTER an Inpatient

Site assignment has been made!!

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>Example: Message sent for Invalid Data:

Subj. UPDATE AR/WS AMIS STATS/INVALID DATA 06 AUG 93 09:30 18 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket.

------------------------------------------------------------------------------

\*\*\*\*\*\*\*\*\*\* INVALID DATA NOTIFICATION \*\*\*\*\*\*\*\*\*\*

On AUG 6,1993, the nightly job to update AR/WS AMIS Stats file (#58.5)

identified INVALID Inpatient Site data in the PHARMACY AOU STOCK file (#58.1)

for the following AOU:

1\. MED ROOM 3

=\>currently has an Inpatient Site assignment of NURSING HOME

Until a VALID Inpatient Site selection (i.e. an Inpatient Site that has been

flagged as 'Selectable for AR/WS' in the INPATIENT SITE file (#59.4)) is made

for the above AOU, NO AMIS data can be stored. The Inpatient Site field

can be edited through the Supervisor option 'Create the Area of Use'.

\*\*\* Please note that the AMIS data for the listed AOU has NOT been lost.

It will be picked up the next time the nightly job runs AFTER a VALID

Inpatient Site assignment has been made!!

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>Example 2: Non-Pharmacy items found in AOUs

Non-Pharmacy packages, such as SURGERY, have the ability to flag certain drugs in the DRUG file (#50) for their exclusive use. This is accomplished by putting a package specific code in the DRUG file field called APPLICATION PACKAGES’ USE. Drugs that are flagged for non-pharmacy packages are *not* selectable by AR/WS for on-demands or to be used as stock items in AOUs. It is possible, however, for non-pharmacy packages to flag drugs *after* they have been defined in an AOU. This can cause a very confusing situation for AR/WS users when they are unable to do an on-demand request on the drug in question. The following is an example of what they would see if they try to look at the drug through the option *Stock Items - Enter/Edit*.

Example: Message sent for Non-Pharmacy Items:

Subj. NON-PHARMACY ITEMS FOUND 06 AUG 93 09:30 17 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket.

------------------------------------------------------------------------------

On AUG 6,1993, the nightly job to update AR/WS AMIS Stats file (#58.5)

identified the following items in the following AOUs that have been marked

in the Drug file (#50) for NON-PHARMACY use.

ITEM AOU

------------------------------------------------------------------------------

1\. DIGOXIN

MED ROOM 1

DRUG CLOSET

2\. DIAZEPAM

DRUG CLOSET

It will be necessary to either inactivate these items in the AOUs or mark

the items for PHARMACY use in the Drug file. For further explanation, please

refer to item \#7 (\[PSGW UPDATE AMIS STATS\]) under the Supervisor's Menu in

the AR/WS version 2.3 USER MANUAL.

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>

At this point it would be necessary for Pharmacy to determine if each drug is truly a non-pharmacy item, in which case it should be inactivated in the AOU. It will eventually be purged from the AOU by the option *Purge Dispensing Data*. If, however, Pharmacy determines that the drug has been incorrectly flagged by the non-pharmacy package it will be necessary to have that package remove the non-pharmacy code from the field APPLICATION PACKAGES’ USE in the DRUG file.

Production Menu  
  
Chapter Two: Production Menu<span id="_Toc511400141" class="anchor"></span>

; \[PSGW WARD STOCK\]

This menu provides access to the options that are used routinely in the normal Automatic Replenishment/Ward Stock operations. There are currently eleven sub options on this menu. They include

> *Inventory Sheet Print (132 column)*

> *Single AOU Inventory Print (132 column)*

> *Delete Inventory Date/Time*

> *Input AOU Inventory*

> *Pick List (132 column)*

> *Enter/Edit Quantity Dispensed*

> *On-Demand Requests . . .*

> *Backorder Requests . . .*

> *Return Items for AOU*

> *Crash Cart Menu . . .*

> *Auto Replenishment Reports . . .*Getting Out of an Option

To stop what you are doing, enter an up-arrow (^). You can use the up-arrow at any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering up-arrows to completely exit from the system.

1.0 Inventory Sheet Print<span id="_Toc511400143" class="anchor"></span> (132 column); \[PSGW INVENTORY SHEET\]

This option prints the AOU inventory sheet used to conduct an inventory. The columns shown on this report are directly affected by the way in which your site parameters are set. Refer to the *Site Parameter* option under the *Supervisor’sMenu* for more information on establishing the site parameters.

If you are conducting an actual “physical count” of the items in an AOU, entering the on hand amounts into the computer, and printing a pick list to pick the items to send to the AOU, then you will need a column on the inventory sheet to record the on hand quantity. If this is what you wish to do, then the “MERGE INV. SHEET AND PICK LIST” site parameter should be set to “NO”.

If you “visually” check the stock in the Area of Use for an item and place stock on the shelf, then you will need a column on the inventory sheet to enter the quantity dispensed. If this is what you wish to do, then the “MERGE INV. SHEET AND PICK LIST” site parameter should be set to “YES”.

Regardless of your stocking method, if you wish to have a column on the inventory sheet to record returns, and the reason for the return, then the “PRINT RETURN COLUMNS?” site parameter should be set to “YES”. The return reason codes have the following meanings: “E” - expired, “O” - overstocked, “D” - deleted item, and “C” - change in stock level. If you do not want the return column and return reasons on the sheet, answer “NO” to the site parameter.

The first step in creating the inventory sheet is to enter the date/time for the inventory. It is beneficial to use “NOW” as the date/time, so as to create a unique inventory number which does not conflict with other inventories done on the same date. The inventory is defined by listing the AOU Inventory Groups to be included. When your AOU Inventory Groups were created, they established the AOUs and type of items to be inventoried.

After selecting AOUs, the inventory sheet should be printed. At print time, the data for the inventory is stored in a special global - the PSI(58.19,"AINV") global. The inventory is stored in this location for three weeks. There is a background job which runs in the system every night to delete all inventory data in this global which is over 100 days old. Thus, you will not be allowed to edit inventories which are 100 days old, because they are purged from the system. This does not purge the inventory itself, but only the ability to edit the inventory sheet data.

The inventory sheet prints in AOU order, item location within AOU, inventory type, and then by item name. The columns which print on the report are affected by the setting of the Site Parameters. You will always see item name, stock level, and quick codes (if you have them defined). Depending on your site parameter settings, you may also see a column for on hand, quantity dispensed, reorder level, minimum quantity to dispense, returns, and return reason.

Right margin for this report is 132. This report may be queued to print at a later time.  
Example: Inventory Sheet Print (132 column)

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>INV</u>entory Sheet Print (132 column)

SELECT DATE/TIME FOR INVENTORY: N AUG 10, 1993@14:46

ARE YOU ADDING 'AUG 10, 1993@14:46' AS

A NEW PHARMACY AOU INVENTORY (THE NTH)? <u>Y</u> (YES)

PHARMACY AOU INVENTORY ID: 69//

PHARMACY AOU INVENTORY PERSON DOING INVENTORY: WARD-STOCK,SUPER// <u>\<RET\></u>

Select AOU INVENTORY GROUP: <u>DAY SHIFT</u>

\#1 MEDICATION ROOM \#2 MEDICATION ROOM \#3 MEDICATION ROOM

Select AOU INVENTORY GROUP: <u>\<RET\></u>

Do you wish to print the AOU Inventory Sheet: YES// <u>\<RET\></u>

Right margin for this printout is 132!

DEVICE: *\[queue report here or send to designated device\]*

Merged Inv. Sheet/Pick List follows

WARD STOCK INVENTORY FOR AUG 11,1993@09:47:49 INVENTORY \# 72 AUG 11,1993 PAGE 1

GROUP: DAY SHIFT

ITEM STOCK QUICK ON REORDER MINIMUM QTY QUANTITY RETURN

LEVEL CODE HAND LEVEL TO DISPENSE DISPENSED RETURN REASON

INVENTORIED/DELIVERED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------

\#1 MEDICATION ROOM

B BIN

RA,S3

DEXTROTHYROXINE SODIUM 2MG TAB 6 D5W1000 \_\_\_\_ 1 6 \_\_\_\_ \_\_\_\_\_ E O D C

Expiration Date: DEC 12,1993

MC MEDICINE CABINET

B2,S1

MEPHOBARBITAL 50MG TAB 2 \_\_\_\_ 5 5 \_\_\_\_ \_\_\_\_\_ E O D C

Expiration Date: SEP 23,1993

WARD STOCK INVENTORY FOR AUG 11,1993@09:47:49 INVENTORY \# 72 AUG 11,1993 PAGE 2

GROUP: DAY SHIFT

ITEM STOCK QUICK ON REORDER MINIMUM QTY QUANTITY RETURN

LEVEL CODE HAND LEVEL TO DISPENSE DISPENSED RETURN REASON

---------------------------------------------------------------------------------------------------------------

\#2 MEDICATION ROOM

B BIN

DEXTROTHYROXINE SODIUM 2MG TAB 2 \_\_\_\_ 1 1 \_\_\_\_ \_\_\_\_\_ E O D C

MC MEDICINE CABINET

B2,S1

DYPHYLLINE GG ELIXIR 100 BACOT \_\_\_\_ 1 2 \_\_\_\_ \_\_\_\_\_ E O D C

Expiration Date: OCT 10,1993

C1,C2

MESORIDAZINE 25MG/ML SOLN 10 LT1 \_\_\_\_ 1 2 \_\_\_\_ \_\_\_\_\_ E O D C

Expiration Date: DEC 14,1993

HYDROCORTISONE 1% CREAM 30GM 4 HC1 \_\_\_\_ 2 2 \_\_\_\_ \_\_\_\_\_ E O D C

WARD STOCK INVENTORY FOR AUG 11,1993@09:47:49 INVENTORY \# 72 AUG 11,1993 PAGE 3

GROUP: DAY SHIFT

ITEM STOCK QUICK ON REORDER MINIMUM QTY QUANTITY RETURN

LEVEL CODE HAND LEVEL TO DISPENSE DISPENSED RETURN REASON

---------------------------------------------------------------------------------------------------------------

\#3 MEDICATION ROOM

B BIN

CA,S1

DEXTROTHYROXINE SODIUM 2MG TAB 6 DML \_\_\_\_ 2 6 \_\_\_\_ \_\_\_\_\_ E O D C

D DRAWER

CA,S2

DYPHYLLINE GG ELIXIR 100 PH5 \_\_\_\_ 1 6 \_\_\_\_ \_\_\_\_\_ E O D C

MC MEDICINE CABINET

CC,S1

MEPHOBARBITAL 50MG TAB 2 HP \_\_\_\_ 1 1 \_\_\_\_ \_\_\_\_\_ E O D C

Non-Merged Inv. Sheet/Pick List follows

WARD STOCK INVENTORY FOR AUG 10,1993@14:46 INVENTORY \# 69 AUG 10,1993 PAGE 1

GROUP: DAY SHIFT

ITEM STOCK QUICK ON RETURN

LEVEL CODE HAND RETURN REASON

INVENTORIED/DELIVERED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------

\#1 MEDICATION ROOM

B BIN

RA,S3

DEXTROTHYROXINE SODIUM 2MG TAB 6 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

Expiration Date: DEC 12,1993

MC MEDICINE CABINET

B2,S1

MEPHOBARBITAL 50MG TAB 2 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

Expiration Date: SEP 23,1993

WARD STOCK INVENTORY FOR AUG 10,1993@14:46 INVENTORY \# 69 AUG 10,1993 PAGE 2

GROUP: DAY SHIFT

ITEM STOCK QUICK ON RETURN

LEVEL CODE HAND RETURN REASON

---------------------------------------------------------------------------------------------------------------------

\#2 MEDICATION ROOM

B BIN

CC,S1

DEXTROTHYROXINE SODIUM 2MG TAB 6 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

MC MEDICINE CABINET

CC,S1

DYPHYLLINE GG ELIXIR 100 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

Expiration Date: OCT 10,1993

CA,S2

MESORIDAZINE 25MG/ML SOLN 10 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

Expiration Date: DEC 14,1993

WARD STOCK INVENTORY FOR AUG 10,1993@14:46 INVENTORY \# 69 AUG 10,1993 PAGE 3

GROUP: DAY SHIFT

ITEM STOCK QUICK ON RETURN

LEVEL CODE HAND RETURN REASON

---------------------------------------------------------------------------------------------------------------------

\#3 MEDICATION ROOM

B BIN

RA,S3

DEXTROTHYROXINE SODIUM 2MG TAB 6 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

D DRAWER

B2,S1

DYPHYLLINE GG ELIXIR 100 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

MC MEDICINE CABINET

REF,S2

MEPHOBARBITAL 50MG TAB 2 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

2.0 Single AOU Inventory Print<span id="_Toc511400144" class="anchor"></span>; (132 column) \[PSGW INVENTORY SINGLE\]

This option will print an inventory sheet for a single AOU that is included in the inventory date/time. This option is meant primarily to be used as a means of avoiding a reprint of a lengthy inventory sheet when there has been a problem such as a printer jam.

Example: Single AOU Inventory Print

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>S</u>ingle AOU Inventory Print (132 column)

This option will print an Inventory Sheet for a single AOU that is included in

an existing Inventory Date/Time.

SELECT DATE/TIME FOR INVENTORY: <u>8 11 93</u> AUG 11, 1993

1 8-11-1993@09:18:48 WARD-STOCK,SUPER WED

DAY SHIFT

2 8-11-1993@09:47:49 WARD-STOCK,SUPER WED

DAY SHIFT

3 8-11-1993@10:08:25 WARD-STOCK,SUPER WED

DAY SHIFT

CHOOSE 1-3: <u>2</u>

The following AOUs are included on this Inventory Sheet:

\#1 MEDICATION ROOM

\#2 MEDICATION ROOM

\#3 MEDICATION ROOM

Select AOU: <u>\#1 M</u>EDICATION ROOM

Right margin for this printout is 132!

DEVICE: *\[queue report here or send to designated device\]*

Merged Single AOU Inventory Print List follows

WARD STOCK INVENTORY FOR AUG 11,1993@09:47:49 INVENTORY \# 72 AUG 11,1993 PAGE 1

GROUP: DAY SHIFT

ITEM STOCK QUICK ON REORDER MINIMUM QTY QUANTITY RETURN

LEVEL CODE HAND LEVEL TO DISPENSE DISPENSED RETURN REASON

INVENTORIED/DELIVERED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------

\#1 MEDICATION ROOM

B BIN

B1,S1

DEXTROTHYROXINE SODIUM 2MG TAB 6 D5W1000 \_\_\_\_ 1 6 \_\_\_\_ \_\_\_\_\_ E O D C

Expiration Date: DEC 12,1993

MC MEDICINE CABINET

B2,S1

MEPHOBARBITAL 50MG TAB 2 \_\_\_\_ 5 5 \_\_\_\_ \_\_\_\_\_ E O D C

Expiration Date: SEP 23,1993

Non-Merged Single AOU Inventory Print List follows

WARD STOCK INVENTORY FOR AUG 10,1993@14:46 INVENTORY \# 69 AUG 10,1993 PAGE 1

GROUP: DAY SHIFT

ITEM STOCK QUICK ON RETURN

LEVEL CODE HAND RETURN REASON

INVENTORIED/DELIVERED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---------------------------------------------------------------------------------------------------------------------

\#1 MEDICATION ROOM

B BIN

RA,S3

DEXTROTHYROXINE SODIUM 2MG TAB 6 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

Expiration Date: DEC 12,1993

MC MEDICINE CABINET

CA,S2

MEPHOBARBITAL 50MG TAB 2 \_\_\_\_\_ \_\_\_\_\_\_ E O D C

Expiration Date: SEP 23,1993

3.0 Delete Inventory Date/Time<span id="_Toc511400145" class="anchor"></span> ; \[PSGW DELETE INVENTORY\]

This option may be used to delete an Inventory Sheet that was created erroneously.

> **NOTE:** The *only* Inventory Sheets that may be deleted are those that *have not* been printed.

Example 1: Delete Inventory Date/Time

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>DEL</u>ete Inventory Date/Time

\*\*\* READY TO DELETE \*\*\*

Select DATE/TIME FOR INVENTORY to be deleted: <u>71</u> 6-10-1993@15:19:00 SMITH,J.D. FRI MED ROOM 1 (ONLY)

First, let me check for existing entries in other files for this Inventory Date.

........

None found.

Are you sure you want to delete this Inventory Sheet ? NO// <u>Y</u> (YES)

...Deleted

Example 2: Inventory Date/Time which cannot be deleted

Select DATE/TIME FOR INVENTORY to be deleted: <u>66</u> 6-17-1993@07:47:00 SMITH,J.D.. THU MED ROOM 1 (ONLY)

First, let me check for existing entries in other files for this Inventory Date.

........

\*\*\* There are entries in the PHARMACY AOU STOCK FILE (#58.1) for this

DATE/TIME FOR INVENTORY for MED ROOM(S):

------------------------------------------------------------------------------

MED ROOM 1

Because this Inventory Date is pointed to, it cannot be deleted at this time.

Select DATE/TIME FOR INVENTORY to be deleted: <u>\<RET\></u>  
4.0 Input AOU Inventory<span id="_Toc511400146" class="anchor"></span> ; \[PSGW AOU INVENTORY INPUT\]

This option is accessible only if the “MERGE INV. SHEET AND PICK LIST” site parameter is set to “NO”.

After each AOU has been manually inventoried, the amount on hand needs to be entered into the computer. At the “Select DATE/TIME FOR INVENTORY:” prompt, you may enter the inventory number from the top of the inventory sheet, or you may enter the actual date/time. You will then be prompted with items in the order that they appear on the inventory sheet. At the “ON-HAND” prompt, you may enter the amount on-hand, or you may press \<RET\> and the system will enter the item stock level as the quantity on-hand. Also, at the “ON-HAND:” prompt, you may enter an up-arrow (^), followed by an item name to jump to another item.

If you have the “PRINT RETURN COLUMNS” site parameter answered “YES”, then you may wish to mark returns and return reason on the Inventory Sheet at the time the inventory is conducted. Subtract the return quantity from the amount on hand and enter the result at the “ON-HAND” prompt in order for the pick list to calculate the correct number to pick. For example, if there are 8 items on the shelf, but 2 are being returned, then there are actually only 6 left on the shelf, so you should enter “6” at the “ON-HAND” prompt. You should then use the *ReturnItems for AOU* option to enter the returns.

You will notice that it takes a little while to enter on hand amounts. The system must subtract on hands from the stock level to determine Quantity to be Dispensed and store this information. Additionally, with the new fields, REORDER LEVEL and MINIMUM QUANTITY TO DISPENSE, adjustments will be made accordingly to the Quantity to be Dispensed if these fields are defined. For example, suppose the following set ups for an item in an AOU:

Example 1: Input AOU Inventory

ITEM STOCK LEVEL REORDER LEVEL MIN. QTY TO DISPENSE

------------------------------------------------------------------------------

MYLANTA II SUSP (OZ) 12

=\> ON-HAND AMOUNT: 10 = QUANTITY TO BE DISPENSED: 2

For this case, since the REORDER LEVEL and the MINIMUM QTY TO DISPENSE fields are blank, the system will calculate a Quantity to be Dispensed of “2”.

  
Example 2: Input AOU Inventory

ITEM STOCK LEVEL REORDER LEVEL MIN. QTY. TO DISPENSE

------------------------------------------------------------------------------

MYLANTA II SUSP (OZ) 12 6 6

=\> ON-HAND AMOUNT: 10 = QUANTITY TO BE DISPENSED: 0

For this case, suppose a site has decided that they do not wish to have any amounts dispensed for this item until the on-hand amount has dropped to at least “6”. Furthermore, because this item comes in packages of “6”, they have decided that the minimum quantity of this item to be dispensed is “6”. Now, the system will calculate a Quantity to be Dispensed of “0” since the reorder level has not been reached. Finally, the system must enter the quantity dispensed into the AMIS statistics, and enough data must be retained to be able to recalculate the AMIS if necessary.

Example 3: Input AOU Inventory

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>INPUT AOU</u> Inventory

SELECT DATE/TIME FOR INVENTORY: <u>66</u> 7-13-1993@07:47:00 SMITH,J.D. THU

MED ROOM 1 (ONLY)

Select AREA OF USE: MED ROOM 1// <u>\<RET\></u>

ITEM: ACETONE

ON-HAND: <u>3</u>

ITEM: BLEOMYCIN INJ 15 UNIT

ON-HAND: <u>1</u>

ITEM: SODIUM CHLORIDE 0.9% 1000ML IRRIGATION

ON-HAND: <u>6</u>

ITEM: DEXTROSE 5% IN WATER 1000ML

ON-HAND: <u>1</u>

ITEM: BUSULFAN TAB 2MG

ON-HAND: <u>5</u>

ITEM: DISULFIRAM TAB 250MG

ON-HAND: <u>1</u>

ITEM: BACITRACIN OINTMENT 1OZ

ON-HAND: <u>2</u>

ITEM: CLOTRIMAZOLE 1% CREAM

ON-HAND: <u>0</u>

ITEM: HYDROCORTISONE 1% CREAM 30GM

ON-HAND: <u>1</u>

ITEM: DOMOL BATH & SHOWER OIL

ON-HAND: <u>2</u>

ITEM: HEXACHLOROPHENE DET. 5OZ

ON-HAND: <u>5</u>

ITEM: HYDROGEN PEROXIDE SOLN 480ML

ON-HAND: <u>1</u>

ITEM: ISOPROPYL ALCOHOL 70% 480ML

ON-HAND: <u>4</u>

ITEM: CHLORAMBUCIL TAB 2MG

ON-HAND: <u>1</u>

ITEM: TIMOLOL 0.25% OP.SOL. 10ML

ON-HAND: <u>2</u>

ITEM: KETO-DIASTIX 100'S

ON-HAND: <u>2</u>

ITEM: ATROPINE SULFATE INJ 0.4MG/ML,20ML

ON-HAND: <u>1</u>

ITEM: DEXTROSE 50% 50ML SYRINGE

ON-HAND: <u>1</u>

ITEM: DIAZEPAM 5MG/ML 2ML AMP

ON-HAND: <u>4</u>

ITEM: EPINEPHRINE INJ 1:1000 1ML (AMPUL)

ON-HAND: <u>2</u>

ITEM: GLUCAGON INJ 1MG

ON-HAND: <u>2</u>

ITEM: HEPARIN 1,000 UNIT/ML 10ML INJ

ON-HAND: <u>5</u>

ITEM: LIDOCAINE 1% INJ 30ML

ON-HAND: <u>2</u>

ITEM: SODIUM BICARBONATE 50ML SYR 8.4%

ON-HAND: <u>4</u>

•

•

•

*\[This report has been abbreviated to save space.\]*

Select Production Menu Option: <u>\<RET\></u>5.0 Pick List<span id="_Toc511400147" class="anchor"></span> (132 column); \[PSGW INVENTORY PICK LIST\]

This option is accessible only if the “MERGE INV. SHEET AND PICK LIST” site parameter is set to “NO”.

If you are conducting an actual physical count of the stock in an AOU, and entering the on hand amounts into the computer, the pick list indicates the quantities to dispense. If an item requires no action for this inventory (amount to be dispensed is zero), the item does not appear on the pick list.

The pick list consists of two parts. The first part prints in the same format as the inventory sheet. The report prints item name, stock level, the on hand amount, amount on backorder, and the amount to be dispensed. The “TO BE DISPENSED” amount is automatically computed when the on hand amount is entered. There is also a column to record the amount dispensed if it is less than the “TO BE DISPENSED” amount (i.e., to be dispensed amount is 25, but the supply is low, and you are only able to dispense 10). If an item is a controlled substance, a line is printed on the pick list which may be used for the receiving person’s signature. The AR/WS package determines that an item is a controlled substance if the code in the DEA, SPECIAL HDLG field of the DRUG file (#50) contains an “A”.

The second part of the pick list is used by the pharmacy to pick the items. The list sorts on the INPATIENT PHARMACY LOCATION field (which is a field in the DRUG file), and then sorts on item name within pharmacy location. INPATIENT PHARMACY LOCATION is a location code similar to the Item Location Codes which identify where items are stored in the Area of Use; however, this location identifies where the item is located within inpatient pharmacy storage. You could use VA FileMan to enter the INPATIENT PHARMACY LOCATION values for AR/WS items if you wish. You may elect to have part two of the pick list print with: 1) a total for each item on the pick list, or 2) sub-totals for each item within each AOU, with an item total. This second part of the pick list prints item name, quantity to be dispensed, and a column to record the actual quantity picked. This column is for information only.

You may queue the pick list to print at a later time. The right margin for this report is 132.

Example 1: Pick List with Print total for each item on pharmacy pick list

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment\]

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>PICK</u> List (132 column)

SELECT DATE/TIME FOR INVENTORY: <u>66</u> 7-13-1993@07:47:00 SMITH,J.D. THU

MED ROOM 1 (ONLY)

Print total for each item on pharmacy pick list? Y// <u>\<RET\></u>

Right margin for this printout is 132!

DEVICE: *\[queue report here or send to designated device\]*

report follows

WARD STOCK PICK LIST FOR JUL 13,1993@07:47 INVENTORY \# 66 AUG 18,1993 PAGE 1

GROUP: MED ROOM 1 (ONLY)

INVENTORIED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ITEM STOCK QUICK ON BACKORDERED TO BE ACT DISPENSED

LEVEL CODE HAND DISPENSED IF \< TO BE

---------------------------------------------------------------------------------------------

MED ROOM 1

ACETONE 10 3 0 7 \_\_\_\_\_\_\_\_\_

BLEOMYCIN INJ 15 UNIT 3 1 0 2 \_\_\_\_\_\_\_\_\_

CUR CLEAN UTILITY ROOM

RA,S3

DEXTROSE 5% IN WATER 1000ML 12 D5W1 1 0 11 \_\_\_\_\_\_\_\_\_

MR MEDICINE ROOM

B2,S1

BUSULFAN TAB 2MG 10 5 0 5 \_\_\_\_\_\_\_\_\_

C1,C2

DISULFIRAM TAB 250MG 2 1 0 1 \_\_\_\_\_\_\_\_\_

CA,S1

CLOTRIMAZOLE 1% CREAM 4 CLT1 0 0 4 \_\_\_\_\_\_\_\_\_

HYDROCORTISONE 1% CREAM 30GM 4 HC1 3 0 7 \_\_\_\_\_\_\_\_\_

CA,S2

DOMOL BATH & SHOWER OIL 8 DML 1 0 3 \_\_\_\_\_\_\_\_\_

HYDROGEN PEROXIDE SOLN 480ML 2 HP 2 0 6 \_\_\_\_\_\_\_\_\_

CA,S3

CHLORAMBUCIL TAB 2MG 5 1 0 1 \_\_\_\_\_\_\_\_\_

CC,S1

ATROPINE SULFATE INJ 0.4MG/ML,20ML 3 AT20 1 0 4 \_\_\_\_\_\_\_\_\_

DEXTROSE 50% 50ML SYRINGE 5 D5DSY 1 0 2 \_\_\_\_\_\_\_\_\_

HEPARIN 1,000 UNIT/ML 10ML INJ 12 H1000 1 0 4 \_\_\_\_\_\_\_\_\_

LIDOCAINE 1% INJ 30ML 3 LID1 5 0 7 \_\_\_\_\_\_\_\_\_

CC,S4

PSYLLIUM HYDROPHILIC MUCILLOID 14O 2 PHM 1 0 1 \_\_\_\_\_\_\_\_\_

REF,S2

GLYCERIN SUPPOSITORIES 12'S 1 GLSUP 1 0 1 \_\_\_\_\_\_\_\_\_

WARD STOCK PHARMACY PICK LIST FOR JUL 13,1993@07:47 INVENTORY \# 66 AUG 18,1993 PAGE 2

GROUP: MED ROOM 1 (ONLY)

ITEM TO BE QUANTITY

DISPENSED PICKED

---------------------------------------------------------------------------------------------

ACETONE 7 \_\_\_\_\_\_

ATROPINE SULFATE INJ 0.4MG/ML,20ML 2 \_\_\_\_\_\_

BLEOMYCIN INJ 15 UNIT 2 \_\_\_\_\_\_

BUSULFAN TAB 2MG 5 \_\_\_\_\_\_

CHLORAMBUCIL TAB 2MG 4 \_\_\_\_\_\_

CLOTRIMAZOLE 1% CREAM 4 \_\_\_\_\_\_

DEXTROSE 5% IN WATER 1000ML 11 \_\_\_\_\_\_

DEXTROSE 50% 50ML SYRINGE 4 \_\_\_\_\_\_

DISULFIRAM TAB 250MG 1 \_\_\_\_\_\_

DOMOL BATH & SHOWER OIL 6 \_\_\_\_\_\_

GLYCERIN SUPPOSITORIES 12'S 1 \_\_\_\_\_\_

HEPARIN 1,000 UNIT/ML 10ML INJ 7 \_\_\_\_\_\_

HYDROCORTISONE 1% CREAM 30GM 3 \_\_\_\_\_\_

HYDROGEN PEROXIDE SOLN 480ML 1 \_\_\_\_\_\_

LIDOCAINE 1% INJ 30ML 1 \_\_\_\_\_\_

PSYLLIUM HYDROPHILIC MUCILLOID 14OZ 1 \_\_\_\_\_\_

Example 2: Pick List (132 column) with Print sub-total for each item by AOU

Select PHARMACY INPATIENT MENU option: <u>AUTOM</u>atic Replenishment

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>PICK</u> List (132 column)

SELECT DATE/TIME FOR INVENTORY: <u>66</u> 7-13-1993@07:47:00 SMITH,J.D. THU

MED ROOM 1 (ONLY)

Print total for each item on pharmacy pick list? Y// <u>N</u>

Print sub-total for each item by AOU? Y// <u>\<RET\></u>

Right margin for this printout is 132!

DEVICE: *\[queue report here or send to designated device\]*

report follows

WARD STOCK PICK LIST FOR JUL 13,1993@07:47 INVENTORY \# 66 AUG 18,1993 PAGE 1

GROUP: MED ROOM 1 (ONLY)

INVENTORIED BY \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ITEM STOCK QUICK ON BACKORDERED TO BE ACT DISPENSED

LEVEL CODE HAND DISPENSED IF \< TO BE

---------------------------------------------------------------------------------------------

MED ROOM 1

ACETONE 10 3 0 7 \_\_\_\_\_\_\_\_\_

BLEOMYCIN INJ 15 UNIT 3 1 0 2 \_\_\_\_\_\_\_\_\_

CUR CLEAN UTILITY ROOM

RA,S3

DEXTROSE 5% IN WATER 1000ML 12 D5W1 1 0 11 \_\_\_\_\_\_\_\_\_

MR MEDICINE ROOM

B2,S1

BUSULFAN TAB 2MG 10 5 0 5 \_\_\_\_\_\_\_\_\_

C1,C2

DISULFIRAM TAB 250MG 2 1 0 1 \_\_\_\_\_\_\_\_\_

CA,S1

CLOTRIMAZOLE 1% CREAM 4 CLT1 0 0 4 \_\_\_\_\_\_\_\_\_

HYDROCORTISONE 1% CREAM 30GM 4 HC1 3 0 7 \_\_\_\_\_\_\_\_\_

CA,S2

DOMOL BATH & SHOWER OIL 8 DML 1 0 3 \_\_\_\_\_\_\_\_\_

HYDROGEN PEROXIDE SOLN 480ML 2 HP 2 0 6 \_\_\_\_\_\_\_\_\_

CA,S3

CHLORAMBUCIL TAB 2MG 5 1 0 1 \_\_\_\_\_\_\_\_\_

CC,S1

ATROPINE SULFATE INJ 0.4MG/ML,20ML 3 AT20 1 0 4 \_\_\_\_\_\_\_\_\_

DEXTROSE 50% 50ML SYRINGE 5 D5DSY 1 0 2 \_\_\_\_\_\_\_\_\_

HEPARIN 1,000 UNIT/ML 10ML INJ 12 H1000 1 0 4 \_\_\_\_\_\_\_\_\_

LIDOCAINE 1% INJ 30ML 3 LID1 5 0 7 \_\_\_\_\_\_\_\_\_

CC,S4

PSYLLIUM HYDROPHILIC MUCILLOID 14O 2 PHM 1 0 1 \_\_\_\_\_\_\_\_\_

REF,S2

GLYCERIN SUPPOSITORIES 12'S 1 GLSUP 1 0 1 \_\_\_\_\_\_\_\_\_

WARD STOCK PHARMACY PICK LIST FOR JUL 13,1993@07:47 INVENTORY \# 66 AUG 18,1993 PAGE 2

GROUP: MED ROOM 1 (ONLY)

ITEM TO BE QUANTITY

DISPENSED PICKED

---------------------------------------------------------------------------------------------

ACETONE MED ROOM 1 7

-------------------------

TOTAL 7 \_\_\_\_\_\_

ATROPINE SULFATE INJ 0.4MG/ML,20ML MED ROOM 1 2

-------------------------

TOTAL 2 \_\_\_\_\_\_

BLEOMYCIN INJ 15 UNIT MED ROOM 1 2

-------------------------

TOTAL 2 \_\_\_\_\_\_

BUSULFAN TAB 2MG MED ROOM 1 5

-------------------------

TOTAL 5 \_\_\_\_\_\_

CHLORAMBUCIL TAB 2MG MED ROOM 1 4

-------------------------

TOTAL 4 \_\_\_\_\_\_

CLOTRIMAZOLE 1% CREAM MED ROOM 1 4

-------------------------

TOTAL 4 \_\_\_\_\_\_

DEXTROSE 5% IN WATER 1000ML MED ROOM 1 11

-------------------------

TOTAL 11 \_\_\_\_\_\_

DEXTROSE 50% 50ML SYRINGE MED ROOM 1 4

-------------------------

TOTAL 4 \_\_\_\_\_\_

DISULFIRAM TAB 250MG MED ROOM 1 1

-------------------------

TOTAL 1 \_\_\_\_\_\_

DOMOL BATH & SHOWER OIL MED ROOM 1 6

-------------------------

TOTAL 6 \_\_\_\_\_\_

GLYCERIN SUPPOSITORIES 12'S MED ROOM 1 1

-------------------------

TOTAL 1 \_\_\_\_\_\_

HEPARIN 1,000 UNIT/ML 10ML INJ MED ROOM 1 7

-------------------------

TOTAL \_\_\_\_\_\_

HYDROCORTISONE 1% CREAM 30GM MED ROOM 1 3

-------------------------

TOTAL 3 \_\_\_\_\_\_

HYDROGEN PEROXIDE SOLN 480ML MED ROOM 1 1

-------------------------

TOTAL 1 \_\_\_\_\_\_

LIDOCAINE 1% INJ 30ML MED ROOM 1 1

-------------------------

TOTAL 1 \_\_\_\_\_\_

PSYLLIUM HYDROPHILIC MUCILLOID 14OZ MED ROOM 1 1

-------------------------

TOTAL 1 \_\_\_\_\_\_

6.0 Enter/Edit Quantity Dispensed<span id="_Toc511400148" class="anchor"></span> ; \[PSGW INVENTORY DISPENSE\]

If you are conducting an actual “physical” count of the AOU stock, entering on hands into the computer, and printing a pick list to pick the dispense quantities, you will only use this option to edit the dispense quantities. The quantity dispensed should only be edited if the actual amount dispensed was less than the “TO BE DISPENSED” amount. The difference between the actual amount dispensed and the “TO BE DISPENSED” amount is the total amount that should be on backorder. If the MERGE INV. SHEET AND PICK LIST site parameter is set to “NO”, the computer computes the backorder amount for you and creates an entry in the BACKORDER file.

On the other hand, if you have the “MERGE INV. SHEET AND PICK LIST” answered “YES”, you will use this option to input *all* quantities dispensed. Also, since on hand quantities are not entered by this method, the computer is unable to calculate backorders and you must enter backorders using the *Enter Backorders* option.

In this option, you will be prompted for dispensed quantity in the same order as the items appear on the inventory sheet. You may enter an up-arrow (^) and an item name or “^” and the quick code for the item at the “DISPENSE QUANTITY:” prompt to jump to another item. If you enter only “^” at the “DISPENSE QUANTITY” prompt, you will jump to another AOU if there is more than one AOU on the inventory sheet.

An inventory may only be edited within a time limitation of 100 days. There is a background task which runs in the system every night. All inventory sheet data which is over 100 days old is deleted and may no longer be edited.

You will notice that it takes a little while to enter the quantity dispensed. The system must store the quantity dispensed, as before. Additionally, the quantity dispensed must be entered into the AMIS statistics, and enough data must be retained to be able to recalculate the AMIS if necessary.

Example: Enter/Edit Quantity Dispensed

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>ENTER</u>/Edit Quantity Dispensed

SELECT DATE/TIME FOR INVENTORY: <u>67</u> 7-14-1993@07:58 SMITH,J.D. FRI

FIRST FLOOR (M-W-F)

Select AREA OF USE: MED ROOM 2// <u>\<RET\></u>

ITEM: SODIUM CHLORIDE 0.9% LVP 1000ML

DISPENSE QUANTITY: <u>10</u>

<u>  
</u>ITEM: DEXTROSE 5% IN WATER,1000ML

DISPENSE QUANTITY: <u>20</u>

ITEM: SODIUM CHLORIDE 0.9% IRRIGATION,1000ML

DISPENSE QUANTITY: <u>16</u>

ITEM: NEOSPORIN OINTMENT 30GM

DISPENSE QUANTITY: <u>5</u>

ITEM: AMPICILLIN SOD. 1GM S.P.

DISPENSE QUANTITY: <u>3</u>

ITEM: DIGOXIN 0.5MG/2ML S.S.

DISPENSE QUANTITY: <u>4</u>

ITEM: CEFAZOLIN SOD 1GM S.P.

DISPENSE QUANTITY: <u>5</u>

ITEM: STREPTOMYCIN SULFATE 1GM S.S.

DISPENSE QUANTITY: <u>3</u>

ITEM: ACETAMINOPHEN 120MG/5ML EL (16OZ BT)

DISPENSE QUANTITY: <u>2</u>

ITEM: PHM/DEXTROSE (14OZ CAN)

DISPENSE QUANTITY: <u>2</u>

ITEM: ARTIFICIAL TEARS (15ML)

DISPENSE QUANTITY: <u>5</u>

ITEM: PROPINE 0.1% OPH SOLN (10ML)

DISPENSE QUANTITY: <u>2</u>

ITEM: DARVON-N SUSP

DISPENSE QUANTITY: <u>1</u>

ITEM: PHENYTOIN 125MG/5ML SUSPENSION (8OZ)

DISPENSE QUANTITY: <u>3</u>

ITEM: DEXTROSTIX REAGENT STRIPS (25/BTL)

DISPENSE QUANTITY: <u>1</u>

ITEM: GRANULEX SPRAY (4OZ)

DISPENSE QUANTITY: <u>5</u>

ITEM: BENZOIN TINCTURE USP, COMPOUND (4OZ BT)

DISPENSE QUANTITY: <u>2</u>

ITEM: AMYL NITRITE INHALANT AMPULE

DISPENSE QUANTITY: <u>18</u>

ITEM: PROCHLORPERAZINE 25MG SUPPOS.

DISPENSE QUANTITY: <u>20</u>

ITEM: ANUSOL SUPPOSITORIES

DISPENSE QUANTITY: <u>12</u>

Select AREA OF USE: CARDIAC CATH LAB// <u>\<RET\></u>

ITEM: DEXTROSE 5% IN WATER,1000ML

DISPENSE QUANTITY: <u>12</u>

ITEM: STERILE WATER FOR IRRIGATION,1000ML BT

DISPENSE QUANTITY: <u>10</u>

ITEM: SODIUM CHLORIDE 0.9% IRRIGATION,1000ML

DISPENSE QUANTITY: <u>30</u>

ITEM: BECLOMETHASONE ORAL INHALER

DISPENSE QUANTITY: <u>2</u>

ITEM: BENZOCAINE OINTMENT 20% (1OZ)

DISPENSE QUANTITY: <u>1</u>

ITEM: LACTULOSE SYRUP (16OZ BT)

DISPENSE QUANTITY: <u>1</u>

ITEM: POTASSIUM CHLORIDE 20MEQ PKT

DISPENSE QUANTITY: <u>65</u>

ITEM: KETO-DIASTIX STRIPS (100'S)

DISPENSE QUANTITY: <u>^ HYDROCORTISONE</u> 1% CREAM (OZ)

ITEM: HYDROCORTISONE 1% CREAM (OZ)

DISPENSE QUANTITY: <u>2</u>

ITEM: GLUCAGON 1MG S.P.

DISPENSE QUANTITY: <u>6</u>

ITEM: KAOLIN AND PECTIN SUSPENSION (16OZ BT)

DISPENSE QUANTITY: <u>4</u>

ITEM: MILK OF MAGNESIA SUSP (16OZ BT)

DISPENSE QUANTITY: <u>2</u>

ITEM: AFRIN NASAL SPRAY (15ML)

DISPENSE QUANTITY: <u>2</u>

ITEM: ATROPINE 1MG/10ML SYRINGE (BRISTOJECT)

DISPENSE QUANTITY: <u>4</u>

ITEM: DIAZEPAM 5MG/ML 2ML S.S.

DISPENSE QUANTITY: <u>25</u>

•

•

•

*\[This report has been abbreviated to save space.\]*

Select Production Menu Option: <u>\<RET\></u>7.0 On-Demand Requests<span id="_Toc511400149" class="anchor"></span>; \[PSGW ON-DEMAND\]

The *On-Demand Requests* menu gives access to all on-demand options. There are currently three sub options on this menu. They include

> *Enter/Edit On-Demand Request (80 column)*

> *Delete an On-Demand Request*

> *Print an On-Demand Report by Date/AOU (80 column)*

Additionally, there is a *Enter/Edit Nurses’ On-Demand Request* option which is on the AR/WS Nurses’ menu. The basic difference between the *Nurses’ On-Demand Request* option and the Pharmacy version is that the Nurses’ version does not allow an on-demand request for items that are not regularly stocked items. Thus, the AOU stock list cannot be altered with the Nurses’ option. If this option is given to the nursing staff, then some agreement must be made. 1) If you choose, Nursing may enter their on-demand requests, print the report at their station, and send the paper copy to pharmacy to be filled. Using this method, you are assured that the request printed. 2) Or, Nursing may enter the on-demand requests, and at the “DEVICE:” prompt, enter a printer number for a device in the pharmacy. Someone in pharmacy would have to be responsible for removing the requests, picking the items, and distributing them to the proper Area of Use. The drawback with this approach is that the printer could be off-line, out of paper, etc., and Nursing would not know that Pharmacy did not get the request. Or alternately, 3) you may establish a scheduled time that someone in pharmacy prints the report, picks the requested items, and sends them to the AOUs. Nursing and Pharmacy must both know what time this will take place to avoid re-ordering items that were previously requested. Also, any requests for non-standard stock items from Nursing would still have to come to the pharmacy via current methods.

> **NOTE:** Items dispensed through the on-demand options are counted as Ward Stock on the AMIS Report, not as Automatic Replenishment.

7.1 Enter/Edit On-Demand Request <span id="_Toc511400150" class="anchor"></span>(80 column); \[PSGW ON-DEMAND EDIT\]

An on-demand request is the non-scheduled distribution of an item to an AOU. For AMIS purposes, an on-demand is reported in a different category than Automatic Replenishment, which is more labor intensive. On-demand requests should generally be for unique items; if regular stock items are frequently requested, then perhaps the stock levels need to be adjusted.

Since the AOU stock list can be altered with this option, it is suggested that this option remain in the pharmacy. There is an on-demand request option available for Nursing which does not allow the user to add new items to the stock list. However, on-demand requests for non-standard stock items would still have to be sent to the pharmacy in the same manner that is currently used, i.e., phone or form.

To use this option, you must enter a date/time for the on-demand request. If you will answer “NOW”, a unique request is created which does not conflict with other requests, and your printout will include only those items you have requested. If you answer “TODAY”, then the request is batched with all other requests for today, and the printout shows all requests placed today, regardless of who entered the request. Future dates are *not* permitted.

Additionally, you will be asked for the Area of Use, and the item being requested. If the item requested is on backorder, the backorder total is displayed, and you will be asked if you wish to continue. If the item requested is not a standard stocked item in the AOU, you will be asked if you are adding the drug as a new item to the AOU. If you answer “YES”, the item will automatically be treated as a “one-time” request and will be added to the stock list with “today” as the inactivation date. Thus the item will not show up on the List Stock Items report, or the Inventory Sheet or Pick List. Finally, you will be asked to enter the quantity to be dispensed.

The following “truth-table” concerning the allowable selection of drugs for on-demands is used for this option:

If Item in: Pharmacy AOU Stock file (#58.1) Drug file (#50) User Action

--------------------------------------------------------------------------------------------------

does not exist INACTIVE may not select

(Only for Phar.) does not exist ACTIVE may select

ACTIVE ACTIVE may select

(Only for Phar.) INACTIVE ACTIVE may select

ACTIVE INACTIVE may select \*

INACTIVE INACTIVE may not select

\*This selection is allowed because some sites have stated that they may continue to stock an item for a time after it has been inactivated in the DRUG file.

After the on-demand request is entered, you may print a copy of the request just entered. The report shows the date of the request, Areas of Use, name of person entering the request, item name, expiration date, backorders, and quantity dispensed. If the item requested is a standard stock item, it will be flagged as such. The right margin for this report is 80.

Example: Enter/Edit On-Demand Request (80 column)

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>ON</u>-Demand Requests

Select On-Demand Requests Option: <u>ENTER</u>/Edit On-Demand Request (80 column)

SELECT DATE/TIME FOR ON-DEMAND REQUEST: <u>N</u> (AUG 08, 1993@09:05)

Select AOU: <u>DENTAL</u> CLINIC

Select ITEM: <u>HIBICLENS SOLN</u> (GALLON)

ARE YOU ADDING 'HIBICLENS SOLN (GALLON)' AS A NEW ITEM? <u>Y</u> (YES)

ON-DEMAND QUANTITY DISPENSED: <u>2</u>

Select ITEM: <u>MASSAGE LOTION (8OZ</u> BT)

ARE YOU ADDING 'MASSAGE LOTION (8OZ BT)' AS A NEW ITEM? <u>Y</u> (YES)

ON-DEMAND QUANTITY DISPENSED: <u>6</u>

Select ITEM: <u>\<RET\></u>

Select AOU: <u>\<RET\></u>

SELECT DATE/TIME FOR ON-DEMAND REQUEST: <u>\<RET\></u>

Do you wish to print a copy of this on-demand request ? N// <u>YES</u>

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>DENTAL CLINIC</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

The right margin for this report is 80 columns.

You may queue the report to print at a late time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

ON DEMAND REQUEST LIST BY DATE DATE: AUG 8,1993 PAGE: 1

REQUEST DATE: AUG 8,1993

BACK-

ITEM DT/TIME ORDERED QTY ORDER

------------------------------------------------------------------------------

==\> AREA OF USE: DENTAL CLINIC

ENTERED BY: SMITH,J.D.

Next Item LAST EDITED BY: CLINE,S.B. on AUG 8,1993@10:00

HIBICLENS SOLN. (GALLLON) AUG 8,1993@09:05 2 \*Std. Stock

Expiration Date: FEB 1993

MASSAGE LOTION (8OZ BT) AUG 8,1993@09:05 6 1 Std. Stock

7.2 Delete an On-Demand Request<span id="_Toc511400151" class="anchor"></span>; \[PSGW ON-DEMAND DELETE\]

This option allows you to delete an on-demand request. You may delete either a single item on the request, or you may delete all items on the request (i.e., the whole request). This option should be used when an on-demand request is canceled because the item is no longer needed, i.e., patient for whom item was requested has been discharged, etc.

When you use this option, the quantity dispensed for the item(s) is subtracted from the total quantity dispensed on the AMIS report. Therefore, if the item(s) has been dispensed, you should not use this option because it affects AMIS. The correct way to deal with a request which has been dispensed is to enter it into the system as a return. It will then show up correctly on AMIS as having been dispensed and returned.

To use this option, you will be asked for the request date/time. You must then answer the question, “Do you wish to delete all items on this on-demand request?”. If you answer “YES”, then all items on the request will be deleted. If you answer “NO”, then you will be asked for the Area of Use and the item to be removed. Again, realize that answering “YES” will cause the entire request to be deleted.

Example: Delete an On-Demand Request

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>ON</u>-Demand Requests

Select On-Demand Requests Option: <u>DELETE</u> an On-Demand Request

SELECT DATE/TIME FOR ON-DEMAND REQUEST: <u>T@0608</u> (JUN 08, 1993@09:08)

Do you wish to delete ALL items on this on-demand request? N// <u>?</u>

Answer "Y" or "N". If yes, the program will loop thru all items which were requested on the date/time selected and delete the request. If no, the user will be asked for the AOU and the item will be removed.

Do you wish to delete ALL items on this on-demand request? N// <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>DENTAL</u> CLINIC

Select ITEM: <u>PEN-V POTASSIUM 250MG C.T</u>. MR,CC,S2

DENTAL CLINIC PEN-V POTASSIUM 250MG C.T. On-demand request deleted

Select ITEM: <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

Select On-Demand Requests Option: <u>\<RET\></u>7.3 Print an On-Demand Report by Date/AOU<span id="_Toc511400152" class="anchor"></span> (80 column);

\[PSGW ON-DEMAND PRINT\]

The on-demand report shows the on-demand requests within a selected date range, and for one, several, or all Areas of Use. The report prints items and quantity to be dispensed, as well as the name of the person who entered the request. If the item requested is a standard stock item, it will be flagged as <span id="MaxStockExpl2" class="anchor"></span>such. The maximum ward stock level for the item is displayed on the second line, but only if the system-level parameter PSGW_WS_LVL_ON is set to ON by a user with the PSGWMGR security key. To set this parameter, select the "AR/WS Package-wide Parameter Edit" option from the "Set Up AR/WS (Build Files)" \[PSGW SETUP\] menu. At the "WARD STOCK LEVEL:" prompt, enter “Y” to turn the maximum ward stock display option ON. This option might be useful for tracking and analyzing on-demand requests. The right margin for this report is 80.

Example: Print an On-Demand Report by Date/AOU (80 column)

Select INPATIENT PHARMACY MENU option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>ON</u>-Demand Requests

Select On-Demand Requests Option: <u>PR</u>int an On-Demand Report by Date/AOU (80 column)

BEGINNING date for report: <u>6 1 93</u> (JUN 06, 1993)

ENDING date for report: <u>6 8 93</u> (JUN 08, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>^ALL</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to a designated device\]*

report follows

ON DEMAND REQUEST LIST BY DATE DATE: JUN 30,1993 PAGE: 1

REQUEST DATE: JUN 6,1993

BACK-

ITEM DT/TIME ORDERED QTY ORDER

------------------------------------------------------------------------------

==\> AREA OF USE: DRUG CLOSET

ENTERED BY: SMITH,J.D.

HEPARIN 1,000 UNIT/ML 10ML INJ JUN 6,1993@09:03 1 \*Std. Stock

Expiration Date: NOV 1993 STOCK LEVEL: 10

ACETAMINOPHEN 325MG/COD 30MG TAB JUN 6,1993@09:05 1 \*Std. Stock

Expiration Date: FEB 1993 STOCK LEVEL: 30

ON DEMAND REQUEST LIST BY DATE DATE: JUN 30,1993 PAGE: 2

REQUEST DATE: JUN 8,1993

BACK-

ITEM DT/TIME ORDERED QTY ORDER

------------------------------------------------------------------------------

==\> AREA OF USE: MED ROOM 1

ENTERED BY: SMITH,J.D.

BUSULFAN TAB 2MG JUN 8,1993@11:08 1 \*Std. Stock

STOCK LEVEL: 10

MILK OF MAGNESIA 480ML JUN 8,1993@11:09 1 \*Std. Stock

STOCK LEVEL: 5

BUSULFAN TAB 2MG JUN 8,1993@12:54 1 \*Std. Stock

STOCK LEVEL: 20

CASTOR OIL 60ML U.D. JUN 8,1993@13:07 1 \*Std. Stock

STOCK LEVEL: 10

SODIUM BICARBONATE 50ML SYR 8.4% JUN 8,1993@13:07 2 \*Std. Stock

STOCK LEVEL: 10

ON DEMAND REQUEST LIST BY DATE DATE: JUN 30,1993 PAGE: 3

REQUEST DATE: JUN 8,1993

BACK-

ITEM DT/TIME ORDERED QTY ORDER

------------------------------------------------------------------------------

==\> AREA OF USE: DRUG CLOSET

ENTERED BY: SMITH,J.D.

HEPARIN 1,000 UNIT/ML 10ML INJ JUN 8,1993@10:19 1 \*Std. Stock

Expiration Date: NOV 1991 <span id="StdStockScreen3" class="anchor"></span>STOCK LEVEL: 20

HEPARIN 1,000 UNIT/ML 10ML INJ JUN 8,1993@10:44 1 \*Std. Stock

Expiration Date: NOV 1991 STOCK LEVEL: 20

ACETAMINOPHEN 325MG/COD 30MG TAB JUN 8,1993@11:01 1 \*Std. Stock

Expiration Date: FEB 1993 STOCK LEVEL: 30

ACETAMINOPHEN 325MG/COD 30MG TAB JUN 8,1993@12:54 1 \*Std. Stock

Expiration Date: FEB 1993 STOCK LEVEL: 30

8.0 Backorder Requests<span id="_Toc511400153" class="anchor"></span> ; \[PSGW BACKORDER\]

This option allows access to the backorder options. There are currently six backorder sub options. They are

> *Enter Backorders*

> *Fill Requests for Backorder Items*

> *AOU Backorder Report (80 column)*

> *Current (ALL) Backorder Report (80 column)*

> *Single Item Report (80 column)*

> *Multiple Items Report (80 column)*

If the MERGE INV. SHEET AND PICK LIST site parameter is set to “NO”, then you are conducting an actual physical count of the AOU stock, entering on hands into the computer, and printing a pick list to determine quantity to be dispensed. If the amount actually dispensed is less than the “TO BE DISPENSED” amount, then the difference is automatically entered into the BACKORDER file for you.

However, if the MERGE INV. SHEET AND PICK LIST Site Parameter is set to “YES”, then you must enter Backorders yourself using the *Enter Backorders* option. This is because the computer does not have on hand quantities needed to calculate the backorder quantity.

The amount to be backordered is calculated in the following way: IF AMOUNT ACTUALLY DISPENSED IS LESS THAN AMOUNT TO BE DISPENSED, THEN BACKORDER = AMOUNT TO BE DISPENSED - AMOUNT ACTUALLY DISPENSED.

8.1 Enter Backorders<span id="_Toc511400154" class="anchor"></span>; \[PSGW BACKORDER IN\]

This option should be used when the MERGE INV. SHEET AND PICK LIST site parameter is set to “YES”. The option is used to create an entry in the BACKORDER file (#58.3). Data must be entered into the following fields to make an entry in the PHARMACY BACKORDER file:

> ITEM:

> Enter the name of the drug or item being backordered.

> AOU:

> Enter the name of the Area of Use for which the item has been backordered.

> DATE/TIME FOR BACKORDER:

> Enter the date/time or an N (now) for the item being backordered.

> CURRENT BACKORDER:

> Enter the quantity to be backordered.

If an item, AOU, or date/time for backorder is entered in error, you may delete the entry by using the “@” (shift 2). You *must* answer all questions when entering a backorder or the backorder will be deleted.

Example: Enter Backorders

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>BACK</u>order Requests

Select Backorder Requests Option: <u>ENTER</u> Backorders

Example: Showing “complete” order

Select PHARMACY BACKORDER ITEM: <u>BENZOCAINE OINTMENT</u> 20% (1OZ)

ARE YOU ADDING 'BENZOCAINE OINTMENT 20% (1OZ)' AS A NEW PHARMACY BACKORDER (THE NTH)? <u>Y</u> (YES)

Select AOU: <u>MED ROOM 1</u>

Select DATE/TIME FOR BACKORDER: <u>N</u> AUG 9, 1993@08:31

ARE YOU ADDING 'AUG 9, 1993@08:31' AS

A NEW DATE/TIME FOR BACKORDER (THE NTH FOR THIS AOU)? <u>Y</u> (YES)

CURRENT BACKORDER: <u>2</u>

Select DATE/TIME FOR BACKORDER: <u>\<RET\></u>

Select AOU: <u>MED ROOM 3</u>

...OK? YES// <u>\<RET\></u> (YES)

Select DATE/TIME FOR INVENTORY: <u>N</u> AUG 9, 1993@08:31

ARE YOU ADDING 'AUG 9, 1993@08:31' AS

A NEW DATE/TIME FOR BACKORDER (THE NTH FOR THIS AOU)? <u>Y</u> (YES)

CURRENT BACKORDER: <u>2</u>Example: Missing CURRENT BACKORDER amount

Select PHARMACY BACKORDER ITEM: <u>HYDROCORTISONE 1% CREAM</u> (OZ)

ARE YOU ADDING 'HYDROCORTISONE 1% CREAM (OZ) ' AS A NEW PHARMACY BACKORDER (THE NTH)? <u>Y</u> (YES)

Select AOU: <u>MED ROOM 1</u>

Select DATE/TIME FOR BACKORDER: <u>N</u> AUG 7,1993@08:02

ARE YOU ADDING 'AUG 7,1993@08:02' AS

A NEW DATE/TIME FOR BACKORDER (THE NTH FOR THIS AOU)? <u>Y</u> (YES)

CURRENT BACKORDER: <u>\<RET\></u>

Missing CURRENT BACKORDER data, deleting BACKORDER entry...

Example: Missing data for a new Backorder Item

Select PHARMACY BACKORDER ITEM: <u>CEFAZOLIN SOD 1GM S.P.</u>

ARE YOU ADDING 'CEFAZOLIN SOD 1GM S.P.' AS A NEW PHARMACY

BACKORDER (THE NTH)? <u>Y</u> (YES)

Select AOU: <u>MED ROOM 2</u>

Select DATE/TIME FOR BACKORDER: <u>N</u> AUG 7,1993@08:58

ARE YOU ADDING 'AUG 7,1993@08:02' AS

A NEW DATE/TIME FOR BACKORDER (THE NTH FOR THIS AOU)? <u>Y</u> (YES)

CURRENT BACKORDER: <u>^</u>

Missing CURRENT BACKORDER data, deleting BACKORDER entry...

Select DATE/TIME FOR BACKORDER: <u>\<RET\></u>

Missing DATE/TIME FOR BACKORDER data, deleting MED ROOM 2 entry...

Select AOU: <u>\<RET\></u>

Missing MED ROOM data, deleting PHARMACY BACKORDER ITEM entry...

Select PHARMACY BACKORDER ITEM: <u>\<RET\></u>

Select Backorder Requests Option: <u>\<RET\></u>8.2 Fill Requests for Backorder Items<span id="_Toc511400155" class="anchor"></span> ; \[PSGW BACKORDER EDIT\]

Once the backorder shipment arrives, the backorder entry in File 58.3 needs to be marked as filled. There are two methods of doing this.

> 1\) If the item is immediately dispensed to the AOU for which it was backordered, use this option to mark the backorder request as filled. To do this, you must enter the item name, Area of Use, backorder date/ time (enter “?” to see the selectable dates), and the date filled. You will not be able to manually enter a partial fill.

> 2\) If the item is not sent to the AOU until the next regular inventory, there is no need to use this option. The computer will automatically mark the backorder as filled when the quantity dispensed values are input on the next inventory. By this method, the computer will automatically record a partial fill and adjust the backorder balance when you enter the quantity dispensed through the regular *Enter/Edit Quantity Dispensed* option.

Example: Fill Requests for Backorder Items

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>BACK</u>order Requests

Select Backorder Requests Option: <u>FILL</u> Requests for Backorder Items

Select PHARMACY BACKORDER ITEM: <u>BACITRACIN</u> OINTMENT (1OZ)

Select AOU: <u>MED ROOM 1</u>

Select DATE/TIME FOR BACKORDER: <u>6-2@0942</u> 6-2-1993 09:42

DATE FILLED: <u>T</u> (AUG 8,1993)

Select Backorder Requests Option: <u>\<RET\></u>8.3 AOU Backorder Report (80 column)<span id="_Toc511400156" class="anchor"></span>; \[PSGW BACKORDER AOU PRINT\]

This option prints all backordered items by Area of Use. The sort order is Area of Use, item, and backorder date.

In previous versions of AR/WS when the *Purge Dispensing Data* option was used to delete obsolete data in the files, any inventory for which there was an outstanding backorder would not be purged. This connection is no longer true as backorders are no longer tied to inventory dates, however, you may wish to use this *AOU Backorder Report (80 column)* option to determine if there are any “forgotten” backorders in the file. The file may contain, for example, a backorder entry which has not been marked as filled after an extensive time lapse.

Example: AOU Backorder Report (80 column)

Select INPATIENT PHARMACY Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>BACK</u>order Requests

Select Backorder Requests Option: <u>AOU BACK</u>order Report (80 column)

This option will print a list of Current Backorders for selected AOU(s).

You will only be allowed to choose AOUs that have Backorder entries (current

or non-current) in the Pharmacy Backorder file (#58.3).

Select AOU: <u>CARDIAC CATH LAB</u>

Select AOU: <u>DENTAL CLINIC</u>

Select AOU: <u>\<RET\></u>

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

PHARMACY AOU BACKORDER LIST PAGE: 1

PRINTED: AUG 10,1993@13:25

=\> AOU

ITEM DATE/TIME FOR CURRENT

LOCATION BACKORDER BACKORDER

------------------------------------------------------------------------------

=\> CARDIAC CATH LAB

ACETAMINOPHEN TAB 325MG JAN 28,1993@09:32 5

MR,CC,S4

DEXTROSE 50% 50ML SYRINGE FEB 17,1993@13:18 8

MR,CC,S1

DIGOXIN TAB 0.125MG MAR 9,1993@09:55 4

MR6,S4,D1

GLUCAGON INJ 1MG FEB 17,1993@13:18 5

UNKNOWN

PHARMACY AOU BACKORDER LIST PAGE: 2

PRINTED: AUG 10,1993@13:25

=\> AOU

ITEM DATE/TIME FOR CURRENT

LOCATION BACKORDER BACKORDER

------------------------------------------------------------------------------

=\> DENTAL CLINIC

DEXTROSE 50% 50ML SYRINGE JAN 28,1993@09:32 6

UNKNOWN

DIGOXIN TAB 0.125MG MAR 9,1993@09:55 2

MR9,S2,D3

EPINEPHRINE 1:10,000 SYRINGE FEB 17,1993@13:18 5

UNKNOWN

8.4 Current (ALL) Backorder Report (80 column) ;<span id="_Toc511400157" class="anchor"></span>

\[PSGW BACKORDER (ALL) PRINT\]

This option prints a list of ALL Current (i.e., unfilled) Backorders. You may choose to sort this report by Area of Use or by Item.

Example 1: Current (ALL) Backorder Report (80 COLUMN) Sorted by AOU

Select INPATIENT PHARMACY Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>BACK</u>order Requests

Select Backorder Requests Option: <u>CURR</u>ent (ALL) Backorder Report (80 column)

This option will print a list of ALL Current Backorders.

Do you want to sort by (A)rea of Use or by (I)tem? <u>A</u>

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

PHARMACY BACKORDER LIST BY AOU PAGE: 1

PRINTED: AUG 10,1993@13:28

=\> AOU

ITEM DATE/TIME FOR CURRENT

LOCATION BACKORDER BACKORDER

------------------------------------------------------------------------------

=\> CARDIAC CATH LAB

ACETAMINOPHEN TAB 325MG JAN 28,1993@09:32 5

MR,CC,S4

DEXTROSE 50% 50ML SYRINGE FEB 17,1993@13:18 8

MR,CC,S1

DIGOXIN TAB 0.125MG MAR 9,1993@09:55 4

MR6,S4,D1

GLUCAGON INJ 1MG FEB 17,1993@13:18 5

UNKNOWN

=\> DENTAL CLINIC

DEXTROSE 50% 50ML SYRINGE JAN 28,1993@09:32 6

UNKNOWN

DIGOXIN TAB 0.125MG MAR 9,1993@09:55 2

MR9,S2,D3

EPINEPHRINE 1:10,000 SYRINGE FEB 17,1993@13:18 5

UNKNOWN

=\> MED ROOM 3 \*\*

DIGOXIN TAB 0.125MG MAR 9,1993@09:55 3

MR3,S5,D2

\*\* Indicates an Inactive AOU

Example 2: Current (ALL) Backorder Report (80 COLUMN) Sorted by ITEM

Select INPATIENT PHARMACY Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>BACK</u>order Requests

Select Backorder Requests Option: <u>CURR</u>ent (ALL) Backorder Report (80 column)

This option will print a list of ALL Current Backorders.

Do you want to sort by (A)rea of Use or by (I)tem? <u>I</u>

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

PHARMACY BACKORDER LIST BY ITEM PAGE: 1

PRINTED: AUG 10,1993@13:40

=\> ITEM

DATE/TIME FOR CURRENT

AOU LOCATION BACKORDER BACKORDER

------------------------------------------------------------------------------

=\> ACETAMINOPHEN TAB 325MG

CARDIAC CATH LAB MR,CC,S4 JAN 28,1993@09:32 5

-------

TOTAL: 5

=\> DEXTROSE 50% 50ML SYRINGE

CARDIAC CATH LAB MR,CC,S1 FEB 17,1993@13:18 8

DENTAL CLINIC UNKNOWN JAN 28,1993@09:32 6

-------

TOTAL: 14

=\> DIGOXIN TAB 0.125MG

CARDIAC CATH LAB MR6,S4,D1 MAR 9,1993@09:55 4

DENTAL CLINIC MR9,S2,D3 MAR 9,1993@09:55 2

MED ROOM 3 \*\* MR3,S5,D2 MAR 9,1993@09:55 3

-------

TOTAL: 9

=\> EPINEPHRINE 1:10,000 SYRINGE

DENTAL CLINIC UNKNOWN FEB 17,1993@13:18 5

-------

TOTAL: 5

=\> GLUCAGON INJ 1MG

CARDIAC CATH LAB UNKNOWN FEB 17,1993@13:18 5

-------

TOTAL: 5

\*\* Indicates an Inactive AOU

  
8.5 Single Item Report (80 column)<span id="_Toc511400158" class="anchor"></span>; \[PSGW BACKORDER ITEM PRINT\]

This option prints a list of all backorders for a specific item. For the item, each Area of Use with a backorder is shown with the date of the backorder and the amount backordered for that AOU. Also, the total backorder for the item is listed.

Example: Single Item Report (80 column)

Select INPATIENT PHARMACY Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>BACK</u>order Requests

Select Backorder Requests Option: <u>SIN</u>gle Item Report (80 column)

Select PHARMACY BACKORDER ITEM: <u>DIGOXIN TAB</u> 0.125MG

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to a designated device\]*

report follows

PHARMACY SINGLE ITEM BACKORDER LIST PAGE: 1

PRINTED: AUG 10,1993@13:45

=\> ITEM

DATE/TIME FOR CURRENT

AOU LOCATION BACKORDER BACKORDER

------------------------------------------------------------------------------

=\> DIGOXIN TAB 0.125MG

CARDIAC CATH LAB MR6,S4,D1 MAR 9,1993@09:55 4

DENTAL CLINIC MR9,S2,D3 MAR 9,1993@09:55 2

MED ROOM 3 \*\* MR3,S5,D2 MAR 9,1993@09:55 3

-------

TOTAL: 9

\*\* Indicates an Inactive AOU

8.6 Multiple Items Report (80 column)<span id="_Toc511400159" class="anchor"></span> ; \[PSGW BACKORDER ITEMS PRINT\]

For all items that you select, this option prints a report of backorders for those items. For each of the items selected, the AOU is shown with the date of the backorder and the amount backordered for that AOU. The total backorder for the item is also listed. The right margin for this report is 80.

Example: Multiple Items Report (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>BACK</u>order Requests

Select Backorder Requests Option: <u>MUL</u>tiple Items Report (80 column)

Select PHARMACY BACKORDER ITEM: <u>DIGOXIN TAB 0.125MG</u>

Select PHARMACY BACKORDER ITEM: <u>ACETAMINOPHEN TAB 325MG</u>

Select PHARMACY BACKORDER ITEM: <u>EPINEPHRINE 1:10,000 SYRINGE</u>

Select PHARMACY BACKORDER ITEM: <u>HETASTARCH INJ 6% 500ML</u>

Select PHARMACY BACKORDER ITEM: <u>HEPARIN 1,000 UNIT/ML 10ML INJ</u>

Select PHARMACY BACKORDER ITEM: <u>DEXTROSE 50% 50ML SYRINGE</u>

Select PHARMACY BACKORDER ITEM: <u>GLUCAGON INJ 1MG</u>

Select PHARMACY BACKORDER ITEM: <u>\<RET\></u>

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to a designated device\]*

report follows

PHARMACY MULTIPLE ITEMS BACKORDER LIST PAGE: 1

PRINTED: AUG 10,1993@13:49

=\> ITEM

DATE/TIME FOR CURRENT

AOU LOCATION BACKORDER BACKORDER

------------------------------------------------------------------------------

=\> ACETAMINOPHEN TAB 325MG

CARDIAC CATH LAB MR,CC,S4 JAN 28,1993@09:32 5

-------

TOTAL: 5

=\> DEXTROSE 50% 50ML SYRINGE

CARDIAC CATH LAB MR,CC,S1 FEB 17,1993@13:18 8

DENTAL CLINIC UNKNOWN JAN 28,1993@09:32 6

-------

TOTAL: 14

=\> DIGOXIN TAB 0.125MG

CARDIAC CATH LAB MR6,S4,D1 MAR 9,1993@09:55 4

DENTAL CLINIC MR9,S2,D3 MAR 9,1993@09:55 2

MED ROOM 3 \*\* MR3,S5,D2 MAR 9,1993@09:55 3

-------

TOTAL: 9

=\> EPINEPHRINE 1:10,000 SYRINGE

DENTAL CLINIC UNKNOWN FEB 17,1993@13:18 5

-------

TOTAL: 5

=\> GLUCAGON INJ 1MG

CARDIAC CATH LAB UNKNOWN FEB 17,1993@13:18 5

-------

TOTAL: 5

=\> HEPARIN 1,000 UNIT/ML 10ML INJ \<NO CURRENT BACKORDERS\>

=\> HETASTARCH INJ 6% 500ML \<NO CURRENT BACKORDERS\>

\*\* Indicates an Inactive AOU

9.0 Return Items for AOU<span id="_Toc511400160" class="anchor"></span>; \[PSGW RETURN ITEMS\]

This option is used to record items returned from an Area of Use. Return quantity will be reflected on the AMIS report, and on all usage and cost reports.

To return an item, you must enter the Area of Use, item name, date of return, return quantity, and return reason or reasons. Return reasons include expired, overstocked, deleted item, and change in stock level.

If an unreasonable volume of returns occur for an AOU, then the stock levels for that AOU should probably be adjusted. Use the Returns Analysis Report to make this determination, thereby minimizing returns.

Example: Return Items for AOU

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>RETURN</u> Items for AOU

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select ITEM: <u>POTASSIUM CHLO</u>RIDE 20MEQ PKT MR,CA,S3

Select RETURNS DATE OF RETURN: <u>T</u> AUG 9, 1993

ARE YOU ADDING 'AUG 9, 1993' AS A NEW RETURNS (THE 1ST FOR THIS ITEM)? <u>Y</u> (YES)

RETURN QUANTITY: <u>12</u>

RETURN REASON: <u>?</u>

CHOOSE FROM:

E EXPIRED

O OVER STOCK

D DELETED ITEM

C CHANGE IN STOCK LEVEL

RETURN REASON: <u>E</u> EXPIRED

ARE YOU ADDING 'EXPIRED' AS A NEW RETURN REASON (THE 1ST FOR THIS RETURNED

ITEM)? <u>Y</u> (YES)

RETURN REASON: <u>\<RET\></u>

Select ITEM: <u>HEXACHLOROPHENE 3% DET</u>ERGENT LOTION,5OZ MR,CE,S2

Select RETURNS DATE OF RETURN: <u>T</u> AUG 9, 1993

ARE YOU ADDING 'AUG 9, 1993' AS A NEW RETURNS (THE 1ST FOR THIS ITEM)? <u>Y</u> (YES)

RETURN QUANTITY: <u>7</u>

RETURN REASON: <u>O</u> OVER STOCK

ARE YOU ADDING 'OVER STOCK' AS A NEW RETURN REASON (THE 1ST FOR THIS RETURNED

ITEM)? <u>Y</u> (YES)

RETURN REASON: <u>O</u> OVER STOCK

ARE YOU ADDING 'CHANGE IN STOCK LEVEL' AS A NEW RETURN REASON (THE 2ND FOR THIS RETURNED ITEM)? <u>Y</u> (YES)

RETURN REASON: <u>\<RET\></u>

Select ITEM: <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>10.0 Crash Cart Menu<span id="_Toc511400161" class="anchor"></span>; \[PSGW CRASH CART MENU\]

This menu contains the crash cart options for production. With the options on this menu the user can enter new crash cart locations, edit locations, or print a report listing all AOUs with Crash Carts and their locations.

> *Enter/Edit Crash Cart Locations*

> *Print Crash Cart Locations*10.1 Enter/Edit Crash Cart Locations<span id="_Toc511400162" class="anchor"></span>; \[PSGW CRASH CART LOCATION EDIT\]

This option will allow users to enter or edit the LOCATION field for AOUs that are flagged as Crash Carts.

Example: Enter/Edit Crash Cart Locations

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>C</u>rash Cart Menu

Select Crash Cart Menu Option: <u>E</u>nter/Edit Crash Cart Locations

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>OPERATING ROOM</u>

CRASH CART LOCATION: <u>OPERATING ROOM 3</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>CICU</u>

CRASH CART LOCATION: 1 NORTH// <u>\<RET\></u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

Select Crash Cart Menu Option: <u>\<RET\></u>10.2 Print Crash Cart Locations<span id="_Toc511400163" class="anchor"></span> ; \[PSGW CRASH CART LOCATION PRINT\]

This option will print an 80 column report listing all AOUs that are flagged as Crash Carts with their locations.

Example: Print Crash Cart Locations

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>C</u>rash Cart Menu

Select Crash Cart Menu Option: <u>P</u>rint Crash Cart Locations

This option will list crash carts and their locations.

Right margin for this report is 80 columns.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

CRASH CART LOCATION LIST PAGE: 1

PRINTED: JUN 21,1993

CRASH CART LOCATION

------------------------------------------------------------------------------

OPERATING ROOM OPERATING ROOM 3

CICU 1 NORTH

11.0 Auto Replenishment Reports<span id="_Toc511400164" class="anchor"></span> ; \[PSGW REPORTS\]

This menu gives access to various report options for Automatic Replenishment/Ward Stock.

There are currently nine sub options on the *Auto Replenishment Reports* menu.

> *List Stock Items (132 column)*

> *Expiration Date Report (80 column)*

> *Inventory Outline (80 column)*

> *Ward/AOU List for an Item (80 column)*

> *Item Activity Inquiry (80 column)*

> *Percentage Stock On Hand (132 column)*

> *Returns Analysis Report (80 column)*

> *Usage Report for an Item (80 column)*

> *Zero Usage Report (80 column)*

All reports in this module may be queued to print at a later time. Each report includes in the “title” the right margin needed for the successful printing of the report.

In order to queue a report, at the “DEVICE:” prompt, enter a “Q”. You will then be asked, “QUEUE TO PRINT ON DEVICE:”. Enter the device number of the printer to which you wish to send the report. The next prompt is: “REQUESTED START TIME: NOW//”. Enter the time that you wish for the report to begin.

11.1 List Stock Items (132 column)<span id="_Toc511400165" class="anchor"></span>; \[PSGW PRINT AOU STOCK\]

This option allows you to print the items entered as active stock for an Area of Use in PHARMACY AOU STOCK file (#58.1). The report prints all items currently available for inventory, by AOU and will display the following information:

> 1\. Item TYPE (for the report sorted by TYPE/LOCATION/ITEM)

> 2\. Current Stock Level

> 3\. Current Reorder Level

> 4\. Current Minimum Quantity to Dispense

> 5\. Expiration Date

The report may be printed for a single AOU, several AOUs, or you may enter “^ALL” to print the report for all Areas of Use. Also, the report may be printed by two different sort order methods. You may print the stock list in order by type, and within type, by location. An alternate method is to print the stock list in alphabetical order.

Example 1: List Stock Items (132 column) By TYPE/LOCATION/ITEM

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>LIST STOCK</u> Items (132 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

You may print by either of these sorting methods:

\(1\) By TYPE/LOCATION/ITEM

\(2\) Alphabetical by ITEM

Select SORT ORDER for report (enter 1 or 2): <u>1</u>

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

AOU STOCK LIST BY TYPE/LOCATION - DATE: JUN 10,1993 PAGE: 1

AREA OF USE

TYPE MINIMUM QTY EXPIRATION

LOCATION ITEM STOCK LEVEL REORDER LEVEL TO DISPENSE DATE

---------------------------------------------------------------------------------------------

==\> MED ROOM 1

TYPE: EXTERNALS

MR,CA,S1 BACITRACIN OINTMENT 1OZ 3 1 2 DEC 02,1993

MR,CA,S1 CLOTRIMAZOLE 1% CREAM 4 1 2 DEC 02,1993

MR,CA,S1 HYDROCORTISONE 1% CREAM 30G 4 2 2 AUG 13,1993

MR,CA,S2 DOMOL BATH & SHOWER OIL 8 2 6 DEC 02,1993

MR,CA,S2 HEXACHLOROPHENE DET. 5OZ 6 1 6 NOT LISTED

MR,CA,S2 HYDROGEN PEROXIDE SOLN 480ML 2 1 1 NOV 05,1993

MR,CA,S2 ISOPROPYL ALCOHOL 70% 480ML 6 1 6 DEC 02,1993

MR,CD,S3 BENZOIN COMP TINCT 1 NOT LISTED NOT LISTED

NOT LISTED ACETONE 10 5 5 DEC 02,1993

TYPE: ORAL LIQUID

MR,CC,S2 ACETAMINOPHEN 500MG/15CC ELIX 2 1 1 DEC 02,1993

MR,CC,S2 CASTOR OIL 60ML U.D. 2 1 1 SEP 25,1993

MR,CC,S2 MILK OF MAGNESIA 480ML 4 2 2

MR,CC,S3 ALUM.& MAG. HYDROXIDE GEL 6 2 6 NOT LISTED

MR,CC,S3 KAOLIN AND PECTIN SUSP 360ML 2 1 1

MR,CC,S3 MAGNESIUM CITRATE SOLN 300ML 3 1 3

TYPE: ORAL SOLID

MR,B2,S1 BUSULFAN TAB 2MG 10 5 5

MR,CA,S3 CHLORAMBUCIL TAB 2MG 5 1 3 DEC 02,1993

MR,CC,S4 ACETAMINOPHEN TAB 325MG 50 10 25

MR1,S1,D2 DIGOXIN TAB 0.125MG 2 NOT LISTED NOT LISTED

TYPE: INJECTION

MR,CC,S1 DEXTROSE 50% 50ML SYRINGE 5 1 4

MR,CC,S1 DIAZEPAM 5MG/ML 2ML AMP 10 2 6 SEP 10,1993

MR,CC,S1 GLUCAGON INJ 1MG 3 1 2 DEC 02,1993

MR,CC,S1 LIDOCAINE 1% INJ 30ML 3 2 1

TYPE: OPHTHALMIC, OTIC

MR,CA,S4 TIMOLOL 0.25% OP.SOL. 10ML 3 1 2 NOT LISTED

TYPE: SUPPOSITORY

MR,REF,S2 ACETAMINOPHEN SUPP 650MG 12 1 6 NOT LISTED

MR,REF,S2 ASPIRIN SUPP 650MG 12 1 6 NOT LISTED

MR,REF,S2 GLYCERIN SUPPOSITORIES 12'S 2 1 1

TYPE: CONTROLLED DRUG (II)

MR,CC,S1 DIAZEPAM 5MG/ML 2ML AMP 10 4 6 SEP 10,1993

TYPE: REAGENT/TEST ITEM

MR,CB,S1 KETO-DIASTIX 100'S 2 1 1

Example 2: List Stock Items (132 column) Alphabetical by ITEM

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>LIST STOCK</u> Items (132 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

You may print by either of these sorting methods:

\(1\) By TYPE/LOCATION/ITEM

\(2\) Alphabetical by ITEM

Select SORT ORDER for report (enter 1 or 2): <u>2</u>

The right margin for this report is 132.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

ALPHABETICAL LISTING OF AOU STOCK - DATE: AUG 10,1993 PAGE: 1

AREA OF USE

TYPE MINIMUM QTY EXPIRATION

ITEM LOCATION STOCK LEVEL REORDER LEVEL TO DISPENSE DATE

---------------------------------------------------------------------------------------------------------------------

==\> MED ROOM 1

ACETAMINOPHEN 500MG/15CC ELIX. MR,CC,S2 2 1 1 DEC 02,1993

ACETAMINOPHEN SUPP 650MG MR,REF,S2 12 1 6 DNOT LISTED

ACETAMINOPHEN TAB 325MG MR,CC,S4 50 10 25 DEC 02,1993

ACETONE NOT LISTED 10 5 5 DEC 02,1993

ALUM.& MAG. HYDROXIDE GEL MR,CC,S3 6 2 6 DEC 02,1993

ASPIRIN SUPP 650MG MR,REF,S2 12 1 6 NOT LISTED

ATROPINE SULFATE INJ 0.4MG/ML,20ML MR,CC,S1 3 2 1

BACITRACIN OINTMENT 1OZ MR,CA,S1 3 1 2 DEC 02,1993

BECLOMETHASONE ORAL.INHALER 16.8GM MR,CC,S5 6 1 5

BENZOIN COMP TINC MR,CD,S3 1 NOT LISTED NOT LISTED

BLEOMYCIN INJ 15 UNIT NOT LISTED 3 1 2

BUSULFAN TAB 2M MR,B2,S1 10 5 5

CASTOR OIL 60ML U.D. MR,CC,S2 2 1 1 SEP 25,1993

CHLORAMBUCIL TAB 2MG MR,CA,S3 5 1 3 DEC 02,1993

CLOTRIMAZOLE 1% CREAM MR,CA,S1 4 1 2 DEC 02,1993

DEXTROSE 50% 50ML SYRINGE MR,CC,S1 5 1 4

DIAZEPAM 5MG/ML 2ML AMP MR,CC,S1 10 2 6 SEP 10,1993

DIGOXIN TAB 0.125MG MR1,S1,D2 2 NOT LISTED NOT LISTED

DISULFIRAM TAB 250MG MR,C1,C2 2 1 1 DEC 02,1993

DOMOL BATH & SHOWER OIL MR,CA,S2 8 2 6

EPINEPHRINE INJ 1:1000 1ML (AMPUL) MR,CC,S1 3 1 2

GLUCAGON INJ 1MG MR,CC,S1 3 1 2

GLYCERIN SUPPOSITORIES 12'S MR,REF,S2 2 1 1

HEPARIN 1,000 UNIT/ML 10ML INJ MR,CC,S1 12 6 6

HEXACHLOROPHENE DET. 5OZ MR,CA,S2 6 1 6 NOT LISTED

HYDROCORTISONE 1% CREAM 30GM MR,CA,S1 4 2 2 AUG 13,1993

HYDROGEN PEROXIDE SOLN 480ML MR,CA,S2 2 1 1 NOV 05,1993

ISOPROPYL ALCOHOL 70% 480ML MR,CA,S2 6 1 6 DEC 02,1993

KAOLIN AND PECTIN SUSP 360ML MR,CC,S3 2 1 1

KETO-DIASTIX 100'S MR,CB,S1 2 1 1

LACTULOSE SYRUP 10GM/15ML 480ML MR,CC,S3 2 1 1

LIDOCAINE 1% INJ 30ML MR,CC,S1 3 2 1

MAGNESIUM CITRATE SOLN 300ML MR,CC,S3 3 1 3

MILK OF MAGNESIA 480ML MR,CC,S2 4 2 2

POTASSIUM CHLORIDE 20MEQ EFF. T. MR,CC,S4 30 10 20

PSYLLIUM HYDROPHILIC MUCILLOID 14OZ MR,CC,S4 2 NOT LISTED NOT LISTED

SODIUM BICARBONATE 50ML SYR 8.4% MR,CC,S1 5 1 4

SODIUM CHLORIDE 0.9% 1000ML IRRIGATION CUR,CB,S3 12 1

TIMOLOL 0.25% OP.SOL. 10ML MR,CA,S4 3 1 2 NOT LISTED

11.2 Expiration Date Report (80 column)<span id="_Toc511400166" class="anchor"></span>; \[PSGW EXP REPORT\]

This report will print a listing of the expiration dates for the items in an AOU for one, several, or ALL AOUs. If multiple AOUs are selected, the user may choose to sort the report by DATE/DRUG/AOU or by DATE/AOU/DRUG. If only one AOU is selected, the sort order is by DATE/DRUG.

Example 1: Expiration Date Report (80 column) of Multiple AOUs sorted by Date/Drug/AOU:

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>EXP</u>iration Date Report (80 column)

BEGINNING date for report: <u>T-100</u> (MAY 03, 1993)

ENDING date for report: <u>T</u> (NOV 19, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I'): <u>I</u>

Select AOU INVENTORY GROUP NAME: <u>DAY SHIFT</u>

This Inventory Group contains the following AOU(s):

\#1 MEDICATION ROOM

\#2 MEDICATION ROOM

\#3 MEDICATION ROOM

CRASH CART

Since you have chosen multiple AOUs,

please select a sort order for the report:

\(1\) Date/Drug/AOU or (2) Date/AOU/Drug

Enter '1' or '2' or "^" to Exit ==\> <u>1</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

DRUG EXPIRATION DATE REPORT PAGE 1

FOR PERIOD MAY 3,1993 TO NOV 19,1993

PRINTED AUG 11,1993@12:47

FOR INVENTORY GROUP - DAY SHIFT

=\> DATE

ITEM

AOU/(LOCATION)

------------------------------------------------------------------------------

=\> AUG 14,1993

MECLOFENAMATE SODIUM 100MG CAP

CRASH CART/(1 WEST)

=\> SEP 23,1993

MEPHOBARBITAL 50MG TAB

\#1 MEDICATION ROOM

=\> OCT 10,1993

DYPHYLLINE GG ELIXIR

\#2 MEDICATION ROOM

=\> OCT 14,1993

PENICILLIN G POTASSIUM 200000U TAB

\#1 MEDICATION ROOM

=\> OCT 30,1993

METOPROLOL TARTRATE 50MG TAB

\#2 MEDICATION ROOM

END OF REPORT! Press \<RETURN\> to return to Menu: <u>\<RET\></u>Example 2: Expiration Date Report (80 column) of Multiple AOUs sorted by Date/AOU/Drug

Select Auto Replenishment Reports Option: <u>EXP</u>iration Date Report (80 column)

BEGINNING date for report: <u>T-100</u> (MAY 03, 1993)

ENDING date for report: <u>T</u> (NOV 19, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I'): <u>I</u>

Select AOU INVENTORY GROUP NAME: <u>DAY SHIFT</u>

This Inventory Group contains the following AOU(s):

\#1 MEDICATION ROOM

\#2 MEDICATION ROOM

\#3 MEDICATION ROOM

CRASH CART

Since you have chosen multiple AOUs,

please select a sort order for the report:

\(1\) Date/Drug/AOU or (2) Date/AOU/Drug

Enter '1' or '2' or "^" to Exit ==\> <u>2</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

DRUG EXPIRATION DATE REPORT PAGE 1

FOR PERIOD MAY 3,1993 TO NOV 19,1993

PRINTED AUG 11,1993@12:47

FOR INVENTORY GROUP - DAY SHIFT

=\> DATE

AOU/(LOCATION)

ITEM

------------------------------------------------------------------------------

=\> AUG 14,1993

CRASH CART/(1 WEST)

MECLOFENAMATE SODIUM 100MG CAP

=\> SEP 23,1993

\#1 MEDICATION ROOM

MEPHOBARBITAL 50MG TAB

=\> OCT 10,1993

\#2 MEDICATION ROOM

DYPHYLLINE GG ELIXIR

=\> OCT 14,1993

\#1 MEDICATION ROOM

PENICILLIN G POTASSIUM 200000U TAB

=\> OCT 30,1993

\#2 MEDICATION ROOM

METOPROLOL TARTRATE 50MG TAB

END OF REPORT! Press \<RETURN\> to return to Menu: <u>\<RET\></u>Example 3: Expiration Date Report (80 column) of Single AOU sorted by Date/Drug

Select Auto Replenishment Reports Option: <u>EXP</u>iration Date Report (80 column)

BEGINNING date for report: <u>T-100</u> (MAY 03, 1993)

ENDING date for report: <u>T+100</u> (NOV 19, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I'): <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\#1 M</u>EDICATION ROOM

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

DRUG EXPIRATION DATE REPORT for \#1 MEDICATION ROOM PAGE 1

FOR PERIOD MAY 3,1993 TO NOV 19,1993

PRINTED AUG 11,1993@13:15

=\> DATE

ITEM

------------------------------------------------------------------------------

=\> MAY 1,1993

ACETAMINOPHEN TAB 325MG

MILK OF MAGNESIA 480ML

=\> JUN 13,1993

TIMOLOL 0.25% OP.SOL. 10ML

=\> SEP 23,1993

MEPHOBARBITAL 50MG TAB

=\> OCT 14,1993

PENICILLIN G POTASSIUM 200000U TAB

END OF REPORT! Press \<RETURN\> to return to Menu: <u>\<RET\></u>11.3 Inventory Outline (80 column)<span id="_Toc511400167" class="anchor"></span>; \[PSGW WARD INV PRINT\]

This report lists the principal information for inventories within a selected date range. The option sorts in AOU order, and within AOU, information is presented in chronological order by inventory date and time. The fields shown are AREA OF USE, DATE OF INVENTORY, DAY/WEEK INVENTORIED, INV. ID#, RESPONSIBLE PERSON, and TYPES INVENTORIED. The report might be useful to show all inventories done within a specified time frame, i.e., for a month.

Example: Inventory Outline (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>INVEN</u>tory Outline (80 column)

BEGINNING date for report: <u>6 1 93</u> (JUN 01, 1993)

ENDING date for report: <u>T</u> (AUG 10, 1993)

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

PHARMACY AREA OF USE INVENTORY LIST FROM JUN 1,1993 TO AUG 10,1993

PRINT DATE: AUG 10,1993@13:14 PAGE 1

==\> AREA OF USE

INVENTORY DATE/TIME DAY/WEEK INV. ID# RESPONSIBLE PERSON

TYPES INVENTORIED

------------------------------------------------------------------------------

==\> MED ROOM 1

JUL 13,1993@07:47 THU 66 SMITH,J.D.

ALL

==\> CARDIAC CATH LAB

JUN 9,1993@11:05 FRI 63 SMITH,J.D.

ALL

==\> DENTAL CLINIC

JUN 9,1993@11:05 FRI 63 SMITH,J.D.

EXTERNALS

INHALER

ORAL SOLID

SET

ALL

JUL 27,1993@07:39 THU 67 SMITH,J.D.

ALL

JUL 27,1993@08:03 THU 68 SMITH,J.D.

ALL

==\> DRUG CLOSET

JUN 9,1993@11:05 FRI 63 SMITH,J.D.

CONTROLLED DRUG (II)

JUN 28,1993@08:08 WED 64 SMITH,J.D.

ALL

JUL 13,1993@07:39 THU 65 SMITH,J.D.

CONTROLLED DRUG (II)

JUL 27,1993@07:39 THU 67 SMITH,J.D.

ALL

JUL 27,1993@08:03 THU 68 SMITH,J.D.

ALL

11.4 Ward/AOU List for an Item (80 column)<span id="_Toc511400168" class="anchor"></span>; \[PSGW LOOKUP ITEM\]

This option is used primarily to locate the wards and Areas of Use that stock a selected item. After you enter the name of the item, the report prints out the name of the ward, Area of Use, location, and stock level of the item within the AOU. If an Area of Use stocks the item, but the AOU is not associated with a ward, e.g., cardiac cath lab, then these Areas will be printed at the top of the report. Afterward, those AOUs which have associated wards will be printed.

Example: Ward/AOU List for an Item (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>WARD/AOU</u> List for an Item (80 column)

Using this option, you may look up the wards and/or Areas of Use

which stock the item you select.

The right margin for this report is 80.

You may queue the report to print at a later time.

Select ITEM Name: <u>ACETAMINOPHEN 325MG/CODEINE 30MG TAB</u>

DEVICE: *\[queue report here or send to a designated device\]*

report follows

WARD/AOU LIST FOR AN ITEM DATE: JUN 10,1993

ITEM NAME

STOCK

WARD AREA OF USE LOCATION LEVEL

------------------------------------------------------------------------------

==\> ACETAMINOPHEN 325MG/CODEINE 30MG TAB

1 WEST MEDS \* MR,C2,S1 20

1 NORTH DRUG CLOSET MR,C2,S1 20

1 WEST DRUG CLOSET MR,C2,S1 20

\* Indicates AOU is currently Inactive

11.5 Item Activity Inquiry (80 column) <span id="_Toc511400169" class="anchor"></span>; \[PSGW ITEM INQUIRY\]

This option will display ALL activity (inventories, on-demands, and returns) for a specified item in a specified AOU for a specified date range. This option was primarily designed to be used as a tool to locate bad data input for an item that was ultimately reflected on some type of report. For example, a cost report for an AOU may show an unusually high quantity dispensed for an item. Previously, tracking down the exact transaction that was in error has been very time consuming.

Example: Item Activity Inquiry (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PR</u>oduction Menu

Select Production Menu Option: <u>AU</u>to Replenishment Reports

Select Auto Replenishment Reports Option: <u>ITE</u>m Activity Inquiry (80 column)

This option will list all activity for a specified item, in a specified,

area of use, for a specified date range.

BEGINNING date for report: <u>1 1 93</u> (JAN 01, 1993)

ENDING date for report: <u>T</u> (OCT 10, 1993)

Select AOU: <u>DRUG CLOSET</u>

Select ITEM: <u>HEPARIN 1,000 UNIT/ML 10ML INJ</u> MR,C1,S1

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

ITEM ACTIVITY INQUIRY for period JAN 1,1993 to JUN 10,1993 Page: 1

Printed OCT 10,1993@15:34

AOU : DRUG CLOSET

ITEM: HEPARIN 1,000 UNIT/ML 10ML INJ

------------------------------------------------------------------------------

INVENTORIES:

ID \# - DATE/TIME FOR INVENTORY QUANTITY DISPENSED

------------------------------------------------------------------

ID \#63 - FEB 9,1993@11:05 3

ID \#64 - FEB 28,1993@08:08 2

ID \#65 - MAY 13,1993@07:39 2

ID \#67 - MAY 27,1993@07:39 3

ID \#68 - MAY 27,1993@08:03 1

ID \#72 - JUN 9,1993@13:09 1

Press \<RETURN\> to Continue, "^" to Exit: <u>\<RET\></u>

ITEM ACTIVITY INQUIRY for period JAN 1,1993 to JUN 10,1993 Page: 2

Printed OCT 10,1993@15:34

AOU : DRUG CLOSET

ITEM: HEPARIN 1,000 UNIT/ML 10ML INJ

------------------------------------------------------------------------------

ON-DEMAND REQUESTS:

ON-DEMAND REQUEST DATE/TIME QUANTITY DISPENSED

------------------------------------------------------------------

MAY 26,1993@13:30 1

JUN 6,1993@09:03 1

JUN 7,1993@11:12 1

JUN 8,1993@10:19 1

JUN 8,1993@10:44 1

Press \<RETURN\> to Continue, "^" to Exit: <u>\<RET\></u>

ITEM ACTIVITY INQUIRY for period JAN 1,1993 to JUN 10,1993 Page: 3

Printed OCT 10,1993@15:34

AOU : DRUG CLOSET

ITEM: HEPARIN 1,000 UNIT/ML 10ML INJ

------------------------------------------------------------------------------

RETURNS:

RETURN DATE/TIME QUANTITY RETURNED

------------------------------------------------------------------

JUL 3,1993 2

11.6 Percentage Stock On Hand (132 column)<span id="_Toc511400170" class="anchor"></span>; \[PSGW STOCK PERCENTAGE\]

This option should be used only if you have the MERGE INV. SHEET AND PICK LIST site parameter set to “NO”.

This option is a VA FileMan print template on PHARMACY AOU STOCK file (#58.1). The report is shown in percentage order, beginning with the percentage that you enter for the “START WITH PERCENTAGE OF STOCK ON HAND: FIRST//” prompt. The “START WITH” and “GO TO” prompts refer to 0 (the lowest percentage) through the highest percentage currently available. Also, you select the date range for the report. The report extracts inventory data by percentage of stock on hand for a given inventory date range. The percentage is computed by dividing the on hand amount by the stock level and multiplying the results by 100. Therefore, if you are not entering on hand amounts, this report will not have the necessary data to produce accurate results.

This report allows you to list items which maintain a certain percentage of stock on the shelf in a specified time frame. Thus, you may determine over or under stocked items.

Example: Percentage Stock On Hand(132 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>PER</u>centage Stock On Hand (132 column)

START WITH PERCENTAGE OF STOCK ON HAND: FIRST// <u>1</u>

GO TO PERCENTAGE OF STOCK ON HAND: LAST// <u>100</u>

START WITH DATE(DATE/TIME FOR INVENTORY): FIRST// <u>MARCH 7,1993</u>

GO TO DATE(DATE/TIME FOR INVENTORY): LAST// <u>MARCH 8, 1993</u>

DEVICE: *\[queue report here or send to designated device\]*

report follows

PERCENTAGE OF STOCK ON HAND MAR 10,1993 12:58 PAGE 1

STOCK ON

HAND

STOCK DATE/TIME FOR

LEVEL INVENTORY ITEM AREA OF USE (AOU)

---------------------------------------------------------------------------------------------

13.33% 90 MAR 8, 1993 09:43 POTASSIUM CHLORIDE 20N=MEQ PKT MED ROOM 3

16.67% 24 MAR 8,1993 09:43 ASPIRIN 650MG SUPPOSITORIES MED ROOM 3

16.67% 6 MAR 7,1993 14:32 CEFAZOLIN SOD 1GM S.P. MED ROOM 2

16.67% 30 MAR 7,1993 14:32 DIAZEPAM 5MG/ML 2ML S.S. MED ROOM 3

16.67% 6 MAR 8,1993 09:43 PREDNISOLONE 1% OP.SOL. MED ROOM 3

16.67% 36 MAR 8,1993 09:43 SODIUM CHLORIDE 0.9% IRRIGATION,1000ML MED ROOM 3

20.00% 30 MAR 7,1993 14:32 DIAZEPAM 5MG/ML 2ML S.S. MED ROOM 1

20.00% 10 MAR 7,1993 14:32 HEPARIN 1,000 UNIT/ML S.S. (10ML) MED ROOM 1

20.00% 10 MAR 7,1993 14:32 HEPARIN 1,000 UNIT/ML S.S. (10ML) MED ROOM 3

20.00% 25 MAR 8,1993 09:43 MYLANTA II SUSP (OZ) MED ROOM 3

20.00% 15 MAR 8,1993 09:43 STERILE WATER FOR IRRIGATION,1000ML BT MED ROOM 3

22.22% 18 MAR 8,1993 09:43 DEXTROSE 5% IN WATER,1000ML MED ROOM 3

22.22% 18 MAR 8,1993 09:43 DOMOL BATH & SHOWER OIL (8OZ) MED ROOM 3

25.00% 4 MAR 7,1993 14:32 AMPICILLIN SOD. 1GM S.P. MED ROOM 2

25.00% 8 MAR 8,1993 09:43 HYDROCORTISONE 1% CREAM (OZ) MED ROOM 3

25.00% 4 MAR 8,1993 09:43 LIDOCAINE 2% INJ. 20ML. MED ROOM 3

26.67% 30 MAR 8,1993 09:43 DIAZEPAM 5MG/ML 2ML S.S. MED ROOM 3

30.00% 10 MAR 8,1993 09:43 HEPARIN 1,000 UNIT/ML S.S. (10ML) MED ROOM 3

33.33% 3 MAR 8,1993 09:43 BECLOMETHASONE ORAL INHALER MED ROOM 3

33.33% 6 MAR 8,1993 09:43 CLOTRIMAZOLE 1% CREAM MED ROOM 3

33.33% 6 MAR 7,1993 14:32 DIGOXIN 0.5MG/2ML S.S. MED ROOM 2

33.33% 6 MAR 8,1993 09:43 GENTAMICIN OPH SOLN (5ML) MED ROOM 3

33.33% 3 MAR 7,1993 14:32 GLUCAGON 1MG S.P. MED ROOM 1

33.33% 3 MAR 7,1993 14:32 GLUCAGON 1MG S.P. MED ROOM 3

33.33% 3 MAR 8,1993 09:43 GLUCAGON 1MG S.P. MED ROOM 3

33.33% 6 MAR 8,1993 09:43 ISOPROPYL ALCOHOL 70% (16OZ) MED ROOM 3

33.33% 3 MAR 8,1993 09:43 KAOLIN AND PECTIN SUSPENSION (16OZ BT) MED ROOM 3

38.89% 36 MAR 8,1993 09:43 ACETAMINOPHEN 650MG SUPPOS. MED ROOM 3

40.00% 5 MAR 7,1993 14:32 ATROPINE 1MG/10ML SYRINGE (BRISTOJECT) MED ROOM 1

40.00% 5 MAR 7,1993 14:32 ATROPINE 1MG/10ML SYRINGE (BRISTOJECT) MED ROOM 3

40.00% 5 MAR 8,1993 09:43 ATROPINE 1MG/10ML SYRINGE (BRISTOJECT) MED ROOM 3

48.00% 25 MAR 8,1993 09:43 HEXACHLOROPHENE 3% DETERGENT LOTION,5OZ MED ROOM 3

50.00% 24 MAR 8,1993 09:43 GLYCERIN SUPPOSITORIES MED ROOM 3

50.00% 4 MAR 8,1993 09:43 MILK OF MAGNESIA SUSP (16OZ BT) MED ROOM 3

100.00% 2 MAR 8,1993 09:43 AFRIN NASAL SPRAY (15ML) MED ROOM 3

100.00% 3 MAR 8,1993 09:43 BACITRACIN OINTMENT (1OZ) MED ROOM 3

100.00% 1 MAR 8,1993 09:43 SODIUM BICARBONATE POWDER (1 LB) MED ROOM 3

11.7 Returns Analysis Report (80 column)<span id="_Toc511400171" class="anchor"></span>; \[PSGW RETURNS BREAKDOWN\]

This report may be printed for any date range you wish, and it may be printed for a single Area of Use, several Areas of Use, or for ALL Areas. The purpose of the report is to show for the date range, drugs returned, return date(s), quantity returned, and return reason. This report will assist in reducing stock levels in AOUs with unreasonable amounts of returns, thereby minimizing returns in the future.

The right margin for this report is 80. You may queue the report to print at a later time.

Example: Returns Analysis Report (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>RET</u>urns Analysis Report (80 column)

BEGINNING date for report: <u>1 1 93</u> (JUN 01, 1993)

ENDING date for report: <u>T</u> (AUG 10, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 2</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>DRUG CLOSET</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

RETURNS BREAKDOWN REPORT FROM JUN 1,1993 TO AUG 10,1993 PAGE 1

AREA OF USE DATE: AUG 10,1993@13:16

RETURN QUANTITY RETURN

ITEM DATE RETURNED REASON

------------------------------------------------------------------------------

==\> MED ROOM 2

-------------

CODEINE SULFATE TAB 30MG

JUL 3,1993 2 OVER STOCK

DEL FR STOCK

RETURNS BREAKDOWN REPORT FROM JUN 1,1993 TO AUG 10,1993 PAGE 2

AREA OF USE DATE: AUG 10,1993@13:16

RETURN QUANTITY RETURN

ITEM DATE RETURNED REASON

------------------------------------------------------------------------------

==\> DRUG CLOSET

-------------

ACETAMINOPHEN 325MG/CODEINE 30MG TAB

JUL 3,1993 1 EXPIRED

-------------

HEPARIN 1,000 UNIT/ML 10ML INJ

JUL 3,1993 2 EXPIRED

-------------

HETASTARCH INJ 6% 500ML

AUG 10,1993 2 NOT LISTED

11.8 Usage Report for an Item (80 column) <span id="_Toc511400172" class="anchor"></span>; \[PSGW USAGE REPORT\]

The option prints a report detailing total quantity dispensed within a date range for (1) a single item for an AOU, (2) a single item for all AOUs, (3) all items for a single AOU, and (4) all items for all AOUs.

At the “Select PHARMACY AOU STOCK AREA OF USE (AOU):” prompt, enter the name of a single Area of Use, or enter “^ALL” to print the report for all Areas of Use. At the “Select ITEM:” prompt, enter the name of a single item, or enter “^ALL” to print the report for all items in the Area(s) of Use.

If you print the report for a single item, you will be shown the inventory dates and amounts dispensed (if applicable) for Automatic Replenishment, on-demands, and returns. A total is shown for the item for the date range.

The format is different if you print the report for all items. In this case, you will be shown the drugs in the Area of Use, and for each drug, the total quantity dispensed, the portion of the total that was Automatic Replenishment, on-demand, and returns for the date range.

In either case, if the total quantity dispensed for an item is zero, that item is not printed on the Usage Report. A message prints out indicating: “NO USAGE FOR ITEM FOR SELECTED DATES”. If you wish to get a list of items with no usage for a date range, use the *Zero Usage Report* option.

The right margin for this report is 80. You may queue the report to print at a later time.

Example 1: Single item for an AOU

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>USAGE</u> Report for an Item (80 column)

Usage Report may be printed for:

a single item for one AOU,

a single item for ALL AOUs,

ALL items for one AOU, or

ALL items for ALL AOUs.

To select all AOUs, enter "^ALL" at the

"Select PHARMACY AOU STOCK AREA OF USE (AOU):" prompt.

To select all items, enter "^ALL" at the "Select ITEM:" prompt.

BEGINNING date for report: <u>2-1</u> (FEB 01, 1993)

ENDING date for report: <u>2-29</u> (FEB 29, 1993)

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select ITEM: <u>DIAZEPAM 5MG/ML</u> 2ML S.S. MR,CC,S2

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

USAGE REPORT FROM FEB 1,1993 TO FEB 29,1993 PAGE 1

AREA OF USE DATE: MAR 10,1993@13:29

ITEM INVENTORY DATE DISPENSE QUANTITY

------------------------------------------------------------------------------

==\> MED ROOM 1

DIAZEPAM 5MG/ML 2ML S.S.

AUTO REPLENISHMENT

FEB 1,1993 30

FEB 3,1993 30

FEB 5,1993 15

FEB 8,1993 15

FEB 10,1993 20

FEB 12,1993 25

FEB 15,1993 20

FEB 17,1993 10

FEB 19,1993 15

FEB 22,1993 30

FEB 24,1993 15

FEB 26,1993 20

FEB 29,1993 25

-----

SUBTOTAL AUTO REPL. + 270

ON DEMAND

FEB 18,1993 10

-----

SUBTOTAL ON DEMAND + 10

RETURNS

FEB 27,1993 5

-----

SUBTOTAL RETURNS - 5

=======

TOTAL DISPENSED 275

END OF REPORT! Press \<RETURN\> to return to Menu: <u>\<RET\></u>Example 2: All items for an AOU

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>USAGE</u> Report for an Item (80 column)

Usage Report may be printed for:

a single item for one AOU,

a single item for ALL AOUs,

ALL items for one AOU, or

ALL items for ALL AOUs.

To select all AOUs, enter "^ALL" at the

"Select PHARMACY AOU STOCK AREA OF USE (AOU):" prompt.

To select all items, enter "^ALL" at the "Select ITEM:" prompt.

BEGINNING date for report: <u>2-1</u> (FEB 01, 1993)

ENDING date for report: <u>2-29</u> (FEB 29, 1993)

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select ITEM: <u>^ALL</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

USAGE REPORT FROM FEB 1,1993 TO FEB 29,1993 PAGE 1

AREA OF USE DATE: AUG 10,1993@13:28

ITEM DISPENSE QUANTITY

TOTAL AUTO REPL ON DEMAND RETURNS

------------------------------------------------------------------------------

==\> MED ROOM 1

ACETAMINOPHEN 650MG SUPPOS. 370 370 0 0

AFRIN NASAL SPRAY (15ML) 21 21 0 0

ALBUTEROL INHALER 1 0 1 0

ASPIRIN 650MG SUPPOSITORIES 247 253 0 6

ATROPINE 1MG/10ML SYR. (BRISTOJECT) 57 54 3 0

BACITRACIN OINTMENT (1OZ) 28 28 0 0

BECLOMETHASONE ORAL INHALER 29 28 1 0

BENZOCAINE OINTMENT 20% (1OZ) 19 19 0 0

CALCIUM CHLORIDE 10% 10ML BRISTOJECT 4 0 4 0

CIMETIDINE 300MG/5ML ORAL SOLN (8 OZ ) 4 0 4 0

CLOTRIMAZOLE 1% CREAM 61 61 0 0

DEXTROSE 5% IN NORMAL SALINE 1000ML 8 0 8 0

DEXTROSE 5% IN WATER,1000ML 174 174 0 0

DIAZEPAM 5MG/ML 2ML S.S. 275 270 10 5

DOMOL BATH & SHOWER OIL (8OZ) 176 176 0 0

FLUOCINONIDE 0.05% OINT. (60GM TUBE) 4 0 4 0

GENTAMICIN OPH SOLN (5ML) 62 58 4 0

GLUCAGON 1MG S.P. 32 30 2 0

GLYCERIN SUPPOSITORIES 263 263 0 0

HEPARIN 1,000 UNIT/ML S.S. (10ML) 110 105 5 0

HEXACHLOROPHENE 3% DET LOTION,5OZ 264 264 0 0

HYDROCORTISONE 1% CREAM (OZ) 76 76 0 0

ISOPROPYL ALCOHOL 70% (16OZ) 60 60 0 0

KAOLIN AND PECTIN SUSPENSION (16OZ BT) 28 28 0 0

KETO-DIASTIX STRIPS (100'S) 23 22 1 0

LACTULOSE SYRUP (16OZ BT) 22 20 2 0

LIDOCAINE 2% INJ. 20ML. 68 69 3 4

MILK OF MAGNESIA SUSP (16OZ BT) 37 37 0 0

MYLANTA II SUSP (5OZ) 242 254 0 12

PHENYTOIN 250MG SYRINGE 25 22 3 0

PILOCARPINE 4% OPHT.SOL. 3 0 3 0

POTASSIUM CHLORIDE 20MEQ PKT 785 785 0 0

PREDNISOLONE 1% OP.SOL. 57 57 0 0

SODIUM BICARBONATE POWDER (1 LB) 10 10 0 0

SODIUM CHLORIDE 0.9% IRR.,1000ML 351 351 0 0

STERILE WATER FOR IRR.,1000ML BT 146 146 0 0

VIDARABINE 3% OPH OINT (1/8OZ) 4 0 4 0

11.9 Zero Usage Report (80 column) <span id="_Toc511400173" class="anchor"></span>; \[PSGW ZERO USAGE\]

This report may be printed for a selected date range, and for a single Area of Use, several Areas of Use, or for all Areas. The report lists alphabetically those drugs for which there is no usage during the date range. For each drug the system checks for quantity dispensed by Automatic Replenishment or on-demand. It also subtracts returns for the item. Any item with zero usage or negative usage (because of returns), will be included on the report.

To the left of the drug name, you may see asterisks. For each asterisk printed, ninety days have passed from the date the item was last dispensed until the current date.

To the right of the drug name, you may see the date that the item was last dispensed. If returns were subtracted, then there will also be a message stating “INCLUDES RETURNS”. If there are no inventory dates in the file for the item, then the message, “NO DISPENSE DATES FOUND” will be printed.

Any item on this report may require further investigation. Use the *Usage Reportfor an Item* option to print detailed information for a single item in an Area of Use.

The right margin for the report is 80. You may queue the report to be printed at a later time.

Example: Zero Usage Report (80 column)

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Automatic Replenishment Option: <u>PROD</u>uction Menu

Select Production Menu Option: <u>AUTO</u> Replenishment Reports

Select Auto Replenishment Reports Option: <u>ZERO</u> Usage Report (80 column)

BEGINNING date for report: <u>1-1</u> (JAN 01, 1993)

ENDING date for report: <u>T</u> (AUG 10, 1993)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

ITEMS WITH ZERO USAGE FROM JAN 1,1993 TO AUG 10,1993 PAGE 1

AREA OF USE DATE: AUG 10,1993@13:18

NO USAGE FOR: DATE LAST DISPENSED:

------------------------------------------------------------------------------

==\> MED ROOM 1

ACETAMINOPHEN TAB 325MG NO DISPENSE DATES FOUND

ALUM.& MAG. HYDROXIDE GEL NO DISPENSE DATES FOUND

ATROPINE SULFATE INJ 0.4MG/ML,20ML NO DISPENSE DATES FOUND

BACITRACIN OINTMENT 1OZ NO DISPENSE DATES FOUND

BECLOMETHASONE ORAL.INHALER 16.8GM NO DISPENSE DATES FOUND

BENZOIN COMP TINCT NO DISPENSE DATES FOUND

BLEOMYCIN INJ 15 UNIT NO DISPENSE DATES FOUND

CHLORAMBUCIL TAB 2MG NO DISPENSE DATES FOUND

CLOTRIMAZOLE 1% CREAM NO DISPENSE DATES FOUND

DEXTROSE 5% IN WATER 1000ML NO DISPENSE DATES FOUND

DEXTROSE 50% 50ML SYRINGE NO DISPENSE DATES FOUND

DIAZEPAM 5MG/ML 2ML AMP NO DISPENSE DATES FOUND

DIGOXIN TAB 0.125MG NO DISPENSE DATES FOUND

DOMOL BATH & SHOWER OIL NO DISPENSE DATES FOUND

EPINEPHRINE INJ 1:1000 1ML (AMPUL) NO DISPENSE DATES FOUND

GLUCAGON INJ 1MG NO DISPENSE DATES FOUND

GLYCERIN SUPPOSITORIES 12'S NO DISPENSE DATES FOUND

HEPARIN 1,000 UNIT/ML 10ML INJ NO DISPENSE DATES FOUND

HEXACHLOROPHENE DET. 5OZ NO DISPENSE DATES FOUND

HYDROCORTISONE 1% CREAM 30GM NO DISPENSE DATES FOUND

HYDROGEN PEROXIDE SOLN 480ML NO DISPENSE DATES FOUND

ISOPROPYL ALCOHOL 70% 480ML NO DISPENSE DATES FOUND

KAOLIN AND PECTIN SUSP 360ML NO DISPENSE DATES FOUND

KETO-DIASTIX 100'S NO DISPENSE DATES FOUND

LACTULOSE SYRUP 10GM/15ML 480ML NO DISPENSE DATES FOUND

LIDOCAINE 1% INJ 30ML NO DISPENSE DATES FOUND

MAGNESIUM CITRATE SOLN 300ML NO DISPENSE DATES FOUND

MILK OF MAGNESIA 480ML NO DISPENSE DATES FOUND

POTASSIUM CHLORIDE 20MEQ EFF. T. NO DISPENSE DATES FOUND

PSYLLIUM HYDROPHILIC MUCILLOID 14OZ NO DISPENSE DATES FOUND

SODIUM CHLORIDE 0.9% 1000ML IRRIGATION NO DISPENSE DATES FOUND

TIMOLOL 0.25% OP.SOL. 10ML NO DISPENSE DATES FOUND

For each "\*" printed, 90 days have passed from

the date item was last dispensed to current date.

Auto Replenishment/Ward Stock Nurses’ Menu  
  
Chapter Three: Auto Replenishment/Ward Stock Nurses’ Menu<span id="_Toc511400174" class="anchor"></span>

Auto Replenishment/Ward Stock Nurses’ Menu \[PSGW RN\]

This option is the main menu driver for Automatic Replenishment/Ward Stock options used by nursing staff. There are currently three sub options on the menu. They include

> *Enter/Edit Nurses’ On-Demand Request (80 column)*

> *List Stock Items (132 column)*

> *Ward/AOU List for an Item (80 column)*Getting Out of an Option

To stop what you are doing, enter an up-arrow (^). You can use the up-arrow at any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering up-arrows to completely exit from the system.

1.0 Enter/Edit Nurses’ On-Demand Request (80 column) <span id="_Toc511400175" class="anchor"></span>;

\[PSGW ON-DEMAND NURSING EDIT\]

An on-demand request is the non-scheduled distribution of an item to an Area of Use. This option is designed for Nursing to enter requests into the computer. You may enter an on-demand request for any item that is on the stock list for the Area of Use. For items which are not on the stock list, the request must be sent to the pharmacy in the same manner that is currently used.

To use this option, you must enter a date/time for the on-demand request. The default answer for this prompt is “NOW”, and in most cases you should accept the default answer, future dates will not be permitted. Next, you should enter the name of the Area of Use for which the request is made. If you are unsure of the correct AOU, enter “?” for a listing of all Areas from which you may select. <span id="StockLvlAllowedText" class="anchor"></span>

When you enter an item, the maximum ward stock level allowed for that item displays, but only if the system-level parameter PSGW_WS_LVL_ON is set to ON by a user with the PSGWMGR security key. To set this parameter, select the "AR/WS Package-wide Parameter Edit" option from the "Set Up AR/WS (Build Files)" \[PSGW SETUP\] menu. At the "WARD STOCK LEVEL:" prompt, enter “Y” to turn the maximum ward stock display option ON. Taking into account the allowed stock level, enter the on-demand quantity.

If you select an item which is currently on backorder, you will be informed that the item is on backorder. You will not be able to enter a quantity for this item, as it is unavailable or “out of stock”. The following “truth-table” concerning the allowable selection of drugs for on-demands by nursing staff is used for this option.

If Item in: PHARMACY AOU DRUG file (#50) User Action

STOCK file (#58.1)

--------------------------------------------------------------------------------------------

does not exist INACTIVE may not select

does not exist ACTIVE may not select

ACTIVE ACTIVE may select

INACTIVE ACTIVE may not select

ACTIVE INACTIVE may select \*

INACTIVE INACTIVE may not select

\*This selection is allowed because some sites have stated that they may continue to stock an item for a time after it has been inactivated in the DRUG file.

After the on-demand request is entered, you may print a copy of the request just entered. The right margin for the report is 80 columns. The report shows the date of the request, Area of Use, name of the person entering the request, item name, backorders, quantity to be dispensed, and the maximum ward stock level.

When Pharmacy and Nursing jointly decide to use this option, some agreement must be made about its use. 1) If you choose, Nursing may enter the on-demand requests, print the report at their station, and send the paper copy to pharmacy to be filled. Using this method, you are assured that the request printed. 2) Or, Nursing may enter the on-demand requests, and at the “DEVICE:” prompt, enter a printer number for a device in the pharmacy. Someone would have to be responsible for removing the requests, picking the items, and distributing them to the proper Area of Use. The drawback with this approach is that the printer could be off-line, out of paper, etc., and Nursing would not know that Pharmacy did not get the request. 3) You may establish a scheduled time of day for someone in pharmacy to print the report for the day for all Areas of Use. He/she would then pick the requested items, and send them to the AOUs. Nursing and Pharmacy must both know what time this will take place to avoid re-ordering items that were previously requested. 4) A specific pharmacy printer for each area can be configured by a CAC or ADPAC to automatically print all Nurses' on-demand requests. This is accomplished by populating the DEFAULT WS REQUESTS PRINTER field (#32) in the INPATIENT SITE file (#59.4) with a printer from the DEVICE file (#3.5). You can still also send output to a local printer after configuring this pharmacy printer.

Again, realize that any request for a non-standard stock item will still have to come to the pharmacy via current methods.

> **NOTE:** Items dispensed through the on-demand options are counted as Ward Stock on the AMIS Report, not as Automatic Replenishment.

> **NOTE:** The "Stock Level Allowed is:" and "Stock Level:" lines in the example below appear only if the system-level parameter PSGW_WS_LVL_ON is set to ON.

Example: Enter/Edit Nurses’ On-Demand Request (80 column)

Select NURSES' MENU Option: <u>AUTO</u> Replenishment/Ward Stock Nurses' Menu

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Auto Replenishment/Ward Stock Nurses' Menu Option: <u>ENTER</u>/Edit Nurses'

On-Demand Request (80 column)

SELECT DATE/TIME FOR ON-DEMAND REQUEST: NOW // <u>N</u> (JUN 10, 1993@14:31)

Select MEDICATION AREA OF USE: <u>MED ROOM 1</u>

Select ITEM: <u>DIAZEPAM 5MG</u>/ML 2ML S.S. MR,CC,S2

Stock Level Allowed is: 20

ON-DEMAND QUANTITY: <u>8</u>

Select ITEM: <u>HEPARIN 1,000</u> UNIT/ML S.S. (10ML) MR,CC,S2

Stock Level Allowed is: 10

ON-DEMAND QUANTITY: <u>4</u>

Select ITEM: <u>GENTAMICIN</u> OPH SOLN (5ML) MR,CC,S2

Stock Level Allowed is: 8

ON-DEMAND QUANTITY: <u>3</u>

Select ITEM: <u>\<RET\></u>

Do you wish to print a copy of this on-demand request ? N// <u>YES</u>

DEVICE: *\[queue report here or send to designated device\]*

report follows

ON DEMAND REQUEST LIST BY DATE DATE: JUN 10,1993 PAGE: 1

REQUEST DATE: JUN 10,1993

BACK-

ITEM DT/TIME ORDERED QTY ORDER

------------------------------------------------------------------------------==\> AREA OF USE: MED ROOM 1

ENTERED BY: NURSE,NANCY

DIAZEPAM 5MG/ML 2ML S.S. JUN 10,1993@14:31 8 \*Std. Stock

STOCK LEVEL: 20

GENTAMICIN OPH SOLN (5ML) JUN 10,1993@14:31 3 \*Std. Stock

STOCK LEVEL: 8

HEPARIN 1,000 UNIT/ML S.S. (10ML) JUN 10,1993@14:31 4 \*Std. Stock

STOCK LEVEL: 10<span id="StdStockScreen4_end" class="anchor"></span>

2.0 List Stock Items (132 column)<span id="_Toc511400176" class="anchor"></span>; \[PSGW PRINT AOU STOCK\]

This option allows you to print the items entered as active stock for an Area of Use in the PHARMACY AOU STOCK file (#58.1). The report prints all items currently available for inventory, by AOU and will display the following information:

> 1\. Item TYPE (for the report sorted by TYPE/LOCATION/ITEM)

> 2\. Current Stock Level

> 3\. Current Reorder Level

> 4\. Current Minimum Quantity to Dispense

The report may be printed for a single AOU, several AOUs, or you may enter “^ALL” to print the report for all Areas of Use. Also, the report may be printed by two different sort order methods. You may print the stock list in order by type, and within type, by location. An alternate method is to print the stock list in alphabetical order.

Example 1: List Stock Items (132 column) By Type/Location/Item

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Auto Replenishment/Ward Stock Nurses' Menu Option: <u>LIST STOCK</u> Items (80 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

You may print by either of these sorting methods:

\(1\) By TYPE/LOCATION/ITEM

\(2\) Alphabetical by ITEM

Select SORT ORDER for report (enter 1 or 2): <u>1</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

AOU STOCK LIST BY TYPE/LOCATION - DATE: JUN 10,1993 PAGE: 1

AREA OF USE

TYPE MINIMUM QTY EXPIRATION

LOCATION ITEM STOCK LEVEL REORDER LEVEL TO DISPENSE DATE

---------------------------------------------------------------------------------------------

==\> MED ROOM 1

TYPE: EXTERNALS

MR,CA,S1 BACITRACIN OINTMENT 1OZ 3 1 2 DEC 02,1993

MR,CA,S1 CLOTRIMAZOLE 1% CREAM 4 1 2 DEC 02,1993

MR,CA,S1 HYDROCORTISONE 1% CREAM 30G 4 2 2 AUG 13,1993

MR,CA,S2 DOMOL BATH & SHOWER OIL 8 2 6 DEC 02,1993

MR,CA,S2 HEXACHLOROPHENE DET. 5OZ 6 1 6 NOT LISTED

MR,CA,S2 HYDROGEN PEROXIDE SOLN 480ML 2 1 1 NOV 05,1993

MR,CA,S2 ISOPROPYL ALCOHOL 70% 480ML 6 1 6 DEC 02,1993

MR,CD,S3 BENZOIN COMP TINCT 1 NOT LISTED NOT LISTED

NOT LISTED ACETONE 10 5 5 DEC 02,1993

TYPE: ORAL LIQUID

MR,CC,S2 ACETAMINOPHEN 500MG/15CC ELIX 2 1 1 DEC 02,1993

MR,CC,S2 CASTOR OIL 60ML U.D. 2 1 1 SEP 25,1993

MR,CC,S2 MILK OF MAGNESIA 480ML 4 2 2

MR,CC,S3 ALUM.& MAG. HYDROXIDE GEL 6 2 6 NOT LISTED

MR,CC,S3 KAOLIN AND PECTIN SUSP 360ML 2 1 1

MR,CC,S3 MAGNESIUM CITRATE SOLN 300ML 3 1 3

TYPE: ORAL SOLID

MR,B2,S1 BUSULFAN TAB 2MG 10 5 5

MR,CA,S3 CHLORAMBUCIL TAB 2MG 5 1 3 DEC 02,1993

MR,CC,S4 ACETAMINOPHEN TAB 325MG 50 10 25

MR1,S1,D2 DIGOXIN TAB 0.125MG 2 NOT LISTED NOT LISTED

TYPE: INJECTION

MR,CC,S1 DEXTROSE 50% 50ML SYRINGE 5 1 4

MR,CC,S1 DIAZEPAM 5MG/ML 2ML AMP 10 2 6 SEP 10,1993

MR,CC,S1 GLUCAGON INJ 1MG 3 1 2 DEC 02,1993

MR,CC,S1 LIDOCAINE 1% INJ 30ML 3 2 1

TYPE: OPHTHALMIC, OTIC

MR,CA,S4 TIMOLOL 0.25% OP.SOL. 10ML 3 1 2 NOT LISTED

TYPE: SUPPOSITORY

MR,REF,S2 ACETAMINOPHEN SUPP 650MG 12 1 6 NOT LISTED

MR,REF,S2 ASPIRIN SUPP 650MG 12 1 6 NOT LISTED

MR,REF,S2 GLYCERIN SUPPOSITORIES 12'S 2 1 1

TYPE: CONTROLLED DRUG (II)

MR,CC,S1 DIAZEPAM 5MG/ML 2ML AMP 10 4 6 SEP 10,1993

TYPE: REAGENT/TEST ITEM

MR,CB,S1 KETO-DIASTIX 100'S 2 1 1

Example 2: List Stock Items (132 column) Alphabetical by Item

Select INPATIENT PHARMACY MENU Option: <u>AUTOM</u>atic Replenishment

Enter AR/WS Inpatient Site Name: <u>GEN</u>eral Hospital

Select Auto Replenishment/Ward Stock Nurses' Menu Option: <u>LIST STOCK</u> Items (80 column)

You may select a single AOU, several AOUs,

or enter "^ALL" to select all AOUs.

-OR-

You may select an Inventory Group.

Do you want to select AOU(s) or an Inventory Group? (Enter 'A' or 'I')=\> <u>A</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>MED ROOM 1</u>

Select PHARMACY AOU STOCK AREA OF USE (AOU): <u>\<RET\></u>

You may print by either of these sorting methods:

\(1\) By TYPE/LOCATION/ITEM

\(2\) Alphabetical by ITEM

Select SORT ORDER for report (enter 1 or 2): <u>2</u>

The right margin for this report is 80.

You may queue the report to print at a later time.

DEVICE: *\[queue report here or send to designated device\]*

report follows

ALPHABETICAL LISTING OF AOU STOCK - DATE: AUG 10,1993 PAGE: 1

AREA OF USE

TYPE MINIMUM QTY EXPIRATION

ITEM LOCATION STOCK LEVEL REORDER LEVEL TO DISPENSE DATE

---------------------------------------------------------------------------------------------------------------------

==\> MED ROOM 1

ACETAMINOPHEN 500MG/15CC ELIX. MR,CC,S2 2 1 1 DEC 02,1993

ACETAMINOPHEN SUPP 650MG MR,REF,S2 12 1 6 DNOT LISTED

ACETAMINOPHEN TAB 325MG MR,CC,S4 50 10 25 DEC 02,1993

ACETONE NOT LISTED 10 5 5 DEC 02,1993

ALUM.& MAG. HYDROXIDE GEL MR,CC,S3 6 2 6 DEC 02,1993

ASPIRIN SUPP 650MG MR,REF,S2 12 1 6 NOT LISTED

ATROPINE SULFATE INJ 0.4MG/ML,20ML MR,CC,S1 3 2 1

BACITRACIN OINTMENT 1OZ MR,CA,S1 3 1 2 DEC 02,1993

BECLOMETHASONE ORAL.INHALER 16.8GM MR,CC,S5 6 1 5

BENZOIN COMP TINC MR,CD,S3 1 NOT LISTED NOT LISTED

BLEOMYCIN INJ 15 UNIT NOT LISTED 3 1 2

BUSULFAN TAB 2M MR,B2,S1 10 5 5

CASTOR OIL 60ML U.D. MR,CC,S2 2 1 1 SEP 25,1993

CHLORAMBUCIL TAB 2MG MR,CA,S3 5 1 3 DEC 02,1993

CLOTRIMAZOLE 1% CREAM MR,CA,S1 4 1 2 DEC 02,1993

DEXTROSE 50% 50ML SYRINGE MR,CC,S1 5 1 4

DIAZEPAM 5MG/ML 2ML AMP MR,CC,S1 10 2 6 SEP 10,1993

DIGOXIN TAB 0.125MG MR1,S1,D2 2 NOT LISTED NOT LISTED

DISULFIRAM TAB 250MG MR,C1,C2 2 1 1 DEC 02,1993

DOMOL BATH & SHOWER OIL MR,CA,S2 8 2 6

EPINEPHRINE INJ 1:1000 1ML (AMPUL) MR,CC,S1 3 1 2

GLUCAGON INJ 1MG MR,CC,S1 3 1 2

GLYCERIN SUPPOSITORIES 12'S MR,REF,S2 2 1 1

HEPARIN 1,000 UNIT/ML 10ML INJ MR,CC,S1 12 6 6

HEXACHLOROPHENE DET. 5OZ MR,CA,S2 6 1 6 NOT LISTED

HYDROCORTISONE 1% CREAM 30GM MR,CA,S1 4 2 2 AUG 13,1993

HYDROGEN PEROXIDE SOLN 480ML MR,CA,S2 2 1 1 NOV 05,1993

•

•

•

*\[This report has been abbreviated to save space.\]*3.0 Ward/AOU List for an Item (80 column) <span id="_Toc511400177" class="anchor"></span>; \[PSGW LOOKUP ITEM\]

This option is used primarily to locate the wards and Areas of Use that stock a selected item. After you enter the name of the item, the report prints out the name of the ward, Area of Use, location, and stock level of the item within the AOU. If an Area of Use stocks the item, but the AOU is not associated with a ward, e.g., cardiac cath lab, then these Areas will be printed at the top of the report. Afterward, those AOUs which have associated wards will be printed.

Example: Ward/AOU List for an Item (80 column)

Select NURSES' MENU Option: <u>AUTO</u> Replenishment/Ward Stock Nurses' Menu

Enter AR/WS Inpatient Site Name: <u>GEN</u>ERAL HOSPITAL

Select Auto Replenishment/Ward Stock Nurses' Menu Option: <u>WARD</u>/AOU List for an Item (80 column)

Using this option, you may look up the wards and/or Areas of Use

which stock the item you select.

The right margin for this report is 80.

You may queue the report to print at a later time.

Select ITEM Name: <u>HEPARIN 1,000</u> UNIT/ML S.S. (10ML)

DEVICE: *\[queue report here or send to designated device\]*

report follows

WARD/AOU LIST FOR AN ITEM DATE: MAY 26,1993

ITEM NAME

STOCK

WARD AREA OF USE LOCATION LEVEL

------------------------------------------------------------------------------

==\> HEPARIN 1,000 UNIT/ML S.S. (10ML)

1 NORTH MED ROOM 1 MR,CC,S2 10

1 WEST MED ROOM 1 MR,CC,S2 10

2 NORTH MED ROOM 3 MR,CC,S2 10

2 SOUTH MED ROOM 3 MR,CC,S2 10

2 WEST MED ROOM 3 MR,CC,S2 10

# # Appendices


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Appendices](#appendices)
- [# AppendicesAppendix A. How To Work With The System<span id="Toc511400179" class="anchor"></span>](#appendicesappendix-a-how-to-work-with-the-systemspan-idtoc511400179-classanchorspan)
- [# Glossary](#glossary)
- [Index](#index)

# # AppendicesAppendix A. How To Work With The System<span id="_Toc511400179" class="anchor"></span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

I. IntroductionIs this appendix for you?

If you’re just learning to use DHCP software, this appendix will introduce you to a small but important part of the DHCP world—signing on, entering data, and getting out. You do not have to be a computer expert to use DHCP software. You do not have to know a lot of technical terms. You do have to follow instructions. And, in general, you need to be curious, flexible, and patient. This appendix will help you get started. If you are an experienced DHCP user, this appendix can serve as a reminder.

Other Resources

If you are not familiar with DHCP software applications, we recommend that you study the DHCP *Users Guide to Computing*. This orientation guide is a comprehensive handbook benefiting first time users of any DHCP application. The purpose of the introductory material is to help you become familiar with basic computer terms and the components of a computer. It is reproduced and distributed periodically by the Kernel Development Group. To request a copy, contact your local Information Resource Management (IRM) staff.

How Does DHCP Work?

The Decentralized Hospital Computer Programs (DHCP) use the computer in an interactive fashion. An interactive system involves a conversation with the computer. The computer asks you to supply information and immediately processes it. You will be interacting with the software by responding to prompts (the questions) in the program. Your responses are recognized by the computer when you complete the interaction by pressing the return or enter key.

DHCP software is “menu driven.” A menu is a screen display which lists all of the choices (options) available. You will see only the menus, options, and functions which you have security clearance to use. Once you have made a selection, the software may branch to another menu (submenu) or you may be asked to answer questions which allow the computer to perform tasks.

II. How to Sign On

The procedure for establishing a link to the terminal involves access and verify codes. These codes are assigned by your supervisor. For security reasons, the access code and verify code are not displayed on the terminal screen when you type them in. Please do not write your code down or reveal it to others. The sign-on banner shows the date and time when you last signed on. The banner also shows if the account had any unsuccessful attempts at log-on. You will be required to change your verify code every 90 days.

Press the return key on the keyboard. A blinking cursor will appear on the terminal. You will then see:

ACCESS CODE: *\[Enter your assigned access code.\]*

VERIFY CODE: *\[Enter your assigned verify code.\]*III. How to Stop

In most cases, when you begin an option you will continue through it to a normal ending. At times however, you may wish to exit the option to do something else. To stop what you are doing, enter an up-arrow (^). You may use the up-arrow at any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering the up-arrow to completely exit the system.

IV. How to Enter Data

Each message you type in must be followed by pressing the return key (or enter key on some keyboards) to indicate you have completed that entry. In many cases, you need only enter the first few letters (called shortcut synonyms) of an option or field, and the computer fills in the rest. Shortcut synonyms help increase speed and accuracy.

If you want to bypass a prompt, press the return or enter key and the computer will go on to the next question. You will be allowed to bypass a question only if the information is not required to continue with the option.

Some typists use the lower case “L” for the number “1” and the letter “O” for zero. Please keep in mind that with this software the number “1” and the letter “l” are not interchangeable. Also the number “0” and the letter “O” are not interchangeable.

V . How to Get Help

If you need assistance while interacting with the software, enter a question mark or two to receive on-line help.

? Entering a single question mark at a prompt will provide a brief help message.

?? Two question marks entered at a prompt will provide a more extensive description and/or a list of choices appropriate to the prompt.

VI. Responding to Prompts

When the computer prompts you with a question, typically a colon (:) will follow. Several types of prompts may be used including yes/no, select, and default. Prompts can be a field in a file, like the basic prompt shown below:

DATE OF BIRTH: This type of prompt is waiting for you to enter a value, like March 3, 1960. Don’t forget to complete your interaction by pressing the return or enter key.

<u>Select Prompt</u>

If the answer to the prompt is a choice of several alternatives, the question may appear prefixed with the word “Select”, as below:

Select PATIENT NAME:

<u>Yes/No Prompt</u>

If the question requires either a Yes or No response (in which case simply Y or N, upper or lower case, is acceptable), the question may be followed by a question mark rather than a colon.

ARE YOU SURE?

Sometimes, the test of the question will include, within parentheses, the different allowable responses that you can make to that question:

ARE YOU SURE (Y/N)?

<u>Default Prompt</u>

Sometimes the question the computer is asking you has a standard expected answer. This is known as the default response. In order to save you the trouble of typing the most probable answer, the computer provides the answer followed with a double slash (//). You either enter nothing (also known as a null response) by pressing the return key to indicate acceptance of the default response as your answer, or you can type a different response:

IS IT OKAY TO DELETE? NO//

  
VII. Invalid Response

The computer software checks each answer immediately after it is entered. Whenever the computer determines that an answer is invalid for any reason, it beeps, displays two spaces and two questions marks, and repeats the question on a new line.

VIII. LAYGO

DHCP software checks your answers against an internally stored table of valid answers. If your answer is not stored in this table but the Learn-As-You-Go (LAYGO) mode is allowed, the computer adds your response as one of those valid answers. If LAYGO mode is allowed then an example dialogue goes something like this:

ARE YOU ADDING A NEW CLINIC? If you respond with a Y (or YES), the software adds the new clinic in its validation table and accepts the answer. If anything other than Yes is entered, the original answer will be invalidated and the question will be repeated.

IX. How to Enter Dates and Times

When the acceptable answer to a question is a date, use the following answer formats. Note that the response is not case sensitive, upper or lower case input is acceptable:

> JULY 20, 1969

> 7/20/69

> 20 JUL 69

> 10jul69

> 10 jul 69

> 072069

> TODAY or Today or T or t (today)

> TODAY+1 or T+1 or t+1 (tomorrow)

> TODAY-7 or T-7 or t-7 (one week ago)

> TODAY+3W or T+3W or t+3w (3 weeks hence)

> NOW+1H (present time plus one hour)

> NOW+4M (present time plus four months)

> NOON (12:00 p.m.)

> MID (12:00 a.m.)

The year portion of the date can be left off; normally the system will assume current year.

Occasionally, the software will allow you to enter a time-of-day in connection with a date, for example, 4:00 p.m. on July 20, 1969. To do this, type the date in one of the above forms followed by an at sign (@), followed by the time. For example, you might enter:

20 JUL 69@4PM

In this mode, you can enter time either as military (four digit) time, hour AM/PM, or hour:minute:second AM/PM, or simply NOW (or Now or now) for the current date/time.

The colon (:) can be omitted and AM/PM can also be omitted if the time being entered is between 6 a.m. and 6 p.m. Thus, today at 3:30 p.m. may be entered as:

T@330

Use MID as a response to mean 12:00 a.m. (midnight) and NOON as a response to mean 12:00 p.m. for time associated with dates:

T+3W@MID

X. Making Corrections

When you want to delete an answer previously entered, without substituting any other answer, enter an at sign (@) as a response to that prompt. This leaves the answer blank.

DATE OF BIRTH: May 21, 1946//@ In this example, the date on file has been erased and now there is no answer to the DATE OF BIRTH prompt; it is null.

The system will ask you to confirm that you really intend to delete the information. You may not be able to delete a response if the information is required:

ARE YOU SURE? This question is a safety feature, giving you a chance to change your mind now, without reediting later.

XI. Spacebar Recall Feature

When using this software, you may want to answer a prompt with a code meaning *the same as before*. The computer is capable of remembering what your last response(s) were the last time you signed on. This feature is called spacebar recall and employs the spacebar and return keys.

You generally can repeat information you entered the first time by entering a space and pressing the return or enter key. For example, you may wish to do a series of procedures for one patient. Each time (after the first) you are asked for the patient name, you may enter a space and press the return key and the computer will enter the same patient.

XII. Printing Reports

Frequently, when you have finished some data entry you will be asked if you wish to print the record, file, or report. You may display the report on your terminal screen or produce a paper copy. You will be prompted to enter a device number of the printer you want to use. If you do not know the device number of the printer, you may type in a question mark for a list of printers. In some cases the device you will use has already been decided for you and you will not be asked where you want to print. If you need assistance in determining the device number, ask your application coordinator or site manager.

<u>Right Margin</u>

Sometimes you will be asked to specify the right margin of the report. You will not be asked this in all cases as the information may be preset for the device you specify and a default answer provided. Nevertheless, your choices are simple. Generally, “80” is used for standard size paper and displaying on the terminal screen; “132” is used for larger paper.

DEVICE: Right Margin: 80//

<u>Display the Report on the Terminal Screen</u>

Display is the word used to indicate the data is printed to a terminal screen rather than on paper. At the DEVICE prompt, if you want to view a report on your screen, press the return key. Normally, if you do not specify a device number, the information will print on your screen. After the screen fills with the first page of the report, you will be prompted to press the return key to continue with the next screen of data. The process is repeated at the bottom of every screen. You may exit the option at any time by entering an up-arrow (^).

Press \<RET\> to continue, or '^' to quit

<u>Queue Report to a Printer</u>

If you want to queue your output to run in the background, type the letter “Q” at the DEVICE prompt. Next, you will be prompted to enter a device number of the printer you want to use. Finally, enter the date and time you would like the report to print.

DEVICE: Enter the letter “Q” to queue the print job.

DEVICE: Enter the device name or number.

Requested Start Time: NOW// Press the return key or enter a time here using the date and time formats discussed above (e.g., NOW+1 for one hour from now).

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc511400180" class="anchor"></span>

> AMIS Category The AMIS category will classify AR/WS drugs for AMIS purposes. The 4 AMIS categories are “0”, “1”, “2”, and “3”. “0” means the drug is classified as field 03 or 04. This includes tablets, capsules, multi-dose vials, etc. It does not include multiple- dose externals, liquids, or antacids. “1” means the drug is classified as field 06 or 07. This includes multiple-dose externals, liquids, antacids, otics, ophthalmics, and inhalations. “2” means the drug is classified as field 17. This includes solutions and administration sets. “3” means the drug is classified as field 22. This includes blood and blood products.

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

> (Location Code) item in the AOU. For example, if isopropyl alcohol is stored in an AOU on the second set of shelves, third shelf from the top, its item address code could be expressed as S,2,3. The address code can consist of up to 3 levels separated by a comma. Each level should further define the exact location. The code is associated with an expansion for clarity.

> Item Address Code Text used to clarify the meaning of an item

> Expansion address code. For example, on the inventory sheet and pick list, the code S would be expanded and printed as shelf. (These codes and expansions are locally created terms.)

> Minimum Quantity The least amount of an item to be

> to Dispense dispensed. If defined for an item it will be used by a site as a guideline for dispensing items that are best dispensed in bulk quantities.

> On Demand Request Non-scheduled distribution of an item to an AOU.

> PSGW PARAM The PSGW PARAM key should be given ONLY to the Inpatient Pharmacy Package Coordinator. This lock controls when the collection of AMIS data begins.

> PSGW PURGE The PSGW PURGE key should be given *only* to the Inpatient Pharmacy Package Coordinator or his/her designee. This lock controls the deletion of data from the AR/WS files and should be assigned with discretion.

> PSGW TRAN The PSGW TRAN key should be given *only* to the Inpatient Pharmacy Package Coordinator or his/her designee. The key controls access to the *Transfer AOU StockEntries* option. Using the transfer option, users may “copy” the stock entries from one Area of Use into other Areas.

> PSGW RN Primary menu option for the Automatic Replenishment/Ward Stock Nurses’ Menu. This menu allows nursing to enter on demand requests, list stock items, and locate AOUs which stock a specified item.

> PSGWMGR The name of the key that must be assigned to Inpatient Pharmacy Package Coordinators using the AR/WS package. This key allows access to the *Supervisor’sMenu* options. Also, the name of the primary menu option to be assigned to all pharmacy personnel using the AR/WS package.

> Pick List Used to dispense the inventory. This is a two part report. The first part prints in same format as the inventory sheet. It shows: item location, item name, stock level, on-hand amount, total backorders, the amount to be dispensed, and a column to enter the amount dispensed if it is less than the number in the “to be dispensed” column. The second part of the pick list is used by the pharmacy to pick the items. It contains item name, quantity to be dispensed, and a column to record actual quantity dispensed.

> Quick Code An abbreviated form of the drug generic name (from 1 to 10 characters). Lookup is done on print name, QUICK CODE, or synonym. Quick codes are displayed on the Inventory Sheet.

> Reorder Level If defined for an item, this is the stock level an item should reach before it can be replenished.

> Service Service is located under Ward (For Percentage) in the PHARMACY AOU STOCK file. It is the name of the service which composes the ward. For example, cardiology and neurology are services.

> Service Percentage The percentage of ward use by a particular service. For example, 40 beds used by Cardiology out of 100 would be 40%.

> Stock Item An item (from the DRUG file) stored in the AOU.

> Stock Level The quantity of an item stocked in a specific AOU.

> Ward (for item) The name of the ward or wards that will use this particular item. It is important to accurately answer this prompt because this is the link between the AR/WS package and the Unit Dose package. The Unit Dose package looks at this field to know if the drug is a Ward Stock item.

> Ward/Location The name of the MAS location that is served

> (for percentage) partially or totally by an Area of Use. This field will generally be used for reporting purposes. If the AOU is *not* composed of any wards, enter “^” \<RET\> at the “Ward/Location (for percentage)” prompt.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Index<span id="_Toc511400181" class="anchor"></span>
A
Add/Delete Ward (for Item) 32
Addition of a Ward (for Item) assignment 32
AMIS Data Enter/Edit (Single Drug) 70
AMIS Data Purge 104
AOU Backorder Report 144
AOU Backorder Report (80 column) 144
AOU Inventory Group-Enter/Edit 39
AOU with associated clinics 20
AOU with associated wards 19
AOU with NO associated wards 21
AR/WS AMIS Report 77
Auto Replenishment Reports 157
Auto Replenishment/Ward Stock Nurses’ Menu 185
B
Backorder Requests 140
C
Cost Report Per AOU 86
Crash Cart Menu 154
Create the Area of Use 17
Current (ALL) Backorder Report (80 column) 146
D
Data for AMIS Stats - Print 68
Delete an On-Demand Request 137
Delete Inventory Date/Time 122
Deletion of a Ward (for Item) assignment 34
Duplicate Entry Report 96
E
Edit ‘Person Doing Inventory’ 55
Enter AMIS Data for All Drugs/All AOUs 66
Enter Backorders 141
Enter/Edit Crash Cart Locations 155
Enter/Edit Inventory Types 12
Enter/Edit Nurses’ On-Demand Request (80 column) 186
Enter/Edit On-Demand Request 134
Enter/Edit Quantity Dispensed 130
Expiration Date - Enter/Edit 29
Expiration Date Report (80 column) 162
F
Fill Requests for Backorder Items 143
G
Glossary 205
H
High Cost Report 91
High Volume Report 94
How This Manual Is Organized 1
I
Identify AOU INPATIENT SITE 73
Identify AOU Returns & AMIS Count 71
Inactivate AOU 37
Inactivate AOU Stock Item 38
Incomplete AMIS Data 80
Input AOU Inventory 123
Inventory Group List 53
Inventory Outline (80 column) 167
Inventory Sheet Print 116
Item Activity Inquiry (80 column) 170
Item Address Code/Expansion 16
Item Location Codes - Enter/Edit 14
L
List Location Codes 45
List Stock Items 49
List Stock Items (132 column) 158, 188
M
Management Reports 76
Menu Outline 3
Multiple Items Report 151
Multiple Items Report (80 column) 151
N
Non-Pharmacy Items in AR/WS 26
Nurses’ Menu 6
O
Obsolete Data Purge 103
On-Demand Requests 133
P
Package Functional Description 1
Package Management/Legal Requirements 2
Percentage Stock On Hand (132 column) 172
PHARMACY AOU STOCK File Worksheet 27, 28
Pick List 126
Prepare AMIS Data 62
Print AMIS Report 82
Print AMIS Worksheet 63
Print an On-Demand Report by Date/AOU 138
Print AR/WS Stock Item Data 47
Print Crash Cart Locations 156
Print Inventory Types 44
Print Set Up Lists 43
Production Menu 5, 115
Prototype AOU Inventory Group 42
PSGW PURGE INVENTORY 107
PSGW RE-INDEX AMIS 108
PSGW UPDATE AMIS STATS 110
Purge Dispensing Data 105
R
Recalculate AMIS 84
Return Items for AOU 153
Returns Analysis Report (80 column) 174
S
Set Up AR/WS (Build Files) 10
Show AOU Status for AMIS 75
Show AOU/Ward/Service 46
Single AOU Inventory Print 120
Single Item Cost Report 90
Single Item Report (80 column) 150
Site Parameters 58
Sort AOUs in Group 56
Special Instructions for the “First-Time” Computer User 1
Special Notations 2
Standard Cost Report (132 column) 99
Standard Cost Report for an AOU 101
Standard Cost Report for an Inventory Group 99
Stock Items - Enter/Edit 24
Supervisor’s Menu 3, 9
T
Transfer AOU Stock Entries 35
U
Usage Report for an Item (80 column) 176
W
Ward (For Item) Conversion 30
Ward/AOU List for an Item (80 column) 169, 191
Worksheet for Creating the Area of Use 23
Z
Zero Usage Report (80 column) 180
